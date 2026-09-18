---
source_url: https://github.blog/changelog/2026-09-17-agentic-cli-customizations-now-in-the-usage-metrics-api
source_type: docs
title: "Agentic CLI customizations now in the usage metrics API"
author: GitHub (official changelog)
date_published: 2026-09-17
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: settled
issue: "#3527"
---

# Agentic CLI Customizations Now in the Usage Metrics API (GitHub Changelog, September 17, 2026)

> GitHub's September 17, 2026 changelog adds five new `totals_by_*` array
> fields and five matching `distinct_*_use_count` fields to the Copilot
> usage metrics API, giving enterprise and organization administrators
> per-item visibility into which Copilot CLI skills, custom agents, MCP
> servers, slash commands, and plugins developers actually use — the first
> metrics surface in the corpus to break CLI activity down *within* the
> CLI surface by customization type, rather than adding a new top-level
> surface dimension.

## Source Context

- **Type**: docs (GitHub official product changelog, ~200 words, "2 minute
  read," September 17, 2026). Also fetched and cross-checked the linked
  conceptual reference page
  (`docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics`,
  section "Copilot CLI customization fields (API only)", retrieved via
  direct HTTP fetch on 2026-09-18), which supplies field type/nullability
  tables and two operational caveats not stated in the changelog itself —
  see Extraction Notes.
- **Author credibility**: GitHub engineering team announcing a production
  API field addition. Authoritative for the fact that the fields exist,
  their names, what each counts, and their report-type scope. Not
  authoritative for how much genuine "enablement gap" insight this data
  actually produces in practice — no adoption numbers or customer examples
  are cited, only the measurement mechanism and its stated intent.
- **Scope**: Ten new fields (five `totals_by_*` arrays and five matching
  `distinct_*_use_count` counters) added to the Copilot usage metrics REST
  API, covering Copilot CLI skills, custom agents, MCP servers, slash
  commands, and plugins. Covers: which report types carry the fields, what
  each array/counter measures, the privacy-driven grouping of
  customer-defined names under `other`/`custom`, the MCP connection-attempt
  counting rule, the plugin/skill overlap rule, null/empty semantics, and
  the access tier. Does NOT cover: any enumerated list of "recognized
  GitHub-provided" skills, agents, MCP servers, or plugins; how this data
  relates to the `feature=copilot_cli` dimension in `totals_by_feature`
  documented in the April 10, 2026 CLI-integration changelog; whether this
  data feeds the adoption-phase cohort model; or any comparison against the
  September 11, 2026 sibling changelog adding VS Code agent metrics (title
  observed in the same changelog feed but not fetched or read for this
  note — flagged as a candidate for separate mining).

## Extracted Claims

### Claim 1: GitHub Copilot expands existing CLI report coverage with agentic activity metrics for five specific customization types: skills, custom agents, MCP servers, slash commands, and plugins

- **Evidence**: Changelog introductory sentence, confirmed via direct HTTP
  fetch of the raw article HTML.
- **Confidence**: settled (product fact — explicitly stated as the change)
- **Quote**: "GitHub Copilot expands existing CLI report coverage with agentic activity metrics for skills, custom agents, Model Context Protocol (MCP) servers, slash commands, and plugins."
- **Our assessment**: This is the central claim. Unlike the April 10, 2026
  change (`docs-github-copilot-cli-activity-usage-metrics.md`), which added
  CLI as a peer *surface* alongside IDE in existing aggregate fields, this
  change adds a breakdown *within* the CLI surface — the same architectural
  pattern the corpus already documented for third-party agents in
  `docs-github-copilot-usage-metrics-agent-app-activity.md` (per-agent
  breakdown within the agent-app surface, rather than a new surface
  dimension). Five customization types get identical treatment: a top-five
  "most used" array plus a distinct-count field.

### Claim 2: The new fields appear in enterprise and organization per-user and aggregate 1-day reports, per-user 28-day reports, and the `day_totals` entries in aggregate 28-day reports

- **Evidence**: "What's new" section, opening sentence.
- **Confidence**: settled (explicit report-type scope statement)
- **Quote**: "The fields appear in enterprise and organization per-user and aggregate 1-day reports, per-user 28-day reports, and the day_totals entries in aggregate 28-day reports."
- **Our assessment**: This scoping is corroborated, with slightly more
  precise phrasing, by the conceptual reference page: "Per-user 1-day and
  28-day reports. Aggregated 1-day reports. Each `day_totals` record in
  aggregated 28-day reports." Notably absent from both: aggregated (rolled-up,
  non-`day_totals`) 28-day reports do not carry these fields directly — a
  team wanting a 28-day view of customization adoption must sum or inspect
  the `day_totals` entries rather than reading a single top-level 28-day
  field, unlike the simpler per-day-and-aggregate scoping the corpus
  documented for CLI integration (April 10) and agent-app activity
  (August 7). This is a new, more granular scoping pattern than prior
  Copilot metrics surface additions in the corpus.

