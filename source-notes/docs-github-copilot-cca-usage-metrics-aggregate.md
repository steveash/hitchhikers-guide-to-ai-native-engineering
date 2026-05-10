---
source_url: https://github.blog/changelog/2026-04-10-copilot-usage-metrics-now-aggregate-copilot-cloud-agent-active-user-counts
source_type: docs
title: "Copilot usage metrics now aggregate Copilot cloud agent active user counts"
author: GitHub (official changelog)
date_published: 2026-04-10
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: anecdotal
issue: "#131"
---

# Copilot Cloud Agent Active User Counts in the Usage Metrics API (GitHub Changelog)

> GitHub's official announcement of three new aggregate-level active-user-count
> fields for Copilot cloud agent (CCA) in the Copilot usage metrics API, covering
> daily, weekly, and monthly windows at the enterprise and organization levels —
> a fleet observability primitive that complements the earlier user-level CCA flag
> and the existing IDE agent-mode active user count.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words, April 10, 2026)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these fields now exist and what they measure.
  Not a credible source for any causal claim about CCA adoption effects — no
  outcomes data is cited.
- **Scope**: Three new fields added to the Copilot usage metrics REST API at the
  enterprise and organization levels, providing aggregate CCA active user counts
  across daily, weekly, and monthly windows. Covers field definitions,
  nullability semantics, and the stated use cases for adoption tracking. Also
  documents the Copilot coding agent → Copilot cloud agent rename (announced
  April 1, 2026) and its forthcoming schema migration. Does NOT cover: what
  counts as a CCA "active use" event (the predecessor March 25 changelog defines
  the trigger as assigning Copilot to an issue or tagging `@copilot` in a PR
  comment, but this changelog does not repeat it); how these fields interact with
  Copilot plan tiers; or any guidance on what counts as a "good" adoption rate.

## Extracted Claims

### Claim 1: Three new aggregate active-user-count fields are now available in both enterprise and organization usage reports

- **Evidence**: Official GitHub product changelog announcing the feature. States
  clearly that the fields are "available in both 1-day and 28-day reports at the
  enterprise and organization levels."
- **Confidence**: settled (these fields exist — this is a product fact)
- **Quote**: "Three new fields are available in both 1-day and 28-day reports at the enterprise and organization levels"
- **Our assessment**: The fields themselves are settled product facts. The practical
  implication is that fleet-level CCA adoption is now measurable without having to
  aggregate per-user records. For teams that cannot expose individual user-level
  metrics for privacy or policy reasons, the aggregate counts provide a compliant
  observability path. The dual availability at enterprise and organization level
  means both enterprise admins (cross-org view) and org admins (single-org view)
  can access the data without custom aggregation.

### Claim 2: `daily_active_copilot_cloud_agent_users` counts unique users who used CCA on a given day

- **Evidence**: Field definition from the official changelog and accompanying API
  documentation table.
- **Confidence**: settled (definitional)
- **Quote**: "Number of unique users who used Copilot cloud agent on that day"
- **Our assessment**: A daily active user count is an adoption penetration metric —
  it shows how many distinct individuals triggered CCA on any single day. By
  itself it tells you nothing about the depth or quality of that usage. A user who
  opened a single CCA session and abandoned it counts the same as a user who ran
  twenty sessions to completion. Teams should not treat this metric as a proxy for
  productivity; treat it as a proxy for breadth of exposure.

### Claim 3: `weekly_active_copilot_cloud_agent_users` counts unique users in a trailing 7-day window

- **Evidence**: Field definition from the official changelog and accompanying API
  documentation table.
- **Confidence**: settled (definitional)
- **Quote**: "Number of unique users who used Copilot cloud agent in the trailing 7-day window"
- **Our assessment**: The weekly window smooths out the daily noise (a user who
  uses CCA every other day would show up on half the daily data points but 100%
  of the weekly data points). It is more useful for tracking whether rollout
  coverage is sticky vs. trial-and-drop. For Ch05 measurement guidance: weekly
  active users at 4+ weeks post-rollout is a reasonable stickiness proxy.

### Claim 4: `monthly_active_copilot_cloud_agent_users` counts unique users in a trailing 28-day window

- **Evidence**: Field definition from the official changelog and accompanying API
  documentation table.
- **Confidence**: settled (definitional)
- **Quote**: "Number of unique users who used Copilot cloud agent in the trailing 28-day window"
- **Our assessment**: The 28-day window is the canonical MAU (monthly active user)
  metric from consumer product analytics. Its inclusion here mirrors the
  `monthly_active_agent_users` field for IDE agent mode, creating a direct
  apples-to-apples comparison between CCA (cloud agentic tasks) and IDE agent
  mode (in-editor agentic tasks) adoption at the same aggregation level. This is
  the most useful field for executive-level adoption dashboards.

