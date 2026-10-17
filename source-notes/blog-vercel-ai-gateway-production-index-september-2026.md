---
source_url: https://vercel.com/blog/ai-gateway-production-index-september-2026
source_type: blog-post
title: "Open-weight models take 56% of token volume, Astra doubles Fable 5.1 spend"
author: Amelia Charles, Eric Dodds (Vercel)
date_published: 2026-09-17
date_extracted: 2026-10-17
last_checked: 2026-10-17
status: current
confidence_overall: emerging
issue: "#4186"
---

# Open-weight models take 56% of token volume, Astra doubles Fable 5.1 spend

> Vercel's September 2026 AI Gateway Production Index (August data): open-weight models became the majority of gateway tokens (56%, on 14% of spend), average price per token fell 23.2%, Fable 5 spend moved to the half-price Opus 5 inside Anthropic rather than to other labs, and OpenAI's Astra out-launched Fable 5.1 two to one.

## Source Context

- **Type**: blog-post (Vercel Blog, monthly "AI Gateway Production Index" series; published 17 Sep 2026, 6 min read; reports data through August 2026, with dated "Latest Index updates" appended on Sep 17 and Sep 18).
- **Author credibility**: Amelia Charles and Eric Dodds, Vercel. Eric Dodds also bylines the July-edition installment already in the corpus. This is first-party telemetry from Vercel's own gateway product, so counts are real routed traffic, but the sample is limited to Vercel AI Gateway customers and the post reports only percentage shares, never absolute volumes. Spend is *estimated from list prices*, not actual bills.
- **Scope**: Open-weight token/spend share, price-per-token trend, Fable 5 -> Opus 5 migration, Anthropic spend share, Gemini 3 Flash attrition, GLM-5.3-Flash adoption, OpenAI Astra vs. Fable 5.1 launch comparison, plus image/video modality notes. Does not cover absolute dollars/tokens, non-gateway traffic, or quality comparisons between models.

## Extracted Claims

### Claim 1: Open-weight models became the majority of gateway tokens for the first time in August 2026 (56%), up from 7% in December 2025 and 13% in April
- **Evidence**: Vercel first-party gateway token counts; monthly rise every month April-August.
- **Confidence**: emerging (measured, but single-vendor sample)
- **Quote**: "Open-weight models ran the majority of gateway tokens for the first time, up from 7% in December to 56% in August."
- **Our assessment**: Strong dated data point extending the May->June->July trajectory in the corpus. Note the methodology caveat in the post: "Open-weight classifications follow the current AI Gateway model list, which is broader than the definition used in earlier reports." The April baseline is 13% here versus 11% in the earlier note, which is a definition revision, not a contradiction.

### Claim 2: Open-weight models carry most tokens but only 14% of spend, though the dollar share is accelerating
- **Evidence**: Same dataset; spend estimated from list prices.
- **Confidence**: emerging
- **Quote**: "Open-weight models processed 56% of August’s gateway tokens and accounted for 14% of spend."
- **Our assessment**: Compare 29% tokens / <4% spend in June: spend share rose roughly 3.5x faster than the token ratio implies. Vercel's explanation ("customers are moving more production workloads over to them") is an interpretation, not tested.

### Claim 3: Average price per token fell 23.2% in August (third straight monthly drop); the median heavy-use team paid 7.6% less per token
- **Evidence**: Estimated spend divided by token volume; the median figure is limited to teams running more than ten million tokens in both months.
- **Confidence**: emerging
- **Quote**: "Among teams running more than ten million tokens in both months, the median team paid 7.6% less per token, more than double July's 2.9% decline."
- **Our assessment**: The aggregate drop (23.2%) is largely mix shift toward cheap open-weight models, whereas the like-for-like team figure (7.6%) is much smaller. Readers should not conflate them. The summary also claims "The average token costs less than half what it did five months ago."

### Claim 4: Fable 5 lost two-thirds of its gateway spend share in a month as teams stepped down to Opus 5 at about half the price
- **Evidence**: Fable 5 spend share 13.2% (July) -> 4.9% (August); Opus 5 rose to 22.5%; nine in ten Fable teams cut usage.
- **Confidence**: emerging
- **Quote**: "Nine in ten of the teams that ran Fable cut their usage, and more of them moved their workloads to Opus 5 than any other model. Fable’s extra capability wasn’t worth double the price."
- **Our assessment**: Concrete revealed-preference evidence for tiering down within a lab. The last sentence is Vercel's inference from spend behavior, not a capability evaluation. The July spike (13.2%) followed the Fable restoration on July 1 (see `blog-vercel-ai-gateway-fable-5-restored.md`), so part of the "loss" is reversion from a pent-up burst.

### Claim 5: Anthropic retained spend share because workloads moved within the lab; it has held the top two spend positions every month since December
- **Evidence**: Monthly spend-share series.
- **Confidence**: emerging
- **Quote**: "Anthropic has taken at least 61 cents of every dollar spent through AI Gateway every month since December, and 64 cents in August."
- **Our assessment**: Consistent with 61% (June, earlier note) and 65% (May). Stable lab share despite model churn.

### Claim 6: Customer loyalty follows the model profile (capability/price fit), not the lab
- **Evidence**: Opus 5 gained "almost twice what Fable lost"; GLM-5.3-Flash overtook GLM-5.2 one day after appearing; Gemini 3 Flash lost 95% of its token share since May, with over three-quarters of lost volume going to other labs.
- **Confidence**: emerging
- **Quote**: "Lab loyalty doesn’t follow brand, it follows model profile, and consistency wins."
- **Our assessment**: Supported by the three migration cases, but the post notes "Statements about where volume moved compare changes among the same teams. They do not trace individual tokens between models." so attribution is correlational.

