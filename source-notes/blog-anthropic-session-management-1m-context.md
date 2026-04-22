---
source_url: https://claude.com/blog/using-claude-code-session-management-and-1m-context
source_type: blog-post
title: "Using Claude Code: session management and 1M context"
author: "Thariq Shihipar (Anthropic technical staff, Claude Code team)"
date_published: 2026-04-15
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: settled
issue: "#316"
---

# Using Claude Code: Session Management and 1M Context

> First-party Anthropic guidance on every branching decision in a Claude Code session —
> when to Continue, /rewind, /compact, /clear, or spawn a subagent — including the
> official mechanistic explanation of why bad autocompacts happen and how the 1M context
> window changes session management strategy.

## Source Context

- **Type**: blog-post (first-party Anthropic; official guidance, not practitioner reverse-engineering)
- **Author credibility**: Thariq Shihipar is a member of technical staff at Anthropic
  working on Claude Code. This is the engineering team's own account of how session
  management is intended to work. Claims here carry the highest available authority for
  design intent.
- **Scope**: Session and context management in Claude Code with a 1M context window.
  Covers: context rot definition, a five-tool decision framework for each turn, the
  /rewind mechanic, /compact vs /clear trade-offs, steerable compaction with hints, the
  root cause of bad autocompacts, subagent selection heuristic, and the new /usage
  command. Does NOT cover multi-model routing, CLAUDE.md, or harness-level
  configuration.

## Extracted Claims

### Claim 1: "Context rot" is the official Anthropic term for performance degradation as context grows — attention spread and older irrelevant content distract from the current task

- **Evidence**: First-party definition from the Claude Code team; not a practitioner
  observation but stated explicitly in the article.
- **Confidence**: settled
- **Quote**: "Context rot is the observation that model performance degrades as context
  grows because attention gets spread across more tokens, and older, irrelevant content
  starts to distract from the current task."
- **Our assessment**: This settles the terminology debate. "Context rot" is the official
  Anthropic label for the phenomenon documented empirically in `research-wasnotwas-context-compaction`
  (AI-authored comparative study) and experienced by users in `failure-decker-4hr-session-loss`.
  Treat this as the canonical term for the guide.

### Claim 2: Every turn in a Claude Code session is a branching point with five distinct options — not just "continue"

- **Evidence**: Explicit list from the article with rationale for each option.
- **Confidence**: settled
- **Quote**: "you've now got some information in context (tool calls, tool outputs, your
  instructions) and you have a surprising number of options for what to do next: Continue
  — send another message in the same session / /rewind (esc esc) — jump back to a
  previous message and try again from there / /clear — start a new session... / Compact
  — summarize the session so far... / Subagents — delegate the next chunk of work to an
  agent with its own clean context"
- **Our assessment**: The framing of every turn as a branching decision rather than a
  linear flow is the most pedagogically useful construct in this post. The guide should
  adopt this model as the organizing principle for the session-management chapter.
  Practitioners who think only about "continue or start over" are missing three powerful
  in-between options.

### Claim 3: Anthropic's general rule is "new task = new session," with an explicit exception for tasks where prior session context reduces re-reading overhead

- **Evidence**: Stated as an official heuristic with a concrete counterexample.
- **Confidence**: settled
- **Quote**: "Our general rule of thumb is when you start a new task, you should also
  start a new session... Sometimes you may do related tasks where some of the context
  is still necessary, but not always. For example, writing the documentation for a
  feature you just implemented."
- **Our assessment**: The exception is as important as the rule. The "write docs for
  a feature you just built" case is the clearest example of when carrying context
  forward is cheaper than rebuilding it. The guide should present both the rule and
  the exception with this concrete example.

### Claim 4: /rewind (double-Esc) is the superior correction mechanism — it preserves useful file reads while dropping failed attempts, enabling a tighter re-prompt

- **Evidence**: First-party recommendation with a concrete example contrasting /rewind
  against the naive "that didn't work, try X instead" correction in the same session.
- **Confidence**: settled
- **Quote**: "Claude reads five files, tries an approach, and it doesn't work. Your
  instinct may be to type 'that didn't work, try X instead.' But the better move may
  be to rewind to just after the file reads, and re-prompt with what you learned.
  'Don't use approach A, the foo module doesn't expose that—go straight to B.'"
