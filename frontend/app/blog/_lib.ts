import fs from "node:fs";
import path from "node:path";

export type BlogPost = {
  slug: string;
  title: string;
  date: string;
  lang: string;
  description: string;
  content: string;
  source?: "local" | "supabase";
};

const BLOG_DIR = path.join(process.cwd(), "content");

type RawRow = {
  slug?: string;
  title?: string;
  body_md?: string;
  content?: string;
  description?: string | null;
  lang?: string | null;
  published_at?: string | null;
};

function safeReadBlogFiles(): string[] {
  if (!fs.existsSync(BLOG_DIR)) {
    return [];
  }
  return fs.readdirSync(BLOG_DIR).filter((name) => name.endsWith(".md"));
}

function parseFrontmatter(raw: string): { meta: Record<string, string>; body: string } {
  if (!raw.startsWith("---")) {
    return { meta: {}, body: raw };
  }
  const end = raw.indexOf("\n---", 3);
  if (end === -1) {
    return { meta: {}, body: raw };
  }
  const frontmatter = raw.slice(3, end).trim();
  const body = raw.slice(end + 4).trim();
  const meta: Record<string, string> = {};
  for (const line of frontmatter.split("\n")) {
    const idx = line.indexOf(":");
    if (idx === -1) {
      continue;
    }
    const key = line.slice(0, idx).trim();
    const value = line
      .slice(idx + 1)
      .trim()
      .replace(/^"|"$/g, "");
    meta[key] = value;
  }
  return { meta, body };
}

export function markdownToHtml(markdown: string): string {
  const blocks = markdown.split("\n\n");
  return blocks
    .map((block) => {
      const b = block.trim();
      if (!b) {
        return "";
      }
      if (b.startsWith("```")) {
        const code = b.replace(/^```[a-zA-Z]*\n?/, "").replace(/```$/, "");
        return `<pre><code>${escapeHtml(code)}</code></pre>`;
      }
      if (b.startsWith("### ")) {
        return `<h3>${escapeHtml(b.slice(4))}</h3>`;
      }
      if (b.startsWith("## ")) {
        return `<h2>${escapeHtml(b.slice(3))}</h2>`;
      }
      if (b.startsWith("# ")) {
        return `<h1>${escapeHtml(b.slice(2))}</h1>`;
      }
      if (b.startsWith("- ")) {
        const items = b
          .split("\n")
          .filter((line) => line.startsWith("- "))
          .map((line) => `<li>${escapeHtml(line.slice(2))}</li>`)
          .join("");
        return `<ul>${items}</ul>`;
      }
      return `<p>${escapeHtml(b).replace(/\n/g, "<br />")}</p>`;
    })
    .join("\n");
}

