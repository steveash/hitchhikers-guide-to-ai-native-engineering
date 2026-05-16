---
source_url: https://github.blog/changelog/2026-05-14-team-level-copilot-usage-metrics-now-available-via-api
source_type: docs
title: "Team-level Copilot usage metrics now available via API"
author: GitHub (official changelog)
date_published: 2026-05-14
date_extracted: 2026-05-16
last_checked: 2026-05-16
status: current
confidence_overall: settled
issue: "#758"
---

# Team-level Copilot Usage Metrics via API (GitHub Changelog)

> GitHub's official announcement of a new user-teams report endpoint that enables
> team-level Copilot usage metrics via a JOIN operation on per-user usage data —
> a distinct granularity tier below org/enterprise aggregates and above individual
> user records, with concrete operational caveats around minimum team size and
> multi-team user counting.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words, May 14, 2026)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these endpoints exist, what they return, and the
  stated behavioral constraints. Not a credible source for any claim about how
  team-level metrics will affect engineering practices — no outcomes data is cited.
- **Scope**: A new user-teams report endpoint available at enterprise and organization
  levels, returning NDJSON files mapping Copilot-licensed users to their team
  memberships. Covers API endpoints, data structure, join guidance, access
  permissions, and key operational caveats. Does NOT cover: how to interpret
  team-level metrics for actionable decisions; what constitutes a "good" team
  adoption rate; how team-level data integrates with existing BI tooling; or
  historical data availability (unclear if the report can be joined to historical
  per-user data or only the current window).

## Extracted Claims

### Claim 1: The Copilot usage metrics API now exposes a new user-teams report that maps licensed users to their team memberships, enabling team-level metrics via a JOIN with per-user usage data

- **Evidence**: Official GitHub product changelog, May 14, 2026. The core capability —
  joining the user-teams report with per-user usage data — is described as the
  architectural pattern for constructing team-level metrics.
- **Confidence**: settled (documented product fact from the authoritative source)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is the architecturally significant claim. The April 10
  release (`docs-github-copilot-cca-usage-metrics-aggregate.md`) provided
  pre-aggregated counts at org/enterprise level — no join required, just read
  a field. This release introduces a different approach: a raw mapping file
  (user-teams) that teams must JOIN with per-user usage data to compute team-level
  metrics. Team-level is NOT a pre-aggregated metric; it requires data engineering
  work. A harness that needs team-level adoption numbers must implement and maintain
  the join pipeline rather than simply reading a pre-computed field.

### Claim 2: Two new endpoints return signed download URLs to NDJSON reports containing the user-teams mapping

- **Evidence**: Official changelog with explicit endpoint paths at enterprise and
  org level.
- **Confidence**: settled (product fact)
- **Quote**: "return signed download URLs to NDJSON reports"
- **Our assessment**: The signed URL pattern (rather than streaming data directly)
  is an operational consideration for harness design. Signed URLs expire, so any
  harness code that caches the response must re-fetch before the URL expires.
  The NDJSON format (newline-delimited JSON) is streaming-friendly and common in
  data engineering pipelines, but teams using SQL-only tooling will need a
  preprocessing step to load NDJSON into a queryable form.

### Claim 3: Team-level metrics cover active users, completions, chats, and breakdowns by language, IDE, feature, and model

- **Evidence**: Explicit statement in changelog.
- **Confidence**: settled (stated available dimensions after join)
- **Quote**: "active users, completions, chats, as well as breakdowns by language, IDE, feature, and model"
- **Our assessment**: These dimensions match what is available in the per-user usage
  data (the join source). The team-level view is a groupby over the same underlying
  data — no new metric types are introduced, only a new grouping dimension (team).
  Teams already familiar with the per-user Copilot usage API fields will find the
  same breakdown dimensions available at the team level after the join.

### Claim 4: Teams with fewer than five Copilot-seated users are excluded from the user-teams report

- **Evidence**: Explicit statement in changelog. This threshold is consistent with
  common differential-privacy practice for small-cohort suppression.
