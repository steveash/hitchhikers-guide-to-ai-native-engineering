---
source_url: https://github.github.com/gh-aw/patterns/correction-ops
source_type: docs
title: "GitHub Agentic Workflows: CorrectionOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#468"
---

# GitHub Agentic Workflows: CorrectionOps Pattern

> An experimental gh-aw pattern for comparing AI predictions with later human
> corrections and using the difference to improve the workflow system —
> instructions, routing, thresholds, and rollout decisions — without retraining
> the underlying model.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/correction-ops`
  page — in the `patterns/` section alongside ExpertOps, DailyOps, Agentic
  Ops, DataOps, and Orchestration. Patterns pages are practitioner
  implementation references, not conceptual overviews or API references. The
  pattern is explicitly labeled experimental by the source.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series, the `gh aw` CLI, and all other `patterns/`
  pages in the corpus). Claims about pattern design, recommended workflow
  classes, and the deterministic relay principle are authoritative for the
  `gh aw` platform. The experimental designation indicates the pattern is
  under active development; implementation details may change.
- **Scope**: Covers the CorrectionOps design pattern: when to apply it,
  the three-step feedback loop, a two-surface architecture (production +
  Ops), the deterministic relay / semantic judgment design rule, four
  workflow class roles, and related pattern links (Staged Mode, SideRepoOps,
  MultiRepoOps, Safe Outputs, GitHub Tools). Does NOT cover: the full Safe
  Outputs permission model (see `docs-ghaw-how-they-work.md`), the rollout
  ladder for promoting workflow autonomy (see `docs-ghaw-safe-rollout.md`),
  fleet-level monitoring (see `docs-ghaw-agentic-ops.md`), or model retraining
  infrastructure (explicitly out of scope by design).

## Extracted Claims

### Claim 1: CorrectionOps is an experimental named gh-aw pattern for comparing AI workflow predictions with later human corrections and using the differences to iteratively improve the workflow system

- **Evidence**: Opening definition and experimental designation from the
  pattern page, extracted consistently across three independent WebFetch
  passes. The experimental label is explicit on the page.
- **Confidence**: emerging (first-party documentation; experimental designation
  is an authorial warning that the pattern's design is not yet settled)
- **Quote**: "an experimental pattern"
- **Our assessment**: "Experimental" in a gh-aw patterns page is a signal
  worth preserving in the corpus. The team operates 183+ production workflows;
  when they label a pattern experimental, it means the pattern is real and
  they are using it, but the implementation guidance may shift. For Ch02 and
  Ch04: cite CorrectionOps as a validated-but-evolving pattern rather than a
  settled design. Track the pattern page for updates as it matures. Compare
  with `docs-ghaw-agentic-ops.md` (Claim 1) which is a non-experimental
  fleet-monitoring pattern; CorrectionOps fills a different role (human
  correction feedback loop), not fleet monitoring.

### Claim 2: CorrectionOps solves a different problem than model retraining — it improves the workflow system surrounding the model (instructions, routing rules, thresholds, rollout decisions), not the model weights

- **Evidence**: Page explicitly contrasts CorrectionOps with model training/retraining.
  Stated consistently across all three WebFetch passes as a key distinction.
- **Confidence**: settled (first-party; the contrast with model retraining is
  the primary definitional framing of the pattern)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the phrasing
  varied across fetch passes)
- **Our assessment**: The three fetches all describe the same core claim but
  in varying phrasing: "CorrectionOps solves a different problem than model
  training" (1st fetch), "differs fundamentally from model retraining — it
  modifies the workflow system surrounding the AI rather than adjusting model
  weights, typically through instruction updates, routing modifications, or
  rollout governance" (3rd fetch). The substance is consistent. The practical
  implication: CorrectionOps outputs are changes to workflow prompts, routing
  logic, safe-outputs thresholds, or staged-mode decisions — not training data
  or fine-tuning runs. This positions it as a prompt engineering and workflow
  engineering feedback mechanism, not an ML feedback loop. For Ch04 (production
  patterns and feedback loops): this is the key distinction — CorrectionOps
  is for teams who cannot or will not retrain the model but still want to
  improve agent behavior over time using real human decisions.

### Claim 3: The pattern operates on a three-step loop: save what the workflow predicted, collect what humans later decided, use the difference to improve the workflow

- **Evidence**: Described as the core loop on the page. The 1st fetch returned
  this as a quoted passage.
- **Confidence**: emerging (appears in quotes in the 1st fetch; the 2nd and
  3rd fetches paraphrase the same three steps consistently, but phrasing
  differs slightly — marked emerging due to WebFetch AI-processing uncertainty)
- **Quote**: "Save what the workflow predicted, collect what humans later
  decided, use the difference to improve the workflow."
- **Our assessment**: The three-step framing maps cleanly to the safe rollout
  design rules in `docs-ghaw-safe-rollout.md`: step 1 (save prediction) =
  Claim 7 ("persist what the workflow predicted at decision time"); step 2
  (collect human truth) = Claim 8 ("record provenance" of corrections); step
  3 (use difference) = the improvement-without-retraining mechanism that safe
  rollout does not document. CorrectionOps closes the loop that safe rollout
  opens: safe rollout gets a workflow to production; CorrectionOps makes it
  better once there. For Ch04: name this three-step loop as the abstract
  structure of any feedback-loop improvement pattern, positioning CorrectionOps
  as the gh-aw implementation.

### Claim 4: CorrectionOps is most applicable when humans remain the final decision authority but you want the workflow to improve iteratively — typical use cases are labeling, classification, routing, moderation, approvals, and summaries humans later correct

- **Evidence**: "When to use" section enumerated across all three fetches
  consistently. The conditioner — humans remaining as decision authority —
  appears as a quoted passage in the 2nd fetch.
- **Confidence**: settled (first-party; use cases enumerated explicitly and
  consistent across fetches)
- **Quote**: "humans still make or correct the real decision, but you want
  the workflow to improve over time"
- **Our assessment**: The "humans remain authoritative" conditioner is
  architecturally significant: CorrectionOps does not fully automate the
  decision loop. It captures human overrides and decisions as training signal
  for the workflow, not for autonomous self-improvement. This connects to the
  safe rollout framing in `docs-ghaw-safe-rollout.md` Claim 6 ("production
  events and later trusted human actions should remain authoritative"). The
  six named use cases (labeling/classification, routing/prioritization,
  moderation/approval, summaries/recommendations) are the gh-aw team's
  validated contexts. For Ch02 (agent design and iteration): when a team's
  use case matches one of these six categories and humans make the final call,
  CorrectionOps is the pattern to consider for systematic improvement.

### Claim 5: The core design rule is to keep relays, snapshot resolution, diffing, and grouping deterministic while using the agent only for semantic judgment — not for reconstructing event history or inferring provenance

- **Evidence**: Stated as a key principle on the page. The phrase "relays,
  snapshot resolution, diffing, and grouping deterministic" appears consistently
  across all three fetch passes, with the 1st and 2nd fetches placing the phrase
  in direct quotes.
- **Confidence**: settled (first-party; the phrase is consistent and specific
  across three independent fetches — specificity of the enumeration suggests
  verbatim accuracy)
- **Quote**: "Keep relays, snapshot resolution, diffing, and grouping
  deterministic. Use the agent for semantic judgment, not for reconstructing
  event history or inferring provenance after the fact."
- **Our assessment**: This design rule is the most actionable claim in the
  source. It prevents a specific anti-pattern: using the LLM agent to figure
  out what happened (who made which correction, what the system predicted at
  the time, whether two correction events are related) instead of relying on
  deterministic code for those inferences. The LLM's job in CorrectionOps is
  exclusively semantic: "is this correction pattern significant enough to
  change the instructions?" — not "what did the system predict on day 7 and
  who corrected it?" The enumeration is precise: relays (data forwarding from
  production to ops) must be deterministic, as must snapshot resolution
  (finding the right prediction snapshot for a given human correction),
  diffing (computing the difference between prediction and correction), and
  grouping (aggregating corrections by type or topic). For Ch02 (harness
  engineering): document this as the canonical deterministic/agentic split
  rule for feedback-loop workflows — it extends the principle in
  `docs-ghaw-deterministic-agentic-patterns.md` Claim 1 to the specific
  correction-collection context.

### Claim 6: The recommended architecture maintains two long-lived surfaces: a production environment (authoritative source of events and human truth) and an Ops repository (hub for prediction storage, correction collection, comparison, reporting, and instruction updates)

- **Evidence**: Architectural description consistent across all three fetch
  passes. Production-as-authoritative and Ops-as-hub are stated as the
  two-surface model.
- **Confidence**: settled (consistent across three fetches; corroborated
  by the safe rollout note's three-repo shape which includes an ops repository
  with the same described role)
- **Quote**: (no direct quote; the description is consistent but phrasing
  varies across fetches)
- **Our assessment**: The two-surface model (production + ops) is a proper
  subset of the safe rollout three-repo shape in `docs-ghaw-safe-rollout.md`
  Claim 10 (production + ops + shadow). In safe rollout, the shadow target is
  a temporary write surface for validating behavior before production. In
  CorrectionOps, there is no shadow target — the pattern runs after deployment,
  in production, collecting human corrections to improve the already-deployed
  workflow. The ops repository role is identical: "persists predictions,
  collects corrections, publishes reports, and updates instructions" (from
  `docs-ghaw-safe-rollout.md` Claim 10). This is not a contradiction — the
  safe rollout ops repo role was designed with CorrectionOps in mind; they
  are the same repository serving different phases of the workflow lifecycle
  (rollout vs. ongoing improvement). For Ch04: the ops repository is a
  durable harness component, not a temporary artifact — it accumulates
  prediction/correction history over time and is the improvement surface
  for CorrectionOps.

### Claim 7: CorrectionOps involves four workflow classes: a thin relay, a prediction workflow, a review/compare/decide workflow, and an optional deterministic collector

- **Evidence**: Implementation structure described across all three fetches,
  with consistent four-part decomposition: (1) relay, (2) prediction
  workflow, (3) compare/review/decide workflow, (4) optional collector. The
  names vary slightly across fetches.
- **Confidence**: emerging (four-part structure is consistent; exact workflow
  names are from AI-processed page content, not raw source)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The thin relay is the deterministic bridge between
  production and ops — it forwards stable facts (what the workflow predicted,
  when, for which event) without any agentic interpretation. The prediction
  workflow applies current rules (current prompt/instructions/thresholds) and
  persists a snapshot at decision time, implementing the safe rollout design
  rule from `docs-ghaw-safe-rollout.md` Claim 7 ("persist what the workflow
  predicted at decision time"). The review/compare/decide workflow is the
  semantic agent: it reads the accumulated prediction/correction pairs,
  assesses significance, generates improvement proposals, and updates
  instructions or routing rules when the evidence is strong enough. The
  optional collector is a separate deterministic job for gathering correction
  evidence from non-workflow sources (e.g., human-edited labels, moderation
  queue outcomes). The four-class decomposition is the most architecturally
  concrete element of the pattern. For Ch02 (agent design): document these
  four roles as the standard workflow decomposition for any feedback-loop
  improvement workflow on gh-aw.

### Claim 8: The compare/report/decide workflow checks human truth and updates instructions only when correction evidence is strong — it applies a threshold before triggering changes

- **Evidence**: Described in the architectural overview across fetch passes:
  the compare/review/decide workflow "checks human truth and updates when
  evidence is strong" (1st fetch). The threshold conditioner is consistent
  across fetches.
- **Confidence**: emerging (threshold conditioner is consistent but no
  specific threshold values are documented on the page)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The "when evidence is strong" qualifier is critical
  for production safety: a single human correction might be idiosyncratic,
  user error, or context-specific. The pattern deliberately requires
  accumulated evidence before updating instructions. This is analogous to
  the safe rollout escalation model in `docs-ghaw-safe-rollout.md` Claim 2
  (build evidence at each rung before promoting). The page does not specify
  what "strong evidence" means quantitatively; teams will need to configure
  their own thresholds. The semantic agent (compare/decide workflow) makes
  the evidence-strength judgment — this is the appropriate use of agentic
  judgment per Claim 5. For Ch04: recommend that teams deploying CorrectionOps
  configure explicit evidence thresholds (minimum N corrections per class,
  minimum X% agreement across correctors) to prevent noise-driven instruction
  updates.

## Concrete Artifacts

### CorrectionOps Three-Step Loop (from source)

```
Core feedback loop:

Step 1: Save what the workflow predicted
  → At decision time, the prediction workflow persists a snapshot
  → The relay forwards stable production facts to the ops repository
  → Deterministic — no AI interpretation at capture time

Step 2: Collect what humans later decided
  → The ops repository collects human corrections as they occur
  → Provenance is recorded (who corrected, manual vs. automated)
  → Optional: a separate deterministic collector captures corrections
    from non-workflow sources

Step 3: Use the difference to improve the workflow
  → The compare/review/decide workflow diffs predictions against corrections
  → The AI agent applies semantic judgment: Is this evidence significant?
  → Updates are applied to instructions, routing rules, thresholds,
    or rollout decisions — NOT to model weights
```

*Source: `patterns/correction-ops` — Core Concept / Basic Loop section*

### Two-Surface Architecture (from source description)

```
Production surface (authoritative):
  - Emits live events
  - Records authoritative human decisions
  - Thin relay forwards stable facts to ops (deterministic)

Ops surface (improvement hub):
  - Stores prediction snapshots (written by prediction workflow)
  - Collects correction evidence (via relay + optional collector)
  - Compares predictions against corrections (deterministic diffing)
  - Reports on accuracy and trends
  - Updates workflow instructions, routing, thresholds (agentic decision)
  - Governs rollout decisions
