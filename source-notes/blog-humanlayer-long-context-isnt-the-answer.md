---
source_url: https://www.humanlayer.dev/blog/long-context-isnt-the-answer
source_type: blog-post
title: "Long-Context Isn't the Answer"
author: "Kyle (HumanLayer)"
date_published: 2026-03-23
date_extracted: 2026-07-13
last_checked: 2026-07-13
status: current
confidence_overall: emerging
issue: "#1822"
---

# Long-Context Isn't the Answer

> HumanLayer's production experience switching Claude Code's default model to Opus 4.6
> (1M context) and back to Opus 4.5 (~200k) after observing dramatically degraded
> instruction adherence — introducing the "instruction budget" concept (a model's fixed
> capacity to follow instructions reliably, which does not scale with context window size)
> and recommending context isolation via sub-agents over context expansion.

## Source Context

- **Type**: blog-post (practitioner production experience report from an agentic
  coding-tools company)
- **Author credibility**: Kyle, writing for HumanLayer, a company building agentic
  coding/human-in-the-loop tooling. This is first-party production experience with
  Claude Code model defaults, not a controlled benchmark study — the team observed the
  behavior "over the course of a couple of weeks" of real usage before reverting models.
  The article cites at least one external research paper (arxiv.org/pdf/2507.11538, on
  instruction-following capacity scaling with model size) and references YaRN
  (arxiv.org/pdf/2309.00071) as the general technique class for context-length extension,
  giving the practitioner narrative some grounding in published research, though the
  specific Opus 4.6 vs. 4.5 comparison itself is anecdotal/internal.
- **Scope**: Covers instruction adherence degradation observed with a 1M-context model in
  Claude Code, the "instruction budget" concept (previously introduced in an earlier
  HumanLayer post, "Skill issue: harness engineering for coding agents" — see
  Cross-References), a "needle in a haystack" framing for instruction-following within a
  context window, and HumanLayer's own remediation (context isolation via sub-agents,
  progressive disclosure, context-efficient backpressure; lowering their context-warning
  threshold to 100k tokens for long-context models). Does NOT cover: controlled
  quantitative benchmarks of Opus 4.6 vs. 4.5 (the comparison is qualitative/experiential),
  other vendors' long-context models, or a full description of their sub-agent
  architecture (that lives in the referenced companion posts).

## Extracted Claims

### Claim 1: HumanLayer adopted Opus 4.6 (1M context window) as Claude Code's new default when it launched, then reverted to Opus 4.5 after finding it worse in production

- **Evidence**: First-party account of an internal model-adoption decision and reversal.
- **Confidence**: anecdotal
- **Quote**: "Anthropic just switched the default model in Claude Code to Opus 4.6 with a 1M context window. We tried it when it launched. But now we're switching back to Opus 4.5"
- **Our assessment**: A concrete, named reversal decision by a production agentic-tooling
  team is high-signal even without a controlled benchmark — teams don't revert a default
  model lightly. This is the article's load-bearing anecdote; every other claim in the
  piece is offered as the explanation for this one decision.

### Claim 2: Instruction adherence was dramatically degraded with the larger-context model, not only at long context lengths but broadly across usage

- **Evidence**: First-party observation over "a couple of weeks" of production use.
- **Confidence**: anecdotal
- **Quote**: "While the context window is dramatically larger, we noticed over the course of a couple of weeks that instruction adherence was dramatically degraded, not just at longer context lengths."
- **Our assessment**: The "not just at longer context lengths" qualifier is the important
  part — it rules out the simpler explanation that quality only drops as the window fills
  up. If true, it means the degradation is a property of the model/context-extension
  technique itself, not merely a symptom of running long sessions. This directly motivates
  the "instruction budget" framing in Claim 4.

### Claim 3: Concrete failure symptoms included ignoring design documents when writing plan files and disobeying simple explicit instructions

