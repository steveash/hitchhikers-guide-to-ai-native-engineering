---
source_url: https://github.blog/changelog/2026-07-07-add-review-cycles-and-time-to-adoption-phases-in-the-usage-api
source_type: docs
title: "Add review cycles and time to adoption phases in the usage API"
author: GitHub (official changelog)
date_published: 2026-07-07
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: settled
issue: "#1686"
---

# Add Review Cycles and Time to Adoption Phases in the Usage API (GitHub Changelog, July 7, 2026)

> GitHub's July 7, 2026 changelog extends the `totals_by_ai_adoption_phase` array with two
> new code-review velocity fields — `avg_pull_requests_minutes_to_review` (median minutes to
> first review) and `avg_pull_requests_review_cycles` (median review-submission count before
> merge) — completing a volume/velocity/cycle-time/review-latency metric set that lets
> organizations compare review speed across AI adoption cohorts.

## Source Context

- **Type**: docs (GitHub official product changelog, ~150 words, July 7, 2026, "1 minute read")
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these two fields exist, their definitions, their scoping
  to merged PRs, and their availability windows. Not authoritative for the implied causal
  claim that deeper Copilot adoption produces faster reviews — the changelog frames this as
  something teams "can see" by breaking the metrics out per phase, but cites no actual
  cross-phase data or study confirming the effect exists.
- **Scope**: Two new fields (`avg_pull_requests_minutes_to_review`,
  `avg_pull_requests_review_cycles`) added to the existing `totals_by_ai_adoption_phase`
  array in the Copilot usage metrics API, at enterprise and organization levels, in 1-day
  and 28-day reports. Covers field definitions, merged-PR scoping, and the stated
  cross-phase comparison use case. Does NOT cover: the access tier for this specific update
  (not restated in this changelog); whether review latency actually varies by phase in
  practice; how "first review" is defined for PRs with no human reviewer (e.g.,
  Copilot-only review); or how these fields interact with the `median_time_to_merge`
  field already present in the phase array since May 29, 2026.

## Extracted Claims

### Claim 1: Two new fields — `avg_pull_requests_minutes_to_review` and `avg_pull_requests_review_cycles` — extend the existing `totals_by_ai_adoption_phase` array with code-review velocity data, building on the adoption phase cohorts fields

- **Evidence**: Official GitHub product changelog opening statement announcing the feature
  as an extension of the existing adoption phase cohorts fields.
- **Confidence**: settled (product fact — the fields exist and their relationship to the
  existing array is stated)
- **Quote**: "The Copilot usage metrics API now reports two additional code-review velocity
  metrics for each AI adoption phase, extending the adoption phase cohorts fields available
  in the enterprise and organization reports."
- **Our assessment**: This is the third additive extension to `totals_by_ai_adoption_phase`
  documented in the corpus, following the May 29, 2026 establishment of the array
  (`docs-github-copilot-usage-metrics-adoption-cohorts.md`) and the June 26, 2026 addition
  of `total_pull_requests_merged` (`docs-github-copilot-usage-metrics-adoption-phase-total-merges.md`).
  GitHub is incrementally building out a per-phase delivery-metrics surface roughly one
  field-group per month rather than shipping it complete. For harness engineering: pipelines
  that already consume `totals_by_ai_adoption_phase` need no new integration pattern — this
  is a schema-additive change to an array they are presumably already reading.

### Claim 2: `avg_pull_requests_minutes_to_review` reports the median time, in minutes, from PR creation to its first review

- **Evidence**: Explicit field definition stated in the changelog, confirmed identically
  across three independent WebFetch passes.
- **Confidence**: settled (definitional)
- **Quote**: "The median time, in minutes, from when a pull request is created to its first
  review."
- **Our assessment**: Despite the `avg_` prefix in the field name, the definition explicitly
  states this is a *median*, not an arithmetic mean. This is a naming/documentation
  inconsistency worth flagging for teams building data pipelines against this API: the
  `avg_` prefix convention (also used for `avg_pull_requests_merged`, established June 26,
  2026) cannot be trusted to indicate the underlying statistic. Teams should read the field
  *description*, not infer behavior from the field *name*. Separately, "first review" measures
  time-to-first-touch, not time-to-resolution — it is a responsiveness metric, distinct from
  the cycle-time metrics already in the array.

