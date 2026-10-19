---
source_url: https://simonwillison.net/2026/Oct/12/python-3-15-web-edit-profiling/
source_type: blog-post
title: "Profiling web-edit with Python 3.15: flame graphs and source heatmaps"
author: Simon Willison
date_published: 2026-10-12
date_extracted: 2026-10-19
last_checked: 2026-10-19
status: current
confidence_overall: anecdotal
issue: "#4206"
---

# Profiling web-edit with Python 3.15: flame graphs and source heatmaps

> A very short "research" post in which a Codex agent drove Python 3.15's built-in sampling profiler against an unmodified app; its only transferable lesson is that all-thread sampling was needed because nearly all stacks ran on a worker thread.

## Source Context

- **Type**: blog-post (Simon Willison "Research" entry: a one-paragraph summary, the verbatim prompt, and links to generated flame graph/heatmap artifacts)
- **Author credibility**: Simon Willison is the author of the web-edit app being profiled and a prolific practitioner-commentator on LLM tooling. First-hand account, but the post is a demo, not an analysis.
- **Scope**: Covers one agent run: prompt, headline profile numbers, one methodological note (sample all threads). Does NOT cover: how the agent chose its profiler flags, whether any fix was made or measured, repeat runs, or the underlying research write-up. Only the summary text on the post page was read; the linked flame graph/heatmap pages were not followed.

## Extracted Claims

### Claim 1: An agent was able to run Python 3.15's `profiling.sampling` against an unmodified app from a one-line prompt and produce flame graph and heatmap demos
- **Evidence**: The verbatim prompt is given; outputs are linked as artifacts. No transcript of the agent's steps is in the post.
- **Confidence**: anecdotal
- **Quote**: "I need a Python 3.15 flame graph and heatmap demo of the "web-edit" app from PyPI - research first then make me those demos"
- **Our assessment**: Plausible and low-bar: a single run on a small app. It shows a "research first, then build" prompt shape with a tool the model likely has little training data on (new in 3.15), but the post does not show how the agent learned the tool. Don't generalize beyond "it worked once".

### Claim 2: Mixed line-ending preservation dominated a busy editing workload
- **Evidence**: Profile counts: `preserve_endings` in 64.8% of 15,296 recorded CPU stacks.
- **Confidence**: anecdotal
- **Quote**: "`preserve_endings` appeared in 64.8% of 15,296 recorded CPU stacks"
- **Our assessment**: Concrete number, but from one workload on one personal app, with no statement of workload definition, duration, or sampling rate. App-specific; not a general finding.

### Claim 3: `SequenceMatcher.find_longest_match` was the largest leaf contributor
- **Evidence**: 38.3% of leaf samples.
- **Confidence**: anecdotal
- **Quote**: "`SequenceMatcher.find_longest_match` contributing 38.3% of leaf samples"
- **Our assessment**: Consistent with Claim 2 (diff matching inside ending preservation). No fix or before/after measurement is reported, so this is diagnosis only.

### Claim 4: Sampling all threads was essential because almost all stacks ran on AnyIO's worker thread
- **Evidence**: 95.1% of stacks came from the AnyIO worker thread.
- **Confidence**: anecdotal (but mechanistically sound)
- **Quote**: "Sampling all threads was essential, since 95.1% of stacks came from AnyIO's worker thread and would have been missed by a main-thread-only profile."
- **Our assessment**: The most reusable point, and it is a verification-coverage lesson: a measurement that looks complete (a profile exists) can silently omit where the work happens. It applies to reviewing agent-produced profiles of async/threaded code. Caveat: the post doesn't say whether the agent chose all-thread sampling itself or was told to, so it can't support a claim about agent judgment.

## Concrete Artifacts

```
Prompt (verbatim, from the post, run in Codex with GPT-6 Astra Extra High):
I need a Python 3.15 flame graph and heatmap demo of the "web-edit" app from PyPI - research first then make me those demos

Headline results (from the post summary):
- preserve_endings: 64.8% of 15,296 recorded CPU stacks
- SequenceMatcher.find_longest_match: 38.3% of leaf samples
- 95.1% of stacks on AnyIO's worker thread
```

## Cross-References

- **Corroborates**: None directly.
- **Contradicts**: None.
- **Extends**: None. Overlap is incidental: `blog-ghaw-weekly-2026-09-21.md` Claim 12 concerns CRLF line endings in an unrelated GitHub Actions bug; it is not about this app.
- **Novel**: Only note in the corpus on agent-driven profiling or Python 3.15's `profiling.sampling`. Compare for "agent runs a specialist tool end-to-end" framing: `blog-openai-codex-quantum-computing-experiments.md` Claim 1 (much stronger evidence, far larger scope).

## Guide Impact

- **Chapter 03 (verification)**: At most a one-line example under measurement-coverage checks: when an agent profiles threaded/async code, confirm the profile covers worker threads (here 95.1% of stacks were off the main thread). Evidence is a single anecdote, so cite as illustration only, not as a recommendation backed by data.
- **Chapter 01**: No change recommended; the evidence is too thin to add a workflow.

## Extraction Notes

- The post is a few sentences plus the prompt; the fetch tool returned only a summary, so quotes were verified against the raw page text fetched with curl. Quotes are verbatim.
- Linked flame graph/heatmap/research artifacts were not read. The Prospector flagged this as a short single-run demo; the note stays narrow accordingly.
- No contradictions found, so no contradiction issue was filed.
