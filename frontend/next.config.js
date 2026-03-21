const path = require("path");

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Monorepo: parent repo has its own lockfile; align tracing with repo root for Vercel.
  outputFileTracingRoot: path.join(__dirname, ".."),
};

module.exports = nextConfig;
