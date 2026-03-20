import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "SeekAPI.ai — DeepSeek Global Wrapper",
  description: "跨境算力套利与 AI 自动化内容矩阵，一站式接入 DeepSeek 能力。",
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
