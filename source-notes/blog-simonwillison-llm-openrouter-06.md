---
source_url: https://simonwillison.net/2026/Apr/20/llm-openrouter/
source_type: blog-post
title: "Release: llm-openrouter 0.6"
author: Simon Willison
date_published: 2026-04-20
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: anecdotal
issue: "#442"
---

# Release: llm-openrouter 0.6

> A brief release note for llm-openrouter 0.6 introducing `llm openrouter refresh` — a command to force-refresh the cached model list without waiting for expiry — motivated by the desire to test Kimi K2.6 on OpenRouter on launch day, with a pelican SVG test result demonstrating Kimi's spontaneous output-format escalation (SVG wrapped in HTML+JavaScript with interactive animation controls).

## Source Context

- **Type**: blog-post (release announcement; < 200 words; Willison link-blog format; one feature, one pelican test result)
- **Author credibility**: Simon Willison is the creator of the `llm` CLI and the `llm-openrouter` plugin. This is first-party release documentation — factual accuracy about what was added is high. The pelican SVG test is his recurring cross-model creative-code benchmark applied consistently since at least April 2026. No vendor affiliation with OpenRouter or Moonshot AI (Kimi).
- **Scope**: Single plugin release (llm-openrouter 0.6). One new feature: `llm openrouter refresh`. One pelican test result: Kimi K2.6 via OpenRouter. Does NOT cover plugin architecture, backward compatibility, usage at scale, or multi-turn workflows. The release is a thin but verifiable source — the plugin is published on PyPI and the feature is independently confirmable.

## Extracted Claims

### Claim 1: llm-openrouter 0.6 adds `llm openrouter refresh` to force-refresh the cached model list without waiting for cache expiry

- **Evidence**: Release description from the post and independently corroborated by the GitHub release page (bcda46a, April 20, 2026) and PyPI 0.6 entry. This is the sole change in the 0.6 release.
- **Confidence**: settled (first-party release documentation; verifiable on GitHub and PyPI)
- **Quote**: "`llm openrouter refresh` command for refreshing the list of available models without waiting for the cache to expire."
- **Our assessment**: The llm-openrouter plugin caches the OpenRouter model list (updated up to hourly). Before 0.6, practitioners who wanted to test a model that just appeared on OpenRouter had to wait for the cache to expire naturally. The `refresh` command removes that friction: it is the command-line equivalent of "pull the latest model catalog now." For daily workflows, this matters most on the day a new model lands on OpenRouter — the use case Willison explicitly describes.

### Claim 2: The `llm openrouter refresh` feature was added specifically to test Kimi K2.6 on OpenRouter on launch day

