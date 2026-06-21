---
source_url: https://github.blog/changelog/2026-04-10-copilot-cli-activity-now-included-in-usage-metrics-totals-and-feature-breakdowns
source_type: docs
title: "Copilot CLI activity now included in usage metrics totals and feature breakdowns"
author: GitHub (official changelog)
date_published: 2026-04-10
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: settled
issue: "#129"
---

# Copilot CLI Activity Integrated into Usage Metrics Totals and Feature Breakdowns (GitHub Changelog, April 10, 2026)

> GitHub's April 10, 2026 changelog integrates CLI activity into the top-level Copilot usage metrics totals and adds CLI as a named feature dimension in breakdown fields — changing prior IDE-only interpretations of key aggregate fields and establishing `copilot_cli` as a first-class feature surface in the multi-surface metrics API.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words, April 10, 2026)
- **Author credibility**: GitHub engineering team announcing a production API behavior change. Authoritative for the fact that the fields changed, which fields are affected, what breakdowns now include CLI, and what remains unchanged. Not a credible source for how meaningful CLI activity metrics are as a proxy for productivity outcomes — no outcome data is cited.
- **Scope**: Integration of Copilot CLI activity into the existing Copilot usage metrics API. Covers: which aggregate fields changed meaning, the new `feature=copilot_cli` dimension in `totals_by_feature` and related breakdowns, what remains excluded (`totals_by_ide`), what remains unchanged (`totals_by_cli`), and the scope of the change (enterprise, organization, per-user; single-day and 28-day). Does NOT cover: how CLI activity is defined or what constitutes a CLI interaction; whether CLI completions are counted differently than IDE completions; any guidance on what CLI adoption rates indicate; or how this change interacts with the CCA → cloud agent rename announced on the same date.

## Extracted Claims

### Claim 1: CLI activity is now integrated into top-level Copilot usage metrics totals, ending its prior isolation in the separate `totals_by_cli` section for aggregate counting purposes

- **Evidence**: Official GitHub product changelog announcing the API behavior change. The framing confirms CLI was previously tracked separately and is now merged into the main aggregates.
- **Confidence**: settled (explicit product announcement of a behavioral change to live API fields)
- **Quote**: "CLI activity is now integrated into the metrics you already use."
- **Our assessment**: This is the central claim of the source. The practical implication is that any team consuming the Copilot usage metrics API after April 10, 2026 will see higher numbers in the affected top-level fields than before, without any underlying change in actual usage. The step-up is entirely attributable to previously excluded CLI activity now being counted. This parallels the June 15, 2026 server-side telemetry change (which added previously invisible users to the count): both are improvements in measurement completeness that produce time-series discontinuities, not genuine adoption growth signals.

### Claim 2: Four specific top-level aggregate fields now include CLI data alongside IDE data: `code_generation_activity_count`, `code_acceptance_activity_count`, `user_initiated_interaction_count`, and lines-of-code metrics (`loc_added_sum` / `loc_deleted_sum`)

- **Evidence**: Official changelog enumerates these specific fields as the ones whose meaning has changed.
- **Confidence**: settled (explicit field-level enumeration from official changelog)
- **Quote**: (no direct verbatim sentence listing all four fields; field names are enumerated in the changelog — see Concrete Artifacts)
- **Our assessment**: The fields affected are the most semantically significant aggregates in the metrics API: code generation and acceptance counts are the primary adoption metrics; user-initiated interaction counts reflect how often practitioners actively invoke Copilot; lines-of-code metrics track the volumetric output of AI assistance. That all four now include CLI contributions means CLI is being counted equally with IDE activity for all primary productivity proxy fields — not as a marginal surface.

### Claim 3: CLI now appears as `feature=copilot_cli` in four dimensional breakdown categories: `totals_by_feature`, `totals_by_model_feature`, `totals_by_language_feature`, and `totals_by_language_model`

- **Evidence**: Official changelog specifies the breakdowns where CLI appears as a named dimension, using the identifier `copilot_cli`.
- **Confidence**: settled (explicit enumeration of breakdown categories from official changelog)
- **Quote**: (no single verbatim sentence listing all four breakdowns; categories are named individually in the changelog — see Concrete Artifacts)
- **Our assessment**: The `copilot_cli` identifier makes CLI a peer of other named features in the `totals_by_feature` breakdown. This enables the analytics question "how much of our Copilot activity is CLI vs. IDE vs. other surfaces?" directly from the metrics API. The `totals_by_model_feature` and `totals_by_language_feature` breakdowns additionally reveal which AI models are used for CLI tasks and which programming languages are most common in CLI sessions — two analytics dimensions not previously available for CLI activity. This `feature=copilot_cli` dimension is the instrumentation prerequisite that enables the May 29, 2026 adoption cohort model to classify CLI engagement as a Phase 2 surface.

