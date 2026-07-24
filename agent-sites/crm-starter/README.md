# Optional CRM: Next.js + Convex + Clerk

Concrete integration files for the marketing starter. This directory is excluded from the credential-free website build because Convex generates `_generated/*` only after project configuration.

## Enable only with owner approval

1. Create separate development projects in Convex and Clerk (these external actions may be billable; obtain approval first).
2. Copy `convex/` into `agent-sites/convex/` and `dashboard/LeadDashboard.tsx` into `components/`.
3. Configure Clerk middleware/provider following the current official Clerk + Convex integration docs; never paste secrets into source.
4. Set Clerk's Convex JWT template and the four values shown in `.env.example`.
5. Run `npx convex dev` to generate `_generated/*`, then mount `LeadDashboard` at an authenticated `/admin` route.
6. Submit the public form to `api.leads.submit` only after the privacy/consent review.
7. Verify: non-admin rejected, admin can search and filter by source/intent/status/follow-up, edit/follow up/export, CSV data escapes spreadsheet formulas, consent timestamps persist, and public users cannot list records.

`site.config.json#admins` is the allowlist. The query/mutations enforce it server-side; hiding the page alone is not authorization.

## Data notes

- `estimatedTransactionValue` and `estimatedCommission` are rough **internal planning estimates**, not promises, valuations, invoices, or client-facing figures.
- Store commission as entered; do not infer a standard rate.
- Activity is append-only. The public mutation records purpose, channel, text/version, and a server-generated capture timestamp. Only extend it with IP/user-agent data through a reviewed trusted server route; never trust those values from the browser.
- CSV export begins with a UTF-8 BOM and neutralizes cells starting with `=`, `+`, `-`, `@`, tab, or carriage return.
- Define retention/deletion rules with the brokerage. Export is not a backup strategy.
- No Stripe dependency is included.
