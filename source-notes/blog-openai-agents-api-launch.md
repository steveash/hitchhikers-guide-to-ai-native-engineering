---
source_url: https://openai.com/index/introducing-the-agents-api
source_type: blog-post
title: "Introducing the Agents API"
author: OpenAI
date_published: 2026-09-10
date_extracted: 2026-09-20
last_checked: 2026-09-20
status: current
confidence_overall: emerging
issue: "#3579"
---

# Introducing the Agents API

> OpenAI's public-beta launch of the Agents API: a managed, versioned
> exposure of the same Codex harness and infrastructure that powers Codex
> and ChatGPT for Work, giving developers server-side context compaction,
> tool search, and subagent orchestration without building their own
> harness — with a choice of OpenAI-hosted sandboxes, nine named
> third-party sandbox partners, or fully self-hosted compute.

## Source Context

- **Type**: blog-post (official OpenAI product announcement, `openai.com/index/`,
  published September 10, 2026), cross-checked against four linked first-party
  docs pages on `developers.openai.com` for technical depth: the Agents API
  overview, the Compaction guide, the Tool search guide, and the Multi-agent
  guide.
- **Author credibility**: First-party OpenAI product announcement — maximum
  authority on what the product provides and how it is configured. The
  announcement includes eight named customer testimonials with named
  individuals and companies (Ciridae, Long Lake, WithCoverage, SafetyKit,
  Dwelly, Hypha, deepsense.ai, Nash.ai), which is higher-signal than generic
  marketing copy, but the quantitative claims inside those testimonials
  (eval-score deltas, latency reductions, cost reductions) are self-reported
  by customers in a vendor-published post, not independently audited. The
  linked docs pages are OpenAI's own API reference/guide content — accurate
  as a description of what shipped, but not independent verification of
  performance claims.
- **Scope**: Covers what the Agents API is (a managed API wrapper around the
  open-source Codex harness), how sessions/agents/environments/events are
  structured, sandboxing options (OpenAI-hosted vs. self-hosted vs. nine
  named partners), three specific harness capabilities (context compaction,
  tool search, multi-agent/subagent delegation), the open-source relationship
  to the `openai/codex` repo, and beta pricing/availability. Does NOT cover:
  independent benchmarking of the customer-reported metrics, full API
  reference detail for every endpoint, migration guidance from other agent
  frameworks, or a technical explanation of how compaction/tool-search
  algorithms work internally (the linked guides describe the *interface*,
  not the internals).

## Extracted Claims

### Claim 1: The Agents API exposes the same harness and infrastructure that powers Codex and ChatGPT for Work, now available to any developer via API
- **Evidence**: Direct vendor statement of product design; positioned as the
  culmination of lessons learned scaling Codex/ChatGPT for Work "to millions
  of people."
- **Confidence**: settled (this is a factual description of the product,
  not a disputable performance claim)
- **Quote**: "Today, we're introducing the Agents API in public beta, bringing
  that same harness and infrastructure that powers Codex to developers
  through a simple, flexible API."
- **Our assessment**: This is the core positioning claim of the launch — the
  harness is not a new product built for this API, it's productized
  internal infrastructure. That lineage claim is corroborated structurally
  by the "open-source foundation" claim (Claim 9 below): the harness is the
  same public `openai/codex` codebase, not a black box built separately for
  enterprise customers.

### Claim 2: A production-ready agent can be created in a single API call, specifying task, model, tools, and environment together
- **Evidence**: Code example showing `client.beta.agents.sessions.create()`
  with `agent.model`, `agent.tools`, `agent.multi_agent`, `environment`, and
  `input` all set in one call.
- **Confidence**: settled (directly demonstrated in the docs)
- **Quote**: "With the Agents API, you can create a production-ready agent in
  a single API call by specifying the task, model, tools, and environment."
