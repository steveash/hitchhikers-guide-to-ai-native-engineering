---
source_url: https://github.github.com/gh-aw/guides/organization-practices/safe-rollout
source_type: docs
title: "GitHub Agentic Workflows: Safe Rollout Guide"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: emerging
issue: "#481"
---

# GitHub Agentic Workflows: Safe Rollout Guide

> The official gh-aw framework for escalating agentic workflow autonomy in four named rungs
> (report-only → staged → shadow evaluation → direct production writes), with a key
> distinction between staged mode (decision quality risk) and shadow evaluation (write-path
> operational risk), and four design rules that prevent rollout artifacts from corrupting
> production truth.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, "Guides > Organization
  Practices > Safe Rollout" — prescriptive framework page, not a pattern reference or
  conceptual overview. Guides pages document organizational-level practices that cut across
  patterns.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team (GitHub Next /
  Microsoft Research — the team behind Peli de Halleux's "Agent Factory" blog series and the
  `gh aw` platform). Claims about the rollout ladder, design rules, and repository shape are
  authoritative as platform guidance. The framework is prescriptive without empirical
  benchmarks — no data is provided on how long workflows spend at each rung or what metrics
  signal readiness to advance.
- **Scope**: The Safe Rollout framework — core definition (incremental autonomy escalation),
  the four-rung rollout ladder, the staged-vs.-shadow-evaluation distinction with decision
  criteria, four design rules for preventing evaluation-surface drift, and the three-repo
  example shape. Does NOT cover: specific Safe Outputs YAML configuration for staging (linked
  to the Safe Outputs Reference separately), how to instrument report-only mode in practice,
  the SideRepoOps or MultiRepoOps patterns (referenced but not described), or any promotion
  decision metrics (the page has none).

## Extracted Claims

### Claim 1: Safe rollout is defined as increasing workflow autonomy in steps rather than enabling direct production writes immediately

- **Evidence**: Opening definition on the page: "Safe rollout is the practice of increasing
  workflow autonomy in steps instead of enabling direct production writes immediately." This
  is the authoritative definition for the gh-aw platform. The framing positions the ladder
  not as optional refinement but as the default practice for any agentic workflow that will
  eventually write to production.
- **Confidence**: emerging (design principle from first-party documentation; no measurement
  of adoption rate or comparative outcome data is provided)
- **Quote**: "Safe rollout is the practice of increasing workflow autonomy in steps instead of
  enabling direct production writes immediately."
- **Our assessment**: The framing distinguishes safe rollout from permission models (which
  govern what the agent *can* do) by focusing on what the agent *is trusted to do* in a
  given deployment. A workflow with full write permissions can still be placed in report-only
  mode. This is the deployment-side counterpart to the "no write access by default" principle
  in `docs-ghaw-how-they-work.md` (Claim 4): that principle governs the permission model;
  this principle governs the activation model. Together: zero capability by default (how-they-work)
  + earned-activation-in-steps (this page). For Ch03 (Safety and Verification): safe rollout
  should be framed as the deployment standard, not as an optional caution. Every workflow that
  writes to production should start this ladder before being promoted.

### Claim 2: The central question for advancing through the rollout ladder is trust, not utility — "whether it is trusted enough to act on the live system"

- **Evidence**: The page states: "The main question is not whether a workflow is useful, but
  whether it is trusted enough to act on the live system." This reframes the promotion
  decision away from capability assessment ("can the workflow do this?") toward behavioral
  trust assessment ("has the workflow demonstrated trustworthy behavior at this scope?").
- **Confidence**: emerging (architectural framing; trust is not operationally defined with
  measurable criteria — the page provides no thresholds or checklists for promotion)
- **Quote**: "The main question is not whether a workflow is useful, but whether it is trusted
  enough to act on the live system."
- **Our assessment**: The trust framing matters for how teams approach adoption. The risk in
  most agentic adoption discussions is that teams ask "is this workflow capable enough?" and
  skip directly to production. The guide's framing redirects: capability is necessary but not
  sufficient — the evidence of trustworthy behavior at each rung is the gate. Operationally,
  this means teams need to run a workflow in report-only or staged mode long enough to observe
  its judgment before promoting it. The guide does not specify how long, which is a genuine
  gap — but the framing is correct. For Ch05 (Team Adoption): the trust-not-utility framing
  is the vocabulary needed to explain to stakeholders why a capable workflow is still running
  in report-only mode.

