---
source_url: https://github.blog/changelog/2026-07-17-github-copilot-app-now-available-in-the-usage-metrics-api
source_type: docs
title: "GitHub Copilot app now available in the usage metrics API"
author: Allison (GitHub official changelog)
date_published: 2026-07-17
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: settled
issue: "#1989"
---

# GitHub Copilot App Now Available in the Usage Metrics API (GitHub Changelog, July 17, 2026)

> GitHub's July 17, 2026 changelog adds two new fields — `daily_active_copilot_app_users`
> and `totals_by_copilot_app` — to the enterprise and organization Copilot usage metrics
> API, giving the GitHub Copilot app its own isolated observability section (session,
> request, prompt, and token-usage counts) rather than folding it into the existing
> `totals_by_feature` breakdown the way Copilot CLI activity was integrated on April 10, 2026.

## Source Context

- **Type**: docs (GitHub official product changelog, ~150 words, "1 minute read",
  July 17, 2026). Fetched directly from `github.blog` HTML source (not the summarizing
  WebFetch tool) to guarantee verbatim quotes — see Extraction Notes.
- **Author credibility**: GitHub's own changelog, byline "Allison" (`author.name` in the
  page's JSON-LD metadata) — the same byline as the July 14, 2026 Copilot app
  `/security-review` announcement (`docs-github-copilot-app-security-review.md`).
  Authoritative for: the existence of the two new fields, their placement in the report
  hierarchy, their sub-field composition, and the null-value behavior for inactive
  orgs/enterprises. Not a credible source for: the exact JSON data types of the new
  fields, whether `totals_by_copilot_app` is filterable by the May 14, 2026 team-level
  JOIN pattern or the May 29, 2026 adoption-phase `teams filter`, or any access-tier
  restriction (this changelog does not restate the access tier stated in prior Copilot
  metrics changelogs).
- **Scope**: Two new fields added to enterprise and organization 1-day and 28-day Copilot
  usage metrics reports: a daily active-user count for the Copilot app, and a dedicated
  `totals_by_copilot_app` breakdown section. Covers: field names, field definitions,
  sub-metrics inside `totals_by_copilot_app`, isolation from other breakdown totals, and
  null-value behavior. Does NOT cover: the access tier required to read these fields (no
  "Important notes" access-tier line, unlike the May 14 and May 29 changelogs); whether
  Copilot app activity now counts toward the `ai_adoption_phase` Phase 3 "engaged with
  ... the new GitHub Copilot app" qualifier documented May 29, 2026 (`docs-github-copilot-usage-metrics-adoption-cohorts.md`
  Claim 5); whether `totals_by_copilot_app` participates in the May 14 team-level
  user-teams JOIN; or the underlying definition of a Copilot "app" session/request/prompt
  (i.e., whether one chat turn = one request = one prompt).

## Extracted Claims

### Claim 1: The Copilot usage metrics API now reports GitHub Copilot app usage in enterprise and organization 1-day and 28-day reports, alongside the IDE, chat, code review, and coding agent metrics already available

- **Evidence**: Opening paragraph of the changelog, stated as the lead fact.
- **Confidence**: settled (direct product statement from GitHub's own changelog)
- **Quote**: "The Copilot usage metrics API now reports the GitHub Copilot app usage in the enterprise and organization 1-day and 28-day reports. This gives enterprise and organization admins visibility into the app's activity alongside the IDE, chat, code review, and coding agent metrics they already retrieve."
- **Our assessment**: This is the eighth documented expansion of the Copilot usage
  metrics API in the corpus's time series (April 8 PR review, April 10 CCA aggregates,
  April 10 CLI integration, May 14 team-level, May 29 adoption phases, June 15
  server-side telemetry, June 19 AI credits, June 26 total merges, July 7 review cycles,
  now July 17 Copilot app) — GitHub is shipping this API in a steady monthly-or-faster
  cadence of additive fields rather than a single comprehensive release. The explicit
  list of sibling surfaces ("IDE, chat, code review, and coding agent") frames the
  Copilot app as a peer surface to those four, not a subset of any of them.

