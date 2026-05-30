---
source_url: https://github.blog/changelog/2026-05-29-copilot-usage-metrics-api-adds-cohorts-for-ai-adoption
source_type: docs
title: "Copilot usage metrics API adds cohorts for AI adoption"
author: GitHub (official changelog)
date_published: 2026-05-29
date_extracted: 2026-05-30
last_checked: 2026-05-30
status: current
confidence_overall: settled
issue: "#1001"
---

# Copilot Usage Metrics API — Adoption Phase Cohorts (GitHub Changelog, May 29, 2026)

> GitHub's May 29, 2026 changelog introduces a four-phase adoption cohort model to the
> Copilot usage metrics API — classifying each engaged user into Code First, Agent First,
> or Multi-agent based on 28-day rolling engagement — adding a behavioral segmentation
> layer on top of the existing aggregate counts (April 10) and team attribution (May 14).

## Source Context

- **Type**: docs (GitHub official product changelog, ~250 words, May 29, 2026)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these fields exist, the four phase definitions, the
  28-day window basis, and the `version` field mechanism. Not a credible source for any
  claim about whether the phase model accurately captures adoption maturity, or whether
  users actually progress linearly through the phases — no usage outcome data is cited.
- **Scope**: Two new API fields (`ai_adoption_phase` on user-level reports;
  `totals_by_ai_adoption_phase` array on enterprise/org reports), the four phase
  definitions, the 28-day classification window, the `version` field for schema evolution,
  the per-phase metric set, and the explicit capability to combine with the teams filter.
  Does NOT cover: how GitHub determines "engaged" vs. non-engaged users (the engagement
  threshold triggering phase assignment is undefined); what fraction of real org users
  fall into each phase; whether phase progression is monotonic or users can regress; any
  SLA on how frequently the 28-day window is recalculated; or guidance on what a "good"
  distribution across phases looks like.

## Extracted Claims

### Claim 1: A new `ai_adoption_phase` field on user-level reports classifies each engaged Copilot user into one of four adoption phases based on their product engagement over a rolling 28-day window

- **Evidence**: Official GitHub product changelog announcing the feature with explicit
  field name, window duration, and report placement.
- **Confidence**: settled (product fact — the field exists and the design is documented)
- **Quote**: "GitHub's Copilot usage metrics API now classifies engaged users into AI adoption phases based on 28-day rolling window data. A fresh `ai_adoption_phase` field appears on user-level reports"
- **Our assessment**: The 28-day window aligns with the existing
  `monthly_active_copilot_cloud_agent_users` field (also 28-day, per April 10 changelog).
  This alignment means a user's monthly active status and their phase assignment are
  computed over the same time horizon, enabling consistent side-by-side analysis. The
  "engaged users" qualifier is notable — the changelog does not define the engagement
  threshold, so it is unclear whether Phase 0 users are "engaged but unclassified" or
  "not engaged at all." Teams building dashboards should treat Phase 0 carefully: it may
  represent inactive licensed users, not a meaningful adoption cohort.

### Claim 2: Phase 0 (No cohort) identifies users who did not meet the engagement criteria for any adoption phase

- **Evidence**: Official phase definition from the product changelog.
- **Confidence**: settled (definitional — this is the explicit phase description)
- **Quote**: "User did not meet the engagement criteria for any phase."
- **Our assessment**: Phase 0 is essentially the null state — useful as a denominator
  (total licensed users minus Phase 0 = users who have engaged at any level), but not
  an actionable adoption cohort in itself. The undefined "engagement criteria" is a gap:
  teams cannot determine from this changelog alone whether a user with zero completions
  is in Phase 0 or simply absent from the report. Treating the Phase 0 count as a
  proxy for "inactive licensed users" is plausible but unconfirmed.

### Claim 3: Phase 1 (Code first) covers users who engaged with code completion and/or IDE agent mode

