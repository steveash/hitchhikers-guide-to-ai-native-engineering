---
source_url: https://cursor.com/blog/bugbot-learning
source_type: blog-post
title: "Bugbot now self-improves with learned rules"
author: Cursor (product team, no named individual)
date_published: 2026-04-08
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#208"
---

# Bugbot now self-improves with learned rules (Cursor)

> Cursor's first-party description of how Bugbot converts three distinct live
> PR signal types (reactions, replies, human reviewer comments) into a
> candidate→active→disabled rule lifecycle that has pushed resolution rate from
> ~52% at July 2025 launch to 78.13% — the first published account of online
> learning applied to a production AI code review agent at scale (110k+ repos,
> 44k+ rules), along with a vendor-self-reported resolution-rate benchmark table
> covering six tools.

## Source Context

- **Type**: blog-post (Cursor product team announcement, ~600 words, published
  April 8, 2026; no named individual author). This is a product announcement, not
  an engineering deep-dive — the mechanism is described at a conceptual level
  without implementation details, thresholds, or model architecture.
- **Author credibility**: Cursor/Anysphere is the vendor behind Bugbot; this is
  first-party product documentation with a commercial incentive to present
  favorably. The technical claims about signal types and rule lifecycle are
  internally coherent and consistent with Cursor's broader published approach to
  production signal harvesting (see `blog-cursor-real-time-rl.md` for the
  analogous pattern applied to Composer model training). The benchmark figures
  are vendor-self-reported using Cursor's own LLM judge — not independently
  verified. Scale figures (110k repos, 44k rules) are stated without audit
  methodology.
- **Scope**: Covers the signal taxonomy, the rule promotion/demotion lifecycle,
  manual rule control, the resolution-rate benchmark table (six tools), and the
  claim that online learning added what offline experiments alone could not.
  Does NOT cover: the specific LLM or model architecture underlying rule
  generation, promotion thresholds, how candidate rules are generated from raw
  signals, the Bugbot Autofix companion feature (covered in a separate Feb 2026
  post), non-public-repo behavior, or enterprise-specific rule sharing.

## Extracted Claims

### Claim 1: Bugbot converts three distinct live PR signal types into rule candidates — reactions, developer replies, and human reviewer comments

- **Evidence**: Direct product description from the post naming all three signal
  channels and their distinct semantics.
- **Confidence**: emerging (first-party architectural description; mechanism is
  coherent; specific weighting or aggregation not disclosed)
- **Quote**: "A downvote tells Bugbot the finding wasn't useful. Replies let
  developers explain what was wrong or how the suggestion could have been better.
  Human reviewer comments flag issues that Bugbot missed."
