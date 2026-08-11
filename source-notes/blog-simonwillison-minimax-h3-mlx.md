---
source_url: https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/
source_type: blog-post
title: "PipeNetwork/minimax-h3-mlx"
author: Simon Willison
date_published: 2026-08-04
date_extracted: 2026-08-11
last_checked: 2026-08-11
status: current
confidence_overall: emerging
issue: "#2618"
---

# PipeNetwork/minimax-h3-mlx

> Willison's ~120-word link-blog post — a single anecdotal test of MiniMax's
> new omni-modal video+audio generative model (MiniMax-H3) via a third-party
> MLX port on his M5 Max MacBook Pro — is the entry point to two much more
> substantive sources followed for this note: MiniMax's own Hugging Face
> model card (architecture, the three-module pipeline, official deployment
> requirements) and the MLX port's own README (an unusually rigorous
> engineering writeup with measured memory/compute benchmarks, a
> teacher-forcing quantization methodology, and an explicit finding that
> generation speed is compute-bound, not memory-bound). Together they turn
> Willison's one-line "it worked, the audio was garbled" anecdote into a
> detailed, checkable data point on what it actually costs — in download
> size, resident memory, wall-clock time, and prompt-engineering effort — to
> run a frontier multimodal generative model locally.

## Source Context

- **Type**: blog-post (Willison's link-blog format, ~120 words of original
  commentary plus a terminal transcript and an embedded video; auto-discovered
  via trusted feed `simon-willison`). Per MINER.md §1, this note follows three
  substantive linked pages beyond the trigger post: MiniMax's own Hugging Face
  model card (`huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/README.md`,
  fetched as raw markdown), the model's official video-prompting guide
  (`.../docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md`, fetched as raw markdown),
  and the MLX port's own GitHub README
  (`raw.githubusercontent.com/PipeNetwork/minimax-h3-mlx/main/README.md`) —
  four pages total, within MINER.md's up-to-5-page budget.
- **Author credibility**: Simon Willison is a designated `trusted-feed` source
  in this repo (creator of Django, Datasette, `sqlite-utils`, `llm`). For this
  post he is a first-hand tester reporting one real run on his own hardware,
  not an independent benchmarker — the substance beyond his own anecdote comes
  from MiniMax's own vendor documentation (self-reported architecture and
  specs) and from the MLX port's maintainer(s) (PipeNetwork, a GitHub
  organization with no further biographical detail given in either repo — the
  port's README is unusually rigorous for an unverified third party, with
  measured benchmarks, numerical-parity tests against the official `diffusers`
  reference implementation, and an explicit teacher-forcing quantization
  methodology, but none of it is independently reproduced by Willison or by
  this Miner).
- **Scope**: Covers one first-hand local-inference test of MiniMax-H3 (a
  brand-new, 2-days-old-at-post-time omni-modal video+audio generative model)
  via a community MLX port, on one machine (M5 Max MacBook Pro), for one
  prompt. Via the linked pages, also covers: MiniMax's official architecture,
  official deployment recommendations (SGLang/vLLM/diffusers/ComfyUI, not
  MLX), the model's structured prompting requirements, and the MLX port's own
  detailed memory/compute engineering (AdaLN precompute, quantization
  benchmarks measured on a different machine — an M3 Ultra with 550GB unified
  memory — from the one Willison used). Does NOT cover: independent
  third-party benchmarking of the MLX port's own performance numbers, video
  *quality* evaluation beyond the two authors' own subjective descriptions,
  non-Apple-Silicon deployment, or the hosted H3-Context-IR/H3-Regenerate-2K
  API paths (both closed-source, not run locally by either author).

## Extracted Claims

### Claim 1: Willison ran MiniMax-H3 locally on an M5 Max MacBook Pro via a third-party MLX port, downloading ~115GB of model files and generating a video in just under 45 minutes
- **Evidence**: Willison's own first-hand terminal commands and timing report.
- **Confidence**: anecdotal (single practitioner, single machine, single run)
- **Quote**: "I got it running on my M5 Max MacBook Pro. I cloned the repo and ran the model like this:" ... "It downloaded ~115 GB of model files, and the video generation took just under 45 minutes."
- **Our assessment**: This is a concrete, reproducible-in-principle data point for "can a frontier multimodal generative model run on a single high-end consumer Mac" — yes, but at real cost (115GB download, 45 minutes for one clip). Cross-referencing against the MLX port's own benchmarks (Claim 10, below — 8.8 min/step on a different, larger machine), the 45-minute figure is plausible rather than surprising: it is consistent with roughly 5 denoising steps at that per-step cost, though Willison's post does not state the step count or clip duration he used, so this is corroboration, not confirmation.