```

*Source: `patterns/correction-ops` — Architecture section*

### Four Workflow Classes (from source description)

```
Class 1: Thin relay
  Role: Forward stable facts from production to ops
  Rule: DETERMINISTIC — no AI, no interpretation, no inference
  Content: What happened (event), what was predicted (snapshot ref),
           when, for which entity

Class 2: Prediction workflow
  Role: Apply current rules; persist prediction snapshot at decision time
  Rule: DETERMINISTIC snapshot capture; may use agent for the prediction
        itself, but the snapshot write must be deterministic
  Content: Prediction + timestamp + context → stored in ops

Class 3: Review/compare/decide workflow
  Role: Check human truth; compare against predictions; update when strong
  Rule: DETERMINISTIC diffing and grouping; AGENTIC for semantic judgment
  Content: Reads prediction/correction pairs; decides whether to update;
           writes instruction changes or routing updates

Class 4: Optional deterministic collector
  Role: Capture correction evidence from non-workflow sources
  Rule: DETERMINISTIC — shell steps, not agent
  Content: Human-edited labels, moderation outcomes, approval decisions
```

*Source: `patterns/correction-ops` — Implementation Components section*

### Design Rule (from source)

```
Deterministic responsibilities (no AI):
  - Relay: forwarding stable facts to ops
  - Snapshot resolution: matching a correction to its prediction snapshot
  - Diffing: computing prediction-vs-correction differences
  - Grouping: aggregating corrections by category or entity type