### Claim 3: The rollout ladder has four named rungs — report-only, staged behavior, shadow evaluation, direct production writes — representing a progression of increasing autonomy

- **Evidence**: The page defines four rungs explicitly:
  1. **Report-only mode** — Initial observation phase; workflow observes and reports without
     making any writes.
  2. **Staged behavior** — Proposed writes are previewed for review before execution.
  3. **Shadow evaluation** — The real write path is exercised safely on non-production targets.
  4. **Direct production writes** — Full autonomy on live systems.
  The page states: "the usual progression is" through these steps. No skipping is implied.
- **Confidence**: emerging (first-party documentation; the ladder is prescribed but progression
  criteria are not specified — there is no documented threshold for when a workflow is ready
  to advance)
- **Quote**: "the usual progression is" [through the four stages]
- **Our assessment**: The four-rung structure is the most complete autonomy-escalation
  framework in the corpus. Prior sources document point-in-time approval gates
  (`docs-ghaw-dailyops.md` Claim 3 — three-phase approval gates between workflow phases;
  `blog-gh-aw-operations-release-workflows.md` Claim 6 — 22% rejection rate implying human
  verification on PRs), but no existing source documents a structured progression model for
  an entire workflow's lifecycle from inception to full autonomy. The notable operational
  gap: the page does not define what report-only mode means concretely (what gets reported,
  where, or how to use those findings to make a promotion decision). For Ch03: this four-rung
  model is the deployment lifecycle framework missing from the guide's current safety section.
  Paired with `docs-ghaw-how-they-work.md`'s five-layer security architecture, these two
  frameworks cover both the runtime safety model (five layers) and the deployment trust model
  (four rungs).

### Claim 4: Staged mode and shadow evaluation are not interchangeable — staged addresses decision quality risk, shadow evaluation addresses write-path operational risk

- **Evidence**: Direct statement from the page: "staged and shadow evaluation are not
  interchangeable." The page provides specific criteria for each:
  - Staged mode is appropriate "when the main risk is decision quality rather than operational
    behavior. It is usually enough when maintainers only need to review proposed actions,
    compare alternatives, or inspect whether the workflow's judgment is reasonable before any
    write is allowed."
  - Shadow evaluation applies when "staged mode is too weak because the real write path itself
    needs validation." The four specific criteria for when shadow evaluation is needed:
    (a) "the workflow must update real target objects to prove the behavior is correct";
    (b) "concurrency, deduplication, or serialization needs to be tested on a live-like surface";
    (c) "maintainers need to inspect the actual produced state, not only proposed intent";
    (d) "cross-repository writes, permissions, or dispatch boundaries need to be exercised safely."
- **Confidence**: settled (first-party documentation with explicit decision criteria; the
  distinction is clearly articulated and actionable)
- **Quote**: "Use staged mode when the main risk is decision quality rather than operational
  behavior." / "Shadow evaluation is one technique inside safe rollout, not a separate
  top-level pattern."
- **Our assessment**: This is the most extractable novel pattern in the source. The
  staged/shadow distinction maps to two different failure modes that require different
  validation techniques: (1) If you worry the workflow will make wrong *decisions* (propose
  the wrong change), use staged mode to review proposals before they execute. (2) If you worry
  the workflow's *write path itself* will misbehave (race conditions, permission errors,
  deduplication failures), use shadow evaluation to exercise the real write path against a
  non-production target. Skipping shadow evaluation when (b) or (d) above apply means
  promoting a workflow to production without having exercised its actual write path — a class
  of operational risk staged mode cannot catch. For Ch03: teach this distinction explicitly.
  Teams currently defaulting to "let's watch the PRs for a while" are doing staged-equivalent
  validation and may be missing write-path operational validation entirely.

### Claim 5: The staged mode framing distinguishes "what the workflow would do" (proposal review) from "whether the write path behaves correctly" (operational validation)

- **Evidence**: The page states: "staged mode is sufficient when the question is what the
  workflow would do." This delineation makes staged mode a decision-review technique, not
  a write-path validation technique. The distinction is that staged mode never exercises the
  write path at all — it shows the proposed action without executing it.
- **Confidence**: settled (direct quote)
- **Quote**: "staged mode is sufficient when the question is what the workflow would do"
- **Our assessment**: This framing is precise and actionable. "What the workflow would do" =
  staged mode (review proposals). "Does the write path behave correctly?" = shadow evaluation
  (exercise the actual write path on a non-production target). The framing also implies that
  staged mode cannot catch write-path bugs by design — it is not a less thorough version of
  shadow evaluation; it is a different kind of validation entirely. For Ch02 (Harness
  Engineering): when specifying the validation layer for an agentic workflow, require harness
  engineers to explicitly classify their risk: decision-quality or write-path-operational?
  The answer determines whether staged or shadow evaluation is the appropriate next rung.

