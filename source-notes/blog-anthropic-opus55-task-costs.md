---
source_url: https://claude.com/blog/what-a-task-costs-on-opus-5-5
source_type: blog-post
title: "What a task costs on Opus 5.5"
author: Addy Osmani
date_published: 2026-09-22
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: settled
issue: "#3628"
---

# What a task costs on Opus 5.5

> First-party Anthropic guidance breaking Claude Code task cost into four
> levers (turns, cache reads, output tokens, model), giving Opus 5.5's exact
> API list prices and its price cuts versus Opus 5, a worked effort-level
> ROI heuristic, a three-model daily-driver/frontier/lookup selection
> pattern, cache-write/TTL pricing not previously in the corpus, and a
> measured 18%+9% cost reduction from a model migration plus a prompt-audit
> pass on an internal 44-ticket benchmark.

## Source Context

- **Type**: blog-post (official Claude blog, claude.com/blog; "Claude Code"
  category, "Claude Code" product tag; published September 22, 2026;
  ~5 minute read time)
- **Author credibility**: Bylined to Addy Osmani, with an acknowledgments
  line thanking three named Anthropic reviewers (Michael Segner, Kacie
  Jenkins, Molly Vorwerck) for review — a first-party post on Anthropic's
  own product blog, not a third-party guest post despite the named author.
  Pricing figures, slash-command behavior, and cache-lifetime mechanics are
  settled first-party statements about shipping Claude Code behavior. The
  post explicitly flags its own worked examples as illustrations rather
  than measurements: "Some numbers here are list prices, and some are
  illustrations built from them... These are best effort illustrations, so
  be sure to check our docs and your own math." The one benchmark result
  in the post (the 44-ticket customer-support migration, Claim 12) is
  presented as "one benchmark," explicitly flagged by the post itself as
  "an example rather than a number to expect."
- **Scope**: Covers Opus 5.5 API list pricing versus Opus 5, the four
  cost-driver taxonomy (turns/cache reads/output tokens/model), effort
  levels and when to raise them, model selection (Opus 5.5 as daily
  driver, Fable 5.1 for high-stakes/unsupervised work, Sonnet/Haiku for
  subagent lookups, the `opusplan` alias), cache mechanics (TTL by access
  method, what busts the cache, write-vs-read pricing), compaction
  economics, and how to measure your own costs via `/usage`/`/cost`. Does
  NOT cover: Claude Enterprise admin-level cost controls (access gating,
  spend caps) — that is `blog-anthropic-cost-visibility-control.md`'s
  territory, linked from this post's "Manage costs effectively" further-
  reading link but not itself covered here. Does NOT give the contents of
  the "rest of the bill" table (rendered as an image, not extractable
  text — see Extraction Notes) or the interactive calculator's full slider
  logic beyond the example values reproduced in Concrete Artifacts.

## Extracted Claims

### Claim 1: Task cost in Claude Code is set by four factors — turns (each resends the whole conversation), cache reads (billed at a fraction of input price), output token type (the most expensive, and includes thinking), and model (sets the price of every token)
- **Evidence**: Direct enumeration in the "What does a task cost?" section, opening the post's cost model.
- **Confidence**: settled
- **Quote**: "Four things set what the loop costs. Turns. Every turn resends the conversation so far. Fewer turns means less input processed. Cache reads. Most of what a turn resends is text the model saw on the previous turn. It's billed as a cache read, at a small fraction of the input price. Output token type. The most expensive tokens, at five times the input price. Thinking is billed as output, so a model that reasons less on the way to the answer costs less. Model. Each model has its own prices, listed on the pricing page, so the model you pick sets the price of every token."
- **Our assessment**: This is the organizing framework for the rest of the post and gives the guide a citable four-factor taxonomy distinct from `blog-anthropic-maximizing-session-value.md`'s pricing-mechanics framing (that note leads with "token price is a proxy for GPU inference time" and covers three of the same four factors — output/input ratio, cache pricing, context accumulation — but does not name "turns" as an independent lever the way this post does). Note the "five times the input price" figure for output tokens here is the general/Opus-5-era ratio the post uses in this framing section; Claim 3 below gives the Opus-5.5-specific ratio versus cache reads specifically (100x), which is a sharper, model-specific number.