### Claim 3: `avg_pull_requests_review_cycles` reports the median number of review submissions a pull request receives before it merges

- **Evidence**: Explicit field definition stated in the changelog, confirmed identically
  across three independent WebFetch passes.
- **Confidence**: settled (definitional)
- **Quote**: "The median number of review submissions a pull request receives before it
  merges."
- **Our assessment**: This is the first metric in the corpus that counts review *iterations*
  rather than review *presence* or *timing*. A low review-cycle count could mean either "the
  PR was well-formed and needed little back-and-forth" or "reviewers rubber-stamped it
  without engaging deeply" — the field cannot distinguish thoroughness from superficiality.
  As with Claim 2, the `avg_` field-name prefix again describes a median value, reinforcing
  that the naming convention is not a reliable indicator of the statistic used.

### Claim 4: Both new metrics are scoped to merged pull requests only, and are attributed to each pull request's merge day

- **Evidence**: Explicit scoping statement in the changelog, confirmed via targeted
  verbatim-quote WebFetch pass.
- **Confidence**: settled (stated scoping constraint)
- **Quote**: "Both metrics are scoped to merged pull requests and attributed to each pull
  request's merge day."
- **Our assessment**: This mirrors the merge-day attribution model already established for
  `total_pull_requests_merged` (June 26, 2026): a PR's review-latency and review-cycle data
  is counted against the adoption phase the *author* was classified into at merge time, not
  at PR-creation time or first-review time. For a long-lived PR where the author's phase
  classification could plausibly change between creation and merge (given the 28-day rolling
  classification window), only the merge-time snapshot is used. Abandoned or still-open PRs
  are invisible to both fields — a team with many long-review-cycle PRs that never merge
  would show artificially fast numbers, since only completed (merged) cycles are counted.

### Claim 5: The metrics appear in both enterprise and organization reports, in both 1-day and 28-day windows

- **Evidence**: Explicit availability statement in the changelog, confirmed via two
  independent WebFetch passes.
- **Confidence**: settled (stated availability scope)
- **Quote**: "These metrics appear in both the enterprise and organization 1-day and 28-day
  reports."
- **Our assessment**: This is the same dual-window, dual-tier availability pattern documented
  for every prior Copilot usage metrics API addition in the corpus (April 8, April 10, April
  22, May 14, May 29, June 26). It is now a fully settled API design convention — new fields
  in this API are added directly to existing report shapes rather than requiring new
  endpoints or report types.

### Claim 6: GitHub frames review latency and review-cycle counts as "leading indicators of engineering throughput"

- **Evidence**: Stated in the changelog's "Why this matters" section.
- **Confidence**: anecdotal (vendor framing — no throughput data or correlation study is
  cited to support the "leading indicator" characterization)
- **Quote**: "Review latency and review-cycle counts are leading indicators of engineering
  throughput."
- **Our assessment**: This is an assertion, not a demonstrated finding — no data in the
  changelog establishes that these two specific fields actually predict downstream
  throughput changes in practice. It is a plausible hypothesis (slow first-review time and
  high review-cycle counts are intuitively related to slower delivery) but the changelog
  offers it as settled fact. Same rhetorical pattern flagged in
  `docs-github-copilot-pr-review-metrics.md` Claim 6 for the April 8, 2026 changelog's
  "Copilot review helps" framing: GitHub's changelogs consistently assert the intended
  benefit of a new metric rather than presenting it as a hypothesis the metric is meant to
  test.

### Claim 7: GitHub's stated use case is comparing review speed and review-cycle counts across adoption phases to see whether deeper Copilot adoption correlates with faster, more efficient reviews

- **Evidence**: Stated in the changelog's "Why this matters" section as the explicit
  motivating use case for breaking these metrics out by phase.
- **Confidence**: anecdotal (stated use case / vendor hypothesis; no cross-phase data is
  presented in the changelog to confirm the correlation exists)
- **Quote**: "By breaking them out by AI adoption phase, you can see whether teams with
  deeper Copilot adoption get their pull requests reviewed faster and iterate through fewer
  review cycles."
