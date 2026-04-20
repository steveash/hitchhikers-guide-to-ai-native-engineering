---
source_url: https://claude.com/blog/harnessing-claudes-intelligence
source_type: blog-post
title: "Harnessing Claude's Intelligence"
author: Lance Martin (Anthropic Claude Platform team)
date_published: 2026-04-02
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: settled
issue: "#192"
---

# Harnessing Claude's Intelligence

> Authoritative first-party Anthropic post presenting three benchmark-backed
> patterns for agent harness design — use familiar tools, delegate orchestration
> and context management to the model itself, and set deliberate boundaries —
> with the BrowseComp and SWE-bench numbers that quantify each.

## Source Context

- **Type**: blog-post (official claude.com blog, April 2026)
- **Author credibility**: Lance Martin is technical staff on the Anthropic Claude
  Platform team. Acknowledgements list 13 named Anthropic engineers and PMs,
  including Barry Zhang, David Hershey, and Lydia Hallie, indicating team-level
  review. This is a first-party policy document on how to harness Claude, not a
  practitioner write-up. Claims about model behavior (BrowseComp benchmarks,
  SWE-bench figures, caching mechanics) are authoritative for Claude-specific
  behavior. Design recommendations carry vendor weight.
- **Scope**: Covers agent harness architecture decisions across three areas:
  tool selection, context delegation, and boundary setting. Uses BrowseComp
  (web browsing ability) and BrowseComp-Plus as benchmarks throughout.
  References Pokémon game as a qualitative memory quality illustration.
  Does NOT cover multi-agent safety, cost accounting methodology, specific
  CLAUDE.md authoring, or SDK-level API patterns. The article is intentionally
  high-level — links to a github "claude-api skill" for implementation details.

## Extracted Claims

### Claim 1: Building on tools Claude was trained on (bash + text editor) is sufficient for state-of-the-art performance on code tasks

- **Evidence**: SWE-bench Verified benchmark. Claude 3.5 Sonnet achieved 49%
  on SWE-bench Verified using only bash and text editor tools — which the author
  states was state-of-the-art at that time (late 2024).
- **Confidence**: settled (named benchmark with specific score; first-party claim)
- **Quote**: "Claude 3.5 Sonnet achieved 49% on SWE-bench Verified — state of
  the art at the time — with just a bash tool and a text editor tool."
- **Our assessment**: The claim is not merely "simple tools work" — it is that
  *familiar* tools work best. The argument is that Claude's training data
  contains extensive bash and text-editor usage patterns, so the model's implicit
  priors about what these tools do are accurate. Novel or custom tools require
  the harness to teach Claude new behavior; familiar tools exploit what the model
  already knows. This is a strong argument against over-engineering custom tool
  ecosystems. The 49% figure is the strongest point-in-time anchor we have for
  "minimal tooling, maximal results."

### Claim 2: Agent Skills, programmatic tool calling, and the memory tool are all compositions of bash and text editor

- **Evidence**: Architectural description from a first-party Anthropic author.
  The claim is that the higher-level constructs Claude Code uses are built on
  these two primitives, not on separate mechanisms.
- **Confidence**: settled (first-party architectural statement)
- **Quote**: "Agent Skills, programmatic tool calling, and the memory tool are
  all compositions of these two tools."
- **Our assessment**: This reframes the skills/tool ecosystem as derivative rather
  than additive. Practitioners who understand bash + text editor understand the
  full foundation. It also explains why skills can be as simple as a YAML file
  read via the text editor — there is no magic mechanism; the model reads a file
  and acts on the content, using the same text-editor tool it already knows.

### Claim 3: Giving Claude a code-execution tool to filter its own tool outputs improves BrowseComp accuracy from 45.3% to 61.6%

- **Evidence**: BrowseComp benchmark with Opus 4.6. The scenario compared:
  (a) routing all tool outputs through Claude's context window vs. (b) giving
  Claude a bash/REPL tool to write filtering logic that extracts only the
  relevant column/data before it enters context. The 16.3 percentage-point
  improvement is attributed to reduced token consumption and allowing Claude to
  decide what to keep.
