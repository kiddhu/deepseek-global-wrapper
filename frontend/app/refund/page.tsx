import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Refund Policy | SeekAPI.ai",
  description:
    "Refund policy for SeekAPI Technology Limited. 7-day money back on unused balance; processing 3–5 business days.",
  robots: { index: true, follow: true },
};

export default function RefundPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content bg-white">
        <div className="legal-refund-frame">
          <h1>Refund Policy</h1>

          <section className="legal-refund-highlight" aria-labelledby="guarantee-heading">
            <h2 id="guarantee-heading">7-Day Ironclad Money Back Guarantee</h2>
            <p>
              We provide a 100% refund of the UNUSED BALANCE to any user within seven (7) calendar
              days of the initial purchase date, no questions asked.
            </p>
          </section>

          <h3>1. Eligibility Criteria</h3>
          <ul>
            <li>Refunds only apply to the current remaining credit balance.</li>
            <li>
              Used tokens are non-refundable under any circumstances as the compute resources have
              been physically consumed.
            </li>
            <li>
              Promotion-based credits or bonus balances hold no cash value and are strictly
              non-refundable.
            </li>
          </ul>

          <h3>2. Refund Procedure</h3>
          <p>
            All refund requests must be initiated via email to{" "}
            <a className="legal-mail" href="mailto:support@seekapi.ai">
              support@seekapi.ai
            </a>
            . Our financial department will verify the unused balance and process the refund via
            Stripe or the original payment method within 3 to 5 business days.
          </p>

          <h3>3. Finality of Agreement</h3>
          <p>
            Upon the successful processing of a refund, the associated API Key and account access
            will be terminated. This policy is designed to maintain compliance with Stripe&apos;s
            global consumer protection standards and Hong Kong consumer law.
          </p>

          <p className="legal-copy-footer">
            Copyright © 2026 SeekAPI Technology Limited. All rights reserved.
          </p>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
