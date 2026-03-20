import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export default function StatusPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">STATUS</p>
          <h1 className="hero-title">Reliability, Measured</h1>
          <p className="hero-subtitle">
            Public health indicators provide confidence before you route production traffic.
          </p>

          <section className="card-grid" aria-label="Service health metrics">
            <article className="card">
              <h2 className="card-title">API Gateway</h2>
              <p className="card-body">ONLINE · 99.97% uptime (30-day rolling)</p>
              <div className="heartbeat-line" aria-hidden="true">
                <span />
              </div>
            </article>
            <article className="card">
              <h2 className="card-title">DeepSeek Nodes</h2>
              <p className="card-body">STABLE · HK-Global p95 latency 82ms</p>
              <div className="heartbeat-line" aria-hidden="true">
                <span />
              </div>
            </article>
            <article className="card">
              <h2 className="card-title">Billing & Credits</h2>
              <p className="card-body">Operational · real-time balance updates active</p>
            </article>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
