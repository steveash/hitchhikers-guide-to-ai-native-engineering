---
source_url: https://cursor.com/blog/better-models-ambitious-work
source_type: blog-post
title: "Better AI models enable more ambitious work"
author: Luke Melas-Kyriazi (Cursor / Anysphere), with Prof. Suproteem Sarkar (University of Chicago Booth School of Business)
date_published: 2026-04-15
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#245"
---

# Better AI models enable more ambitious work

> A Cursor + UChicago Booth peer-partnered empirical study (n=500 companies, July 2025–March 2026) documenting a Jevons-like demand expansion from model upgrades: AI usage rose 44%, with high-complexity tasks growing 68% vs. low-complexity 22%, but only after a 4–6 week lag — and with a structural shift in what developers do: documentation, architecture, and code review expanded 3–4× faster than UI/styling.

## Source Context

- **Type**: blog-post (companion summary to a peer-partnered research paper on SSRN, DOI abstract_id=6578939, with Professor Suproteem Sarkar of the University of Chicago Booth School of Business as academic co-researcher)
- **Author credibility**: Luke Melas-Kyriazi writes from inside Cursor's engineering and research organization. The study is co-designed with a Booth professor, giving it more methodological rigor than typical vendor blog posts. Behavioral data (message logs) rather than self-report survey is the primary source. This is a vendor publication and should be read with that lens — Cursor benefits from showing that better models drive more Cursor usage — but the SSRN submission signals academic accountability. Treat quantitative findings as emerging rather than settled.
- **Scope**: 500 companies using Cursor from July 2025 through March 2026. Covers two model-step-change releases (Opus 4.5, GPT-5.2). Measures AI usage volume, task complexity distribution, task-category distribution, and industry-level adoption rates. Does NOT measure code quality outcomes, individual developer productivity, team-level throughput, or failure rates. The unit of analysis is usage patterns (messages per user per week), not outcomes (bugs shipped, PR cycle time).

## Extracted Claims

### Claim 1: AI usage grew 44% over the 8-month study period, consistent with a Jevons-like demand expansion

- **Evidence**: Behavioral measurement of average weekly messages per user across 500 companies, July 2025–March 2026. Covers two step-change model releases.
- **Confidence**: emerging (behavioral data, first-party; no external validation; vendor has incentive to report high usage)
- **Quote**: "Better AI leads to greater AI demand. This is consistent with a Jevons-like effect, where gains in efficiency increase total consumption rather than reducing it."
- **Our assessment**: The Jevons framing is the most intellectually load-bearing claim. The Jevons paradox (efficiency gains increase total consumption) was historically observed in coal and energy markets; the authors argue the same dynamic applies to AI model capability. The 44% usage growth figure is plausible directionally — this is consistent with what the Anthropic internal study found (usage doubled at Anthropic over a similar window) — but is inherently self-referential: Cursor is measuring usage on Cursor. Growth in Cursor usage does not prove that total developer AI demand is rising, only that Cursor's share of that demand is rising. The Jevons framing is intellectually useful even if the magnitude is uncertain.

### Claim 2: Developers first used better models for similar-complexity work, then shifted to complex tasks after a 4–6 week lag

- **Evidence**: Temporal analysis of complexity distribution across the 8-month study. Low-complexity messages grew +22% over the full period; high-complexity messages grew +68%, with "most of that growth occurring during the last six weeks."
- **Confidence**: emerging (temporal behavioral data from a single platform; confounds include natural seasonal variation in developer workload)
- **Quote**: "Initially, developers did more of the same with the improved AI models, but after a lag of 4–6 weeks, we observed that they began using models for more complex tasks."
- **Our assessment**: The 4–6 week lag is the most practically actionable finding in the study. If correct, it means: (1) evaluating a model upgrade in the first month will understate its impact; (2) adoption planning should account for a discovery-and-reorientation period; (3) week-1 AI usage metrics are not predictive of steady-state behavior. The proposed mechanism — "the time it takes developers to discover what a better model can do, and the need for firms to reorient their workflows around new capabilities" — is plausible but the authors do not empirically distinguish between individual discovery time and organizational reorientation time. Both explanations have different implications for adoption planning.

### Claim 3: High-complexity AI usage grew 68% vs. 22% for low-complexity over the study period

