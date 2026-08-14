---
source_url: https://openai.com/index/how-the-world-is-putting-chatgpt-to-work
source_type: blog-post
title: "From asking to doing: How the world is putting ChatGPT to work"
author: OpenAI (Economic Research Team)
date_published: 2026-08-06
date_extracted: 2026-08-14
last_checked: 2026-08-14
status: current
confidence_overall: emerging
issue: "#2694"
---

# From asking to doing: How the world is putting ChatGPT to work

> OpenAI's third "Signals" data post (following the June and Q1-2026
> country-ranking releases), publishing new country-by-country ChatGPT
> usage data for Q2 2026: at-work usage skews more than 2x toward "doing"
> (task completion) versus "asking" (information-seeking) compared to
> outside-work usage; the per-capita adoption gap is closing as Latin
> America, Africa, and Oceania catch up to early-adopter countries;
> multimedia is the fastest-growing use case (7.8% of messages globally,
> >10% in Brazil and Colombia); and usage among people over 35 is rising
> in nearly every country, most sharply in France and Czechia. As with the
> June Signals post already in the corpus, this is Individual-plan
> (Free/Go/Plus/Pro) data only — it says nothing about Enterprise, Team,
> API, or organizational ChatGPT Work usage.

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`; a
  data-visualization-led "OpenAI Signals" release built around four
  embedded charts — a per-capita country-rank-change map, a multimedia-share
  choropleth, an age-cohort trend line, and a per-country age-cohort-shift
  chart — each with its own methodology note). Unsigned at the byline
  level but explicitly attributed to "the OpenAI Economic Research Team"
  in the post's own text. Third entry in this Signals series that the
  corpus has now mined, after `blog-openai-chatgpt-adoption-signals.md`
  (June 2026) and the "Q1 2026 update" the post itself links to but this
  note did not separately fetch.
- **Author credibility**: First-party vendor telemetry about the vendor's
  own consumer product, presented without independent audit — the same
  credibility profile as `blog-openai-chatgpt-adoption-signals.md`. Each
  chart carries a disclosed sample/date-window/methodology caption (more
  transparent than typical OpenAI product-launch posts), and the post
  links a public methodology PDF (`cdn.openai.com/signals/data-dictionary.pdf`)
  and a public data-download page (`openai.com/signals/data-download/`),
  neither of which this note independently fetched or verified.
- **Scope**: Covers four Q2-2026 findings — work-vs-non-work task
  orientation ("doing" vs. "asking"), country-level per-capita adoption-rank
  change (Q1→Q2 2026), multimedia-message share by country, and
  self-reported-age-cohort (35+) share change by country and region. The
  dataset is explicitly scoped to "messages sent within ChatGPT Free, Go,
  Plus, and Pro accounts—the group of accounts generally managed by
  individuals rather than organizations." Does NOT cover: Enterprise, Team,
  API, or ChatGPT Work/Codex organizational usage; absolute per-country
  user counts (only per-capita rank changes and percentage-point shares are
  given); task-success or quality data; or any causal explanation for why
  specific countries (Peru, Uruguay, Costa Rica; France, Czechia) moved as
  much as they did.

## Extracted Claims

### Claim 1: OpenAI states that more than 1 billion people are now "putting ChatGPT to work"
- **Evidence**: The post's own framing sentence introducing the country-level
  dataset release.
- **Confidence**: emerging (a specific, if undated-methodology, aggregate
  scale figure, already independently corroborated elsewhere in the corpus)
- **Quote**: "These country-level statistics will help people, including policymakers and researchers around the world, better understand how more than 1 billion people are putting ChatGPT to work."
- **Our assessment**: This is an exact match to `blog-openai-building-abundant-intelligence.md` Claim 9 ("Our models now reach more than one billion active users and more than two million businesses," July 31, 2026) — the two posts, six days apart, state the identical aggregate figure with no methodology in either. Treat the >1B figure as a stable, repeated OpenAI public-messaging number rather than fresh evidence, since neither post discloses a sample definition or measurement date for it.

### Claim 2: At work, people are more than twice as likely to use ChatGPT to complete a task or create something (e.g., writing, coding, analysis) than they are outside work, where "asking" (seeking information or clarification) remains the largest category
- **Evidence**: A message-classification comparison of work-context versus
  non-work-context ChatGPT usage, described in the "At work, 'doing'
  dominates" section.
- **Confidence**: emerging (a specific, falsifiable ratio, but the post
  discloses no sample size, classifier accuracy, or definition of how a
  message is labeled "at work" versus "outside work")
- **Quote**: "Our data shows that, across the globe, people are more than twice as likely to use ChatGPT this way at work than outside of work. Outside of work, use is more exploratory: 'asking,' or seeking information and clarification, remains the largest category."
- **Our assessment**: This is the post's namesake claim and reads as a
  consumer-ChatGPT-usage-pattern counterpart to the "asking to doing"
  framing OpenAI has now used in at least two other posts for different
  products/populations: `blog-openai-building-abundant-intelligence.md`
  Claim 10 ("ChatGPT Work is changing what it means to be a knowledge
  worker... 'asking' to 'doing'" — describing the ChatGPT Work product
  specifically) and `blog-openai-agents-transforming-work.md` Claim 1
  (the "unit of knowledge work" shifting from short chatbot interactions to
  delegated agentic tasks — describing Codex). This post's version is
  narrower and more measurable than either: it is a message-classification
  split within ordinary ChatGPT (not Codex or ChatGPT Work specifically)
  comparing work-context to non-work-context messages, attributed
  explicitly to "the rollout of ChatGPT Work" as a contributing trend but
  not confined to ChatGPT Work usage.

### Claim 3: The global per-capita adoption gap is closing — countries in Latin America, Africa, and Oceania are catching up to early-adopter countries, with Peru, Uruguay, and Costa Rica rising the most in per-capita usage rank between Q1 and Q2 2026
- **Evidence**: A country-level messages-per-capita rank-change chart
  covering 144 countries, comparing Q1 2026 to Q2 2026 rankings, explicitly
  built on the same ranking methodology as a "Q1 2026 update" the post
  links to but this note did not separately fetch.
- **Confidence**: emerging (a specific, named-country, dated rank-change
  claim with a disclosed country count, but "rising the most" is a rank
  change, not an absolute usage-level change, and the underlying per-country
  rank values were not recoverable as text — see Extraction Notes)
- **Quote**: "Notably, in the second quarter, usage in parts of Latin America, Oceania, and Africa increased faster than usage in other parts of the world, with Peru, Uruguay, and Costa Rica rising the most among countries in global rankings. Adoption continues to rise in North America and Europe, but parts of the Southern Hemisphere are catching up in per-capita adoption rates."
- **Our assessment**: Directly extends `blog-openai-chatgpt-adoption-signals.md` Claim 2 (Africa and Asia showing the fastest relative weekly-active-user growth since July 2023) and Claim 3 (lower-HDI countries growing fastest) with a newer, narrower Q1→Q2 2026 snapshot and a different continent emphasis (this post foregrounds Latin America and Oceania alongside Africa; the June post foregrounded Africa and Asia). The two are not in tension — they measure different windows (year-over-year since July 2023 vs. one quarter) and different metrics (relative-growth-index vs. per-capita rank change) — but a future guide citation combining both should not imply a single consistent "which region grows fastest" ranking, since the answer shifts by window and metric.

### Claim 4: Multimedia is the fastest-growing ChatGPT use case globally, reaching 7.8% of messages worldwide and more than one in ten messages in countries including Brazil and Colombia, coinciding with the April 2026 release of ChatGPT Images 2.0
- **Evidence**: A message-classification share chart covering 126 countries
  with an "eligible Q2 multimedia estimate," tied to the ChatGPT Images 2.0
  product release date.
- **Confidence**: emerging (a specific, dated percentage with disclosed
  country coverage, but the post gives no comparison point for what
  multimedia's message share was before the Images 2.0 release, so the
  "fastest-growing" claim is asserted rather than shown with a before/after
  trend line)
- **Quote**: "Since the release of ChatGPT Images 2.0⁠ in April 2026, the share of messages across the world focused on multimedia use increased to 7.8%. While it still lags behind the leading use cases of practical guidance, writing, and information-seeking, multimedia use has been on a consistent upswing year-to-date." ... "in countries like Brazil and Colombia, more than one in ten messages to ChatGPT is categorized as multimedia."
- **Our assessment**: Novel to the corpus — no existing source note tracks
  multimedia (as opposed to text) message share for any AI product, or
  ties a specific feature release (ChatGPT Images 2.0) to a measured usage-share
  shift. This is a citable, product-launch-to-usage-metric linkage that the
  guide's existing OpenAI adoption notes (which track message volume,
  breadth-of-capability, and demographic/language share, but not modality)
  do not have an equivalent for.

### Claim 5: Usage among people over 35 rose in almost every country over the past year, with this cohort's overall share of messages increasing by 5 percentage points year-over-year, and the largest country-level increases in France and Czechia exceeding 10 percentage points
- **Evidence**: A three-month-trailing, self-reported-age-classified message
  share trend, covering 111 countries with complete estimates, indexed to
  each country's own Q2 2025 average.
- **Confidence**: emerging (a specific, disclosed-methodology cohort
  statistic with a stated country-count and baseline, but the post
  explicitly flags this is "an analysis of only users who self-reported
  their age," which is a non-random and likely biased subsample of the
  full user base)
- **Quote**: "The trend line over the last year shows that the percentage of messages sent by people over 35 increased in almost every country. Year over year, these users now account for a 5% higher share of messages than they did 12 months earlier. This is an analysis of only users who self-reported their age on the ChatGPT platform." ... "In France and Czechia, the share of messages sent by users 35 or older increased by more than 10 percentage points in the last year."
- **Our assessment**: Novel to the corpus — this is the first source note
  documenting age-cohort adoption trends for any AI product (the corpus's
  only prior age-specific figure, `blog-openai-chatgpt-work-education-plugins.md`
  Claim 7's ">200 million young adults ages 18–24 use ChatGPT weekly" and
  the associated "capability overhang" for college-age users, describes
  the *younger* cohort's scale and under-utilization, not adoption
  *growth*). Read together, the two posts suggest a genuinely broadening
  age profile: young adults remain the largest weekly-user base (per the
  education-plugins post) while the 35+ cohort is the one still gaining
  share fastest (per this post) — i.e., the age distribution is widening
  from both a large existing young-adult base and a growing older cohort,
  not narrowing toward either extreme. Neither post gives a combined
  age-distribution snapshot that would let the guide state precise shares
  by age band, only the reported trend directions.

### Claim 6: Almost three-quarters of European countries saw larger-than-average increases in their share of messages from users 35 and older, while the opposite pattern (below-average or declining share) emerged in some Southeast Asian countries such as Singapore — though six of eight Southeast Asian countries in the dataset still saw a (smaller) increase
- **Evidence**: The same age-cohort share-change chart underlying Claim 5,
  broken out by region (Europe vs. Southeast Asia) in the post's own prose
  description.
- **Confidence**: anecdotal (a regional pattern described in prose rather
  than shown with per-country chart data recoverable from this extraction —
  see Extraction Notes; "almost three-quarters" and "six of eight" are
  specific fractions but the underlying country list and exact percentages
  were not recoverable as text)
- **Quote**: "Almost three-quarters of European countries saw larger-than-average increases in their share of messages sent by these users, while the opposite pattern emerged in some Southeast Asian countries, such as Singapore. Overall, the share of messages sent by these users increased in six of the eight countries in the region, albeit by only a small margin."
- **Our assessment**: A regional-divergence detail that qualifies Claim 5's
  "almost every country" headline — the 35+ growth pattern is not uniform
  across regions, and Southeast Asia specifically shows a smaller and more
  mixed version of the trend (Singapore explicitly named as a below-average
  or declining case) compared to Europe's more broadly above-average
  pattern. Worth flagging alongside Claim 5 rather than citing Claim 5's
  global "almost every country" framing in isolation.

### Claim 7: The Signals dataset underlying this entire post reflects only messages sent within ChatGPT Free, Go, Plus, and Pro accounts — the group of accounts generally managed by individuals rather than organizations
- **Evidence**: The post's own scope statement, given immediately after
  introducing the OpenAI Signals hub.
- **Confidence**: settled (a direct, unambiguous scope disclosure by the
  source itself)
- **Quote**: "The Signals dataset specifically reflects messages sent within ChatGPT Free, Go, Plus, and Pro accounts—the group of accounts generally managed by individuals rather than organizations."
- **Our assessment**: Identical scope boundary to `blog-openai-chatgpt-adoption-signals.md` Claim 7 (that post's Individual-plan-only disclosure) — this confirms the OpenAI Signals series as a whole is consistently scoped to consumer/Individual-plan accounts across at least two releases three months apart, and every claim in this note (work-vs-non-work usage, per-capita rank change, multimedia share, age-cohort share) must be read as describing Individual-plan ChatGPT usage, not Enterprise, Team, API, or organizational ChatGPT Work/Codex deployment. This is the single most important caveat for correctly citing this post — see Guide Impact.

### Claim 8: OpenAI Signals publishes downloadable per-country CSV data and a public methodology document (a "data dictionary" PDF) alongside its narrative posts
- **Evidence**: The post's closing "More about OpenAI Signals" section,
  linking a data-download page and a methodology PDF.
- **Confidence**: settled (a direct, checkable statement of what is
  publicly available, though this note did not independently fetch either
  the CSVs or the PDF — see Extraction Notes)
- **Quote**: "We encourage you to download the data here⁠ and explore our methodology here⁠(opens in a new window)." (linking to `openai.com/signals/data-download/` and `cdn.openai.com/signals/data-dictionary.pdf` respectively)
- **Our assessment**: Corroborates the same downloadable-dataset claim
  already flagged (but not independently verified) in
  `blog-openai-chatgpt-adoption-signals.md`'s Author-credibility section —
  two OpenAI Signals posts, three months apart, both point to the same
  data-download and methodology infrastructure, which is a meaningful,
  in-principle-checkable claim about vendor transparency, though this note
  again does not verify the download or reproduce any chart from the raw
  data.

## Concrete Artifacts

```
Source: OpenAI, "From asking to doing: How the world is putting ChatGPT to work,"
https://openai.com/index/how-the-world-is-putting-chatgpt-to-work (August 6, 2026)

