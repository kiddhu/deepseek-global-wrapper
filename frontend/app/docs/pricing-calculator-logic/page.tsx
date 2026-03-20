export default function PricingCalculatorLogicPage() {
  return (
    <div>
      <p className="hero-eyebrow">PRICING ENGINE</p>
      <h1 className="hero-title">Pricing Calculator Logic</h1>
      <p className="hero-subtitle">
        Transparent arbitrage pricing by input/output token usage and route tier selection.
      </p>

      <pre className="code-block">
        <code>{`monthly_cost = (input_tokens / 1_000_000) * input_rate
             + (output_tokens / 1_000_000) * output_rate
             + route_multiplier

savings_ratio = 1 - (seekapi_cost / baseline_cost)`}</code>
      </pre>

      <p className="card-body">
        SeekAPI exposes rate assumptions, route multipliers, and billing boundaries so finance and
        engineering can audit costs in the same model.
      </p>
    </div>
  );
}
