---
source_url: https://developers.googleblog.com/gemma-4-12b-the-developer-guide/
source_type: blog-post
title: "Gemma 4 12B: The Developer Guide"
author: "André Susano Pinto, Andreas Steiner, Karolis Misiunas, Karsten Roth, Michael Tschannen, and Omar Sanseviero (Google)"
date_published: 2026-06-03
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: emerging
issue: "#1533"
---

# Gemma 4 12B: The Developer Guide

> Google's official developer guide for Gemma 4 12B documents a genuinely new
> architecture — vision and audio fed directly into the LLM backbone with no
> separate encoders — plus concrete harness-relevant integration details: a
> `litert-lm serve` CLI that turns the model into a drop-in local
> OpenAI-compatible API server for existing coding-agent tools (Continue,
> Aider, OpenClaw, Hermes, OpenCode), a vendor-published "gemma-skills"
> agent-skill package, and (from linked companion posts) Apache 2.0 licensing
> and multi-token-prediction drafters claiming a 3x inference speedup with no
> quality loss.

## Source Context

- **Type**: blog-post (official Google Developers Blog, published June 3,
  2026, six named Google/DeepMind authors — a first-party technical developer
  guide, not a marketing recap). Companion pages read for corroborating
  detail: the parallel launch post on blog.google
  ("Introducing Gemma 4 12B: a unified, encoder-free multimodal model," Jun 3,
  2026, by Olivier Lacombe and Gus Martins), the companion Multi-Token
  Prediction (MTP) technical post
  (blog.google/.../multi-token-prediction-gemma-4/), and the `gemma-skills`
  GitHub repository README (github.com/google-gemma/gemma-skills).