- **Confidence**: settled (explicitly documented behavioral constraint)
- **Quote**: "Teams with fewer than five Copilot-seated users are excluded from the user-teams report."
- **Our assessment**: This is the most operationally significant caveat.
  Organizations with fine-grained team structures (e.g., two-person sub-teams,
  tiger teams, on-call rotations) will have data gaps. Any harness that builds
  team-level dashboards must handle the case where a team has no entry in the
  user-teams report — that absence is privacy suppression, not a pipeline error.
  Dashboards should render "< 5 users (suppressed)" for excluded teams, not
  zero or an error state.

### Claim 5: Users who belong to multiple teams have their activity counted in each team's aggregate, so team totals cannot be summed to org totals

- **Evidence**: Explicit statement in changelog, described as an operational constraint.
- **Confidence**: settled (explicitly documented behavioral semantic)
- **Quote**: "users who belong to multiple teams will have their activity counted in each team's aggregate."
- **Our assessment**: This is the most subtle data modeling trap. If a user belongs
  to both Team A and Team B, their activity appears in both team reports.
  SUM(all team active users) > org active users whenever multi-team membership
  exists. Any harness or dashboard that attempts to reconcile team sums against
  org totals will observe persistent discrepancies — these are expected behavior,
  not data quality issues. Document this for anyone building cross-layer
  reconciliation checks or executive roll-up dashboards.

### Claim 6: Access is restricted to enterprise administrators, organization owners, billing managers, and enterprise custom role holders with "View Enterprise Copilot Metrics" permission

