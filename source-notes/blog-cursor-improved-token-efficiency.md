---
source_url: https://cursor.com/blog/improved-token-efficiency
source_type: blog-post
title: "Improved token efficiency for longer agent runs"
author: "Jediah Katz, Connor O'Keefe & Calvin Yee (Cursor / Anysphere)"
date_published: 2026-09-23
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: emerging
issue: "#3660"
---

# Improved token efficiency for longer agent runs (Cursor)

> Cursor's first-party account of six harness-level changes — system prompt
> trimming, lazy built-in tool loading, explicit prompt-cache breakpoints,
> file-read line-numbering compression, and two subagent-usage tightenings —
> that together cut production token costs by 7% without degrading agent
> quality, framed around the observation that longer agent runs shift where
> token spend concentrates.

## Source Context

- **Type**: blog-post (cursor.com/blog, "research" category, published
  September 23, 2026, 7-minute read; three named engineers — Jediah Katz,
  Connor O'Keefe, and Calvin Yee)
- **Author credibility**: First-party account from Cursor/Anysphere engineers
  describing changes to their own production agent harness, which serves a
  large developer user base. This is vendor blog content with an obvious
  commercial incentive (Cursor sells inference-metered plans, so "we cut
  costs 7%" is also a marketing claim), and the post discloses no
  methodology detail beyond naming the metrics it tracked (token usage,
  cost, latency, tool-call errors, agent usage) and the general shape of its
  A/B testing practice. No confidence intervals, sample sizes, or the
  specific A/B test duration are given for any of the percentage figures.
  Treat as emerging: directionally informative about what Cursor did and
  why, but the magnitude figures (7%, 66%, 60%, 46.9%, 20%, 1.6%) are
  self-reported and unaudited.
- **Scope**: Covers six specific harness changes made "over the past few
  months" prior to publication: system prompt trimming, built-in tool lazy
  loading, prompt-cache breakpoint placement (specific to the OpenAI/GPT-5.6
  API), file-read line-number compression, and two subagent-usage changes
  (removing over-encouraging prompts, tightening model-selection tool
  arguments). Does NOT cover: training methodology or model architecture
  (see `blog-cursor-composer-2-5.md`, `blog-cursor-composer2-technical-report.md`),
  the routing/model-selection product (`blog-cursor-router-model-classifier.md`),
  or implementation code for any of the six changes. Does not name specific
  models beyond "GPT-5.6" (the cache-breakpoint mechanism) and does not
  quantify the "context isolation coordination tax" it names for subagents.

## Extracted Claims

### Claim 1: Six harness-layer changes together reduced token costs for users by 7% without reducing agent quality
- **Evidence**: First-party summary statement covering all six changes described in the post (system prompt trimming, tool loading, cache reuse, file-read compression, subagent tightening, ongoing harness work).
- **Confidence**: emerging (aggregate self-reported figure; no breakdown of how much each of the six changes individually contributed to the 7%)
- **Quote**: "Changes across each of these layers reduced token costs for users by 7% without reducing agent quality."
- **Our assessment**: The 7% is a rollup across six independently-varied changes with individually-reported deltas (66%, 60%, 46.9%, 20%, 1.6% — see Claims 2, 5, 4, 7, 9) that apply to different slices of the request (system prompt tokens, static tool-description tokens, MCP-session tokens, cold-cache-miss rate, cache-read tokens respectively). Because these percentages measure different denominators, they cannot be summed to reconstruct the 7% headline figure, and the post does not attempt to reconcile them. Read the 7% as a plausible blended outcome, not an audited total.

### Claim 2: As models improved, most explicit "DO NOT," "You must," and "Important" style instructions in the system prompt became unnecessary — defining tool behavior was sufficient — allowing the team to trim roughly 66% of the system prompt
- **Evidence**: First-party before/after account of system-prompt content and rationale, stated to hold "across model families."
- **Confidence**: emerging (directional mechanism described with a specific magnitude; no before/after token counts or per-model-family breakdown published)
- **Quote**: "Instead of long lists of \"DO NOT do this,\" \"You must,\" or \"Important\" instructions, we could simply define how a tool behaves and models would generally comply. This was true across model families, allowing us to trim roughly 66% of our system prompt."
- **Our assessment**: This is the sharpest concrete claim in the post because it names a specific instruction *style* (defensive "DO NOT" lists) that became redundant, rather than just asserting "the prompt got smaller." It is consistent with the general harness-simplification-as-models-improve principle already in the corpus (see Cross-References), but it is the first source to specifically identify "DO NOT" instruction density as the trimmable category, and to attach a number (66%) to that category. Practitioners should treat this as a prompt-tuning heuristic to test on their own harness, not an established finding — the post gives no evidence for how the trimmed prompt was validated against regressions beyond the general A/B testing framing in the same paragraph.

### Claim 3: The team treats real-traffic A/B tests as more trustworthy than offline evals for harness optimization decisions, because evals skew toward "hard" problems that don't reflect the true distribution of user requests
- **Evidence**: Stated methodological preference, given as the closing rationale for the system-prompt-trimming section.
- **Confidence**: emerging (stated principle; no comparison data showing eval-driven decisions that would have been wrong)
- **Quote**: "Leveraging A/B tests on a large user base is crucial to effectively optimizing the harness for real traffic. While evals can be a fast and useful proxy, they often represent \"hard\" problems and don't properly reflect the true distribution of user requests."
- **Our assessment**: This is a methodological claim about *how to validate* harness changes, not a claim about a specific optimization outcome. It generalizes across all six changes in the post — Claim 6 makes the same point concretely for tool loading decisions ("we A/B tested several configurations"). This corroborates the online-vs-offline eval distinction already documented for Cursor's harness (see Cross-References): the recurring theme across multiple Cursor engineering posts is that offline evals are treated as a fast proxy but production A/B/online signals are the actual decision criterion.

### Claim 4: An earlier move of MCP tool definitions into dynamic (lazy-loaded) context reduced total tokens by 46.9% across sessions that called an MCP tool
- **Evidence**: First-party retrospective figure, cited as precedent for the built-in-tool change described later in the same post.
- **Confidence**: emerging (specific figure given; no date, sample size, or measurement window disclosed beyond "earlier this year")
- **Quote**: "We'd solved a similar problem earlier this year when we moved MCP tools into dynamic context, loading them only when needed. This reduced total tokens by 46.9% across sessions that called an MCP tool."
- **Our assessment**: This figure is new to the corpus — no existing source note quantifies the token savings from lazy-loading MCP tool definitions specifically for Cursor (the closest prior figure, Bswen's ~5–7k tokens/server linear-cost measurement, is from Claude Code, not Cursor, and measures baseline MCP overhead rather than the savings from lazy-loading it away). It directly extends `blog-cursor-router-model-classifier.md` Claim 11, which described the *same underlying pattern* ("dynamic tool calling... mirroring the existing MCP pattern") in July 2026 as an unquantified forward-looking effort — this September post is the first to attach a number to the MCP-specific instance of that pattern.

### Claim 5: Applying lazy-loading to Cursor's own built-in tools (rather than only MCP tools) — keeping only high-frequency tools (read, search, edit, shell) plus `ask_question` and mode-critical tools like `create_plan` in static context — cut static-context tool-description tokens by 60%
- **Evidence**: First-party description of which tools were kept static vs. offloaded, plus a cited chart figure.
- **Confidence**: emerging (specific figure given; selection criteria named but the A/B test results behind the selection are not published)
- **Quote**: "Ultimately, we kept the high-frequency tools for reading, searching, editing, and using the shell in static context. We also retained ask_question , which some models tended to hallucinate calls for, and tools that are crucial to specific product flows, such as create_plan in Plan Mode. The remaining tools now load when the agent needs them." (the space before the comma after `ask_question` reflects the source's inline code formatting, preserved verbatim). Chart caption: "Offloading built-in tools cut static-context description tokens by 60%"
- **Our assessment**: This is the direct, quantified follow-through on the "dynamic tool calling" effort that `blog-cursor-router-model-classifier.md` Claim 11 described only qualitatively two months earlier ("most native tool descriptions are no longer loaded into every prompt... following the same pattern we already use for MCPs"). The retained-tool list (read/search/edit/shell plus `ask_question` and `create_plan`) is a concrete, reusable heuristic: keep tools static if they are either high-frequency or prone to being hallucinated/needed from turn one, and lazy-load everything else. Notably, each tool was "needed in fewer than 20% of conversations" for the tools ultimately offloaded — the post states this as the opportunity that motivated the change.

### Claim 6: Cursor selected which tools to keep static by A/B testing configurations and tracking token usage, cost, latency, tool-call errors, and overall agent usage, specifically to confirm the savings did not degrade quality
- **Evidence**: First-party description of the evaluation methodology used for the tool-loading decision.
- **Confidence**: emerging (methodology named; no numeric results for the individual tracked metrics beyond the aggregate 60%/7% figures elsewhere in the post)
- **Quote**: "To decide which tools to keep in static context, we A/B tested several configurations based on how often each tool was used and whether models needed to see it from the start. We tracked token usage, cost, latency, tool-call errors, and overall agent usage to make sure the savings did not degrade quality."
- **Our assessment**: Tool-call error rate as one of the five tracked metrics is notable — it shows Cursor treats "does lazy-loading make the model worse at picking/using tools" as a first-class regression risk, not just a token-savings measurement exercise. This is a concrete instantiation of the "measure quality alongside cost when changing the harness" principle.

### Claim 7: Since GPT-5.6, the OpenAI API allows clients to mark explicit cache breakpoints (in addition to its default implicit caching); placing these after stable request layers and before the growing conversation reduced Cursor's cold cache misses by 20%
- **Evidence**: First-party description of a provider API capability and how Cursor's harness uses it.
- **Confidence**: emerging (specific figure given; provider-capability description is a factual claim about the OpenAI API, the harness-usage and resulting 20% figure are self-reported)
- **Quote**: "Before GPT-5.6, the cache boundary was determined automatically based on the latest request. Even though tools and system instructions rarely changed, they were not cleanly marked as reusable on their own. Since GPT-5.6, the OpenAI API allows clients to mark explicit cache breakpoints alongside its default implicit caching. We now place breakpoints after stable layers of the request and before the growing conversation, allowing later turns to reuse more of the unchanged prefix... These changes reduced the rate of cold cache misses by 20%."
- **Our assessment**: This is a provider-specific mechanism distinct from Claude's caching model described in `blog-anthropic-prompt-caching-everything.md` (Claim 3: "static content first, dynamic content last" as the foundational ordering rule for Claude's automatic prefix-based caching, with no client-side breakpoint marking described). The two sources describe the same underlying goal (maximize reused cached prefix across turns) achieved via different provider mechanisms: Anthropic's Claude Code relies entirely on stable prefix ordering with automatic longest-prefix-match caching, while Cursor's GPT-5.6 integration additionally uses explicit client-specified breakpoints. This is a conditioning variable (which provider/API you're on), not a contradiction — both approaches converge on "keep the front of the request stable and reuse it."

### Claim 8: Cursor moved variable, request-specific setup (skills, subagents, environment info) past the cache boundary into a "phantom user message" to keep the front of each request stable for caching
- **Evidence**: First-party architectural description of where variable context is now placed relative to the cache breakpoint.
- **Confidence**: emerging (architectural description; no separate quantification beyond the 20% cold-cache-miss figure in Claim 7, which this technique contributes to)
- **Quote**: "Breakpoints only help if the prefix itself stays stable, so we also tightened what sits at the front of each request. We did this by reserving tools and system instructions for content that rarely changes, and by moving more variable setup past the cache boundaries into our \"phantom user message.\" This holds user- and request-specific context like skills, subagents, and environment info."
- **Our assessment**: The "phantom user message" term is novel to the corpus — no other source note names this specific pattern (a synthetic message inserted to hold variable context past the cache boundary rather than mixing it into the system prompt). It is structurally the same idea as Claude Code's `<system-reminder>` pattern described in `blog-anthropic-prompt-caching-everything.md` Claim 5 (dynamic updates sent via a message construct that doesn't disturb the cached prefix), but the two mechanisms are not identical: Claude's `<system-reminder>` is inserted into the next user message or tool result to convey specific updates (timestamps, file changes), while Cursor's "phantom user message" appears to be a dedicated, always-present message slot for a broader category of session-variable content (skills, subagents, environment info). Treat as a corroborating but distinct implementation of the same "isolate the mutable part of the request into its own slot" principle.

### Claim 9: Numbering only every tenth line (instead of every line) in file reads reduced cache-read tokens by 1.6% with no reduction in quality, because a single line number costs roughly three to five tokens and agents read tens of thousands of lines per session
- **Evidence**: First-party description of the change and its rationale, with an order-of-magnitude token cost estimate for a single line number.
- **Confidence**: emerging (specific figure given; "no reduction in quality" is asserted without describing the quality metric or test used)
- **Quote**: "A single line number uses only around three to five tokens, but when an agent reads tens of thousands of lines during a session, numbering every one adds a meaningful amount of context. We reduced that overhead by including line numbers only on every tenth line. This is still frequent enough for models to cite code properly, and the change reduced cache-read tokens by 1.6% with no reduction in quality."
- **Our assessment**: This is the smallest of the six reported deltas (1.6%), which the post itself frames as a modest optimization relative to the tool-loading and cache-breakpoint changes. It is a concrete, directly-testable technique (sparse line numbering in file-read tool output) that any harness author using a numbered-line Read tool could try, with the specific caveat the post gives: numbering must stay "frequent enough for models to cite code properly" — the post does not state what threshold makes citation unreliable below every-tenth-line, so teams should validate before matching Cursor's specific interval.

### Claim 10: Subagent delegation reduces token spend because each subagent starts with a fresh context window instead of carrying the parent agent's full conversation, but this context isolation carries a "coordination tax" where agents that don't share context can duplicate work or pursue unnecessary tasks
- **Evidence**: First-party description of the tradeoff, stated as the framing for the subagent section.
- **Confidence**: emerging (mechanism and tradeoff both named; the "coordination tax" is not quantified)
- **Quote**: "This can reduce token spend because each subagent typically starts with a fresh context window rather than carrying the parent agent's full conversation. Once it reports its results, the parent can continue without carrying the subagent's full working context. This kind of context isolation between agents and subagents does carry a coordination tax, though, because agents that do not share context can duplicate work or pursue tasks that are no longer necessary."
- **Our assessment**: "Coordination tax" as a named cost of subagent context isolation corroborates the general finding in `blog-cursor-agent-swarm-model-economics.md` Claim 2 (a planner's or worker's narrowed context is framed as the *reason* multi-agent decomposition scales, i.e., context efficiency is the benefit) and Claim 3 (Coase's theory of the firm — coordination costs growing faster than the work itself — offered as the economic analogy for why unbounded agent meshes underperform bounded, tree-shaped organization). This post is the first in the corpus to name the isolation/coordination tradeoff specifically in *token* terms (isolation saves tokens per-subagent but risks token-wasting duplicate work), rather than in the correctness/organizational terms the swarm-economics post uses.

### Claim 11: Cursor removed system-prompt instructions that had strongly encouraged agents to delegate codebase exploration to subagents, because models had independently learned that pattern from training data and post-training, and removing the extra prompting produced more balanced subagent usage
- **Evidence**: First-party description of a specific prompt change and its stated cause (models learning the pattern natively) and effect (more balanced usage).
- **Confidence**: anecdotal (directional claim about model training data trends; no before/after subagent-usage-rate numbers published, "more balanced" is not defined quantitatively)
- **Quote**: "First, we removed instructions that strongly encouraged agents to use subagents for codebase exploration. As subagents became more prevalent in training data and researchers incorporated them into post-training, models learned this pattern natively. Removing the extra prompting produced more balanced subagent usage."
- **Our assessment**: This is the same harness-simplification-as-models-improve pattern as Claim 2 (system prompt trimming) applied specifically to subagent-delegation instructions: an explicit instruction becomes redundant once the underlying model behavior is learned natively, and keeping the instruction around risks *over*-triggering the behavior (implied by "more balanced" replacing what was presumably over-eager subagent use). This is a specific, dated (as of Sep 2026) data point for the general claim that harness prompts should be periodically re-tested for redundancy as frontier models incorporate more agentic post-training.

### Claim 12: Cursor tightened how subagents select which model to run on, updating tool arguments so a subagent only uses a different model than its parent when explicitly directed by the user or the harness — rather than being freely selectable — even though subagents can in principle run on any available model
- **Evidence**: First-party description of a tool-argument change and its rationale (subagent model choice can "shore up blind spots" or pair an expensive planner with a cheaper implementer, but was apparently being selected in unintended ways before the change).
- **Confidence**: anecdotal (change and rationale described; no data on how often unintended model selection was occurring before the fix, or how usage changed after)
- **Quote**: "We also tightened how subagents select models. Cursor can spawn subagents using any of our available models, which makes it possible to shore up blind spots across models or pair an expensive planning model with a cheaper one for implementation. We updated the tool arguments so agents choose a different model only when directed by the user or the harness."
- **Our assessment**: The post frames this as a token-efficiency change (grouped under "using subagents strategically" alongside Claim 11), but the described mechanism reads more like a cost/reliability guardrail against ungoverned model selection by the agent itself, similar in spirit to the admin allow/block-list model governance described in `blog-cursor-router-model-classifier.md` Claim 10 — though that source describes *admin*-level controls on Cursor Router's model routing product, while this claim describes tightening the *agent's own* runtime tool arguments for subagent spawning. These are different governance layers (product-admin policy vs. harness/tool-schema constraint) addressing a similar underlying concern (uncontrolled model selection driving up cost or introducing quality variance).

### Claim 13: Cursor expects harness-level token efficiency work to let token use grow far more slowly than the amount of work agents can complete, and has begun applying these learnings to Grok Bot's harness
- **Evidence**: Forward-looking closing statement.
- **Confidence**: anecdotal (forward-looking; no committed roadmap or metric)
- **Quote**: "Over time, we expect this will allow token use to grow far more slowly than the amount of work agents can complete. We've also taken these learnings to Grok Bot, where we're working to optimize its unique harness so that users can accomplish the most work at the lowest cost."
- **Our assessment**: Notable mainly for confirming that Cursor now maintains (at least) two distinct production agent harnesses — its own agent and Grok Bot — and is explicitly porting harness-efficiency techniques between them. This is a forward-looking, unquantified claim; treat as context about Cursor's product surface rather than as evidence for the guide.

## Concrete Artifacts

### Six changes and their reported token-efficiency deltas
```
# "Improved token efficiency for longer agent runs" — Cursor, Sep 23, 2026
# Source: Jediah Katz, Connor O'Keefe & Calvin Yee

Change                                    Reported delta
--------------------------------------    -----------------------------------
System prompt trimming                    ~66% of system prompt removed
                                           ("DO NOT" / "You must" / "Important"
                                           instructions replaced by tool-behavior
                                           definitions)
Built-in tool lazy loading                60% reduction in static-context
  (retained: read/search/edit/shell,      tool-description tokens
   ask_question, create_plan)
  (precedent: MCP tools moved to lazy     46.9% total-token reduction across
   loading "earlier this year")           sessions that called an MCP tool
Explicit cache breakpoints (GPT-5.6)      20% reduction in cold cache misses
  + "phantom user message" for variable
  setup (skills, subagents, env info)
File-read line-numbering                  1.6% reduction in cache-read tokens
  (every line -> every 10th line)         (no quality reduction reported)
Subagent prompting + model-selection      not separately quantified
  tightening

Aggregate (all six changes combined):     7% reduction in token costs,
                                           "without reducing agent quality"
```

### Tool retention criteria (built-in tool lazy loading)
```
# Source: same post, "Loading tools only when needed" section

KEPT IN STATIC CONTEXT:
  - High-frequency tools: reading, searching, editing, shell access
  - ask_question           (models tended to hallucinate calls for it if absent)
  - create_plan             (crucial to Plan Mode specifically)

OFFLOADED TO DYNAMIC CONTEXT (loaded on demand):
  - All other built-in tools (each needed in <20% of conversations)

Selection method: A/B tested configurations; tracked token usage, cost,
latency, tool-call errors, and overall agent usage
```

### "Phantom user message" cache-boundary placement
```
# Source: same post, "Improving cache reuse" section

[STABLE PREFIX — cache breakpoint placed here, GPT-5.6 explicit breakpoints]
  - Tools
  - System instructions
[PHANTOM USER MESSAGE — variable, request-specific, placed AFTER breakpoint]
  - Skills
  - Subagents
  - Environment info
[GROWING CONVERSATION]
  - Turn-by-turn messages
```

## Cross-References

- **Corroborates**: `blog-anthropic-prompt-caching-everything.md` Claim 3
  ("static content first, dynamic content last" as the foundational rule for
  prompt structure under prefix caching) — Cursor's practice of reserving
  "tools and system instructions for content that rarely changes" and moving
  "variable setup past the cache boundaries" (Claim 8) is the same ordering
  principle applied to a different provider's caching API.
- **Corroborates**: `blog-anthropic-prompt-caching-everything.md` Claim 7
  (changing the tool set mid-session is "one of the most common ways people
  break prompt caching") and Claim 9 (Claude Code's fix: lightweight
  `defer_loading: true` stubs that stay in the cached prefix while full
  schemas load on demand) — Cursor's built-in-tool lazy loading (Claim 5)
  and its earlier MCP lazy loading (Claim 4) describe the same underlying
  fix (keep a lightweight tool reference always present; load the full
  definition only on use) independently arrived at on a different harness.
- **Corroborates**: `blog-cursor-agent-swarm-model-economics.md` Claim 2
  (context efficiency — a narrower context per agent role — is the reason
  the swarm's tree-shaped decomposition scales) and Claim 3 (coordination
  costs growing faster than the work itself, via the Coase theory-of-the-firm
  analogy) — this post's "coordination tax" (Claim 10) names the same
  tradeoff in token-efficiency terms rather than the swarm-economics post's
  correctness/organizational terms.
- **Extends**: `blog-cursor-router-model-classifier.md` Claim 11 ("dynamic
  tool calling," described in July 2026 as a forward-looking, unquantified
  effort to lazy-load native tool descriptions "mirroring the existing MCP
  pattern") — this September 2026 post is the direct follow-through, giving
  the first published figures for both the built-in-tool version (60%
  static-context token reduction, Claim 5) and the earlier MCP-only version
  (46.9% total-token reduction, Claim 4) of the same technique.
- **Extends**: `blog-cursor-continual-harness-improvement.md` Claim 12 (the
  harness evolved from heavy static context toward dynamic, tool-fetched
  context as models improved) — this post's system-prompt trimming (Claim 2)
  and tool lazy-loading (Claim 5) are concrete, dated (Sep 2026) continuations
  of the same static-to-dynamic trajectory that the April 2026 post described
  more abstractly for retrieval context (folder layouts, semantic snippets).
- **Extends**: `blog-bswen-mcp-token-cost.md` Claim 1 (every MCP server
  loads its full tool definitions into the system prompt before the user
  types anything) and Claim 2 (MCP token cost scales roughly linearly with
  server count) — Bswen's post documents the problem in Claude Code with no
  mitigation beyond "prune your server list." This Cursor post documents a
  structural fix to the same problem (lazy-load definitions instead of
  pruning servers) with a quantified result (46.9% reduction, Claim 4) on a
  different harness.
- **Novel**: The following are new to the corpus:
  - The "phantom user message" term and pattern (Claim 8) — a dedicated
    message slot for variable, request-specific context placed after the
    cache boundary
  - GPT-5.6's explicit client-marked cache breakpoints as a provider
    mechanism distinct from Claude's automatic longest-prefix-match caching
    (Claim 7)
  - Sparse line-numbering (every 10th line) in file-read tool output as a
    token-compression technique, with an order-of-magnitude per-line-number
    token cost estimate (~3–5 tokens) (Claim 9)
  - "Coordination tax" as an explicit named cost of subagent context
    isolation, stated in token-efficiency terms (Claim 10)
  - The 46.9% (MCP lazy loading) and 60% (built-in tool lazy loading) token
    reduction figures (Claims 4, 5) — the first quantified Cursor-side
    numbers for a pattern previously only described qualitatively in the
    corpus

## Guide Impact

- **Chapter 03 (Agent patterns) / Chapter 02 (Harness Engineering — tool
  loading)**: Add the tool-retention heuristic from Claim 5 as concrete
  guidance for teams building tool-heavy harnesses: keep tools static only
  if they are high-frequency (used in most conversations) or if omitting
  them causes the model to hallucinate calls to them; lazy-load everything
  else. Cite the 60% static-context reduction and the "<20% of conversations"
  threshold Cursor used to decide what to offload. Pair with the existing
  `blog-anthropic-prompt-caching-everything.md` Claim 9 (`defer_loading`
  stubs) so the guide states this as a technique now independently validated
  on two different harnesses (Claude Code and Cursor).

- **Chapter 05 (System design) / Chapter 02 (Harness Engineering — caching)**:
  Add the "phantom user message" pattern (Claim 8) as a named technique for
  isolating variable, request-specific context (skills, subagents,
  environment info) from the stable, cacheable prefix. Note the provider
  distinction from Claim 7: teams on OpenAI's GPT-5.6 API can use explicit
  client-marked cache breakpoints, while teams on Claude's API rely on
  automatic prefix matching and must achieve the same effect purely through
  ordering discipline (per `blog-anthropic-prompt-caching-everything.md`
  Claim 3).

- **Chapter 06 (Economics/cost optimization)**: Add sparse line-numbering
  (every 10th line, Claim 9) as a low-effort, low-risk token-compression
  technique for any harness with a line-numbered file-read tool. This is the
  smallest of the six reported deltas (1.6%) and should be framed as a
  "free" optimization rather than a major lever — the guide's cost-reduction
  priority ordering should put tool lazy-loading (Claim 5, 60%) and cache
  breakpoint placement (Claim 7, 20%) ahead of it.

- **Chapter 03 (Agent patterns — subagents)**: Add "coordination tax" (Claim
  10) as the token-efficiency-specific framing of the general
  isolation-vs-coordination tradeoff already documented for multi-agent
  swarms (`blog-cursor-agent-swarm-model-economics.md`). Also add Claim 11
  (removing subagent-encouraging instructions once models learn the pattern
  natively) as a specific, dated example of the "re-test harness prompts for
  redundancy as models improve" principle, applied to subagent-delegation
  prompting specifically.

- **Chapter 02 (Harness Engineering — validation methodology)**: Add Claim 6
  (A/B testing tool-loading configurations while tracking token usage, cost,
  latency, tool-call errors, AND overall agent usage) as a concrete example
  of the "measure quality alongside cost" discipline the guide should
  recommend whenever citing a token-savings technique — a savings number
  alone is not sufficient evidence a change is safe to ship.

## Extraction Notes

- WebFetch's default summarization pipeline returned a condensed, paraphrased
  version of this article rather than verbatim text, which is insufficient
  for quote extraction per MINER.md §2a. The full article was instead
  retrieved via direct HTTP fetch (`curl`) and HTML-tag-stripped to recover
  the verbatim article text, which was used for all quotes above. All quotes
  were checked against this verbatim text extraction, not the summarized
  WebFetch output.
- The post is short (7-minute read, six named sections plus intro/close) and
  was read in full; no linked sub-pages within the post itself required
  following (it links to the Cursor Router post and MCP dynamic-context
  precedent only in passing, both of which are already in the corpus as
  `blog-cursor-router-model-classifier.md`).
- The post includes two data visualizations ("Where agent inference spend
  goes" — a stacked breakdown by category/billing type, and "Most commonly
  invoked tools" — share of conversations invoking each tool) that render as
  interactive charts and did not yield extractable numeric values or axis
  labels beyond their category names and captions in the stripped-HTML
  fetch. These are noted as chart-only artifacts; no claim above relies on
  reading values off these charts.
- No contradictions found, either within this post or against existing
  source notes. The explicit-cache-breakpoint mechanism (Claim 7) initially
  looked like it might conflict with Claude Code's automatic-only caching
  model, but on inspection this is a provider-capability difference (OpenAI
  GPT-5.6 API offering explicit breakpoints vs. Claude's automatic
  longest-prefix-match), not a disagreement about the underlying principle —
  both sources agree stable-prefix-first ordering is what matters. No
  contradiction issue filed.
- `confidence_overall` set to "emerging": the post is a credible first-party
  operational account (named engineers, specific named mechanisms) but every
  quantitative figure is self-reported with no disclosed methodology,
  sample size, or measurement window, consistent with how other first-party
  Cursor posts are graded in this corpus (e.g., `blog-cursor-router-model-classifier.md`,
  `blog-cursor-continual-harness-improvement.md`).
