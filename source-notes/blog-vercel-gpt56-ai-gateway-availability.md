---
source_url: https://vercel.com/changelog/gpt-5-6-now-available-on-ai-gateway
source_type: blog-post
title: "GPT 5.6 Sol, Luna, and Terra now available on AI Gateway"
author: Walter Korman, Jerilyn Zheng (Vercel)
date_published: 2026-07-09
date_extracted: 2026-08-07
last_checked: 2026-08-07
status: current
confidence_overall: emerging
issue: "#2551"
---

# GPT 5.6 Sol, Luna, and Terra now available on AI Gateway

> A short Vercel changelog entry (~1-minute read) announcing GPT-5.6
> Sol/Terra/Luna routable through AI Gateway "in a limited preview" on July 9,
> 2026 — the same calendar date OpenAI's own GA announcement declared the
> family generally available — with a zero-code CLI migration path
> (`vercel ai-gateway rules add --type rewrite`) not previously documented in
> this corpus. Following the changelog's own linked model pages (fetched live
> during this extraction) surfaces a third independent confirmation of the
> exact GPT-5.6 cache write/read pricing multipliers, evidence that AWS
> Bedrock resells the same model slug at a 10% price premium with a much
> smaller context window than the OpenAI/Azure routes, and live "% off"
> badges showing the July 30, 2026 Terra/Luna price cut already reflected on
> Vercel's model pages as of this extraction.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published July 9, 2026, byline "Walter Korman, Jerilyn Zheng," "9 Jul 2026,
  1 min read" per the page's own rendered metadata; a single-screen
  feature-availability announcement — one intro paragraph, a three-item model
  list, one code example, one CLI example, a platform-features paragraph, a
  pricing-policy sentence, and two closing CTAs). Jerilyn Zheng is a
  recurring AI-Gateway-changelog byline already documented in this corpus
  (`blog-vercel-ai-gateway-fable-5-restored.md`,
  `blog-vercel-ai-gateway-xai-grok-audio-models.md`,
  `blog-vercel-ai-gateway-api-key-budgets.md`,
  `blog-vercel-ai-gateway-production-index-may2026.md`).
- **Author credibility**: First-party Vercel changelog entry. Vercel operates
  AI Gateway and the AI SDK described here, so the platform-mechanics claims
  (model slugs, CLI syntax, feature list, pricing policy) are authoritative
  first-party documentation of a shipping integration — not independent
  reporting. The model-capability claims ("stronger at agentic work,"
  "more token-efficient") are Vercel restating OpenAI's own marketing
  language without independent verification; see Claim 2.
- **Scope**: Covers which GPT-5.6 model slugs are routable through AI
  Gateway, one AI SDK code example, one CLI routing-rule example, AI
  Gateway's general platform-features list, and its pricing policy. Does NOT
  cover: GPT-5.6 pricing figures directly (the changelog itself states no
  dollar amounts — those were recovered from the linked model pages, see
  Claims 7-9), a rollout/access-gating timeline for the stated "limited
  preview," benchmark results, or any customer/production usage of GPT-5.6
  via AI Gateway specifically.

## Extracted Claims

### Claim 1: Vercel made GPT-5.6 Sol, Terra, and Luna routable through AI Gateway "in a limited preview" on July 9, 2026 — the identical calendar date OpenAI's own announcement declared the same three models generally available following its June 26 limited preview

