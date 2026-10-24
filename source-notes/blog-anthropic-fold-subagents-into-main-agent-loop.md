---
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_type: blog-post
title: "Building agents: When to fold subagents into your main agent loop"
author: Diane Sarkis (Anthropic Applied AI team)
date_published: 2026-10-22
date_extracted: 2026-10-24
last_checked: 2026-10-24
status: current
confidence_overall: emerging
issue: "#4295"
---

# Building agents: When to fold subagents into your main agent loop

> Anthropic's Applied AI team argues that many enterprise multi-agent (orchestrator-subagent) designs should be migrated into a single agent loop with progressively disclosed skills and tools, gives three conditions under which subagents still earn their place, and lays out a staged, eval-driven migration procedure.

## Source Context

- **Type**: blog-post (first-party Anthropic article, category "Best practices, Perspectives", product Claude Platform; 18-minute read)
- **Author credibility**: Diane Sarkis, Anthropic. Written from the Applied AI team's vantage point of comparing architectures across "several enterprise deployments". First-party and informed, but also the vendor that sells the models and the migration kit it promotes.
- **Scope**: Covers failure modes of org-chart-shaped multi-agent systems, the case for a single loop with skills/tool search, a target loop design, a staged migration (evals, merge, subagents-as-tools, fold into skills/MCP tools), governance for multi-team contribution, and a companion `/claude-api` skill kit. Does NOT publish eval data, customer names, or methodology for any quantitative claim.

## Extracted Claims

### Claim 1: A single agent with skills frequently beat both a one-prompt design and a subagent design across several enterprise deployments, often at lower cost and latency
- **Evidence**: Applied AI team comparisons across "several enterprise deployments"; no numbers, customers, or eval method published.
- **Confidence**: anecdotal (vendor-reported, unquantified)
- **Quote**: "In our comparisons across several enterprise deployments, a single agent with skills frequently outperformed both the one-prompt-for-everything design and the subagent design on quality, and often at a lower cost and latency per task."
- **Our assessment**: Same comparative claim as the commerce blueprint (see Cross-References), now generalized beyond commerce to "enterprise deployments". Note the hedged wording ("frequently", "often") versus the commerce post's "consistently". Still no published data, so treat as a strong practitioner signal, not a measured result.

### Claim 2: Subagents are still justified under exactly three conditions
- **Evidence**: Stated by the authors as the keep-a-subagent criteria; reused later as the gate for keeping a subagent called as a tool.
- **Confidence**: emerging
- **Quote**: The stem and its three list items, each quoted verbatim (they are separate list elements in the source):
  - "To be clear, subagents still have their place, including at the research frontier. Use them when:"
  - "A single agent loop hits measurable performance degradation from context bloat, or"
  - "Multiple tasks need to be tackled in parallel with fresh context windows that can be discarded once the task is done, or"
  - "A single agent struggles to select appropriate tools or there are conflicting instructions in the system prompt."
- **Our assessment**: The three conditions are (1) measurable context-bloat degradation in a single loop, (2) parallel tasks that benefit from fresh, discardable context windows, and (3) tool-selection trouble or conflicting system-prompt instructions. Importantly each is an observed failure, not an a priori preference, which turns "start with orchestrator-subagent" into "start single-loop, split on evidence". The article also says subagents "are effective at verification, parallel work, and modular permissioning", which is a fourth set of uses not listed in the three conditions (modular permissioning is later addressed by per-user checks inside tools).

### Claim 3: Enterprise agent architectures tend to mirror org charts (Conway's law), producing five named failure modes
- **Evidence**: Pattern observation by the Applied AI team; five failure modes enumerated (context management, subagent sprawl, the Frankenprompt, unvetted/overly localized evals, latency).
- **Confidence**: emerging
- **Quote**: "But too often we see enterprises give each team or problem type its own subagent, with the agent architecture becoming a copy of their org chart (Conway’s law at work)."
- **Our assessment**: Believable and consistent with common organizational dynamics. The named failure modes are a useful checklist. "The Frankenprompt" is defined as "Every team adds a sentence to the system prompt, resulting in conflicting rules and no consistent voice." The point about localized evals ("leadership makes decisions based on watered-down, overly localized scores") is a distinct, rarely stated governance risk.

### Claim 4: One customer saw roughly 2x faster runtime moving from a multi-agent harness to a single agent loop
- **Evidence**: Single unnamed customer comparison; no measurement details.
- **Confidence**: anecdotal
- **Quote**: "One customer that evaluated their multi-agent harness against a single agent loop saw a roughly 2x faster runtime with the latter."
- **Our assessment**: Directionally plausible (nested model loops add serial latency, which the article also notes later), but n=1, unnamed, unspecified task. Do not cite as a general speedup figure.