### Claim 5: These fields are nullable — they return a count (including zero) when data is available, or null when no CCA data exists for that period

- **Evidence**: Explicit statement in the changelog.
- **Confidence**: settled (explicitly documented behavioral constraint)
- **Quote**: "These fields are nullable — they return a count (including zero) when data is available, or `null` when no Copilot cloud agent data exists for that period."
- **Our assessment**: The null case matters for teams building dashboards or
  alerting on these fields. A null return does not mean "zero CCA users" — it
  means no CCA data was recorded (which could indicate the feature is not yet
  enabled, the reporting window predates CCA availability, or a data pipeline gap).
  Treat null as "unknown" not "zero" in downstream queries. Teams processing this
  data via SQL or BI tools should use `COALESCE(field, -1)` or an equivalent
  null-aware pattern rather than treating null as zero in aggregations.

### Claim 6: The aggregate counts complement the user-level `used_copilot_coding_agent` flag and the existing `monthly_active_agent_users` IDE field, providing a multi-surface Copilot adoption view

- **Evidence**: Explicitly stated in the changelog's "Complete the picture" section.
- **Confidence**: settled (stated as architectural intent in official changelog)
- **Quote**: "These counts sit alongside existing metrics like `monthly_active_agent_users` (IDE agent mode) and the user-level `used_copilot_coding_agent` flag, giving you a full view of Copilot adoption across surfaces."
- **Our assessment**: This is the most guide-relevant claim. GitHub is explicitly
  building a multi-surface metrics layer: IDE agent mode (existing),
  CCA at user level (March 25, 2026 update), CCA at aggregate level (this update).
  A complete enterprise Copilot observability setup should track all three to
  distinguish "how many users are in IDE agent mode?" from "how many users are
  running autonomous CCA tasks?". These are operationally different behaviors
  that serve different use cases. Conflating them yields misleading adoption
  numbers.

### Claim 7: The update was announced alongside the Copilot coding agent → Copilot cloud agent rename, with a data schema migration forthcoming

- **Evidence**: Explicit note at the top of the changelog.
- **Confidence**: settled (official naming announcement)
- **Quote**: "We've recently renamed Copilot coding agent to Copilot cloud agent. We will be updating our data schema for all existing coding agent fields to reflect this change in the coming weeks, and new fields from now forward will reflect the name change."
- **Our assessment**: This is an operational concern for teams with existing
  integrations against the Copilot usage metrics API. Any code or dashboard that
  references `coding_agent` field names should be monitored for the forthcoming
  schema migration. The announcement does not give a specific date for when old
  `coding_agent` fields will be renamed. Until then, both naming conventions are
  in flight: existing fields use `coding_agent`, new fields (including the three
  in this changelog) use `cloud_agent`. Teams building new integrations should
  use the `cloud_agent` naming; teams with existing integrations should plan for
  a migration event.

### Claim 8: The feature enables organizations to track CCA adoption without aggregating user-level data themselves

- **Evidence**: Explicitly stated in the changelog's "Track adoption at a glance"
  section.
- **Confidence**: settled (stated design intent)
- **Quote**: "See how many users are actively using Copilot cloud agent across your enterprise or organization without aggregating user-level data yourself."
- **Our assessment**: This claim frames the aggregate counts as a convenience
  feature that reduces the admin burden of building custom aggregations over the
  per-user `used_copilot_coding_agent` flag. For teams that already consume the
  user-level flag (available since March 25, 2026), the aggregate fields are
  redundant in data content but valuable in operational convenience — no need
  to write and maintain a GROUP BY query. For teams that cannot or do not
  consume user-level data (privacy policy, GDPR constraints, etc.), the
  aggregate fields are the only route to fleet-level CCA visibility.

### Claim 9: Daily, weekly, and monthly windows let organizations "compare engagement across time windows" and "measure the impact of rollout efforts"

- **Evidence**: Explicit statement in the changelog's "Compare engagement across
  time windows" section.
- **Confidence**: anecdotal (vendor framing of how teams should use the metrics;
  no evidence that multi-window comparison actually surfaces rollout impact)
