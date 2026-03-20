import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

const DOC_LINKS = [
  { href: "/docs/introduction", label: "Introduction" },
  { href: "/docs/authentication", label: "Authentication" },
  { href: "/docs/endpoints", label: "Endpoints" },
  { href: "/docs/openai-to-seekapi-migration", label: "Migration (30s)" },
  { href: "/docs/latency-benchmarks", label: "Latency Benchmarks" },
  { href: "/docs/token-saving-strategy", label: "Token Saving Strategy" },
  { href: "/docs/api-status-codes", label: "API Status Codes" },
  { href: "/docs/pricing-calculator-logic", label: "Pricing Calculator Logic" },
  { href: "/docs/reliability-playbook", label: "Reliability Playbook" },
];

export const metadata: Metadata = {
  title: "Developer Docs | SeekAPI.ai",
  description:
    "Authentication, endpoint references, migration guides, and operational best practices.",
  keywords: ["SeekAPI docs", "OpenAI-compatible docs", "DeepSeek API integration"],
};

export default function DocsLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container docs-shell">
          <aside className="docs-sidebar">
            <p className="hero-eyebrow">Documentation</p>
            <nav className="docs-nav">
              {DOC_LINKS.map((link) => (
                <a key={link.href} href={link.href} className="docs-nav-link">
                  {link.label}
                </a>
              ))}
            </nav>
          </aside>
          <section className="docs-content">{children}</section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
