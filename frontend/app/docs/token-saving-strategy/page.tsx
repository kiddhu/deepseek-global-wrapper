export default function TokenSavingStrategyPage() {
  return (
    <div>
      <p className="hero-eyebrow">COST ENGINEERING</p>
      <h1 className="hero-title">Token Saving Strategy with DeepSeek R1</h1>
      <p className="hero-subtitle">
        Practical patterns to reduce inference spend by up to 90% without hurting output quality.
      </p>

      <ul className="card-body" style={{ lineHeight: 1.9 }}>
        <li>Trim system prompts and deduplicate context sections before each call.</li>
        <li>
          Use staged prompting: classify first, then route only expensive tasks to long-chain mode.
        </li>
        <li>Apply response length guards with max token ceilings per endpoint.</li>
        <li>Cache deterministic prompts and replay stable outputs from edge storage.</li>
        <li>Batch low-priority jobs to off-peak windows with lower arbitration rates.</li>
      </ul>
    </div>
  );
}