### Claim 3: Five `totals_by_*` arrays (`totals_by_skill`, `totals_by_custom_agent`, `totals_by_mcp`, `totals_by_slash_cmd`, `totals_by_plugin`) each list up to five items with the most recorded activity, with each entry carrying an `interaction_count` whose meaning varies by category

- **Evidence**: "What's new" section, "Which items are used most?" subsection.
- **Confidence**: settled (definitional, from official changelog)
- **Quote**: "The totals_by_skill, totals_by_custom_agent, totals_by_mcp, totals_by_slash_cmd, and totals_by_plugin arrays list up to five items with the most recorded activity. Each entry includes an interaction_count. Depending on the category, this counts invocations for skills, slash commands, and plugin skills, plus custom agent starts and MCP server connection attempts."
- **Our assessment**: The "depending on the category" caveat means
  `interaction_count` is not one uniform unit of activity across the five
  arrays — it is invocations for skills/slash-commands/plugins, but starts
  for custom agents and connection attempts for MCP. A dashboard that sums
  `interaction_count` across all five array types to get a single
  "customization activity" number would be summing structurally different
  events, echoing the corpus's existing "do not sum fields that look alike
  but measure different things" pattern from the agent-app note's nested-
  vs-top-level `user_initiated_interaction_count` collision (Claim 4 there).
  Here the collision risk is more subtle: it's not a name collision between
  two fields, but a unit-of-measurement inconsistency across five
  same-shaped array types.

### Claim 4: Five `distinct_*_use_count` fields count the number of different items used, with per-user semantics ("each item that user used counts once") differing from aggregate semantics ("each item used by anyone... counts once, not once per user")

- **Evidence**: "What's new" section, "How many different items were used?"
  subsection.
- **Confidence**: settled (explicit definitional and per-user/aggregate
  disambiguation from official changelog)
- **Quote**: "The distinct_skill_use_count, distinct_custom_agent_use_count, distinct_mcp_use_count, distinct_slash_cmd_use_count, and distinct_plugin_use_count fields count the number of different items used. In a per-user report, each item that user used counts once. In an aggregate report, each item used by anyone in the enterprise or organization counts once, not once per user."
- **Our assessment**: This is a meaningful pitfall the changelog proactively
  disambiguates: an aggregate `distinct_skill_use_count` of, say, 12 does
  not mean "12 skill-uses happened" or "the sum of each user's distinct
  count" — it means 12 unique skill identifiers were used by *anyone* in
  scope, however many users used each one. The conceptual reference page
  states this even more explicitly: "Aggregated distinct counts are not
  sums of per-user distinct counts" — a caveat absent from the changelog's
  own text (see Extraction Notes). Anyone building a rollup that adds
  per-user distinct counts to approximate an org-wide total would get a
  meaningless, inflated number.

### Claim 5: These counts include items outside the top-five array, so comparing distinct-use counts over time shows whether the variety of items in use is growing — independent of what the top-five array shows

- **Evidence**: "What's new" section, final sentence of the "How many
  different items were used?" subsection.
- **Confidence**: settled (explicit statement from official changelog)
- **Quote**: "These counts include items outside the top five, and comparing them over time shows whether the variety of items in use is growing."
- **Our assessment**: This decouples the two field types' purposes: the
  `totals_by_*` arrays answer "what's popular" (capped at five, ranked),
  while `distinct_*_use_count` answers "how much breadth is there" (
  uncapped cardinality). An organization could have a stable top-five array
  (same five skills dominate) while `distinct_skill_use_count` climbs
  steadily — meaning long-tail experimentation is growing even though the
  "most used" ranking looks static. Neither field alone gives the full
  adoption picture; the guide should present them as a pair.