### Claim 4: CLI activity remains excluded from `totals_by_ide` — CLI usage is not attributed to any IDE in the metrics API

- **Evidence**: Official changelog explicitly states this exclusion.
- **Confidence**: settled (explicitly documented constraint from official changelog)
- **Quote**: "CLI remains excluded from `totals_by_ide`."
- **Our assessment**: This exclusion is architecturally correct — Copilot CLI is not an IDE, so attributing CLI activity to any IDE would be a category error. The operational implication is that `totals_by_ide` remains a pure IDE-only view after this change; teams using that breakdown to understand IDE-specific adoption do not need to adjust their interpretation. The asymmetry is worth documenting explicitly: CLI contributions appear in `totals_by_feature`, `totals_by_model_feature`, `totals_by_language_feature`, and `totals_by_language_model` — but NOT in `totals_by_ide`. A complete activity picture requires combining all breakdown dimensions; no single breakdown captures all surfaces.

### Claim 5: The existing `totals_by_cli` section and per-user CLI fields persist unchanged

- **Evidence**: Explicit statement in the official changelog that the dedicated CLI section remains intact.
- **Confidence**: settled (explicitly stated in official changelog)
- **Quote**: (no direct verbatim sentence for this claim; stated in changelog — see Extraction Notes)
- **Our assessment**: The preservation of `totals_by_cli` means teams that specifically need CLI-only data for isolated analysis can still get it from the dedicated section. The April 10 change does not eliminate CLI-specific visibility — it adds CLI to the aggregate totals and feature breakdowns while retaining the CLI-specific drill-down. This is an additive change: CLI data is now available in multiple places (aggregate totals + feature breakdowns + the existing CLI section), not a replacement where the CLI-only view was merged away.

### Claim 6: This change affects single-day and 28-day reports at enterprise, organization, and per-user levels

- **Evidence**: Explicit scope statement from the official changelog.
- **Confidence**: settled (scope stated in official changelog)
- **Quote**: (no direct verbatim quote for the scope statement; scope stated in changelog prose)
- **Our assessment**: The cross-scope impact means there is no safe tier of the metrics hierarchy that is unaffected. Enterprise admins using the enterprise endpoint, org admins using the org endpoint, and per-user reports all experience the changed semantics. Parity across reporting windows (single-day and 28-day) means both real-time monitoring dashboards and monthly trend reports need baseline adjustment.

### Claim 7: The change alters the meaning of top-level aggregate fields — organizations that built dashboards or alert thresholds based on prior IDE-only semantics will see inflated totals

- **Evidence**: Explicit warning in the official changelog that top-level totals have changed meaning.
- **Confidence**: settled (explicitly stated in official changelog)
- **Quote**: "Top-level totals have changed meaning. If your dashboards or reporting assumed these fields represented IDE-only activity, the numbers will increase..."
- **Our assessment**: This is the most operationally significant claim for practitioners already consuming the Copilot metrics API. Alert thresholds set against `code_generation_activity_count` will fire at lower relative baselines after April 10. Trend lines will show a step-up on April 10 that does not represent genuine adoption growth — it represents newly included CLI activity. The guide should treat this similarly to the June 15, 2026 server-side telemetry change: both are methodological inflection points that produce time-series discontinuities. Teams should annotate April 10, 2026 as a break point in any Copilot usage trend analysis that uses these aggregate fields.

### Claim 8: The `totals_by_feature` breakdown positions CLI as a first-class named feature surface alongside other Copilot surfaces, establishing the observability foundation for adoption phase classification

- **Evidence**: The use of `feature=copilot_cli` in `totals_by_feature` — the same breakdown used for other Copilot features — implies architectural parity. The May 29, 2026 cohort model depends on this instrumentation.
- **Confidence**: emerging (architectural parity is inferred from the naming convention and the downstream cohort model; the changelog does not explicitly state "CLI is now first-class")
- **Quote**: (no direct quote; inference from changelog structure and downstream dependency — see Our assessment)
- **Our assessment**: Prior to April 10, 2026, CLI activity existed in its own isolated bucket (`totals_by_cli`). After April 10, it is one of the named values in `totals_by_feature`, the same breakdown that captures other Copilot surfaces. This architectural promotion has downstream implications: the adoption cohort model (May 29, 2026) explicitly includes Copilot CLI as one of three Phase 2 "GitHub-based agent surfaces." That classification requires CLI being a tracked, named dimension in the feature breakdown. The `feature=copilot_cli` identifier established by this April 10 change is the prerequisite instrumentation that makes the May 29 cohort model's CLI classification computable.

