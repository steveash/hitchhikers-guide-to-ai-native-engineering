---
source_url: https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything
source_type: blog-post
title: "Lessons from Building Claude Code: Prompt Caching Is Everything"
author: Thariq Shihipar (Technical Staff, Claude Code team, Anthropic)
date_published: 2026-04-30
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: settled
issue: "#478"
---

# Lessons from Building Claude Code: Prompt Caching Is Everything

> First-party operational account from the Claude Code team on six specific design
> patterns they use to maintain high prompt cache hit rates in production — including
> the forked-call compaction architecture, the EnterPlanMode cache-preservation design,
> and the `defer_loading: true` stub pattern — motivated by the team declaring SEVs
> when cache hit rates drop.

## Source Context

- **Type**: blog-post (official claude.com blog, April 30, 2026)
- **Author credibility**: Thariq Shihipar is Technical Staff on the Claude Code team at
  Anthropic — the team that ships Claude Code. This is not a practitioner post or a
  research post; it is an operational retrospective from engineers who built and operate
  the system. Claims about internal architecture, design decisions, and monitoring practice
  are authoritative. The post names concrete pitfalls (timestamps in static prompts,
  non-deterministic tool ordering, tool parameter updates) that caused real cache breaks in
  production, and describes the compaction and Plan Mode designs from the inside.
- **Scope**: Covers seven operational patterns for prompt cache optimization in Claude Code:
  the 4-layer prompt hierarchy, the `<system-reminder>` update pattern, model stability, tool
  stability, Plan Mode design, deferred tool loading, and compaction fork architecture. Includes
  five distilled lessons. Does NOT cover multi-agent orchestration, evaluator design, cost
  accounting, or any topic outside caching and compaction.

## Extracted Claims

### Claim 1: The Claude Code team structures prompts in a 4-layer hierarchy with static content first to maximize cache hit rate

- **Evidence**: First-party architectural description of the production system. The four layers
  are named and ordered by cache scope: (1) static system prompt & tools — globally cached;
  (2) CLAUDE.md — cached within a project; (3) session context — cached within a session;
  (4) conversation messages.
- **Confidence**: settled (first-party, describes the production system)
- **Quote**: "we build our entire harness around prompt caching"
- **Our assessment**: The 4-layer hierarchy is the canonical structure for Claude Code. Practitioners
  building their own harnesses should adopt this ordering. Each layer is separated by its cache
  scope — global, project, session, turn. Putting CLAUDE.md at layer 2 rather than layer 1 means
  project-specific context updates don't invalidate the global system prompt cache. The specific
  naming of the four layers is more precise than the "static first, dynamic last" formulation in
  existing notes.

### Claim 2: The 4-layer hierarchy is "surprisingly fragile" — real production cache breaks were caused by timestamps in static prompts, non-deterministic tool ordering, and tool parameter updates mid-session

- **Evidence**: First-party account of real cache-break incidents at Anthropic. Three specific
  causes are named from production failures.
- **Confidence**: settled (first-party report of actual production incidents)
- **Quote**: "This approach can be surprisingly fragile"
- **Our assessment**: This is the most operationally useful claim in the post for practitioners.
  The three pitfalls are non-obvious: adding a session timestamp to the system prompt for
  logging purposes busts the cache on every turn. Non-deterministic tool ordering implies that
  tool lists must be sorted or otherwise deterministically ordered in the harness, not left to
  dictionary iteration order. These bugs appear to work in light testing but degrade at scale.

### Claim 3: Dynamic information should be injected as `<system-reminder>` tags in the next user message or tool result, not by updating the system prompt

- **Evidence**: First-party description of the pattern Claude Code uses in production for
  conveying time-sensitive or file-changed information while preserving the cached prefix.
- **Confidence**: settled (first-party, describes actual Claude Code production pattern)
- **Quote**: "Claude Code uses a `<system-reminder>` tag in the next user message or tool result"
- **Our assessment**: Modifying the system prompt creates a new cache prefix and invalidates the
  entire cache; appending to the message stream does not. The `<system-reminder>` tag is a naming
  convention that lets the model recognize that this information is injected context, not user
  input — preventing confusion between harness-injected reminders and actual user messages. The
  pattern is empirically observable in Claude Code's own prompts during sessions.

### Claim 4: Switching models mid-session can cost MORE than staying on the expensive model because the prompt cache must be rebuilt for the new model

