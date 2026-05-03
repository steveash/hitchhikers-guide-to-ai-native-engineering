---
source_url: https://github.github.com/gh-aw/guides/organization-practices/safe-rollout
source_type: docs
title: "GitHub Agentic Workflows: Safe Rollout Guide"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-03
last_checked: 2026-05-03
status: current
confidence_overall: emerging
issue: "#481"
---

# GitHub Agentic Workflows: Safe Rollout Guide

> The definitive gh-aw framework for escalating agentic workflow autonomy
> incrementally — documents a four-rung rollout ladder (report-only →
> staged → shadow evaluation → production writes), a precise distinction
> between staged and shadow evaluation as answers to different questions,
> and four design rules that prevent evaluation infrastructure from
> corrupting production truth.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, in the
  `guides/organization-practices/` section — practitioner guidance for
  deploying gh-aw workflows safely in organizations, distinct from the
  conceptual `introduction/` pages and the structural `patterns/` section)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (the same team behind Peli de Halleux / Don Syme's agent factory series).
  This is authoritative practitioner guidance for the `gh aw` platform. The
  design rules and rollout ladder represent operational distillations from
  running 183+ production workflows. Claims about the platform's Safe Outputs
  and staged mode are settled; the design rules are strong practitioner
  recommendations, not platform constraints.
- **Scope**: The safe rollout guide covers: the four-rung autonomy-promotion
  ladder, criteria for choosing staged mode vs. shadow evaluation, four design
  rules governing rollout infrastructure hygiene, and a common three-repository
  shape for rollout. Does NOT cover: the full Safe Outputs permission model (see
  `docs-ghaw-how-they-work.md`), the `staged` Safe Output YAML syntax in
  detail (see the Staged Mode reference linked from this page), individual
  pattern pages such as SideRepoOps or MultiRepoOps, or performance/cost
  benchmarks for different rollout strategies.

## Extracted Claims

### Claim 1: Safe rollout is a trust-promotion framework for escalating workflow autonomy incrementally rather than enabling production writes immediately

- **Evidence**: The page opens with a framing that positions safe rollout as an
  epistemological question, not a deployment question: the central concern is
  whether a workflow is *trusted enough* to act on the live system, not merely
  whether it is useful.
- **Confidence**: emerging (first-party practitioner guidance from the team
  running 183+ production workflows; positions a named methodology without
  external validation)
- **Quote**: "Safe rollout is the practice of increasing workflow autonomy in
  steps instead of enabling direct production writes immediately."
- **Our assessment**: This framing — trust as the gate, not utility — is the
  right inversion. Most teams ask "is this automation good enough?" when they
  should ask "have we established enough evidence of correct behavior on safe
  targets to trust it with production?" The ladder operationalizes the second
  question. The framing also implies that direct production writes are a
  *destination*, not a default starting point — which contrasts with how most
  CI/CD automation is deployed (direct access first, restrict later). For Ch03
  (Safety and Verification): add this framing as the recommended starting
  posture for any new agentic workflow.

### Claim 2: The four-rung rollout ladder — report-only, staged, shadow evaluation, direct production writes — is the standard autonomy-promotion sequence for gh-aw workflows

- **Evidence**: The page presents this as "the usual progression" with four
  named rungs in a specific order. The ordering is deliberate: each rung
  addresses a different risk type and requires a different trust threshold.
- **Confidence**: emerging (first-party documentation; "usual" leaves room for
  exceptions; no quantitative adoption data is provided)
- **Quote**: "The usual progression is: 1. Start in report-only mode. 2. Enable
  `staged` behavior when proposed writes need to be previewed. 3. Use shadow
  evaluation when preview mode is not enough and the real write path needs to
  be exercised safely. 4. Promote the same workflow to direct production writes."
- **Our assessment**: The ladder is the central artifact of this page and the
  most extractable pattern in the GHAW corpus for autonomy promotion. The
  key insight is that rungs 2 and 3 are not alternatives — they are sequential
  escalation levels addressing different risk types. Teams that jump from
  report-only to direct production writes are skipping the two intermediate
  validation surfaces that provide the evidence needed for that promotion. For
  Ch03 and Ch05: the ladder provides a concrete adoption sequence that teams
  can commit to ("start in report-only") without requiring upfront trust in
  the automation.

### Claim 3: Staged and shadow evaluation address different questions and are not interchangeable: staged asks "what would the workflow do?" while shadow evaluation asks "does the real write path behave correctly?"

- **Evidence**: The page states the non-interchangeability explicitly and then
  defines the distinct question each mode answers. The distinction between
  "decision quality" (staged) and "operational behavior" (shadow) is the
  load-bearing insight of the page.
- **Confidence**: settled (first-party documentation with an explicit
  definitional distinction between two named platform features)
- **Quote**: "`staged` and shadow evaluation are not interchangeable. Staged
  mode is sufficient when the question is what the workflow would do. Shadow
  evaluation is needed when the question is whether the real write path behaves
  correctly on a safe non-production target."
- **Our assessment**: This is the most precise claim in the source and the
  most actionable for practitioners. Teams often conflate the two techniques
  because both are "non-production" modes. The page makes clear they answer
  different questions and prevent different failure modes: staged = preventing
  wrong decisions from reaching production; shadow = validating that the
  execution machinery (permissions, concurrency, cross-repo dispatch) works
  before granting live access. Understanding this distinction determines which
  rung of the ladder a team needs before promoting to production writes.

### Claim 4: Staged mode is sufficient when the main risk is decision quality — whether the workflow's judgment is reasonable before any write is allowed

- **Evidence**: The page defines a positive condition for staged mode sufficiency
  tied to what maintainers need to evaluate: proposed actions, alternatives, and
  judgment quality. No write has occurred; only intent has been expressed.
- **Confidence**: emerging (practitioner recommendation backed by platform design;
  "sufficient" implies a judgment call, not a mechanical rule)
- **Quote**: "Use staged mode when the main risk is decision quality rather than
  operational behavior."
- **Our assessment**: Staged mode is appropriate for the large class of workflows
  where the failure mode is "wrong action proposed" rather than "correct action
  proposed but broken execution path." Example: a release-version bumper that
  proposes incorrect SemVer increments. Staged mode lets maintainers review the
  proposed bump before any PR is opened. It does not help if the bump is correct
  but the PR-creation step has concurrency bugs — that requires shadow evaluation.
  For Ch02 (Harness Engineering): staged mode is the standard harness feature for
  decision-quality validation before production writes.

### Claim 5: Shadow evaluation is needed when staged mode is too weak because the real write path itself requires live-like validation

- **Evidence**: The page provides a precise negative condition ("when staged mode
  is too weak") and four specific sub-conditions that signal shadow evaluation
  is appropriate — each tied to a class of operational behavior that staged mode
  cannot surface.
- **Confidence**: emerging (first-party practitioner guidance; the four conditions
  are concrete but their completeness is not formally proven)
- **Quote**: "Use shadow evaluation when staged mode is too weak because the real
  write path itself needs validation."
- **Our assessment**: The four conditions make this actionable: (1) "the workflow
  must update real target objects to prove the behavior is correct" — correctness
  is execution-dependent, not intent-dependent; (2) "concurrency, deduplication,
  or serialization needs to be tested on a live-like surface" — staged mode is
  serial/isolated; (3) "maintainers need to inspect the actual produced state,
  not only proposed intent" — the artifact matters, not just the proposal; (4)
  "cross-repository writes, permissions, or dispatch boundaries need to be
  exercised safely." The fourth condition is particularly important for gh-aw
  orchestrators that fan out across repositories — the permission model at
  dispatch boundaries cannot be validated by staged mode. For Ch03: shadow
  evaluation should be recommended specifically for multi-repo workflows before
  production promotion.

### Claim 6: Design rule — production truth stays authoritative; evaluation surfaces must not become new sources of truth

- **Evidence**: The first design rule is stated as a prohibition against letting
  the evaluation surface accumulate trust, with an explicit statement of what
  should remain authoritative.
- **Confidence**: emerging (practitioner rule from first-party documentation;
  reflects hard-won operational experience without citing specific incidents)
- **Quote**: "Do not let the evaluation surface become the new source of truth.
  Production events and later trusted human actions should remain authoritative."
- **Our assessment**: This rule addresses a known failure mode in evaluation
  infrastructure: systems built to observe and validate production behavior
  gradually accumulate state that downstream consumers begin to depend on. The
  shadow target is a write surface; once it is written to, it can become a de
  facto source of truth if not actively kept subordinate to production. The
  explicit "later trusted human actions should remain authoritative" clause also
  covers the case where a human manually corrects a workflow prediction — those
  corrections should override, not be averaged with, the prediction. For Ch03:
  this rule should accompany any guidance on shadow evaluation to prevent the
  shadow target from growing into a second live system.

### Claim 7: Design rule — prediction snapshots must be explicitly persisted at decision time, not reconstructed from logs

- **Evidence**: The second design rule addresses prediction provenance, framed
  as a conditional requirement ("if later comparison matters"). The prohibition
  on reconstruction is precise: logs are lossy and interpretive, while
  decision-time snapshots are authoritative.
- **Confidence**: emerging (practitioner rule; grounded in standard data
  engineering practice around event sourcing and immutable snapshots)
- **Quote**: "If later comparison matters, persist what the workflow predicted
  at decision time. Do not reconstruct predictions from logs."
- **Our assessment**: This is a data integrity rule. Workflows that produce
  predictions (e.g., "this PR is safe to merge," "this dependency update is
  non-breaking") need to persist those predictions as explicit records, not
  rely on reconstructing them from execution logs. Log reconstruction is
  error-prone because logs reflect what happened, not what the model decided
  to do and why. The "if later comparison matters" qualifier is important:
  this rule applies specifically when predictions will be evaluated after the
  fact — e.g., during rollout evaluation when comparing shadow vs. production
  outcomes. For Ch02: recommend snapshotting workflow decisions as structured
  artifacts (not log entries) when operating in staged or shadow modes.

### Claim 8: Design rule — correction evidence requires provenance metadata to be trustworthy

- **Evidence**: The third design rule addresses the quality of feedback signal.
  The rule specifies exactly which provenance fields matter: actor type, source
  (manual vs. automated), trust status, and origin repository role.
- **Confidence**: emerging (practitioner rule; aligned with standard ML data
  quality requirements for training and evaluation feedback)
- **Quote**: "Not every later edit should count as trustworthy truth. Record
  provenance such as actor type, manual versus automated source, trust status,
  and origin repository role."
- **Our assessment**: This rule is critical for workflows that improve over time
  using human corrections as signal. A maintainer manually reverting a workflow's
  change is high-trust correction evidence; an automated bot reverting the same
  change is not. Without provenance, the correction signal is ambiguous — the
  workflow cannot distinguish "human said this was wrong" from "another
  automation ran and overwrote this." The "origin repository role" field is
  particularly relevant for multi-repo gh-aw deployments where the same workflow
  runs against repositories with different governance levels. For Ch09 (Agent
  Orchestration): when orchestrators collect correction feedback from workers,
  provenance fields should be mandatory, not optional.

### Claim 9: Design rule — shadow targets should remain thin and disposable, not become secondary control planes

- **Evidence**: The fourth design rule explicitly constrains the scope of the
  shadow target with a statement of purpose and a prohibition against scope
  creep.
- **Confidence**: settled (first-party platform guidance; the constraint is
  directly tied to the shadow target's role as a *temporary* rollout artifact)
- **Quote**: "Keep the shadow target thin. It should support measurement and
  rollout, not become a second long-lived control plane."
- **Our assessment**: This rule addresses the lifecycle of the shadow target.
  Shadow repositories are explicitly described as "temporary non-production
  write targets during rollout" — they exist to validate the write path, then
  be discarded once the workflow is promoted to production writes. The failure
  mode this rule prevents is the shadow target accumulating operational
  importance over time: consumers building dashboards from shadow data, other
  workflows reading shadow state, on-call runbooks pointing to shadow targets.
  Once the shadow target acquires dependents, it becomes impossible to delete.
  This rule should be read alongside Claim 1: if the shadow target becomes a
  second control plane, the production truth stays authoritative rule (Claim 6)
  is violated. For Ch02: the shadow repository pattern should include an explicit
  cleanup step in the promotion playbook.

### Claim 10: The three-repository shape — production, ops, shadow — is a common rollout layout, but explicitly remains rollout guidance rather than a primary architectural pattern

- **Evidence**: The page presents the repository split as an "example shape" —
  not as a required architecture or a named pattern. The explicit downgrade
  ("it is still rollout guidance rather than a primary pattern") is important
  context for how to use this in the guide.
- **Confidence**: emerging (first-party recommendation with a significant
  qualifier about its status)
- **Quote**: "That shape is often useful, but it is still rollout guidance
  rather than a primary pattern."
- **Our assessment**: The three-repo split maps roles cleanly: production emits
  authoritative events, ops persists predictions and corrections, shadow is the
  temporary write target. However, the explicit qualification that this is
  *rollout guidance* — not a named pattern like CentralRepoOps or SideRepoOps —
  means the guide should present it as a practical heuristic for teams running
  safe rollout, not as a standalone architectural recommendation. The ops
  repository role ("persists predictions, collects corrections, publishes
  reports, and updates instructions") is the most novel element: it collocates
  the feedback loop infrastructure (predictions + corrections) with the
  reporting surface. For Ch02: include the three-repo shape as an example
  harness layout for safe rollout deployments, with a note that it is not a
  required pattern.

## Concrete Artifacts

### Rollout Ladder (from source, verbatim)

```
The usual progression is:

1. Start in report-only mode.
2. Enable `staged` behavior when proposed writes need to be previewed.
3. Use shadow evaluation when preview mode is not enough and the real write
   path needs to be exercised safely.
4. Promote the same workflow to direct production writes.
```

### Staged vs. Shadow Decision Criteria (from source, verbatim)

```
Staged mode:
  Sufficient when: "the main risk is decision quality rather than
                   operational behavior"
  Use when maintainers need to: review proposed actions, compare
                   alternatives, or inspect whether the workflow's
                   judgment is reasonable before any write is allowed

Shadow evaluation:
  Needed when: "staged mode is too weak because the real write path
               itself needs validation"
  Specific conditions:
  - the workflow must update real target objects to prove the behavior
    is correct
  - concurrency, deduplication, or serialization needs to be tested on
    a live-like surface
  - maintainers need to inspect the actual produced state, not only
    proposed intent
  - cross-repository writes, permissions, or dispatch boundaries need
    to be exercised safely
```

### Four Design Rules (from source, verbatim section headers and text)

```
Production truth stays authoritative
  "Do not let the evaluation surface become the new source of truth.
   Production events and later trusted human actions should remain
   authoritative."

Prediction snapshots should be explicit
  "If later comparison matters, persist what the workflow predicted at
   decision time. Do not reconstruct predictions from logs."

Correction evidence needs provenance
  "Not every later edit should count as trustworthy truth. Record
   provenance such as actor type, manual versus automated source, trust
   status, and origin repository role."

Evaluation surfaces should remain disposable
  "Keep the shadow target thin. It should support measurement and
   rollout, not become a second long-lived control plane."
```

### Three-Repository Example Shape (from source, verbatim)

```
- production repository: emits live events and contains authoritative
  later human truth
- ops repository: persists predictions, collects corrections, publishes
  reports, and updates instructions
- shadow repository: temporary non-production write target during rollout
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as the zero-capability-
    by-default mechanism): the safe rollout ladder operates on top of Safe
    Outputs — staged mode is the platform feature that enables non-write
    output of proposed actions. The "no write access by default" principle in
    `docs-ghaw-how-they-work.md` is the foundation that makes staged mode's
    "no write has occurred" guarantee coherent.
  - `docs-ghaw-dailyops.md` Claim 3 (three-phase DailyOps approach with
    maintainer approval between each phase): both sources share the pattern
    of gated autonomy — humans must approve before escalating to the next
    level. DailyOps uses approval gates within a workflow's execution; safe
    rollout uses promotion criteria between deployment rungs.
  - `docs-ghaw-central-repo-ops.md` Claim 8 (phased rollout categorization
    for org-scale deployment): both sources recommend staged deployment, but
    the CentralRepoOps phased rollout is about *which repositories get the
    workflow* (simple → security → complex → conflicting), while safe rollout
    is about *how much autonomy the workflow has* (report-only → staged →
    shadow → production). These are orthogonal axes that can compose: a
    CentralRepoOps deployment could use safe rollout to promote trust in each
    category before advancing to the next.

- **Contradicts**: None identified. No existing source note documents the
  rollout ladder, the staged/shadow evaluation distinction, or the four
  design rules. No claims in this source materially oppose existing notes.

- **Extends**:
  - `docs-ghaw-how-they-work.md`: this guide page builds directly on the
    Safe Outputs model. Safe Outputs provides the permission-separated
    write mechanism; the safe rollout ladder provides the trust-promotion
    framework for deciding *when* to graduate from permission-separated
    (staged) to direct production writes. Read together: Safe Outputs is the
    mechanism, safe rollout is the governance lifecycle.

- **Novel**:
  - **The four-rung rollout ladder** (Claim 2): No existing source note
    documents this as a named, structured autonomy-promotion sequence.
  - **The staged vs. shadow evaluation distinction** (Claim 3): The precise
    framing — two modes answering different questions (what vs. whether) —
    is entirely new to the corpus. No existing note distinguishes these two
    modes or explains when each is appropriate.
  - **The four design rules** (Claims 6–9): None of these rules appears in
    any existing corpus note. Together they form a hygiene checklist for
    safe rollout infrastructure that prevents evaluation surfaces from
    degrading production truth.
  - **Shadow evaluation as a technique inside safe rollout** (not a separate
    pattern): The explicit scoping of shadow evaluation as one technique
    within the safe rollout framework prevents practitioners from treating
    it as a standalone alternative to staged mode.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: No existing chapter guidance covers
  the shadow repository as a harness pattern. Add the three-repository shape
  (production + ops + shadow) from Claim 10 as the reference harness layout
  for safe rollout. Add the rule that shadow targets must remain thin and
  disposable (Claim 9) as a constraint on that layout. Add the prediction
  snapshot recommendation (Claim 7) as a data artifact standard for
  staged/shadow-mode harnesses.

- **Chapter 03 (Safety and Verification)**: Ch03 currently documents per-PR
  human approval gates (e.g., from `blog-gh-aw-operations-release-workflows.md`)
  as the primary safety mechanism. Add the safe rollout ladder (Claim 2) as the
  deployment-time counterpart to those per-action gates — the ladder governs
  *how much* the workflow can do; per-PR gates govern *whether* a specific
  action proceeds. The staged/shadow distinction (Claim 3) and four design
  rules (Claims 6–9) should accompany this. Add the framing from Claim 1
  ("trusted enough to act on the live system") as the guiding question for
  promoting any agentic workflow.

- **Chapter 05 (Team Adoption)**: The ladder provides a low-friction
  on-ramp: teams can commit to "start in report-only" without needing to
  trust the automation immediately. Add the ladder as the recommended
  adoption sequence for new agentic workflows — each rung accumulates
  evidence before the next promotion, which mirrors how teams build
  institutional trust in new automation. Specifically: report-only mode
  requires no trust investment; staged mode requires read access only;
  shadow evaluation requires a dedicated (temporary) write target; production
  writes require full trust.

- **Chapter 09 (Agent Orchestration)**: Add the correction evidence provenance
  requirement (Claim 8) as a mandatory data field when orchestrators collect
  feedback from workers. The multi-repo gh-aw context in which this guidance
  was developed makes it particularly relevant to orchestrator-worker patterns
  where workers operate across repositories with different governance levels.

## Extraction Notes

Fetched the source URL three times with different prompts to triangulate
verbatim wording. The third fetch returned what appeared to be the full page
text in a well-structured format; all quotes in this note are drawn from
that fetch. There was minor wording variation between the first and third
fetches on some passages (likely rendering artifacts); quotes were chosen
from the third fetch because it returned the most complete and internally
consistent version of the page.

The page links to four related pages in its navigation: SideRepoOps,
MultiRepoOps, Staged Mode, and Safe Outputs Reference. None of these have
dedicated source notes in the current corpus (SideRepoOps and MultiRepoOps
have no notes; Staged Mode details are partially covered in
`docs-ghaw-how-they-work.md`; Safe Outputs Reference is the canonical
companion page to `docs-ghaw-how-they-work.md`). These linked pages were not
fetched as they fall within already-covered territory or are not yet in scope.
