export default function ReliabilityPlaybookPage() {
  return (
    <div>
      <p className="hero-eyebrow">RELIABILITY</p>
      <h1 className="hero-title">Reliability Playbook for Production Teams</h1>
      <p className="hero-subtitle">
        Operational defaults that keep latency predictable and spend under control at scale.
      </p>

      <ol className="card-body" style={{ lineHeight: 1.9 }}>
        <li>Instrument every call with request IDs and model tags for traceability.</li>
        <li>Define SLOs for P95 latency and error budgets per product surface.</li>
        <li>Run canary traffic on new routes before shifting production mix.</li>
        <li>Maintain circuit breakers with bounded retries and jittered backoff.</li>
        <li>Review weekly cost variance against token throughput anomalies.</li>
      </ol>
    </div>
  );
}
