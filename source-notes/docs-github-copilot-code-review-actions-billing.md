---
source_url: https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026
source_type: docs
title: "GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026"
author: GitHub (official changelog)
date_published: 2026-04-27
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: settled
issue: "#445"
---

# GitHub Copilot Code Review Will Start Consuming GitHub Actions Minutes on June 1, 2026

> GitHub's April 27, 2026 changelog announcing that Copilot code review will
> shift from PRU-only billing to dual billing (AI Credits + GitHub Actions minutes
> for private repos) on June 1, 2026 — establishing that the agentic architecture
> behind code review is the direct cause of the new Actions consumption, and that
> this is a material cost variable teams must account for in GitHub Copilot TCO.

## Source Context

- **Type**: docs (GitHub official product changelog, ~400 words, April 27, 2026)
- **Author credibility**: GitHub engineering team announcing a production billing change.
  Authoritative for the fact that this change exists, its effective date, which plans
  are affected, and what the preparation steps are. Published 35 days before the effective
  date — an unusually generous notice period by vendor changelog standards.
- **Scope**: Covers the billing change for Copilot code review only — not Copilot chat,
  Copilot completions, or any other Copilot feature. Affects private repositories only;
  public repos are explicitly excluded. Applies to all paid Copilot plan tiers (Pro,
  Pro+, Business, Enterprise). Does NOT cover: the AI Credits billing model itself
  (a separate "usage-based billing announcement" is referenced), specific Actions minute
  consumption rates per review, or the effect on free plan Copilot users (not mentioned).

## Extracted Claims

### Claim 1: Starting June 1, 2026, each Copilot code review on a private repository will be billed in two ways: as AI Credits and as GitHub Actions minutes

- **Evidence**: Official product changelog announcing the specific change, mechanism,
  and date.
- **Confidence**: settled (specific billing change stated in official changelog)
- **Quote**: "Starting June 1, 2026, each Copilot code review will be billed in two
  ways: All Copilot usage (including code reviews) will be billed as AI Credits under
  the new usage-based billing model ... GitHub Actions minutes will be consumed from
  your existing plan entitlement for each review that is run on private repositories,
  with any usage beyond your included minutes billed at standard GitHub Actions rates."
- **Our assessment**: This is the core billing change and the highest-impact claim for
  teams calculating GitHub Copilot TCO. Prior to June 1, Copilot code review drew only
  from the PRU allowance. After June 1, the same review also draws from Actions minutes.
  For teams with high PR volume on private repos, this doubles the billing-dimension
  surface of the code review feature: they must now track both AI Credits and Actions
  minutes, with independent overage mechanisms for each. For Ch05: this is a first-class
  TCO variable when evaluating or re-evaluating GitHub Copilot for team adoption.

### Claim 2: The agentic tool-calling architecture underlying Copilot code review — which runs on GitHub Actions — is the direct cause of the new Actions minute consumption

- **Evidence**: The changelog explicitly explains the causal link: "Last month, we shared
  how GitHub Copilot code review runs on agentic tool-calling architecture, allowing the
  code review agent to pull in broader repository context and produce more relevant
  feedback on each pull request. That agentic architecture runs on GitHub Actions using
  GitHub-hosted runners."
- **Confidence**: settled (causal mechanism stated explicitly by GitHub)
- **Quote**: "That agentic architecture runs on GitHub Actions using GitHub-hosted runners"
- **Our assessment**: This is the architectural explanation for *why* Actions minutes are
  now consumed. Code review is not a simple model API call — it is a multi-step agentic
  workflow that uses GitHub Actions infrastructure. The billing change is GitHub aligning
  the economic model with the actual infrastructure cost. For Ch02 (Harness Engineering):
  this is a concrete real-world example of agentic features consuming Actions infrastructure
  and the billing implications. Teams building their own agentic workflows on GitHub Actions
  face the same dynamic: agentic execution on GitHub-hosted runners consumes Actions minutes.
  The code review billing change is the same mechanism made visible for Copilot users.

