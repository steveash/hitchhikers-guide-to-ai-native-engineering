---
source_url: https://vercel.com/changelog/nemotron-3-ultra-now-available-on-ai-gateway
source_type: blog-post
title: "Nemotron 3 Ultra now available on AI Gateway"
author: Walter Korman, Rohan Taneja, Jerilyn Zheng (Vercel)
date_published: 2026-06-04
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: emerging
issue: "#1569"
---

# Nemotron 3 Ultra now available on AI Gateway

> Vercel changelog announcing Nvidia's Nemotron 3 Ultra (550B-parameter open MoE reasoning
> model, `nvidia/nemotron-3-ultra-550b-a55b`) on Vercel AI Gateway — a distinct, larger sibling
> to the previously-documented Nemotron 3 Super 120B, explicitly positioned for long-running
> agent orchestration (planning, tool use, sub-agent delegation, error recovery) with a 1M
> token context window, up to 350 tok/s throughput, and up to 30% lower cost on agentic tasks.

## Source Context

- **Type**: blog-post (product changelog / availability announcement)
- **Author credibility**: Written by named Vercel staff (Walter Korman, Rohan Taneja, Jerilyn
  Zheng) as an official product changelog entry. Authoritative for what is now available on
  Vercel's own platform (model ID, AI Gateway feature set, pricing/markup policy) and for
  quoting Nvidia's own positioning language for the model. Not authoritative for independent
  benchmark validation of the model's capabilities — no third-party or Nvidia benchmark
  numbers (comparable to Nemotron 3 Super's PinchBench/RULER scores) are included in this
  piece; it is a platform-availability announcement, not a model technical report.
- **Scope**: Covers (1) Nemotron 3 Ultra's headline specs and positioning as reported by
  Vercel, (2) how to invoke it via the Vercel AI SDK, (3) AI Gateway's general feature set
  (unified API, cost/usage tracking, retries/failover, custom reporting, Zero Data Retention,
  dynamic provider sorting, no-markup pricing, BYOK). Does NOT cover: Nemotron 3 Ultra's
  architecture details, training data, benchmark scores, license terms, or how it compares
  to Nemotron 3 Super — none of that is in this source.

## Extracted Claims

### Claim 1: Nemotron 3 Ultra is a 550B-parameter open Mixture-of-Experts reasoning model built specifically for orchestrating long-running agent workflows, with a 1M token context window
- **Evidence**: Vercel's own product description in the changelog body, plus the model
  identifier itself (`nemotron-3-ultra-550b-a55b`, where the `550b` denotes total parameters
  and `a55b` denotes active parameters per token — the same MoE naming convention used
  elsewhere in the corpus, e.g. `blog-thebatch-nemotron-agent-infra.md` Claim 3's "120B
  total, 12B active" for Nemotron 3 Super).
- **Confidence**: emerging (vendor/platform positioning language, not independently
  benchmarked in this source)
- **Quote**: "Nemotron 3 Ultra is an open Mixture-of-Experts reasoning model built for orchestrating long-running agent workflows, with a 1M token context window."
- **Our assessment**: The 550B/55B active split makes Ultra roughly 4.6x larger in total
  parameters and active parameters than Nemotron 3 Super (120B/12B). This is a materially
  different model, not a rebrand or minor revision of Super — consistent with Prospector's
  triage note that Ultra and Super are "a distinct model" with "different positioning." The
  1M token context window matches Super's context window exactly (per
  `blog-thebatch-nemotron-agent-infra.md` Claim 4's RULER 1M-token benchmark), suggesting
  Nvidia is standardizing on 1M tokens as the context target across the Nemotron 3 family
  regardless of size tier.

### Claim 2: The model explicitly targets four agentic sub-tasks — planning, tool use, sub-agent delegation, and error recovery
- **Evidence**: Direct product-positioning language in the changelog body.
- **Confidence**: emerging (positioning claim, not validated against a benchmark in this
  source)
- **Quote**: "The model targets multi-turn agent workflows: planning, tool use, sub-agent delegation, and error recovery."
- **Our assessment**: This is a more specific agentic-capability claim than Nemotron 3
  Super's positioning (per `blog-thebatch-nemotron-agent-infra.md` Claim 5, Super ships
  "native tool calling, structured outputs, and three reasoning modes" but is not
  specifically marketed around sub-agent delegation or error recovery). "Sub-agent
  delegation" as a named first-class capability is new to the corpus's Nemotron coverage —
  it implies Nvidia is tuning Ultra for orchestrator/supervisor roles in multi-agent
  systems specifically, not just single-agent tool use. No benchmark accompanies this claim
  in this source, so it should be treated as a design target rather than a validated result.

### Claim 3: Nemotron 3 Ultra reaches throughput of up to 350 tokens per second, with up to 30% lower cost on agentic tasks
- **Evidence**: Vercel's changelog body states both figures together as a single sentence;
  no baseline comparison model is named for either figure.
- **Confidence**: anecdotal (single-source figures with no stated comparison baseline or
  benchmark methodology — unlike Nemotron 3 Super's throughput claim, which named specific
  comparison models: gpt-oss-120b at 278 tok/s and Gemini 3.1 Flash-Lite at 266 tok/s, per
  `blog-thebatch-nemotron-agent-infra.md` Claim 1)
- **Quote**: "Throughput reaches up to 350 tokens per second, with up to 30% lower cost on agentic tasks."
- **Our assessment**: 350 tok/s is notably lower than Nemotron 3 Super's reported 442 tok/s
  (`blog-thebatch-nemotron-agent-infra.md` Claim 1) — expected, since Ultra's active
  parameter count (~55B) is roughly 4.6x Super's (12B), and inference throughput typically
  scales inversely with active parameters for MoE models at comparable hardware. This is
  not a contradiction between sources (different models, not competing claims about the
  same model) but it is a useful trade-off data point for model selection: Ultra offers
  more capacity/capability at the cost of throughput relative to Super. The "30% lower cost"
  claim has no stated baseline (lower than what — Super? closed-weights frontier models?
  Ultra's own list price via a different provider?) and no supporting benchmark, so it
  should not be treated as a settled comparative figure.

### Claim 4: Nemotron 3 Ultra is invoked in the Vercel AI SDK by setting the model identifier to `nvidia/nemotron-3-ultra-550b-a55b`
- **Evidence**: Explicit instruction plus a `streamText` code example in the changelog body.
- **Confidence**: settled (concrete, verifiable configuration instruction from the platform
  vendor)
- **Quote**: "To use Nemotron 3 Ultra, set model to nvidia/nemotron-3-ultra-550b-a55b in the AI SDK."
- **Our assessment**: This is a directly actionable integration detail for teams already
  using the Vercel AI SDK — no separate Nvidia API account or NIM deployment is implied;
  the model is called through Vercel's existing `streamText`/`generateText` interface like
  any other AI Gateway model.

### Claim 5: AI Gateway provides a single unified API for calling models across providers, with usage/cost tracking and configurable retries, failover, and performance optimizations aimed at higher-than-provider uptime
- **Evidence**: Vercel's own platform description in the changelog body.
- **Confidence**: settled (platform feature description from the vendor operating the
  platform)
- **Quote**: "AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime."
- **Our assessment**: The "higher-than-provider uptime" framing is notable — it positions
  AI Gateway's retry/failover layer as actively compensating for individual provider outages
  by routing around them, not merely load-balancing. For teams building production agent
  harnesses, this is a specific claim about resilience that would need independent
  verification (e.g., does failover happen transparently mid-request, or only on new
  requests?) before being relied on for SLA-sensitive deployments.

### Claim 6: AI Gateway includes built-in custom reporting, Zero Data Retention (ZDR) support, and dynamic provider sorting by latency and cost
- **Evidence**: Listed as built-in features in the changelog body, each linking to a
  dedicated Vercel changelog/blog post (custom reporting, ZDR, and provider sorting are each
  documented in their own separate Vercel posts referenced from this one).
- **Confidence**: settled (feature list from the platform vendor)
- **Quote**: "It includes built-in custom reporting, Zero Data Retention support, dynamic provider sorting by latency and cost, and more."
- **Our assessment**: Zero Data Retention support is directly relevant to enterprise
  governance discussions in the guide (Ch05-adjacent): it signals that AI Gateway can be
  configured so that request/response payloads are not retained by the gateway or
  (presumably) the underlying provider, which matters for teams routing sensitive data
  through third-party model APIs. This source only names the feature and links to a
  separate post — it does not describe ZDR's scope or guarantees in enough depth to extract
  further without reading that linked post, which is out of scope for this extraction.

### Claim 7: AI Gateway reflects provider pricing with no markup and charges no platform fee on inference, including for Bring Your Own Key (BYOK) requests
- **Evidence**: Stated directly as a pricing policy in the changelog body.
- **Confidence**: settled (pricing policy stated by the platform vendor)
- **Quote**: "AI Gateway reflects provider pricing with no markup and does not charge a platform fee on inference, including on Bring Your Own Key (BYOK) requests."
- **Our assessment**: This extends the BYOK pattern already documented in the corpus for
  GitHub Copilot surfaces (`docs-github-copilot-byok-app.md` Claim 1, `docs-github-copilot-byok-vscode.md`)
  to a different category of product: a model-routing gateway rather than an IDE/agent
  product. The no-markup-on-BYOK claim is a meaningful differentiator for cost-conscious
  teams: it means using AI Gateway as a routing layer over an existing provider API key
  does not add a Vercel margin on top of the provider's own per-token price — the value
  proposition is purely the routing/observability/failover layer, not price arbitrage.

### Claim 8: Vercel positions AI Gateway as eliminating the need to set up separate accounts with each individual model provider
- **Evidence**: The page's meta description (used for search/social previews, written by
  Vercel to summarize the article) states this framing; it does not appear verbatim in the
  visible article body text.
- **Confidence**: anecdotal (marketing/summary copy, not elaborated in the article body)
- **Quote**: "You can now access Nvidia's Nemotron 3 Ultra on Vercel's AI Gateway with no markup and no other provider accounts required."
- **Our assessment**: This implies Vercel account credentials alone are sufficient to call
  Nemotron 3 Ultra — no separate Nvidia NIM/build.nvidia.com account or API key needed. This
  is consistent with Claim 4's `streamText` example, which shows no Nvidia-specific
  authentication step. If accurate, this lowers the setup cost for teams evaluating Nemotron
  3 Ultra relative to going directly through Nvidia's own hosting.

## Concrete Artifacts

### Vercel AI SDK code example (verbatim from changelog)

```typescript
import { streamText } from 'ai';

const result = streamText({
  model: 'nvidia/nemotron-3-ultra-550b-a55b',
  prompt: 'Plan and run a multi-step research task and synthesize a report.',
});
```

### Nemotron 3 Ultra headline specs (as reported by Vercel, June 4, 2026)

```
Model ID:        nvidia/nemotron-3-ultra-550b-a55b
Provider:        Nvidia
Architecture:    Open Mixture-of-Experts reasoning model (550B total / 55B active, per model ID)
Context window:  1,000,000 tokens
Throughput:      Up to 350 tokens/second
Cost:            Up to 30% lower cost on agentic tasks (baseline unstated)
Positioning:     "orchestrating long-running agent workflows" —
                 planning, tool use, sub-agent delegation, error recovery
Availability:    Vercel AI Gateway, via AI SDK `streamText`/model string
Published:       2026-06-04 (Vercel changelog)
Authors:         Walter Korman, Rohan Taneja, Jerilyn Zheng
```

### AI Gateway feature list (as described in this changelog)

```
- Unified API for calling models across providers
- Usage and cost tracking
- Configurable retries, failover, performance optimizations
- Custom reporting (linked: vercel.com/changelog/custom-reporting-ai-gateway)
- Zero Data Retention support (linked: vercel.com/blog/zdr-on-ai-gateway)
- Dynamic provider sorting by latency and cost
  (linked: vercel.com/changelog/sort-providers-by-cost-latency-or-throughput-on-ai-gateway)
- No markup on provider pricing; no platform fee on inference (incl. BYOK)
```

## Cross-References

- **Extends**: `blog-thebatch-nemotron-agent-infra.md` — That note's Claims 1-6 cover
  Nemotron 3 Super 120B (120B total/12B active, 442 tok/s, PinchBench 85.6%, RULER 91.75%
  at 1M tokens, native tool calling/structured outputs/reasoning modes, permissive
  commercial license). This source documents Nemotron 3 Ultra as a separate, larger model
  in the same family (550B total/55B active per the model ID), sharing the 1M-token context
  target but trading throughput (350 vs. 442 tok/s) for scale, and adding "sub-agent
  delegation" as an explicitly named capability not called out for Super. Neither source
  states whether Ultra supersedes, complements, or is priced/licensed differently than
  Super — that gap remains open for a future source to fill.
- **Corroborates**: `docs-github-copilot-byok-app.md` Claim 1, `docs-github-copilot-byok-vscode.md`
  — Both document BYOK as a pattern for routing agent/IDE traffic through externally-held
  provider credentials without vendor markup or lock-in to a single provider. This source
  shows the same BYOK-no-markup pattern applied at the model-gateway layer (Vercel AI
  Gateway) rather than the IDE/agent-product layer, suggesting "no markup on BYOK" is
  becoming a common competitive baseline across different categories of AI infrastructure
  product.
- **Contradicts**: None identified. No existing source note makes a claim about Nemotron 3
  Ultra specifically, or about Vercel AI Gateway's pricing/feature set, that this source
  disagrees with.
- **Novel**: 
  - Nemotron 3 Ultra itself (550B/55B-active variant) is entirely new to the corpus — the
    only prior Nemotron coverage (`blog-thebatch-nemotron-agent-infra.md`) is about the
    120B/12B-active Super variant.
  - Vercel AI Gateway's specific feature set (unified API, cost/usage tracking, dynamic
    provider sorting by latency/cost, Zero Data Retention, no-markup BYOK pricing) is not
    previously documented anywhere in the corpus. This is the first source note describing
    a commercial model-routing gateway product's feature set and pricing policy.
  - "Sub-agent delegation" and "error recovery" as explicitly named, marketed model
    capabilities (as opposed to general "tool use" or "agentic tasks") are new framing to
    the corpus's model-selection coverage.

