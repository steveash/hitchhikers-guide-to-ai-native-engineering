---
source_url: https://github.blog/changelog/2026-09-17-copilot-impact-dashboard-now-shows-feature-engagement
source_type: docs
title: "Copilot impact dashboard now shows feature engagement"
author: GitHub (official changelog)
date_published: 2026-09-17
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: settled
issue: "#3528"
---

# Copilot Impact Dashboard Now Shows Feature Engagement (GitHub Changelog, September 17, 2026)

> GitHub's September 17, 2026 changelog adds a 28-day feature-engagement
> breakdown (`copilot_feature_engagement` / `totals_by_feature`) to the
> Copilot impact dashboard and enterprise/organization aggregate reports —
> the first metrics-API field to report *which* Copilot surfaces active
> users regularly touch — alongside `users_in_phase_28d`, a correction to
> the adoption-phase reporting that stops silently dropping inactive-that-day
> users from the phase population.

## Source Context

- **Type**: docs (GitHub official product changelog, ~300 words, "2 minute
  read," September 17, 2026). Fetched via direct HTTP request (not
  WebFetch) so the extracted text below is raw article text, not an
  AI-summarized pass.
- **Author credibility**: GitHub engineering team announcing a production
  API and dashboard change. Authoritative for the fact that these fields
  exist, their scope, their definitions, and their null/omission semantics.
  Not authoritative for any claim about whether feature-engagement data
  actually changes enablement outcomes in practice — no adoption numbers,
  before/after case study, or customer example is cited.
- **Scope**: Covers three related additions: (1) a dashboard-only feature
  engagement view, (2) the `copilot_feature_engagement` API field (with its
  nested `totals_by_feature` breakdown) on enterprise/organization 28-day
  aggregate reports, and (3) `users_in_phase_28d`, a new field on the
  existing adoption-phase breakdown. Covers field scope, the seven
  engagement-counted features, the two-of-28-days engagement threshold,
  null/omission semantics, and access tier. Does NOT cover: the exact JSON
  schema/types for `copilot_feature_engagement` (the changelog describes it
  in prose, not a schema table); whether the 28-day feature-engagement data
  is also exposed per-user (explicitly stated it is not); how
  `users_in_phase_28d` interacts with the `version` field on phase objects
  documented in `docs-github-copilot-usage-metrics-adoption-cohorts.md`; or
  any outcome/productivity data tied to feature engagement.

## Extracted Claims

### Claim 1: The Copilot impact dashboard now shows how many active users engaged with each included feature on at least two days during the 28-day period

- **Evidence**: "What's new" section, first bullet, official changelog.
- **Confidence**: settled (product fact — dashboard feature explicitly
  described with its threshold)
- **Quote**: "Shows how many active users engaged with each included feature on at least two days during the 28-day period."
- **Our assessment**: The "at least two days" threshold is the operative
  engagement bar — a user who touched a feature exactly once in 28 days does
  not count as "engaged" with it for this metric. This is a materially
  different (stricter) definition than a simple "used at least once" active-
  user count, and it is the first place in the corpus a specific numeric
  engagement threshold is stated for a Copilot metrics field. Teams
  comparing this figure against other "active user" counts elsewhere in the
  API (which typically count any activity on the day/window) should not
  treat the numbers as directly comparable — this one has a higher bar.

### Claim 2: `copilot_feature_engagement` adds the dashboard's active-user total and feature engagement counts to enterprise and organization 28-day aggregate reports

- **Evidence**: "What's new" section, second bullet, official changelog.
- **Confidence**: settled (product fact — explicit field name and report
  placement)
