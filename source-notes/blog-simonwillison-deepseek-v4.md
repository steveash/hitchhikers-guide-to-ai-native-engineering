---
source_url: https://simonwillison.net/2026/Apr/24/deepseek-v4/
source_type: blog-post
title: "DeepSeek V4—almost on the frontier, a fraction of the price"
author: Simon Willison
date_published: 2026-04-24
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#521"
---

# DeepSeek V4—almost on the frontier, a fraction of the price

> Willison's hands-on look at DeepSeek V4-Pro and V4-Flash establishes a concrete cost floor for the model-selection decision tree: V4-Flash at $0.14/M input tokens is the cheapest available small model (undercutting GPT-5.4 Nano); V4-Pro at $1.74/M is the cheapest large frontier-class model — with efficiency metrics showing 10–27% of V3.2's FLOPs at 1M-token context.

## Source Context

- **Type**: blog-post (Willison link-blog + notes format; ~600–800 words; includes a 12-model pricing comparison table, model specs, efficiency metrics from the DeepSeek paper, and pelican SVG test results via OpenRouter)
- **Author credibility**: Simon Willison is creator of Django, creator of the `llm` CLI, and one of the most widely-cited practitioner commentators on LLM tooling. His "pelican on a bicycle" SVG test is a consistent cross-model benchmark he applies publicly. Posts in this format are first-person observation plus synthesis of primary sources (DeepSeek paper citations, pricing from DeepSeek API docs). No disclosed affiliation with DeepSeek.
- **Scope**: Covers V4-Pro and V4-Flash model specs, pricing comparison against 11 other models, efficiency metrics from the DeepSeek technical paper, benchmark performance, MIT licensing, HuggingFace availability, and a brief hands-on pelican SVG test via OpenRouter. Does NOT cover deployment infrastructure, context engineering, safety evaluations, or fine-tuning.

## Extracted Claims

### Claim 1: DeepSeek V4-Pro is the new largest open-weights model (1.6T total parameters, 49B active); V4-Flash is 284B/13B active — both have 1M token context and MIT licenses

- **Evidence**: Model specs stated directly in post, corroborated by HuggingFace file size data (Pro: 865GB; Flash: 160GB). Willison explicitly compares V4-Pro against Kimi K2.6 (1.1T) and GLM-5.1 (754B) to establish the size ranking.
- **Confidence**: settled (published metadata at time of post)
- **Quote**: "I think this makes DeepSeek-V4-Pro the new largest open weights model."
- **Our assessment**: The 1.6T total / 49B active MoE architecture places V4-Pro at the frontier of open-weights model size. The 49B active parameters is comparable to proprietary frontier models at inference time but runs at MoE sparsity — a key cost advantage. The 1M-token context window at this scale is significant: most earlier models in this weight class operated at 64k–256k context. The MIT license and HuggingFace availability are the deployment-relevant details — no API dependency for teams with the hardware.

### Claim 2: V4-Flash at $0.14/$0.28 per million input/output tokens is the cheapest small model available, undercutting GPT-5.4 Nano at $0.20/$1.25

- **Evidence**: Direct price comparison from a table Willison presents covering 12 models. V4-Flash input ($0.14) is lower than GPT-5.4 Nano ($0.20), Gemini 3.1 Flash-Lite ($0.25), and every other small-model-tier entry.
- **Confidence**: settled (published pricing at time of post; subject to vendor changes)
- **Quote**: "DeepSeek-V4-Flash is the cheapest of the small models, beating even OpenAI's GPT-5.4 Nano."
- **Our assessment**: The $0.14 input price point establishes a new floor for small-model API pricing. The Flash output price ($0.28/M) is also notably low — GPT-5.4 Nano outputs at $1.25/M, roughly 4.5× more expensive. For cost-sensitive applications that generate large output volumes, the output price difference is material. Practitioners building high-volume inference pipelines should benchmark Flash against GPT-5.4 Nano on their workloads before assuming substitutability.

### Claim 3: V4-Pro at $1.74/$3.48 per million input/output tokens is the cheapest large frontier-class model

