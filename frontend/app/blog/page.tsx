import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";
import { getAllPosts } from "./_lib";

export const metadata: Metadata = {
  title: "Network Insights & Engineering Blog | SeekAPI.ai",
  description:
    "Engineering notes on API cost optimization, DeepSeek routing, and production integration patterns.",
  keywords: ["SeekAPI blog", "API engineering", "DeepSeek", "network insights"],
};

export default function BlogPage() {
  const posts = getAllPosts();

  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">BLOG</p>
          <h1 className="hero-title">Network Insights &amp; Engineering Blog</h1>
          <p className="hero-subtitle">
            Technical notes for builders operating cost-efficient, OpenAI-compatible inference at
            scale. Posts load from <code>frontend/content/*.md</code> (bundled with the Vercel
            deployment).
          </p>
          <section className="card-grid" aria-label="Blog posts">
            {posts.length === 0 ? (
              <article className="card">
                <h2 className="card-title">No posts yet</h2>
                <p className="card-body">
                  Add markdown files under <code>frontend/content/</code>. Each <code>*.md</code>{" "}
                  file becomes a blog article automatically.
                </p>
              </article>
            ) : null}
            {posts.map((post) => (
              <article className="card" key={post.slug}>
                <h2 className="card-title">{post.title}</h2>
                <p className="card-body">{post.description}</p>
                <p className="card-body">
                  <strong>{post.lang.toUpperCase()}</strong> · {post.date || "No date"}
                </p>
                <a className="button-ghost" href={`/blog/${post.slug}`}>
                  Read Article
                </a>
              </article>
            ))}
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
