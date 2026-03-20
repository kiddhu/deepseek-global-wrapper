export default function DocsAuthenticationPage() {
  return (
    <div>
      <p className="hero-eyebrow">AUTHENTICATION</p>
      <h1 className="hero-title">Use API Keys with Bearer Auth</h1>
      <p className="hero-subtitle">
        Generate a key in dashboard, then pass it in standard Authorization header.
      </p>
      <div className="card">
        <h2 className="card-title">Header</h2>
        <pre className="code-area">
          <code>Authorization: Bearer YOUR_API_KEY</code>
        </pre>
      </div>
    </div>
  );
}