- **Evidence**: Message complexity classification over the 8-month behavioral dataset. High-complexity growth concentrated in the final six weeks.
- **Confidence**: emerging (depends on the complexity classification methodology, which is not described in the blog post)
- **Quote**: "Low complexity messages: +22% over the study period. High complexity messages: +68%, with most of that growth occurring during the last six weeks."
- **Our assessment**: The 68% vs. 22% gap is large. Without knowing the complexity classification methodology (is it based on message length? task category? model output length? user-defined flags?), we cannot evaluate whether the gap is real or an artifact of the classifier. The Anthropic internal study found a related pattern — autonomous tool calls doubled from ~10 to ~20 actions per task over Feb–Aug 2025 — which is a different measure of the same phenomenon (agents taking on longer-horizon work). These two datasets converge directionally even if the exact metrics differ.

### Claim 4: Task-category distribution shifted heavily toward documentation, architecture, and code review — and away from UI/styling

- **Evidence**: Category-level breakdown of message growth over the study period.
  - Documentation: +62%
  - Architecture: +52%
  - Code review: +51%
  - Learning: +50%
  - UI/styling: +15%
- **Confidence**: emerging (task category classification methodology not described; categories may be ambiguous at the margin)
- **Quote**: "as AI-generated code expands codebase size, the need to document, understand, and review that code grows in proportion. Larger and faster-moving codebases also increase the complexity of managing how it all fits together, which may explain the sharp growth in cross-system tasks like architecture and deployment."
- **Our assessment**: This is the most structurally interesting finding for the guide. The proposed causal mechanism — AI-generated code expands the codebase faster than human-authored code, which proportionally increases documentation debt, review burden, and architectural complexity — is coherent and consistent with what practitioners report anecdotally. UI/styling growing only +15% (vs. architecture +52%) suggests that the low-creativity, pattern-following parts of the stack are becoming more commoditized, while the integrative, judgement-heavy parts are expanding. For daily-workflow guidance: if this trend continues, the work that remains distinctly human is precisely the high-judgment work (architecture decisions, cross-system understanding, code review) that the guide's chapters on verification and collaboration already emphasize.

### Claim 5: Industry-specific adoption rates vary — media/advertising +54%, software/dev tools +47%, finance/fintech +45%

- **Evidence**: Industry-level segmentation of the 44% overall growth figure across the 500-company dataset.
- **Confidence**: emerging (industry classification not described; sample composition unknown — if software/dev tools companies are overrepresented, the headline +47% may be conservative for that sector)
- **Quote**: "In finance, better AI can create an arms-race dynamic, where once one firm uses AI to gain a trading edge, others face competitive pressure to follow." "For media/advertising: the mechanism may be different, with more capable models expanding greenfield opportunities that firms take advantage of."
- **Our assessment**: The two proposed adoption mechanisms (arms-race vs. greenfield expansion) are usefully distinct for team-adoption planning. Arms-race adoption is externally driven and compliance-shaped — the decision to adopt is made by competitive pressure, not internal engineering judgment. Greenfield adoption is internally driven and capacity-shaped — teams adopt because they now have capability for work that was previously out of reach. Teams in finance contexts should expect adoption pressure from outside the engineering organization; teams in media/advertising contexts should expect adoption to be self-directed and experimental.

### Claim 6: AI adoption does both existing-work facilitation and new-work expansion — and expansion may eventually be the bigger story

- **Evidence**: Inferred from the task distribution shift and Jevons framing; not an independently measured metric.
- **Confidence**: anecdotal (authorial interpretation of the dataset; not a directly measured claim)
- **Quote**: "A central question around AI adoption is whether it merely facilitates existing work, or also opens up new productive opportunities. Our study indicates that it does both, but that expansion may eventually be the bigger story."
- **Our assessment**: The "expansion may eventually be the bigger story" framing aligns with the Anthropic internal study's Claim 3 (27% of Claude-assisted work consists of tasks that wouldn't have been done otherwise). Both studies point in the same direction: AI is not just doing the same work faster, it's enabling new categories of work. For the guide's measurement section: teams that only measure "did we close existing tickets faster" will miss the expansion contribution. The right measurement captures new categories of work initiated, not just existing backlog velocity.

## Concrete Artifacts

### Study Design Summary

