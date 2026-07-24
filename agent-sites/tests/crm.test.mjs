import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const leads = await readFile(new URL("../crm-starter/convex/leads.ts", import.meta.url), "utf8");
const schema = await readFile(new URL("../crm-starter/convex/schema.ts", import.meta.url), "utf8");
const dashboard = await readFile(new URL("../crm-starter/dashboard/LeadDashboard.tsx", import.meta.url), "utf8");

test("CRM models Realtor lead workflow and internal estimates", () => {
  for (const field of ["source", "intent", "status", "nextFollowUpAt", "estimatedTransactionValue", "estimatedCommission", "consent", "activity"]) {
    assert.match(schema, new RegExp(field));
  }
});

test("CRM enforces admin reads and writes and timestamps consent server-side", () => {
  assert.match(leads, /requireAdmin\(ctx\)/);
  assert.match(leads, /allowlist\.includes\(email\)/);
  assert.match(leads, /consent: \{/);
  assert.match(leads, /capturedAt: now/);
  assert.doesNotMatch(leads, /capturedAt: v\.number\(\)/);
});

test("public lead submission validates email and bounds user-controlled text", () => {
  assert.match(leads, /cleanEmail\(args\.email\)/);
  assert.match(leads, /args\.markets\.length > 20/);
  assert.match(leads, /cleanOptional\(args\.message, "Message", 5000\)/);
  assert.match(leads, /cleanText\(args\.consent\.textVersion, "Consent text version", 500\)/);
});

test("CRM supports useful filters, notes, and formula-safe filtered CSV export", () => {
  for (const filter of ["search", "source", "status", "intent", "followUpBefore"]) assert.match(leads, new RegExp(filter));
  assert.match(leads, /addActivity/);
  assert.match(dashboard, /Export filtered CSV/);
  assert.match(dashboard, /\^\[=\+\\-@\\t\\r\]/);
});