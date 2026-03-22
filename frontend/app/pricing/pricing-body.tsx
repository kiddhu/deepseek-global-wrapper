"use client";

/**
 * Swap these when Stripe / checkout URLs are ready (SeekAPI Technology Limited).
 * All default to the console with UTM for main-site attribution.
 */
const starterLink =
  process.env.NEXT_PUBLIC_PRICING_STARTER_URL ??
  "https://dash.seekapi.ai/login?utm_source=main_site";
const proLink =
  process.env.NEXT_PUBLIC_PRICING_PRO_URL ?? "https://dash.seekapi.ai/login?utm_source=main_site";
const enterpriseLink =
  process.env.NEXT_PUBLIC_PRICING_ENTERPRISE_URL ??
  "https://dash.seekapi.ai/login?utm_source=main_site";
const boostLiteLink =
  process.env.NEXT_PUBLIC_PRICING_BOOST_LITE_URL ??
  "https://dash.seekapi.ai/login?utm_source=main_site&utm_medium=boost_lite";
const boostProLink =
  process.env.NEXT_PUBLIC_PRICING_BOOST_PRO_URL ??
  "https://dash.seekapi.ai/login?utm_source=main_site&utm_medium=boost_pro";

function PaymentMethodStrip() {
  return (
    <div className="pricing-pay-strip" aria-label="Accepted payment methods">
      <span className="pricing-pay-badge" title="Visa">
        VISA
      </span>
      <span className="pricing-pay-badge" title="Mastercard">
        Mastercard
      </span>
      <span className="pricing-pay-badge" title="American Express">
        AMEX
      </span>
      <span className="pricing-pay-badge" title="Apple Pay">
        Apple Pay
      </span>
      <span className="pricing-pay-badge" title="Google Pay">
        Google Pay
      </span>
    </div>
  );
}

function ClockRolloverTip({ children }: { children: React.ReactNode }) {
  return (
    <div className="pricing-rollover-tip" role="note">
      <span className="pricing-rollover-icon" aria-hidden="true">
        <svg
          width="18"
          height="18"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle cx="12" cy="12" r="9" stroke="currentColor" strokeWidth="1.75" />
          <path d="M12 7v5l3 2" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" />
        </svg>
      </span>
      <span className="pricing-rollover-text">{children}</span>
    </div>
  );
}