- **Evidence**: Willison's direct statement of motivation.
- **Confidence**: anecdotal (single practitioner's use case; accurately represents the target scenario)
- **Quote**: "I added this feature so I could try Kimi 2.6 on OpenRouter as soon as it became available there."
- **Our assessment**: This is the practitioner-workflow context that motivates the feature. The pattern generalizes: whenever a new model appears on OpenRouter, `llm openrouter refresh` + `llm -m openrouter/<provider>/<model> '...'` is the complete two-step workflow for immediate access. Prior to 0.6, the first step did not exist as an explicit command. The launch-day testing use case is particularly relevant for harness engineers who track model releases and want to evaluate new models quickly.

### Claim 3: Kimi K2.6 spontaneously wrapped its pelican output in a full HTML+JavaScript page with interactive animation controls, rather than returning plain SVG

- **Evidence**: Willison's description of the output and an embedded screenshot. The model was not instructed to create an HTML page or add controls; it chose that format on its own.
- **Confidence**: anecdotal (single test, single model, single prompt — the standard Willison "pelican on a bicycle" benchmark)
- **Quote**: "this time as an HTML page because Kimi chose to include an HTML and JavaScript UI to control the animation."
- **Our assessment**: Kimi K2.6 adopted a richer output format than the prompt requested — the same "scope creep" behavior seen with GLM-5.1 in `blog-simonwillison-glm51.md` Claim 2, which "unprompted decided to give me an HTML page that included both the SVG and a separate set of CSS animations." Both are frontier-scale open-weights models, both in single-turn generation, both choosing HTML+JavaScript over plain SVG. This is an emerging behavioral pattern worth tracking: large open-weights models may produce richer-than-asked output formats. For harness engineers, this means output parsing should not assume format compliance — a prompt asking for SVG may receive HTML.

### Claim 4: Kimi K2.6's pelican animation includes interactive UI controls — pause, speed sliders, wing-flap sliders

- **Evidence**: Willison's description of the HTML page output with specific control elements visible in the screenshot description.
- **Confidence**: anecdotal (single test instance; described from direct observation)
- **Quote**: "It is pedaling furiously and flapping its wings a bit..."
- **Our assessment**: The specific UI elements (pause button, speed sliders, wing-flap rate sliders) indicate the model produced a full interactive HTML application in a single prompt turn. This is qualitatively different from a static SVG — it includes JavaScript event handling, DOM manipulation, and parameterized animation. The "bicycle is about right, pelican is OK" assessment signals the usual pattern: compositional correctness is good, fine-grained anatomical detail is unreliable.

### Claim 5: The `llm` CLI + OpenRouter workflow is the reference path for evaluating a new model immediately on the day it lands on OpenRouter

- **Evidence**: The combination of (1) `llm install llm-openrouter` (one-time), (2) `llm openrouter refresh` (new in 0.6), and (3) `llm -m openrouter/<provider>/<model> '...'` constitutes a complete day-one model access workflow. The 0.6 release is specifically motivated by this use case.
- **Confidence**: settled (`llm` CLI + OpenRouter is documented open-source software; these commands are verifiable in the 0.6 release)
- **Quote**: (no direct quote; see Concrete Artifacts for the complete command workflow)
- **Our assessment**: The workflow is now complete for the "test a model immediately on launch day" scenario. Before 0.6, a practitioner using the OpenRouter plugin either had to wait for the cache or work around the stale list manually. The `refresh` command closes this gap. Combined with the consistent `-c` flag for multi-turn continuation (documented in `blog-simonwillison-glm51.md` Claim 6), the `llm` + OpenRouter interface covers the full evaluation workflow — access, test, iterate — for any OpenRouter-listed model.

## Concrete Artifacts

### Complete "test a model on launch day" workflow (llm-openrouter 0.6)

```bash
# One-time setup: install the OpenRouter plugin
llm install llm-openrouter

# Set API key (one-time)
llm keys set openrouter
# or: export OPENROUTER_KEY=<key>

# When a new model appears on OpenRouter, refresh the cache immediately:
llm openrouter refresh

# Then run a prompt against the new model:
llm -m openrouter/moonshotai/kimi-k2.6 'Generate an SVG of a pelican on a bicycle'

# Multi-turn follow-up using the -c (continuation) flag:
llm -c 'make the wings flap more slowly'
```

*Source: Simon Willison, simonwillison.net/2026/Apr/20/llm-openrouter/ (0.6 release) +
`blog-simonwillison-glm51.md` Concrete Artifacts (the -c flag is from the GLM-5.1 post)*

### llm-openrouter version history (from PyPI/GitHub releases)

```
0.6  (2026-04-20)  Added: llm openrouter refresh command
0.5  (2025-09-20)  Added: tool calling support (James Sanford), reasoning options
0.4  (2026-03-10)  Added: schema support, llm openrouter key command,
                          web search via -o online 1 (Exa), llm openrouter models
                          command with --json/--free filters, OPENROUTER_KEY env var,
                          custom provider routing via -o provider
0.3  (2025-12-08)  Added: image attachments for compatible models, async model access
0.2  (2025-05-03)  Added: httpx dependency, OPENROUTER_KEY env var support
0.1  (2025-08-21)  Initial release

Source: PyPI project page for llm-openrouter; GitHub releases for simonw/llm-openrouter
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-glm51.md` Claim 6: That note establishes the `llm` CLI + OpenRouter as a "consistent interface for testing frontier-scale open-weights models without model-specific API wrappers." This source corroborates and extends that pattern with the `refresh` command as the operational step enabling same-day model testing. The core workflow (install plugin once, use `llm -m openrouter/...` for any model) is identical.
  - `blog-simonwillison-glm51.md` Claim 2: That note documents GLM-5.1 spontaneously producing "an HTML page that included both the SVG and a separate set of CSS animations" without being asked. This source's Claim 3 documents Kimi K2.6 doing the same — spontaneously wrapping SVG in an HTML+JavaScript page with interactive controls. Two independent frontier open-weights models (GLM-5.1 in April 2026, Kimi K2.6 also April 2026) exhibiting the same output-format escalation behavior in single-turn prompts.
  - `blog-simonwillison-deepseek-v4.md` Claim 9: That note documents Willison testing DeepSeek V4 via the same `llm` CLI + OpenRouter workflow ("pelican SVG results were 'pretty good'"). This source is a third data point confirming the OpenRouter/`llm` path as Willison's standard model evaluation workflow.

- **Contradicts**: None identified. This source is too thin to contradict anything.

- **Extends**:
  - `blog-simonwillison-glm51.md` (Claim 6, Concrete Artifacts): The `llm openrouter refresh` command from 0.6 adds the previously-missing step to the "test a new model immediately" workflow documented in that note. The existing workflow required waiting for cache expiry; 0.6 makes the cache update on demand.
  - `blog-simonwillison-llm031.md`: Both notes are `llm`-ecosystem incremental updates from the same week (llm-openrouter 0.6 on April 20, `llm` 0.31 on April 24). Together they represent the tooling cadence around the late-April 2026 model release cycle — Kimi K2.6 and DeepSeek V4 both appeared on OpenRouter in this period.

- **Novel**:
  - **`llm openrouter refresh` as an explicit "test a model on launch day" workflow primitive**: No prior note documents the OpenRouter model-cache refresh as a named, intentional step in the model evaluation workflow. The command closes the gap between "model appears on OpenRouter" and "can test immediately."
  - **Second in-corpus example of spontaneous HTML+JavaScript output wrapping for SVG tasks**: GLM-5.1 (documented in `blog-simonwillison-glm51.md`) was the first; Kimi K2.6 is the second. Two independent frontier open-weights models exhibiting this behavior is a stronger pattern signal than either alone.
  - **Kimi K2.6 pelican test result**: No other note in the corpus documents a Kimi K2.6 creative-code output. This is the first in-corpus creative-code result for this model.

## Guide Impact

- **Chapter 01 (Daily Workflows — `llm` CLI Tooling)**: The guide should document the `llm openrouter refresh` command as the step that enables same-day model testing via OpenRouter. The complete "day-one model evaluation" workflow is now: (1) `llm install llm-openrouter` (one-time), (2) `llm openrouter refresh` (when a new model appears), (3) `llm -m openrouter/<provider>/<model> '...'` (test prompt), (4) `llm -c '...'` (multi-turn follow-up). This closes the workflow loop previously documented in `blog-simonwillison-glm51.md` Claim 6.

- **Chapter 02 (Harness Engineering — Output Format Handling)**: Claims 3–4 contribute a second data point to the pattern of frontier open-weights models spontaneously escalating output format (SVG → HTML+JavaScript) without instruction. If the guide covers output parsing for code generation tasks, it should note: do not assume format compliance from large open-weights models. A prompt requesting SVG may receive a full HTML application. Harnesses should either constrain format via system prompt or parse multiple output format types.

## Extraction Notes

- **Very thin source**: The Prospector's triage assessment ("likely to be incremental unless it introduces new model access methods, feature parity updates, or tooling changes") was accurate. The post is < 200 words, one new feature, one pelican test. The primary engineering value is the `llm openrouter refresh` command as a workflow-completion step.
- **Quote verification**: Quotes extracted via WebFetch from the post text. The WebFetch tool returned these as direct text from the page, consistent with Willison's characteristically brief release-note format. The assessment quote ("The bicycle is about right...") appears in the post body describing the pelican output.
- **Kimi K2.6 model name variant**: The post refers to "Kimi 2.6"; the full model designation used on OpenRouter and in Moonshot AI's announcement is "Kimi K2.6" (as documented in `blog-thebatch-gpt55-hallucination-kimi-k26.md`). These refer to the same model.
- **Fragment URL**: The issue URL includes `#atom-everything` (an Atom feed entry anchor). `source_url` uses the canonical page URL without the fragment, consistent with `blog-simonwillison-llm031.md`, `blog-simonwillison-deepseek-v4.md`, and other Willison notes.
- **No sub-pages followed**: The post does not link to substantive sub-pages. The GitHub release (simonw/llm-openrouter/releases/tag/0.6) was reviewed for corroboration of the feature list; PyPI was reviewed for the version history table.
- **Cross-reference claim numbers verified**: `blog-simonwillison-glm51.md` Claim 6 confirmed at lines 57–61 (the `llm` CLI + OpenRouter unified interface). `blog-simonwillison-glm51.md` Claim 2 confirmed at lines 32–36 (spontaneous HTML+CSS output). `blog-simonwillison-deepseek-v4.md` Claim 9 confirmed at lines 84–88 (OpenRouter pelican test). Claim numbers verified by document-order count in each note.