### Claim 3: Until June 1, 2026, Copilot code review draws only from the Copilot premium request unit (PRU) allowance and does not consume GitHub Actions minutes

- **Evidence**: Changelog section "When it takes effect" explicitly states the current
  billing model as context for the change.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Until that day, Copilot code review usage will continue to draw only from
  your existing Copilot premium request unit (PRU) allowance and will not consume GitHub
  Actions minutes."
- **Our assessment**: The PRU-to-dual-billing transition is a meaningful discontinuity.
  Teams that have modeled Copilot code review costs entirely in terms of PRU consumption
  will need to add Actions minutes to their model. The transition date (June 1, 2026) is
  the relevant planning horizon — not a future announcement to monitor, but a confirmed
  date. For guide content: present the pre/post June 1 billing model as a factual contrast,
  not as an uncertainty.

### Claim 4: The billing change affects all paid GitHub Copilot plans: Pro, Pro+, Business, and Enterprise — including code reviews from non-licensed users billed via direct org billing

- **Evidence**: Changelog enumerates affected plans explicitly.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "This change applies to the following plans: GitHub Copilot Pro / GitHub
  Copilot Pro+ / GitHub Copilot Business / GitHub Copilot Enterprise / This includes
  Copilot code reviews from non-licensed users and billed via direct org billing."
- **Our assessment**: The "non-licensed users billed via direct org billing" clause is
  particularly significant for Business and Enterprise customers: it confirms the billing
  change applies even when individual contributor seats are not separately licensed, as long
  as the org is using direct billing for those reviews. Teams assuming that only fully-licensed
  seats trigger Actions consumption will be wrong for this subset of usage. For Ch05: when
  calculating expected Actions minute usage, org admins need to account for the full pool
  of contributors whose code review triggers Copilot — not just those with individual Copilot
  seat licenses.

### Claim 5: Public repositories are entirely unaffected — Actions minutes remain free for code reviews on public repositories

- **Evidence**: Changelog explicitly carves out public repos.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "There are no changes to public repositories, where Actions minutes remain free."
- **Our assessment**: The public repo exception is consequential for open-source
  maintainers and teams with mixed public/private repository portfolios. If a team's
  primary use of Copilot code review is on public repos, this billing change does not
  affect them at all. For Ch05: the public/private distinction should be the first
  filter when advising teams on TCO impact — teams with only public repos have zero
  exposure to this change.

### Claim 6: GitHub Copilot code review supports self-hosted runners and larger GitHub-hosted runners, which are billed at different rates than standard GitHub-hosted runners

- **Evidence**: Parenthetical note in the changelog's technical explanation of the
  agentic architecture.
- **Confidence**: settled (stated in official changelog, though specific rate differences
  are not quantified here)
- **Quote**: "GitHub Copilot code review also supports self-hosted runners and GitHub-hosted
  larger runners which are billed at different rates than standard GitHub-hosted runners."
- **Our assessment**: This is an important cost lever for teams with existing runner
  infrastructure. A team that already runs self-hosted runners for CI/CD can potentially
  route Copilot code reviews through those runners — either absorbing the cost into existing
  infrastructure or optimizing the per-minute rate. The changelog does not quantify the rate
  difference; teams would need to consult the GitHub pricing documentation for specific
  figures. For Ch05: runner configuration is a first-class cost optimization variable for
  teams with heavy Copilot code review usage on private repos.

### Claim 7: Teams and Enterprise organizations can use spending limit budgets to manage GitHub Actions overage from Copilot code reviews

- **Evidence**: Changelog both mentions budget controls in the "What's changing" section
  and recommends reviewing spending limits in the "What you need to do" section.
- **Confidence**: settled (stated in official changelog; GitHub Actions spending limits
  are an existing product feature)
- **Quote**: "You or your organization administrator (for GitHub Teams and Enterprise) can
  use budgets to manage spending on GitHub Actions."
