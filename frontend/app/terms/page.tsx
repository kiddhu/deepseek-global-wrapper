import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export default function TermsPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">LEGAL</p>
          <h1 className="hero-title">Terms of Service</h1>
          <p className="hero-subtitle">
            By using SeekAPI.ai, you agree to use the service lawfully and in accordance with these
            terms.
          </p>

          <section className="card-grid" aria-label="Terms content">
            <article className="card">
              <h2 className="card-title">Service Scope</h2>
              <p className="card-body">
                SeekAPI.ai provides API gateway access and related tooling for approved use cases.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Acceptable Use</h2>
              <p className="card-body">
                You must not abuse the platform, violate laws, or attempt unauthorized access to
                systems or data.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Liability</h2>
              <p className="card-body">
                Service is provided as-is. We may update features and limits to maintain security
                and reliability.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Refund Guarantee</h2>
              <p className="card-body">7-Day Money Back Guarantee for unused balance.</p>
            </article>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