- **Evidence**: From the same 12-model pricing comparison table. V4-Pro ($1.74 input) is priced below Gemini 3.1 Pro ($2), GPT-5.4 ($2.50), Claude Sonnet 4.6 ($3), Claude Opus 4.7 ($5), and GPT-5.5 ($5).
- **Confidence**: settled (published pricing at time of post; subject to vendor changes)
- **Quote**: "DeepSeek-V4-Pro is the cheapest of the larger frontier models."
- **Our assessment**: The $1.74/$3.48 price point positions V4-Pro as a cost-accessible large model for practitioners who need large-model capability but face budget constraints. The output price ($3.48/M) is significantly lower than Claude Sonnet 4.6 ($15/M) and GPT-5.5 ($30/M). For teams building cost-aware model routing, this creates a new tier below the standard frontier pricing band: frontier-adjacent capability at roughly 30–40% of typical frontier cost.

### Claim 4: V4-Pro achieves only 27% of V3.2's single-token FLOPs and 10% of its KV cache at 1M-token context — a ~4× FLOP and ~10× KV cache reduction for long-context inference

- **Evidence**: Quoted from the DeepSeek V4 technical paper as cited by Willison. Metric is defined: "single-token FLOPs (measured in equivalent FP8 FLOPs)" in "the scenario of 1M-token context."
- **Confidence**: emerging (paper-cited claim; first-party DeepSeek research; methodology described with units [FP8 FLOPs] but not independently reproducible from the post alone)
- **Quote**: "even DeepSeek-V4-Pro, which has a larger number of activated parameters, attains only 27% of the single-token FLOPs (measured in equivalent FP8 FLOPs) and 10% of the KV cache size relative to DeepSeek-V3.2."
- **Our assessment**: This is the key architectural efficiency claim. At 1M-token context, KV cache dominates memory cost — 10% of V3.2's KV cache is a ~10× reduction in memory pressure at long context. For practitioners evaluating models for RAG, document review, or large codebase analysis, V4-Pro's ability to handle 1M tokens at 10% of V3.2's KV cache cost changes the economics of long-context workloads. The 27% FLOPs figure translates to lower inference cost per token at long context. These are self-reported metrics from the model authors — independent verification would strengthen confidence.

### Claim 5: V4-Flash achieves only 10% of V3.2's single-token FLOPs and 7% of its KV cache at 1M-token context — the most extreme long-context efficiency reported for any open-weights model in this corpus

- **Evidence**: From the DeepSeek V4 technical paper as cited by Willison. Same metric definition as Claim 4.
- **Confidence**: emerging (same sourcing as Claim 4; paper-cited, first-party)
- **Quote**: "DeepSeek-V4-Flash, with its smaller number of activated parameters, pushes efficiency even further: in the 1M-token context setting, it achieves only 10% of the single-token FLOPs and 7% of the KV cache size compared with DeepSeek-V3.2."
- **Our assessment**: V4-Flash's efficiency at 1M context is extreme: 7% of KV cache means ~14× less memory pressure than V3.2. Combined with the $0.14/M input price (Claim 2), Flash becomes exceptionally attractive for applications where full Pro-level reasoning is not required. The 160GB HuggingFace size also makes local deployment feasible (Claim 8). The extreme efficiency is likely the result of architectural changes in the MoE routing and attention mechanism — practitioners should consult the DeepSeek V4 technical paper for architectural details.

### Claim 6: V4-Pro benchmarks show competitive performance but trail GPT-5.4 and Gemini-3.1-Pro by approximately 3–6 months in developmental trajectory, per the authors' own assessment