- **Our assessment**: This "single API call to provision a fully configured
  agent" pattern is not unique to OpenAI — it matches the "managed agents as
  a service" pattern already in the corpus from both Anthropic
  (`blog-anthropic-claude-managed-agents.md`) and Google
  (`blog-google-io-2026-developer-keynote.md`, Claim 3, on the Gemini
  Managed Agents API). All three frontier labs have now converged on the
  same provisioning model within roughly five months of each other
  (Anthropic Apr 2026, Google I/O ~May 2026, OpenAI Sep 2026).

### Claim 3: Developers choose the agent's compute environment — OpenAI-managed sandbox, own infrastructure, or a named sandbox partner — while OpenAI always hosts and maintains the harness itself
- **Evidence**: Explicit architecture description plus a labeled diagram
  separating "Agents API / managed Codex harness" from "sandbox" and "your
  application controls self-hosted compute."
- **Confidence**: settled
- **Quote**: "OpenAI hosts and maintains the harness. You choose the agent's
  compute environment: in an OpenAI-managed sandbox, on your own
  infrastructure, or with one of our sandbox partners."
- **Our assessment**: This is a meaningful architectural decoupling — harness
  (control loop, context management, tool orchestration) is a hosted
  service; environment (where code actually executes) is a separate,
  swappable concern. This mirrors the harness/sandbox separation the Hypha
  testimonial credits for an 86% reduction in failed agent responses (see
  Claim 8 below), suggesting the separation is not just an architecture
  diagram but has a measurable reliability benefit for at least one
  customer.

### Claim 4: OpenAI is partnering with nine named sandbox providers for first-class environment integrations
- **Evidence**: Named partner list plus a description of what the
  integrations provide (deployment location, storage mechanisms, compute
  configuration).
- **Confidence**: settled
- **Quote**: "We're partnering with ecosystem providers, including Blaxel,
  Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, and Vercel,
  to provide first-class integrations for a range of needs."
- **Our assessment**: This is a notably broad partner list for a beta launch
  and signals OpenAI is not trying to lock developers into an OpenAI-only
  sandbox, unlike a fully closed managed-agent product. Worth tracking
  whether Anthropic's and Google's managed-agent offerings have equivalent
  partner ecosystems, or whether this is a genuine differentiator for
  OpenAI's self-hosted flexibility story.

### Claim 5: The Agents API automatically compacts earlier context as a session approaches its context limit, letting developers build workflows spanning multiple context windows without writing their own compaction logic
- **Evidence**: Product description plus, in the linked Compaction guide, a
  concrete mechanism: server-side compaction triggered by a
  `context_management` / `compact_threshold` parameter on `/responses`, and
  a separate stateless `/responses/compact` endpoint for explicit control.
  The compaction output is "an encrypted compaction item" carrying forward
  prior state and reasoning "using fewer tokens."
- **Confidence**: settled (both the announcement and the docs describe the
  same mechanism consistently)
- **Quote**: "The Agents API automatically compacts earlier context as a
  session approaches its context limit, preserving information the agent
  needs to continue. Developers can build workflows that span multiple
  context windows without implementing their own compaction logic."
- **Our assessment**: The compaction item being explicitly described as
  "opaque and not intended to be human-interpretable" (from the Compaction
  guide) is a notable design choice — it forecloses the kind of
  code-location-level inspection that `research-wasnotwas-context-compaction.md`
  performed on Codex, Gemini CLI, Claude Code, and other *open-source*
  harnesses. Once compaction happens through this managed API, its exact
  algorithm and preservation strategy are no longer independently
  auditable the way they are for the seven open-source harnesses that
  source studied by reading source code. This is a real trade-off the
  guide should surface: managed-harness convenience costs some auditability.

### Claim 6: The Compaction guide states server-side compaction is "ZDR-friendly" (Zero Data Retention compliant) only when `store=false` is set on Responses create requests, while the Agents API itself does not support ZDR at all
- **Evidence**: Direct guide text plus the separately-fetched Agents API
  overview page, which explicitly states: "The Agents API currently
  supports data residency only in the United States and does not support
  Zero Data Retention (ZDR). Choosing a self-hosted sandbox does not make
  the Agents API ZDR-eligible."