export function PricingBody() {
  return (
    <>
      <div className="pricing-float-guarantee" role="status">
        <span className="pricing-float-guarantee-inner">
          7-Day Risk-Free — Unused balance fully refundable
        </span>
      </div>

      <main className="page-content pricing-page-main">
        <div className="container">
          <p className="hero-eyebrow">PRICING</p>
          <h1 className="hero-title">The compute bank</h1>
          <p className="hero-subtitle">
            Subscription includes a token pool, rollover windows, and production-grade RPM walls.
            Top up anytime with Credit Boosters — no extra subscription.
          </p>
          <p className="pricing-fomo-line">
            Early pricing — rates may increase as compute demand grows.
          </p>

          <section className="pricing-grid" aria-label="Pricing tiers V4.3">
            <article className="pricing-card">
              <p className="pricing-tier-tag">Lead magnet</p>
              <h2 className="pricing-card-title">Explorer</h2>
              <p className="pricing-card-price">
                <span className="pricing-price-main">$0</span>
                <span className="pricing-price-unit">$0.50 credit · 1 RPM (strictly limited)</span>
              </p>
              <ul className="pricing-card-list">
                <li>Try the gateway with minimal friction</li>
                <li>
                  <strong>1 RPM</strong> — anti-abuse cap; not for production load
                </li>
                <li>Upgrade to Growth when you ship real traffic</li>
              </ul>
              <a href={starterLink} className="button-primary pricing-card-cta">
                Start with Explorer
              </a>
              <PaymentMethodStrip />
            </article>

            <article className="pricing-card pricing-card--best pricing-card--growth-lift">
              <div className="pricing-ribbon" aria-hidden="true">
                Core savings
              </div>
              <p className="pricing-tier-tag pricing-tier-tag--pro">Compute bank</p>
              <h2 className="pricing-card-title">Growth</h2>
              <p className="pricing-card-price">
                <span className="pricing-price-main">$20</span>
                <span className="pricing-price-unit">/ month</span>
              </p>
              <p className="pricing-growth-anchor">Most developers start here.</p>
              <div className="pricing-compare-block" aria-label="OpenAI equivalent savings">
                <p className="pricing-compare-line">
                  Equivalent OpenAI cost: <strong className="pricing-compare-strong">$160</strong>
                </p>
                <p className="pricing-compare-line">
                  You pay: <strong className="pricing-compare-strong">$20</strong>
                </p>
                <p className="pricing-compare-savings-line">
                  → SAVE <strong className="pricing-savings-emphasis">87.5%</strong> (
                  <strong className="pricing-savings-emphasis">$140 SAVED</strong>)
                </p>
              </div>
              <ul className="pricing-card-list">
                <li>
                  <strong>80M tokens</strong> included per billing cycle
                </li>
                <li>
                  <strong>2-month rollover</strong> — unused included balance rolls up to two months
                </li>
                <li>
                  Overage: <strong>$0.14 / 1M</strong> tokens
                </li>
                <li>
                  <strong>30 RPM</strong> — production-grade wall
                </li>
              </ul>
              <ClockRolloverTip>Your compute balance remains valid for 60 days.</ClockRolloverTip>
              <a href={proLink} className="button-primary pricing-card-cta">
                Start Saving $140/month
              </a>
              <PaymentMethodStrip />
            </article>

            <article className="pricing-card">
              <p className="pricing-tier-tag">High throughput</p>
              <h2 className="pricing-card-title">Scale</h2>
              <p className="pricing-scale-hook">
                For teams &amp; high-volume apps. Maximum savings tier.
              </p>
              <p className="pricing-card-price">
                <span className="pricing-price-main">$99</span>
                <span className="pricing-price-unit">/ month</span>
              </p>
              <ul className="pricing-card-list">
                <li>
                  <strong>400M tokens</strong> included per billing cycle
                </li>
                <li>
                  <strong>3-month rollover</strong> on included compute
                </li>
                <li>
                  Overage: <strong>$0.12 / 1M</strong> tokens
                </li>
                <li>
                  <strong>100+ RPM</strong> — high throughput lane
                </li>
              </ul>
              <ClockRolloverTip>
                Included compute rolls for up to 90 days on Scale.
              </ClockRolloverTip>
              <a href={enterpriseLink} className="button-ghost pricing-card-cta">
                Get Maximum Savings
              </a>
              <PaymentMethodStrip />
            </article>
          </section>

          <section className="pricing-boosters" aria-labelledby="boosters-heading">
            <h2 id="boosters-heading" className="pricing-boosters-title">
              Credit Boosters
            </h2>
            <p className="pricing-boosters-lead">
              Need more power? Instantly top up your compute bank without recurring commitments.
            </p>
            <div className="pricing-boosters-grid">
              <article className="pricing-booster-card">
                <h3 className="pricing-booster-name">Lite Boost</h3>
                <p className="pricing-booster-deal">
                  Pay <strong>$50</strong> → bank <strong>250M tokens</strong> of runway at bulk
                  rates.
                </p>
                <a href={boostLiteLink} className="button-ghost pricing-booster-cta">
                  Buy Lite Boost
                </a>
              </article>
              <article className="pricing-booster-card pricing-booster-card--pro">
                <span className="pricing-bonus-badge" aria-label="10 percent bonus">
                  10% BONUS
                </span>
                <h3 className="pricing-booster-name">Pro Boost</h3>
                <p className="pricing-booster-deal">
                  Pay <strong>$100</strong> → Get <strong>$110</strong> compute value.
                </p>
                <a href={boostProLink} className="button-primary pricing-booster-cta">
                  Buy Pro Boost
                </a>
              </article>
            </div>
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
              href="https://dash.seekapi.ai/login?utm_source=main_site"
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
