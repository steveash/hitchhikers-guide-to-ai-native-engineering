---
source_url: https://vercel.com/changelog/query-web-analytics-from-the-vercel-cli
source_type: blog-post
title: "Query Web Analytics from the Vercel CLI"
author: Damien Simonin Feugas, Ergün Erdoğmuş (Vercel)
date_published: 2026-06-26
date_extracted: 2026-07-26
last_checked: 2026-07-26
status: current
confidence_overall: settled
issue: "#2246"
---

# Query Web Analytics from the Vercel CLI

> Vercel's `vercel metrics` CLI command now queries Web Analytics data (page
> views, visitors, custom events) directly from the terminal, explicitly
> framed as enabling "a coding agent access to the CLI" to answer traffic and
> conversion questions, with a `--format json` output mode built specifically
> for "scripts, agents, and continuous integration checks."

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  short (~120-word) feature announcement). Per MINER.md §1, this note follows
  the two substantive pages the changelog entry points to: the linked docs
  page `/docs/analytics/accessing-metrics-with-vercel-cli` (which the
  changelog explicitly directs readers to for "a complete list of supported
  metrics, dimensions, filters, and query options") and that docs page's own
  `related` link, the `vercel metrics` CLI reference at `/docs/cli/metrics`
  (needed for the full flag-by-flag semantics referenced but not spelled out
  on the how-to page). No other linked pages were substantive enough to
  follow — the how-to page's other `related`/`prerequisites` links
  (`/docs/analytics`, `/docs/observability/observability-plus`) are general
  product-overview pages not specific to the CLI feature itself.
- **Author credibility**: First-party Vercel changelog entry, credited to two
  named individuals (Damien Simonin Feugas, Ergün Erdoğmuş). The changelog
  itself is a brief feature announcement; the substantive technical content
  (command syntax, flag semantics, query examples) comes from Vercel's own
  reference and how-to documentation pages, which are authoritative
  first-party descriptions of a shipping CLI feature — not third-party
  reporting, and not a marketing/customer-outcome narrative (no customer
  quotes, adoption figures, or benchmarks appear anywhere in the three pages
  read).
- **Scope**: Covers the `vercel metrics` CLI command as it applies to Web
  Analytics data specifically (page views, visitors, custom events, UTM
  dimensions, feature-flag dimensions) — schema discovery, dashboard-view
  recreation, and query shapes not available in the dashboard UI (multi-path
  filtering, custom event property queries, cross-project team-wide
  queries). Does **not** cover: pricing for Observability Plus (referenced
  but not detailed), the broader set of non-Web-Analytics metrics that
  require Observability Plus, any worked example of an agent actually
  invoking `vercel metrics` end-to-end (the changelog's "agent" framing is
  asserted, not demonstrated with a transcript or code sample), or any
  customer/production evidence that agents are using this feature as
  described.

## Extracted Claims

### Claim 1: The Vercel CLI can now query Web Analytics data points directly — page views, visitors, and custom events — for analyzing traffic, comparing trends, and answering site-performance questions
- **Evidence**: Direct feature description in the changelog's opening two sentences.
- **Confidence**: settled (first-party description of a shipping CLI command)
- **Quote**: "You can now query Web Analytics datapoints directly through the Vercel CLI. Using the `vercel metrics` command, you can pull page views, visitors, and custom events for your Vercel projects to analyze traffic, compare trends, and answer questions about site performance."
- **Our assessment**: This is the changelog's core announcement — Web Analytics data, previously accessible only through the dashboard UI, is now queryable as structured CLI output. This is the prerequisite fact the rest of the source's more interesting claims (agent access, JSON output, dashboard-exceeding query shapes) build on.

### Claim 2: Vercel explicitly frames this feature as enabling a coding agent to answer specific traffic and conversion questions by giving it CLI access, and gives three example questions as illustrations
- **Evidence**: A dedicated sentence in the changelog directly following the feature description, followed by a three-item bulleted list of example questions.
- **Confidence**: settled (first-party framing of the feature's intended use case, though asserted rather than demonstrated — no transcript or code sample shows an agent actually issuing these queries)
- **Quote**: "By providing a coding agent access to the CLI, an agent can answer questions such as: Which pages gained the most traffic this week? Which UTM campaigns drove the most signups this month? Compare conversion events between mobile and desktop users."
- **Our assessment**: This is the single most guide-relevant claim in the source: Vercel is explicitly positioning a data-querying CLI command as an agent-facing tool, not (or not only) a human-operator convenience. The three example questions span three distinct query shapes this note's Concrete Artifacts section documents concretely (time-series aggregation, `--group-by utm_campaign` plus a custom-event filter, and a two-way `--group-by device_type` comparison) — meaning the claim is checkable against the CLI's actual query surface, not just a marketing aspiration. No worked example of an agent invoking these queries is given anywhere in the three pages read, so this remains a stated intent, not demonstrated behavior.

### Claim 3: Web Analytics and Speed Insights metrics are queryable through `vercel metrics` without an Observability Plus subscription, while all other metrics require it
- **Evidence**: Stated identically on both the how-to page and the CLI reference page, as an explicit feature-access boundary.
- **Confidence**: settled (first-party, unambiguous entitlement statement, stated twice across two pages)
- **Quote**: "Web Analytics metrics are available through `vercel metrics` without Observability Plus." (how-to page) / "Speed Insights metrics are available through `vercel metrics` without Observability Plus." (CLI reference page)
- **Our assessment**: This is a concrete, checkable access-tier boundary rather than a vague "some metrics require upgrading" caveat — a team giving an agent CLI access for Web Analytics or Speed Insights queries specifically does not need to provision an additional paid entitlement, whereas broader observability metrics (traces, logs, custom application metrics) do. This matters for anyone evaluating "how cheaply can I let an agent query production telemetry" as a design question.

### Claim 4: `vercel metrics schema` is presented as the mandatory first step before building any query — the schema is "the source of truth" for which metrics, dimensions, and aggregations exist for the account, and can be scoped to a metric or prefix
- **Evidence**: Stated as the opening instruction on both the how-to page ("Start by inspecting the available Web Analytics metrics") and the CLI reference page, each followed by worked `vercel metrics schema` examples.
- **Confidence**: settled (first-party documented workflow recommendation with runnable command examples)
- **Quote**: "The schema is the source of truth for the metrics, dimensions, and aggregations available to your account. Start by inspecting the available Web Analytics metrics" / "Use the schema before you build a query. The metrics schema is the source of truth for the metrics, dimensions, and aggregations available to your account."
- **Our assessment**: This is a discover-then-query pattern that matters specifically for agent tool design: rather than an agent needing hard-coded knowledge of valid metric IDs, dimensions, and aggregations, it can call `vercel metrics schema` (or `vercel metrics schema <metric-or-prefix>`, narrowed) at the start of a session to ground its subsequent queries in what's actually queryable for that account — a self-describing API surface an agent can introspect rather than one it must have pre-trained knowledge of.

### Claim 5: The `--format` option outputs structured JSON instead of the default human-readable table/time-series summary, and the CLI reference page states this exists specifically for automation and agent use
- **Evidence**: A dedicated "Format" subsection on the CLI reference page, plus a matching statement under "Query output" and a repeated recommendation under "Schema subcommand."
- **Confidence**: settled (first-party, explicit statement of the option's intended purpose)
- **Quote**: "By default, `vercel metrics` prints a human-readable table or time series summary. Use `--format` to output structured JSON for scripts, agents, and continuous integration checks." / "The `--format` option outputs JSON instead of text. Use it for automation and agents." / "Use `--format` when you are building scripts or agent workflows that need to validate available fields before querying."
- **Our assessment**: This is the second explicit agent-facing design signal in the source (alongside Claim 2), and a more mechanically specific one — Vercel names "agents" as a distinct consumer category from "scripts" and "CI checks" three separate times across the CLI reference page, and ties `--format json` directly to the schema-discovery workflow of Claim 4 ("validate available fields before querying"). This is a concrete instance of a vendor designing a CLI's *output format*, not just its existence, around agent consumption as a first-class use case — distinct from simply having a `--json` flag that happens to be usable by scripts.

### Claim 6: The CLI supports query shapes explicitly documented as unavailable in the Web Analytics dashboard UI — multi-path-prefix filtering combined with exclusion filters, custom event property filtering/grouping, UTM-dimension grouping combined with feature-flag grouping, and team-wide cross-project queries
- **Evidence**: A dedicated "Query capabilities beyond the dashboard" section on the how-to page with four worked examples, each with explanatory prose distinguishing it from dashboard capability.
- **Confidence**: settled (first-party documented capability with four distinct worked command examples)
- **Quote**: "The following query shapes are not available in the Web Analytics dashboard. Use them when you need more precise filtering, multi-dimensional comparisons, custom event analysis, or team-wide reporting."
- **Our assessment**: This is a specific, checkable claim about the CLI being a strictly richer query surface than the dashboard, not merely a terminal-based re-presentation of the same dashboard views. The four named examples (path-prefix `startswith()` filtering combined with `ne` exclusion and dual `--group-by`; `event_data/plan`-style nested custom-event-property filtering and grouping; combined `utm_source` + `utm_campaign` + `flags/new_checkout` grouping for experiment/campaign analysis; `--all --group-by project_id` for team-wide comparison) map directly onto real analytical needs (funnel/segment analysis, custom conversion tracking, campaign-vs-feature-flag interaction, cross-project comparison) that a dashboard UI's fixed set of views typically cannot express.

### Claim 7: Bounce Rate is explicitly excluded from `vercel metrics` and remains dashboard-only
- **Evidence**: A callout note on the how-to page, placed immediately after the "Recreate dashboard views" examples.
- **Confidence**: settled (first-party, explicitly stated limitation)
- **Quote**: "Bounce Rate is not available through `vercel metrics`; use the Web Analytics dashboard to view Bounce Rate."
- **Our assessment**: This is a self-disclosed gap in an otherwise "CLI exceeds the dashboard" narrative (Claim 6) — worth preserving because it means "give an agent the CLI and it can answer any Web Analytics question the dashboard can" is not quite true; Bounce Rate specifically requires a human to check the dashboard directly, which is a concrete boundary an agent-facing integration built on this CLI needs to know about rather than assume away.

### Claim 8: `--prod` is documented as pure syntactic sugar — it is defined as exactly equivalent to a specific `--filter` expression, not a separate mechanism
- **Evidence**: The CLI reference page's "Production environment" subsection defines the flag by direct equivalence to a filter clause.
- **Confidence**: settled (first-party, unambiguous equivalence statement)
- **Quote**: "The `--prod` option limits the query to production data. It is equivalent to `--filter \"environment eq 'production'\"`."
- **Our assessment**: A small but architecturally clean detail: convenience flags in this query language are defined as sugar over the same underlying filter grammar rather than a parallel special-cased code path, meaning every dashboard-recreation example in Claim 6's "beyond the dashboard" examples (which all combine `--prod` with `--filter`) is actually composing the same primitive twice, not mixing two different querying mechanisms.

### Claim 9: The documentation explicitly frames the dashboard and CLI as complementary rather than competing views — dashboards for curated, pre-built views; the CLI for custom filtering, grouping, aggregations, calendar-timezone bucketing, JSON output, and agent workflows
- **Evidence**: A dedicated "Feature access" section on the CLI reference page enumerating the division of labor in three bullet points.
- **Confidence**: settled (first-party product-positioning statement)
- **Quote**: "The dashboard and CLI are complementary: Use product dashboards for curated views. Use `vercel metrics` for custom filtering, grouping, aggregations, calendar buckets, JSON output, and agent workflows. Use `--all` to query across every project in the current team when you need team-wide comparisons."
- **Our assessment**: This is Vercel's own explicit statement of intended division of labor, and it names "agent workflows" as one of three CLI-specific use cases (alongside custom filtering/grouping and team-wide queries) in the same breath as the more mundane "calendar buckets" and "JSON output" — reinforcing that this is a deliberate design category for the vendor, not an incidental side effect of having a CLI that happens to be scriptable.

## Concrete Artifacts

### Schema discovery commands (verbatim, from `/docs/cli/metrics` and `/docs/analytics/accessing-metrics-with-vercel-cli`)

```bash
# List queryable metrics for the current team context
vercel metrics schema

# Inspect a metric or metric prefix
vercel metrics schema <metric-or-prefix>
vercel metrics schema vercel.analytics_pageview
vercel metrics schema vercel.analytics_event
```

### Dashboard-view recreation examples (verbatim, from `/docs/analytics/accessing-metrics-with-vercel-cli`)

```bash
# Daily page views for the last seven days
vercel metrics vercel.analytics_pageview.count --since 7d --granularity 1d --project project-name --prod

# Top countries by page views
vercel metrics vercel.analytics_pageview.count --group-by country --since 7d --limit 10 --project project-name --prod

# Unique visitors from a specific country over the last day
vercel metrics vercel.analytics_pageview.count --aggregation unique/visitor_id --filter "country eq 'US'" --since 1d --granularity 1h --project project-name --prod

# Most common custom event names
vercel metrics vercel.analytics_event.count --group-by event_name --since 7d --limit 20 --project project-name --prod
```

### Query shapes not available in the dashboard (verbatim, from `/docs/analytics/accessing-metrics-with-vercel-cli`)

```bash
# Filter multiple path prefixes, exclude a country, group by path and device type
vercel metrics vercel.analytics_pageview.count --filter "startswith(request_path, '/docs') or startswith(request_path, '/guides')" --filter "country ne 'US'" --group-by request_path --group-by device_type --since 7d --project project-name --prod

# Filter and group by custom event properties
vercel metrics vercel.analytics_event.count --filter "event_name eq 'signup'" --filter "event_data/plan eq 'pro'" --group-by event_data/source --since 7d --project project-name --prod

# Group by UTM dimensions and a feature flag
vercel metrics vercel.analytics_pageview.count --group-by utm_source --group-by utm_campaign --group-by flags/new_checkout --since 7d --project project-name --prod

# Query every project in the team
vercel metrics vercel.analytics_pageview.count --all --group-by project_id --group-by country --since 7d --limit 20 --prod
```

### Full flag reference (verbatim, condensed from `/docs/cli/metrics`)

```
<metric-id>            positional; run `vercel metrics schema` to list valid IDs
schema [prefix]         discover metrics/dimensions/aggregations available to the account
-a, --aggregation       selects the aggregation; defaults to the metric schema's default
--group-by <dimension>  repeatable, groups by multiple dimensions
-f, --filter "<expr>"   OData filter expression; repeatable, combined with `and`
--prod                  shorthand for --filter "environment eq 'production'"
-s, --since             relative duration (1h/24h/7d), date, or ISO timestamp; default: last hour
-u, --until             end of time range; default: now
-g, --granularity       time bucket size; auto-computed if omitted
--bucket-timezone       IANA timezone for calendar bucket alignment (does not shift --since/--until/output)
-l, --limit             max grouped results per time bucket; default 10
--order-by              count (default) or value; only applies with --group-by
--order                 asc or desc; default desc
-p, --project           project name or ID; defaults to linked project when --all is not set
--all                   query across every project in the team scope; cannot combine with --project
--format                json output for automation and agents (vs. default human-readable table/time-series)

Source: https://vercel.com/docs/cli/metrics
```

## Cross-References

- **Corroborates**:
  - `blog-vercel-ai-sdk-7-release.md` Claim 10 (AI SDK 7's `--format`-equivalent
    structured telemetry design: "AI SDK 7 emits structured telemetry through
    the Node.js tracing channel, allowing observability providers to
    subscribe once" and its `@ai-sdk/otel` package) and Claim 5 (`HarnessAgent`
    runs support "Gateway-ready authentication... simplifying hosted and
    sandboxed agent execution"): both sources show Vercel building
    machine-consumable, structured output/authentication paths as first-class
    design targets across separate product lines (AI SDK observability vs.
    the CLI's Web Analytics query surface), rather than treating "agent
    consumption" as an afterthought bolted onto a human-facing tool.
  - `blog-ghaw-agent-observability.md` Claim 7 (GitHub's Metrics Collector
    "treats the metrics feed as input to higher-level orchestrators," i.e.
    metrics as machine-consumed input rather than only a human dashboard):
    this source's Claim 2/5/9 (an agent given CLI access can query metrics
    directly, with `--format json` built for that purpose) is a second,
    independent vendor's concrete tooling for the same underlying idea —
    metrics data designed to be read by agents/orchestrators, not only
    rendered for a human dashboard. GitHub's is an internal agent-factory
    consuming its own agents' metrics; this source is a general-purpose CLI
    a coding agent can be given access to for a project's product analytics —
    different systems being measured, same "agents as metrics consumers, not
    just humans" pattern.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No
  existing corpus note makes a claim about agent-facing analytics/metrics
  CLIs that this source opposes.

- **Extends**:
  - `blog-vercel-enterprise-apps-and-agents.md` and
    `blog-vercel-ai-gateway-production-index-may2026.md`: both notes cover
    Vercel's agent-facing infrastructure (identity/credential governance,
    AI Gateway cost/routing telemetry respectively) but neither documents a
    CLI tool specifically built for an agent to query a project's own
    application-level analytics (as opposed to LLM-routing/spend telemetry
    or access-control). This source adds a third, distinct Vercel
    agent-infrastructure surface: product/traffic analytics as an
    agent-queryable tool, not LLM usage or platform governance data.
  - `blog-vercel-ai-sdk-7-release.md` Claim 4 (`HarnessAgent`, wrapping
    external coding-agent harnesses like Claude Code behind a standard
    interface, with configurable "sandboxes, instructions, custom skills,
    and tools"): this source's `vercel metrics` command is a concrete
    candidate for exactly the kind of "tool" such a harness-wrapped coding
    agent could be given — the changelog's own framing ("providing a coding
    agent access to the CLI") describes precisely this pattern without
    naming `HarnessAgent` specifically or showing the two products wired
    together.

- **Novel**:
  - **A product-analytics CLI explicitly designed with a `--format json`
    mode "for scripts, agents, and continuous integration checks,"** named
    as such three separate times across the documentation (Claims 2, 5, 9):
    no prior corpus source documents a vendor's web/product-analytics tool
    (as distinct from LLM-usage or cost telemetry) being explicitly
    positioned as an agent-consumable data source with a dedicated machine
    output mode.
  - **Schema-introspection-before-query as a documented agent-friendly
    workflow** (Claim 4): the `vercel metrics schema` discovery step,
    explicitly recommended before building any query and re-emphasized for
    "scripts or agent workflows that need to validate available fields," is
    a self-describing-API pattern not previously documented in this corpus
    for a non-LLM tool surface.
  - **CLI query capability that explicitly and by design exceeds the
    corresponding dashboard UI, with one named, self-disclosed exception**
    (Claims 6-7): the combination of "CLI query surface is broader than the
    dashboard" plus a specific, named metric (Bounce Rate) that remains
    dashboard-only is a level of documented granularity about a tool-vs-UI
    capability gap not seen elsewhere in the corpus's Vercel coverage.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add `vercel metrics` as a concrete,
  named example of a vendor CLI explicitly designed for agent tool access
  (Claim 2's "providing a coding agent access to the CLI" framing, Claim 5's
  `--format json` "for scripts, agents, and continuous integration checks").
  Pair with the schema-discovery pattern (Claim 4: `vercel metrics schema`
  as a mandatory first step) as a reusable design principle for building or
  choosing agent-facing CLI tools generally: prefer tools that expose a
  queryable schema an agent can introspect at runtime over ones requiring
  the agent to have pre-trained, hard-coded knowledge of valid query
  parameters.

- **Chapter 04 (Context Engineering)**: Add this source as a worked example
  of grounding an agent's answers in live, structured external data (traffic
  and conversion metrics) rather than the agent's own training data or
  unstructured context — the three example questions in Claim 2 ("Which
  pages gained the most traffic this week?", etc.) are each answerable only
  by querying current production data, not by anything the agent could infer
  from static context.

- **Chapter 06 (Security Threat Model)** — gap flag, not a positive claim:
  none of the three pages read address what scope of credential or
  permission an agent would need to invoke `vercel metrics` safely (e.g.
  whether a read-only, analytics-only token is available, versus a broader
  Vercel CLI credential that could also deploy or modify projects). Guide
  text citing this source for "give an agent CLI access to analytics" should
  not imply this is a narrowly-scoped, low-risk grant without independently
  verifying what credential the `vercel` CLI actually requires — this
  source is silent on that question.

## Extraction Notes

1. **Changelog entry itself is thin; depth comes from two followed pages.**
   The changelog is ~120 words and contains none of the CLI syntax,
   flag semantics, or query examples used above. Per MINER.md §1, this note
   followed the changelog's own explicit pointer ("explore the
   [documentation](https://vercel.com/docs/analytics/accessing-metrics-with-vercel-cli)")
   and that page's `related` link to the full CLI reference
   (`/docs/cli/metrics`), since the how-to page references flag behavior
   (e.g. `--group-by`, `--filter`) without fully specifying it, and the
   reference page is the authoritative source for exact flag semantics
   (shorthand letters, defaults, mutual exclusions like `--all`/`--project`).
2. **WebFetch used for extraction; no independent raw-HTML cross-check
   performed.** Unlike several other Vercel notes in this corpus that
   cross-verified quotes against raw HTML via direct HTTP fetch (see e.g.
   `blog-vercel-ai-sdk-7-release.md` Extraction Note 1), this extraction
   relied on WebFetch's verbatim-reproduction passes for all three pages,
   each explicitly instructed to reproduce body text character-for-character
   rather than summarize. The docs and reference pages returned as
   structured Markdown with YAML frontmatter (consistent with Vercel's
   documentation source format), which reduces paraphrasing risk relative to
   HTML-rendered marketing prose, but this was not independently re-verified
   against raw HTML the way some other notes in this corpus were.
3. **No demonstrated agent invocation found.** The changelog's and how-to
   page's "agent" framing (Claims 2, 5, 9) is a stated design intent and
   documented output-format affordance, not a worked example — no transcript,
   session log, or code sample anywhere in the three pages read shows an
   actual agent issuing a `vercel metrics` command and using the result.
   This gap is noted explicitly in Claim 2's assessment and should not be
   overstated in guide text as a demonstrated agent workflow.
4. **No contradiction issues filed.** Cross-referenced against all existing
   Vercel source notes and the two GitHub/Anthropic agent-observability notes
   read for this extraction; no claim here opposes an existing note's claim
   in a way that would drive different guide advice (see Cross-References →
   Contradicts).
5. **Confidence calibration: settled.** All nine claims are first-party,
   unambiguous descriptions of a shipping CLI feature's syntax, flags, access
   tiers, and stated design purpose, verified across three consistent pages
   (changelog, how-to, and reference) with no internal conflicts found. This
   note is rated "settled" overall (rather than "emerging," as several other
   Vercel product-announcement notes in this corpus are) because it contains
   no marketing/customer-outcome narrative, no beta/experimental-status
   caveats, and no unverified adoption claims to discount against — every
   claim is a checkable statement about what a shipping command does, not a
   vendor's interpretive or strategic framing.