### Claim 5: Shared context in one window yields better answers than summaries handed back by subagents ("telephone game")
- **Evidence**: Mechanistic argument; no experiment.
- **Confidence**: emerging
- **Quote**: "When agents are split by problem type, they engage in a \"telephone game,\" passing information back and forth with each handoff degrading fidelity."
- **Our assessment**: Corroborates the "state-lossy handoff" claim in the commerce note and the context-centric decomposition principle in the coordination-patterns note. The article's constructive advice: split by context needs and have subagents "hand back a compact result" (good candidates: "independent research paths, separate components with clean interfaces, or black-box verification").

### Claim 6: Progressive disclosure of skills and tools removes the main reason teams split work across subagents; Claude Code's system prompt was cut by over 80%
- **Evidence**: First-party Claude Code change; the same figure appears in the context-engineering note with the "no measurable loss" qualifier, which this article does not repeat.
- **Confidence**: emerging
- **Quote**: "In fact, we reduced Claude Code’s system prompt for more advanced models by over 80% which included cuts related to progressively disclosing skills and tools."
- **Our assessment**: The most concrete evidence in the post, and independently stated in `blog-anthropic-context-engineering-claude-5.md`. Caveat: the article attributes the cuts partly (not wholly) to progressive disclosure, so the 80% is not a measure of what progressive disclosure alone saves.

### Claim 7: Newer models make more harness structure redundant, and rigid multi-agent structures were often what stopped a new model from doing more
- **Evidence**: Migration experience with customers; model capability claims.
- **Confidence**: emerging
- **Quote**: "A simpler loop is also easier to move to the next model; in migrations we have helped customers with, rigid multi-agent structures were often what stopped the new model from doing more of the work."
- **Supporting quotes** (same paragraph, "Models are more capable"):
  - "starting with Opus 4.5, models became capable of managing far more in a single loop than most teams expected."
  - "You cannot turn off thinking on Opus 5.5, and Fable 5.1, and recent models increasingly narrate their progress and check their work as they go, which makes some harness elements redundant."
- **Our assessment**: Ties architecture choice to model-upgrade cost, a point absent from the five-pattern taxonomy. The supporting quotes date the capability shift to Opus 4.5 and state that thinking cannot be turned off on Opus 5.5 and Fable 5.1. The model-capability argument means the guidance is time-indexed and may shift again.

### Claim 8: The target single-loop design lets the model own the plan; ordering moves into skills and hard limits into tools
- **Evidence**: Design description, no benchmark.
- **Confidence**: emerging
- **Quote**: "The model writes its plan in context on the first turn and revises it as results arrive."
- **Our assessment**: Concrete architecture: one model, one context window, an open-ended tool loop; the model emits batches of tool calls that the harness runs in parallel; limits (turn and cost budgets, write gates) live in the harness; "Ordering and domain procedure move into skills"; validation and approval gates move into tools; code is kept only for cheap, almost-always-relevant loading (e.g. entity resolution) and mechanical parts. The key change is that the planner and the executor are the same model, so the plan can change mid-turn.

### Claim 9: Start migration with task-completion evals; even 10 golden examples is enough to begin
- **Evidence**: Practice recommendation from the authors; "one approach that has worked for us internally" for replay is recording timestamps on important events.
- **Confidence**: emerging
- **Quote**: "Even a set of 10 golden examples is enough to start."
- **Our assessment**: A low, actionable bar. Structure: one shared end-to-end eval owned by a central team plus smaller per-skill eval sets from the owning teams. Metrics shift during migration: while an orchestrator exists track routing accuracy ("did it pick the right subagent?"); after folding, check whether the agent loaded the right skill or called the right tool.

### Claim 10: Fold subagents one at a time and compare which tasks flipped, not just the final score; run each task multiple times
- **Evidence**: One worked example on a sample support agent: folding one subagent into another lowered latency but broke a previously passing process, and the break "only showed up in one run out of two".
- **Confidence**: anecdotal (single example, sample agent)
- **Quote**: "When you compare, don’t just examine the final score, take a look at which tasks flipped."
- **Our assessment**: High-value, transferable evaluation hygiene: aggregate scores hide regressions, and non-deterministic failures need repeated runs. The example's cause: the main agent held the order-lookup tool and answered on its own instead of asking the shipping specialist for the delivery date. The eval must also include "a task for every chain of agents that runs together in production and for every rule the agent must not break". Two runs is a thin sample; the article's own example suggests more.

