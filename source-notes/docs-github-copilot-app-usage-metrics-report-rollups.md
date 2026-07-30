---
source_url: https://github.blog/changelog/2026-07-28-github-copilot-app-usage-metrics-now-expand-across-report-rollups
source_type: docs
title: "GitHub Copilot app usage metrics now expand across report rollups"
author: GitHub (official changelog)
date_published: 2026-07-28
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: settled
issue: "#2318"
---

# GitHub Copilot App Usage Metrics Expand Across Report Rollups (GitHub Changelog)

> GitHub's July 28, 2026 changelog attributes Copilot app activity to individual
> users for the first time and folds it into the standard feature/model/language
> rollups already used by every other Copilot surface — retiring the app's
> previous status as an enterprise/org-only aggregate total with no per-user or
> per-surface breakdown.

## Source Context

- **Type**: docs (GitHub official product changelog, ~350 words, "2 minute
  read," July 28, 2026)
- **Author credibility**: GitHub engineering team announcing a production API
  change. Authoritative for the fact that these fields exist, their names, their
  report-level availability, and the stated backward-compatibility guarantee.
  Not authoritative for any claim about how much genuine Copilot app adoption
  this newly-attributed data reveals — no adoption numbers are cited, only the
  mechanism for measuring them.
- **Scope**: Five new/changed fields (`used_copilot_app`,
  `totals_by_copilot_app`, the `copilot_app` feature value in existing rollup
  fields, the inclusion of Copilot app activity in code/lines-of-code totals,
  and the expanded `daily_active_users` definition) added to the Copilot usage
  metrics REST API at the enterprise-user, organization-user, and user report
  levels, for both 1-day and 28-day windows. Explicitly states backward
  compatibility for users/entities with no Copilot app activity. Does NOT
  cover: the exact JSON types or nullability of the new fields (contrast with
  the April 10, 2026 CCA aggregate fields, which the changelog explicitly
  documents as nullable — this changelog makes no nullability statement for
  `totals_by_copilot_app`); whether `ai_credits_used` (June 19, 2026) is broken
  out per Copilot app usage; or any interaction with the adoption phase cohort
  model (May 29, 2026). The REST API reference page linked from this
  changelog (`docs.github.com/rest/copilot/copilot-usage-metrics`, fetched
  directly via `curl` on 2026-07-30) does not yet contain any of the five new
  field names — see Extraction Notes item 2.

## Extracted Claims

### Claim 1: Individual Copilot app activity is now attributed to users in the enterprise-user and organization-user reports, whereas it was previously visible only as a standalone enterprise/organization-level total

- **Evidence**: Official GitHub changelog body text and "Why this matters"
  section, confirmed via direct HTML fetch of the changelog page.
- **Confidence**: settled (product fact — explicitly stated as the change)
- **Quote**: "Copilot app usage is now reported across much more of the
  Copilot usage metrics API. Individual Copilot app activity is now
  attributed to users in the enterprise-user and organization-user reports."
- **Our assessment**: This is the central claim of the changelog: a shift
  from an aggregate-only signal to a per-user attributable one. It mirrors
  the exact same aggregate-first, per-user-later expansion pattern already
  documented in the corpus for Copilot cloud agent (user-level flag added
  March 25, 2026 predates the April 10, 2026 aggregate counts in
  `docs-github-copilot-cca-usage-metrics-aggregate.md`) — except here the
  sequence runs in the opposite order: the July 17, 2026 predecessor
  changelog ("GitHub Copilot app now available in the usage metrics API,"
  not yet a source note in this corpus) shipped enterprise-level aggregate
  totals first, and this July 28 release adds the per-user attribution
  eleven days later. Teams that already dashboard the July 17 aggregate
  total should not expect it to change; this release adds a new, separate
  per-user data path alongside it.

### Claim 2: Copilot app coding activity is now broken out in the feature, model, and language rollups alongside every other Copilot surface

- **Evidence**: Official changelog body text, second paragraph of "What's
  new."
- **Confidence**: settled (product fact)
- **Quote**: "In addition, Copilot app coding activity is now broken out in
  the feature, model, and language rollups alongside every other Copilot
  surface."
- **Our assessment**: This closes a dimensional gap the corpus has already
  documented for other surfaces reaching full rollup parity: the May 14,
  2026 team-level source (`docs-github-copilot-team-level-usage-metrics.md`
  Claim 5) states team-level breakdowns already covered "IDE completions,
  chat, Copilot CLI, code review, and Copilot cloud agent activity" — the
  Copilot app was conspicuously absent from that list at team level as of
  May 14. This July 28 release is the first to fold Copilot app activity
  into the `totals_by_feature`/`totals_by_model_feature`/
  `totals_by_language_feature` family of rollups at the enterprise/org/user
  level (team-level parity is not addressed by this changelog and remains
  unconfirmed).

### Claim 3: `used_copilot_app` is a per-user boolean-style field indicating whether a user was active in the Copilot app on a given day

- **Evidence**: Field definition under the "What's new" section's bulleted
  list.
- **Confidence**: settled (definitional)
- **Quote**: "`used_copilot_app`: Whether a user was active in the Copilot
  app on a given day."
- **Our assessment**: This is structurally identical to the
  `used_copilot_coding_agent` per-user flag documented in
  `docs-github-copilot-cca-usage-metrics-aggregate.md` (Concrete Artifacts,
  "Surface 2 — CCA, user level") — a boolean-per-user-per-day activity flag.
  GitHub is applying the same per-surface user-flag pattern to the Copilot
  app that it previously applied to Copilot cloud agent, six weeks earlier
  in the corpus's timeline (March 25, 2026 predecessor cited there vs. this
  July 28, 2026 release) — though for the Copilot app the aggregate-level
  total (July 17) came before the per-user flag (July 28), the reverse
  ordering from CCA's rollout.

