---
source_url: https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything
source_type: blog-post
title: "Lessons from building Claude Code: Prompt caching is everything"
author: Thariq Shihipar (Claude Code team, Anthropic)
date_published: 2026-04-30
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: settled
issue: "#478"
---

# Lessons from building Claude Code: Prompt caching is everything

> First-party operational account from the Claude Code team of how prompt
> caching works as a foundational design constraint — covering the 4-layer
> cache hierarchy, the cache-safe compaction fork mechanism, the
> `<system-reminder>` pattern, and the production monitoring posture
> (SEVs on cache miss).

## Source Context

- **Type**: blog-post (claude.com/blog — first-party Anthropic, written by a
  Claude Code team member)
- **Author credibility**: Thariq Shihipar is listed as technical staff on the
  Claude Code team at Anthropic. This is the definitive first-party account of
  how caching is built into Claude Code's production harness. Claims about
  architecture, design rationale, and operational practice are authoritative.
- **Scope**: Covers the full stack of caching-aware harness design decisions:
  prompt layer ordering, the `<system-reminder>` update pattern, model-switching
  cost traps, tool-set stability, Plan Mode's cache-preserving design, MCP
  `defer_loading` stubs, and cache-safe forking during compaction. Ends with a
  "Lessons learned" summary with five named principles. Does NOT cover context
  compaction quality, multi-agent coordination, or specific CLAUDE.md content.

## Extracted Claims

### Claim 1: Prompt caching makes long-running agentic products like Claude Code feasible
- **Evidence**: First-party operational statement from the Claude Code team;
  framed as the foundational premise for the entire article.
- **Confidence**: settled
- **Quote**: "Long running agentic products like Claude Code are made feasible
  by prompt caching which allows us to reuse computation from previous
  roundtrips and significantly decrease latency and cost."
- **Our assessment**: Caching is positioned not as a cost optimization but as
  the prerequisite that makes the product viable. This motivates the SEV-level
  monitoring described in Claim 12 and the depth of the design constraints
  described throughout.

### Claim 2: Claude Code structures its cached content in a four-layer hierarchy by mutability
- **Evidence**: First-party architectural description; article includes an
  explicit hierarchy diagram.
- **Confidence**: settled
- **Quote**: "Static system prompt & Tools (globally cached) | CLAUDE.md
  (cached within a project) | Session context (cached within a session) |
  Conversation messages"
- **Our assessment**: The four layers map directly to cache TTL and
  invalidation scope. Globally-cached content (system prompt + tools) survives
  across sessions; project-scoped content (CLAUDE.md) survives within a
  project; session-scoped content within a session; conversation messages are
  always dynamic. Practitioners building their own harnesses can use this
  hierarchy as a template for placing their own content.

### Claim 3: "Static content first, dynamic content last" is the foundational rule for prompt structure under prefix caching
- **Evidence**: First-party prescription from the Claude Code team; given as
  the direct answer to "how do you maximize cache hits?"
- **Confidence**: settled
- **Quote**: "The best way to do this is static content first, dynamic content
  last."
- **Our assessment**: Simple rule with large consequences when violated.
  Any harness that injects dynamic information (timestamps, file contents,
  session state) ahead of stable tool definitions will pay full-price prefill
  on every turn.

### Claim 4: Common cache-breaking pitfalls in production: timestamps in the static prompt, non-deterministic tool ordering, and updating tool parameters
- **Evidence**: First-party operational disclosure; these are described as
  actual examples Claude Code's team encountered.
