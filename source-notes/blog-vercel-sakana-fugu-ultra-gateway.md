---
source_url: https://vercel.com/changelog/sakana-fugu-ultra-now-available-on-ai-gateway
source_type: blog-post
title: "Sakana Fugu Ultra now available on AI Gateway"
author: Rohan Taneja, Jerilyn Zheng (Vercel)
date_published: 2026-06-22
date_extracted: 2026-07-17
last_checked: 2026-07-17
status: current
confidence_overall: emerging
issue: "#1966"
---

# Sakana Fugu Ultra now available on AI Gateway

> Vercel's changelog announces Sakana AI's "Fugu Ultra" model on AI Gateway —
> notable not for the model itself but for its architecture: Fugu Ultra is
> marketed as a single model string (`sakana/fugu-ultra`) but is internally a
> pool of frontier models that dynamically routes each request to 1-3 of them
> and combines the results, a provider-side ensemble pattern with no prior
> example in this corpus. The announcement gives no benchmark scores, no
> per-token pricing for the model itself, and no detail on which models
> compose the pool.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published June 22, 2026; a 1-minute-read feature-announcement entry per the
  page's own read-time estimate — one of the shortest changelog entries
  encountered in this corpus, roughly 150 words of body text).
- **Author credibility**: First-party Vercel product announcement, byline
  Rohan Taneja and Jerilyn Zheng. Jerilyn Zheng is also a listed author on
  `blog-vercel-ai-gateway-api-key-budgets.md` and
  `blog-vercel-ai-gateway-production-index-may2026.md`, both already in this
  corpus, so this is the same changelog-authorship pattern Vercel uses for
  AI Gateway feature/model announcements. Vercel operates the AI Gateway
  product being described, so the integration mechanics (model string, SDK
  usage, pricing policy) are authoritative first-party documentation of a
  shipping capability. Sakana AI (the model's developer) is not itself a
  source of any claim here — Vercel is describing Sakana AI's product, not
  the reverse, and the architecture/benchmark claims about Fugu Ultra itself
  are Vercel repeating Sakana AI's marketing framing, not independently
  verified by Vercel.
- **Scope**: Covers the model's availability on AI Gateway, its
  headline architectural claim (multi-model routing/ensemble), one
  comparative capability claim, the AI SDK integration snippet, and AI
  Gateway's general platform features and pricing policy (reused boilerplate
  also present in Vercel's other AI Gateway changelog entries). Does NOT
  cover: which specific models compose the "pool," any named benchmark or
  score, per-token pricing for Fugu Ultra itself, context window size, release
  history for Sakana AI as a lab, or any usage/adoption data (contrast with
  `blog-vercel-ai-gateway-production-index-may2026.md`, which reports actual
  routing/spend telemetry — this entry is a same-day availability
  announcement with no telemetry).

## Extracted Claims

### Claim 1: Fugu Ultra is architected as a pool of multiple frontier models rather than a single model, dynamically routing each request to 1-3 of those models depending on the problem and combining their outputs into one answer
- **Evidence**: Direct architectural description in the changelog's opening
  paragraph about the model, stated as fact with no hedging language, but
  with no supporting detail on the routing mechanism, which models are in
  the pool, or how outputs are combined (e.g., voting, synthesis by an
  additional model, selection of the single best output).
- **Confidence**: emerging (first-party vendor description of a
  third-party model's architecture, restated without independent
  verification or technical elaboration — Vercel is passing along Sakana
  AI's own claim about its product, not something Vercel measured)
- **Quote**: "Fugu Ultra is built on a pool of publicly accessible frontier
  models, rather than running as a single model. It coordinates several
  models, routing work to 1-3 agents depending on the problem and combining
  their results into a single answer."
- **Our assessment**: This is the single most guide-relevant claim in the
  source: it describes a provider-side, request-level model ensemble
  exposed to the caller as one ordinary model string
  (`sakana/fugu-ultra` — see Claim 3). No existing corpus source documents
  this pattern — the closest analogs (`blog-anthropic-multi-agent-coordination-patterns.md`,
  `blog-vercel-ai-gateway-production-index-may2026.md` Claim 10) describe
  multi-model use at the *application/agent-orchestration* layer, where the
  calling code explicitly picks which model handles which task. Fugu Ultra
  moves that routing decision *inside* the model provider, below the
  application's visibility — from the caller's perspective, one API call to
  one model string may in fact invoke up to three different underlying
  models. The word "agents" in "routing work to 1-3 agents" is notably loose
  — it is unclear whether this means three copies of different models, three
  parallel instances of the same model, or something else; the changelog
  does not disambiguate.

### Claim 2: Fugu Ultra's capabilities are similar to those of Claude Mythos Preview and Fable 5, based on reasoning and scientific benchmarks
- **Evidence**: A single comparative sentence with no benchmark names, no
  numeric scores, and no methodology disclosed.
- **Confidence**: anecdotal (an unsubstantiated comparative marketing claim
  — "reasoning and scientific benchmarks" is not a specific, named benchmark
  suite, and no scores are given for Fugu Ultra, Mythos Preview, or Fable 5
  in this source)
- **Quote**: "Based on reasoning and scientific benchmarks, Fugu Ultra has
  capabilities similar to those of Claude Mythos Preview and Fable 5."
- **Our assessment**: This is the weakest claim in the source and should not
  be repeated in the guide as if it were a measured result. It positions
  Fugu Ultra at frontier tier by comparing it to two Anthropic models already
  well-documented in this corpus (`blog-simonwillison-claude-fable-5.md`,
  `blog-simonwillison-fable-mythos-access-directive.md`), but provides zero
  independently checkable evidence. If this comparison becomes relevant to a
  guide claim, it needs a dedicated benchmark source (e.g., a
  third-party leaderboard or Sakana AI's own model card), not this changelog
  entry.

### Claim 3: Fugu Ultra is invoked through the Vercel AI SDK by setting the `model` parameter to the string `sakana/fugu-ultra`, exactly like any other single AI Gateway model
- **Evidence**: A verbatim TypeScript code example using `streamText` from
  the `ai` package.
- **Confidence**: settled (first-party documentation of a shipping SDK
  integration surface, directly verifiable by any developer with Gateway
  access)
- **Quote**: "To use Fugu Ultra, set `model` to `sakana/fugu-ultra` in AI
  SDK" — see Concrete Artifacts for the full code block.
- **Our assessment**: This confirms the "opaque ensemble behind a single
  model string" framing from Claim 1: the integration surface gives the
  calling application no way to see, select, or constrain which of the 1-3
  underlying models actually served a given request — it is indistinguishable
  at the API level from calling any other single AI Gateway model. For a
  team building evals or debugging output variance, this is a meaningful
  reproducibility caveat that the changelog does not itself raise.

### Claim 4: AI Gateway provides a unified API across models along with usage/cost tracking, retry and failover configuration, and performance optimizations Vercel describes as delivering "higher-than-provider uptime"
- **Evidence**: Standard platform-description paragraph, reused boilerplate
  consistent with Vercel's other AI Gateway changelog entries already in
  this corpus.
- **Confidence**: settled (first-party description of shipping platform
  capabilities, corroborated by the mechanics already documented in
  `blog-vercel-ai-gateway-api-key-budgets.md`)
- **Quote**: "AI Gateway provides a unified API for calling models, tracking
  usage and cost, and configuring retries, failover, and performance
  optimizations for higher-than-provider uptime."
- **Our assessment**: Adds nothing new to the corpus's existing AI Gateway
  platform description — this is boilerplate that also appears (in
  substance, if not verbatim) in the budgets changelog entry. Recorded here
  for completeness since it is part of this entry's verbatim text, not
  because it is novel.

### Claim 5: AI Gateway includes built-in custom reporting, Zero Data Retention (ZDR) support, and budgets for API keys as named platform features, with "and more" left unspecified
- **Evidence**: A single sentence naming three specific features by name,
  each as a hyperlinked term in the original page (custom reporting, Zero
  Data Retention support, budgets for API keys).
- **Confidence**: settled (first-party feature list; the "budgets for API
  keys" feature is independently and much more thoroughly documented in
  `blog-vercel-ai-gateway-api-key-budgets.md`, giving direct corroboration
  that this feature is real and shipping, not just named in passing here)
- **Quote**: "It includes built-in custom reporting, Zero Data Retention
  support, budgets for API keys, and more."
- **Our assessment**: This is a low-detail restatement of a feature this
  corpus already documents in depth (`blog-vercel-ai-gateway-api-key-budgets.md`).
  The value of this claim is purely corroborative — it confirms the budgets
  feature is still live and being actively cross-promoted in new-model
  announcements roughly two weeks after its own changelog entry
  (2026-06-09 to 2026-06-22).

### Claim 6: AI Gateway reflects provider pricing with no markup and charges no platform fee on inference, including on Bring Your Own Key (BYOK) requests
- **Evidence**: Direct pricing-policy statement, presented as a general AI
  Gateway policy rather than specific to Fugu Ultra.
- **Confidence**: settled (first-party pricing policy statement — a
  falsifiable claim about what Vercel charges, not a marketing generality)
- **Quote**: "AI Gateway reflects provider pricing with no markup and does
  not charge a platform fee on inference, including on Bring Your Own Key
  (BYOK) requests."
- **Our assessment**: Notable in combination with Claim 1: if Fugu Ultra
  internally routes a single request across up to three models, and Vercel
  passes through "provider pricing" with "no markup," it's unclear from this
  source alone whether a caller is billed for one model's worth of tokens or
  for the sum of all models Fugu Ultra invokes internally for that request.
  The changelog does not address this, and no per-token price for
  `sakana/fugu-ultra` is given anywhere in the source — a concrete gap a
  cost-governance-focused guide section should flag rather than assume away.

### Claim 7: Fugu Ultra is discoverable via a model playground for testing and via the AI Gateway model leaderboard, which ranks the most popular models over time by total token volume processed across all Gateway traffic
- **Evidence**: Two closing calls-to-action in the changelog, one linking to
  a Fugu-Ultra-specific playground page, one to the general Gateway
  leaderboard.
- **Confidence**: settled (first-party documentation of existing product
  surfaces — the leaderboard mechanism, ranking by token volume, is
  consistent with the aggregate volume-share data already reported in
  `blog-vercel-ai-gateway-production-index-may2026.md`)
- **Quote**: "Try Sakana Fugu Ultra in the model playground." / "The AI
  Gateway model leaderboard tracks the most popular models over time,
  ranking them by the total volume of tokens processed across all Gateway
  traffic."
- **Our assessment**: Confirms that Vercel's leaderboard ranks strictly by
  token volume, not by spend — consistent with, and a useful precision
  addition to, the volume/spend distinction already central to
  `blog-vercel-ai-gateway-production-index-may2026.md` (e.g., that report's
  Claim 1, where DeepSeek reached 17% token share on ~1% spend share; a
  volume-ranked leaderboard would show DeepSeek prominently despite its
  low spend contribution).

### Claim 8: Sakana AI is a named model provider newly listed on AI Gateway, using the provider prefix `sakana/` in the model string
- **Evidence**: The model string `sakana/fugu-ultra` and the explicit
  attribution "Sakana Fugu Ultra from Sakana AI."
- **Confidence**: settled (directly stated provider attribution and
  namespace prefix, consistent with how other AI Gateway model strings are
  namespaced by provider, e.g. `deepseek/deepseek-v4-flash` per
  `blog-vercel-ai-gateway-production-index-may2026.md`)
- **Quote**: "Sakana Fugu Ultra from Sakana AI is now available on AI
  Gateway." (from the page's meta description, matching the article's
  opening sentence)
- **Our assessment**: This is the first mention of Sakana AI as an AI
  Gateway model provider anywhere in this corpus. Unlike the low-cost-tier
  entrants documented in `blog-vercel-ai-gateway-production-index-may2026.md`
  (DeepSeek, and by reference Qwen and Kimi), Sakana AI is positioned at
  frontier-tier capability (Claim 2) rather than as a price-disruption play
  — the changelog gives no pricing figure that would let a reader judge
  whether it is also cost-competitive, unlike DeepSeek V4's clearly stated
  $0.14/$0.28 per-million-token pricing in that note.

## Concrete Artifacts

### Full verbatim article body (changelog page, 2026-06-22)

```
Sakana Fugu Ultra now available on AI Gateway
By Rohan Taneja, Jerilyn Zheng — 22 Jun 2026 — 1 min read

Sakana Fugu Ultra from Sakana AI is now available on AI Gateway.

Fugu Ultra is built on a pool of publicly accessible frontier models, rather
than running as a single model. It coordinates several models, routing work
to 1-3 agents depending on the problem and combining their results into a
single answer.

Based on reasoning and scientific benchmarks, Fugu Ultra has capabilities
similar to those of Claude Mythos Preview and Fable 5.

To use Fugu Ultra, set model to sakana/fugu-ultra in AI SDK:

import { streamText } from 'ai';
const result = streamText({
  model: 'sakana/fugu-ultra',
  prompt: 'Review this pull request and flag correctness bugs.',
});

AI Gateway provides a unified API for calling models, tracking usage and
cost, and configuring retries, failover, and performance optimizations for
higher-than-provider uptime. It includes built-in custom reporting, Zero
Data Retention support, budgets for API keys, and more.

AI Gateway reflects provider pricing with no markup and does not charge a
platform fee on inference, including on Bring Your Own Key (BYOK) requests.

Try Sakana Fugu Ultra in the model playground.

AI Gateway: Track top AI models by usage
The AI Gateway model leaderboard tracks the most popular models over time,
ranking them by the total volume of tokens processed across all Gateway
traffic. View the leaderboard.
```
*Source: https://vercel.com/changelog/sakana-fugu-ultra-now-available-on-ai-gateway
(retrieved via direct HTTP fetch of the raw page HTML, article body
extracted from the rendered DOM text, not from an AI-summarized
intermediate — see Extraction Notes)*

### AI SDK integration snippet (verbatim)

```typescript
import { streamText } from 'ai';
const result = streamText({
  model: 'sakana/fugu-ultra',
  prompt: 'Review this pull request and flag correctness bugs.',
});
```
*Source: same as above*

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-gateway-api-key-budgets.md`,
`blog-vercel-ai-gateway-production-index-may2026.md`,
`blog-anthropic-multi-agent-coordination-patterns.md`, and
`blog-anthropic-opus47-hackathon-winners.md` were re-read directly and the
claim numbers cited below were confirmed against each note's own numbered
`### Claim N:` headings (or, for the hackathon note, the specific paragraph
cited) before writing this section.

- **Corroborates**:
  - `blog-vercel-ai-gateway-api-key-budgets.md` (the entire note): this
    source's Claim 5 ("budgets for API keys" listed as a live AI Gateway
    feature) confirms the budgets feature, launched 2026-06-09, was still
    active and being cross-promoted in a new-model announcement on
    2026-06-22 — thin corroboration, but a genuine confirmation that the
    feature shipped and persisted rather than being a one-off announcement.
  - `blog-vercel-ai-gateway-production-index-may2026.md` Claim 10 (at 1M+
    monthly requests, most apps route across 11+ distinct models): that
    claim documents multi-model use as an *application-level* architecture
    decision (the calling app explicitly integrates many models). This
    source's Claim 1 describes multi-model use one layer lower — a single
    model string that is itself a multi-model router. Both describe "more
    than one model touches a given request" as an increasingly normal
    pattern in production AI systems, just at different architectural
    layers.
  - `blog-vercel-ai-gateway-production-index-may2026.md` Claim 1 (DeepSeek's
    17% token share on ~1% spend share): this source's Claim 7 (leaderboard
    ranks strictly by token volume, not spend) explains the mechanism by
    which a low-spend-share model like DeepSeek would still appear
    prominently on the leaderboard Vercel points readers to here.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about Sakana AI, Fugu Ultra, or provider-side model-ensemble products that
  this source disagrees with.

