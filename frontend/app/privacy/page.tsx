export default function PrivacyPage() {
  return (
    <div className="page-shell">
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
