import { mutation, query } from "./_generated/server";
import { v } from "convex/values";
import { intent, status } from "./schema";
import config from "../../config/site.config.json";

function cleanText(value: string, label: string, maxLength: number) {
  const cleaned = value.trim();
  if (!cleaned) throw new Error(`${label} is required`);
  if (cleaned.length > maxLength) throw new Error(`${label} is too long`);
  return cleaned;
}

function cleanOptional(value: string | undefined, label: string, maxLength: number) {
  if (value === undefined) return undefined;
  const cleaned = value.trim();
  if (cleaned.length > maxLength) throw new Error(`${label} is too long`);
  return cleaned || undefined;
}

function cleanEmail(value: string) {
  const email = cleanText(value, "Email", 254).toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) throw new Error("A valid email is required");
  return email;
}

async function requireAdmin(ctx: { auth: { getUserIdentity: () => Promise<any> } }) {
  const user = await ctx.auth.getUserIdentity();
  const email = String(user?.email ?? "").trim().toLowerCase();
  const allowlist = config.admins.map((value) => value.trim().toLowerCase());
  if (!user || !email || !allowlist.includes(email)) throw new Error("Admin access required");
  return email;
}

export const submit = mutation({
  args: {
    name: v.string(),
    email: v.string(),
    phone: v.optional(v.string()),
    source: v.string(),
    intent,
    message: v.optional(v.string()),
    markets: v.array(v.string()),
    consent: v.object({
      contactAllowed: v.boolean(),
      marketingAllowed: v.boolean(),
      channel: v.string(),
      textVersion: v.string(),
    }),
  },
  handler: async (ctx, args) => {
    if (!args.consent.contactAllowed) throw new Error("Contact consent required");
    if (args.markets.length > 20) throw new Error("Too many markets");
    const now = Date.now();
    return ctx.db.insert("leads", {
      ...args,
      name: cleanText(args.name, "Name", 120),
      email: cleanEmail(args.email),
      phone: cleanOptional(args.phone, "Phone", 50),
      source: cleanText(args.source, "Source", 120),
      message: cleanOptional(args.message, "Message", 5000),
      markets: args.markets.map((market) => cleanText(market, "Market", 120)),
      consent: {
        ...args.consent,
        channel: cleanText(args.consent.channel, "Consent channel", 80),
        textVersion: cleanText(args.consent.textVersion, "Consent text version", 500),
        capturedAt: now,
      },
      status: "new",
      activity: [],
      createdAt: now,
      updatedAt: now,
    });
  },
});

export const list = query({
  args: {
    search: v.optional(v.string()),
    source: v.optional(v.string()),
    status: v.optional(status),
    intent: v.optional(intent),
    followUpBefore: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    await requireAdmin(ctx);
    let rows = await ctx.db.query("leads").withIndex("by_created").order("desc").collect();
    if (args.source) rows = rows.filter((lead) => lead.source.toLowerCase() === args.source!.toLowerCase());
    if (args.status) rows = rows.filter((lead) => lead.status === args.status);
    if (args.intent) rows = rows.filter((lead) => lead.intent === args.intent);
    if (args.followUpBefore) rows = rows.filter((lead) => !!lead.nextFollowUpAt && lead.nextFollowUpAt <= args.followUpBefore!);
    if (args.search) {
      const term = args.search.toLowerCase();
      rows = rows.filter((lead) =>
        [lead.name, lead.email, lead.phone ?? "", lead.source, lead.intent, ...lead.markets]
          .join(" ")
          .toLowerCase()
          .includes(term),
      );
    }
    return rows;
  },
});

export const update = mutation({
  args: {
    id: v.id("leads"),
    status: v.optional(status),
    nextFollowUpAt: v.optional(v.number()),
    estimatedTransactionValue: v.optional(v.number()),
    estimatedCommission: v.optional(v.number()),
    currency: v.optional(v.string()),
    assignedTo: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const by = await requireAdmin(ctx);
    const { id, ...changes } = args;
    const lead = await ctx.db.get(id);
    if (!lead) throw new Error("Lead not found");
    const activity =
      changes.status && changes.status !== lead.status
        ? [...lead.activity, { kind: "status" as const, text: `Status: ${lead.status} → ${changes.status}`, at: Date.now(), by }]
        : lead.activity;
    await ctx.db.patch(id, { ...changes, activity, updatedAt: Date.now() });
  },
});

export const addActivity = mutation({
  args: {
    id: v.id("leads"),
    kind: v.union(v.literal("note"), v.literal("call"), v.literal("email"), v.literal("sms"), v.literal("meeting")),
    text: v.string(),
  },
  handler: async (ctx, args) => {
    const by = await requireAdmin(ctx);
    const lead = await ctx.db.get(args.id);
    if (!lead) throw new Error("Lead not found");
    const text = args.text.trim();
    if (!text) throw new Error("Activity text is required");
    await ctx.db.patch(args.id, {
      activity: [...lead.activity, { kind: args.kind, text, at: Date.now(), by }],
      updatedAt: Date.now(),
    });
  },
});
