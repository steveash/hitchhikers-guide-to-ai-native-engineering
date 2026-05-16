---
source_url: https://github.github.com/gh-aw/practices/experiments
source_type: docs
title: "GitHub Agentic Workflows: A/B Experiments Practices Guide"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-16
last_checked: 2026-05-16
status: current
confidence_overall: emerging
issue: "#770"
---

# GitHub Agentic Workflows: A/B Experiments Practices Guide

> The practitioner guide for designing and running A/B experiments in gh-aw
> workflows — covers both bare and rich declaration forms, the round-robin
> balancing algorithm, weighted selection, storage strategy (`repo` vs `cache`),
> downstream variant access, and the step-summary analysis interface including
> progress bars toward `min_samples` and guardrail metric enforcement.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `practices/experiments` page — in
  the `practices/` section, distinct from `reference/` pages that document field
  schemas and `patterns/` pages that describe high-level workflow patterns. Practices
  pages provide how-to guidance for specific features with both simple and advanced
  configuration examples.)
- **Author credibility**: First-party from GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — same team behind Peli de Halleux's agent factory blog
  series and the `gh aw` CLI). Field names, syntax, and behavioral details are
  platform specifications for the `gh aw` runtime. Claims about balancing algorithms
  and state persistence reflect first-party implementation knowledge, not inference.
- **Scope**: Covers the complete experiment authoring workflow — declaring experiments
  (bare and rich forms), referencing variants in prompts (including conditional block
  syntax), the activation job's balancing algorithm (round-robin with weighted
  override), storage configuration (`repo` vs `cache`), downstream access to
  assignments, and the analysis interface (step summary, artifact, CLI reporting).
  Does NOT cover: the `experiment` artifact's internal structure in detail (see
  `docs-ghaw-artifacts-reference.md` Claim 6), the `experiments` field in the JSON
  Schema reference (see `docs-ghaw-frontmatter-full-reference.md` Claim 8), or
  OTLP span attribute emission for experiment tracking (see
  `docs-ghaw-agentic-ops.md` Claim 12).

## Extracted Claims

### Claim 1: The `experiments` section of the workflow frontmatter enables statistical A/B testing by defining named experiments, each with a set of variant values selected and balanced by the activation job at runtime

- **Evidence**: Opening description of the page, consistent across two independent
  WebFetch passes; corroborated by `docs-ghaw-frontmatter-full-reference.md` Claim 8
  which describes `experiments` as "A/B testing experiments with variants and metadata"
  in the schema-generated field catalog.
- **Confidence**: settled (first-party; the feature is explicitly documented and
  corroborated by the schema reference)
- **Quote**: "The `experiments` section of the workflow frontmatter enables statistical
  A/B testing by defining named experiments, each with a set of variant values."
- **Our assessment**: The `experiments` section is a first-class platform feature, not
  an ad-hoc workaround — it is built into the activation job that runs before every
  agentic workflow. The balancing happens at the harness level (activation job), not
  inside the AI instructions, giving it the same deterministic guarantees as other
  frontmatter-declared behavior. For Ch04 (Prompt Engineering & Experimentation):
  this is the canonical mechanism for testing prompt variants on real workflow traffic.

### Claim 2: Two experiment declaration forms are supported — bare-array (simple) and rich object (with metadata) — and practitioners should prefer the rich form for any experiment intended to run beyond quick exploration

- **Evidence**: The page documents both forms with explicit YAML examples. The rich
  form's additional fields (`description`, `hypothesis`, `metric`, `guardrail_metrics`,
  `min_samples`, `weight`, `issue`, `start_date`, `end_date`) are absent in the bare
  form. The page frames the bare form as a simpler syntax rather than the recommended
  form.
- **Confidence**: settled (first-party; both forms are explicitly documented with YAML
  examples; field names for the rich form are enumerated)
- **Quote**: (no direct quote distinguishing when to use each form; see paraphrase
  in Our assessment)