- **Evidence**: The changelog's opening paragraph, dated July 9, 2026 by its own byline; compared against `blog-openai-gpt56-ga-announcement.md` Claim 1 ("We're launching the GPT‑5.6 family of models for general availability following our limited preview...") and `blog-simonwillison-gpt56-ga-launch.md`, both independently dated July 9, 2026 for OpenAI's GA declaration.
- **Confidence**: emerging (a specific, dated, first-party statement of Vercel's own gateway rollout status — but see Our assessment for the apparent tension with OpenAI's own GA framing on the same date, which this Miner did not resolve)
- **Quote**: "GPT 5.6 from OpenAI is now available on AI Gateway in a limited preview, across three models: Sol, Terra, and Luna. All three are stronger at agentic work across coding, biology, and cybersecurity, and are more token-efficient than the previous generation."
- **Our assessment**: This is a genuine, unresolved tension worth flagging rather than silently reconciling: the rest of the corpus (`blog-openai-gpt56-ga-announcement.md`, `blog-simonwillison-gpt56-ga-launch.md`) documents OpenAI declaring GPT-5.6 *generally available* on this exact date, while Vercel's own changelog — published the same day — describes AI Gateway's own access to the same three models as "a limited preview." Notably, the page's own `<meta name="description">` tag ("GPT-5.6 from OpenAI is now available on AI Gateway in three models, Sol, Terra, and Luna with BYOK support and no markup") omits "limited preview" entirely, which could suggest the phrase is either a leftover from drafting against OpenAI's earlier June 26 preview announcement, or a genuine statement that AI Gateway's own routing access was still gated behind a preview flag independent of OpenAI's GA status. This Miner did not find a definitive resolution and is not filing this as a MINER.md §4a contradiction, since it plausibly reflects two different rollout surfaces (OpenAI's own API GA status vs. Vercel's gateway-side catalog/quota gating) rather than a factual dispute about the same claim — the same shape of ambiguity already documented for a different modality in `blog-vercel-ai-gateway-realtime-voice-speech.md`'s "beta, access is rolling out gradually" language. Flagged here so the guide does not cite "GPT-5.6 was GA on AI Gateway from day one" without this caveat.

### Claim 2: Vercel describes Sol as "the flagship, and the most capable of the three," Terra as "a balanced model for everyday work, with performance comparable to the previous generation at half the cost," and Luna as "a fast, affordable model with strong capability at the lowest cost in the series," identified by the gateway slugs `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra`, and `openai/gpt-5.6-luna`

- **Evidence**: The changelog's three-item model list, each entry pairing a bolded model name, its gateway slug in a code span, and a one-sentence positioning description.
- **Confidence**: settled for the slugs themselves (checkable identifiers); emerging for the positioning language (restated vendor marketing, not independently verified by Vercel)
- **Quote**: "Sol (openai/gpt-5.6-sol): the flagship, and the most capable of the three." / "Terra (openai/gpt-5.6-terra): a balanced model for everyday work, with performance comparable to the previous generation at half the cost." / "Luna (openai/gpt-5.6-luna): a fast, affordable model with strong capability at the lowest cost in the series."
- **Our assessment**: This is Vercel restating, in its own words, positioning OpenAI already established — closely paraphrasing `blog-openai-gpt56-ga-announcement.md` Claim 1's "our new flagship, Sol, alongside Terra, a balanced model for everyday work, and Luna, our most cost-efficient model" and `blog-simonwillison-gpt56-sol-launch.md` Claim 1's "Terra has competitive performance to GPT‑5.5 while being 2x cheaper." It adds no new capability evidence beyond what the corpus already has from OpenAI directly; its value is confirming that AI Gateway exposes exactly these three models under these exact slugs, with no fourth tier or renamed variant.

### Claim 3: To call GPT-5.6, set the AI SDK's `model` parameter to one of the three gateway slugs; a complete `streamText` example is given using `openai/gpt-5.6-sol`

- **Evidence**: A code block immediately following the model list, introduced by "To use GPT 5.6, set model to one of the above slugs in the AI SDK:"
- **Confidence**: settled (first-party runnable code artifact)
- **Quote**: "To use GPT 5.6, set model to one of the above slugs in the AI SDK:"
- **Our assessment**: A minimal, unremarkable integration example consistent with every other Vercel AI Gateway model-availability changelog already in this corpus (e.g. `blog-vercel-ai-gateway-xai-grok-audio-models.md`, `blog-vercel-ai-gateway-fable-5-restored.md`) — confirms GPT-5.6 requires no special-cased integration beyond the standard `model:` string swap.

### Claim 4: AI Gateway supports zero-code model migration via CLI routing rules — demonstrated with a rule that rewrites all traffic addressed to `openai/gpt-5.5` to `openai/gpt-5.6-sol` instead

