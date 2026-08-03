---
source_url: https://vercel.com/changelog/more-granular-observability-for-vercel-sandbox
source_type: blog-post
title: "More granular observability for Vercel Sandbox"
author: Brandon Tuttle, Tom Lienard (Vercel)
date_published: 2026-07-07
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: settled
issue: "#2452"
---

# More granular observability for Vercel Sandbox

> A short Vercel changelog entry announcing four new resource metrics for
> Vercel Sandbox (Active CPU, Provisioned Memory, Data Transfer, running
> sandboxes/sessions), groupable by Sandbox Name and Sandbox Session ID and
> queryable via the Vercel CLI, explicitly framed around cost attribution and
> right-sizing for agent workloads that create sandboxes at scale.

## Source Context

- **Type**: blog-post (Vercel Changelog, `vercel.com/changelog`, published
  July 7, 2026; a short, single-topic feature-announcement entry — not a
  long-form article. Two named authors, Brandon Tuttle and Tom Lienard.)
- **Author credibility**: First-party Vercel product announcement. Vercel
  operates Vercel Sandbox and the Observability dashboard being described, so
  the metric definitions, CLI syntax, and availability tiers are authoritative
  first-party documentation of a shipping feature, not third-party reporting
  or speculation. No named customer quotes or independent validation appear
  in the changelog itself (it is a feature-ships announcement, not a case
  study).
- **Scope**: Covers the specific resource metrics newly exposed for Vercel
  Sandbox (Active CPU, Provisioned Memory, Data Transfer, running
  sandboxes/sessions), the grouping dimensions (Sandbox Name, Sandbox Session
  ID), CLI query syntax, and plan availability (all plans get the
  observability view; manual queries require Pro/Enterprise). Does NOT cover:
  the full Sandbox pricing model (extracted here from the linked
  `/docs/sandbox/pricing` page, followed per MINER.md §1 since the changelog
  itself gives only metric names, not rates or billing rules), the full
  Query/Observability Plus product (briefly followed via `/docs/query` for
  plan-gating context), Sandbox's execution/isolation model (see
  `docs-ghaw-sandbox-reference.md` for GitHub's own sandbox, a different
  product), or any named customer's actual usage of these metrics.

## Extracted Claims

### Claim 1: Vercel Sandbox observability now exposes four metrics — Active CPU, Provisioned Memory, Data Transfer, and running sandboxes/sessions — from the dashboard's Observability tab
- **Evidence**: Direct product description enumerating the four metrics as a
  bulleted list in the changelog body.
