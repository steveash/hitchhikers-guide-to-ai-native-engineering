---
source_url: https://simonwillison.net/2026/Jun/9/agentsview-custom-model-price/
source_type: blog-post
title: "Setting a custom price for a model in AgentsView"
author: Simon Willison
date_published: 2026-06-09
date_extracted: 2026-06-16
last_checked: 2026-06-16
status: current
confidence_overall: emerging
issue: "#1187"
---

# Setting a custom price for a model in AgentsView

> Simon Willison's TIL-style post introduces AgentsView (Wes McKinney's local agent
> cost analytics toolkit) and documents the recipe for adding custom model pricing —
> with a real cost-attribution screenshot showing one project consuming 89.3% of
> daily spending and $516.62 saved via prompt caching, establishing local agent cost
> observability as a concrete practitioner concern.

## Source Context

- **Type**: blog-post (Willison TIL/link-blog format; ~200 words of prose; the
  technical recipe lives on a linked TIL page at
  `https://til.simonwillison.net/llms/agentsview-custom-model-price` which was also
  fetched for this note. The simonwillison.net post provides the motivation and
  dashboard screenshot; the TIL page provides the TOML config and CLI commands.)
- **Author credibility**: Simon Willison is the creator of Django and the `llm`
  Python CLI, and one of the most widely-cited practitioner commentators on LLM
  tooling. He is also the creator of Datasette and the user of the
  `prod_datasette_agent` project shown in the dashboard screenshot — his cost data
  is first-party from his own production local agent usage. No vendor affiliation
  with AgentsView; this is independent practitioner tooling adoption.
- **Scope**: Covers AgentsView's purpose (local agent transcript analysis and cost
  attribution), the concrete problem of a new model lacking pricing data on launch
  day, the TOML-based custom pricing recipe, and a dashboard screenshot showing
  real cost attribution data. Also documents Claude Fable 5's pricing (2x Opus 4.7)
  as the source of the custom config values. Does NOT cover: AgentsView's full
  feature set, all dashboard views, model comparison features, or integration with
  cloud-based agents.

## Extracted Claims

### Claim 1: AgentsView is a Python toolkit by Wes McKinney for analyzing coding agent transcripts and exploring token usage across multiple local coding agents

- **Evidence**: Willison's first-person description in the post, combined with a
  reference to McKinney's prior credibility (creator of Pandas). A working
  dashboard screenshot confirms the tool exists and produces real output.
- **Confidence**: settled (factual tool description corroborated by the working
  dashboard screenshot)
- **Quote**: "I've been really enjoying AgentsView by Wes McKinney as a tool for
  exploring my token usage across different coding agents running on my laptop."
- **Our assessment**: AgentsView fills a specific gap: understanding *local* agent
  cost and usage patterns across projects, in contrast to platform-level cost
  management (GitHub Actions minutes, Copilot organization billing). Wes McKinney's
  Pandas pedigree signals a data-analysis orientation — the tool is designed to
  surface insights from transcript data, not just display totals. The local scope
  (agents "on my laptop") is important: this is practitioner self-monitoring, not
  organizational cost management.

### Claim 2: When a new model is released, cost analytics tools may not immediately include it in their pricing database, creating a gap that practitioners must bridge manually

- **Evidence**: Willison's report of encountering the gap on Claude Fable 5's
  launch day (June 9, 2026), the same day the post was published.
- **Confidence**: emerging (anecdote, but reflects a structural lag that applies to
  any third-party pricing database whenever a new model ships)
- **Quote**: "Claude Fable 5 came out today and wasn't yet included in the pricing
  database AgentsView uses."