- **Extends**: `blog-anthropic-multi-agent-coordination-patterns.md`
  (the five-pattern taxonomy: generator-verifier, orchestrator-subagent,
  agent teams, message bus, shared state): all five patterns in that
  taxonomy assume the application/orchestration layer explicitly controls
  which model instance does which piece of work. This source describes a
  provider-side pattern that sits *underneath* that entire taxonomy — from
  the calling application's point of view, `sakana/fugu-ultra` looks like a
  single leaf model, but the coordination-and-combination behavior that
  taxonomy names at the agent layer (specifically, something resembling
  generator-verifier or a lightweight orchestrator dispatching to 1-3
  workers) is, per Claim 1, happening invisibly inside the model provider
  itself. This is a genuinely new layer for the corpus's multi-model
  coordination material: "ensemble as a product feature of a single model
  endpoint" versus "ensemble as an architecture the application team
  builds."
  `blog-anthropic-opus47-hackathon-winners.md` (a hackathon team's use of
  parallel agent runs for "ensemble diagnosis," cited around line 250 of
  that note): that is an application team deliberately running the *same*
  model multiple times in parallel and combining results — the calling code
  owns and sees the ensemble. Fugu Ultra inverts this: the ensemble (of
  *different* models, per Claim 1) is owned and hidden by the provider, and
  the calling code sees only one model call. The two are structurally
  opposite implementations of "combine multiple runs/models for a better
  answer," useful as a contrast pair for a guide section on ensemble
  patterns at different architectural layers.