Agentic responsibility (AI only):
  - Semantic judgment: Is this correction pattern significant?
    Does the evidence warrant an instruction update?
    If so, what should change?

Anti-pattern (prohibited by the design rule):
  - Using the agent to reconstruct event history
  - Using the agent to infer provenance after the fact
  - Using the agent to determine what was predicted and when
```

*Source: `patterns/correction-ops` — Key Principle section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-safe-rollout.md` Claim 7 ("If later comparison matters,
    persist what the workflow predicted at decision time. Do not reconstruct
    predictions from logs."): CorrectionOps is the pattern that requires this
    rule and operationalizes it via the thin relay and prediction workflow.
    The safe rollout design rule exists because CorrectionOps needs it to
    function — prediction snapshots must be explicit so the compare/decide
    workflow has a reliable ground truth to diff against.
  - `docs-ghaw-safe-rollout.md` Claim 8 ("Not every later edit should count
    as trustworthy truth. Record provenance such as actor type, manual versus
    automated source, trust status, and origin repository role."): CorrectionOps
    depends on provenance to distinguish real human corrections (high-signal)
    from automated overwrites (low- or negative-signal). Without provenance,
    the correction evidence is ambiguous and the compare/decide workflow
    cannot apply the "only update when evidence is strong" threshold reliably.
  - `docs-ghaw-safe-rollout.md` Claim 6 ("Do not let the evaluation surface
    become the new source of truth. Production events and later trusted human
    actions should remain authoritative."): CorrectionOps's two-surface
    architecture explicitly honors this rule — production stays authoritative;
    the ops surface is for improvement, not for replacing production truth.
  - `blog-langchain-human-judgment-improvement-loop.md` Claim 5 ("teams get
    more leverage when humans help design and calibrate automated evaluators,
    rather than manually reviewing large volumes of agent outputs"): Both
    sources converge on the same insight from different angles — LangChain
    says encode human judgment into evaluators; CorrectionOps says collect
    human corrections and use them to update workflow instructions. Both are
    mechanisms for making human judgment scale without requiring per-output
    manual review.
  - `blog-langchain-human-judgment-improvement-loop.md` Claim 11 ("After
    launch, you gain access to a much better source of test cases: real
    production data."): CorrectionOps's core mechanism is precisely this —
    it uses real production human corrections (not synthetic test cases) as
    the improvement signal.

- **Extends**:
  - `docs-ghaw-safe-rollout.md` Claim 10 (three-repo shape: production + ops
    + shadow, where ops "persists predictions, collects corrections, publishes
    reports, and updates instructions"): CorrectionOps is the named pattern
    that operationalizes the ops repository role. The safe rollout guide
    describes the role in one line as part of a rollout-phase layout; this
    pattern makes it the primary architectural surface and provides the four
    workflow classes that populate it. Read together: safe rollout is the
    framework for earning trust during deployment; CorrectionOps is the
    mechanism for improving quality after deployment.
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 1 (three-stage
    hybrid pipeline: deterministic jobs → agent → safe outputs as the named
    GHAW architecture for combining deterministic computation with AI
    reasoning): CorrectionOps applies this same architectural principle to
    the correction-collection domain. The thin relay and snapshot-resolution
    steps are the deterministic jobs; the compare/decide workflow is the
    agent; instruction updates are the safe outputs. The design rule in
    Claim 5 here is the correction-specific instantiation of the broader
    deterministic/agentic split.
  - `blog-langchain-human-judgment-improvement-loop.md` Claim 7 ("the
    agent improvement flywheel" — development → post-deployment → continuous
    refinement): CorrectionOps is the gh-aw native implementation of phase 3
    (continuous refinement). The LangChain post covers this at an abstract,
    platform-agnostic level; CorrectionOps provides the specific workflow
    architecture for teams on gh-aw.

- **Contradicts**: None identified. The ops repository role in CorrectionOps
  is consistent with the safe rollout three-repo shape; the deterministic
  relay principle is consistent with the deterministic-agentic patterns note;
  the human-corrections-as-signal principle is consistent with the LangChain
  improvement loop. No existing source note makes claims that materially
  oppose CorrectionOps at the MINER.md §4a threshold. No contradiction
  issue filed.

- **Novel**:
  - **Named gh-aw pattern for feedback-loop improvement without model
    retraining** (Claims 1–2): No existing corpus note describes a specific,
    named workflow pattern for collecting human corrections and using them to
    improve agent workflow instructions/routing/thresholds. The LangChain
    post covers the concept abstractly; safe rollout mentions the ops
    repository role briefly. This is the first corpus entry naming and
    designing CorrectionOps as a first-class pattern.
  - **Deterministic/agentic split rule for correction workflows** (Claim 5):
    The specific enumeration — relays, snapshot resolution, diffing, and
    grouping must be deterministic; semantic judgment is the only agentic
    responsibility — is not in any existing corpus note. The general
    deterministic/agentic split principle exists in
    `docs-ghaw-deterministic-agentic-patterns.md`, but the correction-specific
    assignment of responsibilities is new.
  - **Four workflow classes for feedback collection** (Claim 7): No existing
    note documents the thin relay / prediction workflow / review-decide
    workflow / optional collector decomposition. This is the first corpus
    entry giving a concrete workflow structure for a human-correction
    feedback loop in the gh-aw context.
  - **"Experimental" designation as a corpus signal** (Claim 1): This is
    the first gh-aw pattern in the corpus explicitly labeled experimental
    by the team. Other patterns (Agentic Ops, DataOps, ExpertOps, DailyOps)
    carry no such qualifier. The experimental designation changes how the
    guide should cite the pattern — not as settled best practice but as
    emerging guidance to revisit as the pattern matures.
  - **Improvement scope definition** (Claim 2): The explicit claim that
    CorrectionOps updates instructions, routing rules, thresholds, and
    rollout decisions — and explicitly not model weights — defines the
    boundary of prompt-engineering-driven improvement vs. ML-driven
    improvement. This boundary is not articulated in any existing corpus note.

## Guide Impact

- **Chapter 02 (Agent Design and Iteration)**:
  - Add CorrectionOps as the named gh-aw pattern for iterative improvement
    via human corrections. Position it as the post-deployment companion to
    the safe rollout ladder: safe rollout builds trust during deployment;
    CorrectionOps captures real-world corrections to improve the workflow
    after deployment. Mark it as experimental.
  - Add the deterministic/agentic split rule for feedback-loop workflows
    (Claim 5): in any workflow that compares predictions to later human
    corrections, the relay, snapshot resolution, diffing, and grouping must
    be deterministic. Only the evidence-significance judgment is agentic.
    This is the most directly actionable harness engineering claim in the source.
  - Add the four workflow classes (thin relay, prediction workflow,
    review/compare/decide, optional collector) as the reference decomposition
    for any gh-aw feedback-loop workflow. Teams can adapt this structure
    without inventing it from scratch.

- **Chapter 04 (Production Patterns and Feedback Loops)**:
  - CorrectionOps is the primary gh-aw answer to the question "how do we
    improve agent behavior in production without retraining?" Position it
    explicitly as the improvement-without-retraining pattern, distinct from
    ML feedback loops (which require model weight changes) and from manual
    prompt engineering iterations (which lack systematic correction evidence).
  - Add the evidence-threshold requirement (Claim 8): instruction updates
    should only occur when correction evidence is strong. Teams deploying
    CorrectionOps should configure explicit evidence thresholds (minimum
    corrections per class, minimum agreement rate) to prevent single-correction
    noise from driving instruction changes.
  - Cross-reference the three-step loop (Claim 3) with the LangChain
    improvement flywheel (`blog-langchain-human-judgment-improvement-loop.md`
    Claim 5 / the three-phase model) — both describe the same feedback-loop
    principle; CorrectionOps is the gh-aw implementation and the LangChain
    post is the platform-agnostic framing.
  - Note that the ops repository role (Claim 6) is the same ops repository
    described in the safe rollout guide's three-repo shape — if a team has
    already set up a safe rollout ops repository, it can become the
    CorrectionOps ops surface without duplicating infrastructure.

## Extraction Notes

1. **Source content is AI-processed via WebFetch**: The `github.github.com/gh-aw`
   documentation site is an SPA; WebFetch renders content through an AI model
   before returning it. Three independent WebFetch passes were made to the
   `patterns/correction-ops` page. Where a phrase appeared consistently across
   passes and/or appeared inside quotation marks in a pass, it is cited as a
   direct quote. Where phrasing varied or appeared to be AI paraphrase, the
   claim is marked "(no direct quote; see paraphrase in Our assessment)" per
   MINER.md §2a. Quotes should be verified against the live source before
   publishing in the guide.

2. **Experimental designation**: All three fetch passes are consistent that
   the pattern carries an "experimental" label from the gh-aw team. This is
   the first gh-aw patterns page in the corpus with this designation. The
   experimental label is preserved in Claim 1 and the confidence_overall
   is set to `emerging` (rather than the `settled` that non-experimental
   first-party gh-aw patterns typically warrant).

3. **Related pages linked from the source**: The page links to Staged Mode,
   SideRepoOps, MultiRepoOps, Safe Outputs, and GitHub Tools as related
   documentation. Of these, Staged Mode and Safe Outputs are partially covered
   by `docs-ghaw-how-they-work.md` and `docs-ghaw-staged-mode-reference.md`.
   SideRepoOps and MultiRepoOps do not yet have dedicated corpus source notes.
   These linked pages were not followed — they are either already covered or
   out of scope for this extraction.

4. **No YAML artifacts on the pattern page**: Like other `patterns/` pages
   (cf. `docs-ghaw-agentic-ops.md` Extraction Note 3), the CorrectionOps
   pattern page appears to describe the pattern in prose and workflow-class
   terms rather than providing full YAML frontmatter examples. The Concrete
   Artifacts section here is reconstructed from consistent prose descriptions
   across three fetches, not extracted from verbatim YAML blocks. There is no
   reference implementation repository mentioned (unlike Agentic Ops, which
   links to `githubnext/agentic-ops`).

5. **No contradictions to file**: Reviewed all GHAW-related source notes
   and the broader corpus. The safe rollout ops repository role is consistent
   with, not contradictory to, CorrectionOps's ops surface role — they
   describe the same repository in different lifecycle phases. The
   deterministic relay principle is consistent with `docs-ghaw-deterministic-agentic-patterns.md`.
   No claims in this source materially oppose existing notes at the MINER.md
   §4a filing threshold.
