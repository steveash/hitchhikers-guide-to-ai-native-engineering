---
source_url: https://simonwillison.net/2026/Oct/1/pwasm/
source_type: blog-post
title: "pwasm 0.2a0 — A WebAssembly engine in pure Python"
author: Simon Willison
date_published: 2026-10-01
date_extracted: 2026-10-08
last_checked: 2026-10-08
status: current
confidence_overall: anecdotal
issue: "#3976"
---

# pwasm 0.2a0

> A short release note recording one scoped prompt given to Claude Opus 5.5 against a 10-month-old, fully vibe-coded project, the resulting 42 commits, and the author's explicit refusal to trust the output.

## Source Context

- **Type**: blog-post (release note with a two-paragraph experience report; very short)
- **Author credibility**: Simon Willison, creator of Django and Datasette, prolific practitioner-commentator on LLM tooling. The project is a self-described "folly" project, so stakes are low.
- **Scope**: Covers the prompt, the commit count, headline outcomes, and a trust caveat. Gives no metrics, test results, spec-conformance numbers, benchmarks, or failure details. pwasm internals are out of scope for this guide.

## Extracted Claims

### Claim 1: A single scoped "evaluate, then consider what it would take" prompt was the whole brief for a multi-goal agent session
- **Evidence**: Author's own report of the prompt text; no transcript linked in the post.
- **Confidence**: anecdotal
- **Quote**: "Evaluate current state of pwasm - then consider what it would take to get the MicroPython and micro JavaScript experiments from the research repo working under it - and what it would take to speed it up"
- **Our assessment**: The prompt asks for assessment and planning first, then two goals (compatibility, speed), rather than prescribing steps. Useful as an example of a plan-first brief for returning to old code, but a single unreplicated example.

### Claim 2: The agent produced 42 commits with minimal follow-up prompting
- **Evidence**: Author-reported commit count; the post does not link the commit history.
- **Confidence**: anecdotal
- **Quote**: "42 commits later (with minimal follow-up prompting)"
- **Our assessment**: Indicates a long autonomous run, but commit count is a weak proxy for progress and says nothing about review effort or rework.

### Claim 3: Outcome self-reported as near-complete WASM spec support plus bundled MicroPython/QuickJS builds
- **Evidence**: Author statement only; no conformance-suite numbers or speed figures given.
- **Confidence**: anecdotal
- **Quote**: "it now handles almost all of the WASM specification, and the wheel from PyPI bundles working WASM builds of  MicroPython, QuickJS and Micro QuickJS."
- **Our assessment**: Treat as an unverified author claim. The speed-up goal in the prompt is not reported on at all.

### Claim 4: The author explicitly does not trust the result, and uses the alpha tag as the trust signal
- **Evidence**: Author statement; version number `0.2a0`.
- **Confidence**: anecdotal
- **Quote**: "I wouldn't trust this thing at all - hence the alpha version tag"
- **Our assessment**: Notable that the author publishes agent-built, unverified work but labels it honestly via versioning. Ties to the verification-vs-vibe-coding theme in his other posts.

### Claim 5: Newer models can improve on work done by older models months earlier
- **Evidence**: Single case: January 2026 vibe-coded project revisited in October 2026 with Opus 5.5.
- **Confidence**: anecdotal
- **Quote**: "it's interesting seeing how today's models can improve on the work of models from 10 months ago."
- **Our assessment**: Interesting framing (agent-built legacy code can be upgraded by later agents), but no comparison against a baseline, so it is an observation, not evidence.

## Concrete Artifacts

```
Prompt (Simon Willison, https://simonwillison.net/2026/Oct/1/pwasm/):
Evaluate current state of pwasm - then consider what it would take to get the MicroPython and micro JavaScript experiments from the research repo working under it - and what it would take to speed it up
```

Metrics reported: 42 commits; model Claude Opus 5.5; version 0.2a0. Nothing else quantitative.

## Cross-References

- **Corroborates**: `blog-simonwillison-vibe-coding-agentic-engineering.md` (same author's discussion of trusting agent output without reading it); here the distrust is stated openly.
- **Contradicts**: none found.
- **Extends**: `blog-anthropic-harness-long-running.md` (long-running agent work) only loosely, as a small low-stakes example of a long run with little human steering.
- **Novel**: Re-visiting an old, fully vibe-coded repo with a newer model as a maintenance pattern; otherwise thin. Related but different topic: `blog-simonwillison-wasm-wheels-pypi.md`.

## Guide Impact

- **Chapter 01**: At most, a one-line anecdote that a plan-first, multi-goal prompt ("evaluate current state, then consider what it would take...") on a dormant codebase led to a long agent run. Not enough to change recommendations.
- **Chapter 03**: Optionally cite as an example of an author declining to vouch for agent output and signaling it via pre-release versioning.

## Extraction Notes

- Read the full post (it is two short paragraphs plus the prompt). No sub-pages followed; the linked pwasm repo and PyPI page were not evaluated, so coverage and bundling claims remain unverified.
- Per the Prospector triage, pwasm/WebAssembly internals were deliberately not extracted. The thin evidence means few claims; this is the source's actual size, not a skim.