- **Our assessment**: Spending limits are the primary guard against unbounded Actions
  overage. Teams that set a $0 overage limit will stop incurring charges once their
  included minutes are exhausted — but code reviews will also stop running. The changelog
  does not describe what happens to queued reviews when the spending limit is hit (whether
  they fail, queue, or are silently skipped). This is operationally important: teams
  should verify the limit-hit behavior before June 1 to avoid a silent degradation of
  code review coverage. For Ch05: recommend teams establish an explicit Actions spending
  policy that accounts for Copilot code review volume alongside CI/CD usage.

### Claim 8: GitHub explicitly provided 35 days' advance notice of the billing change to give teams planning and preparation time

- **Evidence**: The changelog was published April 27, 2026 for a change effective June 1,
  2026 — 35 days in advance. The introduction frames this explicitly.
- **Confidence**: settled (the notice period is a factual observation from publication
  and effective dates)
- **Quote**: "We understand that any change is significant to our customers, especially
  when it relates to billing, so we are sharing this update early to help you plan and
  prepare."
- **Our assessment**: The 35-day notice is a vendor transparency practice worth noting
  explicitly. It contrasts with silent billing-mode changes (see `failure-cursor-pro-silent-billing-switch.md`)
  where users discovered billing mode changes after incurring charges. GitHub's advance
  notice pattern — consistent across this changelog and the April 20 plan change (see
  `docs-github-copilot-individual-plan-changes.md` Claim 8) — establishes that GitHub
  treats billing changes as communications events requiring lead time. For Ch05: when
  evaluating vendor billing practices as a team adoption criterion, advance notice of
  billing changes is the observable signal — and GitHub has now provided it twice in
  consecutive months.

### Claim 9: GitHub recommends teams monitor Copilot usage metrics, GitHub Actions metrics, and the Billing Usage Report as the three-source observability suite for managing the new dual billing

- **Evidence**: Changelog "What you need to do" section enumerates these three tools
  explicitly.
- **Confidence**: settled (product tools stated in official changelog)
- **Quote**: "Monitor your Copilot and Actions usage over time via GitHub Copilot usage
  metrics, GitHub Actions metrics, and Billing Usage Report."
- **Our assessment**: The three-source monitoring recommendation is actionable and
  immediately applicable. For teams that currently use the Copilot usage metrics API
  for code review tracking (see `docs-github-copilot-pr-review-metrics.md`), the new
  dual billing adds GitHub Actions metrics as a parallel data stream to watch. The Billing
  Usage Report is the reconciliation layer — it should be the source of truth when
  Copilot metrics and Actions metrics diverge. For Ch05: add this three-source monitoring
  suite to any GitHub Copilot TCO playbook.

## Concrete Artifacts

### Billing Change Summary (from changelog)

```
GitHub Copilot Code Review Billing Model

BEFORE June 1, 2026:
  Code review billing: Copilot premium request unit (PRU) allowance only
  Actions minutes:     NOT consumed by code reviews

AFTER June 1, 2026:
  Code review billing: TWO dimensions simultaneously —
    1. AI Credits       → billed under Copilot usage-based billing model
    2. Actions minutes  → consumed from plan entitlement (private repos only)
                          Overages billed at standard GitHub Actions rates

Public repositories: UNCHANGED — Actions minutes remain free

Affected plans: Pro, Pro+, Business, Enterprise
                (incl. non-licensed users via direct org billing)
```

### Runner Configuration Options for Code Review

```
Standard GitHub-hosted runners:
  → Default; enabled by default on most repos
  → Actions minutes consumed at standard rates
  → No additional setup required

Larger GitHub-hosted runners:
  → Upgrade path via "Upgrade to larger GitHub-hosted Runners"
  → Billed at different (higher) rates than standard runners
  → Use case: performance customization needs

Self-hosted runners:
  → Available for Copilot code review
  → Billed at different rates (potentially absorbed into existing infra)
  → Use case: teams with existing runner infrastructure seeking cost optimization
```

### Recommended Preparation Checklist (from changelog "What you need to do")