- **Evidence**: First-party analysis with a concrete example. At 100k tokens into a conversation
  with Opus, switching to Haiku to answer an easy question costs more than having Opus answer,
  because the Haiku prompt cache doesn't exist and must be rebuilt from scratch.
- **Confidence**: settled (first-party, economically valid given prompt caching pricing mechanics)
- **Quote**: "if you're 100k tokens into a conversation with Opus and want to ask a question
  that is fairly easy to answer, it would actually be more expensive to switch to Haiku than to
  have Opus answer, because we would need to rebuild the prompt cache for Haiku"
- **Our assessment**: This is counterintuitive and directly actionable. The standard assumption
  "route cheap tasks to cheap models to save money" fails mid-session under prompt caching: the
  switching cost (rebuilding the cache) can exceed the inference cost savings. The correct pattern
  for model routing is subagents — a new subagent starts with no inherited cache state, so it pays
  its own cache-fill cost once without busting the parent session's cache.

### Claim 5: Adding or removing tools mid-session invalidates the cache for the entire conversation because tools are part of the cached prefix

- **Evidence**: First-party architectural description. Tools appear in the API call as part of
  the prefix; any change to the tool list changes the prefix, invalidating everything downstream
  of the change point.
- **Confidence**: settled (first-party, consistent with how prefix caching works)
- **Quote**: (described in context of the Plan Mode design section as the motivation for the
  EnterPlanMode/ExitPlanMode tool design)
- **Our assessment**: Any harness feature that dynamically modifies the tool set between turns
  (context-dependent tool loading, security-based tool removal, task-adaptive tool gating) busts
  the cache on every transition. This constraint is what motivated the Plan Mode tool design
  (Claim 6) and the `defer_loading` stub pattern (Claim 7).

### Claim 6: EnterPlanMode and ExitPlanMode are tools the model can call itself, keeping all tools in the request at all times — this prevents cache breaks AND enables autonomous mode entry

- **Evidence**: First-party description of the Claude Code Plan Mode design, including the
  specific reason (cache preservation) and the emergent benefit (autonomous mode entry).
- **Confidence**: settled (first-party, describes the actual shipped design)
- **Quote**: "we keep _all_ tools in the request at all times and use EnterPlanMode and ExitPlanMode
  as tools themselves...because EnterPlanMode is a tool the model can call itself, it can
  autonomously enter plan mode when it detects a hard problem, without any cache break."
- **Our assessment**: The dual benefit is worth emphasizing separately: (1) cache preservation —
  no tool-set change on mode transition, so the cache is never invalidated; (2) autonomous mode
  entry — because the tool is always present, the model can enter plan mode on its own judgment
  without waiting for the harness to reconfigure. The second benefit (autonomy) is the more
  powerful operational outcome, but it is only possible because of the first (cache stability).
  This is a concrete instance of the general principle: design for cache stability, and autonomous
  capability emerges as a side effect.

### Claim 7: MCP tools loaded as lightweight stubs with `defer_loading: true` enable the model to discover full schemas on demand without changing the cached prefix

- **Evidence**: First-party description of Claude Code's production MCP tool loading strategy
  for handling dozens of MCP tools without token bloat.
- **Confidence**: settled (first-party, describes the actual shipped mechanism)
- **Quote**: "lightweight stubs (just the tool name, with `defer_loading: true`) that the model
  can 'discover' via tool search when needed. The full tool schemas are only loaded when the
  model selects them."
- **Our assessment**: This is the authoritative answer to the MCP token cost problem documented in
  `blog-bswen-mcp-token-cost.md`. Bswen showed that loading 15 MCP servers upfront consumed 100k
  tokens before any user input. The `defer_loading: true` stub pattern is the production solution:
  the stub costs only a tool name in the prefix (near-zero tokens), while the full schema is fetched
  on demand when the model selects the tool. The cache remains stable because the stub is always
  present in the same position; only the tool-call response includes the full schema.

### Claim 8: Compaction must use the exact same prefix as the parent conversation — the naive approach of using a separate summarization call breaks the cache entirely

- **Evidence**: First-party description of the Claude Code compaction design, explicitly
  contrasting the correct (forked) approach against the naive (divergent) approach.
