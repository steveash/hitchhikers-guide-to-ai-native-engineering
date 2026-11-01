---
source_url: https://vercel.com/blog/jev-for-python-engineers
source_type: blog-post
title: "Jev for Python engineers"
author: Yury Selivanov
date_published: 2026-10-02
date_extracted: 2026-11-01
last_checked: 2026-11-01
status: current
confidence_overall: anecdotal
issue: "#4476"
---

# Jev for Python engineers

> Vercel's Python team ships an experimental `evaluate()` API for Jev in the AI SDK for Python, and the author reports two experiments: a successful-ish Python-vs-English classifier and a failed attempt to make Jev generate Python code via AST choices.

## Source Context

- **Type**: blog-post (vendor first-party SDK announcement)
- **Author credibility**: Yury Selivanov, Director of Engineering at Vercel (byline in the post); runs the Python team that builds the SDK. Vendor-authored, so promotional incentives apply, but the post is unusually candid about negative results.
- **Scope**: Covers the `evaluate()` API surface, a Python-vs-English classification trace, and a generation experiment. No quantitative metrics, no benchmarks, no comparison against a text LLM baseline. Does not explain how Jev is built.

## Extracted Claims

### Claim 1: Jev is a "universal classifier" built from an LLM that needs no per-task training
- **Evidence**: Author's explanatory framing (ELI5 section); no measurements.
- **Confidence**: emerging
- **Quote**: "Jev is a universal classifier."
- **Our assessment**: Succinct framing consistent with other Jev notes ("decision model", "System 1"). Vendor framing; the zero-training claim is what distinguishes it from classic classifiers, but accuracy per task is not shown.

### Claim 2: Jev behaves like a classifier: cheap, fast, structured JSON output conforming to user-defined types
- **Evidence**: Assertion by the author; no latency or cost numbers in this post.
- **Confidence**: emerging
- **Quote**: "It's cheap and fast, and it returns structured JSON instead of generating text."
- **Our assessment**: Consistent with Willison's pricing datum (see Cross-References), but this post gives no numbers of its own.

### Claim 3: The whole API is one function, `evaluate(model, state, questions)`, with three question types
- **Evidence**: API description plus a complete runnable example (see Concrete Artifacts).
- **Confidence**: settled (for the SDK as of the post date; the API is labelled experimental)
- **Quote**: "There's just one function, evaluate(), and a few supporting types."
- **Our assessment**: The question types are `ChoiceQuestion` (choose one answer), `ScoreQuestion` (rate on a user-defined scale) and `NoulQuestion` (estimate probability a statement is true). State may be a string or complex JSON. This is an SDK-specific surface under `ai.ops.experimental`, not a stable spec.

### Claim 4: A hand-rolled classifier for Python-vs-English was jittery and the author gave up; Jev does "much better" but still has gaps
- **Evidence**: Author's two-day attempt anecdote and interactive keystroke traces on the page (e.g. `if i` / `if i i` / `if i is` flipping). No accuracy numbers.
- **Confidence**: anecdotal
- **Quote**: "While it does seem to fare much better than my hand-rolled classifier did, it still has gaps."
- **Our assessment**: A real, relevant use case (routing between chat and code in a REPL) with a qualitative result. "Seems" signals no formal evaluation.

### Claim 5: Jev misclassifies partially typed Python (`"what's" + " up` reads as English)
- **Evidence**: Single concrete failure example in the trace.
- **Confidence**: anecdotal
- **Quote**: "For example, \"what's\" + \" up looks like English to Jev, while it's quite obvious to me that it's a partially typed Python expression."
- **Our assessment**: Illustrates that single-shot classification of incomplete input is brittle; fits Latent Space's "single-hop" limitation (Claim 12 there) only loosely. Useful concrete failure mode for a decision-model eval set.

### Claim 6: Character-by-character or keyword-level generation via Jev fails
- **Evidence**: Author's first attempt (letters + Python keywords + whitespace); qualitative.
- **Confidence**: anecdotal
- **Quote**: "Jev could barely type an if statement that way."
- **Our assessment**: Negative result for using Choice questions as a next-token substitute. Contrasts with community hacks that emulate chat/left-pad this way (Willison Claim 11), which were novelty demos rather than quality claims.

### Claim 7: Even AST-node-by-node choice generation yields valid but mostly incorrect code
- **Evidence**: Second attempt, with a GPT-5.6-expanded plan; source code on GitHub (not read). No pass rates.
- **Confidence**: anecdotal
- **Quote**: "I did get Jev to generate syntactically valid (yet still mostly incorrect) Python code using this approach."
- **Our assessment**: Constraining outputs to a grammar guarantees syntax, not semantics; the author's own conclusion is that classifiers doing an LLM's job is hard. Single author, single task, no metrics.

### Claim 8: Without a detailed plan from a stronger LLM, Jev fails even elementary tasks
- **Evidence**: Author's observation during the AST experiment. Page shows prompt "recursive fibonacci" expanded by GPT-5.6 into precise instructions.
- **Confidence**: anecdotal
- **Quote**: "I found that without a detailed \"plan\", Jev struggles to implement even elementary tasks."
- **Our assessment**: Supports a planner (LLM) / executor (decision model) split, but the experiment's overall failure means this is not evidence the pattern works, only that Jev needs it. Notably, the traced output still misspelled the function name (`fibonacio`) despite the instruction to spell names in full.

