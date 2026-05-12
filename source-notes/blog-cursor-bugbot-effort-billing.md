---
source_url: https://cursor.com/blog/may-2026-bugbot-changes
source_type: blog-post
title: "Updates to Bugbot for Teams and Individuals"
author: Cursor Team (no named individual)
date_published: 2026-05-11
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#695"
---

# Updates to Bugbot for Teams and Individuals

> Cursor's announcement of two simultaneous Bugbot changes — a shift from per-seat to usage-based billing and a new configurable effort level — provides the first published quantitative evidence of a code-review agent's effort-quality tradeoff (35% more bugs found at high effort, resolution rate constant at 80%) and introduces a new operational lever that changes how practitioners should design Bugbot-based review workflows.

## Source Context

- **Type**: blog-post (Cursor product announcement, ~300 words, published May 11, 2026; no named individual author). This is a concise product-policy post, not an engineering deep-dive. The billing model change is a concrete commercial policy decision; the performance claim (35% more bugs) derives from Cursor's own internal test runs.
- **Author credibility**: Cursor/Anysphere is the vendor behind Bugbot; this is first-party product documentation with a commercial incentive to present favorably. The quantitative effort-level claim ("35% more bugs while resolution rate stays constant at 80%") is stated as from "our internal runs" — vendor-run, not independently verified. The billing structure details (dollar amounts, timeline) are product policy, not claims requiring independent verification.
- **Scope**: Covers the pricing model transition (seat-based → usage-based), billing transition timeline, per-run cost range, and the new configurable effort levels including the effort-quality tradeoff. Does NOT cover: the technical mechanism behind the effort levels (how Bugbot "thinks for longer"), what "custom logic" for dynamic effort determination looks like in practice, the full help article details for the usage-based billing, or enterprise pricing implications.

## Extracted Claims

### Claim 1: Bugbot is transitioning from a $40 per seat per month subscription to usage-based billing for Teams and Individual plans

- **Evidence**: Direct product policy statement from the announcement. This is a pricing policy change, verifiable against the Cursor pricing page.
- **Confidence**: settled (product pricing policy, not a technical claim; announced with a specific effective date)
- **Quote**: "Bugbot is switching from a $40 per seat per month subscription to usage-based billing for Teams and Individual plans."
- **Our assessment**: The shift from seat-based to usage-based billing is a commercial model change with significant implications for team adoption economics. Under seat-based billing, a team's Bugbot cost was fixed regardless of PR volume — making cost predictable but potentially expensive for low-volume teams. Under usage-based billing, cost scales with PR volume — rewarding low-volume teams and charging more at high volume. For practitioners designing Bugbot-based workflows (such as the Amplitude auto-merge pattern documented in `blog-cursor-amplitude-autonomous-pipeline.md`), the new model changes the calculus: at $1.00-$1.50/run, a team with 1,000 automated runs per week (Amplitude's stated volume) would pay $1,000-$1,500 per week rather than a fixed per-seat fee.

### Claim 2: Existing customers' billing transition takes effect at their next billing renewal after June 8, 2026; annual subscribers wait until their renewal date

- **Evidence**: Explicit timeline provided in the announcement with an illustrative example.
- **Confidence**: settled (specific product policy with named date and example)
- **Quote**: "For existing customers, this change will start at your next billing renewal after June 8th, 2026. For example, if you bought an annual subscription in May 2026, these changes will only take effect in May 2027."
- **Our assessment**: The announced opt-in-before-automatic-transition path (existing customers can switch early via the Cursor dashboard) provides a migration window. This is notable in contrast to Cursor's past billing transitions — the silent billing-mode switch documented in `failure-cursor-pro-silent-billing-switch.md` was automatic without explicit consent at limit-hit time. This announcement is the opposite pattern: advance notice, specific date, explicit early-migration option. Teams evaluating whether to switch early should compare their current per-seat cost vs. their expected per-run cost under the new model before the automatic transition.

### Claim 3: The average Bugbot run costs $1.00–$1.50 depending on PR size and complexity

