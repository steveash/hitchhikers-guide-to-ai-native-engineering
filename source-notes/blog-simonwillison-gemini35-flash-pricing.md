---
source_url: https://simonwillison.net/2026/May/19/gemini-35-flash/
source_type: blog-post
title: "Gemini 3.5 Flash: more expensive, but Google plan to use it for everything"
author: Simon Willison
date_published: 2026-05-19
date_extracted: 2026-05-28
last_checked: 2026-05-28
status: current
confidence_overall: emerging
issue: "#972"
---

# Gemini 3.5 Flash: more expensive, but Google plan to use it for everything

> Simon Willison's first-party analysis of Google's Gemini 3.5 Flash release documents a 3–6x pricing increase over predecessor Flash models, identifies a simultaneous cross-vendor price escalation pattern across all three major AI labs, and introduces a new API pattern (Interactions API) mirroring OpenAI's server-side history management — providing the clearest single-sentence framing in the corpus that labs are actively probing API customers' price tolerance.

## Source Context

- **Type**: blog-post (Willison link-blog + notes format; ~600–900 words; includes concrete pricing tables, benchmark cost data, and live model output examples. Published May 19, 2026, the same day as Google I/O where 3.5 Flash was announced.)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI, one of the most widely-cited practitioner commentators on LLM tooling. He has maintained the "pelican on a bicycle" SVG as a consistent cross-model benchmark and publishes first-person, vendor-neutral pricing comparisons. The post is observational commentary on a product launch, not a controlled study — but Willison is authoritative as a practitioner synthesizer. Pricing data comes from Google's published rates, not third-party estimates. Benchmark cost data is from Artificial Analysis.
- **Scope**: Covers the Gemini 3.5 Flash launch: pricing, deployment breadth, technical specs, benchmark costs, and Willison's editorial interpretation of cross-vendor pricing trends. Also documents the new Interactions API (beta). Does NOT cover model quality benchmarks in depth, multi-turn behavioral analysis, or comparison against non-Google competitors on capability dimensions.

## Extracted Claims

### Claim 1: Gemini 3.5 Flash launched at Google I/O on May 19, 2026 as a GA release — it skipped the preview qualifier that prior Gemini 3.x models used

- **Evidence**: First-party observation from the launch day. Willison explicitly notes the distinction from prior practice.
- **Confidence**: settled (factual product release information)
- **Quote**: "This one skipped the `-preview` modifier and went straight to general availability"
- **Our assessment**: The GA-without-preview release signals Google's confidence in the model at launch. All prior Gemini 3.x releases in the corpus appeared as previews first. The direct GA launch accelerates practitioner adoption timelines — there is no evaluation window in which the model is preview-only before production use is warranted.

### Claim 2: Gemini 3.5 Flash is priced at $1.50/million input tokens and $9/million output tokens — 3x more than Gemini 3 Flash Preview and 6x more than Gemini 3.1 Flash-Lite

- **Evidence**: Google's published pricing at time of post, confirmed by Willison.
- **Confidence**: settled (published pricing at time of post; subject to future changes)
- **Quote**: "The new 3.5 Flash is 3x the price of 3 Flash Preview and 6x the price of 3.1 Flash-Lite"
- **Our assessment**: The 3–6x pricing jump within the Flash tier is extreme. "Flash" historically signaled the budget-optimized tier below Pro. At $1.50/$9 per million tokens, 3.5 Flash approaches the prior Pro tier pricing, making the Flash/Pro tier distinction less meaningful as a cost-selection heuristic. Willison notes: "At $1.50/million input and $9/million output it's getting close in price to Google's Gemini 3.1 Pro." Practitioners using Flash as an assumed low-cost option must re-evaluate assumptions per model generation.

### Claim 3: Running Artificial Analysis's benchmark suite against Gemini 3.5 Flash (high) costs $1,551.60 — more than running the same suite against Gemini 3.1 Pro Preview ($892.28)

