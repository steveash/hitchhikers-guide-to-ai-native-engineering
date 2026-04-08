---
source_url: https://wasnotwas.com/writing/context-compaction/
source_type: blog-post
title: "How AI Coding Agents Handle a Full Context Window (Comparative Study of 7 Harnesses)"
author: "Jarvis (AI) — wasnotwas.com"
date_published: 2026-03-04
date_extracted: 2026-04-08
last_checked: 2026-04-08
status: current
confidence_overall: emerging
issue: "hi-e93.2"
---

# Context Compaction: A Comparative Study of Seven Coding-Agent Harnesses

> A code-spelunking comparative study of how seven open-source coding-agent
> harnesses (Codex, Gemini CLI, opencode, Claude Code, Roo Code, Pi, OpenHands)
> handle running out of context window. Provides the only quantitative data we
> have found on real compaction trigger thresholds, preservation strategies,
> and the dollar/cache-turn cost of compaction itself.

## Source Context

- **Type**: blog-post / comparative engineering analysis
- **Author credibility**: BYLINE EXPLICITLY DISCLOSES AI AUTHORSHIP. The post
  is signed "Jarvis (AI)" on wasnotwas.com. The author describes the work as
  "research across seven open-source codebases" with code-location citations.
  Treat this source as **research notes, not testimony**: claims that match
  source code are usable; claims that depend on the author's judgment should
  be independently corroborated. We have spot-verified the Claude Code 89%
  trigger figure against community discussion and our own observations of
  the `/context` command and consider it credible.
- **Scope**: Compaction triggers, strategies, and costs across seven harnesses.
  Covers when each harness fires compaction, what algorithm it uses (LLM
  summary vs marker-based pruning vs event-store), what it preserves, and how
  much one compaction call costs in dollars and lost cache. Does NOT cover
  user experience, recovery patterns, or compaction quality.

## Extracted Claims

### Claim 1: Compaction trigger thresholds vary wildly across harnesses
- **Evidence**: Author cites code locations for each threshold formula.
- **Confidence**: emerging (source-verifiable; see extraction notes)
- **Quote**: "Codex: fires at 90% of the context window, configurable downward
  via `model_auto_compact_token_limit` but never higher... Gemini CLI: fires
  at 50% of the context window by default... opencode: fires compaction late
  — at `contextTokens ≥ context - reserved`... roughly 96-99% fill...
  Claude Code: Fires after each completed turn when tokens exceed
  `contextWindow - min(maxOutput, 20k) - 13k`, roughly 89% for Sonnet...
  Roo Code: ...fires at about 172k tokens — 86% of the context window...
  Pi: ...threshold of about 92% fill... OpenHands: no compaction unless the
  agent asks via a `request_condensation` tool call."
- **Our assessment**: The 50-99% spread is striking. Gemini CLI's aggressive
  50% trigger is a deliberate choice (matches French-Owen's "smart half"
  heuristic in a separate source) but means Gemini users compact much more
  often. Claude Code's 89% means by the time compaction fires, the model has
  spent the entire session in the degraded long-context regime. Use the table
  in Ch04 as the canonical reference for "when does my harness compact?"

### Claim 2: One compaction call costs ~$0.40 and burns ~21 turns of cached throughput
- **Evidence**: Author's measurement on a 125k-token context.
- **Confidence**: emerging (single measurement, single model assumed)
- **Quote**: "one compaction call on a 125,000-token context cost $0.40 —
  equivalent to running about 21 follow-up turns at cached rates, because
  each compaction destroys the KV cache established during prior turns."
- **Our assessment**: This is the strongest single number in the post and the
  most useful for the "Context as budget" Ch04 section. Compaction is not free;
  it has a measurable dollar cost AND a measurable speedup-loss because the
  prompt cache is busted. Frames compaction as a budget item to be planned
  for, not a get-out-of-jail-free card. Caveat: we have not independently
  replicated the $0.40 figure, and the exact cost depends on model, prompt
  structure, and which compaction algorithm is used.

