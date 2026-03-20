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
              <h2 className="card-title">Standard ($0.15 / 1M Tokens)</h2>
              <p className="card-body">
                Best for daily API usage with predictable pricing and OpenAI-compatible requests.
              </p>
            </article>
            <article
              className="card"
              style={{ borderColor: "#111827", boxShadow: "0 0 0 1px #111827 inset" }}
            >
              <h2 className="card-title">Professional ($0.12 / 1M Tokens)</h2>
              <p className="card-body">
                Recommended for scaling products. Lower token cost, priority routing, and higher
                throughput limits.
              </p>
              <p className="badge" style={{ marginTop: "0.8rem", width: "fit-content" }}>
                Most Popular · 80% cheaper than competition
              </p>
            </article>
            <article className="card">
              <h2 className="card-title">Enterprise</h2>
              <p className="card-body">
                Custom
                <br />
                Dedicated support, SLA options, and private deployment integrations.
              </p>
            </article>
          </section>
          <p className="hero-subtitle" style={{ marginTop: "1rem" }}>
            7-Day Money Back Guarantee (Unused Balance)
          </p>
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