- **Our assessment**: This is the sharpest practical guidance in the post. Keeping the
  file reads while dropping the failed attempt is the mechanistic insight — the failed
  attempt is noise that fills context and risks anchoring the model on a wrong path.
  The guide should present this as the default correction pattern, not an advanced
  technique.

### Claim 5: /rewind supports a "summarize from here" handoff mechanic — the current Claude instance writes a message to its prior self documenting what it tried and why it failed

- **Evidence**: Described in the article as a distinct use case for /rewind beyond simple
  correction.
- **Confidence**: settled
- **Quote**: "You can also use 'summarize from here' or the /rewind slash command to
  have Claude summarize its learnings and create a handoff message, kind of like a
  message to the previous iteration of Claude from its future self that tried something
  and it didn't work."
- **Our assessment**: This is a novel first-party-documented UX pattern not present in
  any existing source note. The temporal framing — "future self to past self" — makes
  the context-transfer mechanic concrete. This is meaningfully different from simply
  re-prompting; it creates an explicit record of failed approaches that the next
  iteration receives as structured guidance. Cite as the official handoff pattern.

### Claim 6: /compact and /clear achieve the same nominal goal via opposite trade-off profiles — /compact is automated but lossy; /clear requires user effort but delivers precise control

- **Evidence**: First-party comparison with explicit trade-off language.
- **Confidence**: settled
- **Quote**: "Compact asks the model to summarize the conversation so far, then replaces
  the history with that summary. It's lossy, but you didn't have to write anything
  yourself and Claude might be more thorough in including important learnings or files.
  With /clear you write down what matters... and start clean. It's more work, but the
  resulting context is what you decided was relevant."
- **Our assessment**: The guide currently underspecifies this distinction. The /compact
  vs /clear choice is not about context size management — it is about who decides what
  matters: the model (compact) vs. the practitioner (clear). Users doing complex
  architectural work where the "why" is load-bearing should prefer /clear. Users doing
  well-bounded tasks where the model can summarize accurately should prefer /compact.
  Add this as the primary decision criterion.

### Claim 7: /compact accepts a natural-language hint that steers which parts of the session history the summary preserves

- **Evidence**: Explicitly stated feature with example syntax.
- **Confidence**: settled
- **Quote**: "You can also steer it by passing instructions (/compact focus on the auth
  refactor, drop the test debugging)."
- **Our assessment**: This is the most actionable new capability in the post. Steerable
  /compact directly addresses the failure mode documented in `failure-decker-4hr-session-loss`
  and `failure-claudemd-ignored-compaction`: the model's summary drops contextually
  important content. With a steering hint, the user can tell the summarizer what matters.
  Add as a concrete mitigation for compaction loss, adjacent to the existing guidance
  on session snapshots.

### Claim 8: Bad autocompacts are caused by two compounding factors — the model cannot predict the direction of future work AND context rot means the model is at its least intelligent point precisely when compaction fires

- **Evidence**: First-party mechanistic explanation with a concrete example. This is the
  only place this two-factor explanation appears in authoritative form.
- **Confidence**: settled
- **Quote**: "bad compacts can happen when the model can't predict the direction your
  work is going... autocompact fires after a long debugging session and summarizes
  the investigation and your next message is 'now fix that other warning we saw in
  bar.ts.' But because the session was focused on debugging, the other warning might
  have been dropped from the summary. This is particularly difficult, because due to
  context rot, the model is at its least intelligent point when compacting."
- **Our assessment**: This is the highest-value claim in the post. The two-factor
  model explains something no existing source note captures: bad compactions are worst
  precisely when you'd expect quality to matter most — at the end of a complex, long
  session. The mechanism is: (1) the model summarizes based on what the session was
  focused on; (2) the model doing the summarizing is impaired by context rot. The
  combination means the most complex sessions produce the worst compaction quality.
  This directly motivates proactive compaction before the window fills.

### Claim 9: Proactive /compact with a steering hint — before the context window fills — is the official remedy for bad autocompacts

- **Evidence**: Stated as the direct solution following the bad autocompact explanation.
- **Confidence**: settled
- **Quote**: "With one million context, you have more time to /compact proactively with
  a description of what you want to do."
- **Our assessment**: The 1M context window changes the calculus. At 200K (earlier
  Claude Code), users had little warning before the autocompactor fired. At 1M, there
  is meaningful runway to issue a proactive /compact with a steering hint while the
  model is still in a better state (earlier in the context fill, lower rot). The guide
  should explicitly recommend proactive compaction as the primary mitigation, not
  session snapshots (which are reactive).