### Claim 4: `totals_by_copilot_app` is a per-user section reporting `session_count`, `request_count`, `prompt_count`, and a `token_usage` breakdown of `output_tokens_sum`, `prompt_tokens_sum`, and `avg_tokens_per_request`

- **Evidence**: Field definition under the "What's new" section's bulleted
  list, giving the full nested field structure.
- **Confidence**: settled (definitional — full field list stated explicitly)
- **Quote**: "`totals_by_copilot_app`: A per-user section reporting
  `session_count`, `request_count`, `prompt_count`, and a `token_usage`
  breakdown of `output_tokens_sum`, `prompt_tokens_sum`, and
  `avg_tokens_per_request`."
- **Our assessment**: This is the richest per-user field set the corpus has
  seen for any single Copilot surface — session, request, and prompt counts
  plus a three-way token accounting breakdown. It is more granular than the
  per-user `ai_credits_used` field documented in
  `docs-github-copilot-usage-metrics-ai-credits-per-user.md`, which is a
  single scalar cost figure with no token- or request-level detail. Neither
  field references the other in this changelog, so it is unclear whether
  `ai_credits_used` for a Copilot-app-only user is derived in any way from
  `totals_by_copilot_app`'s token counts, or computed independently from
  billing data as that note's Claim 2 states for the metric generally.

### Claim 5: The `copilot_app` feature value now appears in `totals_by_feature`, `totals_by_model_feature`, `totals_by_language_feature`, and `totals_by_language_model` — letting consumers see which models and languages Copilot app work happens in

- **Evidence**: Field definition under the "What's new" section's bulleted
  list, naming all four rollup fields affected.
- **Confidence**: settled (definitional — explicit list of affected rollup
  fields)
- **Quote**: "`copilot_app` feature value: Copilot app activity now appears
  in `totals_by_feature`, `totals_by_model_feature`,
  `totals_by_language_feature`, and `totals_by_language_model`, so you can
  see which models and languages Copilot app work happens in."
- **Our assessment**: This is the specific mechanism behind Claim 2's
  "broken out in the feature, model, and language rollups" statement — four
  named rollup fields, not a vague "more visibility" claim. Any team already
  consuming `totals_by_feature` for surface-mix analysis (IDE completions vs.
  chat vs. code review, etc.) will see a new `copilot_app` key appear in
  that structure after this release, without any schema change to the
  rollup fields themselves — only a new enum-style value within them.

### Claim 6: Top-level code generation, code acceptance, lines-added, and lines-deleted totals now include Copilot app activity

- **Evidence**: Field definition under the "What's new" section's bulleted
  list.
- **Confidence**: settled (definitional — explicit statement of which
  top-level totals are affected)
- **Quote**: "Code activity and lines-of-code metrics: Top-level code
  generation, code acceptance, lines added, and lines deleted totals now
  include Copilot app activity."
