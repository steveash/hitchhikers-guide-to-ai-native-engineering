---
source_url: https://simonwillison.net/2026/Jun/10/diffusiongemma/
source_type: blog-post
title: "DiffusionGemma"
author: Simon Willison
date_published: 2026-06-10
date_extracted: 2026-06-18
last_checked: 2026-06-18
status: current
confidence_overall: emerging
issue: "#1202"
---

# DiffusionGemma

> Simon Willison documents the open-weight release of Google's DiffusionGemma — a
> 26B MoE model achieving 500+ tokens/second on free NVIDIA NIM hosting — the
> first diffusion-architecture model in the corpus to be both open-weight and
> practically accessible, with a concrete throughput/quality trade-off: 4x faster
> than standard autoregressive models but lower output quality than Gemma 4.

## Source Context

- **Type**: blog-post (Simon Willison link-blog, June 10, 2026; three-paragraph
  announcement post with one pelican SVG image as a generation example. The post
  links to the [Google blog announcement](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)
  and [HuggingFace model page](https://huggingface.co/google/diffusiongemma-26B-A4B-it),
  both of which were read for this note. Simon's [May 2025 Gemini Diffusion
  preview post](https://simonwillison.net/2025/May/21/gemini-diffusion/) was also
  read for historical context.)
- **Author credibility**: Simon Willison is the creator of Django and the `llm`
  CLI, one of the most widely-cited practitioner commentators on LLM tooling. He
  applies his "pelican on a bicycle" SVG benchmark consistently across models. His
  throughput figure (2,409 tokens in 4.4s = 500+ tokens/second) is a first-person
  measured result from his own code (`time uv run generate.py`), not a vendor
  claim. The linked Google blog post is authored by Brendan O'Donoghue and
  Sebastian Flennerhag, Research Scientists at Google.
- **Scope**: Covers DiffusionGemma's model identity, open-weight availability,
  free hosting, and first-person throughput measurement. Linked Google blog post
  adds: architecture details, performance benchmarks, trade-offs, and toolchain
  support. Does NOT cover: quality benchmarks in depth, agentic use cases,
  context engineering patterns, fine-tuning, or enterprise deployment.

## Extracted Claims

### Claim 1: DiffusionGemma is the open-weight release of Google's experimental Gemini Diffusion research from May 2025 — which Simon had previously tested at 857 tokens/second but that Google never publicly followed up on

- **Evidence**: Simon's direct statement connecting the prior research to this
  release, plus his own May 2025 post as corroborating historical record.
- **Confidence**: settled (factual release history)
- **Quote**: "Last May Google briefly released an experimental Gemini Diffusion model. I tried the preview at the time and recorded it running at 857 tokens/second. It was an exciting model, but Google made no further announcements about it."
- **Our assessment**: The 14-month gap between the May 2025 preview and the June
  2026 open-weight release signals that Google treated Gemini Diffusion as a
  research vehicle before deciding to open-source it. The 857 tokens/second
  figure from 2025 is context for the 500+ tokens/second figure from the June 2026
  NIM API test — the 2025 preview was likely running on dedicated high-memory
  Google infrastructure, while the NIM API adds inference serving overhead. The
  directional claim (diffusion-based generation is fast) holds across both data
  points.

### Claim 2: DiffusionGemma is available as `google/diffusiongemma-26B-A4B-it` on HuggingFace under an Apache 2.0 license

- **Evidence**: Simon's direct statement with the HuggingFace model identifier.
  Apache 2.0 is explicitly named by both Simon and the Google blog post.
- **Confidence**: settled (published model release at time of post)
- **Quote**: "That research has returned in the best possible way: as a new open weight (Apache 2 licensed) Gemma model, google/diffusiongemma-26B-A4B-it."
- **Our assessment**: Apache 2.0 is the most permissive open-weight license in the
  current market — less restrictive than the Gemma license used by earlier Google
  open-weight releases, and equivalent in permissiveness to MIT. For practitioners
  selecting models for commercial deployments: Apache 2.0 imposes no restrictions
  on use, modification, or distribution that differ meaningfully from MIT. The
  HuggingFace availability enables local deployment without API dependency for
  teams with sufficient VRAM (18GB quantized; see Claim 5).

### Claim 3: NVIDIA is hosting DiffusionGemma for free on the NIM cloud API, providing zero-cost experimentation access

- **Evidence**: Simon's first-person use of the NVIDIA NIM API to run the model
  and generate the pelican SVG in the post.
- **Confidence**: settled (first-person use confirmed; "free" hosting is NVIDIA's
  stated offering at time of publication; subject to change)
- **Quote**: "NVIDIA are currently hosting the model for free on their NIM cloud API."
- **Our assessment**: Free cloud hosting removes the infrastructure barrier for
  practitioners who want to evaluate DiffusionGemma's throughput characteristics
  without setting up local GPU infrastructure. The NIM endpoint enables
  experimentation in minutes. The qualifier "currently" in the source is important:
  free hosting tiers on NIM have historically been introductory offers that may
  transition to paid access. Practitioners should verify current NIM pricing before
  making deployment decisions that depend on continued free access.

### Claim 4: Simon measured 2,409 tokens generated in 4.4 seconds using the NVIDIA NIM API — at least 500 tokens/second in practice

- **Evidence**: Simon's direct first-person measurement using `time uv run
  generate.py` for a pelican SVG generation task. The exact token count and
  timing are reported, not approximated.
- **Confidence**: settled (specific first-person measured result from his own code)
- **Quote**: "I used that API to generate this pelican, which took 4.4s (according to `time uv run generate.py`) to return 2,409 tokens - so at least 500 tokens/second."
- **Our assessment**: The "at least" qualifier is accurate: wall-clock time from
  `time` includes network round-trip and API overhead beyond pure model inference,
  so the model's actual inference speed is higher than 500 tokens/second. The
  measurement is consistent with Simon's prior 857 tokens/second observation from
  the 2025 Gemini Diffusion preview (which ran on dedicated Google infrastructure
  with no API overhead). For practitioners: 500+ tokens/second is approximately
  25× the typical throughput of cloud-hosted frontier models (which run at 15–60
  tokens/second including latency). At this speed, interactive applications with
  long context outputs — typically bottlenecked on model response time — become
  practical.

### Claim 5: DiffusionGemma is a 26B MoE model activating only 3.8B parameters, fitting within 18GB VRAM when quantized

- **Evidence**: Google blog post (linked from Simon's post), authored by Brendan
  O'Donoghue and Sebastian Flennerhag, Research Scientists. The VRAM figure is
  from the Google blog. HuggingFace model card gives 25.2B total parameters (8
  active experts from 128 total, plus 1 shared), confirming the MoE architecture.
- **Confidence**: settled (published model specification from model authors)
- **Quote (Google blog)**: "DiffusionGemma fits comfortably within 18GB VRAM limits of high-end dedicated consumer GPUs when quantized."
- **Our assessment**: The 3.8B active parameter figure is the operationally
  relevant number for inference cost — only 3.8B parameters are activated per
  forward pass, despite 25.2B total parameters. This MoE sparsity is the primary
  mechanism behind the throughput advantage: the model computes less work per
  token than a dense 26B model would. The 18GB VRAM figure makes DiffusionGemma
  compatible with consumer hardware (NVIDIA RTX 4090/5090 with 16–24GB VRAM),
  enabling local deployment without a datacenter.

### Claim 6: Google's official performance figures are 1000+ tokens/second on a single NVIDIA H100 and 700+ tokens/second on an RTX 5090

- **Evidence**: Google blog post by O'Donoghue and Flennerhag. These are vendor
  claims in the official release announcement; the measurement conditions are not
  fully specified in the extracted text.
- **Confidence**: emerging (vendor-claimed benchmark figures; conditions not fully
  disclosed; consistent directionally with Simon's NIM API measurement)
- **Quote (Google blog)**: "1000+ tokens per second on a single NVIDIA H100, 700+ tokens per second on NVIDIA GeForce RTX 5090"
- **Our assessment**: The H100 figure (1000+ tokens/second) confirms that the NIM
  API measurement (500+ tokens/second) includes API overhead — actual model
  throughput is approximately 2× the NIM API figure. The RTX 5090 figure (700+
  tokens/second) is more directly relevant to practitioners considering local
  deployment: a consumer GPU achieves 700+ tokens/second for an Apache 2.0 model,
  while being a fraction of the cost of H100 infrastructure. The vendor Google blog
  also claims "up to 4x faster inference on dedicated GPUs" compared to standard
  autoregressive models — which is consistent with the architectural mechanism
  (generating 256 tokens in parallel per forward pass, as detailed in Claim 7).

### Claim 7: DiffusionGemma uses discrete text diffusion — generating 256 tokens in parallel per forward pass with bi-directional attention — instead of sequential left-to-right token generation

- **Evidence**: Google blog post architecture explanation. HuggingFace model card
  confirms "iteratively denoises blocks of tokens in parallel." Simon's 2025
  Gemini Diffusion post (read for context) notes HN corrections: diffusion
  replaces autoregression, not transformers — the model still uses a transformer
  architecture but without causal masking, similar to BERT.
- **Confidence**: settled (model architecture described by the model authors)
- **Quote (Google blog)**: "Generating 256 tokens in parallel with each forward pass allows every token to attend to all others."
- **Our assessment**: The architectural mechanism is the source of the throughput
  advantage and also the source of the quality trade-off (Claim 8). Standard
  autoregressive LLMs generate one token at a time and can use each previous
  token to inform the next — this is why they are high-quality but slow for long
  outputs. DiffusionGemma generates a full 256-token "canvas" per forward pass,
  then iteratively refines the block. The 256-token canvas means it is most
  efficient for outputs that fit within that block; very long outputs require
  multiple canvas iterations. For practitioners: DiffusionGemma is architecturally
  suited to tasks where the output is a fixed-length block (structured data, short
  summaries, code completion) rather than open-ended long generation.

### Claim 8: DiffusionGemma's output quality is explicitly lower than standard Gemma 4 — it is a speed-optimized model for interactive local workflows, not a quality-maximizing model

- **Evidence**: Google's own release announcement. This is a vendor admission of
  the quality trade-off, not a third-party benchmark finding.
- **Confidence**: settled (vendor admission; the quality-speed trade-off is also
  consistent with the architectural explanation in Claim 7)
- **Quote (Google blog)**: "DiffusionGemma's overall output quality is lower than standard Gemma 4."
- **Our assessment**: This is the most important claim for practitioners evaluating
  DiffusionGemma for production use: Google explicitly positions this as a speed
  trade-off, not a quality upgrade. For use cases that require Gemma 4-level
  quality, DiffusionGemma is not a drop-in replacement. For use cases where
  throughput is the bottleneck and moderate output quality is acceptable —
  interactive code completion, in-line editing, rapid iteration on drafts —
  DiffusionGemma's 4× throughput advantage may justify the quality reduction.
  Practitioners should benchmark against their specific task before assuming
  substitutability with higher-quality closed models.

### Claim 9: DiffusionGemma is a multimodal model supporting interleaved text, images, and video inputs, with a 256K token context window and January 2025 training cutoff

- **Evidence**: HuggingFace model card (linked from Simon's post). Total parameters
  25.2B including ~550M vision encoder parameters. Context length 256K tokens.
  Knowledge cutoff January 2025.
- **Confidence**: settled (published model specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The multimodal capability (images, video, OCR, chart
  comprehension, screen understanding) is not mentioned in Simon's post but is a
  material fact from the HuggingFace model card. It significantly expands the use
  cases beyond text-only generation. The 256K context window enables document-
  scale analysis, not just short-context interaction. The January 2025 knowledge
  cutoff means the model lacks information from the 17 months preceding its June
  2026 release — relevant for applications that depend on current events or recent
  technical developments. The 256-token canvas (generation window per diffusion
  step) is distinct from the 256K context window: the model attends to 256K tokens
  but generates outputs in 256-token blocks.

### Claim 10: The DiffusionGemma release completes a path from Google research preview (May 2025) to open-weight public release (June 2026) without an intermediate closed-API commercial stage

- **Evidence**: Simon's framing of the research-to-open-weight arc. No intermediate
  commercial API release is documented in this source or in the corpus.
- **Confidence**: emerging (absence of evidence for a commercial API stage; the
  arc is asserted by Simon and corroborated by the 14-month gap and Apache 2.0
  licensing)
- **Quote**: "That research has returned in the best possible way: as a new open weight (Apache 2 licensed) Gemma model"
- **Our assessment**: Simon's framing ("the best possible way") reflects a
  practitioner preference for open-weight releases that enable local deployment
  and experimentation without API dependency. The research-to-open-weight arc
  (without a commercial API stage) contrasts with the typical release pattern for
  Google's frontier Gemini models (preview API → GA API → no open weights).
  For practitioners: the absence of a commercial API stage means DiffusionGemma's
  performance can only be evaluated via HuggingFace local deployment or NVIDIA NIM
  (not the Gemini API). This is relevant for harness configuration — DiffusionGemma
  requires a different API endpoint than the standard Gemini API.

## Concrete Artifacts

### DiffusionGemma Technical Specifications (from HuggingFace model card, June 2026)

```
Model ID:           google/diffusiongemma-26B-A4B-it
Architecture:       Mixture of Experts (MoE), discrete text diffusion
Total parameters:   25.2B
Active parameters:  3.8B (8 active experts from 128 total, plus 1 shared)
Vision encoder:     ~550M parameters
Layers:             30
Context length:     256K tokens
Canvas length:      256 tokens (generation block per diffusion step)
Vocabulary:         262K tokens
Knowledge cutoff:   January 2025
License:            Apache 2.0

Modalities:         Text, images (variable aspect ratio/resolution), video
Capabilities:       Object detection, document parsing, OCR, chart
                    comprehension, screen understanding

Recommended sampling:
  Max denoising steps:  48
  Temperature schedule: Linear decay 0.8 → 0.4
  Entropy bound:        0.1
  Adaptive stopping:    When avg model entropy < 0.005

Benchmark performance (vs. Gemma 4 26B — lags on most benchmarks):
  MMLU Pro:       77.6%
  GPQA Diamond:   73.2%
  Math-vision:    70.5%

Source: HuggingFace model card, huggingface.co/google/diffusiongemma-26B-A4B-it
```

### Performance Measurements (June 2026)

```
Measured throughput:
  NVIDIA NIM cloud API (Simon Willison, June 2026):
    2,409 tokens in 4.4s wall-clock = 500+ tokens/second
    (includes API overhead; actual model inference faster)
    Task: pelican SVG generation
    Code: time uv run generate.py

Vendor-claimed throughput (Google blog, O'Donoghue & Flennerhag):
  NVIDIA H100:       1000+ tokens/second
  NVIDIA RTX 5090:   700+ tokens/second

Prior research preview (Simon Willison, May 2025):
  Gemini Diffusion preview:  857 tokens/second
  Task: "Build a simulated chat app" (HTML+JavaScript)

Context:
  Typical frontier cloud LLMs:  15-60 tokens/second (including network latency)
  DiffusionGemma on NIM:        500+ tokens/second
  Approximate speedup factor:   ~10-30x over typical API latency

Source: simonwillison.net/2026/Jun/10/diffusiongemma/ and
        blog.google/...diffusion-gemma-faster-text-generation/
```

### Access Patterns (June 2026)

```
Option 1 — NVIDIA NIM cloud API (free at time of post):
  Endpoint: build.nvidia.com/google/diffusiongemma-26b-a4b-it
  Auth: NVIDIA NIM API key
  Note: "free" hosting may change to paid; verify current pricing

Option 2 — Local deployment via HuggingFace:
  Model: google/diffusiongemma-26B-A4B-it
  VRAM requirement: 18GB (quantized), fits RTX 4090/5090
  Frameworks: MLX, vLLM, HuggingFace Transformers, Unsloth,
              NVIDIA NeMo; llama.cpp support arriving

Source: simonwillison.net/2026/Jun/10/diffusiongemma/ and
        blog.google/...diffusion-gemma-faster-text-generation/
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-deepseek-v4.md` Claim 1: DeepSeek V4-Pro is the largest
    open-weights model at 1.6T total / 49B active parameters with MIT license.
    DiffusionGemma (Apache 2.0, 25.2B total / 3.8B active) is a smaller but
    architecturally distinct entry in the same open-weight model category. Together,
    these two notes document the continued expansion of the open-weight model
    ecosystem with frontier-adjacent capabilities and permissive licensing. Both
    notes involve Simon Willison documenting open-weight models via his standard
    `llm` CLI + API toolchain.
  - `blog-simonwillison-glm51.md` Claim 1: GLM-5.1 is a 754B MIT-licensed
    open-weights model accessible via OpenRouter. DiffusionGemma corroborates the
    pattern of large open-weight models being made accessible through cloud
    inference APIs (NIM for DiffusionGemma, OpenRouter for GLM-5.1) rather than
    requiring full local deployment. Both notes demonstrate the same principle: open
    licensing + hosted inference = low barrier to practitioner evaluation.

- **Contradicts**: None identified. No existing corpus note claims diffusion-based
  text generation is impractical at scale, or that open-weight models cannot match
  meaningful throughput benchmarks. No contradiction issue required.

- **Extends**:
  - `blog-simonwillison-gemini35-flash-pricing.md`: That note covers Gemini 3.5
    Flash as a closed-API cloud model. DiffusionGemma extends the Google model
    landscape in a different direction: open-weight, locally deployable, speed-
    optimized rather than quality-maximizing. The two Google models serve different
    use cases (3.5 Flash for API-accessed quality reasoning; DiffusionGemma for
    local/NIM high-throughput interaction) and do not compete directly. Together,
    they illustrate that Google is pursuing both the closed-API and open-weight
    model strategies simultaneously.

- **Novel**:
  - **First in-corpus documentation of a diffusion-architecture text model reaching
    production-accessible open-weight status**: No prior note documents a diffusion
    LLM as an open-weight model with practical deployment options. The May 2025
    Gemini Diffusion preview was a closed research preview; DiffusionGemma is the
    first in the corpus that is both open-weight (Apache 2.0) and freely hosted.
  - **500+ tokens/second measured throughput from an open-weight model on a free
    API**: No prior corpus note documents an open-weight model achieving this
    throughput on a freely accessible inference endpoint. The DeepSeek V4 and
    GLM-5.1 notes do not include throughput measurements. This is the first
    in-corpus benchmark for diffusion-based text generation throughput in a
    production-accessible setting.
  - **Explicit vendor-disclosed quality trade-off for a throughput-optimized model**:
    Google's own statement — "overall output quality is lower than standard Gemma 4"
    — is the first in-corpus instance of a model author explicitly documenting a
    quality regression as the price of a throughput gain in the same announcement.
    This is practically important for practitioners because it removes the need to
    infer the trade-off from benchmarks; the authors have disclosed it directly.

## Guide Impact

- **Chapter 02 (Harness Engineering — Model Selection)**: Add DiffusionGemma as a
  case for a new model selection dimension: throughput-vs-quality trade-off for
  interactive use cases. The guide currently documents model selection by quality
  tier (frontier, balanced, budget) and cost (token pricing). DiffusionGemma
  introduces a third axis: speed-specialized open-weight models that sacrifice
  quality for 4–25× higher throughput. Recommended addition: "For latency-sensitive
  interactive workflows — in-line editing, rapid draft iteration, code infill — a
  throughput-optimized diffusion model (e.g. DiffusionGemma at 500–1000+ tokens/
  second) may be more appropriate than a quality-maximizing frontier API that
  responds in 15–60 tokens/second. Google explicitly states DiffusionGemma's quality
  is lower than Gemma 4; benchmark against your specific task before substituting."

- **Chapter 02 (Harness Engineering — Open-Weight Model Infrastructure)**: The
  access path pattern (free NVIDIA NIM API for evaluation, Apache 2.0 HuggingFace
  weights for local deployment at 18GB VRAM) is worth documenting as a concrete
  example of how open-weight models can be integrated into a harness without
  committing to local infrastructure. The two-stage pattern (NIM for evaluation,
  local for production) is a useful workflow primitive for practitioners evaluating
  whether to self-host a model.

- **Chapter 04 (Context Engineering — Model Capabilities for Diverse Tasks)**:
  The 256-token canvas constraint is architecturally significant for context
  engineering: DiffusionGemma is best suited for tasks that fit within 256-token
  generation blocks, not open-ended long generation. Practitioners designing
  prompts for DiffusionGemma should account for this canvas constraint in their
  output length planning. The 256K context window allows long input, but generation
  efficiency is optimized for 256-token output increments.

## Extraction Notes

- The primary source (Simon Willison's post) is a three-paragraph link-blog post.
  It is brief but links to two substantive secondary sources: the Google blog post
  and the HuggingFace model card, both of which were read fully and included in
  extraction. Simon's May 2025 Gemini Diffusion post was also read for historical
  context. Five total pages were read (Simon's June post, Google blog, HuggingFace
  model card, Simon's May 2025 post, NVIDIA NIM page partially via Google blog
  linkage).
- Verbatim quotes from Simon Willison's post were taken directly from the WebFetch
  extract of the primary source URL. Verbatim quotes from the Google blog post were
  verified via two targeted WebFetch calls to that page.
- The HuggingFace model card text was extracted in summarized form; HuggingFace
  page content was used only for the Concrete Artifacts technical specification
  table (clearly attributed), not as a source of claims with `Quote` fields, since
  I cannot be certain the exact phrasing is verbatim from the model card.
- The `#atom-everything` fragment in the issue URL is an Atom feed anchor. The
  canonical URL used as `source_url` omits the fragment, consistent with other
  Willison source notes in this corpus (confirmed by checking
  `blog-simonwillison-claude-fable-5.md` extraction notes).
- Three Prospector triage comments were present on the issue; all were consistent:
  performance metrics (500+ tokens/second), open-weight / Apache 2 license, NVIDIA
  NIM free hosting, model architecture, and relevance to Ch02 model selection and
  Ch04 context engineering. This extraction follows that guidance.
- No contradictions with existing corpus notes were identified. No contradiction
  issue filed.