- **Confidence**: settled (explicit, unambiguous product documentation)
- **Quote**: "The Agents API currently supports data residency only in the
  United States and does not support Zero Data Retention (ZDR). Choosing a
  self-hosted sandbox does not make the Agents API ZDR-eligible."
- **Our assessment**: This is a concrete, non-obvious compliance constraint
  that a regulated-industry practitioner (finance, healthcare, government)
  would need to know before adopting the Agents API in beta, and it is
  easy to miss because the raw `/responses` endpoint (used outside the
  Agents API) *does* support ZDR via `store=false`. Worth flagging for any
  guide section that discusses managed-agent data handling or compliance
  trade-offs versus self-hosted harnesses.

### Claim 7: Tool search loads relevant tool definitions on demand, reducing token usage and preserving the model's prompt cache; programmatic tool calling then lets agents run tool calls in parallel, chain operations, and filter results in code before bringing only relevant results back into context
- **Evidence**: Product description plus, in the linked Tool search guide, a
  mechanism description: `defer_loading: true` on functions/MCP servers,
  a `tool_search` tool type, hosted vs. client-executed search modes, and
  the explicit design constraint that "all tools are loaded at the end of
  the model's context window... to preserve the model's cache."
- **Confidence**: settled
- **Quote**: "Tool search loads relevant tool definitions as needed, helping
  reduce token usage and cost while preserving the model's cache. Once
  tools are available, programmatic tool calling lets agents run calls in
  parallel, chain related operations, and filter or combine results in
  code so they can work through large volumes of data while bringing only
  the relevant results back into context."
- **Our assessment**: The cache-preservation design detail (new tools always
  appended at the end of context, never inserted mid-context) is the kind
  of specific engineering constraint that's easy to get wrong when building
  a homegrown deferred-tool-loading system, since inserting a tool
  definition anywhere but the end invalidates the cached prefix for every
  subsequent turn. This is directly actionable guidance for Ch04 (Context
  Engineering) on how to implement tool search without destroying prompt
  caching.

### Claim 8: A named customer (Hypha, a financial-services company) reports the harness/sandbox separation reduced failed agent responses by 86%
- **Evidence**: Named customer testimonial with title (Lead Engineer) and
  company.
- **Confidence**: anecdotal (single self-reported customer metric in a
  vendor-published announcement, no methodology disclosed)
- **Quote**: "Earning customers' trust is critical in financial services.
  OpenAI's Agents API enables us to build more reliable agents, giving
  customers the confidence to use them in production. By separating the
  agent harness from the sandbox, we reduced failed agent responses by 86%."
- **Our assessment**: An 86% reduction is a striking number but comes with
  zero methodology (baseline definition, sample size, time window, what
  counted as a "failed agent response"). Treat as a directional signal that
  harness/sandbox separation can materially improve reliability, not as a
  benchmarked result. Consistent in direction with Claim 3's architectural
  description, but not independently verifiable from this source alone.

### Claim 9: The Agents API is built on the open-source Codex harness, giving developers visibility into the coordination logic even though OpenAI operates and maintains it as a managed service
- **Evidence**: Direct statement plus link to the public `openai/codex`
  GitHub repository.
- **Confidence**: settled
- **Quote**: "The Agents API is powered by the open-source Codex harness,
  giving developers visibility into the core logic that coordinates model
  calls, tools, and context. With the Agents API, OpenAI operates and
  maintains that harness while developers can inspect and learn from its
  public codebase."
- **Our assessment**: This partially offsets the auditability trade-off
  noted in Claim 5 (compaction items themselves are opaque, but the
  surrounding orchestration/coordination logic that decides *when* to
  compact, search tools, or spawn subagents is inspectable in the open
  Codex repo). It's a middle ground between Anthropic's and Google's fully
  closed managed-agent harnesses and a from-scratch self-built harness —
  worth noting as a third point on the "how much of your harness do you
  control" spectrum for Ch02.