### Claim 6: The stated purpose is to let enterprise and organization administrators identify which Copilot CLI customizations are gaining traction, find enablement gaps, and focus investment on automations developers find valuable

- **Evidence**: "Why this matters" section, full text.
- **Confidence**: anecdotal (vendor framing of intended use case; no
  adoption data, case study, or before/after example is cited to
  demonstrate administrators actually acting on this data)
- **Quote**: "Enterprise and organization administrators are now able to identify which Copilot CLI customizations are gaining traction, find enablement gaps, and focus investment on automations that developers find valuable."
- **Our assessment**: This is the identical "ground decisions in real usage
  data" framing pattern the corpus already flagged as anecdotal for the
  August 7, 2026 agent-app note (Claim 9 there: "ground rollout and
  licensing decisions in real usage rather than assumption") and the July
  28, 2026 Copilot app note. GitHub is applying the same rhetorical
  template — "here's data you didn't have before; use it to make better
  investment decisions" — across successive metrics-API expansions, without
  independent evidence that customers change behavior as a result. The
  data-availability half of the claim is verifiable (Claims 1-5 above); the
  behavioral half ("focus investment") is not demonstrated by this source.

### Claim 7: Only names for "recognized GitHub-provided items" are shown; customer-defined names are withheld for privacy, with skills/custom agents/MCP servers/plugins grouped under `other` and slash commands grouped under `custom`

- **Evidence**: "Important notes" section, first bullet.
- **Confidence**: settled (explicit privacy/grouping rule from official
  changelog, corroborated by the conceptual reference page)
- **Quote**: "Names for recognized GitHub-provided items are shown. To protect privacy, customer-defined names are not shown. Skills, custom agents, MCP servers, and plugins are grouped under other. Copilot CLI telemetry already groups customer-defined slash commands under custom, so reports use that label for slash commands."
- **Our assessment**: This is a deliberate privacy boundary, not a data gap:
  GitHub can technically observe customer-defined skill/agent/server/plugin
  names (they must be, to count invocations) but chooses not to expose them
  in the API, collapsing them into an `other` bucket instead. The practical
  effect for an organization heavy on custom (non-GitHub-provided)
  customizations: their `totals_by_skill` top-five array may show mostly or
  entirely `other` entries with high combined interaction counts but no way
  to distinguish which specific custom skill drove that count from the API
  alone — an organization would need its own internal telemetry to get
  per-custom-skill granularity. The conceptual reference page adds a related
  detail absent from the changelog: items "identified only by
  customer-specific hashes" are what get grouped under `other`, and "each
  hidden identifier still contributes separately to the corresponding
  distinct count" — so the `other` bucket's interaction count may represent
  many distinct customer skills, and the distinct-count field (not the
  array) is where that cardinality remains visible.

### Claim 8: For MCP servers, `interaction_count` increases only on connection or reconnection attempts (successful or failed), not on individual tool calls within an already-connected session

- **Evidence**: "Important notes" section, second bullet.
- **Confidence**: settled (explicit counting-boundary rule from official
  changelog)
- **Quote**: "For MCP servers, interaction_count increases only when Copilot CLI attempts to connect or reconnect to the server. Successful and failed attempts both count. Calling tools from the same connected server multiple times does not increase the count."
- **Our assessment**: This is an important unit-of-measurement caveat for
  anyone trying to gauge MCP server *usage intensity* from this field: a
  developer who connects once to an MCP server and then calls its tools 200
  times in a session contributes the same `interaction_count` of 1 as a
  developer who connects once and calls a tool once. The field measures
  connection reliability/frequency, not tool-call volume — a materially
  different signal than what "MCP usage" might intuitively suggest. This
  connects to, but is a distinct counting rule from, the enterprise MCP
  governance surface documented in `docs-github-copilot-mcp-allowlists-enterprise.md`
  (which controls *whether* a server can run at all, not how its usage is
  measured); together the two notes show GitHub has now built both a
  governance control point and an adoption-measurement point for MCP
  servers in Copilot CLI, but the measurement point does not reveal
  tool-call-level activity.

### Claim 9: Plugin metrics count only skill invocations associated with a plugin; because plugin totals are a strict subset of skill totals, the two must not be added together

- **Evidence**: "Important notes" section, third bullet.
- **Confidence**: settled (explicit subset/non-additive warning from
  official changelog, corroborated by the conceptual reference page's
  identical "Do not add plugin and skill interaction counts together" line)
- **Quote**: "Plugin metrics count only skill invocations associated with a plugin. Every plugin interaction therefore also appears in the skill totals, but skill interactions that do not come from a plugin appear only in the skill totals. Because the plugin totals are a subset of the skill totals, you should not add the two together."
- **Our assessment**: This is the same category of pitfall the corpus
  already documented for the agent-app note's nested-vs-top-level
  `user_initiated_interaction_count` (a "do not sum these two same-shaped
  fields" warning), but with a different underlying relationship: there it
  was two fields counting different event types that happen to share a
  name; here it is two fields in a strict superset/subset relationship that
  happen to look like independent peer categories (both are `totals_by_*`
  arrays with the same shape). GitHub is proactively warning against a
  double-counting mistake that would be easy to make precisely because
  `totals_by_skill` and `totals_by_plugin` are structurally identical
  arrays sitting side by side in the same response — nothing in the shape
  of the data itself signals the subset relationship. This makes sense
  given the corpus's existing note on Agent Plugins 1.0
  (`docs-github-copilot-agent-plugins-1-0.md`), which documents that
  plugins package agent skills and MCP servers together — the metrics
  subset relationship is a direct consequence of that packaging model.

### Claim 10: Empty arrays and zero counts indicate no matching activity, while the fields are null or absent when customization data is unavailable — the two states (no activity vs. no data) are distinct

- **Evidence**: "Important notes" section, fourth bullet.
- **Confidence**: settled (explicit null-vs-zero semantics from official
  changelog)
- **Quote**: "Empty arrays and zero counts indicate no matching activity. The fields are null or absent when customization data is unavailable."
- **Our assessment**: This distinction matters for any pipeline that treats
  "null" and "zero" as interchangeable "nothing happened" signals. Here,
  zero/empty means GitHub positively observed no activity; null/absent
  means GitHub cannot say either way (e.g., during rollout, per the
  conceptual reference page: "The fields can be null or absent when
  Copilot CLI customization data isn't available during rollout"). A
  dashboard defaulting nulls to zero would silently misreport "confirmed
  zero customization usage" for users or periods where the data was simply
  not yet being collected — a distinction the corpus has not previously
  seen stated this explicitly for a Copilot metrics field.

### Claim 11: Access requires enterprise owner or billing manager status, organization owner status, or a custom organization/enterprise role granting the "View Copilot Metrics" permission, with the Copilot usage metrics policy enabled

- **Evidence**: "Important notes" section, fifth bullet.
- **Confidence**: settled (stated access tier from official changelog)
- **Quote**: "Reports are available to enterprise owners and billing managers, organization owners, and anyone with a custom organization or enterprise role that grants the View Copilot Metrics permission. The Copilot usage metrics policy must be enabled."
- **Our assessment**: This is, again, character-for-character consistent
  with the access-tier language documented in
  `docs-github-copilot-usage-metrics-agent-app-activity.md` Claim 7 (August
  7, 2026) and `docs-github-copilot-app-usage-metrics-report-rollups.md`
  (July 28, 2026) — now a third independently confirmed instance of GitHub
  reusing an identical access-control sentence across metrics-API
  expansions roughly six weeks apart each time. This further confirms the
  corpus's standing observation that the Copilot usage metrics API has one
  stable, uniformly applied permission model rather than per-surface
  permission variants.

## Concrete Artifacts

### Verbatim Changelog Body Text (September 17, 2026, retrieved via direct HTTP fetch of the raw article HTML on 2026-09-18)

```
Agentic CLI customizations now in the usage metrics API
Improvement | September 17, 2026 • 2 minute read

GitHub Copilot expands existing CLI report coverage with agentic activity
metrics for skills, custom agents, Model Context Protocol (MCP) servers,
slash commands, and plugins.

What's new
The fields appear in enterprise and organization per-user and aggregate
1-day reports, per-user 28-day reports, and the day_totals entries in
aggregate 28-day reports.

In a per-user report, the fields answer two questions about that user's
activity. In an aggregate report, they answer the same questions across
the enterprise or organization:

Which items are used most? The totals_by_skill, totals_by_custom_agent,
totals_by_mcp, totals_by_slash_cmd, and totals_by_plugin arrays list up to
five items with the most recorded activity. Each entry includes an
interaction_count. Depending on the category, this counts invocations for
skills, slash commands, and plugin skills, plus custom agent starts and
MCP server connection attempts.

How many different items were used? The distinct_skill_use_count,
distinct_custom_agent_use_count, distinct_mcp_use_count,
distinct_slash_cmd_use_count, and distinct_plugin_use_count fields count
the number of different items used. In a per-user report, each item that
user used counts once. In an aggregate report, each item used by anyone in
the enterprise or organization counts once, not once per user. These
counts include items outside the top five, and comparing them over time
shows whether the variety of items in use is growing.

Why this matters
Enterprise and organization administrators are now able to identify which
Copilot CLI customizations are gaining traction, find enablement gaps, and
focus investment on automations that developers find valuable.

Important notes
Names for recognized GitHub-provided items are shown. To protect privacy,
customer-defined names are not shown. Skills, custom agents, MCP servers,
and plugins are grouped under other. Copilot CLI telemetry already groups
customer-defined slash commands under custom, so reports use that label
for slash commands.

For MCP servers, interaction_count increases only when Copilot CLI
attempts to connect or reconnect to the server. Successful and failed
attempts both count. Calling tools from the same connected server multiple
times does not increase the count.

Plugin metrics count only skill invocations associated with a plugin.
Every plugin interaction therefore also appears in the skill totals, but
skill interactions that do not come from a plugin appear only in the skill
totals. Because the plugin totals are a subset of the skill totals, you
should not add the two together.

Empty arrays and zero counts indicate no matching activity. The fields are
null or absent when customization data is unavailable.

Reports are available to enterprise owners and billing managers,
organization owners, and anyone with a custom organization or enterprise
role that grants the View Copilot Metrics permission. The Copilot usage
metrics policy must be enabled.

Visit the Copilot usage metrics API documentation to get started.
```

*Source: https://github.blog/changelog/2026-09-17-agentic-cli-customizations-now-in-the-usage-metrics-api,
retrieved via direct HTTP fetch of the raw `<article>` element on
2026-09-18. Every quote in this note is taken from this raw-HTML
extraction.*

### Copilot CLI Customization Fields Reference (compiled from the linked conceptual docs page, `docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics`, section "Copilot CLI customization fields (API only)", fetched 2026-09-18)

```
# Copilot usage metrics API — Copilot CLI customization fields
# (as documented on the conceptual reference page, current as of 2026-09-18;
#  NOT present on the separate REST API reference page as of the same date
#  — see Extraction Notes)

Report scope (per conceptual reference page, corroborating changelog Claim 2):
  - Per-user 1-day and 28-day reports
  - Aggregated 1-day reports
  - Each day_totals record in aggregated 28-day reports

Array            | Name field    | interaction_count measures          | Distinct-count field
-----------------|---------------|--------------------------------------|---------------------------------
totals_by_skill[]        | skill         | Skill invocations.                          | distinct_skill_use_count
totals_by_custom_agent[] | custom_agent  | Custom agent starts.                        | distinct_custom_agent_use_count
totals_by_mcp[]          | mcp           | Successful/failed MCP connect or reconnect  | distinct_mcp_use_count
                 |               | attempts. Tool calls through an already     |
                 |               | connected server do not increase this count.|
totals_by_slash_cmd[]    | slash_cmd     | Slash command invocations.                  | distinct_slash_cmd_use_count
totals_by_plugin[]       | plugin        | Skill invocations associated with a plugin. | distinct_plugin_use_count
                 |               | Plugin interactions are a subset of skill   |
                 |               | interactions. Do not add plugin and skill   |
                 |               | interaction counts together.

Caveats stated on the conceptual reference page but NOT in the changelog text:
  - "An entry's absence from an array does not mean that it had zero usage.
     Do not use these arrays to calculate exact adoption."
  - "Aggregated distinct counts are not sums of per-user distinct counts."
  - "Distinct counts retain the full identifier cardinality, including items
     outside the top-five array. When customer-defined artifacts are grouped
     under other, each hidden identifier still contributes separately to the
     corresponding distinct count."
  - "The fields can be null or absent when Copilot CLI customization data
     isn't available during rollout."
```

*Compiled from the conceptual docs page's "Copilot CLI customization fields
(API only)" subsection, fetched directly via HTTP on 2026-09-18 (~1.07MB
raw HTML; the field table was located via full-text search for
`totals_by_skill`, `totals_by_mcp`, and `totals_by_plugin` in the raw HTML
and is reproduced above with attribution).*

## Cross-References

- **Extends** `docs-github-copilot-cli-activity-usage-metrics.md` (April
  10, 2026 — CLI activity integrated into top-level usage metrics totals
  and the `feature=copilot_cli` breakdown dimension): That note established
  CLI as a peer *surface* to IDE in aggregate fields and named feature
  breakdowns. This note goes one level deeper: a breakdown *within* the CLI
  surface, by customization type (skill, custom agent, MCP, slash command,
  plugin). The April 10 note's `docs-github-copilot-cli-activity-usage-metrics.md`
  Concrete Artifacts table of "Known Methodology Inflection Points in the
  Copilot Usage Metrics Time Series" should be extended with a third entry:
  September 17, 2026 — Copilot CLI customization metrics added (this note),
  though unlike the April 10 and June 15 inflections, this one adds wholly
  new fields rather than changing the meaning of pre-existing ones, so it
  does not itself cause a step-discontinuity in any previously-reported
  field.

- **Corroborates** `docs-github-copilot-usage-metrics-agent-app-activity.md`
  (August 7, 2026 — `totals_by_3rd_party_agent` per-agent breakdown): Both
  notes document GitHub adding a *within-surface* breakdown (per distinct
  item, capped top-N array plus a distinct-count field) rather than a new
  top-level surface dimension — the architectural pattern flagged as "novel"
  in that note's Claim/Novel section ("First per-agent... breakdown... This
  is the first to add a breakdown within a surface"). This September 17
  note is now a second, independent instance of the same within-surface
  breakdown pattern, applied to five customization types instead of one
  agent dimension. Both notes also share the identical access-tier sentence
  (this note's Claim 11; that note's Claim 7) and a "do not sum/add these
  two fields" proactive warning (this note's Claim 9 for plugin/skill; that
  note's Claim 4 for nested/top-level `user_initiated_interaction_count`) —
  confirming GitHub's templated approach to warning about metric
  double-counting pitfalls recurs across unrelated metrics surfaces.

- **Corroborates** `docs-github-copilot-mcp-allowlists-enterprise.md`
  (August 6, 2026 — `allowedMcpServers`/`deniedMcpServers` enterprise
  managed-settings keys): That note documents the governance control point
  for MCP servers in Copilot clients (whether a server may run at all).
  This note's Claim 8 (`totals_by_mcp` counts connection/reconnection
  attempts, not tool calls) documents the corresponding measurement point.
  Together they show GitHub built both halves of MCP server management for
  Copilot CLI — control and observability — within about six weeks of each
  other, but the observability half is coarser-grained (connection-level,
  not tool-call-level) than the governance half (which can allow/deny at
  the server level but does not gate individual tool calls either).

- **Corroborates** `docs-github-copilot-agent-plugins-1-0.md` (August 12,
  2026 — Agent Plugins 1.0 packages skills and MCP servers into one
  installable plugin unit): This note's Claim 9 (plugin totals are a strict
  subset of skill totals because "plugin metrics count only skill
  invocations associated with a plugin") is a direct metrics-level
  consequence of that packaging model — a plugin's skill invocations are
  visible from two angles (the plugin's own total and the broader skill
  total) precisely because Agent Plugins 1.0 defines a plugin as bundling
  skills (and MCP servers) rather than being a wholly separate primitive.

- **Extends** `docs-github-copilot-agent-skills-cli.md` (April 16, 2026 —
  `gh skill` CLI package manager for agent skills, with supply-chain
  integrity primitives and a prompt-injection warning for unverified
  skills): That note documents how skills are installed and verified; this
  note documents how skill *usage* is subsequently measured
  (`totals_by_skill`, `distinct_skill_use_count`). An organization
  following that note's supply-chain-integrity guidance (verifying skill
  provenance before installation) can now pair it with this note's
  usage-metrics fields to also monitor which verified skills actually see
  adoption after rollout — though per this note's Claim 7, if a skill is
  customer-defined (as opposed to a "recognized GitHub-provided" skill),
  its specific identity is masked behind the `other` bucket in the
  `totals_by_skill` array, even though its usage still contributes to
  `distinct_skill_use_count`.

