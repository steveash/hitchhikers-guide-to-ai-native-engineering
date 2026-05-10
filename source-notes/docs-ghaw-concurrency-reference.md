---
source_url: https://github.github.com/gh-aw/reference/concurrency
source_type: docs
title: "GitHub Agentic Workflows: Concurrency Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#373"
---

# GitHub Agentic Workflows: Concurrency Reference

> The authoritative reference for gh-aw's two-tier concurrency model — documents
> per-workflow trigger-scoped groups (with a five-row trigger table), per-engine
> singleton enforcement for AI resource isolation, independent Safe Outputs job
> handling, auto-generated Conclusion job groups, and the `job-discriminator`
> mechanism that resolves fan-out concurrency collisions for dispatched runs
> with different inputs.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/concurrency` page —
  in the "Reference" section, distinct from the `patterns/` practitioner pages and
  the `introduction/` conceptual pages. Reference pages document platform behavior
  precisely; this one specifies the complete concurrency model.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — the same team behind Peli de Halleux's "Agent Factory"
  blog series and the `gh aw` CLI). Reference-section claims about group format
  expressions, default behaviors, and configuration fields are settled platform facts,
  not practitioner recommendations.
- **Scope**: The complete gh-aw concurrency model — workflow-level trigger-scoped
  groups, per-engine AI execution limits, custom overrides for both levels, Safe
  Outputs job independent processing, Conclusion job automatic grouping, and the
  `job-discriminator` fan-out mechanism. Does NOT cover: workflow authoring syntax
  (see `docs-ghaw-agentic-authoring.md`), the Safe Outputs permission model in
  general (see `docs-ghaw-how-they-work.md`), fan-out dispatch mechanisms
  (`dispatch-workflow` vs `call-workflow`, see `docs-ghaw-orchestration-patterns.md`),
  or per-run cost and token observability.

## Extracted Claims

### Claim 1: GitHub Agentic Workflows implements a two-tier concurrency model to prevent AI resource exhaustion — one tier scoped to workflow+trigger context, one tier scoped to the AI engine identity

- **Evidence**: The page opens with the two-tier architecture as its primary frame.
  The two tiers are: (1) workflow-level controls based on workflow name and trigger
  context (issue number, PR number, branch ref); (2) engine-level controls that limit
  concurrent AI execution across all workflows via `engine.concurrency`. The resource-
  exhaustion framing is explicit: the engine-level tier exists to prevent runaway
  concurrent AI use.
- **Confidence**: settled (first-party reference documentation; architectural claims
  about the platform's concurrency model are authoritative)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The two-tier design separates two distinct concerns: (1) workflow
  identity — preventing two runs of the same workflow on the same issue/PR/branch from
  interfering with each other; (2) AI resource identity — preventing multiple workflows
  from saturating the same AI engine simultaneously. These require different scoping
  strategies: workflow identity is scoped to the triggering entity (e.g., issue number);
  AI resource identity is scoped to the engine alone. Conflating them would either
  over-restrict (one agent per issue even with different engines) or under-restrict
  (no limit on concurrent AI calls from different workflows using the same engine).
  For Ch02 (Harness Engineering): the two-tier model should be introduced as the
  foundational concurrency architecture before explaining either tier's defaults or
  overrides. For Ch04 (Multi-Agent Orchestration): the engine-level tier is the
  mechanism that prevents multi-workflow fan-out from exhausting shared AI infrastructure.

### Claim 2: Per-workflow concurrency groups use trigger-type-specific expressions — Issues and Push use non-cancelling groups; Pull Requests use a cancelling group; Labels use conditional cancellation

- **Evidence**: The page provides a table mapping each trigger type to its group
  format expression and `cancel-in-progress` behavior. Five trigger types are
  documented. The distinction between cancelling and non-cancelling is per-trigger:
  PR builds are cancelled on supersession (a new push cancels the running PR check);
  issue, push, and schedule workflows are not cancelled (each run completes
  independently).
- **Confidence**: settled (first-party reference documentation; table of group
  formats is authoritative for the `gh aw` platform)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The trigger-specific cancellation design is deliberate and
  correct for each use case. PR workflows benefit from `cancel-in-progress: true`
  because a new commit to the PR branch supersedes the previous check — running both
  wastes resources without adding signal. Issue and push workflows use
  `cancel-in-progress: false` because each run represents a distinct event: issuing
  a comment on issue #42 does not supersede a prior comment on the same issue. The
  Labels trigger's conditional behavior accounts for different label semantics —
  some labels warrant cancellation (e.g., override labels), others do not. For Ch02:
  when designing gh-aw workflows, the trigger type determines the default concurrency
  semantics — teams should understand which trigger type their workflow uses before
  deciding whether to override `cancel-in-progress`.

### Claim 3: Per-engine concurrency defaults to `gh-aw-{engine-id}` singleton enforcement — restricting one agent job per engine across all workflows, regardless of workflow name, issue, PR, or branch

- **Evidence**: The page specifies the per-engine default pattern as `gh-aw-{engine-id}`.
  It explicitly states that the group includes only the engine identifier and prefix —
  workflow names, issue/PR numbers, and branch references are excluded. This means
  any two workflows using the same engine (e.g., two different workflows both using
  `copilot`) cannot run concurrently by default.
- **Confidence**: settled (first-party reference documentation; the group pattern and
  its scope exclusions are authoritative)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The singleton-per-engine default is the correct conservative
  starting point for AI resource management. Without it, an orchestrator that fans out
  10 workers would immediately exhaust the AI engine's capacity with 10 concurrent
  agent jobs. The singleton enforces sequential AI use across all workflows sharing
  that engine. The practical implication for multi-workflow deployments: if a team
  runs three concurrent workflows (e.g., issue-triage, dependency-update, and PR-review)
  all using the `copilot` engine, only one will be running AI inference at any moment
  by default. Teams that need genuine parallelism must explicitly override the engine
  concurrency group (see Claim 5) — the platform errs on the side of safety.
  For Ch04 (Multi-Agent Orchestration): the per-engine singleton is the reason
  fan-out workers need custom engine concurrency groups — without them, all dispatched
  workers share a single engine group and queue behind each other. The `job-discriminator`
  (Claim 8) addresses this at the job level; Claim 5's custom engine override addresses
  it at the configuration level.

### Claim 4: The per-workflow concurrency group for PRs uses `${{ pr.number || ref }}` as the disambiguator — this handles both PR number and branch-ref scenarios in a single expression

- **Evidence**: The page's trigger-type table specifies the PR group format as
  `gh-aw-${{ github.workflow }}-${{ pr.number || ref }}`. The `|| ref` fallback
  handles cases where a PR number is not available (e.g., direct branch pushes
  that trigger PR-adjacent workflows).
- **Confidence**: settled (first-party reference; the exact group format expression
  is a platform specification)
- **Quote**: `gh-aw-${{ github.workflow }}-${{ pr.number || ref }}`
- **Our assessment**: The `|| ref` fallback is a defensive expression: it prevents
  the group from collapsing to a workflow-scoped global lock when the `pr.number`
  is unavailable. Without the fallback, all runs with no PR number would share one
  group — serializing all non-PR-triggered runs together. The branch-ref fallback
  maintains per-branch isolation even in non-PR contexts. This detail matters for
  teams that trigger workflows on branch pushes that share trigger logic with PR
  workflows. For Ch02: document the full PR group expression, not just the presence
  of PR number scoping — the `|| ref` fallback is an operational detail that prevents
  unexpected serialization in edge cases.

### Claim 5: Users can independently override both workflow-level and engine-level concurrency via frontmatter YAML — the two tiers are independently configurable

- **Evidence**: The page shows custom configuration YAML with independent fields
  for workflow-level (`concurrency:`) and engine-level (`engine.concurrency:`)
  overrides. The worker workflow example from `docs-ghaw-central-repo-ops.md`
  demonstrates this in production use: a custom `concurrency.group` scoped to
  the target repository, and a custom `engine.concurrency.group` also scoped to
  the target repository.
- **Confidence**: settled (first-party reference; YAML configuration is authoritative)
- **Quote**: (no direct quote; see paraphrase in Our assessment — YAML artifact below)
- **Our assessment**: Independent override capability is essential for the CentralRepoOps
  fan-out use case. The Dependabot Rollout worker in `docs-ghaw-central-repo-ops.md`
  (Concrete Artifacts) uses both overrides: `concurrency.group: gh-aw-${{ github.workflow }}-${{ github.event.inputs.target_repo }}` and `engine.concurrency.group: gh-aw-copilot-${{ github.workflow }}-${{ github.event.inputs.target_repo }}`. Without these overrides,
  all dispatched workers (one per target repository) would share the same `gh-aw-copilot`
  engine singleton — making the fan-out serial at the AI layer. With the overrides,
  each worker has its own concurrency scope at both tiers, enabling genuine parallel
  execution. For Ch02: document that custom concurrency overrides are the enabling
  mechanism for parallel fan-out — teams must override both tiers, not just one.

### Claim 6: Safe Outputs jobs process independently from agent jobs and use `cancel-in-progress: false` when a `safe-outputs.concurrency-group` is configured — preventing duplicate operations in issue or PR creation workflows

- **Evidence**: The page states that the `safe_outputs` job processes independently
  from agent jobs. When `safe-outputs.concurrency-group` is configured, the Safe
  Outputs job uses `cancel-in-progress: false`. This allows queued runs to wait
  rather than be discarded, preventing duplicate issue/PR creation when multiple
  runs complete around the same time.
- **Confidence**: settled (first-party reference; the default behavior and configuration
  option are specified)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The Safe Outputs independent processing model is important for
  correctness in high-frequency trigger scenarios. If two issue-comment triggers fire
  in quick succession, both agent jobs run and both produce outputs. Without safe
  concurrency semantics, the Safe Outputs job from the second run could cancel the
  first run's output delivery — resulting in lost output. The `cancel-in-progress:
  false` default for Safe Outputs jobs ensures all output deliveries complete, even
  if they queue behind each other. The `safe-outputs.concurrency-group` configuration
  provides the scope for this queuing: teams can choose to serialize Safe Outputs
  operations at the workflow level or at a broader scope. For Ch02: when using Safe
  Outputs in high-frequency trigger workflows (frequent PR comments, issue label
  events), configure `safe-outputs.concurrency-group` explicitly — the non-cancelling
  behavior prevents silent output loss.

### Claim 7: Conclusion jobs automatically receive a workflow-specific non-cancelling concurrency group `gh-aw-conclusion-{workflow-name}` — and when `job-discriminator` is set, the discriminator appends to create per-run distinct groups

- **Evidence**: The page specifies the auto-generated Conclusion job group format
  as `gh-aw-conclusion-{workflow-name}`. It is workflow-specific and non-cancelling
  (does not use `cancel-in-progress: true`). When `job-discriminator` is set, the
  discriminator value appends to the group, creating a distinct group per dispatched
  run.
- **Confidence**: settled (first-party reference; group format is specified)
- **Quote**: `gh-aw-conclusion-{workflow-name}`
- **Our assessment**: The Conclusion job's automatic grouping prevents two Conclusion
  jobs from the same workflow from interfering with each other (e.g., two concurrent
  runs completing at similar times). The non-cancelling default is appropriate because
  Conclusion jobs are final steps — their work should not be discarded simply because
  another instance is starting. The `job-discriminator` interaction is significant:
  in fan-out scenarios where the orchestrator dispatches multiple workers (all using
  the same workflow), each dispatch creates a Conclusion job with the same base
  workflow name. Without `job-discriminator`, all their Conclusion jobs share one
  group and serialize. With `job-discriminator`, each dispatched run's Conclusion
  job has a unique group — enabling truly parallel completion. For Ch02: when using
  `job-discriminator` in fan-out workflows, verify it is set consistently for all
  job types, not just the agent job — otherwise Conclusion jobs become the unexpected
  serialization point.

### Claim 8: The `concurrency.job-discriminator` field resolves fan-out concurrency collisions by appending unique expressions to compiler-generated job-level concurrency groups — enabling true parallel execution for dispatched runs with different inputs

- **Evidence**: The page specifies `concurrency.job-discriminator` as a frontmatter
  field that appends unique expressions to compiler-generated job concurrency groups.
  Three common patterns are documented: `${{ inputs.finding_id }}` for input-specific
  uniqueness, `${{ github.run_id }}` for universal run-level distinctness, and
  `${{ inputs.organization || github.run_id }}` for conditional fallbacks. The stated
  purpose is to prevent fan-out cancellations while preserving workflow-level controls.
- **Confidence**: settled (first-party reference; field name and examples are specified)
- **Quote**: `${{ inputs.finding_id }}`, `${{ github.run_id }}`,
  `${{ inputs.organization || github.run_id }}`
- **Our assessment**: The `job-discriminator` solves a non-obvious problem. When an
  orchestrator dispatches multiple workers via `dispatch-workflow`, each worker is a
  separate GitHub Actions workflow run. However, within each worker's run, the
  compiler generates job-level concurrency groups that include the workflow name but
  not the specific dispatch input (e.g., `target_repo` or `finding_id`). If two
  workers are dispatched for different inputs, their compiler-generated job groups
  collide — one cancels the other. The `job-discriminator` appends the input value
  to the job-level groups, making them unique per dispatch. The three patterns cover
  the main use cases: `inputs.finding_id` for domain-specific discrimination,
  `github.run_id` for guaranteed uniqueness (any dispatched run has a unique run ID),
  and the `|| github.run_id` fallback for cases where the input may be absent.
  For Ch04 (Multi-Agent Orchestration): `job-discriminator` is the required
  configuration for any orchestrator using `dispatch-workflow` with more than one
  concurrent dispatch — without it, fan-out workflows silently cancel each other
  at the job level, creating apparent non-determinism in which worker completes.
  This is the single most non-obvious concurrency footgun in gh-aw fan-out design.

## Concrete Artifacts

### Per-Workflow Concurrency Group Formats by Trigger Type (from source)

```
Trigger       | Group Format                                                              | Cancel In Progress
------------- | --------------------------------------------------------------------------| ------------------
Issues        | gh-aw-${{ github.workflow }}-${{ issue.number }}                          | No
Pull Requests | gh-aw-${{ github.workflow }}-${{ pr.number || ref }}                      | Yes
Push          | gh-aw-${{ github.workflow }}-${{ github.ref }}                            | No
Schedule/Other| gh-aw-${{ github.workflow }}                                               | No
Labels        | gh-aw-${{ github.workflow }}-${{ entity.number }}-${{ github.event.label.name }} | Conditional
```

### Custom Concurrency Override YAML (from source)

```yaml
concurrency:
  group: custom-group-${{ github.ref }}
  cancel-in-progress: true
