---
source_url: https://github.blog/changelog/2026-05-08-copilot-code-review-comment-types-now-in-usage-metrics-api
source_type: docs
title: "Copilot code review comment types now in usage metrics API"
author: GitHub (official changelog)
date_published: 2026-05-08
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: settled
issue: "#574"
---

# Copilot Code Review Comment Types in the Usage Metrics API (GitHub Changelog)

> GitHub's May 8, 2026 announcement adds a `copilot_suggestions_by_comment_type` array to
> the Copilot usage metrics API — the first API-native acceptance-rate signal for Copilot
> code review, and the first field to partially fill Layer 2 (code trust/acceptance) of the
> Faros three-layer measurement framework that the April 8 metrics API announcement left
> entirely empty.

## Source Context

- **Type**: docs (GitHub official product changelog, ~250 words)
- **Author credibility**: GitHub engineering team announcing a production API change.
  Authoritative for the fact that these new fields exist, what they measure, and their
  availability constraints. Not a credible source for whether comment-type distribution
  is a stable, actionable, or interpretable signal — that requires practitioner validation.
- **Scope**: A new `copilot_suggestions_by_comment_type` array added to the `pull_requests`
  section of the Copilot usage metrics REST API (enterprise and organization endpoints).
  Covers field structure, example comment type categories, availability windows, and access
  tier. Does NOT cover: how many comment types exist in total, whether the comment-type
  taxonomy is stable or evolving, how "applied" is defined (author-accepted vs. committed),
  whether comment types are available in non-Copilot review workflows, or any guidance on
  interpreting comment-type distributions.

## Extracted Claims

### Claim 1: A new `copilot_suggestions_by_comment_type` array is added to the `pull_requests` section of the Copilot usage metrics API, enabling per-category breakdown of Copilot code review suggestions

- **Evidence**: Official GitHub product changelog announcing the new API addition at both
  enterprise and organization reporting levels.
- **Confidence**: settled (product fact — these fields now exist)
- **Quote**: "a new `copilot_suggestions_by_comment_type` array is available under `pull_requests`"
- **Our assessment**: This is an additive extension to the April 8 metrics API, which introduced
  `total_merged_reviewed_by_copilot` (adoption count) and `median_minutes_to_merge_copilot_reviewed`
  (cycle time). Both prior fields treated all Copilot reviews as homogeneous. The May 8 update
  introduces structure within the review: not all suggestions are alike, and now teams can see the
  distribution by type. The field name implies the array has one entry per category with a count,
  not a flat list of individual suggestion instances.

### Claim 2: Each entry in `copilot_suggestions_by_comment_type` contains three fields: `comment_type`, `total_copilot_suggestions`, and `total_copilot_applied_suggestions`

- **Evidence**: Field structure described in the changelog. Three named fields per entry.
- **Confidence**: settled (definitional — field names and meanings stated in changelog)
- **Quote**: (no direct quote; field names listed as structured data in the changelog)
- **Our assessment**: The structure is a per-category tuple: what type (comment_type), how many
  were suggested (total_copilot_suggestions), and how many were acted on
  (total_copilot_applied_suggestions). This combination makes it possible to compute a
  per-category acceptance rate: `total_copilot_applied_suggestions / total_copilot_suggestions`.
  A team with high security-comment suggestion volume but low applied rate has different adoption
  dynamics than one where the same suggestions are routinely accepted.

### Claim 3: Example comment types include "security" and "bug_risk", indicating a functional taxonomy of issue categories

- **Evidence**: The changelog provides these as example values for `comment_type`.
- **Confidence**: settled for these two examples; emerging for the full taxonomy (not documented
  in the changelog)
- **Quote**: (comment_type examples "security" and "bug_risk" listed in changelog; exact
  quote not captured by WebFetch — see Extraction Notes)
- **Our assessment**: Two categories hint at a broader functional taxonomy (likely including
  "style", "performance", "documentation", or similar). The word "such as" in the changelog
  implies these are illustrative, not exhaustive. Teams relying on this field for process
  metrics should document which comment_type values actually appear in their API responses
  before building dashboards, since the full taxonomy is not published. Category stability
  is also unknown — GitHub could rename or add categories across API versions without a
  breaking-change notice.

### Claim 4: `total_copilot_applied_suggestions` is the first acceptance-rate signal in the Copilot review metrics API — a Layer 2 (code trust/acceptance) metric that was absent from the April 8 fields

