/* eslint-disable react/no-unescaped-entities */
"use client";

import { useMemo, useState } from "react";
import { SiteFooter } from "./components/site-footer";
import { SiteHeader } from "./components/site-header";

const PYTHON_SAMPLE = `from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENAI_KEY",
    base_url="https://api.openai.com/v1",
)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello"}],
)`;

const NODE_SAMPLE = `import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: "https://api.openai.com/v1",
});

const resp = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Hello" }],
});`;

function convertToSeekApi(code: string) {
  return code
    .replace(/https:\/\/api\.openai\.com\/v1/g, "https://api.seekapi.ai/v1")
    .replace(/base_url\s*=\s*["'][^"']+["']/g, 'base_url="https://api.seekapi.ai/v1"')
    .replace(/baseURL\s*:\s*["'][^"']+["']/g, 'baseURL: "https://api.seekapi.ai/v1"');
}

export default function HomePage() {
  const [tokensM, setTokensM] = useState(120);
  const [lang, setLang] = useState<"python" | "node">("python");
  const [inputCode, setInputCode] = useState(PYTHON_SAMPLE);
  const openAICost = useMemo(() => tokensM * 10, [tokensM]);
  const seekAPICost = useMemo(() => Number((openAICost * 0.12).toFixed(2)), [openAICost]);
  const transformedCode = useMemo(() => convertToSeekApi(inputCode), [inputCode]);

  return (
    <div className="page-shell">
      <SiteHeader />
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
              <span className="badge">OpenAI-compatible API</span>
              <span className="badge">7-Day Money Back Guarantee</span>
            </div>

            <div className="hero-actions">
              <a href="https://dash.seekapi.ai/login" className="button-primary">
                Get Started
              </a>
              <a href="https://dash.seekapi.ai/login" className="button-ghost">
                Login
              </a>
            </div>
            <a href="https://dash.seekapi.ai/login" className="credit-pill">
              $0.50 Free Credit - No Credit Card Required
            </a>
            <p className="hero-subtitle" style={{ marginTop: "-0.5rem", marginBottom: "0.75rem" }}>
              Trusted by teams building on GitHub, Vercel, and Cloudflare.
            </p>
            <div className="trusted-logos" aria-hidden="true">
              <svg viewBox="0 0 64 24" className="logo-placeholder">
                <path d="M8 12h48" stroke="#9ca3af" strokeWidth="2" />
              </svg>
              <svg viewBox="0 0 64 24" className="logo-placeholder">
                <path d="M10 7h44v10H10z" fill="none" stroke="#9ca3af" strokeWidth="2" />
              </svg>
              <svg viewBox="0 0 64 24" className="logo-placeholder">
                <path d="M8 16l8-8 8 8 8-8 8 8 8-8" fill="none" stroke="#9ca3af" strokeWidth="2" />
              </svg>
              <svg viewBox="0 0 64 24" className="logo-placeholder">
                <path d="M8 8h48M8 16h36" stroke="#9ca3af" strokeWidth="2" />
              </svg>
            </div>
          </section>

          <section className="card-grid" aria-label="Core Components">
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
              <h2 className="card-title">Real-time Arbitrage Monitor</h2>
              <p className="card-body">
                Price: OpenAI <strong>($20.00)</strong> vs SeekAPI <strong>($2.00)</strong> / 1M
                tokens
              </p>
              <div className="status-bars">
                <span style={{ width: "22%" }} />
                <span style={{ width: "90%" }} />
              </div>
              <p className="card-body" style={{ marginTop: "0.8rem" }}>
                Latency: OpenAI (US) <strong>137ms</strong> vs SeekAPI (HK-Global){" "}
                <strong>82ms</strong>
              </p>
              <div className="status-bars">
                <span style={{ width: "59%" }} />
                <span style={{ width: "87%" }} />
              </div>
            </article>
            <article className="card">
              <h2 className="card-title">1-Click Migration Transformer</h2>
              <p className="card-body">Keep your code, cut your bill.</p>
              <div className="tab-row">
                <button
                  type="button"
                  className={lang === "python" ? "tab tab-active" : "tab"}
                  onClick={() => {
                    setLang("python");
                    setInputCode(PYTHON_SAMPLE);
                  }}
                >
                  Python
                </button>
                <button
                  type="button"
                  className={lang === "node" ? "tab tab-active" : "tab"}
                  onClick={() => {
                    setLang("node");
                    setInputCode(NODE_SAMPLE);
                  }}
                >
                  Node.js
                </button>
              </div>
              <div className="code-grid">
                <label className="code-box">
                  <span className="code-title">OpenAI Code Input</span>
                  <textarea
                    value={inputCode}
                    onChange={(e) => setInputCode(e.target.value)}
                    className="code-area"
                  />
                </label>
                <label className="code-box">
                  <span className="code-title">SeekAPI Output</span>
                  <textarea value={transformedCode} readOnly className="code-area" />
                </label>
              </div>
              <button
                type="button"
                className="button-ghost"
                onClick={() => navigator.clipboard.writeText(transformedCode)}
                style={{ marginTop: "0.8rem" }}
              >
                Copy SeekAPI Code
              </button>
            </article>
          </section>

          <section className="card-grid" aria-label="Code Bridge">
            <article className="card">
              <h2 className="card-title">Code Bridge</h2>
              <p className="card-body">
                Migrate with one change:
                <br />
                <code>openai.base_url = "https://api.seekapi.ai/v1"</code>
              </p>
              <a href="/compare" className="button-ghost" style={{ display: "inline-block" }}>
                Compare vs OpenAI
              </a>
            </article>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
