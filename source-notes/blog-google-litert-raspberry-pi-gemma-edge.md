---
source_url: https://developers.googleblog.com/mastering-edge-ai-on-raspberry-pi-with-litert-and-gemma/
source_type: blog-post
title: "Mastering Edge AI on Raspberry Pi with LiteRT and Gemma"
author: "Lu Wang, Terry Heo (Google); Naushir Patuck (Raspberry Pi Ltd); José María Casanova (Igalia)"
date_published: 2026-08-11
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: emerging
issue: "#2644"
---

# Mastering Edge AI on Raspberry Pi with LiteRT and Gemma

> A first-party Google Developers Blog post co-authored with Raspberry Pi Ltd
> and Igalia engineers, documenting concrete Raspberry Pi 5 performance
> numbers (Gemma 4 E2B: 99 tok/s prefill, 9 tok/s decode, 1432 MB peak
> memory, 4x less memory than llama.cpp), a heterogeneous CPU/GPU
> execution pattern for real-time robotics, and an "Agentic Coding with
> LiteRT" pattern — installing a LiteRT CLI skill into Google Antigravity
> so a coding agent can autonomously convert/quantize/benchmark/run edge
> models — via a live Reachy Mini robot demo with vision, ASR, LLM
> reasoning, and TTS running concurrently and entirely offline.

## Source Context

- **Type**: blog-post (official Google Developers Blog, published August 11,
  2026, four named co-authors: Lu Wang and Terry Heo, Google Software
  Engineers; Naushir Patuck, Software Engineer at Raspberry Pi Ltd; José
  María Casanova, Graphics Software Engineer at Igalia — a genuine
  cross-organization byline, not a solo Google product announcement). One
  page was fetched via raw HTML (`curl`) rather than the WebFetch
  summarizer to get character-for-character quotes; three data tables
  embedded in the post as images (not HTML `<table>` markup) were
  downloaded and read directly to extract their numeric content, since
  they are invisible to text-only scraping.
- **Author credibility**: First-party vendor technical post with a named,
  cross-organizational author list spanning the model/runtime vendor
  (Google), the hardware vendor (Raspberry Pi Ltd), and a graphics-driver
  contributor (Igalia, credited for GPU/Vulkan work) — this is closer to
  the corpus's existing Gemma developer-guide posts (six named
  Google/DeepMind authors) than to thinner single-author marketing recaps
  already in the corpus (e.g. `blog-google-tensor-pixel-on-device-ai.md`).
  Benchmark numbers are vendor-disclosed with an explicit test-methodology
  footnote (hardware variant, benchmark tool, token counts, thread count),
  which is more disclosure than several other Google on-device posts
  already in the corpus provide.
- **Scope**: Covers five edge-tuned Gemma model sizes, CPU-only performance
  benchmarks for Gemma 4 E2B (vs. llama.cpp) on Raspberry Pi 5, a
  CPU-vs-GPU hardware capability comparison, a WebGPU/Vulkan GPU-inference
  backend for classical CV/audio models with a four-model latency table,
  a concurrent multi-model robotics pipeline (Reachy Mini), an "Agentic
  Coding with LiteRT" pattern for wiring the LiteRT CLI into coding agents
  (named example: Google Antigravity), a LiteRT-CLI-vs-Ollama binary
  footprint comparison, and a three-command getting-started path. Does
  **not** cover: GPU-accelerated *LLM* inference numbers for Gemma 4 E2B
  on the Pi (only CPU numbers are given for the LLM; the GPU section
  covers only classical CV/audio models), independent third-party
  reproduction of any benchmark, pricing, non-Raspberry-Pi ARM boards, or
  the internals of the "LiteRT CLI skill" file itself (linked as a GitHub
  sample, not reproduced in the post).

## Extracted Claims

### Claim 1: Edge AI on a Raspberry Pi enables fully offline, low-latency, private autonomous systems with zero cloud dependency
- **Evidence**: Opening framing statement of the post.
- **Confidence**: settled (a factual architecture description of what the
  rest of the post demonstrates — offline operation is directly verified
  by the concurrent Reachy Mini demo, Claim 8 below — not merely asserted)