- **Evidence**: Official phase definition from the product changelog.
- **Confidence**: settled (definitional)
- **Quote**: "User engaged with code completion and/or IDE agent mode."
- **Our assessment**: Phase 1 represents the baseline Copilot use case — IDE-based
  assistance. The "and/or" framing means this phase does NOT require both surfaces; a
  user who only uses code completions qualifies. This is architecturally important: IDE
  agent mode is explicitly in Phase 1, not Phase 2, despite being an agentic surface.
  GitHub's classification treats IDE agent mode as part of the "code-first" baseline,
  reserving the "Agent first" label (Phase 2) for GitHub-based cloud agent surfaces.
  Teams using this to measure agentic adoption should note: Phase 1 includes IDE agent
  mode users, so "Phase 2 and above" is the threshold for cloud/web agent adoption.

### Claim 4: Phase 2 (Agent first) covers users who engaged with a single GitHub-based agent surface — Copilot cloud agent, Copilot code review, or Copilot CLI

- **Evidence**: Official phase definition from the product changelog.
- **Confidence**: settled (definitional)
- **Quote**: "User engaged with a single GitHub-based agent surface (i.e., Copilot cloud agent, Copilot code review, or Copilot CLI)."
- **Our assessment**: The enumeration of three surfaces (cloud agent, code review, CLI)
  is the authoritative list of "GitHub-based agent surfaces" as of May 29, 2026. The
  phrase "single... surface" is the distinguishing criterion between Phase 2 and Phase 3
  — one surface qualifies for Agent first; two or more surface qualifies for Multi-agent.
  This makes Phase 2 users the prime target for cross-surface enablement: they have
  demonstrated agentic capability on one surface and are one step from multi-agent
  adoption. For enablement teams, the Phase 2 cohort is the highest-leverage group
  to push toward Phase 3.

### Claim 5: Phase 3 (Multi-agent) covers users who engaged with two or more GitHub-based agent surfaces, or with the new GitHub Copilot app

- **Evidence**: Official phase definition from the product changelog.
- **Confidence**: settled (definitional)
- **Quote**: "User engaged with two or more GitHub-based agent surfaces, or with the new GitHub Copilot app."
- **Our assessment**: Phase 3 has two independent qualification paths: (1) multi-surface
  engagement across the enumerated GitHub-based agent surfaces (cloud agent, code review,
  CLI), or (2) any engagement with the new GitHub Copilot app — which apparently qualifies
  as multi-agent independently. This suggests GitHub considers the Copilot app to be
  inherently a multi-agent surface, not a single surface counted alongside the others.
  The Copilot app's standalone Phase 3 qualification is notable and warrants monitoring
  as the app matures — it could inflate Phase 3 counts relative to a pure multi-surface
  reading.

### Claim 6: A `totals_by_ai_adoption_phase` array on enterprise and organization reports exposes aggregate metrics broken down by phase

- **Evidence**: Official field announcement with explicit placement at enterprise/org report level.
- **Confidence**: settled (product fact)
- **Quote**: "`totals_by_ai_adoption_phase` arrays surface metrics at enterprise and organization levels"
- **Our assessment**: The array model means phase-level aggregate data is pre-computed
  server-side (similar to the April 10 aggregate CCA counts), not requiring client-side
  aggregation. This is architecturally different from the May 14 team-level metrics, which
  require a client-side JOIN. For harness engineering: consuming phase-level org totals
  is a simple array read; consuming team-level metrics requires a download + JOIN pipeline.
  The two capabilities complement each other but require different integration patterns.

### Claim 7: Per-phase metrics include: engaged users, interaction averages, code generation/acceptance activity, lines added/deleted, pull request metrics, and median time-to-merge averages

- **Evidence**: Explicit enumeration of per-phase metric fields in the official changelog.
- **Confidence**: settled (stated metric coverage)
- **Quote**: "Enterprise and organization reports group metrics by phase, tracking: engaged users, interaction averages, code generation/acceptance activity, lines added/deleted, pull request metrics, and median time-to-merge averages."
- **Our assessment**: The inclusion of median time-to-merge within each phase is the
  most analytically significant metric here — it enables comparing delivery velocity
  across adoption phases. If Phase 3 (Multi-agent) users show materially lower
  time-to-merge than Phase 1 users, that constitutes evidence for a productivity
  correlation with deeper agentic adoption. However, this is observational data from
  a single vendor's tool, and selection bias is severe: users who adopt more agent
  surfaces may already be higher-velocity developers. The metric is available; causal
  inference requires additional experimental design. Note: "averages per user within
  each phase" is the aggregation level, per the changelog.

