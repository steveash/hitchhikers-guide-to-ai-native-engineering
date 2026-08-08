---
source_url: https://github.blog/changelog/2026-08-07-copilot-usage-metrics-api-adds-agent-app-activity
source_type: docs
title: "Copilot usage metrics API adds agent app activity"
author: GitHub (official changelog)
date_published: 2026-08-07
date_extracted: 2026-08-08
last_checked: 2026-08-08
status: current
confidence_overall: settled
issue: "#2566"
---

# Copilot Usage Metrics API Adds Agent App Activity (GitHub Changelog, August 7, 2026)

> GitHub's August 7, 2026 changelog adds a `totals_by_3rd_party_agent` array to
> the Copilot usage metrics API, breaking out per-agent activity (agent name,
> stable ID, job-start count, session count) for third-party agent apps like
> Claude and Codex running in GitHub workflows — replacing a previously
> undifferentiated single bucket for all agent activity.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words, "2 minute
  read," August 7, 2026)
- **Author credibility**: GitHub engineering team announcing a production API
  field addition. Authoritative for the fact that the field exists, its name,
  its sub-fields, and its stated scope/access tier. Not authoritative for any
  claim about how much genuine multi-agent adoption this newly-attributed data
  reveals — no adoption numbers are cited, only the measurement mechanism.
  Also fetched and cross-checked the linked conceptual documentation page
  (`docs.github.com/copilot/reference/copilot-usage-metrics/copilot-usage-metrics#agent-apps-metrics-fields`,
  retrieved via direct HTTP fetch on 2026-08-08), which supplies field types
  and nullability not stated in the changelog itself — see Extraction Notes.
- **Scope**: One new optional array field (`totals_by_3rd_party_agent`) added
  to the Copilot usage metrics REST API at the enterprise, organization,
  enterprise-user, and organization-user report levels, for both 1-day and
  28-day windows. Covers the four sub-fields, the aggregation/collapse rule
  for multiple integrations per agent, the access tier, and the stated
  backward-compatibility behavior. Does NOT cover: which specific agent apps
  are currently "recognized" (no enumerated list of supported agents is
  given); how `session_count` is defined for a "session" precisely, beyond
  "distinct, non-empty session counts"; whether this data feeds into the
  `ai_credits_used` per-user billing metric or the adoption-phase cohort
  model; or any comparison of this per-agent breakdown against Copilot's own
  coding-agent (CCA) usage figures.

## Extracted Claims

### Claim 1: The Copilot usage metrics API now reports third-party agent app activity broken out by individual agent, at the enterprise, organization, enterprise-user, and organization-user levels, for both 1-day and 28-day reports

- **Evidence**: Changelog opening paragraph, confirmed via direct HTTP fetch
  of the raw article HTML.
- **Confidence**: settled (product fact — explicitly stated as the change)
- **Quote**: "Since agent apps arrived on GitHub, teams have been able to run
  agents from partners like Claude and Codex directly in their GitHub
  workflows. The Copilot usage metrics API now reports that activity, broken
  out by individual agent. The usage metrics API does this in the enterprise,
  organization, enterprise-user, and organization-user 1-day and 28-day
  reports."
- **Our assessment**: This is the central claim: agent-app activity moves
  from an undifferentiated aggregate to a per-agent breakdown. The scope
  statement is precise about four report types (enterprise, organization,
  enterprise-user, organization-user) — narrower than the plain "user" report
  type, a distinction the corpus has already flagged as significant for the
  July 28, 2026 Copilot-app fields (`docs-github-copilot-app-usage-metrics-report-rollups.md`
  Claim 10), which used the identical enterprise-user/organization-user
  scoping for its new per-user fields.

### Claim 2: `totals_by_3rd_party_agent` is a new optional array containing one entry per recognized agent app, with fields `agent_name`, `agent_id`, `user_initiated_interaction_count`, and `session_count`

- **Evidence**: "What's new" section, full bulleted field list.
- **Confidence**: settled (definitional — full field list stated explicitly)
- **Quote**: "A new optional `totals_by_3rd_party_agent` array contains one
  entry per recognized agent app."