- **Our assessment**: This is the analytically central claim of the source, and it carries
  the same selection-bias caveat already flagged for the June 26, 2026 PR-volume-by-phase
  metric (`docs-github-copilot-usage-metrics-adoption-phase-total-merges.md` Claim 3): teams
  or individuals who reach Phase 3 (Multi-agent) may already be higher-velocity, more
  disciplined reviewers independent of Copilot adoption depth. A finding of "Phase 3 authors
  get reviewed 2x faster than Phase 1 authors" from this field pair would be consistent with
  either "deeper Copilot adoption speeds up review" or "developers who adopt more agent
  surfaces were already faster at getting reviews" — the API cannot distinguish the two
  without a matched-cohort or pre/post design.

## Concrete Artifacts

### Updated `totals_by_ai_adoption_phase` Array Schema (July 7, 2026 state)

```
# Copilot usage metrics API — totals_by_ai_adoption_phase (updated July 7, 2026)
# Available at:
#   GET /enterprises/{enterprise}/copilot/metrics
#   GET /orgs/{org}/copilot/metrics
# Reporting windows: 1-day and 28-day rolling
# Docs: https://docs.github.com/rest/copilot/copilot-usage-metrics

totals_by_ai_adoption_phase (array, one entry per phase 0-3):

  # Fields present before July 7, 2026 (established May 29 / June 26, 2026):
  phase                            -> phase identifier (0-3)
  version                          -> classification schema version (e.g., "v1")
  engaged_users                    -> count of engaged users classified in this phase
  avg_pull_requests_merged         -> per-user average PRs merged in this phase
  total_pull_requests_merged       -> aggregate count of PRs merged by users in this phase
  median_time_to_merge (averages)  -> cycle time from open to merge, per phase
  [other per-user averages]        -> interaction averages, code gen/acceptance activity,
                                       lines added, lines deleted

  # NEW fields added July 7, 2026:
  avg_pull_requests_minutes_to_review  -> "The median time, in minutes, from when a pull
                                           request is created to its first review."
                                           (median despite the avg_ prefix)
  avg_pull_requests_review_cycles      -> "The median number of review submissions a pull
                                           request receives before it merges."
                                           (median despite the avg_ prefix)

  Both new fields: scoped to merged pull requests only, attributed to the PR's merge day.
```

*Source: Add review cycles and time to adoption phases in the usage API,
GitHub Changelog, July 7, 2026*
*Note: Field names and definitions from WebFetch-processed output, cross-checked across
three independent fetch passes with consistent verbatim results for the two field
definitions and the scoping statement. Pre-July-7 fields are derived from
`docs-github-copilot-usage-metrics-adoption-cohorts.md` and
`docs-github-copilot-usage-metrics-adoption-phase-total-merges.md`.*

### Per-Phase PR Lifecycle Metric Set — Before and After July 7, 2026

```
Per-adoption-phase PR lifecycle coverage, by changelog date:

May 29, 2026:   median_time_to_merge_averages   -> cycle time (open -> merge)
Jun 26, 2026:   total_pull_requests_merged      -> volume (how many PRs, this phase)
                avg_pull_requests_merged        -> velocity (PRs per user, this phase)
Jul  7, 2026:   avg_pull_requests_minutes_to_review  -> review latency (create -> first review)
                avg_pull_requests_review_cycles      -> review iteration count (submissions before merge)

Resulting coverage as of July 7, 2026:
  Volume:          total_pull_requests_merged
  Author velocity: avg_pull_requests_merged
  Review latency:  avg_pull_requests_minutes_to_review   [NEW]
  Review iteration: avg_pull_requests_review_cycles       [NEW]
  End-to-end cycle time: median_time_to_merge

  Still missing: acceptance/quality signal for what happens during those review
  cycles (e.g., whether cycles resolve substantive issues or are rubber-stamp
  re-approvals); a non-Copilot-adopting baseline cohort for comparison.
```

*Compiled from May 29, June 26, and July 7, 2026 GitHub changelogs.*

## Cross-References

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 6
  (`totals_by_ai_adoption_phase` arrays surface metrics at enterprise and organization
  levels) and Claim 7 (per-phase metrics include pull request metrics and median
  time-to-merge averages): This July 7 source adds two more concrete field names to the
  array Claim 6 established and the "pull request metrics" category Claim 7 described only
  generically. Together with the June 26 addition, three separate changelogs have now each
  added named fields to a category Claim 7 originally described only as "pull request
  metrics."

