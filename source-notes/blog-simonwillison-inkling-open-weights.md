---
source_url: https://simonwillison.net/2026/Jul/16/inkling/
source_type: blog-post
title: "Inkling: Our open-weights model"
author: Simon Willison (linking to Thinking Machines Lab's own announcement, model card, and training data documentation)
date_published: 2026-07-16
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2088"
---

# Inkling: Our open-weights model

> Simon Willison's link-blog post on Thinking Machines Lab's first
> open-weights model, Inkling (975B total / 41B active MoE, Apache-2.0,
> multimodal, 45T training tokens) — read alongside TML's own announcement
> page, model card, and training data documentation. TML is explicit that
> Inkling is not a frontier model but a fine-tuning base for their Tinker
> platform; the announcement page adds architectural detail (DeepSeek-V3-style
> MoE with relative positional embeddings instead of RoPE, encoder-free
> audio/vision), a self-fine-tuning demo, an RL-at-scale chart showing
> emergent chain-of-thought compression, and dual-grader factuality training —
> none of which appear in Willison's four-paragraph summary.

## Source Context

- **Type**: blog-post (Simon Willison's link-blog, ~230 words of original
  commentary across four short paragraphs; auto-discovered via trusted feed
  `simon-willison`). Per MINER.md §1, this note follows four linked pages the
  post points at: Thinking Machines Lab's own announcement
  (`thinkingmachines.ai/news/introducing-inkling/`), the Inkling model card
  (`thinkingmachines.ai/model-card/inkling/`), the Training Data Documentation
  page (`thinkingmachines.ai/training-data-documentation/`), and the Tinker
  product page (`thinkingmachines.ai/tinker/`, skimmed for context only).
- **Author credibility**: Simon Willison is a designated `trusted-feed` source
  in this repo (creator of Django, Datasette, `sqlite-utils`, `llm`); for this
  post he is a curator/tester, not the primary technical source — he ran his
  own pelican-SVG and image-description tests against the live Tinker API
  (his standard cross-model evaluation ritual, corroborating his methodology
  in other notes in this corpus) but the architectural, training, and
  benchmark claims originate from Thinking Machines Lab's own announcement,
  model card, and training-data-documentation pages. TML is Mira Murati's
  lab; the announcement page and model card are first-party vendor
  documentation, not independently audited.
- **Scope**: Covers Inkling's architecture, training regime, RL-at-scale
  results, multimodal design, epistemics/safety training, self-reported
  benchmark scores against six open- and closed-weight competitors,
  deployment/availability partnerships, and the (explicitly thin) training
  data documentation. Does NOT cover: independent third-party benchmark
  verification, the Inkling-Small full release (still in testing at
  publication), Thinking Machines Lab's "Connectionism" research blog, or the
  Tinker platform's own architecture beyond what's needed to contextualize
  Inkling's fine-tuning positioning.

## Extracted Claims

### Claim 1: Inkling is a 975B-total/41B-active-parameter Mixture-of-Experts transformer, Apache-2.0 licensed, trained on 45 trillion tokens of text, images, audio, and video, with up to a 1M-token context window
- **Evidence**: Stated identically (modulo phrasing) in Willison's post, TML's announcement page, and the model card's "Model properties" table — three independent restatements of the same headline specs from the same underlying vendor source.
- **Confidence**: settled (specific, repeatedly-stated figures corroborated verbatim across the announcement, model card, and Willison's summary)
- **Quote**: "Our model, called Inkling, is a Mixture-of-Experts transformer with 975B total parameters, 41B active. It supports a context window of up to 1M tokens. It was pretrained on 45 trillion tokens of text, images, audio and video." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Our assessment**: The headline scale (975B/41B) sits between the mid-2026 open-weights field's other large MoE releases (Nemotron 3 Ultra, GLM 5.2, DeepSeek V4 Pro, Kimi K2.6 — all named as comparison points in TML's own benchmark tables). The Apache-2.0 license is the most permissive tier available and matches Willison's framing of Inkling as a genuinely open (not just open-weights-with-restrictions) release.

### Claim 2: Thinking Machines Lab explicitly frames Inkling as a fine-tuning base model, not a frontier model — "not the strongest overall model available today, open or closed"
- **Evidence**: Direct vendor self-positioning statement, repeated with near-identical wording in both Willison's post (which blockquotes it) and the announcement page itself.
- **Confidence**: settled (an explicit first-party statement, not an inference)
- **Quote**: "Inkling is not the strongest overall model available today, open or closed. Instead, a combination of qualities makes it a good open-weights base for customization: multimodal capabilities, efficient thinking, and availability on Tinker for fine-tuning." (`thinkingmachines.ai/news/introducing-inkling/`, blockquoted by Willison)
- **Our assessment**: This is a deliberate, disclosed positioning choice rather than an oversight — TML's own benchmark tables (Claim 6) show Inkling trailing Claude Fable 5 and GPT 5.6 Sol on most reasoning/agentic evals, which corroborates the stated positioning rather than contradicting it. For practitioners: Inkling should be evaluated as a fine-tuning starting point (comparable to base/pretrained-model tier in `blog-simonwillison-open-source-ai-gap-map.md` Claim 5's maturity ladder), not benchmarked head-to-head against frontier closed models for direct deployment.