- **Evidence**: Direct cost figure from the announcement.
- **Confidence**: emerging (vendor-stated; the actual per-run cost will vary by PR size and complexity, making this a range estimate rather than a fixed rate; no methodology for how this average was calculated)
- **Quote**: "The average Bugbot run costs $1.00-$1.50, depending on PR size and complexity."
- **Our assessment**: The $1.00-$1.50 range is the first published per-run cost figure for Bugbot. It enables practitioners to model their expected monthly cost: at $1.25/run average, a team running 200 PRs/month would pay ~$250/month vs. the previous $40 × (number of seats). For a team of 6+ developers, the usage-based model is likely cheaper at typical PR volume; for teams with fewer developers but high PR volume, the seat model may have been more cost-effective. Teams should calculate their crossover point before switching. Note: "high effort" runs likely cost more than the $1.00-$1.50 average (since they involve deeper analysis), though no separate high-effort cost is stated.

### Claim 4: Users can now configure Bugbot to use different effort levels — including default, high effort, or custom dynamic logic

- **Evidence**: Direct product feature description from the announcement.
- **Confidence**: emerging (stated as a product feature; verifiable in product; details of "custom logic" configuration not provided in this post)
- **Quote**: "With usage billing, you can now choose the effort level Bugbot uses when reviewing PRs. Users can configure Bugbot to think for longer and run deeper reviews, or set up custom logic that Cursor uses to dynamically determine review effort."
- **Our assessment**: Configurable effort is a new operational lever absent from all prior Bugbot documentation in the corpus. This is architecturally significant: rather than a fixed review heuristic, practitioners now have a tuning knob that trades cost and time against bug-catch rate. The "custom logic for dynamic determination" is the most interesting capability — it implies users can define rules that select effort level based on PR characteristics (e.g., "use high effort for PRs touching auth code; use default for CSS changes"). This dynamic routing pattern is exactly the kind of harness configuration discussed in Chapter 02 and is novel to the corpus.

### Claim 5: Default effort preserves current Bugbot behavior with an 80% resolution rate

- **Evidence**: Explicit statement from the announcement comparing default to current behavior.
- **Confidence**: emerging (vendor-stated; from "our internal runs"; not independently verified)
- **Quote**: "Default effort preserves how Bugbot works today: 80% of bugs identified are resolved by merge time."
- **Our assessment**: This 80% figure is the updated resolution rate, slightly above the April 2026 benchmark table's 78.13% (`blog-cursor-bugbot-learning.md` Claim 4 and 6). The April post stated Bugbot was "nearing 80%"; the May post rounds or confirms the rate has reached 80%. This is consistent with the trajectory — no contradiction to file. The "80% of bugs identified are resolved by merge time" definition clarifies the resolution rate metric: it measures the fraction of Bugbot-identified bugs that are addressed before the PR merges, not overall bug-catch recall.

### Claim 6: High effort finds 35% more bugs while the resolution rate stays constant at 80%

- **Evidence**: Specific quantitative claim from "internal runs" by Cursor.
- **Confidence**: emerging (vendor-stated; from internal testing; not independently replicated; "35% more bugs" is relative to default effort on the same PRs, not to a human baseline)
- **Quote**: "From our internal runs, Bugbot with high effort finds 35% more bugs while resolution rate stays constant at 80%."
- **Our assessment**: This is the most actionable new claim in the source. The effort-quality tradeoff quantification — 35% more bugs found with no degradation in resolution rate — gives practitioners a concrete model for deciding whether high effort is worth the additional cost and time. The constant 80% resolution rate is the key finding: high effort does not produce more noise or false positives (which would lower the resolution rate if developers stop acting on spurious comments). If the 80% resolution rate held constant at higher effort, the incremental bugs found at high effort are as actionable as the bugs found at default effort. For practitioners: the question becomes whether the additional ~35% bug catch is worth the additional cost per run. For high-risk codepaths (authentication, payment processing, data migrations), the answer is likely yes; for CSS or documentation changes, likely no.

### Claim 7: Existing customers can opt into usage-based billing early via the Cursor dashboard before the automatic transition

- **Evidence**: Direct product option stated in the announcement.
- **Confidence**: settled (product feature; verifiable in dashboard)
- **Quote**: "Existing customers can switch to usage-based billing early in the Cursor dashboard."
- **Our assessment**: The early-switch option is a practical adoption signal: teams that calculate their crossover point and find usage-based billing advantageous do not need to wait until their renewal. Teams should calculate their expected monthly cost under both models using their actual PR volume and current seat count before deciding whether to switch early.

## Concrete Artifacts

### Bugbot Effort Level Configuration

