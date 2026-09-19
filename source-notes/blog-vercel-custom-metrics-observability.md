---
source_url: https://vercel.com/changelog/custom-metrics-are-now-supported-in-vercel-observability
source_type: blog-post
title: "Custom metrics are now supported in Vercel Observability"
author: Tobias Lins, Tom Lienard (Vercel)
date_published: 2026-08-20
date_extracted: 2026-09-19
last_checked: 2026-09-19
status: current
confidence_overall: settled
issue: "#3565"
---

# Custom metrics are now supported in Vercel Observability

> Vercel Functions can now emit application-specific numeric metrics via a
> `metric()` call from the `@vercel/functions` package, queryable alongside
> Vercel's built-in observability data through the dashboard, a Query tab, or
> the `vercel metrics` CLI — billed per data point as an Observability event,
> with no explicit "for agents" framing anywhere in the source or its linked
> docs page.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`; a
  short feature announcement — one framing paragraph, one code example, and a
  bulleted feature list). Per MINER.md §1, this note follows the changelog's
  one linked page, `/docs/observability/custom-metrics`, which is the
  authoritative mechanism-level reference (parameters, limits, sanitization
  rules, CLI query examples, pricing) and supplies most of this note's
  claims. That docs page's own "Related pages" list (auto-generated
  `docsgraph:related` cross-links to `/docs/cli/metrics`, `/docs/pricing/legacy`,
  and several other changelog/docs pages) was not followed further — those
  are either general product-overview pages already covered by
  `blog-vercel-web-analytics-cli.md`'s extraction of `/docs/cli/metrics`'s
  full flag reference, or unrelated legacy-pricing pages.
- **Author credibility**: First-party Vercel product-team announcement,
  credited to two named individuals (Tobias Lins, Tom Lienard) in the
  changelog byline. The linked docs page carries no separate byline
  (standard product documentation) but is consistent with the changelog
  everywhere the two overlap. No customer quotes, adoption figures, or
  independent benchmarks appear anywhere in either page — this is first-party
  documentation of a shipping feature, not third-party reporting.
- **Scope**: Covers the `metric()` function's parameters, name/attribute
  sanitization and size limits, per-invocation emission limits, automatically
  attached metadata, the three ways to access recorded data (dashboard, Query
  tab, CLI), and per-event pricing. Does **not** cover: any explicit framing
  of custom metrics as an agent-consumable or agent-emitted data source (unlike
  the sibling `vercel metrics` Web Analytics announcement — see Cross-References
  → Contradicts-adjacent), a GA/beta status label for the feature (none found
  in either page), retention/query-history windows for custom metric data, or
  any worked example of using custom metrics to drive an alerting or
  verification workflow.

## Extracted Claims

### Claim 1: Vercel Functions can emit application-specific metrics — such as database query latency or business events — via a new `metric()` function in the `@vercel/functions` package, queryable alongside Vercel's built-in observability data
- **Evidence**: The changelog's opening framing sentence and code example; corroborated by the docs page's "Emit a custom metric" section using the identical function signature.
- **Confidence**: settled (first-party, unambiguous, matching syntax across both pages)
- **Quote**: "you could emit metrics to measure database queries latency, record the number of signups, or count the requests per second of a specific endpoint."
- **Our assessment**: This is a first-party, general-purpose escape hatch from Vercel's built-in (traffic/performance) observability metrics into arbitrary application-defined ones — the three named example use cases (query latency, signups, request rate) span infrastructure-level and business-level metrics without distinction, meaning the feature is not scoped to any one category of measurement.

### Claim 2: `metric()` takes a required string name, a required 64-bit floating-point numeric value, and an optional string-keyed attributes map used for filtering and grouping in Observability
- **Evidence**: The docs page's "`metric()` parameters" table, giving type, required/optional status, and description for each of the three parameters.
- **Confidence**: settled (first-party parameter reference table)
- **Quote**: "`name` | `string` | Yes | The custom metric name, such as `query.duration_ms`. `value` | `number` | Yes | The numeric value to record (64-bit floating-point). `attributes` | `Record<string, string>` | No | String attributes that you can use to filter and group the metric."
- **Our assessment**: Restricting `attributes` to string values only (not numbers or nested objects) is a deliberate constraint that keeps the attribute space simple and directly usable for dashboard filter/group-by UI and CLI `--filter` expressions, at the cost of requiring the caller to stringify anything else (e.g. a plan tier enum, a boolean flag) before attaching it.

### Claim 3: Metric names and attribute names/values must each be non-empty, under 64 bytes, and restricted to ASCII letters, digits, hyphens, underscores, periods, and slashes — any other character is automatically replaced with an underscore rather than rejected
- **Evidence**: The docs page's "Metric and attribute requirements" section, including a worked before/after example.
- **Confidence**: settled (first-party, specific and checkable sanitization rule)
- **Quote**: "Unsupported characters are automatically replaced with an underscore (`_`). For example, `data+summary` is stored as `data_summary`."
- **Our assessment**: The silent-replace-rather-than-reject behavior is worth flagging as a footgun: a caller who passes an attribute value containing, say, a colon or an email address will not get an error — the value will be silently mangled character-by-character into underscores, which could produce misleading or collided attribute values (e.g. two distinct inputs both sanitizing to the same string) without any signal that sanitization occurred.

### Claim 4: Each custom metric emission may include up to 50 user-supplied attributes, and each Vercel Function invocation may emit up to 100 custom metrics total
- **Evidence**: The docs page's "Custom metric emission limits" section, stated as two separate bulleted limits.
- **Confidence**: settled (first-party, explicit numeric limits)
- **Quote**: "Each custom metric emission can include up to 50 user-supplied attributes. Each Vercel Function invocation can emit up to 100 custom metrics."
- **Our assessment**: These are hard per-invocation ceilings a team should design around before treating `metric()` as a general-purpose structured-logging replacement — a function that calls `metric()` in a loop (e.g. once per item in a batch) could hit the 100-per-invocation cap silently; the docs page does not state what happens to the 101st call in an invocation (dropped, error, or truncated attributes), which is a gap worth flagging.

### Claim 5: Vercel automatically attaches five metadata fields to every custom metric data point — deployment ID, request ID, function region, execution path type, and edge network region — without the caller including them in the `attributes` object
- **Evidence**: The docs page's "Automatically collected metadata" table, listing all five fields with one-line descriptions.
- **Confidence**: settled (first-party reference table)
- **Quote**: "Vercel automatically attributes each custom metric data point with the following metadata. You don't need to include these fields in the `attributes` object"
- **Our assessment**: This means a caller's 50-attribute budget (Claim 4) is purely for application-specific dimensions — deployment/request/region context comes free and does not compete with that budget. It also means every custom metric data point is automatically joinable against the same deployment/request/region dimensions Vercel's built-in observability data uses, which is the mechanism that makes "analyze them alongside Vercel's built-in observability data" (the changelog's own framing) concretely true rather than just marketing language.

### Claim 6: Recorded custom metrics are accessible through three distinct surfaces — a dedicated Custom Metrics dashboard view, a Query tab for ad hoc aggregation/filtering, and the `vercel metrics` CLI command
- **Evidence**: The docs page's "Access custom metrics data" section, describing each of the three surfaces with its specific use.
- **Confidence**: settled (first-party, three concretely described access paths)
- **Quote**: "After you deploy and invoke the Vercel Function, you can access custom metrics data from the dashboard, the Query tab, or the Vercel CLI"
- **Our assessment**: Custom metrics reuse the exact same `vercel metrics` CLI command that `blog-vercel-web-analytics-cli.md` documents for Web Analytics data (schema discovery, `--filter`, `--group-by`, `--format json`), rather than introducing a separate CLI surface — see Cross-References → Extends for the specific reused mechanics this implies.

### Claim 7: The `vercel metrics` CLI can list all available custom metrics via `vercel metrics schema`, and query one with an attribute filter using a `key:value` syntax, e.g. `vercel metrics database.duration_ms --filter "plan:pro"`
- **Evidence**: Two worked CLI examples given directly on the docs page, immediately following the "Access custom metrics data" section.
- **Confidence**: settled (first-party worked CLI examples) — see Our assessment for a syntax discrepancy worth flagging
- **Quote**: "List all available metrics: `vercel metrics schema` ... Query a custom metric and filter it by an attribute: `vercel metrics database.duration_ms --filter "plan:pro"`"
- **Our assessment**: The `--filter "plan:pro"` colon syntax shown here does not match the OData-style filter grammar (`--filter "country eq 'US'"`) that `blog-vercel-web-analytics-cli.md`'s Concrete Artifacts section documents for the same `--filter` flag on Web Analytics metrics, sourced from the authoritative `/docs/cli/metrics` reference page. This reads as an informal shorthand in this feature's own docs page rather than a genuinely different filter grammar for custom metrics specifically — but it was not independently resolved (the `/docs/cli/metrics` reference page was not re-fetched for this extraction), so a practitioner should verify the actual accepted syntax with `vercel metrics --help` or the CLI reference rather than assume this example is copy-pasteable as shown.

### Claim 8: Each custom metric data point is billed as one Observability event, at $1.20 per 1 million Observability events, and the only way to stop being charged for a metric is to remove its `metric()` call from the application
- **Evidence**: The docs page's "Pricing" section, including a worked example converting invocation count to event count.
- **Confidence**: settled (first-party, explicit unit price and worked example)
- **Quote**: "Each custom metric data point counts as one Observability event. Vercel charges $1.20 per 1 million Observability events. For example, emitting one custom metric during each of 1 million function invocations records 1 million Observability events. To stop collecting custom metrics, remove the `metric()` calls from your application."
- **Our assessment**: Because emission volume scales linearly with invocation count and with how many `metric()` calls a function makes per invocation (up to the 100-metric cap in Claim 4), a function calling `metric()` multiple times per invocation multiplies its Observability-event cost accordingly — a team instrumenting a high-traffic function with, say, 10 `metric()` calls per invocation is implicitly paying 10x the per-invocation event cost of a function emitting one. Neither page gives a cost-management recommendation (e.g. sampling) for high-volume emission beyond "remove the calls."
- **Note**: The changelog itself does not mention pricing at all — this claim comes entirely from the linked docs page.

### Claim 9: Custom metrics require a Pro or Enterprise plan with the Observability Plus add-on
- **Evidence**: A single sentence surfaced via the WebFetch summary pass of the changelog page (not independently re-verified against the docs page's own text, which does not restate the plan requirement in the sections captured).
- **Confidence**: emerging (stated once, not cross-verified against a second independent passage)
- **Quote**: (no direct quote located in the docs page text captured for this extraction; see Extraction Notes)
- **Our assessment**: This is consistent with `blog-vercel-web-analytics-cli.md` Claim 3's documented pattern that most non-Web-Analytics/Speed-Insights metrics require Observability Plus — custom metrics, being neither Web Analytics nor Speed Insights, would fall under that general paid-tier gate rather than being an exception to it. Treat the specific plan-gating claim as directionally right but not independently confirmed character-for-character against the docs page in this extraction.

### Claim 10: Neither the changelog nor its linked docs page frames custom metrics as an agent-facing or agent-consumable feature — no mention of coding agents, AI workflows, or agent tool access appears anywhere in either page
- **Evidence**: Absence check across both pages read in full for this extraction.
- **Confidence**: settled (absence of a specific framing, checked directly against both full page texts)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is a direct answer to the Prospector's triage question ("What observability patterns emerge when teams use custom metrics to instrument agents?"): the source itself supplies none. This is a notable contrast with `blog-vercel-web-analytics-cli.md`, whose changelog and docs pages explicitly and repeatedly (three separate times) frame the same `vercel metrics` CLI's `--format json` output and schema-discovery workflow as built "for scripts, agents, and continuous integration checks." Custom metrics reuse that same CLI (Claim 6) and could plausibly be emitted from within an agent's own tool-calling code to self-report latency or outcome data, but this specific source does not make that connection — it is a plausible extrapolation, not a documented pattern, and should not be cited in the guide as if Vercel positioned this feature for agent self-instrumentation.

## Concrete Artifacts

### `metric()` usage example (verbatim, from `/docs/observability/custom-metrics`)

```ts
// filename: api/query.ts
import { metric } from '@vercel/functions';