- **Our assessment**: This is an important arithmetic caveat for any pipeline
  already consuming these top-level code metrics: post-July 28, 2026, the
  same field names will silently include a new activity source. A team
  trend-charting "lines of code generated by Copilot" month-over-month will
  see a step change coincident with this release for any organization with
  active Copilot app users — not because generation activity increased, but
  because a previously-uncounted surface is now folded into the same
  top-level total. This is the same kind of methodological-inflection-point
  concern the June 15, 2026 server-side telemetry source
  (`docs-github-copilot-usage-metrics-server-side-telemetry.md` Claim 3 and
  Guide Impact) already flags for DAU counts — here it applies to
  code-volume totals instead of active-user counts.

### Claim 7: `daily_active_users` now counts users who were only active in the Copilot app

- **Evidence**: Field definition under the "What's new" section's bulleted
  list.
- **Confidence**: settled (definitional — explicit statement of the changed
  counting rule)
- **Quote**: "`daily_active_users`: Now counts users who were only active in
  the Copilot app."
- **Our assessment**: This is the second documented instance in the corpus
  of a `daily_active_users`-style field's population changing due to a
  methodology or coverage update rather than a genuine adoption shift — the
  first being the June 15, 2026 server-side telemetry expansion. Both cases
  produce the identical downstream risk: an organization's top-line DAU
  count rises after the change takes effect, for reasons unrelated to actual
  usage growth. A team doing month-over-month DAU trend analysis must now
  track two known step-change dates (June 15 for server-side telemetry
  coverage, July 28 for Copilot-app-only users) rather than one, when
  explaining any DAU count discontinuity.

### Claim 8: Copilot app usage was previously visible only as a standalone enterprise/organization-level total, with no way to identify which users were driving it or what code it produced

- **Evidence**: "Why this matters" section, describing the prior state this
  release replaces.
- **Confidence**: settled (stated prior-state description from the vendor
  announcing its own product's history — GitHub is describing its own
  July 17, 2026 release, made 11 days earlier)
- **Quote**: "Copilot app usage was previously only visible as a standalone
  enterprise and organization-level total, so you could see that the
  Copilot app was being used but not who was using it or what it produced."
- **Our assessment**: This confirms the July 17, 2026 predecessor changelog
  ("GitHub Copilot app now available in the usage metrics API") shipped only
  an aggregate total with no user attribution and no code-output
  attribution — consistent with this note's Claim 1 characterization of that
  predecessor. That July 17 changelog is not yet a source note in this
  corpus (see Extraction Notes item 3); this July 28 changelog is the first
  point at which the corpus documents the Copilot app's usage-metrics
  history in any depth.

### Claim 9: With Copilot app activity attributed to individual users and folded into standard breakdowns, organizations can identify Copilot app adopters, measure the code the Copilot app generates, and compare the Copilot app against IDE, chat, code review, and coding agent surfaces using the same fields they already consume

- **Evidence**: "Why this matters" section, second half.
- **Confidence**: anecdotal (vendor framing of intended use case; no
  adoption or comparison data is cited to demonstrate this actually happens
  in practice)
- **Quote**: "With Copilot app activity attributed to individual users and
  folded into the standard breakdowns, you can identify your Copilot app
  adopters, and measure the code the Copilot app generates. You can also
  compare the Copilot app against the IDE, chat, code review, and coding
  agent surfaces using the same fields you already consume."
- **Our assessment**: The "same fields you already consume" claim is the
  most concretely verifiable part of this framing — Claims 2 and 5
  establish that `totals_by_feature` and related rollups now carry a
  `copilot_app` value alongside existing surface values, which does support
  an apples-to-apples comparison query without new field-specific logic.
  The "identify your Copilot app adopters" framing is plausible given Claim
  3's per-user flag, but as with the April 10, 2026 CCA aggregate source's
  Claim 9 (`docs-github-copilot-cca-usage-metrics-aggregate.md`), no
  evidence is given that this identification capability is actually used
  for targeted enablement — it is a data-availability claim, not an
  outcomes claim.

### Claim 10: The `used_copilot_app` field and the user-level `totals_by_copilot_app` section are available in the enterprise-user and organization-user reports for both 1-day and 28-day windows; the `copilot_app` feature value and the code-activity/lines-of-code/`daily_active_users` changes apply to the enterprise, organization, and user reports for both windows

- **Evidence**: "Important notes" section, first paragraph, stating scope
  precisely per field group.
