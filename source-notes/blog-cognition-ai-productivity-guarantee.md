---
source_url: https://cognition.com/blog/ai-guarantee
source_type: blog-post
title: "AI should earn its keep: Introducing the AI Productivity Guarantee"
author: Scott Wu (Cognition)
date_published: 2026-06-04
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: emerging
issue: "#2001"
---

# AI should earn its keep: Introducing the AI Productivity Guarantee

> Cognition's announcement of a financial guarantee (up to $10M in credits)
> backing Devin's delivered engineering value, paired with a companion
> technical post disclosing the estimator methodology behind it in unusual
> detail — dataset size, design principles, held-out evaluation correlation
> (r_log = 0.74), a log-space calibration formula, disclosed threats to
> validity, and a direct numeric comparison to two independent
> effort-estimation studies (METR, Anthropic).

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  2026-06-04; byline "By Scott Wu" — Cognition's co-founder/CEO). A second,
  directly linked companion post — "Estimating the Productivity of an
  Autonomous AI Software Engineer," byline "By The Cognition Team," same
  publish date (06.04.26), reached via the primary article's "technical
  details of our methodology" link (`cognition.com/blog/ai-productivity`,
  redirects from `cognition.ai/blog/ai-productivity`) — was fetched in full
  as a substantive linked page per MINER.md §1 and is treated as part of this
  source's evidentiary base throughout. Claims below are attributed to
  "primary post" or "methodology post" where the distinction matters.
- **Author credibility**: Published directly by Cognition, the company that
  builds and sells Devin — this is a vendor announcement with a direct
  commercial incentive (the guarantee is a sales/trust mechanism), and the
  methodology post is Cognition's own unaudited internal validation, not a
  third-party or peer-reviewed study. Scott Wu is Cognition's CEO for the
  primary post; the methodology post carries no individual byline. Unusually
  for a vendor post, the methodology piece discloses dataset size (258
  sessions, 126 users), a held-out evaluation split, a specific correlation
  statistic with significance testing, an explicit calibration formula, and a
  "Threats to Validity" section naming its own weaknesses — this is closer to
  a technical report than typical vendor marketing copy, though it remains
  self-published and self-audited.
- **Scope**: Covers why Cognition believes usage/activity metrics (tokens,
  lines of code) fail to answer "how much value is the business getting,"
  the two-step estimator mechanism (useful/not-useful classification, then
  human-hour estimation), the guarantee's financial structure (hours →
  dollars via a standard global rate, compared to consumption at contract
  end, credits up to $10M on shortfall), the dataset and design principles
  behind the estimator, held-out evaluation statistics and calibration, a
  numeric comparison to two independent studies (METR 2026, Anthropic 2026),
  and four explicitly disclosed threats to validity. Does NOT cover: the
  exact model(s) powering the estimator agent, the "standard global rate"
  used to convert hours to dollars, per-customer results (only aggregate
  statistics across the 126-user/258-session dataset are given), the guarantee's
  contractual mechanics beyond "compared against consumption... near the end
  of their annual contract," or any named customer who has actually received
  guarantee credits.

## Extracted Claims

### Claim 1: Existing AI usage dashboards (tokens consumed, lines of code generated) do not answer the business-value question, and the industry should shift from maximizing usage metrics to maximizing outcomes
- **Evidence**: Opening framing statement of the primary post, presented as
  the motivating premise for building the estimator and offering the
  guarantee.
- **Confidence**: anecdotal (vendor framing statement, not a measured claim,
  though the underlying observation — that token/LOC counts don't map to
  value — is a widely held practitioner view elsewhere in this corpus, see
  Cross-References → Corroborates)
