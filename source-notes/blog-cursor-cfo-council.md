---
source_url: https://cursor.com/blog/cfo-council
source_type: blog-post
title: "CFOs and the new economics of AI"
author: Jordan Topoleski (Cursor / Anysphere)
date_published: 2026-07-06
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: emerging
issue: "#1633"
---

# CFOs and the New Economics of AI

> Cursor announces a quarterly "CFO Council" for finance leaders and uses the
> announcement to publish first-party product-usage statistics on AI economics:
> a Jevons-style usage-growth dynamic following model upgrades, extreme
> concentration of AI-driven output and spend among top-percentile users (Gini
> coefficient more unequal than any national income distribution), 7-9x cost
> variance per unit of AI work across model families, and 84% of power users
> already routing across multiple models weekly — framed against a McKinsey
> stat that 88% of organizations have deployed AI but only 39% can trace it to
> EBIT impact.

## Source Context

- **Type**: blog-post (Cursor/Anysphere company blog, "Company" category,
  published July 6, 2026; ~4 minute read; auto-discovered via the trusted
  `cursor-blog` RSS feed)
- **Author credibility**: Jordan Topoleski, bylined author on Cursor's own
  blog — a first-party vendor announcement, not an independent analysis. The
  post's primary purpose is announcing a product/community initiative (the
  Cursor CFO Council); the economics statistics are used to justify why the
  council exists. Most of the quantitative claims are drawn from Cursor's own
  internal product telemetry (the "Developer Habits Report," referenced but
  not linked or dated within this article) or from third-party analyses that
  used Cursor's data (a BCG study, a separate unnamed "study of Cursor
  usage"). No methodology, sample size, or time window is disclosed for any
  of the cited statistics within this article itself — treat all figures as
  vendor-published summary numbers, not independently verifiable research.
  The McKinsey adoption/impact-gap statistic is attributed secondhand ("a
  recent McKinsey study") with no link or report title given.
- **Scope**: Covers the launch of the Cursor CFO Council (a quarterly
  finance-leader working group), a BCG revenue-growth correlation with token
  usage, a Jevons-style usage-growth finding tied to late-2025 model
  upgrades, concentration statistics from Cursor's "Developer Habits Report"
  (p99 vs. median output and PR throughput, Gini-coefficient concentration of
  spend/tokens/AI-generated code), cost-per-unit-of-work variance across
  model families, and the rate of multi-model adoption among power users.
  Does NOT cover: any technical detail of how "power user," "high-complexity
  work," or "accepted line" are defined; the actual Gini coefficient value;
  which McKinsey report is being cited; the BCG report's methodology or
  publication; or any named company/customer case study. No sub-pages were
  linked from the article; it is a single, short, self-contained post with no
  inline citations to the primary reports it references (Developer Habits
  Report, BCG analysis, McKinsey study).

## Extracted Claims

### Claim 1: AI spend has shifted from experimental pilots into a major recurring operating expense, reaching $1.5 trillion globally in 2025
- **Evidence**: Opening framing statement, presented without a citation or link to the underlying spend estimate.
- **Confidence**: anecdotal (specific aggregate figure asserted with no source, methodology, or link given within the article)
- **Quote**: "AI spend is shifting from experimental pilots into a major recurring operating expense that reached $1.5 trillion globally in 2025."
- **Our assessment**: The $1.5 trillion figure is stated as established fact but is unsourced within this article. It is directionally consistent with the broader "AI spend is now a major line item" narrative already in the corpus (e.g., the Tokenomics Foundation's formation and Goldman Sachs's 2026-2030 usage forecast in `blog-thoughtworks-kamelman-token-crisis.md` Claims 10-11), but should not be cited in the guide as an independently verified number — only as Cursor's framing for why it is launching the CFO Council.

### Claim 2: A McKinsey study found 88% of organizations have deployed AI in at least one business function, but only 39% can trace that investment to enterprise-level EBIT impact
- **Evidence**: Secondhand citation of an unnamed, unlinked McKinsey study, used as the article's central justification for the adoption/impact gap.
- **Confidence**: emerging (attributed to a named, credible research organization, but the specific report is not linked or titled, so it cannot be independently verified within this extraction)
- **Quote**: "88% of organizations have deployed AI in at least one business function, but only 39% can trace that investment to enterprise-level EBIT impact."
- **Our assessment**: This exact statistic also appears, independently cited, in the Prospector's triage comment on this issue and is consistent with (though not identical in wording to) the general "deployment outpaces measurable value" thesis already present in this corpus via `blog-anthropic-admin-analytics-cost-controls.md` (per-team cost-vs.-impact reporting tooling) and `blog-thoughtworks-kamelman-token-crisis.md` Claim 1 ("no one owns the aggregate" outcome). It is the clearest single statistic in this article and the one most likely to be independently checkable if the guide wants to cite McKinsey directly — the guide should locate and cite the primary McKinsey report rather than this secondhand mention.

### Claim 3: Cursor is launching the "Cursor CFO Council," a quarterly working group of finance leaders meeting in rotating cities, organized around the question of how to keep AI spend tied to value
- **Evidence**: Direct first-party product/community announcement — the article's stated purpose.
- **Confidence**: settled (a concrete, verifiable action being announced by the company making the announcement, not a measured research finding)
- **Quote**: "That is why we are launching the Cursor CFO Council, a working group of finance leaders focused on answering a single question: How do you keep AI spend tied to value?"
- **Our assessment**: This is the article's actual news content; everything else in the post is supporting rationale. The council's first meeting is stated to occur in August 2026, with Cursor planning to "publish updates on the group's work." This is a new, named industry body for AI economics — comparable in kind (though not scope) to the Tokenomics Foundation documented in `blog-thoughtworks-kamelman-token-crisis.md` Claim 10, except vendor-hosted (Cursor) rather than standards-body-hosted (Linux Foundation), and focused on ROI/value framing rather than cost-measurement standards. Worth flagging for the Prospector to queue a follow-up source once the council publishes its first output.

### Claim 4: A BCG analysis using Cursor data found companies in the highest quintile of token usage saw 16.5% median year-over-year revenue growth, compared to 5.1% for companies in the lowest quintile
- **Evidence**: Third-party analysis (Boston Consulting Group) using Cursor's own usage data, cited without a link to the BCG report.
- **Confidence**: emerging (attributed to a named, credible third-party research firm rather than Cursor itself, which reduces vendor self-interest bias somewhat, but the report is not linked, and no detail is given on causality, sample composition, or how "highest/lowest quintile of token usage" was defined)
- **Quote**: "A recent BCG analysis using Cursor data found that companies in the highest quintile of token usage saw 16.5% median year-over-year revenue growth compared to 5.1% for companies in the lowest quintile."
- **Our assessment**: This is a correlational finding, not a causal one — the article does not claim (and this note does not assume) that high token usage *causes* higher revenue growth; companies already growing faster may simply also be heavier AI adopters. This is the concrete, named-firm complement to the "4% revenue lift" anecdote in `blog-anthropic-admin-analytics-cost-controls.md` Claim 9 (a single customer's self-reported, unaudited figure) — the BCG figure is broader (quintile-level, multi-company) but still lacks a disclosed methodology or link to the primary report.

### Claim 5: Following major model improvements in late 2025, Cursor workers sent 44% more agent messages per week overall, with the largest increase (68%) coming from high-complexity work — consistent with a Jevons-style dynamic where usage rises with capability rather than falling
- **Evidence**: Cited as "a separate study of Cursor usage," unnamed and unlinked within this article.
- **Confidence**: emerging (the exact figures — 44% overall usage growth, 68% growth for high-complexity work — match the peer-partnered Cursor/UChicago Booth SSRN study already extracted in this corpus; see Cross-References)
- **Quote**: "A separate study of Cursor usage found that following major model improvements in late 2025, workers sent 44% more agent messages per week. The largest increase came from high-complexity work, where messages rose 68%." Followed by: "Better models are expanding the set of work teams are willing to attempt, pointing to a Jevons-style dynamic where usage tends to rise with capability rather than fall."
- **Our assessment**: The "44%" and "68%" figures are identical to the headline numbers in `blog-cursor-better-models-ambitious-work.md` (the Cursor + UChicago Booth study covering July 2025-March 2026, Claims 1 and 3), which reported "+44% weekly messages per user" overall and "+68%" growth for high-complexity messages. This article does not name that study or link to it, but the figures are specific enough that this is very likely the same underlying dataset being restated here without attribution to its own publication, rather than an independent replication. The guide should treat this as the same evidence, not as independent corroboration from a second study — see Cross-References.

### Claim 6: Cursor's Developer Habits Report found p99 developers produced 46x more AI-assisted lines of code per day than the median active user, and merged 15x more pull requests per week than the median active pull-request author
- **Evidence**: First-party product-usage-log statistics from Cursor's "Developer Habits Report" (named but not linked or dated in this article).
- **Confidence**: settled (concrete, first-party product-telemetry figures, though the underlying report itself is not linked for independent verification)
- **Quote**: "Our recently released Developer Habits Report found that p99 developers produced 46x more AI-assisted lines per day than the median active user and merged 15x more pull requests per week than the median active pull request author."
- **Our assessment**: This is the article's sharpest concentration statistic and a genuinely new data point for the corpus: no existing source note quantifies the *ratio* between top-percentile and median AI-assisted output at this magnitude (46x for lines/day, 15x for merged PRs/week). It substantiates the article's framing that "AI adoption" as an aggregate org-wide metric can obscure a small number of people capturing nearly all of the productivity leverage.

### Claim 7: Concentration of AI spend, token consumption, and AI-generated code — measured by Gini coefficient — is more unequal than income distribution in any country in the world
- **Evidence**: First-party statistical claim from the same Developer Habits Report dataset, stated as a direct comparison to a well-known inequality metric.
- **Confidence**: emerging (a specific, checkable-in-principle statistical claim, but the article gives no actual Gini coefficient value, no comparison dataset, and no country-by-country reference points — "more unequal than any country in the world" is a strong universal claim asserted without supporting data)
- **Quote**: "We observed similar concentration around spend, token consumption, and AI-generated code. Measured by Gini coefficient, these distributions are more unequal than income distribution in any country in the world."
- **Our assessment**: This is a striking, quotable framing, but it is the weakest-sourced quantitative claim in the article — no Gini value is disclosed (the most unequal national income Gini coefficients on record are in the high 0.5s-0.6s; without a number, the reader cannot judge how much more unequal AI usage distribution is). Paired with Claim 6's p99/median ratios, it strongly reinforces the "small number of people capture nearly all of the leverage" thesis, but the guide should present it as a directional, vendor-reported finding rather than a precise, sourced statistic.

### Claim 8: Cost per agent request varied by nearly 9 times across model families, while cost per accepted line varied by roughly 7 times, in Cursor's Developer Habits Report
- **Evidence**: First-party product billing/usage-log statistics from the same Developer Habits Report.
- **Confidence**: settled (concrete, first-party billing-derived figures)
- **Quote**: "In the Developer Habits Report, cost per agent request varied by nearly 9 times across model families, while cost per accepted line varied by roughly 7 times."
- **Our assessment**: This is the article's most directly actionable cost-governance statistic — a quantified range for how much cost-per-unit-of-work can vary purely from model selection, independent of task volume. It gives concrete numeric grounding to the "route work to the right model" advice already present in the corpus via `blog-thoughtworks-kamelman-token-crisis.md` Claim 8 (unrouted premium-model usage as a waste pattern) and `blog-vercel-ai-gateway-production-index-may2026.md` Claim 5 (the 49%/4% vs. 28%/70% DeepSeek/Anthropic coding-agent volume/spend split) — this article supplies the "why it matters" multiplier (7-9x) that those two sources illustrate with real routing outcomes but do not themselves quantify as a single variance figure.

### Claim 9: 84% of Cursor power users already use multiple models each week, because different models are better suited to different kinds of work (planning, frontend development, debugging, lower-cost execution)
- **Evidence**: First-party product-usage statistic, presented alongside the cost-variance figures as the practical response to Claim 8's cost gap.
- **Confidence**: settled (concrete, first-party usage-log figure)
- **Quote**: "Different models are better for different kinds of work — planning, frontend development, debugging, lower-cost execution — and in Cursor, 84% of power users already use multiple models each week."
- **Our assessment**: This directly corroborates and adds a user-level percentage to `blog-vercel-ai-gateway-production-index-may2026.md` Claim 10 (at 1M+ monthly requests, most production apps route across 11 or more distinct models). Where the Vercel note measures multi-model routing at the *application/infrastructure* level (across an org's aggregate traffic), this article measures it at the *individual power-user* level (84% of a named user segment personally switching models weekly) — together the two sources show the same multi-model-routing pattern holding at both the individual workflow layer and the aggregate production-traffic layer.

### Claim 10: As AI providers move toward usage-based pricing, model/provider optionality becomes more valuable because it turns intelligence from a predictable cost into a variable one that is harder to forecast
- **Evidence**: Author's own forward-looking interpretive claim, presented as the article's synthesis of the cost-variance and multi-model-adoption findings (Claims 8-9).
- **Confidence**: anecdotal (interpretive/predictive claim, not a measured finding)
- **Quote**: "That optionality is becoming more important as AI providers move toward usage-based pricing, which turns intelligence into a variable cost that is harder to predict."
- **Our assessment**: This is a reasonable inference from Claims 8-9 rather than new evidence, but it is a useful bridge for the guide: it connects the "route to the cheapest adequate model" tactic (already documented via cost-governance sources) to the *strategic* reason optionality matters — as pricing becomes more usage-based across the industry (a trend independently documented in `blog-vercel-ai-gateway-production-index-may2026.md`'s DeepSeek-entry data and `blog-thoughtworks-kamelman-token-crisis.md`'s Goldman Sachs usage-growth forecast), predictable-cost planning depends on maintaining multiple viable model/provider options rather than single-vendor commitment.

## Concrete Artifacts

### Key statistics (verbatim figures, as published in the article)

```
CFOs and the new economics of AI — Cursor / Jordan Topoleski, July 6, 2026
Source: https://cursor.com/blog/cfo-council

MARKET CONTEXT
  Global AI spend (2025):                    $1.5 trillion
  Orgs that have deployed AI in >=1 function: 88% (McKinsey)
  Orgs that can trace it to EBIT impact:      39% (McKinsey)

REVENUE CORRELATION (BCG analysis using Cursor data)
  Highest quintile token usage -> revenue growth (YoY, median): 16.5%
  Lowest quintile token usage  -> revenue growth (YoY, median):  5.1%

USAGE GROWTH AFTER MODEL IMPROVEMENTS (late 2025; "separate study of Cursor usage")
  Overall agent messages/week:      +44%
  High-complexity work messages:    +68%

CONCENTRATION (Cursor Developer Habits Report)
  p99 developers vs. median: AI-assisted lines/day        46x
  p99 developers vs. median: merged pull requests/week    15x
  Spend / token consumption / AI-generated code concentration:
    "more unequal than income distribution in any country in the world"
    (measured by Gini coefficient; no numeric value disclosed)

COST VARIANCE (Cursor Developer Habits Report)
  Cost per agent request, across model families:   ~9x variance
  Cost per accepted line, across model families:    ~7x variance

MULTI-MODEL ADOPTION
  Power users using multiple models weekly: 84%

CFO COUNCIL
  Cadence: quarterly, rotating cities
  First meeting: August 2026
  Focus: shared productivity benchmarks, ROI measurement frameworks,
         model-allocation / cost-management practices
```

## Cross-References

### Cross-reference verification notes
Before writing the citations below, `blog-cursor-better-models-ambitious-work.md`,
`blog-vercel-ai-gateway-production-index-may2026.md`,
`blog-anthropic-admin-analytics-cost-controls.md`, and
`blog-thoughtworks-kamelman-token-crisis.md` were re-read directly (MINER.md
§4b) and the claim numbers cited below were confirmed against each note's
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-cursor-better-models-ambitious-work.md` Claim 1 (AI usage grew 44%
    over the 8-month study period, consistent with a Jevons-like demand
    expansion) and Claim 3 (high-complexity usage grew 68% vs. 22%
    low-complexity): this article's Claim 5 restates the identical 44%/68%
    figures without naming or linking the underlying study. Given the exact
    numeric match, this should be treated as the same evidence resurfacing in
    a second Cursor publication, not as independent replication — see "Our
    assessment" under Claim 5.
  - `blog-vercel-ai-gateway-production-index-may2026.md` Claim 10 (at 1M+
    monthly requests, most production apps route across 11 or more distinct
    models): this article's Claim 9 (84% of power users use multiple models
    weekly) corroborates the same multi-model-routing pattern from the
    individual-user side rather than the aggregate-application-traffic side.
  - `blog-anthropic-admin-analytics-cost-controls.md` Claim 9 (a named CIO's
    self-reported "4% revenue lift" tied to Claude usage, and the framing that
    "seeing cost next to business impact by team" is what satisfies a CFO):
    this article's Claim 4 (BCG's quintile-level 16.5% vs. 5.1% revenue growth
    split) is a broader, multi-company version of the same "tie AI spend to
    measurable business outcome" argument, and this article's Claim 3 (the
    CFO Council's founding question, "How do you keep AI spend tied to
    value?") is the same governance concern stated as an explicit
    organizational mission rather than a single customer anecdote.
  - `blog-thoughtworks-kamelman-token-crisis.md` Claim 1 ("no one [function]
    currently owns the aggregate" of token spend, now simultaneously a
    finance, engineering, and governance problem): this article's Claim 2 (the
    McKinsey 88%/39% adoption-vs.-impact gap) is a different framing of the
    same underlying diagnosis — organizations are spending on AI broadly but
    cannot consistently connect that spend to a measurable outcome owner.

- **Contradicts**: None identified. No claim in this article materially
  opposes an existing corpus note's claim in a way that would drive different
  guide advice. No contradiction issue filed.

- **Extends**:
  - `blog-thoughtworks-kamelman-token-crisis.md`: that note documents
    organizational and industry-level responses to token-cost pressure
    (budget blowouts at Uber/Microsoft, the Tokenomics Foundation, a Goldman
    Sachs usage-growth forecast) but does not address *within-organization*
    concentration of AI value capture. This article's Claims 6-7 (p99 vs.
    median output ratios; Gini-coefficient concentration of spend/tokens/code)
    add a distinct, previously undocumented dimension to the corpus's
    AI-economics coverage: even within a single adopting organization, AI
    value and cost are not evenly distributed across users, which has
    different governance implications (targeting enablement at power users,
    or investigating why most users see little benefit) than aggregate
    org-level budget overruns.
  - `blog-vercel-ai-gateway-production-index-may2026.md` Claim 5 (coding-agent
    use case: DeepSeek drives 49% of tokens at 4% of cost, Anthropic 28% of
    tokens at 70% of cost) and Claim 6 (average cost per token rose ~20%
    month-over-month even as a much cheaper model entered at scale): this
    article's Claim 8 (7-9x cost variance per unit of work across model
    families) supplies a general, cross-model-family multiplier that the
    Vercel note's provider-specific percentages illustrate but do not
    themselves state as a single variance figure — the two sources describe
    the same underlying cost-routing dynamic at different levels of
    abstraction (aggregate market-share data vs. a summary variance
    statistic).
  - `blog-anthropic-admin-analytics-cost-controls.md` Claim 2 (Claude Code's
    admin-console "Value" tab estimates cost-per-commit and productivity lift
    with visible, adjustable formulas): this article's cost-per-agent-request
    and cost-per-accepted-line variance figures (Claim 8) are the kind of
    concrete cost-per-unit-of-work inputs such an ROI dashboard would need to
    make legible — the two sources are complementary (one documents a tool
    for exposing this variance to admins, the other quantifies how large the
    variance actually is).

- **Novel**:
  - **p99-vs-median output ratios (46x lines/day, 15x merged PRs/week)**: no
    prior corpus source quantifies the ratio between top-percentile and
    median AI-assisted developer output at this level of specificity.
  - **Gini-coefficient framing for AI value/spend concentration**: no prior
    corpus source applies an explicit inequality metric (Gini coefficient) to
    AI usage, spend, or output concentration, or compares it to national
    income distribution.
  - **Cost-per-unit-of-work variance quantified as a single multiplier (9x
    per request, 7x per accepted line) across model families**: prior corpus
    sources on model-cost variance (`blog-vercel-ai-gateway-production-index-may2026.md`)
    document provider-specific percentage splits within named use cases;
    this is the first source to state variance as a single cross-model-family
    ratio.
  - **The Cursor CFO Council itself**: a new, named vendor-hosted industry
    working group for AI economics, distinct in structure from the
    standards-body model of the Linux Foundation's Tokenomics Foundation
    (`blog-thoughtworks-kamelman-token-crisis.md` Claim 10).
  - **BCG's quintile-level token-usage-to-revenue-growth correlation
    (16.5% vs. 5.1%)**: the first corpus source with a multi-company,
    quintile-segmented revenue-growth correlation tied to AI token usage
    intensity (as distinct from the single-customer revenue-lift anecdotes
    already documented).

## Guide Impact

- **Chapter on Governance and Cost Management**: Add the 7-9x cost-per-unit-of-work
  variance across model families (Claim 8) as a concrete, quotable multiplier
  justifying multi-model routing infrastructure, paired with the 84%
  power-user multi-model-adoption figure (Claim 9) and
  `blog-vercel-ai-gateway-production-index-may2026.md` Claim 10 (11+ models
  per app at scale) — together these three data points argue that
  single-model dependency is both a cost risk and a minority practice among
  both individual power users and mature production applications.

- **Chapter on Team Adoption / Measuring AI Impact**: Add the p99-vs-median
  concentration statistics (Claim 6: 46x lines/day, 15x merged PRs/week) and
  the Gini-coefficient framing (Claim 7) as a caution against org-wide
  "AI adoption rate" metrics that don't account for how unevenly the benefit
  is actually distributed. Recommend the guide explicitly note that a high
  aggregate adoption number can coexist with most users capturing little
  value — the McKinsey 88%/39% gap (Claim 2) is the organization-level
  version of the same distributional problem Claims 6-7 document at the
  individual-user level.

- **Chapter on Economics / ROI Measurement**: Add the McKinsey adoption/impact
  gap statistic (Claim 2) and the BCG quintile revenue-growth correlation
  (Claim 4) as two independent (though both secondhand-cited) anchors for
  discussions of the gap between AI deployment and demonstrated business
  value — flag both explicitly as unlinked secondary citations requiring
  independent verification before being presented as settled numbers, per
  this note's Source Context and per-claim confidence ratings.

- **Any chapter discussing Jevons-style demand-expansion dynamics**: Do not
  cite this article's Claim 5 (44%/68% usage growth) as a second, independent
  data point alongside `blog-cursor-better-models-ambitious-work.md` — the
  figures match exactly and almost certainly come from the same underlying
  study. Cite the original study note for methodology and confidence
  caveats; this article only adds the observation that Cursor is now
  restating those figures in a finance/economics context a few months later.

## Extraction Notes

- The article was fetched via WebFetch with a verbatim-extraction prompt. It
  is short (~4 minute read, five section headers) and appears fully
  self-contained — no inline links to the Developer Habits Report, the BCG
  analysis, the McKinsey study, or the "separate study of Cursor usage" were
  present in the fetched markdown, so none could be followed per MINER.md's
  "follow up to 5 linked pages" guidance. This is a real limitation: nearly
  every quantitative claim in this article depends on a primary report this
  note could not independently verify. If WebFetch's markdown conversion
  stripped inline links (a limitation observed and noted in other recent
  source notes, e.g. `blog-thoughtworks-kamelman-ai-governance-category-error.md`
  Extraction Note 4), a future pass with direct HTML access might recover
  them and should be prioritized if this article is revisited.
- The strongest single finding of this extraction is that Claim 5's
  44%/68% figures are very likely the same dataset already documented in
  `blog-cursor-better-models-ambitious-work.md`, restated here without
  attribution to the original SSRN-linked study. This is flagged prominently
  in Cross-References and Guide Impact so the Assayer/Smith do not
  double-count it as independent corroboration.
- No contradictions were found against the existing corpus and none were
  filed. The article's claims (adoption-impact gap, usage concentration,
  cost variance, multi-model adoption) are all directionally consistent with
  and additive to existing AI-economics and cost-governance source notes.
- `blog-anthropic-fong-finance-narrative.md` was checked (per the Prospector's
  triage comment listing it as a potentially overlapping note) but was found
  to have no substantive claim-level overlap with this article — Fong's note
  documents Claude tooling for finance-team internal workflows (board decks,
  reconciliations), while this article is about aggregate AI-spend economics
  and ROI measurement. Both are finance-function-adjacent but address
  different topics; no cross-reference was forced between them.
- Confidence overall is rated "emerging": a majority of the article's
  individual statistics are first-party, concrete, settled-confidence
  figures (Claims 3, 6, 8, 9), but the article's most attention-grabbing
  numbers (Claims 1, 2, 4, 7) are either unsourced, secondhand-cited without
  a link, or lack a disclosed methodology, which caps the overall confidence
  below "settled."