- **Quote**: "Daily, weekly, and monthly counts let you spot adoption trends and measure the impact of rollout efforts."
- **Our assessment**: The multi-window capability is real and useful, but the claim
  that it "measures the impact of rollout efforts" is vendor marketing. What these
  fields measure is activity counts — they cannot distinguish between a rollout
  causing adoption growth and adoption growing for independent reasons (e.g.,
  word-of-mouth, a high-profile CCA demo). To measure rollout impact, teams need
  a before/after comparison window, ideally with a control cohort. The API fields
  provide the raw data; the impact measurement design is the team's responsibility.

## Concrete Artifacts

### Three New CCA Aggregate Active User Fields (from changelog, April 10, 2026)

```
# Copilot usage metrics API — CCA aggregate active user fields (added April 10, 2026)
# Available at:
#   GET /enterprises/{enterprise}/copilot/metrics
#   GET /orgs/{org}/copilot/metrics
# Reporting windows: 1-day and 28-day rolling
# API version: apiVersion=2026-03-10

daily_active_copilot_cloud_agent_users
  Type: integer | null
  Description: Number of unique users who used Copilot cloud agent on that day.
  Nullability: null when no CCA data exists for the period; 0 when data exists
               but no users were active.

weekly_active_copilot_cloud_agent_users
  Type: integer | null
  Description: Number of unique users who used Copilot cloud agent in the
               trailing 7-day window.
  Nullability: same as above.

monthly_active_copilot_cloud_agent_users
  Type: integer | null
  Description: Number of unique users who used Copilot cloud agent in the
               trailing 28-day window.
  Nullability: same as above.
```

### Multi-Surface Copilot Adoption Metrics Landscape (as of April 10, 2026)

```
Surface 1 — IDE agent mode:
  monthly_active_agent_users
    → Aggregate monthly count, org/enterprise level (pre-existing field)

Surface 2 — CCA, user level (added March 25, 2026):
  used_copilot_coding_agent                    [note: field name uses old naming]
    → Boolean flag per user row; true if user assigned Copilot to an issue
      or @copilot-tagged a PR comment in the reporting period.
    → Allows per-user CCA activity identification.

Surface 3 — CCA, aggregate level (added April 10, 2026, THIS CHANGELOG):
  daily_active_copilot_cloud_agent_users       → daily unique active users
  weekly_active_copilot_cloud_agent_users      → trailing-7d unique active users
  monthly_active_copilot_cloud_agent_users     → trailing-28d unique active users

Upcoming schema migration (date TBD as of April 10, 2026):
  Existing coding_agent field names to be renamed to cloud_agent equivalents.
  New fields (this changelog) already use cloud_agent naming.

Missing for complete outcome measurement:
  task_completion_rate_copilot_cloud_agent     → not yet available
  pr_merge_rate_copilot_cloud_agent_initiated  → not yet available
  (adoption metrics only; no quality or outcome metrics currently in API)
```

## Cross-References

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 1 (two new API
  fields track Copilot code review adoption) — same architectural pattern: GitHub
  incrementally extends the Copilot usage metrics API by adding one new product
  surface at a time. PR review metrics (April 8, 2026) and CCA aggregate counts
  (April 10, 2026) were announced two days apart, reflecting a systematic expansion
  of the metrics API surface rather than a one-time addition.
- **Extends** `docs-github-copilot-pr-review-metrics.md` Claim 5 (fields restricted
  to enterprise administrators and organization owners with Copilot usage metrics
  access) — the same access tier restriction applies to CCA aggregate fields.
  Enterprise-only limitation is a recurring constraint across the Copilot metrics
  API series; any Ch05 guidance citing these fields must include this caveat.
- **Corroborates** `docs-github-copilot-cca-custom-properties.md` Claim 7 (pilot-first
  progressive rollout is the prescribed CCA adoption pattern) — this metrics note
  provides the measurement layer that makes phased rollouts observable. The
  governance API (which orgs have CCA enabled) from the custom-properties note
  is logically prior; these aggregate counts are the feedback signal that tells
  admins whether a rollout cohort is actually using CCA after enablement.
- **Extends** `docs-github-copilot-cca-custom-properties.md` — the governance layer
  (enable/disable CCA per org) now has a corresponding measurement layer
  (aggregate CCA active users per org). Together they give enterprise admins both
  levers and gauges for CCA deployment. Neither note alone is sufficient for a
  complete CCA observability story.
- **Extends** `docs-github-copilot-cca-validation-parallel.md` (issue #105, CCA
  validation tools 20% faster) — that note documents CCA operational performance;
  this note documents CCA adoption measurement. The two together provide distinct
  observability angles on CCA deployments: how fast it runs vs. how many users
  are using it. Neither corroborates nor contradicts the other.
