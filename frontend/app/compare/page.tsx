export default function ComparePage() {
  return (
    <div className="page-shell">
      <main className="page-content">
        <div className="container">
          <header>
            <p className="hero-eyebrow">COMPARE</p>
            <h1 className="hero-title">SeekAPI vs OpenAI</h1>
            <p className="hero-subtitle">
              Same OpenAI-compatible API shape, lower token cost, and routing optimized for global
              teams.
            </p>
          </header>

          <section aria-label="Feature comparison">
            <table className="compare-table">
              <caption className="sr-only">SeekAPI and OpenAI feature comparison</caption>
              <thead>
                <tr>
                  <th scope="col">Dimension</th>
                  <th scope="col">SeekAPI.ai</th>
                  <th scope="col">OpenAI Direct</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">Compatibility</th>
                  <td>100% OpenAI-style request format</td>
                  <td>Native</td>
                </tr>
                <tr>
                  <th scope="row">Typical Cost</th>
                  <td>10%-15% of comparable baseline spend</td>
                  <td>Baseline market pricing</td>
                </tr>
                <tr>
                  <th scope="row">Migration Effort</th>
                  <td>Change only `base_url`</td>
                  <td>Not applicable</td>
                </tr>
                <tr>
                  <th scope="row">High Concurrency</th>
                  <td>Enterprise routing and dedicated lanes</td>
                  <td>Depends on plan and account tier</td>
                </tr>
                <tr>
                  <th scope="row">Refund Policy</th>
                  <td>7-Day Money Back Guarantee (unused balance)</td>
                  <td>Varies by provider policy</td>
                </tr>
              </tbody>
            </table>
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