### Claim 11: Keep a subagent as a tool (not a handoff) unless it must talk to the user directly; this is a safe first migration step
- **Evidence**: Recommendation; rationale given as enabling a shared response schema, verification against real data, and trimming input to a final synthesis step.
- **Confidence**: emerging
- **Quote**: "Everything else can be a skill plus tools in the main loop."
- **Our assessment**: Provides a staging ladder: merge tightly coupled specialists, then subagents-as-tools (no rewrite required, gives an eval baseline), then fold into skills plus MCP tools. Residual failure modes of the as-tool step are listed: separate prompt/owner/evals per specialist, lossy summaries, and nested loops adding latency.

### Claim 12: Tool-choice quality degrades past roughly 30-50 tool definitions; group tools by user intent and use deferred loading
- **Evidence**: Stated rule of thumb, no data.
- **Confidence**: anecdotal
- **Quote**: "We recommend tools grouped by user intent (not one tool per API) because once you exceed 30-50 tool definitions in the system prompt, tool choice tends to degrade."
- **Our assessment**: A useful numeric heuristic that is model-dependent and probably moving. Additional tool guidance: use tool search with deferred loading; put hard preconditions inside tools so a tool "returns an instruction the model can act on" when a prerequisite is missing; per-user permission checks inside tools return "a plain refusal the model can read", allowing one loop to serve users with different access without an agent per permission level.

### Claim 13: Governance: one small central team owns the system prompt and end-to-end quality; teams own skills and tools, with DRIs and evals shipped per skill
- **Evidence**: Recommendation; no outcomes reported.
- **Confidence**: emerging
- **Quote**: "One central team should own end-to-end quality and the system prompt, vetting every new tool and eval before it ships."
- **Our assessment**: Converts the Conway's-law critique into an ownership model: team ownership shifts "from agents to skills and tools". To limit skill sprawl: per-team DRIs, distinct skills, evals with each skill, and tooling (`/skill-creator`, `/skill-doctor`) to audit and prune. Matches the single-owner-per-skill model in the commerce note (Claim 14 there).

### Claim 14: Reference material belongs behind lookup tools or in skill reference files, not pasted into prompts by code
- **Evidence**: Recommendation only.
- **Confidence**: emerging
- **Quote**: "Avoid having code retrieve and paste this context into prompts."
- **Our assessment**: Short but opinionated: moves retrieval decisions from harness code to the model. Consistent with the "code step that rewrites the plan from a catalog of rules is no longer needed" theme.

### Claim 15: The principle matters more than the architecture: measure, change one thing at a time, keep what holds up
- **Evidence**: Closing guidance.
- **Confidence**: emerging
- **Quote**: "Build a small end-to-end eval, fold in one subagent, and keep it as a subagent only if the folded version scores worse, then rinse and repeat."
- **Our assessment**: Sets the burden of proof: subagent must justify itself against a folded alternative, reversing the "start with orchestrator-subagent" default. Also carves out a plain multi-agent route: "If you go the multi-agent route, start with the simplest pattern (generator-verifier, orchestrator-subagent, or other) that could work."

## Concrete Artifacts

Target loop design (source: "How to fold subagents into the main agent loop"):

```
One model and one context window running an open-ended tool loop, with limits
(turn and cost budgets, write gates) set in the harness.

Each turn, the model emits a batch of tool calls. The harness runs them in
parallel and returns raw results to the same model, which decides the next
step: another batch, a question to the user, or an answer.

The loop stops when the model answers or hits a budget. A goal or verifier
check can optionally run after the answer.
```

Companion migration-kit commands named in the article (tool references; capabilities not independently verified by us):

```
/claude-api build-eval      first end-to-end set owned by central team / small per-skill evals
/claude-api prompt-audit    flag instructions written for older models; propose fixes as a diff
/claude-api hillclimb       iteratively improve an app against an existing eval ("folded in vs kept")
/claude-api cost-optimize   prompt caching, token trimming, effort and model choice, one change at a time
/skill-creator              author well-formed skills; audit/trim/deduplicate existing ones
/skill-doctor               show what each skill costs and how often it is used; delete dead weight
```

Migration ladder distilled from the article (our summary, not a quote): task-completion evals -> merge tightly coupled specialists (by shared context, most-used first) -> keep remaining subagents as tools -> fold one at a time into skills + MCP tools, comparing flipped tasks over multiple runs -> central team vets skills/tools/evals.

## Cross-References

