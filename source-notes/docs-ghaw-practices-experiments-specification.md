---
source_url: https://github.github.com/gh-aw/practices/experiments-specification
source_type: docs
title: "GitHub Agentic Workflows: A/B Experiments Specification (v1.0.0)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-17
last_checked: 2026-05-17
status: current
confidence_overall: emerging
issue: "#788"
---

# GitHub Agentic Workflows: A/B Experiments Specification (v1.0.0)

> Formal normative specification (v1.0.0, Draft) for the gh-aw A/B experiment
> system — establishes MUST/MUST NOT requirements for schema validation, variant
> selection algorithms, date-range gating, state persistence contracts, expression
> compiler integration, audit CLI interface, statistical reporting, simultaneous
> experiment constraints, and security requirements; organized into three conformance
> levels (Basic, Standard, Complete). Deepens and formalizes the practices guide
> already captured in `docs-ghaw-practices-experiments.md`.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows formal specification at
  `practices/experiments-specification` — a W3C-style normative document distinct
  from the `practices/experiments` how-to guide. Uses MUST/MUST NOT/SHOULD language
  throughout. Status: Draft; Version: 1.0.0. This is a sibling page to the
  practices guide, providing formal system contracts rather than authoring guidance.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research). Because this is a normative specification,
  MUST/MUST NOT requirements describe actual implementation contracts — not
  suggestions or best practices. The corrective item (R-SELECT-006) that supersedes
  a prior ADR demonstrates this is an actively maintained specification used for
  implementation conformance.
- **Scope**: Covers the full formal contract for the A/B experiment system: §4
  (frontmatter schema), §5 (variant selection algorithms), §6 (date-range gating),
  §7 (state persistence), §8 (expression integration), §9 (OTEL attribute
  emission), §10 (audit CLI), §11 (statistical analysis and reporting), §12
  (simultaneous experiments), §13 (security). Defines three conformance levels
  (Basic, Standard, Complete). Does NOT cover: authoring workflow guidance or
  rich YAML examples (see `docs-ghaw-practices-experiments.md`); OTEL span
  emission details (see `docs-ghaw-agentic-ops.md` Claim 12).

## Extracted Claims

### Claim 1: The experiments-specification is a formal normative document (v1.0.0, Draft) with MUST/MUST NOT requirements organized into three conformance levels — Basic, Standard, and Complete

- **Evidence**: Version and status stated explicitly in the document header.
  Conformance level definitions cite specific section numbers and use
  "satisfies all MUST/MUST NOT requirements in §N" language throughout.
- **Confidence**: settled (first-party; the version, status, and conformance
  structure are explicitly stated)
- **Quote**: "**Version**: 1.0.0  **Status**: Draft"
- **Our assessment**: The existence of this formal spec alongside the practices
  guide signals a two-tier documentation model: the practices guide for authoring
  guidance, the specification for implementation conformance. Practitioners do
  not need to read the spec in detail for day-to-day use, but teams building
  tooling on top of gh-aw (e.g., custom reporting workflows, CI integration) must
  satisfy the appropriate conformance level. For Ch04: note that the spec defines
  what a *conformant* A/B experiment implementation must do, enabling practitioners
  to audit their own setups against a formal baseline.

### Claim 2: Conformance is defined at three levels — Level 1 (Basic: schema + selection + expression), Level 2 (Standard: adds gating + persistence + audit CLI), Level 3 (Complete: adds statistical analysis + multi-experiment handling)

- **Evidence**: The specification explicitly defines three conformance levels
  with section references.
- **Confidence**: settled (first-party; definitions are explicit and cite section numbers)
- **Quote**: "**Level 1 — Basic**: Satisfies all MUST/MUST NOT requirements in §4, §5, §8, and §9"
- **Our assessment**: The three-level structure is the specification's roadmap for
  incremental adoption. A team running a quick one-off experiment needs only Level 1.
  A team running production experiments with state persistence needs Level 2.
  A team making automated promotion decisions based on statistical results needs
  Level 3. For Ch04: present the three conformance levels as the progression path
  for experiment infrastructure maturity — do not require Level 3 from teams who
  are still at the exploration phase.

