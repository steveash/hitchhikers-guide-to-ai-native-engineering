---
source_url: https://github.blog/changelog/2026-04-08-copilot-reviewed-pull-request-merge-metrics-now-in-the-usage-metrics-api
source_type: docs
title: "Copilot-reviewed pull request merge metrics now in the usage metrics API"
author: GitHub (official changelog)
date_published: 2026-04-08
date_extracted: 2026-04-15
last_checked: 2026-04-15
status: current
confidence_overall: anecdotal
issue: "#91"
---

# Copilot PR Review Metrics in the Usage Metrics API (GitHub Changelog)

> GitHub's official announcement of two new Copilot usage metrics API fields that
> track whether Copilot reviewed a merged PR and how long Copilot-reviewed PRs
> take to merge. The metrics are a measurement primitive, not a demonstrated
> finding — the changelog frames Copilot review as benefiting time-to-merge, but
> no evidence supports that claim; these fields exist to let teams collect evidence
> themselves.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these fields now exist and what they measure.
  Not a credible source for the *effect* of Copilot reviews on merge time — that
  causal claim is vendor marketing, not a measured outcome.
- **Scope**: Two new fields added to the Copilot usage metrics REST API
  (`/orgs/{org}/copilot/metrics` and the enterprise-level equivalent). Covers
  field definitions, availability tiers, and the implicit measurement rationale.
  Does NOT cover: whether Copilot reviews actually improve merge times, how the
  review quality compares to human review, any data on adoption of the Copilot
  review feature, or any guidance on what thresholds indicate success.

## Extracted Claims

### Claim 1: Two new API fields track Copilot code review adoption at the PR lifecycle level

- **Evidence**: Official GitHub product changelog announcing general availability
  of two new fields in the Copilot usage metrics API.
- **Confidence**: settled (these fields exist — this is a product fact)
- **Quote**: The metrics "capture how Copilot helps review pull requests, letting
  you compare merge rates and cycle times"
- **Our assessment**: The fields themselves are settled — they are documented,
  available, and measurable. What is not settled is whether the numbers they
  produce will tell you anything useful, since that depends on whether Copilot
  review has any effect on the outcomes they measure. A team can start collecting
  these metrics immediately; interpreting them requires baseline data and a
  comparison period. For Ch05: note that these fields give teams a no-cost,
  vendor-native starting point for measuring Copilot review impact — more
  accessible than the Faros cohort methodology, but narrower (no control group,
  no matching, no baseline comparison built in).

### Claim 2: `pull_requests.total_merged_reviewed_by_copilot` counts merged PRs that received a Copilot code review during the reporting period

- **Evidence**: Field definition from official API documentation accompanying the
  changelog. Available in single-day and 28-day rolling windows.
- **Confidence**: settled (definitional)
- **Quote**: N/A (field name and definition stated directly)
- **Our assessment**: This is an *adoption* metric: how many of your merged PRs
  had Copilot review at all. By itself it does not measure quality or speed, only
  penetration. A team that enables Copilot review enterprise-wide but whose
  engineers dismiss every suggestion will show a high `total_merged_reviewed_by_copilot`
  count — the metric is blind to engagement quality. Cf. Faros's "vanity metrics
  to avoid" warning: raw counts without engagement depth are gameable.

### Claim 3: `pull_requests.median_minutes_to_merge_copilot_reviewed` reports the median time from PR creation to merge for Copilot-reviewed PRs

- **Evidence**: Field definition from official API documentation. Available in
  single-day and 28-day rolling windows.
- **Confidence**: settled (definitional)
- **Quote**: N/A
- **Our assessment**: This is the more interesting field. Median cycle time is a
  real outcome metric, not a vanity metric — if Copilot reviews meaningfully speed
  up review cycles, this number will fall over time. But it is only half of the
  measurement needed: to know whether the change is *because* of Copilot review,
  a team needs the same metric for PRs that were *not* Copilot-reviewed in the same
  period. The API does not currently provide that comparison field directly, meaning
  teams either need to compute it from raw PR data or use a third-party analytics
  layer (e.g., Faros). Without the baseline, this metric shows a number, not a
  direction.

### Claim 4: Copilot review metrics build on earlier PR authoring metrics (added February 2026), completing an authoring-to-merge measurement arc

- **Evidence**: Changelog explicitly references "earlier pull request authoring
  metrics from February" as the prior addition.