### Claim 10: Multi-agent support lets the main agent delegate independent subtasks to subagents that run in parallel, each maintaining its own context, without the developer building their own orchestration
- **Evidence**: Product description plus, in the linked Multi-agent guide,
  concrete mechanics: `agent.multi_agent.enabled: true`, a
  `max_concurrent_subagents` limit (default 6, excluding the coordinator),
  harness-supplied tools to create/message/wait-for/interrupt subagents
  that the developer does not need to declare, and an explicit guardrail
  that "agents that edit the same files must coordinate their changes."
- **Confidence**: settled
- **Quote**: "With multi-agent support, the Agents API can break complex
  tasks into independent pieces and delegate them to subagents that work
  in parallel. Each subagent maintains its own context, helping it stay
  focused on its assignment, while the main agent coordinates their work
  and brings the results together."
- **Our assessment**: The explicit guidance to use subagents "for
  independent tasks, such as reviewing separate documents or investigating
  different causes of a failure" and to "keep short tasks and dependent
  steps in the main agent" is a concrete decision rule that lines up
  closely with the orchestrator-subagent pattern documented in
  `blog-anthropic-multi-agent-coordination-patterns.md` — independent
  first-party guidance from two competing labs converging on the same
  "delegate only genuinely independent subtasks" heuristic.

### Claim 11: One customer (Ciridae) reports the subagent support gave a 4x latency reduction and moved an evaluation score from 0.71 to 0.85, describing prior manual subagent orchestration as "cumbersome"
- **Evidence**: Named customer testimonial (CTO, Ciridae).
- **Confidence**: anecdotal (single self-reported customer metric, no
  methodology, benchmark, or baseline disclosed)
- **Quote**: "With the Agents API, our evaluation score went from 0.71 to
  0.85. The subagent support in the API is great and drastically sped up
  our workflow. Previously it was pretty cumbersome to observe and
  orchestrate subagents in our old setup but the new APIs gave us a 4x
  latency reduction."
- **Our assessment**: Like Claim 8, directionally interesting but not a
  controlled measurement — we don't know what "evaluation score" measures,
  what changed besides adopting the API (e.g., did they also change
  models?), or the sample size behind the 4x latency figure. Cite only as
  an anecdote of adoption motivation, not as a benchmarked capability
  claim.

### Claim 12: There are no additional fees for using the Agents API beyond standard token and tool costs — it is priced identically to direct model/tool usage
- **Evidence**: Direct pricing statement with link to the standard pricing
  page.
- **Confidence**: settled
- **Quote**: "There are no additional fees for using the Agents API – you
  simply pay for the tokens and tools your agents use, as outlined on our
  pricing page."
- **Our assessment**: This differs from Anthropic's Claude Managed Agents,
  which (per `blog-anthropic-claude-managed-agents.md`) charges a distinct
  session-hour rate ($0.08/session-hour) on top of model usage. If accurate
  and durable beyond the beta period, OpenAI's harness-as-a-service has a
  simpler and potentially cheaper cost model than Anthropic's — a concrete,
  checkable point of competitive contrast for any guide section comparing
  managed-agent platforms. Should be re-verified at GA, since beta pricing
  commonly changes.

## Concrete Artifacts

