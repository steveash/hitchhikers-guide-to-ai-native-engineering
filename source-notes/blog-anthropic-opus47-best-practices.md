---
source_url: https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
source_type: blog-post
title: "Best practices for using Claude Opus 4.7 with Claude Code"
author: Anthropic (Claude team)
date_published: 2026-04-16
date_extracted: 2026-04-23
last_checked: 2026-04-23
status: current
confidence_overall: settled
issue: "#317"
---

# Best practices for using Claude Opus 4.7 with Claude Code

> First-party Anthropic guidance on the five effort levels, adaptive thinking,
> and three behavioral changes between Opus 4.6 and 4.7 that practitioners
> must account for when upgrading existing Claude Code setups and agentic harnesses.

## Source Context

- **Type**: blog-post (official claude.com blog, April 16, 2026)
- **Author credibility**: Published directly on Anthropic's Claude blog — the same
  team and venue as the session management post (Thariq Shihipar) and multi-agent
  coordination post. This is first-party Anthropic guidance on how to use a specific
  model version; treat effort-level recommendations, adaptive thinking mechanics, and
  behavioral default descriptions as authoritative product documentation, not practitioner
  opinion. The post is explicitly prescriptive ("we recommend," "we find," "we've set
  the default").
- **Scope**: Covers Opus 4.7 in Claude Code specifically — effort level taxonomy and
  per-level guidance, adaptive thinking as a replacement for fixed thinking budgets,
  session structuring for delegation-style use, and three behavioral defaults that
  changed from 4.6 to 4.7 (verbosity, tool-call rate, subagent spawning rate). Does
  NOT cover: SDK-level API parameters, multi-agent topology selection, CLAUDE.md
  authoring, or pricing comparisons. Five-minute read; this is a practitioner transition
  guide, not an architecture post.

## Extracted Claims

### Claim 1: Five effort levels exist for Opus 4.7, each with a distinct tradeoff profile — low, medium, high, xhigh, and max

- **Evidence**: First-party taxonomy with explicit per-level guidance from the post.
  Each level is named, positioned relative to the others, and described with a specific
  use-case recommendation.
- **Confidence**: settled (first-party vendor taxonomy; authoritative for Claude Code)
- **Quote**: "Here's some additional guidance for each effort level: `medium` and `low`:
  Available for cost-sensitive, latency-sensitive, or tightly scoped work... `high`:
  Balances intelligence and cost... `xhigh` (default, recommended): The best setting for
  most coding and agentic uses... `max`: Squeezes out additional performance on genuinely
  hard problems, but shows diminishing returns and is more prone to overthinking."
- **Our assessment**: The five-level taxonomy is cleaner than the prior three-level
  framing. The critical new level is `xhigh` — it fills the practical gap between
  cost-managed `high` and overthinky `max`. Prior guidance collapsed this into a
  binary choice; practitioners who tuned `max` for intelligence were accepting runaway
  token usage as the cost. `xhigh` represents a deliberate calibration point that
  Anthropic has validated as better for the typical agentic workload.

### Claim 2: `xhigh` is the new default effort level for Opus 4.7 in Claude Code, automatically applied to existing users who have not manually set effort

- **Evidence**: Explicit first-party statement: "We've set the default effort level for
  Opus 4.7 to xhigh because we believe it's the best setting for most coding tasks.
  If you're an existing Claude Code user but you haven't manually set your effort level,
  you'll be upgraded to `xhigh` automatically."
- **Confidence**: settled (first-party configuration statement)
- **Quote**: "If you're an existing Claude Code user but you haven't manually set your
  effort level, you'll be upgraded to `xhigh` automatically. You can still adjust your
  effort manually."
- **Our assessment**: This is an important migration note. Practitioners who benchmarked
  Opus 4.6 at some effort level and compared it against a fresh Opus 4.7 deployment may
  be unknowingly comparing different effort configurations. The automatic `xhigh` upgrade
  means token usage and response quality baselines will both shift compared to whatever
  effort level the user had before. Any A/B comparison of 4.6 vs. 4.7 should control for
  effort level explicitly.

### Claim 3: `xhigh` is recommended for most agentic coding work; `max` is for deliberate ceiling-testing on non-cost-sensitive problems

- **Evidence**: Per-level guidance in the post with explicit use-case mapping:
  `xhigh` → "intelligence-sensitive tasks like designing APIs and schemas, migrating
  legacy code, and reviewing large codebases"; `max` → "tasks like testing the model's
  maximum ceiling in evals and for extremely intelligence-sensitive and non-cost-sensitive uses."
- **Confidence**: settled (explicit vendor recommendation with use-case examples)
- **Quote**: "`xhigh`... has strong autonomy and intelligence without the runaway token
  usage that max can produce on long agentic runs."
- **Our assessment**: The explicit warning about `max` — "runaway token usage" and
  "diminishing returns" — is more direct than prior Anthropic guidance on effort
  management. This positions `max` as a deliberate, bounded choice for specific
  evaluation scenarios, not a "more is better" default. The guide should adopt this
  framing: `xhigh` is the production default; `max` is an evaluation tool.

### Claim 4: `high` is the recommended effort level when running concurrent sessions or managing costs without a large quality drop

- **Evidence**: Explicit per-level guidance in the post.
- **Confidence**: settled (first-party recommendation with a specific use-case trigger)
- **Quote**: "`high`: Balances intelligence and cost. Choose high if you're running
  concurrent sessions or want to spend less without a large quality drop."
- **Our assessment**: The concurrent-sessions trigger is the most actionable guidance
  here. Practitioners running multiple parallel Claude Code instances simultaneously
  should default to `high` because the aggregate token cost of multiple `xhigh` sessions
  compounds quickly. The quality-per-cost framing makes this a deliberate architectural
  decision rather than a default accepted without thought.

### Claim 5: Extended thinking with a fixed thinking budget is not supported in Opus 4.7 — practitioners must rewrite any harnesses that used fixed-budget extended_thinking from Opus 4.6

- **Evidence**: Explicit first-party statement: "Extended Thinking with a fixed thinking
  budget is not supported in Opus 4.7."
- **Confidence**: settled (first-party breaking-change statement)
- **Quote**: "Extended Thinking with a fixed thinking budget is not supported in Opus 4.7.
  Instead, Opus 4.7 offers adaptive thinking."
- **Our assessment**: This is the hardest migration break in the post. Any harness that
  set a fixed `thinking_budget` for extended thinking when calling Opus 4.6 will break or
  be silently ignored on Opus 4.7. The post does not specify whether the API returns an
  error or silently ignores the parameter — practitioners must test. This is a concrete
  action item for any team using extended thinking programmatically.

### Claim 6: Adaptive thinking replaces fixed thinking budgets — the model decides at each step whether and how much to think, optimizing thinking tokens over the full agentic run

- **Evidence**: First-party description of the adaptive thinking mechanism: "This makes
  thinking _optional_ at each step and allows the model to decide when to use more
  thinking based on context. It can respond to simple queries quickly, skip thinking
  when a step doesn't benefit from it, and invest its thinking tokens where they're most
  likely to be useful."
- **Confidence**: settled (first-party behavioral description of a shipped model feature)
- **Quote**: "Over an agentic run, this can add up to faster responses and a better
  user experience."
- **Our assessment**: The key implication is that thinking resource allocation is now
  dynamic across an agentic run rather than fixed per-call. This is architecturally
  significant: harnesses that relied on thinking-budget settings to control inference
  cost (e.g., "set a low budget for routine steps, high budget for hard steps") must
  switch to prompt-based control (Claims 7–8). The benefit is that the model
  self-allocates thinking where it matters most — the cost is that the harness loses
  direct numeric control over thinking cost.

### Claim 7: To elicit more thinking from Opus 4.7, prompt directly with language that signals task difficulty

- **Evidence**: First-party recommendation with example prompt text.
- **Confidence**: settled (first-party guidance with concrete examples)
- **Quote**: "If you want more thinking, try something like, 'Think carefully and
  step-by-step before responding; this problem is harder than it looks.'"
- **Our assessment**: This is the replacement interface for fixed thinking budget control.
  The mechanism is prompt-based rather than parameter-based. The specific signal —
  "this problem is harder than it looks" — is notable: it frames difficulty calibration
  as the lever, not just instruction following. Practitioners building harnesses that
  previously used thinking budget as a quality dial should test this prompt pattern
  as the replacement.

### Claim 8: To elicit less thinking (faster, cheaper responses) from Opus 4.7, prompt for speed over depth explicitly

- **Evidence**: First-party recommendation with example prompt text and explicit tradeoff.
- **Confidence**: settled (first-party guidance with concrete tradeoff stated)
- **Quote**: "If you want less thinking, try something like, 'Prioritize responding
  quickly rather than thinking deeply. When in doubt, respond directly.' You'll save
  tokens but may lose some accuracy on harder steps."
- **Our assessment**: The honest tradeoff disclosure ("may lose some accuracy on harder
  steps") is useful calibration for practitioners considering this prompt pattern. For
  well-scoped, low-ambiguity tasks (code formatting, simple lookups, templated generation),
  the speed/cost saving is likely worth the accuracy cost. For tasks where the model must
  reason through ambiguity, this prompt is counterproductive. The guide should present
  both prompt patterns as matched pairs with their tradeoff profiles.

### Claim 9: Opus 4.7 performs best when treated as a capable engineer being delegated to, not as a pair programmer being guided step-by-step

- **Evidence**: Explicit first-party framing backed by four behavioral recommendations.
  The post states directly: "we've found it's helpful to treat Claude more like a capable
  engineer you're delegating to than a pair programmer you're guiding line by line."
- **Confidence**: settled (explicit vendor recommendation with behavioral specifics)
- **Quote**: "Specify the task up front, in the first turn. Well-specified task descriptions
  that incorporate intent, constraints, acceptance criteria, and relevant file locations
  give Opus 4.7 the context it needs to deliver stronger outputs. Ambiguous prompts
  conveyed progressively across many turns tend to reduce both token efficiency and,
  sometimes, overall quality."
- **Our assessment**: This is the sharpest behavioral principle in the post. It directly
  inverts the "interactive pair programming" mental model that many practitioners carry
  from earlier, less capable models. The mechanism is specific: every user turn adds
  reasoning overhead (Claim 10), and ambiguity spread across many turns compounds both
  the token cost and the coordination cost. This aligns with the session management
  guidance from `blog-anthropic-session-management-1m-context.md` (Claim 2 there:
  "every turn is a branching point") but goes further: the preferred branching point
  for Opus 4.7 is the first turn.

### Claim 10: Every additional user turn adds reasoning overhead — batching context into the first turn improves both token efficiency and overall quality

- **Evidence**: First-party behavioral statement with explicit reasoning: "Reduce the
  number of required user interactions. Every user turn adds reasoning overhead. Batch
  your questions and give the model the context it needs to keep moving."
- **Confidence**: settled (first-party behavioral description)
- **Quote**: "Every user turn adds reasoning overhead."
- **Our assessment**: This is a new, explicit data point on why interactive prompting
  degrades performance in Opus 4.7. Prior guidance framed this as a context management
  concern (fewer turns = smaller context = lower rot risk). This post adds a second
  mechanism: each user turn triggers additional reasoning, which compounds on prior
  turns. Practitioners who treat Claude as a REPL should consider restructuring into
  front-loaded delegation prompts, with clarifying questions reserved for after the
  model reports its plan (not distributed across the whole session).

### Claim 11: Opus 4.7's default response length is calibrated to task complexity — it is less verbose than Opus 4.6 by default

- **Evidence**: Explicit behavioral change description from the post's "Behavior changes
  worth knowing" section.
- **Confidence**: settled (first-party behavioral change notification)
- **Quote**: "Response length is calibrated to task complexity. Opus 4.7 isn't as
  default-verbose as Opus 4.6. You can expect shorter answers on simple lookups and
  longer ones on open-ended analysis."
- **Our assessment**: Practitioners who built downstream parsers or UIs expecting verbose
  Opus 4.6 responses may see unexpected truncation on Opus 4.7. Conversely, practitioners
  who complained about Opus 4.6's over-verbosity now have a model that calibrates more
  naturally. The fix for length-dependent use cases: state length expectations explicitly
  in the prompt. The post provides a useful UX heuristic for style prompting in Claim 12.

### Claim 12: Positive examples of desired voice/style are more effective than negative "Don't do this" instructions for length and style control

- **Evidence**: First-party recommendation in the context of response length calibration.
- **Confidence**: settled (explicit vendor guidance; corroborated by general prompting
  best practices in the field)
- **Quote**: "We find that positive examples of the voice you want work better than
  negative 'Don't do this' instructions."
- **Our assessment**: This is a portable prompt-engineering principle that extends well
  beyond length control. Negative constraints ("don't be verbose," "don't use bullet
  lists") are harder for models to reliably apply than positive exemplars. Practitioners
  building system prompts with style constraints should provide a short example of the
  desired output format rather than a list of prohibitions.

### Claim 13: Opus 4.7 calls tools less often and reasons more — harnesses that require aggressive tool use (search, file reading) must explicitly guide when and why tools should be used

- **Evidence**: Explicit behavioral change description: "The model calls tools less often
  and reasons more. This produces better results in many cases. If you want _more_ tool
  use (say, more aggressive search or file reading during agentic work), provide guidance
  that explicitly describes when and why the tool should be used."
- **Confidence**: settled (first-party behavioral change notification)
- **Quote**: "The model calls tools less often and reasons more."
- **Our assessment**: This change has two sides. For practitioners who observed Opus 4.6
  calling tools aggressively (sometimes unnecessarily), this is a positive improvement.
  For practitioners who built harnesses relying on aggressive tool calls (e.g., code
  search agents that were expected to grep widely before reasoning), this is a breaking
  behavior change that requires updated system prompts. The fix is explicit: tell the
  model when to use which tool, not just what tools are available.

### Claim 14: Opus 4.7 spawns fewer subagents by default — harnesses relying on automatic subagent spawning for parallelism must explicitly instruct when to delegate

- **Evidence**: Explicit behavioral change description with concrete remediation guidance.
- **Confidence**: settled (first-party behavioral change with actionable guidance)
- **Quote**: "It spawns fewer subagents by default. Opus 4.7 tends to be more judicious
  about when to delegate work to subagents. If your use case benefits from parallel
  subagents (for example, fanning out across files or independent items), we recommend
  spelling that out."
- **Our assessment**: This is the most operationally consequential behavior change for
  practitioners building multi-agent harnesses. An orchestrator that previously relied
  on Opus 4.6 spontaneously spawning subagents for parallel work will observe significantly
  reduced parallelism on Opus 4.7 without explicit spawning instructions. This is NOT
  a quality regression — Opus 4.7 is making a better judgment about when spawning is
  warranted. But harnesses designed around the old spontaneous-spawning behavior need
  explicit delegation guidance added to their system prompts.

### Claim 15: The authoritative subagent spawning heuristic for Opus 4.7 — do not spawn for work completable in a single response; spawn multiple subagents in the same turn when fanning out

- **Evidence**: Verbatim guidance from the post, explicitly framed as a concrete rule
  for practitioners to adopt in their own system prompts.
- **Confidence**: settled (explicit first-party spawning rule)
- **Quote**: "Do not spawn a subagent for work you can complete directly in a single
  response (e.g., refactoring a function you can already see). Spawn multiple subagents
  in the same turn when fanning out across items or reading multiple files."
- **Our assessment**: This is the most precisely extractable and directly usable artifact
  in the post. The rule has two parts: a prohibition (do not spawn for single-response
  work) and a prescription (spawn multiple in the same turn for fan-out work). The
  prohibition prevents unnecessary orchestration overhead; the prescription ensures that
  genuine parallelism is explicitly requested rather than hoped for. This rule should be
  added verbatim (or near-verbatim) to any system prompt for an orchestrating agent on
  Opus 4.7.

### Claim 16: Auto mode (Shift+Tab toggle) is now available in research preview for Claude Code Max users, and is especially suited for long-running fully-specified tasks

- **Evidence**: First-party announcement of research preview availability.
- **Confidence**: settled (first-party feature availability statement)
- **Quote**: "Use auto mode when appropriate. For tasks where you trust the model to
  execute safely without frequent check-ins, auto mode cuts cycle time. It's an especially
  good fit for long-running tasks where you've provided full context up front. Auto mode
  is now available in research preview for Claude Code Max users—you can toggle it on
  using Shift+Tab."
- **Our assessment**: The access restriction (Max users only) limits the immediate
  applicability but this is consistent with the research preview label. The best-fit
  description (long-running tasks, full context up front, trusted execution) aligns
  directly with the `blog-anthropic-claude-code-auto-mode.md` architecture: auto mode's
  safety classifier is most effective when the system prompt provides clear task context
  that the classifier can compare actions against.

### Claim 17: Hook-based task completion notifications can be self-generated — ask Claude to create its own notification hooks

- **Evidence**: First-party recommendation with a concrete capability description.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Set up notifications for completed tasks. Ask Claude to play a sound when
  it's done with a task, and it can create its own hook-based notifications."
- **Our assessment**: This is a small but useful pattern — especially for long agentic
  tasks where the practitioner walks away. The fact that Claude can create its own
  notification hooks underscores the maturity of the hook system: it is self-discoverable
  by the model, not just a harness-engineering primitive. No other source in the corpus
  documents this pattern; it belongs in any hooks tutorial alongside practitioner-authored
  hook examples.

## Concrete Artifacts

### Effort Level Decision Table

```
# Opus 4.7 effort level guidance
# Source: "Best practices for using Claude Opus 4.7 with Claude Code", Anthropic, April 16, 2026

Level   | Default? | Recommended For                                      | Watch Out For
--------|----------|------------------------------------------------------|-----------------------------
low     | No       | Cost/latency-sensitive, tightly scoped tasks         | Reduced capability on harder tasks
medium  | No       | Cost/latency-sensitive, tightly scoped tasks         | Reduced capability on harder tasks
high    | No       | Concurrent sessions; spending less without large     | Less capable than xhigh
        |          | quality drop                                         |
xhigh   | YES      | Most agentic coding (APIs, migrations, code review)  | —
max     | No       | Evals, ceiling testing, non-cost-sensitive tasks     | Diminishing returns; overthinking;
        |          |                                                      | runaway token usage on long runs
```

### Adaptive Thinking Prompt Control Patterns

```
# Prompt-based thinking rate control for Opus 4.7
# Source: Anthropic, April 16, 2026
# (Replaces fixed extended_thinking budget from Opus 4.6 — fixed budgets NOT supported in 4.7)

More thinking (harder problems, careful reasoning):
  "Think carefully and step-by-step before responding; this problem is harder than it looks."

Less thinking (faster, cheaper, simpler tasks):
  "Prioritize responding quickly rather than thinking deeply. When in doubt, respond directly."
  [Tradeoff: saves tokens; may lose accuracy on harder steps]
```

### Opus 4.6 → 4.7 Behavioral Change Summary

```
# Behavioral defaults that changed from Opus 4.6 to Opus 4.7
# Source: "Best practices for using Claude Opus 4.7 with Claude Code", Anthropic, April 16, 2026
# These require prompt or harness updates if prior behavior was load-bearing

Change 1: RESPONSE LENGTH
  4.6 behavior: Default-verbose — longer responses even on simple queries
  4.7 behavior: Calibrated to task complexity — shorter on simple lookups, longer on analysis
  Fix if needed: State length/style expectations explicitly; use positive examples, not prohibitions

Change 2: TOOL CALL RATE
  4.6 behavior: Called tools more frequently; aggressive tool use
  4.7 behavior: Calls tools less often; reasons more instead
  Fix if needed: Provide explicit guidance on when/why to use specific tools

Change 3: SUBAGENT SPAWNING RATE
  4.6 behavior: More spontaneous subagent spawning for parallel work
  4.7 behavior: More judicious; fewer spontaneous spawns
  Fix if needed: Add explicit spawning instruction to system prompt:
    "Do not spawn a subagent for work you can complete directly in a single response.
     Spawn multiple subagents in the same turn when fanning out across items or
     reading multiple files."
```

### Session Structuring Checklist for Opus 4.7

```
# Delegation-first session structuring for Opus 4.7
# Source: Anthropic, April 16, 2026

✓ Specify task up front, first turn:
    Include intent + constraints + acceptance criteria + relevant file locations

✓ Reduce required user interactions:
    Every user turn adds reasoning overhead; batch questions; give context to keep moving

✓ Consider auto mode for long fully-specified tasks (Max plan users, research preview):
    Shift+Tab to toggle on

✓ Experiment with effort levels within a task:
    Toggle between effort levels mid-task to manage token usage and reasoning tradeoff

✓ Set up notification hooks for long-running tasks:
    Ask Claude to create its own hook-based notifications (e.g., play a sound when done)
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` — The subagent spawning rule
    here (Claim 15: "Do not spawn a subagent for work you can complete directly in a
    single response") provides a more specific, model-version-anchored form of the
    orchestrator-subagent guidance in that post. The Anthropic post (April 10) established
    the five-pattern taxonomy and recommended orchestrator-subagent as the default; this
    post (April 16) provides the precise Opus 4.7 behavioral heuristic for WHEN the
    orchestrator should actually spawn. The two posts are directly complementary for Ch02
    guidance on subagent orchestration.
  - `blog-anthropic-session-management-1m-context.md` — Session structuring guidance
    (Claims 9–10) dovetails closely with that post. The "specify task up front, first
    turn" recommendation here is the delegation-mode implementation of the "new task =
    new session" general rule from the session management post. The "reduce user turns"
    guidance here deepens the session branching-point framework (Claim 2 there). Both
    posts are written by the same Anthropic Claude Code team in the same week.
  - `blog-anthropic-claude-code-auto-mode.md` — The auto mode mention here (Claim 16:
    available for Max users, research preview, best for long tasks with full context)
    is the user-facing counterpart to the architectural account there. That post documents
    the two-stage classifier and three-tier permission structure; this post documents the
    user conditions (Max plan) and access path (Shift+Tab) that make it available.
  - `blog-anthropic-harness-long-running.md` — The delegation posture advice (Claim 9)
    aligns with that post's guidance on sprint decomposition: providing a well-specified
    task up front (sprint contract) and reducing mid-session corrections maps directly
    to what makes agentic runs succeed in that post's framework.

- **Contradicts**: None filed. There is a potential tension between the "reasoning more,
  fewer tool calls" behavior of Opus 4.7 (Claim 13) and the RAG→Grep→progressive
  disclosure search evolution described in `blog-anthropic-seeing-like-an-agent.md`
  (which implicitly assumes the model will call Grep aggressively). However, this is a
  contextual difference, not a contradiction: the progressive disclosure design gives
  the model tools to use when it decides to search; Opus 4.7 simply requires explicit
  prompting to trigger aggressive search rather than defaulting to it. The fix described
  here (explicit guidance on when/why to use tools) is consistent with the design intent
  documented there. No contradiction issue needed.

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` — Adds the precise per-model
    spawning heuristic (Claim 15) that the coordination patterns post omits. That post
    describes orchestrator-subagent as the default architecture; this post specifies the
    Opus 4.7 behavioral rule for executing that architecture correctly.
  - `blog-anthropic-session-management-1m-context.md` — Adds model-specific session
    structuring guidance that the session management post (general across model versions)
    does not provide. The delegation-over-pair-programming framing here is the Opus 4.7
    instantiation of the general session management advice.
  - `blog-anthropic-seeing-like-an-agent.md` — The "treat Claude like a capable engineer
    you delegate to" posture (Claim 9) is the user-facing complement to the "see like an
    agent" design principle there. That post tells tool designers to match tools to model
    capabilities; this post tells practitioners to match their interaction patterns to
    model capabilities.

- **Novel**:
  - **Five-level effort taxonomy with per-level guidance**: No prior corpus source names
    all five effort levels (low, medium, high, xhigh, max) with explicit per-level
    recommendations and tradeoff profiles. `xhigh` is a new named level introduced with
    Opus 4.7.
  - **Adaptive thinking as a named mechanism replacing fixed budgets**: The explicit
    statement that fixed extended_thinking budgets are NOT supported in Opus 4.7 is a
    breaking-change notification not present in any prior corpus source.
  - **Prompt-based thinking rate control patterns**: The two specific prompt patterns
    ("Think carefully and step-by-step" / "Prioritize responding quickly") as the
    replacement interface for numeric thinking budget control are new to the corpus.
  - **Three 4.6→4.7 behavioral change notifications**: The specific changes to response
    length calibration, tool-call rate, and subagent spawning rate are first documented
    here; no prior source covers Opus 4.7 behavioral deltas.
  - **Verbatim subagent spawning rule**: The two-part rule ("Do not spawn a subagent
    for work you can complete directly in a single response. Spawn multiple subagents in
    the same turn when fanning out across items or reading multiple files.") is a precise,
    extractable system-prompt artifact new to the corpus.
  - **Self-generated hook notifications**: The pattern of asking Claude to create its
    own hook-based task-completion notifications is not documented in any other corpus
    source.
  - **xhigh as automatic default for existing Opus 4.7 users**: The automatic migration
    of effort level for existing Claude Code users is a concrete configuration change note
    not present elsewhere.

## Guide Impact

- **Chapter 02 (Harness Engineering — Model Configuration)**: Add an "Effort Level
  Selection" section anchored on the five-level taxonomy from Claim 1. Recommend `xhigh`
  as the production default for most agentic coding work (Claim 3), `high` for concurrent
  sessions (Claim 4), `max` only for deliberate ceiling evaluation (Claim 3). Add a note
  on the automatic upgrade to `xhigh` for existing Opus 4.7 users (Claim 2) as a
  migration consideration when benchmarking 4.6 vs. 4.7.

- **Chapter 02 (Harness Engineering — Thinking Configuration)**: Add a subsection on
  adaptive thinking as the replacement for fixed extended_thinking budgets (Claims 5–6).
  Document the breaking change explicitly: if a harness was setting `thinking_budget`
  for Opus 4.6, that must be removed and replaced with prompt-based control. Provide the
  two prompt patterns (Claims 7–8) as the reference implementation.

- **Chapter 02 (Harness Engineering — Subagent Orchestration)**: Update system prompt
  guidance for orchestrator agents running on Opus 4.7 to include the verbatim spawning
  rule from Claim 15. This is the most copy-pasteable artifact in the source. Pair with
  the multi-agent coordination patterns taxonomy from `blog-anthropic-multi-agent-
  coordination-patterns.md` — that post says WHEN to use orchestrator-subagent; this
  post says HOW to prompt it correctly for Opus 4.7.

- **Chapter 04 (Context Engineering — Session Structuring)**: Add delegation-first
  session structuring as a named pattern for Opus 4.7 (Claims 9–10). Contrast with the
  interactive pair-programming mode that prior models supported more naturally. Present
  the four-item checklist (Concrete Artifacts: Session Structuring Checklist) as an
  actionable setup guide. Cross-reference `blog-anthropic-session-management-1m-context.md`
  for the five-tool decision table — the two posts together form the complete session
  management guidance for Opus 4.7.

- **Chapter 06 (Prompt Engineering)**: Add the positive-examples-over-negative-
  constraints principle (Claim 12) as a named prompt-engineering heuristic. This is
  portable across domains: style, length, format, persona — wherever a practitioner is
  currently using negative constraints ("don't do X"), a positive example is likely
  more effective.

- **Chapter 04 or Chapter 02 (Behavioral Defaults)**: Add a "4.6 → 4.7 migration
  checklist" section using the three behavioral change descriptions (Concrete Artifacts:
  Opus 4.6→4.7 Behavioral Change Summary). Frame as: if you carefully tuned your system
  prompt for Opus 4.6, you may need to update it for these three defaults. Provide the
  per-change fixes.

## Extraction Notes

- The article is a short, dense practitioner guide (~1,000 words, 5-minute read).
  All sections were read in full. There are no sub-pages or linked content requiring
  follow-up — the related articles sidebar links to separate posts already in the corpus
  or in queue.
- The post explicitly references a companion "Opus 4.7 prompting guide" linked in the
  final section ("Learn more in our Opus 4.7 prompting guide") — this companion guide
  may warrant a separate source submission if it exists and is published.
- The post does not specify whether the API silently ignores a fixed `thinking_budget`
  parameter on Opus 4.7 or returns an error. Practitioners migrating from Opus 4.6
  should test this specifically. The source says the parameter "is not supported" but
  does not clarify the failure mode.
- The `registry/sources.json` file contains an empty schema (`{"sources": {},
  "last_updated": null}`). Per standing instructions, it was left unchanged.
- Three separate Prospector triage comments appear on the issue — all three are
  consistent on novelty (high), type (blog-post, first-party), and chapters (Ch02,
  Ch04, Ch05/Ch06). All key extraction targets across the three triage comments were
  found in the source.