### Claim 10: The subagent decision heuristic is "Will I need this tool output again, or just the conclusion?" — if only the conclusion is needed, spawn a subagent

- **Evidence**: Stated explicitly as "the mental test used at Anthropic" with three
  concrete example invocation patterns.
- **Confidence**: settled
- **Quote**: "The mental test used at Anthropic: will I need this tool output again,
  or just the conclusion?"
- **Our assessment**: This is the first first-party subagent selection criterion in
  our corpus. The existing corpus has practitioner heuristics for multi-agent
  orchestration (worktrees, task atomicity) but not an official "when to spawn vs
  not" rule. The examples in the post (verify against spec, summarize another codebase,
  write docs from git changes) make the heuristic concrete. Add to Chapter 04 as the
  authoritative subagent selection criterion.

### Claim 11: /usage is a new slash command that surfaces token consumption information within a Claude Code session

- **Evidence**: Announced and described in the opening of the article as the hook for
  the whole post.
- **Confidence**: settled
- **Quote**: "We released /usage, a new slash command to help you understand your usage
  with Claude Code. This feature was informed by a number of conversations with customers."
- **Our assessment**: Not present in any existing source note. The /usage command is the
  tool that makes proactive session management possible — without visibility into token
  consumption, users cannot know when to issue a proactive /compact. Pair with the
  proactive compaction guidance (Claim 9) as the tooling prerequisite.

### Claim 12: Claude Code's context window is now 1M tokens — this is first-party confirmation of the current window size

- **Evidence**: Directly stated in the article.
- **Confidence**: settled
- **Quote**: "Claude Code has a context window of one million tokens."
- **Our assessment**: Settles the context size question. The `research-wasnotwas-context-compaction`
  note was written against an older window size and calculated the 89% trigger threshold
  based on a different window size. The trigger threshold formula in that note
  (`contextWindow - min(maxOutput, 20k) - 13k`) yields different absolute token counts
  at 1M than at earlier sizes — practitioners using those numbers for planning should
  recalculate. Update any guide sections citing a specific token count for Claude Code's
  context window.

## Concrete Artifacts

### Official Five-Tool Decision Table

```
| Situation                                          | Tool           | Why                                                     |
|----------------------------------------------------|----------------|---------------------------------------------------------|
| Same task, context is still relevant               | Continue       | Everything in the window is load-bearing; don't rebuild.|
| Claude went down a wrong path                      | Rewind (⎋⎋)    | Keep file reads, drop failed attempt, re-prompt.        |
| Mid-task, session bloated with stale exploration   | /compact <hint>| Low effort; Claude summarizes. Steer with a hint.       |
| Starting a genuinely new task                      | /clear         | Zero rot; you control what carries forward.             |
| Next step generates output you'll only need        | Subagent       | Intermediate noise stays in child; result returns.      |
| the conclusion from                                |                |                                                         |
```
*(Table reproduced verbatim from the article, authored by Thariq Shihipar, Anthropic)*

### Subagent Invocation Examples

Three first-party example prompts for explicit subagent delegation:

```
"Spin up a subagent to verify the result of this work based on the following spec file"
"Spin off a subagent to read through this other codebase and summarize how it implemented
 the auth flow, then implement it yourself in the same way"
"Spin off a subagent to write the docs on this feature based on my git changes"
```
*(From the article, Thariq Shihipar, Anthropic)*

### /compact Steering Syntax

```
/compact focus on the auth refactor, drop the test debugging
```
*(Verbatim example from article)*

## Cross-References

- **Corroborates**: `research-wasnotwas-context-compaction` — the "context rot" phenomenon
  documented empirically in that source (model quality degrades as context grows) now has
  an official Anthropic term and first-party confirmation. The compaction-trigger formula
  (~89% threshold) in that note is corroborated by this post's first-party description
  of compaction as firing when "nearing the end of the context window." However, this
  source adds something that note lacks: the claim that model quality is *worst* at the
  moment compaction fires (Claim 8).

