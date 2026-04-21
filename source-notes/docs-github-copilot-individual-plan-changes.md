---
source_url: https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals
source_type: docs
title: "Changes to GitHub Copilot plans for individuals"
author: GitHub (official changelog)
date_published: 2026-04-20
date_extracted: 2026-04-21
last_checked: 2026-04-21
status: current
confidence_overall: settled
issue: "#289"
---

# Changes to GitHub Copilot Plans for Individuals

> GitHub's April 20, 2026 changelog documenting plan-level model access
> restrictions, usage-limit tiering, and new signup pauses for individual
> Copilot plans — establishing that Opus-tier model access is now a
> plan-gated constraint for individual practitioners, not a universal
> individual-plan entitlement.

## Source Context

- **Type**: docs (GitHub official product changelog, ~400 words, April 20 2026)
- **Author credibility**: GitHub engineering team announcing production changes
  to individual Copilot plans. Authoritative for the fact that these changes
  exist, what the model-tier mapping is per plan, and what the refund window is.
  Not a credible source for long-term plan strategy or whether these restrictions
  will persist — the changelog is a point-in-time announcement.
- **Scope**: Changes to individual-tier Copilot plans (Free, Pro, Pro+, Student).
  Covers: new signup restrictions, usage-limit tiering rationale, Opus model
  availability per plan tier, and a refund policy for affected subscribers.
  Does NOT cover: Business or Enterprise plan changes (those are separate
  subscription tiers); specific numeric usage limits (only the ">5x" differential
  between Pro and Pro+ is given); pricing amounts; whether these restrictions
  apply to the github.com agent model selection interface (which requires
  Business/Enterprise — see `docs-github-copilot-agent-model-selection.md`).

## Extracted Claims

### Claim 1: New signups are paused for Copilot Pro, Pro+, and Student — only Free remains open for new users

- **Evidence**: Official GitHub product changelog stating the change explicitly.
  Existing subscribers are not affected; the pause applies only to new signups.
- **Confidence**: settled (product fact, stated in official changelog)
- **Quote**: "New signups paused for Pro, Pro+, and Student"
- **Our assessment**: This is the most disruptive claim for individual practitioners
  currently evaluating GitHub Copilot. A developer who reads about Pro or Pro+ as
  the recommended tier and tries to sign up will be blocked. The Free tier remains
  the only entry point for new individual users. For Ch01: update any workflow
  guidance that directs individual developers to sign up for Pro/Pro+ — those
  signup paths are currently closed. For Ch05: teams evaluating GitHub Copilot for
  individual developer seats cannot currently onboard new individuals onto Pro/Pro+.
  The practical recommendation while the pause is in effect: use Free (with its
  limits) or evaluate alternatives.

### Claim 2: Existing users retain the ability to upgrade between individual plans

- **Evidence**: Official changelog: "Existing users can still upgrade between
  plans." The signup pause applies to new accounts; existing subscribers are not
  locked into their current tier.
- **Confidence**: settled (stated directly)
- **Quote**: "Existing users can still upgrade between plans"
- **Our assessment**: The upgrade path surviving the pause mitigates one failure
  mode — Pro subscribers who need Opus 4.7 can still move to Pro+. The asymmetry
  (existing users can upgrade; new users cannot subscribe to paid plans) suggests
  the pause is a demand management measure rather than a permanent product change.
  For practitioners who already have Pro: upgrading to Pro+ to access Opus 4.7 is
  still possible while the pause is in effect.

### Claim 3: Pro+ offers more than 5× the usage limits of Pro — usage limits are now explicitly tiered between individual plans

- **Evidence**: Official changelog: "Pro+ offers more than 5X the limits of Pro."
  No specific numeric limits are provided — only the relative differential.
- **Confidence**: settled (ratio stated in official changelog, though specific
  limits are not published)
