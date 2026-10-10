---
source_url: https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words/
source_type: blog-post
title: "Qwen3.8 27B addition in words"
author: Simon Willison
date_published: 2026-10-04
date_extracted: 2026-10-10
last_checked: 2026-10-10
status: current
confidence_overall: anecdotal
issue: "#4029"
---

# Qwen3.8 27B addition in words

> A short, agent-run experiment showing that a local Qwen3.8-27B (Q4_K_M) with reasoning disabled is badly unreliable at exact multi-digit addition (23.57% overall, collapsing with operand length) while a reasoning-enabled run got 167 of 169 right, supporting "verify or delegate exact computation" advice.

## Source Context

- **Type**: blog-post (simonwillison.net "Research" entry; short, mostly charts plus an LLM-generated summary and a linked report)
- **Author credibility**: Simon Willison is a trusted-feed author (creator of Django, Datasette, `llm`). This is a first-person informal experiment, inspired by a Bluesky post from Colin Frasier, not a controlled study. The experiment code and report were produced by an agent (Codex Remote session, GPT-6 Astra), not hand-written by the author.
- **Scope**: One model (`Qwen3.8-27B-Q4_K_M.gguf`), one machine (DGX Spark), one task (add two positive integers, answer in English words only). The post body is brief; most numbers live in the summary and in heatmap images and a linked report that are not reproduced in the page text. It does NOT test tool/calculator access, other models (beyond a reference to GPT-4o results by Frasier), or why accuracy falls with length.

## Extracted Claims

### Claim 1: With reasoning disabled, the local Qwen3.8-27B is only 23.57% accurate on exact addition expressed in words over 5,070 cases
- **Evidence**: Benchmark of 5,070 reasoning-disabled cases (30 attempts per operand-length combination per the post body), run by a Codex agent on a DGX Spark. Numbers come from the post's summary; the heatmap itself is an image.
- **Confidence**: anecdotal (single model, single run setup, summary text is LLM-generated)
- **Quote**: "Without reasoning, it achieved 23.57% numeric accuracy, with performance dropping from 97.04% for one- to three-digit operands to 6.44% for ten- to thirteen-digit operands, despite 96.17% format compliance."
- **Our assessment**: Plausible and consistent with the well-known weakness of non-reasoning LLMs at multi-digit arithmetic. Useful as a concrete number, but not general: it is one quantised 27B model. Note that the 23.57% aggregate depends on how many cells at each length were sampled, so the per-length figures matter more than the headline.

### Claim 2: Accuracy degrades sharply with operand length while format compliance stays high, i.e. the model fails confidently rather than visibly
- **Evidence**: 97.04% (1-3 digits) vs 6.44% (10-13 digits), with 96.17% of outputs in the required words-only format.
- **Confidence**: anecdotal
- **Quote**: "despite 96.17% format compliance"
- **Our assessment**: The key verification lesson: output that looks well-formed (right format, fluent English) says nothing about correctness. A format/schema check would pass ~96% of these outputs while ~76% are wrong. This is an inference from the two numbers, not a statement the author makes.

### Claim 3: With reasoning enabled, a paired run got 167 of 169 correct, but this was one sample per cell and is noisy
- **Evidence**: Reasoning (medium, per the summary) run with a single attempt per operand-length square because it "took a lot longer per pair"; the author says each heatmap square is therefore 100% or 0%.
- **Confidence**: anecdotal
- **Quote**: "It got the right answer in 167 out of 169 attempts, and since these were one-shot I'm confident a second run would produce different results here."
- **Our assessment**: Direction (reasoning recovers most accuracy) is believable; the exact 167/169 figure is not a stable estimate, and the author says so. Comparing it with the 30-sample reasoning-off run is only roughly apples to apples. Cost is unquantified: slower per pair, token cost not given.

### Claim 4: Reasoning traces show the model doing schoolbook column addition, which is why reasoning fixes the problem
- **Evidence**: The linked report includes traces from large calculations; the post excerpts one that aligns digits and adds right to left with carries.
- **Confidence**: anecdotal
- **Quote**: "Adding from right to left:"
- **Our assessment**: Shows the mechanism is the model externalising an algorithm into tokens, effectively doing in-context computation rather than recall. The excerpt also includes a "Wait, let me redo this more carefully." self-correction. Not a proof that reasoning is always reliable; just two failures in 169.

