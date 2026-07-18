---
source_url: https://cognition.com/blog/ai-productivity
source_type: blog-post
title: "Estimating the Productivity of an Autonomous AI Software Engineer"
author: The Cognition Team
date_published: 2026-06-04
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: emerging
issue: "#2000"
---

# Estimating the Productivity of an Autonomous AI Software Engineer

> Cognition's first-party writeup of a production-deployed statistical system for
> estimating how many "human-equivalent engineering hours" each Devin session is
> worth — an LLM-judge estimator trained and validated against 258 self-reported
> ground-truth sessions from 126 enterprise users, achieving r_log = 0.74, explicitly
> calibrated to underestimate, and directly benchmarked against two independent
> vendor studies (METR, Anthropic) doing the same kind of estimation.

## Source Context

- **Type**: blog-post (Cognition's own research/engineering blog, cognition.com,
  published 2026-06-04, byline "By The Cognition Team," no individual author named)
- **Author credibility**: Published directly by Cognition, the company that builds
  and sells Devin. This is a first-party vendor account with a commercial incentive
  to show Devin delivering value, but unlike most of this corpus's Cognition posts
  it is dense with falsifiable methodological detail: dataset size, held-out
  evaluation statistics (r_log, r_log², F-statistic, p-value, ICC), an explicit
  calibration equation, an ablation comparing three estimator variants, and a named
  "Threats to Validity" section that discloses self-report bias, sampling bias, and
  scope limitations against the vendor's own interest. It also directly benchmarks
  its own number against two named third-party studies (METR, Anthropic) rather than
  only against itself.