- **Confidence**: settled (first-party benchmark with specific model version and
  percentage-point delta)
- **Quote**: "On BrowseComp, giving Opus 4.6 the ability to filter tool outputs
  improved accuracy from 45.3% to 61.6%."
- **Our assessment**: This is the strongest single benchmark claim in the post
  and the one most directly actionable. The pattern inverts the standard harness
  assumption: instead of the harness deciding what to pass to the model, the
  model writes code to decide what to keep. The cost benefit is double — fewer
  tokens in context (cost) plus the model makes better filtering decisions than
  a static harness rule (quality). The mechanism is general: any harness that
  routes large tool results through context should consider whether a REPL/bash
  tool could let Claude filter first.

### Claim 4: Skills provide progressive disclosure — YAML frontmatter summaries pre-loaded in context, full content read on demand

- **Evidence**: Architectural description from the author. Skills are described
  as having YAML frontmatter summaries held in context, with the full skill
  content disclosed progressively via file-read tool calls when Claude determines
  it needs the details.
- **Confidence**: settled (first-party architectural description of a shipping
  Claude Code feature)
- **Quote**: "Skills provide YAML frontmatter summaries in context; full skill
  content disclosed progressively via file-read tool calls."
- **Our assessment**: This is the mechanism behind why loading many skills does
  not proportionally expand context cost — only the summaries live in context,
  not the full bodies. The model decides which skills to read fully based on the
  task. This is a pull-on-demand pattern rather than push-all-upfront. The
  implication for harness design is significant: large instruction libraries can
  be made context-efficient by indexing with summaries and letting the model
  retrieve what it needs. Compare with the standard pattern of loading all
  instructions at session start.

### Claim 5: Context editing — removing stale tool results and thinking blocks — is a first-class harness pattern

- **Evidence**: Described as one of the three approaches to letting Claude manage
  its own context. The author treats it alongside skills and subagents as an
  architectural choice, not a workaround.
- **Confidence**: settled (first-party pattern description)
- **Quote**: "Context editing: selectively remove stale context like old tool
  results or thinking blocks."
- **Our assessment**: The explicit inclusion of "thinking blocks" as removable
  context is notable — extended thinking generates substantial token overhead that
  can be pruned once the thinking has been acted on. This is not widely
  documented. The pattern aligns with the harness-long-running source's observation
  that stale intermediate state degrades model coherence.

### Claim 6: Spawning subagents (fresh context windows) improved BrowseComp accuracy by 2.8% with Opus 4.6

- **Evidence**: BrowseComp benchmark with Opus 4.6 comparing single-agent vs.
  subagent-spawning configurations. The 2.8% improvement is presented as evidence
  that subagents for isolated task work yield measurable quality gains.
- **Confidence**: settled (first-party benchmark, specific delta)
- **Quote**: "With Opus 4.6, using subagents improved BrowseComp results by 2.8%
  over single-agent runs."
- **Our assessment**: The 2.8% lift is modest compared to the 16.3pp gain from
  code-execution filtering (Claim 3), but it validates the subagent pattern as a
  real (not just theoretical) quality lever. The framing is important: subagents
  are described as giving Claude "fresh context windows for isolated task work"
  — not as parallelism or load distribution, but as context hygiene. A subagent
  that handles a bounded subtask cleanly avoids contaminating the main agent's
  context with irrelevant intermediate state.

### Claim 7: Compaction performance scales with model generation — Sonnet 4.5 flat at 43%; Opus 4.5 reaches 68%; Opus 4.6 reaches 84% on BrowseComp

- **Evidence**: BrowseComp benchmark run at varying compaction budgets across
  three models. The finding is that the ability to benefit from increased
  compaction budget is a model-generation property, not a harness configuration
  knob. Sonnet 4.5 cannot leverage more compaction budget; Opus 4.6 can.
- **Confidence**: settled (first-party benchmark across three named model versions)
- **Quote**: "Sonnet 4.5 remained at 43% regardless of compaction budget; Opus
  4.5 scaled to 68%; Opus 4.6 reached 84%."
