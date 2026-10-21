---
source_url: https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
source_type: blog-post
title: "What's the ROI of software engineers' spending on AI?"
author: Gergely Orosz (The Pragmatic Engineer)
date_published: 2026-10-20
date_extracted: 2026-10-21
last_checked: 2026-10-21
status: current
confidence_overall: anecdotal
issue: "#4248"
---

# What's the ROI of software engineers' spending on AI? (Pragmatic Engineer)

> Per-developer AI spend bands and PR-throughput before/after figures from 27 companies plus CodeRabbit/Gitar vendor aggregates, showing that PR volume rises far more reliably than delivery velocity, and that spend caps are the dominant control.

## Source Context

- **Type**: blog-post (paid newsletter)
- **Author credibility**: Gergely Orosz writes The Pragmatic Engineer and has broad access to engineering leaders; the data here are interviews he collected, not instrumented measurements.
- **Scope**: Covers sections 1-3 and the start of section 4 only (CodeRabbit/Gitar stats, patterns across the 27 companies, high spenders $1,000+/month). The canonical page is paywalled; the text was read from the feed's `content:encoded` field, which ends at the "AI spend at Big Tech" heading with a "Read more" cut-off. Big Tech (Meta, NVIDIA, Apple), medium spenders ($300-500), low spenders (<$300) and the final "What's the ROI of AI?" section were NOT readable and nothing is inferred about them. Charts are images and their values are unavailable except where the text states them.

## Extracted Claims

### Claim 1: Developers using CodeRabbit create roughly twice as many PRs per week as a year ago
- **Evidence**: Vendor-aggregated, anonymized CodeRabbit data: +113% weekly PRs, +127% monthly PRs, and +128% when tracking a fixed cohort of 20,000 developers for a year. Chart images only.
- **Confidence**: anecdotal (vendor aggregate, no control group; platform users are self-selected adopters of an AI review tool)
- **Quote**: "On average, devs are creating more than twice as many PRs as they did a year ago."
- **Our assessment**: Plausible direction, but a PR count is the metric Faros warns is a vanity metric (see Cross-References). Cohort tracking guards against population drift but not against PR-splitting or verbose generation.

