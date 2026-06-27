---
source_url: https://github.blog/changelog/2026-06-26-track-total-merges-by-adoption-phase-in-enterprise-and-organization-reports
source_type: docs
title: "Track total merges by adoption phase in enterprise and organization reports"
author: GitHub (official changelog)
date_published: 2026-06-26
date_extracted: 2026-06-27
last_checked: 2026-06-27
status: current
confidence_overall: settled
issue: "#1330"
---

# Track Total Merges by Adoption Phase (GitHub Changelog, June 26, 2026)

> GitHub's June 26, 2026 changelog extends the `totals_by_ai_adoption_phase` array with a
> new `total_pull_requests_merged` aggregate count field — adding PR volume alongside the
> existing per-user average metrics, enabling proportional analysis of each adoption phase's
> share of total merged pull requests.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200–300 words, June 26, 2026)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that this field exists, what it measures, and its availability
  scope. Not authoritative for any causal claim about adoption phase effects on productivity —
  the field is a measurement primitive, not a demonstrated outcome.
- **Scope**: A single new field (`total_pull_requests_merged`) added to the
  `totals_by_ai_adoption_phase` array in the Copilot usage metrics API at enterprise and
  organization levels. Available in both 1-day and 28-day reports. Covers the field
  definition, its distinction from existing per-user average metrics, and the business
  rationale. Does NOT cover: whether total merge counts correlate with productivity; how
  to interpret cross-phase volume differences; any guidance on what a "healthy" phase
  distribution looks like; or how this interacts with the user-level `ai_adoption_phase`
  field.

## Extracted Claims

### Claim 1: A new `total_pull_requests_merged` field in the `totals_by_ai_adoption_phase` array records the aggregate count of PRs merged by all users in each adoption phase

- **Evidence**: Official GitHub product changelog announcing the feature with explicit field
  name and definition.
- **Confidence**: settled (product fact — the field exists and its definition is documented)
- **Quote**: "The total number of pull requests merged on that day by users in that adoption phase."
- **Our assessment**: This is a straightforward aggregate count — the sum of all merged PRs
  attributed to users classified in a given adoption phase. The "on that day" qualifier applies
  to the 1-day report; the 28-day report uses a rolling window. The field sits within the
  existing `totals_by_ai_adoption_phase` array (established May 29, 2026), so no new array
  structure is needed — this is an additive field to an existing per-phase object. Before this
  update, computing per-phase PR totals required client-side multiplication of `avg_pull_requests_merged`
  × `engaged_users`, an approximation that is now superseded by a direct aggregate.

### Claim 2: The new `total_pull_requests_merged` field is an aggregate total count, distinct from the existing `avg_pull_requests_merged` per-user average already in the array

- **Evidence**: Changelog explicitly references the new total as complementary to the existing
  per-user average metric and notes it uses "consistent attribution methodology with existing
  `avg_pull_requests_merged` metrics."
