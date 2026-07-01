---
source_url: https://newsletter.pragmaticengineer.com/p/the-job-market-in-2026-part-2
source_type: blog-post
title: "The job market in 2026, part 2"
author: Gergely Orosz and Jessica Salmon (The Pragmatic Engineer)
date_published: 2026-06-09
date_extracted: 2026-07-01
last_checked: 2026-07-01
status: current
confidence_overall: emerging
issue: "#1399"
---

# The job market in 2026, part 2

> A market-analysis newsletter piece arguing that the AI-adoption boom is
> restructuring the *demand side* of the software engineering job market, not
> just individual workflows: AI labs are out-recruiting Big Tech, new-grad and
> intern hiring keeps shrinking even as overall hiring recovers, frontend and
> native-mobile titles are disappearing in favor of full-stack and AI-engineer
> roles, and management headcount is shrinking relative to engineer headcount
> (the "great flattening").

## Source Context

- **Type**: blog-post / market-analysis (The Pragmatic Engineer newsletter,
  Substack; second installment in a two-part series, published two weeks
  after Part 1)
- **Author credibility**: Gergely Orosz is an ex-Uber engineering manager who
  runs The Pragmatic Engineer, the largest paid technology newsletter on
  Substack (~750k+ subscribers). This piece is co-bylined with Jessica
  Salmon. The article draws on third-party labor-market data (Interviewing.io
  coaching-request data, job-title analysis) rather than Orosz's own survey
  instrument — a different evidentiary basis than the same author's
  `survey-pragmaticengineer-ai-tooling-2026` (a self-run practitioner
  survey). Orosz is a practitioner-journalist, not an economist or
  labor-market researcher; the piece synthesizes and interprets third-party
  datasets rather than presenting original raw data.
- **Scope**: Covers macro job-market structure in 2026 — employer
  attractiveness and retention at AI labs vs. Big Tech, new-grad/intern
  hiring trends, the decline of frontend/mobile as standalone titles, AI vs.
  general software engineering compensation, and shrinking management ratios.
  Does NOT cover individual tool adoption, workflow practices, harness
  configuration, or productivity/quality outcomes — those are the domain of
  the same author's tooling survey and other sources in this corpus. Part of
  the article (the compensation-comparison section) is paywalled; see
  Extraction Notes.

## Extracted Claims

### Claim 1: Anthropic has become the single most sought-after employer for engineering candidates, ahead of OpenAI and Big Tech
- **Evidence**: Interviewing.io coaching-request data, cited by the article, showing Anthropic and OpenAI together account for the majority of coaching demand, with Anthropic alone the largest single share.
- **Confidence**: emerging
- **Quote**: "Anthropic and OpenAI account for 51% of all interviewing.io coaching requests"
- **Our assessment**: Coaching-request volume is a reasonable proxy for "which employer are candidates preparing hardest to get into," but it is a proxy, not a direct measure of offer acceptance or applicant volume — engineers might seek coaching disproportionately for employers with famously difficult interview loops rather than employers they most want to join. Still, combined with the retention data (Claim 2) and the recruiting factors cited (funding round, IPO filing, Claude Code's popularity, hiring Andrej Karpathy), this is a reasonably well-triangulated claim that frontier AI labs are currently winning the talent competition against traditional Big Tech.

### Claim 2: AI labs retain engineers at meaningfully higher rates than Big Tech, with a gap even between labs
- **Evidence**: Two-year retention rates cited in the article: Anthropic 80%, Google DeepMind 78%, OpenAI 67%.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment — the retention figures are stated as data points rather than embedded in a quotable sentence)
- **Our assessment**: The OpenAI figure (67%) is presented as "consistent with Big Tech" retention norms, which implies Anthropic's 80% is the outlier requiring explanation, not the baseline. This is useful evidence against a simplistic "AI lab = AI lab" framing: within the frontier-lab category there is real variance, and Anthropic's retention edge specifically (rather than "AI labs in general") is the standout data point. Should not be over-read as a durable structural fact — retention rates are a snapshot and can shift quickly with a single high-profile departure or compensation event.

### Claim 3: AI engineering job openings grew roughly 60% year-over-year even as new-graduate and intern hiring contracted
- **Evidence**: Industry-wide job-opening growth figure cited by the article, contrasted with declining new-grad hiring share.
- **Confidence**: emerging
- **Quote**: "AI engineering job openings have increased 60% in the past year"
- **Our assessment**: The juxtaposition is the interesting part: aggregate engineering hiring recovering, AI-specific roles surging ~60%, and new-grad/intern intake falling at the same time. That combination is consistent with a market that is not simply "hiring more engineers" but reallocating hiring toward a specific, higher-skill specialization while raising the bar for entry-level roles. As one practitioner quoted in the piece put it, this defies the normal pattern where growing demand pulls more entry-level hiring along with it.

