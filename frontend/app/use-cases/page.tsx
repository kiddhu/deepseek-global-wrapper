export default function UseCasesPage() {
  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">USE CASES</p>
          <h1 className="hero-title">Blueprints That Convert</h1>
          <p className="hero-subtitle">
            Proven deployment patterns for teams that care about cost per request and growth speed.
          </p>

          <section className="card-grid" aria-label="Use case templates">
            <article className="card">
              <h2 className="card-title">Customer Support Copilot</h2>
              <p className="card-body">
                Reduce support response cost while maintaining quality for high-volume ticket
                queues.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Marketing Content Engine</h2>
              <p className="card-body">
                Power multilingual blog and ad generation pipelines with lower variable API spend.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Code Review Assistant</h2>
              <p className="card-body">
                Integrate into CI to analyze pull requests, summarize risk, and suggest fixes at
                scale.
              </p>
            </article>
          </section>
        </div>
      </main>
      <div className="footer" role="contentinfo" aria-label="Site footer">
        <div className="footer-inner">
          <span className="footer-brand">
            Room P11, Flat 2C, 2/F, Hung To Ctr., 94-96 How Ming St., Kwun Tong, Kowloon, HK
          </span>
          <span className="footer-meta">support@seekapi.ai</span>
          <span className="footer-meta">© 2026 SeekAPI.ai | AION: The Era of the One.</span>
        </div>
      </div>
    </div>
  );
}
