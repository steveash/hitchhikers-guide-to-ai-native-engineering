---
source_url: https://simonwillison.net/2026/Apr/7/glm-51/
source_type: blog-post
title: "GLM-5.1: Towards Long-Horizon Tasks"
author: Simon Willison
date_published: 2026-04-07
date_extracted: 2026-04-19
last_checked: 2026-04-19
status: current
confidence_overall: anecdotal
issue: "#167"
---

# GLM-5.1: Towards Long-Horizon Tasks

> A brief link-blog post documenting Simon Willison's "pelican SVG test" of Z.ai's GLM-5.1 — a 754B MIT-licensed open-weights model — demonstrating one-command OpenRouter access via the `llm` CLI, unprompted multi-modal output (SVG + CSS animations), and successful single-turn self-correction of a CSS coordinate-system bug.

## Source Context

- **Type**: blog-post (link-blog style; ~400 words, no methodology, no measurements)
- **Author credibility**: Simon Willison is the creator of Django, a prolific open-source engineer, and one of the most widely-cited commentators on LLM tooling. His "pelican on a bicycle" SVG benchmark is a recurring, informal creative-code test he applies consistently across models, making it a de-facto comparative signal even if not rigorous. He documents his tests publicly and accurately. This post is observational, not analytical; treat claims as high-quality anecdote from a credible practitioner, not controlled evidence.
- **Scope**: Single model (GLM-5.1), single task type (creative SVG generation + animation), single session (two prompts). Does NOT cover code generation benchmarks, multi-turn agentic tasks, reasoning, or any task relevant to software engineering workflows beyond creative code. The Bluesky update adds one more anecdotal sample (opossum SVG). No comparisons against other models in this post.

## Extracted Claims

### Claim 1: GLM-5.1 is a 754B parameter MIT-licensed open-weights model from Z.ai, accessible via OpenRouter in one CLI command
- **Evidence**: Willison states the model size (754B), license (MIT), and weight storage (1.51TB on Hugging Face). He shows the full OpenRouter access pattern with two commands.
- **Confidence**: settled (factual model metadata; commands are verbatim)
- **Quote**: "Chinese AI lab Z.ai's latest model is a giant 754B parameter 1.51TB (on Hugging Face) MIT-licensed monster"
- **Our assessment**: The noteworthy fact here is not the model's capabilities but its availability path. A frontier-scale MIT-licensed model reachable via two CLI commands (`llm install llm-openrouter` + `llm -m openrouter/z-ai/glm-5.1 '...'`) represents a meaningful reduction in the cost-of-experimentation for harness engineers evaluating open-weights models. The `llm` CLI + OpenRouter pattern generalizes beyond GLM-5.1 to any model OpenRouter carries.

### Claim 2: GLM-5.1 spontaneously produced HTML+CSS animations alongside an SVG without being asked
- **Evidence**: Willison's direct observation: "something new happened... unprompted, the model decided to give me an HTML page that included both the SVG and a separate set of CSS animations!"
- **Confidence**: anecdotal (single instance, no controls)
- **Quote**: "unprompted, the model decided to give me an HTML page that included both the SVG and a separate set of CSS animations!"
- **Our assessment**: This "scope creep" behavior (producing more than asked) is the kind of model behavior that can surprise harness engineers. It is a positive surprise here (richer output), but it demonstrates that large open-weights models may exceed the literal task specification in ways smaller models don't. Relevant to prompt design: if you want exactly what you asked for, you need to be more constraining; if you want the model to show initiative, some models will do it unprompted.

### Claim 3: GLM-5.1 correctly diagnosed and fixed a CSS coordinate-system bug from a vague symptom description in a single follow-up prompt
- **Evidence**: Willison's session log. Bug symptom reported: "the animation is a bit broken, the pelican ends up positioned off the screen at the top right." Model diagnosis: "The issue is that CSS `transform` animations on SVG elements override the SVG `transform` attribute used for positioning." Model produced corrected HTML in the same response.
- **Confidence**: anecdotal (single session, single bug type)
- **Quote**: "GLM 5.1 replied: 'The issue is that CSS `transform` animations on SVG elements override the SVG `transform` attribute used for positioning'"
- **Our assessment**: The model identified the correct root cause (CSS/SVG transform interaction is a known browser quirk) from a vague symptom without being told what was technically wrong. This is evidence that multi-turn refinement — even with imprecise natural-language feedback — can surface correct technical diagnoses in one step. The limitation: this is one instance of one model fixing one specific and well-known CSS bug. Willison explicitly notes this was exceptional enough that he broke his usual single-prompt rule for the pelican test.