- **Confidence**: settled (first-party, describes the actual shipped mechanism)
- **Quote**: "When we run compaction, we use the _exact same_ system prompt, user context,
  system context, and tool definitions as the parent conversation...From the API's perspective,
  this request looks nearly identical to the parent's last request—same prefix, same tools,
  same history—so the cached prefix is reused."
- **Our assessment**: This is the first-party confirmation of the forked-call compaction mechanism
  described from external code inspection in `research-wasnotwas-context-compaction.md`. The key
  implementation detail: the compaction call prepends the parent messages, then appends the
  compaction prompt as a new user message. The only "new" tokens are the compaction instruction
  itself and the summary output — the entire prefix is cached. A "compaction buffer" (reserved
  token budget for the compact message and summary output tokens) must be maintained by the harness.

### Claim 9: Anthropic monitors prompt cache hit rate for Claude Code like uptime and declares SEVs if it drops too low

- **Evidence**: First-party operational disclosure about internal monitoring practice at Anthropic.
- **Confidence**: settled (first-party operational disclosure)
- **Quote**: "we run alerts on our prompt cache hit rate and declare SEVs if they're too low"
- **Our assessment**: SEV-level (Service Event / Incident) alerting on cache hit rate means cache
  failures are treated as production outages, not optimization opportunities. The practical
  implication for harness builders: if the team that ships Claude Code treats cache hit rate as
  incident-worthy, practitioners building their own harnesses should treat it as a first-class
  operational metric, not an afterthought.

### Claim 10: Fork operations (compaction, summarization, skill execution) must share the parent's prefix to avoid paying full cache-rebuild cost

- **Evidence**: Stated as the fifth and final distilled lesson from the article. Covers the
  general pattern beyond just compaction.
- **Confidence**: settled (first-party principle)
- **Quote**: "Fork operations need to share the parent's prefix."
- **Our assessment**: This generalizes the compaction insight (Claim 8) to any parallel or
  branching API call. A harness that spawns a skill-execution call using a different system prompt
  or different tools than the parent pays full cache-rebuild cost on that fork. The discipline:
  all forked calls should inherit the parent's prefix (system prompt, tools, conversation history),
  with only the fork-specific instruction appended as a new message. This affects multi-agent
  harness design broadly, not just compaction.

## Concrete Artifacts

### The 5 Distilled Lessons from the Claude Code Team

```
# Five operational lessons from the Claude Code team
# Source: "Lessons from Building Claude Code: Prompt Caching Is Everything"
# Author: Thariq Shihipar (Technical Staff, Claude Code team), April 30, 2026

Lesson 1: Prompt caching is a prefix match. Any change anywhere in the
          prefix invalidates everything after it.

Lesson 2: Use messages instead of system prompt changes.
          (Inject <system-reminder> in the message stream for dynamic info)

Lesson 3: Don't change tools or models mid-conversation.
          (Use subagents for model routing; keep tool sets stable)

Lesson 4: Monitor your cache hit rate like you monitor uptime.
          (Anthropic declares SEVs if cache hit rates are too low)

Lesson 5: Fork operations need to share the parent's prefix.
          (Compaction, summarization, skill calls: same prefix, append only)
```

### 4-Layer Prompt Hierarchy

```
# Claude Code prompt structure ordered by cache scope
# Source: Thariq Shihipar, April 30, 2026

Layer 1: Static system prompt & Tools     → globally cached
Layer 2: CLAUDE.md                        → cached within a project
Layer 3: Session context                  → cached within a session
Layer 4: Conversation messages            → per-turn (dynamic tail)

Rule: Static content first, dynamic content last.
      Each layer is ordered by how frequently it changes.
```

### Compaction Fork Mechanism

```
# Cache-safe compaction call construction
# Source: Thariq Shihipar, April 30, 2026

WRONG (naive — breaks cache entirely):
  system_prompt = "You are a summarizer. Summarize this conversation."
  messages      = [full conversation history]
  # Diverges immediately from parent prefix → cache miss on all subsequent turns

CORRECT (forked — reuses cache):
  system_prompt = <exact same as parent conversation>
  tools         = <exact same as parent conversation>
  messages      = [parent messages]
               + [{"role": "user", "content": "<compaction_prompt>"}]
  # API sees same prefix as parent → cached prefix is reused

NOTE: Reserve a "compaction buffer" in the token budget for:
  - The compaction instruction message (small, but must fit)
  - The summary output tokens (proportional to context length)
```