- **Novel**:
  - **Provider-side, request-level model ensemble marketed as a single
    model** (Claim 1, Claim 3): no prior corpus source documents an AI
    provider shipping a product where one model string opaquely invokes and
    combines 1-3 different underlying frontier models per request. This is
    architecturally distinct from every multi-model pattern previously
    extracted (application-level routing, agent-orchestration taxonomies,
    or ensemble-via-repeated-calls).
  - **Sakana AI as a named AI Gateway model provider** (Claim 8): the first
    corpus mention of this lab, positioned at frontier capability tier
    rather than as a low-cost entrant.
  - **Ambiguous billing implication of opaque internal multi-model routing**
    (Claim 6, "Our assessment"): a previously-unraised question for this
    corpus's cost-governance material — how a "no markup, provider pricing"
    policy applies when the provider itself invokes multiple models per
    request behind a single billed call.

## Guide Impact

- **Chapter 02 (Harness Engineering — model selection)**: Add
  provider-side model-ensemble products (Claim 1) as a distinct, newer
  category practitioners now need to account for when selecting or
  benchmarking a model: the model string a team chooses may not correspond
  to a single, stable, reproducible model — it may itself be a dynamic
  router over several frontier models with provider-controlled selection
  logic that can change without notice. Flag the reproducibility and
  eval-design implication directly from Claim 3's "Our assessment": teams
  building evals against `sakana/fugu-ultra` cannot assume a fixed model is
  being tested run-to-run. Explicitly caveat Claim 2's benchmark comparison
  as unsubstantiated vendor marketing, not a citable capability claim, per
  MINER.md's confidence grading.