- **Evidence**: DeepSeek's self-reported benchmarks in the paper, cited by Willison. The "3 to 6 months" framing comes from the DeepSeek paper's own characterization.
- **Confidence**: anecdotal (self-reported benchmarks by the model authors; the trajectory claim is the paper's own characterization; no independent third-party benchmark corroboration in this post)
- **Quote**: "its performance falls marginally short of GPT-5.4 and Gemini-3.1-Pro, suggesting a developmental trajectory that trails state-of-the-art frontier models by approximately 3 to 6 months."
- **Our assessment**: This is an unusually candid self-assessment — the authors explicitly position their model as behind the frontier rather than claiming parity or superiority. The Artificial Analysis Intelligence Index (from `blog-thebatch-gpt55-hallucination-kimi-k26.md`) places V4-Pro at 52, below GPT-5.5 (60), Claude Opus 4.7 (57), and Gemini 3.1 Pro (57) but comparable to Kimi K2.6 (54) — broadly consistent with this self-assessment. For practitioners: V4-Pro is sub-frontier on benchmarks but priced below half the frontier cost, which may be an acceptable tradeoff for many production workloads.

### Claim 7: Cost, not raw performance, is the headline story for DeepSeek V4

- **Evidence**: Willison's direct editorial judgment after conducting the pelican SVG test.
- **Confidence**: anecdotal (single practitioner's qualitative assessment; directly stated)
- **Quote**: "So the pelicans are pretty good, but what's really notable here is the cost. DeepSeek V4 is a very, very inexpensive model."
- **Our assessment**: Willison's editorial judgment aligns precisely with the pricing data: both models are at or below the cheapest in their tier. The "pretty good" pelican SVG result combined with "very, very inexpensive" is a practitioner-facing endorsement of the value proposition. For practitioners: this source suggests capability is sufficient for creative/generative tasks at substantially lower cost than alternatives. Whether code generation and reasoning tasks show the same value ratio requires separate evaluation.

### Claim 8: V4-Flash (160GB on HuggingFace, MIT license) may be viable for local deployment on high-RAM consumer hardware; V4-Pro is 865GB

- **Evidence**: Willison states the HuggingFace file sizes and explicitly expresses intent to run a quantized Flash locally on his hardware.
- **Confidence**: anecdotal (Willison's expectation at time of post, not a confirmed outcome; "lightly quantized" implies further work is needed)
- **Quote**: "I'm hoping that a lightly quantized Flash will run on my 128GB M5 MacBook Pro."
- **Our assessment**: The 160GB size for Flash aligns with what would fit in quantized form on a 128GB M5 MacBook Pro (with Q4 quantization, a 160GB FP16 model compresses to roughly 80GB). This is a significant local deployment possibility — a 13B-active-parameter model at the cheapest-in-class API price, potentially runnable on high-RAM Apple Silicon consumer hardware. For teams with data-residency requirements or API cost ceilings: this is a meaningful option to track. The MIT license removes licensing barriers for commercial local deployment. No follow-up confirmation from Willison is included in this post.

### Claim 9: Willison tested both models via OpenRouter using llm-openrouter; pelican SVG results were "pretty good"

- **Evidence**: Willison's direct description of his test method. He uses the same `llm` CLI + OpenRouter workflow documented in his GLM-5.1 and GPT-5.5 posts.
- **Confidence**: anecdotal (single practitioner, single test, creative task only)
- **Quote**: (no direct quote captures the full test description; see paraphrase in Our assessment)
- **Our assessment**: The pelican SVG test is Willison's recurring cross-model creative-code benchmark. The "pretty good" quality framing, combined with his explicit pivot to cost as the headline ("but what's really notable here is the cost"), suggests the quality is comparable to other frontier/near-frontier models he has tested — not remarkable, not broken. For practitioners evaluating V4 for code generation or reasoning tasks: the pelican test does not cover those workloads. The OpenRouter/`llm` workflow from this post is consistent with the pattern documented in `blog-simonwillison-glm51.md` and `blog-simonwillison-gpt55-codex-plugin.md`.

## Concrete Artifacts

### Pricing Comparison Table (from the post, April 2026)

```
Model                        Input ($/M)   Output ($/M)
------------------------------------------------------
DeepSeek V4 Flash            $0.14         $0.28
GPT-5.4 Nano                 $0.20         $1.25
Gemini 3.1 Flash-Lite        $0.25         $1.50
Gemini 3 Flash Preview       $0.50         $3.00
GPT-5.4 Mini                 $0.75         $4.50
Claude Haiku 4.5             $1.00         $5.00
DeepSeek V4 Pro              $1.74         $3.48
Gemini 3.1 Pro               $2.00         $12.00
GPT-5.4                      $2.50         $15.00
Claude Sonnet 4.6            $3.00         $15.00
Claude Opus 4.7              $5.00         $25.00
GPT-5.5                      $5.00         $30.00

Source: Simon Willison, simonwillison.net/2026/Apr/24/deepseek-v4/, April 24, 2026
(assembled from DeepSeek API docs and provider pricing pages at time of post)
```

### Model Specifications (DeepSeek V4, April 2026)

```
DeepSeek V4-Pro:
  Architecture:       Mixture of Experts
  Total parameters:   1.6 trillion
  Active parameters:  49 billion
  Context:            1 million tokens
  HuggingFace size:   865 GB
  License:            MIT

DeepSeek V4-Flash:
  Architecture:       Mixture of Experts
  Total parameters:   284 billion
  Active parameters:  13 billion
  Context:            1 million tokens
  HuggingFace size:   160 GB
  License:            MIT

Source: Simon Willison, simonwillison.net/2026/Apr/24/deepseek-v4/, April 24, 2026
(citing DeepSeek API docs and DeepSeek V4 technical paper)
```

### Efficiency Metrics vs. DeepSeek V3.2 at 1M-Token Context (from DeepSeek V4 paper, via Willison)

```
Model              Single-token FLOPs (vs V3.2)   KV Cache size (vs V3.2)
-------------------------------------------------------------------------
DeepSeek V4-Pro    27%  (~4×  reduction)           10%  (~10× reduction)
DeepSeek V4-Flash  10%  (~10× reduction)            7%  (~14× reduction)

Measurement: single-token FLOPs in equivalent FP8 FLOPs; 1M-token context window scenario
Baseline:    DeepSeek V3.2

Source: DeepSeek V4 technical paper, cited by Simon Willison,
        simonwillison.net/2026/Apr/24/deepseek-v4/, April 24, 2026
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-glm51.md` Claim 1: That note establishes GLM-5.1 as "a giant 754B parameter 1.51TB (on Hugging Face) MIT-licensed monster." This source's Claim 1 positions V4-Pro (1.6T) explicitly as larger than both GLM-5.1 (754B) and Kimi K2.6 (1.1T), corroborating rapid escalation in open-weights model scale: within roughly two months (GLM-5.1 April 7, V4-Pro April 24, 2026), the "largest open-weights model" title changed hands.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Concrete Artifacts → Artificial Analysis Intelligence Index Leaderboard: That note's leaderboard table places DeepSeek-V4-Pro at 52 on the Artificial Analysis Intelligence Index, below GPT-5.5 (60), Claude Opus 4.7 (57), and Gemini 3.1 Pro (57) but comparable to Kimi K2.6 (54). This is independently consistent with Claim 6 here ("trails state-of-the-art frontier models by approximately 3 to 6 months").
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 4: That note documents GPT-5.5 pricing at $5/$30 per 1M input/output tokens. The pricing table in this source independently confirms those same figures and places V4-Pro's $1.74/$3.48 in context: V4-Pro costs 35% of GPT-5.5 for input and 12% of GPT-5.5 for output.
  - `blog-cursor-composer2-technical-report.md` Claim 1: That note reports Cursor evaluated DeepSeek V3.2 as a base model candidate (alongside Kimi K2.5 and GLM-5) and selected Kimi K2.5. This corroborates V3.2 as the immediate predecessor in DeepSeek's model lineage. The V4 efficiency claims (27%/10% of V3.2's FLOPs/KV cache) can be read as DeepSeek's architectural response to V3.2's relative inefficiency at long context — the same model Cursor found lacking against Kimi K2.5.

- **Contradicts**: None identified.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md`: That note documents Willison's pelican test methodology and the `llm` + OpenRouter pattern for GPT-5.5 and adds a pricing table. This post extends the pricing table by adding V4-Flash and V4-Pro — both below all prior entries in their respective tiers — establishing new price floors for small and large models.
  - `blog-simonwillison-glm51.md`: That note documents the `llm` CLI + OpenRouter pattern and the GLM-5.1 pelican test result. This post applies the same workflow to DeepSeek V4 and adds V4-Flash/Pro to the cross-model creative-code comparison corpus. Together, these three Willison posts form a consistent cross-model test dataset using the same methodology and benchmark.

- **Novel**:
  - **Sub-$0.20/M small model pricing tier**: V4-Flash at $0.14/M input is the first model in the corpus priced below $0.20/M input for a small model. The prior corpus floor (GPT-5.4 Nano, $0.20/M) is no longer the cheapest.
  - **Frontier-class model below $2/M input**: V4-Pro at $1.74/M is the first frontier-adjacent model in the corpus priced below $2/M input. This creates a new pricing tier in the cost/quality spectrum that the guide has not yet addressed.
  - **1M-token context KV cache efficiency metrics**: V4-Pro's 10% KV cache and V4-Flash's 7% KV cache vs V3.2 at 1M context are the first in-corpus efficiency measurements specifically for 1M-token long-context inference KV cache. Prior efficiency discussions in the corpus focus on general parameter counts or FLOP counts, not KV cache specifically at this context length.
  - **Consumer local deployment possibility for a 1M-context model**: Claim 8 (Flash-on-M5-MacBook-Pro) is the first in-corpus suggestion that a 1M-context model may be viable for local consumer hardware. Earlier notes document open-weights models (GLM-5.1 at 754B, Kimi K2.6 at 1T) but not at 1M context scale for local deployment.
  - **Complete 12-model pricing table (April 2026)**: The pricing comparison table (Concrete Artifacts) is the most current and complete single-source model pricing snapshot in the corpus as of April 2026, spanning small-tier through top-tier frontier models across all major vendors.

## Guide Impact

- **Ch03 / Model Selection**: This post provides the most complete current model pricing table in the corpus (12 models, April 2026). Recommend adding a section or callout: "As of April 2026, DeepSeek V4-Flash ($0.14/M input, $0.28/M output) is the cheapest small-tier model API available, below GPT-5.4 Nano; V4-Pro ($1.74/M input) is the cheapest large frontier-adjacent model, below Gemini 3.1 Pro. Both are MIT licensed with HuggingFace availability." The Concrete Artifacts pricing table should feed directly into any model-selection cost framework in the guide.

- **Ch05 / Cost Optimization**: Claims 4 and 5 (efficiency at 1M token context) have direct cost implications for long-context workloads. "At 1M-token context, V4-Pro requires only 10% of V3.2's KV cache memory — making it dramatically cheaper to run at long context than parameter count alone would suggest." For teams evaluating RAG, large codebase analysis, or document processing: the KV cache efficiency is the relevant cost driver, and V4-Pro's ~10× improvement over V3.2 on this metric should be highlighted.

- **Ch02 / Model Selection Framework**: Claim 6 introduces a "3–6 months behind frontier" self-assessment from the model authors. The guide could use this as a practitioner heuristic template: a model that self-reports trailing the frontier by 3–6 months but prices below half the frontier cost may be appropriate for use cases where near-frontier capability suffices. This is a new framing dimension for model selection not previously in the guide.

- **Ch04 / Local Deployment Patterns**: Claim 8 (Flash local deployment on high-RAM Apple Silicon) matters for teams with data-residency requirements or API cost ceilings. "A lightly quantized V4-Flash (~80GB Q4) may fit on a 128GB M5 Mac, potentially bringing 1M-context capability to local deployment." This should be tracked for confirmation; note Willison's post expresses the hope but does not confirm the result.

## Extraction Notes

- Source is a link-blog-style post (~600–800 words) consistent with Willison's posting format for model commentary. Efficiency metrics (FLOPs, KV cache) are quoted from the DeepSeek V4 paper (first-party from DeepSeek). Pricing data is from DeepSeek API docs and provider pricing pages at time of post.
- WebFetch returned structured summaries rather than full verbatim text. All `Quote` fields except Claim 9 are verified verbatim via multiple targeted fetches returning the same text. Claim 9 has no identified verbatim quote for the testing method description; the paraphrase is in the Our assessment field instead.
- Three Prospector triage comments all agree: focus on cost/efficiency data, model specs, and pricing tables; benchmark comparisons are secondary. This extraction follows that guidance.
- No sub-pages followed. The DeepSeek paper is cited but not directly linked in the post; its claims are mediated through Willison's reporting.
- No contradictions to file.
- Fragment `#atom-everything` in the original issue URL is a feed anchor; `source_url` uses the canonical page URL without the fragment.
