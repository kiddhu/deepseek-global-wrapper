export default function TermsPage() {
  return (
    <div className="page-shell">
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
