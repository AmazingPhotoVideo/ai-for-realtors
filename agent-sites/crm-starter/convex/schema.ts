import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";
export const status = v.union(v.literal("new"),v.literal("attempted"),v.literal("connected"),v.literal("appointment"),v.literal("active"),v.literal("closed"),v.literal("nurture"),v.literal("lost"));
export const intent = v.union(v.literal("buy"),v.literal("sell"),v.literal("valuation"),v.literal("relocate"),v.literal("invest"),v.literal("other"));
export default defineSchema({ leads: defineTable({
 name:v.string(),email:v.string(),phone:v.optional(v.string()),source:v.string(),intent,status,message:v.optional(v.string()),markets:v.array(v.string()),assignedTo:v.optional(v.string()),nextFollowUpAt:v.optional(v.number()),
 estimatedTransactionValue:v.optional(v.number()),estimatedCommission:v.optional(v.number()),currency:v.optional(v.string()),
 consent:v.object({contactAllowed:v.boolean(),marketingAllowed:v.boolean(),channel:v.string(),textVersion:v.string(),capturedAt:v.number(),ip:v.optional(v.string()),userAgent:v.optional(v.string())}),
 activity:v.array(v.object({kind:v.union(v.literal("note"),v.literal("call"),v.literal("email"),v.literal("sms"),v.literal("meeting"),v.literal("status")),text:v.string(),at:v.number(),by:v.string()})),createdAt:v.number(),updatedAt:v.number()
}).index("by_created",["createdAt"]).index("by_status",["status"]).index("by_follow_up",["nextFollowUpAt"]) });