- **Confidence**: settled (explicit scope statement, differentiated by field
  group — not a single blanket scope claim)
- **Quote**: "`used_copilot_app` and the user-level `totals_by_copilot_app`
  section are available in the enterprise-user and organization-user 1-day
  and 28-day reports. The `copilot_app` feature value and the code activity,
  lines-of-code, and `daily_active_users` changes apply to the enterprise,
  organization, and user reports for both the 1-day and 28-day windows."
- **Our assessment**: This is a report-scope asymmetry worth flagging
  precisely: the two brand-new per-user fields (`used_copilot_app`,
  `totals_by_copilot_app`) are scoped to enterprise-user/organization-user
  reports specifically, while the rollup and top-level-total changes (which
  extend existing fields rather than introduce new ones) apply more broadly
  across enterprise, organization, and user report types. A team building a
  pipeline against the plain "user" report type (as opposed to
  "enterprise-user"/"organization-user") should not expect
  `totals_by_copilot_app` to appear there, even though `copilot_app`-tagged
  rollup entries will.

### Claim 11: Access requires enterprise owner or billing manager status, organization owner status, or a custom organization/enterprise role granting the View Copilot Metrics permission, with the Copilot usage metrics policy enabled

- **Evidence**: "Important notes" section, second paragraph.
- **Confidence**: settled (stated access tier from official changelog)
- **Quote**: "These metrics are available to enterprise owners and billing
  managers, organization owners, and anyone with a custom organization or
  enterprise role that grants the View Copilot Metrics permission. The
  Copilot usage metrics policy must be enabled."
- **Our assessment**: This matches the access tier already documented
  across the corpus's Copilot metrics series (e.g.
  `docs-github-copilot-team-level-usage-metrics.md` Claim 7 and
  `docs-github-copilot-repository-level-usage-metrics.md` Claim 7), though
  it uses the generic "View Copilot Metrics" phrasing rather than the
  level-specific "View Enterprise Copilot Metrics" / "View Organization
  Copilot Metrics" permission names the July 17, 2026 repository-level
  source found were the actual distinct fine-grained permission names on
  the REST API reference page. This changelog does not clarify whether one
  or both level-specific permissions are required for the new Copilot app
  fields specifically.

### Claim 12: The changes are backward compatible — users and entities with no Copilot app activity omit `totals_by_copilot_app` and produce no `copilot_app` breakdown entries, and existing fields keep their current shape

- **Evidence**: "Important notes" section, third paragraph.
- **Confidence**: settled (explicit backward-compatibility guarantee stated
  in the official changelog)
- **Quote**: "The changes are backward compatible. Users and entities with
  no Copilot app activity omit `totals_by_copilot_app` and produce no
  `copilot_app` breakdown entries, and existing fields keep their current
  shape."
- **Our assessment**: This is a sparse-inclusion behavior structurally
  similar to the July 17, 2026 repository-level report's "only repositories
  that had activity ... are included" rule
  (`docs-github-copilot-repository-level-usage-metrics.md` Claim 4) — an
  absent field/entry means "no activity," not "error" or "not yet
  supported." Unlike that repository-level case, this changelog is explicit
  that omission is intentional backward-compatibility design (existing
  consumers parsing the response schema will not encounter unexpected
  fields for entities that never used the Copilot app), whereas the
  repository report's sparse-inclusion rule was framed as a reporting
  characteristic rather than a compatibility guarantee.

## Concrete Artifacts

### Verbatim Changelog Body Text (July 28, 2026, confirmed via raw HTML fetch)