- **Evidence**: Field definition from changelog. The April 8 changelog (`docs-github-copilot-pr-review-metrics.md`)
  contained no applied/accepted field — both fields measured activity, not developer response.
- **Confidence**: settled (definitional; the Layer 2 framing is our analytical mapping)
- **Quote**: (no direct quote; analytical synthesis across two changelogs)
- **Our assessment**: The Faros three-layer measurement framework (Claim 4 of `blog-faros-claude-code-roi.md`)
  structures AI tool measurement as: Layer 1 (adoption — is the tool being used?), Layer 2 (code
  trust/acceptance — do engineers accept suggestions?), Layer 3 (team performance outcomes). The
  April 8 note explicitly mapped the two existing fields to Layer 1 and Layer 3, observing that
  Layer 2 was entirely missing from the API. `total_copilot_applied_suggestions` fills that gap,
  at least at the per-comment-type aggregate level. It is not a full quality metric — it cannot
  detect whether applied suggestions introduced defects or reduced complexity — but it is the
  first API-native signal that measures developer *response* to Copilot feedback rather than
  just Copilot's *activity*. This is a meaningful step toward the Layer 2 signal the April
  note called missing.

### Claim 5: The new metrics carry the same access restrictions as the April 8 fields: enterprise administrators and organization owners with Copilot usage metrics access only

- **Evidence**: Access tier stated in the changelog. Mirrors the April 8 restrictions.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "enterprise administrators and organization owners"
- **Our assessment**: Same operational constraint as before. Teams on GitHub.com (non-enterprise)
  or alternative git hosting (GitLab, Bitbucket) cannot access this data. Within GitHub Enterprise
  Cloud, only admins and org owners see the metrics — individual engineers and team leads cannot
  access comment-type data without escalation or a dedicated reporting pipeline. For Ch05 guidance:
  this restriction means comment-type metrics are a leadership-layer signal, not an engineer-facing
  feedback loop.

### Claim 6: The metrics are available in single-day and 28-day rolling windows at enterprise and organization levels; repository-level drilling is explicitly not yet supported

- **Evidence**: Window and granularity stated directly in the changelog; the "not yet" phrasing
  for repository-level explicitly acknowledges this as a current limitation.
- **Confidence**: settled (stated directly)
- **Quote**: "single-day and 28-day rolling window reports" / "cannot drill down to the repository level"
- **Our assessment**: The lack of repository-level drilling is the most operationally significant
  limitation of this feature. A team wanting to know which repositories generate the most security
  suggestions, or where bug_risk comments have the lowest acceptance rate, cannot get that from the
  API alone. The "not yet" phrasing implies GitHub intends to add this, but there is no commitment
  timeline. Teams needing repository-level comment-type data must either wait for a future API
  update or build a custom extraction layer against the Copilot code review comments in individual
  PR review events.

### Claim 7: The changelog frames comment-type metrics as enabling teams to "identify which categories of issues Copilot code review surfaces most often" and to "compare suggestion volume to applied suggestions per type" — a measurement value framing, not a causal claim

- **Evidence**: Business value language from changelog.
- **Confidence**: anecdotal (vendor framing; actual measurement utility is undemonstrated)
- **Quote**: "which categories of issues Copilot code review surfaces most often" / "compare suggestion volume to applied suggestions per type"
- **Our assessment**: Unlike the April 8 changelog's implicit "Copilot helps" causal framing
  (flagged as Claim 6 of `docs-github-copilot-pr-review-metrics.md`), the May 8 value framing
  is more defensible — it presents the metrics as analytical tools, not as proof of benefit. A team
  can legitimately use this data to understand which issue categories Copilot finds most often and
  whether developers act on them. What cannot be inferred: whether more suggestions accepted means
  better code, whether comment-type frequency reflects actual codebase risk, or whether a low
  applied rate for security suggestions means developers disagree with Copilot or simply don't read
  the suggestions. The metrics enable questions; they do not answer them.

## Concrete Artifacts

### New API Structure (from changelog, May 8, 2026)