- **Our assessment**: This is the clearest evidence in the corpus that context
  management capability is a model-generation property. The implication for
  practitioners is direct: throwing more compaction budget at Sonnet 4.5 is
  wasted configuration effort. If your task requires high compaction performance,
  model selection matters. The progression also provides the best-available
  Anthropic-published data on absolute BrowseComp capability: 43% / 68% / 84%
  is a ladder that practitioners can use to calibrate task complexity against
  model choice.

### Claim 8: A memory folder (Claude writes context to files, reads as needed) lifted Sonnet 4.5 BrowseComp-Plus from 60.4% to 67.2%

- **Evidence**: BrowseComp-Plus benchmark with Sonnet 4.5. The "memory folder"
  pattern gives the model a directory to write notes to and read from, replacing
  external retrieval infrastructure with the model's own file I/O.
- **Confidence**: settled (first-party benchmark, named model, specific delta)
- **Quote**: "On BrowseComp-Plus, giving Sonnet 4.5 a memory folder lifted
  accuracy from 60.4% to 67.2%."
- **Our assessment**: The 6.8pp lift from a memory folder is significant for
  Sonnet 4.5 — a model that cannot benefit from compaction budget (Claim 7).
  This means the memory folder is effectively a workaround that extends the
  practical reach of smaller models on long-horizon tasks. The pattern is also
  infrastructure-light: no retrieval system, no vector database, just a
  directory the model can write and read. The harness only needs to mount a
  directory; Claude handles the read/write pattern itself.

### Claim 9: Opus 4.6 memory quality is qualitatively superior to Sonnet 3.5 on the same long-running task

- **Evidence**: Pokémon game experiment run at 14,000 steps. Both models had
  memory folder access. Sonnet 3.5 produced 31 files with redundant information;
  Opus 4.6 produced 10 files in organized directories with tactical learnings
  and three gym badges completed.
- **Confidence**: emerging (single qualitative comparison; no controlled ablation)
- **Quote**: "Sonnet 3.5: 31 files including duplicates about caterpillar Pokémon,
  still in second town. Opus 4.6: 10 organized files in directories, three gym
  badges, tactical learnings file."
- **Our assessment**: The Pokémon example is the most memorable concrete
  illustration in the post. The Sonnet 3.5 memory output (caterpillar Pokémon
  facts classified as "crucial for future encounters") vs. the Opus 4.6 output
  (spin tile maze navigation notes, bag limit, combo strategies) shows a
  difference in what the model considers worth storing. Opus 4.6 is storing
  actionable strategic knowledge; Sonnet 3.5 is storing encyclopedic facts.
  This is a qualitative difference in task-relevant compression, not just
  organization. For harness authors: memory quality is model-dependent and may
  require model upgrade rather than prompt tuning to fix.

### Claim 10: Cache hits require static content before dynamic content — ordering is the primary lever

- **Evidence**: Caching principles table in the article. Cached tokens cost 10%
  of base input tokens. The ordering principle (static system prompt and tool
  definitions first, dynamic user content and tool results last) is the first
  listed and described as the foundational principle for cache hit maximization.
- **Confidence**: settled (first-party description of Claude caching mechanics)
- **Quote**: "Order requests so stable content (system prompt, tools) comes
  first; dynamic content (user messages, tool results) comes last."
- **Our assessment**: This is well-known in theory but frequently violated in
  practice when prompts are assembled dynamically. The key implication is that
  tools listed in the API call are part of the cacheable prefix — any change to
  the tool list busts the cache. This matters especially for harnesses that
  dynamically add/remove tools based on task context.

### Claim 11: Appending `<system-reminder>` tags in messages rather than editing the system prompt preserves cache hits for mid-session updates

- **Evidence**: Caching principles table. Listed as "Messages for updates."
  Editing the system prompt creates a new cache prefix; appending to the message
  array does not.
- **Confidence**: settled (first-party caching mechanic)
- **Quote**: "Append `<system-reminder>` in messages instead of editing prompt."
- **Our assessment**: This is a concrete implementation pattern that many
  practitioners will not discover without being told explicitly. The cost of
  missing it is full cache invalidation on every mid-session instruction update.
  The pattern: if you need to update Claude's instructions during a session,
  inject into the message stream rather than rewriting the system prompt. The
  `<system-reminder>` tag is the convention Claude Code itself uses (visible
  in this very conversation) — so the pattern has first-party validation.

