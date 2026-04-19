---
source_url: https://cursor.com/blog/self-summarization
source_type: blog-post
title: "Training Composer for Longer Horizons"
author: "Federico Cassano & Sasha Rush (Cursor Research)"
date_published: 2026-03-17
date_extracted: 2026-04-19
last_checked: 2026-04-19
status: current
confidence_overall: emerging
issue: "#162"
---

# Training Composer for Longer Horizons (Cursor Research)

> Cursor's research team shows that training a model to self-summarize *inside*
> the RL training loop produces context compression that is 5× more token-efficient
> and 50% less error-prone than the best prompt-engineered harness baseline —
> fundamentally challenging the assumption that context compaction is a harness
> engineering problem.

## Source Context

- **Type**: blog-post (engineering research write-up from Cursor)
- **Author credibility**: Federico Cassano and Sasha Rush are named Cursor researchers.
  Sasha Rush (Srush) is also a well-known ML researcher (Harvard NLP / Cornell Tech),
  which raises the evidential weight of the RL framing. This is a vendor blog post, so
  Cursor has an incentive to present Composer favorably; however, the specific numbers
  and the DOOM benchmark are concrete enough to be treated as real, albeit unaudited,
  evidence. The post links to Terminal-Bench 2.0 as an external benchmark.
- **Scope**: Covers the design and evaluation of a single training technique —
  self-summarization-in-the-loop — applied to Composer's RL training. Does NOT cover
  other Cursor products, the broader Cursor inference stack, or any harness-side
  changes. Does NOT provide source code or training details beyond what is described
  in the post.

## Extracted Claims

### Claim 1: Agent trajectories expand faster than context length, and all current mitigation strategies risk losing critical information
- **Evidence**: Authors categorize three families of approaches — text-space compaction (prompted summaries), sliding context windows, and latent-space methods — and assert all three share the same failure mode.
- **Confidence**: emerging
- **Quote**: "These techniques risk causing models to 'forget critical information from the context, reducing its efficacy as it advances through long-running tasks.'"
- **Our assessment**: This is the framing claim that motivates the whole paper. The failure mode is real and corroborated by failure-decker-4hr-session-loss (4 hours of architectural rationale gone after silent compaction) and research-wasnotwas-context-compaction (6/7 harnesses use lossy LLM-summary strategies). The Cursor team's proposed solution is to move compaction from an external harness responsibility into the model training itself.

### Claim 2: Self-summarization trained in-the-loop produces far better summaries than prompt-based approaches
- **Evidence**: Quantitative comparison against a "highly-tuned baseline" with ~12 carefully-worded prompt sections producing 5,000+ token summaries.
- **Confidence**: emerging (vendor benchmark; unaudited)
- **Quote**: "Trained self-summaries average ~1,000 tokens vs ~5,000+ tokens for a highly-tuned prompt-based baseline. Reduces compaction error by 50% compared to the baseline on CursorBench."
- **Our assessment**: The 50% error reduction is a striking claim on an internal benchmark (CursorBench), so treat it as directionally compelling rather than a settled number. The 5× token efficiency advantage is independently meaningful: smaller summaries mean less context consumed per compaction cycle, directly extending effective session length without additional training tricks.

### Claim 3: The self-summarization mechanism integrates into RL as a four-step in-trajectory loop
- **Evidence**: Authors describe the mechanism explicitly. The final reward signal spans all tokens in the summarization chain, making summarization quality a first-class RL objective.
- **Confidence**: emerging
- **Quote**: (no verbatim quote; the post describes the mechanism in prose)
- **Our assessment**: This is the core architectural claim. The key insight is that by including summaries inside the RL rollout — not as a separate supervised task — Composer learns compaction natively. The reward signal directly penalizes summaries that cause downstream task failures. This is structurally different from every approach in research-wasnotwas-context-compaction, where compaction is handled by an external model or fixed algorithm.

### Claim 4: The trained model's inference-time summarization requires only a minimal prompt, not a multi-section prompt template
- **Evidence**: Authors contrast the baseline (~12 carefully-worded sections, thousands of tokens of prompt) with Composer's inference trigger (~"Please summarize the conversation").
- **Confidence**: emerging
- **Quote**: "Prompt requirement: minimal instruction (~'Please summarize the conversation')"
- **Our assessment**: This is practically significant beyond the accuracy gains. Every harness in the wasnotwas study requires a carefully-maintained prompt template that must be updated as the model changes. Cursor's approach eliminates prompt maintenance cost entirely. If this generalizes, it shifts the engineering burden from "write a good compaction prompt" to "train a model that can compact."

