"use client";

export function PricingBody() {
  return (
    <>
      <div className="pricing-float-guarantee" role="status">
        <span className="pricing-float-guarantee-inner">
          7-Day Money Back Guarantee for Unused Balance
        </span>
      </div>

      <main className="page-content pricing-page-main">
        <div className="container">
          <p className="hero-eyebrow">PRICING</p>
          <h1 className="hero-title">Hybrid pricing built for conversion</h1>
          <p className="hero-subtitle">
            Start free, scale on usage, graduate to VIP routing when revenue justifies it. DeepSeek
            R1 &amp; V3 · OpenAI-compatible SDKs.
          </p>

          <section className="pricing-grid" aria-label="Pricing tiers">
            <article className="pricing-card">
              <h2 className="pricing-card-title">Free Starter</h2>
              <p className="pricing-card-price">
                <span className="pricing-price-main">$0</span>
              </p>
              <ul className="pricing-card-list">
                <li>$0.50 Free Credit</li>
                <li>No Card Required</li>
                <li>30s Setup</li>
              </ul>
              <p className="pricing-card-psych">
                Low friction — we only need your email to issue a key and meter usage.
              </p>
              <a href="https://dash.seekapi.ai/login" className="button-primary pricing-card-cta">
                Claim free credit
              </a>
            </article>

            <article className="pricing-card">
              <p className="pricing-tier-tag">Standard Performance</p>
              <h2 className="pricing-card-title">Pay-as-you-go</h2>
              <p className="pricing-card-price">
                <span className="pricing-price-main">$0.20</span>
                <span className="pricing-price-unit">/ 1M tokens</span>
              </p>
              <ul className="pricing-card-list">
                <li>Usage-based billing — pay only for what you run</li>
                <li>Global OpenAI-compatible endpoint</li>
                <li>Ideal for prototypes and steady production traffic</li>
              </ul>
              <a href="https://dash.seekapi.ai/login" className="button-ghost pricing-card-cta">
                Start on Standard
              </a>
            </article>

            <article className="pricing-card pricing-card--best">
              <div className="pricing-ribbon" aria-hidden="true">
                Best Value
              </div>
              <p className="pricing-tier-tag pricing-tier-tag--pro">The Growth Engine</p>
              <h2 className="pricing-card-title">Professional</h2>
              <p className="pricing-card-price">
                <span className="pricing-price-main">$29</span>
                <span className="pricing-price-unit">/ month</span>
              </p>
              <ul className="pricing-card-list">
                <li>
                  <strong>Rate:</strong> $0.15 / 1M tokens (included tier economics)
                </li>
                <li>
                  <strong>Priority VIP Routing</strong> — faster lanes when it matters
                </li>
                <li>
                  <strong>SLA Guarantee</strong> — enterprise-grade uptime commitments
                </li>
              </ul>
              <a href="https://dash.seekapi.ai/login" className="button-primary pricing-card-cta">
                Upgrade to Professional
              </a>
            </article>
          </section>

          <section className="pricing-api-anchor" aria-labelledby="api-anchor-title">
            <h2 id="api-anchor-title" className="pricing-api-anchor-title">
              One-line integration
            </h2>
            <p className="pricing-api-anchor-lead">
              Replace your OpenAI base URL — keep your SDK and prompts.
            </p>
            <pre className="pricing-api-snippet" tabIndex={0}>
              <code>base_url = &quot;https://api.seekapi.ai/v1&quot;</code>
            </pre>
            <a
              href="https://dash.seekapi.ai/login"
              className="button-ghost"
              style={{ marginTop: "0.75rem" }}
            >
              Open dashboard
            </a>
          </section>
        </div>
      </main>
    </>
  );
}