### Claim 12: Switching models mid-session breaks the cache; use subagents with cheaper models instead

- **Evidence**: Caching principles table. Model switching changes the cache key;
  subagents with different model specifications create isolated contexts that do
  not bust the parent session's cache.
- **Confidence**: settled (first-party caching mechanic)
- **Quote**: "Don't change models — switching breaks cache; use subagents for
  cheaper models."
- **Our assessment**: This is the architectural justification for the subagent
  model-routing pattern Osmani and others recommend. The advice is not just
  "route cheap tasks to cheap models" — it is "route cheap tasks to cheap
  *subagents* to avoid breaking the expensive parent session's cache." Without
  this, a harness that intelligently downgrades to Haiku for simple subtasks
  may inadvertently make each subsequent Opus call more expensive by busting
  the prefix cache.

### Claim 13: Tool search enables dynamic tool discovery without breaking cache — adding/removing tools from the prefix does

- **Evidence**: Caching principles table. Listed as "Carefully manage tools."
  The article explicitly names tool search as the mechanism for accessing tools
  dynamically without cache invalidation.
- **Confidence**: settled (first-party pattern)
- **Quote**: "Tools in cached prefix; adding/removing invalidates cache; use
  tool search for dynamic discovery without breaking cache."
- **Our assessment**: This is an important constraint on dynamic tool
  architectures. A harness that adds tools to the tool list based on task type
  (common pattern) busts the cache every time the task type changes. The
  alternative — keeping a fixed tool list with a "search for more tools" meta-tool
  — preserves the cache at the cost of an extra tool call when the model needs
  to discover a new tool. For most workloads, the cache preservation is worth
  the extra tool call.

### Claim 14: Promoting actions to dedicated tools gives the harness action-specific hooks for security, UX, and observability

- **Evidence**: Architectural principle described with concrete examples.
  The criterion for promoting an action to a dedicated tool: (a) it needs a
  security boundary (reversibility matters), (b) it requires user-facing
  presentation (modal, options, blocking feedback), or (c) it requires
  observability (logging, tracing, replay).
- **Confidence**: settled (first-party pattern with decision criteria)
- **Quote**: "Promoting actions to dedicated tools gives the harness
  action-specific hooks with typed arguments for interception, gating, rendering,
  or auditing."
