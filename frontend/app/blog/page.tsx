import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";
import { getAllPosts } from "./_lib";

export const metadata: Metadata = {
  title: "Network Insights Blog | SeekAPI.ai",
  description:
    "Engineering articles on API cost optimization, latency routing, and DeepSeek operations.",
  keywords: ["SeekAPI blog", "AI API optimization", "DeepSeek guides", "network insights"],
};

export default function BlogPage() {
  const posts = getAllPosts();

  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">BLOG</p>
          <h1 className="hero-title">SEO Traffic Pool</h1>
          <p className="hero-subtitle">
            Technical growth content for builders, operators, and AI product teams running on
            cost-efficient inference.
          </p>
          <section className="card-grid" aria-label="Blog posts">
            {posts.length === 0 ? (
              <article className="card">
                <h2 className="card-title">No posts yet</h2>
                <p className="card-body">
                  Drop markdown files into root <code>/blog</code> and this page will auto-render
                  them.
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