### Claim 9: Division of labor: host code handles syntax, the model only decides structure and content
- **Evidence**: Description of the AST harness.
- **Confidence**: emerging
- **Quote**: "The host code handles punctuation and indentation; Jev decides the program's overall structure and contents."
- **Our assessment**: A reusable harness pattern: deterministic code owns everything it can, each model call is a bounded choice with previews of each option's rendered output. Pattern is sound even though the outcome here was poor.

### Claim 10: The author warns Jev errs and accuracy must be tested per use case
- **Evidence**: Explicit caveat in the intro; reinforced in the conclusion.
- **Confidence**: settled (as author's stated position)
- **Quote**: "Jev is built for making narrow decisions. Whether it's accurate enough for your use cases is something you'll need to test."
- **Our assessment**: Strong, honest vendor caveat; aligns with Latent Space's rejection of public benchmarks (Claim 10 there) and Willison's eval emphasis.

## Concrete Artifacts

Complete example from the post (formatting reconstructed from the page's line-numbered code block):

```python
import asyncio

import ai
from ai.ops import experimental as jev

async def main():
    result = await jev.evaluate(
        ai.get_model("typesafe-ai/jev"),
        "You're Neil deGrasse Tyson",
        {"bigger": jev.ChoiceQuestion(
            instructions="Which is bigger, the Sun or the Earth?",
            criteria={"Sun": None, "Earth": None},
        )},
    )
    print(result.value["bigger"])

if __name__ == "__main__":
    asyncio.run(main())
```

Setup (from the post): `uv add ai`, create an AI Gateway key, set `AI_GATEWAY_API_KEY`.

AST-generation loop (author's description, condensed): (1) an LLM (GPT-5.6) expands the user prompt into concrete instructions; (2) show Jev the current program, mark the field being filled, offer possible next nodes (function call, arithmetic, variable) each with a code preview; (3) apply the choice to the tree, render back to Python; repeat until Jev picks "end".

Trace shown on the page for prompt "recursive fibonacci": expanded prompt specified a function named `fibonacci` with parameter `number`; the rendered output was `def fibonacio(n):` with `if n <= 1: return n` and `else: return fibonacio(n - 1) + fibonacio(n - 2)`; a step shows "Choices (7)", "Confidence 76%", "end 80%", "FunctionDef 19%".

The post also includes a copy-paste "Prompt for coding agents" for building a REPL playground that prints choice, probabilities, confidence and latency per line.

## Cross-References

- **Corroborates**: `blog-simonwillison-jev-decision-models.md` Claim 4 (three question types incl. Choice/Score/Noul) and Claim 6 (Jev weak in some areas; vendor admits jaggedness). `blog-latentspace-jev-system-one-for-prod.md` Claim 10 (evaluate on your own workflow, not public benchmarks) agrees with this post's "you'll need to test" caveat.
- **Contradicts**: None found. The Latent Space and Thoughtworks notes pitch Jev for evaluative/decision tasks (e.g. Thoughtworks Claim 5, guardrail on agent-produced code), which this post's negative generation result does not oppose; it marks the boundary.
- **Extends**: `blog-simonwillison-jev-decision-models.md` Claim 11 (community hacks like jevchat that emulate generation with Choice questions): this post gives a first-party attempt at that idea and reports it works poorly. `blog-latentspace-jev-system-one-for-prod.md` Claim 12 (single-hop tool; System 1/System 2 boundary is empirical) gets a concrete data point at the boundary. `blog-thoughtworks-mugrage-jev-decision-models-what-to-know.md` Claim 3 (constrained capability suits rapid evaluation) is supported by the failure of the opposite use.
- **Novel**: The Python AI SDK `evaluate()` surface and gateway model id `typesafe-ai/jev`; the grammar-constrained AST-by-choice generation harness and its negative result; the LLM-plans / Jev-executes split (Claim 8); the Python-vs-English partial-input failure.

## Guide Impact

- **Ch02 (harness engineering)**: If the guide discusses decision models as routing/classification steps, add the boundary evidence: using a classifier-style model as a generator (even grammar-constrained) produced "syntactically valid (yet still mostly incorrect)" output. Cite as anecdotal, single vendor author. Optionally note the pattern "deterministic host renders, model chooses among previewed options".
- **Ch03 (verification)**: Add the Python-vs-English partial-input failure as an example of why decision-model classifiers need an eval set including incomplete/ambiguous inputs. Cite the author's "you'll need to test" caveat.
- **Ch04 (context engineering)**: Weak evidence only: an LLM-expanded plan was necessary for Jev to perform. Hold until corroborated.

## Extraction Notes

- Read the full post via raw HTML of the source URL (WebFetch returned only a summary, so quotes were taken from the raw HTML text). Interactive widget text (traces) appears in the page source and was used for the artifacts above; trace numbers are as rendered, without independent verification.
- Did not follow the GitHub repository for the AST experiment or the SDK reference docs (ai-python.dev); the API summary rests on the post.
- No contradictions filed: the post's negative result is compatible with the existing Jev notes.