- **Scope**: Covers the design and validation of an automated system that estimates
  "productive engineering hours" per Devin session — metric selection rationale,
  ground-truth data collection, a classifier for filtering unproductive sessions,
  four design principles for the estimator agent, held-out evaluation statistics,
  log-space calibration, an ablation against simpler predictors (lines-changed only;
  agent-trace-only), a direct comparison to METR's and Anthropic's own LLM-based
  effort-estimation studies, and a "Threats to Validity" section. Does NOT cover:
  the specific model(s) used to build the estimator or to run Devin sessions, the
  actual prompt(s) given to the estimator agent, dollar-value conversion rates, the
  identity of the "eight deployments"/enterprise customers involved, or any
  controlled comparison against a non-Devin baseline (there is no "human engineer
  alone, no AI" condition — the comparison is Devin session vs. the same user's own
  self-reported estimate of how long they'd have taken).

## Extracted Claims

### Claim 1: Cognition built and is now running in production the first (to its knowledge) automated system for measuring AI engineering productivity, using an LLM agent that reviews each completed Devin session, classifies whether it produced useful output, and then estimates the human-equivalent hours it would have taken to produce the same output
- **Evidence**: Direct framing and methodology statement in the article's
  introduction, plus an explicit "first" claim.
- **Confidence**: emerging (first-party production-deployment claim; the "first...
  to our knowledge" framing is self-limiting and not independently verified, but the
  mechanism described — an LLM-judge agent scoring sessions — is concrete and
  falsifiable)
- **Quote**: "In our system, an agent reviews each completed Devin session — first classifying whether it produced useful output, then estimating how long a human engineer would have taken to produce the same work. We validated it by asking human engineers how long they would have spent on the same tasks. The system is now running with customers. To our knowledge, this is the first automated system measuring AI engineering productivity in production."
- **Our assessment**: The two-stage design (classify productive/not, then estimate
  hours only for productive sessions) is the article's core architectural claim and
  is corroborated by the more detailed mechanism descriptions in Claims 4-6 below.
  "First... to our knowledge" is an honest hedge rather than an absolute claim, and
  is consistent with the article's own "Comparison to Prior Work" section (Claim 11)
  naming two prior studies that do related but narrower estimation — those studies
  are described as effort-estimation research, not production-deployed measurement
  systems, so the "first production system" framing is plausible as stated.

### Claim 2: Cognition chose "productive engineering hours" as its metric after rejecting both dollar-value impact (too hard to attribute) and raw activity metrics like lines of code, commits, and tokens consumed (don't correspond to effort)
- **Evidence**: Direct metric-selection rationale under the "Choosing a Metric"
  heading, with a worked counterexample for why raw activity fails (a large
  mechanical refactor vs. a small but investigation-heavy bug fix).
- **Confidence**: emerging (first-party design rationale, internally consistent and
  argued from concrete counterexamples rather than asserted)
- **Quote**: "On the other end of the spectrum, we could measure raw activity: lines of code, commits, PRs, tokens consumed. These are easy to collect but don't correspond to effort. A mechanical refactor can touch thousands of lines in an afternoon; a two-line bug fix can represent hours of investigation. Many valuable tasks — triaging bugs, running analytics queries, reviewing code — produce no code at all. The middle ground we decided to measure is human engineering hours: how long would a human engineer have taken to produce the same output?"
- **Our assessment**: This is a specific, well-argued rejection of the exact vanity
  metrics (LOC, commits, PR counts) that `blog-faros-claude-code-roi.md` Claim 5
  independently flags as anti-patterns — see Cross-References. The additional point
  that "many valuable tasks... produce no code at all" is a useful, specific
  argument for why any measurement system anchored only on code-diff volume will
  systematically miss a category of real engineering work (triage, analytics,
  review).

### Claim 3: The dataset consists of 258 real production Devin sessions from 126 users across a diverse set of enterprise customers, collected via live interviews and a survey, with each session backed by a full execution trace (user request, every action taken, resulting code, codebase context)
- **Evidence**: Direct dataset description under "Collecting a Dataset."
- **Confidence**: emerging (specific, stated sample size and collection method;
  no breakdown of how many sessions came from interviews vs. survey, and no
  per-customer sample sizes disclosed)
- **Quote**: "Our dataset consists of 258 sessions from 126 users across a diverse set of enterprise customers. We collected the data via live interviews and a survey. Every Devin session has a full execution trace: the user's request, every action taken, the resulting code, codebase context."
- **Our assessment**: This is real production data, not a synthetic benchmark or a
  small internal pilot — 126 distinct users is a meaningfully larger and more
  organizationally diverse ground-truth panel than the comparable METR study cited
  later in the same article (7 METR technical staff; see Claim 11). The tradeoff,
  which the article's own "Threats to Validity" section acknowledges (Claim 12), is
  that ground truth is self-reported by users who knew they were talking to
  Cognition, not independently timed or audited.

### Claim 4: Sessions with an associated PR are filtered for productivity using a simple merged/not-merged rule (deliberately conservative — some closed-PR sessions may still have been productive); sessions without a PR use a separate classifier that discards roughly 1–20% of sessions depending on the customer
- **Evidence**: Direct description of the two filtering mechanisms under "Filtering
  for Useful Work," including named examples of retained non-PR productive work and
  named discard conditions.
- **Confidence**: emerging (first-party mechanism description with a stated
  numeric range; no absolute counts of sessions discarded, and no accuracy/precision
  figure for the non-PR classifier itself)
- **Quote**: "For sessions with a PR, this is relatively straightforward: if any PR from the session is merged, we include the estimate; if not, we discard it. This is slightly lossy... We built a classifier to filter out unproductive sessions, which removes around 1-20% of sessions, depending on the customer... We discard sessions where the agent lacked access to carry out the task, sessions where the agent asked for clarification and the user never replied, and other scenarios where Devin was unable to meaningfully advance the task."
- **Our assessment**: The merged-PR filter is a clean, verifiable proxy for the PR
  case, and the article is explicit that it is conservative (biased toward
  undercounting productive work), consistent with the article's overall calibration
  philosophy (Claim 8). The named non-PR discard reasons (no access, unanswered
  clarification request, agent stalled) are useful as a concrete taxonomy of
  "unproductive session" failure modes for any team building a similar filter,
  independent of Cognition's specific implementation.

### Claim 5: The estimator agent is built on four explicit design principles intended to keep it conservative: reason about the human's likely path rather than the agent's actual trajectory, credit only work the user did not already specify, account for codebase familiarity, and assume relevant expertise on the human's part
- **Evidence**: Direct enumeration of the four principles under "Building the
  Estimator," each with a worked example (discounting agent retries/detours;
  crediting bug triage time only if the user came without a proposed fix; crediting
  exploration time only when the session shows the user asking how the system
  works; not crediting cross-disciplinary reach a human reference engineer wouldn't
  have had).
