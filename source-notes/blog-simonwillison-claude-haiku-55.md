---
source_url: https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/
source_type: blog-post
title: "Claude Haiku 5.5"
author: Simon Willison
date_published: 2026-10-07
date_extracted: 2026-10-14
last_checked: 2026-10-14
status: current
confidence_overall: emerging
issue: "#4094"
---

# Claude Haiku 5.5

> Willison's measured read on Haiku 5.5: list price now matches GPT-6 Luna up to 100k tokens, but a 5x price step above 100k and a new tokenizer (~1.25x tokens on one prompt) erode the headline, and reasoning cannot be disabled.

## Source Context

- **Type**: blog-post (launch commentary with his own measurements; ~600 words)
- **Author credibility**: Simon Willison runs same-day model tests (pelican SVG sweeps across reasoning levels) with his own tooling (`llm`, `llm-anthropic`, Claude Token Counter). Evidence is informal and single-prompt, not benchmarks.
- **Scope**: Haiku 5.5 pricing, tokenizer change, reasoning-effort cost/latency on one SVG prompt, and Anthropic's same-day subscriber API-credit scheme. Does NOT cover: capability benchmarks (he only says Haiku "reports higher benchmark scores"), agentic/coding tests, context window, or latency for real workloads. Release facts belong to Anthropic's announcement (open issue #4055); not mined here.

## Extracted Claims

### Claim 1: Haiku 5.5 list price matches GPT-6 Luna up to 100,000 tokens, a 10x cut from Haiku 4.5
- **Evidence**: Price figures read from Anthropic's announcement and compared with Haiku 4.5's $1/$5.
- **Confidence**: settled (published list prices)
- **Quote**: "The new Haiku exactly matches the price of GPT-6 Luna—$0.10/$0.50—up to 100,000 tokens."
- **Our assessment**: Resolves the pending state in `blog-simonwillison-claude-sonnet-55.md` Claim 8 and the 10x gap in `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 12. Prices are as of 2026-10-07.

### Claim 2: Pricing rises 5x beyond 100,000 tokens, so Luna is the better deal for long-context workloads
- **Evidence**: List prices ($0.50/$2.50 above 100k) vs Luna's step at 272,000 tokens to only $0.20/$0.75; Willison's conclusion.
- **Confidence**: settled for the prices; emerging for the conclusion
- **Quote**: "Above 100,000 tokens, Luna looks like a much better deal."
- **Our assessment**: A concrete context-budget cliff: agent sessions that grow past 100k input tokens re-price the whole request tier. Willison does not say whether the higher rate applies to the whole request or only the excess; check Anthropic's pricing page before relying on it.

### Claim 3: A new tokenizer yields ~1.25x tokens on the same prompt, a hidden price increase
- **Evidence**: One long prompt counted with his Claude Token Counter tool against Haiku 4.5 and 5.5. Prompt not disclosed.
- **Confidence**: anecdotal (single prompt)
- **Quote**: "the same long prompt uses around 1.25x as many tokens with Haiku 5.5 compared to Haiku 4.5, so there’s a hidden price increase there."
- **Our assessment**: Directionally important: per-token price comparisons across model generations are misleading when tokenizers differ. The ratio will vary by content type (code vs prose); do not generalize 1.25x. Even so, 1.25x on a 10x price cut is still a large net saving versus Haiku 4.5.

### Claim 4: Within 100k tokens Haiku 5.5 is the same price as Luna and reports higher benchmark scores
- **Evidence**: Assertion; benchmarks are Anthropic's, not reproduced.
- **Confidence**: anecdotal
- **Quote**: "If your workloads fit in 100,000 tokens, Haiku is the same price as Luna and reports higher benchmark scores."
- **Our assessment**: Vendor-reported benchmarks; treat as unverified. Combined with Claim 3, the effective price of Haiku is above Luna's on token-inflated content only if Luna's tokenizer is leaner, which he did not measure.

### Claim 5: Haiku 5.5 cannot disable reasoning and defaults to medium effort
- **Evidence**: Observed via the API while sweeping `thinking_effort`.
- **Confidence**: emerging
- **Quote**: "The new Haiku doesn’t let you disable reasoning, and defaults to medium."
- **Our assessment**: Matters for latency/cost-sensitive uses of a "fast" model: the cheap tier now always pays a reasoning cost, so callers must explicitly set `low`. Haiku 4.5 had no reasoning levels.

### Claim 6: Reasoning effort spans a ~44x cost and ~44x latency range on one prompt (low: 0.0936¢/7s; max: 3.3826¢/5m09s)
- **Evidence**: Two runs of the pelican-SVG prompt via `llm -m claude-haiku-5.5 ... -o thinking_effort low`; costs and times quoted. Willison reports a good bicycle frame at everything above low.
- **Confidence**: anecdotal (n=1 per level)
- **Quote**: "The low effort pelican cost 0.0936 cents and took 7 seconds."
- **Our assessment**: Ratios are our arithmetic (3.3826/0.0936 ≈ 36x cost; 309s/7s ≈ 44x latency). Even max is cheap in absolute terms, but 5 minutes is unusable interactively. Compare Opus 5.5 / Sonnet 5.5 "max" failures (`blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 9; `blog-simonwillison-claude-sonnet-55.md` Claim 3): here max completes and produces output.

