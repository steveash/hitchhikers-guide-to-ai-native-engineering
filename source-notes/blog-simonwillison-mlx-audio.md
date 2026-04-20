---
source_url: https://simonwillison.net/2026/Apr/12/mlx-audio/
source_type: blog-post
title: "Gemma 4 audio with MLX"
author: Simon Willison (tip from Rahim Nathwani)
date_published: 2026-04-12
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: anecdotal
issue: "#238"
---

# Gemma 4 audio with MLX

> A brief practitioner tip demonstrating that `uv run` can serve as a zero-install
> harness for local multimodal audio inference on macOS — one command downloads and
> runs Gemma 4 E2B via `mlx_vlm` without a permanent Python environment — with a
> single 14-second transcription test showing functional but imperfect results.

## Source Context

- **Type**: blog-post (short link-blog note / tip, ~150 words, no methodology; Willison
  crediting Rahim Nathwani for the recipe)
- **Author credibility**: Simon Willison is the creator of Django, a widely-read
  open-source engineer, and a consistent practitioner-grade commentator on LLM tooling.
  His posts are accurate first-person observation, not vendor marketing. This specific tip
  originated from Rahim Nathwani (no further background given); Willison ran the command
  himself and reported the test result. The source is observational anecdote, not a
  controlled evaluation.
- **Scope**: Covers one command, one model (Gemma 4 E2B, 10.28 GB), one 14-second WAV
  file test on macOS via MLX. Does NOT cover: transcription quality at scale, comparison
  against dedicated STT tools (Whisper, etc.), Windows/Linux compatibility, GPU vs CPU
  performance, or any practitioner workflow beyond the initial tip. The source is
  intentionally thin — a "here's a command that works" note, not an evaluation.

## Extracted Claims

### Claim 1: A single `uv run` invocation can perform local audio transcription via Gemma 4 E2B + MLX on macOS with no permanent installation

- **Evidence**: Willison ran the exact command below on his own machine and received
  output. The `uv run --with` pattern installs packages ephemerally into a temporary
  virtual environment; no prior Python setup is required beyond `uv` itself.
- **Confidence**: anecdotal (one author, one machine, one test; `uv` behavior is
  settled; the inference result is the anecdotal part)
- **Quote**: (command provided verbatim; Willison reports the model "produced" the
  transcription; minor errors noted by the author)
- **Our assessment**: The signal here is the `uv run` pattern itself, not Gemma 4's
  quality. Using `uv run --with` to pull inference dependencies on demand is a zero-setup
  experimentation workflow that generalizes to any Python-based ML package. A practitioner
  can try a new local model without touching their existing environment — the kind of
  frictionless experimentation that belongs in a daily-workflow section of the guide. The
  model-specific invocation will age; the `uv run` pattern will not.

### Claim 2: Gemma 4 E2B (10.28 GB) supports audio transcription via `mlx_vlm` on Apple Silicon

- **Evidence**: Willison ran the command and received a transcription output. The model
  weight size (10.28 GB) suggests it fits comfortably in Apple Silicon unified memory at
  16 GB+ configurations.
- **Confidence**: anecdotal (single test; no VRAM/RAM specs provided; no benchmark
  against other local models)
- **Quote**: model is "google/gemma-4-e2b-it" with `--audio file.wav`; the command
  accepts an `--audio` flag, confirming multimodal audio input support in `mlx_vlm`
- **Our assessment**: Gemma 4's multimodal audio capability via MLX is a notable model
  landscape update (post-Apr 2026). The practical relevance is narrow: local audio
  inference on macOS without a cloud API. The weight size (10.28 GB) is the key
  constraint — not viable on machines with 8 GB RAM. Worth noting as an available option,
  not a recommendation.

### Claim 3: Transcription quality is functional but imperfect — minor mishearings on a 14-second clip

- **Evidence**: Willison reports the model transcribed "This right here" as "This front
  here" and "how well that works" as "how that works." He notes "I can hear why it
  misinterpreted that" — acoustically plausible errors, not random failures.
- **Confidence**: anecdotal (one 14-second test; no word error rate; no comparison)
- **Quote**: "That was supposed to be 'This right here...' and '... how well that works'
  but I can hear why it misinterpreted that as 'front' and 'how that works'."
- **Our assessment**: The error type (acoustically similar substitutions) is consistent
  with how speech models make mistakes — not hallucinating unrelated content but mishearing
  phonetically close sounds. For practitioners considering local transcription: this is
  enough evidence to say "it works" but not enough to say "it works well enough to
  replace Whisper or cloud STT." A single 14-second clip is not a quality evaluation.
  The author himself stops short of a quality claim.

### Claim 4: The `uv run` + MLX pattern generalizes to other multimodal open-weights models supported by `mlx_vlm`

- **Evidence**: The command structure (`uv run --with mlx_vlm --with torchvision --with
  gradio mlx_vlm.generate --model <HF-model-id> ...`) is model-agnostic — the model is
  specified by a Hugging Face ID flag, not hardcoded into the tooling. Any model
  `mlx_vlm` supports can be swapped in by changing `--model`.
- **Confidence**: emerging (the pattern is structurally model-agnostic; mlx_vlm's
  breadth of model support is not documented in this post; inference from the command
  structure)
