export default function LegalPage() {
  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">LEGAL</p>
          <h1 className="hero-title">Trust Fortress</h1>
          <p className="hero-subtitle">
            Policies that protect both your business and your users. Start here for compliance and
            billing guarantees.
          </p>

          <section className="card-grid" aria-label="Legal pages">
            <article className="card">
              <h2 className="card-title">Terms of Service</h2>
              <p className="card-body">
                Usage boundaries, responsibilities, and service-level expectations.
                <br />
                <a
                  href="/terms"
                  className="button-ghost"
                  style={{ display: "inline-block", marginTop: 12 }}
                >
                  Read Terms
                </a>
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Privacy Policy</h2>
              <p className="card-body">
                Data handling standards and retention principles.
                <br />
                <a
                  href="/privacy"
                  className="button-ghost"
                  style={{ display: "inline-block", marginTop: 12 }}
                >
                  Read Privacy Policy
                </a>
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Refund Policy</h2>
              <p className="card-body">
                7-Day Money Back Guarantee for unused balance.
                <br />
                <a
                  href="/refund"
                  className="button-ghost"
                  style={{ display: "inline-block", marginTop: 12 }}
                >
                  Read Refund Policy
                </a>
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