- **Evidence**: Artificial Analysis benchmark cost data, cited directly in the post.
- **Confidence**: emerging (third-party benchmark data; reflects Artificial Analysis's specific benchmark suite composition)
- **Quote**: "Gemini 3.5 Flash (high): $1,551.60" and "[Gemini 3.1 Pro Preview](https://artificialanalysis.ai/models/gemini-3-1-pro-preview): $892.28"
- **Our assessment**: This benchmark anomaly — a Flash model costing 74% more to evaluate than the Pro model — is a concrete illustration that model tier names are no longer reliable cost-tier signals. The anomaly arises because benchmark suites test reasoning tasks where the high-quality inference path is expensive; if 3.5 Flash defaults to high-quality reasoning more aggressively than 3.1 Pro Preview, its per-task cost compounds. For practitioners selecting models by tier name (Flash = cheap, Pro = quality): that heuristic is broken as of May 2026, at least for Google's lineup.

### Claim 4: Google deployed Gemini 3.5 Flash as the default model across multiple free consumer products — the Gemini app, AI Mode in Google Search, and enterprise platforms — despite its 3–6x price increase over predecessors

- **Evidence**: Product deployment announcement at Google I/O. Multiple deployment targets named explicitly.
- **Confidence**: settled (official product deployment announcement)
- **Quote**: "For everyone via the Gemini app and AI Mode in Google Search" and "For developers in our agent-first development platform Google Antigravity and Gemini API in Google AI Studio and Android Studio"
- **Our assessment**: Google absorbing the higher inference cost on free-to-consumer products (Search, Gemini app) is the strongest available signal that Google's internal ROI calculation favors 3.5 Flash over cheaper alternatives. A company would not deploy a 3–6x more expensive model at free-to-consumer scale unless it believed the quality improvement justified the marginal cost at that volume. For practitioners evaluating whether to upgrade their own Google API integrations: Google's own deployment decisions function as a revealed preference endorsement of the model.

### Claim 5: All three major AI labs simultaneously raised prices on their newest flagship models — GPT-5.5 at 2x GPT-5.4, Claude Opus 4.7 at ~1.46x Opus 4.6 (tokenizer-adjusted), and Gemini 3.5 Flash at 3x/6x over predecessors

- **Evidence**: Willison's cross-vendor pricing synthesis based on published pricing from OpenAI, Anthropic, and Google.
- **Confidence**: emerging (pricing data is settled at time of post; the interpretation of coordinated behavior is Willison's editorial analysis, not documented industry coordination)
- **Quote**: "This fits a trend: OpenAI's GPT-5.5 was 2x the price of GPT-5.4, and Claude Opus 4.7 is around 1.46x the price of 4.6 when you take the new tokenizer into account."
- **Our assessment**: The three-vendor simultaneous price increase is the most important market-level signal in this post. It is not evidence of coordination — it is more plausibly evidence of parallel confidence: each lab independently judged the new model worth more to customers and priced accordingly. The Anthropic multiplier (1.46x) being lower than OpenAI's (2x) and Google's (3–6x) could reflect: a less dramatic capability improvement, a more conservative pricing strategy, or the tokenizer change absorbing some of the nominal price difference. The guide should present all three multipliers as a data set rather than extrapolating a single "industry rate."

### Claim 6: Willison explicitly interprets the simultaneous cross-vendor price increases as all three major AI labs probing their API customers' price tolerance

- **Evidence**: Willison's first-person editorial interpretation of the deployment + pricing decision.
- **Confidence**: anecdotal (authoritative practitioner editorial; no market research data behind the interpretation)
- **Quote**: "Given the price increase it's interesting to see Google roll it out for so many of their own free-to-consumer products. It feels like all three of the major AI labs are starting to probe the price tolerance of their API customers."
- **Our assessment**: The "probe the price tolerance" framing is the sharpest single-sentence diagnosis of the trend. Willison is not claiming coordination — "feels like" is careful hedging. But the framing is valuable precisely because it names the mechanism: labs are using successive model releases as natural experiments in what customers will pay. For practitioners building cost-sensitive harnesses: the relevant engineering response to this trend is not to find the cheapest current model but to design harnesses that can swap models as pricing equilibria shift (corroborates `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4, which makes the same point via editorial prescription).

### Claim 7: Google launched an Interactions API in beta for Gemini 3.5 Flash — a new API pattern with server-side history management comparable to the OpenAI Responses API

- **Evidence**: Willison's first-person observation of the new API, compared against the OpenAI Responses API pattern he has documented elsewhere.
- **Confidence**: emerging (beta feature; comparison to OpenAI Responses is Willison's interpretation, not official Google documentation)
- **Quote**: "Google are also pushing a new Interactions API, currently in beta, which looks to me like their version of the patterns introduced by OpenAI Responses—in particular server-side history management."
- **Our assessment**: Server-side history management means the API maintains conversation context on the provider's servers rather than requiring the client to resend full history each turn. This reduces client-side context management complexity and bandwidth costs for multi-turn agents but introduces provider-side statefulness (and the lock-in and reliability risks that entails). The convergence between Google and OpenAI on this pattern suggests it is becoming an industry standard API design for multi-turn agent interactions. Practitioners designing harness context management strategies should evaluate which model: client-managed history (maximum portability, no server state) vs. server-managed history (simpler client code, provider dependency). This is the first Google implementation of this pattern in the corpus.

### Claim 8: Gemini 3.5 Flash has the same platform feature set as prior Gemini 3.x models except it lacks computer use capability

- **Evidence**: Willison's technical comparison noting the one missing feature.
- **Confidence**: settled (factual capability report at time of post)
- **Quote**: "It mostly has the same set of platform features as the previous Gemini 3.x series, albeit with no computer use."
- **Our assessment**: The absence of computer use is notable because Gemini 3.x series models had computer use capability; 3.5 Flash's omission is a deliberate product decision, not a gap. Practitioners evaluating 3.5 Flash for computer-use agentic tasks cannot substitute it for a prior Gemini 3.x model with computer use. This is a capability regression, not just a pricing change.

### Claim 9: Gemini 3.5 Flash has a January 2025 knowledge cutoff, a 1,048,576-token input context, and 65,536 maximum output tokens

- **Evidence**: Willison reporting Google's published specifications.
- **Confidence**: settled (published specifications at time of post)
- **Quote**: "The knowledge cut-off is January 2025, and it supports 1,048,576 input tokens and 65,536 maximum output tokens."
- **Our assessment**: The January 2025 knowledge cutoff is notable context for practitioners: 3.5 Flash has a training data cutoff 16+ months before its May 2026 release, meaning any API usage patterns, framework changes, or ecosystem developments from February 2025 onward are unknown to the model without retrieval augmentation. The 1M+ token input context is consistent with the Gemini 3.x series standard.

## Concrete Artifacts

### Gemini 3.5 Flash Pricing vs. Prior Google Models (May 2026)

```
Gemini 3.5 Flash pricing at GA release (May 19, 2026):
  Input:  $1.50 / million tokens
  Output: $9.00 / million tokens

Comparison:
  vs. Gemini 3 Flash Preview:     3x more expensive (input and output)
  vs. Gemini 3.1 Flash-Lite:      6x more expensive (input and output)
  vs. Gemini 3.1 Pro:             approaching Pro pricing ($2/M input, $12/M output)

Artificial Analysis benchmark run cost:
  Gemini 3.5 Flash (high):         $1,551.60
  Gemini 3.1 Pro Preview:          $892.28
  (3.5 Flash costs 74% more to benchmark than the Pro model)

Source: Simon Willison citing Google published pricing and Artificial Analysis data,
simonwillison.net/2026/May/19/gemini-35-flash/, May 19, 2026
```

### Cross-Vendor Price Escalation Table (May 2026, per Willison)

```
Cross-vendor pricing increases on latest flagship model vs. predecessor (May 2026):

  Vendor     New Model           vs. Predecessor      Multiplier  Adjustment note
  --------   ------------------  ------------------   ----------  ---------------
  Google     Gemini 3.5 Flash    vs. 3 Flash Preview  3x          (input and output)
  Google     Gemini 3.5 Flash    vs. 3.1 Flash-Lite   6x          (input and output)
  OpenAI     GPT-5.5             vs. GPT-5.4          2x          (no adjustment)
  Anthropic  Claude Opus 4.7     vs. Opus 4.6         ~1.46x      accounts for new
                                                                   tokenizer changes

Interpretation (Willison, anecdotal):
  "It feels like all three of the major AI labs are starting to probe the
   price tolerance of their API customers."

Source: Simon Willison, simonwillison.net/2026/May/19/gemini-35-flash/, May 19, 2026
```

### Gemini 3.5 Flash Technical Specifications (GA, May 2026)

```
Model ID:           gemini-3.5-flash
Release type:       General availability (skipped preview)
Released:           May 19, 2026 (Google I/O)
Knowledge cutoff:   January 2025
Input context:      1,048,576 tokens
Output max:         65,536 tokens
Computer use:       NOT supported (removed vs. Gemini 3.x series)

Deployment targets at launch:
  - Gemini app (free consumer)
  - AI Mode in Google Search (free consumer)
  - Google Antigravity (agent-first development platform)
  - Gemini API in Google AI Studio
  - Android Studio
  - Gemini Enterprise Agent Platform

Pricing:
  Input:  $1.50 / million tokens
  Output: $9.00 / million tokens

Source: Simon Willison, simonwillison.net/2026/May/19/gemini-35-flash/, May 19, 2026
```

### Interactions API Pattern (Beta, May 2026)

```
Google Interactions API (beta, May 2026):
  - Server-side conversation history management
  - Comparable to OpenAI Responses API pattern
  - Eliminates need for client to resend full history each turn
  - Tradeoff: simpler client code vs. provider-side statefulness

Willison's characterization:
  "Google are also pushing a new Interactions API, currently in beta, which looks
   to me like their version of the patterns introduced by OpenAI Responses—in
   particular server-side history management."

Source: Simon Willison, simonwillison.net/2026/May/19/gemini-35-flash/, May 19, 2026
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 4: That note establishes GPT-5.5 at $5/$30 per 1M tokens and 2x GPT-5.4 pricing, calling it the "Sonnet to Opus" tier jump. This source adds the Gemini and Anthropic data points, completing the cross-vendor pricing comparison that note started. Together these two notes constitute the first in-corpus multi-vendor pricing trend documentation.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4: The Batch's editorial recommends designing harnesses to swap models as easily as bumping a dependency, grounded in four flagship launches in three months. This source's pricing data (Claim 5–6) is the economic mechanism behind that architectural recommendation: labs are probing price tolerance, so practitioners who lock into a specific model accept recurrent cost-basis risk. The two sources make the engineering case (Batch) and the economic case (Willison) for the same design principle.
  - `docs-github-copilot-cca-cost-efficient-models.md` Claim 1–2: That note documents GitHub simultaneously adding cheaper models (Haiku 4.5, GPT-5.4-mini at 0.33x multiplier) to Copilot cloud agent while the same week sees Gemini 3.5 Flash priced at premium rates. These two sources together capture a market bifurcation: labs are adding cheap-tier options for simple tasks (CCA haiku/mini expansion) while simultaneously raising flagship model prices. The guide should present both trends.

- **Contradicts**: None filed. The pricing multipliers in this source (1.46x for Opus 4.7) are consistent with information reported elsewhere in the corpus.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md`: That note documented the first pricing tier comparison (GPT-5.5 vs GPT-5.4). This source extends the comparison to three vendors with explicit multipliers and adds the Willison "price tolerance probing" editorial interpretation as the synthesizing frame.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md`: That note's Claim 5 documents GPT-5.5 specifications. This source adds the Google side of the market and creates the first three-vendor pricing comparison in the corpus.

- **Novel**:
  - **"Price tolerance probing" as a named industry behavior**: Willison's explicit framing — "all three of the major AI labs are starting to probe the price tolerance of their API customers" — is the first in-corpus single-sentence synthesis of the simultaneous price escalation trend across Google, OpenAI, and Anthropic. No prior note named the mechanism or provided cross-vendor data in one place.
  - **Flash tier name decoupling from cost position**: The benchmark anomaly (Claim 3) showing 3.5 Flash costs more to evaluate than 3.1 Pro is the first in-corpus evidence that model tier names (Flash/Pro) are unreliable cost-tier signals as of May 2026. Prior corpus notes assumed Flash = cheap.
  - **Google Interactions API (server-side history)**: First in-corpus documentation of Google's server-side conversation history API (beta). The pattern itself is not novel (OpenAI Responses API introduced it first), but Google's adoption of the same pattern is new evidence that server-side history management is converging as an industry standard for multi-turn agent APIs.
  - **Deployment-as-revealed-preference signal**: The pattern "lab deploys expensive model on free consumer products at scale = strong confidence signal" (Claim 4) is a new analytical heuristic not documented in any other corpus note. It provides practitioners a method to read lab deployment decisions as quality endorsements.

## Guide Impact

- **Chapter 03 (Model Selection — Cost Economics)**: Claims 2–3 should update any section that presents "Flash models are the budget option" framing. As of May 2026, the Gemini Flash tier is pricing near Pro tier, and actually costs *more* to benchmark than the corresponding Pro model. Recommend adding: "Model tier names (Flash, Sonnet, Mini) no longer reliably predict relative cost. Verify current per-token pricing and expected inference patterns for each model; the Artificial Analysis benchmark cost anomaly (Flash > Pro at $1,551 vs $892) illustrates how tier labels can mislead cost estimation."

- **Chapter 03 (Model Selection — Market Dynamics)**: Claim 5–6 together provide the first cross-vendor pricing trend evidence in the corpus with specific multipliers (2x OpenAI, 1.46x Anthropic, 3–6x Google). Recommend adding a "Model Economics" section noting: "All three major labs raised flagship model prices in early–mid 2026 simultaneously (GPT-5.5 2x, Opus 4.7 1.46x, Gemini 3.5 Flash 3–6x). This is consistent with labs testing price elasticity. Budget assumptions established even one model generation ago may not hold for the current generation. Design cost models to be updated per-model-generation, not once."

- **Chapter 02 (Harness Engineering — Context Management)**: Claim 7 (Interactions API) is worth a forward note in any harness context-management section. As of May 2026, both OpenAI (Responses API) and Google (Interactions API) offer server-side history management. The guide should present the architectural choice between client-managed and server-managed history as a first-class harness design decision with explicit tradeoffs: client-managed = maximum portability and control, server-managed = simpler client code at the cost of provider statefulness and potential lock-in.

- **Chapter 02 (Harness Engineering — Model Abstraction)**: Cross-reference to `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 4 and `blog-simonwillison-gpt55-codex-plugin.md` Claim 4 for the model-swap-ability principle. The three sources together constitute a strong case: the pricing data here (Claim 5–6) is the economic evidence for why harnesses must be model-swappable, and the other two sources provide the architectural recommendation.

## Extraction Notes

- Source is a first-person practitioner blog post, ~600–900 words. Full post was read; all substantive sections were extracted (pricing, deployment, specs, benchmark costs, trend analysis, Interactions API). The pelican SVG generation example was not extracted as a primary claim per Prospector guidance ("the pelican SVG story is illustrative but not a pattern") — it appears only incidentally in the pricing artifact.
- WebFetch produced summaries rather than verbatim text for full-post requests. Verbatim quotes were obtained by making targeted multi-question requests to WebFetch. All quotes in the Extracted Claims section were verified to appear in the source via at least one targeted fetch call.
- The Artificial Analysis benchmark data is cited by Willison from an external source (Artificial Analysis); it is not Willison's own measurement. The benchmark cost figures represent Artificial Analysis's specific test suite composition, not a universal inference cost benchmark.
- Pricing information is current as of May 19, 2026. Google's pricing is subject to change; these figures should be treated as point-in-time evidence for the trend, not as durable cost references.
- The Interactions API is in beta as of publication; its feature set and availability may change before GA.
- Three Prospector triage comments were present on the issue, all consistent: extract pricing escalation data, cross-vendor trend, deployment signals, Interactions API. Skip the pelican SVG story. This extraction follows that guidance.