### Claim 6: Four design rules prevent evaluation surfaces from becoming corrupted or permanent — governing how predictions, corrections, and shadow targets should behave

- **Evidence**: The page articulates four named rules with explicit explanations:
  1. **Production truth stays authoritative**: "Do not let the evaluation surface become the
     new source of truth. Production events and later trusted human actions should remain
     authoritative."
  2. **Prediction snapshots should be explicit**: "If later comparison matters, persist what
     the workflow predicted at decision time. Do not reconstruct predictions from logs."
  3. **Correction evidence needs provenance**: "Not every later edit should count as
     trustworthy truth. Record provenance such as actor type, manual versus automated source,
     trust status, and origin repository role."
  4. **Evaluation surfaces should remain disposable**: "Keep the shadow target thin. It
     should support measurement and rollout, not become a second long-lived control plane."
- **Confidence**: emerging (first-party prescriptive rules; well-reasoned but without
  empirical evidence for the failure modes they prevent)
- **Quote**: "Keep the shadow target thin. It should support measurement and rollout, not
  become a second long-lived control plane."
- **Our assessment**: These four rules are terse but each encodes a real failure mode:
  Rule 1 prevents the ops/shadow repo from being treated as ground truth (it is an evaluation
  artifact, not the source of truth). Rule 2 prevents post-hoc rationalization — if you want
  to measure whether the workflow's prediction was correct, you must persist the prediction
  at decision time, not reconstruct it later. Rule 3 prevents all edits from being treated
  as equally authoritative — a human correction by a trusted maintainer is not the same signal
  as an automated re-run. Rule 4 prevents shadow evaluation infrastructure from outliving its
  purpose and becoming permanent operational overhead. For Ch02 (Harness Engineering): these
  rules are requirements for the ops/shadow repository design in any evaluation-instrumented
  agentic system. They should be encoded in the harness spec, not left to implementation
  conventions.

### Claim 7: The three-repo shape (production, ops, shadow) is rollout guidance, not a primary pattern, and is explicitly positioned as temporary

- **Evidence**: The page defines the common repository split:
  - **production repository**: "emits live events and contains authoritative later human truth"
  - **ops repository**: "persists predictions, collects corrections, publishes reports, and
    updates instructions"
  - **shadow repository**: "temporary non-production write target during rollout"
  Crucially, the page qualifies this: "That shape is often useful, but it is still rollout
  guidance rather than a primary pattern." The shadow repository is explicitly "temporary."
- **Confidence**: emerging (first-party documentation; the temporary/disposable framing is
  deliberate)
- **Quote**: "That shape is often useful, but it is still rollout guidance rather than a
  primary pattern."
- **Our assessment**: The three-repo shape gives teams a concrete starting architecture for
  safe rollout — an ops repository as the evaluation control plane is a reusable pattern
  independent of the specific workflow being rolled out. However, the guidance that this is
  "rollout guidance rather than a primary pattern" is important: teams should not architect
  the shadow repository as permanent infrastructure. The ops repository may become permanent
  (it holds predictions, corrections, and reports even after rollout completes), but the
  shadow repository should be decommissioned once the workflow is promoted to direct
  production writes. This is consistent with Design Rule 4 (evaluation surfaces remain
  disposable). For Ch09 (Agent Orchestration): the three-repo shape is the concrete
  repository architecture for agentic evaluation pipelines. The relationship to
  `docs-ghaw-central-repo-ops.md`'s CentralRepoOps pattern should be noted — the ops
  repository here is analogous to the CentralRepoOps control-plane repository, though
  with different semantics (evaluation vs. orchestration).

### Claim 8: Shadow evaluation is "one technique inside safe rollout, not a separate top-level pattern"

- **Evidence**: Direct statement: "Shadow evaluation is one technique inside safe rollout,
  not a separate top-level pattern." This positions shadow evaluation as a sub-technique of
  the safe rollout framework, not as an independent deployment pattern.
- **Confidence**: settled (direct quote clarifying scope)
- **Quote**: "Shadow evaluation is one technique inside safe rollout, not a separate
  top-level pattern."
