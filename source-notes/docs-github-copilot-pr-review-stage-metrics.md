---
source_url: https://github.blog/changelog/2026-09-25-usage-metrics-api-adds-pull-request-review-stages
source_type: docs
title: "Usage metrics API adds pull request review stages"
author: GitHub (official changelog)
date_published: 2026-09-25
date_extracted: 2026-09-27
last_checked: 2026-09-27
status: current
confidence_overall: settled
issue: "#3750"
---

# Usage Metrics API Adds Pull Request Review Stages (GitHub Changelog, September 25, 2026)

> GitHub's September 25, 2026 changelog adds a `pull_request_review_times`
> array to each `repos-1-day` report row, breaking human-reviewed pull
> request cycle time into three timed stages (ready-to-first-review,
> first-to-final-review, final-review-to-merge) with median and p90 per
> stage — the first documented per-row field for the repository-level
> report and the first stage-level (not just aggregate) PR review timing
> primitive in the Copilot usage metrics API.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words body text,
  "2 minute read," September 25, 2026)
- **Author credibility**: GitHub engineering team announcing a production
  API change. Authoritative for the fact that the field exists, its
  structure, and its inclusion/exclusion rules. Not authoritative for
  whether stage-level breakdowns actually help teams fix review bottlenecks
  in practice — no outcome data or case study is cited, only the stated
  design rationale.
- **Scope**: One new field (`pull_request_review_times`) added to the
  `repos-1-day` enterprise/organization report row schema; its six
  sub-metrics (three stages × median/p90); the human-only, non-bot
  inclusion rule; the no-backfill start date; the empty-array-vs-zero
  distinction; and access requirements. Does NOT cover: the exact JSON
  key names as they appear in the downloaded NDJSON row (the changelog
  describes the fields in prose, not as a literal schema block); whether
  a `repos-28-day` rolling-window equivalent will ever exist; how
  `pull_request_review_times[].total_merged` values compare numerically,
  repository-by-repository, against `pull_requests.total_merged`; or any
  UI/dashboard surface that visualizes the new stages.

## Extracted Claims

### Claim 1: A new `pull_request_review_times` array on each `repos-1-day` row reports median and p90 durations for three review stages: ready-to-first-review, first-to-final-review, and final-review-to-merge

- **Evidence**: Stated directly in the changelog's opening summary paragraph
  (above the "What's new" heading) and restated with field-level detail
  under "What's new."
- **Confidence**: settled (product fact — the field exists as documented)
- **Quote**: "The enterprise and organization repository-level Copilot
  usage metrics reports now break down how long pull requests spend in
  each stage of review. A new pull_request_review_times array on each
  repos-1-day row reports a median and a 90th percentile for the time
  from ready for review to first review, first review to final review,
  and final review to merge."
- **Our assessment**: This is the first documented per-row field for the
  `repos-1-day` report since its July 17, 2026 general availability
  release (`docs-github-copilot-repository-level-usage-metrics.md`), whose
  Claim 3 explicitly noted that "the row schema is presumably documented
  inside the NDJSON file itself... not published on the reference page."
  This changelog is that missing row-schema documentation arriving via a
  feature announcement rather than a reference-page update — the REST API
  reference page at `docs.github.com/rest/copilot/copilot-usage-metrics`
  still contained zero occurrences of the string `pull_request_review_times`
  when fetched directly on 2026-09-27 for this extraction, so the
  changelog prose is currently the only documented source for this field's
  existence and shape.

### Claim 2: Each `pull_request_review_times` entry includes `authored_by` and `reviewed_by`, both restricted to human contributors in this release

- **Evidence**: Field-by-field description under "What's new."
- **Confidence**: settled (definitional, stated directly)
- **Quote**: "authored_by and reviewed_by: Who opened and who reviewed the
  pull requests in this entry. Both are human in this release."
- **Our assessment**: "In this release" signals this is a current
  constraint, not a permanent design decision — a future update could
  extend `reviewed_by` to include bot/Copilot identities, which would
  change the meaning of the aggregate entry from "human-reviewed PR
  timing" to something broader. Teams building dashboards on this field
  today should not assume the human-only scope is permanent; a future
  changelog could silently widen who counts as a "reviewer" for this
  array without changing the field name.