- **Confidence**: emerging (first-party mechanism description with concrete worked
  examples for each principle; derived from a stated 25-session development set via
  manual triage, not from a separately validated ablation of each individual
  principle)
- **Quote**: "Reason about the human's path instead of the agent's. The agent's own trajectory is sometimes a poor proxy for human effort. Agents take detours, recover from environment and setup failures, and produce artifacts like summary reports that a solo engineer wouldn't." ... "Credit only the work the user did not specify." ... "Account for codebase familiarity." ... "Assume relevant expertise."
- **Our assessment**: These four principles are the article's most transferable
  methodological contribution — any team building an LLM-judge estimator for
  agent-vs-human effort (not just Cognition's specific use case) faces the same four
  failure modes: crediting the agent's inefficiencies as if they were unavoidable
  human effort, crediting work the user had already done themselves, ignoring that
  familiarity dominates task time, and inflating estimates by assuming the human
  reference lacks skills the actual engineer has. The "codebase familiarity" example
  is also a specific, mechanism-level explanation for why Cognition's other posts
  (see Cross-References → Corroborates) claim Devin's clearest advantage is
  unfamiliar/legacy codebases: it is baked directly into how this estimator credits
  time.

### Claim 6: On a held-out evaluation set of 233 sessions, the estimator achieves r_log = 0.74 and r_log² = 0.54 (statistically significant, F(1,231) = 279.9, p < 10⁻⁵), with about 50% of sessions falling within a factor of 2 of the true estimate, and individual 2–3× errors that are roughly unbiased and independent so that they cancel out as session count grows
- **Evidence**: Direct statistical results under "Evaluation," including the
  correlation coefficients, significance test, and an explicit noise-cancellation
  argument for why aggregate totals are more trustworthy than individual session
  estimates.
- **Confidence**: emerging (specific, held-out (not training-set) evaluation
  statistics with a significance test — meaningfully more rigorous disclosure than
  most vendor productivity claims in this corpus — but self-reported, internally
  computed, and not independently replicated or peer-reviewed)
- **Quote**: "On the held-out evaluation set of 233 sessions, our estimator has an r_log of 0.74 and r_log² of 0.54. The correlation is highly statistically significant (F(1,231) = 279.9, p < 10⁻⁵). Around 50% of sessions fall within a factor of 2 of the true estimate. Individual estimates are noisy — 2–3× errors in either direction are common — but because errors are roughly unbiased and independent, they cancel as session count grows and the aggregate converges toward the human-reported total."
- **Our assessment**: This is a meaningfully more rigorous evaluation disclosure
  than the typical vendor blog claim in this corpus — a held-out test set, a named
  correlation statistic, a significance test, and an explicit "individual estimates
  are noisy" caveat rather than presenting only the aggregate number. The framing
  that "errors cancel as session count grows" is the article's core argument for why
  this metric is usable for organizational-level ROI reporting even though any
  single session's estimate could be off by 2–3×; the guide should carry this caveat
  whenever citing an aggregate-hours figure derived from this kind of estimator —
  it is not meant to be trusted at the individual-session level.

### Claim 7: About half of the residual disagreement between the model and self-reported ground truth is attributable to variance between different users' estimation habits (ICC = 0.58) rather than variance within any one user's own sessions, and Cognition deliberately chose not to apply per-user calibration for simplicity
- **Evidence**: Direct statistical claim (intraclass correlation coefficient) plus
  an explicit design decision and its stated rationale.
- **Confidence**: emerging (specific named statistic with a clear methodological
  implication; the decision not to use per-user calibration is explicitly justified
  as a simplicity tradeoff, not claimed to be optimal)
- **Quote**: "A lot of the noise comes from variance between users, both in how they estimate and in genuine differences in speed. Roughly half the residual disagreement lies between users rather than within a user's own sessions (ICC=0.58). We considered per-user calibration, for example, prompting users in-product to give a few estimates for bootstrapping. We decided against it for simplicity and since, for our purpose of aggregation, estimating relative to an 'average' user is sufficient."
- **Our assessment**: This is a useful, specific caution for any team designing a
  similar self-reported ground-truth study: a large share of "estimator error" may
  actually be measurement noise in how different humans estimate their own
  counterfactual effort, not model error. It also implies the estimator's accuracy
  could plausibly improve with per-user calibration — a concrete, named direction
  for future work that Cognition explicitly chose not to pursue yet, worth flagging
  as unresolved rather than settled.

### Claim 8: The uncalibrated model consistently underestimated; Cognition corrected this with a log-space linear regression (h = 2.28 × m^0.923), then deliberately reported the resulting figure as a conservative underestimate rather than applying a further correction for the known bias that summing log-unbiased predictions in linear space still understates the true total
- **Evidence**: Direct calibration equation and a worked numerical example (a
  2-hour prediction implies an expected true value of 2.5 hours, 25% above the
  prediction, due to Jensen's-inequality-style asymmetry between log-space and
  linear-space aggregation) explaining why totals remain conservative even after
  calibration.
- **Confidence**: emerging (specific equation and worked derivation disclosed;
  this is unusually transparent quantitative detail for a vendor blog, though the
  underlying raw data is not published for independent verification)
- **Quote**: "Our initial, uncalibrated model consistently underestimated. To correct this, we fit a linear regression in log-space: h = 2.28 × m^0.923... Even after this correction, the total of the human estimates remains 1.4× the total of the corrected model estimates. This gap is expected: an estimator that is unbiased in log-space becomes biased once its predictions are summed in linear space, systematically underestimating the total... Rather than apply a further correction for this, we report the unadjusted figure as a deliberately conservative underestimate."
- **Our assessment**: This is a specific, checkable statistical point (log-space
  unbiasedness does not imply linear-space-sum unbiasedness) presented with a
  worked toy example, and the explicit choice to leave the reported figure
  conservative (rather than correct it upward to match the human-reported total) is
  a credibility-supporting decision — a vendor motivated purely by favorable
  marketing numbers would have made the opposite choice. Any guide citation of a
  Devin-hours total derived from this system should note it is likely a
  deliberate *underestimate* of the true figure, per the source's own framing.

### Claim 9: A simpler predictor using only total lines changed (additions + deletions) performed poorly (R_log² = 0.27), and a predictor using only the agent's own edit-tool trace (no user messages or other session context) performed better but still lagged the full estimator — evidence that effort signal lives outside the code diff
- **Evidence**: Direct ablation comparison of three estimator variants (lines-only,
  agent-trace-only, full context), stated as a deliberate test of "how much of the
  signal comes from the final code change versus the full Devin session."
- **Confidence**: emerging (specific ablation with a named metric for the weakest
  variant; the middle variant's exact R_log² is not given in the article, only
  described qualitatively as "better... but still lagged")
- **Quote**: "The first regresses a single scalar, the total lines changed (additions + deletions summed across all PRs in the session), against our human estimates. It performed poorly, with an R²_log of 0.27, confirming that code volume is a weak proxy for engineering effort. We then evaluated an estimator agent given only the trace of the agent's edit tool calls as context, with no user messages or other session activity. It performed better, but still lagged the full estimator, suggesting that important signal lives outside the diff."
- **Our assessment**: This ablation is direct, quantified evidence against using
  code-diff size as an effort proxy — R_log² = 0.27 is a specific, low number, not
  just an assertion that "LOC is a bad metric." The three-tier comparison (diff
  size alone → agent trace alone → full session context) is a clean methodological
  pattern any team could reuse to test how much of their own effort-estimation
  signal is actually visible in code artifacts versus requiring the full
  user-request-and-process context.

### Claim 10: The regression subset for the lines-changed ablation covers only 129 of the 233 held-out sessions (those with available diff-statistics data), even though 170 sessions in that set produced a PR, because Cognition's git-hosting integrations for some customers do not capture diff statistics
- **Evidence**: Direct disclosure of a data-availability limitation specific to the
  ablation analysis, given immediately after the ablation results.
- **Confidence**: settled (a stated data-completeness fact about the analysis
  itself, disclosed against the vendor's interest in appearing to have complete
  data)
- **Quote**: "The regression results below are for the 129 sessions in our evaluation dataset for which we have line-count data (the number of lines added and deleted across the session's pull requests). A total of 170 sessions in our evaluation dataset created PRs, but our integrations with some of our customer's git hosting platforms do not capture diff statistics."
- **Our assessment**: This is a small but important piece of methodological
  transparency — it explains a specific gap between the full held-out set (233),
  the PR-producing subset (170), and the subset used for the lines-changed ablation
  specifically (129), rather than leaving readers to assume the ablation ran on the
  full evaluation set. Worth citing as an example of the kind of instrumentation
  gap (diff stats not captured across all customer integrations) that any team
  building similar analytics on top of third-party git-hosting integrations should
  expect to hit.

### Claim 11: Cognition directly benchmarks its r_log = 0.74 against two named prior studies — METR's 2026 estimator (GPT-4o/GPT-5 on compressed Claude Code transcripts from 7 METR staff, 34 sessions, r_log = 0.83) and Anthropic's 2026 study (Claude estimating duration from only the title/description of 1,000 open-source Jira tickets, r_log = 0.46, versus human estimators on the same tickets at r_log = 0.67) — and attributes its lower correlation than METR's, and higher correlation than Anthropic's, to differences in data diversity and granularity
- **Evidence**: Direct comparison section ("Comparison to Prior Work") naming both
  studies, their sample sizes, and their reported statistics, with an explicit
  causal attribution for each direction of difference.
- **Confidence**: emerging (specific, named comparison with sample sizes and
  statistics for both cited studies; Cognition's causal explanations for the
  differences — "more diverse users" for METR, "far more granular data per session"
  for Anthropic — are plausible but not independently tested against alternative
  explanations, e.g. model-quality differences or task-domain differences)
- **Quote**: "METR (2026) used a combination of GPT-4o and GPT-5 to estimate the human-equivalent times from compressed Claude Code transcripts. These transcripts were collected from 7 METR technical staff. On 34 sessions labeled on human ground truth, their estimator had an r_log of 0.83. Our r_log is lower likely due to our data being collected from a much more diverse set of users. Anthropic (2026) estimated task duration on 1,000 open-source Jira tickets using Claude, but the estimator only had the ticket title and description to work with. They had an r_log of 0.46; human developers estimating the same tickets reached r_log = 0.67. Our system establishes stronger correlation than Anthropic's (r_log = 0.74 vs 0.46) because we have far more granular data per session."
- **Our assessment**: This is the most valuable single passage in the article for
  the guide's measurement chapter: it places three independent organizations'
  human-equivalent-time estimation results side by side (METR r_log=0.83 on 34
  small-panel sessions; Anthropic r_log=0.46 on 1,000 tickets with minimal context,
  versus human estimators at r_log=0.67 on the same tickets; Cognition r_log=0.74
  on 233 held-out production sessions with full execution traces). The pattern
  across all three — richer session context correlates with higher estimator
  accuracy, and minimal-context estimation (Anthropic's title+description-only
  case) underperforms even human estimators on the same limited information — is a
  genuinely novel, cross-vendor data point for this corpus's measurement-methodology
  material. Neither the METR nor the Anthropic study currently has its own source
  note in this corpus (verified via search — see Extraction Notes), so this article
  is currently the only place in the corpus these two figures appear; a stronger
  version of this claim would come from mining METR's and Anthropic's original
  publications directly.

### Claim 12: The article's own "Threats to Validity" section names four specific limitations against its own favorable framing: ground truth is self-reported by users aware they're speaking with Cognition, voluntary respondents may skew toward more engaged users, hours measure engineering capacity deployed rather than business value, and hours do not capture output quality or defects introduced
- **Evidence**: Direct, explicitly labeled limitations section with four named
  sub-points, each with a short explanation.
- **Confidence**: settled (first-party admission of specific, unresolved
  measurement limitations — disclosed against the vendor's own promotional
  interest, which is inherently more credible than an unqualified capability claim)
- **Quote**: "Ground truth bias. Our ground truth is self-reported. In our video user interviews, users were aware they were talking to Cognition, which might bias them." ... "Hours are not business value. We measure engineering capacity, not whether that capacity was deployed on high-value work. One hour spent fixing a critical production bug has very different business value than one hour spent on a project that eventually gets canceled." ... "Hours don't account for quality. If the agent introduces a subtle bug that takes a long time to debug and fix, its uplift on that task is negative. The merged-PR filter removes the clearest failures but not defects discovered after merging."
- **Our assessment**: This is a directly usable checklist of caveats for the guide
  whenever citing any "AI agent saved N human-equivalent hours" figure from this or
  a similar system: (1) self-reported ground truth carries interviewer-effect bias,
  (2) voluntary-response sampling likely skews toward more satisfied/engaged users,
  (3) hours-saved is capacity deployed, not proven business value, and (4) hours
  figures say nothing about whether the delivered work introduced defects that
  surface later. This directly corroborates and sharpens `blog-faros-claude-code-roi.md`
  Claim 5's warning against vanity metrics — see Cross-References.

### Claim 13: The overall conclusion figure — validated against 126 users across eight deployments, r_log = 0.74 on held-out sessions, calibrated to underestimate, currently in production use with Devin customers — is the article's summary headline result
- **Evidence**: Direct closing/conclusion paragraph restating the key figures.
- **Confidence**: emerging (restates figures already independently sourced in
  Claims 1, 3, and 6; adds the "eight deployments" detail not stated elsewhere in
  the article)
- **Quote**: "We presented a system for estimating the engineering output delivered by an autonomous coding agent, measured in equivalent human engineering hours. Validated against 126 users across eight deployments, the estimator has an r_log of 0.74 on held-out sessions. Individual estimates are noisy but approximately unbiased; aggregated across a deployment, errors cancel and the total converges toward what engineers report. The system is calibrated to underestimate rather than overestimate delivered output. It is currently in use with Devin customers."
- **Our assessment**: "Eight deployments" is a new detail not given earlier in the
  article (the "Collecting a Dataset" section names only "a diverse set of
  enterprise customers" without a count) — it should be read as the number of
  distinct customer deployments the 126 users and 258 sessions were drawn from,
  giving roughly 16 users per deployment on average. This is useful context for
  judging how much any single deployment could dominate the aggregate statistics,
  though the article gives no per-deployment breakdown to check for that directly.

## Concrete Artifacts

```
Article section structure (headings, in order):
1. (intro, unheaded)
2. Choosing a Metric
3. Collecting a Dataset
4. Filtering for Useful Work
5. Building the Estimator
6. Evaluation
7. Comparison to Prior Work
8. Threats to Validity
9. Conclusion
Source: cognition.com/blog/ai-productivity, "By The Cognition Team," 06.04.26
```

```
The four estimator design principles, verbatim (from "Building the Estimator"):

1. "Reason about the human's path instead of the agent's."
2. "Credit only the work the user did not specify."
3. "Account for codebase familiarity."
4. "Assume relevant expertise."

Source: cognition.com/blog/ai-productivity, "Building the Estimator" section
```

```
Key statistics, verbatim/transcribed (LaTeX in source rendered here as plain text):

- Ground-truth dataset: 258 sessions, 126 users, diverse enterprise customers
- Held-out evaluation set: 233 sessions
- r_log = 0.74, r_log^2 = 0.54
- Significance: F(1, 231) = 279.9, p < 10^-5
- ~50% of sessions within a factor of 2 of the true estimate
- Individual errors: 2-3x common, roughly unbiased and independent
- Between-user share of residual variance: ICC = 0.58
- Calibration equation (log-space linear regression): h = 2.28 x m^0.923
- Alternate constrained calibration: single multiplicative constant of 2.08
  (changes every metric by at most 0.01 vs. the regression fit)
- Post-calibration gap: human-reported total remains 1.4x the corrected model total
- Non-PR productive-session classifier: removes ~1-20% of sessions, customer-dependent
- Ablation: lines-changed-only predictor, R^2_log = 0.27 (129 of 233 sessions had
  diff-stat data available; 170 of 233 produced a PR)
- Conclusion figure: validated against 126 users across 8 deployments

Comparison studies cited by this article:
- METR (2026): GPT-4o + GPT-5 estimating human-equivalent time from compressed
  Claude Code transcripts, 7 METR technical staff, 34 sessions, r_log = 0.83
- Anthropic (2026): Claude estimating task duration from title+description only,
  1,000 open-source Jira tickets, r_log = 0.46 (model) vs. r_log = 0.67 (human
  estimators on the same tickets)

Source: cognition.com/blog/ai-productivity, "Evaluation" and "Comparison to Prior
Work" sections
```

## Cross-References

- **Corroborates**:
  - `blog-cognition-verifying-agentic-development.md` Claim 3 ("engineers running
    10 to 20 Devins in parallel, each with its own dev server") and its broader
    theme that Devin sessions are increasingly triggered asynchronously without a
    human watching live — this source's entire premise (Claim 1: an automated
    system is needed because "it's essentially impossible to measure value over
    thousands of sessions & billions of tokens") is the measurement-side
    consequence of that same async-scale shift; together the two sources describe
    complementary halves of the same underlying problem (verifying individual
    session correctness at scale vs. measuring aggregate productivity at scale).
  - `blog-faros-claude-code-roi.md` Claim 5 (vanity metrics to avoid: lines of
    code, raw PR counts, autocomplete acceptance percentages) — this source's
    Claim 2 independently arrives at the same rejection of code-volume metrics
    ("lines of code, commits, PRs, tokens consumed... don't correspond to
    effort"), and Claim 9's ablation result (R_log² = 0.27 for a lines-changed-only
    predictor) supplies the first quantified evidence in this corpus for exactly
    the qualitative warning Faros gives — two independent organizations (an AI
    coding-agent vendor and a developer-productivity-analytics vendor) converge on
    "code volume is a weak/misleading effort proxy," one qualitatively and one now
    with a specific statistic.
  - `blog-cognition-devin-in-windsurf.md` Claim 5 ("tasks in unfamiliar or legacy
    codebases that would cost a developer a day of ramp-up are often delivered
    quickly" — cited there as one of "Devin's clearest advantages") — this source's
    Claim 5 (the "account for codebase familiarity" design principle) supplies the
    underlying measurement mechanism for that claim: the estimator explicitly
    credits more hours when a session shows the user asking how unfamiliar parts of
    the system work, which is the concrete implementation detail behind the more
    general marketing claim in the other source.

- **Contradicts**: None filed. This source's own internally-disclosed limitations
  (Claim 12) are consistent with, not in tension with, the rest of this corpus's
  general skepticism toward vendor-reported productivity figures (e.g. the
  productivity-paradox framing in `blog-faros-claude-code-roi.md`) — no existing
  source note was found making an opposing quantitative claim about Devin's
  measured productivity specifically, so there is no same-claim conflict to file
  per MINER.md §4a.

- **Extends**: `blog-faros-claude-code-roi.md`, which supplies a team-level cohort
  measurement methodology (control vs. treatment teams, PR merge/review-time
  deltas) for a different AI coding tool (Claude Code) and a different vendor
  (Faros, a third-party analytics platform rather than the agent vendor itself).
  This source extends that corpus coverage with a session-level, LLM-judge-based
  estimation methodology from the agent vendor's own internal telemetry, applied to
  an autonomous agent (Devin) rather than an IDE-assistant-style tool — together the
  two sources give the guide two structurally different measurement approaches
  (external team-cohort analytics vs. internal per-session LLM-judge estimation)
  for the same underlying problem of quantifying AI coding-tool productivity.

- **Novel**: The entire LLM-judge session-estimation methodology (four design
  principles, log-space calibration equation, ICC-based variance decomposition, and
  the lines-only/trace-only/full-context ablation) is new to this corpus — no
  existing source note documents an agent vendor's internal quantitative
  measurement architecture at this level of statistical detail. The direct,
  named three-way comparison to METR's and Anthropic's own 2026 effort-estimation
  studies (Claim 11) is also new; neither study currently has its own source note
  in this corpus (verified by search — see Extraction Notes), so this is currently
  the corpus's only record of those two studies' reported r_log figures.

## Guide Impact

- **Chapter 05 (Team Adoption), section on measuring impact**: Add this source's
  metric-selection rationale (Claim 2: reject dollar-impact as unattributable,
  reject raw activity as effort-decoupled, land on human-equivalent hours as the
  measurable middle ground) alongside the existing Faros framework
  (`blog-faros-claude-code-roi.md`). Where Faros recommends team-level cohort
  comparison as the measurement design, this source shows a complementary
  session-level estimation design — the guide should present both as valid
  approaches operating at different granularities (team-aggregate vs.
  per-session), not as competing methodologies.

- **Chapter 05 (Team Adoption)**: Add Claim 12's four-item "Threats to Validity"
  checklist (self-report bias, voluntary-sampling bias, hours ≠ business value,
  hours don't capture quality/defects) as a standing caveat block for the guide to
  attach whenever it cites any "AI saved N human-equivalent hours" style figure —
  from this source or any other vendor. This is a more specific, source-grounded
  version of the general skepticism the guide should already carry toward
  self-reported productivity metrics.

- **Chapter 05 (Team Adoption)**: Add Claim 6's aggregation caveat explicitly:
  individual-session estimates from an LLM-judge system can be off by 2-3x, and
  are only trustworthy in aggregate ("errors cancel as session count grows"). If
  the guide recommends teams build or adopt similar per-session estimation
  tooling, it should state clearly that single-session numbers should never be
  used to evaluate an individual task or engineer — only aggregate totals over
  enough sessions for the noise to average out.

- **Chapter 05 (Team Adoption)**: Add Claim 9's ablation finding (R_log² = 0.27
  for a lines-changed-only predictor vs. the full estimator) as a concrete,
  quantified data point reinforcing the guide's existing warning against
  lines-of-code-style metrics, upgrading that warning from qualitative
  (Faros) to quantitatively demonstrated (this source).

## Extraction Notes

- The source is a JavaScript-rendered (Next.js) page; a first WebFetch pass
  returned only a condensed paraphrase, consistent with the verbatim-extraction
  difficulty already documented in other Cognition source notes in this corpus
  (e.g. `blog-cognition-devin-in-windsurf.md`, `blog-cognition-verifying-agentic-
  development.md` Extraction Notes). To obtain and verify verbatim text, the raw
  HTML was fetched directly via `curl` with a browser user-agent, stripped of
  script/style tags and HTML markup with a small Python script, and every quote
  used above was located and confirmed character-for-character in that stripped
  text before being copied into this note (per MINER.md §2a). Statistics rendered
  as MathJax/KaTeX in the live page (e.g. r_log, r_log²) appear in the raw HTML
  as duplicated text nodes and `annotation encoding="application/x-tex"` elements
  containing the original LaTeX source (confirmed as `r_{log}`, `r_{log}^2`,
  etc.); this note transcribes those as plain-text `r_log` / `r_log^2` for
  readability, consistent with how the visually-rendered page displays them, not
  as a paraphrase of different underlying content.
- No sub-pages were followed. The article does not link out to other substantive
  Cognition posts (its outbound links are to the site's article-list footer and
  standard nav/legal pages), so no additional pages met the MINER.md §1 "follow up
  to 5 linked pages that seem substantive" criterion.
- Publish date (2026-06-04) and author byline ("By The Cognition Team") were
  confirmed both from the visible page text and from the `article:published_time`
  meta tag in the raw HTML.
- Searched this corpus specifically for existing source notes on the two studies
  this article cites (METR's Claude Code transcript study; Anthropic's Jira-ticket
  duration-estimation study) before writing Claim 11 and the Novel section above.
  No source note dedicated to either study was found — the "metr" substring
  matches in a corpus-wide grep are all incidental matches inside the word
  "metric," and no file discusses a 34-session or 1,000-Jira-ticket estimation
  study. This is worth flagging to the Prospector as a possible future mining
  target: both studies, if publicly published, would likely be valuable
  independent sources for this corpus's measurement-methodology material.
- Cross-references verified before writing: re-read `blog-faros-claude-code-roi.md`
  in full and confirmed Claim 5 by number and content; re-read
  `blog-cognition-verifying-agentic-development.md` in full and confirmed Claim 3
  by number and content; re-read `blog-cognition-devin-in-windsurf.md` in full and
  confirmed Claim 5 by number and content. No claim number was guessed or
  approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified — see
  Cross-References → Contradicts. No contradiction issue filed.
- Confidence is rated `emerging` overall: the source discloses unusually rigorous
  statistical detail (held-out evaluation, significance testing, an ablation, and
  an explicit limitations section) for a vendor blog post, which is why it is not
  rated `anecdotal`; it is not rated `settled` because the underlying raw data is
  not published for independent replication, ground truth is self-reported by a
  population aware they were speaking with the vendor, and the "first automated
  system... to our knowledge" framing is explicitly self-limiting rather than
  independently verified.