```
1. Review billing and usage:
   □ Review current GitHub Actions usage (billing managers: billing settings)
   □ Check and confirm spending limit budgets align with expected usage
   □ Adjust spending limits for GitHub Actions if needed
   □ Monitor Copilot usage metrics + Actions metrics + Billing Usage Report
   □ Review usage-based billing announcement for AI Credits model
   □ Share update with billing administrators and engineering leads before June 1

2. Review runner settings:
   □ Verify GitHub-hosted Runners are enabled on relevant repos (no setup
     required if already enabled)
   □ Decide on runner configuration: standard, larger, or self-hosted
   □ Review documentation for self-hosted runner setup if applicable
```

## Cross-References

- **Corroborates** `docs-github-copilot-individual-plan-changes.md` Claim 8
  ("GitHub explicitly frames the changes as a service reliability measure"):
  Both changelogs show a consistent GitHub pattern of providing explicit advance
  communication for billing-affecting changes. The April 20 plan change gave a
  clear refund window; this April 27 billing change gives 35 days of advance
  notice. Together they establish a vendor behavior pattern: GitHub treats billing
  changes as requiring proactive communication with lead time and explicit user
  actions. For Ch05: cite both as evidence of the positive transparency pattern.

- **Extends** `docs-github-copilot-pr-review-metrics.md` (issue #91) in two ways:
  (1) That note documented the Copilot usage metrics API as the measurement tool
  for code review adoption (Claim 1: `total_merged_reviewed_by_copilot`,
  `median_minutes_to_merge_copilot_reviewed`). This source adds a new measurement
  obligation: those same reviews now consume Actions minutes, meaning teams need
  the Actions metrics data alongside the Copilot metrics. The measurement arc is
  no longer Copilot-only.
  (2) That note's Claim 6 flagged that the "Copilot review helps" framing in the
  April 8 changelog was an undemonstrated hypothesis. This billing change implicitly
  raises the stakes of that hypothesis: if Copilot review does not demonstrably
  improve outcomes, teams now have a concrete cost reason to reduce review frequency
  (to avoid consuming Actions minutes). The billing change makes the ROI question
  a TCO question.

- **Contrasts with** `failure-cursor-pro-silent-billing-switch.md` (issue #58) as a
  positive counter-example: That report documented Cursor silently enrolling a Pro
  subscriber in per-token billing with no advance notice, misleading UI terminology
  ("On-Demand usage"), and a support explanation that didn't reconcile with the actual
  invoice. This GitHub changelog is the structural opposite: 35 days of advance notice,
  explicit billing mechanism explanation, actionable preparation checklist, and a clear
  description of what changes and what does not. For Ch05: use this pairing as a vendor
  evaluation criterion — "how does this vendor handle billing changes?" GitHub's approach
  here (explicit, early, with specific preparation steps) is the pattern to look for.

- **Complements** `docs-github-copilot-individual-plan-changes.md` (issue #289):
  The Prospector correctly identified these as distinct sources. The April 20 plan
  change affected individual-plan model access (which Opus tier per plan) and signup
  availability. This April 27 change affects a specific feature's billing mechanism
  across all paid plans. Together they document a pattern: in consecutive months, GitHub
  made meaningful changes to both the model access tier and the billing mechanics of
  GitHub Copilot. For Ch05: teams should monitor the GitHub changelog as a routine
  practice, not an occasional check — two consecutive months of material billing/access
  changes confirms that the changelog is an active communication channel.

- **Novel**:
  - First source in corpus to document that Copilot code review consumes GitHub Actions
    minutes specifically — and to establish the causal link: the agentic architecture
    is built on GitHub Actions infrastructure.
  - First source to document the PRU → dual billing (AI Credits + Actions minutes)
    transition for any Copilot feature. Prior billing sources focused on plan tier
    access and request unit allowances, not infrastructure-level consumption.
  - First source to document runner configuration (standard, larger, self-hosted) as
    a cost optimization variable for Copilot usage specifically.
  - First source to establish "non-licensed users billed via direct org billing" as
    an explicit Actions minute consumption category — a coverage gap in assumptions
    based on "licensed seat" counts alone.

## Guide Impact

### Chapter 05: Team Adoption / Tool Evaluation

- **TCO model for GitHub Copilot code review**: Any team-adoption cost model for GitHub
  Copilot that includes the code review feature must now include a GitHub Actions minutes
  estimate for private-repo reviews, effective June 1, 2026. The prior model (PRU
  allowance only) is no longer accurate. Add a "code review cost component" that factors
  in: (a) estimated reviews per month on private repos, (b) runner type (standard,
  larger, self-hosted), (c) existing Actions minute entitlement and current consumption,
  (d) overage rate if consumption exceeds entitlement. Without this update, TCO estimates
  for teams with heavy private-repo PR volume will understate Copilot cost.
- **Vendor billing communication as evaluation criterion**: Add GitHub's 35-day
  advance notice (this changelog) and the April 20 refund window (see
  `docs-github-copilot-individual-plan-changes.md`) as examples of the vendor billing
  transparency pattern teams should look for when evaluating any AI tool. Contrast with
  `failure-cursor-pro-silent-billing-switch.md`. The evaluation question: if this vendor
  changes billing, will we get explicit advance notice with time to act?
- **Monitoring suite for Copilot TCO**: After June 1, the minimum monitoring suite for
  GitHub Copilot cost governance is three sources: Copilot usage metrics (AI Credits),
  GitHub Actions metrics (minutes consumed), and Billing Usage Report (reconciliation).
  The April 8 changelog (`docs-github-copilot-pr-review-metrics.md`) established
  Copilot usage metrics as the starting point; this changelog adds Actions metrics as
  a required parallel stream.

### Chapter 01: Daily Workflows / Tool Setup and Configuration

- **Copilot code review usage awareness**: Individual practitioners and team leads who
  use Copilot code review on private repos should check their organization's GitHub
  Actions minute entitlement and current consumption before June 1, 2026. A team
  already near its Actions minute ceiling from CI/CD workloads may see unexpected
  overage once Copilot code reviews start consuming minutes. The recommendation: check
  the billing settings before June 1, not after.
- **Public vs. private repo distinction**: Engineers who contribute primarily to public
  repos do not need to adjust their Copilot code review usage — Actions minutes remain
  free for public repos. Document this as a workflow context: the billing change is
  conditional on repository visibility.

### Chapter 02: Harness Engineering

- **Agentic features consume Actions infrastructure**: The causal explanation in this
  changelog (Claim 2) is directly instructive for harness engineers: agentic tool-calling
  workflows built on GitHub Actions consume Actions minutes. Copilot code review is a
  production example of exactly this pattern. Teams building their own agentic harnesses
  on GitHub Actions face the same billing dimension. For Ch02: reference this as a
  real-world case where an agentic feature's infrastructure consumption (GitHub Actions)
  became a billing consideration distinct from the AI model consumption.

## Extraction Notes

1. **Source is a short changelog**: Approximately 400 words across three sections
   (What's changing, When it takes effect, What you need to do). All substantive claims
   are exhausted in nine items above. The source is self-contained with no linked
   sub-pages — linked references point to the usage-based billing announcement (a
   separate source), runner upgrade documentation, and GitHub Community discussion.
2. **Specific Actions minute consumption rate not provided**: The changelog does not
   quantify how many Actions minutes one Copilot code review consumes. This is a
   meaningful gap for cost modeling — teams must measure their own consumption after
   June 1 or wait for GitHub to publish per-review benchmarks. Any guide content
   citing specific per-review minute counts would need a different source.
3. **AI Credits billing model referenced but not explained**: The changelog references
   "the usage-based billing announcement" for details on AI Credits. That announcement
   is a separate source; this source note does not attempt to synthesize it. The AI
   Credits dimension of the dual billing is noted here as a fact, not analyzed in depth.
4. **WebFetch limitations**: WebFetch returned summaries rather than verbatim text.
   All quotes above were validated against the full HTML-stripped text obtained via
   curl and Python HTML parsing. Quotes are character-for-character from that parse.
5. **No contradictions to file**: No existing source note claims that Copilot code
   review does not consume Actions minutes, or that the billing model for code review
   is PRU-only in perpetuity. The new billing model extends the prior model rather
   than contradicting any existing claim. No contradiction issue is warranted.