- **Chapter 04 (multi-agent coordination material, alongside
  `blog-anthropic-multi-agent-coordination-patterns.md`)**: Add a short note
  distinguishing "ensemble as an application-owned architecture pattern"
  (the five-pattern taxonomy, and the hackathon team's parallel-run
  diagnosis) from "ensemble as a provider-owned product feature hidden
  behind a single model call" (Fugu Ultra). This is a layering distinction
  worth making explicit so readers don't conflate the two when reasoning
  about where coordination complexity and failure modes actually live.

- **Chapter [Cost Engineering, wherever `blog-vercel-ai-gateway-api-key-budgets.md`
  and `blog-vercel-ai-gateway-production-index-may2026.md` are cited]**: Note
  the open billing question from Claim 6 as a gap worth flagging rather than
  assuming — "provider pricing, no markup" is documented, but this source
  does not resolve whether a request that internally invokes multiple models
  is billed as one model-call's worth of tokens or the sum across all models
  Fugu Ultra invokes for that request.

## Extraction Notes

1. **WebFetch summarization discarded; source fetched via direct HTTP
   instead.** An initial WebFetch pass on the changelog URL returned a
   plausible-looking but non-verbatim summary (correct in substance, but
   phrased as an AI-generated "content summary" rather than the page's
   actual words, and it did not surface the exact byline, publish date
   format, or read-time estimate). Per MINER.md §2a, this note discarded
   that output and instead retrieved the raw page HTML via a direct `curl`
   request (`/tmp/sakana.html`, 430KB, HTTP 200), located the rendered
   article body inside the page's DOM markup, and stripped tags to recover
   the plain text. Every `Quote` field and the full verbatim article body in
   Concrete Artifacts is taken from that directly-fetched HTML, not from the
   WebFetch summarization.
