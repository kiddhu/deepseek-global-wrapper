import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export default function DocsPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <main className="page-content">
        <div className="container">
          <p className="hero-eyebrow">DEVELOPER DOCS</p>
          <h1 className="hero-title">API Quickstart</h1>
          <p className="hero-subtitle">
            Use your SeekAPI key with a standard bearer token header and an OpenAI-compatible
            endpoint.
          </p>

          <section className="card-grid" aria-label="API guide">
            <article className="card">
              <h2 className="card-title">Endpoint</h2>
              <p className="card-body">POST https://api.seekapi.ai/v1/chat/completions</p>
            </article>
            <article className="card">
              <h2 className="card-title">Auth Header</h2>
              <p className="card-body">Authorization: Bearer YOUR_API_KEY</p>
            </article>
            <article className="card">
              <h2 className="card-title">Model Example</h2>
              <p className="card-body">deepseek-r1</p>
            </article>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