### Claim 2: The generated video's audio was "weird speech-like garbage" because Willison did not supply audio prompt guidance, and MiniMax's prompting guide (which he had not read) documents how to do this correctly
- **Evidence**: Willison's own first-hand assessment of his output, with an explicit self-diagnosed cause.
- **Confidence**: anecdotal (single test, self-diagnosed cause, not independently verified against a version of the same prompt written with proper audio guidance)
- **Quote**: "The video is impressive, but the audio is weird speech-like garbage, because I didn't provide any prompt guidance as to what the audio should be. The prompting guide (which I didn't read prior to this experiment) has a whole bunch of information on how to get this to work."
- **Our assessment**: This is corroborated by the prompting guide's own content (Claim 12, below): the guide requires prompts to explicitly separate diegetic dialogue, ambient soundscape, and non-diegetic music into three distinct structured fields, rather than leaving audio content to be inferred by the model. A one-sentence, unstructured prompt like Willison's ("a rainbow colored skunk leaps over a mossy log in a supermarket") supplies none of that structure, which plausibly explains the garbled result — a direct, checkable illustration of "read the vendor's prompting docs before judging model quality," relevant to how the guide frames evaluating new generative models.

### Claim 3: MiniMax describes H3 as "a general-purpose, omni-modal generative system" that understands text, image, video, and audio context and generates video with native stereo audio at up to 2K resolution and 15-second duration
- **Evidence**: MiniMax's own Hugging Face model card, System Overview section.
- **Confidence**: settled (vendor-published model description, directly checkable against the model card)
- **Quote**: "MiniMax H3 is a general-purpose, omni-modal generative system. It supports unified understanding of multimodal contexts composed of text, images, video, and audio, and can generate video with native stereo audio at resolutions up to 2K and durations of up to 15 seconds."
- **Our assessment**: This positions H3 as a genuinely new capability class in this corpus — prior corpus multimodal/local-model sources cover text (LLMs), audio transcription (`blog-simonwillison-mlx-audio.md`), or text-to-video without native synchronized audio; H3 is the first source documenting a single model that jointly generates video and stereo audio from mixed multimodal input. The "up to 2K / 15 seconds" ceiling is a vendor spec, not something either Willison or the MLX port maintainers achieved locally (see Claim 11).

### Claim 4: The complete H3 system is a three-module pipeline — H3-Context-IR (prompt preprocessing), H3-Base (generation), H3-Regenerate-2K (upscaling) — but only H3-Base is open-sourced; the other two modules remain hosted-only
- **Evidence**: MiniMax's own model card, Model Architecture section, stating the reason for withholding each module.
- **Confidence**: settled (vendor-stated release scope, directly checkable)
- **Quote**: "Because H3\-Context\-IR relies on a multi\-stage workflow and multiple hosted models and services, it is not included in this open\-source release\. We provide an API that enables users to reproduce the behavior of the official workflow\." ... "**Due to the complexity of the system, this module is not yet open\-sourced. We will release it once it is ready.**" (H3-Regenerate-2K)
- **Our assessment**: This is a materially important caveat for anyone reading "open-weights omni-modal model" as "fully self-hostable": the open-source release is the middle third of MiniMax's own recommended pipeline. Local/MLX users (Willison, the PipeNetwork port) can only run H3-Base, which — per the model card — outputs at 768p, not the "up to 2K" headline spec; full-quality 2K output requires the closed, hosted H3-Regenerate-2K API. The backslash-escaped hyphens in the quoted text are preserved verbatim from the raw `README.md` file as fetched (see Extraction Notes) — the rendered Hugging Face page strips them for display.

