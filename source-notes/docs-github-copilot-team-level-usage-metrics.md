---
source_url: https://github.blog/changelog/2026-05-14-team-level-copilot-usage-metrics-now-available-via-api
source_type: docs
title: "Team-level Copilot usage metrics now available via API"
author: GitHub (official changelog)
date_published: 2026-05-14
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: settled
issue: "#758"
---

# Team-Level Copilot Usage Metrics via User-Teams Report (GitHub Changelog)

> GitHub's May 14, 2026 changelog introduces team-level Copilot metrics via a new
> user-teams report and JOIN pattern, adding a distinct granularity tier below the
> org/enterprise aggregate counts announced April 10, 2026 — with material operational
> constraints around privacy thresholds and multi-team user counting.

## Source Context

- **Type**: docs (GitHub official product changelog, ~350 words, May 14, 2026)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these endpoints exist, the NDJSON data model, the
  JOIN recipe, and the operational constraints. Not a credible source for any outcomes
  from team-level metric adoption — the changelog contains no usage data or outcome
  evidence.
- **Scope**: The new `user-teams-1-day` report endpoint, the data model for that report,
  the join-and-aggregate pattern for computing team-level metrics, access controls, and
  four "important notes" covering operational constraints. The linked docs page (referenced
  but not fetchable at extraction time — see Extraction Notes) covers the step-by-step
  join recipe, day-level aggregation, and rolling-window pattern. Does NOT cover: what
  counts as a Copilot "active user" at team level (that definition lives in the per-user
  usage report, not here); how team membership changes affect historical metric comparisons;
  any guidance on what team adoption rates are "good"; or timeline for when a dashboard
  surface might be added.

## Extracted Claims

### Claim 1: A new user-teams report maps each Copilot-licensed user to their team memberships, enabling team-level metrics by joining with the per-user usage report

- **Evidence**: Official GitHub product changelog stating the new report's purpose and
  the join operation required to produce team-level metrics.
- **Confidence**: settled (product fact — the endpoint exists and the design is documented)
- **Quote**: "The Copilot usage metrics API now exposes a new user-teams report that maps
  each Copilot-licensed user to the teams they belong to. By joining the user-teams report
  with the existing per-user usage report, enterprise administrators and organization owners
  can produce team-level Copilot usage metrics for any team in their organization or enterprise."
- **Our assessment**: This is architecturally distinct from the org/enterprise aggregate fields
  announced April 10, 2026. That release added pre-computed aggregate counts as direct JSON
  fields (no computation required). This release adds a raw report that requires a JOIN
  operation to produce team-level metrics. The two approaches differ in operational model:
  aggregate fields are suited for real-time dashboards; the JOIN pattern requires a pipeline
  that downloads NDJSON, performs the join, and aggregates. Teams building observability
  infrastructure need to handle both surfaces distinctly.

### Claim 2: Two new REST API endpoints return signed download URLs to NDJSON-formatted user-teams reports at the enterprise and organization levels

- **Evidence**: Official changelog enumerates both endpoints explicitly.
- **Confidence**: settled (definitional — these endpoints either exist or not)
- **Quote**: "Two new endpoints return signed download URLs to NDJSON reports"
- **Our assessment**: The NDJSON format and "signed download URL" delivery model is
  different from the existing Copilot metrics API endpoints that return JSON responses
  directly. Teams building pipelines against these endpoints need to handle: (1) a
  redirect to a signed URL, (2) NDJSON parsing (one JSON object per line, not a JSON
  array), and (3) the fact that the URL is time-limited (signed URLs expire). This is
  a different integration pattern than querying `GET /orgs/{org}/copilot/metrics` for
  the aggregate fields documented in the April 10 changelog.

### Claim 3: Each row in the user-teams report represents a team membership for a given day, with fields for team enterprise/org ID, team slug, user ID, and user login

- **Evidence**: Direct field-level data model stated in the official changelog.
- **Confidence**: settled (definitional data model)
- **Quote**: "Each row in the user-teams report represents a team membership for a given
  day, including the team's enterprise or organization id, team slug, and the user's ID
  and login."
- **Our assessment**: The join key is `user_id` and `day`, which links to the matching
  fields in the per-user usage report. The day-level granularity means a user who belongs
  to three teams will have three rows per day in the user-teams report (one per team),
  each joinable to the same usage row for that user-day combination. This is the foundation
  of Claim 8's multi-team counting caveat: because the join is one-to-many from usage to
  team memberships, a single day's usage activity fans out into each team the user belongs
  to, making team totals non-additive.