- **Confidence**: settled (stated in changelog)
- **Quote**: "building on earlier pull request authoring metrics from February"
- **Our assessment**: The authoring-plus-review coverage means a team can now
  measure the full AI-augmented PR lifecycle through the Copilot API: how many
  PRs were written with Copilot assistance, how many were reviewed by Copilot,
  and how long those reviewed PRs took to merge. This is a more complete
  measurement arc than existed six weeks earlier. The missing link remains quality:
  neither the authoring metrics nor the review metrics track whether Copilot's
  contributions introduced defects, reduced complexity, or affected test coverage.
  Pair with Miller et al. (Speed at the Cost of Quality) for that dimension.

### Claim 5: These metrics are restricted to enterprise administrators and organization owners with Copilot usage metrics access

- **Evidence**: Access tier stated directly in the changelog.
- **Confidence**: settled (stated in official changelog)
- **Quote**: N/A
- **Our assessment**: Operational constraint that matters for teams. If a team
  is not on GitHub Enterprise Cloud or does not have an admin role, these fields
  are not available. Teams using GitHub.com (non-enterprise) or other git hosting
  (GitLab, Bitbucket) cannot use this measurement approach. The Faros cohort
  methodology is host-agnostic and remains the more portable option for
  cross-platform teams.

### Claim 6: The framing that Copilot review "helps" and "compare merge rates and cycle times" implies an expected positive outcome — this is an undemonstrated hypothesis

- **Evidence**: Prospector triage note; standard vendor marketing practice; no
  empirical study cited in the changelog.
- **Confidence**: anecdotal (vendor assertion, not a measured finding)
- **Quote**: "capture how Copilot helps review pull requests, letting you compare
  merge rates and cycle times" (emphasis on "helps" — stated as given, not as
  hypothesis)
- **Our assessment**: The changelog frames Copilot review as already known to be
  beneficial and positions these metrics as tools to *observe* that benefit. This
  is logically backwards: the metrics are what you would use to *determine* whether
  the benefit exists. The Prospector correctly flagged this: "the claimed benefit
  is a hypothesis the metrics are designed to test, not a demonstrated finding."
  Do not cite this changelog as evidence that Copilot reviews reduce cycle time.
  Cite it only as evidence that the measurement primitive now exists.

## Concrete Artifacts

### API Fields (from changelog and related docs)

```
# Copilot usage metrics API — PR review fields (added April 8, 2026)
# Available at: GET /orgs/{org}/copilot/metrics
# Also available at enterprise level
# Reporting windows: single-day and 28-day rolling

pull_requests.total_merged_reviewed_by_copilot
  Type: integer
  Description: Count of merged PRs that received a Copilot code review
               during the reporting period.
  What it measures: Adoption penetration of Copilot review feature.
  What it does NOT measure: Review quality, acceptance rate, engineer engagement.

pull_requests.median_minutes_to_merge_copilot_reviewed
  Type: integer (minutes)
  Description: Median time from PR creation to merge for PRs that received
               a Copilot code review.
  What it measures: Cycle time for the Copilot-reviewed cohort.
  What it does NOT measure: Cycle time for the non-Copilot-reviewed cohort
                            (needed to compute the baseline delta).
```

### Full Copilot PR Authoring + Review Measurement Arc (as of April 2026)

```
Stage 1 — Authoring (added February 2026, approx):
  pull_requests.total_pr_summaries_created
    → Count of PRs where Copilot generated a PR summary

Stage 2 — Review (added April 8, 2026):
  pull_requests.total_merged_reviewed_by_copilot
    → Count of merged PRs that had Copilot code review

Stage 3 — Cycle time (added April 8, 2026):
  pull_requests.median_minutes_to_merge_copilot_reviewed
    → Median minutes to merge, Copilot-reviewed PRs

Missing:
  pull_requests.median_minutes_to_merge_baseline
    → Median minutes to merge, PRs NOT reviewed by Copilot (same period)
    → Must be computed externally (e.g., GitHub Advanced Security, Faros,
       custom script against pull request REST API)
```

## Cross-References

- **Corroborates** `blog-faros-claude-code-roi.md` Claim 4: the three-layer
  measurement framework (adoption → code trust → team performance). The new API
  fields slot directly into Layer 1 (adoption: `total_merged_reviewed_by_copilot`)
  and Layer 3 (team performance: `median_minutes_to_merge_copilot_reviewed`). They
  do not address Layer 2 (code trust / acceptance rate).
