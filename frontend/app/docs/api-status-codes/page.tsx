export default function ApiStatusCodesPage() {
  return (
    <div>
      <p className="hero-eyebrow">OPERATIONS</p>
      <h1 className="hero-title">API Status Codes and Error Handling</h1>
      <p className="hero-subtitle">
        Use these standard responses to build reliable retry and alert logic.
      </p>

      <table className="compare-table">
        <thead>
          <tr>
            <th>Status</th>
            <th>Meaning</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>200</td>
            <td>Request successful</td>
            <td>Parse output and continue.</td>
          </tr>
          <tr>
            <td>401</td>
            <td>Invalid or missing API key</td>
            <td>Rotate key and verify auth header format.</td>
          </tr>
          <tr>
            <td>429</td>
            <td>Rate limit reached</td>
            <td>Apply exponential backoff and token bucket control.</td>
          </tr>
          <tr>
            <td>500</td>
            <td>Upstream execution failure</td>
            <td>Retry with jitter and trigger incident logging.</td>
          </tr>
          <tr>
            <td>503</td>
            <td>Temporary lane congestion</td>
            <td>Fail over to alternate route group.</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