## Guide Impact

- **Chapter on Model Selection**: Add Nemotron 3 Ultra as a second Nemotron 3 data point
  alongside Super (already cited via `blog-thebatch-nemotron-agent-infra.md`), explicitly
  flagging the trade-off this source reveals: Ultra is ~4.6x larger (550B/55B active vs.
  120B/12B active) with the same 1M-token context target but lower reported throughput
  (350 vs. 442 tok/s). Flag the "up to 30% lower cost on agentic tasks" and "up to 350
  tok/s" figures as vendor/platform-reported with no stated baseline or benchmark
  methodology — weaker evidence than Super's PinchBench/RULER comparisons, which at least
  named comparison models. Recommend noting this as an open question for a future source:
  whether Ultra is meant to replace Super for agentic workloads or serve a different
  (higher-capability, higher-latency) tier.
- **Chapter on Agent Infrastructure / Deployment**: Vercel AI Gateway's feature set (unified
  API across providers, no-markup BYOK, dynamic provider sorting by latency/cost, Zero Data
  Retention) is a concrete example of a commercial model-gateway product relevant to any
  discussion of how teams route agent traffic across multiple model providers without
  building custom routing/failover logic. This is the first corpus source describing this
  category of product in any depth; recommend citing it as a reference point when discussing
  build-vs-buy decisions for model routing infrastructure.

