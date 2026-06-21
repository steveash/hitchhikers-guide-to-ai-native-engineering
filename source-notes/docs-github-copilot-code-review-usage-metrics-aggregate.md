---
source_url: https://github.blog/changelog/2026-04-22-copilot-code-review-user-counts-now-aggregate-in-usage-metrics-api
source_type: docs
title: "Copilot code review user counts now aggregate in usage metrics API"
author: GitHub (official changelog)
date_published: 2026-04-22
date_extracted: 2026-06-21
last_checked: 2026-06-21
status: current
confidence_overall: settled
issue: "#347"
---

# Copilot Code Review Aggregate User Counts in the Usage Metrics API (GitHub Changelog)

> GitHub's April 22, 2026 changelog introduces six new fields tracking active and passive
> user counts for Copilot code review at the org and enterprise level — the first Copilot
> metrics primitive to distinguish intentional engagement (manual request or applied
> suggestion) from policy-driven activation (auto-triggered review), enabling teams to
> measure whether adoption is genuine or merely mandated.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words, April 22, 2026)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these fields exist, their definitions, and the
  active/passive classification rules. Not authoritative for any causal claim about
  what active vs. passive ratios indicate about rollout health — no outcome data is
  cited.
- **Scope**: Six new fields added to the Copilot usage metrics REST API at enterprise
  and organization levels, providing aggregate active and passive user counts for
  Copilot code review across daily, weekly, and monthly windows. Covers field
  definitions, the active/passive classification rule, and the stated use cases for
  adoption tracking. Does NOT cover: what counts as "applying a suggestion" in
  detail; how these fields interact with PR-level code review metrics from April 8,
  2026; any guidance on what active-to-passive ratios are "good"; or whether the
  April 6, 2026 user identification predecessor is a prerequisite for these aggregate
  fields to populate.

## Extracted Claims

### Claim 1: Six new fields provide aggregate active and passive user counts for Copilot code review at the enterprise and organization level, available in both 1-day and 28-day reports

- **Evidence**: Official GitHub product changelog announcing the feature. States that the
  fields are available "in both 1-day and 28-day reports at the enterprise and organization
  levels."
- **Confidence**: settled (these fields exist — this is a product fact)
- **Quote**: (no direct quote recovered verbatim; see Extraction Notes — the phrase "in
  both 1-day and 28-day reports at the enterprise and organization levels" appeared
  consistently across both WebFetch passes)
- **Our assessment**: This follows the exact same architectural pattern as the CCA aggregate
  counts announced two weeks earlier on April 10 (`docs-github-copilot-cca-usage-metrics-aggregate.md`
  Claim 1). GitHub is systematically extending the usage metrics API one product surface at
  a time: CCA active user counts (April 10), then code review active+passive user counts
  (April 22). The novel element here is the passive dimension — the CCA aggregate note
  documented only active user counts, with no corresponding passive count. Code review is
  the first surface in the corpus to expose the active/passive split at the aggregate level.

### Claim 2: Active users are those who manually requested a Copilot code review or applied a Copilot suggestion

- **Evidence**: Explicit definition in the changelog describing what qualifies as an active
  code review user.
- **Confidence**: settled (definitional)
- **Quote**: "manually requested a Copilot code review or applied a Copilot suggestion"
- **Our assessment**: "Manually requested" means the user explicitly triggered a code review
  (e.g., via the GitHub UI or an API call), as opposed to having it triggered automatically
  by an org or repo policy. "Applied a Copilot suggestion" means the user acted on at least
  one of Copilot's review suggestions — the strongest available signal of intentional
  engagement. Crucially, "applied a suggestion" is a higher signal than "received a review":
  a user can passively receive auto-triggered reviews without applying any suggestions and
  still count as passive, not active. For adoption measurement: active counts reflect
  genuine user engagement; passive counts reflect tool exposure, not necessarily engagement.

### Claim 3: Passive users are those whose code reviews were auto-triggered by a repository or organization policy

- **Evidence**: Explicit definition in the changelog describing what qualifies as a passive
  code review user.
- **Confidence**: settled (definitional)
- **Quote**: "reviews auto-triggered by a repository or organization policy"
- **Our assessment**: Auto-trigger policies are the mechanism by which organization or
  repository admins configure Copilot code review to automatically activate on every PR
  (or PRs matching specific criteria), without requiring the individual author or reviewer
  to opt in. A user whose PRs are auto-reviewed appears in passive counts even if they
  never interacted with a Copilot suggestion. The `docs-github-copilot-code-review-config-controls.md`
  source documents the governance controls that enable these auto-trigger policies — Claim 1
  in that note covers org-level default runner configuration, and Claim 2 covers lock
  enforcement. The passive user count is the measurable consequence of those governance
  choices: the more broadly an organization mandates auto-trigger, the larger the passive
  count grows relative to active.

