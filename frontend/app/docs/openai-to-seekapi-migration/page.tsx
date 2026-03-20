export default function OpenaiToSeekapiMigrationPage() {
  return (
    <div>
      <p className="hero-eyebrow">MIGRATION GUIDE</p>
      <h1 className="hero-title">OpenAI to SeekAPI in 30 Seconds</h1>
      <p className="hero-subtitle">
        Keep your existing SDK integration and swap only the API gateway endpoint.
      </p>

      <pre className="code-block">
        <code>{`from openai import OpenAI

client = OpenAI(
  api_key="YOUR_SEEKAPI_KEY",
  base_url="https://api.seekapi.ai/v1",
)

resp = client.chat.completions.create(
  model="deepseek-r1",
  messages=[{"role": "user", "content": "Hello"}],
)`}</code>
      </pre>

      <p className="card-body">
        Migration checklist: rotate key, update base URL, validate model name, and ship.
      </p>
    </div>
  );
}