- **Our assessment**: This is a coarser per-agent field set than the
  richer `totals_by_copilot_app` section documented for GitHub's own Copilot
  app (`docs-github-copilot-app-usage-metrics-report-rollups.md` Claim 4:
  `session_count`, `request_count`, `prompt_count`, plus a three-way
  `token_usage` breakdown). The third-party agent fields have no
  `request_count`, `prompt_count`, or token accounting — only a job-start
  interaction count and a session count. This is a meaningful capability gap
  between what GitHub can measure for its own first-party app versus
  third-party agent apps, presumably because GitHub does not have
  request/token-level visibility into a third-party agent's internal
  operation, only into the job-start events it can observe at the platform
  boundary.

### Claim 3: `agent_name` is the agent's display name and can change over time, so `agent_id` — the stable identifier — is the correct key for grouping and joining across reporting periods

- **Evidence**: "What's new" section, field definitions for `agent_name` and
  `agent_id`.
- **Confidence**: settled (definitional, with an explicit usage
  recommendation)
- **Quote**: "`agent_name`: The agent's display name. Display names can
  change, so group on `agent_id` rather than this field. `agent_id`: The
  agent's stable identifier, and the right key for joining across reporting
  periods."
- **Our assessment**: This display-name-vs-stable-id split mirrors a pattern
  already established elsewhere in the metrics API for model names (which
  can be renamed for marketing reasons) — but this is the first place in the
  corpus this pattern is documented for *agents* specifically. Any dashboard
  or pipeline built to track a given third-party agent's usage trend over
  time must key on `agent_id`, not `agent_name`, or it risks silently
  splitting one agent's history into two rows if GitHub or the publisher
  ever renames the display string.

### Claim 4: The nested `user_initiated_interaction_count` counts agent app job starts and is distinct from the top-level field of the same name, which counts explicit prompts from other supported telemetry — the two must not be summed or treated as interchangeable

- **Evidence**: "Important notes" section, first bullet.
- **Confidence**: settled (explicit disambiguation warning from the official
  changelog)
- **Quote**: "The nested `user_initiated_interaction_count` counts agent app
  job starts. It is distinct from the top-level field of the same name,
  which counts explicit prompts from other supported telemetry. Do not sum
  the two or treat them as interchangeable."
