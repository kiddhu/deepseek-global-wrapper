import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Privacy & Data Governance | SeekAPI.ai",
  description:
    "Privacy policy for SeekAPI Technology Limited. Stateless relay architecture, metadata for billing, zero-retention for prompt content.",
  robots: { index: true, follow: true },
};

export default function PrivacyPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content bg-white">
        <article className="legal-prose legal-prose--privacy" lang="en">
          <h1>Privacy &amp; Data Governance</h1>

          <h3>1. Data Pass-Through Architecture</h3>
          <p>
            Our infrastructure is designed as a &quot;stateless relay.&quot; We do not store, log,
            or analyze the content of your API prompts (inputs) or model completions (outputs) in
            any persistent storage. Data is transmitted via secure SSL/TLS encryption directly to
            the upstream inference nodes.
          </p>

          <h3>2. Metadata Collection</h3>
          <p>
            For the sole purposes of billing, rate-limiting, and security audit, we collect
            non-content metadata, which includes: User Email, API Key ID, Timestamp of Request,
            Total Token Count, and Origin IP Address.
          </p>

          <h3>3. Zero-Retention Policy</h3>
          <p>
            SeekAPI Technology Limited guarantees a zero-retention policy for user-generated
            content. We are physically incapable of complying with data requests for historical
            prompt content as said data is never saved to our disks.
          </p>

          <h3>4. Global Compliance (GDPR/CCPA Context)</h3>
          <p>
            While based in Hong Kong, we adhere to the principles of data minimization and purpose
            limitation. By using the service, you consent to the processing of your metadata in our
            Hong Kong-based infrastructure nodes.
          </p>

          <p className="legal-copy-footer">
            Copyright © 2026 SeekAPI Technology Limited. All rights reserved.
          </p>
        </article>
      </main>
      <SiteFooter />
    </div>
  );
}