### Claim 4: A user counted as both active and passive in the same reporting window counts as active only

- **Evidence**: Consistent description across both WebFetch passes of the counting rule.
- **Confidence**: settled (definitional counting rule)
- **Quote**: (no direct verbatim quote; WebFetch summarized this as "active always trumps
  passive" — see Extraction Notes)
- **Our assessment**: This rule prevents double-counting: a user who received an auto-triggered
  review (passive signal) AND manually requested a review or applied a suggestion (active
  signal) contributes only to the active count. The design choice is deliberate — GitHub
  preserves the active count as a "best case" view of engagement. A practical implication:
  the sum `daily_active + daily_passive` does NOT equal total unique users who had any code
  review interaction, since it intentionally excludes the dual-signal users from the passive
  bucket. Teams building dashboards should treat these counts as exclusive cohorts: active
  and passive users are disjoint sets.

### Claim 5: The weekly fields use a trailing 7-day window; the monthly fields use a trailing 28-day window

- **Evidence**: Field description language consistent across both WebFetch passes.
- **Confidence**: settled (definitional)
- **Quote**: "Active users who used Copilot code review in the trailing 7-day window"
  (weekly_active); "Active users who used Copilot code review in the trailing 28-day
  window" (monthly_active)
- **Our assessment**: The 28-day window for monthly fields aligns with the CCA aggregate
  `monthly_active_copilot_cloud_agent_users` field (April 10) and the `ai_adoption_phase`
  classification window (May 29). This means a user's monthly code review active status,
  CCA monthly active status, and adoption phase are all computed over the same 28-day
  horizon — enabling consistent side-by-side comparisons. The 7-day weekly window smooths
  daily noise for trend analysis; the 28-day monthly window is the standard MAU metric
  appropriate for executive adoption dashboards.

### Claim 6: The active/passive split enables organizations to distinguish intentional adoption from policy-driven activation

- **Evidence**: Stated as the primary use case in the changelog's "Why this matters" section.
- **Confidence**: settled (stated design intent; the mechanism is real even if outcomes are
  vendor-framed)
- **Quote**: "Distinguish adoption drivers"
- **Our assessment**: This is the guide-relevant insight of this source. Org admins who
  mandate Copilot code review via auto-trigger policies will see large passive counts and
  potentially small active counts — a signal that users are being exposed to the tool but
  not choosing to engage with it. Conversely, a high active-to-passive ratio indicates
  organic adoption: users are asking for reviews and acting on suggestions without being
  forced to. This distinction is operationally significant for planning enablement
  investment: a fleet with 80% passive users needs training and change management, not
  additional policy mandates. A fleet with 80% active users is self-sustaining. No prior
  source in the corpus documents any mechanism to distinguish mandated from voluntary
  AI tool usage at the aggregate level.

### Claim 7: Three intended use cases are distinguishing adoption drivers, comparing engagement across time windows, and making informed rollout decisions

- **Evidence**: Explicit "Why this matters" section in the changelog, three bullets.
- **Confidence**: anecdotal (vendor framing; no evidence that teams have successfully
  used these metrics for these purposes)
- **Quote**: "Distinguish adoption drivers" / "Compare engagement across time windows" /
  "Make informed rollout decisions"
- **Our assessment**: The first use case is the most analytically novel (see Claim 6).
  The second ("compare engagement across time windows") mirrors the CCA aggregate note's
  multi-window framing — the same caution applies: temporal trends show correlation with
  rollout events, not causation. The third ("make informed rollout decisions") is the
  most actionable: active/passive ratios at different stages of a phased rollout can tell
  admins whether to proceed with the next cohort or pause for enablement. However, the
  changelog does not define thresholds for "good" active ratios, leaving interpretation
  to the consumer. As with the CCA aggregate note's Claim 9 assessment, the API provides
  the data; the decision framework is the team's responsibility.

### Claim 8: This feature builds on an earlier April 2026 Copilot code review user identification capability

- **Evidence**: Changelog references a predecessor update. Prospector triage comment
  explicitly identifies "the user identification system from April 6, 2026."
- **Confidence**: settled (stated in changelog and confirmed by Prospector)
- **Quote**: (no direct verbatim quote recovered; WebFetch described "an earlier April 2026
  announcement regarding Copilot code review user identification capabilities")
- **Our assessment**: The April 6, 2026 update (not yet a source note in this corpus as of
  this extraction) introduced user-level code review identification — likely a per-user flag
  analogous to the `used_copilot_coding_agent` flag added March 25, 2026 for CCA. The April
  22 aggregate counts are the fleet-level complement of that user-level capability: where the
  April 6 update enables identifying which individual users had code review activity, the
  April 22 update provides pre-aggregated org/enterprise-level counts without requiring
  per-user enumeration. This mirrors the exact pattern of CCA user identification (March 25)
  → CCA aggregate counts (April 10).

## Concrete Artifacts

### Six New Code Review Aggregate User Fields (from changelog, April 22, 2026)

```
# Copilot usage metrics API — code review aggregate user fields (added April 22, 2026)
# Available at:
#   GET /enterprises/{enterprise}/copilot/metrics
#   GET /orgs/{org}/copilot/metrics
# Reporting windows: 1-day and 28-day rolling

daily_active_copilot_code_review_users
  Description: Active users who used Copilot code review on that day.
  Active = manually requested a review OR applied a Copilot suggestion.

daily_passive_copilot_code_review_users
  Description: Passive users who used Copilot code review on that day.
  Passive = auto-triggered by a repository or organization policy.

weekly_active_copilot_code_review_users
  Description: Active users who used Copilot code review in the trailing 7-day window.

weekly_passive_copilot_code_review_users
  Description: Passive users who used Copilot code review in the trailing 7-day window.

monthly_active_copilot_code_review_users
  Description: Active users who used Copilot code review in the trailing 28-day window.

monthly_passive_copilot_code_review_users
  Description: Passive users who used Copilot code review in the trailing 28-day window.

Counting rule: A user with both active and passive signals in the same window
               counts as ACTIVE only. Active/passive counts are mutually exclusive.

Note: Field names from WebFetch-processed output. Verify against
      API docs for exact names and nullability semantics.
```

*Source: Copilot code review user counts now aggregate in usage metrics API,
GitHub Changelog, April 22, 2026*

### Copilot Code Review Metrics Surface: User Count vs. PR Level (as of April 22, 2026)

```
# Two distinct measurement dimensions for Copilot code review:

Dimension 1 — PR-level metrics (added April 8, 2026):
  pull_requests.total_merged_reviewed_by_copilot
    → Count of merged PRs that received a Copilot code review.
    → Measures: adoption penetration at the PR level.
  pull_requests.median_minutes_to_merge_copilot_reviewed
    → Median time-to-merge for Copilot-reviewed PRs.
    → Measures: delivery velocity for the Copilot-reviewed cohort.

Dimension 2 — User-level aggregate counts (added April 22, 2026, THIS CHANGELOG):
  daily/weekly/monthly_active_copilot_code_review_users
    → Count of unique users who actively engaged with code review.
    → Measures: intentional engagement (request + apply signals).
  daily/weekly/monthly_passive_copilot_code_review_users
    → Count of unique users with auto-triggered code reviews.
    → Measures: policy-driven exposure without active engagement.

Missing for complete outcome measurement:
  Acceptance rate for Copilot suggestions in code review  → not yet in API
  PR-level metrics for non-Copilot-reviewed PRs (baseline) → must compute externally
  Per-user code review activity flag                      → predecessor April 6 update
                                                           (not yet in corpus as source note)
```

*Source: Compiled from April 8 and April 22, 2026 GitHub changelogs*

## Cross-References

- **Corroborates** `docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 1 (three new
  aggregate active-user-count fields available in both enterprise and organization usage reports):
  This source follows the identical architectural pattern — aggregate user counts at org/enterprise
  level in daily/weekly/monthly windows. GitHub announced CCA aggregate counts April 10 and code
  review aggregate counts April 22, twelve days apart, reflecting a systematic per-surface
  expansion of the metrics API rather than a one-time addition.

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md` Claim 6 (multi-surface
  Copilot adoption view giving "a full view of Copilot adoption across surfaces"): The April 10
  source framed the metrics API as covering multiple surfaces. This source adds the code review
  surface to that multi-surface view. Together, the April 10 and April 22 changelogs provide
  aggregate user counts for two of the three "GitHub-based agent surfaces" enumerated in the
  adoption cohort model: CCA (April 10) and code review (April 22). Copilot CLI remains without
  a dedicated aggregate user count note in the corpus as of this extraction.

- **Extends** `docs-github-copilot-pr-review-metrics.md` Claim 1 (two new API fields track
  Copilot code review adoption at the PR lifecycle level): The April 8 source provided PR-level
  code review metrics (how many PRs were reviewed, how long they took to merge). This source
  adds a user-count dimension (how many users are reviewing with Copilot, and how engaged are
  they). The two sources together cover distinct observability angles on the same feature: "what
  is Copilot doing to PRs?" (April 8) vs. "who is using Copilot code review, and voluntarily?"
  (April 22). Neither replaces the other.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 5 (metrics are restricted
  to enterprise administrators and organization owners with Copilot usage metrics access): The
  same access tier restriction applies to the aggregate code review user counts documented here.
  This is a consistent constraint across the entire Copilot metrics API series.

- **Corroborates** `docs-github-copilot-team-level-usage-metrics.md` Claim 5 (team-level
  breakdowns cover "IDE completions, chat, Copilot CLI, code review, and Copilot cloud agent
  activity"): The May 14 team-level metrics source confirms code review is one of five surfaces
  tracked at team granularity. The org/enterprise aggregate counts in this April 22 source are
  the Tier 1/2 counterpart to that Tier 4 team-level view — both cover code review user
  activity, at different granularity tiers. The aggregate counts require no JOIN; the team-level
  data requires the NDJSON download + JOIN pattern from `docs-github-copilot-team-level-usage-metrics.md`.

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 4 (Phase 2 "Agent
  first" covers users who engaged with a single GitHub-based agent surface — Copilot cloud agent,
  Copilot code review, or Copilot CLI): The adoption phase model (May 29) classifies code review
  engagement as a Phase 2 qualifier. This April 22 source provides the underlying aggregate metric
  that would count those Phase 2 code-review users. The active/passive distinction adds nuance
  the phase model does not capture: a passive code review user (auto-triggered, no suggestion
  applied) might still be classified as Phase 2 by the adoption phase model — but the active/passive
  split here reveals whether that Phase 2 classification reflects genuine engagement or only
  policy-mandated exposure. The two sources together give a more complete picture.

- **Corroborates** `docs-github-copilot-code-review-config-controls.md` Claims 1–2 (org-level
  runner default configuration and lock enforcement): The config controls note documents the
  governance mechanisms that create passive users: org-level runner configuration and auto-trigger
  policies let admins mandate code review across all repositories. The passive user count in this
  note is the measurable consequence of deploying those governance mechanisms without accompanying
  enablement for users to engage actively. Together: the controls note explains how passive users
  are created; this note explains how to measure the passive population.

- **Novel**:
  - **Active/passive user classification**: No prior source in the corpus distinguishes intentional
    from policy-driven Copilot usage at any granularity. This is the first API field that
    explicitly separates organic engagement (active) from mandated exposure (passive) for any
    Copilot surface.
  - **Passive user count as a governance artifact**: The passive count directly reflects the
    scope of auto-trigger policy deployment. An organization can now measure the reach of its
    mandate decisions — something no prior source in the corpus documents as measurable.
  - **Exclusive counting rule (active trumps passive)**: The mutual exclusivity constraint (dual-signal
    users counted as active only) is a novel measurement design choice not documented in any prior
    source. It means `active + passive ≠ total unique code review users` — a subtle but important
    data modeling fact for dashboard builders.
  - **Code review as a distinct measurable adoption signal**: Prior metrics sources (April 8, April 10)
    treated code review as either a PR-level event or one of several agent surfaces. This source
    provides the first user-count aggregate specifically for code review engagement — equivalent
    to the CCA user count but for the human-facing review surface rather than autonomous task execution.
  - **Predecessor user identification update not yet in corpus**: The April 6, 2026 code review
    user identification changelog (the per-user precursor to these aggregate counts) is referenced
    by the Prospector but is not yet a source note in this corpus. It warrants mining as the
    upstream context for this aggregate API.

## Guide Impact

### Chapter 05: Measurement — Copilot Code Review Adoption

- **Section "Measuring code review adoption" (add or extend)**: Reference the six new
  aggregate fields as the canonical vendor-native measurement primitive for code review
  adoption at fleet level. Distinguish from the April 8 PR-level metrics: those measure
  "what Copilot did to PRs"; these measure "who is using code review and how." The
  `monthly_active_copilot_code_review_users` field is the code review equivalent of
  `monthly_active_copilot_cloud_agent_users` for CCA — a MAU metric for code review
  adoption suitable for executive dashboards.
- **Section "Active vs. passive adoption: distinguishing genuine use from policy mandates"
  (new section)**: This is the most novel guide contribution from this source. When
  organizations deploy Copilot code review via auto-trigger policies, they will see large
  passive counts but potentially low active counts. A predominantly passive profile suggests
  users are exposed to the tool but not engaging with it — a signal for enablement investment,
  not additional policy mandates. Guide should recommend tracking the active/passive ratio
  over time: a healthy rollout should show passive counts declining (or active counts growing)
  as users convert from passive exposure to active engagement. Cite this source as the
  measurement primitive that makes this distinction possible.
- **Section "Code review measurement stack" (new or extend)**: Document the complete
  two-source measurement stack for Copilot code review:
  - PR-level impact: April 8 changelog (`docs-github-copilot-pr-review-metrics.md`)
    → `total_merged_reviewed_by_copilot` and `median_minutes_to_merge_copilot_reviewed`
  - User-level adoption: April 22 changelog (this note)
    → active/passive user counts across daily/weekly/monthly windows
  These two sources are complementary: PR-level metrics answer whether Copilot review
  affects delivery velocity; user-level counts answer who is engaging and how voluntarily.
- **Section "Adoption phase model and code review engagement" (add note)**: The adoption
  cohort model (May 29, `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 4)
  counts any code review engagement as Phase 2. The active/passive distinction from this
  source adds nuance: teams should monitor whether their Phase 2 code-review users are
  predominantly active or passive, as Phase 2 via passive exposure may not represent the
  same genuine agentic adoption maturity as Phase 2 via active engagement.

### Chapter 02: Harness Engineering — Observability

- **Section "Enterprise Copilot observability"**: Add the code review aggregate user count
  fields to the recommended observability primitives. These fields answer "Is our code
  review rollout generating genuine engagement?" at fleet level without requiring per-user
  data access. Reference the active/passive distinction as the key signal for distinguishing
  policy-compliance metrics from adoption-quality metrics.
- **Section "Counting model caveats for code review metrics"**: Document the exclusive
  counting rule: `active_count + passive_count ≠ total_users_with_code_review_exposure`
  because dual-signal users (both active and passive in the same window) are counted as
  active only, not in both buckets. Any pipeline computing total exposure must not simply
  sum active and passive fields.

## Extraction Notes

1. **Source is thin by design**: This is a product changelog (~300 words). All substantive
   claims are exhausted in eight items above. The source should not be cited for more than
   it contains.
2. **Two WebFetch passes with different prompts**: The source was fetched twice — first with
   a general extraction prompt, then with an explicit verbatim-extraction prompt. Both passes
   returned substantially consistent content. The second pass produced closer-to-verbatim
   rendering for the active/passive definitions and the field description phrases. All quotes
   used in this note appeared in both passes. As in prior Copilot metrics source notes, the
   Assayer should verify quotes against the live source URL, as WebFetch applies model
   processing that may affect exact character fidelity.
3. **Active/passive definition quotes**: The phrases "manually requested a Copilot code review
   or applied a Copilot suggestion" (Claim 2) and "reviews auto-triggered by a repository or
   organization policy" (Claim 3) appeared in quoted form in the second WebFetch pass and are
   used as verbatim quotes here. These are the highest-confidence quotes in this note.
4. **"Active always trumps passive" rule**: Claim 4's counting rule was described consistently
   across both passes as a disambiguation rule where active always wins over passive. No exact
   verbatim phrase was recoverable; the quote field is marked accordingly.
5. **Predecessor April 6 changelog**: The issue body and Prospector triage confirm a predecessor
   April 6, 2026 changelog on code review user identification. That source was not separately
   fetched (the April 22 changelog was the direct source for this note). The April 6 update
   is flagged under Novel as a gap in the corpus.
6. **No contradictions to file**: No existing source note claims that code review adoption
   cannot or should not be measured at the aggregate level, or that the active/passive
   distinction is inappropriate. The April 8 PR-level metrics note (`docs-github-copilot-pr-review-metrics.md`)
   and this note are complementary, not contradictory. The Prospector explicitly noted "no
   contradictions" for this source.
7. **Access tier not explicitly stated in source**: The changelog does not explicitly state
   the access tier in either WebFetch pass. Based on the consistent pattern across all Copilot
   usage metrics changelogs (April 8, April 10, May 14, May 29 — all restricted to enterprise
   admins and org owners), the same restriction almost certainly applies here. This is noted
   as an inference rather than a direct quote.