### Production Cache Break Pitfalls

```
# Real production cache invalidation causes identified by the Claude Code team
# Source: Thariq Shihipar, April 30, 2026

1. Timestamp in static system prompt
   Problem:  Regenerates on every request → cache miss every turn
   Fix:      Move time-sensitive info to <system-reminder> in message stream

2. Non-deterministic tool ordering
   Problem:  Tool list order varies between calls → prefix changes → cache miss
   Fix:      Sort or otherwise deterministically order all tool definitions

3. Updating tool parameters mid-session
   Problem:  Tool definition change → full conversation cache invalidated
   Fix:      Use defer_loading:true stubs; load full schemas only at selection
```

### defer_loading Stub Pattern

```
# MCP tool loading with defer_loading: true
# Source: Thariq Shihipar, April 30, 2026

STUB (always in prefix — costs approximately one tool name in tokens):
  { "name": "tool_name", "defer_loading": true }

FULL SCHEMA (loaded only when model selects the tool via tool_search):
  { "name": "tool_name", "description": "...", "input_schema": {...} }

Effect: Dozens of MCP tools can be listed as stubs without token bloat.
        Prefix stays stable across turns → high cache hit rate preserved.
        Model uses tool_search to discover which tools it needs.
```

### EnterPlanMode / ExitPlanMode Design Rationale

```
# Plan Mode cache-preserving design
# Source: Thariq Shihipar, April 30, 2026

WRONG (breaks cache on every mode transition):
  entering_plan_mode:
    remove: [all action tools]
    add:    [plan-only tools]
  exiting_plan_mode:
    remove: [plan-only tools]
    add:    [all action tools]

CORRECT (keeps all tools always present):
  tools: [EnterPlanMode, ExitPlanMode, ... all other tools ...]
  # Mode transitions are tool calls, not tool-set changes
  # Dual benefit:
  #   1. Cache never invalidated on mode switch
  #   2. Model can autonomously enter plan mode on its own judgment
```

## Cross-References

- **Corroborates**: `research-wasnotwas-context-compaction.md` — the wasnotwas post described
  the Claude Code compaction mechanism from external code inspection: "Claude Code forks a cached
  call to summarize, then resumes with the summary in place of original messages, preserving the
  existing KV cache." This article is the first-party confirmation of exactly that description,
  adding the WHY (same prefix = API reuses cached KV) and the full HOW (identical system prompt,
  tools, and parent messages, with only the compaction instruction appended). The corroboration
  is near-exact.

- **Corroborates**: `blog-anthropic-harnessing-claude-intelligence.md` — Claims 10-13 in that
  note (static-first ordering, `<system-reminder>`, no model switching, tool search for dynamic
  discovery) overlap with this article and are fully consistent. Both are first-party Anthropic
  posts that agree on the caching principles. This article provides the operational depth
  (4-layer hierarchy with named cache scopes, production pitfalls, SEV monitoring, compaction
  fork mechanics, `defer_loading` pattern) absent from the harnessing post.

- **Corroborates**: `failure-cursor-ultra-billing-cache-explosion.md` — throwawayround's billing
  disaster (4k user tokens billed as 21M cache tokens) is the real-world consequence of the
  design failures this article documents. Cache depth grew unbounded without the discipline this
  post prescribes (static-first ordering, tool stability, proper compaction). This article
  provides the positive patterns; the Cursor failure note provides the negative example.

- **Extends**: `research-wasnotwas-context-compaction.md` — adds the first-party design
  rationale and implementation intent behind the forked compaction. Wasnotwas observed the
  mechanism from source code; this post explains WHY it works (prefix reuse) and adds the
  compaction buffer concept missing from the external account.

- **Extends**: `blog-bswen-mcp-token-cost.md` — Bswen documented MCP token bloat (15 servers
  = 100k tokens before the user types anything) and recommended pruning to 3-6 servers. This
  article provides the authoritative production solution: `defer_loading: true` stubs, so tool
  count does not translate to prefix token cost. Bswen's pruning recommendation and the
  `defer_loading` pattern are complementary: `defer_loading` removes the cost driver, reducing
  the need for aggressive pruning.