- **Confidence**: settled (first-party description of a shipping dashboard feature)
- **Quote**: "From the Observability tab in your dashboard, you can now monitor:" followed by a bulleted list: "Active CPU and CPU usage:", "Provisioned Memory:", "Data Transfer:", "Running sandboxes and sessions:"
- **Our assessment**: This is the headline claim of the changelog. The four
  metrics map directly onto four of the five billed dimensions documented on
  the separate Sandbox pricing page (Active CPU, Provisioned Memory, Data
  Transfer, plus Sandbox Creations and Snapshot Storage — see Claim 8 for the
  one metered dimension the changelog's four bullets do not mention). This
  means the new observability surface lets a team see, before the invoice
  arrives, the exact quantities their bill will be calculated from — turning
  billing dimensions into pre-invoice, drillable telemetry.

### Claim 2: Active CPU measures only time the code actively uses the CPU, in core-hours, and explicitly excludes I/O wait time such as network requests or model calls
- **Evidence**: Direct metric definition in the changelog's bulleted list, corroborated verbatim on the separate pricing reference page.
- **Confidence**: settled (first-party metric definition, identically worded on two separate first-party pages)
- **Quote**: "Active CPU and CPU usage: Measures when your code actively uses the CPU. Active CPU is measured in core-hours and time spent waiting on I/O, such as network requests or model calls, is not billed"
- **Our assessment**: The explicit call-out that "network requests or model calls" do not count toward Active CPU is the load-bearing detail for agent workloads specifically: an agent sandbox that spends most of its wall-clock time waiting on an LLM API call (a very common pattern for coding-agent sandboxes) is not billed for that waiting time under Active CPU. This directly supports the changelog's own framing that these metrics are meant for "tracking agent workloads that create sandboxes at scale" — a sandbox whose task is mostly "call a model, wait, call a tool, wait" will show low Active CPU relative to its wall-clock Provisioned Memory duration, and a team reading only wall-clock duration would over-estimate the CPU-driven portion of their cost.

### Claim 3: Provisioned Memory is billed as memory allocated to the sandbox multiplied by runtime, measured in GB-hours
- **Evidence**: Direct metric definition in the changelog, corroborated with a worked example on the pricing reference page.
- **Confidence**: settled (first-party metric definition; the GB-hours formula is confirmed with a worked numeric example on a separate first-party page)
- **Quote**: "Provisioned Memory: Memory allocated to your sandboxes multiplied by runtime, measured in GB-hours"
- **Our assessment**: Unlike Active CPU, Provisioned Memory is not reduced by I/O wait — it accrues for the full time the sandbox is provisioned, regardless of whether the agent is actively computing or waiting on a model call. This is a meaningful asymmetry for cost modeling: a long-running, mostly-idle-waiting-on-model-calls agent sandbox will show low Active CPU but full-duration Provisioned Memory cost. The pricing page's worked example (a 4 vCPU / 8 GB sandbox running 30 minutes = 4 GB-hours, i.e. `8 GB × 0.5 hours`) confirms the formula is wall-clock runtime, not CPU-active time.

### Claim 4: Data Transfer covers total data transferred in and out of sandboxes, including package downloads and API calls, per the changelog — but the separate pricing page clarifies that only outbound/egress traffic and exposed-port traffic is actually billed, while inbound downloads (packages, git repos, artifacts) are free
- **Evidence**: The changelog's own metric description is broader ("in and out... including package downloads") than the billing rule stated on the linked pricing reference page.
- **Confidence**: settled for the pricing page's billing rule (first-party, explicit "is free" / "is billable" language); the changelog's own metric description is presented at a lower level of precision and should not be read as the billing rule on its own
- **Quote (changelog)**: "Data Transfer: Total data transferred in and out of your sandboxes, including package downloads and API calls"
- **Quote (pricing page)**: "Data your sandbox sends to the internet, plus all traffic to and from exposed ports, is billable and measured in GB. Data your sandbox downloads from the internet, such as packages, Git repositories, artifacts, and datasets, is free. For example, downloading an npm package is free. If you run a web server on an exposed port, both the request it receives and the response it sends are billable."
- **Our assessment**: This is a case where the short changelog entry's plain-English metric description ("data transferred in and out... including package downloads") is imprecise relative to the actual billing semantics documented on the authoritative pricing page — package downloads are named in the changelog's Data Transfer bullet but are explicitly free per the pricing page's billing rule. A practitioner using the new Data Transfer metric to estimate cost impact should read it as "egress + exposed-port traffic," not "all network I/O," or they will over-estimate their Data Transfer bill contribution from routine dependency installs. This is not a MINER.md §4a contradiction (both statements come from the same vendor, are not in conflict about a guide-relevant fact once reconciled, and the pricing page is explicitly the more authoritative, detailed source on a billing question) — it is flagged here as a precision gap between a marketing/feature-announcement description and a billing reference page.

### Claim 5: Each metric can be grouped by Sandbox Name and Sandbox Session ID, enabling drill-down from aggregate usage to the individual sandbox responsible
- **Evidence**: Direct product description in the changelog.
- **Confidence**: settled (first-party description of a shipping dashboard capability)
- **Quote**: "Each metric can be grouped by Sandbox Name and Sandbox Session ID, so you can drill down from aggregate usage to the individual sandbox responsible."
- **Our assessment**: This grouping capability is what converts the four metrics from a single aggregate number into an actionable debugging/cost-attribution tool. Without per-name or per-session grouping, a team could see that total Data Transfer spiked but would have no way to identify which sandbox caused it. With grouping, the changelog's own stated use case — "identifying sandboxes with unexpectedly high data transfer" — becomes directly actionable: filter/group by Sandbox Name to find the specific workload.

### Claim 6: Metrics are queryable via the Vercel CLI using `vercel metrics schema vercel.sandbox` to view the schema and `vercel metrics vercel.sandbox.cpu_usage --all` to retrieve CPU usage across all projects
- **Evidence**: A CLI code example embedded in the changelog, presented as a terminal snippet with two commands.
- **Confidence**: settled (first-party CLI syntax from the vendor operating the CLI)
- **Quote**: "# View all available metrics\nvercel metrics schema vercel.sandbox\n\n# Retrieve the CPU usage of all projects\nvercel metrics vercel.sandbox.cpu_usage --all"
- **Our assessment**: The `vercel metrics <namespace>` command pattern (with `vercel.sandbox` as the metric namespace and `.cpu_usage` as a specific metric under it) implies a broader, structured metrics-namespacing convention on Vercel's platform, not something invented specifically for Sandbox. This is a practical, scriptable access path distinct from the dashboard UI — useful for teams that want to pull sandbox metrics into their own monitoring/alerting pipeline rather than reading the dashboard manually.

### Claim 7: Sandbox observability is included on all Vercel plans, but manual queries are restricted to Pro and Enterprise plans
- **Evidence**: Direct availability statement in the changelog's closing paragraph.
- **Confidence**: settled for the changelog's own statement; see Extraction Notes for a plan-terminology nuance found on the separate Query docs page
- **Quote**: "Observability for Sandbox is included on all plans, and manual queries are available on Pro and Enterprise plans."
- **Our assessment**: This draws a specific line between passive observability (viewing the dashboard, available to Hobby-tier users too) and active querying (constructing custom queries, gated to paid plans). Note that the separate `/docs/query` reference page states that "Full Query access requires Observability Plus" (an add-on/feature-tier name not mentioned in this changelog) rather than naming Pro/Enterprise directly — see Extraction Notes for why this is treated as a terminology gap rather than a contradiction.

### Claim 8: The Sandbox pricing reference page documents five metered billing dimensions in total — Active CPU, Provisioned Memory, Sandbox Creations, Data Transfer, and Snapshot Storage — of which the changelog's four new observability metrics cover only three exactly (Active CPU, Provisioned Memory, Data Transfer) plus a fourth non-billing metric (running sandboxes/sessions) not itself a priced dimension
- **Evidence**: Cross-comparison between the changelog's four-item bulleted list and the pricing page's five-row pricing table (`Sandbox Active CPU`, `Sandbox Provisioned Memory`, `Sandbox Creations`, `Sandbox Data Transfer`, `Snapshot Storage`).
- **Confidence**: settled (both are first-party Vercel pages; the comparison is a direct structural observation, not an inference)
- **Quote**: (no single quote; see the pricing table in Concrete Artifacts)
- **Our assessment**: Sandbox Creations (billed at $0.60 per million) and Snapshot Storage (billed at $0.08/GB-month) are priced dimensions that the new observability metrics do not appear to expose directly per the changelog's own four-item list. A team relying solely on the new Observability-tab metrics to fully explain a Sandbox invoice would still be missing visibility into creation-count and snapshot-storage charges unless those are surfaced elsewhere in the dashboard (not stated one way or the other in this changelog). This is a coverage gap worth naming for practitioners doing cost attribution, not a claim the source itself makes explicitly.

### Claim 9: Vercel frames the specific use cases for these metrics as tracking agent workloads that create sandboxes at scale, right-sizing sandbox configurations based on actual utilization, and identifying sandboxes with unexpectedly high data transfer
- **Evidence**: Direct framing sentence in the changelog, presented as the practical motivation for the feature.
- **Confidence**: settled as a statement of vendor intent (first-party framing of the feature's intended use); anecdotal as to whether teams actually use it this way, since no usage data or customer example is given
- **Quote**: "Metrics are available at both the team and project level and align directly with how Sandbox usage is billed, so you can attribute costs to specific workloads and catch unexpected usage early. This is useful for tracking agent workloads that create sandboxes at scale, right-sizing sandbox configurations based on actual utilization, and identifying sandboxes with unexpectedly high data transfer."
- **Our assessment**: This is the changelog's explicit statement that these metrics exist specifically for agent-workload operators, not general web-hosting customers — Sandbox is being talked about here purely in its "execution environment for agents that create sandboxes at scale" role, not as a general-purpose compute product. "Align directly with how Sandbox usage is billed" is the vendor's own framing connecting the observability feature to the pricing dimensions (see Claim 8's more precise mapping of that alignment).

## Concrete Artifacts

### Full changelog body (verbatim, reconstructed from the page's embedded rich-text JSON and cross-checked against the rendered HTML)

```
Vercel Sandbox observability now includes detailed resource metrics, giving
you deeper visibility into how your sandboxes consume compute and networking.

From the Observability tab in your dashboard, you can now monitor:

- Active CPU and CPU usage: Measures when your code actively uses the CPU.
  Active CPU is measured in core-hours and time spent waiting on I/O, such as
  network requests or model calls, is not billed
- Provisioned Memory: Memory allocated to your sandboxes multiplied by
  runtime, measured in GB-hours
- Data Transfer: Total data transferred in and out of your sandboxes,
  including package downloads and API calls
- Running sandboxes and sessions: How many sandboxes are running at any
  given time, and when sessions are stopped or started

Each metric can be grouped by Sandbox Name and Sandbox Session ID, so you can
drill down from aggregate usage to the individual sandbox responsible.

You can also query and visualize metrics via the Vercel CLI:

# View all available metrics
vercel metrics schema vercel.sandbox

# Retrieve the CPU usage of all projects
vercel metrics vercel.sandbox.cpu_usage --all

Metrics are available at both the team and project level and align directly
with how Sandbox usage is billed, so you can attribute costs to specific
workloads and catch unexpected usage early. This is useful for tracking
agent workloads that create sandboxes at scale, right-sizing sandbox
configurations based on actual utilization, and identifying sandboxes with
unexpectedly high data transfer.

Observability for Sandbox is included on all plans, and manual queries are
available on Pro and Enterprise plans. Learn more in the Sandbox
documentation.

Source: https://vercel.com/changelog/more-granular-observability-for-vercel-sandbox
Published: July 7, 2026, by Brandon Tuttle and Tom Lienard
```

### Sandbox pricing table (verbatim, from `/docs/sandbox/pricing`, followed per MINER.md §1)

```
|                              | Hobby (Included)    | Pro (Per month)   | Enterprise (Per month) |
|------------------------------|----------------------|--------------------|--------------------------|
| Sandbox Active CPU           | 5 hours/month        | $0.128/hour        | $0.128/hour              |
| Sandbox Provisioned Memory   | 420 GB-hours/month   | $0.0212/GB-hour    | $0.0212/GB-hour          |
| Sandbox Creations            | 5,000/month          | $0.60/1M           | $0.60/1M                 |
| Sandbox Data Transfer        | 20 GB/month          | $0.15/GB           | $0.15/GB                 |
| Snapshot Storage             | 15 GB (lifetime)     | $0.08/GB-month     | $0.08/GB-month           |
| Concurrent Sandboxes         | 10                   | 2,000              | 2,000                    |
| Max Runtime Duration         | 45 minutes           | 24 hours           | 24 hours                 |
| vCPU Allocation Rate         | 20-40/min            | 5,000/min          | 5,000/min                |

Source: https://vercel.com/docs/sandbox/pricing
```

### Provisioned Memory worked example (verbatim, from `/docs/sandbox/pricing`)

```
"The memory allocated to your sandbox (in GB) multiplied by the time it
runs (in hours). Each vCPU includes 2 GB of memory. Provisioned memory is
billed in 1 minute minimum increments to account for sandbox lifecycle
management. For example, a 4 vCPU sandbox with 8 GB of memory running for
30 minutes uses:"

8 GB × 0.5 hours = 4 GB-hours

Source: https://vercel.com/docs/sandbox/pricing — "Provisioned Memory" section
```

### Data Transfer billing rule (verbatim, from `/docs/sandbox/pricing`)

```
"Data your sandbox sends to the internet, plus all traffic to and from
exposed ports, is billable and measured in GB. Data your sandbox downloads
from the internet, such as packages, Git repositories, artifacts, and
datasets, is free. For example, downloading an npm package is free. If you
run a web server on an exposed port, both the request it receives and the
response it sends are billable."

Source: https://vercel.com/docs/sandbox/pricing — "Network" section
```

### Query plan-gating language (verbatim, from `/docs/query`)

```
"Full Query access requires Observability Plus. With free observability,
you can open a query. To modify filters or create new queries, enable
Observability Plus."
"Enterprise teams can contact sales to get a customized plan based on
their requirements."

Source: https://vercel.com/docs/query — "Getting started" section
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-connector-observability.md` Claim 1 (Anthropic shipped a
    production dashboard for MCP connector developers, June 8, 2026,
    explicitly filling an operational-monitoring gap): this source is a
    second, independent vendor (Vercel, one month later) shipping
    fine-grained production observability for a specific agent-adjacent
    execution surface (Sandbox rather than MCP connectors). Both sources
    corroborate a broader pattern of infrastructure vendors treating
    granular, drillable observability as a necessary companion feature to
    agent-execution products, not an afterthought.
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional
    when you're running dozens of AI agents"): that note documents a
    practitioner team building their own observability tooling internally
    for a multi-agent factory; this source shows a platform vendor building
    the equivalent capability (granular per-workload metrics, drill-down
    grouping) directly into a hosted execution product, so practitioners
    using Vercel Sandbox do not need to build the equivalent instrumentation
    themselves.

- **Extends**:
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 9 (Vercel Sandbox
    offering VPC peering and bring-your-own-cloud for enterprise deployment
    isolation, per the cited `blog-anthropic-claude-managed-agents-selfhosted.md`
    Claim 8): that prior corpus material documents Vercel Sandbox's
    *deployment/isolation* dimension (where sandbox compute runs). This
    source extends the Sandbox product picture with its
    *cost-observability* dimension (what a sandbox is billed for and how to
    see it) — a different, complementary axis of the same product, not
    previously documented in the corpus at this level of metric-by-metric
    detail.

- **Contradicts**: None rising to the MINER.md §4a filing threshold. One
  internal precision gap was identified and evaluated: the changelog's own
  Data Transfer metric description ("in and out... including package
  downloads") is broader than the actual billing rule on the pricing
  reference page (downloads are free; only egress and exposed-port traffic
  is billed) — see Claim 4. This is not filed as a contradiction because both
  statements come from the same vendor on two pages of the same product,
  addressing different questions (an approachable feature description vs. a
  precise billing specification) rather than making opposing claims about
  the same fact once the precision gap is accounted for. Similarly, the
  changelog's "manual queries are available on Pro and Enterprise plans"
  (Claim 7) versus the Query docs page's "Full Query access requires
  Observability Plus" is treated as a plan-naming inconsistency across two
  Vercel pages rather than a substantive contradiction — see Extraction
  Notes.

- **Novel**:
  - The specific four newly-exposed Sandbox observability metrics (Active
    CPU, Provisioned Memory, Data Transfer, running sandboxes/sessions) and
    their Sandbox Name / Sandbox Session ID grouping dimensions (Claims 1, 5)
    are new to the corpus — no prior source documents Vercel Sandbox's
    observability surface at this granularity.
  - The `vercel metrics <namespace>` CLI query pattern (Claim 6) is a new,
    concrete, scriptable access mechanism not previously documented for any
    Vercel product in this corpus.
  - The full Sandbox pricing table and Active-CPU/Provisioned-Memory/Data-
    Transfer billing formulas (Claim 8, Concrete Artifacts) are new to the
    corpus — no existing source note documents Vercel Sandbox's pricing
    model in this detail.

## Guide Impact

- **Chapter 03/04 (Execution Layer & Cost Engineering)**: Add the four new
  Sandbox observability metrics (Claims 1-3, 5) and the CLI query pattern
  (Claim 6) as a concrete example of platform-native cost-attribution
  tooling for agent execution environments. Pair this with Claim 2's
  I/O-wait exclusion detail — it is directly relevant for any team
  estimating the cost of agent sandboxes whose workload is mostly "call
  model, wait" rather than CPU-bound, since Active CPU will systematically
  under-represent wall-clock sandbox duration for such workloads (Claim 3
  shows Provisioned Memory does not have this exclusion, so the two metrics
  diverge for I/O-heavy agent tasks).

- **Chapter 04 (Cost Engineering at Scale)**: Add the Data Transfer billing
  precision gap (Claim 4) as a concrete "read the fine print" example for
  practitioners: a metric named "Data Transfer" that appears to include
  "package downloads" in its plain-language description is, per the
  authoritative pricing page, billed only for egress and exposed-port
  traffic — inbound package/repo/artifact downloads are free. This is a
  reusable caution for interpreting any vendor's cost-metric naming against
  its actual billing rule.

- **Chapter 02 (Harness Engineering)**: Add this source alongside
  `blog-anthropic-connector-observability.md` and `blog-ghaw-agent-observability.md`
  as a third, independent data point that production observability for
  agent-execution surfaces (sandboxes, connectors, multi-agent factories) is
  now a standard, expected feature across infrastructure vendors — not a
  bespoke practice teams must build themselves.

## Extraction Notes

1. **Verified against raw HTML, not WebFetch summarization alone.** Per
   MINER.md §2a, two initial WebFetch passes on the changelog URL returned
   text that was reworded differently between passes (e.g. "shifted token
   share" vs. paraphrased headings, differing section titles), indicating
   AI-model paraphrasing rather than verbatim extraction. This note instead
   fetched the raw page HTML directly via `curl`, located the changelog
   body's escaped rich-text JSON payload (a Contentful-style document
   embedded in the page's React Server Component data), and confirmed every
   quoted phrase both in that escaped JSON and in the corresponding rendered
   HTML `<article>` markup. Every `Quote` field in this note — the full
   changelog body, the pricing table, the Provisioned Memory formula, the
   Data Transfer billing rule, and the Query plan-gating language — was
   located character-for-character in raw HTML before being used here.
2. **Two linked docs pages followed, per MINER.md §1.** The changelog links
   to `/docs/sandbox/pricing` (for the billing rates behind the new metrics)
   and `/docs/query` (for the "manual queries" availability claim). Both
   were fetched in full and cross-checked against raw HTML for the pricing
   table figures. A third linked page, `/docs/sandbox` (the general Sandbox
   docs page, linked as "Learn more" at the end of the changelog), was not
   followed — it is the general product overview already substantially
   covered by `blog-vercel-enterprise-apps-and-agents.md`'s treatment of
   Sandbox's deployment/BYOC model, and following it would be redundant with
   existing corpus coverage for this issue's specific observability-metrics
   scope.
3. **Plan-gating terminology gap, not a contradiction.** The changelog states
   "manual queries are available on Pro and Enterprise plans" (Claim 7), but
   the separate `/docs/query` reference page gates full Query access behind
   an "Observability Plus" feature/add-on rather than naming Pro/Enterprise
   directly, and separately tells Enterprise teams to "contact sales" for a
   customized plan. It is unclear from these two pages alone whether
   Observability Plus is bundled automatically with Pro/Enterprise or is a
   separate paid add-on on top of those plans — the two pages use different
   vocabulary for what may be the same gating boundary. This was evaluated
   against MINER.md §4a and judged not to rise to a contradiction (no
   guide-relevant fact is actually disputed; the ambiguity is in tier-naming
   consistency across two vendor pages, not a factual disagreement), but is
   flagged here as a real gap a practitioner would hit when trying to
   reconcile the two pages.
4. **Confidence calibration: settled.** This is a short, unambiguous,
   first-party feature-shipping announcement with no marketing narrative or
   unverified customer claims — every individual claim is a direct,
   verifiable description of a shipping dashboard/CLI feature or a billing
   rule from an authoritative pricing reference page, cross-checked against
   raw HTML. The one precision gap (Claim 4) and one terminology gap (Claim
   7 / Extraction Note 3) are noted explicitly but do not undermine the
   overall settled rating, since both are minor documentation-consistency
   issues rather than uncertainty about what the feature actually does.
5. **No contradiction issue filed.** Both near-tensions identified during
   cross-referencing (Claim 4's Data Transfer description vs. billing rule;
   Claim 7's Pro/Enterprise vs. Observability Plus gating language) were
   evaluated against MINER.md §4a and judged to be same-vendor documentation
   precision/consistency gaps, not opposing claims about a guide-relevant
   fact from independent sources. No contradiction issue was filed.
