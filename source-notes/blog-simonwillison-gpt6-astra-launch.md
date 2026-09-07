---
source_url: https://simonwillison.net/2026/Sep/3/gpt6-astra/
source_type: blog-post
title: "GPT‑6 Astra"
author: Simon Willison
date_published: 2026-09-03
date_extracted: 2026-09-07
last_checked: 2026-09-07
status: current
confidence_overall: emerging
issue: "#3288"
---

# GPT‑6 Astra

> Simon Willison's day-one link/notes post on OpenAI's GPT‑6 Astra launch:
> price parity with Claude Fable 5/5.1 ($10/$50 per million tokens), a mixed
> benchmark profile (trails Fable 5.1 on Artificial Analysis's Intelligence
> Index but leads on Coding Agent Index cost-efficiency), a huge harness-
> dependent swing on ARC-AGI-3 (99.9% vs. 62.7%), and a large jump over
> GPT‑5.6 Sol on security/reverse-engineering benchmarks — all reported
> secondhand from vendor/Artificial Analysis data, since Willison had not
> yet used the model himself at time of writing.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, September 3, 2026 — a short,
  same-day "notes" post reacting to a model launch, not a hands-on
  evaluation).
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` CLI, and one of the most widely-cited practitioner commentators on
  LLM tooling — already a heavily-used trusted-feed source in this corpus
  (e.g. `blog-simonwillison-claude-fable-5.md`,
  `blog-simonwillison-gpt56-sol-launch.md`). Critically, **this specific
  post is not a hands-on evaluation** — Willison states outright that he
  had not tried Astra himself. All benchmark and pricing claims in this
  post are Willison curating and synthesizing OpenAI's own announcement and
  Artificial Analysis's independent benchmark numbers, not his own
  first-person testing (contrast with `blog-simonwillison-claude-fable-5.md`,
  where he ran the model directly for ~5.5 hours). Treat this note's
  authority as "trusted synthesizer of day-one vendor/third-party data,"
  not "practitioner who used the model."
- **Scope**: Covers Astra's rollout timeline, API pricing, the API model
  label, Artificial Analysis's Intelligence Index and Coding Agent Index
  scores, ARC-AGI-3 performance under two harness configurations, security/
  reverse-engineering benchmark deltas versus GPT‑5.6 Sol, and long-context
  (needle-in-haystack) performance. Does **not** cover: any first-person
  usage, coding-task walkthrough, context window size or knowledge cutoff
  date, multimodal capability, SWE-bench-style coding benchmarks, or a
  system-card-level safety disclosure (the post makes no mention of
  Preparedness Framework tier, cyber-capability classification, or
  safeguards — contrast with `blog-openai-astra-critical-cyber-capabilities.md`
  and `blog-openai-pacing-model-development-cyber-capabilities.md`, both of
  which are about this same model but from OpenAI's own safety-disclosure
  channel, not this launch-commentary post).

## Extracted Claims

### Claim 1: GPT‑6 Astra began rolling out on September 3, 2026 to a limited set of organizations, with broader availability to all ChatGPT Plus/Pro/Business/Enterprise users and the OpenAI API and AWS to follow over the coming days
- **Evidence**: Direct statement in the opening paragraph, describing OpenAI's stated rollout plan.
- **Confidence**: settled (a specific, dated, first-party rollout description, though the actual pace of the multi-day rollout is not independently verified in this post)
- **Quote**: "rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API and AWS"
- **Our assessment**: The AWS availability detail is notable — a same-launch-week AWS distribution channel alongside the direct OpenAI API is not something this corpus has previously documented for a GPT-series model at day-one. Practitioners tracking access windows should verify current availability rather than assume immediate universal access, since the post itself frames this as a staged rollout, not an instant GA.

### Claim 2: The API model label for Astra will be `gpt-6-astra`
- **Evidence**: Direct statement, likely OpenAI's own naming disclosure.
- **Confidence**: settled (a specific, checkable API identifier string)
- **Quote**: "The API model label once it rolls out will be `gpt-6-astra`."
- **Our assessment**: A concrete, verifiable string practitioners can check against the OpenAI API model list once Astra reaches general availability — useful for anyone updating a model-routing table or allowlist.

### Claim 3: GPT‑6 Astra's API pricing is $10/million input tokens and $50/million output tokens — identical to Claude Fable 5 and 5.1's pricing
- **Evidence**: Willison's direct statement of OpenAI's published pricing, explicitly framed as a price-parity comparison to Anthropic's flagship.
- **Confidence**: settled (published pricing at time of post)
- **Quote**: "It's going to be API priced at the same rate as Claude Fable 5 and 5.1: $10/million input and $50/million output."
- **Our assessment**: This is the first corpus documentation of OpenAI matching Anthropic's flagship price point exactly, rather than undercutting or exceeding it. Per `blog-simonwillison-claude-fable-5.md` Concrete Artifacts, $10/$50 is Fable 5's launch pricing (2x Opus 4.8); per `blog-simonwillison-gpt56-sol-launch.md` Concrete Artifacts, GPT‑5.6 Sol launched at $5/$30 — so Astra represents a 2x price jump over its own immediate predecessor (Sol) to land exactly at Fable's price point. This directly extends the cross-vendor flagship-pricing pattern tracked in `blog-simonwillison-gemini35-flash-pricing.md` Claim 5-6 and contradicted/refined in `blog-simonwillison-gpt56-sol-launch.md`'s Contradicts section (that note found Sol held flagship pricing flat rather than raising it) — Astra now shows OpenAI raising its true flagship price 2x over Sol, converging on Fable's rate rather than continuing Sol's flat-pricing pattern.

### Claim 4: Per Artificial Analysis, GPT‑6 Astra scores 61 on the Intelligence Index — equal to GPT‑5.6 Sol and 5 points lower than Claude Fable 5.1
- **Evidence**: Third-party benchmark aggregator score, cited by Willison.
- **Confidence**: emerging (third-party aggregate benchmark index; methodology not detailed in this post, though Artificial Analysis is an established third-party source already used elsewhere in the corpus)
- **Quote**: "GPT-6 Astra scores equal to GPT-5.6 Sol in the Index at 61. This is 5 points lower than Claude Fable 5.1"
- **Our assessment**: This is a direct, quantified rebuttal to any assumption that Astra is a strict Sol-successor on general intelligence — on this particular aggregate index, Astra does not improve on Sol at all, and trails Fable 5.1. Consistent with Willison's own closing framing (Claim 9 below) that Astra "doesn't win at everything." Practitioners selecting on raw general-intelligence benchmark score alone would still prefer Fable 5.1 per this metric.

### Claim 5: At max reasoning effort, GPT‑6 Astra costs about the same as GPT‑5.6 Sol (max) on Artificial Analysis's Coding Agent Index while scoring 2 points higher, and per-task costs less than half of Claude Fable 5 for the same score
- **Evidence**: Third-party benchmark aggregator cost/score comparison, cited by Willison.
- **Confidence**: emerging (third-party aggregate benchmark index; cost-per-task methodology not detailed in this post)
- **Quote**: "At max effort, GPT-6 Astra costs about the same as GPT-5.6 Sol (max) while scoring 2 points higher on the Index. Per task, the model is less than half the cost of Claude Fable 5, for the same score."
- **Our assessment**: This is the sharpest cost-efficiency claim in the post: despite matching Fable's *per-token* price exactly (Claim 3), Astra is claimed to cost less than half of Fable 5 *per completed coding task* at equivalent quality — implying Astra uses substantially fewer tokens (or fewer retries) to reach the same coding-agent outcome. If this holds up under independent verification, it is a meaningful practitioner data point: identical sticker price does not imply identical real-world cost, and per-task cost (not per-token price) is the number that matters for coding-agent budgeting. This is vendor/third-party-sourced and not independently reproduced by Willison himself, so it should be flagged as unverified pending practitioner testing.

### Claim 6: Artificial Analysis's own commentary frames Astra as still trailing Claude Fable on their metrics, despite Astra's Coding Agent Index cost-efficiency lead
- **Evidence**: Willison links to and paraphrases an Artificial Analysis social-media post.
- **Confidence**: emerging (third-party commentary, linked but only summarized by Willison rather than fully quoted in the post's own prose)
- **Quote**: "Artificial Analysis note that Astra is still beaten by Fable"
- **Our assessment**: This is a useful editorial signal alongside the raw numbers in Claims 4-5: even the source of the favorable Coding Agent Index comparison (Claim 5) does not characterize Astra as an overall win over Fable. Guide language should preserve this nuance — Astra leads on specific cost-efficiency metrics, not on Fable's own turf overall, per the benchmark aggregator's own framing.

### Claim 7: On the ARC-AGI-3 benchmark, GPT‑6 Astra scored 99.9% using OpenAI's custom "Provider Adapter harness" (at a stated cost of $19K), versus 62.7% using the default ARC-AGI harness (at a stated cost of $26K) — with the Provider Adapter harness preserving opaque reasoning state between requests and using compaction for longer conversations
- **Evidence**: Willison cites the ARC-AGI blog (arcprize.org) directly for both scores and both cost figures, plus the stated mechanism for the custom harness.
- **Confidence**: emerging (a specific, quantified benchmark result from a named third-party source — ARC Prize's own blog — but not independently reproduced by Willison, and the "$19K"/"$26K" cost figures' methodology is not detailed in this post)
- **Quote**: "the ARC-AGI blog notes that the 99.9% score was achieved for $19K using OpenAI's custom 'Provider Adapter harness', while the default ARC-AGI harness scored 62.7% for $26K." … "The Provider Adapter harness preserves opaque reasoning state between requests and uses compaction for longer conversations, allowing the model to reuse prior work." (two adjacent sentences from the same paragraph)
- **Our assessment**: This is a striking data point on its own terms — the custom harness scored dramatically higher (99.9% vs. 62.7%) *and* cost less ($19K vs. $26K) than the default harness on the same benchmark. It directly corroborates the mechanism (not just the direction) documented in `blog-openai-arc-agi-3-two-settings.md` Claims 2, 4-8: that note found GPT‑5.6 Sol's ARC-AGI-3 score tripled (13.3% → 38.3% RHAE) and output tokens fell 6x when OpenAI enabled "retained reasoning" and "compaction" via the Responses API — the exact same two mechanisms ("preserves opaque reasoning state between requests" = retained reasoning; "uses compaction for longer conversations") named here for Astra's "Provider Adapter harness." This is now a second model generation (Astra, not just Sol) and a second, even larger magnitude (99.9%/62.7% ≈ 1.6x, but from a much higher baseline, versus Sol's 13.3%→38.3% ≈ 2.9x from a much lower baseline) for the same underlying "harness configuration — not raw model capability — dominates this specific benchmark" finding. Guide treatment should present the 99.9% figure with this harness caveat attached every time it is cited, exactly as `blog-openai-arc-agi-3-two-settings.md`'s Guide Impact already recommends for Sol's number.

### Claim 8: GPT‑6 Astra shows large security-benchmark gains over GPT‑5.6 Sol: 100% on ExploitBench (Sol: 78.5%), 42.4% on ExploitGym (Sol: 30.3%), and 99.2% within four attempts on SRE-Bench binary reverse engineering (Sol: 68.7%)
- **Evidence**: Direct benchmark comparison, cited by Willison, presumably from OpenAI's own model/system-card disclosure.
- **Confidence**: emerging (specific, named-benchmark, quantified comparisons, but vendor-sourced and not independently reproduced or audited by a third party in this post)
- **Quote**: "Astra is a beast at security tasks. It scores 100% on ExploitBench (GPT-5.6 Sol got 78.5%), 42.4% on ExploitGym (Sol got 30.3%)" … "99.2% within four attempts on SRE-Bench binary reverse engineering compared to Sol's 68.7%."
- **Our assessment**: This is a directly relevant corroborating data point for the security-capability trajectory already documented from OpenAI's own safety-disclosure channel: `blog-openai-astra-critical-cyber-capabilities.md` Claim 1 disclosed (Aug 7, 2026) that OpenAI "cannot rule out critical cyber capabilities" for Astra based on internal evaluations showing "significant advancements in agentic coding and cybersecurity," and that post's Claim 4 placed the immediately preceding model, GPT‑5.6‑Sol, at the "High" (not Critical) cyber-capability tier. These ExploitBench/ExploitGym/SRE-Bench deltas are the first *quantified, named-benchmark* evidence in this corpus of the magnitude of Astra's security-capability jump over Sol specifically — a 21.5-point ExploitBench gain, a 12.1-point ExploitGym gain, and a 30.5-point SRE-Bench reverse-engineering gain. None of the three OpenAI safety posts already in this corpus (`blog-openai-astra-critical-cyber-capabilities.md`, `blog-openai-pacing-model-development-cyber-capabilities.md`) name ExploitBench, ExploitGym, or SRE-Bench specifically or give any numeric score — this post is the first to attach concrete numbers to the capability jump those posts discussed only in hedged, qualitative terms ("significant advancements," "may have a critical level of cyber capability"). This is high-value corroborating context: it shows Astra's actual measured security-benchmark performance is consistent with the concern OpenAI's own safety team raised about it a month before launch.

### Claim 9: On OpenAI's "eight-needle" long-context benchmark, GPT‑6 Astra scored 100% at 256K–512K tokens and 96.3% at 512K–1M tokens
- **Evidence**: Direct benchmark figures, cited by Willison, presumably from OpenAI's own model documentation.
- **Confidence**: emerging (specific, quantified, named-benchmark figures, but vendor-sourced and not independently reproduced in this post)
- **Quote**: "on OpenAI's eight-needle benchmark it got 100% at 256K–512K tokens and 96.3% at 512K–1M tokens."
- **Our assessment**: A near-ceiling score at up to 1M tokens on a needle-in-haystack-style test is a meaningful long-context retrieval data point, though "eight-needle" retrieval tests measure findability of inserted facts, not necessarily reasoning-quality preservation across long context (a distinction already raised in this corpus by `blog-humanlayer-long-context-isnt-the-answer.md` and the "context rot" framing in `blog-anthropic-session-management-1m-context.md` Claim 1). The post does not state Astra's maximum context window size directly, so this benchmark's upper bound (1M tokens) should not be read as a confirmed context-window-size claim — only as a performance data point within whatever window Astra supports.

### Claim 10: Willison states he had not personally tried Astra at the time of writing, and characterizes the model's overall performance as not universally superior — trailing Claude Fable 5.1 on general intelligence despite strengths elsewhere
- **Evidence**: Willison's own direct disclaimers, opening and closing the post.
- **Confidence**: anecdotal (editorial framing/disclaimer, not a benchmark claim)
- **Quote**: "I've not tried it yet myself, so I don't have a great deal to say about it yet." … "It doesn't win at everything though."
- **Our assessment**: This self-disclaimer is important for calibrating the whole post's evidentiary weight: every benchmark and pricing figure in this note (Claims 3-9) is secondhand vendor/Artificial-Analysis data curated by Willison, not first-person practitioner testing — a materially different evidentiary basis than `blog-simonwillison-claude-fable-5.md`, where Willison ran Fable 5 directly for ~5.5 hours and reported his own experience. Treat this entire source as "day-one launch digest," not "hands-on review," and expect a possible follow-up post once Willison gains direct access.

## Concrete Artifacts

```
Source: Simon Willison, "GPT-6 Astra,"
https://simonwillison.net/2026/Sep/3/gpt6-astra/ (published Sept 3, 2026,
8:18pm)