### Claim 3: The control variant is formally defined as the first variant in the declared array — used as the statistical baseline in analysis and as the fallback when date gating is active

- **Evidence**: The specification gives an explicit definition for "control variant."
  The date-gating fallback behavior (§6) is linked to this definition.
- **Confidence**: settled (first-party; explicitly defined in the specification)
- **Quote**: "The first variant in the declared `variants` array; used as baseline
  and as fallback during date gating."
- **Our assessment**: The control variant definition has practical ordering
  consequences: practitioners MUST place their baseline (e.g., the existing
  prompt) first in the `variants` array. A common mistake would be listing the
  new variant first (e.g., `variants: [new_style, concise]`) — which would make
  the new variant the control and the existing behavior the treatment. This matters
  especially when `start_date` is in the future (before the experiment is active,
  all traffic goes to the first-listed variant). For Ch04: document that variant
  array order is significant — the first entry is the control, not arbitrary.

### Claim 4: Round-robin selection MUST choose the variant with the lowest cumulative invocation count; when two or more variants are tied, the selection MUST be uniformly random among tied variants

- **Evidence**: §5.1 provides normative MUST/MUST requirements for both the
  selection rule and the tie-breaking rule.
- **Confidence**: settled (first-party normative requirement; the MUST language
  is explicit for both behaviors)
- **Quote**: "When `weight` is absent or invalid (§5.2), implementations **MUST** select
  the variant with the lowest cumulative invocation count stored in `state.json`."
  And: "When two or more variants share the lowest count — including the initial
  state where all counts are zero — implementations **MUST** break ties by selecting
  uniformly at random from the tied variants."
- **Our assessment**: The practices guide described the lowest-count algorithm
  correctly (see `docs-ghaw-practices-experiments.md` Claim 4), but did not capture
  the formal tie-breaking requirement. The uniform random tie-breaking is
  significant for multi-variant experiments (K≥3): on the first run, all variants
  have count 0 and one is selected randomly — giving each equal first-run probability
  regardless of declaration order. This prevents the first-listed variant from
  systematically receiving more early traffic than others. For Ch04: add the
  tie-breaking rule to any explanation of the balancing algorithm to prevent
  practitioners from assuming declaration order affects early distribution.

### Claim 5: Weighted selection MUST use probability proportional to weight values AND MUST increment invocation counters after selection — correcting ADR-29618 Rule 9 which incorrectly prohibited counter increments for weighted selection

- **Evidence**: §5.2 defines the weighted selection requirement. Corrective item
  R-SELECT-006 explicitly supersedes ADR-29618 Rule 9 and provides the normative
  rationale. The reference implementation (`pick_experiment.cjs`) already
  implements the corrected behavior.
- **Confidence**: settled (first-party normative correction; explicitly identifies
  the prior ADR and supersedes it with normative language)
- **Quote**: "**R-SELECT-006**: Weighted random selection **MUST** increment the
  invocation counter for the selected variant before persisting state. **Note
  (normative correction)**: ADR-29618 Rule 9 incorrectly stated that weighted
  selection 'MUST NOT increment any variant counter.' This rule is hereby
  superseded."
- **Our assessment**: R-SELECT-006 is a breaking correction to a prior
  specification decision. Any team that built custom experiment tooling based on
  ADR-29618 Rule 9 (no counter increments for weighted selection) has a conformance
  defect — their `min_samples` progress tracking and per-run history will be
  incorrect. The corrective item notes the reference implementation already
  implements the correct behavior, meaning the runtime itself has been fixed;
  only custom tooling outside the reference implementation is at risk. For Ch04:
  note R-SELECT-006 explicitly when documenting weighted selection — practitioners
  building custom reporters or auditors must ensure counter increments are included.

### Claim 6: Date-range gating returns the control variant without incrementing any counters when a run falls outside the `start_date`/`end_date` window — keeping experiment state clean during inactive periods