```
# Copilot usage metrics API — PR comment-type breakdown (added May 8, 2026)
# Available at: GET /orgs/{org}/copilot/metrics
# Also available at enterprise level
# Reporting windows: single-day and 28-day rolling
# Repository-level: NOT available (acknowledged limitation; "not yet supported")

pull_requests.copilot_suggestions_by_comment_type
  Type: array of objects
  Description: Breakdown of Copilot code review suggestions by the comment type
               assigned by Copilot at posting time.

  Each array entry contains:
    comment_type
      Type: string
      Description: Category label assigned by Copilot (e.g., "security", "bug_risk")
      Note: Full taxonomy not published; categories may evolve across API versions.

    total_copilot_suggestions
      Type: integer
      Description: Count of suggestions posted in this category during the reporting period.
      What it measures: Suggestion volume per issue category.
      What it does NOT measure: Suggestion quality, accuracy, or relevance.

    total_copilot_applied_suggestions
      Type: integer
      Description: Number of suggestions in this category that developers actually applied.
      What it measures: Developer acceptance rate (used as numerator vs. total_copilot_suggestions).
      What it does NOT measure: Whether applied suggestions improved code quality,
                                how "applied" is defined (accepted vs. committed to branch).
```

*Source: GitHub Copilot official changelog, May 8, 2026*

### Full Copilot PR Measurement Arc (as of May 2026)

```
Stage 1 — Authoring (added ~February 2026):
  pull_requests.total_pr_summaries_created
    → Count of PRs where Copilot generated a PR summary
    → Layer 1 (adoption)

Stage 2 — Review adoption (added April 8, 2026):
  pull_requests.total_merged_reviewed_by_copilot
    → Count of merged PRs that received a Copilot code review
    → Layer 1 (adoption)

Stage 3 — Review cycle time (added April 8, 2026):
  pull_requests.median_minutes_to_merge_copilot_reviewed
    → Median minutes to merge for Copilot-reviewed PRs
    → Layer 3 (team performance) — requires baseline comparison to interpret

Stage 4 — Comment-type acceptance (added May 8, 2026):
  pull_requests.copilot_suggestions_by_comment_type[]
    → Per-category: suggestions posted + suggestions applied
    → Layer 2 (code trust / acceptance) — first acceptance signal in the API

Still missing (May 2026):
  pull_requests.median_minutes_to_merge_baseline
    → Non-Copilot-reviewed cohort cycle time (needed to interpret Stage 3)
    → Must be computed externally

  pull_requests.copilot_suggestions_by_comment_type[].quality_outcome
    → Whether applied suggestions reduced defects, complexity, incidents
    → Not available through the API; requires pairing with static analysis data
```

*Derived from this source, `docs-github-copilot-pr-review-metrics.md`, and the
 April 2026 authoring metrics reference in that note*

## Cross-References

- **Extends** `docs-github-copilot-pr-review-metrics.md` Claim 1: the April 8
  announcement introduced two fields tracking Copilot review at the PR lifecycle level
  (adoption count, cycle time). This May 8 update adds a third dimension — per-category
  suggestion volume and acceptance — turning a two-variable API into a three-variable one.

- **Extends** `docs-github-copilot-pr-review-metrics.md` Claim 4: the April 8 note
  described the authoring-to-merge measurement arc (Stage 1: PR summaries, Stage 2: review
  adoption, Stage 3: cycle time). This source adds Stage 4 (comment-type acceptance),
  completing the arc with a feedback quality signal. The arc now covers: creation → adoption
  → cycle time → suggestion engagement.

- **Directly addresses the gap** identified in `docs-github-copilot-pr-review-metrics.md`
  Extraction Notes (point 4): "The API provides no quality metrics for Copilot reviews."
  `total_copilot_applied_suggestions` is not a full quality metric, but it is the first
  API-native signal measuring developer *response* to review feedback rather than just
  Copilot's *activity*. The gap is partially closed, not fully.

- **Fills Layer 2** of the Faros three-layer measurement framework (`blog-faros-claude-code-roi.md`
  Claim 4). The April 8 note mapped the existing fields to Layer 1 and Layer 3 while noting
  Layer 2 (code trust/acceptance) had no API equivalent. `total_copilot_applied_suggestions`
  per comment type is the first Layer 2 signal available natively through the Copilot API.

- **Corroborates** `docs-github-copilot-pr-review-metrics.md` Claim 5 (access tier): the
  same enterprise admin / org owner restriction applies to the new fields. The governance
  model is consistent across the Copilot metrics API.

- **Corroborates** the measurement sequencing principle from `blog-faros-claude-code-roi.md`
  Claim 5: `total_copilot_suggestions` alone, without `total_copilot_applied_suggestions`,
  would be a vanity metric of the kind Faros warns against. GitHub has bundled both fields
  together in the same array entry, structurally preventing "suggestions posted" from being
  reported without the "suggestions applied" counterpart.