```javascript
// Single-call agent creation with MCP tool, multi-agent, and hosted sandbox
// (from openai.com/index/introducing-the-agents-api)
import OpenAI from "openai";

const client = new OpenAI();

const session = await client.beta.agents.sessions.create({
  agent: {
    model: "gpt-6-astra",
    tools: [
      {
        type: "mcp",
        server_label: "observability",
        transport: {
          type: "http",
          server_url: "https://observability.example.com/mcp",
        },
      },
    ],
    multi_agent: { enabled: true, max_concurrent_subagents: 3 },
  },
  vault_ids: ["vault_YOUR_VAULT_ID"],
  environment: {
    type: "openai_hosted",
    capability_directories: ["/workspace/capabilities/skills"],
  },
  input:
    "Investigate service-api's elevated 5xx rate over the last 30 minutes. " +
    "Delegate deployment, error, and dependency analysis to subagents. " +
    "Save findings, evidence, and recommended mitigation in /workspace/outputs.",
});
```

```
// Server-side compaction opt-in (from developers.openai.com/api/docs/guides/compaction)
const response = await client.responses.create({
  model: "gpt-5.3-codex",
  input: conversation,
  store: false,
  context_management: [{ type: "compaction", compact_threshold: 200_000 }],
});
```

```
// Deferred tool loading with tool search (from developers.openai.com/api/docs/guides/tools-tool-search)
{
  "tools": [
    {
      "type": "namespace",
      "name": "crm",
      "description": "CRM tools for customer lookup and order management.",
      "tools": [
        {
          "type": "function",
          "name": "list_open_orders",
          "description": "List open orders for a customer ID.",
          "defer_loading": true,
          "parameters": { "type": "object", "properties": { "customer_id": { "type": "string" } }, "required": ["customer_id"], "additionalProperties": false }
        }
      ]
    },
    { "type": "tool_search" }
  ]
}
```

```
Named sandbox partners (from openai.com/index/introducing-the-agents-api):
Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, Vercel
```

