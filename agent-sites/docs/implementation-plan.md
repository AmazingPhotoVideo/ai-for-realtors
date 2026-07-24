# Realtor Site + CRM Builder Implementation Plan

**Goal:** Deliver a deterministic, configuration-driven Realtor marketing site with three presets and an optional authenticated lightweight CRM.

**Architecture:** A static-exportable Next.js site reads one schema-validated JSON config. Preset routes reuse semantic content while CSS data selectors create distinct visual systems. A credential-free demo form is separated from an optional concrete Convex + Clerk CRM implementation.

**Tasks:** (1) define schema and fictional config; (2) implement semantic sections and three responsive visual presets; (3) model/admin-gate Realtor leads and activity; (4) document board/feed and consent boundaries; (5) add deterministic validation/render tests; (6) install, test, build, inspect output, and commit.
