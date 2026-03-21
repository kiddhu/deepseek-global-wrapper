import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Legal | SeekAPI.ai",
  description: "Terms, privacy, and refund policies for SeekAPI International Limited.",
};

export default function LegalPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
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
      <SiteFooter />
    </div>
  );
}
