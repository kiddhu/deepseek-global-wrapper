export default function StatusPage() {
  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">STATUS</p>
          <h1 className="hero-title">Reliability, Measured</h1>
          <p className="hero-subtitle">
            Public health indicators provide confidence before you route production traffic.
          </p>

          <section className="card-grid" aria-label="Service health metrics">
            <article className="card">
              <h2 className="card-title">Global API Gateway</h2>
              <p className="card-body">Operational · 99.97% uptime (30-day rolling)</p>
            </article>
            <article className="card">
              <h2 className="card-title">HK Primary Node</h2>
              <p className="card-body">Operational · p95 latency 137ms</p>
            </article>
            <article className="card">
              <h2 className="card-title">Billing & Credits</h2>
              <p className="card-body">Operational · real-time balance updates active</p>
            </article>
          </section>
        </div>
      </main>
      <footer className="footer">
        <div className="footer-inner">
          <span className="footer-brand">
            Room P11, Flat 2C, 2/F, Hung To Ctr., 94-96 How Ming St., Kwun Tong, Kowloon, HK
          </span>
          <span className="footer-meta">support@seekapi.ai</span>
          <span className="footer-meta">© 2026 SeekAPI.ai | AION: The Era of the One.</span>
        </div>
      </footer>
    </div>
  );
}
