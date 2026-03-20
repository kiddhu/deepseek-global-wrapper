import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export default function PrivacyPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">LEGAL</p>
          <h1 className="hero-title">Privacy Policy</h1>
          <p className="hero-subtitle">
            We only process data required to operate, secure, and improve the SeekAPI.ai platform.
          </p>

          <section className="card-grid" aria-label="Privacy content">
            <article className="card">
              <h2 className="card-title">Data We Collect</h2>
              <p className="card-body">
                Account, billing, usage metrics, and request metadata required for service operation
                and abuse prevention.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">How We Use Data</h2>
              <p className="card-body">
                To provide API access, monitor performance, prevent fraud, and support customers.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Retention & Security</h2>
              <p className="card-body">
                Data is retained only as necessary and protected through technical and
                administrative safeguards.
              </p>
            </article>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