### Claim 2: Opus 5.5 API list prices are $4 per million input tokens, $20 per million output tokens, and $0.20 per million cache reads — a 20% cut on input/output versus Opus 5's $5/$25, and a 60% cut on cache reads versus Opus 5's $0.50
- **Evidence**: Direct pricing statement, cross-verified against the raw HTML's embedded pricing-widget JavaScript, which encodes `PRICES = { prev: {input: 5, output: 25, cacheRead: 0.50}, new: {input: 4, output: 20, cacheRead: 0.20} }`.
- **Confidence**: settled (first-party list pricing, corroborated by both the prose and the page's own interactive-widget source data)
- **Quote**: "Our examples use Opus 5.5 API list prices: $4 per million input tokens, $20 per million output tokens and $0.20 per million cache reads." And: "Input and output tokens are 20% cheaper than on Opus 5. Cache reads are 60% cheaper."
- **Our assessment**: The Opus 5 baseline this claim implies ($5/$25/$0.50) is independently corroborated by `blog-simonwillison-llm-anthropic-0251.md` Concrete Artifacts ("Standard Opus 4.8 pricing: $5 / MTok, $25 / MTok"), since `blog-simonwillison-introducing-opus-5.md` Claim 3 established Opus 5 is priced identically to Opus 4.8. This is a clean three-source chain (this post → Opus 5 = Opus 4.8 price → Opus 4.8's own documented $5/$25 figures) with no discrepancy found. The $0.20 cache-read price on Opus 5.5, against a $4 input price, works out to 5% of input — a sharper cut than the general "cache reads cost 10% of input" convention documented elsewhere in the corpus (`blog-anthropic-cost-visibility-control.md` Claim 11; `blog-anthropic-maximizing-session-value.md` Claim 3's "0.1x"). This is not a contradiction — those figures describe the general/prior-generation ratio, and this post explicitly frames the 60%-vs-20% cut as *changing* that ratio for Opus 5.5 specifically ("The input price falls, and the read rate falls with it, from a tenth of the input price to a twentieth"). The guide should treat "cache reads cost ~10% of input" as the pre-Opus-5.5 baseline and this post's 5% figure as the current Opus 5.5 number.

### Claim 3: On Opus 5.5, an output token costs 100 times a cache read (versus 5x the *input* price in the general framing), and a 60K-output-token task costs $1.20 — the same as reading 6M tokens from cache
- **Evidence**: Direct statement in the "Output tokens" subsection, with a worked cost comparison.
- **Confidence**: settled
- **Quote**: "On Opus 5.5, an output token costs 100 times a cache read. The 60K output tokens of a typical task cost $1.20, the same as reading 6M tokens from cache. Output includes thinking. You pay for all of it, even when Claude Code only shows you a summary."
- **Our assessment**: The 100x-cache-read ratio is model-specific to Opus 5.5 and is the sharpest version of the "output is far more expensive than everything else" point in the corpus — more specific than the general "output ≈ 5x input" ratio in `blog-anthropic-maximizing-session-value.md` Claim 2, because it's benchmarked against the cheapest cost line (cache reads) rather than input. This directly explains why the post ties effort level (which "mostly changes how much the model thinks") to the single biggest cost lever: thinking tokens are billed as output, at the 100x-cache-read rate.

### Claim 4: A worked example shows turn count alone changing cost by ~59% for the same task shape — a 40-turn version of a task that grows from 20K to 120K tokens of context costs about $1.62 in input at a 90% cache-hit rate, while a 25-turn version of the same task costs about $1.02
- **Evidence**: Worked numeric example in the "Turns" subsection.
- **Confidence**: settled (worked example built from stated list prices, explicitly framed by the post as an illustration, not a measured task)
- **Quote**: "Let's say a task starts with 20K tokens of context and grows to 120K as the model reads files and tool results. At 40 turns, the average turn sends about 70K tokens. That's about 2.8M input tokens for the task, though the conversation never grew past 120K. With 90% read from cache, the input costs about $1.62. The same task in 25 turns processes about 1.75M tokens and costs about $1.02 in input. A turn costs more than the tokens it adds, because it resends everything before it. So the cheapest turn is the one you don't need."
- **Our assessment**: This is the clearest single illustration in the post of why "turns" is listed as its own cost factor separate from context size — the *same* final context size (120K) costs 59% more in a 40-turn session than a 25-turn session, purely from how many times that context got resent. The post's stated mitigation — "giving the model a way to check its work" (a test, a build, a script) so it finds mistakes earlier, and "batches its tool calls" to gather what it needs in one pass — gives the guide a concrete practitioner action tied to a concrete number, rather than a vague "reduce turns" recommendation.

### Claim 5: Cache-hit rate alone moves input cost more than any other single setting — the same 2.8M input tokens cost $11.20 with no cache, $1.62 at a 90% hit rate, and about $0.99 at a 96% hit rate
- **Evidence**: Direct numeric comparison in the "Cache reads" subsection, continuing the Claim 4 example.
- **Confidence**: settled
- **Quote**: "The same 2.8M input tokens cost $11.20 if none come from cache. At a 90% hit rate they cost $1.62, and at 96% about $0.99. No other setting moves input cost this much. A steady session keeps a high hit rate on its own."
- **Our assessment**: This quantifies the stakes of cache-hit rate directly: going from 0% to 90% cached is an ~86% cost reduction on input, and the marginal gain from 90% to 96% (a further ~39% reduction on the already-discounted figure) shows diminishing but still meaningful returns near the top of the range. This gives the guide a concrete "why cache hygiene matters" number to pair with `blog-anthropic-maximizing-session-value.md`'s list of specific cache-busting triggers (model switch, effort-level change, MCP connect/disconnect, session gap) — this post's Claim 8 below gives Opus-5.5-specific cache-bust triggers, and Claim 9 quantifies the write-vs-read cost gap those triggers cause.

### Claim 6: A same-token-count session comparison (Fig B) shows Opus 5.5 costing about 31% less than the identical session on Opus 5, priced at $3.50 on Opus 5 versus the lower Opus 5.5 total — isolating the price change alone from any change in how much work the model does
- **Evidence**: Description of the page's interactive Fig B comparison, whose underlying JavaScript encodes `EXAMPLE = {cachedInput: 2000000, freshInput: 200000, output: 60000}` and computes the percentage reduction dynamically; the prose states the resulting percentage explicitly.
- **Confidence**: settled (a worked example built from stated list prices and a fixed illustrative token mix, not a measured real session — the post is explicit that "your own sessions can use more or fewer tokens on Opus 5.5" than this fixed comparison assumes)
- **Quote**: "Fig B gives both models the same token counts, so it shows the price change alone... Priced that way, the session costs about 31% less. A recorded run adds the second effect, the change in how much work the model does. On a task with a false start, the gap should widen."
- **Our assessment**: This is the post's key methodological separation: it isolates *price change* (31%, from Claim 2's per-token cuts) from *behavior change* (how many tokens/turns Opus 5.5 actually uses on a real task, which the post says it does not claim to know in general — "Opus 5.5 can use more tokens on an answer, because it always thinks before it replies... it varies by task, so measure it on your own work"). The guide should present the 31% figure as a same-tokens price-only comparison, not as an expected real-world savings percentage, and pair it with Claim 12's measured example (18%+9% = 25% reduction on a real benchmark) as the one case in the post where both effects were actually measured together.