- **Corroborates**: `failure-decker-4hr-session-loss` — the decker failure (silent
  autocompact during a long debugging session destroying architectural rationale) is
  exactly the pattern described in Claim 8. The official explanation of *why* this
  happens (model can't predict direction; model is at its least intelligent point)
  validates decker's experiential account. These two sources together provide the
  complete picture: the failure mode and its first-party mechanism.

- **Extends**: `research-wasnotwas-context-compaction` — that note covers *when*
  compaction fires and *what it costs* ($0.40, ~21 cached turns). This source adds
  the first-party explanation of *why quality varies* across compactions (context
  rot at peak fill + inability to predict future direction). Together they give both
  the economics and the quality model for compaction.

- **Extends**: `failure-claudemd-ignored-compaction` — that note documents CLAUDE.md
  instructions being summarized away during compaction. This source's steerable
  /compact hint (Claim 7) is the official partial mitigation: if the user explicitly
  tells the compaction summary what to preserve, CLAUDE.md-equivalent rules can
  survive the compaction boundary more reliably.

- **Extends**: `blog-ccunpacked-claude-code-architecture` — the ccunpacked note
  documents the agent loop Step 10 (Post-Sampling Hooks: Auto-compaction from
  autoCompact.ts) and its architectural position. This source provides the user-facing
  mechanics and decision framework that corresponds to that architectural step. Together
  they give the inside (loop step + source file) and outside (when to invoke which
  command) views of the compaction system.

- **Novel**: (1) The first-party five-tool decision table mapping situations to session
  management commands — no existing source has this authoritative mapping. (2) The
  /rewind "summarize from here" handoff mechanic — not documented elsewhere in the
  corpus. (3) The two-factor bad-autocompact explanation (direction unpredictability +
  context-rot impairment at peak fill) — first-party and mechanistically specific.
  (4) Steerable /compact with a hint — `/compact <instructions>` syntax is new.
  (5) The subagent "will I need this again?" heuristic as the official selection
  criterion — first-party decision rule, not present in any existing note.
  (6) The /usage command — announced here, not in any existing note.
  (7) First-party confirmation of Claude Code's 1M context window as the current size.

## Guide Impact

- **Chapter 04 (Context Engineering — Session Management)**: Replace or supplement any
  current "when to compact/clear" guidance with the five-tool decision table (Claim 2
  artifact). This is the authoritative Anthropic framework. Add the new task = new
  session rule (Claim 3) as the baseline decision heuristic with the related-task
  exception.

- **Chapter 04 (Correction Patterns)**: Add /rewind as the preferred correction
  mechanism over in-session retry prompts (Claim 4). Add the "summarize from here"
  handoff pattern (Claim 5) as the official way to pass learned constraints forward
  after a rewind.

- **Chapter 04 (Compaction Guidance)**: Add the two-factor bad-autocompact explanation
  (Claim 8) as the mechanistic justification for proactive compaction. Update guidance
  from "avoid compaction" to "compact proactively with a hint before the window fills."
  Add steerable /compact syntax (Claim 7) as the primary mitigation for compaction
  quality loss — this partially addresses the failure mode in `failure-claudemd-ignored-compaction`.

- **Chapter 04 (Subagent Orchestration)**: Add the "will I need this tool output again,
  or just the conclusion?" heuristic (Claim 10) as the official Anthropic selection
  criterion for spawning subagents. Pair with the three invocation examples from the
  Concrete Artifacts section.

- **Chapter 02 (Harness Engineering — Tooling)**: Add /usage as a tool for monitoring
  context consumption. Frame it as the prerequisite for proactive session management:
  you cannot compact proactively if you cannot see where you are in the context window.

- **Chapter 04 (Context Window Sizing)**: Update any section citing an older Claude Code
  context window size. The first-party figure is 1M tokens (Claim 12). The trigger
  threshold formula from `research-wasnotwas-context-compaction` applies at 1M, which
  yields a larger absolute token budget before compaction fires than prior versions.

## Extraction Notes

- The article is short (~1,000 words, 5-minute read) but information-dense.
  Every section adds a distinct actionable claim; none of the content is filler.
- This is the primary source for the /rewind command mechanics. No other source in our
  corpus covers /rewind at this level of detail. The double-Esc keybinding, the
  "summarize from here" handoff pattern, and the correction use case are all
  documented here for the first time.
- The article opens by noting /usage was "informed by a number of conversations with
  customers" — suggesting the session management guidance throughout is a response to
  observed practitioner failure modes (consistent with the decker and sukit failure
  reports in our corpus).
- Author (Thariq Shihipar) is not a researcher; this is product/engineering team
  communication. Claims reflect design intent and intended use patterns, not controlled
  study findings. Confidence is settled for design-intent claims; treat as authoritative
  on "how Claude Code is supposed to work" even though individual user experiences
  may vary.
- No paywalled or inaccessible content. The article is public on claude.com.