### Claim 4: GLM-5.1's generated SVG code includes detailed human-readable inline comments explaining each geometric element
- **Evidence**: Willison reproduces an SVG excerpt with comments like `<!-- Pouch (lower beak) with wobble -->`, `<!-- Earring sparkle -->`, `<!-- Opossum fur gradient -->`, `<!-- Distant treeline silhouette - Virginia pines -->`.
- **Confidence**: anecdotal
- **Quote**: `<!-- Pouch (lower beak) with wobble -->` (and others from the SVG code block)
- **Our assessment**: The self-documenting code behavior is relevant to harness engineering: a model that annotates its own generated geometry is more debuggable output than uncommented code. The specific level of detail ("Virginia pines," "CRUISING THE COMMONWEALTH SINCE DUSK") suggests the model extrapolated narrative context from minimal input — both a feature and a potential distraction for constrained tasks.

### Claim 5: GLM-5.1 produces some animation glitches at fine-grained detail (eyes "occasionally fall off the face")
- **Evidence**: Bluesky community opossum test (cited in the post's Update section): "slight glitches where eyes occasionally fall off the face."
- **Confidence**: anecdotal (single community example, no reproduction)
- **Quote**: "with slight glitches where eyes occasionally fall off the face"
- **Our assessment**: The glitch pattern (small positional errors in fine details) is consistent with the general behavior of large generative models on geometrically constrained tasks: large-scale composition is good, small-scale precision is unreliable. For practitioners using models for SVG/code generation: expect correct overall structure, unreliable fine-grain detail, and plan a review/correction step for precision-sensitive outputs.

### Claim 6: The `llm` CLI + OpenRouter plugin provides a consistent interface for testing frontier-scale open-weights models without model-specific API wrappers
- **Evidence**: The workflow shown (`llm install llm-openrouter` once, then `llm -m openrouter/<provider>/<model> '...'` for any model, `llm -c '...'` for follow-up in the same context) is the same CLI interface Willison uses across models. The `-c` flag for continuing a context is the multi-turn primitive.
- **Confidence**: settled (the `llm` CLI and its OpenRouter plugin are documented open-source software; this workflow is verifiable)
- **Quote**: `llm -c 'the animation is a bit broken...'` (demonstrates the continuation flag)
- **Our assessment**: The `-c` flag for multi-turn continuation is worth noting in the harness engineering context: it is the command-line equivalent of a follow-up prompt, and it is consistent across every model the `llm` CLI supports. This means practitioners can script multi-turn refinement loops without model-specific SDKs.

## Concrete Artifacts

### Full CLI invocation from the post

```bash
# Install the OpenRouter plugin (one-time)
llm install llm-openrouter

# Initial prompt
llm -m openrouter/z-ai/glm-5.1 'Generate an SVG of a pelican on a bicycle'

# Follow-up (continues same context via -c flag)
llm -c 'the animation is a bit broken, the pelican ends up positioned off the screen at the top right'
```

*Source: Simon Willison, simonwillison.net/2026/Apr/7/glm-51/*

### Self-documenting SVG excerpt (beak animation)

```svg
<!-- Pouch (lower beak) with wobble -->
<g>
    <path d="M42,-58 Q43,-50 48,-42 Q55,-35 62,-38 Q70,-42 75,-60 L42,-58 Z" fill="url(#pouchGrad)" stroke="#b06008" stroke-width="1" opacity="0.9"/>
    <path d="M48,-50 Q55,-46 60,-52" fill="none" stroke="#c06a08" stroke-width="0.8" opacity="0.6"/>
    <animateTransform attributeName="transform" type="scale"
    values="1,1; 1.03,0.97; 1,1" dur="0.75s" repeatCount="indefinite"
    additive="sum"/>
</g>
```

*Source: Simon Willison, simonwillison.net/2026/Apr/7/glm-51/ — reproduced from GLM-5.1 output*

### Model's self-diagnosis of the bug

```
User: "the animation is a bit broken, the pelican ends up positioned off the screen at the top right"

GLM-5.1: "The issue is that CSS `transform` animations on SVG elements override the
SVG `transform` attribute used for positioning"
[followed by corrected HTML]
```

*Source: Simon Willison, simonwillison.net/2026/Apr/7/glm-51/*

## Cross-References

- **Corroborates**: None of the existing source notes cover open-weights model access via `llm` CLI or OpenRouter, so this is primarily novel in that dimension.
- **Contradicts**: Nothing. The post is too narrow and anecdotal to contradict any existing note.
- **Extends**:
  - **blog-addyosmani-code-agent-orchestra.md** (Osmani, Claim on multi-model routing): Osmani recommends routing planning to "capable models." This post provides a concrete example of how the `llm` CLI + OpenRouter makes the model-switching step of that routing pattern operationally simple — one flag change, consistent interface, no new SDK.
  - **paper-miller-speed-cost-quality.md** (Prospector identified as overlapping): The Miller et al. paper covers quality outcomes of Cursor adoption; it does not address model selection or open-weights availability. The only connecting thread is "model capabilities matter for quality outcomes" — but the GLM-5.1 post provides no quality metrics, so the connection is weak. The overlap noted by the Prospector is thematic rather than evidentiary.
- **Novel**:
  - **GLM-5.1 model metadata** (754B, MIT, Z.ai, 2026-04-07) — not covered elsewhere in our corpus; post-cutoff.
  - **`llm` CLI + OpenRouter as a harness-agnostic model-testing interface** — no other source in the corpus describes this pattern. The `-c` continuation flag for multi-turn is the specific artifact worth preserving.
  - **Multi-turn self-correction from a vague symptom** — Claim 3 is the only instance in our corpus of a model self-diagnosing a CSS coordinate-system bug without being told the technical root cause. The single-prompt self-correction pattern (not multi-step iteration) is worth noting.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add a tool-note or sidebar on the `llm` CLI + OpenRouter as the lowest-friction path for testing a new model without switching harnesses. The two-command setup (`llm install llm-openrouter` + `llm -m openrouter/...`) is a practical daily-workflow addition for practitioners who want to compare model outputs quickly. The `-c` flag for multi-turn continuation is worth calling out explicitly.
- **Chapter 02 (Harness Engineering — Model Selection)**: GLM-5.1's MIT license and OpenRouter availability are evidence that the landscape of viable open-weights models for harness integration has expanded to frontier scale (754B). If the chapter covers model selection criteria, add a note that MIT-licensed frontier-scale open-weights models are now accessible via commodity APIs, which changes the build-vs-vendor calculus for teams with data-residency or cost constraints.
- **Chapter 02 (Multi-Turn Refinement Patterns)**: Claim 3 (self-diagnosis of CSS transform bug from vague symptom) is weak evidence but the only in-corpus example of vague-symptom → correct-technical-diagnosis in a single follow-up. If the chapter covers multi-turn refinement patterns, this is a concrete (if anecdotal) illustration of what "just describe the symptom" can achieve.

## Extraction Notes

- **Thin source, as expected**: The Prospector's triage correctly assessed this as minimal extractable signal. The post is ~400 words, no methodology, no benchmarks, two prompts. The value is currency (post-cutoff, 2026-04-07) and the specific `llm` + OpenRouter workflow artifact.
- **Pelican test context**: Willison applies the "generate an SVG of a pelican on a bicycle" prompt consistently across models — it is his recurring creative-code benchmark. Results are intentionally informal and comparative across his blog, not rigorous. The fact that he made an exception to his "single-prompt" rule is itself a signal about the model's output quality.
- **No sub-pages followed**: The post links to Gists with the full SVG code but the Gist content is not reproduced in the main article. The SVG excerpt reproduced by Willison is sufficient for extraction purposes.
- **Z.ai / GLM lineage**: GLM-5.1 shares architecture with GLM-5 (same paper, same 754B parameter count). The "Towards Long-Horizon Tasks" subtitle in the paper title is the only harness-relevant signal in the model name — it suggests the model is intended for multi-step tasks, not just single-turn generation. Willison does not evaluate this claim.