- **Evidence**: §6 describes date gating behavior. The "without incrementing counters"
  rule preserves statistical integrity during the inactive period.
- **Confidence**: settled (first-party; the control-variant-fallback and
  no-counter-increment behaviors are documented in the spec)
- **Quote**: (no single direct prose quote covers both behaviors together; see
  paraphrase in Our assessment)
- **Our assessment**: The date-gating behavior has a subtle but important consequence:
  workflow runs during inactive periods (before `start_date`, after `end_date`) do
  not pollute the experiment's variant counts. All traffic during inactive periods
  goes to the control (first variant), and when the experiment window opens, the
  round-robin algorithm starts from a clean state. This means practitioners can
  deploy a workflow with a future `start_date` without worrying that pre-experiment
  runs contaminate their sample. For Ch04: document date gating as the mechanism
  for scheduling experiments — include the control-fallback rule so practitioners
  understand what users experience before the experiment starts.

### Claim 7: The `state.json` persistence format has a formal two-section structure: `counts` (per-variant invocation totals) and `runs` (ordered per-run assignment history with run_id, timestamp, and assignments map)

- **Evidence**: §7 defines the state.json structure with explicit JSON schema.
  The `runs` array with per-run assignment history is a new structural detail
  not captured in the practices guide.
- **Confidence**: settled (first-party normative schema; the JSON structure is
  explicitly defined)
- **Quote**: (no direct prose quote; the structure is specified as a JSON schema;
  see Concrete Artifacts section)
- **Our assessment**: The `runs` array is the audit trail — it records every
  run's assignment, enabling statistical reporting to use actual observed
  assignments rather than inferring them from count deltas. This is specifically
  mandated by the specification: reporting must use `state.runs` assignments,
  not count-delta inference (a corrective item). For Ch04: document `state.json`
  as the experiment ledger — practitioners building custom analysis workflows
  should read `runs` for assignment history, not reconstruct assignments from `counts`.

### Claim 8: The expression compiler rewrites `${{ experiments.<name> }}` to `steps.pick-experiment.outputs.<name>` and also exposes assignments as `GH_AW_EXPERIMENTS_<NAME>` environment variables (uppercased)

- **Evidence**: §8 documents expression integration. The environment variable
  form (`GH_AW_EXPERIMENTS_<NAME>`) is a new detail not documented in the
  practices guide.
- **Confidence**: settled (first-party; compiler rewrite target and env var
  naming convention are specified)
- **Quote**: (no direct prose quote; the compiler rewrite target
  `steps.pick-experiment.outputs.<name>` and env var pattern are specified
  in §8)
- **Our assessment**: The `GH_AW_EXPERIMENTS_<NAME>` environment variable form is
  significant for shell steps that cannot use YAML template syntax. Shell scripts
  in `run:` steps can read `$GH_AW_EXPERIMENTS_PROMPT_STYLE` without needing
  to reference `${{ steps.pick-experiment.outputs.prompt_style }}` directly.
  The uppercasing convention means experiment names with mixed case (e.g.,
  `promptStyle`) become `GH_AW_EXPERIMENTS_PROMPTSTYLE`. For Ch04: document the
  env var form as the shell-accessible alternative to template syntax, and note
  the uppercasing convention to prevent casing bugs in shell scripts.

### Claim 9: The audit CLI has three formal MUST requirements: `--experiment` MUST filter by named experiment; `--variant` combined with `--experiment` MUST filter by variant value; `--variant` used without `--experiment` MUST fail with non-zero exit code and a suggestion to add `--experiment`

- **Evidence**: §10.1 states all three requirements with explicit MUST language.
- **Confidence**: settled (first-party normative requirements; MUST language is
  explicit for all three behaviors)
- **Quote**: "The `gh aw audit` command **MUST** accept an `--experiment <name>` flag
  that filters runs to those with a variant assignment for the named experiment."
  And: "`--variant` used without `--experiment` **MUST** cause a non-zero exit code
  with an error message that includes a suggestion to add `--experiment`."