- **Our assessment**: This scoping statement is significant because it prevents teams from
  treating shadow evaluation as a replacement for the full rollout ladder. A team that goes
  directly to shadow evaluation without a report-only phase has skipped the decision-quality
  review; a team that does staged mode and then goes straight to production has skipped the
  write-path validation. Shadow evaluation is one rung, not the whole framework. For Ch03:
  when recommending safe rollout, present the full four-rung ladder and position shadow
  evaluation correctly within it, not as the sole validation technique.

## Concrete Artifacts

### The Safe Rollout Ladder (from documentation)

```
Safe rollout progression (in order — "the usual progression is"):

Rung 1: Report-only mode
  → Workflow observes, reports findings, makes no writes
  → Purpose: establish behavioral baseline and surface decision patterns
  → No configuration for writes is active

Rung 2: Staged behavior
  → Proposed writes are previewed for review before execution
  → "Enable staged behavior when proposed writes need to be previewed"
  → Appropriate when: "the main risk is decision quality rather than operational behavior"
  → Staged mode is sufficient when "the question is what the workflow would do"

Rung 3: Shadow evaluation
  → Real write path exercised safely on non-production targets
  → Use when staged mode is "too weak because the real write path itself needs validation"
  → Required when any of:
      (a) workflow must update real target objects to prove behavior is correct
      (b) concurrency, deduplication, or serialization needs live-like testing
      (c) maintainers need actual produced state, not just proposed intent
      (d) cross-repository writes, permissions, or dispatch boundaries need safe exercise
  → "Shadow evaluation is one technique inside safe rollout, not a separate top-level pattern"

Rung 4: Direct production writes
  → "Promote the same workflow to direct production writes"
  → Full autonomy on live systems
```

### Staged Mode vs. Shadow Evaluation — Decision Table

```
                   | Staged Mode                      | Shadow Evaluation
-------------------|----------------------------------|-----------------------------------------
Core question      | "What would the workflow do?"    | "Does the write path behave correctly?"
Risk addressed     | Decision quality                 | Operational behavior of write path
Write path active? | No — proposals only              | Yes — writes to non-production target
Appropriate when   | Reviewing judgment, comparing    | Real target objects needed; concurrency,
                   | alternatives, inspecting         | dedup, or serialization; cross-repo
                   | reasoning                        | permissions need exercise
Sufficient when    | "main risk is decision quality"  | Staged mode "too weak" for the validation
                   |                                  | needed
Key limitation     | Cannot catch write-path bugs     | Requires a shadow target to be provisioned
```

### Four Design Rules for Rollout Artifacts

```
Rule 1: Production truth stays authoritative
  "Do not let the evaluation surface become the new source of truth.
   Production events and later trusted human actions should remain authoritative."
  → Implication: ops/shadow repos are evaluation artifacts, not ground truth

Rule 2: Prediction snapshots should be explicit
  "If later comparison matters, persist what the workflow predicted at decision time.
   Do not reconstruct predictions from logs."
  → Implication: harness must write prediction records at decision time; post-hoc
    reconstruction is insufficient for evaluating workflow quality

Rule 3: Correction evidence needs provenance
  "Not every later edit should count as trustworthy truth.
   Record provenance such as actor type, manual versus automated source, trust status,
   and origin repository role."
  → Implication: correction records must carry metadata; treating all edits equally
    contaminates the evaluation signal

Rule 4: Evaluation surfaces should remain disposable
  "Keep the shadow target thin.
   It should support measurement and rollout, not become a second long-lived control plane."
  → Implication: decommission shadow repositories after promotion; resist expanding
    shadow targets with permanent operational scope
```

### Three-Repository Shape for Safe Rollout

