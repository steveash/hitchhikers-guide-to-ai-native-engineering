---
source_url: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
source_type: blog-post
title: "Qwen 3.8 27B on my laptop can interpret model weights, too"
author: Simon Willison
date_published: 2026-11-03
date_extracted: 2026-11-04
last_checked: 2026-11-04
status: current
confidence_overall: anecdotal
issue: "#4510"
---

# Qwen 3.8 27B on my laptop can interpret model weights, too

> Willison reruns the "which game was this policy network trained on?" no-tools prompt from the Sparks of Weight-Space Programming paper on a local 27B model: 3 of 4 games identified in 46–65 minutes each, one single-run data point that also separates "reading weights without tools" from "editing weights with tools".

## Source Context

- **Type**: blog-post (simonwillison.net; experiment report on a companion paper)
- **Author credibility**: Simon Willison is a trusted-feed author (creator of the `llm` CLI and Datasette); results are first-hand runs with linked transcripts.
- **Scope**: Only the paper's first experiment (identify the game from raw weights, no tools), run once per game on Qwen 3.8 27B (three of four games) plus one Kimi K3.1 Pro run. Does NOT test the paper's GPT-6 Astra weight-editing claims.

## Extracted Claims

### Claim 1: The paper's headline claim bundles two separate questions: what models can do with raw weights without tools, and what they can do to improve other models once armed with code
- **Evidence**: Author's framing, plus two critics he cites (spaCy author Matthew Honnibal; Sean Goedecke, who deconstructed the Qwen3.5-0.8B example).
- **Confidence**: emerging
- **Quote**: "The paper combines two topics that I think deserve to be treated separately."
- **Our assessment**: A sound methodological point: capability claims should name which tools were available. Critics are cited secondhand; we did not read them.

### Claim 2: The paper reports GPT-6 Astra can identify a network's task from raw weights and edit 0.016% of Qwen3.5-0.8B's weights to lift MATH-500 from 7.9% to 48.1%
- **Evidence**: Quoted from the paper's abstract; not tested by Willison.
- **Confidence**: anecdotal (vendor/paper claim, unreplicated here)
- **Quote**: "this weight correction raises MATH-500 from 7.9% to 48.1% and generalizes out of the box to instruction following, raising IFEval by 3x."
- **Our assessment**: Treat as an unverified claim. Willison explicitly leaves it unexamined, and Goedecke's critique (per Willison) is that the edit followed steps a human ML researcher would take.

### Claim 3: Qwen 3.8 27B on a laptop identified Pac-Man-style gameplay from raw weights after 46m 12s and 43,506 reasoning tokens, at self-reported 72% confidence
- **Evidence**: Single run via LM Studio and `llm`; linked reasoning trace.
- **Confidence**: anecdotal
- **Quote**: "After 46m 12s and 43,506 reasoning tokens, Qwen on my laptop returned a response that ended like this"
- **Our assessment**: Real data point, but n=1. The model's answer describes "an 8x8 maze" while the prompt refers to a 10x10 grid per Willison's description of the paper, so the description is only partly right; the game name was what was scored.

### Claim 4: Qwen also identified Pong (75%, 1h 4m 54s) and Breakout (88%, 52m 25s), but failed Freeway, calling it a "Pac-Man-like grid game"
- **Evidence**: Linked transcripts; Willison attributes the failure to Freeway being more obscure.
- **Confidence**: anecdotal
- **Quote**: "Qwen failed at the Freeway prompt, which didn’t surprise me considering that game is more obscure than the other three."
- **Our assessment**: 3/4 with one sample each cannot support reliability claims. Self-reported confidence (72–88%) was given on both the right and, presumably, wrong answers; calibration is not assessed. The obscurity explanation is the author's guess.

### Claim 5: A frontier hosted model (Kimi K3.1 Pro) solved Breakout about 5x faster with fewer reasoning tokens than local Qwen
- **Evidence**: One OpenRouter run: 9m 41s, 19,493 reasoning tokens vs Qwen Breakout 52m 25s.
- **Confidence**: anecdotal
- **Quote**: "which successfully guessed Breakout after 9m 41s and 19,493 reasoning tokens."
- **Our assessment**: Not like-for-like (different hardware/serving); the token counts are the more comparable figure. Reinforces the local-model time cost in [[blog-simonwillison-qwen38-27b-overthinking]].