- **Our assessment**: The non-zero exit code requirement for misuse (`--variant`
  without `--experiment`) is important for CI scripts that wrap audit commands —
  a silent failure would allow pipelines to proceed even when an invalid audit
  query was made. The mandatory error message with a suggestion is a UX
  requirement, ensuring practitioners understand why their command failed.
  For Ch04 (and any audit-workflow documentation): present the `--experiment`
  flag as required context for all variant-filtered queries; the CLI enforces this.

### Claim 10: Guardrail evaluation is INFORMATIVE at the schema level — the compiler does not enforce guardrails at compile time — but reporting tools MUST issue an ABANDON recommendation when any guardrail threshold is violated

- **Evidence**: §4 states the informative nature of guardrail enforcement.
  §11 specifies the ABANDON recommendation requirement for reporting tools.
  The threshold format constraint is a normative schema rule.
- **Confidence**: settled (first-party; both the non-enforcement at compile time
  and the ABANDON requirement for reporting tools are explicitly stated)
- **Quote**: "Guardrail evaluation is **INFORMATIVE** at the schema level — the
  compiler does not enforce guardrails at compile time." And the threshold
  must match: "The `threshold` **MUST** match the pattern
  `^(>=|<=|==|>|<)-?\d+(\.\d+)?$`"
- **Our assessment**: This clarifies the uncertainty flagged in
  `docs-ghaw-practices-experiments.md` Claim 9, which was marked `emerging` and
  noted that "the specific enforcement behavior — halt vs. alert — is inferred."
  The specification resolves this: guardrails do NOT halt or trigger an alert at
  compile time; they are only evaluated by reporting tools at analysis time, where
  a threshold violation forces an ABANDON recommendation. Practitioners who
  expected compile-time rejection of dangerous experiments (e.g., a variant that
  exceeds a cost threshold) must implement guardrail evaluation in their reporting
  workflow, not rely on the compiler. For Ch04: clarify that guardrails are an
  analysis-phase safety gate, not a deployment-phase gate.

### Claim 11: Statistical reporting MUST NOT issue a PROMOTE recommendation until ALL variants reach min_samples runs; for K≥3 variants, SHOULD apply Bonferroni correction (α_adjusted = 0.05 / (K − 1)) for pairwise comparisons against control

- **Evidence**: §11 defines both requirements with MUST NOT and SHOULD language.
  The Bonferroni formula is explicitly given.
- **Confidence**: settled (first-party normative requirements; both rules are
  explicitly stated with normative language)
- **Quote**: "Reporting tools **MUST NOT** issue a PROMOTE recommendation for any
  variant until all variants in the experiment have accumulated at least
  `min_samples` runs (or 20 if `min_samples` is not declared)."
  And: "When an experiment declares K ≥ 3 variants and reporting tools perform
  pairwise comparisons against the control, the significance threshold **SHOULD**
  be adjusted using the Bonferroni correction: `α_adjusted = 0.05 / (K − 1)`."
- **Our assessment**: The all-variants-must-reach-min_samples rule is stronger
  than it might appear: if variant A reaches min_samples quickly but variant B
  is undersampled (e.g., because weighted selection gives it less traffic),
  the PROMOTE gate is blocked for all variants until the slowest one catches up.
  This prevents premature promotion of a variant that looks good only because
  it ran on a favorable traffic sample. The Bonferroni correction (SHOULD, not
  MUST) addresses the multiple comparisons problem in multi-variant tests —
  without it, the false positive rate grows with the number of pairwise comparisons.
  For Ch04: document the PROMOTE gate as the minimum-evidence bar for variant
  selection decisions; document Bonferroni as the recommended correction for
  multi-variant experiments.

### Claim 12: Simultaneous experiments must each be assigned independently; SHOULD NOT exceed three active experiments per workflow; mixed storage modes (some repo, some cache) are not supported; interaction effects MUST be noted in reports