- **Confidence**: settled (team's own production experience)
- **Quote**: "putting an in-depth timestamp in the static system prompt,
  shuffling tool order definitions non-deterministically, and updating
  parameters of tools."
- **Our assessment**: Each pitfall has a structural fix: timestamps go in
  `<system-reminder>` messages (Claim 5); tool ordering must be deterministic;
  tool parameter updates require the same immutability treatment as tool
  additions/removals (Claim 7). These are the canonical anti-patterns for
  the guide's Ch02 "what breaks the cache" section.

### Claim 5: Dynamic updates (timestamps, file changes) are sent via `<system-reminder>` in the next user message or tool result, preserving the cached prefix
- **Evidence**: First-party implementation pattern; described as the team's
  standard practice.
- **Confidence**: settled
- **Quote**: "we add a <system-reminder> tag in the next user message or
  tool result with the updated information for the model, which helps preserve
  the cache."
- **Our assessment**: This is the specific implementation pattern for the
  broader "use messages for updates, not system prompt edits" principle. The
  tag convention (`<system-reminder>`) is empirically observable in Claude
  Code's own harness — this article names and explains it. The practical
  trigger: "if you have the time or if the user changes a file."

### Claim 6: Switching from Opus to Haiku mid-session at 100k tokens costs more than staying on Opus, because the Haiku cache must be rebuilt from scratch
- **Evidence**: First-party cost analysis from the Claude Code team, with a
  specific scenario and explicit conclusion.
- **Confidence**: settled (team's own cost calculation)
- **Quote**: "If you're 100k tokens into a conversation with Opus and want to
  ask a question that is fairly easy to answer, it would actually be more
  expensive to switch to Haiku than to have Opus answer, because we would need
  to rebuild the prompt cache for Haiku."
- **Our assessment**: This inverts the common practitioner heuristic of
  "downgrade to a cheaper model for simpler subtasks." In long-session
  contexts, the rebuild cost of the new model's cache makes the switch
  net-negative. The correct pattern is a subagent with a handoff message —
  the subagent has its own fresh context and does not inherit or destroy the
  parent's cache.

### Claim 7: Adding or removing tools mid-session is the most common way practitioners break prompt caching
- **Evidence**: First-party operational observation; called out as "one of the
  most common ways."
- **Confidence**: settled
- **Quote**: "Changing the tool set in the middle of a conversation is one of
  the most common ways people break prompt caching. But because tools are part
  of the cached prefix, adding or removing a tool invalidates the cache for
  the entire conversation."
- **Our assessment**: Any harness that conditionally adds tools (e.g., enabling
  a "web search" tool only when the task needs it) will bust the cache on every
  task transition. The fix is either to keep the full tool set always present
  (Claim 8) or to use lightweight stubs with deferred loading (Claim 9).

### Claim 8: Claude Code's Plan Mode keeps all tools in every request and introduces EnterPlanMode/ExitPlanMode as tools — never changing the tool set
- **Evidence**: First-party architectural design rationale; described as the
  explicit lesson learned from trying to change tool sets for mode switching.
- **Confidence**: settled
- **Quote**: "we keep _all_ tools in the request at all times and use
  EnterPlanMode and ExitPlanMode as tools themselves"
- **Our assessment**: This is the canonical example of designing a product
  feature around the cache constraint rather than fighting it. Plan Mode is
  not a reduced-capability mode with fewer tools — it is a state-machine mode
  implemented via tools that are always present. Any harness author who wants
  mode-switching should adopt this pattern: model the mode as a callable tool,
  not as a change to the tool list.

### Claim 9: MCP tools are loaded as lightweight stubs with `defer_loading: true` and full schemas are fetched on demand via tool search
- **Evidence**: First-party implementation description.
- **Confidence**: settled
- **Quote**: "we send lightweight stubs (just the tool name, with
  `defer_loading: true`) that the model can 'discover' via tool search when
  needed."
- **Our assessment**: This directly addresses the MCP token bloat problem (see
  Bswen, Cross-References) without removing tools from the prefix. The stub is
  lightweight and stable; the full schema is loaded only when the model selects
  the tool. This keeps the cached prefix stable across dozens of MCP tools while
  avoiding the full token cost of loading all schemas upfront.

### Claim 10: Naive compaction (separate API call with a new "summarize this" system prompt and no tools) pays the full uncached input rate for the entire conversation
- **Evidence**: First-party cost analysis; the article describes this as "exactly
  where the cost trap is."
- **Confidence**: settled
- **Quote**: "The simplest way to do that is a separate API call with its own
  system prompt (something like 'summarize this') and no tools attached, but
  that's exactly where the cost trap is." And: "you end up paying the full,
  uncached input rate for the entire conversation you're sending in — and the
  longer the conversation (i.e., the more you need compaction in the first
  place), the more expensive that one call becomes."
- **Our assessment**: This is why the wasnotwas $0.40 per compaction call
  figure exists: naive compaction pays cold-prefill for the entire accumulated
  conversation. The irony is that the more the agent has worked (the longer the
  conversation), the more expensive compaction becomes — the cost is highest
  exactly when the need is greatest.

### Claim 11: Cache-safe forking reuses the parent conversation's cached prefix during the compaction call by using the exact same system prompt, user context, system context, and tool definitions
- **Evidence**: First-party implementation description; named as "cache-safe
  forking" in the article.
- **Confidence**: settled
- **Quote**: "When we run compaction, we use the _exact same_ system prompt,
  user context, system context, and tool definitions as the parent conversation."
  And: "From the API's perspective, this request looks nearly identical to the
  parent's last request—same prefix, same tools, same history—so the cached
  prefix is reused."
- **Our assessment**: Cache-safe forking reduces the cost of the compaction call
  itself by matching the cached prefix exactly. It is important to note that
  this optimization applies to the compaction API call — not to subsequent turns
  after compaction fires. After compaction, the new (summary-based) prefix is
  different from the original, so subsequent turns begin rebuilding a new warm
  cache from scratch. The wasnotwas note's finding that compaction "destroys the
  KV cache" describes this post-compaction effect; cache-safe forking addresses
  the in-compaction cost, not the post-compaction rebuild.

### Claim 12: The Claude Code team runs alerts on cache hit rates and declares SEVs when they fall too low
- **Evidence**: First-party operational disclosure; framed as production practice.
- **Confidence**: settled
- **Quote**: "we run alerts on our prompt cache hit rate and declare SEVs if
  they're too low."
- **Our assessment**: This establishes cache hit rate as a first-class production
  reliability metric — equivalent to uptime. The "Lessons learned" section
  echoes this with "Monitor your cache hit rate like you monitor uptime." For
  practitioners, this is the strongest possible signal that cache management
  is not a post-launch optimization but a day-one operational requirement.

## Concrete Artifacts

### Four-Layer Cache Hierarchy
```
# Claude Code prompt cache layers (globally → session → turn scope)
# Source: "Lessons from building Claude Code," Thariq Shihipar, 2026-04-30

Layer 1: Static system prompt & Tools     — globally cached (across sessions)
Layer 2: CLAUDE.md                        — cached within a project
Layer 3: Session context                  — cached within a session
Layer 4: Conversation messages            — dynamic (per turn)
```

### Cache-Breaking Pitfalls (from production experience)
```
# Common cache invalidation sources — Claude Code team's own list
# Source: "Lessons from building Claude Code," Thariq Shihipar, 2026-04-30

1. Timestamp in the static system prompt
   — Fix: inject time via <system-reminder> in the next user message

2. Non-deterministic tool ordering
   — Fix: sort tool definitions deterministically before every request

3. Updating parameters of tools mid-session
   — Fix: treat tool schemas as immutable for the session lifetime

4. Adding or removing tools mid-session
   — Fix: keep full tool set always; use EnterPlanMode/ExitPlanMode as tools
```

### Naive vs. Cache-Safe Compaction
```
# Compaction cost comparison
# Source: "Lessons from building Claude Code," Thariq Shihipar, 2026-04-30

Naive compaction:
  - Separate API call with its own system prompt ("summarize this"), no tools
  - Pays full uncached input rate for the entire conversation
  - Cost scales with conversation length — most expensive when most needed

Cache-safe forking (Claude Code's approach):
  - Same system prompt, user context, system context, tools as parent
  - "From the API's perspective, this request looks nearly identical to the
    parent's last request—same prefix, same tools, same history—so the
    cached prefix is reused."
  - Requires saving a 'compaction buffer' to leave room in context window
    for the summary output tokens

Note: Cache-safe forking optimizes the compaction CALL itself.
Post-compaction turns begin with a new (summary-based) prefix and rebuild
the cache from scratch — the same post-compaction cost wasnotwas measured.
```

### Five "Lessons Learned" (verbatim from article)
```
# Summary lessons from "Lessons from building Claude Code"
# Source: Thariq Shihipar, 2026-04-30

1. "Prompt caching is a prefix match. Any change anywhere in the prefix
   invalidates everything after it."

2. "Use messages instead of system prompt changes."

3. "Don't change tools or models mid-conversation."

4. "Monitor your cache hit rate like you monitor uptime."

5. "Fork operations need to share the parent's prefix."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-harnessing-claude-intelligence.md` Claims 10–13: that note's
    caching principles table covers the same four rules (static first, messages
    for updates, don't switch models, manage tools via tool search). The new
    article adds implementation specifics absent from that table: the `defer_loading`
    flag for MCP stubs (Claim 9 here), the Plan Mode concrete design (Claim 8
    here), and the production compaction fork mechanism (Claim 11 here). Both
    are first-party Anthropic sources confirming the same caching principles.
  - `blog-bswen-mcp-token-cost.md` Claim 1 ("Every MCP server you connect loads
    all its tool definitions into Claude's system prompt. Not when you use
    them—before you even start working."): Bswen documents the MCP token bloat
    problem from a practitioner cost perspective. This article provides the
    authoritative first-party design pattern (`defer_loading` stubs) that
    addresses that problem. Together: Bswen names the cost; this article provides
    the fix.

- **Extends**:
  - `research-wasnotwas-context-compaction.md` Claim 2: that note measures the
    cost of compaction ("one compaction call on a 125,000-token context cost
    $0.40 — equivalent to running about 21 follow-up turns at cached rates,
    because each compaction destroys the KV cache established during prior
    turns."). The wasnotwas note quantifies the post-compaction cost to
    subsequent turns; this article explains why naive compaction is additionally
    expensive (pays cold-prefill during the compaction call itself) and provides
    the first-party fix (cache-safe forking, which reuses the cached prefix for
    the compaction call itself). Both observations are simultaneously true: naive
    compaction is expensive at call time (this article); and all compaction
    results in a post-compaction cold-prefill rebuild for subsequent turns
    (wasnotwas). Cache-safe forking eliminates only the first cost, not the
    second.
  - `failure-cursor-ultra-billing-cache-explosion.md`: that note documents the
    user-facing billing failure from unmanaged prompt cache state. This article
    provides the design-level patterns — cache-layer discipline, immutable tool
    sets, cache-safe compaction — that prevent such failures. The failure note
    describes what goes wrong; this article describes the architecture that
    avoids it.

- **Contradicts**: None found.

- **Novel**:
  - The five-lesson "Lessons learned" summary (Claim 12 and the Concrete
    Artifacts section) is the most compact authoritative caching checklist from
    any Anthropic source to date.
  - Cache-safe forking (Claim 11) — the specific mechanism of matching the
    parent's full prefix during the compaction call — is described nowhere else
    in the corpus. Other sources measure compaction cost or describe compaction
    trigger thresholds; only this source explains how to run the compaction call
    itself efficiently.
  - The SEV-level monitoring posture (Claim 12) is unique to this source. No
    other corpus source establishes cache hit rate as a production reliability
    metric requiring incident response.
  - `defer_loading: true` for MCP stubs (Claim 9) is the first named
    implementation pattern for keeping MCP tools in the prefix without paying
    full schema cost.
  - The model-switching cost trap at 100k tokens (Claim 6) is the first
    explicit quantified statement of when the model-switching heuristic inverts.

## Guide Impact

- **Chapter 02 (Harness Engineering — tool design)**: Add the four cache-breaking
  pitfalls (Claim 4) as a "what not to do" checklist. Add Plan Mode's tool
  design as the canonical example of designing features around the cache
  constraint (Claim 8). Add the `defer_loading` stub pattern (Claim 9) as
  the authoritative fix for MCP token bloat (currently addressed via "prune
  your MCP server count" per Bswen — this pattern provides a complementary
  approach that does not require removing tools).

- **Chapter 04 (Context Engineering — cache design)**: Replace any generic
  "static first, dynamic last" guidance with the specific four-layer hierarchy
  (Claim 2). Add the `<system-reminder>` tag as the named implementation pattern
  for dynamic update injection (Claim 5). Add the model-switching cost inversion
  at 100k tokens (Claim 6) as a callout box or warning alongside any "use
  cheaper models for simpler tasks" recommendation.

- **Chapter 04 (Compaction)**: Add cache-safe forking (Claim 11) as the
  recommended compaction pattern, explicitly contrasting it with the naive
  "separate API call" approach (Claim 10). Cross-reference wasnotwas Claim 2
  for the post-compaction cold-prefill cost that cache-safe forking does NOT
  eliminate. The complete picture: cache-safe forking makes the compaction call
  cheap; the post-compaction prefix rebuild is still a cost that the wasnotwas
  $0.40 figure describes.

- **Chapter 02 (Harness Engineering — operational practice)**: Add cache hit
  rate monitoring as a required production metric (Claim 12). The "Monitor your
  cache hit rate like you monitor uptime" lesson should appear in any operational
  checklist for Claude Code deployments.

## Extraction Notes

- The article is available at claude.com/blog (not anthropic.com/engineering).
  The domain difference is noted; Thariq Shihipar's Claude Code team affiliation
  confirms this is first-party engineering content, not a marketing post.
- The article does not specify a threshold for cache hit rate alerts (only that
  SEVs are declared when rates are "too low"). The exact threshold is not
  extractable.
- The article was self-contained with no linked sub-pages requiring follow-up.
  Extraction covered all eight sections plus the "Lessons learned" summary.
- The previous PR (#504) for this source note was closed after the Assayer
  identified a fabricated quote in the cross-references. This note has been
  written from scratch with all cross-reference quotes verified against the
  cited source notes prior to writing. In particular: the Corroborates
  characterization of `research-wasnotwas-context-compaction.md` cites Claim 2
  verbatim from that note without fabricating a description; the Extends section
  clarifies the distinction between the compaction call cost (which cache-safe
  forking addresses) and the post-compaction rebuild cost (which wasnotwas
  measured and which cache-safe forking does not address).