### Claim 4: New-graduate hiring at larger companies has fallen from roughly 3-in-10 to roughly 1-in-10 of engineering hires between 2023 and 2025, alongside a multi-year decline in intern hiring
- **Evidence**: Year-over-year hiring-composition figures cited in the article, plus commentary from a named source (Alex Hamilton) noting intern intake fell even during a period when it would normally track overall hiring.
- **Confidence**: emerging
- **Quote**: "In 2025, just one in 10 engineering hires at larger companies were recent grads, down from nearly three in 10 in 2023"
- **Our assessment**: This is the most concrete, falsifiable statistic in the piece and the most consequential for a "how do we staff AI-native teams" chapter: if entry-level hiring is structurally contracting, "hire more juniors and let AI make them productive faster" is not the strategy most large companies are actually pursuing. Combined with the article's note that elite-university pedigree now matters more for the shrinking pool of new-grad hires, the pattern reads as a bar-raising contraction, not a proportional scale-down — companies are hiring fewer new grads and being more selective about which ones, not simply hiring less of everything evenly.

### Claim 5: Frontend and native-mobile engineering are disappearing as standalone job titles in favor of full-stack roles, while AI engineering, Forward Deployed Engineer, and sales-engineer titles are growing
- **Evidence**: Job-title analysis cited by the article covering shifts in posted role titles.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment — this claim is stated as a title-trend finding rather than a single quotable sentence)
- **Our assessment**: This is a title-taxonomy claim, not a claim that frontend or mobile *work* is disappearing — the article's own framing is that "pure" frontend roles are concentrating at larger companies that need dedicated design-systems expertise, implying the specialization survives but consolidates into fewer, larger employers rather than being spread across the market. For a team-adoption chapter, the actionable read is narrower than "frontend engineers are obsolete": it's that generalist/full-stack hiring is displacing specialist hiring at small-and-mid-size companies specifically, which is a different (and more defensible) claim.

### Claim 6: AI engineering compensation now exceeds general software engineering compensation at comparable seniority, and senior engineers at the 80th percentile expect $300K+ base salaries in the US
- **Evidence**: Compensation-comparison data referenced by the article (section partially paywalled — see Extraction Notes) plus a specific base-salary figure for senior engineers.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment — the underlying comparison section was not fully accessible; treat the compensation-gap claim as directionally reported rather than independently verified against primary figures)
- **Our assessment**: Downgraded confidence relative to the other claims because the full comparison methodology was not visible in extraction (paywalled). The direction of the claim (AI-specialist comp > generalist SE comp) is plausible and consistent with the AI-labs-outcompeting-Big-Tech narrative elsewhere in the piece, but without seeing the actual comparison table this should be treated as a headline claim to verify against a primary compensation-survey source (e.g., levels.fyi, a future Pragmatic Engineer compensation report) before it anchors a guide recommendation.

### Claim 7: Engineering-management headcount is shrinking relative to engineer headcount industry-wide — the "great flattening"
- **Evidence**: Industry-wide trend the article attributes to falling counts of VP Engineering and Director-level roles at Big Tech specifically, framed as a continuation of an existing trend rather than a new one.
- **Confidence**: emerging
- **Quote**: "There are fewer engineering managers for each engineer across the industry"
- **Our assessment**: The word "continues" in the article's own section heading matters — this is presented as an ongoing multi-year trend, not a 2026-specific inflection tied to AI adoption. The article does not explicitly draw a causal line from "AI makes each engineer more productive" to "therefore fewer managers are needed," and the Miner did not find a stated mechanism connecting the two in the accessible text. Any guide use of this claim should describe it as a concurrent trend during the AI-adoption period, not as AI-caused flattening, absent a more explicit causal claim in the source.

### Claim 8: Big Tech employment has become more stable and tenured as zero-interest-rate-era mobility incentives have faded
- **Evidence**: The article's closing observation contrasting current Big Tech tenure patterns with the high-mobility hiring environment of the 2020–2022 period.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is offered as background context for why Big Tech's talent pool looks different from AI labs' in this piece, not as a claim about AI adoption specifically. It's useful as a caveat against over-attributing all of the article's hiring shifts to AI: some of the stability described is a macro-labor-market effect (end of the zero-rate hiring boom) independent of AI's arrival.

## Concrete Artifacts

None. This is a market-analysis newsletter piece built from cited third-party
datasets (Interviewing.io coaching-request data, job-title-posting analysis,
compensation-survey references) and prose interpretation; it contains no
code, configuration, workflow diagrams, or reproducible artifacts to extract.

## Cross-References

- **Corroborates**: `survey-pragmaticengineer-ai-tooling-2026` — same author
  (Orosz), different evidentiary layer. The February 2026 tooling survey
  shows individual engineers rapidly adopting AI tools (Claude Code tying
  Copilot at 46% usage within 8 months of launch); this June 2026 piece
  shows the labor market repricing around that adoption (AI-lab retention
  edge, AI-role compensation premium, AI-engineering job-opening growth).
  The two pieces describe the same underlying shift — AI moving from
  optional tool to structural factor — observed from two different vantage
  points (individual practice vs. market structure).
