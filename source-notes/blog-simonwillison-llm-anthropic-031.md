---
source_url: https://simonwillison.net/2026/Nov/9/llm-anthropic/
source_type: blog-post
title: "llm-anthropic 0.31"
author: Simon Willison
date_published: 2026-11-09
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: anecdotal
issue: "#4633"
---

# llm-anthropic 0.31

> A short Willison release beat adding Fable 5.2 / Mythos 5.2 to `llm-anthropic`, whose main value is one single-author failure datapoint (Fable 5.2 at `max` effort burns 128,000 thinking tokens and returns nothing) and a stated 20% price cut versus Fable 5.1.

## Source Context

- **Type**: blog-post (Willison "Release" beat, roughly 200 words, one shell snippet). The linked GitHub release for tag `0.31` was also read; its body is a single bullet naming `claude-fable-5.2` and `claude-mythos-5.2`.
- **Author credibility**: Simon Willison maintains `llm` and `llm-anthropic` and runs the pelican SVG benchmark across models, so the observations are first-hand. Single author, single prompt.
- **Scope**: Install/invoke steps, a five-level reasoning sweep on one prompt, one failure, and one price comparison. It gives no run counts, no token or cost figures for the successful levels, and no pricing source. The mysterious-beep reference is covered in `blog-simonwillison-mysterious-beeps.md`.

## Extracted Claims

### Claim 1: llm-anthropic 0.31 adds Fable 5.2 and Mythos 5.2, invoked as `claude-fable-5.2`
- **Evidence**: Author statement, a shell snippet, and the one-line GitHub release body.
- **Confidence**: settled (shipped tooling fact)
- **Quote**: "I've added the new models to llm-anthropic, so you can now run prompts through Fable 5.2 like this:"
- **Our assessment**: Accurate as far as it goes. The note's 0.30 sibling (`blog-simonwillison-llm-anthropic-030.md` Claim 1) described `llm anthropic refresh` so that a plugin release would not be needed per model. This release still names the two models explicitly. The post does not say whether `refresh` could have served them. It is therefore not evidence that the refresh feature failed, only that the author shipped a release on launch day anyway.

### Claim 2: At `max` reasoning effort Fable 5.2 spent 128,000 tokens thinking and returned no image
- **Evidence**: One run of the pelican SVG prompt at each of five levels (low, medium, high, xhigh, max); results linked by the author. No repeat count, no cost figure given.
- **Confidence**: anecdotal (one author, one prompt, apparently one run)
- **Quote**: "max failed to return an image at all, running out of tokens after spending 128,000 thinking about them."
- **Our assessment**: Consistent with the earlier Opus 5.5 report. Reasoning tokens share the 128k output cap, so a maximal effort setting can yield no deliverable. Nothing here shows how often it occurs; do not generalise beyond "observed once on a trivial prompt."

### Claim 3: The `max` failure is a regression within the Fable series: Fable 5 and 5.1 handled `max`, Fable 5.2 does not
- **Evidence**: Author's comparison with his earlier runs of the same prompt.
- **Confidence**: anecdotal
- **Quote**: "That's the same bug that I saw with Opus 5.5 - but it's new for the Fable series, both Fable 5 and Fable 5.1 returned max effort pelicans just fine."
- **Our assessment**: Useful because it shows that "max works" is a per-model-version property, not a family property; effort levels should be re-tested on each model upgrade. Fable 5.2 is also Anthropic's stated recommended-effort story (Medium default; High roughly matching Opus 5.5 at Max, per `blog-anthropic-claude-fable-and-mythos-5-2.md` Claim 7), which fits with avoiding `max`. We have no evidence Anthropic acknowledged the bug.

### Claim 4: Fable 5.2 is priced at $8/M input and $40/M output, a 20% cut from Fable 5.1
- **Evidence**: Author statement of list price.
- **Confidence**: settled (corroborated by the vendor launch post in our corpus)
- **Quote**: "It's priced at $8/million input and $40/million output, which is a 20% discount on the previous Fable 5.1 ($10/$50)."
- **Our assessment**: Arithmetic checks out (8/10 and 40/50 are both 0.8). The $10/$50 figure for Fable 5 matches `blog-simonwillison-claude-fable-5.md` Claim 1, and $8/$40 matches `blog-anthropic-claude-fable-and-mythos-5-2.md` Claim 5, so the pricing is independently supported. The post states Fable 5.1 pricing as equal to Fable 5; we did not verify that separately.

### Claim 5: The `xhigh` run gave the best pelican of the five levels, though with minor flaws
- **Evidence**: Author's judgement on a single image per level (the post links the images; flaws are only in the linked page, not reproduced here).
- **Confidence**: anecdotal
- **Quote**: "here's the best result I got, from xhigh:"
- **Our assessment**: Weak quality evidence (n=1 per level, subjective). Worth noting only because the best output came from the level below the one that failed, which is the same pattern as in `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 9 and 10 where `max` was the problem level. It does not show monotonic improvement with effort.

## Concrete Artifacts

```
# From the post (Willison, 2026-11-09)
uv tool install llm
llm install llm-anthropic
llm keys set anthropic
# paste key here
llm -m claude-fable-5.2 "Generate an SVG of a pelican riding a bicycle"
```

```
# GitHub release body for llm-anthropic 0.31
- `claude-fable-5.2` and `claude-mythos-5.2`.
```

Failure symptom: at `max` effort, 128,000 output tokens consumed by thinking, no SVG returned.

## Cross-References

- **Corroborates**: `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 9 (Opus 5.5 at `max` hit the 128,000 output cap while still reasoning and returned no answer); `blog-anthropic-claude-fable-and-mythos-5-2.md` Claim 5 ($8/$40 pricing).
- **Contradicts**: none found. The Fable 5.2 `max` failure sits beside, not against, `blog-simonwillison-claude-fable-5.md` Claim 11, where Fable 5 at `max` produced 14,430 output tokens and a result; the difference is a model-version change, not a conflict. No contradiction issue filed.
- **Extends**: `blog-simonwillison-llm-anthropic-030.md` (same plugin; this release again adds models by explicit plugin release) and `blog-simonwillison-claude-fable-5.md` (same pelican five-level sweep, now on 5.2).
- **Novel**: The first report in the corpus of a `max`-effort exhaustion failure on a Fable model, and the explicit statement that it is new in 5.2 relative to Fable 5 and 5.1.

## Guide Impact

- **Effort / context budgeting chapters (Ch04 per triage; Ch02 harness settings)**: Add this as a second independent model-version example, next to Opus 5.5, that top effort settings can consume the whole output cap with no result. Recommended wording: test each effort level on each new model version, and cap or avoid `max` for unattended runs. Cite as anecdotal, with Opus 5.5 as the corroborating data point.
- **Cost planning**: If the guide cites Fable pricing, use $8/$40 for 5.2 (supported by the vendor note too), not $10/$50.
- Low priority overall: thin source; do not build a section on it.

## Extraction Notes

- Fetched the post HTML directly to copy quotes verbatim; the summarising fetch tool alone was not used for quotes.
- Followed the one linked page that carries content (the GitHub release for 0.31); it is a single bullet. Did not follow the Artificial Analysis ranking or the black-hole physics claim, which the post only relays from Anthropic; neither is extracted as a claim.
- Triage comments suggested checking if 0.31 still needs a release per model. The post and release say nothing about `refresh`, so that is left as an open observation in Claim 1.
- No contradictions found, so none were filed.