```
# Cursor / UChicago Booth Behavioral Study (April 2026)

DATA SOURCE
  Platform: Cursor (AI coding tool)
  Measurement: Average weekly messages per user (behavioral, not self-report)
  Sample: 500 companies
  Period: July 2025 – March 2026 (8 months)
  Triggers: Two model step-change releases studied (Opus 4.5, GPT-5.2)
  Full paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6578939
  Academic co-researcher: Prof. Suproteem Sarkar, University of Chicago Booth School of Business

KEY METRICS (overall)
  Usage growth: +44% weekly messages per user
  Low-complexity messages: +22%
  High-complexity messages: +68% (growth concentrated in final 6 weeks)
  Adoption lag: 4–6 weeks before complexity shift visible after model upgrade

TASK CATEGORY GROWTH
  Documentation:  +62%
  Architecture:   +52%
  Code review:    +51%
  Learning:       +50%
  UI/styling:     +15%

INDUSTRY BREAKDOWN
  Media and advertising:       +54%
  Software and developer tools: +47%
  Finance and fintech:         +45%
```

### Key Quotes

```
Jevons framing:
"Better AI leads to greater AI demand. This is consistent with a Jevons-like
effect, where gains in efficiency increase total consumption rather than
reducing it."

Complexity lag:
"Initially, developers did more of the same with the improved AI models,
but after a lag of 4–6 weeks, we observed that they began using models
for more complex tasks."

Lag mechanism:
"the lag reflects both the time it takes developers to discover what a
better model can do, and the need for firms to reorient their workflows
around new capabilities."

Task shift interpretation:
"as AI-generated code expands codebase size, the need to document,
understand, and review that code grows in proportion. Larger and
faster-moving codebases also increase the complexity of managing how
it all fits together, which may explain the sharp growth in cross-system
tasks like architecture and deployment."

Finance arms-race mechanism:
"In finance, better AI can create an arms-race dynamic, where once one
firm uses AI to gain a trading edge, others face competitive pressure
to follow."

Opening research question:
"We are interested in understanding how improvements in AI models change
how developers work. In particular, to what extent do developers perform
more of the tasks they were already doing, and to what extent do better
models enable work that was out of reach before?"

Conclusion framing:
"A central question around AI adoption is whether it merely facilitates
existing work, or also opens up new productive opportunities. Our study
indicates that it does both, but that expansion may eventually be the
bigger story."
```

## Cross-References

