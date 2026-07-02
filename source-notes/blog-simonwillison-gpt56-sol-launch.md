---
source_url: https://simonwillison.net/2026/Jun/26/openai/
source_type: blog-post
title: "A quote from OpenAI"
author: Simon Willison (quoting OpenAI)
date_published: 2026-06-26
date_extracted: 2026-07-02
last_checked: 2026-07-02
status: current
confidence_overall: emerging
issue: "#1427"
---

# A quote from OpenAI (GPT-5.6 Sol/Terra/Luna launch)

> Simon Willison's link-blog quote of OpenAI's official announcement previewing the GPT-5.6 series — a three-tier lineup (Sol/Terra/Luna) with Terra pitched as GPT-5.5-competitive at half the price, plus prompt-caching changes (explicit cache breakpoints, 30-minute minimum cache life, 1.25x write / 90%-discount read pricing) and a limited preview gated by U.S. government notification.

## Source Context

- **Type**: blog-post (Willison "quote" format — a single blockquote of external
  text with no first-person commentary, one of his short-form link-blog post
  types distinct from his usual "notes" posts)
- **Author credibility**: Simon Willison is the creator of Django and the `llm`
  CLI, and one of the most widely-cited practitioner commentators on LLM
  tooling. In this post specifically, Willison adds no editorial interpretation
  of his own — he curates and quotes OpenAI's official announcement text
  verbatim. The credibility of the underlying claims therefore rests on OpenAI
  as the primary source (via Willison's curation as a trusted filter for what's
  worth reading), not on Willison's own analysis. This is a lower-analysis-value
  post than his usual "notes" format (compare `blog-simonwillison-gpt55-codex-plugin.md`
  or `blog-simonwillison-gemini35-flash-pricing.md`, both of which include his
  own editorial synthesis).
- **Scope**: Covers OpenAI's announcement of the GPT-5.6 series (Sol, Terra,
  Luna): model positioning, per-token pricing for all three tiers, prompt
  caching mechanics, and preview/rollout timeline. Does NOT cover independent
  benchmark results, context window size, knowledge cutoff, or any capability
  comparison beyond OpenAI's own "competitive with GPT-5.5" framing. There is
  no independent (non-OpenAI) verification of the performance claims in this
  post — everything is OpenAI's own marketing language.

## Extracted Claims

### Claim 1: OpenAI previewed a three-tier GPT-5.6 series — Sol (flagship), Terra (balanced/everyday), and Luna (fast/affordable)
- **Evidence**: OpenAI's official announcement, quoted by Willison, titled
  "Previewing GPT‑5.6 Sol: a next-generation model," published at
  openai.com/index/previewing-gpt-5-6-sol/.
- **Confidence**: settled (official vendor announcement of product naming and
  tiering; not independently verified but not a claim requiring third-party
  verification — it's a naming/positioning fact)
- **Quote**: "Terra has competitive performance to GPT‑5.5 while being 2x
  cheaper and Luna brings strong capability at our lowest cost."
- **Our assessment**: This is the third distinct three-tier model launch
  pattern in the corpus (following Gemini 3.5 Flash's tiering documented in
  `blog-simonwillison-gemini35-flash-pricing.md`, and the existing GPT-5.5/5.5
  Pro/5.4 spread in `blog-simonwillison-gpt55-codex-plugin.md`). Three-tier
  (flagship/balanced/economy) product structuring is now the dominant lineup
  shape across OpenAI and Google, not a one-off decision by either vendor.

### Claim 2: GPT-5.6 Sol is priced at $5/$30 per million input/output tokens — identical to GPT-5.5's current pricing
- **Evidence**: OpenAI's published per-tier pricing table, quoted in the post.
- **Confidence**: settled (published pricing at time of post; subject to
  change)
- **Quote**: (no direct quote of the pricing table rows; see paraphrase — the
  post presents Sol at $5 input / $30 output per million tokens)
- **Our assessment**: Sol's price is flat versus GPT-5.5 ($5/$30, per
  `blog-simonwillison-gpt55-codex-plugin.md` Claim 4/Concrete Artifacts) rather
  than another price hike. This breaks the pattern documented in
  `blog-simonwillison-gemini35-flash-pricing.md` Claim 5 of successive
  flagship-tier price increases (GPT-5.5 was 2x GPT-5.4; Opus 4.7 was ~1.46x
  Opus 4.6; Gemini 3.5 Flash was 3-6x its predecessors). OpenAI appears to be
  holding the flagship price point flat this generation and differentiating
  instead via the new Terra/Luna tiers below it — see Claim 3.