### Claim 8: Each phase object includes a `version` field (starting at `v1`) enabling classification logic to evolve without breaking historical data

- **Evidence**: Explicit statement in the official changelog about the versioning mechanism.
- **Confidence**: settled (stated design intent for schema evolution)
- **Quote**: "Each phase includes a `version` field (starting at `v1`) enabling classification logic evolution without breaking historical data."
- **Our assessment**: This versioning mechanism is operationally significant for teams
  building pipelines. The `version` field is essentially a signal for "which phase
  definition was in effect when this classification was computed." If GitHub revises the
  criteria for (say) Phase 2 in a future update, historical records retain the `v1`
  label, while new records get a `v2` label. Teams should store the `version` field
  alongside the phase value in any data warehouse, and treat phase comparisons across
  versions as potentially inconsistent. This is similar to schema migration design
  patterns seen in the April 10 `coding_agent` → `cloud_agent` rename (which did NOT
  use a versioning mechanism, causing migration pain); the `version` field here reflects
  a more disciplined schema evolution approach.

### Claim 9: Phase cohort data can be combined with the teams filter for simultaneous team-level and phase-level analysis

- **Evidence**: Explicit statement in the "Important Notes" section of the official changelog.
- **Confidence**: settled (stated as supported capability in official changelog)
- **Quote**: "Users can combine this with the teams filter for enhanced granularity."
- **Our assessment**: This is the most architecturally significant claim in the source
  for guide purposes. Combining phase cohorts with the May 14 team-level attribution
  produces a two-dimensional view: which teams have which phase distributions. This
  enables operational patterns such as: "Team A has 40% Phase 3 users; Team B has 80%
  Phase 0 users — target Team B for enablement." The exact mechanism for combining
  ("the teams filter") implies that the phase data is filterable rather than requiring
  a separate JOIN, suggesting a simpler integration than the May 14 NDJSON download
  pattern. The changelog does not detail the teams filter API parameter.

### Claim 10: Access requires enterprise administrator or organization owner status with Copilot usage metrics REST API permissions

- **Evidence**: Explicit access tier statement in the official changelog's "Important Notes" section.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Access requires enterprise administrator or organization owner status with Copilot usage metrics REST API permissions."
- **Our assessment**: Consistent with the access tier documented across the full Copilot
  metrics API series (April 8, April 10, May 14). The May 14 source additionally noted
  a "View Enterprise Copilot Metrics" custom role as an access path; this changelog does
  not mention that custom role explicitly. It is likely still valid (the role grants
  metrics API access broadly), but the changelog's wording returns to the simpler
  "enterprise administrator or organization owner" framing.

### Claim 11: GitHub frames the three intended use cases as: maturity storytelling, cohort progression tracking, and targeted enablement

- **Evidence**: Explicit "Why This Matters" section in the official changelog listing
  three use case bullets.
- **Confidence**: anecdotal (vendor framing of intended use; no evidence that real
  organizations have successfully used the phase model for these purposes)
- **Quote**: "Tell the maturity story: Progress beyond active-user counts toward capability adoption visibility" / "Track cohort progression: Monitor users advancing from code-first to agent-first and multi-agent workflows" / "Target enablement: Direct training and rollout programs toward phases showing greatest opportunity"
- **Our assessment**: The first use case ("tell the maturity story") is the most
  differentiated from prior metrics: aggregate active-user counts answer "how many
  users?" while phase data answers "at what capability level?" The second ("track
  cohort progression") assumes users move upward through phases over time — an
  assumption the API does not validate. The 28-day rolling window resets classification
  continuously, so a user who stops using agent surfaces would drop from Phase 2 to
  Phase 1 or 0 — the API measures current engagement, not cumulative achievement.
  The third ("target enablement") is the highest-leverage use case: identifying which
  phase has the most users and designing targeted training accordingly is a concrete,
  actionable pattern for adoption teams.

