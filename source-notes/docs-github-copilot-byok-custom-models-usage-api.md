---
source_url: https://github.blog/changelog/2026-11-03-byok-and-enterprise-custom-models-in-the-copilot-usage-api
source_type: docs
title: "BYOK and enterprise custom models in the Copilot usage API"
author: GitHub (official changelog)
date_published: 2026-11-03
date_extracted: 2026-11-04
last_checked: 2026-11-04
status: current
confidence_overall: settled
issue: "#4512"
---

# BYOK and Enterprise Custom Models in the Copilot Usage API (GitHub Changelog, Nov 3, 2026)

> The Copilot usage metrics API now separates local BYOK and enterprise custom-model traffic from Copilot-hosted usage, with explicit field names and explicit undercount caveats for the client-telemetry-based half.

## Source Context

- **Type**: docs (GitHub official product changelog, ~3 minute read)
- **Author credibility**: GitHub, the API owner. Authoritative for the schema and stated limitations; says nothing about whether BYOK improves outcomes.
- **Scope**: New fields for local BYOK (`used_local_byok`, `totals_by_local_byok`, active-user counts) and the `is_custom_enterprise_model` flag, plus caveats (lower bound, name normalization, no backfill, access). Does not cover pricing/billing of BYOK, field-level numeric examples, or how to enable BYOK.

## Extracted Claims

### Claim 1: Two distinct BYOK categories are now separated from Copilot-hosted usage: developer-configured local BYOK and admin-configured enterprise custom models
- **Evidence**: Schema description in the changelog.
- **Confidence**: settled
- **Quote**: "Local BYOK is configured by developers in their client."
- **Our assessment**: The split matters because the data path differs (direct to provider vs. routed through GitHub), which drives the different measurement reliability in Claims 4 and 5.

### Claim 2: Local BYOK is exposed via a per-user boolean, a breakdown by kind and surface, and distinct-user counts
- **Evidence**: Field list: `used_local_byok` (user-level reports), `totals_by_local_byok` with `byok_kind` (`local_managed`, `local_user`, `local_auto`, `remote_user`) and `surface` (`copilot_cli`, `copilot_app`), and `daily_active_local_byok_users` / `weekly_…` / `monthly_…` (aggregate reports).
- **Confidence**: settled
- **Quote**: "Session, request, prompt, and token counts, broken out by"
- **Our assessment**: Gives admins a concrete way to see who bypasses Copilot-hosted models. Surfaces are limited to CLI and the Copilot app; IDE local BYOK is not covered by these fields.

### Claim 3: Enterprise custom models are flagged by a boolean on each per-client model entry, and a model used both ways appears as two entries
- **Evidence**: Field `is_custom_enterprise_model` on `totals_by_client[].totals_by_model[]`.
- **Confidence**: settled
- **Quote**: "A model used both as a Copilot-hosted model and as a custom model appears as two entries, so the counts stay separate."
- **Our assessment**: Consumers aggregating by model name must now group by (name, flag) or they will double-count or misread rows.

### Claim 4: Local BYOK data is a lower bound because it depends on client telemetry and provider token reporting
- **Evidence**: "Important notes" section.
- **Confidence**: settled
- **Quote**: "Local BYOK fields rely on client telemetry, so they undercount when telemetry is disabled."
- **Our assessment**: Same structural weakness GitHub acknowledged for client telemetry generally (see server-side telemetry note). Governance use ("who is using BYOK") can produce false negatives; absence of a flag is not proof of non-use.

### Claim 5: Enterprise custom-model counts are observed server-side and cover every client including IDEs
- **Evidence**: Schema notes and "Lower bound" caveat.
- **Confidence**: settled
- **Quote**: "GitHub observes these requests server-side, so the field covers every client, including IDEs."
- **Our assessment**: Admin-configured routing gives a reliable audit trail; developer-configured BYOK does not. Argues for admin-managed custom models when auditability matters.

