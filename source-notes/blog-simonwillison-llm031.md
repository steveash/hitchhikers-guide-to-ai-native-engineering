---
source_url: https://simonwillison.net/2026/Apr/24/llm/
source_type: blog-post
title: "llm 0.31"
author: Simon Willison
date_published: 2026-04-24
date_extracted: 2026-05-04
last_checked: 2026-05-04
status: current
confidence_overall: anecdotal
issue: "#528"
---

# llm 0.31

> A four-bullet release announcement for the `llm` CLI, notable primarily for adding native `llm -m gpt-5.5` support — confirming that GPT-5.5 has moved from the Codex-backdoor access path documented in prior notes to an official API route.

## Source Context

- **Type**: blog-post (release announcement format; < 100 words; four bullet points only; no workflow analysis or practitioner commentary)
- **Author credibility**: Simon Willison is the creator of Django and the `llm` CLI itself. As the tool's author, this is first-party release documentation — factual accuracy about what was added is high. The post contains no practitioner analysis; it is a changelog entry, not an experience report.
- **Scope**: Four features in `llm` 0.31: native GPT-5.5 model access, GPT-5+ verbosity control via CLI flag, vision image detail control, and async registration for custom YAML-defined models. Does NOT include workflow guidance, motivating examples, or before/after comparisons.

## Extracted Claims

### Claim 1: GPT-5.5 is now natively accessible via the `llm` CLI as `llm -m gpt-5.5`, without the Codex subscription workaround previously required