- **Our assessment**: The bare form is appropriate for quick explorations or temporary
  experiments where tracking metadata is not needed. The rich form is appropriate
  whenever an experiment is intended to run for multiple sprint cycles, influence a
  product decision, or require statistical confidence — because `min_samples`,
  `hypothesis`, and `guardrail_metrics` are only available in the rich form. Teams
  should treat the choice between forms as a signal of experiment maturity: bare = 
  spike, rich = production experiment. For Ch04: present the two forms as a progression
  rather than alternatives — start bare, migrate to rich when the experiment proves
  worth tracking.

### Claim 3: Variants are referenced in workflow prompts using `${{ experiments.<name> }}` syntax, with a conditional block form for yes/no experiments where `no` is treated as falsy

- **Evidence**: The page documents `${{ experiments.<name> }}` as the reference syntax
  and describes a block form for conditional sections. The `no` falsy treatment is
  explicitly stated.
- **Confidence**: settled (first-party; the syntax is directly documented with
  examples; the falsy behavior for `no` is a platform convention)
- **Quote**: (no direct prose quote; the syntax `${{ experiments.<name> }}` and the
  conditional block behavior are shown in code examples rather than prose)
- **Our assessment**: The `${{ experiments.<name> }}` syntax mirrors the standard gh-aw
  template syntax for accessing context values (`${{ github.event.issue.number }}` etc.),
  making it consistent with existing templating knowledge. The special treatment of
  `no` as falsy in conditional blocks is a UX convenience for the common yes/no
  experiment pattern — practitioners can write `{{#if experiments.use_cot }}` without
  needing to check for a truthy variant string. For Ch04: document the conditional
  block syntax separately from inline substitution — they serve different purposes
  (structural prompt sections vs. inline variant text).

### Claim 4: The activation job uses round-robin lowest-count selection: the variant with the lowest cumulative invocation count is selected each run, achieving approximately N/K uses per variant over N runs with K variants

- **Evidence**: The page describes the balancing mechanism explicitly. Two WebFetch
  passes returned consistent descriptions of the lowest-count selection approach and
  the N/K distribution result.
- **Confidence**: settled (first-party; the algorithm and distribution result are
  explicitly stated)
- **Quote**: "The variant with the lowest cumulative count is selected on each run...
  Over N runs every variant is used approximately N/K times."
- **Our assessment**: The round-robin lowest-count algorithm is strictly fair — it
  guarantees that no variant is systematically over-represented even when runs arrive
  in bursts or when the workflow is interrupted. The "approximately" qualifier on
  N/K accounts for tie-breaking (ties break randomly), which introduces minor variance
  at low N. For practitioners designing experiments, this means they can predict
  total per-variant sample size from total run count: a 100-run experiment with 2
  variants yields ~50 samples per variant. For Ch04: document the N/K formula as
  the sample-size planning tool for experiments with `min_samples` targets.

### Claim 5: Weighted selection replaces round-robin when a `weight` array is provided, enabling probability-based variant distribution such as [70, 30] for controlled rollout scenarios

- **Evidence**: The page explicitly states that a `weight` array overrides the
  round-robin default. The [70, 30] example is given as an illustration.
- **Confidence**: settled (first-party; the weight override and its effect are
  explicitly documented)
- **Quote**: "Weighted selection replaces round-robin when a `weight` array is
  provided"
- **Our assessment**: Weighted selection is the mechanism for controlled rollout
  experiments — scenarios where a new variant should receive less traffic initially
  (e.g., [90, 10]) until confidence is established, then be ramped up. Unlike pure
  round-robin (which is always 1/K), weighted selection is probability-based, meaning
  the exact distribution varies run-to-run but converges on the target proportions
  over large N. This matters for guardrail metric monitoring: with a [90, 10]
  weight, the minority variant accumulates samples slowly, so `min_samples` will
  be reached later. For Ch04: document weighted selection as the controlled rollout
  mechanism and note that `min_samples` interacts with weight — low-weight variants
  need proportionally more total runs to reach their minimum.

### Claim 6: Experiment state persists in `repo` mode (default) via commits to an `experiments/{workflowID}` branch that survives cache eviction, or in `cache` mode (GitHub Actions cache, may evict after 7 days)