- **Contradicts**: None identified. No existing source note claims that
  CLI customization activity (skills, custom agents, MCP servers, slash
  commands, plugins) cannot or should not be measured per-item, or that a
  single undifferentiated CLI activity count was sufficient. No
  contradiction issue filed.

- **Novel**:
  - **First per-customization-type breakdown for Copilot CLI specifically**:
    Prior CLI-related notes in the corpus (`docs-github-copilot-cli-activity-usage-metrics.md`,
    `docs-github-copilot-cli-auto-model-selection.md`,
    `docs-github-copilot-cli-settings-command.md`) address CLI as a whole
    surface, model-selection behavior, or settings — none document
    per-skill, per-agent, per-MCP-server, per-slash-command, or per-plugin
    breakdowns of CLI activity. This is the first.
  - **Explicit array-vs-distinct-count dual-metric design for adoption
    breadth vs. concentration**: No prior corpus note documents GitHub
    pairing a capped top-N "most popular" array with an uncapped
    "how many distinct items" counter as a deliberate two-part measurement
    design, with an explicit statement that the two answer different
    questions (concentration vs. breadth).
  - **"Absence from the array does not mean zero usage" caveat**: The
    conceptual reference page's explicit warning against inferring
    non-adoption from an item's absence from a top-five array is new to the
    corpus — a distinct pitfall from the null-vs-zero distinction (Claim 10)
    already stated in the changelog itself.
  - **Aggregated distinct counts are not sums of per-user distinct counts**:
    This non-additivity rule for `distinct_*_use_count` fields, stated only
    on the conceptual reference page and not the changelog, is a new
    documented pitfall category — not a name collision or subset
    relationship like the corpus's prior "do not sum" warnings, but a
    fundamentally non-additive aggregation (set cardinality across users,
    not a per-user sum).

