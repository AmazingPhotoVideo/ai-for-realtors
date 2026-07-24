import { notFound } from "next/navigation";
import { Site } from "@/components/Site";
import { isPreset, PRESETS } from "@/lib/site";
export function generateStaticParams() { return PRESETS.map((preset) => ({ preset })); }
export default async function PresetPage({ params }: { params: Promise<{ preset: string }> }) {
  const { preset } = await params; if (!isPreset(preset)) notFound(); return <Site preset={preset} />;
}