## Extraction Notes

- This is a short product changelog (roughly 4 paragraphs of body text plus a code sample),
  not a technical deep-dive — consistent with Prospector's triage assessment across all
  three triage comments on this issue ("primarily a product availability announcement,"
  "infrastructure/availability announcement," "likely to be a short product announcement").
  I fetched and read the full rendered article (via WebFetch) and cross-checked every quoted
  passage against the raw page HTML (via curl) to confirm verbatim accuracy — the HTML
  contains the article body as both server-rendered markup and an embedded Contentful JSON
  payload, which let me confirm exact wording character-for-character.
- The source does not mention Nemotron 3 Super, so any comparison between Ultra and Super
  in this note is my own analysis (in "Our assessment" fields), cross-referencing the
  separately-sourced `blog-thebatch-nemotron-agent-infra.md`, not a claim made by this
  source itself.
- I did not follow the three linked sub-pages (custom reporting, ZDR, provider-sorting
  changelog posts) or the AI Gateway docs/leaderboard/playground links, since Prospector's
  triage scoped this issue to the Nemotron 3 Ultra announcement itself and MINER.md's
  "follow up to 5 linked pages" guidance is for pages that seem substantive to the source's
  own claims — these are generic AI Gateway feature pages, not elaborations specific to
  this model announcement. A future source note on AI Gateway's ZDR or provider-sorting
  features specifically should read those pages directly.
- No benchmark data (comparable to Super's PinchBench/RULER figures) is available in this
  source for Ultra. If Nvidia has published an official model card or benchmark comparison
  for Nemotron 3 Ultra elsewhere, that would be a stronger source for the Model Selection
  chapter than this changelog and should be mined separately.
- I did not find any existing `contradiction`-labeled issue or `C-NNN` entry in
  CONTRADICTIONS.md touching Nemotron or Vercel AI Gateway, and this source does not
  materially contradict any existing source note (it covers a different, previously
  undocumented model and product), so no contradiction issue was filed per MINER.md §4a.
