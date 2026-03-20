/* eslint-disable react/no-unescaped-entities */
"use client";

import { useMemo, useState } from "react";

export default function HomePage() {
  const [tokensM, setTokensM] = useState(120);
  const openAICost = useMemo(() => tokensM * 10, [tokensM]);
  const seekAPICost = useMemo(() => Number((openAICost * 0.12).toFixed(2)), [openAICost]);

  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <section aria-labelledby="hero-title">
            <p className="hero-eyebrow">SEEKAPI.AI · GLOBAL COMPUTE ARBITRAGE</p>
            <h1 className="hero-title" id="hero-title">
              Save 90% on AI API Costs.
            </h1>
            <p className="hero-subtitle">100% OpenAI Compatible. Switch in 30 seconds.</p>

            <div className="hero-badges">
              <span className="badge">DeepSeek R1 / V3 Gateway</span>
              <span className="badge">HK Nodes + Global Edge</span>
              <span className="badge">7-Day Money Back Guarantee</span>
            </div>

            <div className="hero-actions">
              <a href="https://dash.seekapi.ai/login" className="button-primary">
                Get Started
              </a>
              <a href="https://dash.seekapi.ai/login" className="button-ghost">
                Login
              </a>
              <a href="/pricing" className="button-ghost">
                See Pricing
              </a>
            </div>

            <p className="hero-subtitle" style={{ marginTop: "-0.5rem", color: "#9ca3af" }}>
              Trusted by teams building on GitHub, Vercel, and Cloudflare.
            </p>
          </section>

          <section className="card-grid" aria-label="Cost calculator and migration">
            <article className="card">
              <h2 className="card-title">Interactive Calculator</h2>
              <p className="card-body">
                Monthly usage: <strong>{tokensM}M</strong> tokens
                <br />
                OpenAI Cost: <strong>${openAICost.toLocaleString()}</strong>
                <br />
                SeekAPI Cost: <strong>${seekAPICost.toLocaleString()}</strong>
              </p>
              <input
                type="range"
                min={1}
                max={1000}
                value={tokensM}
                onChange={(e) => setTokensM(Number(e.target.value))}
                className="range-slider"
                aria-label="Monthly token usage in millions"
              />
            </article>
            <article className="card">
              <h2 className="card-title">Speed Radar (HK Node)</h2>
              <p className="card-body">
                p50 latency: <strong>82ms</strong>
                <br />
                p95 latency: <strong>137ms</strong>
                <br />
                Uptime: <strong>99.97%</strong>
              </p>
              <div className="status-bars" aria-hidden="true">
                <span style={{ width: "92%" }} />
                <span style={{ width: "84%" }} />
                <span style={{ width: "97%" }} />
              </div>
            </article>
            <article className="card">
              <h2 className="card-title">Code Bridge</h2>
              <p className="card-body">
                Migrate with one change:
                <br />
                <code>openai.base_url = "https://dash.seekapi.ai/v1"</code>
              </p>
              <a href="/compare" className="button-ghost" style={{ display: "inline-block" }}>
                Compare vs OpenAI
              </a>
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
