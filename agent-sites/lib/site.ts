import config from "@/config/site.config.json";
export const PRESETS = ["luxury-editorial", "neighbourhood-journal", "modern-team"] as const;
export type Preset = (typeof PRESETS)[number];
export type Testimonial = { quote: string; attribution: string; verified: true };
export type Stat = { label: string; value: string; verified: true };
export type SiteConfig = Omit<typeof config, "preset" | "testimonials" | "stats"> & { preset: Preset; testimonials: Testimonial[]; stats: Stat[] };
export const site = config as SiteConfig;
export function isPreset(value: string): value is Preset { return PRESETS.includes(value as Preset); }