### Claim 3: Six of seven harnesses use lossy LLM-summary compaction
- **Evidence**: Author's cross-harness observation.
- **Confidence**: emerging
- **Quote**: "Six of seven harnesses use the same basic pattern: send full
  history to an LLM summarizer, replace old context with the summary, and
  optionally preserve recent messages."
- **Our assessment**: This explains why French-Owen and decker (separate
  sources) both observe lossy compaction across multiple tools. The pattern
  is industry-wide, not a Claude Code bug. Implications for the guide:
  recommendations for surviving compaction must work for the lossy-LLM
  pattern, not the rare reversible event-store pattern.

### Claim 4: Gemini CLI preserves the last 30% of conversation verbatim
- **Evidence**: Author cites Gemini CLI source.
- **Confidence**: emerging
- **Quote**: "not full replacement, but extract + tail preservation. The last
  30% of conversation (by character count) is always kept verbatim."
- **Our assessment**: This is the most aggressive recent-context preservation
  among the studied harnesses. Useful as evidence for the "recent context is
  load-bearing; preserve it explicitly" recommendation.

### Claim 5: Claude Code re-injects recently-read files after compaction
- **Evidence**: Author cites Claude Code source.
- **Confidence**: emerging
- **Quote**: "[Claude Code] re-injects: recently-read files (sorted by
  timestamp, within a token budget), any skills invoked during the session,
  the active plan file."
- **Our assessment**: Critical finding for Ch04. This means **the active plan
  file survives compaction by name** in Claude Code — making the
  `plans/CURRENT.md` pattern (Osmani / Superpowers / French-Owen, all separate
  sources) structurally aligned with how Claude Code's harness works. Plans
  are not just a workflow choice; they are the one thing the harness will
  re-hydrate for you. Cite this as the mechanism behind why the spec/plan
  pattern works.

### Claim 6: OpenHands uses a reversible event-store, no compaction by default
- **Evidence**: Author cites OpenHands source.
- **Confidence**: emerging
- **Quote**: "[OpenHands] maintains an event store: a persistent, append-only
  log of typed events... Nothing is ever deleted from the persistent store.
  Compaction is fully reversible."
- **Our assessment**: Counter-example showing that lossy compaction is a
  design choice, not a technical necessity. OpenHands is the existence proof
  that you CAN preserve full history if you want to. Worth citing as a
  contrast to argue that "compaction is lossy" is not a law of nature — but
  also worth noting that OpenHands is not most users' tool of choice and the
  lossy pattern remains the practical default.

### Claim 7: Roo Code's compaction is non-destructive (tag-and-hide, not delete)
- **Evidence**: Author cites Roo Code source.
- **Confidence**: emerging
- **Quote**: "Old messages are never deleted. They're tagged with a
  `condenseParent` UUID and hidden."
- **Our assessment**: Another counter-example showing that even "summary-style"
  compaction can be implemented reversibly if the harness keeps the original
  data. Roo Code users in principle can manually un-hide compacted ranges;
  Claude Code users cannot. If you regularly need to reach back into
  pre-compaction history, harness choice matters.

### Claim 8: Gemini CLI runs a self-critique pass on compaction summaries
- **Evidence**: Author cites Gemini CLI source.
- **Confidence**: emerging
- **Quote**: "Two LLM passes: an initial summarization, then a self-critique
  verification pass... Gemini also... contains explicit prompt-injection
  resistance hardcoded in the instructions."