```
Named customer testimonials with quantified claims (from openai.com/index/introducing-the-agents-api):
- Ciridae (CTO): eval score 0.71 -> 0.85; "4x latency reduction" on subagent orchestration
- SafetyKit (Member of Technical Staff): "60% reduction in cost per case" after migrating case-review workflow
- Hypha (Lead Engineer): "reduced failed agent responses by 86%" via harness/sandbox separation
- Dwelly (Co-founder & CTO): fan-out across "hundreds of agents" run asynchronously for bursty workloads
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-managed-agents.md` and
    `blog-google-io-2026-developer-keynote.md` (Claim 3, Google's Managed
    Agents API) — all three frontier labs now ship a "single API call
    provisions a fully configured, harness-managed agent" product, with the
    harness hosted by the vendor and the compute environment optionally
    swappable. This is a converging industry pattern across Anthropic,
    Google, and now OpenAI within roughly five months.
  - `blog-anthropic-multi-agent-coordination-patterns.md` — OpenAI's
    subagent-delegation guidance ("use subagents for independent tasks...
    keep short tasks and dependent steps in the main agent") matches
    Anthropic's orchestrator-subagent decision criteria almost exactly,
    despite being independently authored by a competing lab.
  - `blog-cursor-continual-harness-improvement.md` — OpenAI's framing that
    "we maintain and continuously improve the harness alongside our
    models, helping your agents get better performance from every upgrade"
    matches Cursor's first-party account of continual harness evolution as
    a distinct engineering discipline from model improvement, though
    Cursor's post is about a self-built harness and OpenAI's is about a
    vendor-hosted one.
- **Contradicts**: None identified. No existing source note makes a claim
  that directly opposes anything extracted here.
- **Extends**:
  - `research-wasnotwas-context-compaction.md` — that source's comparative
    study covers seven *open-source* harnesses' compaction mechanics
    (thresholds, algorithms, cost) inspected via source code. This source
    adds an eighth data point (the Codex/Agents API harness) but the
    compaction *item itself* is explicitly documented as opaque and "not
    intended to be human-interpretable" — meaning this harness cannot be
    inspected the same way the wasnotwas study inspected the other seven,
    since it's exposed only through a managed API, not a readable
    codebase. This is a meaningful asymmetry worth noting alongside that
    study's table.
  - `blog-openai-agents-transforming-work.md` — that source covered
    OpenAI's internal Codex *adoption* telemetry (June 2026); this source
    covers the *infrastructure product* OpenAI is now selling externally,
    built on the same Codex harness referenced there. Complementary: one is
    usage evidence, the other is the productization of what generated that
    usage.
- **Novel**: The explicit architectural claim that compaction, tool search,
  and multi-agent orchestration are *harness-level* capabilities that
  improve automatically with each model launch via API versioning ("The
  Agents API provides versioned access to these capabilities with each
  model launch") — i.e., developers don't need to rewrite their harness to
  benefit from harness improvements, only to opt into a new API version.
  This versioned-harness-upgrade model is not described in this specific
  form (version-gated harness capability upgrades decoupled from model
  upgrades) in any other source note found in this corpus. Also novel: the
  explicit ZDR/data-residency limitation (Claim 6) and the nine-partner
  sandbox ecosystem (Claim 4), both concrete compliance/deployment details
  not present in the existing Anthropic or Google managed-agent source notes.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the Agents API as a third
  example (alongside Anthropic Claude Managed Agents and Google's Managed
  Agents API) of the "buy the harness, bring your own environment" pattern,
  citing Claim 3's explicit harness/sandbox decoupling and Claim 9's
  partial-transparency model (open-source coordination logic, opaque
  compaction internals) as a distinct middle position between fully closed
  managed harnesses and self-built ones.
- **Chapter 04 (Context Engineering)**: Cite Claim 7's cache-preservation
  design detail (deferred tools always appended at the *end* of context,
  never inserted mid-context) as a concrete implementation rule for anyone
  building their own tool-search/deferred-loading system — inserting
  definitions elsewhere breaks the cached prefix. Also cite Claim 5's
  contrast with `research-wasnotwas-context-compaction.md`: a managed
  compaction API trades auditability (you cannot inspect what the
  compaction step kept or discarded) for convenience (no compaction logic
  to build or maintain).
- **Chapter 05 (Team Adoption) / compliance-adjacent sections**: Flag Claim
  6's explicit ZDR/data-residency limitation as a concrete question
  practitioners in regulated industries need to ask before adopting any
  managed-agent API in beta — self-hosting the sandbox does not restore
  ZDR eligibility for the harness layer itself.

## Extraction Notes

- The primary announcement page (`openai.com/index/introducing-the-agents-api`)
  returned HTTP 403 to both direct `curl` and the WebFetch tool (bot
  protection). Retrieved via the Wayback Machine snapshot from 2026-09-19
  (`web.archive.org/web/20260919175740/...`), fetched with `curl` and
  converted to Markdown with `html2text` for verbatim quote extraction.
  Cross-checked the quoted customer testimonials and product-description
  text against this snapshot only; no live version of the page was
  accessible at extraction time.
- Followed four linked `developers.openai.com` docs pages for technical
  depth beyond the announcement's marketing framing, fetched directly (no
  403 encountered on these): the Agents API overview
  (`/api/docs/guides/agents-api/overview`), Compaction
  (`/api/docs/guides/compaction`), Tool search
  (`/api/docs/guides/tools-tool-search`), and Multi-agent
  (`/api/docs/guides/agents-api/multi-agent`). Did not follow the
  quickstart, pricing, self-hosted-environments, or programmatic-tool-calling
  pages beyond a brief check, staying within the ~5-link budget while
  prioritizing the pages that added claims not already stated in the
  announcement itself.
- All customer-testimonial metrics (Claims 8, 11, and the SafetyKit/Dwelly
  entries in Concrete Artifacts) are self-reported, vendor-published
  figures with no disclosed methodology. Flagged as anecdotal throughout;
  do not upgrade to settled/emerging without independent corroboration.
- The docs pages are large (400-700KB of raw HTML each, dominated by a
  shared sidebar-navigation tree common to the whole developer docs site);
  extracted only the page-specific content section after locating it via
  the page's own `<h1>` heading, to avoid quoting unrelated navigation text.
