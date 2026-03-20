import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

const DOC_LINKS = [
  { href: "/docs/introduction", label: "Introduction" },
  { href: "/docs/authentication", label: "Authentication" },
  { href: "/docs/endpoints", label: "Endpoints" },
];

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