## Guide Impact

- **Chapter 05 (Measurement) — "Metrics granularity hierarchy" / multi-surface
  adoption section**: Add Copilot CLI customization metrics
  (`totals_by_skill`, `totals_by_custom_agent`, `totals_by_mcp`,
  `totals_by_slash_cmd`, `totals_by_plugin` plus their `distinct_*_use_count`
  companions) as a third documented instance of GitHub's within-surface
  breakdown pattern (alongside the August 7, 2026 per-agent breakdown).
  Note the report-type scoping is more restrictive than other metrics
  surfaces in the corpus: no direct field on rolled-up 28-day aggregate
  reports, only per-user 28-day and the `day_totals` entries within
  aggregate 28-day reports.
- **Chapter 05 — "Adoption metric completeness caveats"** (extend the
  existing subsection on `totals_by_3rd_party_agent` silent omission from
  the August 7, 2026 note): Add the parallel but distinct caveat here — an
  item's absence from a `totals_by_*` top-five array does not mean zero
  usage (per the conceptual reference page), and aggregated distinct counts
  are not sums of per-user distinct counts. Both caveats mean these fields
  should be presented to stakeholders with explicit interpretation guidance,
  not as raw self-explanatory numbers.
- **Chapter 05 — "Metrics field-name collisions" / non-additive fields**
  (extend the existing subsection from the August 7, 2026 note): Add two
  new instances: (1) `interaction_count` means a different underlying event
  per array type (invocations vs. starts vs. connection attempts) — do not
  sum across the five `totals_by_*` arrays as if it were one unit; (2)
  `totals_by_plugin` is a documented strict subset of `totals_by_skill` —
  do not add plugin and skill interaction counts together.