```
GitHub Copilot app usage metrics now expand across report rollups
Improvement | July 28, 2026 • 2 minute read

Copilot app usage is now reported across much more of the Copilot usage
metrics API.

Individual Copilot app activity is now attributed to users in the
enterprise-user and organization-user reports. In addition, Copilot app
coding activity is now broken out in the feature, model, and language
rollups alongside every other Copilot surface.

This builds on the earlier release that brought the Copilot app into the
usage metrics API with enterprise-level Copilot app totals.

What's new
used_copilot_app: Whether a user was active in the Copilot app on a given
day.
totals_by_copilot_app: A per-user section reporting session_count,
request_count, prompt_count, and a token_usage breakdown of
output_tokens_sum, prompt_tokens_sum, and avg_tokens_per_request.
copilot_app feature value: Copilot app activity now appears in
totals_by_feature, totals_by_model_feature, totals_by_language_feature, and
totals_by_language_model, so you can see which models and languages Copilot
app work happens in.
Code activity and lines-of-code metrics: Top-level code generation, code
acceptance, lines added, and lines deleted totals now include Copilot app
activity.
daily_active_users: Now counts users who were only active in the Copilot
app.

Why this matters
Copilot app usage was previously only visible as a standalone enterprise
and organization-level total, so you could see that the Copilot app was
being used but not who was using it or what it produced. With Copilot app
activity attributed to individual users and folded into the standard
breakdowns, you can identify your Copilot app adopters, and measure the
code the Copilot app generates.

You can also compare the Copilot app against the IDE, chat, code review,
and coding agent surfaces using the same fields you already consume.

Important notes
used_copilot_app and the user-level totals_by_copilot_app section are
available in the enterprise-user and organization-user 1-day and 28-day
reports. The copilot_app feature value and the code activity,
lines-of-code, and daily_active_users changes apply to the enterprise,
organization, and user reports for both the 1-day and 28-day windows.

These metrics are available to enterprise owners and billing managers,
organization owners, and anyone with a custom organization or enterprise
role that grants the View Copilot Metrics permission. The Copilot usage
metrics policy must be enabled.

The changes are backward compatible. Users and entities with no Copilot
app activity omit totals_by_copilot_app and produce no copilot_app
breakdown entries, and existing fields keep their current shape.

Visit the Copilot usage metrics API documentation to get started.
```

*Source: https://github.blog/changelog/2026-07-28-github-copilot-app-usage-metrics-now-expand-across-report-rollups,
retrieved via direct `curl` fetch of the raw HTML `<article>` element on
2026-07-30 (WebFetch's model-processed summary omitted the "This builds on
the earlier release ..." sentence and its embedded link on an initial pass
— see Extraction Notes item 1).*

### New/Changed Field Reference (compiled from the changelog, July 28, 2026)

```
# Copilot usage metrics API — Copilot app attribution fields (added/changed
# July 28, 2026)

used_copilot_app
  Scope: enterprise-user, organization-user reports (1-day and 28-day)
  Description: whether a user was active in the Copilot app on a given day

totals_by_copilot_app
  Scope: enterprise-user, organization-user reports (1-day and 28-day)
  Description: per-user section:
    session_count
    request_count
    prompt_count
    token_usage:
      output_tokens_sum
      prompt_tokens_sum
      avg_tokens_per_request

copilot_app (feature value, not a new field name)
  Scope: enterprise, organization, user reports (1-day and 28-day)
  Appears in:
    totals_by_feature
    totals_by_model_feature
    totals_by_language_feature
    totals_by_language_model

Top-level code metrics (existing fields, now inclusive of Copilot app):
  Scope: enterprise, organization, user reports (1-day and 28-day)
  code generation total, code acceptance total, lines added total,
  lines deleted total

daily_active_users (existing field, redefined)
  Scope: enterprise, organization, user reports (1-day and 28-day)
  Change: now counts users active only in the Copilot app (previously would
  not have counted a Copilot-app-only user as active, per this changelog's
  framing of the prior state)

Backward compatibility: entities/users with no Copilot app activity omit
totals_by_copilot_app and produce no copilot_app breakdown entries;
existing field shapes are unchanged.
```

*Compiled from the July 28, 2026 GitHub changelog body text above.*