### Claim 2: Teams fall into culturally determined "tiers" of PR frequency; AI-native teams ship 60+ PRs/dev/week
- **Evidence**: Gitar (described as Sonar's AI code verification agent) data across hundreds of customers; the 60+ figure comes from the intro summary, the tier chart is an image. Orosz's explanation of the tiers is his own suspicion.
- **Confidence**: anecdotal
- **Quote**: "Meanwhile, Gitar sees “AI-native” teams ship 60+ PRs/dev/week."
- **Our assessment**: A vendor statistic with no definition of "AI-native". Orosz's culture hypothesis ("whenever you join a new team, you pick up the pace pretty quickly") is speculation but a useful caution that PR rate partly reflects team norms and PR granularity.

### Claim 3: Company size and AI spend are unrelated
- **Evidence**: Two data points from the 27-company set: a 2-person .NET startup at $3,000/dev/month versus a public company with 1,500 engineers capped at $150/month.
- **Confidence**: anecdotal
- **Quote**: "Company size and spend on AI are unrelated."
- **Our assessment**: Supported by the extremes cited, but sample is small and self-selected; read it as "policy and culture, not headcount, set the budget", not a statistical finding.

### Claim 4: Per-dev spend peaked in summer 2026 and is falling, largely from model change
- **Evidence**: Interviewee reports; costs "roughly halved" for API-plan companies. Attributed to Opus 5.5 and a move to open models. Also, the hospitality Series D engineer expects spend to halve moving from Opus 5 to Opus 5.5.
- **Confidence**: anecdotal
- **Quote**: "June and July saw peak monthly spend at nearly all companies, and costs have roughly halved for those on API plans."
- **Our assessment**: Contrasts with the quant shop where spend rose 16x since January, so "falling" is not universal. Useful reminder that cost budgets are model-version-dependent and go stale.

### Claim 5: Spending caps are the norm at medium-and-above spenders, and are usually soft
- **Evidence**: Across the 27 companies; individual caps listed: $1,500 default (Series D hospitality, can request more), $1,200 budget (public SaaS; under 5% of devs hit it), $1,000 soft cap with short justification form (5,000-employee public company), $2,000 effectively hard (AI SaaS), $4,000 hard (multinational; average ~$1,000), $25,000 per employee (quant shop).
- **Confidence**: emerging (consistent pattern across many independent interviewees)
- **Quote**: "It’s normal to have a spending cap in place at medium-and-above spenders, where additional spend needs to be justified. Most people say the caps are easily avoided."
- **Our assessment**: Credible and practically useful: caps function as a justification speed bump more than a ceiling. The AI SaaS counter-example shows a deliberately hard cap enforced socially.

### Claim 6: Flat-rate subscriptions hide true cost, and subsidies are ending
- **Evidence**: Several unnamed companies said subsidized subscriptions are ending.
- **Confidence**: anecdotal
- **Quote**: "Several companies mentioned that their subsidized AI subscriptions are coming to an end, so they need to prepare to either optimize costs, or have their bill increase 5-10x."
- **Our assessment**: Important planning risk for any ROI calculation based on current subscription pricing. No vendor named, no evidence offered beyond interviewees.

### Claim 7: A quant trading firm's AI spend grew ~16x in nine months, with traders (not devs) the biggest spenders
- **Evidence**: Current engineer: $8M/month in September vs $500K/month in January (~2,000 devs); average $1,600/dev/month, up from ~$80; $25,000 per-employee limit. The article's intro summary says "15x" while the section body says 16x ($8M / $500K = 16x).
- **Confidence**: anecdotal
- **Quote**: "total spend was $8M/month in September, a 16x increase on the $500K/month spend in January!"
- **Our assessment**: Single firm, unusual economics. The takeaway worth keeping: non-engineers can dominate agent spend, and rate limiting is needed for accidental expensive queries ("Engineering is learning the importance of rate limiting for traders who accidentally run expensive queries without realizing it.").

### Claim 8: Quant firms judge AI ROI by desk profit, so AI is just a cost-base line
- **Evidence**: Interviewee explanation; no numbers.
- **Confidence**: anecdotal
- **Quote**: "ROI is measured differently at trading firms."
- **Our assessment**: Illustrates that ROI tolerance depends on how directly the business converts output into revenue; not generalizable to most engineering orgs.

### Claim 9: PR frequency rises sharply for small, high-agency teams on a single stack
- **Evidence**: Two-person EU .NET/Blazor shop at $3,000/dev/month reports ~60 PRs/dev/week (10-15/day) vs 1-2/day before; "work of about 5-7 people"; used heavily on backlog cleanup of 5-10 year old systems. Spend mostly Claude Opus and GitHub Copilot.
- **Confidence**: anecdotal
- **Quote**: "We used to do 1-2 PRs per day, and now it’s 10+. It feels like our two-person team is doing the work that would have taken about 5-7 people before AI."
- **Our assessment**: Self-report from the developers themselves, greenfield-ish agency work. Note that this lone team is also the likely anchor for the 60+/week Gitar-style figure, but the article does not link them.

### Claim 10: At companies that keep quality standards, PR volume can rise without velocity rising
- **Evidence**: Public SaaS (~600 engineers): PR volume "up (no data)", merge velocity little changed; human reviewers still catch unnecessary changes and PRs "10 times bigger than they should be". AI SaaS (~100 employees, $2,000 cap): velocity unchanged. Hospitality Series D: PR frequency not much changed, deliberately holding PR size and quality standards.
- **Confidence**: anecdotal (three interviewees)
- **Quote**: "When the focus is on quality, velocity probably does not increase all that much."
- **Our assessment**: Directly relevant to the guide's throughput claims. Interviewee's own framing: "Overall, I personally see accelerated slop produced all around me" (same company, same quote block). Consistent with the Faros 47%-more-PRs/35%-longer-review result.

### Claim 11: Higher spend does not map to higher PR frequency; one $1,000-cap company saw flat PR count but 3x larger PRs
- **Evidence**: 5,000-employee public company with $1,000 soft cap: backend engineers ~$1,500/month, Staff+/leads ~$2,500/month, PR frequency flat, lines per change request 3x. Versus a 5,000-dev company at ~$1,000/dev/month average with PRs doubling from ~4 to ~8/dev/week (experienced engineers 2-3x).
- **Confidence**: anecdotal
- **Quote**: "Meanwhile, PRs have exploded in size and have 3x as many lines of code per change request as before."
- **Our assessment**: Strong evidence against using raw PR count as the ROI proxy Orosz proposes at the top of the piece. His own speculation that LLM verbosity explains the 3x is unverified.

### Claim 12: Story-level metrics give a more credible velocity signal than PR counts
- **Evidence**: Multinational (10K+ employees, Copilot, $4,000 hard cap, ~$1,000 average): one team's PRs rose from ~1.5 to ~4/dev/week, but the lead says this is skewed by one engineer; user stories closed per month are ~3x higher since Feb/March, and for the first time more are closed than incoming. Based on 5 years of Scrum+Kanban plan-board history.
- **Confidence**: anecdotal (single team lead; team not fully adopted)
- **Quote**: "On average we close 3x more user stories per month since feb/march. It tells me we deliver more business value."
- **Our assessment**: The best-instrumented before/after in the piece because it uses a pre-existing stable process metric, but it is still one team and one reporter.

### Claim 13: Public leaderboards and AI-assisted justification are used as soft cost-control mechanisms
- **Evidence**: AI SaaS (~100 employees) runs a public #ai-limits Slack channel pinging those near limits and top spenders; to request a raise you first run an AI skill that audits for wasteful loops/subagents, then ask your manager. Engineer says increases are rarely granted so the $2K is treated as hard.
- **Confidence**: anecdotal
- **Quote**: "When needing a limit increase, you run an AI skill that looks for common reasons why you might be burning tokens."
- **Our assessment**: Novel concrete mechanism. Orosz notes it "sounds a bit like a “public embarrassment” strategy!" - an effect on adoption was not examined, and the same engineer says most colleagues are adopting slowly.

### Claim 14: AI shows largest gains outside raw code output (triage, research, POCs)
- **Evidence**: Public SaaS Staff Engineer: customer-issue triage from a day to minutes plus at most an hour of verification; code-history research from 1-2 days to minutes; complex POC prototypes for PMs from 1-2 weeks to hours.
- **Confidence**: anecdotal
- **Quote**: "Triaging of customer issues. What previously took a whole day sometimes, is now finished in a few minutes with agent work and a maximum one hour of human verification."
- **Our assessment**: Specific time-saving ranges, self-reported by one engineer; worth listing as use cases that don't show up in PR metrics.

### Claim 15: Few companies can answer the ROI question
- **Evidence**: Stated in the free summary bullet; the full section is behind the paywall/cut-off and was not read.
- **Confidence**: emerging
- **Quote**: "What’s the ROI of AI? A question that few companies seem able to answer – at least for now."
- **Our assessment**: The article provides spend and throughput data, not a measured ROI. Orosz motivates PR throughput as ungamed because "it’s possible to compare a “before AI” and “after AI” measurement", yet the cases above undermine it as a value proxy.

## Concrete Artifacts

```
Spend bands from the 27-company interviews (Pragmatic Engineer, 2026-10-20; only $1,000+ tier readable)
Company                                  Spend/dev/mo         Cap                    PR change
Quant shop (~2,000 devs)                 avg $1,600 (was $80) $25,000/employee       n/a
2-dev .NET shop, EU                      $3,000               n/a                    1-2/day -> 10+/day (~60/wk)
Series D hospitality (~200 eng)          up to $2,200         $1,500 default         not much changed
Public SaaS (~600 eng)                   cap $1,200           $1,200 (<5% hit)       volume up (no data); velocity flat
Public co (~5,000 devs)                  avg $1,000           $1,000 soft (planned)  ~4 -> ~8 PRs/dev/week
Public co (5,000 employees)              $1,500 / $2,500      $1,000 soft            flat count, 3x lines per PR
AI SaaS (~100 employees)                 allowance $2,000     effectively hard       velocity unchanged
Multinational (10K+)                     avg ~$1,000          $4,000 hard            1.5 -> 4 PRs/dev/week (one team); 3x stories closed
```

```
CodeRabbit (vendor-aggregated, anonymized): weekly PRs +113%, monthly PRs +127%, fixed 20,000-dev cohort +128%.
Gitar: "AI-native" teams 60+ PRs/dev/week.
```

## Cross-References

- **Corroborates**: `blog-faros-claude-code-roi.md` Claim 3 (47% more PRs merged daily but 35% longer review) and Claim 5 (raw PR counts as a vanity metric): Claims 10 and 11 here show PR count rising or staying flat independent of velocity and with 3x larger PRs. `blog-anthropic-cost-visibility-control.md` Claim 8 (hard spend caps at org, user and group level) and `blog-anthropic-admin-analytics-cost-controls.md` Claim 7 (spend-threshold alerts and user limit requests): Claim 5 here shows these mechanisms in real company practice, including the limit-request workflow.
- **Contradicts**: None filed. Orosz opens by calling PR throughput a useful, not-yet-gamed metric, which is in tension with Faros Claim 5, but his own data (Claims 10-11) largely concede the point, so no contradiction issue was filed.
- **Extends**: `survey-pragmaticengineer-ai-tooling-2026.md` (adoption survey that lists productivity metrics as a gap) with spend and throughput figures. `blog-anthropic-cost-visibility-control.md` Claim 1 (cost-per-outcome rather than token consumption): Claim 12 here is an example of an outcome metric (stories closed).
- **Novel**: Per-dev monthly spend bands and cap levels across real companies; the 16x quant-shop growth; public #ai-limits channel and AI-audit-before-raise workflow; subsidized-subscription end risk (5-10x); 3x PR-size inflation with flat PR count; spend decline since summer 2026 linked to Opus 5.5 and open models.

## Guide Impact

- **Chapter 05**: The "Measuring AI ROI" passage (currently sourced only to `blog-faros-claude-code-roi`, marked [stale]) could add an additional corroborating source: PR count alone misleads (flat count with 3x PR size; rising volume with flat merge velocity), and an outcome-based metric (stories closed) was the only credible velocity gain reported. Attribute as practitioner reports, not measured effects.
- **Chapter 05**: Add a cost-governance example paragraph: typical per-dev spend bands ($1,000-$4,000 caps at larger firms) with soft caps plus justification forms, citing Claims 5 and 13, and warn that subsidized subscriptions may end (Claim 6).
- **Chapter 00**: If an ROI framing is used, note that the article reports no measured ROI (Claim 15); avoid quoting CodeRabbit/Gitar figures as independent evidence of productivity.

## Extraction Notes

- Text was read from the Pragmatic Engineer feed `content:encoded` (about 13.8K characters), not the paywalled page, as the triage comment advised. The feed excerpt truncates at the Big Tech section; the later sections, charts, and the closing ROI section were not available and nothing is inferred from them.
- All quotes were copied from that feed text; the "15x" (summary) vs "16x" (body) discrepancy in the source is noted in Claim 7.
- Triage comments mention Meta/NVIDIA/Apple, the $300-500 tier, and Lendscape/Lonestone/Paulina24; those names appear only in the summary bullets and were not extracted as claims.
- Cross-referenced claim numbers were checked against headings in the cited notes.
