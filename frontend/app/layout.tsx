import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "SeekAPI.ai | Global DeepSeek Cost Gateway",
  description:
    "SeekAPI.ai is an OpenAI-compatible gateway for DeepSeek R1/V3 with global routing and lower inference cost.",
  keywords: [
    "SeekAPI",
    "DeepSeek R1",
    "DeepSeek V3",
    "OpenAI compatible API",
    "AI API cost reduction",
    "global inference gateway",
  ],
  icons: {
    icon: "/icon.svg",
    shortcut: "/icon.svg",
    apple: "/icon.svg",
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="bg-white text-neutral-900">{children}</body>
    </html>
  );
}