### Claim 4: Team-level metrics are produced by joining the user-teams report to the per-user usage report on user_id and day, then aggregating

- **Evidence**: Explicit recipe stated in the official changelog.
- **Confidence**: settled (stated join recipe from official documentation)
- **Quote**: "To produce team-level metrics, join the user-teams report to the per-user
  usage report on user_id and day, then aggregate."
- **Our assessment**: The three-step recipe (download user-teams, download per-user usage,
  join on user_id+day and aggregate) is the canonical approach. Notably, this is a
  client-side operation — GitHub provides the raw reports; the aggregation is performed
  by the consumer. This contrasts with the April 10 aggregate fields, which are pre-aggregated
  server-side. For harness engineering: teams building team-level dashboards must build a
  data pipeline that periodically fetches both reports, performs the join, and materializes
  the results. There is no "query once and get team metrics" endpoint.

### Claim 5: The user-teams metrics cover the full Copilot feature surface: IDE completions, chat, Copilot CLI, code review, and Copilot cloud agent activity, with breakdowns by language, IDE, feature, or model

- **Evidence**: Changelog states coverage under the "Full feature coverage" benefit and
  also in the intro paragraph.
- **Confidence**: settled (explicit feature coverage statement from official changelog)
- **Quote**: "Team-level breakdowns are available across IDE completions, chat, Copilot
  CLI, code review, and Copilot cloud agent activity. They can be cut by language, IDE,
  feature, or model."
- **Our assessment**: This means the team-level view is as dimensionally rich as the
  per-user view — the same dimensions available for individual user analysis are now
  available at the team cohort level. For Claim 1 in `docs-github-copilot-cca-usage-metrics-aggregate.md`,
  the aggregate note covers only CCA active-user counts at org/enterprise level. This
  source confirms that at the team level, CCA activity is one of five feature surfaces
  available, alongside IDE completions and chat — providing full adoption coverage across
  all Copilot surfaces at team granularity.

### Claim 6: These metrics enable "identifying adoption champions and gaps" by showing which teams are driving adoption and which need enablement

- **Evidence**: Stated explicitly in the changelog's "Identify champions and gaps" benefit
  section.
- **Confidence**: anecdotal (vendor framing of intended use case; no evidence that teams
  actually use it this way or that it produces actionable signals)
- **Quote**: "Identify champions and gaps: See which teams are driving adoption and which
  need enablement, so you can target campaigns and rollout investments."
- **Our assessment**: The use case framing (champions vs. laggards) is plausible and
  represents a standard enterprise adoption management pattern: identify high-adoption
  teams, study their practices, and apply them to low-adoption teams. However, the
  changelog provides no evidence that this strategy works, nor does it define what
  "champion" thresholds look like. This is vendor-intended use framing, not a documented
  outcome. Teams building dashboards around this pattern should define their own adoption
  threshold criteria rather than treating this claim as prescriptive.

### Claim 7: Access requires enterprise administrator, organization owner, billing manager, or "View Enterprise Copilot Metrics" enterprise custom role

- **Evidence**: Explicit access tier statement in the official changelog.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "These metrics are available through the REST API to enterprise administrators,
  organization owners, billing managers, and people with an enterprise custom role with
  the View Enterprise Copilot Metrics permission."
- **Our assessment**: The same access tier documented in `docs-github-copilot-pr-review-metrics.md`
  (Claim 5) and `docs-github-copilot-cca-usage-metrics-aggregate.md` (implicitly through the
  enterprise/org admin context). The "View Enterprise Copilot Metrics" custom role is notable:
  it creates a dedicated role for analytics consumers who don't need full admin access, enabling
  organizations to grant metrics access to data analysts or engineering managers without
  granting admin rights. This is operationally significant for large enterprises where
  admin privileges are tightly governed.

### Claim 8: Teams with fewer than five Copilot-seated users are excluded from the user-teams report — but their members' individual activity remains visible in the per-user usage report

- **Evidence**: Explicit constraint stated in the "Important notes" section of the changelog.
- **Confidence**: settled (explicitly documented behavioral constraint)
- **Quote**: "Teams with fewer than five Copilot-seated users are excluded from the
  user-teams report, though their members' individual activity remains visible in the
  per-user usage report."