## Cross-References

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md`:
  - Claim 6 (aggregate CCA counts complement the user-level flag and IDE
    field, giving "a full view of Copilot adoption across surfaces"): This
    source's Claim 9 makes the same multi-surface-comparison claim for the
    Copilot app specifically, now naming "IDE, chat, code review, and
    coding agent surfaces" as the comparison set the Copilot app can be
    measured against using shared fields.
  - Concrete Artifacts "Multi-Surface Copilot Adoption Metrics Landscape":
    this source adds a further surface (Copilot app) to that landscape,
    with its own aggregate-then-per-user rollout sequence (aggregate July
    17, 2026; per-user July 28, 2026) — the same two-stage pattern
    documented there for CCA (user-level March 25, 2026; aggregate April
    10, 2026), but in reverse order.

- **Extends** `docs-github-copilot-team-level-usage-metrics.md` Claim 5
  (team-level breakdowns cover "IDE completions, chat, Copilot CLI, code
  review, and Copilot cloud agent activity" as of May 14, 2026, with no
  mention of the Copilot app): This source's Claim 2 brings Copilot app
  activity into feature/model/language rollups at the
  enterprise/organization/user level, closing part of that gap — but this
  changelog does not state whether team-level (`user-teams-1-day`) rollups
  also now include `copilot_app`, so team-level parity with this source's
  new fields remains unconfirmed.

- **Extends** `docs-github-copilot-usage-metrics-server-side-telemetry.md`
  Claim 3 and its "Historical trend analysis and time-series
  comparability" Guide Impact section (June 15, 2026 methodological
  inflection point for `daily_active_users`/DAU counts): This source's
  Claim 7 is a second, independent cause of a `daily_active_users`-style
  count changing for coverage/definitional reasons rather than genuine
  adoption growth. Any Ch05 guidance on DAU time-series comparability
  should now track two known step-change dates: June 15, 2026
  (server-side telemetry) and July 28, 2026 (Copilot-app-only users now
  counted).

- **Extends** `docs-github-copilot-usage-metrics-ai-credits-per-user.md`
  Claim 1 (`ai_credits_used` is the first per-user cost metric in the API):
  This source's Claim 4 adds a much richer per-user activity/token
  breakdown (`totals_by_copilot_app`) for one specific surface, but does
  not state whether or how it relates to the cross-surface
  `ai_credits_used` scalar. A team wanting to explain a user's total AI
  credit consumption in terms of per-surface token usage cannot yet do so
  purely from these two sources — the linkage between `token_usage` fields
  and billing-derived `ai_credits_used` is not documented by either
  changelog.

- **Corroborates** `docs-github-copilot-repository-level-usage-metrics.md`
  Claim 4 (sparse-inclusion rule: repository rows are omitted, not
  zero-filled, for repositories with no activity): This source's Claim 12
  documents the same "omit rather than zero-fill" design pattern for
  `totals_by_copilot_app` and `copilot_app` breakdown entries, applied to
  per-user/per-rollup data instead of per-repository data. Both changelogs
  independently confirm GitHub's default convention for the Copilot usage
  metrics API is sparse inclusion for zero-activity subjects, not explicit
  zero values.

- **Corroborates** the general per-surface, incremental expansion pattern
  already noted across `docs-github-copilot-cca-usage-metrics-aggregate.md`,
  `docs-github-copilot-code-review-usage-metrics-aggregate.md`, and
  `docs-github-copilot-repository-level-usage-metrics.md`: this is another
  instance of GitHub adding one new dimension (per-user Copilot app
  attribution) to an already-established rollup structure rather than
  introducing a new report type or endpoint.

- **Novel**:
  - **A surface whose aggregate total shipped before its per-user
    attribution**: Every other surface expansion in the corpus (CCA, code
    review, repository-level) either launched with per-user granularity
    from the start or added aggregate counts after user-level data already
    existed. The Copilot app is the first documented case in the corpus
    where GitHub shipped an aggregate-only total (July 17, 2026) and only
    later back-filled per-user attribution (July 28, 2026) — a sequencing
    novel to this corpus.
  - **Explicit backward-compatibility guarantee tied to sparse inclusion**:
    While sparse inclusion itself is corroborated (see above), this is the
    first source to explicitly frame the omit-rather-than-zero-fill
    behavior as a stated backward-compatibility design goal for existing
    API consumers, rather than simply a reporting characteristic.
  - **A second documented DAU-methodology step-change date**: The corpus
    now has two distinct, dated causes of `daily_active_users` counts
    shifting independent of genuine adoption change (June 15 server-side
    telemetry; July 28 Copilot-app-only users) — the first time the corpus
    documents more than one such inflection point for the same field.
  - **Token-level per-surface accounting (`token_usage` with
    `output_tokens_sum`/`prompt_tokens_sum`/`avg_tokens_per_request`)**: No
    prior source in the corpus documents token-level accounting broken out
    for a specific Copilot surface at the per-user level; the closest
    prior field, `ai_credits_used`, is a single billing-derived scalar with
    no token-level detail.

## Guide Impact

- **Chapter 05 (Measurement) — "Metrics granularity hierarchy" / multi-surface
  adoption section**: Add the Copilot app as a sixth tracked surface
  alongside IDE completions, chat, Copilot CLI, code review, and Copilot
  cloud agent, noting its two-stage rollout (aggregate-only July 17, 2026;
  per-user attribution July 28, 2026) as a caveat for anyone querying
  historical data — per-user Copilot app breakdowns simply do not exist for
  dates before July 28, 2026, even though the enterprise-level aggregate
  total does, back to July 17, 2026.
- **Chapter 05 — "Historical trend analysis and time-series comparability"**
  (extending the section already recommended in
  `docs-github-copilot-usage-metrics-server-side-telemetry.md`): Add July
  28, 2026 as a second dated inflection point for `daily_active_users`,
  alongside June 15, 2026. Any DAU trend chart spanning both dates should
  annotate both step-changes rather than attributing either to adoption
  growth.
- **Chapter 05 — new subsection "Per-surface token accounting"**: Document
  `totals_by_copilot_app`'s `token_usage` breakdown as the first
  per-surface, per-user token-level metric in the corpus, and flag the open
  question (not answered by any source yet) of how per-surface token counts
  reconcile with the cross-surface `ai_credits_used` billing metric.
- **Chapter 02 (Harness Engineering) — "Enterprise Copilot observability
  pipeline"**: Note that pipelines already parsing `totals_by_feature` (or
  the model/language variants) will begin seeing a new `copilot_app` key
  without any schema change — defensive code that enumerates expected
  feature values (rather than iterating whatever keys are present) will
  silently miss Copilot app data after July 28, 2026 unless updated.

## Extraction Notes

1. **WebFetch initial pass omitted content; raw HTML fetch used instead**:
   Two WebFetch calls against the changelog URL, prompted differently,
   produced two internally-consistent but non-identical summaries — neither
   included the "This builds on the earlier release ..." sentence or its
   embedded link, and both slightly reworded quoted phrases (e.g. rendering
   "much more of the Copilot usage metrics API" and "session count, request
   count, prompt count" without the underscored field-name formatting).
   Per MINER.md §2a, the page was re-fetched via direct `curl` and the raw
   `<article>` text extracted with a Python HTML-stripping pass; every
   quote in this note is taken from that raw fetch, not from either
   WebFetch summary.
2. **Linked REST API reference page does not yet document the new fields**:
   `docs.github.com/rest/copilot/copilot-usage-metrics` was fetched
   directly via `curl` on 2026-07-30 (463KB of HTML). A full-text search for
   `copilot_app`, `used_copilot_app`, and `totals_by_copilot_app` returned
   zero matches, while `download_links`, `report_day`, and `repos-1-day`
   (fields documented by the July 17, 2026 repository-level source) were
   each found multiple times. This indicates the reference page has not
   yet been updated to reflect this changelog's field additions as of the
   extraction date — a documentation lag, not evidence that the fields
   don't exist (the changelog itself is the authoritative announcement).
   No claim in this note depends on the reference page; all twelve claims
   are sourced from the changelog body itself.
3. **Predecessor changelog identified but not mined**: The changelog links
   to "the earlier release that brought the Copilot app into the usage
   metrics API with enterprise-level Copilot app totals" at
   `https://github.blog/changelog/2026-07-17-github-copilot-app-now-available-in-the-usage-metrics-api/`.
   A search of this corpus's `source-notes/` directory found no existing
   note for that URL or title. It is referenced here (Claim 1, Claim 8) only
   insofar as this changelog's own text describes it; its full content was
   not independently fetched or extracted, since doing so is out of scope
   for this issue and would duplicate the Miner/Prospector triage pipeline
   for a distinct source. A future source-note PR for that predecessor
   would let this note's Claim 1 and Claim 8 be cross-checked directly
   against the July 17 changelog's own text rather than through this
   changelog's secondhand characterization of it.
4. **No contradictions to file**: No existing source note claims that
   Copilot app usage cannot or should not be attributed per-user, or that
   `daily_active_users` should exclude Copilot-app-only users. The two-stage
   rollout sequencing (aggregate before per-user) is a novel pattern, not a
   contradiction of anything already in the corpus — see Cross-References →
   Novel.
5. **Source is a short product changelog (~350 words)**: All substantive
   claims are extracted in the twelve claims above, drawn from all four
   named sections of the changelog ("What's new," "Why this matters,"
   "Important notes," plus the introductory two paragraphs). No additional
   signal would come from re-reading the changelog itself; the only
   unexplored thread is the unmined July 17, 2026 predecessor (Extraction
   Notes item 3).