### Claim 6: Existing totals do not change; BYOK was already counted and the new fields are a subset breakdown
- **Evidence**: "No change to existing totals" note.
- **Confidence**: settled
- **Quote**: "Local BYOK is a subset of totals_by_cli and totals_by_copilot_app, and custom model usage is already in totals_by_client."
- **Our assessment**: Historical dashboards stay valid, but they have always blended BYOK into "Copilot" numbers, so per-user efficiency comparisons before this release were contaminated.

### Claim 7: Custom model names follow existing normalization so unrecognized names show as `unknown`; local BYOK has no model-name breakdown
- **Evidence**: "Model names" note.
- **Confidence**: settled
- **Quote**: "Custom model names use the existing model name normalization, so unrecognized names appear as unknown."
- **Our assessment**: Limits per-model analysis of custom models; the flag and counts are reliable but identity may not be.

### Claim 8: No backfill; the custom-model flag is absent for days before release
- **Evidence**: "No backfill" note.
- **Confidence**: settled
- **Quote**: "Report days before this release don’t include is_custom_enterprise_model."
- **Our assessment**: Trend lines across the 2026-11-03 boundary will show a step; treat pre-release custom-model share as unknown, not zero.

### Claim 9: GitHub frames the value as governance, spend understanding, cross-tool visibility, and efficiency comparison
- **Evidence**: "Why this matters" section; vendor framing, no outcome data.
- **Confidence**: emerging
- **Quote**: "BYOK usage used to blend into Copilot-hosted totals, because local and custom models often share names with Copilot models."
- **Our assessment**: The diagnosis (name collisions blending data) is credible. The benefits are plausible but unevidenced; this is measurement, not proof that BYOK improves outcomes.

### Claim 10: Access requires specific roles and the usage metrics policy
- **Evidence**: "Access" note.
- **Confidence**: settled
- **Quote**: "The Copilot usage metrics policy must be enabled."
- **Our assessment**: Roles: enterprise owners, billing managers, org owners, or custom role with `View Copilot Metrics`.

## Concrete Artifacts

```
# Source: GitHub changelog 2026-11-03 (field names verbatim)
used_local_byok                                  # user-level, boolean per day
totals_by_local_byok                             # session/request/prompt/token counts
  byok_kind: local_managed | local_user | local_auto | remote_user
  surface:   copilot_cli | copilot_app
daily_active_local_byok_users
weekly_active_local_byok_users
monthly_active_local_byok_users                  # aggregate reports
totals_by_client[].totals_by_model[].is_custom_enterprise_model   # boolean
# Available in enterprise and organization reports, user and aggregate level, 1-day and 28-day.
# Local BYOK providers named: Ollama, Foundry Local, LM Studio, llama-server.
```

## Cross-References

- **Corroborates**: `docs-github-copilot-usage-metrics-server-side-telemetry.md` Claim 1 (client telemetry can fail to reach GitHub) — the local BYOK undercount is the same failure mode; Claim 2 there (server-side supplement) parallels the server-side observability of custom models here.
- **Contradicts**: none found.
- **Extends**: `docs-github-copilot-byok-app.md` (Claims 1–2, BYOK in the Copilot app; this adds the measurement side); `docs-github-copilot-app-usage-metrics-report-rollups.md` (Claims 3–4, `used_copilot_app` / `totals_by_copilot_app`, of which local BYOK is a subset); `docs-github-copilot-cli-activity-usage-metrics.md` (Claim 5, `totals_by_cli`).
- **Novel**: BYOK-vs-hosted separation fields, `byok_kind` taxonomy, `is_custom_enterprise_model`, and the asymmetry in measurement reliability between developer-configured and admin-configured models.

## Guide Impact

- **Chapter 05**: In the usage-metrics governance material, add that per-user Copilot efficiency metrics before 2026-11-03 blended BYOK and custom-model traffic, and that local BYOK fields are lower bounds (telemetry-dependent) while custom-model flags are server-side. Cite this note.
- **Chapter 02**: Optionally note that BYOK/local-model routing is now observable at org level, with the caveat that observation is reliable only for admin-configured models.

## Extraction Notes

- Read the full changelog page (fetched raw HTML and stripped tags to obtain verbatim text; quotes are copied from it). Linked API docs page was not followed.
- Triage comments requested the caveats and field families; all are covered. No contradictions found, so no contradiction issue was filed.