- **Evidence**: First-party specific failure examples from production usage.
- **Confidence**: anecdotal
- **Quote**: "It would ignore design documents and other inputs when writing a plan file."
- **Our assessment**: This is a specific, checkable failure mode (design docs excluded
  from plan generation) rather than a vague "it felt worse" impression, which raises the
  evidentiary value above a pure gut-feel anecdote. The corresponding second symptom —
  "It would make trivial mistakes, or misunderstand simple instructions - or worse,
  directly disobey them" — describes graduated failure severity from misunderstanding to
  outright disobedience.

### Claim 4: The "instruction budget" is a measurable property of an LLM describing how many instructions it can follow reasonably well before adherence drops off, and this budget does not scale with a larger context window

- **Evidence**: Concept introduced in an earlier HumanLayer post and restated/applied here;
  presented as the causal explanation for Claims 1–3.
- **Confidence**: emerging
- **Quote**: "We've written about the concept of the instruction budget before - a measurable property of LLMs which describes how many instructions they can follow reasonably well before instruction adherence drops off."
- **Our assessment**: This is the article's central theoretical contribution. It reframes
  "context window size" and "instruction-following capacity" as two independent
  properties of a model rather than one scaling with the other. If a lab extends sequence
  length without a proportional increase in instruction budget, then shipping a bigger
  window is not a strict quality upgrade — it's a trade that can net negative for
  instruction-heavy agentic workloads. The "measurable" framing implies HumanLayer
  believes this is empirically testable, though this article itself doesn't publish a
  benchmark quantifying the budget for Opus 4.5 vs. 4.6.

### Claim 5: Techniques that extend a model's usable context length (e.g., YaRN) extend sequence length the model can attend to without necessarily increasing the model's instruction-following capacity, and typically involve post-training to stabilize the model at the new length

- **Evidence**: General technical claim about how context-extension techniques work,
  citing YaRN (arxiv.org/pdf/2309.00071) as the example technique class.
- **Confidence**: emerging
- **Quote**: "you're likely getting the same model with some clever math (e.g. YaRN) to extend the sequence length the model can attend to, and probably some more post-training to stabilize the model at the longer sequence lengths."
- **Our assessment**: This is the mechanistic bridge between Claim 1 (Opus 4.6 got worse)
  and Claim 4 (instruction budget is fixed): if a 1M-context variant is fundamentally
  "the same model" with sequence-length-extension math applied on top, it's plausible
  that its instruction-following capacity was inherited unchanged from the base model
  rather than re-trained upward alongside the window expansion. HumanLayer doesn't claim
  to know Anthropic's exact training recipe for Opus 4.6 — this is offered as the likely
  general mechanism, not a confirmed fact about that specific model.

### Claim 6: A cited research paper (arxiv.org/pdf/2507.11538) found that larger models can follow substantially more instructions before their adherence drops, compared to smaller models

- **Evidence**: External academic citation, relayed by the article.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment — the article references the paper's finding without a standalone quotable sentence distinct from its own instruction-budget framing)
- **Our assessment**: This citation supports the instruction-budget concept's premise
  (that instruction-following capacity is a real, measurable, model-dependent quantity)
  but does not itself test context-window-extension techniques like YaRN — it appears to
  be about model *size* (parameter count) rather than context *length*. HumanLayer is
  using it as supporting evidence for the general concept, not as a direct study of the
  Opus 4.5/4.6 comparison. Treat as background support, not a controlled test of this
  article's central claim.

### Claim 7: Instruction-following can be framed as a "needle in a haystack" problem — the context window is a haystack of tool calls, documents, files, and instructions, and the model's next-step quality depends on its ability to locate the most-relevant instruction within that haystack

- **Evidence**: Author's own analogy, offered as the connecting mental model between
  context size and instruction adherence.