### Claim 3: Terra is positioned as matching GPT-5.5 performance at half the price ($2.50/$15 vs. GPT-5.5's $5/$30 per million tokens)
- **Evidence**: OpenAI's own claim, quoted directly by Willison.
- **Confidence**: emerging (this is OpenAI's own performance-parity claim in
  marketing copy, not an independently verified benchmark result — treat the
  "competitive performance" framing as vendor positioning until third-party
  benchmarks corroborate it)
- **Quote**: "Terra has competitive performance to GPT‑5.5 while being 2x
  cheaper and Luna brings strong capability at our lowest cost."
- **Our assessment**: If this claim holds up under independent benchmarking,
  it is a meaningful cost-optimization data point for practitioners currently
  budgeting for GPT-5.5: a same-capability, half-price substitute becomes
  available. This directly counters the "labs are raising flagship prices
  every generation" trend synthesized in
  `blog-simonwillison-gemini35-flash-pricing.md` Claim 5-6 — rather than
  raising the top price, OpenAI is undercutting its own prior-generation
  flagship with a new mid-tier. Practitioners should treat the parity claim
  as unverified until an independent benchmark (e.g., Artificial Analysis,
  as used in the Gemini 3.5 Flash note) confirms it.

### Claim 4: Luna is priced at $1/$6 per million input/output tokens as OpenAI's lowest-cost GPT-5.6-generation tier
- **Evidence**: OpenAI's published pricing, quoted in the post.
- **Confidence**: settled (published pricing at time of post)
- **Quote**: "Luna brings strong capability at our lowest cost."
- **Our assessment**: At $1/$6, Luna sits below GPT-5.4's $2.5/$15 (the
  previous generation's cheaper tier, per
  `blog-simonwillison-gpt55-codex-plugin.md` Concrete Artifacts). This is the
  first corpus evidence of OpenAI pricing a current-generation model tier
  below the *previous* generation's cheap tier, rather than only adding
  expensive tiers above. Worth tracking alongside the Gemini 3.5 Flash
  counter-example, where Google's "budget" Flash tier got 3-6x *more*
  expensive per `blog-simonwillison-gemini35-flash-pricing.md` Claim 2.

### Claim 5: GPT-5.6 introduces explicit prompt-cache breakpoints and a 30-minute minimum cache life, described as making caching "more predictable"
- **Evidence**: OpenAI's own feature description, quoted directly.
- **Confidence**: settled (announced product feature; mechanics not yet
  independently exercised by any corpus source)
- **Quote**: "GPT‑5.6 also introduces more predictable prompt caching,
  including support for explicit cache breakpoints and a 30-minute minimum
  cache life."
- **Our assessment**: "Explicit cache breakpoints" — the caller marks specific
  points in the prompt where the cache boundary should sit, rather than relying
  purely on longest-common-prefix matching — is a caching control primitive not
  documented elsewhere in the corpus for OpenAI's API. Anthropic's caching
  model (documented in `blog-anthropic-prompt-caching-everything.md`) is
  prefix-match based with no mention of explicit breakpoints; if OpenAI's
  breakpoint mechanism is genuinely a different (more controllable) caching
  primitive, it's worth flagging as a cross-vendor caching-API divergence
  practitioners building multi-provider harnesses should account for. The
  30-minute minimum cache life is a concrete, checkable number once the API
  is generally available.

### Claim 6: GPT-5.6 cache writes cost 1.25x the uncached input rate; cached reads receive a 90% discount
- **Evidence**: OpenAI's published cache pricing multipliers, quoted in the
  post.
- **Confidence**: settled (published pricing at time of post)
- **Quote**: Cache writes are billed at 1.25x the uncached input rate, while
  reads receive a "90% cached-input discount." (the "90% cached-input
  discount" fragment is verbatim; the 1.25x write-rate figure is reported
  numerically in the source without a standalone quotable sentence)
- **Our assessment**: A 90% read discount on cache hits is consistent with
  Anthropic's own cache-read economics in spirit (large discount on hits), but
  this is the first corpus source to name OpenAI's specific write/read
  multipliers. The 1.25x write surcharge is a cost practitioners must model
  explicitly when deciding whether to place volatile content ahead of a cache
  breakpoint — writing to a fresh cache segment costs more than a plain
  uncached call, so cache breakpoints only pay off if that segment is read
  from cache more than once.