### Claim 3: TML's own Training Data Documentation page is short and generic — it describes data sourcing categories in template language ("publicly available sources," "acquired from third parties," "synthetically generated") without naming any specific dataset, source, or license
- **Evidence**: Directly read the full Training Data Documentation page (`thinkingmachines.ai/training-data-documentation/`, fetched 2026-07-21) — nine numbered sections, all boilerplate, explicitly stated to be generic ("This information reflects general practices, not specific to any single model") rather than Inkling-specific.
- **Confidence**: settled (read directly from the primary document; the genericness is a structural property of the document, independently verifiable by anyone who reads it)
- **Quote**: "This document provides information regarding the datasets used by Thinking Machines Lab to develop its generative artificial intelligence systems and services, including its models (collectively "AI services"). This information reflects general practices, not specific to any single model." (`thinkingmachines.ai/training-data-documentation/`)
- **Quote (Willison's characterization)**: "The model card is much shorter than I've come to expect from US AI labs. It links to even shorter Training Data Documentation with almost nothing of interest in it." (`simonwillison.net/2026/Jul/16/inkling/`)
- **Our assessment**: Willison's characterization checks out against the primary source: the document's nine sections amount to "we used public data, third-party data, and synthetic data, and we cleaned it" with no dataset names, no license inventory, and no per-modality provenance breakdown. This directly instantiates the "disclosure gap" concept from `blog-simonwillison-open-source-ai-gap-map.md` Claim 6 — Inkling is Stage-5-mature on openness axes that are easy to score (license, weight availability) while remaining opaque on the axis (training data provenance) that the Gap Map's methodology explicitly separates out as a distinct, unresolved gap type even for otherwise-mature categories.

### Claim 4: Inkling's architecture departs from the common open-weights recipe in three specific ways: relative positional embeddings instead of RoPE, short convolutions on attention/MLP branches, and a DeepSeek-V3-style MoE router with 256 routed + 2 shared experts (6 active per token)
- **Evidence**: Detailed architectural description in the announcement's "Architecture" section, citing two academic papers (Shaw et al. 2018 for relative position representations; the DeepSeek-V3 MoE design as the base recipe) as the basis for the design choices.
- **Confidence**: emerging (specific, technically coherent vendor architectural description with cited prior work, but not independently verified against the released weights/code by this note)
- **Quote**: "The MoE design largely follows DeepSeek-V3. Each MoE layer contains 256 routed experts and 2 shared experts, with 6 routed experts active per token. Inkling uses a sigmoid-based router with an auxiliary-loss-free load-balancing bias. [...] For attention, we interleave sliding-window and global layers at a 5:1 ratio with 8 KV heads. We find that encoding position with a relative positional embedding [...] performs better and extrapolates better to longer sequences than the more widely adopted Rotary Positional Embedding (RoPE). We also apply short convolutions at two points — after the key and value projections in each attention layer, and on the attention and MLP residual branch outputs before they rejoin the main residual stream." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Our assessment**: The RoPE-vs-relative-positional-embedding choice is notable because RoPE has been the default for most large open-weights transformers released in 2024–2026 (including, per the corpus, DeepSeek and Gemma variants); TML's explicit claim that relative positional embeddings "extrapolate better to longer sequences" is a direct, falsifiable architectural counter-bet against the current default, worth flagging for anyone building long-context evaluation harnesses against Inkling specifically.

### Claim 5: Inkling's multimodal components (audio and vision) are trained from scratch with an encoder-free architecture — audio as dMel spectrograms, images as 40×40-pixel patches via a four-layer hierarchical MLP (hMLP) — explicitly to serve as the background reasoning model for TML's separately-announced real-time "interaction models" system
- **Evidence**: Direct architectural description with stated design rationale (compatibility with the interaction-model system) and two cited papers for the specific techniques (dMel; hMLP/"Three things everyone should know about Vision Transformers").
- **Confidence**: emerging (specific, cited technical description; the stated purpose — serving as the interaction-models background reasoner — is a design intent claim, not yet demonstrated in this source)
- **Quote**: "A major goal of Inkling's design is to serve as the background reasoning model in the interaction models system we recently introduced. [...] The multimodal components were trained from scratch on general-domain data. We opted for an encoder-free architecture for audio and vision inputs, consistent with the interaction model design. Audio signals are input as dMel spectrograms [...], while images are encoded as patches of 40x40 pixels using a four-layer hMLP." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Our assessment**: This directly extends `blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 7 (TML-Interaction-Small's "encoder-free early fusion" architecture, jointly trained without pretrained encoders). That earlier note documented the 276B-parameter real-time interaction model itself; this source reveals the follow-on piece — Inkling is being positioned as the large-scale asynchronous *background reasoner* that pairs with a (smaller, faster) foreground interaction model, per the foreground/background split documented in that same prior note's Claim 10. TML is building a matched architectural family (shared encoder-free multimodal philosophy) across both its real-time and background-reasoning model lines, not two unrelated products.

### Claim 6: On TML's own benchmark suite, Inkling scores competitively with other open-weights models (Nemotron 3 Ultra, Kimi K2.5/K2.6, GLM 5.2, DeepSeek V4 Pro) but trails closed frontier models (Claude Fable 5, GPT 5.6 Sol, Gemini 3.1 Pro) on most reasoning, agentic, and factuality evals — while leading on safety refusal (FORTRESS Adversarial)
- **Evidence**: A full benchmark table (identical in the announcement page and the model card's "Evaluations" section) spanning reasoning (HLE, AIME 2026, GPQA Diamond), agentic coding (SWEBench Verified/Pro, Terminal Bench 2.1), agentic-general (GDPVal-AA v2, MCP Atlas, Tau 3 Banking, Toolathlon, BrowseComp), factuality (SimpleQA Verified, AA Omniscience), chat (IFBench, Global-MMLU-Lite), vision (MMMU Pro, Charxiv RQ), audio (Audio MC, MMAU, VoiceBench), and safety (FORTRESS, StrongREJECT) — all at effort=0.99, temperature 1.0.
- **Confidence**: emerging (vendor-run benchmarks on the vendor's own model, with stated methodology caveats — e.g., "a small number of [Terminal Bench] solutions were found to be contaminated from web search and were assigned a score of 0" — and explicit reliance on third-party-reported scores, via Artificial Analysis, for some competitor rows)
- **Quote**: "Inkling shows the strongest built-in safeguards of any open-weights model we compared on FORTRESS, a benchmark that tests refusal of requests related to weapons and violence alongside benign look-alike queries." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Concrete numbers** (from the shared announcement/model-card table, effort=0.99): HLE (text only) Inkling 29.7% vs. Claude Fable 5 (max) 53.3% and GPT 5.6 Sol 47.2%; SWEBench Verified Inkling 77.6% vs. Claude Fable 5 95.0%; FORTRESS Adversarial Inkling 78.0% vs. Claude Fable 5 96.0% and Nemotron 3 Ultra 77.6% — Inkling actually trails Claude Fable 5 on the adversarial-safety metric despite the "strongest among open-weights" framing, which is scoped correctly to the open-weights comparison set only.
- **Our assessment**: The gap to closed frontier models (roughly 15–25 percentage points on reasoning/agentic evals) is consistent with Claim 2's stated positioning — this is not a frontier-competitive model, and TML does not claim it is. The FORTRESS Adversarial safety framing ("strongest... of any open-weights model") is accurate as scoped but should not be read as "safest model overall"; Claude Fable 5 scores materially higher (96.0% vs. Inkling's 78.0%) on the same metric among all models compared.

### Claim 7: Inkling supports "controllable thinking effort," letting operators trade token spend for benchmark performance along a continuous curve, and reaches a given Terminal Bench 2.1 score at roughly one-third the mean generated tokens of Nemotron 3 Ultra
- **Evidence**: An effort-sweep chart (effort parameter 0.2 to 0.99) plotted against mean generated tokens on three benchmarks (Terminal Bench 2.1, Humanity's Last Exam, IFBench), with named competitor models shown at their default operating points for comparison.
- **Confidence**: emerging (vendor-run internal comparison; the claim is quantitatively specific but the competitor models are shown only at a single default point rather than their own full effort curves, which would be the fairer comparison)
- **Quote**: "Sweeping Inkling's effort setting from 0.2 to 0.99 traces its performance against mean generated tokens on Terminal Bench 2.1, HLE, and IFBench; competing models are shown at their default operating point. Inkling reaches a given score at fewer tokens — for example, it matches Nemotron 3 Ultra on Terminal Bench 2.1 at roughly a third of the tokens." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Our assessment**: This is architecturally the same "controllable thinking effort" pattern already documented for TML-Interaction-Small's foreground/background split (`blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 9) but generalized to a single continuously-tunable dial rather than a two-model split. For cost-sensitive fine-tuning deployments (Inkling's stated use case), a token-efficiency claim of this magnitude — if it holds under independent testing — would materially change the cost calculus of choosing Inkling as a base model over a token-hungrier open-weights alternative.

### Claim 8: TML observed an emergent, unintended compression of chain-of-thought verbosity over the course of large-scale RL training — the model's reasoning traces became more "telegraphic" (dropping articles and connectives) while remaining comprehensible and without degrading the final answer, purely as a side effect of token-efficiency pressure rather than an explicit training target
- **Evidence**: A worked before/after example (the same math problem's reasoning trace shown early vs. late in RL training) plus an explicit statement that this was not a targeted reward signal, with a corroborating citation to a similar effect reported by a different lab (Cognition, training SWE-1.7).
- **Confidence**: emerging (a specific, illustrated observation from the vendor's own training run, corroborated by an independent citation to another lab's similar finding, but not independently reproduced in this source)
- **Quote**: "We also observed an emergent shift in the reasoning style over the course of RL training. The chain of thought became more concise over time, dropping grammatical overhead while remaining comprehensible and leaving the final response unaffected. This wasn't targeted by the reward — efficiency alone drove the compression. A similar effect was also recently noted by the Cognition team in the process of training SWE-1.7." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Quote (the compression itself)**: "The late-RL trace drops articles and connectives — 'We need to understand' becomes 'We need determine' — while staying comprehensible and reaching the same answer." (`thinkingmachines.ai/news/introducing-inkling/`, image caption)
- **Our assessment**: This is a genuinely novel claim to the corpus: an emergent, reward-unspecified drift toward terser (grammatically degraded) reasoning traces purely from RL optimization pressure, cross-corroborated by a second lab (Cognition/SWE-1.7) independently observing the same phenomenon. This has a direct practical implication for anyone building tooling that parses or displays chain-of-thought traces for debugging or auditability — traces from heavily-RL'd models may become progressively less human-readable even as task performance improves, which is a legibility/oversight tradeoff worth flagging distinct from the capability tradeoff.

### Claim 9: Inkling's factuality/epistemics training combines two automated graders — a rubric grader (checklist-based, prone to being gamed by "spraying plausibly relevant facts") and a claims grader (verifies each factual claim via agentic web search, penalizing unverified claims) — used together specifically to avoid trading helpfulness for hallucination reduction or vice versa
- **Evidence**: Explicit architectural/training-process description with a named failure mode for the rubric-only approach and a named mechanism (agentic web search) for the claims grader.
- **Confidence**: emerging (specific training-process description from the vendor; the stated outcome — "improve helpfulness and reduce hallucination at the same time" — is a vendor claim without independent measurement isolated to this mechanism)
- **Quote**: "We did RL with two automated graders: a rubric grader and claims grader. The first grader scores each response against a checklist of what a good answer should contain. Rubrics can penalize errors in principle, but in practice they emphasize recall and can be hacked by models spraying plausibly relevant facts hoping to match rubric items. The claims grader verifies each factual claim in the response, penalizing claims that don't check out. It performs agentic web search for claim verification, not relying solely on its own knowledge. Together, the two graders improve helpfulness and reduce hallucination at the same time, rather than trading one for the other." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Our assessment**: The named rubric-gaming failure mode ("spraying plausibly relevant facts hoping to match rubric items") is a specific, reusable red flag for anyone designing rubric-based LLM-judge evaluations elsewhere in this guide's corpus — it names a concrete way rubric graders get gamed that is distinct from more commonly-discussed judge-model failure modes (e.g., verbosity bias, position bias). The two-grader pairing (recall-oriented rubric + precision-oriented claims-verification) is a reusable design pattern for any RL post-training pipeline aiming at factuality.

### Claim 10: Thinking Machines Lab demonstrated Inkling fine-tuning itself end-to-end via the Tinker API — writing its own training objective and synthetic dataset for a target behavior (never using the letter "e"), launching the training run, evaluating the result, and self-updating to the new checkpoint, completing in roughly 27 minutes
- **Evidence**: A detailed worked demo embedded in the announcement page (terminal-style transcript with actual code, log lines, and a checkpoint hash), explicitly framed by TML as "what customization means in practice."
- **Confidence**: emerging (a single staged demonstration by the vendor, not an independently reproduced or randomly-sampled example; the target task — a lipogram constraint — is a clean, easily-verified toy behavior rather than a representative production fine-tuning task)
- **Quote**: "To show what customization means in practice, we asked Inkling to fine-tune itself. Using Tinker, the model wrote its own fine-tuning job, ran it, and evaluated the result." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Quote (result)**: "PASS. The pipeline finished after ~27 minutes. objective_improved=true; [...] Now switching to the improved version." (`thinkingmachines.ai/news/introducing-inkling/`, terminal transcript)
- **Our assessment**: This is a marketing demo for the Tinker platform as much as it is a claim about Inkling itself, and the target behavior (never use the letter "e") is deliberately chosen because it's cheap to write an automated verifier for (`if 'e' in answer: return 0.0`) — it doesn't generalize to fine-tuning objectives that lack a trivial programmatic reward function. Still, it is a concrete, code-level illustration of an agent-driven self-improvement loop (write objective → generate synthetic data → train → evaluate → hot-swap weights) that is architecturally similar to (but a different domain from) the judge-model goal-evaluation loop documented in `blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 4 — both use an external evaluation step to decide whether to continue or commit a change, but Hermes Agent applies it to conversational task completion while this applies it to model weight updates.

### Claim 11: Willison assesses Inkling as strengthening the US open-weights ecosystem specifically because it is competitive with Chinese open-weight releases, positioning it alongside NVIDIA Nemotron and Gemma 4 as a "viable contender"
- **Evidence**: Willison's own editorial assessment, not a TML claim — his independent judgment based on having tested and written about the referenced comparison models in prior posts (per this corpus, `blog-simonwillison-deepseek-v4.md` and Google's Gemma 4 coverage).
- **Confidence**: anecdotal (an editorial opinion from a credible, experienced commentator, not a benchmark-backed claim — Willison does not cite specific comparative numbers against Chinese open-weights models in this post)
- **Quote**: "There's a lot to like about this release. It's Apache-2.0 licensed, and looks competitive with the open weight models coming out of China - it's good to see the US open weights ecosystem gain a new viable contender to join NVIDIA Nemotron and Gemma 4." (`simonwillison.net/2026/Jul/16/inkling/`)
- **Our assessment**: This framing is directionally consistent with the vendor's own benchmark table (Claim 6), which does show Inkling ahead of or competitive with GLM 5.2 and DeepSeek V4 Pro (both Chinese-origin open-weights models) on several evals — but Willison's post itself doesn't do that comparison explicitly; it's an assessment based on general familiarity rather than a documented head-to-head in this source. Treat the "competitive with Chinese models" framing as directionally plausible but not independently verified within this note's scope.

### Claim 12: Inkling requires substantial self-hosting hardware — at least 2TB aggregated VRAM for the BF16 checkpoint (8× NVIDIA B300 or 16× NVIDIA H200), or at least 600GB for the quantized NVFP4 checkpoint (4× B300 in W4A4, or 8× H200 in W4A16) — and is available through five third-party inference API providers plus direct Hugging Face weight downloads
- **Evidence**: Directly stated in the model card's "Methods of distribution" section (hardware table) and the announcement's "Inkling availability" section (partner list).
- **Confidence**: settled (specific, itemized hardware and partner requirements from the primary model card, not inferred or estimated)
- **Quote**: "The BF16 checkpoint requires a GPU cluster with at least 2 TB of aggregated VRAM. [...] The NVFP4 checkpoint offers a quantized alternative that reduces the aggregated VRAM requirement to at least 600 GB." (`thinkingmachines.ai/model-card/inkling/`)
- **Quote (partners)**: "Inkling is available via APIs on Together AI, Fireworks, Modal, Databricks, and Baseten. We worked with RadixArk to provide open-source inference and RL support in SGLang and Miles. We worked with Inferact to support inference in vLLM, with Lightseek for inference in TokenSpeed, and with Unsloth for inference in llama.cpp. Finally, we partnered with Hugging Face on integration with transformers." (`thinkingmachines.ai/news/introducing-inkling/`)
- **Our assessment**: The hardware floor (2TB VRAM even for BF16) puts genuine self-hosting out of reach for all but well-resourced teams — this is consistent with Inkling's stated purpose (a Tinker-hosted fine-tuning base) rather than a model designed for individual-developer local deployment, unlike smaller open-weights releases in this corpus (e.g., Gemma 4 12B's laptop/edge-hardware framing in `blog-google-gemma-4-12b-laptop-ai-edge.md`). The six-provider inference-partner list (plus direct HF weights) is a concrete data point on how quickly a major lab's open-weights release gets distributed across the third-party inference ecosystem.

## Concrete Artifacts

### Architecture summary (verbatim specs, `thinkingmachines.ai/news/introducing-inkling/` and model card)

```
Inkling (Thinking Machines Lab, released July 15, 2026)

SCALE
  Total parameters:      975B (MoE)
  Active per token:      41B
  Layers:                66-layer decoder-only transformer
  Context window:        up to 1M tokens
  License:               Apache 2.0

ARCHITECTURE
  MoE design:            follows DeepSeek-V3 recipe
                          256 routed experts + 2 shared experts
                          6 routed experts active per token
                          sigmoid-based router, aux-loss-free load balancing
  Attention:              sliding-window : global layers = 5:1, 8 KV heads
  Position encoding:      relative positional embedding (NOT RoPE)
                          — claimed better long-sequence extrapolation
  Extra layers:           short convolutions after K/V projections and on
                          attention/MLP residual branch outputs

MULTIMODAL (encoder-free, trained from scratch)
  Audio input:            dMel spectrograms (WAV, 16kHz, <=20 min optimal)
  Image input:            40x40px patches via 4-layer hierarchical MLP (hMLP)
                          (40px-4096px per dimension optimal)
  Design goal:            background reasoning model for TML's "interaction
                          models" real-time system

TRAINING
  Pretraining tokens:     45 trillion (text, images, audio, video)
  Optimizer:              Muon (large matrix weights) + Adam (other params)
  Weight decay:            coupled to square of learning rate (stability)
  Hardware:               NVIDIA GB300 NVL72 systems
  RL scale:               30M+ rollouts, 2 long continuous runs
  RL reward trajectory:   SFT init 0.264 -> released checkpoint 0.356
                          (log-linear improvement on held-out reasoning evals)
  Numerics:               BF16, MXFP8, NVFP4

SIBLING MODEL
  Inkling-Small (preview): 276B total, 12B active
                          matches/exceeds Inkling on many benchmarks
                          full weights pending (still in testing at launch)

SELF-HOSTING HARDWARE
  BF16 checkpoint:        >=2TB aggregated VRAM
                          (8x NVIDIA B300, or 16x NVIDIA H200)
  NVFP4 checkpoint:       >=600GB aggregated VRAM
                          (4x B300 W4A4 [needs SM100+], or 8x H200 W4A16)

DISTRIBUTION
  Direct:                 Hugging Face (original + NVFP4 checkpoints)
  Managed fine-tuning:    Tinker (64K / 256K token context options,
                          50% launch discount)
  Inference API partners: Together AI, Fireworks, Modal, Databricks, Baseten
  OSS inference support:  SGLang + Miles (via RadixArk), vLLM (via Inferact),
                          TokenSpeed (via Lightseek), llama.cpp (via Unsloth),
                          transformers (via Hugging Face)
```

### Selected benchmark scores (verbatim from shared announcement/model-card table, effort=0.99, temp=1.0)

```
                          Inkling  Nemotron3Ultra  Kimi K2.6  GLM5.2  DeepSeekV4Pro  ClaudeFable5(max)  GPT5.6Sol
HLE (text only)            29.7%    26.6%           40.1%     35.9%   35.9%          53.3%              47.2%
AIME 2026                  97.1%    94.2%           99.2%     96.4%   96.7%          99.9%              99.9%
SWEBench Verified          77.6%    70.7%           80.0%     80.2%   80.6%          95.0%              82.2%
Terminal Bench 2.1         63.8%    56.4%           82.7%     71.3%   64%            84.6%              89.5%
SimpleQA Verified          43.9%    32.4%           38.1%     38.7%   57.0%          68.3%              71.6%
FORTRESS (Adversarial)     78.0%    77.6%           71.3%     65.6%   36.0%          96.0%              82.4%
StrongREJECT                98.6%    98.7%           98.5%     99.8%   98.6%          98.7%              98.5%

Source: thinkingmachines.ai/news/introducing-inkling/ and
        thinkingmachines.ai/model-card/inkling/ (identical table)
Caveats stated by TML: some Terminal Bench 2.1 solutions scored 0 for
web-search contamination; some competitor scores are third-party-reported
via Artificial Analysis rather than internally reproduced.
```

### Token-efficiency claim (verbatim)

```
"Inkling spends one third as many tokens to achieve the same performance
as Nemotron 3 Ultra on Terminal Bench." — thinkingmachines.ai/news/introducing-inkling/
```

### Willison's own hands-on test (curl command against Tinker API, verbatim from post)

```bash
curl "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1/chat/completions" \
  -H "Authorization: Bearer $TINKER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "thinkingmachines/Inkling",
    "messages": [
      {"role": "user", "content": "Generate an SVG of a pelican riding a bicycle"}
    ],
    "stream": false
  }'
```
Willison also sent a multimodal follow-up (image_url + text) asking Inkling
to describe its own rendered SVG; Inkling described the pelican as
resembling "a stork or seagull" — noted here as Willison's standard
pelican-benchmark methodology (also used in his other model-review posts in
this corpus) applied to Inkling specifically.

## Cross-References

- **Extends** `blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 7
  (TML-Interaction-Small's encoder-free early-fusion architecture) and
  Claim 10 (the foreground/background model split, sharing context): Claim 5
  here reveals that Inkling is explicitly designed as the *background
  reasoning model* for that same interaction-models system, and shares its
  encoder-free multimodal design philosophy (dMel audio, patch-based vision).
  The two notes together now document both halves of TML's real-time
  multimodal architecture family — a fast foreground interaction model
  (TML-Interaction-Small, 276B/12B active) and a large background reasoner
  (Inkling, 975B/41B active) built on compatible architectural principles.
- **Extends** `blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 9's
  interactivity/intelligence tradeoff framing for TML-Interaction-Small:
  Claim 7 here shows the same lab applying a continuously-tunable
  effort/token-cost dial (rather than a discrete foreground/background split)
  to a different model in the same family, generalizing the pattern.
- **Extends** `blog-thebatch-hermes-openclaw-tml-cybersecurity.md` Claim 4
  (Hermes Agent's judge-model goal-evaluation loop): Claim 10 here (Inkling's
  self-fine-tuning demo) applies the same "external evaluator decides whether
  to commit" pattern to model-weight updates rather than conversational task
  completion — a different application of the actor/evaluator separation
  principle.
- **Corroborates** `blog-simonwillison-open-source-ai-gap-map.md` Claim 6
  (the "disclosure" gap type — closed frontier labs' training data/recipe
  staying invisible even when the model itself is otherwise mature): Claim 3
  here is a directly-observed instance of exactly that gap in an
  otherwise-fully-open (Apache-2.0, weights-on-Hugging-Face) release —
  Inkling scores well on license/weight-availability openness while its
  Training Data Documentation remains generic boilerplate with no named
  datasets. This is independent evidence, from a source the Gap Map note
  didn't cover, that the disclosure gap persists even in the most
  permissively-licensed 2026 open-weights releases.
- **Corroborates** `blog-google-gemma-4-12b-developer-guide.md` Claim 1
  (Gemma 4 12B's encoder-free multimodal architecture, feeding audio/vision
  directly into the LLM backbone with no separate pretrained encoders):
  Inkling's encoder-free design (Claim 5) is an independent, larger-scale
  instance of the same architectural trend — two different labs (Google,
  Thinking Machines) converging on encoder-free multimodal fusion for their
  2026 open-weights releases, at very different parameter scales (12B vs.
  975B total).
- **Novel** (new to corpus):
  - The specific architectural departures from the DeepSeek-V3-style MoE
    baseline (relative positional embeddings instead of RoPE; short
    convolutions on attention/MLP branches) are the first documented
    RoPE-alternative claim in the corpus for a large 2026 open-weights model.
  - The emergent chain-of-thought compression under RL (Claim 8),
    cross-corroborated with an independent Cognition/SWE-1.7 observation, is
    new to the corpus — prior notes document RL improving task performance
    but not this legibility side effect.
  - The dual rubric-grader/claims-grader factuality training pattern
    (Claim 9), including the named rubric-gaming failure mode, is new to the
    corpus and reusable for LLM-judge design discussions elsewhere in the
    guide.
  - The self-fine-tuning-via-Tinker demo (Claim 10) is the first documented
    example in the corpus of a model performing an end-to-end weight-update
    loop on itself (write objective -> generate data -> train -> evaluate ->
    hot-swap) rather than a conversational or code-editing self-improvement
    loop.
  - The self-hosting hardware floor (Claim 12: >=2TB VRAM even at BF16) is
    the most demanding hardware requirement documented in the corpus for any
    single open-weights model, useful as a concrete data point for
    "open-weights does not mean self-hostable by most teams."

## Guide Impact

- **Model-selection guidance (wherever the guide discusses choosing an
  open-weights base model for fine-tuning)**: Cite Inkling as a worked
  example of a lab explicitly disclosing "this is a base model, not a
  frontier model" (Claim 2) with benchmark data to back the positioning
  (Claim 6). Recommend the guide draw the distinction TML itself draws:
  evaluate a fine-tuning base on breadth, multimodal coverage, and token
  efficiency (Claim 7), not on raw frontier-benchmark parity.
- **LLM-judge / evaluation-rubric design sections**: Add the rubric-grader
  gaming failure mode (Claim 9: "spraying plausibly relevant facts hoping to
  match rubric items") as a named anti-pattern, alongside the two-grader
  mitigation (rubric grader + independent claims-verification grader via
  agentic search) as a concrete design pattern for factuality-focused RL or
  eval pipelines.
- **Chain-of-thought / reasoning-trace legibility discussions**: Add Claim 8
  (emergent CoT compression under RL, corroborated by Cognition's
  independent observation) as evidence that heavily-RL'd models' reasoning
  traces may become progressively harder for humans to audit even as
  measured task performance improves — relevant to any guide section
  discussing chain-of-thought monitoring or interpretability as a safety
  layer.
- **Open-weights licensing / "openness" framing sections**: Use Claim 3
  (Inkling's generic Training Data Documentation) as a second, independently-
  sourced concrete instance of the disclosure-gap concept already introduced
  via `blog-simonwillison-open-source-ai-gap-map.md` — strengthens the case
  for treating "Apache-2.0 + weights on Hugging Face" and "training data
  provenance disclosed" as two separate axes practitioners should evaluate
  independently when picking an "open" model for compliance-sensitive use
  cases.
- **Hardware/deployment planning sections**: Cite Claim 12's hardware table
  (2TB VRAM for BF16, 600GB for NVFP4) as a concrete self-hosting cost
  floor when the guide discusses total cost of ownership for self-hosted vs.
  API-based open-weights deployment.

## Extraction Notes

- **Verbatim text obtained via direct `curl`, not an AI-summarizing fetch
  tool**: consistent with the prior note's flagged lesson
  (`blog-simonwillison-open-source-ai-gap-map.md` Extraction Notes), all raw
  HTML for `simonwillison.net`, `thinkingmachines.ai/news/introducing-inkling/`,
  `thinkingmachines.ai/model-card/inkling/`, and
  `thinkingmachines.ai/training-data-documentation/` was fetched directly
  with a browser-UA `curl` request and parsed for text, not summarized by an
  intermediary model. All quotes in this note were copied character-for-
  character from that fetched raw HTML (converted to plain text by stripping
  tags, no rewording).
- **Linked pages followed (4, within MINER.md §1's up-to-5 budget)**:
  Thinking Machines Lab's announcement page (the largest source of
  substantive claims — self-fine-tuning demo, architecture, RL-at-scale
  chart, benchmark tables, deployment partners), the Inkling model card
  (largely duplicates the announcement's benchmark table but adds the
  hardware/distribution section used in Claim 12), the Training Data
  Documentation page (read in full — nine short sections, confirmed thin per
  Willison's characterization), and the Tinker product page (skimmed only
  for context on the fine-tuning platform Inkling is designed for; not
  separately extracted since it predates this specific release and is not
  Inkling-specific).
- **Benchmark tables are vendor-run and duplicated verbatim between the
  announcement page and the model card** — this note treats them as one
  source, not independent corroboration, since both pages are published by
  the same organization from what is evidently the same underlying results
  table.
- **No contradictions identified** against existing source notes. The
  "disclosure gap" instantiation (Claim 3) corroborates rather than
  contradicts `blog-simonwillison-open-source-ai-gap-map.md`'s existing
  framing of that concept; no issue filed per MINER.md §4a.
- **Overall confidence set to `emerging`**: Claims 1, 3, and 12 are `settled`
  (directly read from primary machine-readable/documented sources, or
  cross-corroborated verbatim across multiple TML-published pages). Claims
  2, 4–10 are `emerging` (specific vendor-described mechanisms and
  vendor-run benchmarks, technically detailed but not independently
  reproduced). Claim 11 is `anecdotal` (Willison's own editorial judgment,
  not benchmark-backed within this source). The note-level confidence
  reflects this mixed bag: strong on documented specs and hardware/
  distribution facts, weaker on performance and positioning claims that rest
  on the vendor's own self-reported evaluation.
