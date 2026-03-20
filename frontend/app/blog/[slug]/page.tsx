import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { SiteFooter } from "../../components/site-footer";
import { SiteHeader } from "../../components/site-header";
import { getAllPosts, getPostBySlug, markdownToHtml } from "../_lib";

type Params = { slug: string };

export function generateStaticParams() {
  return getAllPosts().map((post) => ({ slug: post.slug }));
}

export function generateMetadata({ params }: { params: Params }): Metadata {
  const post = getPostBySlug(params.slug);
  if (!post) {
    return { title: "Article Not Found" };
  }
  return {
    title: `${post.title} | SeekAPI Blog`,
    description: post.description,
  };
}

export default function BlogArticlePage({ params }: { params: Params }) {
  const post = getPostBySlug(params.slug);
  if (!post) {
    notFound();
  }

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    headline: post.title,
    inLanguage: post.lang,
    datePublished: post.date || undefined,
    author: {
      "@type": "Organization",
      name: "SeekAPI.ai",
    },
    publisher: {
      "@type": "Organization",
      name: "SeekAPI.ai",
    },
    mainEntityOfPage: `https://seekapi.ai/blog/${post.slug}`,
    description: post.description,
  };

  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container article-shell">
          <p className="hero-eyebrow">NETWORK INSIGHTS</p>
          <h1 className="hero-title">{post.title}</h1>
          <p className="hero-subtitle">
            {post.lang.toUpperCase()} · {post.date || "Undated"}
          </p>
          <article
            className="card article-card"
            dangerouslySetInnerHTML={{ __html: markdownToHtml(post.content) }}
          />
        </div>
      </main>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <SiteFooter />
    </div>
  );
}