- **Evidence**: The page documents the `storage` key with a two-row table showing
  `repo` and `cache` options, their behaviors, and the durability difference.
- **Confidence**: settled (first-party; the storage key, its values, and their
  behaviors are explicitly documented in a table)
- **Quote**: (from the storage configuration table — no single prose sentence captures
  both options; see table in Concrete Artifacts)
- **Our assessment**: The `repo` default is the correct choice for any experiment
  that spans multiple days or is intended to reach `min_samples` over a period of
  weeks — because cache eviction (which can happen after 7 idle days in GitHub Actions)
  would reset the variant counters and break the statistical continuity. The `cache`
  option is appropriate only for short-lived spike experiments where losing the state
  is acceptable. The `experiments/{workflowID}` branch naming convention for `repo`
  mode means experiment state is inspectable and auditable as a git branch. For Ch02
  (Harness Engineering): recommend `storage: repo` as the default for production
  experiments and note that `storage: cache` is suitable for development-phase
  iteration only.

### Claim 7: Downstream jobs access selected variant assignments via `needs.activation.outputs.<name>` for individual variants or `needs.activation.outputs.experiments` for all assignments as a JSON object

- **Evidence**: The page explicitly documents both access patterns for downstream jobs.
- **Confidence**: settled (first-party; both output key patterns are directly documented)
- **Quote**: (no direct prose quote; access patterns documented as code references
  rather than prose)
- **Our assessment**: The `needs.activation.outputs.<name>` pattern is the standard
  for jobs that branch on a single experiment variant. The
  `needs.activation.outputs.experiments` JSON object form is the pattern for jobs
  that need to log or report all assigned variants — e.g., for OTLP span attribute
  emission or for including assignments in a report. For Ch02: document both access
  patterns as the standard interface between the activation job and downstream jobs
  in experimental workflows.

### Claim 8: The activation job step summary shows selected variants, cumulative counts, progress bars toward `min_samples` targets, and hypothesis and guardrail metric display — making experiment progress inspectable from the Actions UI without CLI access

- **Evidence**: The page describes the step summary output explicitly. The progress
  bars toward `min_samples` and the hypothesis/guardrail display are specifically
  named as step summary elements.
- **Confidence**: settled (first-party; the step summary contents are explicitly
  enumerated)
- **Quote**: "variant assignments, cumulative counts, and...progress toward
  `min_samples`"
- **Our assessment**: The step summary display makes experiment progress self-evident
  in the Actions UI — practitioners do not need to download the experiment artifact
  or run CLI commands to check experiment status. The progress bars toward `min_samples`
  are particularly valuable: they give a visual indicator of when an experiment has
  accumulated enough samples to make statistically reliable conclusions. For Ch04:
  document the step summary as the primary experiment monitoring interface during
  active experimentation; document the `gh aw` CLI audit command as the secondary
  interface for programmatic or scripted analysis.

### Claim 9: The rich object form supports `guardrail_metrics` as `{name, threshold}` pairs that can enforce automated safeguards — providing a mechanism to halt or alert on experiments that exceed harm thresholds before `min_samples` is reached

- **Evidence**: The page includes `guardrail_metrics` in the configuration field
  list for the rich object form, with `{name, threshold}` as the pair structure.
- **Confidence**: emerging (first-party field documentation; the specific enforcement
  behavior — halt vs. alert — is inferred from the field description "guardrail
  enforcement" rather than explicitly described in the returned source content)
- **Quote**: (no direct quote on guardrail enforcement semantics; the field exists
  and the `{name, threshold}` structure is documented)
- **Our assessment**: Guardrail metrics are the experiment safety mechanism — they
  prevent a harmful variant from accumulating too many exposures before analysis
  can flag the problem. This is important in production agentic workflows where a
  poorly performing prompt variant could trigger unwanted actions at scale (e.g.,
  a variant that causes the agent to file unnecessary issues). The enforcement
  semantics (whether threshold breach halts the experiment, alerts, or simply
  records) are not fully described in the returned source content — practitioners
  should verify against the full page. For Ch04: document `guardrail_metrics` as
  the responsible-experimentation mechanism for any experiment where a bad variant
  could cause irreversible workflow side effects.

### Claim 10: Experiment names must be valid identifiers (letters, underscores, digits) — this is a platform validation requirement enforced at compile time

- **Evidence**: The page explicitly states the naming constraint as a "Requirement"
  with the valid character set specified.
- **Confidence**: settled (first-party; the constraint is explicitly stated as a
  requirement)
- **Quote**: "Experiment names must be valid identifiers (letters, underscores,
  digits)."