metric('query.duration_ms', 100, { plan: 'pro' });
```

### Sanitization example (verbatim, from `/docs/observability/custom-metrics`)

```ts
// data+summary is stored as data_summary
metric('query.duration_ms', 100, { data_summary: 'pro/v1' });
```

### CLI access examples (verbatim, from `/docs/observability/custom-metrics`)

```bash
# List all available custom metrics
vercel metrics schema

# Query a custom metric filtered by an attribute
vercel metrics database.duration_ms --filter "plan:pro"
```

### Automatically collected metadata fields (verbatim table, from `/docs/observability/custom-metrics`)

```
Field               | Description
deploymentId        | Vercel deployment that emitted the metric.
requestId           | Request that emitted the metric.
functionRegion      | Region where the function emitted the metric.
pathType            | Execution path type that emitted the metric.
edgeNetworkRegion   | Vercel CDN region that handled the request.
```

### Pricing (verbatim, from `/docs/observability/custom-metrics`)

```
Each custom metric data point counts as one Observability event.
Vercel charges $1.20 per 1 million Observability events.

Example: emitting one custom metric during each of 1 million function
invocations records 1 million Observability events.

To stop collecting custom metrics, remove the metric() calls from your
application.
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-web-analytics-cli.md` and `blog-vercel-eve-integrations-cli.md`
were re-read in full (including their numbered `### Claim N:` heading lists)
during this extraction per MINER.md §4b, and every claim number cited below
was located and confirmed against that note's own numbered claims in
document order before writing this section.