### Claim 3: `total_merged` counts qualifying pull requests merged in the repository that day, and is expected to be lower than `pull_requests.total_merged` because it excludes PRs merged without any human review

- **Evidence**: Field description ("total_merged: The number of
  qualifying pull requests merged in the repository that day") combined
  with the explicit comparison stated under "Important notes."
- **Confidence**: settled (stated directly, including the expected
  direction of the discrepancy)
- **Quote**: "As a result, pull_request_review_times[].total_merged is
  usually lower than pull_requests.total_merged, which also counts pull
  requests merged without any reviews."
- **Our assessment**: This is a concrete, falsifiable claim about how two
  fields on the same report relate to each other — useful for a pipeline
  sanity check. If a repository shows
  `pull_request_review_times[].total_merged` *higher* than
  `pull_requests.total_merged` for the same day, that is a signal of a
  data integrity problem, not normal variance, since the changelog states
  the inequality should hold in one direction ("usually lower"). Extends
  `docs-github-copilot-repository-level-usage-metrics.md` Claim 4, which
  already documented that `pull_requests`-style CCA/CCR breakdowns exist on
  the same row — this is the first source to state a numeric relationship
  between two fields on that row rather than just listing what each field
  covers.

### Claim 4: Only pull requests that a person opened and at least one other person reviewed qualify; reviews from Copilot code review, other bots, and the PR's own author are excluded from the timing calculation, but a PR reviewed by both a human and Copilot code review is still included

- **Evidence**: "Important notes" → "What is counted" subsection.
- **Confidence**: settled (definitional inclusion/exclusion rule, stated
  directly)
- **Quote**: "Pull requests that a person opened and at least one other
  person reviewed. Only human reviews are timed. Reviews from Copilot
  code review, other bots, and the author are ignored, so a pull request
  reviewed by both a person and Copilot code review is still included."
- **Our assessment**: This is a subtler exclusion rule than "Copilot
  reviews don't count" — it specifically clarifies that Copilot review
  activity does not disqualify a PR from this dataset, it just doesn't
  contribute review-timing signal. This matters for teams that have
  Copilot code review auto-triggered on every PR
  (per the passive-user mechanism documented in
  `docs-github-copilot-code-review-usage-metrics-aggregate.md` Claim 3):
  such organizations will still see those PRs counted in
  `pull_request_review_times` as long as a human also reviewed, and the
  timing reflects only the human review cadence, not any Copilot
  involvement. This means `pull_request_review_times` cannot be used to
  measure whether Copilot code review is speeding up or slowing down the
  human review stages — it measures human-only review timing regardless
  of whether Copilot also touched the PR.

### Claim 5: Durations are measured in minutes and attributed to the day the pull request merged; the existing `pull_requests` fields are unchanged by this addition

- **Evidence**: Closing sentence of the "What's new" section.
- **Confidence**: settled (stated directly)
- **Quote**: "Durations are in minutes and attributed to the day the pull
  request merged. The existing pull_requests fields are unchanged."
- **Our assessment**: The explicit "unchanged" reassurance is a
  backward-compatibility signal for any pipeline already parsing
  `repos-1-day` rows for `pull_requests` fields — this is a purely
  additive change with no schema migration required for existing
  consumers. The merge-date attribution (not PR-creation date, and not the
  date of any individual review event) means a PR spanning multiple report
  days in review will show up once, on its merge day, with all three
  stage durations computed retrospectively. Note this is a new, explicit
  attribution rule for this field specifically — the April 8, 2026
  `median_minutes_to_merge_copilot_reviewed` field
  (`docs-github-copilot-pr-review-metrics.md` Claim 3) is defined only as
  a median time from PR creation to merge, without stating which reporting
  day the data point is attributed to, so this changelog cannot be read as
  confirming the same attribution rule already applied there.

### Claim 6: Splitting total review wait time into three stages reveals which of three distinct bottlenecks is driving delay — waiting for reviewer attention, back-and-forth between reviewers, or sitting approved but unmerged — and each points to a different fix

- **Evidence**: "Why this matters" section, GitHub's stated design
  rationale.
- **Confidence**: anecdotal (vendor framing / design rationale; no case
  study or measured outcome is cited showing teams actually diagnosed and
  fixed a bottleneck using this breakdown)
- **Quote**: "Teams can already see when pull requests take a long time to
  merge, but not where the time goes. Splitting the wait into three stages
  shows whether a pull request is waiting for someone to look at it,
  waiting on back-and-forth between reviewers, or sitting approved and
  unmerged. Each of those points to a different fix, and the 90th
  percentile beside the median shows when a handful of slow pull requests
  is driving the delay."
- **Our assessment**: The three-stage decomposition is a genuinely useful
  measurement primitive independent of whether GitHub's narrative framing
  is proven — knowing *which* stage is slow is objectively more actionable
  than a single aggregate cycle-time number, regardless of outcome
  evidence. But per the same caution already applied to
  `docs-github-copilot-pr-review-metrics.md` Claim 6 (flagging the "helps"
  framing as an undemonstrated hypothesis rather than a measured finding),
  this note should be cited as evidence that a diagnostic *capability* now
  exists, not as evidence that teams using it have actually reduced review
  cycle time. The p90-beside-median design choice is the more concretely
  useful detail: it directly addresses the known weakness of median-only
  cycle-time metrics (a small number of severely delayed PRs can be
  invisible in a median while dominating a p90).

### Claim 7: No backfill — data builds forward only from the release date; pull requests that became ready for review before September 21, 2026 are excluded from `pull_request_review_times` but still count toward `pull_requests.total_merged`

- **Evidence**: "Important notes" → "No backfill" subsection.
- **Confidence**: settled (stated directly, including the exact cutoff
  date and the explicit carve-out for the older field)
- **Quote**: "Data builds forward from the release date, so early days
  will be thin. Pull requests that became ready for review before
  September 21, 2026 are left out of this section but still count toward
  pull_requests.total_merged."
- **Our assessment**: The September 21, 2026 cutoff (four days before the
  September 25 announcement) implies GitHub began collecting the
  underlying ready-for-review timestamps slightly ahead of the public
  release. For any team building a review-SLA dashboard on this field: the
  first several days to weeks of data will show artificially low sample
  counts (per the "days will be thin" phrasing) and should not be
  compared against later, fuller weeks without accounting for this
  ramp-up period.

### Claim 8: A quiet day is represented as an empty array (`[]`), not a zero-value entry; the first-to-final-review stage is `0` when a PR receives only a single review

- **Evidence**: "Important notes" → dedicated subsection distinguishing
  these two null-like cases.
- **Confidence**: settled (stated directly as a data-shape clarification)
- **Quote**: "The array is [] on days a repository merged no qualifying
  pull requests. The first-to-final review stage is 0 when pull requests
  receive a single review."
- **Our assessment**: This is an important parsing distinction for
  pipeline consumers: `[]` means "no qualifying PRs merged that day" (a
  sample-size-zero condition — do not average this day in as if it
  contributed a 0-minute PR), whereas a stage value of `0` inside a
  present entry means "PRs did receive a value, and that value happens to
  be zero minutes because there was no gap between first and final
  review" (a genuine measured zero, not a missing-data marker). A naive
  pipeline that treats `[]` as "0 for all stages" would silently corrupt
  any aggregate computed across days with and without qualifying merges —
  this is the same class of empty-array-vs-zero ambiguity the guide should
  flag as a general Copilot metrics API parsing hazard, not unique to this
  field.

### Claim 9: Access is restricted to enterprise owners/billing managers, organization owners, or custom-role holders with the "View Copilot Metrics" permission, and the Copilot usage metrics policy must be enabled

- **Evidence**: "Important notes" → "Access" subsection.
- **Confidence**: settled (stated directly; wording is materially
  consistent with the access-tier language in prior Copilot metrics
  changelogs)
- **Quote**: "Enterprise owners and billing managers, organization owners,
  and anyone with a custom organization or enterprise role that grants the
  View Copilot Metrics permission can access these reports. The Copilot
  usage metrics policy must be enabled."
- **Our assessment**: This is functionally the same access-tier statement
  already documented in `docs-github-copilot-pr-review-metrics.md` Claim 5
  and echoed across the Copilot metrics changelog series — this field
  inherits the existing `repos-1-day` report's access model rather than
  introducing a new one, consistent with it being an additive field on an
  existing report rather than a new endpoint. Note that the July 17, 2026
  repository-level source (`docs-github-copilot-repository-level-usage-metrics.md`
  Claim 7) found the *linked REST reference page* differentiates enterprise-
  vs. org-scope permission names and OAuth/PAT scopes more precisely than
  the changelog's blanket phrasing — that same gap between changelog prose
  and reference-page precision likely applies here too, though this
  changelog does not repeat the enterprise/org distinction at all.

## Concrete Artifacts

### Verbatim Changelog Body Text (September 25, 2026, confirmed via raw HTML fetch of the `<article>` element)

```
Usage metrics API adds pull request review stages
Improvement | September 25, 2026 • 2 minute read

The enterprise and organization repository-level Copilot usage metrics
reports now break down how long pull requests spend in each stage of
review. A new pull_request_review_times array on each repos-1-day row
reports a median and a 90th percentile for the time from ready for review
to first review, first review to final review, and final review to merge.

What's new
Each entry in pull_request_review_times includes:

authored_by and reviewed_by: Who opened and who reviewed the pull requests
in this entry. Both are human in this release.

total_merged: The number of qualifying pull requests merged in the
repository that day.

median_minutes_ready_to_first_review and p90_minutes_ready_to_first_review:
Time from the pull request becoming ready for review to its first review.

median_minutes_first_to_final_review and p90_minutes_first_to_final_review:
Time between the first and final review.

median_minutes_final_review_to_merge and p90_minutes_final_review_to_merge:
Time from the final review to merge.

Durations are in minutes and attributed to the day the pull request
merged. The existing pull_requests fields are unchanged.

Why this matters
Teams can already see when pull requests take a long time to merge, but
not where the time goes. Splitting the wait into three stages shows
whether a pull request is waiting for someone to look at it, waiting on
back-and-forth between reviewers, or sitting approved and unmerged. Each
of those points to a different fix, and the 90th percentile beside the
median shows when a handful of slow pull requests is driving the delay.

Important notes
Availability: Present in the enterprise and organization repos-1-day
reports.

What is counted: Pull requests that a person opened and at least one
other person reviewed. Only human reviews are timed. Reviews from Copilot
code review, other bots, and the author are ignored, so a pull request
reviewed by both a person and Copilot code review is still included. As a
result, pull_request_review_times[].total_merged is usually lower than
pull_requests.total_merged, which also counts pull requests merged without
any reviews.

No backfill: Data builds forward from the release date, so early days will
be thin. Pull requests that became ready for review before September 21,
2026 are left out of this section but still count toward
pull_requests.total_merged.

A quiet day is an empty array, not a zero: The array is [] on days a
repository merged no qualifying pull requests. The first-to-final review
stage is 0 when pull requests receive a single review.

Access: Enterprise owners and billing managers, organization owners, and
anyone with a custom organization or enterprise role that grants the View
Copilot Metrics permission can access these reports. The Copilot usage
metrics policy must be enabled.

Visit the Copilot usage metrics API documentation to get started.
```

*Source: https://github.blog/changelog/2026-09-25-usage-metrics-api-adds-pull-request-review-stages,
retrieved via direct `curl` fetch of the raw HTML `<article>` element on
2026-09-27.*

### Field Summary (compiled from changelog prose above)

```
# pull_request_review_times — new array field on repos-1-day rows
# Added: September 25, 2026
# Availability: enterprise and organization repos-1-day reports only

Per-entry fields:
  authored_by                                  (human only, this release)
  reviewed_by                                   (human only, this release)
  total_merged                                  (int; qualifying merged PRs that day)
  median_minutes_ready_to_first_review / p90_...
  median_minutes_first_to_final_review  / p90_...
  median_minutes_final_review_to_merge  / p90_...

Inclusion rule: PR opened by a person AND reviewed by >=1 other person.
Exclusion from timing: Copilot code review, other bots, PR author's own
  reviews (PR itself is NOT excluded merely for having a Copilot review).

Data shape rules:
  no qualifying merges that day  -> []            (not a zero-filled entry)
  single review received         -> first_to_final stage = 0 (real zero)
  no backfill                    -> excludes PRs ready-for-review before
                                     2026-09-21

Unchanged: pull_requests.* fields on the same row are not modified by
  this addition.
```

## Cross-References

- **Extends** `docs-github-copilot-repository-level-usage-metrics.md`
  Claim 3 (the `repos-1-day` wrapper response returns only `download_links`
  and `report_day`; the per-repository row schema was "not published on
  the reference page" as of July 18, 2026): This changelog is the first
  source in the corpus to document a concrete field inside that per-row
  schema (`pull_request_review_times`). It does not fill the whole gap —
  it documents one new field, not the complete row schema — but it is
  the first crack in that previously undocumented row structure.
- **Extends** `docs-github-copilot-repository-level-usage-metrics.md`
  Claim 5 (no `repos-28-day` variant confirmed as of July 17, 2026): This
  September 25 update adds a field only to `repos-1-day` rows and makes no
  mention of a rolling-window equivalent, consistent with Claim 5's finding
  still holding as of this extraction — re-checked directly against the
  live REST reference page on 2026-09-27, which still shows 0 occurrences
  of `repos-28-day`.
- **Extends** `docs-github-copilot-pr-review-metrics.md` Claim 3
  (`pull_requests.median_minutes_to_merge_copilot_reviewed` reports a single
  aggregate median cycle time for Copilot-reviewed PRs, with no baseline
  comparison field): This new field is a different, complementary
  measurement — it is not restricted to Copilot-reviewed PRs (it explicitly
  times *human*-only review activity) and it decomposes cycle time into
  three stages with both median and p90, rather than reporting one
  aggregate median. The two fields answer different questions: April 8's
  field asks "how fast do Copilot-reviewed PRs merge, in aggregate?"; this
  field asks "for any PR with human review, which stage of the review
  process is slow?" Neither field lets a team measure whether Copilot
  code review itself speeds up or slows down the human review stages this
  field times, because Copilot's own review activity is explicitly
  excluded from the timing calculation (see Claim 4 above).
- **Corroborates** `docs-github-copilot-code-review-usage-metrics-aggregate.md`
  Claim 3 (passive users are those whose code reviews were auto-triggered
  by a repository or organization policy, without requiring the user to
  actively engage): This new field's exclusion rule (Claim 4 above) means
  a PR that received only an auto-triggered Copilot review — the passive
  pattern that note describes — will not have that review activity
  reflected in `pull_request_review_times` timing at all; the passive
  Copilot review population that note documents at the user level is
  structurally invisible to this new stage-timing field, which only
  measures human review cadence.
- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 5 and
  `docs-github-copilot-repository-level-usage-metrics.md` Claim 7 (access
  restricted to enterprise/org admins and owners with the relevant Copilot
  Metrics permission): The access language in this changelog is
  materially the same blanket statement used in the April 8 changelog,
  continuing the pattern across the Copilot metrics changelog series.
- **Novel**:
  - **First stage-level (not aggregate) PR review timing primitive**: All
    prior Copilot metrics sources in the corpus report either a single
    aggregate cycle-time number (`median_minutes_to_merge_copilot_reviewed`,
    April 8) or user/PR counts. This is the first field to decompose review
    time into ordered sub-stages with per-stage percentiles.
  - **First documented per-row field for the `repos-1-day` report**: As
    noted above, the row-level schema for this report was an open gap in
    the corpus as of July 17, 2026.
  - **Explicit numeric relationship between two sibling fields on the same
    row** (Claim 3): No prior Copilot metrics source states a directional
    inequality between two fields on the same report row; this is the
    first to do so (`pull_request_review_times[].total_merged` usually
    lower than `pull_requests.total_merged`).
  - **Empty-array-vs-zero data-shape distinction stated explicitly**
    (Claim 8): No prior Copilot metrics changelog in the corpus explicitly
    calls out this ambiguity as a named data-shape rule; it is new
    guidance for the guide's general "how to parse Copilot metrics API
    responses" advice, not just for this one field.

## Guide Impact

- **Chapter 05 (Measurement) — "Code review measurement stack" section**
  (extend the section already recommended by
  `docs-github-copilot-code-review-usage-metrics-aggregate.md`'s Guide
  Impact): Add `pull_request_review_times` as a third measurement layer
  alongside PR-level Copilot-review adoption (April 8) and user-level
  active/passive engagement (April 22). Explicitly note this layer measures
  *human* review cadence only and is blind to Copilot's own review
  contribution — it cannot be used, on its own, to argue that Copilot code
  review sped up or slowed down human reviewers, only to diagnose which
  stage of human review is slow for PRs that also happen to qualify (person-
  opened, human-reviewed).
- **Chapter 05 — "Review SLA / bottleneck diagnosis" section** (new or
  extend): Recommend the three-stage breakdown as the concrete "before you
  build a custom review-latency pipeline" starting point: ready-to-first-
  review, first-to-final-review, and final-review-to-merge map to three
  different interventions (reviewer availability/notification tooling,
  review-cycle process changes, merge-queue/CI gating fixes respectively).
  Cite this source for the mapping, but flag per Claim 6 that GitHub's
  framing is design rationale, not a demonstrated outcome — the guide
  should not claim teams that adopt this field have measurably fixed
  bottlenecks, only that the field gives them the diagnostic granularity to
  try.
- **Chapter 02 (Harness Engineering) — "Enterprise Copilot observability
  pipeline" section** (extend, per the pipeline component list already
  built up across the `repos-1-day` and team-level source notes): Add two
  parsing hazards a pipeline consuming this field must handle: (1) the
  empty-array-vs-zero distinction (Claim 8) — do not treat a `[]` day as a
  zero-valued sample in an average; (2) the no-backfill ramp-up period
  (Claim 7) — exclude or flag the first several days after September 21,
  2026 from any trend baseline, since early-period sample sizes will be
  thin by design.

## Extraction Notes

1. **WebFetch summary discarded in favor of raw HTML fetch, per MINER.md
   §2a**: An initial WebFetch call against the changelog URL returned a
   plausible-looking but non-verbatim summary (e.g., it rendered the
   `authored_by`/`reviewed_by` note as "currently limited to human
   contributors" rather than the source's actual "Both are human in this
   release," and collapsed the nuanced Copilot-exclusion rule into a
   flatter "Copilot code reviews and bot reviews are excluded from timing
   calculations" that dropped the "author" exclusion and the "still
   included if also human-reviewed" clarification). The page was
   re-fetched via direct `curl` of the raw HTML, and the `<article>`
   element's text was extracted with a Python script stripping tags —
   every quote in this note is taken from that raw-HTML extraction, not
   from the WebFetch summary.
2. **REST API reference page checked directly, not through WebFetch**: The
   linked `docs.github.com/rest/copilot/copilot-usage-metrics` page was
   fetched via `curl` on 2026-09-27 and searched for `pull_request_review_times`
   (0 matches) and `repos-1-day` (6 matches, consistent with the July 17,
   2026 source note's prior count). This confirms the new field is not yet
   documented on the REST reference page — the changelog prose is
   currently the sole documented source for this field, which is noted as
   a scope gap above rather than guessed at.
3. **Three prior Prospector triage comments on this issue diverge somewhat
   in emphasis**: The issue carries three separate triage comments (an
   apparent re-triage artifact). Two rate novelty "medium" and frame the
   update as an incremental extension of the April 8 aggregate metrics; the
   third rates novelty "high" and correctly identifies the specific new
   field name, its three-stage structure, and the empty-array/no-backfill
   data-quality caveats — that third comment's characterization is the one
   this extraction bears out most closely once the actual changelog text
   was read. The extraction above does not simply adopt either triage
   comment's framing; all nine claims are independently sourced from the
   changelog body text and cross-checked against the corpus.
4. **No contradictions found**: No existing source note claims that
   PR review timing cannot or should not be broken into stages, that
   Copilot review activity should be included in human review timing, or
   makes any conflicting claim about the `repos-1-day` report's row
   schema. This source is purely additive/extending relative to the
   existing corpus — no contradiction issue filed.
5. **No sub-pages beyond the linked REST reference page were followed**:
   The changelog links only to "the Copilot usage metrics API
   documentation" (the REST reference page checked in Extraction Note 2).
   No other substantive linked pages were present on the changelog page
   to follow per MINER.md §1's "up to 5 linked pages" guidance.
