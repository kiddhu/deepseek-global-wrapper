import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "SeekAPI.ai | Save 90% on AI API Costs",
  description:
    "OpenAI-compatible gateway for DeepSeek R1/V3 with global routing, transparent pricing, and a 30-second migration path.",
  keywords: [
    "SeekAPI",
    "DeepSeek gateway",
    "OpenAI compatible API",
    "AI API cost reduction",
    "global inference routing",
  ],
};

export default function MarketingLayout({ children }: { children: React.ReactNode }) {
  return children;
}