- **Confidence**: anecdotal
- **Quote**: "You can think of your context window as a haystack where all of your tool calls and documents and files are hay - every line in your CLAUDE.md file, every instruction in your tool descriptions, every tool result, every instruction in your system prompt, and every user message."
- **Our assessment**: This reframes the classic "needle in a haystack" retrieval-benchmark
  metaphor (usually used to test whether a model can find a fact buried in a long
  context) as an *instruction-following* problem instead of a *fact-retrieval* problem.
  That's a meaningful shift: it implies that even models with excellent long-context
  retrieval on standard needle-in-haystack benchmarks could still fail at "which
  instruction applies right now" if the instructions themselves are diluted by growing
  volumes of tool output and file content. This is presented as an analogy rather than a
  tested claim, but it's a genuinely useful reframing not present elsewhere in the corpus.

### Claim 8: Context isolation (sub-agents, progressive disclosure, context-efficient backpressure) beats context expansion for keeping a model within its effective operating range ("smart zone")

- **Evidence**: Author's prescriptive recommendation, presented as HumanLayer's own
  design philosophy and the article's central "what works instead" answer.
- **Confidence**: emerging
- **Quote**: "Context isolation beats context expansion. Sub-agents, progressive disclosure, and context-efficient backpressure keep each context window small, focused, and in the smart zone."
- **Our assessment**: This is the article's actionable takeaway and matches a pattern
  already well-represented in the corpus (see Cross-References) — using sub-agents to
  keep individual context windows small rather than relying on a larger window to hold
  everything. What's new here is the specific justification: not "large contexts are
  slow/expensive" (the usual argument) but "large contexts specifically degrade
  instruction-following, independent of cost or latency." The "smart zone" term itself is
  used but not rigorously defined within this article (it references a companion video);
  practitioners should treat it as a qualitative zone, not a specific token count.

### Claim 9: Even well within what HumanLayer considers the "smart zone" of a 200k-context frontier model, the model was less precise

- **Evidence**: First-party observation contrasting behavior within a presumed-safe
  operating range against the larger model's behavior.
- **Confidence**: anecdotal
- **Quote**: "Even well-within what we would consider the smart zone of a 200k-context frontier model, the model was less precise."
- **Our assessment**: This sharpens Claim 2 — the degradation wasn't observed only near
  the edge of the (much larger) 1M window, but at absolute token counts that would have
  been comfortably "safe" under the older 200k-window model's own operating norms. This
  is the strongest single piece of evidence in the article for "bigger window, worse
  behavior at the same absolute context size," though it remains a qualitative
  observation rather than a quantified comparison.

### Claim 10: HumanLayer lowered its context-warning threshold for long-context models to trigger at 100k tokens, replacing a prior threshold set around 40% of the usable window

- **Evidence**: First-party description of an actual product/policy change made in
  response to the observed degradation.