- **Our assessment**: The model-release → pricing-database lag is a predictable
  pattern, not a one-off bug. Any cost analytics tool maintaining an internal
  pricing database (rather than querying the provider's pricing API live) will have
  this gap on launch day for new models. Practitioners relying on cost analytics
  for billing oversight must account for this lag when a new model is adopted.
  The manual custom pricing recipe (Claim 3) is the mitigation pattern.

### Claim 3: AgentsView supports custom model pricing via a TOML configuration file at `~/.agentsview/config.toml`, using a `[custom_model_pricing."<model-id>"]` section with input, output, cache_creation, and cache_read fields in dollars per million tokens

- **Evidence**: The linked TIL page (`til.simonwillison.net/llms/agentsview-custom-model-price`)
  provides the working TOML recipe, confirmed by Willison's statement that he
  "figured out this recipe for setting custom prices" (the post links directly to
  the TIL).
- **Confidence**: settled (working configuration extracted from a practitioner who
  confirmed it successfully added Fable 5 pricing to AgentsView)
- **Quote**: (no direct prose quote for the recipe; verbatim TOML in Concrete
  Artifacts, sourced from `til.simonwillison.net/llms/agentsview-custom-model-price`)
- **Our assessment**: The config file location (`~/.agentsview/config.toml`) and
  section name (`[custom_model_pricing."<model-id>"]`) are the operative details
  for practitioners. The four fields (input, output, cache_creation, cache_read)
  map directly to Anthropic's billing categories, enabling accurate cost attribution
  including prompt caching economics. This recipe is applicable any time a new
  model ships before it's in AgentsView's database.

### Claim 4: Using the new model itself to reverse-engineer how to configure it in third-party tooling is a practical AI-assisted workflow for day-zero adoption gaps

- **Evidence**: Willison's explicit statement that he used Claude Fable 5 to
  discover the custom pricing recipe on Fable 5's launch day.
- **Confidence**: anecdotal (single practitioner; but the meta-pattern — using AI
  to understand the tool that prices AI — is generalizable and demonstrates
  self-referential utility)
- **Quote**: "I used Fable to reverse-engineer AgentsView and figured out this
  recipe for setting custom prices."
- **Our assessment**: The meta-pattern here is notable: Fable 5 was the subject
  of the pricing gap *and* the tool used to close the gap. This is a concrete
  instance of the broader pattern "use AI to configure AI tooling" — not just
  prompt engineering, but using an AI assistant to analyze a tool's codebase or
  configuration format and produce working configuration. For practitioners:
  when a tool doesn't yet support a new model, prompting the new model itself
  to inspect the tool's code or config format is a viable day-zero workaround.

### Claim 5: Real-world local agent cost attribution shows extreme per-project variation — one project can account for nearly 90% of total daily spending

- **Evidence**: The dashboard screenshot in the post showing a treemap of Claude
  Fable 5 usage across Willison's local projects. The `prod_datasette_agent`
  project is shown at $74.06 (89.3% of total); other projects range from $3.98
  to $0.15.
- **Confidence**: anecdotal (one practitioner's single-day usage data; but the
  pattern of one project dominating spending is a realistic reflection of agent
  workload distribution)
- **Quote**: "Here's my Claude Fable 5 usage for today so far, plotted by
  AgentsView as a treemap across my different local projects:"
- **Our assessment**: The 89.3% / 10.7% split is the key practitioner insight in
  this screenshot. Without per-project attribution, total spend appears as a single
  number that obscures which workloads are driving cost. The treemap visualization
  makes the distribution immediately readable. For practitioners running multiple
  local agents: the agent driving the most value is likely also driving the most
  cost, and only per-project attribution reveals whether that ratio is appropriate.
  At $74.06 for a single production agent in one day, the economics of agent
  deployment become non-trivial even at individual practitioner scale.

### Claim 6: Prompt caching generates substantial and measurable savings in production local agent workflows — Willison's single-day session shows $516.62 saved versus running without caching

- **Evidence**: Dashboard screenshot showing "saved via caching" metric visible
  alongside the cost attribution treemap.
- **Confidence**: anecdotal (single practitioner's single-day data; the underlying
  caching economics are well-documented elsewhere, but the scale of savings at
  individual usage scale is novel)
- **Quote**: (no direct prose quote; figure appears in the dashboard screenshot only)
- **Our assessment**: $516.62 in caching savings against ~$83 in actual spend
  represents approximately 6:1 savings ratio. This is the most concrete
  single-data-point illustration of prompt caching ROI for individual practitioners
  in the corpus. Caching savings of this scale are only visible when a tool like
  AgentsView surfaces the `cache_read_input_tokens` data — the raw billing totals
  alone would not reveal this. For practitioners evaluating whether to configure
  prompt caching: this ratio (roughly 6x cost avoidance vs. actual spend) is
  the strongest available practitioner evidence of caching value at individual
  agent usage scale.

### Claim 7: Claude Fable 5 is priced at 2x Claude Opus 4.7 for input and output — $10/M input, $50/M output, with $12.50/M cache creation and $1/M cache read

- **Evidence**: Willison sourced pricing from Anthropic's official documentation
  and embedded it in the TOML recipe on the TIL page.
- **Confidence**: settled (Anthropic official pricing at time of post; June 9, 2026)
- **Quote**: "Fable is 2x the price of Opus for input and output."
- **Our assessment**: The 2x Opus 4.7 multiplier for Fable 5 is the first pricing
  datapoint for Claude's highest-tier model since the Opus 4.7 release documented
  in `blog-simonwillison-gemini35-flash-pricing.md` (Claim 5: Opus 4.7 at ~1.46x
  Opus 4.6). Adding Fable 5 at 2x Opus 4.7 continues the upward price trajectory:
  each new top-tier Claude release adds a further pricing step. The cache_creation
  rate ($12.50/M = 1.25x input) and cache_read rate ($1/M = 0.1x input) follow
  Anthropic's standard caching pricing ratios, providing practitioners with the
  full cost model for budgeting Fable 5 in cache-intensive workflows.

### Claim 8: AgentsView provides two primary interfaces — `uvx agentsview usage daily` for terminal-based usage tables and `uvx agentsview serve` for a web dashboard on port 8080

- **Evidence**: TIL page lists both commands explicitly with their output
  descriptions.
- **Confidence**: settled (concrete CLI commands from a working tool)
- **Quote**: (no verbatim quote for the full command descriptions; see Concrete
  Artifacts for the verbatim commands)
- **Our assessment**: The `uvx` invocation pattern (no installation required)
  means AgentsView can be evaluated without committing to a persistent install.
  The two modes (terminal table vs. web dashboard) serve different audiences:
  quick terminal checks during development vs. the treemap visualization for
  analysis and retrospective review. The port 8080 web dashboard is the view
  shown in Willison's screenshot.

## Concrete Artifacts

### Custom Model Pricing Recipe (from `til.simonwillison.net/llms/agentsview-custom-model-price`)

```toml
# File: ~/.agentsview/config.toml
[custom_model_pricing."claude-fable-5"]
input = 10.0
output = 50.0
cache_creation = 12.50
cache_read = 1
```

*Source: Simon Willison, `til.simonwillison.net/llms/agentsview-custom-model-price`, 2026-06-09.
Pricing values sourced from Anthropic's official documentation. Units: dollars per million tokens.
Section name `[custom_model_pricing."<model-id>"]` is the AgentsView custom pricing extension point.*

### AgentsView CLI Commands (from `til.simonwillison.net/llms/agentsview-custom-model-price`)

```bash
# Terminal usage table
uvx agentsview usage daily

# Web dashboard (port 8080)
uvx agentsview serve
```

*Source: Simon Willison, `til.simonwillison.net/llms/agentsview-custom-model-price`, 2026-06-09.*

### Claude Fable 5 Pricing at Launch (June 9, 2026)

```
Claude Fable 5 pricing (Anthropic, June 9, 2026):
  Input:            $10.00 / million tokens   (2x Opus 4.7)
  Output:           $50.00 / million tokens   (2x Opus 4.7)
  Cache creation:   $12.50 / million tokens   (1.25x input)
  Cache read:       $1.00  / million tokens   (0.10x input)

Reference: Willison's custom config at til.simonwillison.net/llms/agentsview-custom-model-price,
sourced from Anthropic's official documentation.
```

### Dashboard Cost Attribution (from post screenshot, June 9, 2026)

```
AgentsView treemap — Claude Fable 5 usage by project (single day, June 9, 2026):

  Project                  Cost       Share    Tokens
  -----------------------  ---------  -------  ---------
  prod_datasette_agent     $74.06     89.3%    55.9M
  (unnamed project 2)      $3.98      4.8%     826.8k
  (unnamed project 3)      $2.81      3.4%     924.7k
  (unnamed project 4)      $1.92      2.3%     542.9k
  (unnamed project 5)      $1.37      (est.)   455k
  (unnamed project 6)      $0.15      (est.)   26.4k

  Cache savings:           $516.62 saved vs uncached

Source: Simon Willison, simonwillison.net/2026/Jun/9/agentsview-custom-model-price/,
screenshot of AgentsView web dashboard. Dollar amounts and percentages read from
the treemap image caption as reported in the post.
```

## Cross-References

- **Corroborates**:
  - `failure-cursor-ultra-billing-cache-explosion.md` Lesson 6 ("Billing
    transparency requires exporting CSV, not reading the product UI"): AgentsView
    addresses exactly the transparency gap that lesson documents. Where the Cursor
    failure report finds billing opacity requiring manual CSV export, AgentsView
    provides automated local cost attribution that surfaces the same underlying
    data (cache tokens, per-project costs) in a navigable dashboard. The two
    sources together make the case that local cost observability tooling is a
    practitioner need, not a nice-to-have.
  - `failure-cursor-ultra-billing-cache-explosion.md` Lesson 2 ("Prompt-cache
    replay costs scale with session state depth"): The $516.62 caching savings
    figure (Claim 6) is the positive-side mirror of the Cursor billing explosion.
    Both demonstrate that prompt caching is the dominant cost variable in
    sustained agentic sessions — in the Cursor case, it caused unexpected costs;
    in Willison's case, it generated measurable savings. Both make the same
    underlying argument: cache economics must be visible to practitioners.
  - `blog-bswen-mcp-token-cost.md` Claim 1 ("Every MCP server loads its full tool
    definitions before you type anything"): Both Bswen and Willison surface the
    same general problem — agent token costs are opaque unless you instrument them.
    Bswen's solution is `/context` inspection within Claude Code; Willison's is an
    external analytics dashboard (AgentsView). The two approaches are complementary:
    `/context` shows the current session's composition; AgentsView shows historical
    trends across sessions and projects.
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 5 (cross-vendor price
    escalation table, Opus 4.7 at ~1.46x Opus 4.6): This source extends that
    pricing trajectory with Fable 5 at 2x Opus 4.7 (Claim 7). Together the two
    notes document the ongoing upward pricing trend at Anthropic's top tier:
    Opus 4.6 → Opus 4.7 (+46%) → Fable 5 (+100%).

- **Contradicts**: None identified. No existing note makes claims about AgentsView
  or conflicts with the pricing data presented here.

- **Extends**:
  - `blog-simonwillison-deepseek-v4.md` Concrete Artifacts → Pricing Comparison
    Table: That table documents Claude Opus 4.7 at $5/$25 per million input/output
    tokens (April 2026). This source adds Fable 5 at $10/$50 (2x Opus 4.7),
    extending the frontier model pricing history one generation forward. Adding
    Fable 5 to the table: Haiku 4.5 ($1/$5) → Sonnet 4.6 ($3/$15) → Opus 4.7
    ($5/$25) → Fable 5 ($10/$50).
  - `docs-ghaw-cost-management.md` Claim 1 (two billing components: Actions minutes
    + inference): That note covers organizational platform cost management
    (GitHub Actions + provider inference). This source covers the local equivalent:
    practitioner-level inference cost attribution across local agent sessions.
    Together they establish that cost observability is a concern at both individual
    and organizational scale, requiring different tooling (AgentsView vs. `gh aw
    audit`).

- **Novel**:
  - **First in-corpus documentation of AgentsView**: No prior note covers Wes
    McKinney's AgentsView toolkit. This is the first extraction documenting it
    as a practitioner observability tool for local agent costs.
  - **Custom model pricing recipe for AgentsView**: The TOML recipe pattern
    (`~/.agentsview/config.toml`, `[custom_model_pricing."<model-id>"]`) is not
    documented in any prior note. It is immediately actionable for any AgentsView
    user encountering a new model not in the pricing database.
  - **Claude Fable 5 pricing at launch**: $10/$50 per million input/output
    tokens ($12.50 cache creation, $1 cache read) is the first in-corpus
    documentation of Fable 5 pricing from Anthropic's official documentation.
  - **$516.62 caching savings in a single practitioner session**: This is the
    most concrete single-data-point illustration of prompt caching ROI for an
    individual practitioner in the corpus. No prior note quantifies caching
    savings at this level of specificity for individual-scale usage.
  - **AI-assisted tooling configuration as a day-zero workaround pattern**: The
    meta-pattern of using a new model to reverse-engineer the tooling that needs
    to support it is not documented elsewhere in the corpus.

## Guide Impact

- **Chapter 03 (Observability / Cost Tracking)**: Add AgentsView as a concrete
  tool for local agent cost attribution. The guide currently covers organizational
  cost management (GitHub Copilot billing, gh-aw audit) but lacks coverage of
  individual practitioner cost tracking. AgentsView fills this gap: it surfaces
  per-project, per-model, per-session cost attribution for locally-running agents
  using uvx (no installation required). Recommend adding a note: "For practitioners
  running multiple local coding agents, AgentsView (`uvx agentsview serve`) provides
  a treemap dashboard of cost attribution by project and cache efficiency metrics.
  When a new model is released before AgentsView updates its pricing database,
  add a `[custom_model_pricing."<model-id>"]` section to `~/.agentsview/config.toml`."
  Cite Claims 1, 3, and 8 and the Concrete Artifacts recipe.

- **Chapter 02 (Model Selection — Pricing)**: Claim 7 updates the frontier model
  pricing table with Claude Fable 5 at $10/$50 per million tokens (2x Opus 4.7).
  Any pricing table or model selection cost framework should add this entry.
  Cross-reference `blog-simonwillison-deepseek-v4.md` Concrete Artifacts for the
  full April 2026 pricing table; Fable 5 extends it to June 2026. Note the
  continuing upward trend: Opus 4.7 → Fable 5 adds another 2x step to the
  already-documented 1.46x Opus 4.6 → Opus 4.7 jump.

- **Chapter 03 (Observability — Caching Economics)**: Claim 6 ($516.62 caching
  savings vs. ~$83 actual spend in one day) is the strongest practitioner-scale
  evidence of prompt caching ROI in the corpus. Pair with `failure-cursor-ultra-billing-cache-explosion.md`
  Lesson 2 for the negative-side caching economics story: together they establish
  that caching is both the largest cost driver when it accumulates invisibly AND
  the largest savings lever when properly accounted for. Guide recommendation:
  "Enable caching and instrument it. Unmonitored, cached prefixes are a billing
  risk (cf. Cursor Ultra billing explosion). Monitored, caching can save multiples
  of actual inference cost (cf. Willison's $516 savings vs. $83 spend)."

- **Chapter 01 (Daily Workflows — AI-Assisted Tooling Configuration)**: Claim 4
  (using Fable 5 to reverse-engineer AgentsView's config format on Fable 5's
  launch day) illustrates a generalizable pattern: when a tool does not yet support
  a new model, use the model itself to inspect the tool's configuration format.
  This is distinct from "ask the LLM to write code" — it is using LLM reasoning to
  understand undocumented tool internals quickly. Worth a brief callout in the
  guide's daily-workflow patterns section.

## Extraction Notes

- The source post is short (~200 words of prose). The main technical content
  (TOML recipe, CLI commands) lives on the linked TIL page
  (`til.simonwillison.net/llms/agentsview-custom-model-price`), which was fetched
  separately. Both the simonwillison.net post and the TIL page were read for this
  note, as the TIL page contains the concrete artifacts that make the post
  actionable.
- WebFetch returned summaries rather than verbatim text for full-post requests.
  Verbatim quotes were obtained through targeted question prompts. Three of the
  five verbatim quotes were confirmed across multiple independent fetches
  returning consistent text. Quotes from the dashboard screenshot (cost values,
  percentages, token counts) and the TIL page TOML snippet are attributed
  accurately to their respective pages.
- The dashboard screenshot shows numeric values that appear in the image rather
  than in prose — these are included in Concrete Artifacts with clear attribution
  to the screenshot.
- No contradictions identified. No contradiction issue required.
- The `#atom-everything` fragment in the original issue URL is a feed anchor;
  `source_url` uses the canonical URL without the fragment, consistent with prior
  Willison source notes in this corpus.
- Three triage comments from the Prospector were present on the issue, all
  consistent: extract AgentsView as a cost attribution tool, the custom model
  pricing recipe, and the caching savings data. The third triage comment explicitly
  rates novelty as high and identifies Ch03 and Ch02 as the relevant chapters.
  This extraction follows that guidance.
