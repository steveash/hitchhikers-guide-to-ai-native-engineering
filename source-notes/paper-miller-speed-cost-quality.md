---
source_url: https://arxiv.org/abs/2511.04427
source_type: paper
title: "Speed at the Cost of Quality: How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects"
author: Hao He, Courtney Miller, Shyam Agarwal, Christian Kästner, Bogdan Vasilescu (Carnegie Mellon University)
date_published: 2025-11-06
date_extracted: 2026-04-08
last_checked: 2026-04-08
status: current
confidence_overall: settled
issue: "hi-e93.4 — Ch 05 Team Adoption discovery"
---

# Speed at the Cost of Quality (Miller et al., MSR '26)

> The first large-scale, peer-reviewed difference-in-differences study of Cursor adoption in open-source projects (n=806 adopting + 1,380 matched controls). Finds a 281% velocity spike in month 1 that decays to zero by month 3, alongside a *persistent* 41.6% increase in cognitive complexity and a 30.3% increase in static analysis warnings. Presented at MSR '26 (April 2026, Rio de Janeiro). Provides the strongest available counter-evidence to the "AI tools obviously make teams faster" framing.

## Source Context

- **Type**: paper (peer-reviewed, MSR '26 — the top venue for mining-software-repositories research)
- **Author credibility**: Carnegie Mellon University. Bogdan Vasilescu and Christian Kästner are senior authors with extensive publication records in empirical software engineering (mining repositories, developer behavior, OSS sustainability). Courtney Miller is a CMU PhD student with prior MSR/ICSE publications. This is the most credible single source on Cursor adoption outcomes published to date — the methodology is the kind of difference-in-differences design that has been applied to open-source-project-effects research for over a decade by this group.
- **Scope**: GitHub repositories that adopted Cursor (detected by committed `.cursor/` configuration files) vs. matched controls. Languages: JavaScript, TypeScript, Python. Time window: January 2024 to August 2025. Outcome metrics: lines of code added, cognitive complexity, static analysis warnings (reliability, maintainability, security). Does NOT measure: pull-request review time, developer self-reported satisfaction, individual-level productivity, or non-OSS proprietary codebases.

## Methodology

### Sample
- **806 Cursor-adopting repositories** (detected by committed `.cursor/` configs)
- **1,380 matched control repositories** (1:3 matching ratio that never adopted Cursor)
- **Time window**: January 2024 to August 2025 (most adoptions Aug 2024 – Mar 2025)
- **Languages**: JavaScript, TypeScript, Python
- **Matching**: propensity score matching via logistic regression on repository age, six months of recent dynamics, historical baselines, stars, forks, PRs, issues, events. Language-specific matching applied. Achieved AUC 0.83–0.91.

### Design
- Difference-in-differences (DiD) comparing pre/post adoption trajectories of treated vs. control repositories
- This is a quasi-experimental design that controls for observable confounders and time-invariant repository characteristics

### Limitations explicitly acknowledged
- Only observable adoptions detected (committed config files); silent users invisible
- Unknown usage intensity per repository
- Unobserved confounders (developer expertise, team culture) cannot be tested
- Generalization limited to JavaScript, TypeScript, Python OSS contexts

## Extracted Claims

### Claim 1: Cursor adoption causes a 281.3% increase in lines added in month 1, 48.4% in month 2, then disappears
- **Evidence**: DiD estimates over the 6-month post-adoption window, n=806 adopters + 1,380 controls.
- **Confidence**: settled (peer-reviewed, large sample, matched controls)
- **Quote**: "Cursor adoption leads to a statistically significant, large, but transient increase in project-level development velocity."
- **Our assessment**: This is the central empirical finding and it cuts both ways. The 281% spike is real and large, validating that Cursor *does* let people produce more code in the first month. The decay to zero by month 3 is the inconvenient finding that vendor productivity narratives systematically omit. For the chapter's "Measuring impact" section: any measurement window shorter than 3 months will overstate Cursor's impact; any measurement window of 3+ months will catch the decay. Recommend the chapter explicitly require a 6-month measurement window, not a 30-day window, for any team adoption ROI calculation.

### Claim 2: Cognitive complexity increases by 41.6% post-adoption, persistently
- **Evidence**: DiD estimate on cognitive complexity metrics across 806 treated repositories.
- **Confidence**: settled
- **Quote**: "a substantial and persistent increase in static analysis warnings and code complexity"
- **Our assessment**: Cognitive complexity is a measurable, language-agnostic proxy for "how hard is this code to read." A 41.6% increase that persists across the post-adoption window is the most direct evidence that Cursor adoption produces code that is harder to maintain, not just more code. The persistence (no decay) means this isn't a learning-curve artifact — the new normal includes more complex code. For the chapter's "Code review when AI wrote it" section: this number is the empirical case for why review practices need to change. AI-generated code is, on average, 41.6% harder to read than the same team's pre-adoption baseline.

### Claim 3: Static analysis warnings (reliability, maintainability, security) increase by 30.3% post-adoption, persistently
- **Evidence**: DiD estimate on aggregated static analysis warnings across treated repositories.
- **Confidence**: settled
- **Quote**: N/A (statistic stated directly)
- **Our assessment**: Static analysis warnings are a noisy metric — they include false positives, churn from rule updates, and category-specific issues. But a 30.3% increase that survives matching and DiD is large enough to overcome measurement noise. The composition (reliability + maintainability + security) is the right grouping: these are the three categories that map to user-facing failure modes. A 30% increase in static analysis warnings does not mean "30% more bugs in production" — it means "30% more places that look like bugs to a linter." The honest framing for the chapter: if your team adopted Cursor and your static analysis warnings did not go up, you are an outlier and should investigate.

### Claim 4: Velocity gains last only ~2 months, then disappear entirely
- **Evidence**: Time-series analysis of treatment effect across post-adoption months.
- **Confidence**: settled
- **Quote**: "Effects dissipate; no significant velocity gains observed" by months 3-6
- **Our assessment**: This is the single most important finding for the team-adoption chapter and the one most likely to be uncomfortable for vendors. The DiD design rules out the obvious "people stopped using Cursor" explanation — the treated group still has the config file. The most likely mechanism (per the paper) is that quality degradation creates a long-tail of complexity-driven slowdowns that wash out the early productivity gains. For the chapter: this is the empirical evidence that "AI productivity is real but transient if you don't pair it with quality gates." The recommendation: a team rolling out AI tools must invest in quality automation *before* the velocity gains decay, not after.

### Claim 5: Quality assurance is the major bottleneck for sustained AI productivity benefit
- **Evidence**: Authors' synthesis of velocity-decay + persistent-quality-degradation findings.
- **Confidence**: emerging (this is interpretation, not direct measurement)
- **Quote**: "quality assurance as a major bottleneck for early Cursor adopters"
- **Our assessment**: The authors explicitly call for quality assurance to be "a first-class citizen in the design of agentic AI coding tools and AI-driven workflows." This is the strongest peer-reviewed support we have for the chapter's existing thesis that verification deserves top billing in adoption playbooks. For the "Verification before autonomy" section: cite this as the empirical case that you cannot defer verification investment until after you see productivity gains — by then, the gains are already gone.

### Claim 6: The mechanism is velocity → codebase size → technical debt, not Cursor introducing more bugs per line
- **Evidence**: Causal path analysis comparing AI-adopting projects to non-adopting projects with similar velocity.
- **Confidence**: emerging
- **Quote**: N/A (paraphrased: "LLM agent assistants amplify existing velocity-quality dynamics by enabling faster code production, but may not necessarily introduce more code quality issues than non-adopting projects moving with the same velocity.")
- **Our assessment**: This is a critical nuance. Cursor is not making the average line of code worse — it is letting teams produce more lines of code, and the existing velocity-quality dynamics of the project then play out at a larger scale. The implication for team adoption is that AI tools are a *velocity multiplier on existing dynamics*, not a quality changer. A team with strong existing quality practices (code review, CI, linting, type checking) will see quality hold up; a team with weak practices will see quality degrade in proportion to how much faster they ship. The "fix the process, then add the AI" framing from other practitioner reports is empirically supported by this finding. Recommend leading the chapter with this framing: if your team's quality bar is fragile, AI adoption will expose it. If your quality bar is strong, AI adoption will scale it.

## Notable Strengths

### Methodological strengths

1. **Difference-in-differences with matched controls** is the strongest causal-inference design available without a randomized trial. The 1:3 control ratio and language-specific matching are best practices.
2. **Pre-registered detection mechanism** (committed `.cursor/` configs) avoids retrospective adoption-date inference.
3. **Multiple outcome metrics** (velocity + complexity + static analysis) reduces single-metric gaming.
4. **AUC 0.83–0.91 on the propensity model** indicates strong matching quality.
5. **Limitations explicitly acknowledged** by the authors — they call out the language scope, the silent-user blind spot, and the unobserved-confounders gap.

### Why the conclusions are robust

The DiD design controls for time-invariant project characteristics (codebase size, language, team culture). The match controls for observable repository state at the moment of adoption. The remaining confounders would have to be (a) time-varying, (b) coincident with Cursor adoption, and (c) plausibly causing the velocity-then-decay pattern. No obvious candidate exists.

## Notable Limitations

1. **OSS only**: Open-source contributors may have different velocity-quality tradeoffs than enterprise teams. Enterprise teams with code review gates may not experience the velocity spike at all (because review capacity caps it). Generalization to corporate teams should be flagged.
2. **Three languages only**: JavaScript, TypeScript, Python. Cursor's behavior on Rust, Go, C++, Java, etc. is untested. The complexity metric for cognitive complexity is well-defined for these languages but may behave differently for, e.g., systems languages.
3. **Adoption signal is binary**: Detecting `.cursor/` configs tells you a project uses Cursor, not how many contributors use it or how often. A high-intensity small-team project and a low-intensity large-team project look identical to the matching.
4. **No individual-level data**: All effects are project-level. Individual developer outcomes (skill change, workflow change) are invisible.
5. **No code review time data**: This is a major gap. The Faros productivity-paradox report finds a 91% increase in PR review time, which would explain part of the velocity decay. Miller et al. cannot test this directly.

## Cross-References

- **Reinforces** the Faros productivity-paradox finding that individual velocity gains do not translate to organizational outcomes. Miller et al. provide the *mechanism* (quality degradation) that Faros only describes.
- **Reinforces** the Sentry profile's heavy investment in production-bug-pattern detection (`sentry-backend-bugs` skill, 638 real production issues). If Cursor adoption is producing 30% more static analysis warnings on average, the Sentry-style investment in production-grounded review skills is the only practical defense.
- **Tension with** the Anthropic transformation report, which reports doubling autonomy and 60% AI work share without obvious quality decay. The most likely reconciliation: Anthropic has unusually strong existing quality gates (small teams, fast deploys, internal-release loop) that absorb the velocity-quality dynamic. Anthropic's experience may not generalize.
- **Tension with** the Pragmatic Engineer survey's optimistic adoption sentiment. Both can be true: practitioners are enthusiastic and the code is getting more complex. Sentiment is not a quality metric.
- **Complements** the Bessemer Shopify piece's reversion-rate-tracking practice. Miller et al. provide the empirical justification for *why* a team like Shopify needs to track quality metrics from day one.

## Guide Impact

### Chapter 05: Team Adoption

- **Section "Start with the harness"**: Use Claim 6 to argue that the harness must include quality automation, not just productivity tooling. A CLAUDE.md without lint/test/typecheck commands is a CLAUDE.md that will let your team's complexity metric drift up by 41.6%.
- **Section "Verification before autonomy"**: Lead the section's empirical case with Claim 5 verbatim ("quality assurance as a major bottleneck for early Cursor adopters"). This is peer-reviewed evidence that the verification investment cannot be deferred.
- **Section "Code review when AI wrote it"**: Use Claim 2 (41.6% complexity increase) and Claim 3 (30.3% static analysis warnings) as the empirical case for why review practices must change. AI-generated code is measurably harder to review.
- **Section "Measuring impact"**: Use Claim 1 (281% → 48% → 0% velocity decay) as the empirical case for a 6-month minimum measurement window. Any 30-day pilot will overstate the gain.
- **Section "Common objections"**: Use Claim 4 (velocity gains disappear by month 3) to validate the "AI productivity is overhyped" objection. The honest answer is "yes, the early gains are not durable without quality investment, and this is the empirical reason."

### Chapter 03: Safety and Verification

- The 41.6% complexity increase and 30.3% static analysis warning increase are direct empirical support for the chapter's existing position that automated quality gates are non-negotiable.

### Chapter 02: Harness Engineering

- The decay finding strengthens our existing recommendation that the harness should include explicit lint, format, typecheck, and test commands — these become the only durable productivity gain after the velocity spike fades.

## Extraction Notes

1. **Two paper versions exist**: arXiv v1 (Nov 6, 2025) and v3 (Jan 26, 2026). The v3 is the MSR '26 camera-ready and is the version cited here. The findings are consistent across versions; v3 has refined statistics and a tightened scope.
2. **Methodology depth**: The full methodology is in the paper's Section 3. Key numbers (n=806, 1:3 matching, AUC 0.83–0.91) verified from the HTML version on arxiv.org.
3. **Available CMU summary**: A CS.CMU.edu news piece ("The Hidden Cost of AI Speed") provides a plain-language summary at https://www.cs.cmu.edu/news/2026/hidden-cost-ai-speed and is suitable for citing in the chapter as a secondary source if the arXiv paper is too dense.
4. **PDF available**: https://arxiv.org/pdf/2511.04427 — full paper with all figures and tables.
5. **MSR '26 conference**: April 13–14, 2026, Rio de Janeiro, Brazil. The MSR proceedings will be published in the IEEE/ACM conference proceedings; current arXiv version is the camera-ready.
6. **No raw data release noted in summary**: The paper may publish replication data; check the GitHub for eth-sri or CMU Strategic Software Engineering lab for replication packages.
7. **Confidence is "settled"**: This is one of only two settled-confidence sources in our corpus (the other is the Gloaguen et al. AGENTS.md paper). Use with high weight.