- **Extends** `docs-github-copilot-usage-metrics-adoption-phase-total-merges.md` Claim 2
  (the `total_pull_requests_merged` field is an aggregate total, distinct from the existing
  `avg_pull_requests_merged` per-user average) and its Concrete Artifacts "Complete per-phase
  delivery metric set (volume + velocity + cycle time)" table: that table listed volume,
  velocity, and cycle time as the complete per-phase delivery metric set as of June 26, 2026.
  This July 7 source adds a fourth and fifth dimension — review latency and review
  iteration count — that the June 26 note's table did not yet include and could not have
  anticipated. The "complete" framing in that note is superseded; see the updated table in
  this note's Concrete Artifacts section.

- **Corroborates** `docs-github-copilot-usage-metrics-adoption-phase-total-merges.md`
  Claim 3 (the June 26 field enables proportional PR-share analysis by phase, with the
  caveat that this does not establish causation because higher-phase users may already be
  higher-output developers): This source's Claim 7 makes an structurally identical
  selection-bias-vulnerable claim, this time about review speed rather than PR volume. The
  same interpretive caution applies to both, and now applies to the whole per-phase metric
  family: any cross-phase comparison from `totals_by_ai_adoption_phase` risks conflating
  Copilot-adoption effects with pre-existing differences between the developers who reach
  each phase.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 6 (the April 8, 2026
  changelog's "Copilot review helps... compare merge rates and cycle times" framing asserts
  an undemonstrated benefit rather than presenting it as a hypothesis): This July 7 source's
  "Why this matters" framing (Claims 6-7 in this note) follows the identical rhetorical
  pattern — asserting that the new fields are "leading indicators" and that adoption depth
  correlates with review speed, without presenting supporting data. This is now a
  consistent pattern across at least two Copilot usage-metrics changelogs (April 8 and July
  7, 2026): new measurement fields are introduced with an implied positive finding baked
  into the announcement, rather than framed neutrally as measurement primitives.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 3
  (`pull_requests.median_minutes_to_merge_copilot_reviewed` reports median time from PR
  creation to merge for Copilot-reviewed PRs, added April 8, 2026): Both this field and the
  new `avg_pull_requests_minutes_to_review` measure PR-lifecycle timing in minutes from PR
  creation, but they answer different questions and use different segmentation axes. The
  April 8 field segments by "was this PR reviewed by Copilot?" and measures full
  creation-to-*merge* time for that cohort. The July 7 field segments by "what adoption
  phase was the PR author in?" and measures creation-to-*first-review* time (not merge)
  for that cohort. Neither field can be substituted for the other; a complete review-latency
  analysis crossing both dimensions (was the PR itself Copilot-reviewed, and was the author
  a deep Copilot adopter) is not directly available from either changelog alone.

- **Novel**:
  - **Review-cycle iteration count as a phase-level metric**: No prior source in the corpus
    documents a Copilot metrics API field that counts review *submissions* (iterations)
    rather than review *presence*, *timing*, or *volume*. `avg_pull_requests_review_cycles`
    is the first metric in the corpus that could distinguish a PR that merged after one
    clean approval from one that went through five rounds of requested changes.
  - **`avg_` field-name prefix confirmed to denote a median, not a mean**: This is the first
    source in the corpus where the field's own documented definition explicitly contradicts
    the naming convention implied by its prefix (`avg_` describing a value stated as
    "median"). Prior notes on `avg_pull_requests_merged` (June 26) could not confirm the
    underlying statistic because no verbatim definition was recovered; this source closes
    that gap for the `avg_` prefix generally, and the answer is that the prefix is not a
    reliable guide to the statistic.
  - **First review-latency metric segmented by author's adoption phase (not by whether the
    reviewer was Copilot)**: All prior review-latency/cycle-time metrics in the corpus
    (April 8) segment by whether Copilot performed the review. This is the first to segment
    review latency by the *PR author's* AI-adoption depth, regardless of who or what
    reviewed the PR.

## Guide Impact

### Chapter 05: Team Adoption

- **Section "Measuring impact" (extend)**: Add `avg_pull_requests_minutes_to_review` and
  `avg_pull_requests_review_cycles` to the vendor-native, no-cost measurement primitives
  already documented from the April 8, 2026 and June 26, 2026 sources. Recommend presenting
  the four-metric per-phase delivery set together (volume, author velocity, review latency,
  review iteration count) rather than any single field in isolation, since each captures a
  different dimension and none alone supports a "Copilot made reviews faster" conclusion.