### Claim 5: Self-summarization works at both 80k and 40k token trigger thresholds, with more frequent compaction still outperforming the baseline
- **Evidence**: Authors tested both trigger points.
- **Confidence**: emerging
- **Quote**: "Works across 40k and 80k trigger thresholds, with more frequent compaction (40k) still outperforming the baseline."
- **Our assessment**: The 40k trigger result is notable. Harnesses that trigger compaction early (Gemini CLI at 50% per research-wasnotwas-context-compaction) pay a quality cost because they compact more often, each time risking information loss. Cursor's result suggests that if compaction is accurate enough, triggering earlier is safe or even beneficial because context never gets dangerously long. This would resolve the trigger-threshold tradeoff the wasnotwas study identified.

### Claim 6: Self-generated summaries preserve KV cache across compaction events
- **Evidence**: Authors describe efficiency properties; "uses one-fifth of the tokens while reusing KV cache."
- **Confidence**: emerging
- **Quote**: "uses one-fifth of the tokens while reusing KV cache"
- **Our assessment**: This is a significant second-order gain. In harness-external compaction, the act of compaction destroys the KV cache (per research-wasnotwas-context-compaction Claim 2: $0.40 per compaction, ~21 turns of cached throughput burned). If Cursor's self-summarization genuinely preserves the KV cache, it avoids both the token overhead AND the cache-busting cost. Mechanism is not explained in the post and should be treated cautiously — the cache-preservation claim deserves independent verification.

### Claim 7: The DOOM benchmark demonstrates compaction preserving actionable technical detail across 170 turns
- **Evidence**: Terminal-Bench 2.0 "make-doom-for-mips" challenge — build a MIPS little-endian ELF executable running DOOM in a JavaScript VM. Authors provide the actual self-generated summary text as evidence.
- **Confidence**: emerging (one benchmark, vendor-selected for publication)
- **Quote**: "Composer successfully solved this over 170 turns, compressing more than 100,000 tokens of working context down to approximately 1,000 tokens of preserved critical information."
- **Our assessment**: The DOOM case is the most credible piece of evidence in the post because the problem is well-specified, the benchmark is external (Terminal-Bench 2.0), and Cursor publishes the actual summary text. The summary includes specific syscall numbers, memory allocation strategies, and compilation flags — exactly the kind of architectural "why" that decker reported losing in the failure-decker-4hr-session-loss case. This is the strongest concrete evidence that trained compaction preserves the information that prompt-based compaction loses.

### Claim 8: Self-summarization is a stepping stone toward multi-agent and longer-horizon tasks
- **Evidence**: Authors' stated research direction.
- **Confidence**: anecdotal (forward-looking)
- **Quote**: "training Composer over even longer, more complex processes such as multi-agent coordination" and "better model training as improving the scope and intelligence of these agentic systems."
- **Our assessment**: Forward-looking framing, not current evidence. Worth noting for Ch02 (harness engineering) because it signals that Cursor's competitive strategy is to push the long-context problem down into the model rather than solve it at the harness level. This changes the harness engineering calculus: if models get native long-context capability, the complex compaction machinery in today's harnesses becomes technical debt.

### Claim 9: Trained compaction metadata is minimal — current plan state, remaining tasks, prior summarization count
- **Evidence**: Authors describe the inference-time tracking state.
- **Confidence**: emerging
- **Quote**: (paraphrased from post): For inference, Composer requires only a brief trigger prompt asking for summarization, plus metadata tracking: current plan state, remaining tasks, count of prior summarizations.
- **Our assessment**: The metadata list aligns with what practitioners recommend storing externally for survival through harness-level compaction (Osmani's SPEC.md, Sankalp's handoff pattern). The model has learned to track exactly the same state that expert practitioners maintain manually. Useful as evidence that the "what survives compaction" question has a principled answer, and that expert practitioner habits encode domain knowledge the model can learn.

## Concrete Artifacts

The post includes the actual self-generated summary from the DOOM benchmark (170-turn session, 100k+ tokens → ~1k tokens). Key elements preserved:

```
# Self-Generated Summary: make-doom-for-mips (170-turn session)

User goal:
  Build MIPS little-endian ELF executable running DOOM in a JavaScript VM.

Implementation details:
  - Custom libc construction (no standard C library available)
  - Build configuration for MIPS little-endian ELF
  - VM modifications to support DOOM execution environment

Error history and fixes:
  - Syscall issues: custom syscall numbers for JS VM (0=read, 1=write, 2=open, ...)
  - Linking problems: compilation flags -fno-pic -mno-abicalls to avoid GP-relative addressing
  - Memory allocation: Uint32Array buffers instead of plain objects (avoid V8 OOM)

Path references:
  - File locations for all components documented

Remaining work:
  - Debugging guidance for next iteration

[Source: Cursor blog post — self-generated summary excerpt]
```