- **Confidence**: settled (definitional distinction stated in changelog)
- **Quote**: (no direct verbatim quote recovered; WebFetch described "consistent attribution
  methodology with existing `avg_pull_requests_merged` metrics" — see Extraction Notes)
- **Our assessment**: The distinction matters for analysis. `avg_pull_requests_merged` per user
  within a phase answers "how productive is a typical user in this phase?" while
  `total_pull_requests_merged` across the phase answers "how much of total org PR throughput
  comes from this cohort?" A phase with many users at low per-user average can produce the
  same aggregate total as a phase with few highly-productive users — the two metrics provide
  orthogonal views. Prior to this update, the array contained only per-user averages; this is
  the first aggregate total count in the `totals_by_ai_adoption_phase` array.

### Claim 3: The new field enables proportional analysis — organizations can determine each adoption phase's share of merged pull requests across the org

- **Evidence**: Changelog explicitly states this as a key use case, framing it as enabling
  organizations to "determine each adoption phase's share of merged pull requests."
- **Confidence**: settled (stated design intent; the mechanism is real even if outcomes
  depend on team context)
- **Quote**: (no direct verbatim quote recovered — see Extraction Notes)
- **Our assessment**: This is the primary guide-relevant use case. For example: a Phase 3
  (Multi-agent) cohort that accounts for 5% of licensed users but produces 25% of merged PRs
  suggests a disproportionate throughput contribution from the highest-adoption cohort.
  Conversely, a Phase 1 cohort with 80% of users producing 60% of PRs shows Code First users
  remain the dominant contributors by volume even if Phase 3 users outpace them per-user.
  Both findings are actionable for adoption program storytelling. Caveat: without a non-Copilot
  control group, this data does not establish that adoption phase causes higher PR throughput —
  Phase 3 users may simply be higher-output developers regardless of Copilot.

### Claim 4: The field is available in both 1-day and 28-day reports at the enterprise and organization level

- **Evidence**: Changelog explicitly states the availability scope as both 1-day and 28-day reports.
- **Confidence**: settled (stated in official changelog)
- **Quote**: (no direct verbatim quote recovered; both windows stated consistently in WebFetch
  output — see Extraction Notes)
- **Our assessment**: The dual-window availability mirrors the established pattern for all prior
  `totals_by_ai_adoption_phase` metrics (May 29) and the Copilot metrics API broadly (April 8,
  April 22, May 14). The 1-day granularity enables time-series tracking of volume shifts; the
  28-day window smooths daily noise for executive dashboards. The 28-day window is a rolling
  report, not a monthly average of daily values.

### Claim 5: The field uses consistent attribution methodology with the existing `avg_pull_requests_merged` metric in the same array

- **Evidence**: Changelog explicitly notes the attribution consistency.
- **Confidence**: settled (stated in changelog)
- **Quote**: (no direct verbatim quote recovered — see Extraction Notes)
- **Our assessment**: Attribution consistency means the same logic that determines which PRs
  count toward a user's `avg_pull_requests_merged` also governs which PRs count toward the
  phase-level `total_pull_requests_merged`. This is important for data integrity: teams can
  trust that `total_pull_requests_merged / engaged_users ≈ avg_pull_requests_merged` within
  a phase (modulo rounding). Attribution here means "PRs merged by users who were classified
  in that phase during that reporting window" — it is a user-attribution model, not a
  PR-attribution model (i.e., a PR counts toward whichever phase the author was classified
  in at merge time).

### Claim 6: Access requires enterprise administrator or organization owner status with Copilot usage metrics access

- **Evidence**: Consistent access tier across the entire Copilot usage metrics API series.
- **Confidence**: settled (consistent constraint documented in all prior Copilot metrics changelogs)
- **Quote**: (no direct verbatim quote recovered)
- **Our assessment**: Consistent with every prior Copilot metrics API changelog (April 8, April 10,
  April 22, May 14, May 29). This is a settled constraint for the entire API surface. Guide
  recommendations citing per-phase PR volume data must note this access prerequisite — the field
  is not available to individual contributors, team leads, or non-enterprise GitHub plans.

## Concrete Artifacts

### Updated `totals_by_ai_adoption_phase` Array Schema (June 26, 2026 state)

```
# Copilot usage metrics API — totals_by_ai_adoption_phase (updated June 26, 2026)
# Available at:
#   GET /enterprises/{enterprise}/copilot/metrics
#   GET /orgs/{org}/copilot/metrics
# Reporting windows: 1-day and 28-day rolling
# Access: enterprise administrator or organization owner

totals_by_ai_adoption_phase (array, one entry per phase 0–3):

  # Fields present before June 26, 2026 (established May 29, 2026):
  phase                          → phase identifier (0 = No cohort, 1 = Code first,
                                    2 = Agent first, 3 = Multi-agent)
  version                        → classification schema version (e.g., "v1")
  engaged_users                  → count of engaged users classified in this phase
  avg_pull_requests_merged       → per-user average PRs merged in this phase (existing)
  [other per-user averages]      → interaction averages, code gen/acceptance activity,
                                    lines added, lines deleted, median_time_to_merge averages

  # NEW field added June 26, 2026:
  total_pull_requests_merged     → aggregate count of all PRs merged by users in this phase
                                    Definition: "The total number of pull requests merged
                                    on that day by users in that adoption phase."
                                    (total, not average; first aggregate count in the array)
```

*Source: Track total merges by adoption phase in enterprise and organization reports,
GitHub Changelog, June 26, 2026*
*Note: Exact JSON field names from WebFetch-processed output; verify against the linked
API documentation. Pre-June-26 fields are derived from `docs-github-copilot-usage-metrics-adoption-cohorts.md`.*

### Analytical Capability Before and After June 26, 2026

```
Per-adoption-phase delivery analysis — what each source update adds:

BEFORE June 26, 2026 (May 29 state):
  Questions answerable from the API:
    - How many engaged users are in each phase? (engaged_users)
    - How fast do users in each phase merge PRs on average? (avg_pull_requests_merged)
    - How long do PRs take to merge for users in each phase? (median_time_to_merge averages)

  Questions NOT directly answerable (required client-side approximation):
    - What share of total org PRs comes from Phase 3 users?
      → Required: avg_pull_requests_merged × engaged_users (approximation only)
    - What is the total throughput contribution of each phase to org-wide delivery?

AFTER June 26, 2026:
  Questions now answerable directly from the API:
    - What share of merged PRs came from Phase 1 / 2 / 3 users?
      → total_pull_requests_merged per phase / sum(total_pull_requests_merged)
    - Does Phase 3's higher per-user velocity translate into disproportionate org-level volume?
    - How does total PR volume shift across phases over time?

  Complete per-phase delivery metric set (volume + velocity + cycle time):
    total_pull_requests_merged   → volume:      how much total output from this phase?  [NEW]
    avg_pull_requests_merged     → velocity:    how fast per developer in this phase?   [existing]
    median_time_to_merge         → cycle time:  how long from open to merge?            [existing]
    engaged_users                → cohort size: denominator for per-user calculations   [existing]
```

*Compiled from May 29, 2026 and June 26, 2026 GitHub changelogs*

## Cross-References

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 6
  (`totals_by_ai_adoption_phase` arrays surface metrics at enterprise and organization levels):
  The May 29, 2026 source established the `totals_by_ai_adoption_phase` array and its role
  as the pre-aggregated, server-side per-phase metric store. This June 26 source adds
  `total_pull_requests_merged` as a new aggregate field within that array. The extension is
  strictly additive — no existing fields change meaning or availability.

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 7
  (per-phase metrics include "pull request metrics" as a category): The May 29 source
  documented "pull request metrics" as a generic category within `totals_by_ai_adoption_phase`,
  without naming specific fields. This June 26 source reveals two concrete field names within
  that category: `avg_pull_requests_merged` (existing, per-user average) and
  `total_pull_requests_merged` (new, aggregate count). This is the first source to provide
  explicit field names for the PR metrics category of the phase array.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 3
  (`pull_requests.median_minutes_to_merge_copilot_reviewed` reports median time-to-merge for
  Copilot-reviewed PRs): The April 8 source added a cycle-time metric segmented by whether
  a PR received Copilot review. This June 26 source adds an aggregate volume metric segmented
  by the PR author's adoption phase. The two operate on orthogonal cut dimensions: April 8
  segments by "did this PR receive Copilot review?"; June 26 segments by "which adoption
  phase was the PR author in?" A complete picture of phase-driven delivery impact would need
  both: per-phase total merged PRs AND per-phase Copilot-review rate — the latter is not yet
  available from the API.

- **Corroborates** `docs-github-copilot-code-review-usage-metrics-aggregate.md` Claim 1
  (six new fields for code review aggregate user counts, available in 1-day and 28-day reports):
  The April 22 source established the same dual-window (1-day and 28-day) availability pattern.
  This June 26 source repeats it. The consistent dual-window availability across all Copilot
  metrics additions (April 8, April 10, April 22, May 14, May 29, June 26) confirms this as
  the settled API design choice for the Copilot metrics surface.

- **Novel**:
  - **First aggregate total count in `totals_by_ai_adoption_phase`**: Prior to June 26, 2026,
    all per-phase metrics in the array were per-user averages or simple counts (engaged_users).
    `total_pull_requests_merged` is the first aggregate total metric in the array — enabling
    direct proportional analysis without client-side multiplication or approximation.
  - **Volume-velocity-cycle-time trifecta by phase**: With `total_pull_requests_merged`
    (volume), `avg_pull_requests_merged` (velocity), and median time-to-merge (cycle time)
    all available within the same `totals_by_ai_adoption_phase` array entry, this is the
    most complete per-phase delivery impact metric set documented anywhere in the corpus.
    No prior source documents all three delivery dimensions available in a single API call
    segmented by adoption cohort.
  - **Proportional PR share analysis by phase**: No prior source in the corpus enables
    directly computing "what fraction of merged PRs comes from Phase 3 users?" from the
    Copilot API. The April 8 PR metrics (`docs-github-copilot-pr-review-metrics.md`) segment
    by Copilot-review status, not user adoption phase. This is the first adoption-phase-aware
    PR volume metric in the corpus.

## Guide Impact

### Chapter 05: Measurement — Per-Phase Delivery Metrics

- **Section "Per-phase delivery metrics" (extend from May 29 recommendation in
  `docs-github-copilot-usage-metrics-adoption-cohorts.md`)**: The May 29 source recommended
  adding median time-to-merge as the first delivery-velocity metric per adoption phase. This
  June 26 update completes the picture — add `total_pull_requests_merged` as the volume
  complement. Guide should document the trifecta: volume (`total_pull_requests_merged`),
  per-user velocity (`avg_pull_requests_merged`), and cycle time (median time-to-merge) —
  all now available per phase in a single API call. Recommend this combination as the
  standard adoption-program delivery report.

- **Section "Proportional PR analysis by adoption phase" (new)**: Document the proportional
  calculation: `total_pull_requests_merged[phase_N] / sum(total_pull_requests_merged[all phases])`.
  This answers the question no prior Copilot API field could: "What fraction of our merged
  PRs comes from our most advanced Copilot users?" Note the selection-bias caveat: Phase 3
  users may be higher-output developers independent of Copilot adoption; the metric supports
  adoption program storytelling but not causal attribution without a control group.

- **Section "Aggregate vs. per-user metrics — analytical distinction"**: Distinguish the
  two dimensions now available per phase: aggregate total (answers "how much volume?") and
  per-user average (answers "how fast per developer?"). A phase with a small, highly-productive
  cohort shows high per-user average but potentially low total volume; the trifecta gives the
  full picture for leadership reporting.

### Chapter 01: Daily Workflows — Code Review

- **Code review segmentation by adoption phase (add note)**: With phase-aware PR volume now
  measurable, engineering managers can track what fraction of merged PRs were authored by
  Phase 1 vs. Phase 3 users. This supports workflow segmentation decisions: e.g., prioritizing
  Copilot code review enablement for high-volume Phase 2 users who have not yet reached Phase 3.
  The recommendation is speculative at this stage (the metric is new) but operationally grounded.

## Extraction Notes

1. **Source is a short product changelog (~200–300 words)**: All substantive claims are extracted
   in the six claims above. The source is narrow — a single field addition to an existing API
   array. It does not introduce new adoption phase definitions, a new array structure, or a new
   reporting endpoint.
2. **WebFetch processing caveat**: This source was fetched once via WebFetch, which applies AI
   model processing to convert HTML to markdown. The output was substantially summarized rather
   than fully verbatim. The Claim 1 quote ("The total number of pull requests merged on that day
   by users in that adoption phase.") appeared in the WebFetch output and is the most likely
   verbatim field description from the changelog or linked API docs, but character-exact fidelity
   cannot be guaranteed. The Assayer should verify all quotes against the source URL directly.
3. **`avg_pull_requests_merged` field name**: The WebFetch output referenced this as the existing
   per-user average field complemented by the new total. This field name is not explicitly
   documented in `docs-github-copilot-usage-metrics-adoption-cohorts.md` (which describes the
   array as containing generic "pull request metrics"). The Assayer should verify the exact field
   name against the API documentation linked in the June 26 changelog.
4. **No contradictions filed**: This changelog is strictly additive — a new field in an existing
   array. No existing source note claims the `totals_by_ai_adoption_phase` array cannot include
   aggregate totals, or documents an alternative approach to proportional PR analysis by phase.
   No contradiction issue is needed.
5. **Attribution to predecessor source**: The June 26 changelog explicitly states it "builds on
   earlier AI adoption phase cohorts functionality" — confirming `docs-github-copilot-usage-metrics-adoption-cohorts.md`
   as the prerequisite context. Readers of this note should read the May 29 source first for
   the phase definitions, `totals_by_ai_adoption_phase` array structure, and versioning mechanism.
