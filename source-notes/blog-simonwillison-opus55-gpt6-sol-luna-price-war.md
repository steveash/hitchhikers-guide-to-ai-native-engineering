---
source_url: https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
source_type: blog-post
title: "Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war"
author: Simon Willison
date_published: 2026-09-22
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: emerging
issue: "#3799"
---

# Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war

> Willison's same-day impressions of three simultaneous launches: a nine-model price table showing GPT-6 Sol/Luna at half their GPT-5.6 prices, Opus 5.5 with a 20% price cut and 60% cheaper cache reads, and a first-hand failure where Opus 5.5 at "max" thinking exhausts the 128k output-token limit without answering.

## Source Context

- **Type**: blog-post (launch-day impressions, ~1,000 words, one pricing table)
- **Author credibility**: Simon Willison is a long-running LLM tooling practitioner who runs his own repeatable comparisons (pelican-on-a-bicycle SVG across reasoning levels) and reports actual spend. Pricing figures are vendor list prices copied into a table; the source does not link them individually.
- **Scope**: Pricing landscape, Opus 5.5 pricing/positioning, one reasoning-level failure, and Willison's default-model changes. Not covered: benchmarks, capability evals beyond pelican SVGs, Sonnet 5.5 / Haiku 5.5 (only "coming soon"). Written the day of release ("It's going to take a while to get a good read on all of these new models").

## Extracted Claims

### Claim 1: GPT-6 Luna and Sol are each roughly half the price of their GPT-5.6 equivalents
- **Evidence**: Pricing table in the post (per M tokens, input/cached/output): GPT-6 Luna $0.10/$0.01/$0.50 vs GPT-5.6 Luna $0.20/$0.02/$1.20; GPT-6 Sol $2/$0.20/$10 vs GPT-5.6 Sol $4/$0.40/$20.
- **Confidence**: emerging
- **Quote**: "Somehow GPT-6 Luna is half the price of that again—and GPT-6 Sol had a similar reduction compared to GPT-5.6 Sol."
- **Our assessment**: Table figures support "half" on input and cached input; Luna output is 0.50 vs 1.20 (~58% cut), not exactly half. Note the GPT-5.6 prices in this table ($4/$20 Sol) differ from the $5/$30 recorded in earlier notes (see Claim 2).

### Claim 2: The "half price" comparison is against GPT-5.6 promotional pricing, which is scheduled to rise 25% in November
- **Evidence**: Author's note under the table.
- **Confidence**: emerging
- **Quote**: "Note that GPT-5.6 has a scheduled 25% price increase for November, so GPT-6 is half the price of the promotional pricing for those models."
- **Our assessment**: Explains the discrepancy with `blog-simonwillison-astra-pelican-comparison-grid.md` (Sol stated as $5/$30) and `blog-simonwillison-gpt56-luna-price-drop.md` Claim 2 (Luna $0.20/$1.20, Sol unchanged): the table here appears to show current promotional GPT-5.6 rates. The source does not itself say which earlier figures were promotional; treat exact 5.6 baselines as uncertain. Price tables in the guide need dated "as of" labels.

### Claim 3: With Terra priced identically to GPT-6 Sol, GPT-5.6 Terra has no remaining reason to be used
- **Evidence**: Table: Terra $2/$0.20/$12 vs GPT-6 Sol $2/$0.20/$10.
- **Confidence**: anecdotal
- **Quote**: "(With GPT-5.6 Terra priced the same as GPT-6 Sol, any remaining reasons to use Terra just evaporated.)"
- **Our assessment**: Inference from price alone; Terra is actually $2 more on output. Reasonable heuristic (a dominated option) but unverified on capability, since the author hasn't benchmarked.

### Claim 4: Grok 4.7's aggressive pricing was undercut in a day by GPT-6 Sol
- **Evidence**: Grok 4.7 at $2/$0.50/$6 vs GPT-6 Sol $2/$0.20/$10 in the table.
- **Confidence**: emerging
- **Quote**: "Grok 4.7 priced itself at $2/$6, less than half the price of GPT-5.6 Sol, but is now equally priced to GPT-6 Sol on input and closer on output."
- **Our assessment**: Illustrates how quickly mid-tier price advantages evaporate — a reason not to hard-code model choices on price alone. Sol's cached input ($0.20) is also cheaper than Grok's ($0.50).

