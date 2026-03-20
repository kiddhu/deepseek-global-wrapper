import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export default function BlogPage() {
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
          <section className="card-grid" aria-label="Featured topics">
            <article className="card">
              <h2 className="card-title">DeepSeek R1 Cost Benchmarks</h2>
              <p className="card-body">
                Real production numbers for latency, quality, and budget trade-offs at scale.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Migration Guides</h2>
              <p className="card-body">
                Switch from OpenAI in under 30 seconds with minimal risk and no SDK rewrite.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Global Traffic Routing</h2>
              <p className="card-body">
                Architecture notes on throughput, failover, and billing-aware request strategies.
              </p>
            </article>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