2. **No linked sub-pages followed.** The changelog links to a Fugu-Ultra
   model playground page and the general AI Gateway leaderboard, both
   interactive product surfaces rather than substantive additional text
   content (no further prose to extract), so neither was fetched as a
   sub-page per MINER.md §1's "linked pages that seem substantive"
   guidance — they are recorded as claims (Claim 7) about their existence
   and function, not as separate sources.
3. **Source is genuinely thin.** At ~150 words of body text and a
   self-reported "1 min read," this is one of the shortest sources
   extracted into this corpus. Eight claims were still extracted by treating
   every substantive sentence (including the reused platform-boilerplate
   paragraphs) as a distinct, separately-gradable claim, but readers should
   not expect this note to contain deep technical detail — it doesn't exist
   in the source. No contradiction issue was filed; none of this source's
   claims materially oppose an existing note.
4. **Confidence calibration: emerging.** The integration mechanics, feature
   list, and pricing policy (Claims 3-8) are settled first-party product
   documentation, directly verifiable and consistent with prior corpus
   entries from the same changelog family. But the note's two most
   guide-relevant claims — the architectural description of Fugu Ultra as a
   multi-model ensemble (Claim 1) and its capability comparison to Claude
   Mythos Preview and Fable 5 (Claim 2) — are Vercel repeating a
   third-party lab's own claims about its product with zero independent
   verification, benchmark names, or scores. The overall note is graded
   "emerging" rather than "settled" to reflect that its most interesting
   content is the least independently verified.
