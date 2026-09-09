---
source_url: https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
source_type: blog-post
title: "Reducing cost and improving performance with Claude Platform"
author: Lance Martin (Anthropic)
date_published: 2026-09-08
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: emerging
issue: "#3321"
---

# Reducing Cost and Improving Performance with Claude Platform

> First-party Anthropic guide to three developer-facing cost levers on Claude
> Platform — prompt cache hit-rate maximization, removal of stale prompting
> anti-patterns when migrating to frontier models, and effort-level
> calibration — packaged as a `claude-api` Claude Code skill with three
> slash commands (`prompt-audit`, `cost-optimize`, `hillclimb`) and backed by
> vendor-run benchmark numbers (14.6%–73% cost reductions across several
> scenarios).

## Source Context

- **Type**: blog-post (claude.com/blog, "Agents" category, Claude Platform
  product line; published September 8, 2026; ~5 minute read)
- **Author credibility**: Lance Martin, individually bylined (unlike the
  house-authored `blog-anthropic-cost-visibility-control.md` and
  `blog-anthropic-admin-analytics-cost-controls.md` posts). First-party
  Anthropic source — authoritative for platform mechanics (how caching,
  effort, and the `claude-api` skill work) and for what the vendor's own
  benchmark runs measured. Not independently verified: all quantitative
  results (cost/accuracy deltas, benchmark scores) come from Anthropic's own
  test runs with no third-party replication, and methodology detail is
  compressed into single sentences per scenario (e.g., no per-run variance,
  no confidence intervals, no description of how "customer support benchmark"
  tickets were constructed).
- **Scope**: Covers prompt cache mechanics and cache-preserving practices,
  a named list of six prompting anti-patterns, the `effort` API parameter
  and its cost/quality tradeoff, and three `claude-api` skill commands
  (`prompt-audit`, `cost-optimize`, `hillclimb`) with worked examples on one
  internal customer-support benchmark and four public benchmarks (LegalBench,
  tau2-bench retail, OfficeQA Pro, SWE-bench Verified). Does NOT cover:
  Claude Enterprise admin controls, Workspaces, batch-API pricing mechanics,
  or spend-cap/access-gating features (all covered by the two related
  `blog-anthropic-*` cost posts already in the corpus — see Cross-References).

## Extracted Claims