- **Chapter 04 (Observability) — "Enterprise Copilot observability
  pipeline"**: Note that per-item CLI customization visibility exists only
  for "recognized GitHub-provided" names; customer-defined skills, custom
  agents, MCP servers, and plugins are anonymized into an `other` bucket
  (slash commands into `custom`) for privacy, even though their activity
  still counts toward the corresponding distinct-count field. Organizations
  relying heavily on custom, in-house CLI customizations will not be able
  to identify *which* custom item drove usage from this API alone.
- **Chapter 02 (Harness Engineering)**: For teams building or governing MCP
  server access for Copilot CLI (per `docs-github-copilot-mcp-allowlists-enterprise.md`),
  note that the new `totals_by_mcp`/`distinct_mcp_use_count` fields measure
  connection/reconnection attempts only, not tool-call volume — insufficient
  on its own to gauge how intensively a given MCP server is actually used
  once connected. Pair with the enterprise MCP allowlist's own audit
  surface, if any, for tool-call-level insight.

## Extraction Notes

1. **Direct HTTP fetch used for verbatim quotes, not WebFetch**: The
   changelog page was fetched via direct HTTP request (`curl` with a
   browser user agent, no redirect needed) and the raw `<article>` element
   extracted with a Python HTML-stripping script. Every quote in this note
   is taken from that raw-HTML extraction, so none carries the "verify
   against live source" caveat some earlier notes in this corpus required
   when only a WebFetch-summarized version was available.