- **Author credibility**: First-party vendor engineering team (Google
  DeepMind research engineers/scientists + a developer-relations lead)
  writing the technical developer-facing companion to the product launch.
  Specific architectural details (parameter counts, frame sizes, layer
  counts) read as genuine technical specification rather than promotional
  copy, but performance/quality claims (benchmark parity with the 26B model,
  MTP's "no degradation" claim) are vendor-asserted with no independent
  third-party benchmark in this source.
- **Scope**: Covers Gemma 4 12B's encoder-free multimodal architecture,
  two worked capability demos (an agent-built local image-processing app;
  video+audio understanding of a 5-minute clip), on-device/desktop serving
  (macOS apps, `litert-lm serve` local API server), and a "Getting Started"
  integration checklist (Hugging Face/Kaggle weights, dev docs, toolchain
  support, `gemma-skills`, cloud deployment). Does NOT cover: independent
  third-party benchmark results, pricing, a detailed comparison against
  competing local multimodal models, or long-form quality evaluation of the
  worked examples beyond the vendor's own narration.

## Extracted Claims

### Claim 1: Gemma 4 12B replaces separate vision/audio encoders with a single encoder-free architecture that feeds multimodal data directly into the LLM backbone, reducing multimodal latency

- **Evidence**: Stated as the model's headline architectural claim, then
  elaborated with a comparison to the encoder-based approach used by other
  Gemma 4 sizes.
- **Confidence**: settled (this is a factual architecture description from
  the model's own creators, not a benchmarked performance claim)
- **Quote**: "Bypassing heavy multi-stage vision and audio encoders entirely, multimodal data is fed straight into the LLM backbone, reducing multimodal latency."
- **Our assessment**: This is a genuine architectural departure, not
  incremental tuning — prior Gemma 4 sizes (per this same source) used
  separate frozen vision (150M/550M-parameter) and audio (300M-parameter)
  encoders. Removing them is a structural latency/memory optimization
  distinct from quantization or distillation, and it's the mechanism behind
  every downstream capability claim in this source (16GB VRAM footprint,
  unified fine-tuning, native audio).

### Claim 2: Gemma 4 12B is the first medium-sized Gemma model with native audio input — smaller Gemma 4 sizes (E2B/E4B) had audio, larger sizes did not

- **Evidence**: Direct statement contrasting Gemma 4 12B against the rest of
  the Gemma 4 lineup's audio support.
- **Confidence**: settled (factual product-lineup claim from the vendor)
- **Quote**: "In the Gemma family, audio inputs were restricted to small, lightweight edge architectures (e.g. E4B). Gemma 4 12B is the first medium-sized model capable of natively ingesting audio."
- **Our assessment**: This directly extends `blog-simonwillison-mlx-audio.md`
  (Claim 2), which documents Gemma 4 E2B's audio transcription via a
  conformer-based audio encoder run through `mlx_vlm`. This source's Claim 5
  below states Gemma 4 12B "eliminates the separate audio encoder (skipping
  the 12 conformer layers used in Gemma 4 E2B and E4B)" — so the E2B/E4B
  audio path Willison exercised and the 12B audio path this source describes
  are architecturally different (encoder-based vs. encoder-free), not the
  same mechanism at a different parameter count.

### Claim 3: Gemma 4 12B is small enough to run locally on dedicated GPU laptops with 16GB VRAM or unified memory

- **Evidence**: Stated as a headline capability under "Developer-friendly
  size."
- **Confidence**: emerging (vendor hardware-fit claim; no independent
  third-party VRAM benchmark is given in this source, though it is
  consistent with the parameter-reduction argument in Claim 1)
- **Quote**: "Small enough to run locally on dedicated GPU laptops with 16GB VRAM or unified memory."
- **Our assessment**: This is directly comparable to `blog-simonwillison-diffusiongemma.md`
  Claim 5, which documents DiffusionGemma (26B MoE, 3.8B active) fitting
  "within 18GB VRAM limits" when quantized. Gemma 4 12B's 16GB figure is for
  a dense 12B model rather than a quantized MoE, making it a slightly
  different data point on the same "frontier-adjacent capability inside
  consumer-GPU VRAM" trend both notes document.

### Claim 4: Gemma 4 12B's vision embedder is a 35M-parameter single-matmul module (replacing 27 vision-transformer layers) that projects raw 48x48 pixel patches to the LLM hidden dimension, with spatial location attached via a factorized coordinate lookup

- **Evidence**: Technical architecture description under "The Architecture."
- **Confidence**: settled (specific, falsifiable technical specification from
  the model authors)
- **Quote**: "Vision embedder (35M parameters): Replaces the 27 vision transformer layers of the other medium-sized Gemma 4 models. Raw 48x48 pixel patches are projected to the LLM hidden dimension with a single matmul. A factorized coordinate lookup (X and Y matrices) attaches spatial location information directly to the input."
- **Our assessment**: Collapsing a 27-layer vision transformer into a single
  matrix multiplication plus a coordinate lookup is the most concrete
  evidence in the source for how the "encoder-free" claim is actually
  implemented for vision — it is not merely "no separate model," it is a
  specific, minimal linear-projection-plus-position-encoding design.

### Claim 5: Gemma 4 12B's audio path eliminates the separate audio encoder (skipping the 12 conformer layers used in Gemma 4 E2B/E4B), instead slicing raw 16kHz audio into 40ms frames (640 floats each) and projecting them linearly into the LLM input space

- **Evidence**: Technical architecture description under "The Architecture."
- **Confidence**: settled (specific technical specification from the model
  authors)
- **Quote**: "Audio wave projection: Eliminates the separate audio encoder (skipping the 12 conformer layers used in Gemma 4 E2B and E4B). Raw 16 kHz audio signals are sliced into 40ms frames (640 floats each) and projected linearly to the LLM input space."
- **Our assessment**: The 40ms/640-float framing detail is a specific,
  reusable technical fact (16kHz × 0.040s = 640 samples) that confirms the
  audio path really is a linear projection of raw waveform slices, not a
  learned feature extractor — the same "replace a deep encoder with a linear
  projection" pattern as the vision path in Claim 4, applied to a different
  modality.

### Claim 6: Because vision, audio, and text share the same weights in this unified architecture, developers can fine-tune (LoRA or full) across all three modalities in a single pass, rather than having to separately co-tune frozen encoders

- **Evidence**: Stated as a direct consequence of the unified architecture,
  under "The Architecture."
- **Confidence**: emerging (architecturally plausible consequence of Claims
  1/4/5, but no worked fine-tuning example or benchmark is shown in this
  source to confirm tuning quality/stability in practice)
- **Quote**: "Because vision, audio, and text inputs share the exact same weights, you no longer have to co-tune separate frozen encoders."
- **Our assessment**: This is the practical payoff of the encoder-free design
  for practitioners who fine-tune rather than only run inference: a single
  LoRA/full-tune pass can, in principle, update the entire multimodal
  pathway. The source names Hugging Face and Unsloth as the tools for this,
  but does not show a fine-tuning run or its results — the claim should be
  read as an architectural capability, not a demonstrated outcome.

### Claim 7: A worked demo shows Gemma 4 12B served locally via llama.cpp, used inside the OpenCode agent harness with the `gemma-skills` package, building a Gradio image-processing app — with the same model instance both writing the app and powering it

- **Evidence**: First-party worked example under "Example 1," described in
  the article's own narration of what was built and how.
- **Confidence**: anecdotal (single vendor-narrated demo; no independent
  reproduction, no task-success metric beyond the narrative claim that it
  worked)
- **Quote**: "we served it locally using llama.cpp using the gemma-skills to code a Gradio app that helped the user process images. This app was powered by the same Gemma 4 12B model that built it!"
- **Our assessment**: This is the single clearest piece of evidence in the
  source that Gemma 4 12B is being positioned as a coding-agent model, not
  just a multimodal chat model — it names a specific open harness (OpenCode),
  a specific local runtime (llama.cpp), and a specific skill package
  (gemma-skills) working together. As a one-off vendor demo it doesn't
  establish reliability, but it is a concrete, reproducible-in-principle
  recipe (runtime + harness + skill package) rather than an abstract
  capability claim.

### Claim 8: A second worked demo has Gemma 4 12B analyze 5 minutes of video (313 frames at 1 FPS, resized to a visual token budget of 70) plus its audio track, answering a question about video content

- **Evidence**: First-party worked example under "Example 2," with specific
  frame count, sampling rate, and token-budget numbers given for the input.
- **Confidence**: anecdotal (single demo; qualitative answer shown, no
  accuracy metric against ground truth)
- **Quote**: "313 frames (at 1FPS, images resized to visual token budget 70)"
- **Our assessment**: The specific numbers here (1 FPS sampling, 313 frames
  for a 5-minute-13-second-equivalent segment, 70-token-per-frame budget) are
  a concrete, reusable data point for estimating token cost of video
  ingestion with this model: at a 70-visual-token-per-frame budget, 313
  frames is roughly 21,900 visual tokens for 5 minutes of video, before
  accounting for the audio track and text prompt — relevant to context-budget
  planning for practitioners building video-understanding agents on this
  model.

### Claim 9: Gemma 4 12B can be served locally as an OpenAI-compatible API server via the new `litert-lm serve` CLI, with stateless prefix caching that lets existing coding-agent integrations bypass prefill latency on repeated context

- **Evidence**: Feature description under "Drop-in Local API Servers
  (litert-lm serve)," with an accompanying shell snippet (see Concrete
  Artifacts) and named integration targets.