engine:
  id: copilot
  concurrency:
    group: "gh-aw-copilot-${{ github.workflow }}"
```

Users can override either tier independently. The example shows a custom workflow-level
group (with explicit `cancel-in-progress: true`) and a custom engine-level group that
scopes the copilot singleton to a per-workflow granularity rather than the global default.

### Per-Engine Singleton Default

```
Default engine concurrency group pattern: gh-aw-{engine-id}

Scope: engine identifier + prefix only
Excludes: workflow names, issue/PR numbers, branch references

Effect: one agent job per engine across all workflows (global singleton per engine)
```

### Fan-Out `job-discriminator` Patterns (from source)

```yaml
# In fan-out worker workflow frontmatter:
concurrency:
  job-discriminator: ${{ inputs.finding_id }}             # input-specific uniqueness
  # or:
  job-discriminator: ${{ github.run_id }}                 # universal run-level distinctness
  # or:
  job-discriminator: ${{ inputs.organization || github.run_id }}  # conditional fallback
```

Purpose: appends the discriminator to compiler-generated job-level concurrency groups,
making each dispatched run's jobs unique — preventing fan-out cancellations.

### Conclusion Job Auto-Generated Group Format

```
Conclusion job group: gh-aw-conclusion-{workflow-name}
With job-discriminator: gh-aw-conclusion-{workflow-name}-{discriminator-value}