- **Our assessment**: The three channels cover the complete feedback vocabulary
  of a PR review cycle: explicit negative signal (downvote), explanatory signal
  (reply), and miss signal (human reviewer catches what Bugbot didn't). The
  miss signal is the most novel — it turns human reviewer activity into an
  implicit label that the AI system missed something. This is RLHF-adjacent
  applied to rule curation rather than model weights: the signal taxonomy maps
  onto negative reward, corrective explanation, and recall gap, respectively.
  For practitioners designing similar feedback loops: all three signal types are
  available in standard PR tooling without custom instrumentation.

### Claim 2: Rules follow a candidate→active→disabled lifecycle, with promotion triggered by accumulated positive signal and demotion by consistent negative signal

- **Evidence**: Direct lifecycle description from the post.
- **Confidence**: emerging (first-party description; promotion/demotion thresholds
  not disclosed)
- **Quote**: "As signal accumulates, Bugbot can promote a candidate rule to active
  status where it begins influencing future reviews. If an active rule starts
  generating consistent negative signal, Bugbot can disable it."
- **Our assessment**: The three-state lifecycle (candidate → active → disabled)
  is the key architectural pattern from this source. Candidate state provides a
  buffer period where the rule is evaluated against real PRs before influencing
  output — analogous to canary deployment for model changes. The disabled state
  (not deleted) preserves the signal history, which matters for audit trails and
  for potential re-promotion if team context changes. The lifecycle is described
  without thresholds: "accumulates" and "consistent" are not quantified, which
  limits the ability to replicate or tune the pattern.

### Claim 3: Users can directly edit or delete rules in a UI, providing manual override of the automated lifecycle

- **Evidence**: Direct statement from the post.
- **Confidence**: settled (stated as a product feature; verifiable in product)
- **Quote**: "You can also edit or delete rules directly in the UI."
- **Our assessment**: Manual override is a critical safety valve for any
  automated rule system. It allows teams to correct learned rules that are
  technically promoted but operationally incorrect for their specific context
  (e.g., a rule about naming conventions that conflicts with the team's
  documented style guide). The absence of manual control in similar systems
  is a common failure mode — this addresses it. For harness engineering:
  any AI rule or preference system should expose a manual override path.

### Claim 4: Resolution rate improved from approximately 52% at July 2025 launch to 78.13%, nearing 80%, described as 15 percentage points above the next-closest competitor

- **Evidence**: Direct improvement claim with launch baseline and current figure.
- **Confidence**: emerging (vendor-self-reported; benchmark methodology is
  described but not independently verified; "nearing 80%" suggests the figure
  in the benchmark table is not the very latest internal number)
- **Quote**: "nearing 80%, 15 percentage points higher than the next-closest
  AI code review product"
- **Our assessment**: The 26pp improvement from 52% to 78% is the headline
  claim. The causal attribution to online learning (vs. the offline improvements
  that would have happened anyway) is implicit, not empirically isolated in the
  post. The post asserts that offline experiments alone were insufficient at
  scale, but does not provide a counterfactual. Take the directional claim
  (online signals accelerated improvement) as plausible given the scale (110k+
  repos), while treating the specific 15pp advantage over the next competitor as
  vendor-favorable framing. The "nearing 80%" language suggests the 78.13%
  benchmark figure slightly lags current performance.

### Claim 5: Offline experiment-based improvement was the prior methodology — Bugbot changes were tested offline and shipped only if the resolution rate improved

- **Evidence**: Author's explicit description of the prior process as the
  contrast case for why online learning is additive.
- **Confidence**: emerging (self-reported process description)
- **Quote**: "We tweak Bugbot, test to see if the change improves the resolution
  rate, and we ship it if it does."
- **Our assessment**: The prior offline loop is the standard model improvement
  process for AI products. The post's implicit claim is that this loop is
  insufficient at scale because: (a) it cannot capture org-specific patterns
  without training on each org's data, and (b) the feedback cycle is slow
  relative to the volume of signals available in production. Neither limitation
  is explicitly quantified, but both are architecturally sound. The transition
  from offline-only to hybrid offline+online improvement is the same trajectory
  described in `blog-cursor-real-time-rl.md` for Composer — suggesting this is
  a deliberate platform-level design philosophy at Cursor, not a Bugbot-specific decision.

### Claim 6: Resolution-rate benchmark table shows Bugbot at 78.13% (50,310 PRs), 15pp above Greptile (63.49%), with four other tools below 49%

- **Evidence**: Vendor-run benchmark on public repositories only, using an LLM
  judge to check whether each AI code review comment was addressed before merge.
- **Confidence**: anecdotal (vendor-self-reported; LLM judge methodology not
  audited independently; public-repo-only scope may not represent enterprise
  usage patterns)
- **Quote**: "For each comment produced by an AI code review product, we checked
  to see if it was addressed by the time it merged using an LLM judge."
- **Our assessment**: The LLM judge methodology is a reasonable proxy for
  "did the comment provide useful guidance?" — if a comment is addressed before
  merge, it likely influenced the PR author's decision. However, there are two
  systematic biases to flag: (1) Bugbot is trained on the same signal this
  benchmark measures, giving it a structural optimization advantage; (2) comments
  that are "addressed" by rejection (author explicitly chose not to act) may be
  counted differently from comments that were acted on. The public-repo-only
  scope (stated) means the benchmark may not reflect enterprise/private-repo
  behavior where team-specific rules matter most. **Do not compare this table
  directly to the DeepSource OpenSSF CVE benchmark** (`discussion-hn-autofix-hybrid-review.md`):
  that table measures precision/recall on security CVEs; this table measures
  comment resolution rate on general PRs — completely different metrics.

### Claim 7: 110,000+ repos have enabled learning; 44,000+ learned rules have been generated; Bugbot reviews hundreds of thousands of PRs per day

- **Evidence**: Scale figures stated directly in the post.
- **Confidence**: emerging (vendor-stated; no audit methodology described)
- **Quote**: "More than 110,000 repos have enabled learning" and "more than
  44,000 learned rules"
- **Our assessment**: The 44k-rules / 110k-repos ratio (~0.4 rules per repo
  on average) suggests most repos have learned zero or one rules, while a subset
  have accumulated many. This sparsity is expected: rule learning requires
  sufficient PR volume and consistent human feedback signals, which only
  high-velocity repos generate. The "hundreds of thousands of PRs per day"
  processing volume is the scale justification for why offline learning alone
  cannot capture the signal diversity — the volume of feedback signal dwarfs
  what any offline experiment set could cover.

### Claim 8: Learned rules enable team-specific customization — "helping Bugbot focus on specific issues, business context, and more"

- **Evidence**: Post's description of the rule system's purpose.
- **Confidence**: emerging (stated intent; whether the learned rules actually
  reflect team-specific business context vs. generic code quality patterns is not
  demonstrated)
- **Quote**: "Rules enable greater customization of Bugbot runs, helping Bugbot
  focus on specific issues, business context, and more."
- **Our assessment**: The customization framing positions learned rules as a
  substitute for manual configuration: rather than requiring teams to explicitly
  document their review preferences, Bugbot infers them from behavior. This is
  the adaptive-to-team-context pattern that is broadly desirable in AI coding
  tools (per `survey-pragmaticengineer-ai-tooling-2026.md`, team-specific
  customization is a top practitioner ask). Whether the inferred rules actually
  capture business context (e.g., "never approve changes to the payment module
  without a security review") vs. superficial stylistic patterns is the open
  question. The post does not provide examples of learned rules.

## Concrete Artifacts

### Resolution Rate Benchmark Table (vendor-run, public repos only, LLM judge)

```
# Bugbot resolution-rate benchmark (Cursor, April 2026)
# Methodology: LLM judge checks whether each AI code review comment
#              was addressed by the time the PR merged
# Scope: public repositories only
# Source: vendor-self-reported; not independently verified

Tool                 | Resolution Rate | PRs Analyzed
---------------------|-----------------|-------------
Cursor Bugbot        | 78.13%          | 50,310
Greptile             | 63.49%          | 11,419
CodeRabbit           | 48.96%          | 33,487
GitHub Copilot       | 46.69%          | 24,336
Codex                | 45.07%          | 19,384
Gemini Code Assist   | 30.93%          | 21,031

IMPORTANT: Do NOT compare to DeepSource OpenSSF CVE benchmark
(discussion-hn-autofix-hybrid-review.md) — different metric
(resolution rate vs. security CVE precision/recall).
```

### Bugbot Rule Lifecycle

```
# Bugbot learned-rules lifecycle (Cursor product description, April 2026)

SIGNAL COLLECTION
  Source 1 — Reactions:
    Downvote → finding was not useful (negative signal)
    [Upvote behavior not described in post]
  Source 2 — Replies:
    Developer reply → explains what was wrong or how to improve the suggestion
    (corrective/explanatory signal)
  Source 3 — Human reviewer comments:
    Human flags an issue Bugbot missed
    (miss signal / recall gap indicator)

RULE LIFECYCLE
  CANDIDATE state:
    - Rule generated from accumulated signals
    - Not yet influencing reviews
    - Being evaluated against incoming PRs

  ACTIVE state (promotion from candidate):
    - Triggered when "signal accumulates" [threshold not disclosed]
    - Rule begins influencing future Bugbot reviews
    - Target: focus on specific issues, business context

  DISABLED state (demotion from active):
    - Triggered when active rule generates "consistent negative signal"
    - Rule removed from influencing reviews
    - [Whether historical signal is preserved: not stated]

MANUAL OVERRIDE
  - Users can edit rules directly in the UI
  - Users can delete rules directly in the UI
  - Manual override applies regardless of automated lifecycle state

SCALE (as of April 2026)
  - 110,000+ repos with learning enabled
  - 44,000+ learned rules generated
  - Hundreds of thousands of PRs reviewed per day
```

### Resolution Rate Trajectory

```
# Bugbot resolution rate improvement (Cursor, April 2026)

July 2025 (launch):  ~52%
April 2026:          78.13% (benchmark table) / "nearing 80%" (post text)

Net improvement:     ~26 percentage points over ~9 months
Claimed advantage:   15 pp above next-closest competitor (Greptile at 63.49%)

Prior methodology:   Offline experiments — tweak → test → ship if improved
Current methodology: Offline experiments + online learning from production signals
```

## Cross-References

- **Corroborates**: `blog-cursor-real-time-rl.md` — Cursor's real-time RL pipeline
  for Composer uses the same foundational design philosophy: harvest production user
  signals (edit persistence, dissatisfied follow-ups) as learning signal, rather than
  relying on offline evaluation alone. The Bugbot learned-rules system is the code
  review equivalent: production PR signals (reactions, replies, human comments) replace
  the offline experiment loop for rule discovery. The `blog-cursor-real-time-rl.md`
  post frames this as "each attempted reward hack becomes a bug report" — the same
  meta-principle applies here: each human reviewer who catches something Bugbot missed
  is a recall-gap bug report that gets incorporated into future runs. The key
  difference: Composer RL updates model weights; Bugbot updates discrete rules.
  The discrete-rule approach is more interpretable and manually auditable.

- **Corroborates**: `blog-cursor-composer2-technical-report.md` — The Composer 2
  technical report describes Cursor's philosophy of training on production-identical
  environments and using real user interactions as ground truth. Bugbot's learned
  rules extend this to code review: real PR reviewer behavior is ground truth for
  what constitutes a useful review comment. Both sources reveal Cursor's platform-level
  commitment to production signals over synthetic evaluation.

- **Complements** (different metric, same tool): `discussion-hn-autofix-hybrid-review.md`
  — That note covers Bugbot's precision/recall on the DeepSource OpenSSF CVE security
  benchmark (recall 87.80%, precision 69.23%, F1 77.42%). This source covers Bugbot's
  general resolution rate on public PRs (78.13%). These metrics are not contradictory:
  they measure different dimensions on different benchmarks. The security benchmark
  measures coverage of real vulnerabilities; the resolution rate benchmark measures
  developer uptake of comments. A team choosing Bugbot should consult both dimensions.

- **Extends**: `docs-github-copilot-pr-review-metrics.md` — GitHub's Copilot review
  metrics API tracks `median_minutes_to_merge_copilot_reviewed` as the outcome metric.
  This source provides the complementary view: resolution rate (did the comment get
  acted on?) is a direct proxy for comment quality, whereas merge time is a proxy for
  review efficiency. Together the two metrics would give a fuller picture of AI review
  impact. Neither source provides both dimensions simultaneously.

- **Corroborates**: `blog-cursor-security-agents.md` — Cursor's security agents post
  (March 2026) reports 3,000+ PRs reviewed weekly by Cursor's own internal AI agents.
  This Bugbot post reports hundreds of thousands of PRs reviewed per day across all
  Bugbot users. Together they establish Cursor's operational familiarity with AI code
  review at production scale — making the signal-to-rule claims more credible as
  engineering conclusions, not just product marketing.

- **Novel**: The three-signal taxonomy (reactions / replies / human reviewer comments)
  as a structured feedback vocabulary for AI code review is new to the corpus. No other
  source has articulated how AI review systems can harvest the full behavioral signal
  available in a PR review cycle. The candidate→active→disabled rule lifecycle as a
  pattern for online learning in code review tools is also new — `blog-cursor-real-time-rl.md`
  covers weight updates, not discrete rule curation. The LLM-judge-on-public-repos
  resolution-rate methodology is a reusable eval pattern not documented elsewhere in
  the corpus.

## Guide Impact

- **Chapter on AI-Assisted Code Review (Ch07 or equivalent)**: Add the six-tool
  resolution rate benchmark table as the most current head-to-head comparison for
  general code review quality. Frame it with the methodology caveats: vendor-run,
  LLM judge, public repos only, Bugbot optimized for this metric. Contrast with the
  DeepSource security-specific benchmark from `discussion-hn-autofix-hybrid-review.md`
  so readers understand they are measuring different dimensions (general utility vs.
  security recall). The 15pp gap between Bugbot and Greptile is currently the largest
  differentiation in the general-review dimension.

- **Chapter on Feedback Loops / Agent Self-Improvement (Ch09 or equivalent)**: The
  three-signal taxonomy and candidate→active→disabled lifecycle are the most concrete
  published description of online learning applied to a production AI code review agent.
  Extract as a reference pattern: signal collection (reactions + replies + miss signals)
  → rule candidacy → signal accumulation → promotion → active influence → demotion on
  negative. The manual override requirement is a design lesson — any automated rule
  system needs an explicit human-override path. Contrast with Cursor Composer's weight-
  level RL (`blog-cursor-real-time-rl.md`) to illustrate the spectrum from discrete
  interpretable rules (Bugbot) to continuous weight updates (Composer RL).

- **Chapter on Evaluation Design (Ch04 or equivalent)**: The resolution rate
  methodology ("did the comment get addressed before merge, checked by LLM judge,
  across public repos") is a reusable eval pattern for any AI code review system.
  Teams building their own AI review pipelines can implement this benchmark against
  their own PR history. The key design decisions to replicate: (a) scope to merged
  PRs only, (b) use an LLM judge rather than exact-match heuristics, (c) measure per
  comment rather than per PR. Flag the systematic bias: a system trained on this
  signal has an advantage over systems that are not — so this metric favors
  production-signal-learning systems structurally.

- **Chapter on Team Adoption (Ch05)**: The "110k repos, 44k rules" scale data supports
  the claim that AI tools that adapt to team context will win adoption over tools that
  do not. Teams operating at rule-sparse scale (0.4 rules/repo average) should expect
  meaningful learned rules only after accumulating sufficient PR volume. For teams
  evaluating Bugbot: the self-improvement mechanism provides most value to high-velocity
  teams (many PRs, many reviewers, many feedback signals). Low-velocity teams will see
  slower rule accumulation and less differentiation from the offline-trained baseline.

- **Chapter on Harness Engineering (Ch02)**: The signal taxonomy is a transferable
  pattern for any AI tool that processes human accept/reject signals in a loop:
  (1) collect explicit rejection signals (thumbs down), (2) collect corrective
  explanatory signals (replies), (3) collect miss signals (what did a human reviewer
  catch that the AI didn't?). The third signal type — detecting misses — is the most
  powerful and the least obvious. Teams building custom AI review hooks should instrument
  all three signal channels, not just the explicit feedback UI.

## Extraction Notes

1. **Source is thin by design**: The blog post is ~600 words and a product announcement.
   Full content was read. The mechanism is described at a conceptual level — the post
   does not disclose promotion thresholds, rule generation model, or specific signal
   weighting. This is intentional product communication, not an engineering specification.
   The claims above extract everything stated; the gaps (thresholds, model details) are
   genuine omissions, not artifacts of skimming.

2. **Benchmark methodology caveat (critical)**: The resolution-rate benchmark is
   Cursor's own measurement using Cursor's own LLM judge on public repos. Bugbot is
   specifically optimized via online learning to maximize this signal — making this
   benchmark partially circular for Bugbot specifically. The other five tools are
   measured on the same metric but are NOT optimized for it in the same way. Treat
   Bugbot's 78.13% as an upper-bound estimate under favorable conditions; the other
   tools' figures are more likely to reflect typical performance.

3. **No contradictions to file**: The resolution-rate table does not contradict the
   DeepSource security benchmark in `discussion-hn-autofix-hybrid-review.md` because
   they measure different things. No other existing source note makes claims about
   production AI code review resolution rates that this source would oppose.

4. **Companion post not fetched**: The post references "Closing the code review loop
   with Bugbot Autofix" (published Feb 26, 2026) as a companion feature. That post was
   not fetched for this extraction — it covers automated fix generation, not the
   learned-rules mechanism. It may be worth a separate source submission if it contains
   extractable patterns.

5. **Issue #142 (PlanetScale case study)**: The first Prospector triage comment
   references Issue #142 as a prior Bugbot case study at `cursor.com/blog/planetscale`.
   No corresponding source note was found in `source-notes/`. If that issue has not
   been mined, it may provide a practitioner adoption story that complements the
   mechanism description here.
