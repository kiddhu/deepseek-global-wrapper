import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Privacy Policy | SeekAPI.ai",
  description:
    "How SeekAPI Technology Limited handles personal data, billing telemetry, and API traffic metadata.",
  keywords: ["SeekAPI privacy", "API privacy policy", "data processing Hong Kong"],
};

export default function PrivacyPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">LEGAL</p>
          <h1 className="hero-title">Privacy Policy</h1>
          <article className="legal-doc card" style={{ padding: "1.75rem 1.5rem 2rem" }}>
            <p className="legal-lead">
              This Privacy Policy describes how <strong>SeekAPI Technology Limited</strong>{" "}
              (“SeekAPI”, “we”) collects, uses, and shares information when you use SeekAPI.ai and
              related services (the “Services”).
            </p>
            <p className="legal-meta">Effective date: March 21, 2026 · Hong Kong SAR operations</p>

            <h2>1. Scope</h2>
            <p>
              This policy applies to visitors, account holders, and developers integrating our API.
              If you integrate SeekAPI into your own product, you are responsible for providing
              appropriate notices to your end users where required.
            </p>

            <h2>2. What we collect</h2>
            <ul>
              <li>
                <strong>Account &amp; billing:</strong> name, email, organization details, billing
                address where required, payment references, and transaction history.
              </li>
              <li>
                <strong>Service telemetry:</strong> request metadata needed to operate the platform
                (timestamps, request ids, model identifiers, token counts, latency, error codes, and
                abuse-prevention signals).
              </li>
              <li>
                <strong>Support communications:</strong> messages you send to support@seekapi.ai and
                related troubleshooting context.
              </li>
            </ul>

            <h2>3. API requests and prompt content</h2>
            <p>
              <strong>
                We do not store the substantive text of your API prompts or model outputs for
                analytics, training, or secondary product purposes.
              </strong>{" "}
              Our standard metering flow is designed to record what is necessary to deliver the
              Services and bill usage—principally <strong>token counts and related metadata</strong>{" "}
              associated with each request.
            </p>
            <p>
              Transient processing may occur in memory or short-lived infrastructure buffers to
              complete a request and return a response. We do not use your prompts or completions to
              build advertising profiles. If we ever offer an opt-in feature that requires retention
              of content (for example, optional logging), it will be clearly disclosed and
              controlled by contract or product settings.
            </p>

            <h2>4. How we use information</h2>
            <ul>
              <li>Provide, secure, and troubleshoot the Services.</li>
              <li>Meter usage, prevent fraud, and enforce our Terms of Service.</li>
              <li>Comply with legal obligations and respond to lawful requests.</li>
              <li>Communicate service updates, security notices, and billing matters.</li>
            </ul>

            <h2>5. Processors &amp; infrastructure</h2>
            <p>
              We use vetted hosting, payment, and communications providers. They may process data on
              our behalf under contractual safeguards appropriate to the processing activity.
            </p>

            <h2>6. Retention</h2>
            <p>
              We retain information only as long as needed for the purposes above, including legal,
              tax, and accounting requirements. Telemetry retention periods may vary by subsystem
              and security need.
            </p>

            <h2>7. Security</h2>
            <p>
              We implement technical and organizational measures designed to protect information
              against unauthorized access, alteration, or destruction. No method of transmission or
              storage is completely secure.
            </p>

            <h2>8. International transfers</h2>
            <p>
              Your information may be processed in Hong Kong and other regions where our providers
              operate. Where transfers are required, we take steps consistent with applicable law.
            </p>

            <h2>9. Your rights</h2>
            <p>
              Depending on your jurisdiction, you may have rights to access, correct, delete, or
              restrict certain personal data, or to object to processing. Contact us to exercise
              rights; we may need to verify your request.
            </p>

            <h2>10. Contact</h2>
            <p>
              Privacy inquiries:{" "}
              <a href="mailto:support@seekapi.ai" className="footer-link-min">
                support@seekapi.ai
              </a>
            </p>
          </article>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