- **Corroborates** `blog-faros-claude-code-roi.md` Claim 5: vanity metrics warning.
  `total_merged_reviewed_by_copilot` alone is the kind of metric Faros warns
  against — it measures "did the tool touch this?" not "did the tool help?"
  `median_minutes_to_merge_copilot_reviewed` without a baseline is also vacuous.
  The fields become meaningful only when compared to non-Copilot-reviewed PRs.
- **Extends** `blog-faros-claude-code-roi.md` with a no-cost vendor-native
  measurement entry point. Teams that cannot afford or justify Faros can start
  collecting these metrics immediately via the existing Copilot usage metrics API
  access they already have, provided they are on GitHub Enterprise Cloud.
- **Complements** `survey-pragmaticengineer-ai-tooling-2026.md` which explicitly
  notes that code review process changes are NOT covered by that survey. This API
  changelog is the closest thing to a measurement specification for those gaps, even
  if it does not fill the empirical gap in the survey.
- **Complements** `paper-miller-speed-cost-quality.md` (Speed at the Cost of
  Quality): Miller et al. find velocity gains from AI assistance come with quality
  costs. The Copilot review metrics track velocity (`median_minutes_to_merge`)
  but are blind to quality — the combination of this API data and static-analysis
  metrics would give a fuller picture of whether Copilot review improves cycle time
  without degrading quality.
- **Novel**: This is the first source in the corpus documenting a vendor-native
  API-accessible measurement primitive for AI code review adoption. Prior sources
  discuss what to measure (Faros), who is using tools (Pragmatic Engineer survey),
  or task-level patterns (Anthropic transformation report) — none documented a
  specific API field pointing at Copilot review cycle time.

## Guide Impact

### Chapter 05: Team Adoption

- **Section "Measuring impact"**: Add a note that GitHub Enterprise teams using
  Copilot already have free access to review-cycle metrics via the usage metrics
  API. Reference `pull_requests.median_minutes_to_merge_copilot_reviewed` as a
  low-cost starting point before investing in a full Faros-style cohort study.
  Caveat: this metric needs a non-Copilot-reviewed baseline to be interpretable;
  document how to extract that from the GitHub PR API.
- **Section "Measuring impact"**: Use this source to illustrate the difference
  between an adoption metric (`total_merged_reviewed_by_copilot`) and an outcome
  metric (`median_minutes_to_merge_copilot_reviewed`). Only the outcome metric
  is meaningful — but only in comparison to a baseline.
- **Section "Measuring impact"**: Explicitly flag that the API provides no quality
  metrics for Copilot reviews. Teams using these fields should pair them with
  static analysis data (e.g., CodeQL, SonarQube) to detect whether faster merge
  cycles come at a quality cost (per Miller et al.).

### Chapter 01: Daily Workflows

- **Code review patterns**: Reference this as evidence that vendor tooling now
  tracks Copilot's involvement in the review stage, not just the authoring stage.
  Engineers can now see in their organization's metrics whether PRs they receive
  have been Copilot-reviewed — a relevant context signal for calibrating how
  carefully to read the review suggestions.

## Extraction Notes

1. **Source is thin by design**: This is a product changelog, not a practitioner
   post or research paper. The full content is ~300 words. The substantive claims
   are exhausted in six extracted claims above — this source should not be cited
   for more than it contains.
2. **Two API fetches**: Main changelog fetched once; the linked documentation page
   was fetched but returned only partial PR metric details (the docs page renders
   dynamically and the full field schema was not returned). Field definitions above
   are derived from the changelog text and the partial docs return.
3. **Vendor framing noted and quarantined**: The changelog's implicit "Copilot
   review helps" framing was explicitly extracted as Claim 6 and flagged as an
   undemonstrated hypothesis, per the Prospector's guidance.
4. **No contradictions to file**: No existing source note claims that Copilot
   review does or does not reduce cycle time, so there is no side to contradict.
   Miller et al.'s quality-cost finding is complementary, not contradictory.
5. **Enterprise-only limitation**: If Ch05 or Ch01 cites these metrics, they should
   note the GitHub Enterprise Cloud prerequisite — the fields are not available on
   github.com free/team plans.
