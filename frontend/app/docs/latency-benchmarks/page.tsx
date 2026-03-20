export default function LatencyBenchmarksPage() {
  return (
    <div>
      <p className="hero-eyebrow">PERFORMANCE REPORT</p>
      <h1 className="hero-title">Latency Benchmarks: HK vs Global Nodes</h1>
      <p className="hero-subtitle">
        Representative request timings for comparable payloads under production-like load.
      </p>

      <table className="compare-table">
        <thead>
          <tr>
            <th>Region Pair</th>
            <th>P50</th>
            <th>P95</th>
            <th>Stability</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>OpenAI US-East</td>
            <td>137ms</td>
            <td>312ms</td>
            <td>Baseline</td>
          </tr>
          <tr>
            <td>SeekAPI HK Hub</td>
            <td>82ms</td>
            <td>191ms</td>
            <td>High</td>
          </tr>
          <tr>
            <td>SeekAPI Global Lane</td>
            <td>94ms</td>
            <td>208ms</td>
            <td>High</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