- **Our assessment**: This is a privacy threshold. By excluding teams smaller than five
  from the aggregated view, GitHub prevents reverse-engineering individual user activity
  from team-level aggregates (a single-person team's aggregate would trivially reveal
  that person's activity). The "but their members' individual activity remains visible in
  the per-user usage report" clause is important: the individual data is still there; it
  just doesn't get the team-level JOIN attribution for small teams. For teams building
  dashboards: small teams (<5 Copilot users) will appear to have no team-level metrics
  even if their members are active. This is expected behavior, not a data pipeline bug.
  Any completeness check on team coverage must account for this threshold.

### Claim 9: Users in multiple teams have their activity counted in each team's aggregate — team totals cannot be summed to reproduce an organization or enterprise total

- **Evidence**: Explicit constraint stated in the "Important notes" section of the changelog.
- **Confidence**: settled (explicitly documented behavioral constraint — this is a
  fundamental property of the join-based counting model)
- **Quote**: "Users who belong to multiple teams will have their activity counted in each
  team's aggregate, so team totals cannot be summed to reproduce an organization or
  enterprise total."
- **Our assessment**: This is the most operationally significant constraint in the source.
  The counting model is NOT exclusive: a user in three teams contributes to all three teams'
  metrics. This means: (1) summing team totals overcounts org activity for any org with
  cross-team membership; (2) team totals are correct in isolation but must not be used for
  org-level arithmetic; (3) the org/enterprise aggregate from the April 10 API fields
  remains the canonical source for fleet-level counts. Teams building combined dashboards
  must NOT replace the aggregate-level counts with summed team counts — they serve different
  purposes and will produce different numbers.

### Claim 10: Team-level metrics are available through the REST API only — there is no dashboard surface in this release

- **Evidence**: Explicit statement in the "Important notes" section.
- **Confidence**: settled (negative product fact: dashboard does not exist)
- **Quote**: "User-teams reports are available through the REST API only. There is no
  dashboard surface for team-level metrics in this release."
- **Our assessment**: This is operationally significant: organizations that want to visualize
  team-level metrics must build their own pipeline and dashboard layer. There is no
  GitHub-native UI for team-level Copilot analytics as of May 2026. The API-only availability
  also means any consumer must manage the signed URL expiration, NDJSON parsing, and join
  computation. This is a higher-friction access pattern than the aggregate metrics, which can
  be queried directly from existing Copilot usage metrics dashboards.

### Claim 11: The changelog release also introduces step-by-step guidance in the docs covering the join recipe, day-level aggregation, and a rolling-window pattern for multi-day reporting

- **Evidence**: Explicit statement in the changelog body.
- **Confidence**: settled (the docs page is announced as part of this release)
- **Quote**: "This release also introduces step-by-step guidance in the docs covering the
  join, day-level aggregation, and a rolling-window pattern for multi-day reporting."
- **Our assessment**: The linked docs page is the canonical implementation reference for
  teams building pipelines. The "rolling-window pattern" for multi-day reporting is
  specifically mentioned — suggesting the naive approach (summing single-day reports) is
  insufficient for trend analysis and that the docs provide a specific pattern to address
  this. The docs page was not accessible at extraction time (see Extraction Notes), so
  the specific join recipe and rolling-window pattern are not reproduced here. Teams
  should consult the official docs page for the implementation recipe.

## Concrete Artifacts

### API Endpoints (from changelog, May 14, 2026)

```
# Copilot user-teams report endpoints (added May 14, 2026)
# Return signed download URLs to NDJSON reports

GET /enterprises/{enterprise}/copilot/metrics/reports/user-teams-1-day
GET /orgs/{org}/copilot/metrics/reports/user-teams-1-day

# Access tier: enterprise admin, org owner, billing manager,
#              or "View Enterprise Copilot Metrics" enterprise custom role
# Response: signed download URL → NDJSON file
# One report per day; "1-day" in path reflects the daily granularity
```

*Source: Team-level Copilot usage metrics now available via API, GitHub Changelog, May 14, 2026*

### User-Teams Report Data Model (from changelog, May 14, 2026)

```
# user-teams-1-day NDJSON report — row schema
# Each row = one team membership for one day

{
  "day": "YYYY-MM-DD",
  "team_enterprise_or_org_id": <integer>,
  "team_slug": "<string>",
  "user_id": <integer>,
  "user_login": "<string>"
}

# Join key to per-user usage report: user_id + day
# One user in N teams → N rows per day (one per team)
# Teams with < 5 Copilot-seated users: excluded from report
```

*Source: Team-level Copilot usage metrics now available via API, GitHub Changelog, May 14, 2026*
*(Note: field names inferred from changelog description; exact schema from docs page not confirmed at extraction time)*

### Metrics Granularity Hierarchy (as of May 14, 2026)

```
Copilot Usage Metrics — Granularity Hierarchy

Tier 1 — Enterprise-level aggregate (pre-computed, direct field access):
  GET /enterprises/{enterprise}/copilot/metrics
  → daily_active_copilot_cloud_agent_users (CCA-specific, added April 10, 2026)
  → monthly_active_agent_users (IDE agent mode)
  → other aggregate fields

Tier 2 — Org-level aggregate (pre-computed, direct field access):
  GET /orgs/{org}/copilot/metrics
  → same aggregate fields at org scope

Tier 3 — Per-user usage (per-user rows, direct field access):
  GET /enterprises/{enterprise}/copilot/metrics/reports/user-level-activity
  GET /orgs/{org}/copilot/metrics/reports/user-level-activity
  → one row per user per day; used_copilot_coding_agent flag; all surfaces

Tier 4 — Team-level (JOIN required, NDJSON download):   ← NEW May 14, 2026
  GET /enterprises/{enterprise}/copilot/metrics/reports/user-teams-1-day
  GET /orgs/{org}/copilot/metrics/reports/user-teams-1-day
  → join to Tier 3 on user_id+day, then aggregate
  → covers: IDE completions, chat, Copilot CLI, code review, CCA
  → constraint: teams < 5 Copilot users excluded
  → constraint: cross-team users counted per-team (totals non-additive)
  → constraint: no dashboard; REST API only

Missing:
  Team-level dashboard UI                     → not available (API only)
  Task completion / outcome metrics by team   → not available
```

*Compiled from: April 10, 2026 and May 14, 2026 GitHub changelogs*

## Cross-References

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md`:
  - Claim 1 (three new CCA aggregate fields at org/enterprise level): The April 10 source
    provides the fleet-level CCA active-user counts. This source adds team-level granularity
    for ALL Copilot surfaces including CCA. Together they provide two distinct aggregation
    tiers: fleet-wide totals (April 10) and team-level attribution (May 14). Neither
    replaces the other — fleet totals are non-additive from team subtotals due to Claim 9's
    multi-team counting constraint.
  - Claim 6 (multi-surface Copilot adoption view): The April 10 source frames the metrics
    as a "full view of Copilot adoption across surfaces." The May 14 source extends this
    view to the team granularity level, confirming that the same multi-surface coverage
    (CCA, IDE agent mode, completions, etc.) is available at team level.
  - Claim 8 (convenience vs. privacy tradeoff for aggregate fields): The April 10 source
    notes aggregate fields let admins avoid aggregating per-user data (a convenience for
    privacy-constrained environments). The May 14 source introduces a new privacy tradeoff:
    teams < 5 users are excluded entirely, rather than receiving a null, which affects
    small-team visibility.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md`:
  - Claim 5 (access restricted to enterprise admins and org owners with Copilot usage
    metrics access): Same access tier pattern. The addition of the "View Enterprise Copilot
    Metrics" custom role in the May 14 source extends this pattern — it is now possible to
    grant metrics-only access without full admin rights.

- **Corroborates** `docs-github-copilot-cca-usage-metrics-aggregate.md` (Extraction Notes
  item 4, no contradictions): Both sources are complementary layers of the same metrics
  API. No contradiction filed.

- **Novel**:
  - **Team as a queryable attribution unit**: No prior source in corpus documents a
    mechanism to attribute Copilot usage to organizational teams. The April 10 and April 8
    sources provide org/enterprise aggregates and per-user flags — team attribution is new.
  - **NDJSON download pattern**: No prior source documents the signed-URL + NDJSON
    delivery model for Copilot metrics. The existing aggregate metrics use direct JSON
    response endpoints. The NDJSON pattern has different integration requirements (time-limited
    URLs, line-by-line parsing, client-side JOIN computation).
  - **Privacy threshold for team exclusion**: The < 5 user threshold is a novel operational
    constraint not documented in any prior source. It has implications for how dashboards
    handle gaps in team coverage.
  - **Multi-team non-additivity constraint**: No prior source explicitly states that
    team-level totals cannot be summed to reproduce org/enterprise totals. This is a novel
    data modeling caveat critical to correctly interpreting team vs. fleet metrics.
  - **Dedicated "View Enterprise Copilot Metrics" custom role**: Prior sources document
    access as "enterprise admins and org owners." The introduction of a named custom role
    specifically for metrics access is a governance capability not previously documented in
    the corpus.

## Guide Impact

### Chapter 05: Measurement — Team-Level Adoption Metrics

- **Section "Measuring agentic AI adoption" (add or extend)**: Reference team-level
  metrics as the canonical mechanism for cohort-level adoption analysis. Specifically,
  document the JOIN pattern as the required approach: download user-teams and per-user
  reports, join on user_id+day, aggregate. Distinguish this from the April 10 aggregate
  fields (no JOIN needed; pre-computed; not team-addressable). Note that Ch05 currently
  lacks any team-level measurement pattern — this is the first vendor-native mechanism
  for it.
- **Section "Metrics data modeling caveats" (new section if not present)**: Add the
  non-additivity constraint (Claim 9) as a critical data modeling rule: team totals cannot
  be summed to reproduce org totals. Use org/enterprise aggregate fields for fleet-level
  counts; team-level metrics for attribution and targeting. If a dashboard shows both, they
  will not reconcile, and that is expected and correct.
- **Section "Privacy thresholds and metrics gaps" (new)**: Document the < 5 user threshold
  (Claim 8). Teams below this threshold will appear to have no team-level metrics even if
  members are active. Any completeness check on team coverage must account for this. Recommend
  that dashboards show an explicit "team excluded (< 5 users)" indicator rather than silently
  omitting small teams.

### Chapter 02: Harness Engineering — Observability Pipelines

- **Section "Enterprise Copilot observability pipeline"**: Add the team-level layer to the
  recommended observability architecture. Document that the NDJSON download + JOIN approach
  requires a data pipeline component distinct from the aggregate metrics API query. The full
  stack now includes: aggregate query (direct API → JSON), per-user query (direct API → JSON
  or NDJSON), team attribution (NDJSON download + join computation). Note the signed-URL
  expiration concern for pipeline reliability.
- **Section "Metrics access governance"**: Add the "View Enterprise Copilot Metrics" custom
  role (Claim 7) as the recommended access pattern for data analysts and engineering managers
  consuming Copilot metrics. This enables metrics access without full admin privileges — an
  important security hygiene pattern for large organizations.

## Extraction Notes

1. **Source is a short product changelog (~350 words)**: All substantive claims are extracted
   in the eleven claims above. The changelog is exhausted — no additional signal would come from
   re-reading.
2. **One WebFetch + one WP API fetch**: The changelog page redirects (HTTP 301). The final
   content was retrieved via the WordPress API (`/wp-json/wp/v2/changelogs/96113`), which
   returned the full rendered HTML content. The verbatim text in all quotes above is from that
   fetch. Two WebFetch calls to the human-readable URL returned summarized versions (WebFetch
   applies model processing); the WP API fetch returned the raw content.
3. **Docs page not accessible**: The changelog references a docs page titled "Team-level Copilot
   usage metrics" containing the step-by-step join recipe and rolling-window aggregation pattern.
   Two URL attempts (404 responses, likely auth-required) failed to retrieve this page. Claims
   about the docs page (Claim 11) are therefore based solely on the changelog's description of
   its contents. The specific join recipe and rolling-window pattern are not reproduced here.
4. **Field names inferred**: The user-teams report data model (Concrete Artifacts) lists field
   names as described in the changelog prose. The exact JSON field names from the NDJSON schema
   are not confirmed — the docs page (inaccessible) would contain the authoritative schema.
5. **No contradictions to file**: The April 10 aggregate counts and May 14 team-level metrics
   are complementary, not contradictory. The non-additivity constraint (Claim 9) is consistent
   with — and expected by — the April 10 design (aggregate counts are server-side pre-computed
   totals, not sums of team subtotals). The privacy threshold (Claim 8) is a new constraint with
   no prior corpus position to contradict.
6. **Access tier extended**: The "View Enterprise Copilot Metrics" custom role in this changelog
   is a superset of the access tier documented in prior Copilot metrics sources (which stated
   "enterprise admins and org owners only"). This is an extension, not a contradiction — the
   prior sources were accurate at their time of publication; this changelog adds a new access
   mechanism.