- **Confidence**: settled (as a factual description of HumanLayer's own product change,
  not as a general prescription for other teams' thresholds)
- **Quote**: "We've updated our context warnings for long-context models to trigger at the 100k token mark instead of 40% of the usable context."
- **Our assessment**: This is the article's single most concrete, adoptable artifact — a
  specific number (100k tokens) that HumanLayer now treats as an absolute ceiling for
  "safe" instruction adherence, replacing a percentage-of-window-based threshold. The
  shift from a *relative* threshold (40% of window) to an *absolute* one (100k tokens
  regardless of total window size) is itself evidence for the instruction-budget thesis:
  if the safe operating point scaled with window size, a percentage-based threshold would
  still make sense; switching to an absolute number implies HumanLayer now believes the
  safe zone is a property of the model's instruction budget, not a fraction of whatever
  window it happens to have.

## Concrete Artifacts

### HumanLayer's TL;DR (verbatim, three-point summary from the article's closing section)

```
"Long-context models degrade at all context lengths, not just long ones."
"More context isn't more capability - the instruction budget doesn't scale with the context window."
"Context isolation beats context expansion. Sub-agents, progressive disclosure, and
context-efficient backpressure keep each context window small, focused, and in the smart zone."

Source: https://www.humanlayer.dev/blog/long-context-isnt-the-answer
```

### Context-warning threshold change (verbatim)

```
"We've updated our context warnings for long-context models to trigger at the 100k
token mark instead of 40% of the usable context."

For a 168k-token Sonnet window, the prior 40% threshold worked out to roughly 67k
tokens; for a 1M-token Opus window, the same 40% rule would allow ~400k tokens before
warning. HumanLayer replaced this relative threshold with a flat 100k-token absolute
ceiling for long-context models.

Source: https://www.humanlayer.dev/blog/long-context-isnt-the-answer
```

### Section structure of the article (for navigation / re-reading)

```
1. Long-Context Isn't the Answer (title/intro)
2. How about some context?
3. More context, less instruction adherence
4. What determines instruction adherence?
5. Instruction adherence at long context lengths
6. Instruction-following as needle in a haystack
7. What Works Instead
8. How we're incorporating this at HumanLayer
9. TL;DR
```

## Cross-References

- **Contradicts**: `blog-anthropic-session-management-1m-context.md` (Claim 9, Claim 12) —
  Anthropic's first-party post frames Claude Code's 1M-token context window as a
  straightforward capability upgrade ("With one million context, you have more time to
  /compact proactively"), while this source reports the same underlying capability
  (a 1M-context Claude Code default) degrading instruction adherence badly enough to
  revert to the smaller-window model. **Filed as contradiction issue #1832** — see that
  issue for the full Side A / Side B breakdown. Do not present the 1M context window as
  an unqualified upgrade in the guide until this is resolved; the resolver should decide
  whether to present this as "settled feature, contested real-world performance" or pick
  a side.

- **Corroborates**: `docs-github-copilot-1m-context-reasoning-levels.md` — that source
  documents GitHub Copilot also shipping a 1M-token context window (announced June 2026),
  framed purely as a capability expansion ("work across larger codebases... without
  losing context") with no mention of instruction-adherence trade-offs. This source
  doesn't directly test Copilot, but it suggests the guide should flag that *any*
  1M-context-window announcement (not just Anthropic's) should be read skeptically for
  instruction-adherence trade-offs until vendors publish adherence data alongside window
  size — the corpus currently has product announcements praising window size but no
  vendor-published adherence benchmarks at all.

- **Extends**: `research-wasnotwas-context-compaction.md` — that note provides
  quantitative compaction-trigger thresholds and cost data across seven coding-agent
  harnesses, but is about *when compaction fires*, not about *instruction-following
  quality before compaction fires*. This source adds a distinct, earlier-onset quality
  concern: degradation can occur well before any compaction-trigger threshold is reached,
  motivating proactive context management even in a session nowhere near "full."

- **Extends**: `failure-claudemd-ignored-compaction.md` — that note documents CLAUDE.md
  instructions being systematically deprioritized/ignored, especially after compaction,
  attributing much of the effect to compaction summarization dropping rules. This source
  offers a complementary and partially distinct mechanism for the same broad symptom
  (instructions not followed): a fixed instruction budget that gets diluted by growing
  context even without compaction ever firing. Together they suggest CLAUDE.md/instruction
  non-adherence has at least two independent causes — compaction summarization loss, and
  budget dilution from context volume — that compound in long sessions.

- **Extends**: `docs-ghaw-inline-sub-agents.md` — that note documents gh-aw's mechanism
  for composing sub-agents inline within a workflow file. This source provides the
  motivating rationale (instruction-budget preservation, not just cost/latency) for why
  a team would reach for sub-agent composition patterns like gh-aw's in the first place.

- **Novel**: (1) The "instruction budget" concept as a property distinct from context
  window size — not present elsewhere in the corpus under this name. (2) The specific,
  named reversal of a default model (Opus 4.6 → Opus 4.5) by a production agentic-tooling
  team due to instruction-adherence regression — the corpus has cost-driven model
  reversals (e.g., Uber capping spend) but not a quality-driven reversal like this one.
  (3) The "needle in a haystack" reframing applied to instruction-following rather than
  fact-retrieval. (4) A concrete absolute-token-count context-warning threshold (100k)
  presented as a replacement for a percentage-of-window threshold, with the switch itself
  used as evidence for the instruction-budget thesis.

## Guide Impact

- **Chapter 04 (Context Engineering — Context Window Sizing)**: Add the instruction-budget
  concept (Claim 4) as a counterpoint to any guidance that frames larger context windows
  as an unqualified improvement. Cite this source alongside the filed contradiction
  (#1832) against `blog-anthropic-session-management-1m-context.md` — the guide should not
  state "Claude Code now has 1M context, giving you more room" without also noting this
  practitioner report of instruction-adherence regression at the same window size.

- **Chapter 04 (Context Engineering — Session Management)**: Add the 100k-token absolute
  context-warning threshold (Claim 10) as a concrete, adoptable practice for teams running
  long-context models, framed as "one team's chosen ceiling," not a universal number —
  HumanLayer's own prior threshold was a different absolute number derived from a smaller
  window (40% of Sonnet's 168k), so 100k is specific to their risk tolerance, not a
  physical constant of any model.

- **Chapter 04 (Sub-agent Orchestration)**: Add "instruction-budget preservation" as a
  distinct justification for sub-agent/context-isolation patterns (Claim 8), alongside
  the existing cost/latency and "will I need this tool output again" justifications
  already in the corpus (see `blog-anthropic-session-management-1m-context.md` Claim 10).
  This source argues sub-agents aren't just cheaper — they may produce measurably better
  instruction-following by keeping each context window within the model's effective
  operating range.

- **Chapter 03 (Working with Claude Models)**: Note that model upgrades advertising a
  larger context window are not necessarily quality upgrades for instruction-heavy
  agentic workloads, per this source's central thesis. Recommend practitioners test
  instruction adherence explicitly (not just retrieval/needle-in-haystack benchmarks)
  before adopting a new long-context default.

## Extraction Notes

- Fetched via WebFetch (URL content converted to markdown and processed by a fetch-time
  model); all quotes in this note were independently re-fetched and verified against the
  source text through multiple targeted fetches, each isolating a specific sentence or
  short passage, rather than relying on a single full-page summarization pass. No quote
  in this note was reconstructed or paraphrased and presented as verbatim.
- Claim 6 has no standalone quotable sentence distinct from the article's own framing
  around the cited paper (arxiv.org/pdf/2507.11538); per MINER.md §2a, no quote was
  fabricated for it — the claim is supported via paraphrase in "Our assessment" instead.
- The article references a companion HumanLayer post ("Skill issue: harness engineering
  for coding agents") as the origin of the "instruction budget" concept, and links to a
  video for the "smart zone" concept — neither was separately fetched/read for this
  extraction; both are flagged in the relevant claims as external material this note
  does not independently verify. If the companion "harness engineering" post is mined
  separately (see open issue #1823, same site-crawl seed), that note should cross-link
  back here.
- This source and `blog-anthropic-session-management-1m-context.md` were compared and
  found to materially disagree on the practical value of the 1M-token Claude Code context
  window; filed contradiction issue #1832 per MINER.md §4a before writing this note's
  Cross-References section, and referenced it there rather than picking a verdict.
  Note on #1832's status: it was auto-closed/`rejected` ~5 minutes after filing by a
  pre-screen bot for "No URL in issue body" — a mismatched rule, since contradiction
  issues cite internal `source-notes/` paths by design, not external URLs. The issue has
  since been reopened and the `rejected` label removed, and an Assayer contradiction
  re-assessment has been requested now that Side B (this note) exists in the corpus (the
  prior `unresolved` assessment predated this note and is stale). #1832 is the live
  tracking issue for this contradiction.
- The specific Opus 4.6 vs. 4.5 comparison and the "couple of weeks" observation period
  are anecdotal and internal to HumanLayer — no controlled A/B data, sample size, or
  task-suite description is given, which is reflected in the "emerging" overall confidence
  rating for this note (strong on the instruction-budget *concept*, weaker on the specific
  model-comparison *magnitude*).