- **Corroborates**:
  - `research-anthropic-ai-transforming-work.md` — Claim 3 (27% of Claude-assisted work consists of tasks that wouldn't have been done otherwise) is the internal Anthropic equivalent of the Jevons finding: AI creates new work, not just faster old work. Claim 5 (autonomous tool calls doubled from ~10 to ~20 actions per task, Feb→Aug 2025) is a different measure of the same complexity-increase phenomenon that this study's +68% high-complexity figure documents. The two studies converge directionally from different methodologies (internal usage logs at 1 company vs. behavioral data at 500 companies), strengthening the overall signal.
  - `survey-pragmaticengineer-ai-tooling-2026.md` — High adoption trajectory and staff+ leading complex-task usage (63.5%) align with the Cursor study's finding that complex task growth (+68%) concentrates in the later period as developers grow into new capability. Both datasets show AI use is expanding in scope, not just in volume.

- **Extends**:
  - `research-anthropic-ai-transforming-work.md` — The Cursor study is larger (500 companies vs. 132 individuals at 1 company), externally validated (academic co-researcher), and covers a different time window (July 2025–March 2026 vs. Feb–Aug 2025). It adds the Jevons framing, industry-level segmentation, and task-category shifts that the Anthropic report does not cover. Together they are stronger than either alone: one provides the internal behavioral richness (team-by-team, tool-call-level analysis); the other provides external scale and the economic demand-expansion framing.
  - `survey-pragmaticengineer-ai-tooling-2026.md` — The Pragmatic Engineer survey documents adoption patterns via self-report; this study adds behavioral measurement (actual usage data) and the temporal complexity-shift dynamic that surveys cannot capture.

- **Contradicts**: None filed. The Jevons-like finding is broadly consistent with all prior corpus sources. No existing note claims AI reduces overall AI demand or that task complexity does not shift after model upgrades.

- **Novel**: This study introduces to the corpus:
  - **The 4–6 week complexity-adoption lag** — no prior source documents the timing of the shift from same-complexity to higher-complexity tasks following a model upgrade. This is directly actionable for adoption planning (don't evaluate a model upgrade by week-1 metrics).
  - **Empirical Jevons framing at scale** — prior sources described demand expansion qualitatively or via small internal datasets. This is the first corpus source to frame it explicitly as Jevons at n=500 companies over 8 months.
  - **Task-distribution shift as a structural prediction** — the proposed mechanism (AI expands codebase → meta-work grows proportionally) is not stated elsewhere and generates a testable prediction: documentation/architecture/code review should keep growing faster than generative coding tasks as AI-generated code volume rises.
  - **Industry-sector adoption mechanisms** (arms-race in finance, greenfield in media) — no prior source distinguishes adoption drivers by sector.

## Guide Impact

### Chapter 01: Daily Workflows

- **"What developers actually spend time on"**: Use the task-distribution shift (documentation +62%, architecture +52%, code review +51% vs. UI/styling +15%) as evidence that the daily workflow of an AI-native developer skews toward high-judgment meta-work, not code generation. Frame as: "The more AI generates code, the more developer time shifts to understanding, reviewing, and architecting it. Chapter 01 should set expectations that AI-native engineering means *more* time on architecture and documentation, not less — not because the work gets harder, but because there is more of it to manage."

### Chapter 05: Team Adoption

- **"Plan for the 4–6 week lag"**: Add as a concrete adoption-planning heuristic: do not evaluate a model upgrade's impact before six weeks post-rollout. Teams that measure AI productivity in week 1 or 2 will see mostly volume growth in existing-complexity tasks and underestimate the subsequent complexity shift. Recommend setting rollout evaluation milestones at weeks 4, 8, and 12, not week 2.
- **"The Jevons effect as a counterargument"**: Use the +44% usage growth finding to directly address the "AI will reduce developer headcount" prediction. If AI efficiency gains cause *more* AI consumption, not less, the demand curve for developer effort shifts outward, not inward — especially for the high-judgment work (architecture, code review) that AI cannot fully automate. This is the empirical counterweight to the displacement-only narrative.
- **"Industry context shapes adoption trajectory"**: Add a note distinguishing arms-race adoption (finance, externally driven) from greenfield adoption (media, internally driven). Teams in regulated industries with competitive AI pressure should expect faster mandated rollout; teams in greenfield contexts have more latitude to adopt experimentally. Adoption playbooks should branch on this distinction.
- **"Measuring expansion, not just acceleration"**: Pair with `research-anthropic-ai-transforming-work.md` Claim 3 (27% of tasks are new). Adoption success metrics should capture new categories of work initiated, not just existing ticket velocity. A team that is not seeing new categories of work emerge after 8+ weeks of AI use may be under-utilizing the capability.

## Extraction Notes

1. **Full paper inaccessible**: The SSRN paper (abstract_id=6578939) returned a 403 error during extraction. The blog post is the primary accessible source and contains the key quantitative findings. The methodology details — complexity classification method, category classification scheme, sample composition by industry — are not described in the blog post and could differ materially from what the methods section of the full paper describes. Treat classification-dependent figures (task categories, complexity buckets) as emerging with higher uncertainty than the aggregate usage growth figure.
2. **Complexity classification opaque**: The blog post does not describe how "high complexity" vs. "low complexity" messages are classified. This is a significant gap — if the classifier is based on message length or token count, it may conflate verbose prompts with genuinely complex tasks. The Assayer should flag if this detail is obtainable from the full paper.
3. **Vendor framing caveat**: Cursor publishes this. The core finding ("better models drive more Cursor usage") aligns with Cursor's commercial interest. The Jevons framing is intellectually honest but also convenient — it reframes "usage growth" as an economic law rather than a product metric. Read the headline numbers with this lens: they are likely accurate as measures of Cursor usage, but their interpretation as general-AI-demand expansion requires the external comparison the study does not provide.
4. **No code quality data**: This study measures what developers *ask* AI to do, not whether the output is good. For the quality dimension, pair with `paper-miller-speed-cost-quality.md` (external measurement of code quality after AI adoption).
5. **No contradictions filed**: The findings are directionally consistent with all prior corpus sources. The Jevons finding reinforces rather than contradicts the Anthropic study's "27% new work" claim.