- **Confidence**: settled (a specific, named CLI command is given; this is a
  factual capability description, though "instantly bypass prefill latency"
  is not independently measured in this source)
- **Quote**: "Run Gemma 4 12B as a local, OpenAI-compatible API server using the new litert-lm serve CLI command. Seamlessly connect standard integrations (e.g., Continue, Aider, OpenClaw, Hermes or OpenCode), leveraging stateless prefix caching in memory to match context history and instantly bypass prefill latency."
- **Our assessment**: This is the most directly harness-relevant claim in the
  source: naming five specific coding-agent/integration tools (Continue,
  Aider, OpenClaw, Hermes, OpenCode) that can point at a local Gemma 4 12B
  instance through an OpenAI-compatible endpoint means practitioners can swap
  a cloud model for a local one in an existing agent harness without
  reconfiguring the harness itself — only the API base URL changes. "Prefix
  caching in memory" addressing prefill latency on repeated context is
  directly relevant to any agentic loop that resends a growing conversation
  history on every turn.

### Claim 10: The new native macOS "Google AI Edge Gallery" desktop app runs Gemma 4 12B fully offline on Apple Silicon GPUs and includes a sandboxed Python execution loop to write, run, and plot charts inside the chat interface

- **Evidence**: Feature description under "On-Device & Desktop Serving:
  Powered by LiteRT-LM."