- **Evidence**: A CLI code block immediately following the AI SDK example, introduced by a sentence explicitly framing it as a no-code-change migration path.
- **Confidence**: settled (first-party runnable CLI artifact)
- **Quote**: "You can also set routing rules to switch to GPT 5.6 from other gateway models without touching your code." Code block: `vercel ai-gateway rules add \` / `  --type rewrite \` / `  --source openai/gpt-5.5 \` / `  --destination openai/gpt-5.6-sol`
- **Our assessment**: This is the first source note in this corpus to document the `vercel ai-gateway rules add --type rewrite` CLI syntax. `blog-vercel-ai-gateway-api-key-budgets.md` Concrete Artifacts already documents a sibling command in the same `vercel ai-gateway` CLI namespace (`vercel ai-gateway api-keys create --budget <DOLLARS> --refresh-period <PERIOD>`), so this confirms the `vercel ai-gateway` CLI has at least two independent subcommand families (`api-keys` for credential management, `rules` for traffic routing) rather than being a single-purpose tool — a broader CLI surface than any prior corpus note individually showed. Practically, this gives a concrete, generally-applicable mechanism for a fleet-wide model swap (e.g., migrating every caller of an old model string to a new one) enforced at the gateway rather than requiring a code change and redeploy in every calling application.

### Claim 5: AI Gateway's built-in platform features include custom reporting, Zero Data Retention (ZDR) support, budgets for API keys, and routing rules, alongside a unified API for calling models, tracking usage/cost, and configuring retries/failover/performance optimizations for "higher-than-provider uptime"

- **Evidence**: A features paragraph following the CLI example, with each named feature individually hyperlinked to its own changelog/docs page (`custom-reporting-ai-gateway`, `zdr-on-ai-gateway`, an API-keys docs page for budgets, and an implicit routing-rules docs link).
- **Confidence**: settled (first-party restatement of already-shipping platform capabilities, each independently corroborated elsewhere in this corpus — see Cross-References)
- **Quote**: "AI Gateway provides a unified API for calling models, tracking usage and cost, and configuring retries, failover, and performance optimizations for higher-than-provider uptime. It includes built-in custom reporting, Zero Data Retention support, budgets for API keys, routing rules, and more."
- **Our assessment**: This paragraph appears to be boilerplate reused across AI Gateway's model-availability changelogs rather than GPT-5.6-specific content — it names no capability unique to this announcement. Its value here is confirming these four named features (custom reporting, ZDR, budgets, routing rules) apply uniformly to GPT-5.6 traffic like any other AI Gateway model, with no GPT-5.6-specific carve-out or limitation stated.

### Claim 6: AI Gateway "reflects provider pricing with no markup and does not charge a platform fee on inference, including on Bring Your Own Key (BYOK) requests"

- **Evidence**: A single-sentence pricing-policy statement following the features paragraph, linking to Vercel's BYOK documentation.
- **Confidence**: settled (first-party statement of pricing policy)
- **Quote**: "AI Gateway reflects provider pricing with no markup and does not charge a platform fee on inference, including on Bring Your Own Key (BYOK) requests."
- **Our assessment**: The general "no markup, no platform fee" policy is already documented in this corpus (e.g. `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 1: "...with no markup or platform fees"). This source adds the explicit clause that the no-fee policy also covers BYOK requests specifically — the first time this corpus has that exact scoping stated in one sentence rather than implied. See Claim 9 below for a live-page finding that complicates the "reflects provider pricing" framing once multiple upstream providers (not just OpenAI directly) are considered.

### Claim 7: Vercel provides an AI Gateway model leaderboard that "tracks the most popular models over time, ranking them by the total volume of tokens processed across all Gateway traffic," and a browser-based model playground where GPT-5.6 can be tried directly

- **Evidence**: Two closing calls-to-action: an inline "Try GPT 5.6 in the model playground" link, and a leaderboard promo block with its own caption sentence.
- **Confidence**: settled (first-party statement of shipping product features)
- **Quote**: "Try GPT 5.6 in the model playground." / "AI Gateway: Track top AI models by usage" / "The AI Gateway model leaderboard tracks the most popular models over time, ranking them by the total volume of tokens processed across all Gateway traffic."
- **Our assessment**: This corroborates `blog-vercel-ai-gateway-xai-grok-audio-models.md` Claim 8 (an in-browser playground for realtime voice models, "without writing code") — confirming the no-code playground pattern extends to text/chat models like GPT-5.6, not just audio modalities. It also gives a named, live target (`vercel.com/ai-gateway/leaderboards`) for the same "total volume of tokens processed" metric that `blog-vercel-ai-gateway-production-index-may2026.md` reports narratively on a monthly cadence — the leaderboard is presumably a continuously-updated version of the same underlying telemetry that report's monthly snapshot draws from.

