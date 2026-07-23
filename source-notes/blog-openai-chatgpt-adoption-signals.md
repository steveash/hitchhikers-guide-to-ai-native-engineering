---
source_url: https://openai.com/index/how-chatgpt-adoption-has-expanded
source_type: blog-post
title: "How ChatGPT adoption has expanded"
author: OpenAI
date_published: 2026-06-30
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: emerging
issue: "#2166"
---

# How ChatGPT adoption has expanded

> A short OpenAI "Signals" data-visualization post arguing that ChatGPT usage
> is deepening (existing users send more messages and try more distinct
> capabilities over time) and broadening (adoption is growing fastest in
> Africa, Asia, and lower-Human-Development-Index countries; the user base is
> now majority non-male-name and majority non-English). The post covers
> Individual ChatGPT plans only (Free, Go, Plus, Pro) — it says nothing about
> Enterprise, Team, API, or agentic/Codex usage, and is a consumer-adoption
> companion piece to OpenAI's developer- and organization-facing adoption
> posts already in the corpus.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`; short,
  data-visualization-led piece built around four embedded interactive
  charts, each with its own methodology caption). Unsigned, published under
  OpenAI's own domain. Part of "OpenAI Signals," described in the post as
  "an ongoing effort to ensure that researchers and policymakers have the
  best data at their fingertips to understand how AI is affecting and will
  impact the economy."
- **Author credibility**: First-party vendor telemetry about the vendor's
  own consumer product, presented without independent audit. Unlike the
  post's own thin narrative text, each chart in this piece carries a
  detailed methodology caption (sample definition, date windows, exclusion
  criteria), which is more methodological transparency than typical OpenAI
  adoption posts in this corpus (contrast with
  `blog-openai-agents-transforming-work.md`, which discloses no methodology
  for its telemetry figures). OpenAI also states the underlying dataset is
  downloadable by outside researchers (`openai.com/signals/data-download/`),
  which is a meaningful, checkable claim — though this note does not
  independently verify the download or attempt to reproduce the charts from
  the raw data.
- **Scope**: Covers Individual ChatGPT plans (Free, Go, Plus, Pro) only —
  the post explicitly excludes Enterprise, Team, and API usage from this
  analysis. Covers: within-user usage depth/breadth over the user lifecycle,
  regional and Human-Development-Index-tier growth in weekly active users
  since July 2023, name-inferred gender distribution of usage by country,
  and language distribution of usage (English vs. non-English, plus
  fastest-growing individual languages). Does NOT cover: absolute user
  counts, revenue, retention/churn, task-category breakdowns (contrast with
  the Codex-focused posts in this corpus), any organizational/enterprise
  adoption data, or comparison to competing chatbot products.

## Extracted Claims

### Claim 1: Six months after signing up, ChatGPT users send 50% more messages per day and have tried twice as many distinct capabilities as they had at signup
- **Evidence**: A cohort analysis from a 0.1% sample of users whose accounts
  were created between 2025-10-15 and 2026-05-01, tracked through
  2026-05-31, using a 53-category message classifier to measure "breadth"
  and message volume to measure "depth."
- **Confidence**: emerging (a specific, dated cohort statistic with a
  disclosed sample fraction, date window, and classifier methodology — more
  methodologically transparent than most first-party vendor telemetry in
  this corpus — but still unaudited and the classifier's accuracy is not
  characterized)
- **Quote**: "Six months after signing up, users sent 50% more messages per day than they did when they signed up. They also doubled the number of distinct tasks they've tried on ChatGPT."
- **Our assessment**: This is the post's clearest within-user evidence for
  a "deepening engagement" thesis, comparable in spirit to
  `blog-openai-agents-transforming-work.md` Claim 3 (task-length thresholds
  crossed by individual Codex users), but measuring a different product
  (consumer ChatGPT, not Codex) and a different behavior (message
  frequency and task-category breadth, not task duration). The two should
  not be conflated — this is evidence of habit formation and capability
  discovery in a chatbot product, not evidence of longer-horizon agentic
  delegation.

### Claim 2: ChatGPT weekly-active-user growth since July 2023 has been fastest, in relative terms, in Africa and Asia
- **Evidence**: A regional growth-index chart plotting each continent's
  change in weekly active users relative to that continent's own July 2023
  baseline (countries where ChatGPT does not operate, and users under 18,
  are excluded).
- **Confidence**: emerging (a relative-growth-index chart with disclosed
  baseline and exclusion methodology, but "relative to baseline" figures
  can be large off a small base — the post gives no absolute user counts by
  region, so the magnitude of the underlying shift is not assessable from
  this post alone)
- **Quote**: "ChatGPT adoption has grown sharply across every continent since July 2023. In relative terms, the fastest growth has been in Africa and Asia."
- **Our assessment**: Directionally novel to our corpus — no existing
  source note contains continent-level ChatGPT adoption growth data. The
  "relative terms" caveat in the post's own text is important: this is
  explicitly not a claim about which regions have the most absolute users,
  only which regions are growing fastest off their own starting point,
  which is a materially weaker claim than it first appears.

### Claim 3: Lower-Human-Development-Index countries have seen the fastest relative growth in weekly active ChatGPT users since July 2023, a pattern OpenAI attributes partly to its free and low-cost (Go) plans
- **Evidence**: A growth-index chart grouping countries by 2023 HDI
  category, each indexed to its own July 2023 baseline, with the same
  active-user and exclusion definitions as Claim 2.
- **Confidence**: emerging (disclosed grouping methodology and baseline,
  but no absolute figures given, and the causal attribution to free/Go-plan
  pricing is the post's own interpretive claim, not something the chart
  itself demonstrates)
- **Quote**: "A similar pattern appears across country-development groupings: lower-Human Development Index (HDI) countries have seen the fastest relative growth in weekly active users since July 2023. OpenAI has continued to provide low-cost access to ChatGPT through our free and Go plans."
- **Our assessment**: The pricing-drove-adoption inference is plausible but
  unsupported by the chart itself — the post juxtaposes the growth data
  with a sentence about its own pricing strategy without presenting any
  data connecting the two (e.g., adoption timing versus Go-plan
  availability by country). Treat the HDI growth pattern as reasonably
  well-evidenced and the pricing-causation framing as an unverified,
  self-serving inference from the vendor.

### Claim 4: Users with typically-female names now represent most ChatGPT usage globally, with the most female-skewed usage in Brazil, Colombia, Poland, and Namibia, and the most male-skewed usage in Pakistan, Bangladesh, Angola, the Democratic Republic of Congo, and Mali
- **Evidence**: A name-to-gender crosswalk applied to active users (7-day
  window preceding month-start), excluding users under 18, users with
  non-classifiable names, and countries where at least half of active
  users' names cannot be classified.
- **Confidence**: emerging (the post is explicit that this is a proxy
  measure — "our best estimate of how many people with typically feminine
  or masculine names are using ChatGPT since we do not collect information
  on users' gender" — not a direct gender measurement, and name-to-gender
  crosswalks carry well-known cultural and regional accuracy limitations
  that the post does not characterize or quantify)
- **Quote**: "Usage by people with typically-female names has increased, now representing most usage globally. Brazil, Colombia, Poland, and Namibia rank among the countries where messages sent by users with typically feminine names most significantly exceed users with typically masculine names. In contrast, Pakistan, Bangladesh, Angola, the Democratic Republic of Congo, and Mali have the most concentrated usage by those with typically masculine names."
- **Our assessment**: Novel to our corpus — no existing source note
  contains demographic (gender-proxy) adoption data for any AI product.
  The self-disclosed proxy-measurement caveat is a point in the post's
  favor (it does not overclaim a direct gender measurement), but the
  country-level rankings should be read as illustrative extremes from a
  noisy classifier, not precise shares — the post gives no confidence
  intervals or classifier accuracy rate.

### Claim 5: Users predominantly writing in a language other than English now represent over half of active ChatGPT users, led by Spanish, Portuguese, and Arabic
- **Evidence**: Language-share chart assigning each user's primary language
  from their most recent message-classification profile, over the 7 days
  preceding each month's start, users 18+.
- **Confidence**: emerging (disclosed classification and time-window
  methodology, but the underlying per-message language classifier's
  accuracy is not characterized)
- **Quote**: "Non-English ChatGPT usage grew alongside global usage. Users predominantly using a language other than English now represent over half of active users. The leading non-English languages on ChatGPT are Spanish, Portuguese, and Arabic."
- **Our assessment**: A significant, specific crossover claim (English
  usage is now a minority of active users) that is plausible given Claims
  2-3's regional growth pattern, and internally consistent with them — a
  product growing fastest in Africa, Asia, and lower-HDI countries would
  be expected to cross this threshold. Novel to our corpus; no existing
  note tracks language distribution for any AI product's user base.

### Claim 6: Among languages with at least 1 million active users as of June 2026, Uzbek, Kazakh, and Burmese had the largest percentage-point increase in their share of active ChatGPT users since July 2023
- **Evidence**: A language-share-growth chart, each series indexed to its
  own July 2023 share, restricted to languages clearing the 1-million-active-user
  threshold in June 2026.
- **Confidence**: emerging (disclosed threshold and indexing methodology,
  but — as with Claim 2 — an indexed "share growth" figure for
  lower-starting-share languages can look dramatic off a small base; the
  post gives no absolute share percentages for these three languages)
- **Quote**: "Uzbek, Kazakh, and Burmese were the languages with the largest percentage increase in their share of active users since July 2023."
- **Our assessment**: A specific, checkable, and narrow claim (three named
  languages, a named threshold, a named date range) that is novel to our
  corpus. Its guide relevance is low on its own — it is a granular
  data point about consumer-language adoption, not a claim about
  engineering practice — but it corroborates the broader "adoption is
  growing fastest outside the traditional US/Western-Europe/English-language
  core" pattern running through Claims 2, 3, and 5.

### Claim 7: This analysis covers only Individual ChatGPT plans (Free, Go, Plus, Pro) — it explicitly excludes Enterprise, Team, and API usage
- **Evidence**: The post's own scope statement, given in its second
  paragraph before any chart is presented.
- **Confidence**: settled (a direct, unambiguous scope disclosure by the
  source itself)
- **Quote**: "Using aggregated data, OpenAI Signals measures how people interact with Individual ChatGPT plans (these include Free, Go, Plus, and Pro plans) over time. This analysis offers a view into how Individual AI usage is evolving as ChatGPT reaches global scale."
- **Our assessment**: This scope boundary is the single most important
  fact for correctly citing this source — every other claim in this note
  describes consumer/individual usage, not organizational or developer
  usage, and must not be cited as evidence about enterprise AI adoption,
  workplace deployment, or agentic/Codex usage. This is a different
  population from every other OpenAI adoption post already in the corpus
  (`blog-openai-agents-transforming-work.md`,
  `blog-openai-codex-knowledge-work.md`,
  `blog-openai-samsung-chatgpt-codex-deployment.md`,
  `blog-openai-bbva-banking-transformation.md`), all of which describe
  Codex or organizational/enterprise deployments rather than Individual-plan
  consumer chatbot usage.

## Concrete Artifacts

```
Source: OpenAI, "How ChatGPT adoption has expanded,"
https://openai.com/index/how-chatgpt-adoption-has-expanded (June 30, 2026)