### Claim 5: GPT-6 Luna is among the cheapest models OpenAI has ever shipped and is Willison's pick for building applications
- **Evidence**: Historical comparison (GPT-4.1 Nano $0.10/$0.40, GPT-5 Nano $0.05/$0.40); Willison upgraded his Datasette Agent demo to Luna and reports it "seems to be fast and competent at both SQL queries and building HTML and JavaScript".
- **Confidence**: anecdotal
- **Quote**: "GPT-5.6 Luna was already my favorite model for building applications against, because it combined excellent performance with being really cheap."
- **Our assessment**: Single-practitioner, single-demo evidence; consistent with his Luna switch in `blog-simonwillison-gpt56-luna-price-drop.md` Claim 5.

### Claim 6: Opus 5.5 cut list price 20% versus Opus 4.5–5, and cache-read price 60%
- **Evidence**: Willison's arithmetic: previous $5/$25 → $4/$20; table shows Opus 5.5 cached input $0.20/M.
- **Confidence**: emerging
- **Quote**: "The price for cache reads fell 60%."
- **Our assessment**: The 60% cache figure is consistent with the table only if the prior cache-read price was $0.50/M (standard 10% of $5); the source does not state the old price. Plausible but derived.

### Claim 7: In long agentic sessions, cache-read pricing dominates cost because 90%+ of input tokens are cached
- **Evidence**: Author's assertion, no measurement shown.
- **Confidence**: anecdotal
- **Quote**: "That’s significant for longer agentic conversations, where 90%+ of input tokens are processed at cached token prices."
- **Our assessment**: Directionally matches the cache-centric design in `blog-anthropic-prompt-caching-everything.md` and Blitzy's 24%→90% reuse in `blog-simonwillison-gpt56-luna-price-drop.md` Claim 12. Implies cached-input price should be the primary column when comparing models for agent workloads. Note Fable 5.1 cached ($0.25) is only slightly above Opus 5.5 ($0.20) despite 2.5x list price.

### Claim 8: Anthropic positions Opus 5.5 as fixing communication style, token-efficient, and working at every effort level
- **Evidence**: Quoted statement from Thariq Shihipar (Anthropic) reproduced in the post; not tested by Willison in this post.
- **Confidence**: anecdotal (vendor claim)
- **Quote**: "Opus 5.5 is the result of your feedback."
- **Our assessment**: Vendor claim. It is undercut in part by Claim 9 ("works across every effort level" vs. max failing). The remainder of the quoted text is not reproduced here to keep the quote contiguous.

### Claim 9: Opus 5.5 at "max" thinking hit the 128,000 output-token cap while still reasoning and returned no answer, twice
- **Evidence**: Two failed runs of the pelican SVG prompt; cost $2.56 each, ~20 minutes each; reasoning excerpts show the model verifying shin length, chainring teeth, layer order, etc. Fable 5.1 on max did not over-think.
- **Confidence**: emerging (reproduced twice, one prompt, one author)
- **Quote**: "Opus 5.5 has a 128,000 maximum output token limit (as do the other Claude models), and it hit that while it was still reasoning about the SVG!"
- **Our assessment**: A concrete, costed failure mode: reasoning tokens count against the output cap, so a maximal effort setting can yield zero deliverable at full price. Real limitation of max effort on a trivially scoped prompt, not obviously misconfiguration. Caveat: launch-day behavior may be patched.

### Claim 10: Willison concludes "max" effort is effectively unusable for him
- **Evidence**: Extrapolation from Claim 9.
- **Confidence**: anecdotal
- **Quote**: "This makes me suspect that “max” is effectively useless—if it over-thinks to breaking point on a stupid SVG prompt I don’t trust it not to do the same for more interesting work."
- **Our assessment**: Hedged ("suspect") and generalized from n=2 on a low-complexity task. Useful as a caution to cap or test top effort levels before defaulting to them; contrast with Cursor's use of higher effort finding 35% more bugs (`blog-cursor-bugbot-effort-billing.md` Claim 6).

### Claim 11: Reasoning-level sweeps within one model family remain a useful comparison method even if cross-vendor pelican comparison is not
- **Evidence**: Author's method statement; comparison grids for Opus 5.5 vs Opus 5, Fable 5.1, Sonnet 5.
- **Confidence**: anecdotal
- **Quote**: "Comparing different model vendors by how well they draw a pelican riding a bicycle may not make much sense now (if it ever did), but I’m still finding value in using them for comparisons of the same model families at different reasoning levels."
- **Our assessment**: Supports guidance to evaluate effort levels per model empirically rather than assuming monotonic quality gains.