### Claim 7: The max-effort reasoning trace shows awareness of the benchmark
- **Evidence**: The trace begins with a reference to the classic test; Willison added an armadillo-in-fishnet-tights prompt as a hedge.
- **Confidence**: anecdotal
- **Quote**: "(with a reasoning trace that starts “This is the classic pelican-on-bicycle SVG test...”)"
- **Our assessment**: Evidence of benchmark contamination or at least recognition, weakening pelican results as a capability signal; reinforces that his post supports price/token claims, not capability claims.

### Claim 8: Haiku 4.5's pelican cost 0.7583 cents and was poor; no reasoning levels
- **Evidence**: A year-old run compared side by side.
- **Confidence**: anecdotal
- **Quote**: "(for 0.7583 cents—Haiku 4.5 did not support reasoning levels)"
- **Our assessment**: Useful baseline: Haiku 5.5 at low (0.0936¢) is ~8x cheaper on this prompt than Haiku 4.5, which squares with the 10x list-price cut after tokenizer inflation.

### Claim 9: Anthropic halved Sonnet 5.5 cache-read prices and added monthly API credits for Max and Team subscribers
- **Evidence**: Quoted Anthropic announcement; Willison says credits "exactly match the cost of the subscription itself".
- **Confidence**: settled (vendor announcement)
- **Quote**: "Max 5x users will get $100 in credits per month, Max 20x users will get $200, and Team subscribers will receive up to $500, pooled across their users."
- **Our assessment**: Commercial offer, not an engineering pattern. Relevant to Ch05 budget planning only insofar as credits are use-it-or-lose-it ("the monthly credits do not roll over") and auto-reload can be disabled so requests stop at zero balance. Extends the cache-read emphasis in `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 7.

### Claim 10: OpenAI's Codex subscription for personal API use is still a better deal for heavy API users, though Anthropic's credits narrow the gap
- **Evidence**: Willison's comparison; no figures.
- **Confidence**: anecdotal
- **Quote**: "OpenAI still allow you to use your Codex subscription for personal API use, which works out as a better deal for heavy API users."
- **Our assessment**: Opinion without numbers; plans change quickly. Low priority.

### Claim 11: `llm-anthropic` no longer needs a new release per new model
- **Evidence**: Author's workflow: `llm install -U llm-anthropic` then `llm anthropic refresh`.
- **Confidence**: anecdotal
- **Quote**: "The most recent release of llm-anthropic finally fixed it so I don’t need to ship a new version of that plugin for every new model."
- **Our assessment**: Minor tooling note: dynamic model-list refresh reduces lag for same-day testing.

## Concrete Artifacts

```
# Source: Simon Willison, "Claude Haiku 5.5", 2026-10-07
llm install -U llm-anthropic
llm anthropic refresh
llm -m claude-haiku-5.5 "Generate an SVG of a pelican riding a bicycle" -o thinking_effort low
```

| Item (all from the source) | Haiku 4.5 | Haiku 5.5 up to 100k | Haiku 5.5 above 100k | GPT-6 Luna |
|---|---|---|---|---|
| Input / output per 1M | $1 / $5 | $0.10 / $0.50 | $0.50 / $2.50 | $0.10 / $0.50 (to 272k), then $0.20 / $0.75 |

Pelican runs: Haiku 4.5, 0.7583¢ (no reasoning levels); Haiku 5.5 low, 0.0936¢, 7 s; Haiku 5.5 max, 3.3826¢, 5 min 9 s. Efforts tested: low, medium, high, xhigh, max.

## Cross-References

- **Corroborates**: `blog-simonwillison-gpt56-luna-price-drop.md` Claim 4 (Luna vs Haiku 4.5 price gap, which this release closes); `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 7 (cache reads dominate agentic cost) via the Sonnet 5.5 cache-read halving.
- **Contradicts**: none filed. Note, in context only: Claim 12 of the price-war note (10x gap) and Claim 8 of `blog-simonwillison-claude-sonnet-55.md` are superseded by new facts, not contradicted.
- **Extends**: `blog-simonwillison-claude-sonnet-55.md` Claim 8 (Haiku 5.5 pending → shipped at Luna's price); `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 12 and Claim 9 (max-effort behavior now seen on a small model that completes).
- **Novel**: Tokenizer-driven hidden price increase measured across model generations; the 100k-token 5x price cliff; a small model that cannot disable reasoning; per-effort cost/latency for a cheap model. Related open issue #4055 (Anthropic announcement) should be mined/cross-linked for release facts.

## Guide Impact

- **Chapter 04**: Add a rule of thumb that token budgets and cost comparisons must be re-measured per model generation because tokenizers change (Claude Haiku 5.5: ~1.25x on one prompt), and that Haiku 5.5 has a 100k-token tier boundary relevant to context budgeting. Mark as single data point.
- **Chapter 05**: When comparing small-model costs for teams, use the effective cost (list price × token inflation) and tier thresholds, not the headline per-token price; note subscriber API credits do not roll over.
- **Chapter 02**: Note that effort/reasoning controls matter even on the cheapest tier: Haiku 5.5 defaults to medium and cannot be turned off, so latency-sensitive callers must set `low` explicitly.

## Extraction Notes

- The WebFetch tool returned only a summary; quotes were taken from the raw HTML fetched with curl and verified against that text. Quotes use the source's curly apostrophes.
- Single-prompt, single-author source; supports pricing/token-count claims, not capability claims. Images (pelicans) not inspected. No sub-pages followed; the Anthropic announcement is tracked separately in #4055.
- The subscriber-credit scheme was extracted briefly (Claims 9-10) at low priority per triage guidance.
