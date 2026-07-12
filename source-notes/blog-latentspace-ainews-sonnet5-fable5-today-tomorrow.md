---
source_url: https://www.latent.space/p/ainews-sonnet-5-today-and-fable-5
source_type: blog-post
title: "[AINews] Sonnet 5 today, and Fable 5 tomorrow"
author: swyx / smol.ai (AINews aggregation, published under Latent Space)
date_published: 2026-07-01
date_extracted: 2026-07-12
last_checked: 2026-07-12
status: current
confidence_overall: emerging
issue: "#1778"
---

# [AINews] Sonnet 5 today, and Fable 5 tomorrow

> A same-day AINews aggregation of Claude Sonnet 5's July 1, 2026 launch,
> notable for supplying the specific benchmark deltas, task-cost figures, and
> tokenizer-driven pricing quirks that the official GitHub Copilot GA
> changelog omitted — and for documenting a genuine practitioner split
> between "clear upgrade" and "worst Anthropic launch" reactions, driven
> almost entirely by task-level cost rather than raw capability.

## Source Context

- **Type**: blog-post (Latent Space's "AINews" daily digest — largely
  automated aggregation of Twitter/X and Reddit discussion plus official
  vendor statements, published under the Latent Space umbrella; subtitle:
  "Everything is open again!", referencing the parallel Fable/Mythos 5
  access-restoration story covered in the same post). Published 2026-07-01
  for the 6/29–6/30/2026 news cycle ("We checked 12 subreddits, 544
  Twitters and no further Discords").
- **Author credibility**: No individual byline; this is the same
  AINews/smol.ai aggregation format already in this corpus
  (`blog-latentspace-ainews-meta-harness-summer.md`,
  `blog-latentspace-fable-5-mythos-launch.md`). Its value is curation and
  synthesis of what the AI-engineering Twitter conversation converged on
  that day, not first-party reporting — individual figures trace back to
  named accounts (chiefly @ArtificialAnlys, @cursor_ai, @cognition, @cline,
  @kimmonismus, @theo, @simonw) relayed or paraphrased by the digest, so
  credibility should be assessed claim-by-claim rather than for the source
  as a whole.
- **Scope**: Covers the Sonnet 5 launch (official positioning, technical
  specs/pricing, benchmark deltas, tokenizer/cost quirks, ecosystem
  rollout, and a structured "facts vs. opinions" breakdown of the
  reaction), plus separate same-issue sections on Chinese open-weight
  models/infra, inference hardware, agent "loop engineering" discourse from
  AI Engineer World's Fair, and other model/tooling releases. Does NOT
  cover: the AI Reddit Recap section (behind this post's paywall — see
  Extraction Notes), independent verification of any Artificial Analysis or
  Cursor/Cognition benchmark number, or first-hand practitioner testing by
  this digest's own writers.

## Extracted Claims

### Claim 1: Sonnet 5 and Fable/Mythos 5 were announced separately rather than simultaneously, with Fable/Mythos 5 only "approved to be released again after some work with the government"
- **Evidence**: The article's own opening framing sentence, linking to the official Anthropic Sonnet 5 announcement and to an X post about Fable/Mythos 5's re-approval.
- **Confidence**: emerging (the Sonnet 5 launch fact is settled/official; the "approved... after some work with the government" characterization of Fable/Mythos 5 is the digest's own paraphrase of a linked X post, not independently verified by this Miner against a primary regulatory source)
- **Quote**: "In separate announcements, Sonnet 5 was released today, and Fable/Mythos 5 were approved to be released again after some work with the government."
- **Our assessment**: This directly confirms that the pre-launch expectation of a combined Sonnet 5 + Fable 5 release (documented as rumor in this same article's "Launch timeline" section, and consistent with the export-control suspension already in the corpus via `blog-simonwillison-fable-5-export-controls.md` and `blog-simonwillison-fable-mythos-access-directive.md`) did not materialize — the two releases were decoupled, with Fable 5's return gated on unspecified "work with the government." This is a useful timeline anchor: as of July 1, 2026, Fable/Mythos 5 access was being restored but had not shipped alongside Sonnet 5.

### Claim 2: Anthropic officially positioned Sonnet 5 as its "most agentic Sonnet yet," capable of planning and browser/terminal tool use previously requiring larger, more expensive models
- **Evidence**: Digest paraphrase attributed to the official @claudeai account.
- **Confidence**: settled (vendor's own launch framing, consistent with the "most agentic Sonnet yet" language typical of frontier-model launch copy)
- **Quote**: "Anthropic officially announced Claude Sonnet 5 as “our most agentic Sonnet yet,” emphasizing planning, browser/terminal tool use, and autonomous execution that previously “required larger and more expensive models” (@claudeai)"
- **Our assessment**: This is the vendor's own capability-positioning claim, not an independently measured one. It should be read alongside Claims 6-8 below (Artificial Analysis's measured deltas), which complicate the "does what used to require larger models" framing by showing Sonnet 5 trails Opus 4.7/4.8 on the aggregate Intelligence Index and costs more per completed task than Opus 4.8 in practice.

### Claim 3: Standard list pricing for Sonnet 5 is $3/M input and $15/M output tokens, with a promotional rate of $2/M input and $10/M output through Aug. 31/Sept. 1
- **Evidence**: Digest paraphrase attributed jointly to @kimmonismus, @ClaudeDevs, and @ArtificialAnlys, repeated identically in the "Core product specs and pricing" section later in the article.
- **Confidence**: settled (pricing figures corroborated across the digest's two independent mentions and multiple named sources within it)
- **Quote**: "Anthropic kept the standard list price at $3/M input tokens and $15/M output tokens, but introduced a promotional rate of $2/M input and $10/M output through Aug. 31 / Sept. 1 depending on the post"
- **Our assessment**: `docs-github-copilot-sonnet5-ga.md` Claim 4 documented that GitHub's Copilot changelog states Sonnet 5 is "billed at provider list pricing under Usage Based Billing" without disclosing a rate, explicitly flagging that gap ("practitioners need to consult GitHub's models-and-pricing documentation... for the actual UBB multiplier"). This source fills that specific gap for the direct API/Claude Platform surface (not confirmed to be identical to the Copilot UBB multiplier, which is a separate billing conversion) — $3/$15 standard, temporarily discounted to $2/$10. This is an **Extends** relationship, not a straightforward one: the two sources describe different billing surfaces (Copilot UBB vs. Anthropic direct list price), so this should be added as "Anthropic's own list price" context rather than assumed to be the exact Copilot UBB multiplier.

### Claim 4: Sonnet 5 cache pricing carries a 25% premium for cache writes ($3.75/M) and a 90% discount for cache hits ($0.30/M), with a 5-minute TTL
- **Evidence**: Digest's "Core product specs and pricing" bullet list, attributed to @ArtificialAnlys.
- **Confidence**: emerging (specific figures attributed to a single named third-party aggregator, not cross-verified against Anthropic's own pricing page by this Miner)
- **Quote**: "Cache pricing: 25% premium for cache writes ($3.75/M), 90% discount for cache hits ($0.3/M), 5-minute TTL (@ArtificialAnlys)"
- **Our assessment**: This is the first corpus source to state Sonnet 5's specific prompt-cache economics. The 5-minute TTL matches the cache-TTL figure pattern already familiar from other Claude-family pricing in this corpus space, but no other note currently documents Sonnet-5-specific cache pricing, so this is novel and directly actionable for cost-modeling guidance on cache-heavy agent workloads.

### Claim 5: Sonnet 5 adds a new "xhigh" reasoning-effort tier, bringing it to 5 effort levels (max, xhigh, high, medium, low) matching Opus 4.8
- **Evidence**: Digest spec bullet, attributed to @ArtificialAnlys.
- **Confidence**: settled (specific, checkable product detail attributed to a named source)
- **Quote**: "Effort settings: Sonnet 5 adds xhigh, for 5 effort levels total matching Opus 4.8: max, xhigh, high, medium, low (@ArtificialAnlys)"
- **Our assessment**: `docs-github-copilot-sonnet5-ga.md` Claim 3 documented that GitHub's changelog claims "competitive latency at lower effort levels" for Sonnet 5 without naming which levels exist, deferring to `docs-github-copilot-1m-context-reasoning-levels.md` for the general mechanism. This claim supplies the missing specificity: Sonnet 5's effort-level set now numerically matches Opus 4.8's, which previously had a level Sonnet-class models lacked. This directly extends and resolves part of the ambiguity flagged in the GA note.

### Claim 6: On CursorBench, Sonnet 5 scored 57% versus 49% for Sonnet 4.6
- **Evidence**: Digest paraphrase attributed to @cursor_ai, a named third-party coding-agent vendor's own benchmark.
- **Confidence**: emerging (vendor-run benchmark, not independently replicated by this Miner, but a concrete +8-point delta attributed to a specific named evaluator)
- **Quote**: "Cursor said Sonnet 5 is a meaningful step up on CursorBench: 57% vs 49% for Sonnet 4.6 (@cursor_ai)"
- **Our assessment**: This directly contradicts the vagueness of `docs-github-copilot-sonnet5-ga.md` Claim 2, which flagged GitHub's own "internal testing showed strong results" language as "the weakest evidentiary tier the guide accepts" with no benchmark name or number disclosed. This source supplies an independently-named, numeric benchmark result from a different vendor (Cursor, not GitHub), which the guide can cite in place of — or alongside — GitHub's unquantified internal-testing claim.

### Claim 7: On the Artificial Analysis Intelligence Index, Sonnet 5 scored 53 (+6 over Sonnet 4.6), ranking #5 overall — roughly tied with GPT-5.5 high reasoning but still behind Opus 4.7/4.8
- **Evidence**: Digest paraphrase attributed to @ArtificialAnlys.
- **Confidence**: emerging (single named third-party aggregator's composite index; not independently reproduced by this Miner, but methodologically an aggregate cross-benchmark index rather than a single anecdotal test)
- **Quote**: "Artificial Analysis Intelligence Index: Sonnet 5 scores 53, a +6 over Sonnet 4.6, placing it #5 overall, roughly tied with GPT-5.5 high reasoning, but still behind Opus 4.7/4.8 (@ArtificialAnlys)"
- **Our assessment**: This is the clearest single data point undercutting Anthropic's "most agentic Sonnet yet" positioning (Claim 2): on a broad composite index, Sonnet 5 improves meaningfully over its own predecessor but still trails the Opus tier, consistent with the "Benchmark criticism" reaction documented in Claim 11 below ("Sonnet 5 still trails Opus 4.8 'across all evals'"). Useful for a guide table contrasting vendor marketing language against independent aggregate benchmarking.

### Claim 8: Artificial Analysis found Sonnet 5 used ~40% more output tokens per task than Sonnet 4.6 (~69k tokens/task average), costing $2.29 per Intelligence Index task — about 2x Sonnet 4.6's cost and ~15% more than Opus 4.8 despite Sonnet 5's lower per-token list price
- **Evidence**: Digest's two adjacent bullets under "Benchmarks and measured deltas," both attributed to @ArtificialAnlys, and corroborated by the embedded Theo tweet in the same article ("Sonnet 5 was MORE EXPENSIVE THAN FABLE to run the whole bench," quoting his own earlier tweet "Sonnet 5 cost MORE than Opus 4.8 on the Artificial Analysis Intelligence Index").
- **Confidence**: emerging (specific quantitative figures from one named aggregator; independently corroborated in direction, though not in exact figure, by a second named individual's tweet reproduced in the same article — two convergent sources on the qualitative claim that Sonnet 5 costs more per task than Opus 4.8, but only one source for the exact $2.29/40%/15% figures)
- **Quote**: "Artificial Analysis token usage: Sonnet 5 used ~69k output tokens per task on average, about 40% more output tokens than Sonnet 4.6 (@ArtificialAnlys)"
- **Quote (task cost)**: "Artificial Analysis task cost: at standard pricing, Sonnet 5 cost $2.29 per Intelligence Index task, about 2x Sonnet 4.6 and ~15% more than Opus 4.8, despite lower per-token price, because of higher token usage (@ArtificialAnlys)"
- **Quote (embedded tweet, Theo, June 30, 2026, 9:22 PM)**: "Oh my god, Sonnet 5 was MORE EXPENSIVE THAN FABLE to run the whole bench 💀"
- **Our assessment**: This is the single most guide-relevant finding in the source: Sonnet 5's per-token price cut is not the same as a per-task cost cut, because the model uses substantially more output tokens and agentic turns to reach a solution (see Claim 9). For any guide discussion of model-selection cost modeling (`docs-github-copilot-cca-cost-efficient-models.md` territory), this is a concrete, named-source counterexample to "lower list price = cheaper to run" — practitioners evaluating Sonnet 5 for cost-sensitive agentic workloads should benchmark effective cost-per-completed-task, not list price, before switching.

### Claim 9: Sonnet 5 used roughly 3x the agentic turns of Sonnet 4.6 on AA-Briefcase and GDPval-AA benchmarks, and its max effort setting used ~6x more turns than its low effort setting on GDPval-AA
- **Evidence**: Digest bullet attributed to @ArtificialAnlys.
- **Confidence**: emerging (specific multiplier figures from a single named aggregator, not independently reproduced)
- **Quote**: "Agentic turns: Sonnet 5 used ~3x the agentic turns of Sonnet 4.6 on AA-Briefcase and GDPval-AA, and max effort used around 6x more turns than low effort on GDPval-AA (@ArtificialAnlys)"
- **Our assessment**: This is the specific mechanism behind Claim 8's cost finding — more agentic turns per task, not just more tokens per turn, drives the higher effective cost. It also quantifies effort-level tradeoffs for the first time in the corpus for a Sonnet-class model: choosing "max" effort over "low" effort can multiply turn count roughly 6x on at least one benchmark (GDPval-AA), a concrete number practitioners can use when deciding whether to default agentic workflows to lower effort settings for cost control.

### Claim 10: A tokenizer change makes Sonnet 5 approximately 1.4x more expensive to run on English text and ~1.33x on Spanish text than the previous tokenizer would imply, with roughly no change for Simplified Mandarin
- **Evidence**: Digest paraphrase attributed to @simonw (Simon Willison).
- **Confidence**: emerging (attributed to a specific, generally credible named practitioner already well-represented in this corpus for first-hand Claude-family analysis, but relayed here only via digest paraphrase, not Willison's own post directly)
- **Quote**: "Simon Willison noted the new tokenizer makes Sonnet 5 ~1.4x more expensive for English, ~1.33x for Spanish, and roughly the same for Simplified Mandarin (@simonw)"
- **Our assessment**: This is a distinct cost driver from Claims 8-9 (verbosity/turn count) — it is a pure tokenization-efficiency regression specific to English and Spanish, not agentic behavior. Combined with Claim 8, this means English-language practitioners comparing Sonnet 5's $3/$15 list price against Sonnet 4.6 are undercounting the real cost delta from two independent directions: more output tokens per task, and more tokens needed to encode the same text. This is directly actionable for Ch04 cost-modeling guidance: list-price comparisons across a tokenizer change require re-baselining token counts per language, not just per-token rates.

### Claim 11: Sonnet 5 reactions split sharply along naming, benchmark-position, and cost-per-task lines — critics argued the "5" naming implies a major-version leap while evals look closer to "4.8/4.9," that it still trails Opus 4.8 "across all evals," and that its actual task cost can exceed Opus 4.8 or even Fable
- **Evidence**: Digest's structured "Critical views" section, attributing each theme to specific named accounts.
- **Confidence**: anecdotal (aggregated Twitter reactions, not a controlled survey, but multiple independently named accounts converge on each specific theme, which the digest itself flags as "the most technically grounded negative theme" for the cost point)
- **Quote**: "Naming criticism: users argued “Sonnet 5” implies a major-version leap, while evals suggest something closer to Sonnet 4.8/4.9 (@kimmonismus, @teortaxesTex)"
- **Quote (cost)**: "Cost-per-task criticism: this became the most technically grounded negative theme. Theo, Yuchen Jin, Scaling01, and Kimmonismus all amplified that Sonnet 5 can be more expensive than Opus 4.8 or even Fable on actual evaluated tasks due to verbosity/turn count"
- **Our assessment**: The digest's own editorial judgment — explicitly calling the cost-per-task criticism "the most technically grounded" of the three critical themes, as opposed to the naming and benchmark-position complaints, which it does not qualify the same way — is itself a useful signal for the guide: it suggests that even within a mixed-reaction launch, the cost finding (Claims 8-9) is the substantive one, while naming complaints are more subjective. Recommend the guide treat the cost-per-task data as the load-bearing evidence and the naming/positioning complaints as color/context.

### Claim 12: Sonnet 5 was adopted "unusually quickly" across the coding-agent ecosystem — Cursor, Devin/Cognition, Cline, FactoryAI Droid, Perplexity, VS Code, and Agent Arena all added support at or near launch, which the digest frames as evidence of where the market believes the model's value lies
- **Evidence**: Digest's "Ecosystem rollout" section, listing each integration with its own attributed source.
- **Confidence**: emerging (concrete, checkable list of named integrations, each individually sourced to that vendor's own announcement; the "unusually quickly" framing itself is the digest's own editorial characterization, not independently benchmarked against typical launch-adoption timelines)
- **Quote**: "Sonnet 5 was adopted unusually quickly across the coding-agent ecosystem, which is itself evidence of where the market thinks the value lies."
- **Quote (Cline detail)**: "Cline highlighted Opus 4.8-level performance on Terminal-Bench for less than half the cost, plus improved resistance to prompt-injection hijacks for “--yolo coders” (@cline)"
- **Our assessment**: This corroborates and extends `docs-github-copilot-sonnet5-ga.md` Claim 6, which documented Sonnet 5's simultaneous rollout across ten GitHub Copilot surfaces on June 30, by showing the same rapid-adoption pattern held across the broader third-party coding-agent ecosystem (Cursor, Cognition/Devin, Cline, FactoryAI, Perplexity) within roughly 24 hours of the June 30/July 1 launch — not just within Microsoft/GitHub's own product line. Cline's specific claim (Opus 4.8-level Terminal-Bench performance at under half the cost, despite Claims 8-9 showing higher AA-measured task cost than Opus 4.8) is worth flagging as a tension: different evaluators, different benchmarks, and possibly different effort-level defaults can produce opposite cost conclusions — a caution against citing any single vendor's cost claim as universally representative.

### Claim 13: Anthropic-linked summary posts claimed Sonnet 5 is safer than Sonnet 4.6 overall, with lower hallucination and sycophancy and cyber safeguards on by default, while acknowledging Opus remains stronger for serious cyber work
- **Evidence**: Digest paraphrase attributed to @kimmonismus, characterized by the digest as "Anthropic-linked summary posts."
- **Confidence**: anecdotal (secondhand paraphrase of vendor-adjacent claims relayed via a single named aggregator account, not sourced directly to an Anthropic system card or safety report by this Miner)
- **Quote**: "Anthropic-linked summary posts stressed that Sonnet 5 is safer than Sonnet 4.6 overall, with lower hallucination and sycophancy, and that cyber safeguards are on by default, while still acknowledging Opus remains stronger for serious cyber work (@kimmonismus)"
- **Our assessment**: This is a vendor-adjacent safety claim with no primary-source citation in this article (no system card or safety-report link is given for this specific bullet). It should be treated as a pointer to go verify against Anthropic's actual Sonnet 5 system card, not cited directly as settled safety evidence — the "Opus remains stronger for serious cyber work" caveat is notable as an explicit admission of a capability gap between tiers even within a safety-positive framing.

### Claim 14: On the CritPt frontier-physics benchmark, Sonnet 5 scored 17% (+14 points over its predecessor) but still trailed GLM-5.2, Claude Opus, Fable, and GPT-5.5 variants
- **Evidence**: Digest bullet attributed to @ArtificialAnlys.
- **Confidence**: emerging (specific named-benchmark figure from a single third-party aggregator, not independently reproduced)
- **Quote**: "CritPt frontier physics benchmark: Sonnet 5 scored 17%, +14 points over its predecessor, but still behind GLM-5.2, Claude Opus, Fable, and GPT-5.5 variants (@ArtificialAnlys)"
- **Our assessment**: This is the first CritPt figure for Sonnet 5 in the corpus, and it reinforces the same pattern as Claim 7 (large relative improvement over Sonnet 4.6, but still positioned below both the Opus tier and Fable/GPT-5.5) — evidence that Sonnet 5's gains are real but tier-consistent rather than frontier-redefining, corroborating the digest's own "Neutral/engineering interpretation" (Claim 15 below) rather than either the "clear upgrade" or "worst launch" extremes.

### Claim 15: The digest's own synthesis frames Sonnet 5 as "a production-friendly release more than a hype release" and characterizes the split reaction as "clear upgrade" versus "worst Anthropic launch," both responding to genuinely different axes (absolute capability vs. Sonnet 4.6, headline frontier progress vs. Opus/Fable, list price vs. task-level cost, ecosystem utility)
- **Evidence**: The article's own "Context" section, its concluding synthesis paragraph.
- **Confidence**: settled (this is the source's own editorial framing, not an external claim requiring verification)
- **Quote**: "This is a production-friendly release more than a hype release—better on coding/agents, broadly deployable, but not a flagship-redefining jump (@dejavucoder, @OpenAIDevs)"
- **Quote (reaction split)**: "That is why reactions ranged from “clear upgrade” to “worst Anthropic launch.” Both are responding to real but different axes"
- **Our assessment**: This is a useful one-line synthesis for the guide: rather than treating the mixed reception as a contradiction to resolve, the source explicitly enumerates the five distinct axes (capability-vs-predecessor, capability-vs-frontier-expectations, list price, task-level cost, ecosystem utility) on which different observers were independently correct — a template for how the guide itself should present model-launch reactions that appear contradictory only because commentators are implicitly scoring different axes.

## Concrete Artifacts

### Sonnet 5 core specs and pricing (as reported)
```
Source: [AINews] Sonnet 5 today, and Fable 5 tomorrow, Latent Space, 2026-07-01

Context window:        1,000,000 tokens
Standard pricing:       $3/M input, $15/M output
Promotional pricing:    $2/M input, $10/M output (through Aug. 31 / Sept. 1)
Cache write premium:    25% ($3.75/M)
Cache hit discount:     90% ($0.30/M)
Cache TTL:              5 minutes
Effort levels:          max, xhigh, high, medium, low (5 total; xhigh is new)
Rumored knowledge cutoff (pre-launch): January 2026
```

### Artificial Analysis benchmark deltas (Sonnet 5 vs. Sonnet 4.6 / Opus 4.8, as reported)
```
Source: [AINews] Sonnet 5 today, and Fable 5 tomorrow, Latent Space, 2026-07-01,
citing @ArtificialAnlys

Intelligence Index:        53 (+6 vs Sonnet 4.6), #5 overall, ~tied GPT-5.5 high
                            reasoning, behind Opus 4.7/4.8
Output tokens/task (avg):  ~69k (+40% vs Sonnet 4.6)
Task cost (Intelligence
  Index, standard price):  $2.29/task (~2x Sonnet 4.6, ~15% more than Opus 4.8)
Agentic turns:              ~3x Sonnet 4.6 on AA-Briefcase and GDPval-AA
Max- vs low-effort turns:  ~6x more turns at max effort vs low effort (GDPval-AA)
CritPt (frontier physics):  17% (+14 vs predecessor); trails GLM-5.2, Opus,
                            Fable, GPT-5.5 variants
Also improved vs 4.6:       Terminal-Bench v2.1 (+9), Humanity's Last Exam (+10),
                            SciCode (+7)
```

### Named practitioner reactions (as quoted/paraphrased in the article)
```
Source: [AINews] Sonnet 5 today, and Fable 5 tomorrow, Latent Space, 2026-07-01

@theo (embedded tweet, 9:22 PM, Jun 30, 2026):
  "Oh my god, Sonnet 5 was MORE EXPENSIVE THAN FABLE to run the whole bench 💀"
  quoting his own earlier tweet: "Sonnet 5 cost MORE than Opus 4.8 on the
  Artificial Analysis Intelligence Index"

@theo: "It's been 18 days since Fable 5 was banned"
@kimmonismus: "instead we got sonnet 5"
@simonw: tokenizer change makes Sonnet 5 ~1.4x more expensive for English,
  ~1.33x for Spanish, roughly unchanged for Simplified Mandarin
@cline: Opus 4.8-level Terminal-Bench performance for less than half the cost,
  plus improved resistance to prompt-injection hijacks for "--yolo coders"
```

## Cross-References

- **Extends** `docs-github-copilot-sonnet5-ga.md` Claim 4 (GitHub's Copilot
  changelog states Sonnet 5 is "billed at provider list pricing under Usage
  Based Billing" with no rate disclosed): this source's Claim 3 supplies the
  underlying Anthropic list price ($3/$15 standard, $2/$10 promotional
  through Aug. 31/Sept. 1) — though for the direct API/Claude Platform
  surface, not confirmed identical to the Copilot UBB multiplier.
- **Extends** `docs-github-copilot-sonnet5-ga.md` Claim 3 (GitHub's changelog
  claims "competitive latency at lower effort levels" without naming the
  levels): this source's Claim 5 names the specific 5-level effort system
  (max, xhigh, high, medium, low) and confirms xhigh is new to Sonnet-class
  models with this release.
- **Extends** `docs-github-copilot-sonnet5-ga.md` Claim 2 (GitHub's
  unquantified "internal testing showed strong results... particularly
  strong performance on CLI-style tasks," flagged in that note as "the
  weakest evidentiary tier the guide accepts"): this source's Claims 6-9 and
  14 supply multiple independently-named, numeric third-party benchmark
  results (CursorBench, Artificial Analysis Intelligence Index, CritPt,
  Terminal-Bench, Humanity's Last Exam, SciCode) that the guide can cite in
  place of GitHub's unquantified claim.
- **Extends** `docs-github-copilot-sonnet5-ga.md` Claim 6 (ten-surface
  simultaneous rollout across GitHub Copilot on June 30, 2026): this
  source's Claim 12 shows the same rapid, near-simultaneous adoption
  pattern held across the broader third-party coding-agent ecosystem
  (Cursor, Cognition/Devin, Cline, FactoryAI, Perplexity, Agent Arena)
  within the same launch window, not just within GitHub's own product line.
- **Corroborates** `blog-latentspace-fable-5-mythos-launch.md` (documents
  the June 10, 2026 Fable 5/Mythos 5 launch and the subsequent government
  export-control suspension chain): Claim 1 of this note confirms that as
  of July 1, 2026, Fable/Mythos 5 access was reported as being restored
  ("approved to be released again after some work with the government")
  but had not shipped simultaneously with Sonnet 5 as some practitioners
  expected — extending that note's timeline forward by roughly three weeks.
- **Novel**: Sonnet 5's specific cache pricing (25% write premium, 90% hit
  discount, 5-minute TTL); the tokenizer-driven ~1.4x English / ~1.33x
  Spanish cost increase; the ~69k-output-tokens/task and $2.29/task
  Artificial Analysis cost figures; the ~3x-6x agentic-turn multipliers by
  effort level; the CritPt, Terminal-Bench v2.1, Humanity's Last Exam, and
  SciCode deltas; and the structured "clear upgrade vs. worst Anthropic
  launch, five different axes" synthesis framing (Claim 15) are all new to
  this corpus.

## Guide Impact

- **Chapter 04 (Context Engineering / Model Selection & Cost)**: Add Sonnet
  5's task-level cost finding (Claims 8-9-10) as a concrete case study in
  why list-price-per-token comparisons are insufficient for model-selection
  cost modeling: a model with a lower per-token price ($3/$15 vs. Sonnet
  4.6, and vs. Opus 4.8) can still cost more per completed task due to
  higher output-token verbosity (+40%), more agentic turns (~3x), and a
  tokenizer regression (~1.4x for English). Recommend practitioners
  benchmark effective cost-per-solved-task before switching models based on
  list price alone. Add the specific cache-pricing structure (Claim 4) to
  any Sonnet-5-specific cost table.
- **Chapter 06 (Model Selection & Evaluation)**: Add the Artificial Analysis
  Intelligence Index (#5, score 53), CursorBench (57% vs. 49%), and CritPt
  (17%, still behind GLM-5.2/Opus/Fable/GPT-5.5) figures (Claims 6, 7, 14)
  as independently-sourced, numeric benchmark data points to replace or
  supplement the vendor-unquantified "internal testing showed strong
  results" language currently the only performance claim documented for
  Sonnet 5 in `docs-github-copilot-sonnet5-ga.md`. Flag all figures as
  single-aggregator-sourced (Artificial Analysis, Cursor, Cognition) and
  not independently reproduced by this corpus.
- **Chapter 04 (Context Engineering / effort-level tuning)**: Add the
  5-level effort system (max, xhigh, high, medium, low) and the ~6x
  turn-count multiplier between max and low effort on GDPval-AA (Claim 9)
  as concrete guidance for tuning agentic workflows' cost/quality tradeoff
  via effort level — cross-reference with
  `docs-github-copilot-1m-context-reasoning-levels.md` for the general
  Copilot-side mechanism.
- **Chapter 02 (Harness Engineering / ecosystem adoption)**: Add the rapid,
  near-simultaneous third-party ecosystem adoption pattern (Claim 12:
  Cursor, Devin/Cognition, Cline, FactoryAI, Perplexity, Agent Arena all
  within roughly 24 hours of launch) as evidence that coding-agent-tool
  adoption speed is now a reasonable signal of where practitioner-perceived
  model value lies, independent of aggregate benchmark rank — while
  flagging Cline's own cost claim (Opus 4.8-level Terminal-Bench
  performance at under half the cost) as in apparent tension with the
  Artificial Analysis task-cost figures in Claim 8, a caution against
  treating any single vendor's cost claim as universally representative.

## Extraction Notes

- **WebFetch returned only a ~200-word AI-generated summary, not article
  text**: consistent with the precedent already documented in
  `blog-latentspace-ainews-meta-harness-summer.md` and
  `blog-latentspace-databricks-agent-clouds.md` for this same publication.
  The full free-preview article text (through the paywall boundary) was
  recovered via `curl` against the raw page HTML and parsed locally
  (stripping markup while preserving heading structure and the one embedded
  tweet's `data-attrs` JSON, which contains the tweet's `full_text` and
  `quoted_tweet.full_text` verbatim). All quotes above were copied
  character-for-character from that recovered text.
- **Paywall boundary confirmed**: the recovered text ends cleanly at the "AI
  Reddit Recap / /r/LocalLlama + /r/localLLM Recap" heading, followed
  immediately by a "Keep reading with a 7-day free trial" prompt — the
  Reddit recap section is genuinely behind the paywall and was not read.
  Everything above that heading (the full "AI Twitter Recap" section
  covering Sonnet 5, plus separate sections on Chinese open-weight
  models/infra, inference hardware, "loop engineering" discourse from AI
  Engineer World's Fair, and other model/tooling releases) was recovered
  and read in full.
- **Only one tweet is embedded with full inline text** (Theo's, via a
  `data-attrs` JSON payload in the HTML); all other cited tweets
  (@simonw, @ArtificialAnlys, @claudeai, @ClaudeDevs, @kimmonismus, @cline,
  @cursor_ai, @cognition, etc.) appear in the article only as the digest's
  own paraphrase with a hyperlink to the original post, not as embedded
  full-text quotes. Quotes for those items above are the digest's own
  sentence (attributed to the named account via the digest's parenthetical
  citation), not a verbatim quote of the underlying tweet itself — this
  distinction is preserved throughout (each such quote is introduced as
  what the digest itself says, with the named account cited as the digest's
  attribution, not presented as if it were the tweet's own text).
- **Not extracted as standalone claims** (out of scope for the Prospector's
  stated chapter relevance — Ch02/Ch03/Ch04/Ch06 — or thin/already covered
  elsewhere in the corpus): the China open-weights/infrastructure section
  (Meituan 1.6T MoE, Huawei/Pangu, DeepSeek infra) — overlaps with
  `blog-latentspace-glm52-open-frontier-parity.md` territory and is not a
  harness/model-selection story; the inference/chips section (Etched's
  stealth exit, NVIDIA Volta-to-Blackwell explainer, OpenAI's inference
  cost optimization) — infrastructure story, not agent/harness-relevant;
  the "loop engineering" mention (Andrew Ng, AI Engineer World's Fair,
  "loopcraft") — already substantially covered by
  `blog-latentspace-aiewf-loops-software-factories-dispatch.md` and related
  loop-engineering notes already in this corpus, and this article adds no
  new specifics beyond naming the theme; the Google media-model launches
  (Nano Banana 2 Lite, Gemini Omni Flash), Hugging Face hardware filter, and
  other open-source/local-AI tooling items in the closing section — none
  overlap with the Prospector's stated chapter relevance for this issue.
- **No contradictions filed**: Claim 12's Cline-vs-Artificial-Analysis cost
  tension (Cline claims Sonnet 5 beats Opus 4.8 cost at under half the
  price on Terminal-Bench; Artificial Analysis found Sonnet 5 costs ~15%
  more than Opus 4.8 on its own Intelligence Index tasks) does not meet the
  bar in `agents/MINER.md` §4a for a formal contradiction issue — both are
  vendor/aggregator-specific benchmark results on different task sets with
  likely different effort-level defaults, not a claim about the same
  measured quantity. Noted in Claim 12's assessment and Chapter 02 Guide
  Impact as a caution rather than a resolved conflict.
- Cross-references verified: `docs-github-copilot-sonnet5-ga.md` Claims 2,
  3, 4, 6 confirmed by direct re-read of that note (lines 67-83, 85-103,
  105-120, 142-162 respectively) before citing in this note's Cross-References
  and Guide Impact sections.