### Claim 7: OpenAI began limited preview access with trusted partners following U.S. government notification, ahead of a broader rollout planned "in the coming weeks"
- **Evidence**: OpenAI's rollout description, quoted in the post.
- **Confidence**: emerging (rollout timelines in vendor announcements are
  frequently revised; "coming weeks" is not a committed date)
- **Quote**: These would become "generally available in the coming weeks"
  following an initial limited preview with government-approved partners.
- **Our assessment**: A pre-notification-to-government step ahead of frontier
  model preview access is consistent with OpenAI's established pattern for
  major model launches (compliance-first staged rollout). This is a process
  detail, not a technical capability — worth noting for practitioners tracking
  "when will I actually be able to use this" timelines, but not something to
  build technical guidance around.

## Concrete Artifacts

### GPT-5.6 series pricing (per 1M tokens, as announced June 26, 2026)
```
Model    Role                    Input      Output
Sol      Flagship                $5.00      $30.00
Terra    Balanced/everyday       $2.50      $15.00
Luna     Fast/affordable         $1.00      $6.00

Comparison to prior generation (per blog-simonwillison-gpt55-codex-plugin.md):
  GPT-5.5      $5.00 / $30.00   (Sol matches this exactly)
  GPT-5.5 Pro  $30.00 / $180.00
  GPT-5.4      $2.50 / $15.00   (Terra matches this exactly; claimed
                                  GPT-5.5-competitive performance at this price)

Source: OpenAI announcement, quoted by Simon Willison,
simonwillison.net/2026/Jun/26/openai/, June 26, 2026
```

### GPT-5.6 prompt caching mechanics
```
- Explicit cache breakpoints (caller-controlled cache boundary, not just
  longest-prefix match)
- 30-minute minimum cache life
- Cache write: 1.25x the uncached input rate
- Cache read (hit): 90% discount vs. uncached input rate

Source: OpenAI announcement, quoted by Simon Willison,
simonwillison.net/2026/Jun/26/openai/, June 26, 2026
```