- **Section "Measuring impact" (add caveat)**: Explicitly warn readers against citing
  cross-phase review-speed comparisons as evidence that Copilot adoption *causes* faster
  reviews. Per this source's Claim 7 and the corroborating June 26 caveat, phase membership
  is a behavioral classification, not a randomized treatment — faster review times in
  higher phases are equally consistent with developer selection effects.
- **Section "Vendor framing vs. demonstrated findings" (extend, if it exists per the April 8
  note's Claim 6 precedent)**: Add this source as a second documented instance of GitHub
  changelog language asserting a benefit ("leading indicators of engineering throughput")
  without supporting data, reinforcing that this is a recurring pattern in Copilot usage
  metrics changelogs rather than a one-off framing choice.

### Chapter 02: Harness Engineering

- **Section "Enterprise Copilot observability pipeline" (extend)**: Add the two new fields
  to the phase-cohort tier of the metrics architecture (schema-additive, no new endpoint or
  JOIN required — same integration pattern as the June 26 addition).
- **Section "API naming conventions / schema stability" (add caution)**: Document that the
  Copilot usage metrics API's `avg_` field-name prefix does not reliably indicate an
  arithmetic mean — `avg_pull_requests_minutes_to_review` and `avg_pull_requests_review_cycles`
  are both explicitly defined as medians. Pipelines that assume `avg_`-prefixed fields
  support mean-based aggregation (e.g., naively averaging an `avg_` field across multiple
  reporting periods to get a longer-window mean) will produce statistically invalid results,
  since medians do not compose that way.

## Extraction Notes

1. **Source is very short (~150 words, "1 minute read")**: All substantive claims are
   extracted in the seven claims above. The source is exhausted for direct content; several
   claims (1, 6, 7) draw additional analytical weight from cross-referencing the established
   May 29 / June 26 predecessor sources rather than from additional July 7 content.
2. **Four independent WebFetch passes**: The source was fetched four times with progressively
   more targeted prompts (general extraction, verbatim reproduction attempt, targeted
   under-125-character quotes, and a final pass for the opening sentence / "Why this matters"
   heading / documentation link). The verbatim-reproduction pass was refused by the fetch
   model on copyright grounds, so all quotes in this note come from the targeted-quote passes,
   which returned character-identical wording for the two field definitions and the scoping
   statement across repeated asks — this consistency is the basis for treating those quotes
   as high-fidelity. The Assayer should still verify all quotes against the live source URL,
   as WebFetch applies model processing that may affect exact character fidelity, per the
   caution already established in `docs-github-copilot-usage-metrics-adoption-cohorts.md`
   and `docs-github-copilot-usage-metrics-adoption-phase-total-merges.md`.
3. **Access tier not stated in this changelog**: Unlike the May 29 and April 22 changelogs,
   this July 7 changelog does not restate the enterprise-administrator/organization-owner
   access requirement. Based on the consistent pattern across every prior Copilot usage
   metrics API changelog in the corpus, the same restriction almost certainly applies (this
   is an additive field on an array already gated at that tier), but this is an inference,
   not a quote, and is noted as a Source Context gap rather than asserted as a Claim.
4. **No contradictions to file**: This changelog is strictly additive — two new fields on an
   existing array. No existing source note claims the `totals_by_ai_adoption_phase` array
   cannot include review-velocity metrics, or that review latency should not be measured
   per adoption phase. The vendor-framing pattern flagged in Claims 6-7 (assertion of
   benefit without data) corroborates rather than contradicts the same pattern already
   flagged in `docs-github-copilot-pr-review-metrics.md` Claim 6 — both are Miner
   observations about GitHub's changelog rhetoric, not disagreeing claims from GitHub itself.
5. **Two triage comments on this issue**: The issue carries two separate Prospector triage
   comments with slightly different chapter suggestions (Ch05/Ch02 in one, Ch03/Ch04 in the
   other). This note follows the Ch05 (Team Adoption) / Ch02 (Harness Engineering) framing,
   matching the actual chapter files in `guide/` (`05-team-adoption.md`,
   `02-harness-engineering.md`) and the convention already used in
   `docs-github-copilot-pr-review-metrics.md`'s Guide Impact section. The repo has no
   chapters matching "Ch03 (Adoption velocity & cohort analysis)" or "Ch04 (Platform
   observability)" as named in the second triage comment as of this extraction — those
   appear to be descriptive labels rather than literal chapter titles.