- **Corroborates**:
  - `blog-vercel-web-analytics-cli.md` Claim 3 (Web Analytics and Speed
    Insights metrics are queryable without Observability Plus, "while all
    other metrics require it"): this source's Claim 9 (custom metrics require
    Pro/Enterprise with Observability Plus) is consistent with — and a named
    concrete instance of — that general "all other metrics" paid-tier gate.
  - `blog-vercel-web-analytics-cli.md` Claim 9 ("The dashboard and CLI are
    complementary: Use product dashboards for curated views. Use `vercel
    metrics` for custom filtering, grouping, aggregations..."): this source's
    Claim 6 (custom metrics accessible via dashboard, Query tab, or CLI) is
    the same complementary-surfaces pattern applied to a newly-introduced
    metric category rather than to Web Analytics specifically.

- **Contradicts-adjacent (not filed as a MINER.md §4a contradiction)**:
  This source's Claim 7 documents a `key:value` colon syntax for `--filter`
  (`--filter "plan:pro"`) on the custom-metrics docs page, while
  `blog-vercel-web-analytics-cli.md`'s Concrete Artifacts section documents
  an OData-style `--filter` grammar (`--filter "country eq 'US'"`,
  `--filter "startswith(request_path, '/docs')"`) sourced from the
  authoritative `/docs/cli/metrics` CLI reference page for the same flag on
  Web Analytics metrics. This is not filed as a MINER.md §4a contradiction
  because it does not oppose a claim in a way that would change guide
  advice — both notes agree the CLI supports attribute/dimension filtering,
  and the discrepancy looks like an informal example in one product page
  rather than two documented, competing grammars for the same command. It is
  flagged here because a practitioner copying the custom-metrics docs page's
  example verbatim may hit a syntax error if the CLI in fact only accepts the
  OData grammar; this was not independently resolved (see Extraction Notes).

- **Extends**:
  - `blog-vercel-web-analytics-cli.md` (which documents the `vercel metrics`
    CLI's schema-discovery workflow, `--format json` output, and full flag
    reference for Web Analytics data): this source extends that same CLI
    surface to a new, user-defined metric category. Claim 6 here (three
    access surfaces) and Claim 7 (schema/query examples) show the identical
    `vercel metrics schema` / `vercel metrics <id> --filter ...` pattern that
    note's Claim 4 and Concrete Artifacts document, now applied to
    application-emitted rather than platform-collected data.

- **Novel**:
  - **A `metric()` call embeddable directly in application/function code to
    emit arbitrary named, numeric, attributed data points** (Claims 1-3): no
    prior corpus source documents a Vercel-native, in-code metric-emission
    API — the existing Vercel observability notes in this corpus
    (`blog-vercel-web-analytics-cli.md`) cover querying platform-collected
    data, not emitting application-defined data into the same system.
  - **Silent character-sanitization (rather than rejection) of out-of-range
    metric/attribute names** (Claim 3): not previously documented in this
    corpus for any Vercel telemetry surface.
  - **A stated per-invocation instrumentation ceiling (100 metrics, 50
    attributes each) with no documented behavior for exceeding it** (Claim
    4): a concrete, checkable design constraint not seen elsewhere in the
    corpus's Vercel observability coverage.

## Guide Impact

- **Chapter 03 (Verification)**: Do **not** cite this source as evidence that
  custom metrics enable a new agent-verification pattern — Claim 10
  establishes the source itself makes no such connection, unlike the sibling
  `vercel metrics` Web Analytics announcement. If the guide wants to recommend
  "have an agent emit its own success/latency metrics via `metric()` for later
  verification," that is an extrapolation from this source's mechanics
  (Claims 1-6), not a documented Vercel pattern, and should be labeled as
  such.

- **Chapter 05 (Team Adoption) / observability tooling sections**: Add
  `metric()` as a concrete, low-friction mechanism for a team to emit
  business- or application-level metrics from Vercel Functions without a
  separate observability vendor integration (Claim 1), noting the concrete
  per-invocation limits (Claim 4) and per-event pricing model (Claim 8) a
  team should budget for before instrumenting high-traffic functions broadly.

- **Chapter 06 (Security/Cost governance)** — gap flag, not a positive claim:
  neither page addresses rate-limiting, sampling, or cost-capping guidance
  for `metric()` beyond "remove the calls" (Claim 8); a team giving many
  functions or agents write access to emit custom metrics has no documented
  built-in cost ceiling beyond the linear per-event billing itself.

## Extraction Notes

1. **Two pages read; no additional linked pages followed.** The changelog
   (`vercel.com/changelog/custom-metrics-are-now-supported-in-vercel-observability`)
   and its one substantive linked page
   (`vercel.com/docs/observability/custom-metrics`) were both fetched via
   WebFetch with a verbatim-reproduction instruction. The docs page's
   `docsgraph:related` auto-generated cross-link block (pointing to
   `/docs/cli/metrics`, `/docs/pricing/legacy`, and several other
   changelog/docs pages) was not followed — `/docs/cli/metrics`'s full flag
   reference is already captured in `blog-vercel-web-analytics-cli.md`'s
   Concrete Artifacts section, and the remaining links are general
   product-overview or unrelated legacy-pricing pages.
2. **Claim 9 (plan-gating) not independently re-verified against a second
   passage.** The Observability Plus / Pro-or-Enterprise requirement was
   captured from the changelog page but the docs page text obtained for this
   extraction does not restate it in the sections quoted here; confidence is
   marked "emerging" for that specific claim rather than "settled," and no
   `Quote` is given for it per MINER.md §2a (no exact passage was located to
   cite verbatim).
3. **Claim 7's filter-syntax discrepancy was not independently resolved.**
   The custom-metrics docs page's own worked example uses a `key:value`
   colon filter syntax that does not match the OData-style grammar documented
   for the same `--filter` flag in `blog-vercel-web-analytics-cli.md`'s
   extraction of the `/docs/cli/metrics` reference page. Re-fetching
   `/docs/cli/metrics` directly to check whether it documents a
   metric-type-specific filter grammar (rather than one grammar for the
   `--filter` flag regardless of metric) would resolve this; it was out of
   scope for this extraction given the source's own thinness.
4. **No contradiction issues filed.** No claim in this source directly
   opposes an existing corpus note's claim in a way that would change guide
   advice; see Cross-References → Contradicts-adjacent for the one
   docs-internal syntax discrepancy that falls short of that bar.
5. **Confidence calibration: settled.** Most claims are first-party,
   unambiguous mechanism descriptions (parameters, limits, sanitization
   rules, pricing) stated identically or complementarily across the
   changelog and docs page. The note is rated "settled" overall rather than
   "emerging" because the core mechanism claims (1-8) are unambiguous and
   checkable, and the one lower-confidence claim (9, plan-gating) and one
   flagged discrepancy (7, filter syntax) are narrow enough not to undermine
   the source's central claims about what `metric()` does and how it's
   priced.
