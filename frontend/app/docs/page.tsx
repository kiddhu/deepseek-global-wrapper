export default function DocsPage() {
  return (
    <div className="page-shell">
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
              <p className="card-body">POST https://dash.seekapi.ai/v1/chat/completions</p>
            </article>
            <article className="card">
              <h2 className="card-title">Auth Header</h2>
              <p className="card-body">Authorization: Bearer YOUR_API_KEY</p>
            </article>
            <article className="card">
              <h2 className="card-title">Python Integration</h2>
              <p className="card-body">
                <code>
                  import openai
                  <br />
                  client = openai.OpenAI(api_key=&quot;YOUR_API_KEY&quot;)
                  <br />
                  client.base_url = &quot;https://dash.seekapi.ai/v1&quot;
                  <br /># Authorization: Bearer YOUR_API_KEY
                </code>
              </p>
            </article>
          </section>
        </div>
      </main>
      <footer className="footer">
        <div className="footer-inner">
          <span className="footer-brand">
            Room P11, Flat 2C, 2/F, Hung To Ctr., 94-96 How Ming St., Kwun Tong, Kowloon, HK
          </span>
          <span className="footer-meta">support@seekapi.ai</span>
          <span className="footer-meta">© 2026 SeekAPI.ai | AION: The Era of the One.</span>
        </div>
      </footer>
    </div>
  );
}