### Claim 6: The reasoning traces are largely incomprehensible, so the correct answer is not accompanied by an inspectable explanation
- **Evidence**: A quoted trace excerpt of row/col/channel index bookkeeping.
- **Confidence**: anecdotal
- **Quote**: "The reasoning traces are fun to skim, and almost incomprehensible."
- **Our assessment**: Relevant to verification: a correct final answer from an opaque trace is hard to audit.

### Claim 7: The result may not require model capability beyond patience; a human with pencil and paper might get there
- **Evidence**: Author's opinion.
- **Confidence**: anecdotal
- **Quote**: "That said though, I expect a sufficiently experienced human being armed with a notepad and a pencil could get there with enough effort."
- **Our assessment**: Undercuts the "native weight reading" framing, but is untested speculation; the weights are text of floating-point numbers, so it is plausible.

### Claim 8: Wider commentary about the paper (end of source code, machines editing their own weights) is not justified by this evidence
- **Evidence**: Author's judgment.
- **Confidence**: emerging
- **Quote**: "I’m not ready to declare that the age of source code is over and our future involves incomprehensible machines editing their own model weights in incomprehensible ways."
- **Our assessment**: Appropriately cautious; consistent with the single-run, 3/4 evidence.

### Claim 9: Running the long prompt locally needs configuration beyond defaults: a long context window and a raised client timeout
- **Evidence**: Willison's setup notes.
- **Confidence**: anecdotal
- **Quote**: "the default 8192 context failed with errors"
- **Our assessment**: Practical failure symptom for local long-reasoning runs.

## Concrete Artifacts

```
# Source: Willison's post. Hosted control run (needs llm-openrouter)
llm -f https://raw.githubusercontent.com/RikiyaT/lm_understand-logs/refs/heads/main/exp1_which_game/runs/breakout/prompt.txt \
  -m openrouter/moonshotai/kimi-k3.1-pro

# Local run (needs llm-lmstudio, long context loaded in LM Studio)
LMSTUDIO_TIMEOUT=900 \
  llm -f https://raw.githubusercontent.com/RikiyaT/lm_understand-logs/refs/heads/main/exp1_which_game/runs/pacman/prompt.txt \
  -m lmstudio/qwen/qwen3.8-27b
```

| Game | Result | Confidence | Time |
|---|---|---|---|
| Pac-Man | identified | 72% | 46m 12s (43,506 reasoning tokens) |
| Pong | identified | 75% | 1h 4m 54s |
| Breakout | identified | 88% | 52m 25s |
| Freeway | failed (said Pac-Man-like) | n/a | not reported |
| Breakout (Kimi K3.1 Pro) | identified | n/a | 9m 41s (19,493 reasoning tokens) |

## Cross-References

- **Corroborates**: [[blog-simonwillison-qwen38-27b-overthinking]] (Claim 2, Claim 9): same model's long local reasoning runs and slow local throughput.
- **Contradicts**: none found.
- **Extends**: [[blog-simonwillison-qwen38-27b-overthinking]] (Concrete Artifacts / general local-run setup) by adding a non-coding, long-context task; [[blog-simonwillison-astra-pelican-comparison-grid]] covers Astra capability claims of a different kind (pelican SVGs), not weights.
- **Novel**: The Sparks of Weight-Space Programming paper and the no-tools vs tool-assisted distinction; no existing note covers LLMs reading raw weights.

## Guide Impact

- **Chapter 03**: Possible short example in verification discussion: a capability claim should state tool access, sample size, and be reproduced independently (Willison reproduced one sub-experiment, n=1 per game). Evidence is thin; illustrative only.
- **Chapter 00**: Optional illustration of separating what a model can do from broader narratives built on it (Claims 1, 8).
- No change recommended to workflow chapters.

## Extraction Notes

- Read the full post (fetched HTML). Did not follow the paper, repo, or the Honnibal/Goedecke critiques; their content is reported only as Willison describes it.
- Per the triage guidance, the Astra MATH-500 result is recorded as an unverified paper claim, not established.
- Post is short; claims are limited to what it contains.