API identity and pricing:
  Model label (API):     gpt-6-astra
  Input price:           $10 / million tokens
  Output price:          $50 / million tokens
  (identical to Claude Fable 5 / 5.1 pricing)

Artificial Analysis benchmark comparison (GPT-6 Astra vs. GPT-5.6 Sol vs.
Claude Fable 5.1):
  Intelligence Index:       Astra 61  |  Sol 61 (equal)  |  Fable 5.1: 66 (61+5)
  Coding Agent Index (max): Astra ≈ Sol(max) cost, Astra +2 points vs. Sol
                            Astra: <50% of Fable 5's per-task cost, same score

ARC-AGI-3 (per ARC-AGI blog, arcprize.org):
  Provider Adapter harness (custom, opaque reasoning state + compaction):
      99.9% — cost $19K
  Default ARC-AGI harness:
      62.7% — cost $26K

Security benchmarks (Astra vs. GPT-5.6 Sol):
  ExploitBench:                        100%   (Sol: 78.5%)
  ExploitGym:                          42.4%  (Sol: 30.3%)
  SRE-Bench (binary reverse eng.,
    within 4 attempts):                99.2%  (Sol: 68.7%)

Long-context ("eight-needle" benchmark, OpenAI):
  256K–512K tokens:   100%
  512K–1M tokens:      96.3%
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-claude-fable-5.md`, `blog-simonwillison-gpt56-sol-launch.md`,
`blog-simonwillison-gemini35-flash-pricing.md`,
`blog-openai-arc-agi-3-two-settings.md`,
`blog-openai-astra-critical-cyber-capabilities.md`, and
`blog-openai-pacing-model-development-cyber-capabilities.md` were each
re-read in full before writing this section, and every `Claim N` cited
below was located and confirmed by number and content against that note's
own text before use, per MINER.md §4b.

- **Corroborates**:
  - `blog-openai-arc-agi-3-two-settings.md` Claims 2, 4-8 (retained
    reasoning + compaction tripled GPT‑5.6 Sol's ARC-AGI-3 score and cut
    output tokens 6x): this post's Claim 7 (Astra's "Provider Adapter
    harness" — explicitly described as preserving "opaque reasoning state
    between requests" and using "compaction for longer conversations" —
    scoring 99.9% vs. 62.7% for the default harness) is a second,
    independent data point for the identical underlying mechanism on a
    newer model. Both sources agree: ARC-AGI-3 scores are dominated by
    whether reasoning state and compaction are enabled, not by the
    underlying model alone.
  - `blog-openai-astra-critical-cyber-capabilities.md` Claim 1 ("significant
    advancements in agentic coding and cybersecurity," leading OpenAI to
    conclude on Aug 7, 2026 it "cannot rule out critical cyber
    capabilities" for Astra) and Claim 4 (GPT‑5.6‑Sol assessed at "High,"
    not "Critical," cyber-capability tier): this post's Claim 8 (Astra's
    ExploitBench/ExploitGym/SRE-Bench scores well above Sol's) supplies the
    first quantified, named-benchmark evidence in this corpus of the
    capability jump those two hedged, qualitative disclosures described a
    month before launch. This is a direct, dated continuity: the model
    OpenAI's safety team flagged as possibly Critical-tier on Aug 7 is the
    same model now shipping (Sept 3) with measured security-benchmark
    scores well above its immediate predecessor.
  - `blog-simonwillison-claude-fable-5.md` Concrete Artifacts (Fable 5
    priced at $10/$50 per million tokens): this post's Claim 3 corroborates
    that figure as still current for both Fable 5 and 5.1, and establishes
    Astra at the same price point.

- **Contradicts**: None identified rising to the MINER.md §4a filing bar.
  One point of internal tension within this same post is worth flagging
  rather than silently resolving: Claim 5's cost-efficiency framing
  ("Astra is less than half the cost of Claude Fable 5, for the same
  [Coding Agent Index] score") sits alongside Claim 6's citation of
  Artificial Analysis's own view that "Astra is still beaten by Fable"
  overall, and Claim 4's Intelligence Index result showing Fable 5.1 five
  points ahead of Astra. These are not contradictory — they measure
  different things (per-task coding-agent cost-efficiency vs. general
  intelligence vs. an aggregator's overall characterization) — but a
  guide passage citing only the favorable Coding Agent Index figure
  without this context would overstate Astra's competitive position
  relative to Fable. No contradiction issue filed; this is a
  conditioning-variable case (MINER.md §4a "When NOT to file"), not a
  genuine contradiction.

- **Extends**:
  - `blog-simonwillison-gpt56-sol-launch.md` Concrete Artifacts (GPT‑5.6
    Sol priced at $5/$30 per million tokens): this post's Claim 3 extends
    that pricing table forward one generation, showing OpenAI's true
    flagship (Astra) jumping 2x over Sol's price to land exactly at Fable's
    rate — a reversal of the "flat flagship pricing" pattern that note
    documented for Sol itself.
  - `blog-openai-arc-agi-3-two-settings.md`: extends that note's
    Sol-specific case study to a second model (Astra) and a different,
    even more extreme score/cost profile, while confirming the same
    reasoning-retention-plus-compaction mechanism is the operative variable.
  - `blog-openai-astra-critical-cyber-capabilities.md` and
    `blog-openai-pacing-model-development-cyber-capabilities.md`: extends
    both hedged, pre-launch OpenAI safety disclosures about Astra's
    cyber-capability concerns with the first concrete, named-benchmark
    numbers for the model's actual security-task performance, now that it
    has shipped.

- **Novel**:
  - First corpus documentation of a GPT-series model launching at exact
    price parity with Anthropic's flagship model rather than under- or
    over-cutting it.
  - First corpus documentation of the "eight-needle" long-context benchmark
    and its specific 256K–512K / 512K–1M token performance bands.
  - First corpus documentation of the ExploitBench, ExploitGym, and
    SRE-Bench (binary reverse engineering) benchmark names and any
    numeric score on them.
  - First corpus source to report a benchmark configuration (Astra's
    "Provider Adapter harness") scoring dramatically higher *and* costing
    less than the default configuration on the same benchmark, rather than
    the more typical higher-score-for-higher-cost tradeoff.

## Guide Impact

- **Chapter 02/03 (Model Selection — Cost Economics)**: Add Astra to the
  frontier pricing table at $10/$50 per million tokens (Claim 3), noting it
  now matches Fable 5/5.1 exactly rather than sitting above or below it.
  Add the per-task vs. per-token cost distinction from Claim 5 as a
  practitioner caution: identical per-token pricing between two models does
  not imply identical real-world task cost — Astra's claimed sub-half-cost
  Coding Agent Index result versus Fable 5 is a per-task, not per-token,
  comparison, and should be flagged as vendor/third-party-sourced and not
  independently verified pending direct practitioner testing.

- **Chapter 02/03 (Model Selection — Benchmark Interpretation)**: Add
  Claim 7 (ARC-AGI-3: 99.9% custom harness vs. 62.7% default harness) with
  the same harness-dependency caveat `blog-openai-arc-agi-3-two-settings.md`
  already establishes for GPT‑5.6 Sol's ARC-AGI-3 number — any guide
  citation of "Astra scores 99.9% on ARC-AGI-3" must carry the "under a
  custom harness with retained reasoning and compaction enabled" caveat.
  This is now a two-model-generation pattern (Sol and Astra), strengthening
  the general "no single benchmark score is model-only" guidance to a
  recurring, name-checkable phenomenon rather than a one-off.

- **Chapter on Security & Threat Model**: Add Claim 8's ExploitBench (100%
  vs. Sol 78.5%), ExploitGym (42.4% vs. Sol 30.3%), and SRE-Bench reverse
  engineering (99.2% vs. Sol 68.7%) figures as the first quantified,
  named-benchmark evidence connecting to the qualitative Aug 7/Aug 18
  OpenAI safety disclosures about Astra's possible Critical-tier cyber
  capability (`blog-openai-astra-critical-cyber-capabilities.md`,
  `blog-openai-pacing-model-development-cyber-capabilities.md`). Any guide
  passage discussing Astra's security capability should cite both the
  benchmark magnitude (this post) and the hedged capability-tier
  disclosure (those posts) together, since neither alone gives the full
  picture — one has numbers but no tier classification, the other has a
  tier concern but no benchmark numbers.

- **Do not cite this post as a hands-on capability assessment**: per
  Claim 10, Willison explicitly had not used Astra at the time of writing.
  Every figure in this note is vendor- or Artificial-Analysis-sourced, not
  independently reproduced. Guide citations should attribute figures to
  "OpenAI/Artificial Analysis data reported via Willison," not to
  Willison's own testing, and should flag Claims 4-9 as `emerging`
  pending independent reproduction.

## Extraction Notes

- **Fetch method**: The `WebFetch` tool refused to reproduce the post's
  full text verbatim, citing a copyright-related instruction conflict with
  a length constraint. Instead, the post was read via multiple independent,
  narrowly-targeted `WebFetch` prompts (six total), each asking for a
  specific short (under ~150 character) verbatim quote from a specific
  section (opening/rollout, pricing, model label, Intelligence Index,
  Coding Agent Index, ARC-AGI-3, security benchmarks, long-context, closing
  disclaimer). Every quote used in this note appeared identically (or as an
  identical substring) across at least two independent fetch calls before
  being included, as a substitute for the direct programmatic
  substring-verification used in other recent notes in this corpus (e.g.
  `blog-openai-pacing-model-development-cyber-capabilities.md`). No quote
  in this note is drawn from only a single, unverified fetch.
- **No sub-pages followed**: the post links to an Artificial Analysis
  tweet (a social-media embed, summarized rather than independently
  fetched — see Claim 6) and to the ARC-AGI blog's Astra post at
  arcprize.org/blog/astra (cited by Willison for the ARC-AGI-3 figures in
  Claim 7; not independently fetched by this Miner — the figures are taken
  from Willison's citation of it, consistent with how this post itself
  presents the data). A future Miner pass on arcprize.org/blog/astra
  directly could independently verify and likely extend Claim 7 with
  methodology detail, similar to how `blog-openai-arc-agi-3-two-settings.md`
  used the ARC-AGI-3 scoring-methodology docs as a secondary source.
  Neither sub-page was substantive prose beyond what Willison already
  quoted/paraphrased, given the tight time-boxed nature of this same-day
  launch-reaction post.
- **Source is a short, same-day reaction post, not a deep-dive**: at
  roughly 300-400 words (estimated from the fetched summaries), this is
  one of the thinnest Willison posts in the corpus, consistent with
  Willison's own framing that he had not yet tried the model (Claim 10).
  Ten claims were extracted from a genuinely short source by treating each
  distinct benchmark/pricing figure as its own claim; several are
  necessarily `emerging` rather than `settled` because they rest on
  vendor or third-party (Artificial Analysis, ARC Prize) data Willison
  himself did not independently verify.
- **Overall confidence rated `emerging`**: the post is from a highly
  credible curator (Willison) but is explicitly not a first-person
  evaluation, and every quantified claim is one or two removes from direct
  observation (OpenAI's own announcement, or Artificial Analysis's/ARC
  Prize's third-party benchmarking, as relayed by Willison). No claim here
  has been independently reproduced by this Miner or by Willison himself
  at time of writing.
- **No contradiction meeting the MINER.md §4a filing bar was identified.**
  The one internal tension noted (Claim 5's favorable per-task cost framing
  vs. Claim 6's "still beaten by Fable" framing vs. Claim 4's Intelligence
  Index gap) is a conditioning-variable case, not a genuine contradiction,
  and is documented under Cross-References → Contradicts per MINER.md's
  instruction to surface tensions even when not formally filed.
- **Three duplicate Prospector triage comments** were posted to the source
  issue (all on 2026-09-07, within seconds of each other), recommending
  overlapping but not identical chapter targets: the first named Ch02/Ch04,
  the second named Ch02/Ch04/Ch06, and the third named Ch02 only (framed as
  "Harness Engineering — model selection context"). This note's Guide
  Impact section targets Model Selection (Cost Economics and Benchmark
  Interpretation) as the strongest, most specific match across all three
  comments, and adds a Security & Threat Model recommendation given the
  direct, dated continuity with this corpus's existing Astra
  safety-disclosure notes — a connection none of the three triage comments
  identified, since none referenced the existing
  `blog-openai-astra-critical-cyber-capabilities.md` note.