```
# Bugbot configurable effort levels (Cursor product announcement, May 2026)
# Source: https://cursor.com/blog/may-2026-bugbot-changes

EFFORT LEVELS:
  Default:
    - Preserves current Bugbot behavior
    - Resolution rate: 80% of bugs identified are resolved by merge time
    - Cost: included in the $1.00-$1.50 average per run

  High:
    - Bugbot "thinks for longer and runs deeper reviews"
    - Finds 35% more bugs vs. default
    - Resolution rate: stays constant at 80% (no increase in noise)
    - Cost: implied higher than default (no separate figure stated)

  Custom (dynamic):
    - Users define logic that Cursor uses to determine effort level
    - Enables per-PR effort routing (e.g., high effort for auth code, default for CSS)
    - Configuration mechanism: not described in this announcement

EVIDENCE BASIS: "From our internal runs" — vendor-run, not independently verified
```

### Billing Model Transition

```
# Bugbot billing model transition (Cursor product announcement, May 2026)
# Source: https://cursor.com/blog/may-2026-bugbot-changes

OLD MODEL:
  Type:       Per-seat subscription
  Price:      $40 per seat per month
  Cost model: Fixed regardless of PR volume

NEW MODEL:
  Type:       Usage-based billing
  Teams:      Bills from on-demand spend
  Individuals: Bills from included usage
  Per-run cost: $1.00-$1.50 average (varies by PR size and complexity)

TRANSITION TIMELINE:
  Date:       After June 8, 2026 (at next billing renewal)
  Example:    Annual subscription bought May 2026 → changes in May 2027
  Early opt-in: Available in Cursor dashboard (before automatic transition)

COST MODELING (at $1.25/run average):
  100 runs/month  → ~$125/month
  500 runs/month  → ~$625/month
  1,000 runs/month → ~$1,250/month

  Break-even vs. $40/seat: 1,000 runs/month = 25 seats (varies by PR volume)
```

### Resolution Rate Context

```
# Bugbot resolution rate trajectory (from corpus)
# Combining blog-cursor-bugbot-learning.md and this source

July 2025 (launch):     ~52%     (blog-cursor-bugbot-learning.md Claim 4)
April 2026 (benchmark): 78.13%  (blog-cursor-bugbot-learning.md Claim 6)
April 2026 (post text): "nearing 80%"  (blog-cursor-bugbot-learning.md Claim 4)
May 2026 (this source): 80%     (default effort baseline)

High effort (May 2026): 80% resolution rate (same), 35% more bugs found
```

## Cross-References

- **Corroborates**: `blog-cursor-bugbot-learning.md` Claim 4 and 6 — The April 2026 benchmark table reported Bugbot at 78.13% ("nearing 80%"); this source states 80% as the default maintained rate in May 2026. The trajectory from 78.13% → 80% is consistent with the "nearing 80%" language and the ongoing online learning mechanism. No contradiction.

- **Extends**: `blog-cursor-bugbot-learning.md` (entire note) — The April note covers Bugbot's learned-rules mechanism and resolution rate trajectory. This note adds the configurable effort dimension: rather than a single fixed heuristic, practitioners can now select from multiple operating points on the effort-quality curve. Together the two notes provide the mechanism (how Bugbot learns and improves) plus the configuration surface (how practitioners tune the depth of each review run).

- **Extends**: `blog-cursor-amplitude-autonomous-pipeline.md` Claim 2 — Amplitude runs ~1,000+ automated Bugbot runs per week and auto-merges 60–70% of low-risk PRs. Under the new billing model, Amplitude's Bugbot usage would cost ~$1,000–$1,500/week ($1.25/run average × 1,000 runs). The configurable effort level gives teams like Amplitude a new axis: route high-risk PRs to high-effort reviews (finding 35% more bugs before auto-merge decisions) and low-risk PRs to default effort. This changes the risk-stratification capability described in that note.

- **Contextualizes**: `failure-cursor-pro-silent-billing-switch.md` (entire note) — That failure report documents Cursor silently switching Pro subscribers to on-demand billing with no advance notice at the point of plan limit. This announcement is the opposite pattern: advance notice of a billing model change, a specific effective date, an illustrative example, and an explicit early opt-in path. Teams reading the failure report should note this contrast: Cursor has adopted better billing-transition transparency for this change compared to the silent mode-switch pattern documented in February 2026. However, teams should still model their expected costs before the automatic transition, as described in `failure-cursor-pro-silent-billing-switch.md`'s guide impact.

