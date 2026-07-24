import test from "node:test"; import assert from "node:assert/strict"; import { readFile } from "node:fs/promises";
const root = new URL("../", import.meta.url); const config = JSON.parse(await readFile(new URL("config/site.config.json", root)));
test("only verified testimonials and stats can be published", () => { assert.ok(config.testimonials.every(x=>x.verified===true)); assert.ok(config.stats.every(x=>x.verified===true)); });
test("featured listings are explicitly manual", () => { assert.ok(config.featuredListings.length>=2); assert.ok(config.featuredListings.every(x=>x.manual===true)); });
test("all presets and required APV links are configured", () => { assert.ok(["luxury-editorial","neighbourhood-journal","modern-team"].includes(config.preset)); assert.equal(config.apv.mediaConsultationUrl,"https://amazingphotovideo.com"); assert.equal(config.apv.mediaPlanningUrl,"https://amazingphotovideo.com"); });
test("consent and admin configuration are present", () => { assert.match(config.consent.disclaimer,/not a live MLS|not.*MLS/i); assert.ok(config.admins.length); assert.ok(config.consent.requiredLabel.length>20); });