### Claim 7: Claude Code exposes five effort levels (low, medium, high, xhigh, max) via `/effort <level>`; the post gives an explicit ROI heuristic — a high-effort task adding ~20K thinking tokens costs about $0.40 on Opus 5.5, roughly what a 10-turn retry loop (100K cached context, 10K total output tokens) costs, so raising effort "pays for itself on a task where it saves one retry" but is "wasted" on a task medium would have solved anyway
- **Evidence**: Direct description of the effort ladder and a worked cost-equivalence example in "Raise effort before you change models."
- **Confidence**: settled for the mechanism and heuristic; the specific $0.40-vs-retry-loop figures are worked illustrations, not a measured comparison
- **Quote**: "Claude Code sets a default level for each model, and `/effort status` shows yours. Try medium for well-scoped, day-to-day work. When medium stalls, try high. It spends more per turn than medium, but less than moving to a bigger model. Use low for mechanical work, like renames or applying a known pattern across files. A rough way to think about effort pricing: say high adds 20K thinking tokens across a task. On Opus 5.5 that's $0.40. A retry loop of ten turns at 100K of cached context, with 10K output tokens in total, costs about the same. So high pays for itself on a task where it saves one retry. On a task medium would have finished the first time, it's wasted."
- **Our assessment**: **Extends** `blog-anthropic-choosing-claude-model.md` Claim 7 (effort as a second axis independent of model class, illustrated only with unlabeled curves) and `blog-anthropic-cost-visibility-control.md` Claim 13 (effort dialed down for routing/extraction, up for final output) — both prior sources describe effort qualitatively; this post is the first in the corpus to attach a concrete dollar figure and a break-even comparison (cost of raising effort vs. cost of a retry) to the effort decision. The diagnostic given for *when* to raise effort — "the clearest sign you need more effort is a fix that stops at one layer" (e.g., an API field rename fixed in the handler but not in the caller) — is also new and concrete: a specific bug pattern (partial multi-file fixes) as the trigger, distinct from a generic "if it's not working, try harder" heuristic. The post also notes changing effort mid-session busts the cache (Claim 8), which the ROI math above does not include as a cost — the true cost of raising effort mid-task is the $0.40 illustration *plus* a cache-write penalty.

### Claim 8: Five specific actions cause a Claude Code cache write instead of a cache read: pausing longer than the cache lifetime, changing effort or thinking settings, connecting/disconnecting an MCP server, switching models, and compaction
- **Evidence**: Direct enumerated list in "Session shape and hit rate."
- **Confidence**: settled
- **Quote**: "In practice, expect a cache write when: You pause longer than the cache lifetime; You change effort or thinking settings (see the effort section), which can clear the cached conversation; You connect or disconnect an MCP server, which can change what loads at the start of each request; You switch models, since the new model starts from an empty cache; and The conversation is compacted, which rewrites the history the cache matched."
- **Our assessment**: **Corroborates and extends** `blog-anthropic-maximizing-session-value.md` Claim 5 (model switch, effort-level change, fast-mode toggle, and hour-long pause as cache-busting triggers) — this post's list overlaps on three of those four (model switch, effort change, pause) but adds MCP connect/disconnect and compaction as explicit triggers not named in that note, and does not mention fast-mode toggling at all (fast mode is not discussed anywhere in this post). Combined, the corpus now documents six known Claude Code cache-bust triggers across the two sources: model switch, effort/thinking-setting change, fast-mode toggle (prior note only), pause past TTL, MCP connect/disconnect (this note only), and compaction (this note only).

