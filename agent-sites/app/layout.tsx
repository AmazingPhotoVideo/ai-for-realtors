import type { Metadata } from "next";
import "./globals.css";
import { site } from "@/lib/site";
export const metadata: Metadata = { title: site.seo.title, description: site.seo.description, metadataBase: new URL(site.seo.siteUrl) };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  const style = { "--primary": site.brand.primary, "--accent": site.brand.accent, "--paper": site.brand.paper, "--ink": site.brand.ink, "--display": site.brand.displayFont, "--body": site.brand.bodyFont } as React.CSSProperties;
  return <html lang="en"><body style={style}>{children}</body></html>;
}