Headline scale claim:
  >1,000,000,000  people "putting ChatGPT to work" (no methodology given;
                   matches blog-openai-building-abundant-intelligence.md
                   Claim 9's identical figure, six days earlier)

Work-context task orientation:
  At-work "doing" (task completion) vs. outside-work: >2x more likely
  Outside-work: "asking" (info-seeking) remains the largest category

Per-capita adoption-rank change, Q1 2026 -> Q2 2026 (144 countries covered):
  Fastest risers: Peru, Uruguay, Costa Rica (largest rank improvements)
  Regional pattern: Latin America, Oceania, Africa increasing faster than
                     global average; North America and Europe still rising
                     but at a slower relative pace

Multimedia message share (126 countries with eligible Q2 estimate):
  Global:            7.8% of messages
  Brazil, Colombia:  >10% of messages
  Trigger event:     ChatGPT Images 2.0 release, April 2026

Age-cohort (35+) message share change, trailing 3 months vs. own Q2 2025
baseline (111 countries with complete estimates, self-reported age only):
  Global:            +5 percentage points, year over year
  France, Czechia:   +10+ percentage points (largest country increases)
  Europe:            ~3/4 of countries above-average increase
  Southeast Asia:    mixed / below-average in some countries (e.g.
                     Singapore); 6 of 8 countries in the dataset still
                     increased, by a smaller margin

Dataset scope: ChatGPT Free, Go, Plus, Pro (Individual plans) only --
excludes Enterprise, Team, API, and organizational accounts.

Public resources referenced (not independently fetched by this note):
  Data download:  openai.com/signals/data-download/
  Methodology:    cdn.openai.com/signals/data-dictionary.pdf
  Prior release:  openai.com/signals/research/2026q1-update/ (Q1 2026
                   per-capita ranking, referenced but not separately mined)
```

## Cross-References

- **Corroborates**:
  - `blog-openai-chatgpt-adoption-signals.md` Claim 2 (Africa and Asia
    showing the fastest relative weekly-active-user growth since July
    2023) and Claim 3 (lower-HDI countries growing fastest) — this post's
    Claim 3 (Latin America, Oceania, and Africa catching up in per-capita
    rank, Q1→Q2 2026) is a directionally consistent, newer snapshot of the
    same broad "adoption is broadening beyond early-adopter countries"
    trend, using a different metric (quarterly per-capita rank change vs.
    year-over-year relative-growth index) and a different regional
    emphasis (adds Latin America and Oceania to the earlier post's
    Africa/Asia framing).
  - `blog-openai-chatgpt-adoption-signals.md` Claim 7 and this post's Claim
    7 — both posts independently confirm the OpenAI Signals series is
    scoped to Individual ChatGPT plans (Free/Go/Plus/Pro) only, three
    months apart, which is a stable and important scope boundary for
    citing either post.
  - `blog-openai-building-abundant-intelligence.md` Claim 9 (>1 billion
    active users, July 31, 2026) and Claim 10 (the "asking to doing"
    framing applied to ChatGPT Work specifically) — this post restates the
    identical >1 billion figure (Claim 1) six days later and extends the
    "asking to doing" framing (Claim 2) from a ChatGPT-Work-specific
    telemetry claim into a measured, cross-product ChatGPT usage-pattern
    statistic. Three OpenAI posts in roughly a five-week span
    (`blog-openai-agents-transforming-work.md`,
    `blog-openai-building-abundant-intelligence.md`, and this post) have
    now each independently used some version of "asking to doing" or
    "asking vs. doing" language for three different scopes (Codex
    delegation depth; ChatGPT Work + Codex internal adoption; general
    ChatGPT work-context usage) — worth flagging as a consistent OpenAI
    messaging theme across products rather than three restatements of one
    finding.
- **Contradicts**: None identified.
- **Extends**: `blog-openai-chatgpt-work-education-plugins.md` Claim 7
  (>200 million weekly users aged 18–24, plus a "capability overhang" for
  college-age users) — that post describes the *scale* of the youngest
  major cohort and its under-utilization of ChatGPT's capabilities; this
  post's Claim 5 (35+ cohort gaining 5 percentage points of message share
  year-over-year, with France and Czechia exceeding 10 points) describes
  *growth* in an older cohort from the same underlying self-reported-age
  data source. Neither post gives a single combined age-distribution table,
  so the two should be cited together as complementary trend evidence
  (large young base; fastest-growing older cohort), not merged into one
  statistic.
- **Novel**: The multimedia-usage-share data (Claim 4, 7.8% global,
  >10% in Brazil/Colombia, tied to the ChatGPT Images 2.0 release) and the
  age-cohort adoption data (Claims 5-6, 35+ share growth by country and
  region) are both new axes of adoption measurement for the corpus — no
  existing source note tracks message modality (text vs. multimedia) or
  user age as an adoption dimension for any AI product. The Q1→Q2 2026
  per-capita country-rank-change methodology (Claim 3) is also a new
  metric shape in the corpus, distinct from the June post's
  relative-growth-index-since-July-2023 approach.

## Guide Impact

- **Chapter 00 (Principles)**: Claims 3-6 (closing adoption gap, multimedia
  growth, broadening age profile) extend the same "AI-native is a global,
  broadening baseline, not a narrow early-adopter phenomenon" scene-setting
  point already drawn from `blog-openai-chatgpt-adoption-signals.md` — cite
  briefly as updated market context if that point is made, not as
  actionable engineering guidance. As with the June post, this source's
  population (Individual ChatGPT consumer accounts, Claim 7) does not
  describe professional engineering teams or organizational deployment, so
  it should not be cited for team-adoption or harness-engineering
  recommendations.
- **No chapter should cite Claim 2 (the "doing" vs. "asking" 2x ratio) as
  evidence about agentic coding-tool usage or engineering-team workflows.**
  It measures ordinary ChatGPT message classification (work-context vs.
  non-work-context, across all consumer use cases including writing,
  coding, and analysis together), not Codex, ChatGPT Work, or any
  engineering-specific tool — conflating it with the delegation-depth
  statistics in `blog-openai-agents-transforming-work.md` would overstate
  what this post actually measured.
- **Chapter 05 (Team Adoption)**: If the chapter discusses OpenAI's
  repeated "asking to doing" messaging across products (see
  Cross-References → Corroborates), this post is the most general/consumer-facing
  instance of that framing and can be cited alongside
  `blog-openai-building-abundant-intelligence.md` Claim 10 as evidence the
  framing is now a consistent OpenAI narrative across at least three
  product contexts, not a one-off product-launch tagline.

## Extraction Notes

- The live OpenAI URL returned an HTTP 403 to `WebFetch` directly, matching
  the Cloudflare bot-challenge access pattern already documented for
  `openai.com/index/` posts in `blog-openai-agents-transforming-work.md`,
  `blog-openai-chatgpt-adoption-signals.md`, and
  `blog-openai-chatgpt-work-ambitious-partner.md`. The article was
  retrieved successfully via the `r.jina.ai` reader proxy (fetched through
  the `WebFetch` tool, which succeeded on this URL where it failed on the
  direct OpenAI URL), returning the full page converted to Markdown,
  including every heading, paragraph, bullet list, and chart caption. Every
  quote above was checked character-for-character against that fetched
  Markdown.
- The post is built around four embedded interactive charts (a
  world/country rank-change map, a multimedia-share choropleth, an
  age-cohort trend line, and a per-country age-cohort-shift chart). As with
  the June Signals post, the reader-proxy Markdown conversion preserved
  each chart's caption and surrounding prose but not the underlying
  per-country numeric data tables — no per-country rank values, exact
  multimedia percentages beyond the two named examples (Brazil, Colombia),
  or exact per-country age-share percentages beyond the two named examples
  (France, Czechia) were recoverable as text. Claims 3, 4, and 6 are
  therefore drawn from the post's own prose description of what each chart
  shows, not from independently read chart data — flagged per-claim above.
  A future extraction with browser-based chart access, or by fetching the
  linked downloadable CSV dataset directly, could recover the full
  per-country figures and would be a meaningfully stronger version of this
  note.
- Two inline citation markers (rendered as `⁠` zero-width-space characters
  in the reader-proxy Markdown, attached to "OpenAI Signals," "June,"
  "here" (Q1 2026 update), "ChatGPT Images 2.0," and the data-download/methodology
  links) are OpenAI's own hyperlink markers, not footnotes requiring
  separate resolution — all resolved directly to inline links in the
  fetched Markdown and are reproduced as plain URLs above rather than as
  unresolved footnote markers (contrast with the unresolved `[1]`/`[2]`
  footnote markers flagged in `blog-openai-agents-transforming-work.md`
  and `blog-openai-chatgpt-adoption-signals.md`, which are a different,
  genuinely unresolved citation mechanism).
- This note did not independently fetch the linked "Q1 2026 update"
  (`openai.com/signals/research/2026q1-update/`), the data-download page,
  or the methodology PDF — all three are referenced in Claim 3 and Claim 8
  as things the post points to, not as independently verified content.
  A future Miner pass on the Q1 2026 update specifically (if filed as its
  own source) could recover the absolute per-capita country rankings that
  this post's rank-*change* framing does not itself disclose.
- No contradiction with any existing source note was found during
  cross-referencing (see Cross-References → Contradicts), so no
  contradiction issue was filed per MINER.md §4a.
- This is the corpus's third mined OpenAI Signals post (after
  `blog-openai-chatgpt-adoption-signals.md`). The recurring pattern across
  both — first-party telemetry, disclosed-but-shallow per-chart
  methodology, no absolute figures for rank/share-change charts, explicit
  Individual-plan-only scope — is now well-established; a future Miner
  encountering a fourth Signals post should expect the same evidentiary
  shape and can cross-reference both existing notes directly rather than
  re-deriving the pattern.
