---
source_url: https://vercel.com/blog/ai-gateway-production-index-july-2026
source_type: blog-post
title: "Open-Weight Models Surge to 29% of Volume, Price Per Token Flattens"
author: Eric Dodds, Jerilyn Zheng (Vercel)
date_published: 2026-07-13
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: emerging
issue: "#2646"
---

# Open-Weight Models Surge to 29% of Volume, Price Per Token Flattens

> Vercel's monthly AI Gateway production index for June 2026: open-weight
> models nearly tripled their token share since April to 29% (on under 4%
> of spend) while DeepSeek alone reached 22.6% of tokens, within two points
> of second-place Google; the average price per token — which had risen
> ~20% in May — went flat as open-weight growth and a ~12% rise in
> closed-weight frontier prices offset each other; and Claude Fable 5
> reached 22% of Opus 4.8's request volume in four days before a US
> export-control directive suspended it for the rest of the month.

## Source Context

- **Type**: blog-post (Vercel Blog, "AI Gateway production index" recurring
  monthly series; this installment published July 13, 2026, reporting June
  2026 gateway activity — per the post's own text, "The July index reports
  on AI Gateway data collected in June 2026." This is the direct successor
  to the installment already in this corpus,
  `blog-vercel-ai-gateway-production-index-may2026.md`, which reported May
  2026 data and was published June 8, 2026. Includes seven
  charts/figures with alt-text-equivalent captions and a data-methodology
  "About this report" appendix; roughly 900 words of body text plus
  captions.)
- **Author credibility**: Eric Dodds and Jerilyn Zheng, credited under
  "Contributors" at the foot of the post, published under the Vercel Blog.
  Zheng is also the credited author of `blog-vercel-ai-gateway-fable-5-restored.md`,
  a recurring AI-Gateway product-team byline in this corpus. Vercel operates
  the AI Gateway product itself, so this is first-party infrastructure-provider
  telemetry, not third-party survey or self-reported customer data — the
  percentages derive directly from requests routed through Vercel's own
  product. This gives high confidence in the *internal consistency* of the
  reported shares (actual routing/spend counts, not estimates), but the
  dataset reflects only traffic that flows through Vercel AI Gateway, not
  the AI market as a whole — a selection effect the post does not quantify.
- **Scope**: Covers month-over-month (May→June 2026) token volume and spend
  growth, open-weight vs. closed-weight token/spend share, per-provider
  token/spend share (DeepSeek, Google, Anthropic, OpenAI), GLM 5.2's
  adoption curve, per-use-case spend concentration (back-office agents,
  coding agents, app generation), image/video modality market shares,
  Claude Fable 5's adoption and export-control suspension, B2B/B2C
  cost split, and Google's workload concentration by use case. Does NOT
  cover: absolute dollar or token figures (all data is percentage shares);
  non-Gateway traffic; customer identities; or a technical explanation of
  why closed-weight frontier prices rose ~12% in June.

## Extracted Claims

### Claim 1: AI Gateway token volume grew 29% and spend grew 27% month-over-month in June 2026, while the average price per token was flat — reversing May's pattern, where spend had grown more than twice as fast as volume and pushed the average token price up almost 20%
- **Evidence**: Vercel's own first-party aggregate volume/spend ratio, contrasted explicitly against the prior month's figures reported in this same series.
- **Confidence**: settled (directly measured routing/spend counts from the platform operator)
- **Quote**: "In June, token volume and spend grew at nearly the same rate, 29% and 27%, while the price per token remained steady. The month before, spend had grown more than twice as fast as volume, driving the average token cost up by almost 20%."
- **Our assessment**: This is the report's headline finding and a direct sequel to `blog-vercel-ai-gateway-production-index-may2026.md` Claim 6, which documented the ~20% May price rise as a puzzle — a 20-50x cheaper model (DeepSeek V4) entering at scale did not lower the blended average price, because frontier-model demand grew faster than non-frontier demand. This report resolves that trajectory: growth in cheap-model volume and a rise in frontier prices arrived together in June and canceled out in the aggregate average (see Claim 7 for the stated mechanism).