### Claim 9: Writing to the cache costs more than reading from it, at a rate that depends on the cache lifetime — 1.25x the input price for a five-minute cache and 2x the input price for a one-hour cache — illustrated at 120K tokens of context, where a five-minute write costs about $0.60 and a read about $0.02 (one write equals about 25 reads), and a one-hour write at the same size costs about $0.96
- **Evidence**: Direct pricing statement with worked numeric example in "How the cache works."
- **Confidence**: settled
- **Quote**: "Writing to the cache costs more than a fresh read, at 1.25 times the input price for a five-minute cache and twice the input price for a one-hour cache, on today's pricing. Each hit resets the lifetime at no charge... At 120K tokens of context, a five-minute write on Opus 5.5 costs about $0.60 and a read about $0.02. One write costs as much as 25 reads. On an API key, a six-minute coffee break turns the next $0.02 read into a $0.60 write. A one-hour write at the same size costs about $0.96, and on the API you can pay that premium to cover the gaps in your day."
- **Our assessment**: This is a more granular figure than the corpus previously had: `blog-anthropic-maximizing-session-value.md` Claim 3 states cache writes cost "up to 2x" input without distinguishing TTL, and Claim 4 of that same note documents the 1-hour-subscription/5-minute-API-key TTL split, plus the `ENABLE_PROMPT_CACHING_1H=1` override — but does not connect TTL choice to a *different write price*. This post supplies that missing link: the 1-hour cache isn't just longer-lived, it's also priced higher per write (2x vs 1.25x input) than the 5-minute cache. That means `ENABLE_PROMPT_CACHING_1H=1` is not a strictly-better default for API-key users — it trades a lower miss *frequency* for a higher cost *per* write, a tradeoff the guide should state explicitly rather than presenting the 1-hour override as a pure win.

### Claim 10: Every turn resends the entire context, so the same number of turns costs more as context grows even with a warm cache — at 20K tokens of context a turn's cache read costs about $0.004 on Opus 5.5, but at 150K tokens it costs about $0.03 (30 turns at that size spend $0.90 on reads alone, versus $0.12 for 30 turns at 20K)
- **Evidence**: Direct numeric comparison in "Why long sessions cost more per turn."
- **Confidence**: settled
- **Quote**: "Every turn resends the whole context, so a turn costs more as the context grows, even with a warm cache. At 20K tokens of context a turn's cache read costs about $0.004 on Opus 5.5. At 150K it costs about $0.03, and 30 turns at that size spend $0.90 on reads alone. The same 30 turns at 20K cost about $0.12. On Claude 4.6 and later models a bigger context window doesn't change the price per token, so the cost comes entirely from resending the conversation."
- **Our assessment**: **Corroborates** `blog-anthropic-maximizing-session-value.md` Claim 6 ("everything that ends up in the conversation... gets sent again on every turn after it, for the rest of the session") — that note states the mechanism; this post supplies the missing numeric magnitude, showing a 7.5x context-size increase (20K→150K) produces a 7.5x per-turn cost increase (proportional, as expected for a linear cache-read cost), and that 30 turns at the larger size costs 7.5x more in aggregate reads ($0.90 vs. $0.12). The explicit callout that "a bigger context window doesn't change the price per token" on Claude 4.6+ models rules out one possible confound (that long-context models might charge a premium for large windows) — the cost is purely a function of how much gets resent, not a window-size surcharge.

