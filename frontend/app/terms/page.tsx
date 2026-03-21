import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "Terms of Service | SeekAPI.ai",
  description:
    "SaaS and API terms for SeekAPI Technology Limited (Hong Kong). Usage-based billing, acceptable use, and API rules.",
  keywords: ["SeekAPI terms", "API terms of service", "Hong Kong SaaS agreement"],
};

export default function TermsPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">LEGAL</p>
          <h1 className="hero-title">Terms of Service</h1>
          <article className="legal-doc card" style={{ padding: "1.75rem 1.5rem 2rem" }}>
            <p className="legal-lead">
              These Terms of Service (“Terms”) govern access to and use of the SeekAPI.ai platform,
              API gateway, dashboard, and related services (collectively, the “Services”) provided
              by <strong>SeekAPI Technology Limited</strong>, a company incorporated in Hong Kong
              (“SeekAPI”, “we”, “us”).
            </p>
            <p className="legal-meta">
              Effective date: March 21, 2026 · Governing law: Hong Kong SAR
            </p>

            <h2>1. Agreement</h2>
            <p>
              By creating an account, obtaining an API key, or otherwise using the Services, you
              (“Customer”, “you”) agree to these Terms and our Privacy Policy. If you use the
              Services on behalf of an organization, you represent that you have authority to bind
              that organization.
            </p>

            <h2>2. The Services</h2>
            <p>
              SeekAPI provides an OpenAI-compatible API gateway and related tooling to route
              inference requests to configured model providers. Features, models, regions, and
              limits may change as we improve reliability, security, and cost efficiency. We may
              suspend or restrict access to comply with law or to protect the platform.
            </p>

            <h2>3. Accounts &amp; API keys</h2>
            <ul>
              <li>
                You are responsible for safeguarding API keys, credentials, and integration secrets.
              </li>
              <li>
                You must promptly notify us of unauthorized use or suspected compromise of your
                account.
              </li>
              <li>
                You may not share credentials in a way that circumvents billing, quotas, or security
                controls.
              </li>
            </ul>

            <h2>4. API usage rules</h2>
            <ul>
              <li>
                You will use the Services only for lawful purposes and in compliance with applicable
                laws and regulations.
              </li>
              <li>
                You will not probe, scan, or attack our systems, upstream providers, or other
                customers; attempt unauthorized access; or interfere with service integrity
                (including DDoS, credential stuffing, or exploitation of vulnerabilities).
              </li>
              <li>
                You will not use the Services to generate, distribute, or facilitate illegal
                content, malware, fraud, harassment, or rights violations.
              </li>
              <li>
                You remain responsible for your application logic, prompts, outputs, and downstream
                use of model responses.
              </li>
            </ul>

            <h2>5. Usage-based billing</h2>
            <p>
              Unless otherwise agreed in writing, fees are based on measured usage (for example,
              tokens processed, requests, or plan tiers published on our Pricing page). Usage
              metrics recorded by our systems are generally decisive for billing disputes, subject
              to reasonable verification. Taxes may apply where required.
            </p>

            <h2>6. Service levels &amp; disclaimers</h2>
            <p>
              The Services are provided on an “as available” basis unless a separate SLA is
              executed. We do not guarantee uninterrupted operation or error-free outputs from
              underlying model providers. To the maximum extent permitted by law, we disclaim
              implied warranties including merchantability and fitness for a particular purpose.
            </p>

            <h2>7. Limitation of liability</h2>
            <p>
              To the maximum extent permitted by law, SeekAPI’s aggregate liability arising out of
              these Terms will not exceed the fees paid by you for the Services in the three (3)
              months preceding the claim. We are not liable for indirect, incidental, special,
              consequential, or punitive damages, or loss of profits, data, or goodwill, except
              where liability cannot be excluded under applicable law.
            </p>

            <h2>8. Indemnity</h2>
            <p>
              You will defend and indemnify SeekAPI against third-party claims arising from your use
              of the Services, your applications, your content, or your violation of these Terms or
              applicable law.
            </p>

            <h2>9. Suspension &amp; termination</h2>
            <p>
              We may suspend or terminate access for breach, risk to the platform, non-payment, or
              legal requirements. You may stop using the Services at any time. Provisions that by
              nature should survive (fees owed, liability limits, indemnity, governing law) survive
              termination.
            </p>

            <h2>10. Changes</h2>
            <p>
              We may update these Terms by posting a revised version and updating the effective
              date. Continued use after changes become effective constitutes acceptance. Material
              adverse changes will be communicated through reasonable channels where practicable.
            </p>

            <h2>11. Contact</h2>
            <p>
              Questions about these Terms:{" "}
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
