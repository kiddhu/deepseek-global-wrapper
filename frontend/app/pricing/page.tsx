import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";
import { PricingBody } from "./pricing-body";

export const metadata: Metadata = {
  title: "Pricing | SeekAPI.ai",
  description:
    "Compute bank: Explorer free tier, Growth $20/mo with 80M tokens and 2-month rollover, Scale $99/mo with 400M and 3-month rollover. Credit Boosters for instant top-ups. OpenAI-compatible gateway.",
  keywords: [
    "SeekAPI pricing",
    "DeepSeek API pricing",
    "LLM subscription tokens",
    "compute bank",
    "API free credit",
    "money back guarantee",
  ],
};

export default function PricingPage() {
  return (
    <div className="page-shell">
      <SiteHeader />
      <PricingBody />
      <SiteFooter />
    </div>
  );
}