- **Evidence**: Release note lists "New GPT-5.5 OpenAI model: `llm -m gpt-5.5`" as a 0.31 feature (GitHub issue #1418). Prior access required installing the `llm-openai-via-codex` plugin to route through a Codex subscription endpoint — documented in `blog-simonwillison-gpt55-codex-plugin.md`. Built-in plugin support in the base `llm` package indicates official API availability.
- **Confidence**: settled (first-party release notes from the tool's author; command is verifiable against the 0.31 release)
- **Quote**: (no direct quote; the feature is listed as a release bullet referencing the command `llm -m gpt-5.5`)
- **Our assessment**: The significance is the transition, not the syntax. `blog-simonwillison-gpt55-codex-plugin.md` Claim 5 explicitly predicted the Codex endpoint was "transient — likely to be superseded once official API access for GPT-5.5 is fully formalized." This release confirms that transition has occurred. Practitioners who adopted `llm-openai-via-codex` can now use the built-in path instead. The official route still requires an OpenAI API key with GPT-5.5 access; it does not remove the subscription requirement, only the workaround plumbing.

### Claim 2: The `llm` CLI adds output verbosity control for GPT-5+ OpenAI models via `-o verbosity low|medium|high`

- **Evidence**: Release note states the flag and its value set. Uses the same `-o option value` interface as other model-specific options in the `llm` CLI (e.g., `-o reasoning_effort` documented in `blog-simonwillison-gpt55-codex-plugin.md` Claim 6).
- **Confidence**: settled (first-party release notes; flag is verifiable in the 0.31 release)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `-o verbosity` flag is a CLI-level alternative to prompt-engineering for output length control. It offloads to the model API what practitioners would otherwise specify via "be concise" or "be thorough" in the prompt. Limitation: GPT-5+ specific, not a universal `llm` CLI parameter. The post does not describe the observable behavioral difference between verbosity levels; practitioners would need to experiment to calibrate expectations. No workflow example is provided.

### Claim 3: The `llm` CLI adds vision input quality control for image attachments to OpenAI models via `-o image_detail low|high|auto|original`

- **Evidence**: Release note lists the flag and value set; `original` is noted as accepted by GPT-5.4 and GPT-5.5 only.
- **Confidence**: settled (first-party release notes)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `-o image_detail` option maps directly to OpenAI's image detail API parameter, which controls whether a vision model receives a resized low-resolution image (lower cost) or full resolution. The `original` value (GPT-5.4/5.5 only) passes the image without preprocessing. Useful for practitioners using the CLI for vision tasks where image fidelity matters, but incremental tooling coverage — this surface was always in the API, the flag just exposes it in the CLI interface. No source post describes when to choose each level.

### Claim 4: Custom models defined in `extra-openai-models.yaml` are now automatically registered as asynchronous in `llm` 0.31

- **Evidence**: Release note bullet (GitHub issue #1395 cited).
- **Confidence**: settled (first-party release notes; verbatim bullet from the post)
- **Quote**: "Models listed in `extra-openai-models.yaml` are now also registered as asynchronous."
- **Our assessment**: Before this change, custom models defined in `extra-openai-models.yaml` (the mechanism for adding OpenAI-compatible custom endpoints) could only be used synchronously. After this change, they support the `llm` Python library's async API (`await llm.get_async_model(...)`). Relevant only to practitioners who have defined custom models via this YAML file and use the async Python API. No visible behavioral change for standard CLI users.

## Concrete Artifacts

### Feature flags added in llm 0.31

```bash
# Native GPT-5.5 access (replaces llm-openai-via-codex plugin workaround)
llm -m gpt-5.5 'Your prompt here'

# Output verbosity control for GPT-5+ models
llm -m gpt-5.5 -o verbosity low 'Your prompt here'
llm -m gpt-5.5 -o verbosity high 'Your prompt here'
# Values: low, medium, high

# Image detail level for vision tasks with OpenAI models
llm -m gpt-5.5 -o image_detail low 'Describe this image' -a image.png
llm -m gpt-5.5 -o image_detail original 'Describe this image' -a image.png
# Values: low, high, auto, original (original: GPT-5.4 and GPT-5.5 only)
```

*Source: Simon Willison, simonwillison.net/2026/Apr/24/llm/, llm 0.31 release notes*
*Note: `-a image.png` is standard `llm` CLI attachment syntax; not from this post directly.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 5: That note documents OpenAI having "officially signaled that third-party integrations with Codex subscription access are welcome" and assessed the Codex endpoint as "transient — likely to be superseded once official API access for GPT-5.5 is fully formalized." The `llm 0.31` native `gpt-5.5` plugin confirms that official API path has materialized as predicted.

- **Contradicts**: None identified.

- **Extends**:
  - `blog-simonwillison-glm51.md` Claim 6 (`llm` CLI as a unified model-testing interface): `llm 0.31` adds GPT-5.5 to the set of models accessible via the standard `llm -m <model>` interface, continuing the pattern of the CLI as a harness-agnostic model-switching layer.
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 6 (the `-o reasoning_effort` option as the CLI primitive for reasoning control): `llm 0.31` adds `-o verbosity` and `-o image_detail` as parallel model-specific options via the same `-o option value` interface, building out the option layer for GPT-5+ model control.

- **Novel**:
  - **`-o verbosity low|medium|high` for GPT-5+ output length control**: No existing corpus note documents a CLI-level verbosity flag as an alternative to prompt-based output length control.
  - **`-o image_detail` for vision input quality control via CLI**: No existing corpus note covers image detail as a practitioner-facing CLI parameter.
  - **Confirmation that GPT-5.5 official API access has materialized**: Prior notes documented the Codex-backdoor access path and predicted its transience. This release is the first in-corpus evidence that the prediction resolved — official `gpt-5.5` API access is now in the base `llm` package.

## Guide Impact

- **Chapter 01 (Daily Workflows — `llm` CLI Tooling)**: If the guide documents the GPT-5.5 access path from `blog-simonwillison-gpt55-codex-plugin.md`, update to reflect that `llm -m gpt-5.5` is now the primary CLI path. The `llm-openai-via-codex` plugin remains relevant only for users accessing GPT-5.5 via ChatGPT/Codex subscription rather than a direct OpenAI API key.
- **Chapter 02 (Harness Engineering — CLI Parameters)**: If the guide covers the `llm` CLI's model-specific option flags (following the `-o reasoning_effort` coverage from `blog-simonwillison-gpt55-codex-plugin.md`), add `-o verbosity low|medium|high` as the output-length control flag for GPT-5+ models.
- **No substantive new patterns**: The Prospector triage (priority:low, novelty:low) was correct. This source is incremental tooling coverage. The guide does not need restructuring.

## Extraction Notes

- **Very thin source**: Four bullet points, no practitioner analysis. The Prospector triage correctly flagged `priority:low`. The most significant signal is the GPT-5.5 official API transition (Claim 1), which closes a prediction from `blog-simonwillison-gpt55-codex-plugin.md`.
- **No sub-pages followed**: The post references GitHub issues #1418 and #1395 for implementation context; these are internal implementation issues, not usage documentation.
- **Fragment URL**: The issue URL includes `#atom-everything` (an Atom feed entry anchor). `source_url` uses the canonical page URL without the fragment, consistent with `blog-simonwillison-deepseek-v4.md` and `blog-simonwillison-gpt55-codex-plugin.md`.
- **Quote confidence**: The WebFetch result returned structured feature bullets. The one bullet used verbatim in Claim 4 appeared in double quotes in the WebFetch output. The CLI command strings (`llm -m gpt-5.5`, `-o verbosity low`, `-o image_detail low`) are unambiguous technical content that would not be paraphrased by a summarizing model.
- **Cross-reference verification**: Confirmed `blog-simonwillison-gpt55-codex-plugin.md` Claim 5 (lines 54–59) matches the cited content (OpenAI's welcome statement for Codex integrations; assessment of endpoint transience). Confirmed `blog-simonwillison-glm51.md` Claim 6 (lines 56–61) matches the cited content (llm CLI + OpenRouter as a unified interface). Claim numbering verified by document-order count in each note.