- **Evidence**: §12 covers all four rules with SHOULD NOT and MUST language where
  applicable. The mixed-storage constraint is an explicit limitation.
- **Confidence**: settled (first-party normative requirements; all four rules are
  explicitly stated)
- **Quote**: "Implementations **SHOULD NOT** run more than three experiments
  simultaneously in a single workflow. When more than three experiments are active,
  a compile-time warning **SHOULD** be emitted."
  And: "Reporting tools **MUST** note in their output when multiple experiments were
  simultaneously active on runs included in the analysis window, to alert reviewers
  to potential confounding."
- **Our assessment**: The three-experiment soft limit and the interaction-effect
  disclosure requirement address the same underlying problem: when multiple
  experiments run simultaneously on the same workflow invocation, the variant
  assignments are correlated. A workflow run with variant A of experiment 1 and
  variant X of experiment 2 cannot attribute any observed outcome difference
  purely to experiment 1 or experiment 2. The MUST for interaction-effect disclosure
  in reports makes this confounding visible rather than hiding it. For Ch04: warn
  practitioners that running many simultaneous experiments degrades the
  interpretability of each — encourage one or at most two concurrent experiments
  per workflow during active experimentation phases.

### Claim 13: Security requirements mandate that OTEL experiment attributes may leak variant names to tracing backends; repo storage mode requires contents:write; reporting workflows MUST minimize permissions and request issues:write or discussions:write only for workflows that post comments

- **Evidence**: §13 states all three security requirements explicitly.
- **Confidence**: settled (first-party normative security requirements)
- **Quote**: "Experiment assignments exported as OTEL resource attributes (§9.3)
  may be visible in distributed-tracing backends. Variant names and experiment
  names **SHOULD NOT** embed sensitive information."
  And: "The `repo` storage mode requires `contents: write`. Workflows **SHOULD**
  limit all other permissions to `read` to minimize the blast radius of a
  compromised token."
- **Our assessment**: The OTEL leakage risk is real but subtle: if experiment names
  or variant strings embed business-sensitive terms (e.g., `feature: [gdpr_audit_v2,
  legacy_flow]`), those strings appear in distributed traces and may be visible to
  anyone with access to the tracing backend. The minimum-permissions rule for repo
  mode is standard least-privilege hygiene — but the specification adds a nuance:
  reporting workflows (which post results to issues/discussions) must request
  write permissions separately from the experiment-running workflow itself, keeping
  the two permission surfaces distinct. For Ch02 (Harness Engineering): include
  the permissions model for experiments in any security checklist for agentic
  workflow deployment.

## Concrete Artifacts

### state.json Formal Structure

From `https://github.github.com/gh-aw/practices/experiments-specification` §7:

```json
{
  "counts": {
    "<experiment_name>": {
      "<variant>": "<integer>"
    }
  },
  "runs": [
    {
      "run_id": "<string>",
      "timestamp": "<ISO-8601>",
      "assignments": {
        "<experiment_name>": "<variant>"
      }
    }
  ]
}
```

### Conformance Level Definitions

From `https://github.github.com/gh-aw/practices/experiments-specification`:

```
Level 1 — Basic:    §4 (schema), §5 (selection), §8 (expression), §9 (OTEL attrs)
Level 2 — Standard: Level 1 + §6 (date gating), §7 (state persistence), §10 (audit CLI)
Level 3 — Complete: Level 2 + §11 (statistical analysis), §12 (multi-experiment)
```

### Statistical Analysis Type Values

From `https://github.github.com/gh-aw/practices/experiments-specification` §11.2:

```
analysis_type values:
  t_test          — Welch's two-sample t-test (does not assume equal variance)
  mann_whitney    — Mann-Whitney U non-parametric rank test
  proportion_test — Two-proportion z-test
  bayesian_ab     — Bayesian A/B analysis (posterior probability of superiority)

Default when analysis_type absent:
  - Binary outcomes (success/failure) → two-proportion z-test
  - Continuous metrics (e.g., duration) → Welch's t-test
```

### Guardrail Threshold Pattern Constraint