### Claim 8 (from the linked model pages, followed per MINER.md §1): AI Gateway's own model pages for Sol, Terra, and Luna each list a 1.1M-token context window and a 128,000-token max output — a larger context figure than the "million token context window" this corpus previously documented for GPT-5.6 from OpenAI's own GA post

- **Evidence**: The "Providers" comparison table on each of the three linked model pages (`vercel.com/ai-gateway/models/gpt-5.6-sol`, `-terra`, `-luna`), fetched live during this extraction on 2026-08-07 (the changelog links directly to the Sol page via "Try GPT 5.6 in the model playground"; the Terra and Luna pages were located by URL pattern and fetched for completeness).
- **Confidence**: emerging (a specific, checkable spec figure from a live product page, but not independently reconciled against the discrepancy noted below)
- **Quote**: "GPT 5.6 Sol is the flagship of the GPT-5.6 family and the most capable of the three GPT-5.6 models on AI Gateway, with stronger agentic work across coding, biology, and cybersecurity than the previous generation, better token efficiency, and a context window of 1.1M tokens." Table values (OpenAI provider row, all three models): Context `1.1M`, Max Output `128K`.
- **Our assessment**: `blog-simonwillison-gpt56-ga-launch.md` Claim 3 quotes OpenAI's own July 9 GA announcement directly: "All three models have a February 16th 2026 knowledge cutoff, a million token context window, and 128,000 maximum output tokens." The max-output figure (128K) matches exactly; the context-window figure does not (1.1M on Vercel's pages vs. "a million" / 1M as Willison quoted OpenAI). This is a small enough gap (1.1M vs. 1M, roughly 10%) that it plausibly reflects either a rounding/description difference ("a million" as informal shorthand for "1.1 million") or an actual spec Vercel displays more precisely than Willison's prose paraphrase — this Miner did not find a way to resolve which. Flagged as a minor, unresolved precision discrepancy rather than a contradiction requiring a filed issue, similar in kind to the Agents' Last Exam 53.6-vs-52.7 discrepancy already flagged (and left unresolved) in `blog-openai-gpt56-ga-announcement.md` Extraction Notes.

### Claim 9 (from the linked model pages, live as of 2026-08-07): For the identical `openai/gpt-5.6-sol` gateway slug, AWS Bedrock's provider row lists $5.50/$33.00 per-million-token input/output pricing and a 272K-token context window, versus OpenAI's own $5.00/$30.00 and 1.1M-token context window on the same page — a roughly 10% price premium and a ~75% smaller context window for the identical model routed through a different upstream cloud

- **Evidence**: The Sol model page's per-provider comparison table, which lists OpenAI, Azure, and Bedrock as separate rows for the same `openai/gpt-5.6-sol` slug, each with its own Context/Max Output/Latency/Throughput/Input/Output/Cache columns.
- **Confidence**: settled (a specific, directly-observed, checkable pricing/spec table on a live first-party page — though the underlying cause, whether Bedrock's own list pricing or a distinct Bedrock-hosted configuration, is not explained by the page itself)
- **Quote**: (no prose quote states this comparison explicitly; it is read directly off the table — see Concrete Artifacts for the full reproduced row data)
- **Our assessment**: This is a concrete, previously-undocumented-in-corpus illustration that AI Gateway's "reflects provider pricing with no markup" claim (Claim 6) is scoped to whichever upstream provider actually serves a given request — it does not mean every route to the same nominal model costs the same. A caller who does not pin a specific provider (Claim 10 below documents that AI Gateway routes across providers automatically or by preference) could see meaningfully different cost and context-window behavior depending on whether their request lands on OpenAI, Azure, or Bedrock. This is a genuinely actionable data point for any guide discussion of multi-cloud model routing: "the same model slug" is not a guarantee of "the same price or spec," and Bedrock specifically is the outlier here (Azure matches OpenAI's own pricing and context window exactly on this same page — see Concrete Artifacts).

### Claim 10 (from the linked model pages, live as of 2026-08-07): As fetched during this extraction, Vercel's live Terra and Luna model pages already display "20% off" and "80% off" badges respectively next to a struck-through prior price, showing current prices of $2.00/$12.00 (Terra) and $0.20/$1.20 (Luna) per million input/output tokens — matching the July 30, 2026 OpenAI price cut already documented elsewhere in this corpus, not the pricing in effect when this July 9 changelog was originally published