function escapeHtml(value: string): string {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/** Markdown files under frontend/content — sync, safe for generateStaticParams at build time */
export function getAllLocalPosts(): BlogPost[] {
  const files = safeReadBlogFiles();
  return files
    .map((file) => {
      const fullPath = path.join(BLOG_DIR, file);
      const raw = fs.readFileSync(fullPath, "utf-8");
      const { meta, body } = parseFrontmatter(raw);
      const slug = file.replace(/\.md$/, "");
      return {
        slug,
        title: meta.title || slug,
        date: meta.date || "",
        lang: meta.lang || "en",
        description:
          (meta.description && meta.description.trim()) || body.slice(0, 180).replace(/\n/g, " "),
        content: body,
        source: "local" as const,
      };
    })
    .toSorted((a, b) => (a.date < b.date ? 1 : -1));
}

export function getLocalPostBySlug(slug: string): BlogPost | null {
  const safeSlug = slug.replace(/[^a-zA-Z0-9._-]/g, "");
  const fullPath = path.join(BLOG_DIR, `${safeSlug}.md`);
  if (!fs.existsSync(fullPath)) {
    return null;
  }
  const raw = fs.readFileSync(fullPath, "utf-8");
  const { meta, body } = parseFrontmatter(raw);
  return {
    slug: safeSlug,
    title: meta.title || safeSlug,
    date: meta.date || "",
    lang: meta.lang || "en",
    description:
      (meta.description && meta.description.trim()) || body.slice(0, 180).replace(/\n/g, " "),
    content: body,
    source: "local",
  };
}

function supabaseConfigured(): boolean {
  const base = process.env.SUPABASE_URL?.trim();
  const key =
    process.env.SUPABASE_SERVICE_ROLE_KEY?.trim() || process.env.SUPABASE_ANON_KEY?.trim();
  return Boolean(base && key);
}

function rowToPost(row: RawRow): BlogPost | null {
  if (!row.slug) {
    return null;
  }
  const body = (row.body_md ?? row.content ?? "").trim();
  const description =
    (typeof row.description === "string" && row.description.trim()) ||
    body.slice(0, 180).replace(/\n/g, " ");
  return {
    slug: String(row.slug),
    title: String(row.title || row.slug),
    date: row.published_at ? String(row.published_at) : "",
    lang: row.lang ? String(row.lang) : "en",
    description,
    content: body,
    source: "supabase",
  };
}

/** Fetch published rows from Supabase PostgREST (table default: blog_posts). */
async function fetchSupabasePosts(): Promise<BlogPost[]> {
  if (!supabaseConfigured()) {
    return [];
  }
  const baseUrl = process.env.SUPABASE_URL!.replace(/\/$/, "");
  const key =
    process.env.SUPABASE_SERVICE_ROLE_KEY?.trim() || process.env.SUPABASE_ANON_KEY!.trim();
  const table = process.env.SUPABASE_BLOG_TABLE?.trim() || "blog_posts";
  const url = `${baseUrl}/rest/v1/${table}?select=slug,title,body_md,content,description,lang,published_at&order=published_at.desc`;
  try {
    const res = await fetch(url, {
      headers: {
        apikey: key,
        Authorization: `Bearer ${key}`,
        Accept: "application/json",
      },
      next: { revalidate: 120 },
    });
    if (!res.ok) {
      return [];
    }
    const rows = (await res.json()) as RawRow[];
    if (!Array.isArray(rows)) {
      return [];
    }
    return rows.map(rowToPost).filter((p): p is BlogPost => p !== null);
  } catch {
    return [];
  }
}

async function fetchSupabasePostBySlug(slug: string): Promise<BlogPost | null> {
  if (!supabaseConfigured()) {
    return null;
  }
  const safe = slug.replace(/[^a-zA-Z0-9._-]/g, "");
  if (!safe) {
    return null;
  }
  const baseUrl = process.env.SUPABASE_URL!.replace(/\/$/, "");
  const key =
    process.env.SUPABASE_SERVICE_ROLE_KEY?.trim() || process.env.SUPABASE_ANON_KEY!.trim();
  const table = process.env.SUPABASE_BLOG_TABLE?.trim() || "blog_posts";
  const filter = encodeURIComponent(`slug.eq.${safe}`);
  const url = `${baseUrl}/rest/v1/${table}?select=slug,title,body_md,content,description,lang,published_at&${filter}`;
  try {
    const res = await fetch(url, {
      headers: {
        apikey: key,
        Authorization: `Bearer ${key}`,
        Accept: "application/json",
      },
      next: { revalidate: 120 },
    });
    if (!res.ok) {
      return null;
    }
    const rows = (await res.json()) as RawRow[];
    if (!Array.isArray(rows) || rows.length === 0) {
      return null;
    }
    return rowToPost(rows[0]);
  } catch {
    return null;
  }
}

function mergePosts(local: BlogPost[], remote: BlogPost[]): BlogPost[] {
  const map = new Map<string, BlogPost>();
  for (const p of local) {
    map.set(p.slug, p);
  }
  for (const p of remote) {
    map.set(p.slug, p);
  }
  return [...map.values()].toSorted((a, b) => (a.date < b.date ? 1 : -1));
}

/** All posts: frontend/content/*.md plus Supabase table when SUPABASE_URL + key are set (remote wins on slug collision). */
export async function getAllPosts(): Promise<BlogPost[]> {
  const local = getAllLocalPosts();
  const remote = await fetchSupabasePosts();
  return mergePosts(local, remote);
}

export async function getPostBySlug(slug: string): Promise<BlogPost | null> {
  // Same precedence as mergePosts: Supabase row overrides local file when slug matches.
  const remote = await fetchSupabasePostBySlug(slug);
  if (remote) {
    return remote;
  }
  return getLocalPostBySlug(slug);
}