From `https://github.github.com/gh-aw/practices/experiments-specification` §4:

```
threshold MUST match: ^(>=|<=|==|>|<)-?\d+(\.\d+)?$
Examples: ">=0.95", "<=100", ">0", "<-5.5"
```

### Corrective Item R-SELECT-006

From `https://github.github.com/gh-aw/practices/experiments-specification`:

```
R-SELECT-006: Weighted random selection MUST increment the invocation counter
for the selected variant before persisting state.

Note (normative correction): ADR-29618 Rule 9 incorrectly stated that weighted
selection "MUST NOT increment any variant counter." This rule is hereby superseded.
Counter increments for weighted selection are required to enable min_samples
progress tracking and accurate per-run history. The reference implementation
(pick_experiment.cjs) already implements this correct behavior by calling
recordVariant unconditionally after both selection paths.
```

### Audit CLI Formal Interface

From `https://github.github.com/gh-aw/practices/experiments-specification` §10:

```bash
# Filter runs by experiment name (MUST be supported)
gh aw audit --experiment <name>

# Filter by experiment AND specific variant (MUST be supported)
gh aw audit --experiment <name> --variant <value>

# --variant without --experiment MUST fail with non-zero exit code
# and error message suggesting to add --experiment
gh aw audit --variant <value>   # → non-zero exit
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-practices-experiments.md` Claims 1–10: This specification
    formalizes the same feature set documented in the practices guide. Claims 1
    (experiments section enables A/B testing), 4 (round-robin lowest-count
    selection), 5 (weighted selection), 6 (repo vs. cache storage), and 9
    (guardrail_metrics field) are all confirmed here with MUST/MUST NOT requirements.
    The specification adds normative precision to what the practices guide described
    behaviorally.
  - `docs-ghaw-frontmatter-full-reference.md` Claim 8 ("The experiments field
    supports A/B testing with variants and configurable storage — enabling
    statistical workflow iteration with 'cache' (ephemeral) or 'repo' (persistent)
    storage"): the two storage backends and their durability characteristics are
    confirmed; this spec adds the state.json structure, the repo branch naming
    (`experiments/{sanitizedWorkflowID}`), and the formal persistence contract.
  - `docs-ghaw-agentic-ops.md` Claim 12 ("The audit workflow integrates OTLP
    observability with custom `gh_aw.experiment.*` span attributes, enabling A/B
    experiment variant tracking in Datadog, Honeycomb, or any OTLP backend"):
    §9 and §13 of this spec document the OTEL attribute emission (covered in §9.3)
    and the security constraint on attribute content; both notes are consistent on
    the OTEL integration mechanism.
  - `docs-ghaw-artifacts-reference.md` Claim 6 ("The `experiment` artifact is only
    present when workflows declare A/B experiments in frontmatter — it stores
    per-variant invocation counters for load balancing across runs"): this spec's
    §7 provides the formal state.json schema that the artifact stores, confirming
    the artifact's purpose and adding structural detail.

- **Extends**:
  - `docs-ghaw-practices-experiments.md`: The primary extension target. This spec
    adds normative precision to every behavioral claim in the practices note.
    Specific extensions: (a) control variant definition (Claim 3 here); (b) formal
    tie-breaking requirement for round-robin (Claim 4 here, extending practices
    Claim 4); (c) R-SELECT-006 counter increment requirement for weighted selection
    (Claim 5 here, extending practices Claim 5); (d) date-gating no-counter-increment
    rule (Claim 6 here — not in practices note); (e) state.json formal schema
    (Claim 7 here); (f) `GH_AW_EXPERIMENTS_<NAME>` env var form (Claim 8 here);
    (g) audit CLI formal contract (Claim 9 here); (h) guardrail INFORMATIVE
    clarification (Claim 10 here, resolving practices Claim 9's open question);
    (i) PROMOTE gate and Bonferroni correction (Claim 11 here); (j) simultaneous
    experiment constraints (Claim 12 here); (k) security requirements (Claim 13 here).
  - `docs-ghaw-practices-experiments.md` Claim 9 (guardrail enforcement semantics
    were marked `emerging`): This spec resolves the open question — guardrails are
    INFORMATIVE at schema level (no compile-time enforcement) but MUST trigger
    ABANDON in reporting tools. The practices note's uncertainty is now settled.

- **Contradicts**: None identified. The specification is consistent with all
  existing corpus source notes. R-SELECT-006 corrects a prior ADR (ADR-29618 Rule 9)
  but that ADR does not appear in any existing source note — no corpus claim is
  contradicted. The guardrail clarification (Claim 10) extends rather than
  contradicts the practices note's Claim 9 (which was already marked `emerging`
  and explicitly noted enforcement semantics were uncertain). No contradiction
  issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Formal specification status** (Claim 1): v1.0.0 Draft designation and
    MUST/MUST NOT normative language — no existing note characterizes the
    experiment system as a formal spec with conformance levels.
  - **Three conformance levels** (Claim 2): Basic/Standard/Complete progression
    path for experiment infrastructure maturity — entirely new to the corpus.
  - **Control variant as formal role** (Claim 3): "first variant in declared
    array" as baseline and date-gating fallback — not stated in any prior note.
  - **Uniform-random tie-breaking requirement** (Claim 4): The formal MUST for
    random tie-breaking when counts are equal — the practices note described the
    N/K convergence but not the tie-breaking rule.
  - **R-SELECT-006 counter increment correction** (Claim 5): The normative
    correction to ADR-29618 Rule 9 — no existing note mentions this correction.
  - **Date-gating no-counter-increment rule** (Claim 6): Runs outside the
    experiment window return control without affecting state — not documented
    in any prior note.
  - **state.json formal schema** (Claim 7): The `counts` + `runs` two-section
    structure with per-run assignment history — the artifacts reference mentioned
    the artifact exists; this spec defines its internal structure.
  - **`GH_AW_EXPERIMENTS_<NAME>` environment variables** (Claim 8): The shell-
    accessible env var form of experiment assignments — not mentioned in any prior note.
  - **Audit CLI formal contract with error behavior** (Claim 9): The three
    MUST requirements for the CLI, including the non-zero exit for `--variant`
    without `--experiment` — the practices note mentioned the CLI exists but not
    its formal interface.
  - **Guardrail INFORMATIVE clarification** (Claim 10): Compiler does not enforce
    at compile time; reporting tools force ABANDON — resolves an open question
    from the practices note.
  - **PROMOTE gate rule** (Claim 11): MUST NOT issue PROMOTE until ALL variants
    reach min_samples — a critical statistical guard not documented anywhere.
  - **Bonferroni correction for K≥3** (Claim 11): The formula `α_adjusted =
    0.05 / (K − 1)` — not mentioned in any prior note.
  - **`analysis_type` field values** (Concrete Artifacts): Four supported test
    types with defaults — not documented in any prior note.
  - **Simultaneous experiment constraints** (Claim 12): Three-experiment SHOULD
    NOT limit, mixed-storage prohibition, interaction-effect MUST disclosure.
  - **Security requirements** (Claim 13): OTEL leakage risk, repo-mode
    `contents:write` requirement, and per-workflow permission minimization.

## Guide Impact

### Chapter 04: Agent Patterns / Prompt Engineering / Experimentation

- **Add control variant ordering rule** (Claim 3): The guide should explicitly
  document that the first variant in the array is the control — placed first as
  baseline and as fallback during date gating. Any example should show the
  existing prompt/approach first, followed by experimental variants.

- **Add formal tie-breaking rule to balancing algorithm description** (Claim 4):
  When the guide describes the round-robin algorithm, include the uniform-random
  tie-breaking requirement. This is especially important for explaining why
  variant order does not determine early distribution in multi-variant experiments.

- **Document R-SELECT-006 for weighted selection** (Claim 5): Any guide section
  on weighted selection should note that counter incrementation is required for
  weighted variants — and cite R-SELECT-006 as the normative source for teams
  building custom tooling.

- **Add date-gating as the mechanism for scheduling experiments** (Claim 6):
  The guide should document `start_date`/`end_date` as the experiment scheduling
  tool, with the control-fallback behavior making pre-window deployments safe.

- **Document state.json as the audit ledger** (Claim 7): The `runs` array is
  the per-run assignment history; practitioners building custom reporting must
  read `runs`, not infer assignments from `counts`. Add this to any guide section
  on experiment analysis.

- **Add `GH_AW_EXPERIMENTS_<NAME>` env var form** (Claim 8): Shell steps that
  read experiment assignments should use the env var form — this enables cleaner
  shell scripts without YAML template syntax. Note the uppercasing convention.

- **Clarify guardrail timing** (Claim 10): The guide should correct any implication
  that guardrails are enforced at compile time — they are an analysis-phase gate
  that triggers ABANDON in reporting tools. This matters for practitioners who
  expect compile-time rejection.

- **Add the PROMOTE gate rule** (Claim 11): Documenting that PROMOTE must not
  be issued until ALL variants reach min_samples is essential for any guide section
  on experiment conclusions. This prevents premature variant selection based on
  incomplete samples.

- **Add Bonferroni correction guidance** (Claim 11): For experiments with K≥3
  variants, the guide should recommend adjusting significance thresholds using
  `α_adjusted = 0.05 / (K − 1)` to prevent false positives from multiple pairwise
  comparisons.

- **Add simultaneous experiment constraints** (Claim 12): Warn practitioners
  against running more than three concurrent experiments; document the mixed-storage
  prohibition and the interaction-effect disclosure requirement.

### Chapter 02: Harness Engineering / Security

- **Add experiment permissions model** (Claim 13): Include in any security
  checklist for agentic workflow deployment: repo mode requires `contents: write`;
  reporting workflows need `issues: write` or `discussions: write` separately;
  all other permissions should be `read`. The experiment-runner and the reporting
  workflow should have distinct permission scopes.

- **Add OTEL attribute leakage warning** (Claim 13): When documenting OTLP
  integration for experiment tracking (see `docs-ghaw-agentic-ops.md` Claim 12),
  note that variant names and experiment names exported as OTEL attributes may
  be visible in tracing backends — avoid embedding sensitive terms.

- **Add three-conformance-level roadmap** (Claim 2): For teams building experiment
  infrastructure from scratch, the three conformance levels provide a natural
  implementation roadmap — present them as the maturity progression.

## Extraction Notes

1. **Source accessed via WebFetch (three passes)**: Three independent passes were
   made: the first for overall content, the second for verbatim quotes on specific
   normative rules, and the third for CLI interface, security, and corrective item
   details. Technical strings (section numbers, MUST/MUST NOT language, JSON
   schema fields, CLI flag names) are consistent across all three passes.

2. **No publication date**: The specification carries no explicit publication date.
   `date_published` is left null. The version is 1.0.0 Draft as of 2026-05-17.

3. **No contradictions filed**: All claims in this specification are consistent
   with existing corpus source notes. R-SELECT-006 corrects ADR-29618 Rule 9 but
   that ADR does not appear in any existing source note. The guardrail clarification
   (Claim 10) extends rather than contradicts the practices note's Claim 9, which
   was already marked `emerging` with the enforcement question explicitly open.

4. **Specification vs. practices guide scope**: This note intentionally focuses on
   what the specification adds beyond the practices guide. Readers should read
   `docs-ghaw-practices-experiments.md` for authoring guidance (YAML examples,
   the two declaration forms, downstream access patterns) and this note for the
   formal contracts that underpin those behaviors.

5. **Guardrail enforcement timing**: The specification is clear that guardrail
   enforcement is entirely in reporting tools (not the compiler). Teams relying
   on guardrails for safety must implement a reporting workflow that evaluates
   `state.json` against guardrail thresholds and issues ABANDON — the runtime
   alone does not block harmful variants automatically.
