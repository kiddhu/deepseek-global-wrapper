export default function PricingPage() {
  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">PRICING</p>
          <h1 className="hero-title">Plans for Teams of Any Size</h1>
          <p className="hero-subtitle">
            Transparent plans for developers, startups, and enterprise workloads.
          </p>

          <section className="card-grid" aria-label="Pricing plans">
            <article className="card">
              <h2 className="card-title">Free</h2>
              <p className="card-body">$0</p>
            </article>
            <article className="card">
              <h2 className="card-title">Starter</h2>
              <p className="card-body">$20/mo</p>
            </article>
            <article className="card">
              <h2 className="card-title">Enterprise</h2>
              <p className="card-body">Custom</p>
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