Within-user engagement growth (0.1% sample, signups 2025-10-15 to
2026-05-01, tracked through 2026-05-31), 6 months post-signup vs. signup:
  Depth  (messages/day):        +50%
  Breadth (distinct capabilities, of 53 classifier categories): 2x

Regional weekly-active-user growth since July 2023 (relative to each
region's own July 2023 baseline):
  Fastest: Africa, Asia

Growth by 2023 Human Development Index (HDI) tier since July 2023:
  Fastest: lower-HDI countries
  (OpenAI attributes this partly to Free/Go low-cost plans — not
  independently demonstrated by the chart itself)

Name-inferred gender skew by country (messages sent, name-to-gender
crosswalk proxy, users 18+):
  Most female-name-skewed:  Brazil, Colombia, Poland, Namibia
  Most male-name-skewed:    Pakistan, Bangladesh, Angola,
                            Democratic Republic of Congo, Mali
  Global pattern: typically-female-name usage now represents most usage
  globally

Language share (users 18+, 7-day window preceding month start):
  Non-English share of active users: now >50%
  Leading non-English languages: Spanish, Portuguese, Arabic
  Fastest-growing share since July 2023 (languages with >=1M active
  users, June 2026): Uzbek, Kazakh, Burmese

Data access: raw ChatGPT usage data described as downloadable by
researchers at openai.com/signals/data-download/ (not independently
verified or fetched for this note).
```

## Cross-References

- **Corroborates**: None directly — no existing source note covers
  consumer/Individual-plan ChatGPT usage, regional adoption, demographic
  proxies, or language distribution, so there is nothing in the corpus for
  this post's specific claims to corroborate. The general high-level
  "AI adoption is growing fast and broadening beyond its original core
  user base" direction is consistent with the non-developer-adoption
  trend documented for Codex in `blog-openai-codex-knowledge-work.md`
  (Claims 2-3, non-developer and personal-user growth outpacing
  developers) and `blog-openai-agents-transforming-work.md` (Claim 7,
  non-developer growth multipliers), but those posts measure a different
  product (Codex) and a different axis of "broadening" (developer vs.
  non-developer role, not geography/language/demographics), so this is
  a parallel finding rather than a restated one.
- **Contradicts**: None identified.
- **Extends**: `blog-addyosmani-new-software-lifecycle.md` Claim 16 (85% of
  professional developers use AI coding agents regularly, 51% daily, ~41%
  of new code AI-generated) describes a completely different population
  (professional software developers) from this post's Individual ChatGPT
  consumer base — the two are not comparable statistics and should not be
  cited together as if measuring the same adoption phenomenon. This note
  is best read as extending the corpus's adoption-statistics coverage into
  a population (global consumer, non-developer, non-organizational) that
  the guide's existing adoption sources do not touch, rather than
  reinforcing or updating any existing developer-adoption figure.
- **Novel**: The entire regional (Claim 2), HDI-tier (Claim 3),
  demographic-proxy (Claim 4), and language-distribution (Claims 5-6) data
  is new to our corpus — this is the first source note to cover
  geographic, socioeconomic, or demographic breadth of any AI product's
  adoption, as opposed to developer/organizational adoption depth. The
  within-user depth/breadth cohort methodology (Claim 1) is also a new
  measurement approach in the corpus (classifier-based "distinct
  capabilities tried" as a breadth metric), distinct from the
  task-duration and token-share metrics used in the corpus's existing
  Codex-adoption notes.

## Guide Impact

- **Chapter 00 (Principles)**: The scope-bounded framing in Claim 7, plus
  the regional/demographic breadth in Claims 2-6, supports a single
  contextual point: AI assistant adoption is no longer a US/English-language/developer
  phenomenon but a global consumer one, crossing a non-English-majority
  threshold (Claim 5) as of this post. This is background market context
  for why "AI-native" is a global baseline assumption, not evidence for any
  specific engineering practice — cite briefly, if at all, as scene-setting
  rather than as an actionable recommendation.
- **No other chapter should draw specific guidance from this source.** This
  post's population (Individual ChatGPT consumer plans) does not overlap
  with the guide's core subject matter (professional software engineering
  teams building with agentic tools). The triage comments for this issue
  suggested possible relevance to Ch02/04/05/07 (adoption patterns, team
  adoption, practitioner workflows), but on full reading none of this
  post's content — consumer chatbot usage depth, regional growth,
  name-inferred demographics, or language share — describes engineering
  teams, harnesses, workflows, or organizational deployment practices. We
  recommend the guide not cite this source for team-adoption or
  practitioner-workflow claims; it is a consumer-market-signal piece, not
  a practitioner or organizational-deployment source like the Codex- and
  case-study-focused OpenAI posts already in the corpus.

## Extraction Notes

- The live OpenAI URL returned an HTTP 403 with a Cloudflare bot challenge
  (`cf-mitigated: challenge` header) to both `WebFetch` and direct `curl`
  with a browser user-agent — the same access pattern already documented
  for OpenAI's `index/` blog in
  `blog-openai-agents-transforming-work.md`. The article was retrieved in
  full via the `r.jina.ai` reader proxy, which returned the complete page
  converted to Markdown, including every heading, paragraph, chart
  caption, and the closing "Learn more" section. Every quote above was
  checked character-for-character against that fetched Markdown.
- The post is built around four embedded interactive charts. The reader-proxy
  Markdown conversion preserved each chart's methodology caption (which is
  prose, not chart data) but not the underlying chart datasets themselves
  (no data tables, axis values, or per-country/per-language numeric values
  were recoverable as text). All claims above are therefore drawn from the
  post's own prose descriptions of what each chart shows, not from
  independently read chart data — this is flagged per claim above via the
  "relative terms, no absolute figures" caveats on Claims 2, 3, and 6.
  A future extraction with browser-based chart access (or by fetching the
  downloadable dataset linked at the end of the post) could recover the
  actual per-region, per-country, and per-language figures and would be a
  meaningfully stronger version of this note.
- The post contains one footnote marker (`[1]`, linking to a
  `#citation-bottom-1` anchor on the same page) attached to the gender-proxy
  claim (Claim 4). As with the footnote markers found in
  `blog-openai-agents-transforming-work.md`, this anchor did not resolve to
  visible footnote text in the reader-proxy extraction; no footnote content
  was fabricated to fill this gap, and the footnote marker's presence is
  noted here rather than silently dropped.
- No contradiction with any existing source note was found during
  cross-referencing (see Cross-References → Contradicts), so no
  contradiction issue was filed per MINER.md §4a.
- This source is thinner than the typical corpus entry — a ~500-word post
  built around four charts, versus the multi-thousand-word reports typical
  of the OpenAI Codex-adoption posts already mined. Seven claims were
  extracted, at the lower end of MINER.md's 5-15 target range, because the
  underlying post genuinely contains seven distinct factual assertions and
  no more; padding beyond that would mean restating the same regional-growth
  finding (Claims 2-3) or language finding (Claims 5-6) as separate claims,
  which was avoided.
