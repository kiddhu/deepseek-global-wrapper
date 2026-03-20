export default function HomePage() {
  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <section>
            <p className="hero-eyebrow">SEEKAPI.AI · DEEPSEEK GATEWAY</p>
            <h1 className="hero-title">DeepSeek R1, Globally Accessible..</h1>
            <p className="hero-subtitle">
              Cost-effective access to DeepSeek reasoning models (R1) and DeepSeek
              V3 via an OpenAI-compatible interface. Designed for global usage with
              minimal integration friction.
            </p>

            <div className="hero-badges">
              <span className="badge">Cost-effective R1/V3</span>
              <span className="badge">OpenAI-compatible gateway</span>
              <span className="badge">Global deployment pipeline</span>
            </div>

            <div className="hero-actions">
              <a href="/docs" className="button-primary">
                Get Started
              </a>
              <a href="/blog" className="button-ghost">
                AION Insights
              </a>
            </div>
          </section>

          <section className="card-grid" aria-label="Core Components">
            <article className="card">
              <h2 className="card-title">Cost-efficient Model Access</h2>
              <p className="card-body">
                Access DeepSeek R1 and DeepSeek V3 through a unified gateway intended
                for lower inference costs in production workloads.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">OpenAI-compatible Chat API</h2>
              <p className="card-body">
                Keep your existing prompts and client logic. Swap the base URL and
                reuse the Chat Completions flow.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Unified Architecture</h2>
              <p className="card-body">
                Frontend is deployed from <code>/frontend</code>, while backend agents and
                integrations live in the repository root.
              </p>
            </article>
          </section>
        </div>
      </main>

      <footer className="footer">
        <div className="footer-inner">
          <span className="footer-brand">SEEKAPI.AI · SEEKAPI.ai</span>
          <span className="footer-meta">
            Built on Vercel · Protected by Cloudflare · Powered by DeepSeek
          </span>
        </div>
      </footer>
    </div>
  );
}
