---
source_url: https://developers.googleblog.com/fast-reliable-a2ui/
source_type: blog-post
title: "Fast, reliable A2UI, with swappable inference formats"
author: Vishal Motwani and the Google A2UI Team
date_published: 2026-10-27
date_extracted: 2026-10-28
last_checked: 2026-10-28
status: current
confidence_overall: anecdotal
issue: "#4388"
---

# Fast, reliable A2UI, with swappable inference formats

> A vendor announcement arguing that the format a model emits (a compact Python-like DSL, "Express") should be decoupled from the wire protocol (A2UI JSON) and compiled deterministically, cutting output tokens and latency; the only eval evidence is vendor-reported and largely non-numeric.

## Source Context

- **Type**: blog-post (vendor product announcement, Google Developers Blog)
- **Author credibility**: Google A2UI team; first-hand builders of the SDK, but the numbers are self-reported and the post is promotional.
- **Scope**: Covers A2UI inference formats (Direct JSON, Express, Atom, Elemental), the `inference_format` SDK hook, and a Jev-based controlled-generation alternative. Per triage, the UI catalog/protocol details and the Jev material (already covered elsewhere) are deliberately not extracted. Only the format-vs-tokens/latency/accuracy finding is.

## Extracted Claims

### Claim 1: Generating schema-constrained JSON trees is slow and error-prone for LLMs
- **Evidence**: Assertion by the authors; motivation for the work. No error rates are given.
- **Confidence**: anecdotal
- **Quote**: "It turns out that generating JSON trees constrained by a complex JSON schema is slow and error-prone for LLMs."
- **Our assessment**: Plausible and consistent with common experience with deeply nested output, but unquantified here.

### Claim 2: Express, a one-statement-per-line, Python-like DSL, needs up to 3x fewer tokens than Direct JSON for the same UI
- **Evidence**: Vendor-reported; "up to" figure, no distribution or per-task table in the post.
- **Confidence**: anecdotal
- **Quote**: "Express requires up to 3x fewer tokens to generate the same kinds of UI compared to Direct JSON."
- **Our assessment**: Directionally believable (variable-named components remove repeated keys, IDs and braces). "Up to" is a best case; do not treat 3x as typical.

### Claim 3: Express syntax: each line assigns a component to a variable whose name becomes the component ID
- **Evidence**: Design description.
- **Confidence**: settled (as a description of the design)
- **Quote**: "Each line assigns a component to a variable, and the variable name becomes the component ID."
- **Our assessment**: The mechanism worth noting: the model-facing format carries references by name, so the compiler, not the model, handles IDs and structure.

### Claim 4: Four inference formats were compared on the same 51-task eval with gemini-3.5-flash
- **Evidence**: Stated eval design. The post gives no numeric scores for Atom or Elemental in the text we could retrieve; Express was chosen as default.
- **Confidence**: anecdotal
- **Quote**: "We ran all four formats through the same 51-task eval on gemini-3.5-flash."
- **Our assessment**: A single model and 51 tasks is small; the eval is not independently reproducible from the post alone.

### Claim 5: Express holds up with thinking turned off
- **Evidence**: Reported observation from the 51-task eval; no numbers quoted.
- **Confidence**: anecdotal
- **Quote**: "We observed that Express inference format works just as well even with thinking off"
- **Our assessment**: This is the most interesting claim for the guide: a well-chosen output format may substitute for reasoning budget and lower latency. Needs the underlying numbers to be actionable.

### Claim 6: The alternative formats bet on different model strengths (Lisp-style S-expressions vs. HTML custom elements)
- **Evidence**: Format descriptions.
- **Confidence**: settled (descriptive)
- **Quote**: "Writes HTML with custom elements, betting on how well models already write HTML."
- **Our assessment**: Frames format choice as exploiting the model's training distribution (Elemental) versus minimizing tokens (Atom: "Writes Lisp-style S-expressions with no assignments and no closing tags.").

### Claim 7: Using a System One decision model (Jev) yields much lower latency, up to 80x, with a tiny-sample demo
- **Evidence**: One run of 11 prompts in the Apparite (jev2ui) project; authors caveat it.
- **Confidence**: anecdotal
- **Quote**: "the component tree was on screen in 92 to 298 ms and each screen was complete in 0.8 to 1.7 s."
- **Our assessment**: The authors themselves call it a first look ("since the sample is small"). The 80x headline applies to a best case and is not general. Jev mechanics are already covered by existing notes.

## Concrete Artifacts

```python
# Attributed: Google Developers Blog, "Fast, reliable A2UI..." (inference_format sample)
from a2ui.processor import A2uiGenerator, CatalogConfig
from a2ui.inference_formats import ExpressFormatFactory

catalog = CatalogConfig.from_path("catalog.json")
generator = A2uiGenerator(
    [catalog],
    examples=few_shot_examples,  # written once as A2UI JSON
    inference_format_factory=ExpressFormatFactory(),
)

processor = generator.create_processor(renderer_capabilities)
system_prompt = f"{instructions}\n\n{processor.prompt_snippet}"
parts = processor.parse_response(model_reply)  # text parts + validated A2UI messages
```

Pattern: few-shot examples are authored once in the canonical protocol; the SDK renders them into the chosen inference format, generates the prompt snippet from the catalog schema, and `parse_response` compiles the reply into validated messages.

## Cross-References

- **Corroborates**: `blog-google-prompt-transpilation.md` (Claim 4) shares the theme of deterministic compilation between authored content and what runs in production, though for prompts rather than model output.
- **Contradicts**: None found.
- **Extends**: `blog-simonwillison-jev-decision-models.md` (Claim 1, Jev as typed decisions rather than text) and `blog-thoughtworks-mugrage-jev-decision-models-what-to-know.md`: this post adds a Jev + A2UI example where code builds the component tree from decisions.
- **Novel**: The idea of a swappable model-facing DSL compiled to a validated wire protocol, with a four-format comparison and the "thinking off" observation. No existing note covers A2UI or generative UI.

## Guide Impact

- **Chapter 04**: Possible short example in output-format/token-cost discussion: a compact intermediate format plus deterministic expansion can cut output tokens (vendor-reported "up to 3x"). Mark as vendor-reported, single-model, 51 tasks.
- **Chapter 02**: Optional supporting example of a deterministic compile/validate step between model output and a protocol. Weak fit; generative UI itself is out of scope for the guide.

## Extraction Notes

- Read the full article via a fetch tool that returns processed excerpts; quotes were taken from the fetched text. The Assayer should spot-check them against the page. Numeric eval results for Atom/Elemental were not available from the retrieved text, so none are claimed.
- Followed the triage guidance: skipped UI catalog details and the Jev controlled-generation section beyond the latency data point.
