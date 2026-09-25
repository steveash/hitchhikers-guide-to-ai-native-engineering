---
source_url: https://openai.com/index/unlocking-new-ways-of-working
source_type: blog-post
title: "How workers are unlocking new ways of working"
author: "OpenAI (report authors: Alex Martin Richmond and Caroline Chin, OpenAI Economic Research)"
date_published: 2026-09-16
date_extracted: 2026-09-25
last_checked: 2026-09-25
status: current
confidence_overall: emerging
issue: "#3697"
---

# How workers are unlocking new ways of working

> The second "Work at the Frontier" report from OpenAI Economic Research,
> following on from the first report's "task crossover" finding, tracks
> ~6,200 workers over April-July 2026 and finds that cross-occupation
> AI use is not a one-off experiment: the share of a worker's
> occupation-specific AI activity that is a *previously used*
> cross-occupation task nearly doubles, from 13.1% to 25.9%, over four
> months, and workers with a prior month's cross-occupation task use are
> ~15 percentage points more likely to repeat it than matched workers
> with no prior use — but recurrence varies sharply by task type, from
> 54% (customer communication) to under 10% (legal research).

## Source Context

- **Type**: blog-post (OpenAI company blog, `openai.com/index/`,
  category "Global Affairs" / "Economic Research"; unsigned on the blog
  page itself) that summarizes and links a full 13-page companion PDF
  report, *Work at the Frontier: How workers are unlocking new ways of
  working* (September 2026), hosted at
  `https://cdn.openai.com/pdf/work-at-the-frontier-report-202609.pdf`.
  The PDF is signed by two named authors, Alex Martin Richmond and
  Caroline Chin, under the "OpenAI Economic Research" byline. This note
  extracts from both: the blog post for framing/summary quotes, and the
  PDF report for all figures, methodology, and quantitative claims,
  since the PDF contains substantially more detail (six figures, an
  appendix robustness check, and a full methodology section) than the
  blog post reproduces.
- **Author credibility**: First-party OpenAI Economic Research output,
  with named individual authors (unusual among the OpenAI
  `openai.com/index/` posts in this corpus, most of which are unsigned —
  contrast with `blog-openai-agents-transforming-work.md` and
  `blog-openai-work-frontier-task-crossover.md`, both unsigned). The
  underlying data is OpenAI's own ChatGPT message telemetry, which is
  vendor-internal and unaudited by outside researchers, but the PDF
  discloses more methodology than typical OpenAI adoption posts in this
  corpus: sample construction, occupation-classification method (O*NET
  detailed work activities), exclusion criteria, an explicit
  representativeness disclaimer, and a dedicated appendix robustness
  check using a different denominator.
- **Scope**: Covers a second, four-month (April-July 2026) longitudinal
  analysis of more than 1.5 million work-related messages from
  individual ChatGPT accounts belonging to U.S. users who also have a
  linked ChatGPT Business account (occupation/workspace inferred from
  Business-onboarding data, but only individual-account messages are
  analyzed — no ChatGPT Business account messages are included). Covers:
  how cross-occupation vs. within-occupation prompts differ in content,
  whether cross-occupation task use recurs over time (same worker and
  coworkers), and which specific cross-occupation tasks are stickiest.
  Does NOT cover: task success/quality, occupation-level breakdowns by
  name (the per-occupation percentages from the *first* report are not
  repeated here), non-U.S. users, Enterprise/Team/API usage, or
  Codex/agentic (vs. chatbot) usage specifically. The authors explicitly
  disclaim that "the findings describe observed ChatGPT use in this
  selected population and are not representative of the U.S. workforce."

## Extracted Claims

### Claim 1: This report is a direct follow-on to OpenAI's first "Work at the Frontier" report (task crossover), asking not whether workers do cross-occupation AI work but whether that work becomes a recurring, regular part of how they work
- **Evidence**: The report's own framing in its introduction, explicitly
  citing the first report by name and date.