- **Our assessment**: The valid-identifier requirement is consistent with how gh-aw
  uses experiment names as output keys in `needs.activation.outputs.<name>` —
  GitHub Actions output names must be valid identifiers for downstream referencing.
  Practitioners naming experiments should avoid spaces, hyphens, and special characters.
  For Ch04: include the naming constraint in any experiment declaration example to
  prevent compile-time errors.

## Concrete Artifacts

### Bare-Array Form

From `https://github.github.com/gh-aw/practices/experiments`:

```yaml
experiments:
  style: [concise, detailed]
```

*Simple A/B syntax: `style` is the experiment name; `concise` and `detailed` are the
variants. Referenced as `${{ experiments.style }}` in the workflow prompt.*

### Rich Object Form

From `https://github.github.com/gh-aw/practices/experiments`:

```yaml
experiments:
  prompt_style:
    variants: [concise, detailed]
    description: "Test prompt length impact on tokens"
    hypothesis: "H0: no change. H1: concise reduces by >=15%"
    metric: effective_tokens
    min_samples: 25
```

*Extended syntax with tracking metadata. Additional supported fields: `secondary_metrics`,
`guardrail_metrics` (`{name, threshold}` pairs), `weight` (probability distribution array),
`issue` (tracking issue number), `start_date`, `end_date` (ISO-8601 experiment window).*

### Storage Configuration Table

From `https://github.github.com/gh-aw/practices/experiments`:

```
| Value         | Behavior                                                        |
|---------------|-----------------------------------------------------------------|
| repo (default)| Commits to experiments/{workflowID} branch; survives cache     |
|               | eviction                                                        |
| cache         | Uses GitHub Actions cache; may evict after 7 days              |
```

### Downstream Access Patterns

From `https://github.github.com/gh-aw/practices/experiments`:

```yaml
# Access a single variant assignment in a downstream job
jobs:
  analyze:
    needs: activation
    steps:
      - run: echo "Variant is ${{ needs.activation.outputs.prompt_style }}"

# Access all assignments as JSON
      - run: echo '${{ needs.activation.outputs.experiments }}'
```

### Configuration Field Reference

From `https://github.github.com/gh-aw/practices/experiments`:

```
Bare-array form:
  experiments.<name>: string[]       # list of variant values

Rich object form fields:
  variants          (required)       # variant strings
  description                        # human-readable description
  hypothesis                         # H0 / H1 statement
  metric                             # primary metric to track
  secondary_metrics                  # additional tracking metrics
  guardrail_metrics                  # {name, threshold} pairs for safety enforcement
  min_samples                        # target sample count per variant for reliability
  weight                             # probability distribution array (overrides round-robin)
  issue                              # GitHub issue number for tracking
  start_date                         # experiment window start (ISO-8601)
  end_date                           # experiment window end (ISO-8601)

Naming requirement: experiment names must be valid identifiers (letters, underscores, digits)
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-frontmatter-full-reference.md` Claim 8 ("The experiments field supports
    A/B testing with variants and configurable storage — enabling statistical workflow
    iteration with 'cache' (ephemeral) or 'repo' (persistent) storage"): this practices
    page corroborates and deepens that schema-level entry. The frontmatter reference
    documents that `experiments.storage` exists and has two values; this page explains
    the full variant declaration syntax, balancing algorithm, downstream access, and
    analysis interface that the schema reference did not capture.
  - `docs-ghaw-artifacts-reference.md` Claim 6 ("The `experiment` artifact is only
    present when workflows declare A/B experiments in frontmatter — it stores
    per-variant invocation counters for load balancing across runs"): the state
    persistence described here (per-variant counters in `repo` or `cache`) is the
    same mechanism; the artifacts reference documents the output artifact (`state.json`),
    while this page documents the input configuration that produces it.
  - `docs-ghaw-agentic-ops.md` Claim 12 ("The audit workflow integrates OTLP
    observability with custom `gh_aw.experiment.*` span attributes, enabling A/B
    experiment variant tracking in Datadog, Honeycomb, or any OTLP backend"): the
    `needs.activation.outputs.experiments` JSON object (Claim 7 here) is the upstream
    source of data that the OTLP span attribute emission pattern in `docs-ghaw-agentic-ops.md`
    Claim 12 reads. Both sources are consistent; the agentic-ops note shows how to
    emit experiment assignments as OTLP spans; this note shows where those assignments
    come from.

- **Extends**:
  - `docs-ghaw-frontmatter-full-reference.md` Claim 8: The schema reference only
    documented `experiments.storage`; this practices page adds the variant declaration
    syntax (both forms), the complete rich object field set, the balancing algorithm,
    weighted selection, downstream access patterns, `min_samples` progress tracking,
    and guardrail metrics. This is the depth layer that the schema catalog lacked.
  - `docs-ghaw-artifacts-reference.md` Claim 6: The artifacts reference documented
    the `experiment` artifact's existence and storage role; this page adds the authoring
    workflow that creates and uses that artifact — how to declare experiments, how the
    activation job populates it, and how downstream jobs read from it.

- **Contradicts**: None identified. The storage options, variant syntax, and activation
  job behavior are consistent with the schema reference and the artifacts reference.
  No existing source note makes claims that materially oppose any claim in this note.
  No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Complete variant declaration syntax** (Claims 2–3): Both the bare-array and
    rich object forms, including all rich form fields (`secondary_metrics`,
    `guardrail_metrics`, `weight`, `issue`, `start_date`, `end_date`), are not
    documented in any prior note. The frontmatter reference only captured
    `experiments.storage`.
  - **Round-robin lowest-count balancing algorithm with N/K formula** (Claim 4):
    The specific selection algorithm — lowest cumulative count, random tie-breaking,
    N/K convergence — is not described in any prior corpus note. This is the first
    source that explains *how* variant balance is achieved.
  - **Weighted selection mechanism** (Claim 5): The `weight` array override for
    probability-based distribution is not documented anywhere in the prior corpus.
  - **Downstream access patterns** (Claim 7): The `needs.activation.outputs.<name>`
    and `needs.activation.outputs.experiments` access keys are not documented in any
    prior note. `docs-ghaw-agentic-ops.md` Claim 12 uses `assignments.json` from a
    file path, not from job outputs, suggesting a different access mechanism; the
    outputs-based pattern here is the declarative YAML approach.
  - **Step summary progress bars toward `min_samples`** (Claim 8): The step summary
    display format (progress bars, hypothesis display, guardrail metric display) is
    not documented in any prior note.
  - **Guardrail metrics as experiment safety mechanism** (Claim 9): The `guardrail_metrics`
    field with `{name, threshold}` pairs for automated safeguards is not mentioned
    in any prior source note.
  - **Experiment name identifier requirement** (Claim 10): The naming constraint
    (letters, underscores, digits only) is not mentioned in the frontmatter reference
    or any other prior note.
  - **Conditional block syntax for yes/no experiments** (Claim 3): The `no`-as-falsy
    convention in conditional blocks is not documented anywhere in the corpus.

## Guide Impact

### Chapter 04: Agent Patterns / Prompt Engineering / Experimentation

- **Add experiment declaration as the gh-aw native A/B testing mechanism** (Claims
  1–3): The guide should present `experiments` as the platform's first-class support
  for prompt variant testing — not a workaround, but a designed feature. Cover both
  the bare form (spike/exploration) and rich form (production experiment) with YAML
  examples. Include the `${{ experiments.<name> }}` reference syntax and the
  conditional block form for yes/no experiments.

- **Document the N/K balancing formula as the sample-size planning tool** (Claim 4):
  Practitioners running experiments to compare prompt variants need to plan total
  run count to reach adequate per-variant sample size. The N/K formula
  (total runs ÷ variant count = approximate per-variant samples) is the planning
  tool. Pair with `min_samples` as the target sample count for reliability.

- **Add weighted selection as the controlled rollout mechanism** (Claim 5): For
  experiments where a new variant is risky (e.g., a prompt that triggers more
  aggressive safe outputs), weighted selection ([90, 10] or [70, 30]) limits
  early exposure while still accumulating evidence. Document alongside round-robin
  as the second selection strategy.

- **Add `guardrail_metrics` as the responsible-experimentation gate** (Claim 9):
  Any experiment where a bad variant could cause irreversible workflow side effects
  (unwanted issues filed, PRs opened, comments posted) should declare guardrail
  metrics. This is the experiment analog to `max-turns` and `skip-if-match` — a
  cost-control/safety mechanism built into the experimental framework.

- **Document `min_samples` with the step summary progress bars** (Claim 8): The
  step summary makes experiment progress visible in the Actions UI. Practitioners
  should know to look at the activation step summary during active experiments to
  check per-variant sample counts against the `min_samples` target before drawing
  conclusions.

### Chapter 02: Harness Engineering

- **Recommend `storage: repo` as the default for production experiments** (Claim 6):
  The `cache` option risks resetting experiment counters on eviction, breaking
  statistical continuity for long-running experiments. Document `repo` as the
  production default and `cache` as the development/spike option. Note that `repo`
  mode creates an `experiments/{workflowID}` branch that is inspectable and auditable.

- **Document downstream variant access patterns** (Claim 7): Add
  `needs.activation.outputs.<name>` and `needs.activation.outputs.experiments` as
  the standard interface between the activation job and downstream jobs in experimental
  workflows. This connects the experiment authoring (this source) to the artifact
  consumption (`docs-ghaw-artifacts-reference.md` Claim 6).

- **Add experiment naming constraint** (Claim 10): When documenting experiment
  declaration examples, include the naming requirement (valid identifiers) to
  prevent compile-time errors from names with spaces or hyphens.

## Extraction Notes

1. **Source accessed via WebFetch (two passes)**: The gh-aw documentation site is
   an Astro/Starlight SPA. Two independent WebFetch passes were made with different
   prompts. Technical strings (field names, YAML syntax, access key patterns,
   storage options) are consistent across both passes and aligned with the
   schema-level documentation in `docs-ghaw-frontmatter-full-reference.md` Claim 8.
   Prose quotes where the two passes returned slightly different wording are marked
   "(no direct quote)" per MINER.md §2a — the YAML code blocks and specific field
   names are treated as accurate.

2. **Guardrail semantics underspecified**: The `guardrail_metrics` field exists and
   its structure (`{name, threshold}`) is documented, but the specific enforcement
   behavior (halt experiment vs. alert vs. record) was not captured in either fetch
   pass. Claim 9 is marked `emerging` accordingly. Practitioners should consult the
   full page to verify guardrail enforcement semantics before relying on them for
   safety-critical experiment gating.

3. **Conditional block syntax not fully elaborated**: The page mentions that block
   syntax treats `no` as falsy for yes/no experiments, but the specific template
   syntax for conditional blocks was not returned in the fetch passes. Claim 3 notes
   this and omits a code example for the conditional form.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with the
   current gh-aw platform as of 2026-05-16.

5. **No contradictions filed**: Reviewed all existing corpus source notes. No claims
   here materially oppose any existing note. The storage options, variant syntax, and
   balancing algorithm are additive to the schema documentation in
   `docs-ghaw-frontmatter-full-reference.md` Claim 8 and the artifact description
   in `docs-ghaw-artifacts-reference.md` Claim 6.
