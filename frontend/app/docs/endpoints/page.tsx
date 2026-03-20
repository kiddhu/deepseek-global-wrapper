export default function DocsEndpointsPage() {
  return (
    <div>
      <p className="hero-eyebrow">ENDPOINTS</p>
      <h1 className="hero-title">Model Interface Reference</h1>
      <p className="hero-subtitle">Base URL: https://api.seekapi.ai/v1</p>
      <div className="card">
        <h2 className="card-title">Chat Completions</h2>
        <pre className="code-area">
          <code>{`POST /chat/completions
Model: deepseek-r1
Model: deepseek-v3`}</code>
        </pre>
      </div>
    </div>
  );
}