### Rollout timeline
```
Phase 1: Limited preview, trusted partners only, following U.S. government
         notification
Phase 2: General availability "in the coming weeks" (as of June 26, 2026)

Source: OpenAI announcement, quoted by Simon Willison,
simonwillison.net/2026/Jun/26/openai/, June 26, 2026
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 1 (Gemini 3.5 Flash's
    three-tier structure) and Concrete Artifacts (Cross-Vendor Price
    Escalation Table): GPT-5.6's Sol/Terra/Luna split is a third data point for
    the "flagship/balanced/economy" tiering pattern now common across OpenAI
    and Google. Unlike the Gemini 3.5 Flash launch, however, GPT-5.6 does not
    fit the "every tier gets more expensive" trend that note documented —
    see Contradicts below.
  - `blog-anthropic-prompt-caching-everything.md` Claim 1 (caching as a
    foundational cost/latency mechanism for agentic products): OpenAI's
    investment in "more predictable prompt caching" for GPT-5.6 corroborates
    that prompt caching is now considered core infrastructure by every major
    lab, not an Anthropic-specific optimization.

- **Contradicts**: `blog-simonwillison-gemini35-flash-pricing.md` Claim 5-6
  (the "all three major labs are simultaneously raising flagship prices /
  probing price tolerance" thesis, based on GPT-5.5 at 2x GPT-5.4, Opus 4.7 at
  ~1.46x Opus 4.6, and Gemini 3.5 Flash at 3-6x its predecessors). GPT-5.6 Sol
  holds flagship pricing flat at $5/$30 (identical to GPT-5.5, not a further
  increase), and Terra is explicitly positioned as GPT-5.5-equivalent
  performance at half price — a price *decrease* for GPT-5.5-class capability,
  not an increase. This is a single vendor's next-generation pricing move
  against a two-source trend claim (Willison's own synthesis plus corroborating
  Batch commentary), and OpenAI's Terra "competitive performance" claim is
  unverified vendor marketing rather than independent benchmark data — it may
  not hold up, or "competitive" may understate a real quality gap versus
  GPT-5.5. **Filed as contradiction issue #1448** per MINER.md §4a — see that
  issue for the full Side A/Side B writeup. Verdict pending human/Smith
  resolution; do not treat either framing as settled until CONTRADICTIONS.md
  has a C-NNN entry for it.

- **Extends**:
  - `blog-simonwillison-gpt55-codex-plugin.md` Claim 4 (GPT-5.5/5.5 Pro/5.4
    pricing table): this note directly extends that pricing table with the
    next model generation, and shows Sol/Terra land at exactly the prior
    GPT-5.5/GPT-5.4 price points, while Luna undercuts even GPT-5.4.
  - `blog-anthropic-prompt-caching-everything.md` (prefix-based cache
    architecture and cost mechanics for Claude Code): this note adds the
    first corpus documentation of OpenAI's specific cache pricing multipliers
    (1.25x write, 90% read discount) and an explicit-breakpoint control
    primitive, which the Anthropic note does not describe for Claude's API.

- **Novel**:
  - First corpus documentation of a frontier lab holding flagship pricing flat
    generation-over-generation while positioning a *cheaper* mid-tier as the
    prior flagship's performance equivalent, rather than raising prices at
    every tier.
  - First corpus documentation of OpenAI's specific prompt-cache write/read
    pricing multipliers (1.25x write, 90% read discount) and an
    explicit-cache-breakpoint control primitive.
  - First corpus mention of a frontier-model preview gated by U.S. government
    pre-notification as an explicit rollout phase (distinct from general
    "compliance-first" characterizations in other notes).

## Guide Impact

- **Chapter 03 (Model Selection — Cost Economics)**: Add GPT-5.6 Sol/Terra/Luna
  pricing to any per-vendor pricing table alongside the existing GPT-5.5/5.4
  and Gemini 3.5 Flash data. Specifically flag Terra's claimed
  GPT-5.5-equivalent-performance-at-half-price positioning as a cost
  optimization opportunity worth practitioner verification once independent
  benchmarks exist — do not present the "competitive performance" claim as
  settled fact, since it is OpenAI's own marketing language.

- **Chapter 03 (Model Selection — Market Dynamics)**: This source complicates
  the "labs are simultaneously raising flagship prices" narrative sourced from
  `blog-simonwillison-gemini35-flash-pricing.md`. See contradiction issue
  #1448 (filed alongside this note) for the full Side A/Side B analysis; once
  resolved, update Ch03 guidance to reflect the CONTRADICTIONS.md verdict
  rather than asserting either framing as settled in the interim.

- **Chapter 05 (Prompt Engineering — Caching)**: Add OpenAI's explicit
  cache-breakpoint primitive and 30-minute minimum cache life as a
  cross-vendor caching mechanics comparison point alongside the Anthropic
  prefix-cache model in `blog-anthropic-prompt-caching-everything.md`. Add the
  1.25x write / 90% read-discount multipliers as a concrete cost model for
  practitioners deciding where to place cache breakpoints in OpenAI-backed
  harnesses: a cache segment must be read from cache more than roughly once
  to amortize the 1.25x write surcharge.

## Extraction Notes

- **Source format is a bare quote, not a notes post**: Unlike most
  Willison sources in this corpus, this post is his "quotation" link-blog
  format — a single blockquote of OpenAI's announcement with no independent
  Willison commentary. All analytical claims in this note about what the
  pricing/caching changes *mean* are Miner-derived (cross-referenced against
  existing corpus notes), not Willison's own editorial synthesis. This
  lowers the "authoritative practitioner interpretation" weight relative to
  `blog-simonwillison-gemini35-flash-pricing.md`, which does include
  Willison's own analysis.
- **Primary source (openai.com) was unreachable**: A direct fetch of
  `openai.com/index/previewing-gpt-5-6-sol/` returned HTTP 403. All claims
  are sourced through Willison's quotation of that page rather than the
  original OpenAI announcement directly. If the Assayer can reach the OpenAI
  page directly, it should be spot-checked against the quotes reproduced
  here.
- **Three duplicate Prospector triage comments**: as with the companion
  GPT-5.5 note, three separate triage comments were posted to the issue by
  automated re-runs. All three agree on novelty (medium/medium-high/high) and
  relevant chapters (model selection, cost, caching); none flagged a
  disqualifying overlap. I treated the third (most detailed) comment as
  authoritative for chapter targeting.
- **No independent, non-OpenAI verification of Terra's performance-parity
  claim exists in this source or elsewhere in the corpus.** This is flagged
  explicitly in Claim 3 and the Contradicts section rather than silently
  accepted, per MINER.md's emphasis on not letting vendor marketing pass as
  settled evidence.
- **Contradiction filed**: This note's pricing data materially opposes the
  "labs are simultaneously raising flagship prices" trend claim in
  `blog-simonwillison-gemini35-flash-pricing.md` Claim 5-6. Per MINER.md §4a,
  filed contradiction issue #1448 before opening this PR rather than picking
  a verdict in the note itself.
- **No sub-pages followed**: the post is a single blockquote with no
  additional Willison-authored links beyond the OpenAI announcement itself,
  which was unreachable (see above).