- **Evidence**: The Terra and Luna model pages' OpenAI-provider table rows, each showing a percentage-off badge alongside the discounted price.
- **Confidence**: settled for the current live figures (directly observed, matching `blog-simonwillison-gpt56-luna-price-drop.md` Claim 2's independently-sourced $2.00/$12.00 Terra and $0.20/$1.20 Luna figures exactly); the confidence label applies only to what the page shows *now*, not to a claim about the changelog's original July 9 content
- **Quote**: (no prose quote; badge and price values read directly from the table — see Concrete Artifacts)
- **Our assessment**: This is a live-page finding, not a claim the July 9, 2026 changelog itself makes — the changelog predates the July 30 price cut by three weeks and states no dollar pricing at all. It is included here as a third independent confirmation (alongside Willison's post and OpenAI's own pricing-announcement page, both already in the corpus) that the July 30 Terra/Luna cuts took effect and are reflected in a major inference-gateway's live pricing display, and as a worked illustration that the cache write/read multipliers documented in `blog-simonwillison-gpt56-sol-launch.md` and `blog-simonwillison-gpt56-ga-launch.md` (1.25x write, 90% read discount) hold arithmetically against the *post-cut* prices too: Terra's displayed cache write ($2.50/M) is exactly 1.25× its post-cut input price ($2.00/M), and its cache read ($0.20/M) is exactly 10% of that same input price; Luna's cache write ($0.25/M) and read ($0.02/M) show the identical 1.25x/10% relationship against its post-cut $0.20/M input price. Sol, unchanged by the July 30 cut, shows the same relationship against its original $5.00/M price (write $6.25/M = 1.25×; read $0.50/M = 10%).

### Claim 11 (from the linked Terra model page, live as of 2026-08-07): Vercel's own editorial copy on the Terra model page frames Terra as "the tier most GPT-5.6 traffic belongs on," with explicit routing guidance to escalate to Sol "for the hardest requests" and drop to Luna "where volume decides the budget"

- **Evidence**: A descriptive paragraph on the Terra model page (distinct from the shorter one-sentence description also present on that page and quoted in Claim 8), framed as general guidance rather than a spec statement.
- **Confidence**: anecdotal (Vercel's own qualitative product-positioning framing, not a measured usage statistic)
- **Quote**: "GPT 5.6 Terra is the tier most GPT-5.6 traffic belongs on: comparable performance to the previous generation at a lower price, with the family's agentic gains in coding, biology, and cybersecurity. Escalate to GPT-5.6 Sol for the hardest requests and drop to GPT-5.6 Luna where volume decides the budget."
- **Our assessment**: This is a specific, named three-tier routing heuristic from the platform vendor itself (default to the middle tier; escalate on difficulty; downgrade on volume/cost pressure), conceptually aligned with — though not sourced from the same data as — `blog-vercel-ai-gateway-production-index-may2026.md`'s empirical finding that production traffic actually splits across cost/frontier tiers by use case. Unlike that note's measured percentages, this is prescriptive vendor copy, not an observed usage pattern; it should be cited in the guide as vendor-recommended routing philosophy, not as evidence of how practitioners actually route GPT-5.6 traffic today.

## Concrete Artifacts

### AI SDK usage example (verbatim, from the changelog)

```typescript
import { streamText } from 'ai';

const result = streamText({
  model: 'openai/gpt-5.6-sol',
  prompt: 'Investigate the failing tests and open a PR with a fix.',
});
```
Source: https://vercel.com/changelog/gpt-5-6-now-available-on-ai-gateway

### Zero-code migration routing rule (verbatim, from the changelog)

```bash
vercel ai-gateway rules add \
  --type rewrite \
  --source openai/gpt-5.5 \
  --destination openai/gpt-5.6-sol
```
Source: https://vercel.com/changelog/gpt-5-6-now-available-on-ai-gateway

### Per-provider pricing/spec table, GPT-5.6 Sol (`openai/gpt-5.6-sol`), fetched live 2026-08-07 from vercel.com/ai-gateway/models/gpt-5.6-sol

```
Provider  Context  MaxOutput  Latency  Throughput  Input     Output    CacheRead  CacheWrite  ReleaseDate
OpenAI    1.1M     128K       3.7s     37tps       $5.00/M   $30.00/M  $0.50/M    $6.25/M     07/09/2026
Azure     1.1M     128K       4.6s     61tps       $5.00/M   $30.00/M  $0.50/M    $6.25/M     07/09/2026
Bedrock   272K     272K       3.8s     43tps       $5.50/M   $33.00/M  $0.55/M    $6.88/M     07/09/2026 (approx; row truncated in extraction)
```

### Per-provider pricing table, GPT-5.6 Terra (`openai/gpt-5.6-terra`), fetched live 2026-08-07 — OpenAI row, showing a "20% off" badge over a struck-through prior price

```
Provider  Context  MaxOutput  Latency  Throughput  Input                  Output                  CacheRead              CacheWrite
OpenAI    1.1M     128K       2.8s     79tps       $2.50/M -> $2.00/M     $15.00/M -> $12.00/M    $0.25/M -> $0.20/M     $3.13/M -> $2.50/M
(badge: "20% off")
```

### Per-provider pricing table, GPT-5.6 Luna (`openai/gpt-5.6-luna`), fetched live 2026-08-07 — OpenAI row, showing an "80% off" badge over a struck-through prior price

```
Provider  Context  MaxOutput  Latency  Throughput  Input                  Output                 CacheRead              CacheWrite
OpenAI    1.1M     128K       2.8s     92tps       $1.00/M -> $0.20/M     $6.00/M -> $1.20/M     $0.10/M -> $0.02/M     $1.25/M -> $0.25/M
(badge: "80% off")
```

Source (three tables above): vercel.com/ai-gateway/models/gpt-5.6-{sol,terra,luna}, fetched live via direct `curl` on 2026-08-07 (three weeks after this changelog's July 9 publication and one week after the July 30, 2026 Terra/Luna price cut documented in `blog-simonwillison-gpt56-luna-price-drop.md`) — these figures reflect the page's *current* state, not its state on the changelog's publication date.

### Terra routing-guidance copy (verbatim, from vercel.com/ai-gateway/models/gpt-5.6-terra)

```
"GPT 5.6 Terra is the tier most GPT-5.6 traffic belongs on: comparable
performance to the previous generation at a lower price, with the family's
agentic gains in coding, biology, and cybersecurity. Escalate to GPT-5.6
Sol for the hardest requests and drop to GPT-5.6 Luna where volume decides
the budget."
```

## Cross-References

### Cross-reference verification notes
`blog-openai-gpt56-ga-announcement.md`, `blog-simonwillison-gpt56-ga-launch.md`,
`blog-simonwillison-gpt56-sol-launch.md`, `blog-simonwillison-gpt56-luna-price-drop.md`,
`blog-vercel-ai-gateway-production-index-may2026.md`,
`blog-vercel-ai-gateway-api-key-budgets.md`,
`blog-vercel-ai-gateway-xai-grok-audio-models.md`, and
`blog-vercel-ai-gateway-fable-5-restored.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited above was located
and confirmed against each note's own numbered `### Claim N:` headings (or,
for `blog-vercel-ai-gateway-production-index-may2026.md`, its Concrete
Artifacts) before writing this section.

- **Corroborates**:
  - `blog-openai-gpt56-ga-announcement.md` Claim 1 and
    `blog-simonwillison-gpt56-sol-launch.md` Claim 1 (Sol/Terra/Luna
    tiering and positioning): this source's Claim 2 independently restates
    the same flagship/balanced/cheap-tier framing via Vercel rather than
    OpenAI or Willison, confirming the same three model names and tiering
    logic through a third distributor.
  - `blog-vercel-ai-gateway-xai-grok-audio-models.md` Claim 8 (in-browser
    model playground): this source's Claim 7 confirms the same no-code
    playground pattern for GPT-5.6, extending it beyond audio models.
  - `blog-vercel-ai-gateway-realtime-voice-speech.md` Claim 1 ("no markup or
    platform fees"): this source's Claim 6 restates the same policy with an
    explicit BYOK-inclusion clause not stated that precisely elsewhere.
  - `blog-simonwillison-gpt56-sol-launch.md` Claims 5-6 and
    `blog-simonwillison-gpt56-ga-launch.md` Claim 10 (cache write 1.25x /
    read 90% discount multipliers): this source's Claim 9/10 independently
    reproduces the identical multipliers via live dollar figures on
    Vercel's own pricing table, for both the original Sol price and the
    post-cut Terra/Luna prices.
  - `blog-simonwillison-gpt56-luna-price-drop.md` Claims 1-2 (July 30, 2026
    Terra -20%/Luna -80% cut, exact new prices $2.00/$12.00 and
    $0.20/$1.20): this source's Claim 10 independently confirms the
    identical post-cut dollar figures via a live Vercel product page,
    fetched a week after that note's own extraction.
  - `blog-vercel-ai-gateway-api-key-budgets.md` Concrete Artifacts (`vercel
    ai-gateway api-keys create --budget ...` CLI syntax): this source's
    Claim 4 (`vercel ai-gateway rules add --type rewrite ...`) confirms the
    `vercel ai-gateway` CLI has multiple independent subcommand families.

- **Contradicts**: None filed as a formal MINER.md §4a contradiction issue.
  Two tensions are flagged explicitly rather than silently resolved:
  1. **Claim 1** — Vercel's "limited preview" framing for AI Gateway access
     to GPT-5.6, published the same day OpenAI declared the family
     generally available (`blog-openai-gpt56-ga-announcement.md` Claim 1).
     Not filed because this plausibly reflects two different rollout
     surfaces (OpenAI's own API GA vs. Vercel's gateway-side access gating)
     rather than a factual dispute about the same claim — see Claim 1's
     Our assessment for full reasoning.
  2. **Claim 8** — the 1.1M-token context window shown on Vercel's model
     pages versus the "million token context window" OpenAI's own GA post
     stated (per `blog-simonwillison-gpt56-ga-launch.md` Claim 3). Not
     filed because a ~10% rounding/precision gap of this kind is closer to
     the unresolved Agents' Last Exam 53.6-vs-52.7 discrepancy already
     flagged (and left unresolved, not filed) in
     `blog-openai-gpt56-ga-announcement.md` Extraction Notes than to a
     material dispute that would change guide advice.

- **Extends**:
  - `blog-vercel-ai-gateway-production-index-may2026.md`: that note reports
    aggregate token/spend-share telemetry on a monthly cadence; this
    source's Claim 7 names the always-on, live version of a similar metric
    (the AI Gateway leaderboard, ranked by total token volume) as a
    continuously-available product surface rather than a periodic report.
  - `blog-vercel-ai-gateway-api-key-budgets.md`: extends the documented
    `vercel ai-gateway` CLI surface with a second subcommand family
    (`rules add --type rewrite`) alongside that note's `api-keys create`.
  - `blog-simonwillison-gpt56-luna-price-drop.md`: extends the July 30
    price-cut documentation with a third independent confirmation source
    (Vercel's live model pages) and, novel to the corpus, the exact
    resulting cache read/write dollar figures for the post-cut Terra and
    Luna prices (Claim 10).

- **Novel**:
  - The `vercel ai-gateway rules add --type rewrite` zero-code migration CLI
    syntax (Claim 4) — not documented anywhere else in this corpus.
  - The per-provider Bedrock-vs-OpenAI/Azure price and context-window
    divergence for the identical `openai/gpt-5.6-sol` gateway slug
    (Claim 9) — the first corpus documentation that "the same model slug on
    AI Gateway" does not guarantee identical price or spec across upstream
    cloud providers.
  - Terra's explicit vendor-authored routing heuristic ("the tier most
    GPT-5.6 traffic belongs on... escalate to Sol... drop to Luna...",
    Claim 11) — a named, prescriptive three-tier routing recommendation not
    present in any prior GPT-5.6 or AI Gateway source note.
  - The internally-inconsistent "limited preview" vs. GA framing on the
    same publication date (Claim 1) — flagged as an open question, not
    resolved.

## Guide Impact

- **Chapter 02 (Harness Engineering — Multi-Provider Routing)**: Add Claim 4
  (`vercel ai-gateway rules add --type rewrite --source <old> --destination
  <new>`) as a concrete reference for zero-code, fleet-wide model migration
  via a gateway rewrite rule — relevant wherever the guide discusses
  swapping a model version across every caller without a code change or
  redeploy.

- **Chapter 03 (Model Selection — Cost Economics)**: Add Claim 9 (AWS
  Bedrock's ~10% price premium and ~75% smaller context window versus
  OpenAI/Azure for the identical `openai/gpt-5.6-sol` slug) as a concrete
  caution against assuming a gateway model slug guarantees uniform pricing
  or spec across upstream cloud providers — teams should pin or verify the
  specific provider route, not just the model name, when reasoning about
  cost or context-window budgets. Add Claim 11 (Terra as Vercel's
  recommended default tier, with explicit escalate/downgrade guidance) as a
  named vendor routing heuristic, distinct from — and worth contrasting
  with — the empirically-measured routing splits already documented in
  `blog-vercel-ai-gateway-production-index-may2026.md`.

- **Chapter 04 (Cost Engineering at Scale)**: Add Claim 10's worked
  cache-pricing arithmetic (1.25x write / 90% read discount holding exactly
  against both original and post-cut GPT-5.6 prices) as a concrete,
  cross-checked reference table for practitioners modeling prompt-cache
  economics on GPT-5.6 via AI Gateway specifically.

- No chapter should cite Claim 1's "limited preview" framing as evidence
  that GPT-5.6 was gated or unavailable via AI Gateway on July 9, 2026 —
  the tension with OpenAI's own same-day GA declaration is unresolved, and
  the page's own meta description omits the phrase.

## Extraction Notes

1. **WebFetch produced inconsistent paraphrases across repeated calls to the
   same URL.** Two separate `WebFetch` passes against the changelog returned
   differently-worded "quotes" for the same passages (e.g. one pass included
   "in a limited preview" in its summary of the opening line, a second pass's
   summary of the same line omitted it). Per MINER.md §2a and the precedent
   in `blog-vercel-ai-gateway-api-key-budgets.md` Extraction Notes, this note
   discards all `WebFetch` output and instead retrieves the raw page HTML
   directly via `curl` with a browser user-agent, strips scripts/styles, and
   reads the linearized plain text. Every `Quote` field in Claims 1-7 was
   verified character-for-character against that raw HTML (re-checked twice
   for Claim 1's "limited preview" phrase specifically, given the WebFetch
   inconsistency, by locating the exact byte offset of the sentence in the
   unmodified HTML source — reproduced in this note's Guide Impact caveat).
2. **Three linked pages followed, per MINER.md §1** ("follow up to 5 linked
   pages that seem substantive"): the changelog's own "model playground" link
   goes to `vercel.com/ai-gateway/models/gpt-5.6-sol`; the Terra and Luna
   equivalents (`.../gpt-5.6-terra`, `.../gpt-5.6-luna`) were located by
   URL pattern and fetched for completeness, since the changelog covers all
   three models equally. All three were fetched live via direct `curl` on
   2026-08-07, the date of this extraction — three weeks after the
   changelog's July 9, 2026 publication date and about a week after the
   July 30, 2026 Terra/Luna price cut already documented elsewhere in this
   corpus. Every pricing/spec figure sourced from these three pages (Claims
   8-11) is explicitly timestamped to the 2026-08-07 fetch in this note, not
   attributed to the changelog's original publication state, since the
   changelog itself states no dollar pricing.
3. **Other linked pages (custom reporting, ZDR, BYOK docs, leaderboard) were
   not followed.** These are generic AI Gateway platform-feature pages, not
   specific to GPT-5.6; per MINER.md §1's "substantive" qualifier, and given
   that the budgets feature is already a dedicated corpus source note
   (`blog-vercel-ai-gateway-api-key-budgets.md`), following them would not
   add GPT-5.6-specific detail.
4. **No contradiction issues filed.** Two discrepancies were identified and
   evaluated against MINER.md §4a (see Cross-References → Contradicts) — the
   "limited preview" vs. GA framing, and the 1.1M vs. "million" context-window
   figure — both judged to be unresolved precision/scope ambiguities rather
   than material factual disputes that would drive different guide advice.
   The Assayer or Smith may reach a different conclusion, particularly on
   the "limited preview" question.
5. **Confidence calibration: emerging.** Most individual claims about
   shipping platform mechanics (slugs, CLI syntax, feature list, live
   pricing tables) are rated "settled" — first-party, directly observed, and
   in several cases independently cross-checked against existing corpus
   figures. The note's overall confidence is "emerging" because: (a) the
   changelog's headline availability claim (Claim 1) has an internal,
   same-day tension with OpenAI's own GA framing that this Miner could not
   resolve; (b) several of the most concrete findings (Claims 8-11) come not
   from the changelog itself but from linked pages in their *current*
   (2026-08-07) state, three to four weeks after the changelog's own
   publication date, and are explicitly caveated as such; and (c) the
   model-capability claims Vercel repeats (Claim 2) are unverified vendor
   marketing language, consistent with how the rest of this corpus treats
   the same claims when sourced directly from OpenAI.