- **Confidence**: settled (a direct, unambiguous self-description of the
  report's relationship to its predecessor)
- **Quote**: "This new paper, building off the first Work at the Frontier report published in July 2026, continues our series exploring how work is changing across the economy. The first report showed that workers commonly use AI to explore or take on tasks outside their traditional job description. This report asks what happens next: how workers actually do the new work beyond their normal scope, and whether these efforts become part of their ongoing regular work activity."
- **Our assessment**: This is a direct, explicit extension of
  `blog-openai-work-frontier-task-crossover.md`, which documented the
  headline "43.5% of occupation-specific messages are about tasks
  associated with another occupation" finding (that note's Claim 1).
  This report does not re-measure that baseline share; it asks the
  logically next question (does crossover persist?), so the two notes
  should always be cited together for a complete picture of OpenAI's
  task-crossover research line, not as interchangeable sources for the
  same finding.

### Claim 2: Cross-occupation prompts systematically differ in content from within-occupation prompts — less likely to request explanations/how-to help, a specific format, or advice; more likely to include examples/background or ask for checking/verification; and slightly shorter
- **Evidence**: Figure 1 and Figure 2 of the PDF report — per-worker
  differences in prompt-content-category rates and prompt length between
  each worker's cross-occupation and within-occupation messages,
  averaged across workers with equal weighting, with 95% confidence
  intervals shown for each category.
- **Confidence**: emerging (six distinct measured differences, each with
  a reported confidence interval, though the underlying content-category
  classifier's accuracy is not independently validated in the report)
- **Quote**: "In general, cross-occupation requests are noticeably less likely to ask for explanations or 'how-to' help. The cross-occupation requests also are less likely to specify a format or ask for advice. At the same time, cross-occupation requests are more likely to provide examples or background; they also are more likely to involve checking or verification. In addition, cross-occupation prompts are slightly shorter than within-occupation prompts, by about 20 characters on average."
- **Our assessment**: The specific Figure 1 deltas (explanations/how-to
  -3.0pp, format -1.2pp, advice -1.4pp, examples/background +0.9pp,
  checking/verification +0.7pp; "set specific requirements" -0.1pp,
  whose confidence interval crosses zero and is not a reliable
  difference) give this claim more quantitative backing than a typical
  "AI changes how people prompt" observation. The report's own
  interpretation — that workers are "borrowing expertise" rather than
  learning a new skill — is plausible but not independently tested
  against an alternative explanation (e.g., that cross-occupation tasks
  are simply lower-stakes or less complex on average, which could
  produce the same prompt-pattern differences without any "expertise
  borrowing" mechanism).

### Claim 3: Among ~6,200 consistently-observed workers, the share of occupation-specific AI activity made up of previously-used cross-occupation tasks nearly doubled over four months — from 13.1% in the first month to 20.5%, 24.0%, and 25.9% in the second, third, and fourth months
- **Evidence**: Figure 3 of the PDF report, a month-by-month trend line
  with 95% confidence bands, restricted to workers with at least 10
  sampled messages in each of the four months (April-July 2026).
- **Confidence**: emerging (a specific, four-point time series, but drawn
  from a sample explicitly filtered to higher-activity workers, and the
  report itself flags that "as workers try new tasks in any given month,
  the number of tasks that can be considered recurring increases" — some
  of the rise is a mechanical artifact of the growing pool of
  "previously seen" tasks, not necessarily accelerating behavior change)
- **Quote**: "Figure 3 examines whether previously used cross-occupation tasks take up a larger share of a worker's AI activity, finding that cross-occupation tasks become recurring parts of their AI use. To examine this pattern, we use repeated cross-occupation activity among about 6,200 workers observed during our four-month study. [...] Averaging across workers, this share increased by almost 2x, from 13.1% in April to 25.9% in July."
- **Our assessment**: This is the report's headline statistic and the
  strongest evidence for the "recurring, not one-off" thesis. The
  mechanical-growth caveat (explicitly disclosed by the authors in their
  own footnote 3) is important: because the "previously used" pool only
  grows over the four-month window, some rise is definitionally
  guaranteed even under a null model of no behavior change, which is
  presumably why the authors also ran the Appendix A1 robustness check
  (Claim 8 below) with a different, more conservative denominator.

### Claim 4: Workers who used AI for a cross-occupation task in one month were 15.2 percentage points more likely to use it again the next month than matched workers with no prior recorded use (23.6% vs. 8.4%) — a gap similar in size to within-occupation (+16.0pp: 26.4% vs. 10.4%) and general tasks (+16.8pp: 31.8% vs. 14.9%)
- **Evidence**: Figure 4 (top panel) of the PDF report, comparing
  next-month task use between workers with vs. without observed use of
  that task category in the current month, matched on broad occupation
  and next-month AI-activity level, with conditional 95% intervals
  reported for each gap.
- **Confidence**: emerging (a matched-comparison design, which is
  methodologically stronger than a simple before/after trend, with
  reported confidence intervals for all three category gaps)
- **Quote**: "Workers observed using AI for a cross-occupation task in one month were 15.2 percentage points more likely to be observed using it the next month than similar workers with no previous recorded use of that task (23.6% versus 8.4%). The pattern was similar for within-occupation and generic tasks, with gaps of roughly 15-17 percentage points across all three categories. These patterns are consistent with cross-occupation assistance meeting recurring work needs."
- **Our assessment**: The key finding here is that cross-occupation
  recurrence is *not* meaningfully weaker than within-occupation
  recurrence (15.2pp vs. 16.0pp gap, overlapping in magnitude) — once a
  worker has used AI for an outside-occupation task at all, they return
  to it about as reliably as they return to tasks within their own job.
  This undercuts a natural prior that cross-occupation use might be more
  experimental/one-off than within-occupation use; the data says
  otherwise.

### Claim 5: When a cross-occupation task appears in a workplace, coworkers without prior use of it are modestly more likely to pick it up the next month (3.1% vs. 2.5% baseline, +0.6pp) — a smaller spillover effect than the same-worker recurrence effect, and smaller than within-occupation coworker spillover (+1.1pp)
- **Evidence**: Figure 4 (bottom panel) of the PDF report, comparing
  next-month task use between coworkers of a task-using worker vs.
  matched workers in workplaces with no observed use.
- **Confidence**: emerging (measured with reported confidence intervals,
  though the +0.6pp cross-occupation coworker effect is the smallest and
  least precisely bounded of the six gaps reported in Figure 4)
- **Quote**: "We also examine whether these activities subsequently appear in coworkers' AI use, finding that when one person in a workplace does a task, their peers are more likely to as well. [...] Together, these findings show strong recurrence within workers and a smaller increase in subsequent use among coworkers. [...] The smaller increase in a coworker's subsequent use suggests that the workplace may also shape which activities take hold, whether through shared work needs or colleagues learning from one another."
- **Our assessment**: The individual-level recurrence effect (Claim 4,
  ~15pp) is roughly 25x larger than the coworker-spillover effect
  (Claim 5, ~0.6-1.1pp) — task crossover in this data looks much more
  like an individual habit than a socially contagious workplace practice.
  This is a useful nuance for any guide claim about "team-level" AI
  workflow adoption: the report's own data suggests adoption here
  concentrates within individuals rather than propagating quickly across
  a team, at least over a one-month lag.

### Claim 6: Cross-occupation task stickiness varies sharply by task type — customer communication (54.1%), advertising/promotional writing (44.2%), and marketing-materials creation (37.3%) have the highest next-month return rates, while explaining financial information to customers (15.0%), presenting business information (14.9%), and legal research (9.9%) have the lowest, against an overall base rate of 18.5%
- **Evidence**: Figure 5 of the PDF report, per-task next-month return
  rates with worker counts and confidence intervals for six named tasks
  (three highest-, three lowest-recurrence), plus the overall
  worker-task-combination base rate.
- **Confidence**: emerging (specific, per-task percentages with reported
  worker counts (517-2,188 workers per task) and confidence intervals,
  though the report does not explain why these particular six tasks —
  rather than all tasks with sufficient sample — were selected for
  the chart, beyond framing them as "most and least" recurrent)
- **Quote**: "Our research finds that customer communication (54%), advertising or promotional writing (44%), and creating marketing materials (37%) have the highest observed return rates. Explaining financial information to customers (15%), presenting business information (15%), and legal research (10%) have the lowest observed return rates."
- **Our assessment**: This is the report's most actionable finding for
  understanding *which* cross-occupation AI use will stick: customer-facing
  and marketing/communications tasks recur roughly 2-5x more often than
  legal or financial-explanation tasks. The report speculates this
  reflects "uneven expansion of a typical worker's task repertoire" but
  does not test alternative explanations — e.g., legal research and
  financial explanation to customers may carry higher perceived
  liability/compliance risk than drafting marketing copy, which would
  produce the same pattern through risk-aversion rather than task
  "stickiness" per se. Both explanations are consistent with the data;
  the report does not distinguish between them.

### Claim 7: AI lets workers "borrow expertise" from another field by bringing a problem and context and asking AI to apply knowledge associated with a different occupation, rather than asking AI to teach them the field itself
- **Evidence**: The report's own interpretive synthesis of the Claim 2
  (prompt-pattern) and Claim 3/4 (recurrence) findings, not a separately
  measured result.
- **Confidence**: anecdotal (an interpretive framing claim built on top
  of the measured findings, not itself independently tested)
- **Quote**: "AI lets workers 'borrow expertise' by drawing on assistance associated with another field. Compared with the same workers' within-occupation requests, cross-occupation prompts are less likely to seek explanations or advice, and are more likely to provide examples or background and ask for verification. Workers may be bringing the problem and its context, then asking AI for help applying knowledge from another field."
- **Our assessment**: This is the report's central interpretive thesis
  and the most citable one-sentence framing for a guide passage on
  cross-role AI delegation — but it remains an interpretation layered on
  top of prompt-pattern statistics (Claim 2), not a directly observed
  mechanism. The report is transparent that this is an inference
  ("Workers *may* be bringing...") rather than a confirmed finding.

### Claim 8: A robustness check using a broader denominator (all observed task activity, not just occupation-specific work) and a smaller, higher-activity worker subset shows the same rising pattern at a lower absolute level — 7.0% in April, rising to 10.6%, 11.8%, and 12.1% by July
- **Evidence**: Appendix Figure A1 of the PDF report, restricted to the
  highest-activity third (2,100 workers) of Figure 3's eligible cohort,
  with equal worker weighting and a broader denominator including
  broadly-shared and unmapped tasks.
- **Confidence**: emerging (an explicit, disclosed robustness check with
  its own confidence bands, run by the authors specifically to address
  the Claim 3 mechanical-growth concern)
- **Quote**: "The average share of previously used cross-occupation tasks rises from 7.0% in April to 10.6% in May, 11.8% in June, and 12.1% in July. Counting all tasks lowers the level but leaves the upward pattern. The same growing-history and selected-sample qualifications apply."
- **Our assessment**: This is a genuine methodological strength worth
  flagging — the authors ran and published a check against their own
  headline number's most obvious confound (the mechanical growth of the
  "previously seen tasks" pool noted in Claim 3), and the check confirms
  the direction (rising) even though the authors still caveat that
  "growing-history" qualifications apply to this check too. A guide
  citing Claim 3's 13.1%→25.9% figure should pair it with this appendix
  check as evidence the trend is not purely an artifact of the growing
  denominator, while still not treating either number as a precise,
  reproducible rate.

### Claim 9: Report methodology restricts the sample to individual ChatGPT accounts of U.S. users who also have a linked ChatGPT Business account (for occupation/workspace inference), explicitly excludes ChatGPT Business account messages entirely, uses O*NET detailed work activities for task classification, and explicitly disclaims representativeness of the U.S. workforce
- **Evidence**: The PDF report's "Methodology and definitions" section.
- **Confidence**: settled (a direct methodological self-disclosure,
  unusually detailed for an OpenAI adoption/economics post in this
  corpus)
- **Quote**: "We analyze work-related messages from individual ChatGPT accounts belonging to U.S. users with parallel ChatGPT Business accounts. [...] No messages that were sent through a ChatGPT Business account are included in the sample. [...] We use O*NET, the U.S. Department of Labor's database of occupations and work activities, to identify the tasks traditionally associated with each occupation group. [...] This is a sample of ChatGPT users with linked occupation information, not a representative sample of the U.S. workforce."
- **Our assessment**: This population definition is distinct from every
  other OpenAI adoption-telemetry note in the corpus:
  `blog-openai-chatgpt-adoption-signals.md` Claim 7 explicitly scopes
  itself to Individual plans only (Free/Go/Plus/Pro) and excludes
  Enterprise/Team/API; this report instead requires individual-account
  users to *also* have a linked Business account (for occupation data)
  while excluding their Business-account messages — a narrower,
  differently-biased population than either a pure-Individual or
  pure-Business sample would be. The O*NET-based classification
  methodology is more disclosed than the (undescribed) classification
  approach in `blog-openai-agents-transforming-work.md`, which never
  explains how it infers "occupation" or "work category" from Codex
  usage. This report's explicit non-representativeness disclaimer is a
  positive transparency signal relative to several sibling posts in the
  corpus that report percentages without any such caveat.

### Claim 10: The authors frame their findings as a reason for organizations to treat work design, not just AI tool access, as a strategic lever — arguing task crossover and its recurrence are usage-data evidence of where jobs may broaden before job titles change
- **Evidence**: The report's closing synthesis section ("What these
  patterns tell us"), tying the measured findings to a normative
  recommendation for organizations.
- **Confidence**: anecdotal (an interpretive, forward-looking
  recommendation, not itself a measured finding — though built
  atop the measured claims above)
- **Quote**: "Such strategic borrowing offers a way to think about job transformation: changes in the mix of activities within a job. If recurring cross-occupation activities become part of a worker's regular responsibilities, a job could broaden even while its title stays the same. [...] Our findings suggest that work design deserves a place alongside access to AI tools in how organizations implement their AI strategies."
- **Our assessment**: This is the report's practical takeaway and the
  most directly guide-relevant sentence in the source: it argues
  explicitly against a "just give people AI tools" adoption strategy, in
  favor of also redesigning who is expected to do what. This is a
  useful, citable data-backed complement to more prescriptive
  "harness/workflow design" guidance already in the corpus, since it
  comes from usage-pattern evidence rather than practitioner anecdote.

## Concrete Artifacts

```
Source: OpenAI Economic Research, "Work at the Frontier: How workers are
unlocking new ways of working" (PDF, September 2026), authors Alex Martin
Richmond and Caroline Chin.
PDF: https://cdn.openai.com/pdf/work-at-the-frontier-report-202609.pdf
Blog summary: https://openai.com/index/unlocking-new-ways-of-working
(published September 16, 2026)

Sample: >1.5 million work-related ChatGPT messages, individual accounts
of U.S. users with linked ChatGPT Business accounts, April-July 2026.

Figure 1 - cross-occupation vs. within-occupation prompt content
(percentage-point difference, cross-occupation minus within-occupation):
  Explanations or how-to help:      -3.0 pp
  Requested a format:               -1.2 pp
  Provided examples or background:  +0.9 pp
  Set specific requirements:        -0.1 pp (CI crosses zero)
  Asked for advice:                 -1.4 pp
  Checking or verification:         +0.7 pp

Figure 2 - cross-occupation prompt length vs. within-occupation:
  Average length: -20 characters
  Median length:   -6 characters

Figure 3 - previously-used cross-occupation task share of
occupation-specific work (~6,200 workers, equal weighting):
  Month 1 (April):  13.1%
  Month 2 (May):     20.5%
  Month 3 (June):    24.0%
  Month 4 (July):    25.9%

Figure 4 - next-month task recurrence vs. matched no-prior-use benchmark:
  Same-worker recurrence:
    Within-occupation: 26.4% vs 10.4%  (+16.0 pp)
    Cross-occupation:   23.6% vs  8.4%  (+15.2 pp)
    General:            31.8% vs 14.9%  (+16.8 pp)
  Individual coworker use (prior use in workspace):
    Within-occupation:  3.9% vs 2.8%   (+1.1 pp)
    Cross-occupation:    3.1% vs 2.5%   (+0.6 pp)
    General:             6.8% vs 5.7%   (+1.1 pp)

Figure 5 - per-task next-month return rate (overall base rate: 18.5%):
  Highest recurrence:
    Discuss goods/services with customers:      54.1%  (n=2,188 workers)
    Write advertising or promotional material:  44.2%  (n=1,710 workers)
    Create marketing materials:                 37.3%  (n=1,013 workers)
  Lowest recurrence:
    Explain financial information to customers: 15.0%  (n=642 workers)
    Present business information to audiences:   14.9%  (n=743 workers)
    Research legal materials for decision-making: 9.9%  (n=517 workers)

Appendix Figure A1 - robustness check, broader denominator (all observed
task activity), 2,100-worker highest-activity subset:
  Month 1 (April):   7.0%
  Month 2 (May):     10.6%
  Month 3 (June):    11.8%
  Month 4 (July):    12.1%

Methodology: O*NET detailed-work-activity (DWA) classification of
messages; sample restricted (for recurrence analyses) to workers with
>=10 sampled messages per month across all four months; ChatGPT Business
account messages entirely excluded; explicit non-representativeness
disclaimer for the U.S. workforce.
```

## Cross-References

### Cross-reference verification notes
`blog-openai-work-frontier-task-crossover.md`,
`blog-openai-agents-transforming-work.md`, and
`blog-openai-chatgpt-adoption-signals.md` were re-read directly
(MINER.md §4b) and the claim numbers cited above were confirmed against
each note's numbered `### Claim N:` headings in document order before
writing this section.

- **Corroborates**:
  - `blog-openai-work-frontier-task-crossover.md` Claim 1 (16.8%/43.5%
    headline task-crossover statistics from the first report) — this
    report does not re-measure that baseline but takes it as its
    starting premise; the two notes should be read as a matched pair
    (baseline prevalence, then persistence-over-time) rather than
    duplicate or competing sources.
  - `blog-openai-agents-transforming-work.md` Claim 1 ("Agentic AI
    changes the unit of knowledge work from single interactions to
    delegated, long-horizon tasks") and Claim 3 (task-length adoption
    thresholds) describe a *within-occupation* delegation-depth trend
    using Codex; this report's Claim 3/8 describe a *cross-occupation*
    recurrence trend using ChatGPT. Both are "AI use deepens/broadens
    over time" findings from OpenAI's own telemetry, using different
    products and different axes of change (task duration vs.
    occupational breadth), and should be treated as complementary,
    non-overlapping evidence for a general "AI use intensifies with
    tenure" pattern rather than the same statistic restated.

- **Contradicts**: None identified. No existing source note makes a
  claim about cross-occupation task recurrence rates, coworker
  spillover, or task-specific stickiness that this report's figures
  conflict with.

- **Extends**:
  - `blog-openai-work-frontier-task-crossover.md` directly, as described
    in Claim 1 above — this is the explicit, named sequel report from
    the same OpenAI Economic Research series, closing the "does
    crossover persist?" question the first report's Extraction Notes
    (item 5, re: the companion AI Jobs Transition Framework PDF) flagged
    as an open follow-up direction, though from a different angle
    (recurrence over time, not the linked Jobs Transition Framework PDF
    itself, which remains unextracted).
  - `blog-openai-chatgpt-adoption-signals.md`, whose Claim 7 scopes
    itself to Individual ChatGPT plans only and excludes
    Enterprise/Team/API usage — this report's population (individual
    accounts *with* a linked Business account, Business-account messages
    excluded) is a third, distinct population definition alongside
    "Individual plans only" (adoption-signals) and the undisclosed
    population in `blog-openai-agents-transforming-work.md` and
    `blog-openai-codex-knowledge-work.md`. A future guide section citing
    multiple OpenAI usage-telemetry sources together should flag that
    each draws from a different, non-identical user population rather
    than treating them as one consistent sample.

- **Novel**:
  - **Task-crossover recurrence as a measured, time-series finding**
    (Claims 3, 8) — the first source in our corpus to show that
    cross-occupation AI use is not a one-time experiment but grows as a
    share of a worker's activity over a multi-month window, with an
    explicit robustness check against the most obvious confound.
  - **Matched same-worker vs. coworker recurrence comparison** (Claims 4,
    5) — the first source in our corpus to separate individual habit
    formation from workplace-level social spillover for AI task
    adoption, finding the individual effect to be roughly an order of
    magnitude larger than the coworker effect.
  - **Per-task stickiness ranking** (Claim 6) — the first source in our
    corpus to rank specific cross-occupation task types by how often
    workers return to them, rather than reporting only an aggregate
    crossover or recurrence rate.
  - **Prompt-content-pattern differences between cross- and
    within-occupation requests** (Claim 2) — the first source in our
    corpus to characterize *how* prompts differ (shorter, fewer
    explanation requests, more examples/verification) when a worker
    steps outside their occupational boundary, as distinct from *how
    much* crossover occurs.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Claims 3-4 (cross-occupation task share
  nearly doubling over four months; ~15pp recurrence gap matching
  within-occupation recurrence) provide a data-backed answer to "does
  AI-enabled role-boundary-crossing stick, or is it a novelty phase?" —
  cite alongside `blog-openai-work-frontier-task-crossover.md` Claim 3
  (per-occupation crossover shares) for a fuller before/after picture:
  first, how much crossover happens (first report); second, whether it
  persists (this report). Claim 5's finding that coworker spillover is
  much weaker than individual recurrence is a useful caution against
  assuming team-level AI workflow changes will propagate quickly just
  because one team member adopts a new cross-role usage pattern.
- **Chapter 04 (Context Engineering)**: Claim 2 and Claim 7's "borrowing
  expertise" framing (shorter prompts, fewer explanation requests, more
  supplied examples/background, more verification requests when working
  outside one's occupation) is a concrete, measured description of how
  users prompt differently when delegating unfamiliar work — relevant to
  guidance on how much context/verification a workflow should build in
  by default when it's likely to be used by non-specialists.
- **Chapter 01 (Daily Workflows) or Chapter 05**: Claim 10's explicit
  "work design deserves a place alongside access to AI tools" thesis is
  a citable, first-party-research-backed argument against a
  tool-access-only AI adoption strategy — useful as supporting evidence
  for any guide section arguing that organizational role/workflow
  redesign, not just tool rollout, is necessary for durable AI adoption.
- **No chapter should cite the specific per-task recurrence percentages
  in Claim 6 (e.g., "54% of workers who use AI for customer
  communication return to it") as a benchmark a reader's own
  organization should expect to replicate.** These are unaudited,
  first-party classifier-derived rates over a non-representative,
  activity-filtered sample of ChatGPT users, with an explicit
  non-representativeness disclaimer from the authors themselves — use
  directionally (some cross-occupation tasks stick much more than
  others) rather than as precise figures.

## Extraction Notes

1. **The live `openai.com/index/unlocking-new-ways-of-working` URL
   returned HTTP 403** to `WebFetch` directly. A `curl` fetch through
   the `r.jina.ai` reader proxy also returned a Cloudflare
   bot-challenge page (HTTP 403, "Just a moment..." interstitial),
   matching the pattern already documented in
   `blog-openai-agents-transforming-work.md` and
   `blog-openai-work-frontier-task-crossover.md` for other
   `openai.com/index/` posts. Unlike those two prior extractions
   (which found `web.archive.org` entirely unreachable), the Wayback
   Machine's availability API *was* reachable this time and returned an
   archived snapshot from September 18, 2026
   (`http://web.archive.org/web/20260918091116/https://openai.com/index/unlocking-new-ways-of-working/`).
   `WebFetch` could not retrieve that archive.org URL directly (tool
   error: "unable to fetch from web.archive.org"), so the archived HTML
   was instead retrieved with `curl` using a browser user-agent (HTTP
   200, full page returned) and parsed locally to extract the blog
   post's visible text, which was used for the blog-post-specific quotes
   above (title, byline, publish date, "Read the report" framing).
2. **The blog post links a companion PDF report**
   (`https://cdn.openai.com/pdf/work-at-the-frontier-report-202609.pdf`,
   linked via the "Read the report" call-to-action button), which was
   not blocked by Cloudflare and was fetched directly with `curl`
   (HTTP 200, 13-page PDF, ~5.1MB) with no user-agent workaround needed.
   This PDF was the primary source for every figure, statistic, and
   methodology detail in this note — the blog post's own body text is a
   condensed paraphrase of the PDF's introduction and "What these
   patterns tell us" section and does not reproduce any of the six
   figures' underlying data. All PDF quotes above were read directly
   from the rendered PDF pages (not a text-extraction tool), including
   cross-checking each quoted sentence against its source page image.
3. **All six figures in the PDF (Figures 1-5 plus Appendix Figure A1)
   were fully legible as rendered chart images**, unlike the embedded
   interactive charts in `blog-openai-agents-transforming-work.md` and
   `blog-openai-work-frontier-task-crossover.md`, whose underlying data
   tables were not recoverable from reader-proxy text extraction (both
   flagged this as a limitation in their own Extraction Notes). This PDF
   report's static chart images, by contrast, rendered with fully
   readable axis labels, data-point values, and confidence-interval
   bars, so no chart data in this note is drawn from prose-only
   description — every numeric figure cited above was read directly off
   a chart or its accompanying labeled data point.
4. **The "AI Jobs Transition Framework" report referenced in the blog
   post's closing links was not fetched** for this note (out of scope —
   this note focuses on the "Work at the Frontier" series specifically).
   `blog-openai-work-frontier-task-crossover.md` Claim 10's "Our
   assessment" already flags that framework PDF as an unextracted
   follow-up source; that recommendation still stands and is not
   duplicated here.
5. **No contradiction with any existing source note was found** during
   cross-referencing (see Cross-References → Contradicts), so no
   contradiction issue was filed per MINER.md §4a.