### Claim 1: Anthropic frames cost and performance as commonly assumed to trade off against each other, but claims many Claude Platform applications can cut cost without giving up performance via three specific fixes bundled into a `claude-api` skill
- **Evidence**: Opening thesis statement of the article, stated as the framing for everything that follows.
- **Confidence**: settled (vendor's stated framing, not a measured claim in itself)
- **Quote**: "Performance and cost are often viewed as a trade-off: to spend less, you accept worse results. In practice, we've found that many applications using Claude Platform can cut costs without giving up performance with three fixes: maximize the prompt cache hit rate, remove anti-patterns from your prompts when upgrading to frontier Claude models, and calibrate effort to the task."
- **Our assessment**: This is marketing framing for the `claude-api` skill, but the three named levers (caching, prompt anti-patterns, effort) map to three genuinely distinct cost mechanisms already partially documented elsewhere in the corpus (see Cross-References). The value of this source is that it packages all three into one first-party reference with a shared toolset, not that the framing itself is novel.

### Claim 2: On Claude Opus 5 and Fable 5.1 specifically, effort or thinking settings can now be changed mid-conversation without breaking the prompt cache — a capability the article implies did not previously exist
- **Evidence**: Stated as a specific exception within the "practical tips" list for prompt cache management.
- **Confidence**: emerging (model-specific behavior stated without further mechanism detail; not independently verifiable)
- **Quote**: "Avoid changing effort or thinking settings mid-conversation. These settings render into the prompt ahead of your content, so they are part of the cached prefix. With Claude Opus 5 and Fable 5.1 specifically, you can update effort mid-conversation without breaking the cache."
- **Our assessment**: This directly updates the corpus's existing "don't change tools or models mid-conversation" guidance from `blog-anthropic-prompt-caching-everything.md` Claim 3/Lesson 3 ("Don't change tools or models mid-conversation"), which did not name an exception for effort changes on any model. This is not a contradiction — the earlier article predates Opus 5/Fable 5.1 and describes the general rule; this article adds a model-specific carve-out. Guide text repeating the blanket "never change effort mid-conversation" rule should be qualified for these two models.

### Claim 3: Synchronous tool calls or subagents that outlive the prompt cache's time-to-live force the next turn to rewrite the cache at 1.25x the normal input price (2x for a 1-hour cache) instead of the discounted cache-read price
- **Evidence**: Stated as one of the five cache-breaking risk factors, with the specific pricing multiplier given.
- **Confidence**: settled (pricing mechanics stated as a platform fact, consistent with the platform's documented cache-write vs. cache-read pricing model)
- **Quote**: "If an agent blocks on a long-running tool call or sub-agent, the cache can expire before the results come back. The next turn has to rewrite the cache, at 1.25× the normal input price (2× for a 1-hour cache) instead of the cheap read price."
- **Our assessment**: This is the first source in the corpus to state the exact cache-write pricing multiplier (1.25x/2x) as a downside risk of long-running tool calls specifically, as distinct from the general "compaction destroys the cache" cost documented in `research-wasnotwas-context-compaction.md`. It gives practitioners a concrete number to reason about when deciding whether to extend an agent's TTL to 1 hour (also recommended later in the same source, Claim 4) versus accepting more frequent cold-prefill rewrites.

### Claim 4: Recommended prompt-cache management practices include monitoring hit rate via Claude Console diagnostics, deferring rarely-used tools with `defer_loading`, applying system prompt updates as messages, laying out requests stable-content-first, switching model/effort only when the cache will already be broken (e.g., during compaction), moving the cache breakpoint automatically as the conversation grows, pre-warming the cache with a `max_tokens: 0` request, and extending the cache TTL to 1 hour for tool calls that may exceed the default 5-minute TTL
- **Evidence**: Presented as a bulleted "lessons" list under "How to fix it" in the prompt-cache section.
- **Confidence**: settled (first-party description of platform features and recommended practice)
- **Quote**: "To reduce latency, send a request with max_tokens: 0 and an explicit cache breakpoint. This processes the prompt and writes it to the cache without generating anything. If you run it at session start (for example, while a user is typing), the first real request hits a warm cache."
- **Our assessment**: Several of these practices corroborate `blog-anthropic-prompt-caching-everything.md` almost exactly (static-first layout, `defer_loading` stubs, messages instead of system-prompt edits, monitoring hit rate). The genuinely new items here are: pre-warming via `max_tokens: 0`, automatic cache-breakpoint movement as a platform feature, and the explicit recommendation to time model/effort switches to coincide with an already-broken cache (e.g., at compaction) rather than treating switches as a separate cost event.

### Claim 5: Prompting "anti-patterns" that hobble frontier Claude models and inflate cost include verification rituals, thoroughness/emphasis boosters, mandatory step-by-step procedures and scratchpad scaffolds, stale few-shot examples, contradictory rules, and dated configuration (e.g., manual thinking budgets)
- **Evidence**: Named as a definitional list of six anti-pattern categories, each with a one-sentence explanation and (for several) an illustrative bracketed example phrase.
- **Confidence**: settled (first-party taxonomy presented as the direct basis for the `prompt-audit` command's detection logic)
- **Quote**: "Verification rituals. Instructions like \"double-check your work” or \"verify twice before responding” are often taken literally by frontier models and can waste tokens." "Thoroughness and emphasis boosters. \"Be maximally thorough,\" \"CRITICAL: YOU MUST ALWAYS…\" can lead to verbosity and extra tool calls when working with frontier models."
- **Our assessment**: This is the first source in the corpus to name and define this specific six-item taxonomy of prompt anti-patterns as a category distinct from harness-design pitfalls (e.g., cache-breaking mistakes). The mechanism claimed — that frontier models follow these instructions more literally than older models did, so the instructions actively backfire rather than being merely ignored — is a specific and testable claim, not just "trim your prompts." Worth flagging to practitioners auditing CLAUDE.md files or skills written for older model generations.

### Claim 6: In a controlled test migrating a customer-support benchmark from Opus 4.8 to Opus 5, planting one anti-pattern at a time (six legacy prompts total) and then running `/claude-api prompt-audit` to remove them decreased cost by 14.6% and increased accuracy by 5.3% on average, compared to the same prompts run on Opus 5 with only the model ID changed
- **Evidence**: Described as a specific internal benchmark with a stated methodology (clean prompt, six anti-patterns planted one at a time, three model/prompt-audit conditions compared, averaged across the six).
- **Confidence**: emerging (vendor-run, single internal benchmark, no independently reported sample size for "customer support benchmark," no confidence interval, no replication)
- **Quote**: "Running /claude-api prompt-audit removed the anti-patterns, decreasing costs by 14.6% and increasing accuracy by 5.3% on average. Cost dropped because extra tool calls and duplicated reasoning were eliminated."
- **Our assessment**: The article also gives specific causal mechanisms for the accuracy gain — a retired thinking setting causing outright API rejection of routing requests, contradictory refund rules causing Opus 5 to withhold four owed refunds pending confirmation, and a manual scratchpad causing Opus 5 to write tool calls inside its reasoning without executing them on three tickets. These specific failure mechanisms are more useful to practitioners than the headline percentages, because they describe concrete symptoms (a tool call written but never executed) that a team could recognize in their own logs without needing to reproduce Anthropic's benchmark.

### Claim 7: The `effort` parameter controls how much a model deliberates before answering; miscalibrating it in either direction has a cost — high effort causes over-thinking on tasks with no more evidence to find, while low effort can cause Claude to stop before gathering enough evidence, producing an answer that "looks finished" but rests on partial information
- **Evidence**: Direct definitional statement plus two named failure modes (over-thinking and under-evidencing).
- **Confidence**: settled (definitional description of a shipped API parameter and its documented behavior)
- **Quote**: "Effort tells Claude “how hard to work.” At low effort Claude generally reaches conclusions faster. At high effort, Claude deliberates, verifies, and explores alternatives before answering."
- **Quote**: "Biasing to low effort. Set too low, Claude stops before it has enough evidence. It makes fewer tool calls, so it may answer from the first search result instead of the third. It thinks less on hard steps and skips the check it would normally run on its own. The answer looks finished, but it's built on partial information."
- **Our assessment**: The "looks finished but built on partial information" framing is a useful practitioner-facing warning distinct from a simple cost/quality tradeoff — it describes a failure mode that is not visible from the output alone, which has direct implications for any guide section on verification and effort selection.

### Claim 8: On FrontierCode Diamond (the hardest 50 tasks), Claude Fable 5 scores 11.5% at low effort for $5.35/task versus 30.9% at max effort for $19.00/task — roughly 2.7x the score for about 3.5x the cost; on Humanity's Last Exam (without tools), Claude Fable 5.1 scores ~53% at low effort for ~$0.30/question versus ~61% at max effort for ~$2.23/question, with the last step to max effort adding about half a point of score for 46% more cost, a gain the article says falls within the benchmark's run-to-run noise
- **Evidence**: Two specific effort-vs-cost curves on two named benchmarks, presented with a figure (Figure 4) for the first.
- **Confidence**: emerging (vendor-reported benchmark scores and per-task/per-question dollar costs; no stated sample size, variance, or independent replication; the article itself flags the HLE max-effort gain as within run-to-run noise, which is a notable self-critical admission)
- **Quote**: "For example, Claude Fable 5 scores 11.5% at low effort for $5.35 per task on FrontierCode Diamond (the hardest 50 tasks). At max effort, Fable 5 gets 30.9% for $19.00 per task; changing effort raises the score about 2.7x (+19 points) for about 3.5x the cost (Figure 4)."
- **Our assessment**: The HLE example is the more instructive of the two, precisely because Anthropic itself frames the max-effort HLE gain as noise-level and not worth the added cost — this is a rare vendor admission that "turn effort up" is not always the right call, reinforcing Claim 7's "biasing to high effort" failure mode with a concrete benchmark example rather than only a general warning.

### Claim 9: On CursorBench 3.2, Claude Fable 5.1 at low effort matches the performance of Fable 5 at high effort at roughly a third of the cost, driven by both doing less work per task at low effort and Fable 5.1's prompt-cache reads being priced at $0.25 per million tokens versus $1.00 per million tokens for Fable 5 (even holding Fable 5's own prices constant, Fable 5.1 at low effort would cost about 40% less)
- **Evidence**: Specific benchmark comparison (Figure 5) with an explicit two-factor cost decomposition (less work per task, plus a per-model cache-read price difference).
- **Confidence**: emerging (vendor-run single-benchmark comparison; the per-token cache pricing figures are settled as stated platform pricing, but the "matches the performance... at a third of the cost" headline claim is a single benchmark result, not a general guarantee)
- **Quote**: "Test stronger models at lower effort. A stronger model at low effort can be cheaper than a weaker model working hard (high effort). For example, on CursorBench 3.2, Claude Fable 5.1 at low effort matches the performance of Fable 5 at high effort at a third of the cost (Figure 5)."
- **Our assessment**: This is the article's central actionable heuristic: "test stronger models at lower effort" as a cost lever, not just "use a cheaper model." It is a genuinely different recommendation from the model-downgrade advice in `docs-github-copilot-cca-cost-efficient-models.md` (switch to a smaller model for simple tasks) — here the recommendation is to keep or upgrade the model but reduce effort, which the article claims can beat downgrading the model outright when the newer model's per-token cache-read price is also lower.

### Claim 10: Run via `/claude-api hillclimb` on a customer-support benchmark starting from Opus 4.8 at default (high) effort, the search first found Opus 5 at low effort plus prompt-audit cleanup (98.9% train accuracy, 2.6 cents/ticket, matching the Opus 4.8 baseline accuracy), then stepped down to Sonnet 5 at low effort (1 cent/ticket but accuracy fell to 88.9%), then added routing rules and a refund-cap cross-reference derived from reading failing train tickets to bring Sonnet 5 back to 98.9% accuracy at the same 1-cent cost; on the 14 held-out test tickets, the final configuration scored 90.5% versus the original setup's 78.6%, at about one-fifth the cost
- **Evidence**: A worked, step-by-step example of the `hillclimb` command's search process on one internal benchmark, with a held-out test evaluation at the end (Figure 6).
- **Confidence**: emerging (single internal benchmark run, vendor-reported, 14 held-out tickets is a very small test set for a percentage-accuracy claim, no confidence interval given)
- **Quote**: "It then stepped down to Sonnet 5 at low effort, which was cheaper still at 1 cent per ticket, but accuracy fell to 88.9%. Reading the failing train tickets, Claude added routing rules and a refund-cap cross-reference to the prompt, bringing Sonnet 5 back to 98.9% at the same cost."
- **Quote**: "On the 14 held-out tickets the search never saw, the final configuration scored 90.5% against the original setup's 78.6%, at about one fifth the cost."
- **Our assessment**: The 14-ticket held-out set is small enough that a single-digit number of tickets flipping right or wrong would materially change the reported percentage — worth flagging explicitly if this example is cited in the guide as evidence of `hillclimb`'s effectiveness rather than as an illustrative walkthrough of the mechanism. The mechanism itself (train/test split, read failing train cases, propose a fix, re-score on held-out test) is the more durable and citable claim than the specific percentages.

### Claim 11: Running `/claude-api cost-optimize` against four public benchmarks (starting from Sonnet 5 as baseline) produced cost reductions while keeping pass rate flat or within noise: LegalBench ~58% lower cost (thinking tokens fell from 102,779 to 8,284 via shared-prefix caching, low effort, and Batch API routing), tau2-bench retail ~73% lower cost (via prompt caching with explicit breakpoint placement), OfficeQA Pro ~52% lower cost ($136.20 to $64.87, via batch processing and document caching), and SWE-bench Verified ~55% lower cost (default config already cached correctly; savings came from setting effort to medium and constraining output length, with median steps per task falling from 29 to 17 and prompt tokens from 75.2M to 33.7M)
- **Evidence**: A table of four public-benchmark results (Figure 7), each with a named optimization mechanism and before/after numbers for at least one supporting metric (thinking tokens, dollar cost, or step count).
- **Confidence**: emerging (vendor-run against public benchmarks — the benchmarks themselves are named and checkable, which is stronger evidentiary grounding than the two internal customer-support examples, but the specific optimization choices and results are still self-reported with no independent replication)
- **Quote**: "LegalBench (~58% lower cost): cost-optimize proposed caching a shared prefix across tasks, setting low effort, and processing tasks via the Batch API. Thinking tokens fell from 102,779 to 8,284, but pass rate stayed within noise and cost dropped by ~58%."
- **Quote**: "SWE-bench Verified (~55% lower cost): cost-optimize found that the default config already caches correctly. Savings came from setting effort to medium and constraining the agent's output to just a few concise sentences. Median steps per task went from 29 to 17 and prompt tokens fell from 75.2M to 33.7M."
- **Our assessment**: Because these run against named public benchmarks (LegalBench, tau2-bench retail, OfficeQA Pro, SWE-bench Verified) rather than an undisclosed internal dataset, this is the most independently checkable evidence in the article — a third party could in principle rerun `cost-optimize` against the same benchmarks and compare. The SWE-bench Verified result is notable for being the one case where caching was already optimal and the entire gain came from effort and output-length tuning, showing the three levers (caching, anti-patterns, effort) are not always all applicable to the same workload.

### Claim 12: The `claude-api` skill ships three Claude Code slash commands — `/claude-api prompt-audit` (scans prompts, skills, and tool descriptions in the working directory, including application code and Claude Code's own configuration, for the six named anti-patterns), `/claude-api cost-optimize` (profiles where an application's token spend goes — from Admin API cost reports, per-response usage objects, or estimated from request-building code — then ranks and applies savings starting with caching, then trimming, output bounding, and batching, and if given an evaluation measures the performance tradeoff), and `/claude-api hillclimb` (given an evaluation, splits it into train/test sets, iteratively proposes model/effort/prompt changes by reading failing train examples, and scores the final configuration on the held-out test set)
- **Evidence**: Each command is defined in its own subsection with a description of its inputs, method, and output.
- **Confidence**: settled (first-party description of shipped tooling, not a performance claim)
- **Quote**: "cost-optimize starts by finding where your tokens go: from your organization's usage and cost reports if you have a Claude Admin API key, from the usage object on each API response if your application logs it, or, failing both, by reading your request-building code and estimating."
- **Quote**: "Given an evaluation, Claude splits it into train and test sets, then proposes updates to your application that aim to reduce cost while maintaining baseline performance. Claude reads the failing train cases to guide the search, and the final configuration is scored on the held-out test set."
- **Our assessment**: This is the concrete, reusable artifact from the article — three named, invokable commands with defined scopes, as opposed to general advice. `cost-optimize`'s three-tier fallback for locating spend data (Admin API → per-response usage object → static estimation from code) is a specific implementation detail worth documenting for practitioners who lack Admin API access.

## Concrete Artifacts

### Prompt cache mechanics (verbatim definitions)
```
Source: claude.com/blog, "Reducing cost and improving performance with Claude
Platform," Lance Martin, 2026-09-08, "Prompt cache" section

"Before Claude generates a response, it first processes your prompt into an
internal working state. This step, called prefill, is the expensive part of
handling input. Prompt caching saves that state (the key–value, or KV,
cache): when a request starts with the same prefix, Claude reads it back
instead of recomputing it. Cache reads are billed at a fraction of the full
input price."

Three cache constraints named:
1. Cache is pinned to a specific model.
2. Cache reads must be byte-exact across the full span of the prompt.
3. Cache has a limited time-to-live (TTL) — default 5 minutes, extendable to
   1 hour.
```

### Cache-breaking risk list (paraphrased from source, five items)
```
Source: same article, "Prompt cache" section, "practical considerations"

1. Changing effort/thinking settings mid-conversation
   — exception: not on Claude Opus 5 or Fable 5.1 (Claim 2)
2. Volatile values (timestamps, IDs) in the cached prefix
3. Tool definitions that reorder themselves (Messages API renders tools at
   a fixed position; any change to a tool definition breaks the cache)
4. Forking conversations (subagents/branches only share cache when the
   fork's prefix is byte-identical, same model, same effort)
5. Synchronous tool calls / subagents that outlive the cache TTL
   — next turn rewrites cache at 1.25x input price (2x for 1-hour cache)
```

### Six named prompting anti-patterns
```
Source: same article, "Instructions" section

1. Verification rituals — e.g. "double-check your work", "verify twice"
2. Thoroughness and emphasis boosters — e.g. "be maximally thorough",
   "CRITICAL: YOU MUST ALWAYS..."
3. Mandatory procedures and scratchpad scaffolds — e.g. fixed step-by-step
   or "think step by step in a scratchpad" templates
4. Stale examples — few-shot examples tuned to an older model's failure modes
5. Contradictory rules — e.g. "always refund within policy" vs. "never
   issue refunds without escalation"
6. Dated configuration — e.g. manual thinking budgets from an older model
   generation, which can be rejected by the platform on frontier models
```

### cost-optimize four-benchmark results table (compiled from source)
```
Source: same article, "Automating cost reduction" section, Figure 7

| Benchmark            | Cost change | Mechanism                                    | Supporting metric                          |
|-----------------------|-------------|-----------------------------------------------|---------------------------------------------|
| LegalBench             | ~58% lower  | shared-prefix caching, low effort, Batch API  | thinking tokens 102,779 -> 8,284             |
| tau2-bench retail      | ~73% lower  | prompt caching, explicit breakpoint placement | pass rate flat                               |
| OfficeQA Pro           | ~52% lower  | batch processing, document caching            | cost $136.20 -> $64.87                       |
| SWE-bench Verified     | ~55% lower  | medium effort, bounded output (caching already optimal) | median steps/task 29 -> 17; prompt tokens 75.2M -> 33.7M |

All four baselined against Claude Sonnet 5.
```

### Three claude-api slash commands (compiled from source)
```
Source: same article, "Getting started" section

/claude-api prompt-audit
  Scans prompts, skills, and tool descriptions in the working directory
  (application code calling the Claude API, or Claude Code config such as
  CLAUDE.md/skills) for the six anti-patterns above.

/claude-api cost-optimize
  Profiles token spend (Admin API cost reports -> per-response usage object
  -> estimated from request-building code, in that fallback order), applies
  prompt-audit plus caching/trimming/output-bounding/batching, and if given
  an evaluation measures the cost/performance tradeoff across effort levels
  and models.

/claude-api hillclimb
  Given an evaluation, splits it into train/test sets, iteratively proposes
  model/effort/prompt changes by reading failing train examples, and scores
  the final configuration on the held-out test set.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-prompt-caching-everything.md` Claim 3 / "Lessons Learned"
    #2–3 ("static content first, dynamic content last"; "don't change tools
    or models mid-conversation"): this article restates the same static-first
    layout rule and the same general model/effort-switching caution, and
    corroborates the `defer_loading` stub mechanism (that note's Claim 9) for
    rarely-used tools almost verbatim.
  - `blog-anthropic-cost-visibility-control.md` Claim 11 ("prompt caching...
    costs 10% of the normal input rate on cache hits") and Claim 13 (the
    `effort` parameter "dialed down for routing/extraction, up for a final
    recommendation" and the advisor-strategy pattern): both articles describe
    the same two API-level cost levers (caching, effort). This new article
    goes substantially further on both — it gives the cache-write penalty
    multiplier (1.25x/2x, Claim 3 here) that the cost-visibility note does
    not state, and it provides quantified effort-calibration benchmark data
    (Claims 8–9 here) where the cost-visibility note only gives the
    qualitative "dial down for routing, up for recommendations" heuristic.

- **Contradicts**: None found. Claim 2's mid-conversation effort-change
  exception for Opus 5/Fable 5.1 updates rather than contradicts
  `blog-anthropic-prompt-caching-everything.md`'s general rule — the earlier
  article (published 2026-04-30, before Opus 5/Fable 5.1 existed) states a
  general constraint that this article narrows for two specific newer
  models. This is a time-conditioned product/model change, not a
  disagreement between sources, so no contradiction issue was filed per
  MINER.md §4a.

- **Extends**:
  - `blog-anthropic-prompt-caching-everything.md`: adds the `max_tokens: 0`
    cache pre-warming technique, the cache-write pricing multiplier
    (1.25x/2x), automatic cache-breakpoint movement, and the model-specific
    mid-conversation effort exception — none of which appear in the earlier
    article.
  - `blog-anthropic-cost-visibility-control.md`: extends its brief effort
    and caching mentions with a full worked toolset (`prompt-audit`,
    `cost-optimize`, `hillclimb`) and quantified before/after benchmark
    results.
  - `docs-github-copilot-cca-cost-efficient-models.md`: that source's
    guidance is "switch to a smaller model for simple tasks." This article's
    Claim 9 ("test stronger models at lower effort") is a related but
    distinct lever — reduce effort on the same or a newer model rather than
    downgrading the model class — and the two strategies could be evaluated
    against each other for the same workload.

- **Novel**:
  - The six-item named taxonomy of prompting anti-patterns (Claim 5) and the
    controlled Opus 4.8 -> Opus 5 migration test isolating each anti-pattern's
    individual cost/accuracy effect (Claim 6) — no other corpus source
    documents specific prompting patterns that *backfire* on frontier models
    as opposed to being merely wasteful.
  - The three `claude-api` slash commands (Claim 12) as a named, reusable
    toolset — first corpus source describing an automated cost-audit and
    iterative hillclimbing tool built specifically for Claude API cost
    optimization.
  - The "test stronger models at lower effort" heuristic (Claim 9) as an
    alternative to model downgrading, with a specific cache-pricing
    explanation for why a newer model at low effort can beat an older model
    at high effort even before accounting for capability differences.
  - The four-benchmark `cost-optimize` results against named, checkable
    public benchmarks (Claim 11) — the first corpus source to report
    cost-optimization results against benchmarks a third party could
    independently rerun, rather than only an undisclosed internal dataset.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the six-item prompt anti-pattern
  taxonomy (Claim 5) as a checklist for auditing CLAUDE.md files and skills
  written against older model generations — frame it as "instructions that
  backfire on frontier models," not just "instructions to trim." Add the
  cache-write pricing multiplier (1.25x/2x, Claim 3) to any existing
  cache-management guidance as the concrete cost of letting a synchronous
  tool call or subagent outlive the TTL. Update the existing "never change
  model or effort mid-conversation" guidance (sourced from
  `blog-anthropic-prompt-caching-everything.md`) to note the Opus 5/Fable 5.1
  exception (Claim 2).

- **Chapter 04 (Context/Cost Engineering)**: Add effort-level calibration as
  a named lever alongside prompt caching, with the two concrete failure
  modes from Claim 7 (over-thinking on a saturated task; stopping before
  enough evidence is gathered) as the framework for reasoning about when to
  raise or lower effort — not simply "high effort is better" or "low effort
  is cheaper." Cite the FrontierCode Diamond and HLE effort curves (Claim 8)
  as concrete illustrations, but flag the HLE max-effort gain as
  vendor-reported to be within run-to-run noise, i.e., a case where more
  effort measurably was not worth the added cost.

- **Chapter 05 (Team Adoption / TCO)**: If the guide references
  `cost-optimize`-style automated cost audits, cite the four-benchmark
  results (Claim 11) as the most independently checkable evidence in this
  source (named public benchmarks) versus the two internal customer-support
  examples (Claims 6, 10), which should be presented with the small-sample
  caveat (14 held-out tickets for the `hillclimb` example).

## Extraction Notes

1. **WebFetch summarization risk avoided by direct fetch**: An initial
   WebFetch pass against the article URL returned an AI-generated summary
   with paraphrased "quotes" that could not be verified as verbatim
   (including a fabricated-sounding "Reading time" framing and imprecise
   figures). A second WebFetch pass explicitly asking for exact quotes
   still carried reconstruction risk. All quotes in this note were instead
   sourced from a direct `curl` fetch of the raw article HTML, with tags
   stripped and entities unescaped programmatically, then read in full
   before selecting quotes — the same higher-verification approach used in
   `docs-github-copilot-code-review-effort-levels-ga.md`'s Extraction Notes.
2. **Full article read, no sub-pages followed**: The article links to
   Anthropic's developer documentation and cookbook ("See our documentation,
   here" / "See our cookbook, here") but both link to generic doc/cookbook
   landing pages rather than a specific sub-page tied to this article's
   content, so neither was followed as a substantive linked page per
   MINER.md §1.
3. **All benchmark numbers are vendor-reported and unaudited**: FrontierCode
   Diamond, CursorBench 3.2, and the two customer-support benchmarks are
   Anthropic-run with no disclosed sample sizes (beyond the 14-ticket
   `hillclimb` held-out set), no confidence intervals, and no third-party
   replication. LegalBench, tau2-bench retail, OfficeQA Pro, and SWE-bench
   Verified are named public benchmarks, which makes those four results the
   more independently checkable subset — this distinction is called out
   explicitly in Claim 11's assessment and should be preserved if this
   source is cited in the guide.
4. **`confidence_overall` set to emerging**: The mechanical/definitional
   claims (prompt cache architecture, effort parameter definition, the
   anti-pattern taxonomy, the three slash commands' scope) are settled
   first-party product descriptions. However, the source's central
   persuasive content — every specific cost/accuracy percentage — is a
   single vendor's self-reported, unreplicated benchmark result. The overall
   rating reflects that the article's most citable numbers are all in the
   emerging category.