Performance comparison (from post):

```
                    Baseline (prompt-engineered)    Composer (trained)
Compaction prompt   ~12 sections, thousands of      ~"Please summarize"
                    tokens                           (minimal)
Summary output      5,000+ tokens                   ~1,000 tokens
Token efficiency    1×                              ~5× (one-fifth)
Error rate          baseline                        50% reduction on CursorBench
KV cache            destroyed per compaction        preserved (claimed)
Trigger thresholds  n/a                             80k and 40k, both beat baseline
```

## Cross-References

- **Corroborates**: research-wasnotwas-context-compaction (the claim that prompt-based compaction is the industry default is confirmed; the 5,000-token baseline in this post is a real-world example of the "carefully-maintained prompt template" pattern the wasnotwas study describes for 6/7 harnesses)
- **Corroborates**: failure-decker-4hr-session-loss (the "architectural why is the first thing compaction destroys" failure is exactly the class of information the DOOM example shows trained compaction CAN preserve — syscall numbers, memory strategies, compilation flags are precisely the kind of non-obvious decisions that get flattened by prompt-based summarization)
- **Extends**: research-wasnotwas-context-compaction — that study covers only external/harness-side compaction strategies. This post introduces a fundamentally different axis: compaction as a *trained behavior* baked into the model via RL. The wasnotwas study maps the space of what current harnesses do; this post challenges whether harnesses should own the problem at all.
- **Extends**: blog-french-owen-coding-agents-feb-2026 (French-Owen's "smart half" heuristic — stay in the top 50% of context window — is a workaround for compaction quality loss. If trained compaction is accurate enough to trigger safely at 40k tokens, the "smart half" rule becomes less necessary. The Cursor result is a data point against the view that the only solution is to compact less often.)
- **Novel**: Model-trained context compaction as an RL objective is not described in any other source note. All existing notes treat compaction as an external harness mechanism. This is the first source showing that compaction quality can be substantially improved by training the model directly.

## Guide Impact

- **Chapter 04 (Context Engineering — compaction and session management)**: This source should be introduced as the next-state counterpoint to the harness-compaction discussion. After explaining why prompt-based compaction is lossy (wasnotwas, decker), note that Cursor has demonstrated a model-training approach that reduces error 50% and uses 5× fewer tokens. The immediate implication for practitioners: if you use Composer/Cursor, context compaction is substantially less lossy than on other harnesses. If you use Claude Code or other harnesses, the mitigation strategies (handoff patterns, plan files, proactive session limits) remain important.

- **Chapter 02 (Harness Engineering — know your compaction policy)**: Add a note on the emerging split between "harness-side compaction" (current default across all surveyed tools) and "model-side compaction" (Cursor's direction). Harness engineers building on top of Claude Code, Gemini CLI, etc. should design their compaction strategies knowing these are harness-external mechanisms with real quality limitations. Teams building future harnesses should watch whether model providers follow Cursor's approach.

- **Chapter 04 (Specs/plans as compressed context)**: The DOOM summary artifact is strong evidence for WHY the spec/plan pattern works: the self-generated summary preserves exactly the state that external plan files are designed to preserve (goal, implementation decisions, error history, remaining work). The guide can use this as the positive-case complement to the decker failure: "what good compaction looks like is what your SPEC.md should already contain."

- **Chapter 02 (Long-horizon and multi-agent tasks)**: Cite Claim 8 as evidence that the research direction in coding agents is toward model-native long-horizon capability, not harness-complexity. This shapes how the guide should frame Ch02 recommendations — invest in patterns that work both with current harness-external compaction AND will still be correct when models improve.

## Extraction Notes

- The post is authored by two people: Federico Cassano (Cursor engineering) and Sasha Rush (ML research background). Rush's presence raises the evidential weight for the RL framing — this is not just a marketing blog post.
- CursorBench is an internal benchmark. The 50% error reduction and comparison figures are not independently verified. The DOOM example is external (Terminal-Bench 2.0) and concrete; that's the strongest piece of evidence in the post.
- The KV-cache-preservation claim (Claim 6) is the one I'd most want verified. The wasnotwas study explicitly identified KV-cache destruction as the second-order cost of compaction ($0.40 equivalent to ~21 cached turns). If Cursor's approach genuinely preserves the cache, that resolves a major cost concern. The mechanism isn't explained — it's asserted. Flag for independent verification before the guide cites it.
- The post does not include training details, data, or code. It is a research preview, not a methods paper. Treat the quantitative claims as directional and vendor-incentivized.
- An "upcoming version of Composer" is mentioned as forthcoming. The post may age quickly if follow-on releases change the performance profile. `last_checked` should be updated with each Cursor release.