### Claim 5: The author trusts that GPT-4o's earlier failures were genuine model errors, not tool use, and reran the experiment locally to control for that
- **Evidence**: Author's reasoning: the model got many answers wrong, so no calculator was involved; local hardware gives a fully controlled environment (no hidden tools).
- **Confidence**: anecdotal
- **Quote**: "I'm confident GPT-4o didn't cheat and use a calculator, especially since it got so many of the calculations wrong"
- **Our assessment**: A useful methodological point: hosted chat products may silently route arithmetic to code tools, so measuring raw model ability requires a controlled local harness. It also implies that production harnesses with code execution would avoid these errors entirely, though the post does not test that.

### Claim 6: The experiment itself was delegated to a coding agent given only a screenshot of a prior chart
- **Evidence**: The author pasted Frasier's chart image into a Codex Remote session and asked it to run the same experiment against the local model.
- **Confidence**: anecdotal
- **Quote**: "I pasted his image into a Codex Remote session (GPT-6 Astra) and had it run the same experiment using Qwen3.8-27B-Q4_K_M.gguf."
- **Our assessment**: A small example of agents as experiment runners (replicate-from-image). The post gives no detail on how the agent's harness was checked, so the results inherit that unverified layer.

## Concrete Artifacts

```
Experiment design (from the post, Simon Willison, 2026-10-04):
- Task: add positive integers; answer exactly, in English words only
- Model: Qwen3.8-27B-Q4_K_M.gguf on a DGX Spark
- Run A: reasoning disabled, 30 attempts per operand-length combination, 5,070 cases total
- Run B: reasoning enabled (medium), 1 attempt per combination, 169 cases
Results (post summary):
- Run A: 23.57% numeric accuracy; 97.04% (1-3 digit operands) -> 6.44% (10-13 digit operands); 96.17% format compliance
- Run B: 167/169 correct
```

```
Reasoning-trace excerpt quoted in the post:
Wait, let me redo this more carefully.

4,299,366,105,622
6,088,794,067,970
...
Adding from right to left:
Position 1 (units): 2 + 0 = 2
Position 2 (tens): 2 + 7 = 9
Position 3 (hundreds): 6 + 9 = 15, write 5, carry 1
```

## Cross-References

- **Corroborates**: `blog-simonwillison-qwen38-27b-overthinking.md` Claim 3 (reasoning off is faster but lower quality on the SVG prompt) and Claim 7 (bounding-box task failed without reasoning, worked with it). This post adds a quantitative reasoning-off failure on a deterministic task. Together they suggest reasoning-off Qwen 3.8 trades correctness on precise tasks for speed.
- **Contradicts**: None. Claim 5 of `blog-simonwillison-qwen38-27b-overthinking.md` advises trying low or no reasoning first; this post is a caveat on that advice for exact-computation tasks rather than a disagreement (a conditioning variable, so no contradiction issue filed).
- **Extends**: `blog-simonwillison-qwen38-27b-overthinking.md` (same model; adds a measured accuracy contrast). Same-author, same-style agent-run local experiment as `blog-simonwillison-astra-pelican-comparison-grid.md`, which is a different topic.
- **Novel**: No existing note records an arithmetic-reliability measurement (searching the corpus found only incidental mentions of arithmetic/calculators), nor an accuracy-vs-length curve for a non-reasoning model.

## Guide Impact

- **Chapter 03 (verification)**: Optionally add this as a small supporting data point under "don't trust fluent output for exact computation": a format-compliant 96% vs 23.6% correct contrast shows format validation is not correctness validation. Low weight: single model, single author.
- **Chapter 02 (harness)**: Weak support for routing exact computation to deterministic tools; note the post does not itself test tools.
- **Chapter 04 (context/reasoning budget)**: Possible caveat to "use low or no reasoning" advice: for tasks requiring exact multi-step computation, reasoning-off accuracy can collapse with input size.
- No recommendation to restructure any chapter; novelty is low.

## Extraction Notes

- The page is short; read in full. The linked report with reasoning traces and the heatmap images were not available as page text, so per-cell data and the Frasier GPT-4o chart are not captured. The post's top summary appears to be LLM-generated (Willison's usual feature); numbers were taken from it and are consistent with the body (169 cases, 30 vs 1 sample).
- "medium" reasoning appears only in the summary, not the body.
- Cross-reference claim numbers were checked against headings in the cited note.
