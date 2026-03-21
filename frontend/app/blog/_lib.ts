import fs from "node:fs";
import path from "node:path";

export type BlogPost = {
  slug: string;
  title: string;
  date: string;
  lang: string;
  description: string;
  content: string;
};

const BLOG_DIR = path.resolve(process.cwd(), "..", "blog");

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

export function getAllPosts(): BlogPost[] {
  const files = safeReadBlogFiles();
  const posts = files
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
      };
    })
    .toSorted((a, b) => (a.date < b.date ? 1 : -1));
  return posts;
}

export function getPostBySlug(slug: string): BlogPost | null {
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
  };
}
