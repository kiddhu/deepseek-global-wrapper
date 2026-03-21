import type { Metadata } from "next";
import { SiteFooter } from "../components/site-footer";
import { SiteHeader } from "../components/site-header";
import { PricingBody } from "./pricing-body";

export const metadata: Metadata = {
  title: "Pricing | SeekAPI.ai",
  description:
    "Free $0.50 credit, pay-as-you-go at $0.20/1M tokens, or Professional at $29/mo with VIP routing and SLA. OpenAI-compatible DeepSeek gateway.",
  keywords: [
    "SeekAPI pricing",
    "DeepSeek API pricing",
    "pay as you go LLM",
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