### Claim 2: Open-weight models ran 29% of gateway tokens in June on just under 4% of spend, up from 11% of tokens in April — open-weight token share has almost tripled since April
- **Evidence**: Vercel's own first-party token/spend classification by provider (four open-weight-serving labs: DeepSeek, MiniMax, Moonshot, Z.ai).
- **Confidence**: settled (directly measured routing/spend counts)
- **Quote**: "Open-weight models ran 29% of gateway tokens in June on just under 4% of spend. That is nearly a third of the tokens for one twenty-fifth of the dollars." / "Open-weight token share has almost tripled since April."
- **Our assessment**: This is the corpus's first aggregate (multi-lab) open-weight token-share figure for AI Gateway, as opposed to the single-model DeepSeek figure (17% of tokens in May) reported in the prior month's installment. It quantifies a sustained three-month acceleration (11% in April → 29% in June) rather than a one-model spike, meaningfully strengthening the "cheap open-weight models are displacing closed-weight volume at scale" narrative already emerging in this corpus.

### Claim 3: DeepSeek reached 22.6% of gateway token volume in June, third place and less than two points behind Google, whose token share slipped to 24% as its April surge unwound
- **Evidence**: Vercel's own first-party per-provider token-share data.
- **Confidence**: settled (directly measured routing counts)
- **Quote**: "DeepSeek, now the third-largest source of tokens on the gateway at 22.6%, behind Anthropic and Google." / "Google's share of token volume slipped to 24% as its April surge unwound, leaving DeepSeek within two points of second place."
- **Our assessment**: This directly extends `blog-vercel-ai-gateway-production-index-may2026.md` Claim 1 (DeepSeek's token share jumped from <1% to 17% in May) with a fourth consecutive month of growth (22.6% in June), and adds a new data point not in the May report: DeepSeek's growth is now converging on Google's declining share rather than simply adding volume alongside stable incumbents. The post's own framing — "on current trajectories, an open-weight lab will soon be the second-largest by volume on AI Gateway" — is Vercel's own extrapolation, not a measured fact, and should be flagged as such if cited.

### Claim 4: Z.ai's GLM 5.2, an MIT-licensed open-weight model priced at roughly a fifth of Opus 4.8, grew its daily token volume roughly 50x from its June 16 API availability through month-end, ranked #11 on AI Gateway by tokens in its final week (as high as #7 on single days), and captured 76% of its model family's June tokens in barely two weeks — faster than Gemini 3.1 Pro, the previously fastest in-family migration on the gateway, which took until its second month to reach a similar share
- **Evidence**: Vercel's own first-party per-model token-volume time series for GLM 5.2, contrasted explicitly against Gemini 3.1 Pro's previously charted in-family adoption curve.
- **Confidence**: settled (directly measured routing-volume time series)
- **Quote**: "Z.ai released GLM 5.2, an MIT-licensed open-weight model aimed at long-horizon agentic work at approximately a fifth of Opus 4.8 pricing. From its June 16 API availability through month end, its daily token volume grew about 50x. It ranked #11 on AI Gateway by tokens in the final week, and as high as #7 on single days. It took 76% of its family's June tokens in barely two weeks. Gemini 3.1 Pro, the fastest in-family migration we had previously charted, took until its second month to reach a similar share."
- **Our assessment**: This is the first production-routing adoption-velocity figure for GLM 5.2 in this corpus. `blog-latentspace-glm52-open-frontier-parity.md` Claims 3-4 already documented GLM 5.2's capability/cost positioning via Artificial Analysis's AA-Briefcase benchmark ($2.40/task at 1266 Elo, versus Opus 4.8 at $10.40/task and 1356 Elo) — this source corroborates the "much cheaper, near-frontier" positioning with actual gateway-routed adoption speed, giving practitioners both sides of the picture (cost/quality tradeoff and real-world uptake velocity) for the same model within two months of its capability benchmark being mined.

### Claim 5: Anthropic took 61% of gateway spend on 32% of tokens in June, down from 65% spend share in May but in line with April, and captured 72% or more of spend in every high-stakes use case (coding agents, back-office agents, app generation); the top four frontier US labs together took 95% of gateway spend
- **Evidence**: Vercel's own first-party per-provider spend/volume aggregation, plus a per-use-case spend-share breakdown for named high-stakes categories.
- **Confidence**: settled (directly measured share figures)
- **Quote**: "The top four frontier US labs took 95% of AI Gateway spend in June. Anthropic alone took 61% of spend on 32% of tokens, down from 65% in May, but in line with April. It also took 72% or more of spend in the most consequential use cases, where mistakes are costly: coding agents, back-office agents, and app generation."
- **Our assessment**: This directly extends `blog-vercel-ai-gateway-production-index-may2026.md` Claim 3 (Anthropic's spend share grew 61%→65% in May) by showing the May figure was a peak rather than a sustained trend — June's 61% spend share on 32% tokens is a pullback that the post itself frames as "in line with April," meaning May's spike, not June's level, may be the anomaly. This nuance (spend share fluctuating month to month around a ~61% baseline while token share holds near 32%) is a more accurate multi-month picture than either single-month report alone would give.

### Claim 6: OpenAI's token share fell from 12.5% to 10.3% while its spend share rose from 13.3% to 16.1% in June, driving its cost per token up about 50% relative to the market in one month — customers sent OpenAI less volume but costlier work
- **Evidence**: Vercel's own first-party spend and volume data for OpenAI specifically.
- **Confidence**: settled (directly measured share figures; the "50% relative to the market" framing is a direct arithmetic derivation from the token/spend share changes)
- **Quote**: "OpenAI’s token share fell from 12.5% to 10.3% while its spend share rose from 13.3% to 16.1%, driving its cost per token up about 50% relative to the market in one month. In contrast to DeepSeek, customers sent OpenAI less volume but costlier work, a divergence that only shows up in production data."
- **Our assessment**: This sharpens `blog-vercel-ai-gateway-production-index-may2026.md` Claim 4, which reported OpenAI's token share "held near 13%" while spend share ticked up in May and left the underlying mechanism (mix shift vs. price increase) as an open question the Miner flagged as unresolved. This report shows the pattern accelerating and inverting direction (token share now falling, not just flat) with a quantified cost-per-token increase (~50% relative to market) — still without disambiguating list-price change from tier-mix shift, but the magnitude and direction are now unambiguous where May's data was ambiguous.

### Claim 7: The price-per-token flattening happened because open-weight models' rising token share (worth about a tenth of the average token price) pulled the average down, while closed-weight frontier prices rose about 12% per token in June — the two effects offset each other
- **Evidence**: Vercel's own first-party decomposition of the flat aggregate price-per-token figure into its two component trends.
- **Confidence**: emerging (the two component trends — open-weight share/price and closed-weight price rise — are each directly measured, but the "offset each other" causal decomposition is Vercel's own interpretive framing of why the net average landed flat, not an independently audited attribution model)
- **Quote**: "Since April, open-weight models have climbed from a ninth of all token volume to nearly a third, at about a tenth of the average token price on the gateway. That alone should have pulled the price per token down. But as cheap volume rose in June, so too did closed-weight frontier prices, up about 12% per token. They offset each other, so the average price per token was flat."
- **Our assessment**: This is a genuinely new mechanism for this corpus's cost-governance material: it names a second variable (rising closed-weight frontier list prices, +12% per token in June) that was not present in the May report's account of why average costs move the way they do. Practitioners should treat "cheap open-weight adoption will lower our blended costs" as conditional on frontier pricing staying flat — this source shows a case where frontier price increases can fully offset cheap-model savings at the aggregate level, even while the cheap-model share itself is growing rapidly.

### Claim 8: Each media modality has a different market leader — OpenAI's GPT Image generated 53% of images (52% of image spend) and Google's Nano Banana generated 39% of images (43% of spend), together 92% of gateway images; in video, Chinese labs (ByteDance's Seedance, Kling, Alibaba's Wan) together took roughly two-thirds of video spend, with ByteDance's Seedance leading spend at 49% on about a third of videos generated, while xAI's Grok Imagine generated the most videos (42%) on only 19% of spend
- **Evidence**: Vercel's own first-party media-generation classification (image and video figures count generated media, not tokens, per the report's methodology note).
- **Confidence**: settled (directly measured generation/spend counts, per the report's own stated methodology for non-token-billed modalities)
- **Quote**: "OpenAI's GPT Image family generated 53% of images and took 52% of image spend in June. Google's Nano Banana generated almost 39% of images and took 43% of spend. No other family cleared 5% of either." / "ByteDance's Seedance led spend at 49% with only a third of videos generated. xAI's Grok Imagine generated 42% of videos on 19% of spend, the same volume-discount position DeepSeek holds in text. The Chinese labs together, Seedance, Kling, and Alibaba's Wan, took roughly two-thirds of video dollars."
- **Our assessment**: This is the first modality-segmented (image/video) market-share data in this corpus — prior sources document text-model market share only. The explicit parallel Vercel draws ("the same volume-discount position DeepSeek holds in text") for Grok Imagine is a useful cross-modality framing: the volume-cheap/frontier-premium split that structures the text-token market appears to be replicating in video generation specifically, with xAI in the volume-discount role and ByteDance in something closer to the frontier-premium role.

### Claim 9: Claude Fable 5, released June 9, reached 22 requests for every 100 sent to Opus 4.8 within four days; a US export-control directive took effect June 12 covering Fable 5, and Anthropic suspended access to comply for the rest of the month, with controls lifting June 30 and access resuming July 1
- **Evidence**: Vercel's own first-party per-model request-volume ratio (Fable 5 vs. Opus 4.8) for the adoption figure, combined with the post's own account of the suspension/restoration timeline.
- **Confidence**: settled (directly measured request-volume ratio for the adoption figure; the export-control dates corroborate, rather than newly establish, the timeline already documented elsewhere in this corpus)
- **Quote**: "Anthropic released Claude Fable 5 on June 9, and it was adopted rapidly. In only four days, Fable usage rose to 22 requests for every 100 sent to Opus 4.8." / "On June 12, a US export-control directive took effect covering Fable 5, and Anthropic suspended access to comply. The model stayed offline for the rest of the month. Controls lifted on June 30 and access resumed July 1."
- **Our assessment**: The June 9 launch and June 12 suspension dates corroborate `blog-simonwillison-claude-fable-5.md` Claim 3 (first-hand observation of the June 9, 2026 simultaneous launch across Claude surfaces) and `blog-simonwillison-fable-mythos-access-directive.md` Claims 1-2 (the June 12 US government export-control directive and its ~4.5-hour enforcement window), while the June 30 lift / July 1 resumption date corroborates `blog-vercel-ai-gateway-fable-5-restored.md` Claim 1 (Vercel's own July 1 changelog confirming access restoration). What is novel here is the adoption-velocity figure itself — "22 requests for every 100 sent to Opus 4.8 in four days" is the first quantified, gateway-measured production-adoption number for Fable 5 anywhere in this corpus; every prior corpus source documents Fable 5's launch, capabilities, or the suspension/restoration mechanics, but none quantifies how fast it was actually being adopted in production before the suspension cut that curve short.

### Claim 10: Back-office agents are the most expensive workload per token on the gateway, running 5% of total tokens on 14% of total spend; B2B applications drove 46% of June tokens but 60% of spend, while B2C drove the reverse — 43% of tokens and 26% of spend; and Google's volume concentrates in consumer-shaped workloads, running 57% of personal-assistant tokens and 54% of education tokens but less than 2% of coding-agent tokens
- **Evidence**: Vercel's own first-party token/spend classification by use case, by B2B/B2C application type, and by provider-within-use-case.
- **Confidence**: settled (directly measured aggregate classifications)
- **Quote**: "Back-office agents are the most expensive workload per token on the gateway, running 5% of total tokens on 14% of total spend. B2B use cases drove 46% of June tokens but 60% of spend; B2C the reverse, at 43% of tokens and 26% of spend. Google's volume concentrates in consumer-shaped workloads. It ran 57% of personal-assistant tokens and 54% of education tokens in June, but less than 2% of coding agent tokens."
- **Our assessment**: The B2B/B2C split (B2B ~1.5x more expensive per token than B2C, by rough division of the given percentages) is directionally consistent with `blog-vercel-ai-gateway-production-index-may2026.md` Claim 8 (B2B cost roughly 60% more per token than B2C in May), giving the same qualitative pattern a second consecutive month of confirmation, though the two reports present the figure in different units (May: a direct "60% more per token" ratio; June: separate token-share/spend-share percentages) and should not be treated as identical repeated measurements. The Google workload-concentration figure (57% of personal-assistant tokens, <2% of coding-agent tokens) is new to this corpus and gives a first provider-specific use-case specialization data point, distinct from the aggregate provider-share figures reported elsewhere in this note and the May report.

## Concrete Artifacts

### Key month-over-month metrics (June 2026 vs. May 2026, verbatim figures from post body)

```
Total AI Gateway tokens: +29% MoM
Total AI Gateway spend:  +27% MoM
Average cost per token:  flat MoM (May was ~+20% MoM)

Open-weight models: 29% of tokens (up from 11% in April), <4% of spend
DeepSeek:  22.6% of tokens (3rd place, <2 points behind Google)
Google:    24% of tokens (down from April surge)
Anthropic: 61% of spend on 32% of tokens (down from 65% in May, in line with April)
  - 72%+ of spend in every high-stakes use case (coding agents, back-office
    agents, app generation)
OpenAI:    token share 12.5% -> 10.3%; spend share 13.3% -> 16.1%
           (cost per token up ~50% relative to market in one month)
Top 4 frontier US labs: 95% of gateway spend

GLM 5.2 (Z.ai, MIT license, ~1/5 of Opus 4.8 pricing):
  - API available June 16; daily token volume grew ~50x through month-end
  - #11 on AI Gateway by tokens in final week of June (as high as #7 on
    single days)
  - 76% of its model family's June tokens within ~2 weeks
    (vs. Gemini 3.1 Pro: took until 2nd month for similar in-family share)

Images: OpenAI GPT Image 53% volume / 52% spend; Google Nano Banana 39%
  volume / 43% spend (together 92% of images; no other family >5%)
Video: ByteDance Seedance 49% spend on ~1/3 of videos generated;
  xAI Grok Imagine 42% of videos generated on 19% of spend;
  Chinese labs (Seedance, Kling, Alibaba Wan) together ~2/3 of video spend

Claude Fable 5: released June 9; reached 22 requests per 100 sent to
  Opus 4.8 within 4 days; export-control directive June 12 suspended
  access; controls lifted June 30, access resumed July 1

Back-office agents: 5% of tokens, 14% of spend (priciest per-token workload)
B2B: 46% of tokens, 60% of spend  |  B2C: 43% of tokens, 26% of spend
Google: 57% of personal-assistant tokens, 54% of education tokens,
  <2% of coding-agent tokens

"Roughly one in eight enterprise customers now runs an open-weight
model in production."

Source: Vercel Blog, "Open-weight models surge to 29% of volume, price
per token flattens" (AI Gateway production index, June 2026 data),
published July 13, 2026,
https://vercel.com/blog/ai-gateway-production-index-july-2026
```

### Price-flattening mechanism (verbatim)

```
"The market spent more overall, but not more per token. Since April,
open-weight models have climbed from a ninth of all token volume to
nearly a third, at about a tenth of the average token price on the
gateway. That alone should have pulled the price per token down. But as
cheap volume rose in June, so too did closed-weight frontier prices, up
about 12% per token. They offset each other, so the average price per
token was flat.

This is evidence of the routing discipline June's report documented, now
visible in the aggregate: high-volume work goes to low-cost models,
high-risk work stays on the frontier."

Source: same as above, "AI investment kept climbing, and the average
token price went flat" section.
```

### Methodology note on open-weight measurement (verbatim)

```
"Open-weight models are measured two ways. Volume and spend shares (the
lab-share charts) classify by provider, counting the four labs that serve
their own models on the gateway (DeepSeek, MiniMax, Moonshot, Z.ai). This
is conservative. The enterprise-adoption figure classifies by model,
counting open-weight models regardless of which provider served them,
such as Qwen, Gemma, GPT-OSS, and Kimi.

Image and video figures count generated media (successful requests only),
not tokens. Image and video models are not billed per token, so shares
reflect images and videos produced."

Source: same as above, "About this report" appendix section.
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-gateway-production-index-may2026.md`,
`blog-latentspace-glm52-open-frontier-parity.md`,
`blog-simonwillison-claude-fable-5.md`,
`blog-simonwillison-fable-mythos-access-directive.md`, and
`blog-vercel-ai-gateway-fable-5-restored.md` were re-read directly
(MINER.md §4b) and the claim numbers cited above were confirmed against
each note's numbered `### Claim N:` headings in document order before
writing this section.

- **Corroborates**:
  - `blog-simonwillison-claude-fable-5.md` Claim 3 (first-hand observation
    that Anthropic made Fable 5 available across all Claude surfaces on
    June 9, 2026): this source's Claim 9 independently confirms the same
    June 9 launch date from gateway-routing data.
  - `blog-simonwillison-fable-mythos-access-directive.md` Claims 1-2 (a
    US government export-control directive suspended Fable 5 and Mythos 5
    access starting June 12, 2026, with a ~4.5-hour enforcement window):
    this source's Claim 9 independently confirms the June 12 suspension
    date from the platform-operator side.
  - `blog-vercel-ai-gateway-fable-5-restored.md` Claim 1 (Vercel's July 1
    changelog confirming Fable 5 access restored following the US
    Government's decision to lift the export-control directive): this
    source's Claim 9 confirms the same restoration date (July 1) and adds
    the specific date controls were lifted (June 30), which the restored.md
    changelog itself did not state explicitly.
  - `blog-latentspace-glm52-open-frontier-parity.md` Claims 3-4 (Artificial
    Analysis's AA-Briefcase benchmark placed GLM-5.2 at 1266 Elo / $2.40
    per task, versus Opus 4.8 at 1356 Elo / $10.40 per task): this source's
    Claim 4 corroborates GLM-5.2's low-cost positioning ("approximately a
    fifth of Opus 4.8 pricing") with independent, non-overlapping evidence
    — gateway-routed production adoption velocity rather than benchmark
    cost/quality figures.

- **Contradicts**: None identified. Anthropic's spend share fell from 65%
  (May, per `blog-vercel-ai-gateway-production-index-may2026.md` Claim 3)
  to 61% (June, this source's Claim 5) — this is a month-over-month value
  change within the same recurring metric, not a MINER.md §4a contradiction
  between two claims about the same fact; the two reports agree on what
  happened in their respective months, and this source's own framing
  ("down from 65% in May, but in line with April") treats May as the
  outlier rather than disputing the May report's figure.

- **Extends**:
  - `blog-vercel-ai-gateway-production-index-may2026.md`: this source is
    the direct next installment in the same recurring series, extending
    Claims 1, 3, 4, and 6 with a second consecutive month of data (DeepSeek
    17%→22.6% tokens; Anthropic spend share 65%→61%; OpenAI's token-share
    decline accelerating from "held near 13%" to "fell from 12.5% to
    10.3%") and resolving the open causal question that May's Claim 6 left
    unanswered (why did the average price per token rise despite cheap-model
    entry) with a new mechanism for June specifically: rising closed-weight
    frontier prices (+12%) offsetting rising open-weight share (Claim 7).
  - `blog-latentspace-glm52-open-frontier-parity.md`: extends that note's
    capability/cost-benchmark coverage of GLM-5.2 with actual production
    routing-volume adoption data (Claim 4), giving the corpus both halves
    of the "is this model good and is anyone actually using it" picture for
    the same model within roughly one month of each other.
  - `blog-simonwillison-claude-fable-5.md`, `blog-simonwillison-fable-mythos-access-directive.md`,
    and `blog-vercel-ai-gateway-fable-5-restored.md`: extends this corpus's
    Fable 5 timeline (launch → suspension → restoration) with the first
    quantified adoption-velocity figure (22% of Opus 4.8's request volume
    in 4 days) for the period between launch and suspension.

- **Novel**:
  - **Aggregate multi-lab open-weight token/spend share, tracked across
    three consecutive months** (Claim 2: 11% in April → 29% in June): the
    first sustained trend line for open-weight adoption as a category, not
    a single model.
  - **Image and video modality market-share data** (Claim 8): the first
    modality-segmented (non-text) production market data in this corpus —
    OpenAI/GPT Image and Google/Nano Banana in images; ByteDance/Seedance,
    xAI/Grok Imagine, and other Chinese labs in video.
  - **A stated mechanism for price-per-token flattening** (Claim 7:
    open-weight growth offsetting a ~12% closed-weight frontier price
    rise): new to the corpus as an explicit two-variable decomposition of
    an aggregate cost trend.
  - **GLM 5.2's gateway-routed adoption velocity** (Claim 4: ~50x daily
    token growth, 76% in-family share within two weeks) and **Claude
    Fable 5's pre-suspension adoption velocity** (Claim 9: 22% of Opus
    4.8's request volume in four days): both are new, model-specific
    production-adoption figures not present anywhere else in the corpus.
  - **"Roughly one in eight enterprise customers now runs an open-weight
    model in production"**: a new adoption-breadth (customer-count) metric,
    distinct from the token/spend-share metrics used elsewhere in the
    report.
  - **Google's use-case workload concentration** (Claim 10: 57% of
    personal-assistant tokens, 54% of education tokens, <2% of coding-agent
    tokens) and the **back-office-agent per-token cost premium** (5% of
    tokens, 14% of spend): new segmentation dimensions for this corpus's
    cost/architecture data.

## Guide Impact

- **Chapter 01 (Market Overview)**: Update the corpus's production
  market-share figures with June 2026 data: DeepSeek at 22.6% of tokens
  (up from 17% in May), aggregate open-weight models at 29% of tokens on
  <4% of spend (up from 11% of tokens in April), and Anthropic at 61%
  spend/32% tokens (down from 65% spend in May). Present this as a
  three-month trend (April→May→June) rather than a single snapshot, and
  add Claim 8's modality-specific leaders (OpenAI/images, xAI-and-Chinese-labs/video)
  as the corpus's first non-text market-share data.

- **Chapter 03 (Model Selection Dynamics)**: Add Claim 4 (GLM 5.2's ~50x
  adoption growth and 76% in-family token share within two weeks) as a
  concrete illustration of how fast a new, much-cheaper open-weight model
  can be adopted at production scale once it clears a capability bar —
  pair with `blog-latentspace-glm52-open-frontier-parity.md`'s cost/Elo
  data for the full cost-vs-adoption picture. Add Claim 6 (OpenAI's
  token-share decline paired with a rising cost-per-token) as a cautionary
  counter-example: a provider can lose volume share while its per-token
  price to customers rises, a divergence this source states "only shows up
  in production data."

- **Chapter 04 (Cost Engineering at Scale)**: Add Claim 7 (the price-per-token
  flattening mechanism) as an update to any existing guide passage citing
  the May report's "average cost rose despite cheap-model entry" finding —
  the June data shows that outcome is not permanent or one-directional:
  it depends on whether frontier-model prices are simultaneously rising,
  and in June frontier price increases (+12%) offset open-weight savings
  rather than compounding with them. Add Claim 10's back-office-agent
  (5% tokens/14% spend) and B2B/B2C (46%/60% vs. 43%/26%) figures as
  additional, corroborating segmentation data alongside the May report's
  B2B/B2C finding.

- **Chapter 06 (Governance / Security & Threat Model, wherever the Fable 5
  export-control episode is discussed)**: Add Claim 9's adoption-velocity
  figure (22% of Opus 4.8's request volume within four days of Fable 5's
  June 9 launch) as the first quantified data point for how quickly the
  model was being adopted before the June 12 export-control suspension cut
  that curve short — useful context for any discussion of the business
  impact of the suspension, which prior corpus sources document only from
  the policy/mechanics side, not the adoption-curve side.

## Extraction Notes

1. **Source fetched via direct HTTP, not WebFetch's AI-summarized output.**
   An initial WebFetch pass returned a paraphrased summary (confirmed by
   comparing its wording against the raw page — e.g., "captured 72% or more
   of spend" rendered as "maintaining '72% or more of spend'," and several
   sentences reordered or compressed). Per MINER.md §2a and the precedent
   set in `blog-vercel-ai-gateway-production-index-may2026.md` Extraction
   Notes, the page was instead fetched directly via `curl` with a browser
   user-agent, the `<article>` element isolated with a regex, HTML tags
   stripped and entities decoded with Python, and the resulting plain text
   read in full (110 lines, saved locally during extraction as
   `/tmp/vercel_july_article.txt`). Every `Quote` field in this note is
   taken from that locally-parsed verbatim text.
2. **Author names and publish date verified independently of WebFetch.**
   `datePublished: 2026-07-13T00:00-07:00` and the "Contributors: Eric
   Dodds, Jerilyn Zheng" byline were both located directly in the fetched
   HTML (a `BlogPosting` JSON-LD block for the date; the parsed article
   text's own "Contributors" section for the authors), not inferred from
   the WebFetch summary.
3. **No sub-pages followed.** The post links to the prior "May 2026" and
   "June 2026" installments (the latter is the May-2026-data report already
   in this corpus as `blog-vercel-ai-gateway-production-index-may2026.md`);
   both are separate, already-mined or out-of-scope sources in their own
   right and were not re-fetched. MINER.md's "follow up to 5 linked pages"
   guidance applies to substantive supporting pages within scope of the
   current source, not prior installments of the same recurring series.
4. **Filename note**: this note is filed as
   `blog-vercel-ai-gateway-production-index-june2026.md` (naming by the
   *data month*, June 2026) rather than by the URL's "july-2026" publish-month
   slug, for consistency with `blog-vercel-ai-gateway-production-index-may2026.md`'s
   existing convention (that note's source URL slug is "june-2026," its
   data month is May 2026, and it is filed as "-may2026.md").
5. **Three duplicate Prospector triage comments** appeared on issue #2646
   with broadly consistent but not identical chapter-relevance lists (Ch01/Ch03/Ch04
   vs. Ch02/Ch04) — a known corpus pattern from automated re-triage runs,
   also documented in several other recent source notes' Extraction Notes.
   None of the three individually matched this Miner's own reading of the
   content once the full article was fetched, so the Guide Impact section
   above was built from the extracted claims directly rather than from any
   single triage comment's chapter list.
6. **No contradiction issues filed.** Cross-referenced against the May
   installment of this same series, the GLM 5.2 capability-benchmark note,
   and the full Fable 5 launch/suspension/restoration timeline currently in
   the corpus; found no claim here that materially opposes an existing
   note's claim in a way that would drive different guide advice (see
   Cross-References → Contradicts for the one month-over-month value change
   considered and ruled out as a non-contradiction).
7. **Confidence calibration: emerging.** Most individual claims are rated
   "settled" because they are direct, first-party measured routing/spend/generation
   percentages from the platform operator. The overall note is rated
   "emerging" rather than "settled," matching the May installment's
   calibration and for the same reasons: (a) the dataset is limited to
   Vercel AI Gateway traffic specifically, an unquantified and
   unrepresentative-by-definition slice of total AI market activity; (b)
   Claim 7's price-flattening mechanism is Vercel's own interpretive
   decomposition of an aggregate trend, not an independently audited
   attribution; and (c) the post's own forward-looking extrapolation ("on
   current trajectories, an open-weight lab will soon be the second-largest
   by volume") is explicitly a projection, not a measured fact, and is
   flagged as such in Claim 3's assessment rather than treated as settled.