- **Novel**:
  - First source in the corpus to document aggregate-level (org/enterprise) CCA
    active user counts as a distinct primitive from user-level CCA flags. The
    distinction matters for privacy-constrained environments and for executive
    dashboards that should not expose individual user records.
  - The three-window view (daily/weekly/monthly) is new to the corpus. No existing
    source discusses temporal window selection for AI adoption metrics or the
    trade-offs between daily noise and monthly lag.
  - The null vs. zero semantic is new to the corpus. Existing metrics notes do not
    discuss nullability of API fields as an operational concern.
  - The naming-migration alert (coding_agent → cloud_agent schema change forthcoming)
    is not documented in any other source note and is a novel operational concern
    for any team with existing API integrations.
  - No source in the corpus yet covers the March 25, 2026 predecessor (user-level
    `used_copilot_coding_agent` flag); that changelog is the upstream context for
    this one and is not yet a source note (issues #129 and #347 are related but
    not yet mined as of this extraction).

## Guide Impact

### Chapter 05: Measurement — Metrics

- **Section "Measuring agentic AI adoption"** (add or extend): Reference the three
  CCA aggregate fields as the canonical vendor-native measurement primitive for
  fleet-level CCA adoption. Specifically: `monthly_active_copilot_cloud_agent_users`
  is the MAU equivalent for agentic task adoption — the same metric used in
  consumer product analytics, now available for enterprise AI tool tracking.
  Note the enterprise-only access constraint.
- **Section "Multi-surface Copilot adoption"** (new section if not present): Use
  the three-surface model (IDE agent mode / CCA user-level / CCA aggregate) as
  a concrete example of why fleet observability requires disaggregated metrics.
  Conflating "Copilot adoption" as a single number loses the signal about whether
  users are adopting IDE-mode assistance vs. autonomous agent delegation — which
  are operationally distinct behaviors.
- **Section "Metrics nullability and null semantics"** (add): Explicitly warn that
  null ≠ zero for Copilot API fields. A null return on a CCA active-user field
  means "no data recorded," not "zero users active." Document the `COALESCE` or
  null-check pattern for any dashboard or alert that consumes these fields.
- **Section "Adoption metric limitations"** (add or extend): Flag Claim 9 — the
  multi-window view enables trend spotting but does NOT measure rollout impact
  without a before/after design and ideally a control cohort. Cite this source
  as the vendor's own framing ("measure the impact of rollout efforts") and
  annotate it as an underdetermined claim: the API provides the data, but the
  impact measurement design is the team's responsibility.

### Chapter 02: Harness Engineering — Observability

- **Section "Enterprise Copilot observability"**: Add the CCA aggregate active-user
  fields to the list of recommended observability primitives for agentic system
  monitoring. These fields answer the question "Is our agentic deployment actually
  being used?" at fleet level, without requiring per-user data access. Reference
  alongside the governance API from `docs-github-copilot-cca-custom-properties.md`
  to frame the complete "enable → measure" loop for CCA deployment.
- **Section "API schema stability"**: Add a warning about the forthcoming
  `coding_agent` → `cloud_agent` naming migration in the Copilot metrics API.
  Any harness code that calls the Copilot usage metrics API should treat field
  names as potentially unstable until the migration completes.

## Extraction Notes

1. **Source is thin by design**: This is a product changelog, not a practitioner
   post or research paper. The full substantive content is ~300 words. All claims
   are exhausted above in 9 items — the source should not be cited for more than
   it contains.
2. **One primary web fetch**: The changelog page was fetched once and returned the
   full verbatim content including the three field definitions, nullability note,
   and the "Why this matters" bullet points. The linked API documentation page
   (`docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics`)
   was not separately fetched; field details are derived from the changelog table,
   which was verbatim and complete.
3. **Predecessor context**: The March 25, 2026 predecessor changelog (user-level
   `used_copilot_coding_agent` flag) was fetched to understand the upstream context.
   That source is not yet a source note in this corpus. The aggregate counts in
   this note build directly on that user-level primitive.
4. **No contradictions to file**: No existing source note claims that CCA adoption
   cannot or should not be measured at the aggregate level, or that the three-window
   approach is inappropriate. The aggregate vs. user-level distinction is a
   condition variable, not a contradiction.
5. **Vendor framing quarantined**: Claim 9 ("measure the impact of rollout efforts")
   is flagged as anecdotal vendor framing. The API fields are the data primitive;
   impact measurement requires additional experimental design not provided by the API.
6. **Naming migration flagged**: The coding_agent → cloud_agent rename is documented
   in Claim 7 as an operational concern. No existing source note covers this
   migration; it is novel to the corpus.