- **Extends**: `blog-anthropic-harnessing-claude-intelligence.md` — goes significantly deeper
  on each of the caching principles mentioned in that note's Claims 10-13, adding: the 4-layer
  named hierarchy with cache scopes, three concrete production pitfall causes, the `defer_loading`
  stub mechanism with exact mechanics, the Plan Mode cache-preservation design rationale, the
  compaction fork implementation, and the SEV monitoring disclosure.

- **Novel**: The following are new to the corpus:
  - **SEV monitoring for cache hit rate** — Anthropic declares incidents over cache miss rates.
    No other source discloses this monitoring practice or its operational stakes.
  - **`defer_loading: true` stub mechanism** — The exact field name and pattern for deferring
    MCP tool schema loading until selection time. Bswen documented the problem; this is the
    first-party solution.
  - **EnterPlanMode/ExitPlanMode cache-preservation design** — The dual benefit (cache stability
    + autonomous mode entry) of making mode transitions tool calls rather than tool-set swaps,
    described here with explicit design rationale for the first time.
  - **Compaction buffer concept** — The requirement to reserve token budget in the context window
    for the compaction instruction and summary output tokens.
  - **Three specific production cache break pitfalls** — Named from real Claude Code incidents:
    timestamps in static prompts, non-deterministic tool ordering, tool parameter updates.
  - **4-layer hierarchy by cache scope** — More precise than "static first, dynamic last."
    Separates global / project / session / turn cache scopes as distinct, named layers.
  - **Fork operations must share parent prefix** — Generalized principle covering compaction,
    summarization, and skill execution. No prior source states this at the level of a principle.

## Guide Impact

- **Chapter 04 (Context Engineering — caching architecture)**: This article should anchor a
  "Prompt Caching Architecture" section. The 4-layer hierarchy artifact (Claim 1) is the canonical
  prompt structure. The five distilled lessons are the takeaways. The production pitfall list
  (Claim 2) should become the "common mistakes" sub-section.

- **Chapter 04 (Context Engineering — compaction)**: Update the compaction section to cite this
  article's first-party confirmation of the forked-call mechanism (Claim 8), adding the compaction
  buffer concept as a practical note for harness builders. Pair with `research-wasnotwas-context-
  compaction.md` which provides the external corroboration and cost-per-compaction data.

- **Chapter 04 (Context Engineering — model routing)**: Update the subagent/model-routing section
  with the model-switching cost trap (Claim 4) and the 100k-token example. The standard "route
  cheap tasks to cheap models" advice is incorrect for mid-session switching; the guide should
  say: use subagents for model routing, never switch the model mid-session.

- **Chapter 02 (Harness Engineering — tool design)**: Add the `defer_loading: true` pattern
  (Claim 7) as the production solution to MCP token bloat. Pair with Bswen's token measurements
  for the cost context. Add the tool-stability constraint (Claim 5) as a design rule: dynamic
  mid-session tool loading is a cache-busting anti-pattern.

- **Chapter 02 (Harness Engineering — mode transitions)**: Cite the EnterPlanMode/ExitPlanMode
  design (Claim 6) as the canonical pattern for mode switching without cache invalidation. Frame
  the dual benefit: cache stability enables autonomous mode entry.

- **Chapter 02 (Harness Engineering — observability)**: Add prompt cache hit rate as a first-class
  operational metric (Claim 9). If the Claude Code team declares SEVs over cache hit rates,
  practitioners should at minimum measure and alert on it.

## Extraction Notes

- The article is on claude.com/blog (consumer domain), not anthropic.com/engineering, but the
  author (Thariq Shihipar, Technical Staff, Claude Code team) and content (operational account
  of the shipped system) place it in the same authority category as Anthropic Engineering Blog posts.
- The `<system-reminder>` tag referenced in Claim 3 is the same tag used in this extraction
  session by the Claude Code harness — the pattern is empirically observable in the tooling.
- The `defer_loading: true` field is a Claude Code/MCP-specific implementation detail requiring
  harness support; it is not a prompt-only technique.
- The compaction buffer is mentioned in the article but not quantified. Harness builders must
  determine the right buffer size experimentally for their context lengths.
- No sub-pages were linked from the article. The article is self-contained and was read in full.
- No contradiction was found with existing notes. Claims 10-13 of `blog-anthropic-harnessing-
  claude-intelligence.md` cover the same caching principles from a different (broader) angle and
  are fully consistent. No contradiction issue is needed.