- **Quote**: "Pro+ offers more than 5X the limits of Pro"
- **Our assessment**: The 5x differential is concrete enough to make plan selection
  consequential. A practitioner on Pro who regularly hits limits faces a qualitative
  difference in headroom on Pro+, not a marginal one. The lack of published numeric
  limits is operationally frustrating — practitioners cannot pre-calculate which plan
  fits their usage without running into limits and observing. The guide should advise
  individual practitioners to track their usage during their first month on Pro and
  use limit proximity as the signal for whether Pro+ is warranted. For Ch01: the
  usage-limit gap between Pro and Pro+ is the primary plan-selection variable for
  individual users, not just Opus model access.

### Claim 4: Warning notifications will appear in VS Code and Copilot CLI as users approach usage limits

- **Evidence**: Official changelog describes this as a new transparency feature
  added alongside the limit tightening. The mechanism (in-tool notifications)
  is described but the specific threshold (e.g., 80% of limit) is not.
- **Confidence**: settled (stated feature in official changelog)
- **Quote**: (paraphrased from changelog: VS Code and Copilot CLI will show
  warning notifications as users approach limits)
- **Our assessment**: This is GitHub's response to the transparency problem that
  Cursor faced — billing/limit surprises from insufficient in-product signals.
  By surfacing limit proximity in the two primary interaction surfaces (VS Code
  and CLI), GitHub gives individual practitioners an early warning that Cursor
  did not provide (see `failure-cursor-pro-silent-billing-switch.md`). For Ch01:
  practitioners should not rely solely on these notifications, but their existence
  is a concrete improvement over the prior state. The warning also implies that
  hitting the limit without warning is no longer an expected failure mode on
  GitHub Copilot individual plans.

### Claim 5: Opus models have been removed from Copilot Pro — Pro subscribers can no longer access Opus-tier models

- **Evidence**: Official changelog stating Opus models are "removed from Copilot
  Pro." No qualifying language — this is a removal, not a deprecation notice.
- **Confidence**: settled (stated as a current change in official changelog)
- **Quote**: "Opus models removed from Copilot Pro"
- **Our assessment**: This is the highest-impact claim for individual practitioners
  who rely on Opus-tier reasoning (complex refactors, architecture analysis, long
  context tasks). Prior to this change, Copilot Pro could theoretically provide
  Opus access; that access is now gone. The practical implication: any workflow
  guidance that recommends Copilot Pro as sufficient for Opus-tier tasks is now
  outdated. For Ch01: practitioners who need Opus on GitHub Copilot must be on
  Pro+. For Ch05: when comparing GitHub Copilot individual plans against
  alternatives (Claude Code, Cursor Pro), the plan-tier constraint on Opus access
  is now a first-class evaluation criterion. Cross-reference with the CLI auto
  pool note: `docs-github-copilot-cli-auto-model-selection.md` already documented
  that the CLI auto pool excludes Opus (for cost-bounded routing); this new source
  confirms that Pro plan holders cannot access Opus even via explicit pinning.

### Claim 6: Opus 4.7 is available exclusively on Copilot Pro+, not on Pro

- **Evidence**: Official changelog: "Opus 4.7 remains available on Pro+." The
  framing "remains" implies Opus 4.7 was available on Pro+ previously; the
  companion removal (Claim 5) eliminates Opus from Pro entirely.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Opus 4.7 remains available on Pro+"
- **Our assessment**: Opus 4.7 is the highest-capability model in the Anthropic
  lineup as of this writing. Limiting it to Pro+ on individual plans establishes
  a clear capability floor: if a practitioner needs the most capable model for
  individual Copilot use, Pro+ is the only individual-plan path. For Ch01:
  document the model-tier access map (Free/Pro: no Opus; Pro+: Opus 4.7) as a
  plan-selection heuristic. Tasks that require deep reasoning, long context, or
  high-quality multi-file synthesis should be evaluated against the Pro+ price
  point, not assumed accessible on Pro.

### Claim 7: Opus 4.5 and 4.6 will be removed from Copilot Pro+ (announced deprecation)

- **Evidence**: Official changelog explicitly announces this as a future change.
  No deprecation date is given — the phrasing is "will be removed."