- **Complements** `paper-miller-speed-cost-quality.md` (Speed at the Cost of Quality):
  Miller et al. find that AI assistance can increase velocity at the cost of code quality.
  The comment-type acceptance data (especially for "security" and "bug_risk" categories)
  provides a partial proxy for one direction of quality risk — if developers ignore Copilot's
  security suggestions, the acceptance rate will show it. This does not resolve the quality
  measurement gap (Miller's finding is about defect rates, not suggestion acceptance), but
  it adds a new dimension to pair with external quality signals.

- **Contradicts**: None. This source is a direct extension of the April 8 API announcement
  and adds to, not against, the existing corpus claims. No contradiction issue required.

- **Novel**: First API-native per-category acceptance rate signal for Copilot code review.
  The comment_type field is new to the corpus — no prior source documents the existence of
  a typed comment taxonomy in Copilot review. The applied/suggested ratio pattern per category
  is the first two-dimensional view of Copilot review engagement available through the vendor API.

## Guide Impact

### Chapter 05: Team Adoption

- **Section "Measuring impact"**: Update the Copilot review metrics entry (added from
  `docs-github-copilot-pr-review-metrics.md`) to note that as of May 8, 2026, a third
  measurement dimension is available: per-category suggestion acceptance rates. Reference
  `total_copilot_applied_suggestions / total_copilot_suggestions` per comment type as a
  Layer 2 metric (code trust) that was previously unavailable through the vendor API.
- **Section "Measuring impact"**: Add guidance that `copilot_suggestions_by_comment_type`
  enables teams to identify which issue categories Copilot flags most frequently and whether
  developers accept those suggestions. Frame this as an input to triaging the Copilot review
  configuration — a team with high security-comment volume but low acceptance rates may have
  a model misconfigured for its codebase risk profile, or may have developers who disagree
  with Copilot's security assessments. The data surfaces the gap; diagnosing it requires
  qualitative follow-up.
- **Section "Measuring impact"**: Explicitly note the repository-level limitation. Teams that
  want to identify which repositories drive the most low-acceptance security suggestions cannot
  do so from the API alone (as of May 2026). This is a significant gap for large enterprises
  with heterogeneous codebases. Until GitHub adds repository-level drilling, teams must build
  custom extraction pipelines or wait for a future API update.
- **Layer 2 measurement now API-accessible**: If Ch05 adopts the Faros three-layer framework
  as its measurement structure, update the "Layer 2" entry to note that the Copilot usage
  metrics API now provides a native Layer 2 signal via `total_copilot_applied_suggestions`
  per comment type. This replaces the prior "Layer 2 requires Faros or custom instrumentation"
  qualification for GitHub Enterprise teams.

### Chapter 01: Daily Workflows

- **Code review patterns**: Engineers can now see at the org level what types of issues
  Copilot review flags most often. While individual engineers do not have API access (admin/
  org-owner only), engineering leads can surface summary data ("Copilot flags 3x more security
  issues than bug_risk issues in our repos") as context for calibrating how much attention to
  pay to each comment type. This is useful for teams developing harness guidelines around
  Copilot review workflows.

## Extraction Notes

1. **Source is thin by design**: This is a product changelog of ~250 words. The extractable
   content is exhausted in the seven claims above plus the concrete artifacts.
2. **WebFetch returned structured summaries, not verbatim HTML**: Multiple WebFetch calls
   were made to get the most complete text possible. Quoted passages that appeared in
   quotation marks in the WebFetch output (e.g., "a new `copilot_suggestions_by_comment_type`
   array is available under `pull_requests`", "which categories of issues Copilot code review
   surfaces most often", "compare suggestion volume to applied suggestions per type",
   "single-day and 28-day rolling window reports", "cannot drill down to the repository level")
   are reproduced here as quotes. The Assayer should spot-check these against the live source
   URL to confirm character-for-character accuracy.
3. **Full comment-type taxonomy unknown**: The changelog lists "security" and "bug_risk" as
   examples; the full set of valid comment_type values is not published in the changelog or in
   the REST API documentation checked (which did not yet reflect the new fields). Any guide
   advice citing specific comment-type values should acknowledge this limitation.
4. **REST API docs not yet updated**: The Copilot metrics REST API documentation page
   (`docs.github.com/en/rest/copilot/copilot-metrics`) did not yet contain the new fields at
   time of extraction (2026-05-09). The field schema in the Concrete Artifacts section is
   derived from the changelog text, not the formal docs schema. Treat field type annotations
   as inferred, not authoritative.
5. **No contradictions filed**: This source extends the April 8 announcement and introduces
   no material contradictions with any existing source note.