### Claim 2: A new `daily_active_copilot_app_users` field reports the count of distinct users active in the Copilot app on a given day

- **Evidence**: Explicit field definition under the "What's new" heading.
- **Confidence**: settled (definitional product fact)
- **Quote**: "daily_active_copilot_app_users: The number of distinct users active in the Copilot app on a given day."
- **Our assessment**: This follows the same naming and definitional pattern as
  `daily_active_copilot_cloud_agent_users` (added April 10, 2026, per
  `docs-github-copilot-usage-metrics-ai-credits-per-user.md` Concrete Artifacts) and
  `daily_active_cli_users` (implied by the CLI integration pattern) — a per-surface DAU
  counter following an established `daily_active_copilot_<surface>_users` naming
  convention. Unlike the April 10 CLI change, which folded CLI activity into *existing*
  aggregate fields (`code_generation_activity_count` etc.), the Copilot app gets a
  dedicated counter rather than being merged into the generic active-user totals.

### Claim 3: A new `totals_by_copilot_app` field is a dedicated section reporting session count, request count, prompt count, and a token-usage breakdown (output tokens, prompt tokens, and average tokens per request)

- **Evidence**: Explicit field definition under the "What's new" heading, enumerating four
  sub-metrics plus a three-part token breakdown.
- **Confidence**: settled (definitional product fact)
- **Quote**: "totals_by_copilot_app: A dedicated GitHub Copilot app section reporting session_count, request_count, prompt_count, and a token_usage breakdown (i.e., output_tokens_sum, prompt_tokens_sum, and avg_tokens_per_request)."
- **Our assessment**: This is the first Copilot metrics API field in the corpus to expose
  token-level consumption data (`output_tokens_sum`, `prompt_tokens_sum`,
  `avg_tokens_per_request`) directly in the usage metrics API rather than via the
  billing-derived `ai_credits_used` field (June 19, 2026,
  `docs-github-copilot-usage-metrics-ai-credits-per-user.md` Claim 1). `ai_credits_used`
  is an opaque per-user cost total with no feature/model/surface breakdown (per that
  note's Claim 3); `totals_by_copilot_app.token_usage` is the inverse — a token-level
  breakdown scoped to one surface (the app) but not expressed as a cost or credit figure.
  Neither field alone answers "how many AI credits did Copilot app usage cost this org,"
  but together they provide the two halves (token volume for the app surface; overall
  per-user cost) needed to approximate it.

### Claim 4: Copilot app activity was not previously represented in usage reporting; the new fields let admins see how broadly the app is being adopted via active users, session/request volume, and token consumption

- **Evidence**: "Why this matters" section, framing the business rationale.
- **Confidence**: anecdotal (vendor framing of intended use; no evidence cited that any
  organization has used these fields to drive an adoption decision)
- **Quote**: "The GitHub Copilot app activity was not previously represented in usage reporting. With these fields, enterprise and organization admins can see how broadly the app is being adopted (e.g., distinct active users, session and request volume, and token consumption) in the same API they already use for the rest of their Copilot usage metrics."
- **Our assessment**: This confirms a genuine prior observability gap — the Copilot app
  had zero footprint in the metrics API before this change, consistent with the app
  itself being a comparatively new product surface in the corpus (first appearing as a
  Phase 3 adoption qualifier on May 29, 2026, and as a `/security-review` host surface
  on July 14, 2026). "In the same API they already use" is the operationally important
  half of this claim: no separate endpoint or dashboard is required — this is additive
  to the existing `GET /enterprises/{enterprise}/copilot/metrics` and
  `GET /orgs/{org}/copilot/metrics` surface used by every other note in this corpus's
  metrics-API series.

### Claim 5: The Copilot app usage is reported in its own `totals_by_copilot_app` section and is kept separate from the generic feature, model, and language totals, as well as from lines-of-code metrics

- **Evidence**: Explicit isolation statement in the "Important notes" section.
- **Confidence**: settled (explicitly documented architectural constraint)
- **Quote**: "The GitHub Copilot app usage is reported in its own totals_by_copilot_app section and is kept separate from the generic feature, model, and language totals, as well as from lines-of-code metrics."
- **Our assessment**: This is an explicit architectural departure from the pattern set by
  the April 10, 2026 CLI integration. That change added `feature=copilot_cli` as a named
  value *inside* `totals_by_feature`, `totals_by_model_feature`, and
  `totals_by_language_feature` (`docs-github-copilot-cli-activity-usage-metrics.md`
  Claim 3), and also folded CLI activity into the top-level aggregate fields
  (`code_generation_activity_count`, `loc_added_sum`, etc. — that note's Claim 2). The
  Copilot app does neither: it is not a `totals_by_feature` value, and it does not
  contribute to `loc_added_sum`/`loc_deleted_sum` or the other shared aggregates. A team
  querying `totals_by_feature` for "what fraction of Copilot activity is app vs. IDE vs.
  CLI" will not find the app represented there at all — they must separately query
  `totals_by_copilot_app`. This is a conditioning variable (two different Copilot
  surfaces integrated via two different architectural patterns), not a factual
  contradiction between sources, so no contradiction issue is filed per MINER.md §4a —
  but it is a real inconsistency in how "surface" is modeled across the API that the
  guide should document explicitly to prevent an incomplete `totals_by_feature`-only
  adoption query.

### Claim 6: Enterprises or organizations with no Copilot app activity report `null` for both `daily_active_copilot_app_users` and `totals_by_copilot_app`, so existing API integrations are unaffected

- **Evidence**: Explicit backward-compatibility statement in the "Important notes" section.
- **Confidence**: settled (explicitly documented behavior)
- **Quote**: "Enterprises or organizations with no GitHub Copilot app activity report null for both daily_active_copilot_app_users and totals_by_copilot_app, so existing integrations are unaffected."
- **Our assessment**: `null` (not zero, not an omitted key, not an empty object) is the
  specific documented value for the no-activity case. This matters for pipeline
  correctness: a consumer that treats a missing field as an error, or that assumes
  `totals_by_copilot_app.session_count` is always present and numeric, will break on
  organizations with zero app adoption. This is a different completeness pattern than
  the June 15, 2026 server-side telemetry change, where newly surfaced users get
  `included` DAU counts but `empty` (not null) `totals_by_ide`/`totals_by_feature`
  breakdowns (`docs-github-copilot-usage-metrics-server-side-telemetry.md` Claim 4) — one
  case uses `null` to signal "no activity at the org level," the other uses empty
  breakdowns to signal "activity exists but couldn't be attributed at the per-user
  level." Pipelines need to handle both null-checking and empty-breakdown-checking as
  distinct defensive patterns.

### Claim 7: The changelog directs readers to the Copilot usage metrics API documentation "to get started," but as of one day after publication that linked documentation does not yet describe the new fields

- **Evidence**: The changelog's closing line links to `https://docs.github.com/rest/copilot/copilot-usage-metrics`.
  We followed that link, and the linked page in turn points to
  `https://docs.github.com/en/copilot/reference/copilot-usage-metrics` and its
  `example-schema` sub-page. None of the three pages fetched on July 18, 2026 (one day
  after the changelog's July 17 publication) mention `copilot_app`,
  `daily_active_copilot_app_users`, or `totals_by_copilot_app` in any field list or
  example JSON schema.
- **Confidence**: emerging (our own observation from following the changelog's outbound
  link, not a claim made by the source itself — see MINER.md §2a: this is not a source
  quote, it is our finding)
- **Quote**: (no direct quote; this is our own cross-check of the linked documentation,
  not a passage from the changelog itself — see paraphrase above)
- **Our assessment**: This is a real but likely transient documentation lag, not a
  product defect — GitHub Copilot changelog entries have historically preceded the
  corresponding reference-docs update by some period in prior corpus sources (e.g., the
  May 14, 2026 team-level metrics note recorded a similar "docs page not accessible at
  extraction time" gap, per that note's Extraction Notes item 3). Teams building
  pipelines against `daily_active_copilot_app_users` or `totals_by_copilot_app`
  immediately after this changelog should expect the authoritative field-level schema
  (data types, whether `totals_by_copilot_app` is an object or array, exact null vs.
  omitted-key behavior) to lag the changelog announcement and should verify against a
  live API response rather than the reference docs at launch.

## Concrete Artifacts

### New API Fields (from changelog, July 17, 2026)

```
# Copilot usage metrics API — GitHub Copilot app fields (added July 17, 2026)
# Location: enterprise and organization reports
# Report types: 1-day and 28-day reports
# Docs link given in changelog (not yet updated as of 2026-07-18 — see Claim 7):
#   https://docs.github.com/rest/copilot/copilot-usage-metrics

daily_active_copilot_app_users
  Type:        integer (exact type unspecified in changelog)
  Description: The number of distinct users active in the Copilot app on a given day.
  No-activity value: null

totals_by_copilot_app
  Type:        object (exact schema unspecified in changelog)
  Description: A dedicated GitHub Copilot app section reporting:
                 session_count
                 request_count
                 prompt_count
                 token_usage:
                   output_tokens_sum
                   prompt_tokens_sum
                   avg_tokens_per_request
  Isolation:   Kept separate from totals_by_feature, totals_by_model_feature,
               totals_by_language_feature, and lines-of-code metrics
               (loc_added_sum / loc_deleted_sum).
  No-activity value: null
```

*Source: GitHub Copilot app now available in the usage metrics API, GitHub Changelog,
July 17, 2026*

### Copilot Metrics API — Surface Integration Pattern Comparison (compiled by the Miner)

```
Surface        Added        Integrated into shared totals?     Dedicated section?
─────────────────────────────────────────────────────────────────────────────────
CCA             Apr 10, 2026  no (own DAU/WAU/MAU fields)        no dedicated totals_by_*
CLI             Apr 10, 2026  YES — feature=copilot_cli inside    no (folds into shared
                               totals_by_feature, totals_by_       breakdowns instead)
                               model_feature, totals_by_
                               language_feature, plus top-level
                               aggregates (loc_*, code_gen_*)
Copilot app     Jul 17, 2026  NO — explicitly excluded from        YES — totals_by_
                               totals_by_feature/model/language     copilot_app, isolated
                               and lines-of-code metrics

# CLI (Apr 10) merges into the shared feature-breakdown model.
# Copilot app (Jul 17) is architecturally isolated instead — a third
# integration pattern (alongside CCA's own-DAU-fields pattern and
# CLI's merge-into-shared-breakdowns pattern) for a new Copilot surface.
```

*Compiled from: April 10, 2026 and July 17, 2026 GitHub changelogs; see
`docs-github-copilot-cli-activity-usage-metrics.md` for the CLI-side detail.*

## Cross-References

- **Extends** `docs-github-copilot-usage-metrics-adoption-cohorts.md` Claim 5 (Phase 3
  "Multi-agent" qualifies a user who "engaged with two or more GitHub-based agent
  surfaces, or with the new GitHub Copilot app"): The May 29, 2026 adoption-phase
  changelog first named "the new GitHub Copilot app" as a standalone Phase 3 qualifier,
  but that source provided no metric to observe app engagement directly — Phase 3
  classification was the only visible signal. This July 17 changelog is the first source
  in the corpus to expose the Copilot app's own activity metrics
  (`daily_active_copilot_app_users`, `totals_by_copilot_app`) independent of the phase
  model. The changelog does not state whether these two data points are linked (i.e.,
  whether a user counted in `daily_active_copilot_app_users` is guaranteed to be
  Phase 3) — that interaction is unconfirmed and is a gap for a future source to close.

- **Extends** `docs-github-copilot-app-security-review.md` (entire note, July 14, 2026):
  That note documented the `/security-review` slash command shipping inside the Copilot
  app chat window, three days before this changelog. Together the two sources establish
  the Copilot app as a surface receiving both feature investment (July 14) and
  observability investment (July 17) within the same week — consistent with GitHub
  treating the Copilot app as an actively developed, first-class surface rather than an
  experimental one. Neither source states whether `/security-review` invocations inside
  the app are counted toward `totals_by_copilot_app.request_count` /
  `.prompt_count` — a plausible but unconfirmed inference.

- **Extends** `docs-github-copilot-usage-metrics-ai-credits-per-user.md` Concrete
  Artifacts → "Copilot Usage Metrics Analytical Dimensions" table: That table (as of
  June 19, 2026) enumerates the corpus's activity-dimension fields
  (`daily_active_copilot_cloud_agent_users`, `weekly_active_copilot_cloud_agent_users`,
  `monthly_active_copilot_cloud_agent_users`, `monthly_active_agent_users`,
  `used_copilot_coding_agent`). `daily_active_copilot_app_users` (this note) is a new
  entry in that same activity dimension, following the established
  `daily_active_copilot_<surface>_users` naming convention but — unlike the CCA family —
  shipping with no corresponding weekly/monthly variant in this changelog. That note's
  Claim 3 also established that `ai_credits_used` carries no feature/surface breakdown;
  this note's `totals_by_copilot_app.token_usage` sub-fields are the first
  surface-scoped, non-billing token metric in the corpus (see Claim 3 above).

- **Contrasts with (not a contradiction)** `docs-github-copilot-cli-activity-usage-metrics.md`
  Claim 3 and Claim 8 (CLI integrated as `feature=copilot_cli` inside `totals_by_feature`,
  establishing CLI as "a first-class named feature surface" within the shared breakdown
  model): This note's Claim 5 documents the opposite architectural choice for the Copilot
  app — explicit exclusion from `totals_by_feature` and the other shared breakdowns, in
  favor of an isolated `totals_by_copilot_app` section. Both are real, current, and
  non-conflicting facts about two different Copilot surfaces; this is a conditioning
  variable (different surfaces integrated differently), not two sources disagreeing
  about the same fact, so no contradiction issue is filed per MINER.md §4a. The guide
  should document explicitly that `totals_by_feature` alone is NOT a complete
  cross-surface adoption view as of July 17, 2026 — the Copilot app must be queried
  separately.

- **Related** `docs-github-copilot-team-level-usage-metrics.md` Claim 5 (team-level
  breakdowns cover "IDE completions, chat, Copilot CLI, code review, and Copilot cloud
  agent activity," as of May 14, 2026 — the Copilot app is not in that list, since it did
  not yet exist as a tracked surface). This July 17 changelog does not state whether
  `totals_by_copilot_app` is joinable via the May 14 user-teams report, or whether the
  team-level surface list will be extended to include the Copilot app in a future
  release. This is an open question, not answered by either source.

- **Novel**:
  - **First token-usage breakdown in the usage metrics API outside the billing-derived
    `ai_credits_used` field**: `totals_by_copilot_app.token_usage` (`output_tokens_sum`,
    `prompt_tokens_sum`, `avg_tokens_per_request`) is the first corpus example of
    token-level metrics exposed directly in the usage metrics API, as opposed to the
    opaque, non-token, billing-derived `ai_credits_used` total (June 19, 2026).
  - **Third distinct surface-integration architecture**: CCA uses dedicated
    DAU/WAU/MAU fields with no shared-breakdown participation; CLI merges into the
    shared `totals_by_feature` family and top-level aggregates; the Copilot app uses a
    third pattern — a fully isolated dedicated section excluded from all shared totals.
    No prior corpus source documents three distinct integration patterns for the same
    underlying metrics API.
  - **`null` (not empty-object or omitted-key) as the explicit no-activity signal**:
    This is the first corpus source to state `null` as the specific JSON value for a
    Copilot metrics field when no activity exists, as distinct from the June 15,
    2026 server-side telemetry note's "empty breakdown" behavior for a different kind of
    data gap.
  - **Documentation lag observed directly**: This is the first corpus source note where
    the Miner followed the changelog's own linked documentation and found it not yet
    updated to reflect the announced fields (Claim 7) — a first-hand observation rather
    than an inference from changelog text alone.

## Guide Impact

- **Chapter 05 (Measurement) — "Multi-surface Copilot observability" section**: Add
  `daily_active_copilot_app_users` and `totals_by_copilot_app` as the newest tier in the
  Copilot metrics surface inventory (alongside CCA, CLI, IDE, chat, code review). Document
  explicitly, citing Claim 5, that unlike CLI (integrated into `totals_by_feature`), the
  Copilot app is architecturally isolated in its own section — any guide table or
  checklist that says "query `totals_by_feature` for full cross-surface adoption" is now
  incomplete and must add "plus `totals_by_copilot_app` for the Copilot app specifically."
- **Chapter 05 — "Cost and token observability" section** (new or extend): Document
  `totals_by_copilot_app.token_usage` as the first non-billing, surface-scoped token
  metric in the API, distinct from the per-user, non-surface-scoped `ai_credits_used`
  field (June 19, 2026). Note that combining the two does not currently yield an exact
  per-surface cost figure — that requires an unconfirmed mapping between tokens and
  credits.
- **Chapter 05 — "Metrics API null-handling" section** (new or extend, citing Claim 6):
  Add `totals_by_copilot_app` / `daily_active_copilot_app_users` returning `null` (not
  zero or an omitted key) for orgs with no app activity as a concrete example pipeline
  code must defensively null-check, alongside the June 15, 2026 empty-breakdown pattern
  for server-side-only users — two distinct incompleteness patterns in the same API that
  require two distinct defensive checks.
- **Chapter 02 (Harness Engineering) — "Enterprise Copilot observability pipeline"
  section**: Add the Copilot app tier to the recommended pipeline architecture, and flag
  (per Claim 7) that at launch the linked reference documentation may lag the changelog
  announcement — recommend verifying new fields against a live API response rather than
  reference docs alone in the days immediately following a metrics-API changelog.

## Extraction Notes

1. **WebFetch summarization risk avoided by direct HTML fetch**: An initial WebFetch call
   against this URL returned a plausible but shorter paraphrase (e.g., "Type: Improvement"
   framing and a condensed "Key Points" list not present verbatim in the source). All
   quotes and facts in this note were re-verified against a direct `curl` fetch of the
   live page HTML (saved locally during extraction) and cross-checked byte-for-byte,
   including curly vs. straight apostrophe characters (the article body uses `app's`
   with a curly apostrophe `'`, `’`). Every `Quote` field above was copied
   character-for-character from the `<article>` content in that raw HTML.
2. **Linked documentation followed and found not yet updated**: Per MINER.md §1 ("follow
   up to 5 linked pages that seem substantive"), the single outbound documentation link
   was followed, which in turn linked to two further docs pages (the reference index and
   its example-schema sub-page). None of the three mention the new fields as of
   2026-07-18. This is recorded as Claim 7 rather than silently omitted, since it affects
   how confidently a reader can rely on the reference docs immediately after this
   changelog.
3. **No access-tier statement in this changelog**: Unlike the May 14 and May 29, 2026
   Copilot metrics changelogs (both of which stated "enterprise administrator or
   organization owner" access requirements explicitly), this changelog contains no
   "Important notes" line restating the access tier. This is flagged as a scope gap in
   Source Context rather than assumed — we do not infer the access tier is unchanged
   without a stated basis, though it is plausible given the consistent pattern across
   the whole metrics-API changelog series.
4. **No contradictions filed**: The Copilot app's isolated integration pattern (Claim 5)
   differs architecturally from the CLI's merged-into-shared-breakdowns pattern
   (April 10, 2026), but this is a conditioning variable — two different surfaces
   integrated two different ways — not two sources making opposing claims about the same
   fact. Per MINER.md §4a, no contradiction issue was filed; the difference is
   cross-referenced explicitly under "Contrasts with" above so the Assayer and Smith see
   it during review.
5. **Source is a very short product changelog (~150 words, "1 minute read" per the page's
   `twitter:data1` meta tag)**: All substantive claims from the article itself are
   exhausted in Claims 1–6. Claim 7 is the Miner's own follow-up finding from the linked
   documentation, not additional text mined from the changelog body.