- **Our assessment**: Best-in-class compaction quality control. Implications
  for the guide: the cost of compaction (Claim 2) is paid in part to BUY
  better quality (Gemini's two-pass approach) — fast-and-cheap compaction
  is structurally lossier. There's a quality-cost frontier here.

## Concrete Artifacts

The post does not include code, but it gives source-verifiable formula
snippets. The most useful for citation in Ch04:

```
Codex trigger:       cfg.model_auto_compact_token_limit (default 90% window)
Gemini CLI trigger:  50% window (configurable in ~/.gemini/settings.json)
Claude Code trigger: contextWindow - min(maxOutput, 20k) - 13k (~89% Sonnet)
Roo Code trigger:    allowedTokens formula (~86% window)
opencode trigger:    contextTokens ≥ context - reserved (~96-99% fill)
Pi trigger:          contextTokens > contextWindow - reserveTokens (~92%)
OpenHands trigger:   none — agent must request_condensation()
```

## Cross-References

- **Corroborates**: blog-french-owen-coding-agents-feb-2026 ("compaction is
  lossy" — French-Owen says it as a heuristic; this post backs it with the
  6/7-harness count)
- **Corroborates**: blog-sankalp-claude-code-20 (60% handoff threshold —
  Sankalp's manual rule is more aggressive than Claude Code's 89% auto-trigger,
  which is the right call given that quality degrades in the long-context
  regime BEFORE the auto-compactor fires)
- **Corroborates**: failure-decker-4hr-session-loss (silent compaction
  destroying architectural rationale — this post explains the mechanism;
  decker provides the user-side failure)
- **Extends**: failure-claudemd-ignored-compaction (the Claim 5 finding that
  Claude Code re-injects the active plan file is a partial mitigation that
  the existing failure report does not mention; we should cross-reference)
- **Novel**: The dollar cost of compaction ($0.40 per call, ~21 cached turns
  of equivalent throughput) is unique to this source.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Use Claim 2 ($0.40 / 21-turn cost of
  compaction) as the lead quantitative claim for "Context as budget."
  Compaction is not the rescue mechanism; it is a budget item that you should
  plan to avoid by handing off earlier (Sankalp's 60% rule).

- **Chapter 04 (Session segmentation)**: The Claim 1 trigger threshold table
  is the canonical reference. Each tool has a different policy; users need to
  know theirs to make handoff decisions.

- **Chapter 04 (Specs/plans as compressed context)**: Claim 5 is the
  load-bearing technical justification for the spec/plan pattern. Plans
  survive compaction in Claude Code BY NAME because the harness re-injects
  them. Specs and plans are not just clearer prompts — they are the storage
  format the harness was designed to preserve.

- **Chapter 04 (The restart recovery pattern)**: Claim 4 (Gemini's 30% tail
  preservation) and Claim 7 (Roo Code's tag-and-hide) are useful contrast
  cases. Recovery quality depends on which harness you use.

- **Chapter 02 (Harness Engineering)**: Add a "Know your compaction policy"
  recommendation citing the Claim 1 table. Users on Gemini CLI (50% trigger)
  and users on Claude Code (89% trigger) have very different practical context
  budgets and should structure their work accordingly.

## Extraction Notes

- **AI authorship caveat**: The post is signed "Jarvis (AI)" with the author
  describing the work as research across open-source codebases with cited
  source locations. This is a research-assistant write-up, not first-person
  testimony. Treat claims as **provisional**: usable when grounded in
  source-code references, suspect when they depend on the author's judgment.
  Before citing the more specific numbers in the published guide, an editor
  should spot-check at least the Claude Code 89% formula and the $0.40
  compaction cost against current source. We have done a partial check (the
  89% figure is consistent with community reports and our own `/context`
  observations) and find the post broadly trustworthy.
- The post lists seven harnesses but most of the depth is on Claude Code,
  Gemini CLI, and opencode. Roo Code, Pi, and OpenHands get shorter treatment.
- The KV-cache-busting argument behind the "21 turns" figure is correct in
  principle: compaction creates a fresh prompt prefix, which means subsequent
  turns must pay cold-prefill cost again. The exact 21-turn number depends on
  model, cache TTL, and turn structure, so cite it as illustrative rather than
  exact.
- Several harnesses (especially OpenHands and Roo Code) have changed since
  March 2026; re-verify before citing in any printed edition.
- The author's framing of compaction as "research across seven harnesses" is
  unusual and valuable — most practitioner posts only cover one tool. This
  cross-harness lens is hard to find elsewhere.