### Claim 7: Gemini 3 Flash attrition split between cheaper and pricier models
- **Evidence**: About half the lost volume went to cheaper models (led by GPT-5.6 Luna), most of the rest to pricier ones (Opus 5, Sonnet 5); Google's gateway token share fell from 30% to 5%.
- **Confidence**: emerging
- **Quote**: "About half of the volume that left Gemini 3 Flash went to cheaper models, led by GPT-5.6 Luna, which costs less than half as much per token."
- **Our assessment**: Shows that routing moves in both directions (down for cost, up for quality) when a successor fails to offer a relative advantage.

### Claim 8: OpenAI Astra took a third of OpenAI's gateway spend within two days and 7.7% of all gateway spend in 12 days vs. 3.7% for Fable 5.1 at the same price
- **Evidence**: Launch-window comparison (Sep 3 vs. Sep 1 launches); Astra used by twice as many teams; passed Fable 5.1 cumulative spend on day four.
- **Confidence**: emerging (early launch data, novelty effects likely)
- **Quote**: "Astra took 7.7% of all gateway spend in its first twelve days while Fable 5.1, launched two days earlier at the same price, took 3.7%."
- **Our assessment**: Launch-window shares are not steady state; the July Fable 5 spike later fell back (Claim 4). Treat as launch interest.

### Claim 9: Within OpenAI's lineup, premium models drive spend and cheap models drive volume
- **Evidence**: Sep 4-16 token and spend splits.
- **Confidence**: emerging
- **Quote**: "Within OpenAI’s model lineup, Astra and Sol processed 27% of OpenAI’s tokens but accounted for 71% of its spending from September 4 through 16."
- **Our assessment**: Real-world evidence of the tiered-routing pattern (cheap model for bulk, premium for select tasks) within one provider.

### Claim 10: Vercel's recommendation: reserve frontier models for tasks that justify the premium
- **Evidence**: Interpretation of the above data; no controlled evaluation.
- **Confidence**: anecdotal
- **Quote**: "Teams can now get more inference from the same budget and reserve frontier models only for the tasks that justify the premium."
- **Our assessment**: Reasonable but vendor-framed advice; Vercel profits from gateway multi-model routing.

### Claim 11: Update note: Jev reached ~13% of paid teams within 24 hours
- **Evidence**: Dated update appended Sep 18 (after the nominal publish date).
- **Confidence**: anecdotal
- **Quote**: "Jev is now the fastest-adopted model in AI Gateway history."
- **Our assessment**: Thin (one line, no model description in this post); don't build on it without another source.

## Concrete Artifacts

```
Vercel AI Gateway Production Index, Sept 2026 (data through Aug 2026) — figures as reported
Open-weight token share:  Dec 2025 7% -> Apr 13% -> Aug 56%   (spend share Aug: 14%)
Avg price/token Aug:      -23.2% (3rd straight monthly drop); median >10M-token team: -7.6% (July: -2.9%)
Spend share:              Fable 5 13.2% (Jul) -> 4.9% (Aug); Opus 5 -> 22.5%; Anthropic 64% (Aug)
Google gateway token share: 30% -> 5% (Gemini 3 Flash = 22 of 25 points lost)
Launch window (12 days):  Astra 7.7% of gateway spend vs Fable 5.1 3.7% (same price)
Astra = same price as Fable 5.1, 2.5x GPT-5.6 Sol
```

Methodology (verbatim from "About this report"):
- "Spending is estimated using labs’ published list prices; actual bills may differ. Average price per token is estimated spending divided by token volume."
- "Token volume includes input, output, reasoning, cached-input, and cache-creation tokens."

## Cross-References

- **Corroborates**: `blog-vercel-ai-gateway-production-index-june2026.md` (actually the July edition; Claim 2 open-weight rise, Claim 5 Anthropic ~61% spend share); `blog-vercel-ai-gateway-production-index-may2026.md` (Claim 3 Anthropic spend share 65%, Claim 6 price-per-token trend); `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` (Claim 5, Luna as cheap application model; Claim 12, price war below flagship tier).
- **Contradicts**: None filed. The April open-weight share differs (13% here vs. 11% in the July-edition note) because the post says the open-weight classification is now broader; recorded as a methodology revision.
- **Extends**: `blog-vercel-ai-gateway-fable-5-restored.md` (what happened to Fable 5 spend after restoration); `blog-vercel-ai-gateway-api-key-budgets.md` (cost-control tooling; this adds the market-level cost context but makes no reference to budgets).
- **Novel**: First majority-open-weight month; Fable 5 -> Opus 5 step-down with "nine in ten" figure; Gemini 3 Flash attrition destinations; Astra vs. Fable 5.1 launch comparison; like-for-like median team price change (7.6%).

## Guide Impact

- **Model selection / routing chapters** (check current numbering): Add a dated data point that production teams are tiering down within a lab (Fable 5 -> Opus 5) and moving bulk volume to open-weight/cheap models, citing this note's Claims 1, 4 and 9, with the caveat that it is single-vendor, list-price-estimated data.
- **Cost / team budget chapters**: Distinguish aggregate price-per-token decline (23.2%, mix-shift driven) from like-for-like team savings (7.6%) when quoting figures (Claim 3).
- Any text framing open-weight models as a secondary option should be revisited against the 56% token share, while noting they carry only 14% of spend.

## Extraction Notes

- Read the full article (fetched HTML and parsed text); all quotes were copied from the page text. Charts are images and their data were not extracted beyond what the prose states.
- The post lists links to prior June/July/August reports; only the May and July-edition notes exist in the corpus. The August edition is not in the corpus.
- The "Jev" update appears dated after the post's publish date; the post is updated in place.