- **Novel**: The following claims are not documented in any other source note in the corpus:
  - **Configurable effort levels for AI code review**: No prior source documents the pattern of giving practitioners a per-run effort dial (default / high / custom dynamic) on a code review agent. This is the first published example of parametric effort control in a production AI code review tool.
  - **35% more bugs at high effort with constant resolution rate**: No prior source provides a published effort-quality tradeoff curve for an AI code review tool. The finding that more bugs are found without increasing false positives (resolution rate constant at 80%) is the key practical result — it establishes that high effort is additive signal, not additional noise.
  - **$1.00–$1.50 per-run cost baseline**: No prior source provides a published per-run cost estimate for Bugbot. This is the first concrete cost anchor for modeling team-level Bugbot spending under usage-based billing.

## Guide Impact

- **Chapter on Harness Engineering (Ch02)**: The configurable effort level is a new harness pattern — "effort routing" — that belongs in any section on AI review configuration. The recommendation: define per-codebase-area effort routing rules (high effort for auth/payment/migration code; default for CSS, docs, routine refactors). The custom dynamic logic option is the practical implementation path. Practitioners can model the cost uplift from high-effort runs against the 35% additional bug catch to determine routing rules for their codebase.

- **Chapter on AI-Assisted Code Review (Ch07 or equivalent)**: Update the Bugbot resolution rate figure from 78.13% (April 2026) to 80% (May 2026, default effort). Add the effort-quality tradeoff: 35% more bugs at high effort, 80% constant resolution rate. This is the first published number for an AI code review tool's effort-quality curve and should be presented as the current state of the art for production AI code review.

- **Chapter on Team Adoption (Ch05)**: Add a Bugbot cost modeling exercise. Under usage-based billing at $1.00–$1.50/run: (a) calculate your team's expected monthly PR volume, (b) compute expected monthly cost, (c) compare to previous $40/seat cost, (d) decide whether early opt-in is beneficial. For teams running > 25–40 PR reviews/seat/month, usage-based may be more expensive; for teams with fewer reviews per engineer, it may be cheaper. This is a concrete team adoption evaluation step that should appear in any chapter on evaluating commercial AI review tools.

- **Chapter on Agent Execution and Control (Ch04 or equivalent)**: The effort-quality tradeoff pattern (configurable effort → measurable additional bug catch) is a generalizable design pattern for AI agents beyond code review. Any agent that can "think for longer" can be parameterized by effort; the key measurement is whether additional effort produces additional signal (bugs, issues, insights) without additional noise (false positives that lower developer trust). The Bugbot finding — constant resolution rate at higher effort — is the ideal property to demonstrate for this pattern.

## Extraction Notes

1. **Source is short by design**: The blog post is approximately 300 words and is a product announcement covering two changes. Full content was read. The post is deliberately concise — implementation details of the custom dynamic effort logic, the cost of high-effort runs, and the mechanism behind the 35% improvement are not disclosed. These are genuine omissions, not artifacts of skimming.

2. **"Internal runs" evidence**: The 35% more bugs finding is explicitly attributed to "our internal runs" — Cursor's own testing, not a public benchmark. Unlike the April 2026 resolution-rate benchmark (which tested six tools on public repos), this claim has no published methodology, no PR count, and no independent replication. Treat as emerging confidence.

3. **Resolution rate 78.13% vs. 80%**: The April note reported 78.13% from a public-repo benchmark table and "nearing 80%" from the post text. This May post states 80%. The 1.87pp difference is within noise for a vendor rounding a benchmark result in a product announcement. No contradiction issue filed — this is consistent progression, not opposition.

4. **High-effort cost not disclosed**: The post states the average Bugbot run costs $1.00–$1.50, but does not separately state the cost of a high-effort run. Given that high effort involves deeper analysis ("think for longer"), the per-run cost at high effort likely exceeds the stated average. Teams designing effort routing should verify high-effort cost separately in the help article.

5. **Custom effort logic not described**: The "custom logic that Cursor uses to dynamically determine review effort" is mentioned but not detailed in this post. The help article linked in the post's footer ("check out this help article") was not followed for this extraction — it may contain configuration examples that would be valuable as concrete artifacts. If the help article is substantial, it may warrant a separate source note.