2. **One substantive sub-page followed**: The changelog's only content link
   ("Copilot usage metrics API documentation") resolves to
   `docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics`.
   That specific REST API reference page was fetched directly via HTTP
   (~530KB) and searched for all ten new field names
   (`totals_by_skill`, `totals_by_custom_agent`, `totals_by_mcp`,
   `totals_by_slash_cmd`, `totals_by_plugin`, and their five
   `distinct_*_use_count` counterparts) — zero matches, confirming the same
   documentation-lag pattern the corpus already documented twice (the July
   28, 2026 Copilot app fields and the August 7, 2026 agent-app fields, per
   `docs-github-copilot-usage-metrics-agent-app-activity.md` Extraction
   Notes item 2). This is now a third independently confirmed instance,
   about six weeks after the second, suggesting the REST API reference
   page's lag behind the conceptual reference page and changelog is a
   structural, recurring characteristic of GitHub's docs publishing
   pipeline for this API rather than a one-off gap.
3. **Separate conceptual reference page followed instead, and found to
   contain the fields**: Since the REST API reference page lacked the
   fields, the separate conceptual reference page
   (`docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics`,
   ~1.07MB) was fetched directly via HTTP and searched — this page *did*
   contain a "Copilot CLI customization fields (API only)" subsection with
   full field type/nullable tables and the additional caveats reproduced in
   Concrete Artifacts above. This mirrors the same two-tier documentation
   pattern (conceptual page ahead of REST reference page) already confirmed
   for the August 7, 2026 agent-app fields.