## Concrete Artifacts

### Adoption Phase Model (from changelog, May 29, 2026)

```
# Copilot ai_adoption_phase — four-phase model
# Based on: 28-day rolling window of user engagement
# Field location: user-level reports (per-user field)
# API version: 2026-03-10 (Copilot usage metrics API)

Phase 0 — No cohort
  Definition: User did not meet the engagement criteria for any phase.
  Interpretation: inactive or below engagement threshold; not an actionable cohort

Phase 1 — Code first
  Definition: User engaged with code completion and/or IDE agent mode.
  Surfaces: IDE code completion, IDE agent mode
  Interpretation: baseline Copilot adoption (core IDE surfaces)

Phase 2 — Agent first
  Definition: User engaged with a single GitHub-based agent surface
              (i.e., Copilot cloud agent, Copilot code review, or Copilot CLI).
  Surfaces: Copilot cloud agent, Copilot code review, Copilot CLI (one of the three)
  Interpretation: early cloud/web agentic adoption; prime target for cross-surface enablement

Phase 3 — Multi-agent
  Definition: User engaged with two or more GitHub-based agent surfaces,
              or with the new GitHub Copilot app.
  Surfaces: Any two+ of {cloud agent, code review, CLI}, OR the Copilot app alone
  Interpretation: advanced agentic adoption; highest-maturity cohort

Schema evolution:
  Each phase object includes: version (string, starts at "v1")
  Purpose: enables classification logic to change without invalidating historical data
  Implication: store version field alongside phase value in any data warehouse
```

*Source: Copilot usage metrics API adds cohorts for AI adoption, GitHub Changelog, May 29, 2026*

### API Fields Added (from changelog, May 29, 2026)

```
# User-level report — new field
ai_adoption_phase
  Type: object { phase: integer (0–3), version: string }
  Location: per-user usage report rows
  Window: 28-day rolling

# Enterprise/org-level report — new field
totals_by_ai_adoption_phase
  Type: array of phase-aggregate objects
  Location: enterprise and organization reports
  Per-phase metrics: engaged_users, interaction_averages,
                     code_generation_and_acceptance_activity,
                     lines_added, lines_deleted,
                     pull_request_metrics,
                     median_time_to_merge_averages
  Aggregation: averages per user within each phase

# Filter capability
teams filter (existing)
  Can be combined with phase data for team × phase cross-analysis
```

*Source: Copilot usage metrics API adds cohorts for AI adoption, GitHub Changelog, May 29, 2026*
*(Note: exact JSON field names for the phase object and totals array are described in changelog prose;
the structured form above is an interpretation from that description — confirm against the linked API docs)*

### Copilot Usage Metrics Granularity Map (as of May 29, 2026)

```
Copilot Usage Metrics — Full Granularity Hierarchy

Tier 1 — Enterprise-level aggregate (pre-computed, direct field):
  GET /enterprises/{enterprise}/copilot/metrics
  → CCA active users: daily/weekly/monthly (added April 10, 2026)
  → monthly_active_agent_users (IDE agent mode, pre-existing)
  → totals_by_ai_adoption_phase array  ← NEW May 29, 2026

Tier 2 — Org-level aggregate (pre-computed, direct field):
  GET /orgs/{org}/copilot/metrics
  → same aggregate fields and totals_by_ai_adoption_phase  ← NEW May 29, 2026

Tier 3 — Per-user usage (per-user rows, direct field):
  → used_copilot_coding_agent flag (added March 25, 2026)
  → ai_adoption_phase object (phase 0–3, version)  ← NEW May 29, 2026
  → all other per-user engagement fields

Tier 4 — Team-level (JOIN required, NDJSON download — added May 14, 2026):
  GET /enterprises/{enterprise}/copilot/metrics/reports/user-teams-1-day
  GET /orgs/{org}/copilot/metrics/reports/user-teams-1-day
  → join to Tier 3 on user_id+day, then aggregate
  → combinable with phase cohort data via "teams filter"  ← NOTED May 29, 2026

Missing (as of May 29, 2026):
  Phase progression over time (historical phase tracking)  → not available
  Definition of "engaged" threshold for phase assignment  → not documented
  Task completion / outcome metrics by phase              → not available
  Dashboard surface for phase data                        → not confirmed available
```