- **Quote**: "Adds the dashboard's active-user total and feature engagement counts to enterprise and organization 28-day aggregate reports."
- **Our assessment**: This is the API-level counterpart to the dashboard
  view in Claim 1 — the same two-of-28-days engagement data becomes
  queryable rather than only dashboard-visible. Scoping to 28-day aggregate
  reports only (not 1-day reports, per the field's own engagement window)
  is consistent with the metric's inherent multi-day definition: a
  "two of 28 days" threshold cannot be evaluated from a single day's data,
  so a 1-day-report version of this field would be structurally impossible,
  not merely omitted.

### Claim 3: `totals_by_feature` breaks the feature-engagement count down by seven named surfaces: code completion, agent edit, passive Copilot code review, active Copilot code review, Copilot cloud agent, Copilot CLI, and Copilot app

- **Evidence**: "What's new" section, third bullet, official changelog.
- **Confidence**: settled (definitional enumeration from official changelog)
- **Quote**: "Breaks engagement down by code completion, agent edit, passive Copilot code review, active Copilot code review, Copilot cloud agent, Copilot CLI, and Copilot app."
- **Our assessment**: This is the first field in the corpus to report
  feature-level *engagement* (regular, multi-day use) rather than feature-
  level *activity counts*. It also reuses the field name `totals_by_feature`
  — a name already established by the April 10, 2026 CLI-integration
  changelog (`docs-github-copilot-cli-activity-usage-metrics.md` Claim 3) for
  a *different* breakdown: the top-level `totals_by_feature` array that
  tags raw activity-count rows with `feature=copilot_cli` and similar
  values. This changelog's `totals_by_feature` is nested inside
  `copilot_feature_engagement` and counts distinct *engaged users per
  feature over 28 days*, not activity-event totals per feature. The
  changelog does not flag this name reuse or disambiguate the two fields
  from each other; see Cross-References and Extraction Notes for the
  practical risk this creates for anyone building a pipeline that already
  reads the pre-existing top-level `totals_by_feature`.

### Claim 4: Active Copilot code review means a user manually requested a Copilot review or applied a Copilot review suggestion; passive Copilot code review means Copilot was automatically assigned to review the user's pull request without the user actively engaging with the review

- **Evidence**: "Important notes" section, second bullet, official
  changelog.
- **Confidence**: settled (explicit definitional distinction from official
  changelog)
- **Quote**: "Active Copilot code review means a user manually requested a Copilot review or applied a Copilot review suggestion. Passive Copilot code review means Copilot was automatically assigned to review the user's pull request without the user actively engaging with the review."
- **Our assessment**: This active/passive split lets an organization
  distinguish developers who deliberately invoke Copilot review from
  developers who merely receive it via auto-assignment and never engage
  with the output. A high "passive" count relative to "active" would signal
  that auto-assignment, not developer intent, is driving most of an org's
  code-review engagement number — a meaningfully different adoption story
  than the same total driven by active requests. No prior source note in
  the corpus documents this active/passive distinction for Copilot code
  review; it is a new and useful diagnostic axis for Chapter 05 measurement
  guidance.

### Claim 5: Feature engagement data is available in enterprise and organization 28-day aggregate reports only and is not added to user-level reports; a single user can be counted under more than one feature

- **Evidence**: "Important notes" section, first bullet, official
  changelog.
- **Confidence**: settled (explicit scoping and counting-rule statement)
- **Quote**: "Feature engagement is available in enterprise and organization 28-day aggregate reports and is not added to user-level reports. A user can be counted under more than one feature."
- **Our assessment**: The multi-counting rule means the seven per-feature
  counts in `totals_by_feature` do not sum to the dashboard's overall
  active-user total — a user engaged with both code completion and Copilot
  CLI is counted once in each feature's bucket. Anyone summing the seven
  feature counts to reconstruct total active users would overcount for
  every multi-surface user, which is itself useful signal (it approximates
  cross-surface breadth) but must not be mistaken for a headcount. The
  absence from user-level reports also means an org cannot join this data
  to individual users via the API — it is an aggregate-only lens, unlike
  the per-user `ai_adoption_phase` field documented in
  `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 1.

### Claim 6: `users_in_phase_28d` reports the full rolling 28-day population classified into each AI adoption phase as of that day, while the existing `total_engaged_users` field continues to only report users in the phase who were active that specific day

- **Evidence**: "What's new" section, fourth bullet, official changelog.
- **Confidence**: settled (explicit field definition and contrast with
  prior field behavior)
- **Quote**: "Reports the full rolling 28-day population classified into each AI adoption phase as of that day. The existing total_engaged_users field continues to only report users in the phase who were active that day."
- **Our assessment**: This is the corpus's first documentation of a
  `total_engaged_users` field name for the adoption-phase breakdown — the
  May 29, 2026 source (`docs-github-copilot-usage-metrics-adoption-cohorts.md`
  Claim 7) named the per-phase metric only generically as "engaged users"
  without giving the exact field identifier. This changelog both names that
  field explicitly and reveals a previously undocumented limitation in it:
  `total_engaged_users` undercounts the true phase population by excluding
  anyone in the phase who did not happen to be active on the specific
  report day, even though the phase classification itself is already a
  28-day rolling calculation. `users_in_phase_28d` fixes that mismatch by
  reporting the full rolling cohort regardless of same-day activity. For
  any organization that used `total_engaged_users` as a phase-size
  denominator (e.g., computing "% of Phase 3 users who merged a PR today"),
  the historical denominator was silently smaller than the true phase
  population — this is worth flagging prominently for Chapter 05 since it
  affects the correctness of any prior per-phase percentage calculated
  against `total_engaged_users`.

### Claim 7: `users_in_phase_28d` is omitted when the phase population was not measured, while a value of 0 means the phase was measured and had no users

- **Evidence**: "Important notes" section, third bullet, official
  changelog.
- **Confidence**: settled (explicit null/omission semantics from official
  changelog)
- **Quote**: "users_in_phase_28d is omitted when the phase population was not measured. A value of 0 means the phase was measured and had no users."
- **Our assessment**: This omitted-vs-zero distinction is a correctness
  requirement for any consumer: code that treats a missing field as `0` by
  default (a common JSON-parsing default) would silently conflate "we don't
  know" with "we know it's empty," producing false negatives in dashboards
  or alerts that key off phase population size. This mirrors the general
  "absent vs. null vs. zero" caution the corpus has flagged for other
  Copilot metrics fields (e.g., the `copilot_feature_engagement` object
  itself, Claim 8 below) — pipelines built against this API need explicit
  handling for all three states, not just numeric parsing.

### Claim 8: The `copilot_feature_engagement` object can be absent or null when the calculation is unavailable

- **Evidence**: "Important notes" section, fourth bullet, official
  changelog.
- **Confidence**: settled (explicit availability caveat from official
  changelog)
- **Quote**: "The copilot_feature_engagement object can be absent or null when the calculation is unavailable."
- **Our assessment**: Combined with Claim 7's omission semantics for
  `users_in_phase_28d`, this changelog documents two independent
  absent/null fields in the same release — both requiring defensive parsing
  rather than assuming presence. This is a recurring pattern in the
  Copilot usage metrics API (the corpus's `docs-github-copilot-cli-agentic-customization-metrics.md`
  documents similar per-category null/empty semantics for the September 17
  CLI-customization fields released the same day) and should be called out
  as a general integration rule rather than a one-off caveat specific to
  this changelog.

### Claim 9: Access to this data requires enterprise owner/billing manager status, organization owner status, or a custom organization/enterprise role granting the "View Copilot Metrics" permission, with the Copilot usage metrics policy enabled

- **Evidence**: "Important notes" section, fifth bullet, official
  changelog.
- **Confidence**: settled (explicit access-tier statement from official
  changelog)
- **Quote**: "The data is available to enterprise owners and billing managers, organization owners, and anyone with a custom organization or enterprise role that grants the View Copilot Metrics permission. The Copilot usage metrics policy must be enabled."
- **Our assessment**: This is broadly consistent with the access tier
  documented across the corpus's other Copilot usage-metrics changelogs
  (enterprise administrator / organization owner), but is more precisely
  worded here: it explicitly includes "billing managers" alongside owners,
  and names the specific custom-role permission ("View Copilot Metrics")
  rather than describing a generic "custom role." It also restates the
  precondition that "the Copilot usage metrics policy must be enabled" —
  an org-level policy gate that is easy to overlook when a team assumes
  role membership alone is sufficient.

### Claim 10: GitHub frames the purpose as letting enterprise leaders see which Copilot features are becoming part of developers' regular workflows and focus training or configuration changes where adoption is lower

- **Evidence**: "Why this matters" section, first sentence, official
  changelog.
- **Confidence**: anecdotal (vendor framing of intended use case; no
  before/after enablement outcome or customer example is cited)
- **Quote**: "Enterprise leaders can see which Copilot features are becoming part of developers' regular workflows and focus training or configuration changes where adoption is lower."
- **Our assessment**: This follows the same rhetorical pattern the corpus
  has already flagged repeatedly for Copilot metrics changelogs (e.g.,
  `docs-github-copilot-usage-metrics-adoption-phase-review-velocity.md`
  Claims 6-7): a new measurement field is announced with an implied
  positive management use baked in, without evidence that organizations
  actually change training or configuration decisions as a result. The
  data-availability half of the claim (the feature-engagement breakdown
  exists and is queryable) is verified by Claims 1-3; the behavioral half
  ("focus training... where adoption is lower") is asserted, not
  demonstrated.

## Concrete Artifacts

### New Fields Added (from changelog, September 17, 2026)

```
# Copilot impact dashboard + usage metrics API — September 17, 2026 additions

Dashboard: Copilot impact dashboard
  New view: per-feature engagement
  Definition: active users who engaged with each included feature on
              at least two days during the 28-day period

copilot_feature_engagement (object)
  Location: enterprise and organization 28-day aggregate reports only
            (NOT user-level reports)
  Contains: dashboard's active-user total + feature engagement counts
  Nullability: object can be absent or null when calculation unavailable

  totals_by_feature (nested array/breakdown within copilot_feature_engagement)
    Features counted (7):
      - code completion
      - agent edit
      - passive Copilot code review   (auto-assigned, user did not engage)
      - active Copilot code review    (user manually requested/applied review)
      - Copilot cloud agent
      - Copilot CLI
      - Copilot app
    Counting rule: a user can be counted under more than one feature
                   (features do not partition users into exclusive buckets)

users_in_phase_28d (field on adoption-phase breakdown)
  Definition: full rolling 28-day population classified into each AI
              adoption phase, as of that report day
  Omission rule: omitted when the phase population was not measured
  Zero rule: 0 means the phase WAS measured and had no users
  Contrast: total_engaged_users (existing field) only reports users in
            the phase who were active on that specific day — does NOT
            capture the full rolling cohort
```

*Source: Copilot impact dashboard now shows feature engagement, GitHub
Changelog, September 17, 2026*

### Access Requirements (verbatim from changelog)

```
"The data is available to enterprise owners and billing managers,
organization owners, and anyone with a custom organization or enterprise
role that grants the View Copilot Metrics permission. The Copilot usage
metrics policy must be enabled."
```

*Source: Copilot impact dashboard now shows feature engagement, GitHub
Changelog, September 17, 2026, "Important notes" section*

## Cross-References

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md`
  Claim 7 (per-phase metrics include "engaged users" as a generic category,
  established May 29, 2026): This September 17 source is the first to name
  the exact field (`total_engaged_users`) behind that generic "engaged
  users" description, and reveals a limitation not previously documented —
  that field only counts users active on the specific report day, not the
  full 28-day phase population. `users_in_phase_28d` is introduced as the
  corrected/complementary field. Any guide text that cited "engaged users"
  per phase from the May 29 source should now distinguish which of the two
  fields (`total_engaged_users` vs. `users_in_phase_28d`) is meant.

- **Extends** `docs-github-copilot-cli-activity-usage-metrics.md` Claim 3
  (CLI appears as `feature=copilot_cli` in the top-level `totals_by_feature`
  breakdown, established April 10, 2026): This source reuses the identifier
  `totals_by_feature` for a structurally different field — a nested array
  inside `copilot_feature_engagement` counting distinct engaged users per
  feature over a 28-day window, rather than the April 10 field's per-day
  activity-event totals tagged by feature. **This is a field-name collision
  the changelog does not flag or disambiguate.** It is not a contradiction
  (the two fields measure genuinely different things and both can be true
  simultaneously), but it is a real pipeline-design hazard: code that
  already parses a `totals_by_feature` key from the top-level report body
  must not assume a `totals_by_feature` key found nested under
  `copilot_feature_engagement` follows the same schema or units.

- **Corroborates** `docs-github-copilot-cli-agentic-customization-metrics.md`
  (September 17, 2026 sibling changelog on Copilot CLI customization
  metrics, issue #3527): Both changelogs, published the same day, document
  new absent/null/omitted-vs-zero semantics for newly added aggregate
  fields (this source's Claims 7-8; that note's discussion of per-category
  null/empty rules). The pattern of "new field can be absent, null, or
  legitimately zero, and these mean different things" is now attested
  across at least two same-day Copilot metrics releases, reinforcing it as
  a general API design convention rather than a one-off caveat.

- **Corroborates** `docs-github-copilot-usage-metrics-adoption-phase-review-velocity.md`
  Claims 6-7 and `docs-github-copilot-usage-metrics-adoption-phase-total-merges.md`
  Claim 3 (GitHub changelogs consistently assert an intended management
  benefit for new metrics fields without supporting adoption or outcome
  data): Claim 10 here follows the identical rhetorical template. This is
  now attested across at least four Copilot usage-metrics changelogs
  (April 8, June 26, July 7, September 17, 2026).

- **Novel**:
  - **First feature-level *engagement* metric (multi-day threshold), as
    opposed to feature-level *activity-count* metrics**: Every prior
    per-feature breakdown in the corpus (`totals_by_feature` with
    `feature=copilot_cli`, `totals_by_ide`, etc.) counts raw activity
    events or simple daily presence. This is the first field that requires
    engagement on at least two of 28 days before a user counts toward a
    feature's total — a materially stricter, "regular use" bar.
  - **Active vs. passive Copilot code review as a documented distinction**:
    No prior source note in the corpus documents this split. It is
    immediately useful for diagnosing whether code-review engagement
    numbers reflect deliberate developer choice or auto-assignment.
  - **`total_engaged_users` named and its limitation documented**: The
    exact field name and its same-day-only counting behavior are new to
    the corpus, as is the corrective `users_in_phase_28d` field.
  - **Field-name collision between two `totals_by_feature` fields**: Not
    previously noted anywhere in the corpus; a genuine schema-design hazard
    worth flagging in the guide's API-integration guidance (see Guide
    Impact, Chapter 02).

## Guide Impact

- **Chapter 05 (Team Adoption — Measuring Impact)**:
  - Add the two-of-28-days feature engagement metric
    (`copilot_feature_engagement.totals_by_feature`) as a new, more
    "regular use" measure of per-feature adoption, distinct from simple
    activity counts. Recommend pairing it with the active/passive code
    review split (Claim 4) when reporting Copilot code-review adoption —
    a high passive share indicates auto-assignment-driven engagement, not
    developer-initiated adoption.
  - Correct any existing guide language that treats `total_engaged_users`
    (per adoption phase) as the full phase population — it is same-day-
    active users only. Recommend `users_in_phase_28d` as the correct
    denominator for phase-size calculations going forward, and flag that
    historical percentages computed against `total_engaged_users` likely
    understated phase populations.
  - Warn against summing the seven `totals_by_feature` engagement counts to
    approximate total active users — the "a user can be counted under more
    than one feature" rule (Claim 5) makes that sum an overcount, though it
    is a legitimate (different) signal of cross-surface breadth.

- **Chapter 02 (Harness Engineering — API integration / schema stability)**:
  - Document the `totals_by_feature` name collision (nested under
    `copilot_feature_engagement` vs. top-level, from the April 10, 2026
    changelog) as a concrete example of why field access in pipelines
    consuming this API should always be scoped by full path
    (`copilot_feature_engagement.totals_by_feature` vs. the report body's
    top-level `totals_by_feature`), never by bare key name.
  - Add the omitted/null/zero handling rule (Claims 7-8) to the guide's
    general defensive-parsing guidance for the Copilot usage metrics API:
    consumers must distinguish "field absent," "field null," and "field
    present with value 0" as three distinct, meaningful states.

## Extraction Notes

1. **Fetched via direct HTTP request, not WebFetch**: The changelog article
   was retrieved with `curl` and its HTML tags stripped and entities
   decoded directly (no AI-model summarization pass), so all quotes above
   are transcribed from the raw article text rather than a WebFetch
   summary. This gives higher confidence in character-exact fidelity than
   several prior notes in the corpus that flagged WebFetch-summarization
   uncertainty.
2. **Linked API docs page not substantively fetchable**: The changelog
   links to "Copilot usage metrics API documentation"
   (`https://docs.github.com/rest/copilot/copilot-usage-metrics`). Both a
   direct `curl` fetch and two WebFetch passes (targeting that page and its
   cross-linked conceptual reference page,
   `docs.github.com/en/copilot/reference/copilot-usage-metrics`) failed to
   surface any of `copilot_feature_engagement`, `totals_by_feature`,
   `users_in_phase_28d`, or `total_engaged_users` in retrievable page
   content — the docs site appears to be a client-rendered SPA whose
   detailed field-level schema (referenced by WebFetch as an "Example
   schema for Copilot usage metrics" sub-page) was not reachable by these
   fetch methods. All claims in this note rely on the changelog's own prose
   definitions, which are detailed enough to support settled confidence for
   the definitional claims (1-9); no JSON schema/type table could be
   cross-checked or added to the Concrete Artifacts section.
3. **Sibling same-day changelog not deeply read**: The "Related Posts"
   list on this changelog page includes "Agentic CLI customizations now in
   the usage metrics API" (September 17, 2026), which is already covered
   by `docs-github-copilot-cli-agentic-customization-metrics.md` (issue
   #3527, mined separately). This note cross-references that note's
   Extraction Notes/Cross-References sections directly rather than
   re-fetching and re-extracting that source.
4. **No contradictions filed**: All claims in this source are additive —
   new fields and a documented (not previously known) limitation of an
   existing field (`total_engaged_users`). No existing source note asserts
   that `total_engaged_users` already reported the full rolling phase
   population, so there is no opposing claim to adjudicate; this is new
   information correcting a documentation gap, not a disagreement between
   two sources. The `totals_by_feature` name collision (Cross-References,
   above) is also not filed as a contradiction — both fields are real,
   coexist, and measure genuinely different things; the risk is a pipeline-
   design hazard, not a factual disagreement between sources.
5. **Source is short (~300 words) and fully extracted**: All "What's new,"
   "Why this matters," and "Important notes" sections are covered by
   Claims 1-10 above; no additional signal would come from re-reading.