### Claim 11: `/compact` at 150K tokens costs about $0.25 (the read of what's being summarized, a summary of a few thousand output tokens, and a new cache write on the shorter context) and pays for itself within about ten turns, saving roughly $0.025 per later turn in reduced reads — but compacting just before finishing a task costs more than it saves, and can drop details a debugging session still needs
- **Evidence**: Direct numeric compaction cost-benefit statement with an explicit caveat, in "Compaction, /compact and /clear."
- **Confidence**: settled
- **Quote**: "A rough price for compacting at 150K tokens is about $0.25. That's the read, a summary of a few thousand output tokens, and a new cache write on the shorter context. Each later turn saves about $0.025 in reads, so the compaction pays for itself within about ten turns. A compaction just before you finish costs more than it saves. The summary also loses detail. A compaction in the middle of a debugging session can drop the one log line that mattered."
- **Our assessment**: This gives the guide a concrete break-even number (~10 turns) for a "should I compact now?" decision rule — earlier corpus coverage (`blog-anthropic-session-management-1m-context.md` Claim 6, per `blog-anthropic-maximizing-session-value.md`'s cross-reference, frames `/compact` vs `/clear` as "who decides what matters," not a cost/turns-remaining tradeoff). This post adds the missing quantitative side: compact only if you expect at least ~10 more turns in the session, and pass explicit `/compact` instructions (e.g., "keep the failing test names and the schema change") to reduce the risk of losing debugging-relevant detail the summary would otherwise drop.

### Claim 12: On an internal 44-ticket customer-support benchmark testing migration from Opus 4.8 to Opus 5.5, switching models alone (at low effort) cut cost by about 18%; running `/claude-api prompt-audit` to remove ritual/contradictory prompt instructions cut cost by a further 9%, for a total of about 25% below the Opus 4.8 starting point
- **Evidence**: Named internal benchmark with a two-stage measured result, in "Check your prompts when you migrate," illustrated in the post's "Fig D."
- **Confidence**: emerging (a specific, named internal benchmark with concrete percentages, but the post itself explicitly caveats it as a single, non-generalizable data point)
- **Quote**: "We tested this on a migration from Opus 4.8 to Opus 5.5, using an internal customer support benchmark of 44 tickets whose prompt had several of these patterns. The move to Opus 5.5, at low effort, cut the benchmark's cost by about 18%. Running prompt-audit cut it by a further 9%, to about 25% below the Opus 4.8 starting point. The audit removed ritual instructions that made the model write more and repeat tool calls: a mandatory six-step procedure, a scratchpad rule, a verify-twice rule, and instructions that contradicted each other... That result comes from one benchmark, so treat it as an example rather than a number to expect. Run the audit, then compare `/usage` on a real task before and after."
- **Our assessment**: This is the single most concrete, measured (not illustrative) cost figure in the post, and it is novel to the corpus: no existing source note documents the `/claude-api prompt-audit` command, nor gives a measured before/after cost delta from removing "ritual instructions" (mandatory step-count procedures, scratchpad rules, verify-twice rules, self-contradicting instructions) from a production prompt. This corroborates the general "prompts written for an older model can make a newer model write more and repeat tool calls" mechanism the post states just before this example, and gives the guide a named, runnable diagnostic tool (`/claude-api prompt-audit`, which "also checks the code of an app you build on the Claude Platform") rather than a vague "review your CLAUDE.md" recommendation. The named example anti-patterns (mandatory six-step procedure, scratchpad rule, verify-twice rule, contradictory instructions) are a concrete checklist for a prompt-audit pass even without running the tool.

### Claim 13: The recommended three-model household is Opus 5.5 as the supervised daily driver, Fable 5.1 for unsupervised long runs or problems with no existing codebase pattern, and Sonnet/Haiku for subagent lookup work (search, log-reading, "where is this defined") — not for writing code — with a stated rule to switch up after Opus 5.5 on high effort hits the same problem twice, then switch back once solved
- **Evidence**: Direct model-selection guidance across "Opus 5.5 as the daily driver," "Moving up to Fable 5.1," and "Moving down for lookups."
- **Confidence**: settled as stated first-party guidance
- **Quote**: "Use Opus 5.5 for work you supervise: feature work across a few files, debugging, and code review with follow-up edits... Move up to Fable 5.1 when the result matters more than the token price. For example long runs you won't supervise, problems with no existing pattern in the codebase, and large changes that coordinate many subagents. Don't wait for a third failure. If Opus 5.5 on high hits the same problem twice, switch, and switch back once it's solved... Move down to Sonnet or Haiku for lookups, not for writing code: subagents that search and summarize, reading logs and test output, and 'where is this defined' questions. For a mechanical edit across many files, keep Opus 5.5 and set effort to low."
- **Our assessment**: **Corroborates** `blog-anthropic-choosing-claude-model.md` Claim 4 (Sonnet named for "high-volume sub-agents in multi-agent orchestration setups") and `blog-anthropic-cost-visibility-control.md` Claim 3 (Haiku for "high-volume and routine tasks") but is more specific about *what kind* of subagent work belongs on the cheaper model — explicitly lookups/search/log-reading, explicitly *not* code-writing subagents, even for a mechanical multi-file edit (which the post says should stay on Opus 5.5 at low effort rather than move to a smaller model). The "switch after two failures, not three" threshold and "switch back once solved" instruction are new, concrete escalation/de-escalation rules not present in prior corpus coverage of the advisor-strategy or model-tiering pattern. The post also names the `opusplan` alias (Opus plans in plan mode, Sonnet executes) as an alternative split that puts code edits on Sonnet — the *opposite* of this section's general advice — and explicitly flags it as something to "measure... on your own tasks before you make it a default" rather than a recommended default, which the guide should preserve as an explicit caveat rather than presenting `opusplan` as validated guidance.

### Claim 14: `CLAUDE_CODE_SUBAGENT_MODEL` sets a default model for every subagent that doesn't specify its own `model:` field in its definition; a subagent's own `model:` setting overrides the environment variable, and a subagent with neither runs on the main session's model
- **Evidence**: Direct configuration-mechanism statement in "Moving down for lookups."
- **Quote**: "To put a subagent on a smaller model, set `model: haiku` or `model: sonnet` in its definition. To put every subagent on one model, set the `CLAUDE_CODE_SUBAGENT_MODEL` environment variable. A model named in a subagent's definition overrides the variable. A subagent with no model setting runs on your main model, unless the variable is set."
- **Confidence**: settled (first-party configuration documentation)
- **Our assessment**: This is a specific, actionable precedence rule (`model:` field > `CLAUDE_CODE_SUBAGENT_MODEL` env var > main-session model) not documented anywhere else in the corpus surveyed for this note. It gives practitioners a concrete way to implement Claim 13's "lookups on Sonnet/Haiku, code edits on Opus 5.5" split fleet-wide via one environment variable rather than editing every subagent definition individually, with per-subagent overrides available where the blanket default is wrong (e.g., a code-editing subagent that should stay on the main model even when the env var defaults everything else to Haiku).

### Claim 15: The post gives baseline real-world Claude Code cost figures — an average across enterprise deployments of about $13 per developer per active day, and under $30 per active day for 90% of users — attributed to "the Claude Code costs docs," for practitioners to benchmark their own `/usage` numbers against
- **Evidence**: Direct statement in "Reading a session," immediately following the three `/usage`-reading checks (cache share, output-vs-input ratio, total-input-vs-conversation-size).
- **Confidence**: emerging (a specific figure attributed to a separate, unlinked-in-this-note documentation source — "the Claude Code costs docs" — rather than derived or measured within this post itself)
- **Quote**: "For a baseline, the Claude Code costs docs give an average across enterprise deployments of about $13 per developer per active day, and under $30 per active day for 90% of users. A session that costs well above your own normal level is worth reviewing."
- **Our assessment**: This is the first per-developer-per-day cost baseline in the corpus for Claude Code specifically. It gives practitioners (and the guide) a concrete sanity-check number: if `/usage` shows a typical day well above $30, that is presented as an outlier worth investigating, not merely "high." Because the figure is attributed to a separate docs page (`code.claude.com/docs/en/costs`, linked elsewhere in this post as "Manage costs effectively") rather than derived in this post, the guide should cite the docs page as the primary source if it is mined separately, and this post as a secondary citation.

## Concrete Artifacts

### Opus 5.5 vs. Opus 5 pricing (from the article's pricing-widget source data and prose)
```
Source: https://claude.com/blog/what-a-task-costs-on-opus-5-5, "What changed
in Opus 5.5" section + embedded Fig A/Fig B widget JavaScript

                Opus 5 (prev)     Opus 5.5 (new)     Change
Input           $5 / MTok         $4 / MTok          -20%
Output          $25 / MTok        $20 / MTok         -20%
Cache read      $0.50 / MTok      $0.20 / MTok       -60%

Cache-read as % of input price:  10% (Opus 5)  ->  5% (Opus 5.5)
Output cost per cache-read token: 100x on Opus 5.5

Fable 5.1 (for comparison, "Choose the right model" section):
  Input:  $10 / MTok   (2.5x Opus 5.5)
  Output: $50 / MTok   (2.5x Opus 5.5)
  Cache read: $0.25 / MTok (1.25x Opus 5.5's $0.20)
```

### Worked cost examples (from the article, illustrative unless noted)
```
Source: same URL

Turns (illustrative): task grows 20K -> 120K tokens of context
  40 turns, 90% cache hit: ~2.8M input tokens -> ~$1.62 input cost
  25 turns, same shape:    ~1.75M input tokens -> ~$1.02 input cost

Cache hit rate (illustrative): same 2.8M input tokens
  0% cache:   $11.20
  90% cache:  $1.62
  96% cache:  $0.99

Output tokens (illustrative): 60K output tokens on Opus 5.5 = $1.20
  (same cost as reading 6M tokens from cache)

Fig B same-tokens session comparison (illustrative; token mix:
2M cached input + 200K fresh input + 60K output):
  Opus 5:   $3.50 (at Opus 5 list prices)
  Opus 5.5: ~31% less than Opus 5, same tokens

Long-session context cost (illustrative): per-turn cache read on Opus 5.5
  20K tokens context:  ~$0.004/turn  -> 30 turns = ~$0.12
  150K tokens context: ~$0.03/turn   -> 30 turns = ~$0.90

Effort ROI (illustrative): high effort adds ~20K thinking tokens
  Cost on Opus 5.5: ~$0.40
  Roughly equals: a 10-turn retry loop, 100K cached context, 10K output tokens

Compaction (illustrative): /compact at 150K tokens
  Cost: ~$0.25 (read + summary output + new cache write)
  Break-even: ~10 turns (each later turn saves ~$0.025 in reads)

Cache write vs. read, at 120K tokens of context (illustrative):
  5-minute cache write: ~$0.60   (1.25x input price)
  1-hour cache write:   ~$0.96   (2x input price)
  Cache read:            ~$0.02
  -> one 5-min write costs as much as ~25 reads

MEASURED (not illustrative): internal 44-ticket customer-support benchmark,
Opus 4.8 -> Opus 5.5 migration
  Model switch alone (low effort):        -18% cost
  + running /claude-api prompt-audit:     -9% further (i.e. -25% total
                                           vs. the Opus 4.8 starting point)
```

### Effort levels (verbatim descriptions, from the article's interactive effort-ladder widget)
```
Source: same URL, embedded EFFORT array in page JavaScript + surrounding prose

low     ("mechanical")   - Renames, applying a pattern across files, changes
                            you could describe in one line. Thinks least per
                            turn, so each turn costs least.
medium  ("everyday")      - Day-to-day work with a clear scope. Start here
                            when the task is well scoped. [Claude Code default
                            starting level in this widget]
high    ("if it stalls")  - Same model, more thinking per turn. Costs more per
                            turn than medium, less than moving to a larger
                            model. Try when medium fixes one layer of a
                            multi-layer change but not the other.
xhigh   ("hard problems")  - More thinking again. If xhigh hits the same
                            problem twice, move to Fable 5.1.
max     ("one session")    - Available per session, not a standing default.
                            Use for one hard task, then drop back.

Commands shown per level: /effort <level>, /effort status, /model, /usage
```

### Cache-busting triggers and CLAUDE_CODE_SUBAGENT_MODEL precedence (from the article)
```
Source: same URL

Cache write (instead of read) triggered by:
  - pausing longer than the cache lifetime
  - changing effort or thinking settings
  - connecting or disconnecting an MCP server
  - switching models
  - the conversation being compacted

Subagent model precedence:
  1. model: field in the subagent's own definition (highest priority)
  2. CLAUDE_CODE_SUBAGENT_MODEL environment variable (fleet-wide default)
  3. main session's model (fallback if neither is set)
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-llm-anthropic-0251.md` Concrete Artifacts ("Standard
    Opus 4.8 pricing: $5 / MTok, $25 / MTok") and `blog-simonwillison-
    introducing-opus-5.md` Claim 3 (Opus 5 priced identically to Opus 4.8):
    together these confirm this post's implied Opus 5 baseline ($5/$25/$0.50)
    with no discrepancy (Claim 2).
  - `blog-anthropic-choosing-claude-model.md` Claim 7 (effort as an axis
    independent of model class) and `blog-anthropic-cost-visibility-
    control.md` Claim 13 (effort dialed down for routing, up for final
    output; advisor strategy) — this post gives the first concrete dollar
    figures and break-even math for the effort decision (Claim 7).
  - `blog-anthropic-choosing-claude-model.md` Claim 4 and `blog-anthropic-
    cost-visibility-control.md` Claim 3 (Sonnet/Haiku for high-volume,
    routine, lookup-style subagent work) — this post sharpens "lookup work"
    with named examples (search, log-reading, "where is this defined") and
    an explicit "not for writing code" boundary (Claim 13).
  - `blog-anthropic-maximizing-session-value.md` Claim 5 (model switch,
    effort change, fast-mode toggle, hour-long pause bust the cache) and
    Claim 6 ("everything sent again on every turn") — this post's Claim 8
    (cache-bust triggers) and Claim 10 (turn-cost-vs-context-size numbers)
    corroborate and quantify the same mechanisms.
  - `blog-latentspace-ainews-fable-mythos-51-launch.md` Concrete Artifacts
    (Fable 5.1: $10/$50/MTok input/output, cache read cut to $0.25/MTok) —
    this post's Fable 5.1 pricing comparison in Claim 13's context matches
    exactly.

- **Contradicts**: None requiring a filed issue. The apparent tension
  between this post's Opus-5.5-specific 5%-of-input cache-read ratio
  (Claim 2) and the general "cache reads cost 10%/0.1x of input" figures in
  `blog-anthropic-cost-visibility-control.md` Claim 11 and `blog-anthropic-
  maximizing-session-value.md` Claim 3 is a generation-over-time price
  change this post itself explains (cache reads got a *deeper* cut than
  input on Opus 5.5, narrowing the ratio from 10% to 5%), not two sources
  disagreeing about the same state of the world at the same time. No
  contradiction issue filed — see MINER.md §4a's "conditioning variable,
  not a contradiction" carve-out.

- **Extends**:
  - `blog-anthropic-maximizing-session-value.md`: that post gives cache
    read/write pricing ratios (0.1x / up to 2x) and TTL by access method (1hr
    subscription / 5min API key) without connecting TTL choice to a
    *different* write price. This post's Claim 9 supplies that link (1.25x
    input for a 5-minute cache write, 2x for a 1-hour write) — meaning the
    `ENABLE_PROMPT_CACHING_1H=1` override from that note is a frequency/cost
    tradeoff, not a strict win.
  - `blog-anthropic-choosing-claude-model.md` and `blog-anthropic-cost-
    visibility-control.md`: both describe the advisor-strategy/model-tiering
    pattern qualitatively; this post adds the `opusplan` alias (Opus plans,
    Sonnet executes) as a named, shipping Claude Code feature implementing
    a *specific* worker/planner split, explicitly flagged by the post itself
    as unvalidated-by-default ("measure it on your own tasks before you make
    it a default") — Claim 13.
  - No prior corpus source documents `CLAUDE_CODE_SUBAGENT_MODEL` or its
    precedence order relative to a subagent's own `model:` field — Claim 14
    is new mechanism documentation, not an extension of a prior claim.

- **Novel**:
  - The `/claude-api prompt-audit` command and its measured 18%+9%=25% cost
    reduction on an internal 44-ticket benchmark, plus the four named
    "ritual instruction" anti-patterns it targets (mandatory step-count
    procedures, scratchpad rules, verify-twice rules, self-contradicting
    instructions) — Claim 12. First appearance of this tool and this
    measured figure anywhere in the corpus.
  - `CLAUDE_CODE_SUBAGENT_MODEL` and its override precedence — Claim 14.
  - Cache-write pricing split by TTL (1.25x for 5-minute, 2x for 1-hour) —
    Claim 9.
  - The $13/developer/active-day (average) and <$30/active-day (90th
    percentile) enterprise Claude Code cost baselines — Claim 15. First
    per-developer-per-day cost figures in the corpus.
  - MCP connect/disconnect and compaction as cache-bust triggers — Claim 8.
  - The effort-level dollar-cost-vs-retry-cost break-even heuristic and the
    "fix stops at one layer" diagnostic for when to raise effort — Claim 7.
  - The `/compact` break-even-at-~10-turns rule — Claim 11.
  - The "switch to Fable 5.1 after two failures on high effort, not three;
    switch back once solved" escalation/de-escalation rule — Claim 13.

## Guide Impact

- **Chapter 04 (Cost Optimization)**: Add the four-factor cost taxonomy
  (Claim 1: turns, cache reads, output tokens, model) as the chapter's
  organizing framework, ahead of individual levers. Add the Opus 5.5 list
  prices and their cuts versus Opus 5 (Claim 2) as the current reference
  pricing table, explicitly dated (list prices change) and cross-referenced
  against the Opus 5 = Opus 4.8 pricing chain already in the corpus.
- **Chapter 04 (Cost Optimization — effort and model selection)**: Add the
  effort-level ROI heuristic (Claim 7: ~$0.40 for a high-effort thinking
  bump ≈ a 10-turn retry loop, so raise effort only when it plausibly saves
  a retry) and the "fix stops at one layer" diagnostic as a concrete
  decision procedure, replacing any generic "raise effort if it's stuck"
  guidance. Add the three-model household (Claim 13: Opus 5.5 daily driver
  / Fable 5.1 for unsupervised-or-novel work / Sonnet-Haiku for lookups
  only) with the explicit "not for writing code" boundary on cheaper
  subagents, and the two-failure escalation threshold.
- **Chapter 04 (Cache management)**: Add the cache-write-by-TTL pricing
  split (Claim 9: 1.25x for 5-minute, 2x for 1-hour) as a caveat on the
  existing `ENABLE_PROMPT_CACHING_1H=1` recommendation from `blog-anthropic-
  maximizing-session-value.md` — state it as a frequency/cost tradeoff, not
  a pure win. Add the five cache-bust triggers (Claim 8) as an updated,
  more complete list than either prior source alone.
- **Chapter 02 or 04 (Harness Engineering / Subagent configuration)**: Add
  `CLAUDE_CODE_SUBAGENT_MODEL` and its precedence order (Claim 14) as the
  concrete mechanism for implementing fleet-wide subagent model tiering,
  with per-subagent `model:` overrides for exceptions.
- **Chapter 04 (Cost Optimization — measurement)**: Add the `/claude-api
  prompt-audit` command and its measured benchmark result (Claim 12) as a
  concrete, runnable first step for any model migration, alongside the
  named anti-pattern checklist (mandatory step counts, scratchpad rules,
  verify-twice rules, contradictory instructions) as things to look for
  even without running the tool. Add the $13/$30 per-developer-per-day
  baselines (Claim 15) as a sanity-check reference for `/usage` review.
- **Chapter 05 (Team Adoption)**: Add the `/compact` break-even-at-~10-turns
  rule (Claim 11) and the turn-count cost example (Claim 4: 40 vs. 25 turns,
  same final context, 59% cost difference) as concrete, teachable numbers
  for training practitioners on session hygiene, rather than qualitative
  "keep sessions tidy" advice.

## Extraction Notes

- WebFetch's default summarization pass returned only a loose paraphrase
  (and, notably, initially omitted the byline entirely from its summary).
  To get verbatim text for quoting and to confirm authorship, the page was
  fetched directly via `curl` with a browser user agent, and HTML was
  stripped to plain text with a local Python script; all quotes in this
  note are taken from that directly-fetched raw text, not from WebFetch's
  summarized output. The `<title>` tag and raw HTML both confirm the URL
  resolves to "What a task costs on Opus 5.5 | Claude by Anthropic" with
  byline "Addy Osmani," category "Claude Code," dated September 22, 2026.
- The article contains three interactive embedded widgets (a Fig A/Fig B
  price-comparison hero, a "try your own numbers" calculator, and an
  effort-level picker). Where the widgets' underlying JavaScript encodes
  numeric constants (prices, example token counts, effort-level metadata),
  those were extracted directly from the script source in the raw HTML and
  cross-checked against the surrounding prose — both agreed in every case
  checked. The calculator widget's live slider-to-dollar computation logic
  (beyond the fixed example values reproduced in Concrete Artifacts) was
  not fully extracted, since it requires runtime interaction rather than
  static values.
- One section, "The rest of the bill," which the post says "lists the
  other billing rules that affect a Claude Code session, with a link to
  the docs where one exists," is rendered as a static image
  (`cdn.prod.website-files.com/.../a5a12df0.png`) rather than as text or an
  HTML table, so its contents could not be extracted and are not
  represented in this note. Flagging for the Assayer: a future pass with
  image-reading capability could recover this table.
- The post links to several docs/blog pages as "Further reading" (Manage
  costs effectively, Model configuration, Choosing a Claude model and
  effort level in Claude Code, Effort, Prompt caching, Maximizing the
  value of your Claude Code sessions). The last of these is already mined
  in this corpus (`blog-anthropic-maximizing-session-value.md`, issue
  #2714) and is cross-referenced extensively above. The other four
  (`code.claude.com/docs/en/costs`, `code.claude.com/docs/en/model-config`,
  the "Choosing a Claude model and effort level in Claude Code" blog post,
  and the platform docs "Effort" and "Prompt caching" pages) were not
  followed as separate sub-pages — they are reference documentation this
  post already draws its own figures from, not additional argument to
  mine, and following all of them would extraction-creep past what issue
  #3628 asked the Miner to cover. Per MINER.md's "up to 5 linked pages"
  guidance, this was a judgment call given four of the five are pure
  reference docs restating figures already captured here; the "Choosing a
  Claude model and effort level in Claude Code" blog post (distinct from
  the already-mined `blog-anthropic-choosing-claude-model.md`, which is
  Anthropic's general model-class positioning post, not this Claude-Code-
  specific companion) is flagged as a candidate for a future separate
  source-submission issue.
- No contradiction meeting the MINER.md §4a bar was identified; see
  Cross-References "Contradicts" above for the one near-miss (cache-read
  ratio) evaluated and judged a time-conditioned price change, not a
  disagreement.
- The post is fully public on claude.com/blog with no paywall or access
  restriction.