- **Our assessment**: This is the single most operationally important
  caveat in the source — a field-name collision between a per-agent nested
  count and a pre-existing top-level count of a different kind of event
  (explicit prompts, per the conceptual docs page fetched separately: "Number
  of explicit prompts sent to Copilot ... Only counts messages or prompts
  actively sent to the model"). A job start and a prompt are not the same
  unit of activity — one agent job can plausibly involve many prompts, or a
  job could start without a matching top-level prompt event depending on how
  the agent's telemetry is wired. Any pipeline that naively sums
  `totals_by_3rd_party_agent[].user_initiated_interaction_count` into the
  top-level `user_initiated_interaction_count` will double-count or produce
  a meaningless composite number. GitHub explicitly warns against exactly
  that operation.

### Claim 5: Activity is aggregated by agent, so multiple integrations belonging to the same agent collapse into a single entry; activity from agents that cannot be identified is omitted entirely

- **Evidence**: "Important notes" section, second bullet.
- **Confidence**: settled (explicit aggregation and omission rule)
- **Quote**: "Activity is aggregated by agent, so multiple apps belonging to
  the same agent are collapsed into one entry. Activity from agents that
  cannot be identified is omitted."
- **Our assessment**: Two distinct rules here. First, if an agent publisher
  ships more than one integration surface (for example, separate GitHub App
  installations or workflow entry points) that both map to the same
  `agent_id`, their activity is summed into one array entry rather than
  appearing as separate rows — consistent with the conceptual docs page's
  phrasing that entries are "grouped by `agent_id`, and integrations that map
  to the same agent are combined." Second, and more consequential for
  completeness: activity from an agent GitHub cannot identify is dropped
  from the array entirely, not folded into some "unknown agent" bucket. This
  means `totals_by_3rd_party_agent` is not guaranteed to be an exhaustive
  accounting of all agent activity in a workflow run — an organization
  running an unrecognized or custom agent (for example, a bespoke gh-aw
  third-party-engine integration per `docs-ghaw-guides-third-party-agent.md`)
  may see less agent activity in this array than actually occurred, with no
  visible indication that anything was omitted.

### Claim 6: `session_count` — the number of agent app sessions — is included only in the aggregated enterprise and organization reports; per-user report entries omit this field

- **Evidence**: "What's new" section, `session_count` field definition.
- **Confidence**: settled (explicit scope restriction stated per-field,
  distinct from the report-level scope stated in Claim 1)
- **Quote**: "`session_count`: The number of agent app sessions. Included in
  the aggregated enterprise and organization reports only. Per-user entries
  omit this field."
- **Our assessment**: This is a field-level scope restriction nested inside
  the broader report-level scope already established in Claim 1 (which
  covers enterprise, organization, enterprise-user, and organization-user
  reports). So the practical layering is: `agent_name`, `agent_id`, and
  `user_initiated_interaction_count` appear at all four report levels, but
  `session_count` appears only in the two aggregate (non-per-user) report
  types. A team building a per-user drill-down of agent activity gets
  job-start counts per user but cannot get a per-user session count from
  this field — only the aggregate. This mirrors the layered-availability
  pattern the corpus already documented for the July 28, 2026 Copilot app
  fields, where different sub-fields had different report-type scopes within
  the same overall announcement.

### Claim 7: Access requires enterprise owner or billing manager status, organization owner status, or a custom organization/enterprise role granting the "View Copilot Metrics" permission, with the Copilot usage metrics policy enabled

- **Evidence**: "Important notes" section, third bullet.
- **Confidence**: settled (stated access tier from official changelog)
- **Quote**: "These metrics are available to enterprise owners and billing
  managers, organization owners, and anyone with a custom organization or
  enterprise role that grants the View Copilot Metrics permission. The
  Copilot usage metrics policy must be enabled."
- **Our assessment**: This is character-for-character identical to the
  access-tier language in the July 28, 2026 Copilot app metrics changelog
  (`docs-github-copilot-app-usage-metrics-report-rollups.md` Claim 11's
  quote), reused verbatim across two changelogs eleven months apart in the
  metrics-API series. This confirms the corpus's existing observation that
  the Copilot usage metrics API has a single, stable access-control model
  applied uniformly as new surfaces are added — no surface-specific
  permission variant has been introduced for agent-app data specifically.

### Claim 8: The change is backward compatible — existing fields keep their current shape, and reports omit `totals_by_3rd_party_agent` entirely when there is no recognized agent app activity for the period

- **Evidence**: "Important notes" section, fourth bullet.
- **Confidence**: settled (explicit backward-compatibility guarantee)
- **Quote**: "The change is backward compatible. Existing fields keep their
  current shape, and reports omit `totals_by_3rd_party_agent` entirely when
  there is no recognized agent app activity for the reporting period."
- **Our assessment**: This is the same sparse-inclusion (omit-rather-than-
  zero-fill) convention already documented across the corpus's Copilot usage
  metrics series — most directly corroborating
  `docs-github-copilot-app-usage-metrics-report-rollups.md` Claim 12, which
  states the identical omit-not-zero-fill rule and identical
  backward-compatibility framing for `totals_by_copilot_app`, down to the
  near-identical sentence structure ("The changes are backward compatible.
  Users and entities with no Copilot app activity omit
  `totals_by_copilot_app`..." vs. this changelog's "The change is backward
  compatible. Existing fields keep their current shape, and reports omit
  `totals_by_3rd_party_agent`..."). GitHub is applying a consistent,
  templated backward-compatibility statement each time it adds a new
  optional array/section to this API.

### Claim 9: Per-agent breakdowns are framed as answering "which agents are actually being used, by how many people, and how does adoption of a newly rolled-out agent compare to the one it was meant to supplement" and letting organizations "ground rollout and licensing decisions in real usage rather than assumption"

- **Evidence**: "Why this matters" section.
- **Confidence**: anecdotal (vendor framing of intended use case; no
  adoption or comparison data is cited to demonstrate this actually happens
  in practice)
- **Quote**: "Until now, agent activity in your usage metrics was effectively
  a single bucket, so there was no way to tell Copilot coding agent work
  apart from work done through other agents. As teams adopt more than one
  agent, that made it hard to answer basic questions: which agents are
  actually being used, by how many people, and how does adoption of a newly
  rolled-out agent compare to the one it was meant to supplement. Breaking
  activity out per agent lets you distinctly track each agent app, compare
  adoption across them, and ground rollout and licensing decisions in real
  usage rather than assumption."
- **Our assessment**: The "ground ... licensing decisions in real usage" framing
  is the most concretely actionable part: organizations paying per-seat or
  per-agent licensing fees for multiple coding agents (Claude, Codex, and
  others) now have a first-party, no-cost data source to justify or
  reconsider those licenses, rather than relying on anecdote about which
  agent teams "seem to prefer." As with the equivalent framing already
  flagged as anecdotal for the July 28, 2026 Copilot app note
  (`docs-github-copilot-app-usage-metrics-report-rollups.md` Claim 9), the
  data-availability claim (you *can* compare adoption) is verifiable from
  the field definitions above; the implied behavioral claim (organizations
  *will* use this to make better licensing decisions) is not demonstrated by
  this source.

### Claim 10: This changelog's opening sentence explicitly states that "Copilot coding agent work" is one of the things previously conflated inside the single undifferentiated agent-activity bucket — implying Copilot's own cloud agent (CCA) activity is itself one of the entries this new array can now distinguish from third-party agents

- **Evidence**: "Why this matters" section, first sentence: "there was no way
  to tell Copilot coding agent work apart from work done through other
  agents."
- **Confidence**: emerging (the changelog's field name is
  `totals_by_3rd_party_agent`, which by its own name suggests third-party
  scope; whether Copilot's own coding/cloud agent appears as a row inside
  this specifically "3rd-party"-named array, or is tracked elsewhere and
  merely used as the comparison baseline in this sentence, is not
  unambiguously resolved by the changelog text alone)
- **Quote**: "there was no way to tell Copilot coding agent work apart from
  work done through other agents"
- **Our assessment**: This is a genuine ambiguity worth flagging rather than
  resolving. Two readings are both plausible from the text: (a) Copilot
  cloud agent (CCA) activity previously blended into the same undifferentiated
  bucket as third-party agents, and this change lets you separate CCA from
  Claude/Codex — which would imply CCA now shows up as one row inside
  `totals_by_3rd_party_agent`, in tension with the field's "3rd-party" name;
  or (b) the sentence is simply using "Copilot coding agent work" as the
  familiar reference point to explain why *third-party* agent
  undifferentiation was confusing, without claiming CCA itself lives inside
  this array. The corpus already has a fully separate, dedicated CCA
  aggregate-metrics primitive (`docs-github-copilot-cca-usage-metrics-aggregate.md`:
  `daily_active_copilot_cloud_agent_users` / `weekly_...` / `monthly_...`),
  which argues for reading (b) — CCA already has its own fields and would be
  redundant inside a "3rd-party" array. Neither this changelog nor the
  conceptual docs page's "Agent apps metrics fields" section names Copilot
  cloud agent as an example entry in `totals_by_3rd_party_agent`. Flagged as
  emerging rather than settled; the Smith should not assert either reading
  as fact without further evidence.

### Claim 11: These per-agent metrics are sourced from server-side job activity rather than client telemetry

- **Evidence**: Conceptual documentation page (`docs.github.com/copilot/reference/copilot-usage-metrics/copilot-usage-metrics#agent-apps-metrics-fields`),
  fetched directly on 2026-08-08 as a linked sub-page from the changelog's
  "Agent apps metrics fields" link. Not stated in the changelog itself.
- **Confidence**: settled (definitional statement on the first-party
  reference documentation page, though not corroborated by the changelog's
  own text)
- **Quote**: "These metrics come from server-side job activity."
- **Our assessment**: This is a data-provenance detail absent from the
  changelog but present on the linked reference page. It matters because the
  corpus already documents a separate June 15, 2026 methodology change
  adding server-side telemetry to *client*-telemetry-based Copilot usage
  reports specifically to close undercounting gaps
  (`docs-github-copilot-usage-metrics-server-side-telemetry.md`). This
  agent-app metric being server-side-sourced from the start (not a client-telemetry
  field later supplemented by server-side data) suggests GitHub is
  designing newer metrics surfaces around server-observable events (job
  starts, sessions) rather than client-reported ones — plausible given that
  a third-party agent's internal client telemetry, if any, would not be
  GitHub's to instrument. This is a different mechanism from the June 15
  change, not a restatement of it, but both reflect a broader shift toward
  platform/server-side signal sourcing for parts of the Copilot metrics
  API where client instrumentation is unavailable or unreliable.

## Concrete Artifacts

### Verbatim Changelog Body Text (August 7, 2026, retrieved via direct HTTP fetch of the raw article HTML on 2026-08-08)

```
Copilot usage metrics API adds agent app activity
Improvement | August 7, 2026 • 2 minute read

Since agent apps arrived on GitHub, teams have been able to run agents from
partners like Claude and Codex directly in their GitHub workflows. The
Copilot usage metrics API now reports that activity, broken out by
individual agent. The usage metrics API does this in the enterprise,
organization, enterprise-user, and organization-user 1-day and 28-day
reports.

What's new
A new optional totals_by_3rd_party_agent array contains one entry per
recognized agent app. Each entry includes:
agent_name: The agent's display name. Display names can change, so group on
agent_id rather than this field.
agent_id: The agent's stable identifier, and the right key for joining
across reporting periods.
user_initiated_interaction_count: The number of user-initiated agent app job
starts.
session_count: The number of agent app sessions. Included in the aggregated
enterprise and organization reports only. Per-user entries omit this field.

Why this matters
Until now, agent activity in your usage metrics was effectively a single
bucket, so there was no way to tell Copilot coding agent work apart from
work done through other agents. As teams adopt more than one agent, that
made it hard to answer basic questions: which agents are actually being
used, by how many people, and how does adoption of a newly rolled-out agent
compare to the one it was meant to supplement.

Breaking activity out per agent lets you distinctly track each agent app,
compare adoption across them, and ground rollout and licensing decisions in
real usage rather than assumption.

Important notes
The nested user_initiated_interaction_count counts agent app job starts. It
is distinct from the top-level field of the same name, which counts
explicit prompts from other supported telemetry. Do not sum the two or
treat them as interchangeable.

Activity is aggregated by agent, so multiple apps belonging to the same
agent are collapsed into one entry. Activity from agents that cannot be
identified is omitted.

These metrics are available to enterprise owners and billing managers,
organization owners, and anyone with a custom organization or enterprise
role that grants the View Copilot Metrics permission. The Copilot usage
metrics policy must be enabled.

The change is backward compatible. Existing fields keep their current
shape, and reports omit totals_by_3rd_party_agent entirely when there is no
recognized agent app activity for the reporting period.

Visit the Copilot usage metrics API documentation to get started, or see
Agent apps metrics fields for the full field definitions.
```

*Source: https://github.blog/changelog/2026-08-07-copilot-usage-metrics-api-adds-agent-app-activity,
retrieved via direct HTTP fetch of the raw `<article>` element on
2026-08-08 (an initial WebFetch pass returned a paraphrased,
model-processed summary that omitted the exact "Table of Contents"
structure and lightly reworded some sentences — see Extraction Notes item
1). Every quote in this note is taken from this raw-HTML extraction.*

### Agent Apps Metrics Field Reference (compiled from the linked conceptual docs page, `docs.github.com/copilot/reference/copilot-usage-metrics/copilot-usage-metrics#agent-apps-metrics-fields`, fetched 2026-08-08)

```
# Copilot usage metrics API — totals_by_3rd_party_agent fields
# (as documented on the conceptual reference page, current as of 2026-08-08;
#  NOT yet present on the separate REST API reference page — see Extraction
#  Notes item 2)

totals_by_3rd_party_agent[].agent_name
  Type: string | Nullable: No
  Description: Display name of the agent app. The name can change, so use
  agent_id for grouping.

totals_by_3rd_party_agent[].agent_id
  Type: string | Nullable: No
  Description: Stable identifier for the agent app.

totals_by_3rd_party_agent[].user_initiated_interaction_count
  Type: integer | Nullable: No
  Description: Number of user-initiated jobs started for the agent app
  during the reporting period. Each job start increments the count once.

totals_by_3rd_party_agent[].session_count
  Type: integer | Nullable: No
  Description: Sum of distinct, non-empty session counts for integrations
  mapped to the agent during the reporting period. Included only in
  aggregated enterprise and organization reports; omitted from per-user
  reports.

Parent field:
totals_by_3rd_party_agent (array, Nullable: Yes)
  Omitted when the user/enterprise/organization had no recognized agent app
  activity during the reporting period.

Data source note (docs page, not stated in the changelog):
  "These metrics come from server-side job activity."

For comparison — top-level field with the colliding name:
user_initiated_interaction_count (top level, integer, No)
  "Number of explicit prompts sent to Copilot. Only counts messages or
  prompts actively sent to the model. Does not include opening the chat
  panel, switching modes ... using keyboard shortcuts to open the inline
  UI, or making configuration changes."
```

*Compiled from the conceptual docs page's "Agent apps metrics fields" and
top-level-fields tables, fetched directly via HTTP on 2026-08-08 (950KB raw
HTML; the field type/nullable table was located via full-text search for
`3rd_party_agent` in the raw HTML and is reproduced above with attribution).*

## Cross-References

- **Extends** `docs-github-copilot-app-usage-metrics-report-rollups.md`:
  - Claim 4 (`totals_by_copilot_app`'s richer per-user field set:
    `session_count`, `request_count`, `prompt_count`, plus a `token_usage`
    breakdown): This source's Claim 2 adds a sixth surface
    (third-party agent apps) to the corpus's multi-surface metrics landscape,
    but with a visibly coarser field set — no request count, prompt count, or
    token accounting, only job-start and session counts. See this note's
    Claim 2 assessment for the likely reason (GitHub cannot see inside a
    third-party agent's own request/token accounting the way it can for its
    own Copilot app).
  - Claim 11 (the access-tier language — "enterprise owners and billing
    managers, organization owners ... View Copilot Metrics permission ...
    Copilot usage metrics policy must be enabled"): This source's Claim 7
    reuses the identical sentence, confirming a single stable access-control
    model applied uniformly across the metrics-API expansion series.
  - Claim 12 (backward-compatibility / sparse-inclusion guarantee: entities
    with no activity omit the new field/section entirely rather than
    zero-filling): This source's Claim 8 states the same guarantee for
    `totals_by_3rd_party_agent`, using near-identical sentence structure —
    the third documented instance in the corpus of GitHub's templated
    backward-compatibility statement for a new optional metrics field (the
    other two being the July 28 Copilot app note and, per that note's own
    Cross-References, the July 17, 2026 repository-level report's
    sparse-inclusion rule).
  - Extraction Notes item 2 (the REST API reference page,
    `docs.github.com/rest/copilot/copilot-usage-metrics`, had not yet been
    updated to reflect the July 28, 2026 Copilot app fields as of that
    note's extraction date, a documentation-lag finding): This source's
    Extraction Notes item 2 (below) confirms the same documentation-lag
    pattern recurs for the August 7, 2026 agent-app fields — the REST API
    reference page still does not contain `totals_by_3rd_party_agent` as of
    2026-08-08, even though the separate conceptual reference page does.
    This is now a second independently confirmed instance of the same
    documentation-lag behavior, twelve days short of two weeks apart in
    freshness terms, suggesting it is a structural characteristic of
    GitHub's docs publishing pipeline for this API rather than a one-off gap.

- **Extends** `docs-github-copilot-cca-usage-metrics-aggregate.md`:
  - Claim 6 (CCA's aggregate counts "sit alongside existing metrics ...
    giving you a full view of Copilot adoption across surfaces"): This
    source adds yet another surface to that multi-surface view — but for
    *third-party* agents specifically, distinct from Copilot's own cloud
    agent (CCA), which already has its own dedicated
    `daily_active_copilot_cloud_agent_users`/`weekly_...`/`monthly_...`
    fields. This note's Claim 10 flags an unresolved ambiguity in the new
    changelog's own text about whether CCA activity is conflated with or
    distinct from the third-party agents tracked in
    `totals_by_3rd_party_agent` — worth resolving in a future source note if
    GitHub clarifies.

- **Extends** `docs-github-copilot-usage-metrics-server-side-telemetry.md`:
  - This source's Claim 11 (agent app metrics are sourced from server-side
    job activity, per the linked conceptual docs page) is a distinct
    server-side-sourcing decision from the June 15, 2026 note's server-side
    *supplement* to client telemetry for general DAU counts. The two are not
    the same mechanism — the June 15 note describes filling gaps in an
    existing client-telemetry-based pipeline; this source describes a metric
    that appears to be server-side-sourced by design, with no client-telemetry
    predecessor described. Both reflect a broader pattern of GitHub relying
    on server-observable signals where client instrumentation is unavailable
    or unreliable — worth grouping under a shared Ch05 discussion of metric
    provenance.

- **Corroborates** `docs-github-copilot-security-validation-third-party-agents.md`
  Claim 1 (GitHub extending Copilot-exclusive capabilities — there, security
  validation — to third-party agents like Claude and Codex as a "feature
  parity" platform strategy): This source is a second, independent instance
  of the same parity pattern applied to usage-metrics observability rather
  than security scanning. Together the two notes establish that GitHub's
  "treat third-party agents as first-class platform citizens" strategy
  (named explicitly in that note's Claim 1 assessment) now spans at least
  two distinct capability areas — security validation (June 9, 2026) and
  usage-metrics observability (August 7, 2026) — extended to the same named
  agents (Claude, Codex) in both cases.

- **Contradicts**: None identified. No existing source note claims that
  agent app activity cannot or should not be broken out per-agent, or that
  the prior single-bucket behavior was adequate. No contradiction issue
  filed.

- **Novel**:
  - **First per-agent (not per-surface) breakdown in the corpus's Copilot
    usage metrics series**: Every prior surface expansion in the corpus (CLI,
    PR review, CCA, Copilot app) adds a new *surface* dimension to the
    existing per-user/per-org rollups. This is the first to add a breakdown
    *within* a surface — one row per distinct third-party agent — rather than
    one row per surface type.
  - **`agent_id` vs. `agent_name` stable-identifier pattern for agents**: No
    prior source documents this display-name-vs-stable-id distinction applied
    to agents specifically (as opposed to models, which have their own
    separate naming considerations documented elsewhere in the corpus).
  - **Explicit "do not sum" warning for a field-name collision between a
    nested and top-level metric of the same name**: No prior corpus note
    documents GitHub proactively warning against a specific miscalculation a
    consumer might make by conflating two same-named fields at different
    nesting levels. This is a new category of documented pitfall for the
    metrics API.
  - **Silent omission of unidentifiable-agent activity**: No prior corpus
    note documents an explicit "activity that cannot be attributed is dropped
    from the report, not bucketed as unknown" behavior for the Copilot usage
    metrics API. This has a direct implication for completeness claims made
    about any dashboard built on this field.

## Guide Impact

- **Chapter 05 (Measurement) — "Metrics granularity hierarchy" / multi-surface
  adoption section**: Add third-party agent apps (`totals_by_3rd_party_agent`)
  as a per-agent breakdown available at the enterprise/organization/
  enterprise-user/organization-user levels, distinct from and coarser-grained
  than the existing per-surface breakdowns (Copilot app, CLI, CCA, code
  review, PR review). Explicitly note the field-set gap versus
  `totals_by_copilot_app`: no request/prompt/token accounting for
  third-party agents, only job-start and session counts.
- **Chapter 05 — "Metrics field-name collisions" (new subsection)**: Document
  the nested-vs-top-level `user_initiated_interaction_count` collision as a
  concrete example of a metrics-API pitfall worth calling out generally:
  always check whether a field name that appears at two nesting levels in
  the same API response measures the same underlying event before summing or
  comparing them.
- **Chapter 05 — "Adoption metric completeness caveats"**: Add that
  `totals_by_3rd_party_agent` silently omits activity from agents GitHub
  cannot identify — any dashboard built on this field should be presented as
  a lower bound on multi-agent activity, not an exhaustive accounting, and
  this caveat is not visually surfaced anywhere in the API response itself
  (no "N unidentified events omitted" counter).
- **Chapter 04 (Observability) — "Enterprise Copilot observability pipeline"**:
  Note the recurring documentation-lag pattern: the conceptual reference
  page for a new Copilot metrics field is typically updated close to the
  changelog's publish date, but the separate REST API reference page lags
  behind (confirmed independently for both the July 28, 2026 Copilot app
  fields and this August 7, 2026 agent-app field). Teams integrating against
  new fields should treat the changelog and the conceptual reference page as
  authoritative ahead of the REST API reference page.
- **Chapter 02 (Harness Engineering)**: For teams running third-party coding
  agents (Claude, Codex, or a custom gh-aw third-party-engine integration per
  `docs-ghaw-guides-third-party-agent.md`) through GitHub workflows, note
  that usage is now observable natively through the Copilot usage metrics
  API without any agent-side instrumentation — but only if GitHub's platform
  can identify the agent; a fully custom or unrecognized integration may not
  appear in `totals_by_3rd_party_agent` at all (per Claim 5).

## Extraction Notes

1. **WebFetch initial pass produced a paraphrased summary; raw HTTP fetch
   used for verbatim quotes**: An initial WebFetch call against the
   changelog URL returned a reasonably accurate but model-processed summary
   (correctly capturing the field names and most sentences, but reformatting
   section order and lightly rewording some passages). Per MINER.md §2a, the
   page was re-fetched via direct HTTP request (`curl`, following a 301
   redirect from the non-trailing-slash to the trailing-slash URL) and the
   raw `<article>` element extracted with a Python HTML-stripping script.
   Every quote in this note is taken from that raw-HTML extraction, not from
   the WebFetch summary. Unlike some prior source notes in this corpus (e.g.
   `docs-github-copilot-cli-activity-usage-metrics.md`), a raw fetch was
   possible for this source, so no quote in this note carries the "verify
   against live source" caveat those notes required.
2. **REST API reference page still lags this changelog**: The REST API
   reference page (`docs.github.com/rest/copilot/copilot-usage-metrics`) was
   fetched directly via HTTP on 2026-08-08 (460KB of HTML). A full-text
   search for `totals_by_3rd_party_agent`, `3rd_party_agent`, and `agent_id`
   returned zero matches, while `download_links` (a pre-existing field)
   appeared 48 times. This confirms the field has not yet been added to that
   specific reference page as of the extraction date — consistent with the
   documentation-lag pattern already noted for the July 28, 2026 Copilot app
   fields in `docs-github-copilot-app-usage-metrics-report-rollups.md`
   Extraction Notes item 2. No claim in this note depends on the REST API
   reference page; the field definitions are sourced from the changelog
   itself and the separate conceptual reference page (which does contain the
   field — see next item).
3. **One substantive sub-page followed**: The changelog links to "Agent apps
   metrics fields" at
   `docs.github.com/copilot/reference/copilot-usage-metrics/copilot-usage-metrics#agent-apps-metrics-fields`.
   This conceptual reference page (950KB of HTML, fetched directly via HTTP)
   was followed per MINER.md §1 because it supplies field types and
   nullability the changelog itself does not state — the source of Claim 2's
   type table and Claim 11's server-side-sourcing statement. The changelog's
   other link, "Copilot usage metrics API documentation"
   (`docs.github.com/rest/copilot/copilot-usage-metrics`), was also fetched
   and is the REST reference page discussed in Extraction Notes item 2. No
   further sub-pages were followed; both linked pages were substantive and
   directly relevant, and following more would exceed what this ~200-word
   changelog's scope calls for.
4. **No contradictions to file**: No existing source note claims that
   third-party agent activity cannot or should not be broken out per-agent,
   or that the prior undifferentiated-bucket behavior was sufficient. The
   ambiguity flagged in Claim 10 (whether Copilot cloud agent activity is
   itself inside this "3rd-party"-named array) is a genuine open question in
   the source's own text, not a contradiction between two sources — it is
   flagged as `emerging` confidence within Claim 10 rather than filed as a
   contradiction issue, since there is no second source making an opposing
   claim to contradict.
5. **Source is a short product changelog (~200 words)**: All eleven claims
   above are drawn from all three named sections of the changelog ("What's
   new," "Why this matters," "Important notes") plus the introductory
   paragraph, supplemented by the linked conceptual reference page (Claim 2's
   type table, Claim 11). No additional signal would come from re-reading
   the changelog itself.
