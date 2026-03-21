import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Status | SeekAPI.ai",
  description: "Public health indicators for SeekAPI gateway and edge lanes.",
};

export default function StatusPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">STATUS</p>
          <h1 className="hero-title">System Status</h1>
          <p className="hero-subtitle">
            Live posture for core ingress paths. Values are representative health signals for
            production traffic.
          </p>

          <section
            className="card-grid"
            style={{ marginTop: "1.5rem" }}
            aria-label="Regional gateway status"
          >
            <article className="status-lane-card">
              <h2 className="status-lane-title">API Gateway</h2>
              <p className="status-lane-meta">Operational · primary control plane</p>
              <div className="status-lane-bar" role="presentation" />
            </article>
            <article className="status-lane-card">
              <h2 className="status-lane-title">US-East Edge</h2>
              <p className="status-lane-meta">Operational · low-latency ingress</p>
              <div className="status-lane-bar" role="presentation" />
            </article>
            <article className="status-lane-card">
              <h2 className="status-lane-title">HK-Gateway</h2>
              <p className="status-lane-meta">Operational · Asia-Pacific routing</p>
              <div className="status-lane-bar" role="presentation" />
            </article>
          </section>

          <section className="card-grid" style={{ marginTop: "1.25rem" }} aria-label="Additional">
            <article className="card">
              <h2 className="card-title">DeepSeek Nodes</h2>
              <p className="card-body">STABLE · model pools accepting production traffic</p>
              <div className="heartbeat-line" aria-hidden="true">
                <span />
              </div>
            </article>
            <article className="card">
              <h2 className="card-title">Billing &amp; Credits</h2>
              <p className="card-body">Operational · balance updates and metering active</p>
            </article>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