4. **One related sibling changelog noted but not fetched or mined**: The
   September 17, 2026 changelog page's navigation lists an adjacent entry,
   "Add VS Code agents to Copilot usage metrics" (dated September 11, 2026,
   same changelog feed), which by title appears to be a related metrics
   expansion for a different agentic surface (VS Code agents rather than
   CLI customizations). It was not fetched or read for this note — no claim
   here depends on it — but it is flagged as a candidate for a separate
   mining pass, since it may share the within-surface-breakdown pattern
   documented here and in the August 7, 2026 agent-app note.
5. **No contradictions to file**: No existing source note claims that
   Copilot CLI customization activity cannot or should not be broken out by
   type, or that a single undifferentiated CLI metric was adequate. No
   contradiction issue filed.
6. **Source is a short product changelog (~200 words)**: All eleven claims
   above are drawn from all three named sections of the changelog ("What's
   new," "Why this matters," "Important notes") plus the introductory
   sentence, supplemented by the linked conceptual reference page (the
   field-type table and the two additional caveats not in the changelog
   text). No additional signal would come from re-reading the changelog
   itself.
7. **Triage questions addressed**: The Prospector's two triage comments
   asked (a) what new metrics fields are exposed for agentic CLI
   customizations, how they enable observability, and their implications
   for monitoring; and (b) how the fields differ across report types
   (per-user vs. aggregate) and what adoption/observability patterns they
   enable. Answers: (a) ten new fields — five capped top-five "most used"
   arrays and five uncapped distinct-item counters, covering skills, custom
   agents, MCP servers, slash commands, and plugins (Claims 1-5); they
   enable "what's popular" and "how much variety" analysis but require care
   around non-additive distinct counts, array-absence-is-not-zero, and
   type-specific `interaction_count` semantics (Claims 3, 4, 5 and Novel
   section). (b) Per-user reports show that user's own top-five/distinct
   values; aggregate reports show enterprise/organization-wide values with
   distinct counts computed as an aggregate set (not summed from per-user
   counts) — and the fields are scoped more narrowly than other metrics
   surfaces (no plain 28-day aggregate field, only `day_totals` entries
   within it) (Claim 2).