- **Quote**: "Edge AI unlocks this exact autonomy. It enables developers to build highly secure and self-contained systems like intelligent robotics and local AI agents with zero cloud dependencies, ultra-low latency, and total data privacy."
- **Our assessment**: This is the post's thesis statement, substantiated
  concretely later by the Reachy Mini pipeline (Claim 8) rather than left
  as abstract framing — a meaningful difference from thinner Google
  on-device recap posts already in the corpus (e.g.
  `blog-google-tensor-pixel-on-device-ai.md`, whose "next generation of
  on-device AI" framing is never backed by a worked pipeline example).

### Claim 2: The Gemma family offers five edge-tuned sizes for different hardware/latency constraints — Gemma 3 270M, EmbeddingGemma 300M, Gemma 3 1B, Gemma 4 E2B, and Gemma 4 E4B
- **Evidence**: A structured list of five named models with per-model
  use-case descriptions.
- **Confidence**: settled (specific, named, publicly-released model
  identifiers, not a forward-looking roadmap)
- **Quote**: "Gemma 4 E2B: Tailored specifically for mobile and tight edge environments, it features memory-mapped per-layer embeddings, and is ideal for continuous monitoring, fast text/image/audio inference, and edge-based speech processing where saving RAM is absolutely critical." / "Gemma 4 E4B: The sweet spot for performance and size. This model delivers noticeably stronger reasoning capabilities and frontier-level edge performance while remaining compact."
- **Our assessment**: This is the first corpus source to lay out the full
  edge-oriented Gemma size ladder (270M embedding/task model up through
  E4B) in one place, positioning E2B as the RAM-constrained choice and
  E4B as the higher-reasoning tradeoff — a more granular breakdown than
  the corpus's existing Gemma 4 coverage, which centers on the 12B laptop
  variant (`blog-google-gemma-4-12b-developer-guide.md`,
  `blog-google-gemma-4-12b-laptop-ai-edge.md`) and only mentions E2B/E4B
  in passing as the smaller siblings with the same conformer-based audio
  path.

### Claim 3: On Raspberry Pi 5, LiteRT-LM runs Gemma 4 E2B at 99 tokens/sec prefill and 9 tokens/sec decode with 1432 MB peak memory — roughly 4x prefill throughput and 3x lower memory than llama.cpp running the same model quantization class
- **Evidence**: A benchmark table (image-embedded, not HTML text) comparing
  "LiteRT-LM (QAT)" against "Llama.cpp (Q4_0)" for Gemma 4 E2B, with a
  disclosed methodology footnote.
- **Confidence**: settled (a specific, disclosed benchmark with named
  competing framework, hardware variant, and test parameters — the
  strongest-evidenced claim in the post)
- **Quote**: (no direct quote; the comparison is presented in a table image, not prose — see Concrete Artifacts for the verbatim table transcription)
- **Our assessment**: This is a genuine head-to-head benchmark against a
  named competing runtime (llama.cpp), not just a solo performance number
  — a step up in rigor from the corpus's other LiteRT-LM benchmark claims,
  which mostly cite absolute figures with no named comparison framework
  (compare `blog-google-gemma-4-12b-laptop-ai-edge.md`, which gives no
  throughput numbers at all). The methodology footnote (1024 prefill / 256
  decode tokens, 4 CPU threads, specific quantization tags for each tool)
  makes the comparison independently reproducible in principle, though
  this note did not independently re-run it.

### Claim 4: Gemma 4 E2B's tokenizer efficiency (~4.2 characters/token) lets LiteRT-LM's 9 tokens/sec decode translate to ~27.3 characters/sec end-to-end generation, or ~300 words per minute — roughly twice the rate of normal human speech (~150 wpm)
- **Evidence**: A derived-throughput claim connecting the raw
  tokens/sec figure (Claim 3) to a human-comparable speech rate, measured
  in the Reachy Mini voice demo context.
- **Confidence**: emerging (the underlying token throughput is
  vendor-disclosed and benchmarked, but the "twice the speed of normal
  human speech" comparison point — 150 wpm — is asserted without its own
  citation)
- **Quote**: "Thanks to Gemma 4 E2B's highly efficient tokenizer, which packs more text into fewer tokens (averaging ~4.2 characters per token), LiteRT-LM achieves an impressive end-to-end generation speed of ~27.3 characters per sec, roughly 300 words per minute (wpm), in the Reachy Mini voice demo. This throughput makes Gemma 4 E2B excellent for real-time speech and translation tasks, delivering text at twice the speed of normal human speech (~150 wpm)."
- **Our assessment**: This is the clearest practitioner-relevant takeaway
  from the raw benchmark numbers — it translates an abstract tokens/sec
  figure into a concrete claim ("fast enough for real-time voice
  interaction") that is directly falsifiable by anyone reproducing the
  Reachy Mini demo, rather than left as a raw throughput number requiring
  outside context to interpret.

### Claim 5: The Raspberry Pi 5's CPU (ARM Cortex-A76) has roughly 2x the raw FP32 compute of its integrated GPU (Broadcom VideoCore VII) — ~153.6 GFLOPS vs. ~76.8 GFLOPS — but GPU offload is still valuable for freeing CPU cycles via heterogeneous parallel execution
- **Evidence**: Direct hardware specification comparison plus an
  architectural recommendation.
- **Confidence**: settled (specific, named hardware components with
  disclosed compute figures — FP32 GFLOPS and INT8 TOPS for both — a
  factual spec comparison, not a benchmark run)
- **Quote**: "On the Raspberry Pi 5, the quad-core ARM Cortex-A76 CPU is a raw computing powerhouse, delivering ~153.6 GFLOPS (FP32) and up to ~2.0 TOPS (INT8). In comparison, the integrated Broadcom VideoCore VII GPU is clocked at 800 MHz and offers a peak of ~76.8 GFLOPS (FP32) and ~0.24 TOPS (INT8)."
- **Our assessment**: The post is honest that the Pi 5's GPU is *weaker*
  than its CPU in raw FLOPS — an unusual admission for a vendor post
  promoting GPU-accelerated inference — which makes the following
  heterogeneous-execution argument (Claim 6) about *concurrency*, not raw
  GPU speed, a more credible framing than a simple "GPU is faster"
  pitch would be.

### Claim 6: Heterogeneous CPU/GPU parallel execution — offloading continuous vision/audio models to the GPU — is "critical for real-time edge applications" because it frees CPU cycles for LLM inference and system orchestration rather than raw speed
- **Evidence**: Direct architectural claim following the hardware
  comparison in Claim 5, substantiated by the Reachy Mini pipeline design
  (Claim 8) which implements exactly this split.
- **Confidence**: emerging (a design recommendation backed by one worked
  example — the Reachy Mini pipeline — rather than independent
  benchmarked comparison of "GPU-offloaded pipeline" vs. "CPU-only
  pipeline" system-level latency)
- **Quote**: "While the CPU possesses a massive capacity advantage, the GPU introduces heterogeneous parallel execution, a paradigm critical for real-time edge applications. Rather than saturating the CPU, developers can delegate tasks across both processors to optimize overall system and thermal efficiency."
- **Our assessment**: This reframes "why use the GPU" away from
  "GPU is faster" (which Claim 5's own numbers contradict for this
  specific board) toward "GPU frees up the CPU for other concurrent
  work" — a resource-scheduling argument specific to constrained edge
  hardware with weak/no discrete GPU, distinct from datacenter or laptop
  GPU-offload framing (e.g. the 16GB-VRAM/unified-memory framing in
  `blog-google-gemma-4-12b-developer-guide.md` Claim 3) where the GPU is
  assumed faster, not just idle capacity.

### Claim 7: LiteRT's WebGPU (Vulkan)-backed GPU inference on Raspberry Pi shows GPU latency 2-3x *higher* (slower) than CPU latency across four tested classical CV/audio models
- **Evidence**: A four-row latency table (image-embedded) comparing CPU
  vs. GPU latency in milliseconds for MediaPipe Selfie Segmenter,
  Ultralytics YOLO26n, EfficientNet-Lite0, and Moonshine-tiny, with a
  disclosed methodology footnote.
- **Confidence**: settled (a specific, disclosed benchmark table with four
  named models, input sizes, and per-model CPU/GPU latency numbers in
  milliseconds)
- **Quote**: (no direct quote; the comparison is presented in a table image, not prose — see Concrete Artifacts for the verbatim table transcription)
- **Our assessment**: This is a striking, easy-to-miss internal tension in
  the post: every one of the four benchmarked models is *slower* on the
  Pi 5's GPU than on its CPU (e.g. YOLO26n: 101.26ms CPU vs. 375.73ms
  GPU) — directly consistent with Claim 5's raw-FLOPS comparison (CPU
  ~2x GPU), but in apparent tension with Claim 6's "heterogeneous
  execution... critical for real-time edge applications" framing and the
  Reachy Mini pipeline's design choice to run YOLO on GPU specifically
  (Claim 8). The post never states this tension explicitly or reconciles
  single-model latency with system-level throughput; the implicit
  argument is that running YOLO on the (slower per-inference) GPU still
  wins at the *pipeline* level because it leaves the faster CPU free for
  concurrent ASR/LLM/TTS work — but the post's own table would let a
  reader running a single model in isolation reasonably conclude GPU
  offload made that model slower, not faster. Flagging as a claim
  practitioners should verify against their own pipeline's concurrency
  profile rather than assume GPU offload is a per-model latency win.

### Claim 8: The Reachy Mini robot demo runs a four-stage concurrent pipeline entirely on a single Raspberry Pi 5 — GPU-based continuous object detection (Ultralytics YOLO), CPU-based speech recognition (Moonshine), CPU-based reasoning (Gemma 4 E2B), and streaming CPU-based text-to-speech — with no cloud round-trip
- **Evidence**: A four-item architecture breakdown ("Here is how the
  parallel architecture works under the hood"), plus a link to the full
  demo source code on GitHub.
- **Confidence**: settled (a concrete, named, open-sourced architecture
  with linked reproducible code, not an abstract demo description)
- **Quote**: "Object Detection (Ultralytics YOLO on GPU): Camera frames are streamed to the Pi, where a Ultralytics YOLO detection runs continuously on the GPU, avoiding resource contention and frees up the CPU." / "Reasoning & Action (Gemma 4 E2B on CPU): The Gemma 4 E2B model processes the resulting transcript alongside the latest visual metadata to generate low-latency, streaming responses, such as speech replies and physical robotic gestures."
- **Our assessment**: This is the post's strongest concrete artifact — a
  named, four-component, concurrently-running, fully-offline pipeline
  with linked source code (`github.com/google-ai-edge/litert-samples`),
  putting Claim 6's heterogeneous-execution argument into a reproducible
  worked example rather than leaving it abstract. It is also the first
  corpus source documenting a physical robotics platform (not just a
  phone, laptop, or browser) as a Gemma deployment target.

### Claim 9: The LiteRT CLI aggregates the full edge-model development cycle — conversion, quantization, benchmarking, and inference — into a single unified command set, replacing the need to manually manage multiple independent libraries
- **Evidence**: Direct tooling-design claim in the "Agentic Coding with
  LiteRT" section, illustrated with a demo video of the CLI's
  convert/quantize/benchmark/inference flow.
- **Confidence**: settled (describes a concrete, installable CLI tool,
  `pip install litert-cli`, with a runnable getting-started example — see
  Concrete Artifacts)
- **Quote**: "LiteRT provides a comprehensive suite of tools that covers the full development cycle: conversion, quantization, benchmark, and inference. For a fast, frictionless setup, the most straightforward approach is using the LiteRT CLI tool. Rather than requiring developers or coding agents to manually manage multiple independent libraries, the LiteRT CLI aggregates core edge workflows into a single, unified command set."
- **Our assessment**: The phrase "developers **or coding agents**" is the
  key detail — the tool is explicitly designed to be a single,
  low-surface-area interface an *agent* can drive, not just a human CLI
  user, which sets up Claim 10 below.

### Claim 10: Adding the LiteRT CLI skill (and other LiteRT skills) to a coding agent such as Google Antigravity lets the agent autonomously orchestrate and execute complex, multi-stage ML workflows on the developer's behalf
- **Evidence**: Direct claim about agent-skill integration, illustrated
  with a linked worked example (a fully offline voice translator built
  this way, "Gemma Translator") whose implementation is linked on GitHub
  rather than reproduced in the post.
- **Confidence**: emerging (the capability claim — autonomous multi-stage
  ML workflow orchestration by an agent — is stated directly and backed
  by one named linked example, but the post gives no transcript, session
  log, or step-by-step account of the agent actually performing this
  orchestration; the reader must follow the external GitHub repo to
  verify)
- **Quote**: "You can now supercharge your development cycle by adding the LiteRT CLI skill and other advanced LiteRT skills into your AI coding agent, such as Google Antigravity. This empowers agents to autonomously orchestrate and execute complex, multi-stage machine learning workflows on your behalf."
- **Our assessment**: This is the specific claim the Prospector flagged as
  highest-priority for guide relevance (agentic tool orchestration for
  ML workflows). It names Google Antigravity as the example coding agent
  — the same agent runtime documented elsewhere in the corpus
  (`blog-simonwillison-gemini-spark-antigravity.md` Claims 6-7;
  `blog-google-conductor-plugin-antigravity.md`) — extending its known
  use cases from general coding/spec-driven development to ML-specific
  edge-deployment tooling. However, unlike this note's Claim 8 (which has
  a fully reproducible, linked pipeline), this claim's evidentiary weight
  rests on a single external demo repo not itself examined by this
  extraction (see Extraction Notes) — treat as a documented capability
  claim, not an independently verified one.

### Claim 11: LiteRT CLI's modular, on-demand architecture (~46 MB download, ~100 KB pure-Python frontend that installs only needed runtime modules) is roughly 31x smaller than Ollama's monolithic, statically-bundled binary (~1.44 GB)
- **Evidence**: A two-row comparison table (image-embedded) contrasting
  "LiteRT CLI" and "Ollama" on download size and architecture/dependency
  model.
- **Confidence**: settled (a specific, named, quantified comparison
  against a widely-used competing local-inference tool)
- **Quote**: (no direct quote; the comparison is presented in a table image, not prose — see Concrete Artifacts for the verbatim table transcription)
- **Our assessment**: This is the first corpus source to directly,
  numerically compare LiteRT-family tooling against Ollama on install
  footprint — prior corpus mentions of Ollama (e.g.
  `blog-ronacher-local-models-focus-polish.md`) discuss it as one of
  several fragmented local-inference options without a footprint
  comparison to LiteRT. The claim is specifically framed for
  IoT/resource-constrained devices ("For resource-constrained IoT
  devices, minimizing storage and memory overhead is critical"), not as
  a general claim that LiteRT CLI is superior to Ollama for all use
  cases — Ollama's monolithic bundling trades footprint for
  zero-configuration portability across host capabilities, a tradeoff
  this post does not evaluate on its own terms.

### Claim 12: Google plans to bring LiteRT and Gemma model support to Hailo AI accelerators, enabling hardware-accelerated inference on the Raspberry Pi AI HAT+ and AI HAT+ 2 using the same LiteRT workflows already documented
- **Evidence**: A forward-looking roadmap statement in the "What's Next"
  section.
- **Confidence**: anecdotal (an announced future integration with no
  ship date, benchmark, or technical detail on how Hailo NPU offload will
  be exposed through the existing LiteRT CLI/API surface)
- **Quote**: "We are excited to share that LiteRT integration and Gemma models are coming soon to Hailo AI accelerators! This update will allow you to seamlessly offload model inference to the Raspberry Pi AI HAT+ and AI HAT+ 2, delivering massive hardware acceleration benefits through the exact same, familiar LiteRT workflows you use today."
- **Our assessment**: A specific, named, forthcoming hardware target
  (Hailo NPU via the AI HAT+ line) — concrete enough to be checkable
  later, but currently unshipped and unbenchmarked; should not be cited
  in the guide as a present capability.

## Concrete Artifacts

### Gemma 4 E2B performance: LiteRT-LM vs. llama.cpp on Raspberry Pi 5 (verbatim transcription of table image, "Gemma Performance on Raspberry Pi CPU" section)

```
Model: Gemma 4 E2B

Framework (CPU)      | Prefill (tok/sec) | Decode (tok/sec) | Peak Memory (MB)
----------------------|--------------------|--------------------|-------------------
LiteRT-LM (QAT)       | 99                 | 9                  | 1432
Llama.cpp (Q4_0)      | 24                 | 4                  | 4406

* Hardware: Raspberry Pi 5 (8GB RAM variant).
* Benchmark setup: 1024 prefill tokens and 256 decode tokens; CPU runs with 4 threads.
* llama.cpp is benchmarked using llama-bench with gemma-4-E2B-it-Q4_0.gguf.
* LiteRT-LM is benchmarked using litert lm benchmark with gemma-4-E2B-it.litertlm.
```
*Source: developers.googleblog.com/mastering-edge-ai-on-raspberry-pi-with-litert-and-gemma/, table image `Gemma4-perf.original.png`, "Gemma Performance on Raspberry Pi CPU" section*

### CPU vs. GPU latency for classical CV/audio models on Raspberry Pi 5 (verbatim transcription of table image, "Execute on Raspberry Pi GPU with LiteRT" section)

```
Model                     | Task                | Input Size | CPU Latency (ms) | GPU Latency (ms)
---------------------------|----------------------|------------|-------------------|-------------------
MediaPipe Selfie Segmenter | Segmentation         | 256 x 256  | 7.88              | 26.36
Ultralytics YOLO26n        | Object Detection     | 640 x 640  | 101.26            | 375.73
EfficientNet-Lite0         | Image Classification | 224 x 224  | 29.15             | 87.85
Moonshine-tiny              | Speech Recognition   | 5 sec      | 148.67            | 409.03

* Hardware: Raspberry Pi 5 (8GB RAM variant).
* LiteRT CPU runs with 4 threads.
* LiteRT GPU running with WebGPU (Vulkan) on updated Mesa V3DV Vulkan drivers.
```
*Source: developers.googleblog.com/mastering-edge-ai-on-raspberry-pi-with-litert-and-gemma/, table image `classic_model_perf.original.png`, "Execute on Raspberry Pi GPU with LiteRT" section*

### LiteRT CLI vs. Ollama binary footprint (verbatim transcription of table image, "An Ultra-Lean Binary Footprint for IoT Devices" section)

```
Tool       | Download Size | Architecture & Dependency
------------|----------------|----------------------------------------------------------
LiteRT CLI  | ~46 MB         | Modular & On-Demand: A lightweight pure-Python CLI
            |                | frontend (~100 KB) that dynamically installs only the
            |                | specific runtime modules (e.g. inference or conversion)
            |                | optimized for the target hardware.
Ollama      | ~1.44 GB       | Monolithic: A single, pre-compiled binary that
            |                | statically bundles all execution runtimes and heavy
            |                | server-class acceleration drivers, regardless of the
            |                | actual capabilities of the target host.
```
*Source: developers.googleblog.com/mastering-edge-ai-on-raspberry-pi-with-litert-and-gemma/, table image `LiteRT_CLI_vs_Ollama.original.png`, "An Ultra-Lean Binary Footprint for IoT Devices" section (comparison is for LLM inference download footprint on ARM64 Linux)*

### Getting-started CLI commands (verbatim from post, "Running Your First Model" section)

```
# 1. Install LiteRT CLI
pip install litert-cli

# 2. Run the model — provide a Hugging Face auth token
export HUGGING_FACE_HUB_TOKEN=<your_hugging_face_token_here>
litert lm run \
--from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
gemma-4-E2B-it.litertlm \
--attachment=image.jpg \
--prompt="You are Reachy Mini. Identify the main object in front of you, "\
"state its location (Left/Right/Center), and suggest head action in "\
"10 words or less."
```
*Source: developers.googleblog.com/mastering-edge-ai-on-raspberry-pi-with-litert-and-gemma/, "Running Your First Model" section*

### Reachy Mini pipeline architecture (verbatim four-item breakdown)

```
1. Object Detection (Ultralytics YOLO on GPU): Camera frames are streamed
   to the Pi, where a Ultralytics YOLO detection runs continuously on the
   GPU, avoiding resource contention and frees up the CPU.
2. Speech Recognition (Moonshine on CPU): When the user speaks, the ASR
   component transcribes the audio into text directly on the CPU.
3. Reasoning & Action (Gemma 4 E2B on CPU): The Gemma 4 E2B model
   processes the resulting transcript alongside the latest visual
   metadata to generate low-latency, streaming responses, such as speech
   replies and physical robotic gestures.
4. Text-to-Speech (TTS on CPU): The TTS component synthesizes the
   generated text into audio in streaming. The system streams the
   synthesized voice back to the Reachy Mini robot.
```
*Source: same post, "Deep Dive: Reachy Mini Pipeline Powered by LiteRT" section. Full source code linked at github.com/google-ai-edge/litert-samples/tree/main/samples/litert_lm/reachy-voice-robot/*

## Cross-References

- **Corroborates**:
  - `blog-google-gemma-4-12b-developer-guide.md` Claim 2 ("audio inputs
    were restricted to small, lightweight edge architectures (e.g. E4B)")
    and Claim 5 (the 12B model's audio path "skip[s] the 12 conformer
    layers used in Gemma 4 E2B and E4B"): this source's Claim 2 confirms
    Gemma 4 E2B and E4B are real, currently-shipping edge-tier Gemma 4
    sizes with distinct memory/reasoning tradeoffs, consistent with that
    note's framing of E2B/E4B as the smaller siblings of the 12B model.
  - `blog-google-tensor-pixel-on-device-ai.md` Claim 2 (Gemma 4 E2B
    positioned by Google as its edge/mobile-targeted Gemma 4 size,
    running natively on Pixel's Tensor TPU): this source is a second,
    independent Google post confirming Gemma 4 E2B as the vendor's
    chosen edge deployment target, now on a third distinct hardware
    platform (Raspberry Pi CPU, vs. that note's Pixel TPU and
    `blog-simonwillison-mlx-audio.md` Claim 2's Apple Silicon/MLX path).
  - `blog-google-litertjs-web-ai-inference.md` Claim 6 (LiteRT.js "shares
    a unified cross-platform stack with LiteRT" across Android, iOS, and
    desktop) and Claim 10 (LiteRT is Google's umbrella runtime brand with
    separate named bindings per target surface — CLI, browser): this
    source adds Raspberry Pi/embedded Linux as a fourth documented
    target surface in the same one-native-runtime-per-surface strategy,
    via the LiteRT CLI and LiteRT-LM.
  - `blog-google-gemma-4-12b-laptop-ai-edge.md` Claim 6/7 (`litert-lm
    serve` as a local OpenAI-compatible API server) and
    `blog-google-gemma-4-12b-developer-guide.md` Claim 9 (same CLI,
    stateless prefix caching): this source's `litert lm run` command
    (Concrete Artifacts) is the same LiteRT-LM CLI family documented in
    both notes, here shown in its direct-inference (not server) mode
    with a `--from-huggingface-repo` flag consistent with those notes'
    `litert-lm import --from-huggingface-repo` usage.

- **Contradicts**: None identified against other source notes. Internally,
  see Claim 7's "Our assessment" — this post's own classical-model
  latency table (GPU 2-3x *slower* than CPU per-model) sits in tension
  with its own Claim 6 framing that GPU offload is "critical for
  real-time edge applications," without the post reconciling per-model
  latency against pipeline-level throughput. This is flagged as an
  internal tension worth noting in the guide, not filed as a
  cross-source contradiction issue (MINER.md §4a scopes contradiction
  issues to claims that oppose an *existing source note* or oppose each
  other in a way that would change *guide* advice in different
  directions — here, both claims are from the same post, and the
  resolution ["GPU offload wins at the pipeline level despite slower
  per-model latency"] is a plausible, if unstated, reconciliation rather
  than two flatly incompatible recommendations).

- **Extends**:
  - `blog-google-gemma-4-12b-developer-guide.md` and
    `blog-google-gemma-4-12b-laptop-ai-edge.md` (both centered on the
    12B laptop-class Gemma 4 variant, GPU-laptop hardware, and
    coding-agent-server integration): this source extends the corpus's
    Gemma 4 coverage down to the E2B/E4B edge tier, onto embedded
    Linux/Raspberry Pi hardware specifically, with disclosed
    CPU-only benchmark numbers neither laptop-focused note provides.
  - `blog-google-tensor-pixel-on-device-ai.md` (thin, benchmark-free
    Pixel/Tensor TPU recap): this source provides the concrete
    benchmark numbers, disclosed methodology, and reproducible worked
    example (Reachy Mini, with linked GitHub source) that the Tensor/
    Pixel post explicitly lacks — the two sources describe the same
    "Gemma 4 E2B as Google's edge deployment target" strategy from a
    benchmarked-and-reproducible angle (this source) versus an
    unbenchmarked marketing-recap angle (that source).
  - `blog-simonwillison-gemini-spark-antigravity.md` Claims 6-7
    (Antigravity's component stack — desktop app, Go CLI, Python
    SDK — and its role as the runtime inside a major consumer product)
    and `blog-google-conductor-plugin-antigravity.md` (Conductor's
    spec-driven-development plugin extending to Antigravity CLI): this
    source names Google Antigravity as the specific coding agent that
    can run the LiteRT CLI skill (Claim 10), extending the corpus's
    documented Antigravity use cases from general coding/SDD workflows
    to autonomous ML-pipeline orchestration (convert → quantize →
    benchmark → run) for edge-model deployment — a domain-specific skill
    category not previously documented for Antigravity in this corpus.
  - `blog-ronacher-local-models-focus-polish.md` (diagnoses local-model
    tooling fragmentation and praises narrowly-scoped, focused tools
    over general-purpose ones): this source's LiteRT CLI — a single
    pip-installable, ~46MB, modular tool aggregating
    convert/quantize/benchmark/inference — is a concrete example of the
    "focused, narrowly-scoped tool" pattern that note's Claim 9
    recommends, applied specifically to edge/IoT deployment rather than
    Ronacher's general local-chat-app use case.

- **Novel**:
  - **Raspberry Pi (and embedded robotics generally) as a documented
    Gemma/LiteRT deployment target**: no existing corpus source covers
    Raspberry Pi hardware, ARM Cortex-A76/VideoCore VII specs, or a
    physical robotics platform (Reachy Mini) as an LLM/agent deployment
    surface — prior corpus coverage is laptops (macOS/Apple Silicon),
    browsers, and phones (Pixel/Tensor).
  - **Disclosed head-to-head CPU inference benchmark against llama.cpp**
    (Claim 3) and **against Ollama on binary footprint** (Claim 11): no
    existing corpus source runs a named, disclosed-methodology
    comparison of LiteRT-family tooling against either of these two
    widely-used local-inference tools.
  - **The "Agentic Coding with LiteRT" pattern** (Claim 9-10): wiring an
    ML-specific CLI skill (covering the full convert/quantize/benchmark/
    inference cycle) into a general coding agent so the agent can
    autonomously drive edge-model deployment workflows — this specific
    agent-skill-for-ML-tooling pattern, and its named example (Google
    Antigravity + LiteRT CLI skill + Gemma Translator demo), is new to
    the corpus.
  - **Heterogeneous CPU/GPU task-splitting on a single low-power SoC as
    a concurrency (not raw-speed) argument for GPU use** (Claims 5-7):
    the corpus's other GPU-offload discussions (e.g. laptop 16GB-VRAM
    framing) implicitly assume the GPU is the faster path; this source
    is the first to document a case where the GPU is measurably slower
    per-model but still architecturally preferred for freeing up CPU
    concurrency.

## Guide Impact

- **Chapter 02 (Harness Engineering — Local/Edge Model Integration)**:
  The guide currently has no coverage of resource-constrained edge
  hardware (confirmed: no existing chapter file mentions "raspberry",
  "litert", or embedded/IoT deployment). This source's Claim 9-10
  ("Agentic Coding with LiteRT" — a coding agent driven by an ML-specific
  CLI skill covering the full model dev cycle) is a genuinely new pattern
  for the chapter's coverage of tool/skill design: recommend documenting
  the general pattern of packaging a multi-step domain workflow (convert
  → quantize → benchmark → deploy) as a single agent-consumable skill
  rather than requiring the agent to orchestrate several separate CLIs —
  with the explicit caveat (per this note's Claim 10 assessment) that
  the "autonomous orchestration" claim itself is not independently
  verified in the blog post's own text; recommend citing the linked
  Gemma Translator repo directly if the guide wants a reproducible
  example rather than the vendor's narrative claim.
- **Chapter 02 (Harness Engineering — Hardware-Aware Execution)**: Claims
  5-7 (CPU/GPU compute comparison, heterogeneous task-splitting, and the
  internal tension between per-model GPU latency and pipeline-level
  throughput) support a specific, non-obvious guidance point: on
  constrained edge hardware, "should this workload run on the GPU"
  should be evaluated at the *pipeline concurrency* level, not the
  *single-model latency* level — a distinction this post itself
  demonstrates but does not state explicitly (see Claim 7). Recommend
  the guide make this distinction explicit where it exists, since a
  practitioner benchmarking a single model in isolation (as this post's
  own table does) could reasonably reach the opposite conclusion.
- **Chapter 01 (Daily Workflows — Local/Offline Agent Loops)**: Claim 8
  (the Reachy Mini four-stage concurrent pipeline, fully reproducible via
  linked GitHub source) is a concrete, citable example of a real-time,
  fully-offline, multi-model agentic loop (perception → ASR → reasoning
  → TTS) — recommend adding as a worked example of offline agent
  architecture distinct from the corpus's existing cloud/laptop-centric
  workflow examples.

## Extraction Notes

- **Table data was extracted from images, not HTML**: three of this
  post's most load-bearing quantitative claims (Claims 3, 7, 11) are
  presented as image-embedded tables (`Gemma4-perf.original.png`,
  `classic_model_perf.original.png`, `LiteRT_CLI_vs_Ollama.original.png`)
  rather than HTML `<table>` markup — confirmed by inspecting the raw
  page HTML directly (no `<table>` tags present anywhere in the
  document). These images were downloaded via `curl` and read directly
  to transcribe their contents; the transcriptions in Concrete Artifacts
  are manual readings of the rendered images, not OCR or automated
  extraction, and were cross-checked against the post's own surrounding
  prose (e.g. the 99 tok/s / 9 tok/s / 1432 MB figures in Claim 3's
  table match the same figures independently stated in this post's prose
  under "Gemma Performance on Raspberry Pi CPU").
- **Raw HTML fetched directly via `curl`, not via the WebFetch
  summarizer**: an initial WebFetch call against the primary URL returned
  a condensed, paraphrased summary (it collapsed several distinct claims,
  e.g. merging the Gemma 4 E2B/E4B descriptions into generic bullet
  points and omitting the internal CPU-vs-GPU latency tension entirely).
  To get character-for-character text for every `Quote` field, the raw
  page HTML was fetched via `curl` and tags stripped in Python; every
  quote above is copied from that raw-HTML extraction.
- **Sub-pages not followed**: the post links to several external
  destinations — the LiteRT Hugging Face Community, the YOLO guide's
  sample code, the LiteRT and LiteRT-LM GitHub repos, the LiteRT-Samples
  GitHub repo (which does host the Reachy demo's actual source, linked
  directly from the "Deep Dive" section), and the "Gemma Translator"
  GitHub repo referenced in the Agentic Coding section. None of these
  were fetched for this note — they are code repositories rather than
  prose sources, and following them was judged likely to yield
  implementation detail (not new *claims*) beyond MINER.md's "up to 5
  linked pages" guidance being best spent on prose sources. This means
  Claim 10 (the "Gemma Translator" agentic-coding demo) rests entirely on
  the blog post's own narrative description, not on independent
  inspection of that repo's contents — flagged explicitly in that claim's
  "Our assessment" and here for the Assayer.
- **Existing overlap checked before writing**: grepped all
  `source-notes/*.md` for "LiteRT", "Raspberry Pi", "Antigravity",
  "Gemma 4 E2B", "Gemma 4 E4B", "edge AI", and "Reachy" before drafting.
  Found relevant overlap with `blog-google-gemma-4-12b-developer-guide.md`,
  `blog-google-gemma-4-12b-laptop-ai-edge.md`,
  `blog-google-litertjs-web-ai-inference.md`,
  `blog-google-tensor-pixel-on-device-ai.md`,
  `blog-simonwillison-gemini-spark-antigravity.md`, and
  `blog-google-conductor-plugin-antigravity.md` — all handled as
  corroboration or extension above (see Cross-References). No existing
  note covers Raspberry Pi, embedded robotics, or a LiteRT-CLI-vs-Ollama
  footprint comparison; this is confirmed net-new coverage in those
  respects. Also checked `guide/*.md` for "raspberry", "litert", and
  "gemma" — no matches in any of the 8 chapter files, confirming this is
  genuinely new territory for the guide, not an update to existing text.
- **No contradictions filed against other source notes**: the only
  tension found (Claim 7's internal per-model-latency-vs-pipeline-
  throughput tension) is within this single source, not against an
  existing note, and is a plausible-if-unstated reconciliation rather
  than two flatly opposed recommendations — per MINER.md §4a's "when NOT
  to file" guidance (a source disagreeing with itself only rises to a
  filing-worthy contradiction when it recommends materially different
  guide advice; here the more defensible reading is "evaluate GPU offload
  at the pipeline level," which both claims are consistent with once
  reconciled), no contradiction issue was filed. Flagged prominently in
  Claim 7 and the Contradicts section instead so the Assayer and Smith
  can weigh in if they read it differently.
- **Confidence rationale**: Set to `emerging` rather than `settled`
  overall because, while the core hardware and benchmark claims (Claims
  2, 3, 5, 7, 8, 11) are concrete, disclosed, and largely reproducible
  (several with linked source code), the guide-relevant headline claim
  — autonomous agentic ML-workflow orchestration via the LiteRT CLI skill
  (Claim 10) — rests on a single vendor narrative and an unexamined
  external demo repo, and one forward-looking roadmap item (Claim 12,
  Hailo integration) is entirely unshipped. Not `anecdotal` overall,
  because the majority of claims are backed by disclosed benchmark
  methodology and reproducible, linked source code rather than a single
  practitioner's one-off experience.