- **Confidence**: settled (announced intent; specific timing unconfirmed)
- **Quote**: "Opus 4.5 and 4.6 will also be removed from Pro+"
- **Our assessment**: This is a forward-looking constraint that narrows the Opus
  access footprint on individual plans even further. Once Opus 4.5 and 4.6 are
  removed from Pro+, Pro+ subscribers will have access only to Opus 4.7 among
  Opus-tier models — and if that too is ever removed, individual plans would have
  no Opus access at all. The trajectory is clear: GitHub is converging individual
  plan model access toward lower-cost model tiers. Practitioners who depend on
  specific Opus generation features (e.g., tasks that perform better on 4.6 than
  4.7) should note this deprecation. For the guide: cite this as evidence that
  individual-plan model access on GitHub Copilot is actively narrowing — teams
  should not design workflows that depend on a specific Opus version being
  available on individual plans.

### Claim 8: GitHub explicitly frames the changes as a service reliability measure

- **Evidence**: Official changelog states the changes are made "to ensure service
  reliability and a sustainable Copilot experience for all users" and "to
  prioritize service quality for existing paying customers."
- **Confidence**: settled (stated rationale; vendor framing)
- **Quote**: "to ensure service reliability and a sustainable Copilot experience
  for all users"; "to prioritize service quality for existing paying customers"
- **Our assessment**: The reliability rationale is vendor framing, but it is
  informative vendor framing. GitHub is explicitly trading off individual-plan
  capability (Opus access, broad signup) against service quality for existing
  subscribers. This signals that individual Copilot plan limits are not fixed
  technical ceilings but tunable operating parameters — GitHub has demonstrated
  willingness to tighten them in response to demand pressure. For Ch05: when
  advising teams on individual-plan adoption, note that plan capabilities are
  subject to adjustment for service reliability reasons; what is available today
  (Opus 4.7 on Pro+) may not be available tomorrow (as with Opus 4.5/4.6
  deprecation). Teams building workflows that depend on specific individual-plan
  capabilities should monitor GitHub's changelog.

### Claim 9: A full refund of April charges is available for users who cancel Pro or Pro+ between April 20 and May 20, 2026

- **Evidence**: Official changelog describes a specific refund window and support
  contact mechanism.
- **Confidence**: settled (specific terms stated in official changelog, time-bounded)
- **Quote**: (paraphrased: users who cancel between April 20–May 20 may request
  a full April refund via GitHub support)
- **Our assessment**: The refund window acknowledges that the plan changes
  (particularly Opus removal from Pro) may render Pro less valuable for some
  existing subscribers. The explicit refund path — rather than a silent change
  with no recourse — is a transparency practice the guide can contrast against
  the Cursor billing failures (see `failure-cursor-pro-silent-billing-switch.md`
  and `failure-cursor-ultra-billing-cache-exploration.md`). GitHub is providing
  explicit consent and exit options alongside the plan changes. This is the
  positive pattern the guide should hold up when discussing vendor billing
  transparency practices.

## Concrete Artifacts

### Individual Copilot Plan Model Access Map (as of April 20, 2026)

```
GitHub Copilot — Individual Plans — Opus Model Access

FREE:
  Opus models:    NOT available
  Signup:         Open for new users

PRO ($10/month):
  Opus models:    REMOVED (as of April 20, 2026)
  Signup:         Paused for new signups (existing users can remain/upgrade)

PRO+:
  Opus 4.7:       Available (confirmed)
  Opus 4.5/4.6:   Available now; WILL BE REMOVED (date unannounced)
  Signup:         Paused for new signups (existing users can remain/upgrade)

STUDENT:
  Signup:         Paused for new signups

Note: Business and Enterprise plan model access is NOT affected by this changelog.
      See docs-github-copilot-agent-model-selection.md for Business/Enterprise
      model selection (Opus 4.5 and 4.6 available as of April 14, 2026).
```

### Usage Limit Differential

```
GitHub Copilot Individual Plans — Usage Limits

PRO:     [base limit]
PRO+:    >5× the Pro limit (exact numbers not published)

Notifications:
  → VS Code: warning shown as user approaches limit
  → Copilot CLI: warning shown as user approaches limit
  (Threshold for warning not specified in changelog)
```

### Refund Window