- **Extends**: `discussion-hn-agentic-coding-jobs` — that discussion-thread
  note's Claim 1 documents a single job posting (Zapier, March 2026)
  explicitly requiring "directing and reviewing agent-written code" as a
  baseline competency, framed there as "the earliest documented job-market
  artifact in our corpus that explicitly treats hand-written-code-first as
  insufficient." This article provides the aggregate-market-level
  counterpart to that single data point: AI-role job openings up ~60%
  year-over-year (Claim 3 in this note) and AI-role compensation exceeding
  generalist SE compensation (Claim 6), suggesting the Zapier posting was
  an early instance of a broader, now-quantifiable market shift rather than
  an isolated outlier.
- **Extends**: `blog-pragmaticengineer-hightower-infrastructure-ai` — same
  publication, adjacent time window (June 2026). The Hightower interview
  note captures one senior practitioner's framing of AI's impact on the
  *nature* of engineering work; this article provides the market-structure
  evidence for how that shift is showing up in hiring and compensation data
  at the same moment. Neither note's claims overlap directly, but both
  describe the same publication's coverage of the AI-adoption period from
  complementary angles (practitioner reflection vs. market data).
- **Novel**: The new-grad/intern hiring contraction (Claim 4, "one in 10
  down from nearly three in 10") and the AI-lab-vs-Big-Tech retention
  comparison (Claim 2, Anthropic 80% vs. OpenAI 67%) are not present
  anywhere else in the corpus. Prior sources address individual workflow
  and tool adoption; this is the first source with hiring-pipeline-level and
  retention-level market data. The "great flattening" management-ratio claim
  (Claim 7) is also novel to the corpus, though the article itself frames it
  as a pre-existing trend rather than a new AI-driven phenomenon.
- **Contradicts**: None identified. This article's claims operate at the
  labor-market level (hiring, retention, compensation, titles) and do not
  make claims about tool efficacy, code quality, or productivity that would
  conflict with the practice-focused sources already in the corpus
  (`paper-miller-speed-cost-quality`, `survey-pragmaticengineer-ai-tooling-2026`).

## Guide Impact

- **Chapter 05 (Team Adoption)**: The new-grad/intern hiring contraction
  (Claim 4) is the most actionable data point for this chapter. It should
  inform a section on staffing AI-native teams: the market data suggests
  most large companies are not betting on "hire junior engineers and let AI
  accelerate their ramp-up" as a primary strategy — they are hiring fewer,
  more selectively credentialed new grads while growing AI-specialist
  headcount ~60% YoY. A team-adoption playbook should distinguish between
  "using AI to make existing engineers more productive" (well-supported
  across the corpus) and "using AI to substitute for junior hiring" (not
  supported by this data — junior hiring is contracting independently of
  whether AI could theoretically compensate for it).
- **Chapter 05 (Team Adoption)**: The AI-lab retention/attractiveness data
  (Claims 1–2) is relevant to a "competing for talent" framing: teams and
  companies that are visibly serious about AI-native workflows (tooling
  investment, Claude Code adoption, clear technical narrative) may have a
  recruiting and retention advantage, mirroring what frontier labs are
  seeing at a larger scale. This should be presented as a plausible
  incentive for adoption, not as proven causation — the article does not
  isolate AI-native workflow appeal from other factors (valuation, funding,
  brand) driving Anthropic's specific numbers.
- **Chapter 05 (Team Adoption)**: The "great flattening" claim (Claim 7)
  should be used cautiously if at all. Because the source itself frames it
  as a continuing trend rather than a new AI-caused effect, the guide should
  not cite this as evidence that "AI adoption reduces the need for engineering
  managers" without a more direct causal source. Flag as a trend to watch,
  not a lever to pull.
- **Chapter 01 (Fundamentals)**: The frontend/mobile title-consolidation
  claim (Claim 5) could inform a caveat in any section discussing which
  roles benefit most from AI-native workflows — but the guide should adopt
  the article's own more precise framing (specialist titles consolidating at
  larger companies) rather than the simpler "frontend/mobile roles are
  disappearing" headline, which the source itself does not fully support.

## Extraction Notes

- The article is a paid Pragmatic Engineer newsletter post; the compensation-
  comparison section (underlying Claim 6) was not fully accessible during
  extraction — the Miner could see that the section exists and its stated
  headline conclusion but not the primary comparison figures or methodology
  behind them. Claim 6 confidence is downgraded to `anecdotal` for this
  reason and should be re-verified against a primary compensation source
  before being used to anchor a specific recommendation.
- This is Part 2 of a two-part series; Part 1 (published roughly two weeks
  earlier, per the article's own reference) covers general tech-jobs-market
  recruitment trends, Big Tech/public-company hiring, and AI-engineering
  demand, and was not separately available for extraction. If Part 1 is
  filed as its own source later, it should be cross-referenced here.
- No sub-pages were followed; the article does not link out to primary
  datasets (Interviewing.io's own report, job-title-analysis methodology)
  that would let the Miner verify the cited figures against source data
  directly. This is a limitation of the extraction, not a claim that the
  figures are wrong.
