---
source_url: https://calv.info/agents-feb-2026
source_type: blog-post
title: "Coding Agents in Feb 2026"
author: Calvin French-Owen
date_published: 2026-02-17
date_extracted: 2026-04-08
last_checked: 2026-04-08
status: current
confidence_overall: emerging
issue: "hi-e93.2"
---

# Coding Agents in Feb 2026 (Calvin French-Owen)

> A working engineer's heuristics for context budget, tool-choice cost, and
> sub-agent delegation across Claude Code and Codex. Coins (or popularizes) the
> "smart half" rule for context windows and gives the most-cited concrete
> comparison between Skill and MCP token costs.

## Source Context

- **Type**: blog-post (practitioner write-up)
- **Author credibility**: Calvin French-Owen is a co-founder of Segment
  (acquired by Twilio for ~$3.2B) and previously worked on the launch of
  OpenAI's Codex web product. He uses Claude Code and Codex daily and writes
  the post from the perspective of a working engineer, not a vendor. The post
  is widely cited in practitioner discussions through Feb-Mar 2026.
- **Scope**: Personal tactics for getting better results from Claude Code and
  Codex in early 2026. Covers context-window management, when to delegate to
  sub-agents, the relative strengths of Opus vs Codex, Skills vs MCP servers,
  and externalizing state to the filesystem. Does NOT cover team adoption,
  CI integration, or quantitative benchmarks.

## Extracted Claims

### Claim 1: Stay in the "smart half" of the context window
- **Evidence**: Direct heuristic from author's daily use of Claude Code 2.x.
  No specific token count or experiment, but the principle echoes long-context
  degradation observations from other practitioners and matches Anthropic's
  own training data weighting (short-context examples dominate).
- **Confidence**: emerging
- **Quote**: "Stay in the 'smart' half of the context window. It's generally
  easier to train on short-context data vs long-context data. Results will
  tend to be better when the context window is 'less full'."
- **Our assessment**: This is the cleanest, most quotable framing of
  context-as-budget we have found. It also meshes with Sankalp's "effective
  window is 50-60%" observation (separate source). Use this as the canonical
  Ch04 rule of thumb.

### Claim 2: Skills cost ~50-100 tokens; MCP calls cost thousands
- **Evidence**: Direct quantitative comparison from author's instrumented
  usage. Aligns with Bswen's measurement that loading 15 MCP servers consumes
  ~100k tokens of system prompt before any user input (separate source).
- **Confidence**: emerging
- **Quote**: "Skills are also great because they are *very* context efficient.
  Unlike MCP calls (which take up thousands of tokens), skills tend to be
  ~50-100 tokens."
- **Our assessment**: Single most useful quantitative claim for the
  "tool choice and context cost" Ch04 section. The 1-2 order of magnitude
  difference between Skills and MCP calls is large enough to be a hard rule:
  prefer Skills over MCP whenever both can do the job.

### Claim 3: Externalize state to the filesystem instead of the conversation
- **Evidence**: Author's recommended pattern, framed as a context-budget tactic.
- **Confidence**: emerging
- **Quote**: "Externalizing context into the filesystem (e.g. a plan doc with
  stages which are checked or not) allows agents to selectively read and
  remember without filling up the full context."
- **Our assessment**: This is the conceptual bridge between Ch04 (context
  engineering) and the spec/plan pattern advocated by Osmani (separate source)
  and the Superpowers plugin. Plans-as-files are a context optimization, not
  just a workflow choice.

### Claim 4: Compaction is lossy; the agent chooses what to keep
- **Evidence**: Author's direct observation, no metrics.
- **Confidence**: emerging
- **Quote**: "Compaction is a lossy technique. When deciding what to compact
  and how, the agent is going to make choices on which information to include
  and omit."
- **Our assessment**: Corroborates the wasnotwas comparative compaction study
  (separate source) which shows that 6 of 7 harnesses use lossy LLM-summary
  strategies. Also corroborates the decker failure report (separate source)
  where 4 hours of architectural rationale was flattened into a generic
  summary.

### Claim 5: Chunk work that's too big for the window
- **Evidence**: Author's failure observation from trying to give agents
  problems that exceed the smart-half budget.
- **Confidence**: emerging
- **Quote**: "Your work needs to somehow be chunked. If the problem you are
  trying to solve is 'too big' for the context window, the agent is going to
  spin on it for a long time and give you poor results."
- **Our assessment**: This is the practical implication of Claim 1. If smart
  capacity is ~50% of advertised window, problems that need >50% of window
  need decomposition before they're handed to the agent. This is the scoping
  rule for session segmentation.

