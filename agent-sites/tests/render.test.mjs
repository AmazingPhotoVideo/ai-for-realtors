import test from "node:test"; import assert from "node:assert/strict"; import { readFile } from "node:fs/promises";
const css=await readFile(new URL("../app/globals.css",import.meta.url),"utf8"); const site=await readFile(new URL("../components/Site.tsx",import.meta.url),"utf8");
test("three distinct visual presets have render selectors",()=>{ for(const p of ["luxury-editorial","neighbourhood-journal","modern-team"]) assert.match(css,new RegExp(`data-preset=${p}`)); });
test("required public sections and truthful APV media CTAs render",()=>{ for(const id of ["listings","about","services","neighbourhoods","contact"]) assert.match(site,new RegExp(`id=\"${id}\"`)); assert.match(site,/Show the property at its best/); assert.match(site,/Plan the right media mix/); assert.doesNotMatch(site,/SEO|website support/i); assert.match(site,/footerLabel/); });
test("accessibility motion and form affordances exist",()=>{ assert.match(css,/prefers-reduced-motion/); assert.match(site,/Skip to content/); });
test("mobile presets collapse to one column without clipped preset navigation",()=>{ assert.match(css,/grid-template-columns:minmax\(0,1fr\)!important/); assert.match(css,/\.preset-switcher\{[^}]*flex-wrap:wrap/); });
test("required APV links are normal followed attribution links",()=>{ assert.doesNotMatch(site,/rel=\"(?:nofollow|sponsored)\"/); });
