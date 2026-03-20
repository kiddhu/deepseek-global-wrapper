import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";

export default function ComparePage() {
  return (
    <div className="page-shell">
      <SiteHeader />
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
                <tr>
                  <th scope="row">Payment Flexibility</th>
                  <td>Crypto (USDT), Global Cards, No Phone-binding.</td>
                  <td>Strict KYC, Limited Regions, High Ban Risk.</td>
                </tr>
              </tbody>
            </table>
          </section>
        </div>
      </main>
      <SiteFooter />
    </div>
  );
}