- **Corroborates**:
  - `blog-anthropic-commerce-agents-blueprint.md` Claim 6 (single agent with skills outperforms one-prompt and subagent designs) and Claim 7 (handoffs are state-lossy); this article generalizes both from commerce to enterprise agents. Also Claim 14 there (single-owner teams per skill/tool, one deployment unit) matches Claim 13 here.
  - `blog-anthropic-context-engineering-claude-5.md` Claim 1 (over 80% of Claude Code's system prompt removed) and Claim 6 (progressive disclosure of context).
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 13 (decompose by context needs rather than work type) and Claim 12 (start with the simplest pattern that could work); this article's "divide by context" and "telephone game" advice restate both.
- **Contradicts**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 ("For most use cases, we recommend starting with orchestrator-subagent.") versus this article's recommendation to work toward a single loop and keep a subagent only if the folded version scores worse. This is the same tension already filed as **[contradiction #3203](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/3203)** (open, `needs-resolution`); no duplicate filed. This source is significant new evidence for Side B because it extends the claim beyond commerce/conversational domains to general enterprise agents, and it is a later (Oct 2026 vs Apr 2026) first-party post from the same vendor, so it may represent a revision rather than a true conflict. Possible conditioning variables (not a verdict): tightly coupled multi-turn work versus decomposable or parallel work, and model generation (the article explicitly dates the shift to Opus 4.5 and later). A comment was posted on #3203 linking this note's PR (#4329). Verdict is left to the human/Smith.
  - `blog-anthropic-coderabbit-agent-orchestration.md` uses an orchestration structure with Opus orchestrating and cheaper models doing narrow work (Claim 7 there); that is a different problem (staged plan-then-code pipeline) and is not clearly opposed, so we record it as tension only, not a separate contradiction.
- **Extends**: `blog-anthropic-multi-agent-coordination-patterns.md` (adds a migration path away from orchestrator-subagent and explicit keep-conditions); `blog-anthropic-building-enterprise-agents.md` (enterprise agent guidance; adds governance and migration specifics); `blog-anthropic-block-fable-orchestration-migrations.md` (frontier-model orchestration of many workers is a case where parallel fresh-context workers fit condition 2 here).
- **Novel**:
  - The three explicit keep-a-subagent conditions.
  - The staged fold-in migration with "which tasks flipped" comparison and repeated runs.
  - The 30-50 tool-definition ceiling heuristic.
  - The Conway's-law / org-chart framing with named failure modes (subagent sprawl, Frankenprompt, localized evals).
  - Central-team ownership of system prompt and end-to-end evals with per-skill DRIs.
  - The `/claude-api build-eval | prompt-audit | hillclimb | cost-optimize` kit.

## Guide Impact

- **Chapter 02** (Harness Engineering, "Start with orchestrator-subagent", ~L1550): the default currently cites `blog-anthropic-multi-agent-coordination-patterns.md`. Recommend adding a counter-position and the three keep-conditions (Claims 1-2 here), and flagging the disagreement per #3203 rather than silently replacing the default. Add the staged migration ladder and "compare flipped tasks, repeat runs" as an eval practice (Claims 9-11).
- **Chapter 01** (Multi-Agent Orchestration, ~L237): note that the orchestrator-subagent pattern is not the only recommended starting point; add the "subagent as tool vs full handoff" distinction (Claim 11).
- **Chapter 04** (context engineering / progressive disclosure, ~L756): add the single-loop-with-progressive-disclosure design (Claims 6, 8) and the 30-50 tool ceiling plus intent-grouped tools and deferred tool loading (Claim 12). Reference the 80% Claude Code system-prompt reduction jointly with the context-engineering note rather than as an independent data point.
- **Governance / org chapters** (wherever team ownership of agents is discussed): add the central-team-owns-system-prompt-and-end-to-end-evals model (Claim 13).
- Label all quantitative claims here as vendor-reported (Claims 1, 4, 12), per triage.

## Extraction Notes

- Fetched the page directly and read the full text (about 23k characters of page text after stripping navigation). The article has no sub-pages of substance; related-article links at the bottom (source control, BDR with Managed Agents, code review, Uber CISO) are unrelated and were not followed.
- All `Quote` fields are copied character-for-character from the page text, including curly apostrophes; the escaped inner quotes in Claim 5 correspond to the source's straight/double quote marks around "telephone game".
- Contradiction handling: #3203 already tracks this exact tension, so per MINER.md §4a no new issue was filed; this note is cited there instead.
- Companion-kit commands (`/claude-api ...`, `/skill-doctor`) are recorded as stated by the article, not verified.
- The article is partly promotional for the migration kit; the evidence base is unpublished internal comparisons, hence overall confidence "emerging" with the quantitative claims at "anecdotal".