- **Quote**: "Dashboards show activity metrics like tokens consumed and lines of code generated, but none of them actually answer the question: how much value is the business actually getting out?" ... "The industry needs to move from maximizing usage metrics to maximizing outcomes — and right now, there's no good standard for measuring that. AI vendors should be the ones to provide it."
- **Our assessment**: This is a vendor stating a problem it is about to sell a
  solution to, so it should be read as motivated framing — but the specific
  critique (activity metrics don't answer the value question) is directly
  corroborated by independent, non-Cognition sources already in this corpus
  (see Cross-References → Corroborates), which strengthens its credibility
  beyond a self-interested claim.

### Claim 2: Cognition built an estimator agent that reviews each completed Devin session and determines (1) whether it produced useful output and (2) how many hours a human engineer would have taken to produce the same work, validated against engineers' own time estimates, and this validation gave Cognition enough confidence to guarantee productivity up to $10M in credits
- **Evidence**: Direct summary statement in the primary post naming the
  two-step estimator mechanism and its role as the evidentiary basis for the
  guarantee.
- **Confidence**: emerging (a shipped, described mechanism with a disclosed
  validation dataset in the companion methodology post — not a single
  anecdote — but the validation is self-conducted and self-audited)
- **Quote**: "We built an AI estimator that measures the productive engineering output Devin is providing to enterprise customers. We validated our estimator against engineers' assessment of the time it would have taken to do the same work on their own. The results made us confident enough to offer a guarantee to our enterprise customers: if Devin delivers less engineering value than you're paying for, Cognition will fund your usage up to $10M until it does."
- **Our assessment**: This is the source's headline claim and a novel pattern
  for this corpus: an AI vendor backing a productivity claim with a direct
  financial guarantee rather than only a marketing statistic. The guarantee
  is only as strong as the estimator behind it (Claims 4-11 below detail that
  estimator's actual accuracy, which is meaningfully noisy per-session even
  if roughly unbiased in aggregate) — the guide should not repeat "$10M
  guarantee" without also citing the disclosed r_log = 0.74 and the ~2-3x
  per-session error range (Claim 8).

### Claim 3: The guarantee converts engineering hours to dollar value using a standard global rate, compares that figure against the customer's actual consumption near the end of their annual contract, and issues credits up to $10M if the value falls short
- **Evidence**: Direct structural description of the guarantee mechanism in
  the primary post's closing section.
- **Confidence**: emerging (a specific, named contractual structure for a
  shipped commercial offering; no detail on the exact "standard global rate,"
  how disputes are resolved, or whether any customer has yet received
  guarantee credits)
- **Quote**: "Engineering hours are converted to dollar value using a standard global rate and compared against each customer's actual consumption near the end of their annual contract. If the value falls short, we issue credits up to $10M."
- **Our assessment**: This is the concrete financial mechanism behind Claim
  2's headline — worth citing precisely because "guarantee" could otherwise
  be read as a vague marketing term; here it names the specific comparison
  (engineering-hour-value vs. dollar consumption, checked annually) and the
  remedy (credits, capped at $10M). No detail is given on what happens if the
  gap exceeds $10M, or on the "standard global rate" figure itself.

### Claim 4: The estimator measures productivity in hours rather than lines of code, because lines of code don't correspond to effort — "a critical bug that takes hours to investigate might be a two-line fix" — and the estimator agent has access to the user's prompt, the resulting PR, every action Devin took, and codebase context from DeepWiki
- **Evidence**: Direct mechanism description in the primary post naming both
  the chosen metric and the input context available to the estimator.
- **Confidence**: emerging (specific, disclosed design choice and input
  context list for a shipped estimator)
- **Quote**: "We measure in hours of productive output because lines of code don't correspond to effort: a critical bug that takes hours to investigate might be a two-line fix. The estimator agent has access to the user's prompt, the PR if one exists, every action Devin took, and codebase context from DeepWiki."
- **Our assessment**: The "lines of code don't correspond to effort" framing
  is directly corroborated by, and consistent with, existing vanity-metric
  critiques in this corpus (see Cross-References → Corroborates). The
  companion methodology post (Claim 7 below) expands on why hours specifically
  were chosen over both raw activity and direct dollar-impact measurement.

### Claim 5: Cognition considered measuring dollar impact directly (revenue attributable to shipped features, costs avoided by bug fixes) but rejected it as an unsolved problem, and considered raw activity (lines of code, commits, PRs, tokens) but rejected it because it doesn't correspond to effort — settling on human engineering hours as the metric that is standardized, denominated the way organizations already value work, and convertible to dollars via engineering rates
- **Evidence**: Direct three-way metric-selection reasoning in the
  methodology post's "Choosing a Metric" section, naming the two rejected
  alternatives and the mechanism (hourly rates) for the chosen one.
- **Confidence**: emerging (a disclosed reasoning process for a metric
  design decision, not itself a measured outcome)
- **Quote**: "Ideally, we'd measure dollar impact directly, such as revenue attributable to features shipped or costs avoided by bugs fixed. In practice, this is still an unsolved problem in our field." ... "On the other end of the spectrum, we could measure raw activity: lines of code, commits, PRs, tokens consumed. These are easy to collect but don't correspond to effort." ... "The middle ground we decided to measure is human engineering hours... Hours are standardized across organizations, independent of business context, and convertible to dollars via engineering rates."
- **Our assessment**: This three-way framing (dollar impact / raw activity /
  human-hours-as-middle-ground) is a reusable structure for the guide's own
  discussion of what to measure for AI productivity — it explicitly names why
  the two more obvious choices fail, rather than just asserting hours are
  correct. Not all hours are treated equally, though — see Claim 6, the
  productive-session filter this metric depends on.

### Claim 6: Sessions are filtered for usefulness before their hour-estimates are counted — sessions with a PR are included only if the PR merged; sessions without a PR go through a separate classifier that discards roughly 1-20% of sessions (varying by customer), removing cases where the agent lacked access, asked for clarification and got no reply, or otherwise couldn't meaningfully advance the task — while retaining genuinely productive non-PR work like dependency scans, security reviews, PR reviews, and analytics queries
- **Evidence**: Direct mechanism description in the methodology post's
  "Filtering for Useful Work" section, including the specific discard-rate
  range and named categories of retained non-PR work.
- **Confidence**: emerging (a specific, disclosed filtering mechanism with a
  quantified discard-rate range; the post itself flags this filter as
  "slightly lossy" — sessions with all-closed PRs "can still have delivered
  productive work" but are discarded conservatively)
- **Quote**: "For sessions with a PR, this is relatively straightforward: if any PR from the session is merged, we include the estimate; if not, we discard it. This is slightly lossy; sessions with all closed PRs can still have delivered productive work, but we wanted to err conservative." ... "We built a classifier to filter out unproductive sessions, which removes around 1-20% of sessions, depending on the customer."
- **Our assessment**: The merged-PR heuristic and the 1-20% non-PR discard
  range are specific, checkable design choices — worth citing as the concrete
  answer to "how does an automated estimator avoid crediting Devin for
  sessions that didn't actually help," a question the guide should expect
  readers to ask about any AI-value-measurement system.

### Claim 7: The estimator's prompt design rests on four principles distilled from manually triaging a 25-session development set: reason about the human's likely path rather than the agent's own (messier) trajectory; credit only the work the user didn't already specify; account for the assumed engineer's codebase familiarity based on what the session reveals; and assume the reference engineer already has whatever cross-disciplinary expertise the task required, understating effort in cases where a human would first need to learn an unfamiliar stack
- **Evidence**: Direct enumeration of four named design principles in the
  methodology post's "Building the Estimator" section, each with a stated
  rationale and, for two of the four, a worked example.
- **Confidence**: emerging (specific, named prompt-engineering principles
  derived from a disclosed 25-session development process; no ablation study
  showing how much each principle individually affects accuracy)
- **Quote**: "Reason about the human's path instead of the agent's. The agent's own trajectory is sometimes a poor proxy for human effort. Agents take detours, recover from environment and setup failures, and produce artifacts like summary reports that a solo engineer wouldn't." ... "Credit only the work the user did not specify... if a user comes with a bug report and no proposed fix, we include the time to triage the bug, whereas if the user comes with an implementation plan, we only count the implementation time." ... "Assume relevant expertise... Crediting that cross-disciplinary reach would inflate estimates, so we conservatively assume the reference engineer already has the expertise the task demands. This understates the effort in many cases."
- **Our assessment**: These four principles are the most transferable
  technique in the source for any team building a similar "how much would
  this have cost a human" estimator — each is a specific debiasing rule
  aimed at a named failure mode (agent-trajectory-as-proxy inflates estimates
  via detours; ignoring user-specified context inflates estimates by crediting
  work the human already did; ignoring familiarity swings estimates
  arbitrarily; crediting cross-disciplinary reach inflates estimates). Notably
  three of the four principles bias the estimator toward *underestimating*
  rather than overestimating delivered value, which is consistent with the
  methodology post's own framing of the aggregate total as "a deliberately
  conservative underestimate" (Claim 9).

### Claim 8: On a held-out evaluation set of 233 sessions, the estimator achieved r_log = 0.74 (r_log² = 0.54, F(1,231) = 279.9, p < 10⁻⁵); about 50% of sessions fell within a factor of 2 of the true estimate, with individual 2-3x errors common but roughly unbiased and independent, so they cancel out as aggregate totals are computed across more sessions
- **Evidence**: Specific statistical results from the methodology post's
  "Evaluation" section, including significance testing and an explicit
  characterization of noise-cancellation-at-scale.
- **Confidence**: emerging (disclosed, specific evaluation statistics with
  significance testing — more rigorous than a typical vendor claim — but
  self-conducted, self-audited, and not independently replicated or
  peer-reviewed)
- **Quote**: "On the held-out evaluation set of 233 sessions, our estimator has an r_log of 0.74 and r_log² of 0.54. The correlation is highly statistically significant (F(1,231) = 279.9, p < 10⁻⁵). Around 50% of sessions fall within a factor of 2 of the true estimate... 2–3× errors in either direction are common — but because errors are roughly unbiased and independent, they cancel as session count grows and the aggregate converges toward the human-reported total."
- **Our assessment**: This is the single most important caveat for anyone
  citing the $10M guarantee (Claim 2/3): the estimator is explicitly
  described as noisy at the individual-session level (half of estimates are
  off by more than 2x) and only reliable in aggregate across many sessions.
  The guide should present this statistic alongside the guarantee claim, not
  separately — a guarantee backed by a per-session-noisy-but-aggregate-reliable
  estimator is a meaningfully different (and more defensible) claim than one
  implying session-level accuracy.

### Claim 9: The estimator's raw predictions consistently underestimated the human-reported totals, so Cognition fit a log-space calibration (h = 2.28 × m^0.923); even after this correction, the sum of human estimates remains 1.4x the sum of corrected model estimates — a gap the post explains as a mathematical consequence of summing log-unbiased predictions in linear space (Jensen's-inequality-style bias) — and Cognition chose to report the uncorrected, conservative figure rather than apply a further correction for it
- **Evidence**: Direct methodology description in the "Evaluation" section,
  including the calibration formula, the residual 1.4x gap, a worked
  numeric example explaining the direction of the bias, and Cognition's
  explicit choice not to correct for it.
- **Confidence**: emerging (a specific, disclosed statistical correction with
  a stated rationale for a design choice — this level of methodological
  transparency, including naming a bias the vendor chose not to correct
  away, is unusual for a vendor blog post)
- **Quote**: "Our initial, uncalibrated model consistently underestimated. To correct this, we fit a linear regression in log-space: h = 2.28 × m^0.923." ... "Even after this correction, the total of the human estimates remains 1.4× the total of the corrected model estimates. This gap is expected: an estimator that is unbiased in log-space becomes biased once its predictions are summed in linear space, systematically underestimating the total... Rather than apply a further correction for this, we report the unadjusted figure as a deliberately conservative underestimate."
- **Our assessment**: This is a genuinely sophisticated and unusually candid
  piece of statistical reasoning for a vendor post — Cognition names a
  specific mathematical reason its own headline metric under-counts value by
  ~40%, and explicitly chooses not to fix that under-count because it favors
  the conservative direction for a guarantee product. This should be read as
  evidence the reported hour totals (and by extension, any dollar figure
  computed from them) likely *understate* delivered value, not overstate it
  — a rare instance of a vendor's stated bias direction working against
  its own headline number rather than inflating it.

### Claim 10: Cognition names four explicit threats to validity: the ground-truth human time-estimates are self-reported and collected via interviews where users knew they were talking to Cognition (possible social-desirability bias); voluntary responders may skew toward more engaged users; hours measure engineering capacity, not business value, and don't capture second-order effects like freed-up engineers moving to higher-leverage work; and hours don't account for quality, since a subtle bug introduced by the agent that takes a long time to debug represents negative uplift that the merged-PR filter doesn't catch
- **Evidence**: Direct enumeration of four named limitations under an
  explicit "Threats to Validity" heading in the methodology post.
- **Confidence**: settled (first-party admission of specific, named
  methodological weaknesses — a vendor naming the ways its own headline
  metric can be wrong carries more weight than an unqualified capability
  claim, since it works against the guarantee's promotional interest)
- **Quote**: "Ground truth bias. Our ground truth is self-reported. In our video user interviews, users were aware they were talking to Cognition, which might bias them." ... "Hours are not business value. We measure engineering capacity, not whether that capacity was deployed on high-value work... We also don't capture second-order effects, like freeing engineers for higher-leverage tasks." ... "Hours don't account for quality. If the agent introduces a subtle bug that takes a long time to debug and fix, its uplift on that task is negative. The merged-PR filter removes the clearest failures but not defects discovered after merging."
- **Our assessment**: The "hours are not business value" admission is the
  most important caveat for how the guide should frame this source overall:
  Cognition is explicit that its own guarantee measures engineering capacity
  delivered, not business value realized — the guarantee answers "did Devin
  save engineering hours," not "did those hours matter to the business." The
  self-report ground-truth caveat is directly relevant to this corpus's
  existing skepticism about self-reported productivity claims (see
  Cross-References → Corroborates); notably Cognition names this risk itself
  rather than it being surfaced by an outside critic.

### Claim 11: Two independent studies have also used LLMs to estimate human-equivalent task time: METR (2026), using GPT-4o/GPT-5 on compressed Claude Code transcripts from 7 METR staff, achieved r_log = 0.83 on 34 labeled sessions; Anthropic (2026), using Claude with only the title and description of 1,000 open-source Jira tickets, achieved r_log = 0.46 (versus r_log = 0.67 for human developers estimating the same tickets) — Cognition's own r_log = 0.74 is lower than METR's but higher than Anthropic's, which Cognition attributes to having more granular per-session data than the Jira-ticket-only study
- **Evidence**: Direct numeric comparison in the methodology post's
  "Comparison to Prior Work" section, naming both studies, their sample
  sizes, data sources, and correlation statistics.
- **Confidence**: emerging (a specific, named comparison to two independent
  studies with disclosed sample sizes and statistics — though Cognition did
  not independently verify either external study's methodology, and neither
  external study is a source note in this corpus at time of writing)
- **Quote**: "METR (2026) used a combination of GPT-4o and GPT-5 to estimate the human-equivalent times from compressed Claude Code transcripts. These transcripts were collected from 7 METR technical staff. On 34 sessions labeled on human ground truth, their estimator had an r_log of 0.83." ... "Anthropic (2026) estimated task duration on 1,000 open-source Jira tickets using Claude, but the estimator only had the ticket title and description to work with. They had an r_log of 0.46; human developers estimating the same tickets reached r_log = 0.67. Our system establishes stronger correlation than Anthropic's (r_log = 0.74 vs 0.46) because we have far more granular data per session."
- **Our assessment**: This is the first place in this corpus with a direct,
  named, numeric comparison across three independent organizations'
  approaches to the same underlying problem (predicting human-equivalent
  task time from agent session data). The comparison also surfaces a useful,
  generalizable finding on its own: richer session context (full trace, not
  just a ticket title/description) meaningfully improves estimate accuracy —
  Anthropic's ticket-only estimator (r_log = 0.46) underperformed even human
  developers doing the same ticket-only estimation task (r_log = 0.67), while
  Cognition's full-session-trace estimator (r_log = 0.74) outperformed both.
  Neither the METR nor the Anthropic study cited here has its own source note
  in this corpus; this claim should be cited as Cognition's own secondhand
  characterization of those studies, not independently verified against the
  originals.

### Claim 12: A simpler predictor using only total lines changed (additions + deletions) performed poorly (R²_log = 0.27) at predicting human time estimates, confirming code volume is a weak effort proxy; an estimator given only the agent's edit-tool-call trace (no user messages, no other session activity) performed better but still lagged the full estimator, indicating that effort-relevant signal — investigation, diagnosis, environment setup, tradeoff reasoning, non-code outputs — lives outside the final diff and is visible in the fuller session trace but not always in the code change itself
- **Evidence**: Two named ablation comparisons in the methodology post,
  isolating first a pure line-count signal, then an edit-trace-only signal,
  against the full estimator's context.
- **Confidence**: emerging (disclosed ablation results with specific R²
  figures for one comparison; the trace-only comparison's exact figure is
  not given, only a qualitative "performed better, but still lagged")
- **Quote**: "The first regresses a single scalar, the total lines changed... against our human estimates. It performed poorly, with an R²_log of 0.27, confirming that code volume is a weak proxy for engineering effort. We then evaluated an estimator agent given only the trace of the agent's edit tool calls as context, with no user messages or other session activity. It performed better, but still lagged the full estimator, suggesting that important signal lives outside the diff."
- **Our assessment**: This ablation is the strongest quantitative evidence in
  either post for the "lines of code is a bad productivity metric" claim
  asserted more casually elsewhere in the source (Claim 1, Claim 4) — R²_log
  = 0.27 for lines-changed alone versus R²_log = 0.54 for the full estimator
  (Claim 8) is a direct, measured demonstration that code-volume metrics
  capture roughly half the explanatory power of a metric that also considers
  user intent, investigation effort, and codebase-familiarity context.

## Concrete Artifacts

### The guarantee mechanism (primary post, verbatim structure)

```
Source: cognition.com/blog/ai-guarantee, "The AI Productivity Guarantee" section

1. An agent reviews each completed Devin session.
2. It estimates: (a) did this session result in useful output? (b) if so,
   how long would a human engineer have taken to produce the same work?
3. Engineering hours are converted to dollar value using a standard global
   rate.
4. That dollar value is compared against the customer's actual consumption
   near the end of their annual contract.
5. If the value falls short, Cognition issues credits up to $10M.
```

### Metric-selection reasoning (methodology post, "Choosing a Metric," verbatim structure)

```
Source: cognition.com/blog/ai-productivity, "Choosing a Metric" section

Rejected: direct dollar impact (revenue attributable to shipped features,
  costs avoided by bugs fixed) — "still an unsolved problem in our field"
Rejected: raw activity (lines of code, commits, PRs, tokens consumed) —
  "easy to collect but don't correspond to effort"
Chosen: human engineering hours — "standardized across organizations,
  independent of business context, and convertible to dollars via
  engineering rates"
```

### Estimator design principles (methodology post, "Building the Estimator," verbatim headings)

```
Source: cognition.com/blog/ai-productivity, "Building the Estimator" section

1. Reason about the human's path instead of the agent's.
2. Credit only the work the user did not specify.
3. Account for codebase familiarity.
4. Assume relevant expertise.
```

### Evaluation statistics and comparison table (methodology post, verbatim figures)

```
Source: cognition.com/blog/ai-productivity, "Evaluation" and "Comparison to
Prior Work" sections

Dataset: 258 sessions, 126 users, collected via live interviews + survey
Development set: 25 sessions (for prompt iteration)
Held-out evaluation set: 233 sessions

Cognition estimator:  r_log = 0.74, r_log^2 = 0.54  (F(1,231)=279.9, p<10^-5)
  - ~50% of sessions within a factor of 2 of true estimate
  - ICC = 0.58 (roughly half of residual disagreement is between-user, not
    within-user)
  - Calibration: h = 2.28 * m^0.923 (log-space regression)
  - Post-calibration: sum of human estimates still 1.4x sum of model
    estimates (reported as deliberately conservative, uncorrected)

Ablations:
  - Lines-changed-only predictor:  R^2_log = 0.27  (129 of 233 sessions with
    line-count data; 170 of 233 sessions had PRs but not all had diff stats)
  - Edit-trace-only estimator: "performed better, but still lagged the full
    estimator" (no exact figure given)

Comparison to prior work:
  - METR (2026): GPT-4o/GPT-5 on compressed Claude Code transcripts, 7 METR
    staff, 34 labeled sessions -> r_log = 0.83
  - Anthropic (2026): Claude on 1,000 open-source Jira tickets (title +
    description only) -> r_log = 0.46 (model) vs r_log = 0.67 (human
    developers estimating the same tickets)
  - Cognition: r_log = 0.74
```

### Threats to validity (methodology post, verbatim list)

```
Source: cognition.com/blog/ai-productivity, "Threats to Validity" section

1. Ground truth bias — self-reported, users aware they were talking to
   Cognition
2. Sampling — voluntary responders may skew toward more engaged users
3. Hours are not business value — measures engineering capacity, not
   whether that capacity was deployed on high-value work; doesn't capture
   second-order effects (e.g. freeing engineers for higher-leverage tasks)
4. Hours don't account for quality — a subtle bug introduced by the agent
   has negative uplift; the merged-PR filter catches the clearest failures
   but not defects discovered after merging
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-faros-claude-code-roi.md`,
`research-anthropic-ai-transforming-work.md`, `docs-ghaw-measuring-impact.md`,
`blog-thoughtworks-lad-platform-business-value.md`, and
`blog-cognition-hilsil-triage-test-generation.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-faros-claude-code-roi.md` Claim 5 ("Vanity metrics to avoid: lines
    of code, raw PR counts, autocomplete acceptance percentages" — "Individual
    output increases dramatically, but organizational delivery velocity stays
    flat"). This source's Claim 1 ("tokens consumed and lines of code
    generated... none of them actually answer the question") and Claim 12
    (measured: lines-changed-alone predicts human effort with R²_log = 0.27,
    "confirming that code volume is a weak proxy for engineering effort") are
    an independent vendor (Cognition, building an autonomous coding agent)
    reaching the same conclusion as Faros (a developer-productivity analytics
    vendor) about the same specific metrics, with this source additionally
    supplying a quantified, ablation-based demonstration that Faros's note
    does not — moving "LOC is a vanity metric" from stated consensus toward a
    measured, if self-conducted, result.
  - `docs-ghaw-measuring-impact.md` Claim 1 ("Measure impact by using early
    cost signals alongside later outcome signals. Do not try to collapse them
    into a single score") and Claim 2 (cost signals arrive early, outcome
    signals are delayed and downstream). This source's guarantee structure
    (Claim 3: hours converted to dollars, compared against consumption "near
    the end of their annual contract") is a concrete instance of exactly the
    outcome-signal-is-delayed pattern GitHub's docs describe abstractly — the
    guarantee's entire mechanism depends on waiting until contract-end (a
    delayed outcome signal) rather than settling against usage in real time
    (an early cost signal), which is the same timing asymmetry GitHub's docs
    name as a structural property of agentic-workflow measurement generally.
  - `research-anthropic-ai-transforming-work.md` Claim 2 (Anthropic engineers
    self-report a 50% productivity boost, but the note flags this against the
    pre-cutoff METR finding that self-reported 24% productivity gains
    coincided with an objectively measured 19% *slowdown* on the same tasks —
    "self-reported productivity is the least reliable evidence we have").
    This source's own Claim 10 ("ground truth bias... users were aware they
    were talking to Cognition, which might bias them") is Cognition
    independently naming the same self-report-reliability risk that
    motivates that note's skepticism — though the two sources' self-report
    mechanisms differ in kind (Anthropic's is a direct "how much faster do
    you feel" survey question; Cognition's is a counterfactual "how long
    would this specific task have taken you" estimate used as ML training/
    validation ground truth, a narrower and arguably less gameable question).
    See Extraction Notes for why this was evaluated as a tension worth
    flagging rather than a MINER.md §4a contradiction.

- **Contradicts**: None filed. See Extraction Notes for a near-miss
  (self-report-ground-truth reliability) that was evaluated against the
  MINER.md §4a filing bar and did not meet it.

- **Extends**:
  - `blog-cognition-hilsil-triage-test-generation.md` Claim 3 ("reclaimed
    2K–4K engineering hours per month across ~4,000 tickets, equating to
    $1.7M–$3.5M in annual savings") and Claim 8 ("a 10x increase in
    test-generation, from 1-2/day manually to 10-15 tests/day with
    AI-support") — that source discloses hours-to-dollars figures for named
    Cognition customers without disclosing any underlying estimation
    methodology. This source's methodology post is the first documentation in
    this corpus of how Cognition actually derives an hours-saved figure from
    session data (the two-step useful/hours estimator, the filtering
    heuristics, the four design principles) — plausibly the same or a related
    system to whatever produced the HIL/SIL post's figures, though neither
    post states this explicitly, so this should be cited as "the disclosed
    methodology class this kind of figure likely comes from," not as a
    confirmed shared system.
  - `blog-thoughtworks-lad-platform-business-value.md` Claims 5-6 (platform
    teams should reframe infrastructure spend as CAPEX and answer "how does
    this impact the business" in CFO-legible terms, since "if we can't speak
    the language of time-to-value or market share, we lose"). That source
    describes the funding-justification problem from the *buyer* side
    (platform teams needing to justify their existence to a CFO); this
    source is the *vendor* side of the identical dynamic — an AI vendor
    proactively converting its own product's output into dollar terms and
    backing that conversion with a financial guarantee, precisely the kind
    of "speak the language... or lose" proof point Lad's article argues a
    technology investment needs to survive budget scrutiny.

- **Novel**: The financial-guarantee business model itself (vendor credits
  tied to a measured productivity shortfall, up to $10M) is new to this
  corpus — no existing source note documents an AI vendor backing a
  productivity claim with a contractual financial remedy rather than only a
  marketing statistic. The specific statistical apparatus disclosed in the
  methodology post is also new: the log-space-calibration-creates-linear-space-
  underestimation-bias explanation (Claim 9), the direct three-way numeric
  comparison of independent effort-estimation studies (Claim 11), and the
  lines-changed-alone vs. trace-only vs. full-context ablation (Claim 12) are
  a level of quantitative methodological disclosure this corpus's other
  Cognition sources (auto-triage, HIL/SIL, verifying-agentic-development,
  devin-in-windsurf) do not reach — those sources report outcome figures
  without describing how the figures were derived.

## Guide Impact

- **Chapter 04/05 (Agent Evaluation / Measuring Impact)**: Add this source as
  the most methodologically detailed example in the corpus of an AI vendor
  attempting to measure agent-delivered value in a defensible way — cite the
  two-step estimator mechanism (Claim 2), the metric-selection reasoning
  (Claim 5: why not dollar-impact, why not raw activity), the design
  principles for the estimator prompt (Claim 7), and the held-out evaluation
  statistics with their explicit noise characterization (Claim 8: "50%
  within a factor of 2... errors... cancel as session count grows"). This is
  a more rigorous and more transparent methodology than `blog-faros-claude-
  code-roi.md`'s cohort-comparison recommendation or `research-anthropic-ai-
  transforming-work.md`'s self-report survey — recommend citing it as the
  worked example of "how would you actually build an automated estimator for
  this," while explicitly flagging that it remains vendor-self-conducted and
  unreplicated.

- **Chapter 05 (Team Adoption / Vanity Metrics)**: Add Claim 12 (the
  lines-changed-only ablation, R²_log = 0.27 vs. the full estimator's R²_log
  = 0.54) as a quantified data point for the existing "lines of code is a
  vanity metric" position anchored by `blog-faros-claude-code-roi.md` Claim
  5 — this is the first measured (if self-conducted) demonstration in the
  corpus of *how much* explanatory power is lost by using code volume alone.

- **Chapter 05 (Team Adoption / Communicating value upward)**: Add Claim 3
  (guarantee structure) and the Cross-References → Extends discussion with
  `blog-thoughtworks-lad-platform-business-value.md` as a concrete instance
  of a vendor proactively translating product output into CFO-legible dollar
  terms — useful alongside Lad's buyer-side framework as the vendor-side
  mirror image of the same "translate to business language or lose the
  funding argument" dynamic.

- **Chapter 03/05 (Verification / Limitations of self-measurement)**: Add
  Claim 10 (the four disclosed threats to validity, especially "hours are
  not business value" and the self-report ground-truth caveat) as a
  cautionary counterweight whenever Claims 2-3 (the $10M guarantee) or
  Claim 8 (r_log = 0.74) are cited elsewhere in the guide — the source's own
  admitted limitations should travel with its headline numbers, not be
  dropped.

## Extraction Notes

- Two pages were read in full for this note: the primary announcement
  (`cognition.com/blog/ai-guarantee`, ~500 words) and the linked technical
  methodology post (`cognition.com/blog/ai-productivity`, substantially
  longer, ~1,800 words across nine sections: intro, "Choosing a Metric,"
  "Collecting a Dataset," "Filtering for Useful Work," "Building the
  Estimator," "Evaluation," "Comparison to Prior Work," "Threats to
  Validity," "Conclusion"). The methodology post was followed as a
  substantive linked page per MINER.md §1 (reached via the primary post's
  "technical details of our methodology" inline link, which resolves via a
  301 redirect from `cognition.ai/blog/ai-productivity` to
  `cognition.com/blog/ai-productivity`). No further sub-pages were followed;
  the only other outbound link on either page is to DeepWiki's homepage
  (`deepwiki.com`), which is named only as a context-source component, not a
  substantive claim to extract.
- Both pages were fetched via direct HTML retrieval (`curl` with a browser
  user agent) rather than WebFetch's default summarizing pass, specifically
  to obtain character-for-character text for quoting per MINER.md §2a — the
  methodology post in particular contains inline LaTeX/MathML notation for
  statistical symbols (r_log, R²_log, etc.) that a summarizing pass would be
  likely to paraphrase or drop; the raw-HTML-to-text extraction preserved the
  surrounding prose verbatim around each statistic.
- The self-report-ground-truth tension noted under Cross-References →
  Corroborates (this source's Claim 10 vs. `research-anthropic-ai-
  transforming-work.md` Claim 2's METR-sourced self-report skepticism) was
  evaluated against the MINER.md §4a filing bar and does not meet it: the two
  sources are not making opposing claims under matching conditions. Anthropic's
  note is about the reliability of *direct* self-reported productivity-boost
  percentages ("I feel X% faster") as a standalone metric; this source's
  self-report is a *counterfactual time estimate* for a specific completed
  task, used as one of several inputs to train/validate a separate predictive
  model, with the model's output then checked against a further out-of-sample
  evaluation split (Claim 8) — a different measurement design answering a
  narrower question, not a claim that self-report is reliable in the same
  sense Anthropic's note is skeptical of. Cognition names the bias risk itself
  (Claim 10) rather than asserting the self-reported ground truth is
  unbiased, which is consistent with treating this as a shared, cross-source
  concern rather than a factual disagreement. No contradiction issue filed.
- Neither the METR (2026) nor the Anthropic (2026) study cited in Claim 11 has
  its own source note in this corpus at time of writing (a search across
  `source-notes/` for "METR," "r_log," and "Jira ticket" found only
  references *within* other notes to a different, pre-cutoff METR RCT study —
  the 24%-self-report-vs-19%-slowdown finding cited in `research-anthropic-
  ai-transforming-work.md` Claim 2 — which is a distinct study from the 2026
  METR transcript-estimation study this source cites). Claim 11 above is
  therefore Cognition's own secondhand characterization of both external
  studies, not independently verified against either original source; it is
  flagged as such in the claim's "Our assessment."
- Cross-references verified before writing: re-read `blog-faros-claude-code-
  roi.md` in full and confirmed Claim 5 by number and content; re-read
  `research-anthropic-ai-transforming-work.md` in full and confirmed Claim 2
  by number and content; re-read `docs-ghaw-measuring-impact.md` (partial —
  Claims 1-2, sufficient to confirm both by number and content) and confirmed
  by number and content; re-read `blog-thoughtworks-lad-platform-business-
  value.md` in full and confirmed Claims 5-6 by number and content; re-read
  `blog-cognition-hilsil-triage-test-generation.md` in full and confirmed
  Claims 3 and 8 by number and content. No claim number was guessed or
  approximated.