*Compiled from: April 10, May 14, and May 29, 2026 GitHub changelogs*

## Cross-References

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md`:
  - Claim 4 (`monthly_active_copilot_cloud_agent_users` — 28-day window): The April 10
    source established the 28-day window as the standard for monthly CCA active user
    counts. This source uses the same 28-day window for phase classification, creating
    natural alignment: a user's monthly CCA active status and their Phase 2/3 assignment
    are computed over the same horizon. Together they answer different questions: "How
    many users used CCA this month?" (aggregate count) vs. "At what adoption phase is
    each user?" (behavioral segmentation).
  - Claim 6 (multi-surface Copilot adoption view): The April 10 source described the
    metrics as giving "a full view of Copilot adoption across surfaces." The May 29 phase
    model extends this by providing structured behavioral segmentation across those same
    surfaces — moving from "how many users per surface" to "at what multi-surface
    maturity level is each user."

- **Extends** `docs-github-copilot-team-level-usage-metrics.md`:
  - Claim 1 (team-level JOIN pattern): The May 14 source introduced team-level metrics
    via a NDJSON download + JOIN approach. This source explicitly notes that phase cohort
    data "can combine with the teams filter for enhanced granularity" (Claim 9 here),
    enabling a team × phase cross-analysis. The two capabilities together answer: "Which
    teams have the most users stuck in Phase 1?" — a question neither source alone can
    answer.
  - Claim 6 (identifying adoption champions and gaps via team metrics): The May 14 source
    framed team-level metrics as a tool to "identify champions and gaps." The phase model
    provides a new dimension for this: teams can now be characterized not just by active
    user count but by phase distribution, making the "champion team" definition more
    precise — a team where 60% of users are Phase 3 is demonstrably more advanced than a
    team where 60% are Phase 1.

- **Corroborates** `docs-github-copilot-cca-usage-metrics-aggregate.md` and
  `docs-github-copilot-team-level-usage-metrics.md` access tier (enterprise admin/org owner):
  All three Copilot metrics changelog sources (April 10, May 14, May 29) document the same
  access restriction. This is a consistent, settled constraint across the entire metrics API
  surface.

- **Novel**:
  - **Behavioral segmentation vs. activity counts**: No prior source in the corpus
    classifies users by adoption behavior. All prior Copilot metrics notes measure
    "how many users did X" (activity counts). The phase model answers "what level of
    multi-surface sophistication has each user reached?" — a qualitatively different
    question.
  - **The four-phase taxonomy**: Code first → Agent first → Multi-agent is GitHub's
    official model for describing Copilot adoption maturity. No prior source in the
    corpus defines or endorses a staged adoption model for Copilot. This is the first
    vendor-provided framework for Copilot adoption stage classification.
  - **`version` field for schema evolution**: No prior Copilot metrics source documents
    a versioning mechanism for classification logic. The April 10 source documented the
    `coding_agent` → `cloud_agent` rename as a breaking migration with no version field;
    the `version` approach here is a more disciplined evolution pattern.
  - **Time-to-merge as a per-phase metric**: No prior source in the corpus documents
    a Copilot metrics API field for time-to-merge. If this is accurate (the changelog
    is brief and may be simplified), it introduces a delivery velocity metric into the
    Copilot observability API for the first time.
  - **Copilot app as standalone Phase 3 qualifier**: The new GitHub Copilot app
    independently qualifies a user for Phase 3 (multi-agent), distinct from the
    three-surface model for cloud agent/code review/CLI. This "app = multi-agent"
    framing is novel to the corpus.

## Guide Impact

### Chapter 05: Measurement — Copilot Adoption Maturity

- **Section "Beyond active-user counts"** (add or extend): Reference the phase model as
  the canonical mechanism for moving from "breadth of adoption" (active user counts) to
  "depth of adoption" (phase distribution). Specifically: Phase 1 = code-first baseline;
  Phase 2 = single agent surface adoption; Phase 3 = multi-surface or app-level maturity.
  The phase taxonomy gives concrete, measurable criteria for what "mature Copilot adoption"
  looks like — a gap in all prior sources in the corpus.
- **Section "Cohort progression analysis"** (new): Document the phase model as an
  adoption progression framework, but with the caveat that the 28-day window measures
  *current* behavior, not cumulative achievement. A user who drops agent usage will drop
  phases. Recommend tracking phase distribution over time (monthly snapshots) rather than
  treating phase as a permanent label.
- **Section "Per-phase delivery metrics"** (add): If the median time-to-merge metric is
  confirmed in the API docs, add it as the first example of a delivery-velocity metric
  in the Copilot metrics API. Note the selection-bias risk in interpreting cross-phase
  velocity differences as causal.
- **Section "Team × phase cross-analysis"** (add): Document the capability to combine
  the May 14 team filter with May 29 phase data, enabling "which teams are stuck at
  which adoption phase?" — the primary use case for adoption managers and engineering
  leaders. This is the highest-value combination of the two changelog sources.

### Chapter 02: Harness Engineering — Observability Pipelines

- **Section "Enterprise Copilot observability pipeline"**: Add the phase cohort tier to
  the metrics architecture. The `totals_by_ai_adoption_phase` array is a direct API
  field (like April 10 aggregates, no JOIN needed), so it belongs in the same pipeline
  tier as the CCA aggregate counts. Note: `version` field must be stored alongside phase
  values to enable future-safe historical comparison.
- **Section "Schema stability and versioning"**: Reference the `version` field mechanism
  as an example of versioned classification — a more resilient approach than the
  `coding_agent` → `cloud_agent` rename documented in the April 10 source. When building
  pipelines against classification fields, treat the `version` value as a mandatory
  schema tag.

## Extraction Notes

1. **Source is a short product changelog (~250 words)**: All substantive claims are
   extracted in the eleven claims above. The source is exhausted — no additional signal
   would come from re-reading.
2. **Two WebFetch passes**: Two separate fetches were made. The first pass used a
   verbatim extraction prompt and returned phase definitions in the form "User did/engaged..."
   which matches the technical definition style of a GitHub API changelog. The second pass
   returned a slightly summarized form. The first pass's wording is used for all phase
   definition quotes; it has higher fidelity to the source. The Assayer should verify these
   quotes against the source URL, as WebFetch applies model processing that may affect
   character-exact fidelity.
3. **Engagement threshold undefined**: The source does not define what level of activity
   constitutes "engagement" for phase classification purposes. The threshold is likely
   documented in the linked API docs page (not separately fetched). This gap is noted in
   Claims 1 and 2.
4. **"Teams filter" mechanism unspecified**: Claim 9 notes the teams filter can be combined
   with phase data, but the changelog does not describe the API parameter name or whether
   this is a server-side filter or client-side operation. This is a gap — the May 14 NDJSON
   approach required client-side JOIN; the "teams filter" wording implies a simpler
   server-side filter, but this is not confirmed.
5. **Time-to-merge field**: The changelog mentions "median time-to-merge averages" as a
   per-phase metric. This would be a new metric type in the Copilot API if accurate. Field
   name confirmation requires checking the linked API documentation.
6. **No contradictions filed**: The phase model is additive to the existing April 10 and
   May 14 capabilities. No existing source note claims the API cannot segment by adoption
   stage, or that phase classification is inappropriate. The introduction of Phase 3 via
   the Copilot app as a standalone qualifier is novel but not contradictory to any prior claim.
7. **The Copilot app**: Phase 3's inclusion of "the new GitHub Copilot app" references a
   product not previously documented in the corpus. The app's capabilities and how it differs
   from the existing GitHub Copilot surfaces are not described in this changelog. Teams
   assessing Phase 3 counts should note that the app qualifier may reflect Copilot app
   adoption as much as multi-surface engineering sophistication.
