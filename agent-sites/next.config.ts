import type { NextConfig } from "next";
const nextConfig: NextConfig = { output: "export", trailingSlash: true, outputFileTracingRoot: process.cwd(), images: { unoptimized: true } };
export default nextConfig;