### Claim 5: MiniMax's own recommended local-serving path for H3-Base uses SGLang or vLLM across 4 GPUs, a materially different deployment bar than the single-consumer-Mac community MLX port Willison used
- **Evidence**: MiniMax's model card, Sglang Deployment section, giving an exact CLI invocation.
- **Confidence**: settled (verbatim vendor-provided deployment command)
- **Quote**: `sglang serve --model-path MiniMaxAI/MiniMax-H3 --num-gpus 4 --ulysses-degree 4 --performance-mode speed --host 0.0.0.0 --port 30010 --model-variant fl2va`
- **Our assessment**: MLX/Apple Silicon is not among MiniMax's own recommended deployment frameworks (SGLang, vLLM, `diffusers`, ComfyUI) — the MLX port is entirely a third-party, unofficial effort (confirmed independently by the port's own README, Claim 6). The vendor's own multi-GPU serving recommendation is a useful contrast point against the single-Mac path: MiniMax evidently designed for enterprise GPU serving first, with community ports doing the work to make consumer-hardware inference possible at all.

### Claim 6: The MLX port's own maintainers describe H3 as "not a language model" but a 33B-parameter diffusion transformer denoising video and audio latents jointly, requiring an entirely from-scratch MLX pipeline implementation (no `mlx_lm.convert` path, no autoregressive decoding)
- **Evidence**: The MLX port's own GitHub README, opening architecture description.
- **Confidence**: settled (directly checkable against the port's own source and its parity tests, see Claim 13)
- **Quote**: "H3 is **not** a language model. It is a diffusers pipeline: a 33B diffusion transformer denoising video and audio latents jointly, conditioned by a frozen Qwen3-VL-32B encoder, with separate video and audio VAEs. There is no autoregressive decoding and no `mlx_lm.convert` path — this repository is a from-scratch MLX implementation of the pipeline."
- **Our assessment**: This is a useful architectural distinction for the guide's local-model material, which to date has mostly covered autoregressive LLMs (`blog-fowler-boeckeler-local-models-viability.md`) and one audio-transcription VLM (`blog-simonwillison-mlx-audio.md`). Diffusion-transformer video/audio generation is a structurally different local-inference workload — no KV cache, no token-by-token decoding, and (per Claims 7-9) a completely different memory/compute profile driven by per-step dense attention over a packed multimodal sequence rather than autoregressive generation.

### Claim 7: The MLX port's largest structural memory saving comes from precomputing and dropping 13B of the 33B transformer's parameters (the AdaLN modulation projections), since their output depends only on the fixed timestep schedule and not on the input sequence — reducing resident memory by 25.3GB
- **Evidence**: The port's README, "AdaLN precompute" section, with a measured before/after table.
- **Confidence**: settled (a described, testable engineering technique; the port's README states this cache is "verified bit-exact against the live projection" via its own test suite, though not independently reproduced by the Miner)
- **Quote**: "13B parameters live in the per-block `adaln_proj.linear` projections (50 x `[96768, 2688]`). Their only input is the timestep embedding — nothing sequence-dependent — so for a fixed sampler schedule every modulation tensor a run will ever need can be computed once up front and the projections then dropped." Measured result: "DiT as shipped: 33.12B params / 66.3 GB resident" → "after: 20.11B params / 40.3 GB + 745 MB cache" — "A 25.3 GB net saving."
- **Our assessment**: This is a distinct technique from quantization or MoE expert-routing (the two memory-reduction techniques already documented elsewhere in the corpus, e.g. `blog-fowler-boeckeler-local-models-viability.md`) and from Apple's instruction-following pruning (`blog-thoughtworks-lovin-gall-local-inference-boundary.md` Claim 1, which dynamically swaps 1-4B of 20B parameters per task). AdaLN precompute-and-drop is a *static*, schedule-dependent precomputation specific to diffusion transformers with timestep-conditioned modulation — worth naming as a fourth distinct category of local-inference memory optimization, applicable only to this model class.

### Claim 8: Together with a second structural optimization (loading only 50 of 64 text-encoder layers, since H3 only reads the pre-norm hidden state after layer 50), the two techniques reduce the resident pipeline from 144GB to about 102GB before any quantization is applied
- **Evidence**: The port's README, "Encoder truncation" section, with a measured table.
- **Confidence**: settled (measured, stated by the port's maintainers; not independently reproduced by the Miner)
- **Quote**: "H3 reads the **unnormalized** hidden state after the 50th of Qwen3-VL-32B's 64 decoder layers and feeds it straight to the DiT's `condition_proj`. The language-model head, the final norm and layers 50-63 are never touched, so the port loads only what it reads" ... "Together with the AdaLN precompute, the two structural savings take the resident pipeline from 144 GB to about **102 GB before any quantization**."
- **Our assessment**: Even after both structural optimizations, 102GB resident memory before quantization is still far beyond the 15-25GB "viable" range documented for local coding LLMs in `blog-fowler-boeckeler-local-models-viability.md` Claim 1 — underscoring that omni-modal generative video models are a materially heavier local-inference workload than text-coding models, even after aggressive engineering to strip unnecessary weights.

### Claim 9: Quantization is published at 8-bit (21.5GB resident), 6-bit (16.5GB), and 4-bit (11.5GB), but 3-bit was built and then withheld because it visibly destroys the generated subject — a quality cliff that only showed up by actually generating video, not by any proxy error metric
- **Evidence**: The port's README, "Published quants" section, with a measured PSNR/error table and an explicit description of the 3-bit failure mode.
- **Confidence**: settled (measured quantization-error data reported by the port's maintainers, with a specific, checkable numeric claim; not independently reproduced by the Miner)
- **Quote**: "**3-bit and 2-bit are not published.** 3-bit was built and rendered: at 16.3 dB PSNR the subject is destroyed — no animal, no log, just a textured field. It does not fail by blurring, so a sharpness check would have passed it: per-frame variance *rises* to 54.7 against bfloat16's 37.1 as structure becomes high-frequency noise. Velocity error ranked the widths correctly but could not have located that cliff; only generating found it."
- **Our assessment**: This is a specific, well-documented example of a general lesson relevant to any team quantizing generative models: an aggregate error metric (velocity/latent error) can correctly *rank* quantization widths relative to each other while still failing to predict a hard quality cliff — the failure mode here (rising per-frame variance from high-frequency noise, not blur) would have passed a naive sharpness-based automated check. Worth citing in the guide wherever it discusses automated quality gating for generative-model quantization or compression.

### Claim 10: Generation speed is bound by attention compute, not memory, because MiniMax has not released its sparse-attention implementation — so quantization barely accelerates generation (roughly 1.2-1.4x) even though it substantially shrinks download and resident-memory size
- **Evidence**: The port's README, "Performance" section, stating the mechanism and the measured speedup.
- **Confidence**: settled (measured on the port maintainers' own hardware — an M3 Ultra with 550GB unified memory — with a stated mechanism; not independently reproduced)
- **Quote**: "MiniMax has **not** released its sparse-attention implementation (\"the initial open-source release provides inference with full attention only\"), so a run does dense attention over tens of thousands of rows." ... "Peak memory is modest ... so **memory is not the constraint. Compute is.**" ... "This also changes what quantization buys. The bottleneck is attention FLOPs, which quantization does not reduce. At 5 s the linear layers are ~42% of the work, at 15 s ~20%, so a 4-bit DiT is worth roughly 1.2-1.4x end-to-end — useful for *fitting* the model on a smaller Mac, not for making generation quick."
- **Our assessment**: This directly complicates the common assumption (implicit in most of this corpus's other quantization discussions) that quantization is primarily a *speed* lever. For this specific model class — dense attention over a very long packed multimodal sequence, no released sparse-attention kernel — quantization's main benefit is fitting the model into less memory/download size, not making it faster; speed is capped by attention FLOPs regardless of numeric precision. This is a model-class-specific nuance (transformer diffusion models with long dense-attention sequences), not a general claim about all local-inference quantization.

### Claim 11: A full 15-second, full-resolution (1344x768) generation on the 4-bit build took 426 minutes (7.1 hours) total on an M3 Ultra with 550GB unified memory, and MiniMax's flagship "up to 2K" resolution is explicitly out of reach for local generation
- **Evidence**: The port's README, "Full-resolution 15 s generation" section, with a measured table.
- **Confidence**: settled (a single measured run, reported by the port's maintainers; not independently reproduced)
- **Quote**: "5 s is the shortest clip H3 supports and 15 s at 2K is its flagship capability; 2K is out of reach locally." Measured result: "steps: 8 forwards, 3119 s average, **426 min (7.1 h)** total."
- **Our assessment**: This is the clearest concrete boundary on "how far can you actually push local inference of this model": the *shortest* supported clip (5s) is feasible in under an hour (Claim 1's 45-minute anecdote is consistent with this), but the model's advertised flagship output (15s at 2K) is unreachable locally at all — both because 2K generation depends on the closed H3-Regenerate-2K module (Claim 4) and because even 15s at 768p already costs over 7 hours on a much larger machine than Willison's. This tempers the "I got it running!" framing of Willison's post: what he ran is the cheap end of the model's capability range.

### Claim 12: MiniMax's official prompting guide requires a rigid two-part, three-field structured prompt format — `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music` — that explicitly separates dialogue/diegetic audio from ambient soundscape from background score, rather than leaving audio content to be inferred from a general-purpose text description
- **Evidence**: The official Video Prompt Writing Guide (`docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md`), sections 2.2 and 4.6-4.7.
- **Confidence**: settled (directly quoted vendor documentation)
- **Quote**: "**overall_soundscape**: Summarizes ambient sound, physical action sounds, and non-verbal human sounds across the entire video." ... "**non_diegetic_music**: Describes background music that the characters cannot hear and only the audience can hear." ... "Use 1–3 English sentences to describe background music ... Focus on instrumentation, speed, rhythm, and dynamic changes; do not use abstract mood words".
- **Our assessment**: This is the concrete mechanism behind Claim 2's audio failure: the guide does not describe audio quality as an emergent property of a good visual prompt — it requires audio to be explicitly authored across three separate structured fields. A one-sentence unstructured prompt like Willison's supplies content for none of them, so the model has nothing to draw on for audio and (per Willison's own description) produces "weird speech-like garbage" by default rather than silence or a sensible guess.

### Claim 13: MiniMax's hosted Context-IR preprocessing step expands a single free-form prompt into a much larger structured representation — one published reference example for a 10-second text-to-video clip consumed 8,565 total tokens (5,650 prompt, 2,915 completion) just to produce the structured prompt, before any video generation begins
- **Evidence**: MiniMax's own model card, "Full 2K-Workflow" case-T2VA example, showing the raw API response including token usage.
- **Confidence**: settled (a single published reference example, directly quoted from the vendor's own documentation; not necessarily representative of typical usage)
- **Quote**: `"usage": {"total_tokens": 8565, "prompt_tokens": 5650, "completion_tokens": 2915}` (from the case-T2VA H3-Context-IR reference response); a second published example (case-Ref2VA) shows `"total_tokens": 39299`.
- **Our assessment**: This is a striking, previously undocumented-in-corpus data point on the true prompt-engineering cost of frontier generative video systems: going from a short user intent to a production-quality structured prompt is not free-text elaboration but a multi-thousand-token structured generation step in its own right (and, per Claim 4, this step is entirely closed-source — community MLX users cannot replicate it locally and must either hand-author the structure themselves per the prompting guide, as Willison did not, or pay for the hosted Context-IR API).

### Claim 14: H3's model weights are governed by a non-open "MiniMax H3 Community License" requiring attribution branding, geographic exclusions, and separate authorization for commercial use above $20M in annual revenue, despite the MLX port's own code being Apache-2.0
- **Evidence**: The MLX port's README, License section.
- **Confidence**: settled (directly quoted license summary; not independently verified against the full license text by the Miner)
- **Quote**: "The port is Apache-2.0. The **weights** are governed by the [MiniMax H3 Community License] ..., which is not an open-source licence: redistribution must carry a copy of the agreement, mark modified files, and display \"Powered by MiniMax H3\"; commercial use above $20M yearly revenue needs separate authorization; and the grant is **territorially limited** (worldwide excluding the Excluded Territories). Any republished weights inherit these terms."
- **Our assessment**: This mirrors a pattern already established in this corpus (`blog-simonwillison-tencent-hy3.md`'s Apache-2.0-licensed weights vs. Hy3-preview's more restrictive license) of "open weights" being a spectrum, not a binary. H3's license is closer to the restrictive end: named revenue threshold, mandatory branding, and territorial exclusions are all friction points a team evaluating H3 for anything beyond hobbyist local experimentation would need to clear before commercial use.

## Concrete Artifacts

### Willison's full local-run command sequence (verbatim, simonwillison.net/2026/Aug/4/minimax-h3-mlx/)
```bash
# First download the models
uvx --from huggingface_hub hf download MiniMaxAI/MiniMax-H3 \
  --include 'FL2VA/*' --exclude 'FL2VA/transformer/*'
uvx --from huggingface_hub hf download pipenetwork/MiniMax-H3-MLX-8bit

# Now run the prompt
uv run --with mlx-vlm \
  --with-requirements requirements.txt python scripts/generate.py \
  "a rainbow colored skunk leaps over a mossy log in a supermarket" \
  -o skunk.mp4 \
  -c ~/.cache/huggingface/hub/models--MiniMaxAI--MiniMax-H3/snapshots/fa9c8ab1eaa21c8ae25e7e40b83b2e6002f340af/FL2VA \
  -t ~/.cache/huggingface/hub/models--pipenetwork--MiniMax-H3-MLX-8bit/snapshots/3ac52081470b0488921c3ec3ba84a39097bf2361
```

### AdaLN precompute measured savings (verbatim table, PipeNetwork/minimax-h3-mlx README)
```
| | params | resident |
|---|---:|---:|
| DiT as shipped | 33.12B | 66.3 GB |
| adaln_proj dropped | -13.01B | -26.0 GB |
| after | 20.11B | 40.3 GB + 745 MB cache |

A 25.3 GB net saving, with the cache 35x smaller than the weights it
replaces and built in 0.7 s.
```

### Published quantization builds (verbatim table, PipeNetwork/minimax-h3-mlx README)
```
| build | on disk | resident | PSNR vs bf16 | velocity rel-L2 |
|---|---:|---:|---:|---:|
| f32  | 132.5 GB | 80.5 GB | —         | —      |
| bf16 |  66.3 GB | 40.3 GB | reference | reference |
| 8bit |  35.3 GB | 21.5 GB | 27.6 dB   | 0.0329 |
| 6bit |  30.3 GB | 16.5 GB | —         | 0.0611 |
| 4bit |  25.3 GB | 11.5 GB | 22.0 dB*  | 0.1649 |

* measured at 256x256, far off the trained distribution; at the canvas
H3 was built for, 4-bit output is clean.
```

### Per-denoising-step timing, measured on M3 Ultra / 550GB unified memory, bfloat16 (verbatim table, PipeNetwork/minimax-h3-mlx README)
```
| Request        | Packed rows | Per block | Per denoising step | Peak activations |
|---|---:|---:|---:|---:|
| 5 s, 1344x768   | 37,966  | 10.5 s | 8.8 min | 9.3 GB  |
| 15 s, 1344x768  | 109,318 | 74.9 s | 1.04 h  | 24.4 GB |
```

### H3-Context-IR reference prompt-expansion example (excerpt, MiniMax-H3 README, case-T2VA)
```
"usage": {
  "total_tokens": 8565,
  "prompt_tokens": 5650,
  "completion_tokens": 2915
}

Expanded structured prompt begins:
"integrated_multimodal_description: [Shot 1] Cinematic, medium wide shot,
pushing in slowly. In the cavernous, dimly lit bridge of a starship, sleek
metallic consoles with glowing amber displays flank a massive, curved
observation window. A female captain, in her late 40s with an athletic
build and short silver-streaked black hair, stands in the center
midground..." [truncated; full field runs to ~5,650 prompt tokens]

Source: huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/README.md, case-T2VA
```

### Video prompt structure — worked example (verbatim, VIDEO_PROMPT_WRITING_GUIDE_base_en.md, Case 1: T2VA)
```
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a
medium-wide shot frames a baker opening the shutters of a small street
bakery before sunrise. The camera pushes in with small amplitude at slow
speed as the middle-aged baker with a calm, slightly raspy voice (S1)
places a fresh loaf on the wooden counter and says: <d>[English] First
batch of the morning.</d> [Shot 2] At 00:05.000, the camera cuts to a
close-up of steam rising from the sliced bread while the baker's final
words carry over from the previous shot.

overall_soundscape: Wooden shutters scrape open over a quiet street as
trays clink softly inside the bakery. The doorbell rings once, followed
by light footsteps and the crisp sound of bread being sliced.

non_diegetic_music: A soft acoustic-guitar pattern at a moderate tempo,
joined by sparse upright-bass notes and a gentle fade at the end.
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-mlx-audio.md` Claim 1 ("A single `uv run` invocation
    can perform local audio transcription via Gemma 4 E2B + MLX on macOS with
    no permanent installation") and Claim 4 (the `uv run` + MLX pattern
    generalizes to other multimodal open-weights models): Willison's MiniMax-H3
    command (`uv run --with mlx-vlm ...`, Concrete Artifacts above) is a direct
    instance of the same generalized pattern that note documents — `uv run`
    as a zero-install harness for trying a new local multimodal model,
    applied here to a far larger and more demanding model class (video+audio
    diffusion vs. audio transcription).

- **Contradicts**: None identified. No existing corpus source makes claims
  about omni-modal video+audio generation, diffusion-transformer local
  inference, or this model's specific architecture that conflict with this
  source.

- **Extends**:
  - `blog-fowler-boeckeler-local-models-viability.md` Claim 1 (RAM is the core
    constraint on local-model viability; Böckeler's viable range was 15-25GB
    of model weight on 48-64GB Macs): MiniMax-H3's resident-memory footprint —
    102GB *after* two structural optimizations and *before* quantization
    (Claim 8), or 11.5-21.5GB for the DiT alone at 4-8 bit (Claim 9, though
    this excludes the 50GB text encoder and VAEs) — is one to two orders of
    magnitude larger than Böckeler's viable range for local coding LLMs,
    sharpening the point that local-model viability is workload-class-specific:
    omni-modal video generation is a categorically heavier local-inference
    workload than agentic text coding.
  - `blog-thoughtworks-lovin-gall-local-inference-boundary.md` Claim 5
    ("on-device inference offers $0 marginal token costs... but introduces a
    strict physical token budget") and Claim 1 (instruction-following pruning
    as a sparse-activation technique for fitting large models into local
    memory): this source's AdaLN precompute-and-drop technique (Claim 7) is a
    fourth distinct local-inference memory-optimization category, alongside
    quantization, MoE routing, and Apple's IFP — specific to diffusion
    transformers with timestep-conditioned modulation. This source's 45-minute
    to 7.1-hour generation times (Claims 1, 11) are a second, much more
    extreme concrete illustration of the "not actually free" physical cost of
    local inference than that article's 4,096-token context ceiling.
  - `blog-simonwillison-tencent-hy3.md` Claim 6 (Hy3, a 295B/21B-active MoE
    LLM, requires 8 GPUs of H20-3e-class memory to serve; self-hosting is
    infeasible outside well-resourced teams): MiniMax-H3 presents a contrasting
    data point for a different model class — a community MLX port achieves
    single-consumer-Mac inference (Claim 1), at the cost of hours-long
    generation times rather than GPU-cluster requirements. The two sources
    together suggest that *which* resource becomes the local-hosting
    bottleneck (memory for large MoE LLMs; compute/wall-clock time for dense
    diffusion transformers, per Claim 10) depends on model architecture, not
    just parameter count.

- **Novel**:
  - **First omni-modal (synchronized video+audio) generative model in the
    corpus**, and the first diffusion-transformer (non-autoregressive) local
    inference workload documented (Claims 3, 6).
  - **AdaLN precompute-and-drop as a distinct local-inference memory
    optimization technique** (Claim 7), novel to the corpus.
  - **The "quantization saves memory but barely accelerates generation
    because attention is compute-bound" finding** (Claim 10) — a nuance not
    previously documented; complicates the implicit assumption elsewhere in
    the corpus that quantization is primarily a speed lever.
  - **A quantization quality cliff that only appears in generated output, not
    in proxy error metrics** (Claim 9) — a concrete, numeric illustration of
    the general risk of automated quality gating for generative-model
    compression.
  - **Concrete token-cost data for a hosted prompt-expansion/preprocessing
    step** (Claim 13) — the first corpus data point on how many tokens a
    vendor's own prompt-preprocessing pipeline consumes before generation
    begins, distinct from the model's own inference cost.

## Guide Impact

- **Chapter on model selection / landscape**: Add MiniMax-H3 as the corpus's
  first omni-modal (synchronized video+audio) generative model landscape
  entry (Claim 3), noting the important caveat that the open-source release
  covers only the middle third of MiniMax's own three-module pipeline —
  H3-Base — while the prompt-preprocessing (Context-IR) and 2K-upscaling
  (Regenerate-2K) modules remain closed and hosted-only (Claim 4).

- **Chapter on local/edge deployment**: Add this source as a concrete,
  extreme data point on local-inference cost for generative (not just text)
  models: 115GB download, 45 minutes for the shortest supported clip, up to
  7.1 hours for the model's near-flagship 15-second output (Claims 1, 11) —
  and add the AdaLN precompute-and-drop technique (Claim 7) as a fourth named
  category of local-memory optimization alongside quantization, MoE routing,
  and Apple's instruction-following pruning. Also flag Claim 10's
  compute-vs-memory-bound distinction: recommend the guide caution that
  quantization's speed payoff is architecture-dependent, not a universal
  local-inference speedup.

- **Chapter on prompt/context engineering**: Add Claim 12's structured
  three-field prompting requirement (`integrated_multimodal_description`,
  `overall_soundscape`, `non_diegetic_music`) as a concrete illustration that
  frontier generative-video prompting has moved well past natural-language
  description into a semi-formal schema — and pair it with Claim 2's
  practitioner-reported consequence of skipping that schema (garbled audio)
  as a cautionary example for anyone evaluating a new generative model's
  output quality without first reading its prompting documentation. Claim 13's
  token-cost data point (8,565 tokens to preprocess one 10-second-clip prompt)
  is concrete evidence that "just write a good prompt" understates the real
  engineering effort behind production-quality generative-video output.

- **Chapter on licensing/business considerations**: Add Claim 14 (MiniMax H3
  Community License: attribution branding, territorial exclusions, $20M
  revenue threshold for commercial use) alongside the existing Hy3 license
  data point (`blog-simonwillison-tencent-hy3.md`) as a further example that
  "open weights" spans a spectrum of restrictiveness, not a binary open/closed
  choice.

## Extraction Notes

- **The trigger blog post is very thin** (~120 words, similar in scale to
  `blog-simonwillison-mlx-audio.md`), so per MINER.md §1 this note followed
  three substantive linked pages beyond it: MiniMax's own Hugging Face model
  card, the official video-prompting guide, and the MLX port's own GitHub
  README. The last of these — an unusually detailed, benchmark-heavy
  engineering writeup — is the primary source of Claims 6-11 and 14, and is
  the reason this note has substantially more extractable content than the
  trigger post alone would suggest.
- **All quotes were taken from raw markdown fetched directly** (`curl` against
  `simonwillison.net`'s page HTML, `huggingface.co/.../raw/main/...`, and
  `raw.githubusercontent.com/...`), not from an AI-summarizing fetch tool's
  paraphrase, per MINER.md §2a. An initial WebFetch pass on each page was used
  only to decide which pages were substantive enough to follow in full; no
  quote in this note was taken from that summarizing pass.
- **The Hugging Face README's raw markdown contains literal
  backslash-escaped hyphens and periods** in several sections (e.g.
  `H3\-Omni\-Transformer`, `open\-source release\.`) that do not appear on the
  rendered Hugging Face page. This is preserved verbatim in Claims 4 and 7's
  quotes because it is genuinely present in the raw file as fetched via
  `/raw/main/README.md` — flagged here so the Assayer checking against the
  *rendered* page isn't surprised by the discrepancy; checking against the
  raw file URL will match exactly.
- **PipeNetwork (the MLX port's maintainer) is not independently vetted.**
  Its README's measured benchmarks, PSNR numbers, and parity-test results
  (Claims 6-11, 13-14) are the maintainers' own self-reported figures, not
  independently reproduced by Willison or by this Miner. The README's
  internal rigor (explicit teacher-forcing methodology, paired bootstrap
  statistics, numerical parity tests against the official `diffusers`
  reference to sub-1e-6 tolerance) is a point in its favor but does not
  substitute for third-party verification — hence `confidence_overall:
  emerging` rather than `settled` for the note as a whole, despite most
  individual claims being rated `settled` for internal consistency and
  checkability against the source documents themselves.
- **The issue carried three separate, partially conflicting Prospector
  triage comments** with different proposed chapter numbers (Ch01/03/04/05/06
  variously named across the three comments) and different novelty/summary
  framings, rather than one. This note's Guide Impact section uses
  chapter-topic descriptions (model landscape, local/edge deployment,
  prompt engineering, licensing) rather than committing to specific chapter
  numbers, consistent with how this corpus's other notes handle Prospector
  guidance that doesn't map cleanly to a single fixed chapter.
- **The skills repository linked from the model card**
  (`github.com/MiniMax-AI/MiniMax-H3/tree/main/skills`, "Official skills to
  improve prompt writing") was not followed — it is a directory of
  implementation files rather than a documentation page, and the prompting
  guide already fetched (`VIDEO_PROMPT_WRITING_GUIDE_base_en.md`) covers the
  same ground in prose form. This stayed within MINER.md's up-to-5-linked-page
  budget (four pages followed total).