### Claim 6: Opus delegates to sub-agents in parallel; Codex (as of Feb 2026) does not
- **Evidence**: Author's observation from running both tools side by side.
  Attributes part of Claude Code's speed advantage to parallel sub-agent
  dispatch.
- **Confidence**: anecdotal (single observer)
- **Quote**: "Opus has been trained to work across context windows extremely
  efficiently... You'll notice Opus frequently spinning up multiple sub-agents
  simultaneously... Codex is *slow*. The biggest reason for this is that it's
  not delegating tasks across context windows."
- **Our assessment**: Use as supporting evidence for the sub-agents-as-context-firewall
  pattern. Note this is point-in-time (Feb 2026); Codex may add parallelism
  later. Tag with date when citing.

### Claim 7: Author's actual workflow — Claude Code for plans, Codex for code
- **Evidence**: Author's stated daily workflow.
- **Confidence**: anecdotal
- **Quote**: "I'll *start* with Claude Code and keep that open as a pane,
  then flip to Codex when I'm ready to actually start the coding."
- **Our assessment**: Useful as an example of multi-tool routing, but it's
  one engineer's preference. Pragmatic Engineer 2026 survey (separate source)
  shows 70% of engineers use 2-4 AI tools simultaneously, so this pattern
  is broadly representative even if the specific tool choice isn't universal.

## Concrete Artifacts

The post does not include code listings or specific configurations. The
"plan doc with stages which are checked or not" reference is conceptual; for
a concrete realization see the Superpowers plugin (`docs/plans/`) covered in
Dewhurst's writeup, or Sankalp's `.claude/commands/handoff` pattern.

## Cross-References

- **Corroborates**: blog-bswen-mcp-token-optimization (Skills vs MCP token
  comparison — Bswen measures 15 MCP servers = ~100k tokens, French-Owen says
  Skills are 50-100 tokens; the orders-of-magnitude gap matches)
- **Corroborates**: blog-sankalp-claude-code-20 (effective window is 50-60% of
  advertised — French-Owen's "smart half" is the same observation under a
  different name)
- **Corroborates**: blog-wasnotwas-context-compaction-comparative (compaction
  is lossy across 6 of 7 harnesses studied)
- **Extends**: blog-addyosmani-code-agent-orchestra (Osmani's "verification
  is the new bottleneck" — French-Owen adds the parallelism mechanic that
  enables Opus to verify faster)
- **Novel**: The "smart half" framing as a memorable, quotable rule of thumb.
  Other sources observe the effect; French-Owen names it.

## Guide Impact

- **Chapter 04 (Context Engineering)**: This is a primary source. Use the
  "smart half" quote as the lead heuristic for the "Context as budget" section.
  Pair with Sankalp's 60% threshold and the wasnotwas $0.40-per-compaction cost
  to give the section three independent practitioner-grade data points for the
  same phenomenon.

- **Chapter 04 (Tool choice and context cost)**: Lead with the Skills vs MCP
  comparison (50-100 tokens vs thousands). This is the strongest single
  recommendation in the section: prefer Skills, treat MCP as a budget item.
  Cross-cite Bswen for measured server-count thresholds.

- **Chapter 04 (Specs/plans as compressed context)**: Cite the "externalize
  to filesystem" quote as the conceptual frame. Specs and plans aren't just
  about clarity — they're a context optimization. The agent reads only what
  it needs.

- **Chapter 02 (Harness Engineering)**: Add the parallel sub-agent observation
  as a feature of Opus that informs harness design. If your harness allows
  sub-agent dispatch, design tasks to be decomposable; the model will exploit
  the parallelism.

- **Chapter 01 (Daily Workflows)**: The "Claude Code for planning, Codex for
  coding" workflow is a concrete example of multi-tool routing. Add as an
  illustrative case study with the caveat that this is one engineer's preference
  and the optimal split depends on the engineer and the codebase.

## Extraction Notes

- The post is short and dense. We extracted 7 substantive claims; the post has
  more material on agent architectures, sub-agent training, and Opus internals
  that is interesting but not directly relevant to Ch04.
- French-Owen's credibility is unusually high for a single-author blog post:
  Segment founder + ex-OpenAI Codex launch team. Treat his observations as
  weighty even when they're not quantified. Still tag claims as "emerging"
  because none of them are independently replicated benchmarks.
- The post does not provide specific token counts beyond "50-100" for Skills
  and "thousands" for MCP. Quantitative gaps should be filled from Bswen and
  wasnotwas (separate sources).
- Calvin's "smart half" framing is original to this post as far as we can
  tell. It is rapidly being repeated in practitioner threads — track whether
  it becomes the standard term for the phenomenon.
