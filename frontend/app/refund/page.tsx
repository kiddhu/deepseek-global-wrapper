import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Refund Policy | SeekAPI.ai",
  description:
    "7-Day Money Back Guarantee for unused balance. Refunds processed within 3-5 business days where eligible.",
  keywords: ["SeekAPI refund", "money back guarantee", "unused balance refund"],
};

export default function RefundPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">LEGAL</p>
          <h1 className="hero-title">Refund Policy</h1>
          <article className="legal-doc card" style={{ padding: "1.75rem 1.5rem 2rem" }}>
            <p className="legal-lead">
              This Refund Policy explains how <strong>SeekAPI International Limited</strong> handles
              refund requests for SeekAPI.ai prepaid balances and qualifying charges.
            </p>
            <p className="legal-meta">Effective date: March 21, 2026</p>

            <h2>7-Day Money Back Guarantee (unused balance)</h2>
            <p>
              If you are a new paying customer and request a refund within{" "}
              <strong>seven (7) calendar days</strong> of your initial qualifying purchase, we will
              refund the <strong>unused portion</strong> of your prepaid balance or eligible fees,
              subject to verification and the exclusions below.
            </p>
            <ul>
              <li>
                <strong>Unused balance</strong> means amounts not yet consumed as usage credits at
                the time we approve the request.
              </li>
              <li>
                Usage that has already been metered and applied to your account is generally not
                refundable, except where required by law or explicitly agreed in writing.
              </li>
            </ul>

            <h2>Processing timeline</h2>
            <p>
              Approved refunds are typically initiated within{" "}
              <strong>three (3) to five (5) business days</strong> after approval. Settlement to
              your original payment method may take additional time depending on banks, card
              networks, or payment processors.
            </p>

            <h2>How to request a refund</h2>
            <p>
              Email{" "}
              <a href="mailto:support@seekapi.ai" className="footer-link-min">
                support@seekapi.ai
              </a>{" "}
              from your registered account email and include: account identifier, date of purchase,
              transaction references, and a brief description of the issue. We may request
              additional information to prevent fraud and confirm eligibility.
            </p>

            <h2>Non-refundable or limited cases</h2>
            <ul>
              <li>Fees for usage already consumed or invoiced under contract terms.</li>
              <li>Accounts terminated for abuse, fraud, or violation of our Terms of Service.</li>
              <li>Third-party charges (for example, bank fees, FX spreads) outside our control.</li>
              <li>Promotional credits labeled as non-refundable at grant time.</li>
            </ul>

            <h2>Chargebacks</h2>
            <p>
              Please contact us before initiating a chargeback where possible. Chargebacks may
              result in account suspension pending resolution.
            </p>

            <h2>Changes</h2>
            <p>
              We may update this policy from time to time. The effective date at the top will
              reflect the latest version.
            </p>
          </article>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
