export default function RefundPage() {
  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">LEGAL</p>
          <h1 className="hero-title">Refund Policy</h1>
          <p className="hero-subtitle">
            Refund requests are reviewed based on billing status, usage history, and documented
            service incidents.
          </p>
          <p className="hero-subtitle" style={{ marginTop: "-0.5rem" }}>
            7-Day Money Back Guarantee for unused balance.
          </p>

          <section className="card-grid" aria-label="Refund content">
            <article className="card">
              <h2 className="card-title">Eligibility</h2>
              <p className="card-body">
                You may request a refund for accidental charges or confirmed service failures within
                the applicable billing period.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Request Process</h2>
              <p className="card-body">
                Contact support@seekapi.ai with account details and billing evidence for review.
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Review Timeline</h2>
              <p className="card-body">
                Most requests are reviewed within 5-10 business days. Approved refunds are returned
                to the original payment method.
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