## Concrete Artifacts

### Top-Level Aggregate Fields Changed to Include CLI (from changelog, April 10, 2026)

```
# Copilot usage metrics API — fields changed to include CLI activity (April 10, 2026)
# Affected reporting windows: single-day and 28-day rolling
# Affected API levels: enterprise, organization, per-user
# Change: these fields previously counted IDE activity only; they now include CLI

code_generation_activity_count
  Previously: IDE code generation events only
  Now:        IDE + CLI code generation events combined

code_acceptance_activity_count
  Previously: IDE acceptance events only
  Now:        IDE + CLI acceptance events combined

user_initiated_interaction_count
  Previously: IDE user-initiated interactions only
  Now:        IDE + CLI user-initiated interactions combined

loc_added_sum
  Previously: Lines added via IDE only
  Now:        Lines added via IDE + CLI combined

loc_deleted_sum
  Previously: Lines deleted via IDE only
  Now:        Lines deleted via IDE + CLI combined
```

### CLI Presence in Breakdown Dimensions (from changelog, April 10, 2026)

```
# Copilot usage metrics API — breakdown dimensions and CLI status after April 10, 2026

totals_by_feature
  CLI identifier: feature=copilot_cli
  Status: INCLUDED (new as of April 10, 2026)

totals_by_model_feature
  CLI identifier: feature=copilot_cli
  Status: INCLUDED (new as of April 10, 2026)

totals_by_language_feature
  CLI identifier: feature=copilot_cli
  Status: INCLUDED (new as of April 10, 2026)

totals_by_language_model
  CLI presence: INCLUDED (new as of April 10, 2026)

totals_by_ide
  CLI presence: EXCLUDED — explicitly stated; CLI is not an IDE

totals_by_cli
  Status: UNCHANGED — pre-existing dedicated CLI section; still present
```

### Known Methodology Inflection Points in the Copilot Usage Metrics Time Series

```
# These dates mark behavioral changes in the Copilot usage metrics API
# that cause step-changes in reported numbers without corresponding
# real-world adoption changes — annotate these on any trend chart

April 10, 2026 — CLI activity included in top-level totals (this note):
  Affected fields: code_generation_activity_count, code_acceptance_activity_count,
                   user_initiated_interaction_count, loc_added_sum, loc_deleted_sum
  Effect: step-up in top-level aggregates reflecting previously excluded CLI activity
  Breakdowns newly including CLI: totals_by_feature (feature=copilot_cli),
                                  totals_by_model_feature, totals_by_language_feature,
                                  totals_by_language_model
  Breakdowns unaffected: totals_by_ide (CLI excluded), totals_by_cli (unchanged)

June 15, 2026 — Server-side telemetry supplements client telemetry:
  Affected fields: DAU counts (all active-user counts), high-level aggregates
  Effect: ~5% step-up in DAU counts for affected organizations
  Breakdowns partially affected: totals_by_ide and totals_by_feature empty
                                  for server-side-only users
  (documented in docs-github-copilot-usage-metrics-server-side-telemetry.md, issue #1189)
```

## Cross-References