- **Our assessment**: **Reversibility is the key criterion** for security
  boundaries — the article frames hard-to-reverse actions (not just dangerous
  ones) as the candidates for dedicated tool promotion. A file delete is not
  just dangerous; it is hard to reverse. A file write is reversible via version
  control. This reversibility framing is more actionable than a danger taxonomy
  because practitioners can evaluate it at design time without enumerating all
  possible abuse cases. The file staleness check example (file write tools can
  verify the file hasn't changed since Claude last read it) shows the kind of
  tool-specific guard that becomes possible when the action is promoted to a
  typed tool.

### Claim 15: Harness components become dead weight as model capability improves — "What can I stop doing?" is the right review heuristic at each model upgrade

- **Evidence**: The author's framing via Chris Olah's "grown more than built"
  observation. The article cites context-reset logic built for "context anxiety"
  in earlier models becoming dead weight by Opus 4.5 as a concrete example.
  This extends the "bitter lesson" — compute beats inductive bias — to harness
  architecture.
- **Confidence**: settled (first-party principle; the context-anxiety example
  is concrete, though see Contradicts section)
- **Quote**: "Earlier agent versions needed context-reset logic to handle
  'context anxiety,' but Opus 4.5 exhibited no such behavior, making the resets
  'dead weight.'"
- **Our assessment**: This is the most important meta-principle in the post. It
  provides practitioners with a systematic review trigger: at every model upgrade,
  ask "What assumptions did I build into this harness that the new model no
  longer requires?" Components that compensate for limitations are load-bearing
  when those limitations exist and dead weight when they don't. The practical
  implication is a harness review checklist tied to model upgrade cadence, not
  just failure-driven refactoring. **Note**: The specific claim that Opus 4.5
  eliminated context anxiety contradicts `blog-anthropic-harness-long-running.md`,
  which found Opus 4.5 still exhibited context anxiety and Opus 4.6 eliminated
  it. See Contradicts section.

## Concrete Artifacts

### BrowseComp Benchmark Results Table

```
# BrowseComp / BrowseComp-Plus benchmark results
# Source: "Harnessing Claude's Intelligence," Lance Martin, April 2, 2026
# Model: Opus 4.6 (unless noted)

Let Claude orchestrate its own actions:
  Opus 4.6, no code execution:  45.3% BrowseComp
  Opus 4.6, with code execution: 61.6% BrowseComp
  Delta: +16.3pp

Let Claude manage its own context (subagents):
  Opus 4.6, single agent:   baseline BrowseComp
  Opus 4.6, with subagents: baseline + 2.8% BrowseComp

Let Claude persist its own context (compaction):
  Sonnet 4.5:  43%  (flat regardless of compaction budget)
  Opus 4.5:    68%
  Opus 4.6:    84%

Let Claude persist its own context (memory folder, BrowseComp-Plus):
  Sonnet 4.5, no memory folder:   60.4%
  Sonnet 4.5, with memory folder: 67.2%
  Delta: +6.8pp
```

### Pokémon Game Memory Comparison

```
# Memory file quality comparison at 14,000 game steps
# Source: "Harnessing Claude's Intelligence," Lance Martin, April 2, 2026

Sonnet 3.5 — 31 files, still in second town:
  caterpie_weedle_info:
  - Caterpie and Weedle are both caterpillar Pokémon.
  - Caterpie is a caterpillar Pokémon that does not have poison.
  - Weedle is a caterpillar Pokémon that does have poison.
  - This information is crucial for future encounters and battles.
  - If our Pokémon get poisoned, we should seek healing at a Pokémon Center
    as soon as possible.

Opus 4.6 — 10 organized files in directories, three gym badges:
  /gameplay/learnings.md:
  - Bellsprout Sleep+Wrap combo: KO FAST with BITE before Sleep Powder
    lands. Don't let it set up!
  - Gen 1 Bag Limit: 20 items max. Toss unneeded TMs before dungeons.
  - Spin tile mazes: Different entry y-positions lead to DIFFERENT
    destinations. Try ALL entries and chain through multiple pockets.
  - B1F y=16 wall CONFIRMED SOLID at ALL x=9-28 (step 14557)
```

### Cache Hit Maximization Principles

```
# Prompt caching best practices
# Source: "Harnessing Claude's Intelligence," Lance Martin, April 2, 2026
# Cached tokens cost 10% of base input tokens.

Principle              | Implementation
-----------------------|------------------------------------------------------
Static first,          | Order: system prompt → tool definitions →
dynamic last           | user messages → tool results
                       |
Messages for updates   | Inject <system-reminder> in message stream;
                       | do NOT edit the system prompt mid-session
                       |
Don't change models    | Model switching busts cache; use subagents
                       | with cheaper models instead
                       |
Carefully manage tools | Tool list changes bust cache; use tool search
                       | for dynamic discovery without invalidating prefix
                       |
Update breakpoints     | For multi-turn apps: move cache breakpoint to
                       | latest message; enable auto-caching
```

### Declarative Tool Decision Criteria

```
# When to promote an action to a dedicated typed tool
# Source: "Harnessing Claude's Intelligence," Lance Martin, April 2, 2026

Promote to a dedicated tool when the action:
  1. Requires a security boundary — especially REVERSIBILITY.
     Hard-to-reverse actions (mass delete, external sends) → dedicated tool
     with typed arguments for interception/gating.

  2. Requires user-facing presentation — modal dialogs, option selection,
     feedback that blocks execution until user responds.

  3. Requires observability — logging, distributed tracing, session replay.
     Typed tools with structured arguments produce structured logs;
     raw bash strings do not.

Example safeguard:
  File write tools → include staleness check: verify file has not changed
  since Claude last read it, to prevent overwriting concurrent edits.

Counter-example (from article):
  Claude Code auto-mode uses a second Claude to judge bash command safety —
  potentially reducing the need for dedicated tools in some contexts.
```

## Cross-References

- **Corroborates**:
  - `research-wasnotwas-context-compaction.md` — Claim 7 here (compaction scales
    with model generation: 43%/68%/84% across Sonnet 4.5/Opus 4.5/Opus 4.6) adds
    Anthropic's own first-party benchmark numbers to the compaction scaling picture.
    Wasnotwas provided the harness-level trigger thresholds and cost-per-compaction
    data; this source provides the capability-scaling data across model generations.
    Together: compaction is a budget item (wasnotwas) AND a capability property
    (this post) — both must be managed.
  - `blog-anthropic-harness-long-running.md` — Claim 15 here ("what can I stop
    doing?" / harness components become dead weight) aligns with that post's
    Claim 9 ("every component in a harness encodes an assumption about what the
    model can't do"). Both are first-party Anthropic posts making the same meta-
    principle claim from different angles: the harness-long-running post documents
    it through a specific before/after example; this post frames it as a general
    heuristic. The sprint decomposition removal in that post is an instance of the
    "what can I stop doing?" pattern described here.
  - `blog-ccunpacked-claude-code-architecture.md` — Claim 4 here (skills as
    progressive disclosure with YAML frontmatter) corroborates and extends the
    ccunpacked architecture finding. The ccunpacked note documented skills as a
    loadable module system; this post adds the first-party design rationale:
    summaries in context, full content pulled on demand. The mechanism now has
    both source-level (ccunpacked) and design-rationale (this post) backing.
  - `blog-anthropic-claude-code-auto-mode.md` — The article itself cites auto-mode
    as evidence that dedicated tools may not always be needed for safety decisions
    (a second Claude model judges command safety instead). This is the only cross-
    reference the article makes to another Anthropic engineering post.

- **Contradicts**:
  - `blog-anthropic-harness-long-running.md` on context anxiety model version:
    This post claims Opus 4.5 exhibited NO context anxiety (it was eliminated
    before Opus 4.5). The harness-long-running post claims Opus 4.5 DID exhibit
    context anxiety, and it was Opus 4.6 that eliminated it. Both are first-party
    Anthropic posts from the same 10-day window. **See contradiction issue #232
    (C-004 pending).** Do not cite either source's claim about *which* model
    eliminated context anxiety as settled until this is resolved.

- **Extends**:
  - `research-wasnotwas-context-compaction.md` — Adds the generation-level
    capability scaling data (43%/68%/84%) that wasnotwas does not have.
    Wasnotwas measured harness compaction mechanics; this post measures what
    different model generations can *do* with compaction budget. The two sources
    together provide the complete picture: when compaction fires (wasnotwas) and
    what it can achieve (this post).
  - `blog-anthropic-harness-long-running.md` — Adds the systematic review
    trigger ("what can I stop doing?" at each model upgrade) to the concrete
    before/after example in that post. The harness-long-running post shows a
    specific case; this post provides the general heuristic. Together they form
    a pattern + example pair.

- **Novel**:
  - **BrowseComp as a harness design benchmark**: BrowseComp (web browsing
    ability) is used throughout this post as the primary evaluation vehicle for
    harness design decisions. It provides a quantified signal for harness choices
    (code execution filtering, subagent spawning, compaction, memory folder) that
    no other corpus source uses. This is the first source in our corpus to show
    harness architecture choices producing percentage-point benchmark deltas.
  - **The 16.3pp BrowseComp lift from code-execution filtering** (45.3% → 61.6%)
    is the single largest quantified harness improvement in our corpus. Nothing
    else we have gives a benchmark-backed delta of this magnitude for a single
    harness design decision.
  - **The compaction generation ladder** (43%/68%/84% across Sonnet 4.5/Opus
    4.5/Opus 4.6) is new to the corpus as Anthropic's own published numbers.
    Wasnotwas documented the trigger thresholds; these are the capability outcomes.
  - **Progressive disclosure via skills** (YAML frontmatter summaries in context,
    full body pulled on demand) is documented here with the first-party design
    rationale. Ccunpacked documented the mechanism from source code; this post
    confirms it as the intended architecture.
  - **The `<system-reminder>` pattern** for mid-session instruction injection
    without cache invalidation is named explicitly for the first time. Other
    corpus sources discuss caching but not this specific implementation pattern.
  - **Tool search as cache-preserving dynamic discovery** is an explicit
    architectural recommendation that no other corpus source makes.
  - **Memory quality as model-dependent** (Pokémon comparison) is a novel
    qualitative finding: Sonnet 3.5 stores encyclopedic trivia; Opus 4.6 stores
    actionable strategy. This is distinct from quantity (31 files vs 10 files)
    — it is a difference in what the model considers worth persisting.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Claim 15 ("what can I stop doing?")
  should be added as the canonical heuristic for harness review at every model
  upgrade. Pair with the harness-long-running post's before/after example as
  the pattern + instance. Add the declarative tool promotion criteria (Claim 14)
  as the decision framework for when to use structured typed tools vs. raw bash.
  The reversibility criterion is more actionable than a danger taxonomy.

- **Chapter 03 (Agent Architecture / Orchestration)**: Claim 3 (code-execution
  filtering, 45.3% → 61.6%) should anchor any section on "what should the harness
  do vs. what should Claude do?" The answer from this source: let Claude write
  filtering logic rather than routing all tool outputs through context. The 16.3pp
  lift is the benchmark evidence. Add Claim 6 (subagents for fresh context windows,
  +2.8%) as supporting evidence for the subagent spawning pattern.

- **Chapter 04 (Tool Design)**: Claims 4 and 2 together define the tool design
  philosophy: build on bash + text editor (familiar tools), compose more complex
  capabilities from them (skills, memory), and let Claude's knowledge of the
  primitives carry the load. Resist adding novel tool mechanisms when compositions
  of familiar tools suffice.

- **Chapter 05 (Context Management)**: Claims 7 and 8 (compaction generation
  scaling and memory folder) should be the quantitative anchor for context
  management recommendations. Key guidance: (a) compaction capability is
  model-generation-dependent — don't fight Sonnet 4.5's flat compaction ceiling,
  use a memory folder instead; (b) the memory folder is infrastructure-light and
  gives a meaningful 6.8pp lift even on a smaller model. Claim 4 (skills as
  progressive disclosure) should update any "how to manage large instruction sets"
  section — summaries in context, full bodies pulled on demand.

- **Chapter 07 (Cost & Latency Optimization)**: The caching principles table
  (Claims 10-13) should be extracted as a checklist. The `<system-reminder>`
  pattern (Claim 11) and tool-search for dynamic discovery (Claim 13) are the
  two most non-obvious items — both prevent accidental cache invalidation from
  seemingly reasonable harness behaviors.

## Extraction Notes

- The article is available at claude.com/blog (not anthropic.com/engineering) —
  this is the consumer Claude blog, not the engineering blog. Despite the different
  domain, Lance Martin's affiliation and the acknowledgement list confirm this is
  first-party Anthropic engineering content.
- The article links to a "claude-api skill" on GitHub for implementation details
  but does not reproduce it. That skill was not fetched for this extraction; a
  follow-up issue could cover it.
- The `<system-reminder>` pattern referenced in Claim 11 is the same tag used
  in this extraction session by the Claude Code harness — the pattern is
  empirically observable in the tooling, not just documented in theory.
- The contradiction on context anxiety (which model eliminated it: pre-Opus-4.5
  or Opus-4.6) was filed as issue #232 and should be assigned C-004 in
  CONTRADICTIONS.md by a human or Smith resolver. Do NOT cite either side as
  settled until resolved.
- BrowseComp and BrowseComp-Plus are Anthropic benchmarks for web browsing
  ability. They are used throughout this post as harness evaluation vehicles.
  Other corpus sources (wasnotwas, french-owen, etc.) do not use BrowseComp,
  so the results here are not cross-comparable without methodology details.
- The article is 5 minutes reading time by Anthropic's estimate; the extraction
  followed all sections and the full benchmark table. No sub-pages were linked
  that required following.