- **Confidence**: settled (specific named product feature)
- **Quote**: "It comes with a secure sandboxed Python execution loop to write, execute, and plot scientific charts inside the chat bubble."
- **Our assessment**: A sandboxed code-execution loop embedded directly in a
  consumer desktop chat app — not a developer CLI or IDE — signals that
  Google is shipping agentic code-execution as a mainstream desktop feature,
  not just a developer-tooling capability. The "secure sandboxed" framing
  matters for the guide's security-threat-model chapter: this is a
  vendor-shipped example of constraining what generated code can do inside a
  consumer application rather than trusting output at face value.

### Claim 11: Google is releasing an official "gemma-skills" repository — a skills library specifically designed for agents building with Gemma models

- **Evidence**: Stated under "Getting Started Today" as a distinct
  developer-ecosystem release alongside the model weights.
- **Confidence**: settled (a real, checkable GitHub repository exists at the
  linked URL; verified directly — see Concrete Artifacts)
- **Quote**: "To support agents to build with the latest Gemma advancements, we are releasing our official Skills Repository. This is a library of skills designed specifically to enable agents to build with Gemma models."
- **Our assessment**: This is a vendor (a model provider, not an agent-harness
  vendor) publishing directly into the emerging agent-skills package-manager
  ecosystem documented elsewhere in the corpus (see Cross-References). The
  repository currently ships exactly one skill (`gemma-dev`, "for building
  application with Gemma or for general knowledge inquiries related to Gemma
  models" — see Concrete Artifacts), installable via two independent
  third-party skill-installer CLIs (Vercel's `skills.sh`, Context7's `ctx7`),
  neither of which is Google's own tooling. This is a small, single-skill
  release, not yet a mature ecosystem — the claim's real significance is
  that a foundation-model vendor is targeting an existing cross-harness
  skill format rather than inventing a Gemma-specific mechanism.

### Claim 12 (from companion launch post, blog.google): Gemma 4 12B is released under an Apache 2.0 license, and the Gemma 4 family has crossed 150 million downloads

- **Evidence**: Stated in the companion launch post ("Introducing Gemma 4
  12B: a unified, encoder-free multimodal model," blog.google, Jun 3, 2026,
  by Olivier Lacombe and Gus Martins) that this developer guide links to and
  is a technical elaboration of.
- **Confidence**: settled (licensing is a factual, checkable claim; download
  count is a vendor-reported aggregate metric for the whole Gemma 4 family,
  not this model specifically)
- **Quote (companion launch post)**: "Open and accessible: Released under an Apache 2.0 license with support across the developer ecosystem." / "Thanks to the developer community, Gemma 4 models have now crossed 150 million downloads."
- **Our assessment**: Apache 2.0 licensing places Gemma 4 12B in the same
  permissive-license tier as DiffusionGemma (`blog-simonwillison-diffusiongemma.md`
  Claim 2 — also Apache 2.0), a change from earlier Gemma releases that used
  Google's own custom Gemma license. The 150-million-download figure is
  family-wide (not 12B-specific) and vendor-reported without a breakdown by
  model size or time window, so it should be read as a scale indicator, not
  a precise adoption metric for this specific release.

### Claim 13 (from companion MTP post, blog.google): Gemma 4 12B ships with a dedicated Multi-Token Prediction (MTP) drafter model that delivers up to a 3x inference speedup via speculative decoding with no degradation in output quality or reasoning

- **Evidence**: Stated in the companion technical post on Multi-Token
  Prediction for the Gemma 4 family, which the developer guide references
  via "we are additionally releasing a dedicated multi-token prediction (MTP)
  model."
- **Confidence**: emerging (vendor-claimed speedup figure with a stated
  mechanism — pairing a heavy target model with a lightweight drafter that
  proposes multiple tokens for parallel verification — but no independent
  third-party benchmark of the "no degradation" claim is available in this
  source)
- **Quote (companion MTP post)**: "these drafters deliver up to a 3x speedup without any degradation in output quality or reasoning logic."
- **Our assessment**: This corroborates `blog-cursor-composer2-technical-report.md`
  Claim 7, which documents Cursor's Kimi K2.5-based Composer 2 using
  "Multi-token prediction layers trained via self-distillation supporting
  speculative decoding at inference" as an inference-latency optimization.
  Two independent model providers (Google for Gemma 4, Cursor/Moonshot for
  Composer 2) shipping MTP-drafter-based speculative decoding as a
  production latency optimization in the same period is evidence this is
  becoming a standard inference-serving technique, not an isolated research
  trick — relevant to any guide discussion of why local/self-hosted model
  latency has been improving independent of raw model quality gains.

## Concrete Artifacts

### `litert-lm serve` — local OpenAI-compatible API server (verbatim from source, "Drop-in Local API Servers" section)

```
litert-lm import --from-huggingface-repo=litert-community/gemma-4-12B-it-litert-lm  gemma-4-12B-it.litertlm gemma4-12b

# Start the OpenAI-compatible server
litert-lm serve
```
*Source: developers.googleblog.com/gemma-4-12b-the-developer-guide/, "On-Device & Desktop Serving" section*

### `gemma-skills` repository README (verbatim, fetched directly from `raw.githubusercontent.com/google-gemma/gemma-skills/main/README.md`)

`````markdown
# gemma-skills

Skills for the Gemma and model/agent interactions

## Skills in this repo

| Skill | Description |
| :--- | :--- |
| [`gemma-dev`](skills/gemma-dev) | Skill for building application with Gemma or for general knowledge inquiries related to Gemma models |

## Installation

You can browse and install skills using either the [Vercel skills CLI](https://skills.sh) or the [Context7 skills CLI](https://context7.com).

### Using [Vercel skills CLI](https://skills.sh)

```sh
# Interactively browse and install skills.
npx skills add google-gemma/gemma-skills --list

# Install a specific skill (e.g., gemma-dev).
npx skills add google-gemma/gemma-skills --skill gemma-dev --global
```

### Using [Context7 skills CLI](https://context7.com)

```sh
# Interactively browse and install skills.
npx ctx7 skills install /google-gemma/gemma-skills

# Install a specific skill (e.g., gemma-dev).
npx ctx7 skills install /google-gemma/gemma-skills gemma-dev
```

## Disclaimer

This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards
Program](https://bughunters.google.com/open-source-security).
`````
*Source: github.com/google-gemma/gemma-skills (README fetched directly, not via the developer-guide blog post)*

### Speculative decoding mechanism (verbatim, from the companion MTP blog post)

```
"The processor spends the majority of its time moving billions of
parameters from VRAM to the compute units just to generate a single
token. This leads to under-utilized compute and high latency, especially
on consumer-grade hardware."

"By pairing a heavy target model (e.g., Gemma 4 31B) with a lightweight
drafter (the MTP model), we can utilize idle compute to 'predict' several
future tokens at once with the drafter in less time than it takes for
the target model to process just one token. The target model then
verifies all of these suggested tokens in parallel."
```
*Source: blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/*

### Model-output demo text (verbatim blockquote, "Example 2" video-understanding demo)

```
Prompt: "what happens when the man takes a selfie?" + the video's audio + 313 frames (1 FPS, visual token budget 70)

Model's answer (rendered as a blockquote in the article):
"When the man takes a 'selfie' or is shown holding a smartphone in front
of his face in these demonstration videos, it is a clever way to visually
represent how the AI models can take existing media—like a personal photo
or a video clip—and 'reimagine' it. In these specific clips, the model is
taking a selfie and using it as a base to generate various scenarios (like
a person in a space station, or walking through a forest).

Essentially, the man is not actually taking a selfie; rather, he is acting
out a visual metaphor for the AI's capability to take one specific input
(a "selfie") and generate a whole world of new content based on it. This
is part of the "Swap" and "Build worlds" demonstrations of the Gemini Omni
model, showing its ability to perform complex, multi-modal reasoning and
creative generation."
```
*Source: developers.googleblog.com/gemma-4-12b-the-developer-guide/, "Example 2: Processing 5 minutes of Video at 1 FPS with audio" section — full text of the blockquote, verbatim, with the blank line marking the original HTML `<br/><br/>` line break (both paragraphs are one contiguous blockquote element, no text omitted). Flagged here because the passage is unusually meta for vendor marketing copy (the model explaining that a demo participant is not literally doing what he appears to do); read in context it is the model's own answer to the video-understanding prompt, not injected commentary, but it is worth the Assayer's attention as an oddity.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-mlx-audio.md` (Claim 2 — Gemma 4 E2B supports audio
    transcription via a conformer-based audio encoder in `mlx_vlm`): This
    source's Claim 2 corroborates that Gemma 4's audio capability is a family
    trait extending across sizes, while Claim 5 here clarifies that the 12B
    implementation is architecturally different (encoder-free) from the
    E2B/E4B conformer-encoder path Willison exercised.
  - `blog-simonwillison-diffusiongemma.md` (Claim 2 — Apache 2.0 license;
    Claim 5 — 18GB-VRAM consumer-GPU fit for a quantized 26B MoE model):
    Claims 3 and 12 here corroborate the same two trends — Google shipping
    Gemma-family models under Apache 2.0, sized to run on consumer-grade GPU
    VRAM (16GB here vs. 18GB quantized for DiffusionGemma).
  - `blog-cursor-composer2-technical-report.md` (Claim 7 — Kimi K2.5/Composer
    2 uses multi-token-prediction layers trained via self-distillation to
    support speculative decoding at inference): Claim 13 here (Gemma 4's MTP
    drafter, "up to a 3x speedup") corroborates that MTP-based speculative
    decoding is being independently adopted by at least two model
    providers (Google, Cursor/Moonshot) in the same period as a production
    latency-reduction technique.
  - `docs-github-copilot-agent-skills-cli.md` (Claim 5 — the Agent Skills
    open specification at agentskills.io lets a single skill file work across
    GitHub Copilot, Claude Code, Cursor, Codex, Gemini CLI, and Antigravity):
    Claim 11 here (the `gemma-skills` repository, installable via two
    third-party skill CLIs rather than a Google-authored one) corroborates
    that model vendors are beginning to publish into this same
    cross-harness skill ecosystem rather than building bespoke Gemma-only
    tooling. That note's Claim 6 (skills are unverified and may contain
    hidden instructions or malicious scripts) is a relevant caution that
    applies equally to `gemma-skills`, even though it is vendor-published:
    provenance from Google reduces but does not eliminate the
    supply-chain risk the skill-installer ecosystem carries generally.

- **Contradicts**: None identified. No existing corpus note makes a claim
  about multimodal encoder architecture, local model VRAM requirements, or
  agent-skill distribution that this source materially opposes.

- **Extends**:
  - `blog-google-io-2026-developer-keynote.md` (Claim 6 — Android Bench, a
    domain-specific LLM leaderboard, added Gemma 4 as an open-weight
    comparison point): That note documents Gemma 4's presence in Google's own
    evaluation tooling without architectural detail. This source provides the
    architecture (Claims 1, 4, 5) and harness-integration detail (Claims 7, 9)
    behind the specific 12B model variant.
  - `blog-google-tunix-gemma-reasoning-hackathon.md` (Gemma-family training
    methodology — converting non-reasoning Gemma-2-2B/Gemma-3-1B checkpoints
    into reasoning models via SFT+GRPO recipes): That note covers post-training
    methodology for small Gemma checkpoints; this source covers a specific,
    larger (12B), differently-architected (encoder-free multimodal) model
    release. Both extend the corpus's Gemma-family coverage without
    overlapping in subject matter — one is training methodology, this one is
    architecture and deployment.

- **Novel**:
  - **Encoder-free multimodal architecture at production scale**: No
    existing corpus source documents a released model that feeds vision and
    audio directly into an LLM backbone with no separate encoder stage at
    all (as opposed to a smaller/distilled encoder). This is a genuinely new
    architectural pattern in the corpus, not an incremental variant of
    encoder-based multimodal models covered elsewhere (e.g., the E2B/E4B
    conformer-encoder audio path in `blog-simonwillison-mlx-audio.md`).
  - **`litert-lm serve` as a named local-model-to-agent-harness bridge**: No
    prior corpus source documents a specific CLI command that turns a local
    open-weight model into an OpenAI-compatible endpoint explicitly targeted
    at named coding-agent integrations (Continue, Aider, OpenClaw, Hermes,
    OpenCode) with prefix-caching latency optimization.
  - **A foundation-model vendor publishing into the third-party agent-skills
    ecosystem**: `gemma-skills` is the first corpus example of a model
    provider (rather than a harness/IDE vendor) shipping a skill package
    through existing third-party skill-installer tooling (Vercel's
    `skills.sh`, Context7's `ctx7`) rather than building Gemma-specific
    tooling.
  - **Concrete video-ingestion token-budget numbers**: The 313-frames /
    1-FPS / 70-visual-tokens-per-frame figures for a 5-minute video segment
    (Claim 8) are the first corpus data point giving a specific per-frame
    visual token cost for video understanding, useful for context-budget
    estimation on video-capable agentic workflows.

## Guide Impact

- **Chapter 02 (Harness Engineering — Local Model Integration)**: Claim 9
  (`litert-lm serve` as a named local API server bridging to Continue, Aider,
  OpenClaw, Hermes, and OpenCode) is the most concrete, actionable claim in
  this source for the guide. The guide currently has no coverage of local
  open-weight models as drop-in replacements inside existing agent-harness
  configurations (a gap confirmed by grepping `guide/*.md` for "gemma",
  "litert", "ollama", "llama.cpp" — no matches). Recommend adding a note that
  local, OpenAI-API-compatible serving layers (of which `litert-lm serve` is
  one instance) let practitioners point an existing coding-agent
  configuration at a local model by changing only the API base URL, with the
  MTP/speculative-decoding drafter pattern (Claim 13, corroborated by
  `blog-cursor-composer2-technical-report.md` Claim 7) as the current
  state-of-the-art latency mitigation for such local serving.
- **Chapter 04 (Context Engineering — Multimodal Token Budgets)**: Claim 8's
  concrete figures (313 frames, 1 FPS, 70 visual tokens/frame for 5 minutes
  of video) give a first, specific data point for estimating visual-token
  cost of video-understanding agent workflows — currently absent from the
  guide's context-budget guidance, which (per corpus review) has not yet
  addressed video-specific token accounting.
- **Chapter 06 (Security/Threat Model — Agent Skill Supply Chain)**: Claim 11
  (`gemma-skills`, installable via third-party CLIs) is a concrete example
  for the guide's skill-supply-chain discussion (paired with
  `docs-github-copilot-agent-skills-cli.md` Claim 6's warning that skills may
  carry hidden instructions or malicious scripts): even a model vendor's own
  official skill package is installed via third-party tooling outside that
  vendor's control, so the "verify before installing" guidance the guide
  gives for skills generally should apply without a vendor-trust exception.

## Extraction Notes

- **Raw HTML fetched directly, not via the WebFetch summarizer**: Initial
  WebFetch calls against the developer-guide URL returned condensed/
  paraphrased summaries rather than verbatim text (confirmed by comparing
  three separate WebFetch calls that gave inconsistent framing of the same
  passages). To get character-for-character text for `Quote` fields, I
  fetched the raw page HTML directly via `curl` and stripped tags in
  Python — every `Quote` field in this note is copied from that raw HTML,
  not from a WebFetch summary. The same direct-fetch approach was used for
  the two companion blog.google posts and the `gemma-skills` GitHub repo.
- **`gemma-skills` README fetched from `raw.githubusercontent.com`, not the
  GitHub web UI**: The GitHub repo page itself is client-side rendered and
  its raw HTML does not contain the README text; the README was instead
  fetched from the raw content URL. Confirmed the file exists and matches
  what the developer guide describes ("a library of skills") before citing
  it as a Concrete Artifact.
- **Sub-pages followed**: developer guide (primary source), the parallel
  launch post (blog.google/.../introducing-gemma-4-12B/), the companion MTP
  post (blog.google/.../multi-token-prediction-gemma-4/), and the
  `gemma-skills` GitHub README — four sub-pages, within MINER.md's "up to 5"
  guidance. Not followed: the linked "A Visual Guide to Gemma 4 12B" (a
  third-party newsletter, out of scope for verifying this vendor source's
  own claims), the Hugging Face/Kaggle model cards (would mainly duplicate
  the architecture specs already extracted verbatim from the primary
  source), and the Google AI Edge Gallery blog deep-dive on `litert-lm
  serve` (linked but not essential to corroborate Claim 9, which is already
  supported by a verbatim CLI snippet from the primary source).
- **A note on an unusual passage**: The "Example 2" blockquote (see
  Concrete Artifacts) reads as unusually meta for vendor copy — the model's
  own answer includes a somewhat defensive-sounding clarification that "the
  man is not actually taking a selfie; rather, he is acting out a visual
  metaphor." I checked the raw HTML structure directly: it is a genuine
  `<blockquote>` element presented as the model's answer to the demo prompt,
  not a hidden/injected element, script comment, or alt-text. I'm flagging it
  in the Concrete Artifacts section rather than treating it as a red flag,
  but the Assayer may want to independently confirm this reads the same way
  on the live page.
- **No contradictions found**: Checked this source's claims against all
  Gemma-family and local-model-hardware notes currently in the corpus
  (`blog-simonwillison-mlx-audio.md`, `blog-simonwillison-diffusiongemma.md`,
  `blog-google-tunix-gemma-reasoning-hackathon.md`,
  `blog-google-io-2026-developer-keynote.md`). No claim in this source
  materially opposes an existing note; no contradiction issue filed.
- **Confidence rationale**: Set to `emerging` rather than `settled` because,
  while the architectural specifics (parameter counts, frame sizes) are
  concrete and falsifiable vendor specifications, the source's performance
  and quality claims (16GB VRAM fit, benchmark parity implied by "advanced
  reasoning," MTP's "no degradation" claim) are all vendor-asserted without
  independent third-party benchmarking in this source or its companion
  posts. Not `anecdotal`, because unlike a single practitioner's one-off
  test, this is the model authors' own first-party technical specification
  of a shipped, generally-available product.