- **Quote**: `--model google/gemma-4-e2b-it` (any HF-hosted model ID could substitute)
- **Our assessment**: The `uv run` + HF model ID pattern is the durable artifact from
  this source. As `mlx_vlm` adds support for additional multimodal models, the same
  one-liner pattern applies. For harness-engineering contexts, this illustrates how
  `uv`-based tooling can serve as a lightweight "model dispatch" mechanism — specify the
  model at runtime, not at install time.

## Concrete Artifacts

### Full `uv run` command for local audio transcription

```bash
uv run --python 3.13 --with mlx_vlm --with torchvision --with gradio \
  mlx_vlm.generate \
  --model google/gemma-4-e2b-it \
  --audio file.wav \
  --prompt "Transcribe this audio" \
  --max-tokens 500 \
  --temperature 1.0
```

*Source: Simon Willison (tip from Rahim Nathwani), simonwillison.net/2026/Apr/12/mlx-audio/*

### Transcription test result (14-second WAV file)

```
Model output:
  "This front here is a quick voice memo. I want to try it out with MLX VLM.
   Just going to see if it can be transcribed by Gemma and how that works."

Intended speech (per Willison):
  "This right here is a quick voice memo. I want to try it out with MLX VLM.
   Just going to see if it can be transcribed by Gemma and how well that works."

Errors: "front" for "right", "how that works" for "how well that works"
```

*Source: Willison's own test result, simonwillison.net/2026/Apr/12/mlx-audio/*

## Cross-References

- **Corroborates**:
  - **blog-simonwillison-glm51.md** (Claim 6 — `llm` CLI for zero-friction local model
    experimentation): Both notes document Willison's pattern of reaching for a single CLI
    command to try a new model without a persistent environment. GLM-5.1 uses `llm` + 
    OpenRouter; this note uses `uv run` + `mlx_vlm`. The shared theme is frictionless
    model-switching as a practitioner daily-workflow habit. Together they illustrate two
    complementary zero-setup patterns: cloud-routed (llm + OpenRouter) and local
    (uv + MLX).

- **Contradicts**: None. No existing corpus source makes claims about local audio
  transcription quality or MLX multimodal tooling that conflict with this source.

- **Extends**:
  - **blog-simonwillison-voice-mode-weaker.md** (same author; audio/voice quality theme):
    The voice-mode note documents commercial audio AI quality (ChatGPT voice mode running
    on an older model tier). This note provides the local-model counterpart: open-weights
    audio inference is now accessible on macOS via one command. The two notes together
    give practitioners the full landscape — commercial voice interfaces may be capability-
    stratified, and local alternatives now exist (with their own quality caveats). The
    notes don't contradict; they bracket the problem from different angles.
  - **blog-simonwillison-muse-spark.md** (same author, multimodal tool patterns): The
    Muse Spark note documents `container.visual_grounding` as a commercial multimodal
    primitive. This note shows the local-model parallel for audio. Together they trace
    Willison's consistent interest in multimodal capability across commercial and
    open-weights contexts.

- **Novel**:
  - **`uv run` as a zero-install local inference harness**: No other source in the corpus
    documents the `uv run --with <inference-package>` pattern for running ML inference
    without a persistent environment. The GLM-5.1 note covers the `llm` CLI (a
    purpose-built tool); this introduces `uv` as a general-purpose dependency-free
    execution layer for arbitrary Python inference packages. This is the most durable
    and guide-relevant signal in an otherwise thin source.
  - **Gemma 4 E2B audio transcription via MLX (post-Apr 2026)**: Not covered elsewhere
    in the corpus. A model-landscape currency update: Gemma 4's multimodal audio support
    on Apple Silicon, available April 2026.

## Guide Impact

- **Chapter 01 (Daily Workflows — Local Model Experimentation)**: The `uv run` + MLX
  one-liner is a concrete workflow artifact for the "trying a local model in 60 seconds"
  use case. Currently the corpus covers `llm` + OpenRouter (remote) and various IDE-based
  tooling; this adds the zero-install local inference pattern. Recommend adding a sidebar
  or tool note: "To test a local MLX model on macOS without installing anything: `uv run
  --with mlx_vlm ...`." The command will age; the `uv run` pattern is durable.

- **Chapter 02 (Harness Engineering — Model Selection / Multimodal Capabilities)**:
  Local audio inference via open-weights models is now viable enough to mention as an
  option for practitioners building multimodal workflows who have data-residency or cost
  constraints that preclude cloud STT APIs. The quality caveat (functionally correct,
  acoustically imperfect) should be stated explicitly. This source provides one data
  point; the guide should not over-claim from it.

## Extraction Notes

- **Intentionally thin extraction**: The Prospector's triage explicitly warned against
  over-extracting from this source ("should extract sparingly"). The source is ~150 words,
  one command, one 14-second test. The four claims extracted above reflect the full
  extractable content — no substantive claims were left behind.
- **Fragment URL**: The issue URL includes `#atom-everything` (an Atom feed anchor);
  the canonical page URL without the fragment is used as `source_url`.
- **No sub-pages followed**: The post links to `mlx-vlm` GitHub and Gemma 4 on Hugging
  Face, but these are reference destinations for the recipe, not sources of additional
  engineering insight. The Prospector's assessment that the substance is "essentially one
  command and one data point" is accurate.
- **Attribution layering**: Willison credits Rahim Nathwani for the tip. The command
  recipe originates with Nathwani; the test result and quality observation are Willison's.
  Both are treated as practitioner anecdote.