```
Eligibility:    Existing Copilot Pro or Pro+ subscribers
Action:         Cancel plan AND contact GitHub support
Window:         April 20, 2026 – May 20, 2026
Refund scope:   Full refund of April charges
Contact:        GitHub support system
```

### Plan Selection Heuristic for Individual Practitioners

```
Need Opus 4.7?
  → Pro+ only (new signups currently paused; existing users can upgrade)
  → Free / Pro: cannot access Opus

Need Opus 4.5 or 4.6?
  → Pro+ (while still available — announced for future removal)
  → Timebox this dependency: watch GitHub changelog for removal date

Usage-limited on Pro?
  → Pro+ offers >5× the headroom
  → Decision signal: watch VS Code / CLI limit warnings

New to GitHub Copilot?
  → Only Free is open for new signups currently
  → Evaluate whether Free limits meet your workflow before committing
```

## Cross-References

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` (issue #203):
  That source documented (April 17, 2026) that the CLI auto pool deliberately
  excludes Opus-tier models (pool capped at 0x–1x multipliers). This source
  (April 20, 2026) confirms that exclusion by removing Opus from Pro entirely —
  the two sources together show a consistent GitHub policy direction: Opus-tier
  access is being actively narrowed on individual plans and routing mechanisms
  alike. The CLI auto note explains the routing mechanism; this note explains
  the plan-level entitlement. Both point to the same operational conclusion:
  individual practitioners who need Opus must pay for Pro+ and use explicit
  model selection, not rely on routing or Pro subscription defaults.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 2
  (auto routing is cost/availability-driven, not capability-driven): The plan
  restriction rationale ("service reliability and a sustainable Copilot
  experience") echoes the cost-bounded routing rationale for the CLI auto pool.
  Both reveal the same underlying GitHub optimization objective: maximize service
  availability across the user base by constraining access to high-cost models
  at the individual tier.

- **Extends** `docs-github-copilot-agent-model-selection.md` (issue #171):
  That source documented Opus 4.5 and 4.6 as available for Claude agents on
  github.com for Business/Enterprise subscribers (as of April 14, 2026). This
  source introduces an important boundary condition: those Opus versions are
  being removed from Pro+ (individual plans). The two sources together define
  the plan-tier boundary for Opus access: Business/Enterprise subscribers retain
  Opus 4.5/4.6 via agent model selection; individual Pro+ subscribers are on a
  deprecation path. No contradiction — different subscription tiers with different
  access policies.

- **Contrasts** `failure-cursor-pro-silent-billing-switch.md` (issue #58):
  The Cursor Pro failure documented silent billing-mode switching with no
  in-product warning, no explicit refund offer, and support explanations that
  didn't reconcile with actual charges. This GitHub changelog documents the
  opposite: explicit in-product limit warnings (VS Code + CLI notifications),
  an explicit refund window with direct support contact, and a clear changelog
  announcement. GitHub is exhibiting the transparency practices that were absent
  in the Cursor failure. For Ch01 and Ch05: use this contrast as a vendor
  evaluation criterion — when assessing an AI coding tool, check whether
  the vendor communicates plan changes transparently and provides explicit
  recourse. GitHub's approach here is the positive pattern.

- **Complements** `failure-cursor-ultra-billing-cache-explosion.md` (issue #75):
  The Cursor Ultra failure showed that "unlimited" plan tiers have soft billing
  ceilings that can be exceeded via underlying API costs. This GitHub source
  shows that even explicit usage limits are tunable parameters that vendors
  adjust for service reliability. Both reinforce the same guide principle:
  individual plan capabilities (model access, usage limits, pricing) are
  subject to change based on vendor operating conditions, and practitioners
  should not build workflows that assume a specific individual-plan capability
  floor without monitoring vendor changelogs.

- **Novel**:
  - First source in corpus to document a plan-tier Opus access map for GitHub
    Copilot individual plans specifically (Free and Pro have no Opus; Pro+ has
    Opus 4.7, with 4.5/4.6 on deprecation path).
  - First documentation of a new-signup pause on individual Copilot paid plans —
    no prior corpus source treats plan enrollment availability as a constraint
    in AI tool adoption guidance.
  - First source to document in-product usage-limit warnings in VS Code and
    Copilot CLI as a transparency mechanism, contrasting with the absence of
    such warnings in the Cursor billing failure cases.
  - First positive-pattern example in corpus of a vendor explicitly coupling
    a capability reduction with a refund window and transparent changelog
    announcement — a vendor behavior model for the guide to reference.

## Guide Impact

### Chapter 01: Daily Workflows / Tool Setup and Configuration

- **Plan selection for individual Copilot users**: Add a plan-tier model access
  table. Individual practitioners who need Opus-tier reasoning on GitHub Copilot
  must be on Pro+ (not Pro, not Free). Document the new signup pause: as of April
  20, 2026, new accounts cannot sign up for Pro or Pro+; Free is the only entry
  point. Practitioners currently on Pro who need Opus must upgrade to Pro+.
- **Usage monitoring**: Note that VS Code and Copilot CLI now surface limit
  proximity warnings. Recommend practitioners pay attention to these signals and
  track whether Pro limits are sufficient for their workflow before investing in
  Pro+ upgrade.
- **Billing transparency as a workflow practice**: Use the GitHub refund window
  (April 20–May 20, 2026) as a positive example of the vendor behavior
  practitioners should expect and look for. Contrast with the Cursor Pro silent
  billing switch (no warning, no refund offer). Add this to any vendor evaluation
  rubric in the guide.

### Chapter 05: Team Adoption / Tool Evaluation

- **Individual vs. Enterprise plan access differences**: When teams evaluate
  GitHub Copilot for individual developers, document that individual plans
  (Pro/Pro+) have different model access than Business/Enterprise plans. Opus
  model availability is converging toward Enterprise-only over time: Opus is
  removed from Pro, Opus 4.5/4.6 deprecated on Pro+, only Opus 4.7 remains on
  Pro+. Teams advising developers to "use GitHub Copilot" should specify which
  plan tier and confirm Opus access requirements match the plan tier.
- **Plan capability stability**: Add guidance that individual-plan capabilities
  on GitHub Copilot are adjustable by GitHub based on service reliability
  constraints — as this changelog demonstrates. Teams building workflows that
  depend on specific model availability on individual plans should treat the
  GitHub changelog as a required monitoring source, not a set-and-forget
  configuration.
- **Vendor comparison criterion**: Add "how does the vendor handle plan changes?"
  as an explicit tool evaluation criterion for team adoption decisions. GitHub's
  approach (changelog + in-product warnings + explicit refund window) is the
  positive baseline. Any vendor evaluation should ask: if this vendor restricts
  access to a model tier we depend on, will we get explicit notice and recourse?

## Extraction Notes

1. **Source is a short changelog**: Approximately 400 words. All substantive
   claims are exhausted in nine items above. No linked sub-pages — the changelog
   is self-contained.
2. **Numeric limits not published**: The ">5×" differential between Pro and Pro+
   usage limits is the only quantitative claim. GitHub has not published the
   absolute limit values. Any guide content that cites specific limits must
   derive those numbers from a different source.
3. **Business/Enterprise plans not affected**: This changelog is explicitly
   scoped to individual plans. The Opus model access changes documented here
   do not apply to Business or Enterprise subscriptions. Care was taken in
   extraction to maintain this boundary — see the model access artifact and
   the `docs-github-copilot-agent-model-selection.md` cross-reference.
4. **Signup pause may be temporary**: The changelog does not characterize the
   signup pause as permanent. It may be a capacity management measure. The
   guide should present this as a current constraint (as of April 20, 2026)
   rather than a permanent product direction.
5. **No contradictions to file**: The Opus model removal from Pro is new
   information that narrows the scope of individual-plan Opus access. It does
   not contradict any existing source note — prior notes either covered
   Business/Enterprise model access (which is unaffected) or the CLI auto
   pool (which already excluded Opus). No contradiction issue required.
6. **Refund window is time-bounded**: The April 20–May 20, 2026 refund window
   will have passed by the time the guide cites this source. Guide content
   should reference the existence of the refund policy as a transparency
   behavior example, not the specific dates, which will no longer be actionable.