```
production repository
  → Role: Emits live events; contains authoritative later human truth
  → Permanence: Permanent (this is the system being rolled out to)

ops repository
  → Role: Persists predictions; collects corrections; publishes reports; updates instructions
  → Permanence: May persist after rollout (holds evaluation history and correction records)

shadow repository
  → Role: Temporary non-production write target during rollout
  → Permanence: Temporary ("rollout guidance rather than a primary pattern")
  → Design Rule 4 applies: keep it thin; decommission after promotion to Rung 4

Note: "That shape is often useful, but it is still rollout guidance rather than a primary pattern."
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 4 ("no write access by default") and Claim 5 (Safe
    Outputs as permission-separated state mutation): The safe rollout ladder operationalizes
    these principles over time — report-only mode is the zero-write starting point consistent
    with "no write access by default"; staged mode uses Safe Outputs to preview proposed
    writes before executing them. The how-they-work note covers the per-run permission model;
    this note covers the deployment lifecycle model that determines when those permissions
    are activated.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human approval): The
    staged and shadow rungs are concrete implementations of human-in-the-loop approval gates.
    Staged mode = human reviews the proposal before any write. The rollout ladder makes this
    a deployment lifecycle, not just a per-action gate.
  - `docs-ghaw-dailyops.md` Claim 3 (three-phase approach — Research → Configuration →
    Execution — with maintainer approval between phases): Both the DailyOps three-phase model
    and the safe rollout ladder are human-checkpointed autonomy escalation models, but at
    different scopes. DailyOps phases gate *within* a single workflow run (each phase requires
    maintainer approval before the next phase begins). The safe rollout ladder gates *across*
    the workflow's deployment lifetime (each rung requires trust-building before promotion).
    These are complementary patterns at different time scales.
  - `blog-gh-aw-operations-release-workflows.md` Claim 6 (22% rejection rate implies active
    human verification): The Changeset Generator's 22% PR rejection rate is behavioral
    evidence of staged-equivalent validation in practice — humans reviewing proposed releases
    before merge. The safe rollout ladder provides the framework for why that human gate
    exists and when it can eventually be removed.

- **Extends**:
  - `docs-ghaw-how-they-work.md`: That note covers the runtime safety architecture (five
    security layers, Safe Outputs, compilation model). This note covers the deployment trust
    model — how workflows earn the right to exercise those runtime capabilities in production.
    Together: runtime safety architecture (how-they-work) + deployment trust ladder (this note)
    = the complete safety framework.
  - `docs-ghaw-central-repo-ops.md` Claim 8 (phased rollout categorization — simple →
    security → complex → conflicting): The CentralRepoOps phased rollout is about *which
    repositories* to deploy a workflow to (prioritization of targets). The safe rollout ladder
    is about *what level of autonomy* to grant the workflow during that deployment (escalation
    of trust). These are orthogonal dimensions: a team can use both simultaneously — deploying
    first to simple repositories (CentralRepoOps Claim 8) while running in staged mode (safe
    rollout Rung 2), then expanding to complex repositories while promoting to direct writes
    only after shadow evaluation validates the write path.

- **Contradicts**: None identified. The four-rung ladder, staged/shadow distinction, and
  design rules are consistent with all existing source notes. No existing note describes a
  conflicting framework for agentic autonomy escalation. No contradiction issue needs to
  be filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **The staged-vs.-shadow-evaluation distinction with explicit decision criteria** (Claim 4):
    No existing source note distinguishes decision-quality risk (staged mode) from write-path
    operational risk (shadow evaluation) as two separate validation concerns requiring
    different techniques. This is the highest-value novel pattern in the source.
  - **The four-rung safe rollout ladder as a named lifecycle model** (Claim 3): No prior note
    describes a structured deployment lifecycle model for agentic workflows moving from
    observation to full autonomy. DailyOps (three-phase within a run) and CentralRepoOps
    (phased rollout by target complexity) are adjacent but neither covers the lifecycle of
    a single workflow's trust escalation over its deployment lifetime.
  - **Four design rules governing evaluation artifact hygiene** (Claim 6): The rules about
    production truth authority, snapshot explicitness, correction provenance, and disposable
    evaluation surfaces are not documented in any existing note. These are preventative rules
    for a class of operational failure (evaluation surfaces corrupting production truth) not
    yet addressed in the corpus.
  - **The three-repo shape as rollout infrastructure** (Claim 7): The explicit naming of
    production + ops + shadow as a rollout-time repository architecture — with the shadow
    repo explicitly positioned as temporary — is new. CentralRepoOps documents production +
    control-plane repos for orchestration; this note documents production + ops + shadow for
    evaluation. The ops repository role (predictions, corrections, reports, instructions) is
    the most novel element.

## Guide Impact

### Chapter 03: Safety and Verification

- **Add the safe rollout ladder as the deployment-lifecycle safety framework** (Claim 3):
  The guide's current safety section covers runtime controls (five-layer security, Safe Outputs,
  human-in-the-loop per-PR gates). It lacks a deployment lifecycle model. The four-rung ladder
  is that model: every agentic workflow should start in report-only mode and advance only when
  the team has evidence of trustworthy behavior at the current rung. Frame this as the
  deployment standard, not an optional caution.
- **Add the staged/shadow distinction as an actionable safety engineering decision** (Claims
  4–5): When teams are deciding how to validate a new agentic workflow, they need vocabulary
  for two distinct risks: decision quality (staged mode) and write-path operational behavior
  (shadow evaluation). The guide should require teams to classify their risk type before
  choosing a validation technique. This prevents the common failure of doing staged-mode
  review and then going directly to production without ever exercising the write path.
- **Frame safe rollout as the deployment-side counterpart to per-run approval gates** (Claim 1):
  The existing safety content covers per-run gates (human PR review, `docs-ghaw-how-they-work.md`
  Claim 10). Safe rollout is the per-*deployment* gate structure — the evidence accumulation
  process before those per-run gates are relaxed. Both are needed; neither replaces the other.

### Chapter 02: Harness Engineering

- **Add the four design rules as harness requirements for any evaluation-instrumented system**
  (Claim 6): Teams building ops or shadow repositories as part of a safe rollout deployment
  need these rules encoded in their harness spec. Specifically: (a) prediction records must
  be persisted at decision time (not reconstructed); (b) correction records must carry
  provenance metadata; (c) shadow targets must be designed for disposal, not permanence.
  These are harness-level requirements, not organizational policies.
- **Add the three-repo shape as the reference architecture for agentic evaluation pipelines**
  (Claim 7): When a workflow requires shadow evaluation, the production + ops + shadow shape
  is the starting architecture. The ops repository's role (predictions + corrections + reports
  + instructions) defines what the harness must be able to write; the shadow repository's
  temporary nature defines its lifecycle. Cross-reference `docs-ghaw-central-repo-ops.md`
  for the orchestration-side use of a similar control-plane pattern.

### Chapter 05: Team Adoption

- **Use the trust-not-utility framing to explain report-only mode to stakeholders** (Claim 2):
  Teams adopting new agentic workflows will face pressure to promote quickly ("it's working,
  why is it still in report-only mode?"). The guide should give teams the vocabulary: the
  question is not whether the workflow is capable, but whether it has demonstrated trustworthy
  judgment at the current scope. Report-only mode is trust-building, not timidity.
- **Position report-only mode as the zero-risk entry point for any new workflow** (Claim 1):
  The lowest barrier to adoption for a new agentic workflow is "start it in report-only mode."
  No writes means no blast radius. Teams that are uncertain about adopting agentic automation
  can commit to report-only as a genuinely safe first step without governance risk. The
  escalation to staged and shadow can happen incrementally as confidence grows.

### Chapter 09: Agent Orchestration

- **Add the three-repo shape as the orchestration architecture for evaluation-phase deployments**
  (Claim 7): For workflows in the shadow evaluation rung, the three-repo shape defines how
  the orchestration layer should route writes — live events flow from production to the ops
  repository; predicted writes flow to the shadow target rather than production. This is an
  orchestration routing pattern, not just a deployment configuration.

## Extraction Notes

1. **Source is terse but prescriptive**: The Safe Rollout guide is shorter and less
   detailed than other GHAW pattern pages (e.g., CentralRepoOps, DailyOps). Several key
   concepts are named but not fully specified: report-only mode has no concrete definition
   (what gets reported, where, how), and promotion criteria between rungs are not provided
   (no metrics, no thresholds, no timelines). This is a genuine gap in the documentation,
   not a rendering issue. The framework's value is in its vocabulary and distinctions, not
   in its operational prescriptions.

2. **No YAML examples**: Unlike CentralRepoOps and DailyOps, this page contains no
   configuration examples for staged mode, shadow evaluation setup, or ops/shadow repository
   initialization. Staged mode configuration is deferred to the linked "Safe Outputs
   Reference" page; shadow evaluation setup is not detailed anywhere visible on this page.

3. **Related pattern pages referenced but not followed**: The page links to SideRepoOps,
   MultiRepoOps, "Staged Mode" reference, and "Safe Outputs Reference." The Staged Mode
   reference page likely contains the YAML for enabling staged behavior — a separate source
   note may be warranted for that page if it contains substantial harness engineering detail.

4. **Page is from the "Guides > Organization Practices" section**: This distinguishes it
   from "Patterns" pages (which document specific workflow architectures) and "Introduction"
   pages (which document platform concepts). "Guides" pages document cross-cutting
   organizational practices — the rollout ladder applies to any workflow type, not just
   a specific pattern like CentralRepoOps or DailyOps.

5. **No contradictions filed**: Reviewed all existing source notes. No claims in this source
   materially oppose any existing note. The four-rung ladder, staged/shadow distinction, and
   design rules are entirely new to the corpus.