- **Evidence**: Explicit statement in changelog.
- **Confidence**: settled (documented access control policy)
- **Quote**: "available through the REST API to enterprise administrators, organization owners, billing managers, and people with an enterprise custom role."
- **Our assessment**: The same access tier restriction appears in the April 8
  (`docs-github-copilot-pr-review-metrics.md` Claim 5) and April 10
  (`docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 1) releases.
  This is a stable pattern: all Copilot observability primitives require admin-level
  access. Individual engineers and team leads cannot self-serve this data without
  admin involvement. For Ch02 harness design: the metrics-retrieval component must
  run under an admin-privileged service account; team lead credentials will not
  have access.

### Claim 7: This feature is REST API only — no dashboard surface is included in this release

- **Evidence**: Consistent with both WebFetch returns; the announcement describes
  only API access with no mention of any UI surface.
- **Confidence**: settled (stated product scope for this release)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: All three recent Copilot metrics releases (April 8, April 10,
  May 14) are API-only with no dashboard. GitHub is releasing the measurement
  primitives before the visualization layer. Any team wanting team-level dashboards
  must build them on top of the API using their own BI tooling. This increases the
  investment required to operationalize team-level metrics compared to simply reading
  a pre-built org-level dashboard (if one existed).

### Claim 8: Documentation provides step-by-step guidance on the join pattern, day-level aggregation, and rolling-window multi-day reporting

- **Evidence**: Explicit statement in changelog.
- **Confidence**: settled (GitHub's own documentation intent)
- **Quote**: "step-by-step guidance in the docs covering the join, day-level aggregation, and a rolling-window pattern for multi-day reporting."
- **Our assessment**: The existence of join guidance is noteworthy: GitHub acknowledges
  that team-level metrics require data engineering and is providing documentation
  for it. This is a deliberate shift from the April 10 approach (pre-aggregated
  fields requiring no join). Teams deciding between org-level and team-level metrics
  should factor in the engineering overhead: org-level is a simple API read;
  team-level requires a join implementation and an ongoing data pipeline.

## Concrete Artifacts

### API Endpoints (from changelog, May 14, 2026)

```
# Copilot usage metrics — user-teams report endpoints (added May 14, 2026)
# Returns: signed download URL to NDJSON report
# Format: newline-delimited JSON (NDJSON)

GET /enterprises/{enterprise}/copilot/metrics/reports/user-teams-1-day
  Access: enterprise administrators, billing managers,
          enterprise custom role with "View Enterprise Copilot Metrics"

GET /orgs/{org}/copilot/metrics/reports/user-teams-1-day
  Access: organization owners, billing managers,
          enterprise custom role with "View Enterprise Copilot Metrics"
```

### User-Teams Report Data Structure and Join Pattern (from changelog)

```
# Each row in the NDJSON user-teams report contains:
#   team's enterprise/organization ID, team slug, user ID, user login
#
# Join pattern for team-level metrics:
#
#   user-teams report  JOIN  per-user usage data
#   ON  user_id = user_id  AND  day = day
#
# Result: per-user usage records annotated with team_slug
# Then aggregate by team_slug to get team-level counts
#
# Available post-join dimensions:
#   active users, completions, chats, language, IDE, feature, model
```

### Operational Constraints Summary (May 14, 2026)

```
# Copilot team-level metrics — operational constraints

Minimum team size threshold:
  Teams with < 5 Copilot-seated users: EXCLUDED from user-teams report
  → Absence of a team entry is privacy suppression, not a data pipeline error
  → Dashboard: show "< 5 users (suppressed)" not zero or an error

Multi-team user double-counting:
  Users in N teams: activity counted in EACH team's aggregate
  → SUM(team active users across all teams) > ORG active users
  → Do NOT attempt to reconcile team sums to org totals

API surface:
  REST API only — no dashboard in this release
  Response: signed download URL (expires; do not cache the URL itself)
  File format: NDJSON (may require preprocessing for SQL query engines)

Access:
  Enterprise admins, org owners, billing managers, enterprise custom roles
  with "View Enterprise Copilot Metrics" permission only
```

### Copilot Metrics API Granularity Layers (as of May 14, 2026)

```
Layer 1 — Enterprise / Org aggregate (April 10, 2026):
  Pre-aggregated CCA active user counts (daily/weekly/monthly)
  Endpoint: GET /enterprises/{e}/copilot/metrics
            GET /orgs/{o}/copilot/metrics
  No join required; read pre-computed fields directly.
  Ref: docs-github-copilot-cca-usage-metrics-aggregate.md

Layer 2 — Team level (May 14, 2026, THIS CHANGELOG):
  User-teams JOIN per-user usage data → group by team_slug
  Endpoint: GET /enterprises/{e}/copilot/metrics/reports/user-teams-1-day
            GET /orgs/{o}/copilot/metrics/reports/user-teams-1-day
  JOIN required; data engineering pipeline needed.
  Caveat: < 5 users → suppressed; multi-team users counted in each team.

Layer 3 — Individual user level (March 25, 2026 predecessor):
  Per-user flag (used_copilot_coding_agent) in per-user usage report
  Granularity: individual user records; available directly.

Missing layer (as of May 14, 2026):
  Task/session level — no per-task CCA outcome data in the API.
```

## Cross-References

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md` (April 10, 2026):
  That note documents pre-aggregated org/enterprise-level CCA active user counts
  (Claim 1) and identifies team-level attribution as the missing measurement layer
  (Concrete Artifacts → Multi-Surface Copilot Adoption Metrics Landscape section).
  This source fills that gap. The two notes are complementary: org/enterprise
  aggregates for fleet dashboards; team-level JOIN for cohort targeting and
  champion identification. Important distinction: April 10 = read a field; May 14
  = implement a join pipeline. Not interchangeable in harness design.
- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 5 (admin-only
  access restriction): The same access tier constraint applies here. This is the
  third consecutive Copilot metrics release (April 8, April 10, May 14) with the
  same restriction, confirming it is a stable policy, not a per-release exception.
- **Corroborates** `docs-github-copilot-cca-usage-metrics-aggregate.md` overall
  pattern (incremental API surface expansion by dimension): GitHub is methodically
  adding one new measurement dimension per release. This release continues that
  pattern with team as the new grouping dimension.
- **Contradicts**: None found. No existing source note claims team-level Copilot
  metrics are infeasible or unplanned. The April 10 note identifies team-level as
  an open gap; this source fills it. This is extension, not contradiction.
- **Novel**:
  - First source in the corpus to document team-level Copilot usage metrics as
    a queryable dimension.
  - The JOIN-based approach to metrics (versus pre-aggregated fields) is new to
    the corpus — introduces a data engineering requirement not present in prior
    metrics notes.
  - The < 5 user suppression threshold is new to the corpus. No prior source
    discusses privacy thresholds in the Copilot metrics API.
  - The multi-team user double-counting caveat is new to the corpus. No prior
    source discusses non-additivity of team-level metric aggregates.
  - Signed download URL semantics for NDJSON reports are new to the corpus.

## Guide Impact

### Chapter 05: Measurement — team-level adoption metrics

- **Section "Measuring agentic AI adoption at team level"** (add): Reference the
  user-teams report as the infrastructure for team-level Copilot metrics. Note
  that this is a JOIN-based approach requiring a data engineering pipeline, not
  a pre-aggregated read. The granularity model is now four layers: enterprise
  aggregate → org aggregate → team (JOIN) → individual user records.
- **Section "Metrics suppression thresholds"** (add): Explicitly document the
  < 5 user suppression rule. Teams with fewer than five Copilot users will have
  no entry in the team-level report. Dashboards must handle absent entries as
  "suppressed" not "zero." Failing to handle this correctly produces silent data
  gaps in team-level adoption tracking.
- **Section "Non-additive metrics"** (add or extend): Use multi-team user counting
  as a concrete example of non-additive metrics — team counts cannot be summed to
  org counts. This is an instance of the general problem of double-counting in
  hierarchical aggregations; explicitly flag that reconciliation checks between
  team sums and org totals will always show discrepancies for multi-team orgs.
- **Section "API-only metrics pipeline"** (add): The Copilot metrics series
  (April 8, April 10, May 14) is consistently REST API-only with no dashboard.
  Teams wanting visualizations must build a data pipeline. Reference GitHub's
  join and rolling-window documentation as the prescribed starting point.

### Chapter 02: Harness Engineering — Observability

- **Section "Team-level fleet observability"** (add): Introduce the harness-level
  pattern for team-level Copilot adoption: fetch signed NDJSON from user-teams
  endpoint → JOIN with per-user usage data → aggregate by team_slug. The harness
  must handle: signed URL expiry (re-fetch before use), NDJSON preprocessing for
  SQL engines, team suppression rendering (< 5 users), and non-additive team totals
  (no cross-layer reconciliation).
- **Section "Admin-privileged observability services"** (add or extend): The
  consistent admin-only access pattern across all three recent Copilot metrics
  releases (April 8, April 10, May 14) means harness components retrieving Copilot
  metrics must run under an admin-privileged service account. Individual engineer
  or team lead credentials will not work. This should be a named architectural
  requirement, not a footnote.

## Extraction Notes

1. **Source is thin by design**: This is a product changelog (~300 words). The
   eight claims above exhaust what the source asserts; do not cite this changelog
   for more than it contains.
2. **Two WebFetch calls**: First call returned a structured summary; second call
   returned a version with phrasing in quotation marks likely drawn verbatim from
   the source. Quotes in this note that appeared in quotation marks in the WebFetch
   response are used as the `Quote` field; other claims use
   `(no direct quote; see paraphrase in Our assessment)`.
3. **Join documentation not fetched separately**: Claim 8 documents the existence
   of GitHub's step-by-step join guide; the specific join recipe from that linked
   docs page is not included in this note and should be fetched separately if a
   code-level implementation guide is needed.
4. **No contradictions to file**: No existing source note opposes the introduction
   of team-level metrics or the JOIN approach. The April 10 note explicitly leaves
   team-level as an open gap; this source fills it. This is extension, not
   contradiction.
5. **NDJSON preprocessing**: The user-teams report is NDJSON. Teams using SQL
   databases will need a load step (e.g., `jq` to extract fields, then `COPY`
   into a staging table, or a streaming platform load). This is derivable from
   standard NDJSON semantics and not explicitly stated in the source — flagged
   here as an implementation concern for Ch02 harness guidance.