### Claim 12: The price war so far affects only the tier below the flagship models; Haiku faces a 10x price gap
- **Evidence**: Fable 5.1 and GPT-6 Astra both $10/$50; Haiku 4.5 at $1/$5 vs GPT-6 Luna $0.10/$0.50; Sonnet 5.5 and Haiku 5.5 announced as "coming soon".
- **Confidence**: emerging
- **Quote**: "The price war currently affects the next tier of models below that."
- **Our assessment**: Snapshot claim; Anthropic's small-model pricing is likely to change when Haiku 5.5 ships. Consistent with `blog-simonwillison-gpt6-astra-launch.md` Claim 3 (Astra = Fable pricing).

### Claim 13: Willison now defaults to GPT-6 Sol in Codex and Opus 5.5 in Claude Code
- **Evidence**: Self-reported practice.
- **Confidence**: anecdotal
- **Quote**: "I’m now using GPT-6 Sol and Claude Opus 5.5 as my default models in Codex and Claude Code."
- **Our assessment**: Written on launch day, before extended use. Note he chose the second-tier models rather than Astra/Fable 5.1 as defaults, implying price/performance beats top capability for daily agent work for him.

## Concrete Artifacts

Pricing table from the post (per million tokens; Willison, 2026-09-22):

```
Model             Input    Cached input   Output
GPT-6 Luna        $0.10    $0.01          $0.50
GPT-5.6 Luna      $0.20    $0.02          $1.20
Grok 4.7          $2       $0.50          $6
GPT-6 Sol         $2       $0.20          $10
GPT-5.6 Terra     $2       $0.20          $12
Claude Opus 5.5   $4       $0.20          $20
GPT-5.6 Sol       $4       $0.40          $20
Claude Fable 5.1  $10      $0.25          $50
GPT-6 Astra       $10      $1             $50
```

Failure record (Opus 5.5, thinking "max", prompt "Generate an SVG of a pelican riding a bicycle"): 2 of 2 runs terminated at the 128,000 output-token limit with no SVG returned; cost $2.56 per run, ~20 minutes each.

## Cross-References

- **Corroborates**: `blog-simonwillison-gpt6-astra-launch.md` Claim 3 (Astra $10/$50 = Fable pricing); `blog-simonwillison-gpt56-luna-price-drop.md` Claim 5 (Willison picks Luna for his demo site) and Claim 4 (Luna vs Haiku 4.5 price gap, now widened to 10x); `blog-anthropic-prompt-caching-everything.md` (cache-dominated economics of agent sessions).
- **Contradicts**: None filed. Sol's $4/$20 here vs $5/$30 in `blog-simonwillison-astra-pelican-comparison-grid.md` Claim 3 is a pricing-baseline discrepancy explained by the source's own promotional-pricing note (Claim 2), not a position disagreement. Tension between Anthropic's "works across every effort level" (Claim 8) and the max-effort failure (Claim 9) is within one source and is a vendor-claim vs. test result, noted here rather than filed.
- **Extends**: `blog-simonwillison-introducing-opus-5.md` Claim 3 (Opus 5 priced same as 4.8) with the 5.5 price cut; `blog-simonwillison-astra-pelican-comparison-grid.md` reasoning-level sweep method to Opus 5.5.
- **Novel**: The Opus 5.5 max-effort output-cap failure with costs; Opus 5.5's 20%/60% price cuts; GPT-6 Sol/Luna pricing; the promotional-pricing caveat and scheduled November increase for GPT-5.6.

## Guide Impact

- **Chapter 08 (model selection/cost)**: Add a dated pricing snapshot (with cached-input column) and advise picking on cached-input price for long agent sessions; cite Claims 6–7 and the table. Add that price tables go stale within days and cite promotional-vs-list distinctions (Claim 2).
- **Chapter 03 / Ch01 (effort settings)**: Add a warning that the top effort level can burn the full output-token cap on reasoning and return nothing (Claim 9); recommend testing each model's max setting on a small task before defaulting, and setting cost/time limits.
- **Ch04 (context engineering)**: Reinforce cache-read pricing as the main cost lever for agentic sessions (Claim 7), pairing with the existing prompt-caching source.

## Extraction Notes

- Read the full post (fetched raw HTML and stripped markup); quotes copied from that text. Linked pelican galleries and the Thariq Shihipar post were not followed (image galleries / tweet). Pricing figures are the author's transcription and were not verified against vendor pages. Post is launch-day; several conclusions are explicitly preliminary.
