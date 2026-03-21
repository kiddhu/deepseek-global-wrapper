import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export const metadata: Metadata = {
  title: "About | SeekAPI.ai",
  description:
    "SeekAPI Technology Limited operates SeekAPI.ai, an OpenAI-compatible gateway for DeepSeek and global inference routing.",
  keywords: ["SeekAPI Technology Limited", "about SeekAPI", "DeepSeek gateway company"],
};

export default function AboutPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">ABOUT</p>
          <h1 className="hero-title">SeekAPI Technology Limited</h1>
          <p className="hero-subtitle">
            We build infrastructure that makes world-class reasoning models accessible through a
            secure, OpenAI-compatible API—so teams can ship faster without re-architecting their
            stack.
          </p>
          <section className="card" style={{ maxWidth: "42rem", padding: "1.5rem 1.4rem" }}>
            <h2 className="card-title">Company</h2>
            <p className="card-body">
              <strong>SeekAPI Technology Limited</strong> is the operator of SeekAPI.ai and related
              developer services (including the customer console at dash.seekapi.ai). We are
              incorporated in Hong Kong and serve global engineering teams.
            </p>
            <h2 className="card-title" style={{ marginTop: "1.25rem" }}>
              Contact
            </h2>
            <p className="card-body">
              <a href="mailto:support@seekapi.ai" className="footer-link-min">
                support@seekapi.ai
              </a>
            </p>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