Behavior: non-cancelling (cancel-in-progress: false)
```

### Safe Outputs Job Concurrency

```
Default:  safe_outputs job processes independently from agent jobs
Config:   safe-outputs.concurrency-group (user-configurable)
Behavior: uses cancel-in-progress: false (queued runs wait rather than being discarded)
Purpose:  prevents duplicate operations in issue/PR creation workflows
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-workqueue-ops.md` Claim 9 ("Use `concurrency.group` with
    `cancel-in-progress: false` to prevent parallel runs"): The WorkQueueOps
    guidance to use `cancel-in-progress: false` for stateful queue workflows is
    consistent with this reference's Safe Outputs job design. Both sources
    identify `cancel-in-progress: false` as the correct setting when partial-
    state corruption from cancellation is the risk — WorkQueueOps at the workflow
    level; Safe Outputs processing at the job level.
  - `docs-ghaw-central-repo-ops.md` Concrete Artifacts → "Complete Worker Workflow
    Frontmatter": The Dependabot Rollout worker uses custom engine concurrency
    overrides (`engine.concurrency.group: gh-aw-copilot-${{ github.workflow }}-${{ github.event.inputs.target_repo }}`) — exactly the pattern Claim 5 here describes
    as necessary for fan-out scenarios. The CentralRepoOps note provides the
    production instantiation; this reference provides the platform specification
    behind it.
  - `blog-ghaw-weekly-2026-03-30.md` Concrete Artifacts → "Version Summary"
    (v0.64.0: "bot-actor concurrency isolation for workflows combining safe-outputs
    with comment triggers"): That changelog entry documented a specific concurrency
    isolation fix without explaining the configuration API. This reference provides
    the Safe Outputs independent processing model that the v0.64.0 fix operates within.

- **Extends**:
  - `docs-ghaw-orchestration-patterns.md` Claim 2 (`dispatch-workflow` fans out
    via `workflow_dispatch` API — async, independent worker runs) and Claim 4
    (decision framework between `dispatch-workflow` and `call-workflow`): The
    orchestration patterns note documents *what* fan-out mechanisms exist and
    *when* to use them. This reference documents the concurrency management layer
    *beneath* those mechanisms — specifically the `job-discriminator` (Claim 8
    here) that prevents fan-out workers from silently cancelling each other's
    jobs. The two sources compose: orchestration patterns explains the dispatch
    choice; concurrency reference explains what must be configured for the dispatch
    to work correctly in parallel.
  - `docs-ghaw-safe-rollout.md` Claim 5 ("Use shadow evaluation when staged mode
    is too weak because the real write path itself needs validation" — including
    when "concurrency, deduplication, or serialization needs to be tested on a
    live-like surface"): The safe rollout note identifies concurrency as a class
    of behavior that requires live-like testing. This reference provides the
    specific configuration model that teams are testing — knowing what the two
    tiers look like in production is prerequisite to knowing what to validate.

- **Contradicts**: None identified. No existing source note makes claims about
  gh-aw concurrency configuration that oppose this reference's specifications.
  `docs-ghaw-workqueue-ops.md` Claim 9 and this reference both recommend
  `cancel-in-progress: false` for stateful workflows — consistent, not opposing.
  No contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **Five-row trigger-type concurrency group table with exact expressions**: No
    prior corpus note documents the per-trigger group format expressions. The
    CentralRepoOps and orchestration notes show examples of custom overrides but
    not the system defaults they override.
  - **Per-engine singleton enforcement model**: The `gh-aw-{engine-id}` default
    and its scope exclusions (workflow names, issue/PR numbers, branch refs
    excluded) are not described in any prior source note, including
    `docs-ghaw-how-they-work.md`.
  - **`job-discriminator` as fan-out collision resolver**: The `concurrency.job-discriminator` field and its three common patterns are not documented in any
    existing source note, including `docs-ghaw-orchestration-patterns.md`. This
    is the most operationally critical novel piece: teams using `dispatch-workflow`
    fan-out without `job-discriminator` will experience silent job cancellations
    with no obvious error.
  - **Safe Outputs job independent processing with `cancel-in-progress: false`**:
    The separation of Safe Outputs job concurrency from agent job concurrency, and
    the non-cancelling semantics of `safe-outputs.concurrency-group`, are not
    described in any prior note (including `docs-ghaw-how-they-work.md`'s
    Safe Outputs coverage).
  - **Conclusion job auto-generated non-cancelling group**: The `gh-aw-conclusion-{workflow-name}` auto-grouping and its interaction with `job-discriminator`
    are entirely new to the corpus.
  - **Labels trigger with conditional `cancel-in-progress`**: The labels trigger's
    conditional cancellation behavior is a nuance not covered by any prior source.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the two-tier concurrency architecture as a foundational harness design
  concept** (Claim 1): Before covering specific workflow configurations, introduce
  the two tiers (trigger-scoped workflow groups + engine-level singleton) and their
  separate concerns. This is the concurrency mental model for all gh-aw harness design.

- **Add the trigger-type concurrency table as a reference** (Claim 2, Concrete
  Artifacts): Teams designing workflows need to know which default concurrency
  behavior their trigger type establishes. The table is the authoritative reference
  for this decision. Highlight the PR `cancel-in-progress: true` default as the
  most-impactful difference from other triggers.

- **Add `job-discriminator` as a required field for `dispatch-workflow` fan-out**
  (Claim 8): Frame as a mandatory configuration, not an optimization. Without it,
  fan-out dispatches silently cancel each other's jobs — a failure mode that
  produces correct-looking logs but incorrect execution. Cite the three common
  patterns (`inputs.finding_id`, `github.run_id`, `|| github.run_id` fallback)
  and recommend `github.run_id` as the safe default when no domain-specific
  discriminator exists.

- **Add `cancel-in-progress: false` for Safe Outputs configuration** (Claim 6):
  When using Safe Outputs for issue/PR creation in high-frequency trigger workflows,
  configure `safe-outputs.concurrency-group` explicitly to prevent duplicate output
  delivery.

### Chapter 04: Multi-Agent Orchestration Patterns

- **Add per-engine singleton as the concurrency constraint on parallel agent
  workers** (Claim 3): The orchestration patterns chapter documents `dispatch-workflow`
  for fan-out but does not document the per-engine concurrency limit that serializes
  all dispatched workers by default. Add this constraint prominently: fan-out only
  achieves true parallelism when workers override their engine concurrency groups.
  Cross-reference the CentralRepoOps worker YAML as the production example.

- **Add `job-discriminator` to the fan-out design checklist** (Claim 8): Alongside
  `max`, `cancel-in-progress: false`, and engine concurrency overrides, `job-discriminator`
  is a required field for fan-out worker workflows. Document the failure mode
  (silent job cancellations) explicitly so teams recognize it when they encounter it.

- **Add Conclusion job group interaction** (Claim 7): For fan-out workflows, verify
  `job-discriminator` is set consistently across all job types — Conclusion jobs
  using a shared group become the unexpected serialization bottleneck in otherwise-
  parallel fan-out.

## Extraction Notes

1. **Source access via WebFetch AI model**: The `WebFetch` tool processes page content
   through an AI model before returning results. Two fetch passes were made: the first
   returned structured content including the trigger table and YAML examples; the
   second confirmed content but refused verbatim reproduction citing copyright
   constraints. Quotes for technical strings (group format expressions, field names,
   YAML keys) were taken from the first fetch, which returns these accurately. Prose
   descriptions are paraphrased rather than quoted where the AI model's interpretation
   may differ from source wording; these are marked "(no direct quote; see paraphrase
   in Our assessment)."

2. **Table of trigger types**: The five-row trigger table (Issues, Pull Requests, Push,
   Schedule/Other, Labels) was extracted from the first fetch with group format
   expressions that match the technical conventions documented throughout the gh-aw
   corpus. The expressions appear to be verbatim from the source (they are technical
   strings, not prose).

3. **Custom YAML override example**: The YAML code block for custom concurrency
   configuration was consistently returned across both fetches in the same form and
   matches the conventions shown in `docs-ghaw-central-repo-ops.md`'s worker workflow
   YAML.

4. **`job-discriminator` three patterns**: The three `job-discriminator` expressions
   (`inputs.finding_id`, `github.run_id`, `inputs.organization || github.run_id`) were
   extracted from the first fetch. These appear to be direct source examples given their
   specificity.

5. **No contradictions filed**: Reviewed all existing corpus source notes. No existing
   note makes claims that materially oppose the two-tier concurrency model, the trigger-
   type group formats, the per-engine singleton, or the `job-discriminator` mechanism.
   The concurrency guidance in `docs-ghaw-workqueue-ops.md` Claim 9 is consistent with
   this reference (both recommend `cancel-in-progress: false` for stateful scenarios).
   No contradiction issue required.