- **Corroborates** `docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 6 (multi-surface Copilot adoption view giving "a full view of Copilot adoption across surfaces"): The April 10 CCA note adds aggregate CCA active-user counts; this April 10 CLI note integrates CLI activity into top-level aggregates. Published on the same date, the two changelogs represent a paired expansion of the metrics API covering two distinct surfaces simultaneously. Together they make April 10, 2026 the date when the Copilot metrics API achieved meaningful multi-surface aggregate coverage — CCA and CLI both measured in a single reporting pass.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 1 (two new API fields track Copilot code review adoption): Three surface expansions arrived within two days: PR review metrics (April 8), CCA aggregate counts and CLI integration (both April 10). This cadence confirms GitHub was executing a systematic multi-surface expansion of the metrics API rather than adding surfaces ad hoc. The CLI integration follows the same architectural pattern as the PR review addition: a new Copilot surface becomes a named dimension in the existing metrics API schema.

- **Is prerequisite for** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 4 (Phase 2 "Agent first" covers users who engaged with a single GitHub-based agent surface — Copilot cloud agent, Copilot code review, or Copilot CLI): The May 29, 2026 adoption cohort model classifies CLI engagement as Phase 2. That classification requires CLI activity to be tracked as a named dimension in the metrics API — which this April 10 change provides via `feature=copilot_cli` in `totals_by_feature`. Without the April 10 change, the "Copilot CLI" surface referenced in the cohort model would have no corresponding metric dimension to measure Phase 2 membership against. This is the earlier foundational announcement that the May 29 cohort model depends on.

- **Extends** `docs-github-copilot-usage-metrics-server-side-telemetry.md` Claim 4 (newly surfaced server-side-only users have empty `totals_by_ide` and `totals_by_feature` breakdowns): The June 15 note warns that server-side-only users appear in DAU counts but with empty feature breakdowns including `totals_by_feature`. Since `totals_by_feature` now includes `feature=copilot_cli` (this April 10 note), a server-side-only CLI user would contribute to the CLI-inclusive top-level aggregates (Claim 2 above) but would NOT appear in `totals_by_feature[copilot_cli]` — contributing to the gap between top-level totals and breakdown sums that the June 15 note flags as expected behavior. Teams seeing the post-June-15 gap between top-level totals and breakdown sums must account for both the CLI integration (this note) and the server-side-only population (June 15 note) as simultaneous contributions to that gap.

- **Corroborates** `docs-github-copilot-team-level-usage-metrics.md` Claim 5 (team-level breakdowns available across "IDE completions, chat, Copilot CLI, code review, and Copilot cloud agent activity. They can be cut by language, IDE, feature, or model"): The May 14 team-level note lists Copilot CLI as one of five Copilot feature surfaces available at team granularity, with a `feature` cut dimension. That listing depends on CLI being a named feature in the metrics API — which this April 10 change establishes. The `feature=copilot_cli` identifier defined here flows through to team-level analytics.

- **Corroborates** `docs-github-copilot-cli-remote-control-ga.md` Claim 1 (remote control for Copilot CLI sessions is now generally available): The May 18, 2026 remote control GA confirms CLI's status as a first-class Copilot surface receiving active feature investment. Together with this note (CLI metrics integration), the two establish that by April–May 2026, Copilot CLI has reached both observability parity with IDE surfaces (measured in the same API fields) and operational maturity sufficient for remote unattended workflows.

- **Novel**:
  - **CLI inclusion in top-level aggregate fields**: No prior source in the corpus documents the exact fields affected by the April 10 change, nor the pre-change baseline that these fields represented IDE-only activity. This is the first note to explicitly establish that prior to April 10, `code_generation_activity_count` and its peers were IDE-only metrics.
  - **`feature=copilot_cli` as the CLI identifier in `totals_by_feature`**: No prior source names this identifier or describes how CLI appears in the feature dimension of the metrics API.
  - **April 10 as a time-series inflection point for top-level productivity aggregates**: The CCA note (same date, issue #131) documents April 10 as an inflection point for CCA active-user fields; this note establishes April 10 as also an inflection point for the core productivity aggregate fields. Organizations tracking these fields see a step-up on April 10, 2026 that does not reflect real adoption change — and that inflection is separate from the CCA-specific change.
  - **CLI excluded from `totals_by_ide`**: No prior source explicitly states this exclusion. It is a documented constraint that affects how practitioners interpret the IDE breakdown going forward: `totals_by_ide` remains IDE-only after this change, despite CLI being promoted elsewhere in the schema.
  - **`totals_by_cli` persists alongside the new integrations**: No prior source documents the existence or behavior of the `totals_by_cli` dedicated section. Its persistence provides a CLI-isolation primitive for analytics that specifically need to separate CLI from IDE activity.

## Guide Impact

### Chapter 05: Measurement — Copilot Adoption Metrics

- **Section "Time-series comparability"** (add or extend): Add April 10, 2026 as a known inflection point in the Copilot usage metrics time series. The fields `code_generation_activity_count`, `code_acceptance_activity_count`, `user_initiated_interaction_count`, `loc_added_sum`, and `loc_deleted_sum` changed meaning on this date to include CLI activity. A step-up in these fields on or after April 10 does not indicate adoption growth — it indicates measurement scope expansion. Pair this note with `docs-github-copilot-usage-metrics-server-side-telemetry.md` to document both April 10 and June 15, 2026 as the two known break points in the time series.

- **Section "Multi-surface Copilot measurement"** (new or extend): Document the three-way breakdown structure as of April 10, 2026:
  1. `totals_by_ide`: IDE-only activity (unchanged by April 10)
  2. `totals_by_feature[copilot_cli]`: CLI-specific activity (new as of April 10)
  3. Top-level aggregates (`code_generation_activity_count` etc.): IDE + CLI combined (changed as of April 10)
  
  No single field gives a complete multi-surface picture. Teams must combine breakdown dimensions to distinguish IDE vs. CLI contributions.

- **Section "CLI observability in the metrics API"** (add): Reference `feature=copilot_cli` in `totals_by_feature`, `totals_by_model_feature`, and `totals_by_language_feature` as the mechanism for CLI-specific adoption analysis. Note that `totals_by_cli` provides an alternative isolation path. Note explicitly that `totals_by_ide` does NOT include CLI activity.

### Chapter 01: Daily Workflows — CLI as a Primary Copilot Surface

- **Section "Copilot CLI activity tracking"**: Reference this note to document that Copilot CLI activity is fully observable via the usage metrics API from April 10, 2026. CLI sessions appear in both aggregate totals and feature-level breakdowns. Practitioners using CLI-heavy workflows can point their organizations to `totals_by_feature[copilot_cli]` to demonstrate the volume of CLI-based AI assistance they're consuming. Previously, CLI activity was invisible in the aggregate numbers their organizations reviewed.

### Chapter 04: Observability

- **Section "Copilot metrics API coverage"**: Add a note about the April 10 change: dashboards consuming top-level aggregate fields before this date were inadvertently reporting IDE-only numbers under the label of "Copilot usage." Post-April 10 dashboards give a truer multi-surface picture but require baseline adjustment to avoid false-positive adoption signals. Any alert threshold set against the affected aggregate fields before April 10 should be reviewed and updated.

## Extraction Notes

1. **Source is a short product changelog (~300 words)**: All substantive claims are exhausted in the eight claims above. The changelog describes a targeted API change with limited scope; no additional content would emerge from re-reading.
2. **WebFetch model processing applied to all fetches**: Two separate WebFetch calls were made against the source URL. Both returned model-processed summaries rather than verbatim text. Quotes marked as direct in this note carry uncertainty about character-exact fidelity. The Assayer should verify the following against the live source URL: (a) "CLI activity is now integrated into the metrics you already use." (b) "Top-level totals have changed meaning. If your dashboards or reporting assumed these fields represented IDE-only activity, the numbers will increase..." (c) "CLI remains excluded from `totals_by_ide`." Both fetch responses attributed these as direct changelog quotes; they appear consistent with the changelog's described content.
3. **Same-date announcement as CCA metrics (issue #131)**: This changelog was published April 10, 2026, the same date as `docs-github-copilot-cca-usage-metrics-aggregate.md`. The two are separate changelogs covering different aspects of a coordinated metrics API expansion on the same day. They are complementary and not overlapping — the CCA note covers new aggregate active-user fields; this note covers integration of CLI activity into existing aggregate fields.
4. **Field names verified across both fetches**: The specific field names (`code_generation_activity_count`, `code_acceptance_activity_count`, `user_initiated_interaction_count`, `loc_added_sum`, `loc_deleted_sum`, `totals_by_feature`, `totals_by_model_feature`, `totals_by_language_feature`, `totals_by_language_model`, `totals_by_ide`, `totals_by_cli`) appeared consistently across both WebFetch responses and are structurally consistent with the Copilot metrics API schema referenced in multiple other corpus notes.
5. **No contradictions filed**: No existing source note claims that CLI activity was already included in top-level totals before April 10, or that CLI should be excluded from the metrics API. The change is entirely additive — it addresses a prior gap. The server-side telemetry note (June 15) and this note represent parallel methodological expansions; they are not contradictory with each other or with any prior corpus claim.
6. **Triage questions addressed**: The Prospector asked whether this announcement provides granular breakdowns or summary counts, and how it relates to the May 29 adoption-phase framework. Answer: (a) Granular breakdowns — CLI appears as a named dimension in `totals_by_feature`, `totals_by_model_feature`, `totals_by_language_feature`, and `totals_by_language_model`, but is excluded from `totals_by_ide`. (b) This April 10 change is the prerequisite for the May 29 cohort model's Claim 4 — the `feature=copilot_cli` dimension is what makes CLI trackable as a Phase 2 surface in the adoption phase classification.
