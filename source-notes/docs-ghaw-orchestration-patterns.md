---
source_url: https://github.github.com/gh-aw/patterns/orchestration
source_type: docs
title: "GitHub Agentic Workflows: Orchestration Patterns"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-02
last_checked: 2026-05-02
status: current
confidence_overall: emerging
issue: "#330"
---

# GitHub Agentic Workflows: Orchestration Patterns

> Canonical reference for gh-aw's orchestrator/worker fan-out model — documents
> the concrete decision rule between `dispatch-workflow` (async, API-based,
> workers outlive parent) and `call-workflow` (compile-time fan-out, actor
> attribution preserved, workers must finish before orchestrator concludes),
> with compile-time validation guarantees and a correlation-ID coordination
> convention not documented in any existing corpus note.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/orchestration`
  page — in the same `patterns/` section as `patterns/monitoring` covered by
  `docs-ghaw-monitoring-patterns.md`. Patterns pages are practitioner
  implementation references, distinct from the conceptual `introduction/`
  pages and the practitioner `guides/` section.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team that operates Peli de Halleux's agent factory. YAML
  configurations and CLI behavior are authoritative for the `gh aw` platform.
  Claims about the orchestration model are settled platform design; they do
  not generalize to non-`gh-aw` multi-agent systems without qualification.
- **Scope**: Covers one specific orchestration architecture (orchestrator +
  workers) and the two fan-out mechanisms (`dispatch-workflow` and
  `call-workflow`), plus correlation-ID passing as a coordination convention.
  Does NOT cover: the Safe Outputs model in general (see
  `docs-ghaw-how-they-work.md`), how orchestrators themselves are authored
  (see `docs-ghaw-agentic-authoring.md`), observability for multi-workflow
  runs (see `docs-ghaw-monitoring-patterns.md`), or cost benchmarks for
  the two dispatch mechanisms.

## Extracted Claims

### Claim 1: The orchestrator/worker pattern is the canonical gh-aw model for fan-out — orchestrator decides and splits work; workers execute with scoped permissions

- **Evidence**: The page opens with this pattern as the top-level architecture:
  "Use this pattern when one workflow (the orchestrator) needs to fan out work
  to one or more worker workflows." Roles are explicitly differentiated:
  orchestrator = decides + splits; worker = executes with scoped permissions
  and tools.
- **Confidence**: settled (first-party platform documentation; this is the
  canonical reference for the pattern, not a practitioner inference)
- **Quote**: "Use this pattern when one workflow (the orchestrator) needs to
  fan out work to one or more worker workflows."
- **Our assessment**: The role separation — orchestrator as decision-maker,
  worker as executor — is the gh-aw answer to the "how do you split reasoning
  from action?" question in multi-agent systems. The scoped-permissions
  qualifier on workers is significant: workers are not just subordinate by
  task but by capability. This maps to the five-layer security model in
  `docs-ghaw-how-they-work.md` — workers have only the permissions their
  workflow frontmatter grants, not the orchestrator's full permission set.
  For Ch04 (multi-agent orchestration patterns): this is the reference
  definition of the pattern in the CI-native context.

### Claim 2: `dispatch-workflow` fans out via GitHub's `workflow_dispatch` API — async, independent worker runs, supports up to 10 workers, workers can outlive the parent run

- **Evidence**: The page provides the YAML configuration and behavioral
  description: workers "receive a JSON payload and run asynchronously as
  independent workflow runs." The `max: 10` cap is shown in the config block.
  Workers can "run asynchronously, outlive the parent run, or need
  `workflow_dispatch` inputs."
- **Confidence**: settled (first-party documentation; YAML config block is
  authoritative)
- **Quote**: "Workers receive a JSON payload and run asynchronously as
  independent workflow runs."
- **Our assessment**: The key design implication of `dispatch-workflow` is
  decoupling: the orchestrator's run concludes independently of whether
  workers complete. This makes it the right choice for long-running workers
  (e.g., a full dependency audit that takes 30+ minutes) where blocking the
  orchestrator is wasteful. The `max: 10` cap is a platform-level constraint
  that affects fan-out planning — orchestrators that need to dispatch more
  than 10 workers must batch or use a different pattern. The API-call overhead
  is the cost of this decoupling.

### Claim 3: `call-workflow` fans out via compile-time expansion — no API call at runtime, compiler generates a typed MCP tool per worker, preserves `github.actor` and billing attribution

- **Evidence**: The page describes the compile-time mechanism explicitly: "The
  compiler validates that each worker declares `workflow_call`, generates a
  typed MCP tool per worker from its inputs, and emits a conditional `uses:`
  job. At runtime the worker whose name the agent selected executes as part
  of the same workflow run—preserving `github.actor` and billing attribution."
- **Confidence**: settled (first-party documentation; the compile-time
  mechanism is an architectural property of the platform)
- **Quote**: "The compiler validates that each worker declares `workflow_call`,
  generates a typed MCP tool per worker from its inputs, and emits a
  conditional `uses:` job. At runtime the worker whose name the agent selected
  executes as part of the same workflow run—preserving `github.actor` and
  billing attribution."
- **Our assessment**: This is the most architecturally novel claim in the
  source. The compiler generating a typed MCP tool from each worker's
  `workflow_call` inputs is a concrete demonstration of how gh-aw's compile
  model creates agent-navigable capabilities from workflow definitions. It
  extends `docs-ghaw-how-they-work.md` Claim 7 (the `.md` → `.lock.yml`
  compilation model) with a new produced artifact: per-worker MCP tool
  schemas. The actor/billing attribution preservation is important for
  auditability — when a `call-workflow` worker creates a PR, the PR is
  attributed to the triggering user, not to a bot identity. For Ch02 and
  Ch04: the compile-time MCP tool generation is a harness design guarantee
  with no equivalent in `dispatch-workflow`.

### Claim 4: The decision between `dispatch-workflow` and `call-workflow` follows a three-way criterion: actor attribution, worker lifetime, and API overhead

- **Evidence**: The page states the decision rule directly: "Use `call-workflow`
  when actor attribution matters, workers must finish before the orchestrator
  concludes, or you want zero API overhead. Use `dispatch-workflow` when
  workers should run asynchronously, outlive the parent run, or need
  `workflow_dispatch` inputs."
- **Confidence**: settled (explicit recommendation from first-party
  documentation; not a practitioner inference)
- **Quote**: "Use `call-workflow` when actor attribution matters, workers must
  finish before the orchestrator concludes, or you want zero API overhead.
  Use `dispatch-workflow` when workers should run asynchronously, outlive the
  parent run, or need `workflow_dispatch` inputs."
- **Our assessment**: This three-way decision rule is the most directly
  actionable claim in the source. It maps to three distinct concerns:
  (1) auditability — does the PR/issue need to show the triggering user, not
  a bot? → `call-workflow`; (2) synchronization — must the orchestrator know
  workers completed before concluding? → `call-workflow`; (3) lifetime — can
  workers run for hours after the orchestrator exits? → `dispatch-workflow`.
  The zero-API-overhead criterion for `call-workflow` is important at scale:
  if an orchestrator dispatches 8 workers via `dispatch-workflow`, that is 8
  API calls at fan-out time; `call-workflow` makes none. For Ch04: this
  three-way rule should be the primary decision framework for practitioners
  designing multi-agent fan-out.

### Claim 5: Compile-time validation enforces that `dispatch-workflow` targets support `workflow_dispatch` and `call-workflow` targets declare `workflow_call` — a structural safety guarantee before any agent runs

- **Evidence**: The page states for `dispatch-workflow`: "During compilation,
  gh-aw validates the target workflows exist and support `workflow_dispatch`."
  For `call-workflow`: "The compiler validates that each worker declares
  `workflow_call`." Both validations happen at compile time, before the lock
  file is generated.
- **Confidence**: settled (first-party documentation; this is part of the
  compile-time validation layer described in `docs-ghaw-how-they-work.md`
  Claim 3)
- **Quote**: "During compilation, gh-aw validates the target workflows exist
  and support `workflow_dispatch`." / "The compiler validates that each worker
  declares `workflow_call`."
- **Our assessment**: This is a concrete instance of `docs-ghaw-how-they-work.md`
  Claim 3 (Layer 1: compilation-time validation). The orchestration-specific
  content: the compiler does not just validate the orchestrator's structure
  but also checks that named target workflows have the correct trigger
  configuration. This prevents a class of runtime failures — dispatching to
  a workflow that doesn't accept `workflow_dispatch` — from ever reaching
  execution. For Ch02 (Harness Engineering): this is the design guarantee
  that makes `dispatch-workflow` and `call-workflow` safer to use than raw
  GitHub Actions API calls from a script. The compile step is the trust layer.

### Claim 6: Correlation IDs (e.g., `tracker_id`) are the recommended convention for passing shared context across workers in a fan-out run

- **Evidence**: The page recommends: "If your workers need shared context,
  pass an explicit input such as `tracker_id` (string) and include it in
  worker outputs (e.g., writing it into a Project custom field)." This is the
  platform's recommended coordination primitive for multi-worker runs.
- **Confidence**: emerging (recommended pattern; the platform does not enforce
  it; implementations may use different conventions)
- **Quote**: "If your workers need shared context, pass an explicit input such
  as `tracker_id` (string) and include it in worker outputs (e.g., writing it
  into a Project custom field)."
- **Our assessment**: The correlation ID pattern is the lightweight coordination
  primitive for workers that need to contribute to a shared artifact (e.g.,
  multiple workers each processing a different repository, all posting results
  to the same GitHub Project board). The Project custom field write is
  significant: it connects the correlation ID pattern to the `update-project`
  safe output documented in `docs-ghaw-monitoring-patterns.md`. Together they
  form a complete coordination model: the orchestrator passes `tracker_id` to
  each worker; each worker writes its results tagged with `tracker_id` to the
  Project board; the orchestrator (or a monitoring agent) can then aggregate
  by `tracker_id`. For Ch04: name this as the "correlation ID + Project board"
  coordination convention.

### Claim 7: Both orchestrator and workers can optionally update a shared GitHub Project board for cross-workflow visibility

- **Evidence**: The page lists as part of the pattern: "Optional monitoring:
  both orchestrator and workers can update a GitHub Project board for
  visibility." This is presented as an optional extension of the base pattern.
- **Confidence**: settled (first-party; this is the same `update-project`
  safe output documented in `docs-ghaw-monitoring-patterns.md`)
- **Quote**: "Optional monitoring: both orchestrator and workers can update a
  GitHub Project board for visibility."
- **Our assessment**: This is not novel in isolation — `docs-ghaw-monitoring-patterns.md`
  covers `update-project` in detail. Its significance here is that the
  orchestration page explicitly endorses Project board updates from both the
  orchestrator and workers simultaneously, confirming that multiple concurrent
  workflows can safely write to the same Project board. This is the
  distributed-write case for `update-project` not explicitly covered by the
  monitoring patterns note. For Ch04: the monitoring integration is a
  recommended extension, not an afterthought — the orchestration pattern
  documentation itself points practitioners toward it.

## Concrete Artifacts

### `dispatch-workflow` Safe Output Config

```yaml
# Orchestrator workflow frontmatter
safe-outputs:
  dispatch-workflow:
    workflows: [repo-triage-worker, dependency-audit-worker]
    max: 10
```

- Workers receive a JSON payload via the `workflow_dispatch` API
- Workers run as independent workflow runs (async, can outlive the parent)
- Compile-time: gh-aw validates each named workflow supports `workflow_dispatch`
- `max: 10` is the platform cap; orchestrators needing >10 workers must batch

*Source: `patterns/orchestration` — "Dispatch workers with `dispatch-workflow`" section*

### `call-workflow` Safe Output Config

```yaml
# Orchestrator workflow frontmatter
safe-outputs:
  call-workflow:
    workflows: [spring-boot-bugfix, frontend-dep-upgrade]
    max: 1
```

- Compiler generates a typed MCP tool per named worker (derived from worker's `workflow_call` inputs)
- Compiler emits a conditional `uses:` job in the lock file (no API call at runtime)
- Worker executes as part of the same workflow run as the orchestrator
- Preserves `github.actor` and billing attribution
- Compile-time: gh-aw validates each named workflow declares `workflow_call`

*Source: `patterns/orchestration` — "Call workers with `call-workflow`" section*

### Decision Table: `call-workflow` vs `dispatch-workflow`

```
Use call-workflow when:                  Use dispatch-workflow when:
-------------------------------          --------------------------------
Actor attribution matters                Workers should run asynchronously
  (PR/issue attributed to triggering     Workers may outlive the parent run
  user, not a bot identity)
                                         Workers need workflow_dispatch inputs
Workers MUST finish before               (custom parameters at dispatch time)
  orchestrator concludes
                                         Workers are long-running and blocking
Zero API overhead required               the orchestrator is wasteful
  (no API call at fan-out time)

Characteristics:                         Characteristics:
  - Compile-time fan-out                   - Runtime API call per worker
  - Typed MCP tool per worker              - Workers decouple from parent
  - Workers share parent's run             - max: 10 cap
  - Synchronous completion                 - max: any (within cap)
```

*Source: `patterns/orchestration` — "Choosing between the two approaches" section*

### Correlation ID + Project Board Coordination Pattern

```
Pattern: pass tracker_id as an explicit input to all workers

Orchestrator → dispatches workers with:
  inputs:
    tracker_id: "<orchestrator-run-id-or-issue-number>"

Workers → on completion, write to Project board:
  update-project:
    field: tracker_id = "<received tracker_id>"
    status: <worker result>

Monitoring agent (optional) → aggregates by tracker_id
  across all workers' Project entries

Purpose: correlate distributed worker outputs back to the
  originating orchestrator run, without workers needing to
  communicate directly with each other or with the orchestrator.
```

*Source: `patterns/orchestration` — "Passing correlation IDs" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth security
    pipeline, Layer 1: compilation-time validation): Claim 5 here is a concrete
    instance — compile-time validation that dispatch targets support
    `workflow_dispatch` and call targets declare `workflow_call` is a named
    application of that first security layer to the orchestration surface.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as permission-separated
    state mutation): Both `dispatch-workflow` and `call-workflow` are Safe Outputs.
    This source confirms that fan-out itself is gated through the Safe Outputs
    permission model — the orchestrator cannot dispatch workers unless the
    workflow spec explicitly declares which workers it is allowed to call.
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation model):
    Claim 3 here extends the compilation model with a specific produced artifact —
    the compiler generates a typed MCP tool per `call-workflow` worker. This is
    a new concrete output of the compile step not described in the original
    compilation model documentation.
  - `docs-ghaw-monitoring-patterns.md` (Claim 1 on `update-project` for workflow
    audit trails): Claim 7 here confirms that both orchestrators and workers can
    write to the same Project board, enabling the correlation ID + Project board
    coordination convention (Claim 6). The two sources together define the
    distributed-write use case for `update-project`.

- **Extends**:
  - `blog-ghaw-agent-observability.md` Claim 7 (metrics as orchestration input,
    multi-workflow fan-out referenced in passing): That source mentions multi-workflow
    runs in the context of observability but does not document the dispatch
    mechanisms. This source provides the mechanism layer — how the fan-out actually
    happens — beneath the observability discussion.
  - `docs-ghaw-agent-factory-status.md` Claim 5 (factory monitors itself with
    dedicated meta-workflows): The Agent Performance Analyzer listed as a
    "Meta-Orchestrator" in the agent factory catalog is likely an application of
    this orchestration pattern — an orchestrator dispatching monitoring workers
    across the factory. This note provides the implementation primitives behind
    what the catalog labels "meta-orchestrator."
  - `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts allow inline tool definitions):
    Claim 3 here reveals that `call-workflow` generates MCP tools at compile time
    from worker workflow inputs. This is a second path to typed MCP tools — the
    existing note documents MCP Scripts (inline definitions); this source adds
    compiler-derived tools from reusable workflow schemas. Together they describe
    two distinct MCP tool generation mechanisms in gh-aw.

- **Contradicts**: None. No existing source note makes claims that conflict with the
  orchestrator/worker pattern, the two dispatch mechanisms, or compile-time
  validation. The Safe Outputs model in `docs-ghaw-how-they-work.md` is consistent
  with both `dispatch-workflow` and `call-workflow` being Safe Output types —
  this source adds specifics without opposing the base model. No contradiction
  issue required.

- **Novel**:
  - **`dispatch-workflow` vs `call-workflow` decision framework** (Claims 2, 3, 4):
    No existing note documents either mechanism or the three-way decision rule
    (actor attribution / synchronization / API overhead). This is entirely new to
    the corpus.
  - **Compiler-generated typed MCP tools per worker** (Claim 3): The specific
    compilation step that produces a named, typed MCP tool for each `call-workflow`
    target — derived from the worker's `workflow_call` input declarations — is not
    described in any existing note, including the compilation model documentation.
  - **Orchestration as a Safe Output type** (Claims 2, 3): Both fan-out mechanisms
    are Safe Outputs. No existing note identifies worker dispatch as a capability
    gated by the Safe Outputs permission model.
  - **Compile-time validation for orchestration targets** (Claim 5): The specific
    validation checks (dispatch targets support `workflow_dispatch`; call targets
    declare `workflow_call`) are new to the corpus, extending the general
    compilation-time validation claim in `docs-ghaw-how-they-work.md`.
  - **Correlation ID + Project board coordination convention** (Claim 6): The
    `tracker_id` input + Project custom field write as a coordination primitive
    for distributed workers is not described in any existing source note.

## Guide Impact

### Chapter 04: Multi-Agent Orchestration Patterns

- **Add orchestrator/worker pattern as the canonical gh-aw multi-agent
  architecture** (Claim 1): When one agent needs to fan out work, the
  pattern is: orchestrator decides + splits, workers execute with scoped
  permissions. Cite this as the official gh-aw reference; generalize with
  caution to other platforms.

- **Add `dispatch-workflow` vs `call-workflow` decision framework** (Claims 2-4):
  The three-way decision rule (actor attribution → call; async lifetime →
  dispatch; API overhead concerns → call) should be the primary decision
  aid for practitioners designing multi-agent fan-out in CI-native
  environments. Extract as a decision table in the chapter.

- **Add correlation ID + Project board as a coordination convention** (Claims 6, 7):
  For workers that contribute to a shared output, the `tracker_id` +
  `update-project` pattern is the lightweight coordination primitive.
  This does not require workers to communicate directly — the Project
  board is the shared state. Cross-reference with `docs-ghaw-monitoring-patterns.md`.

### Chapter 02: Harness Engineering

- **Add compile-time orchestration validation as a safety property** (Claim 5):
  gh-aw's compile step validates not just the orchestrator workflow's structure
  but also that named target workflows have the correct trigger configuration
  (`workflow_dispatch` or `workflow_call`). This is a concrete instance of the
  "validate at compile time" principle from `docs-ghaw-how-they-work.md` Claim 3
  applied to multi-agent fan-out. For guide: frame this as "the compiler is the
  trust layer for multi-agent orchestration — it catches target misconfigurations
  before any agent runs."

- **Extend the MCP tool generation picture** (Claim 3): Ch02 currently covers
  MCP Scripts (inline tool definitions) from `docs-ghaw-how-they-work.md`. Add
  compiler-generated MCP tools from `call-workflow` worker inputs as a second
  generation path. The distinction: MCP Scripts are manually authored inline;
  `call-workflow` MCP tools are derived automatically from worker workflow
  schemas at compile time.

### Chapter 05: Workflow Design / Team Adoption

- **`dispatch-workflow` max:10 cap affects fan-out planning**: Teams designing
  orchestration patterns that need more than 10 parallel workers must either
  batch dispatch across multiple orchestrator runs or use a different fan-out
  strategy. Flag this constraint for teams planning large-scale fan-out.

## Extraction Notes

1. **Source is compact but information-dense**: The page is shorter than
   most gh-aw documentation (roughly 300-400 words plus two YAML blocks and
   a brief prose section each). The depth is in the specific claims, not in
   narrative explanation. Claims were fully exhausted in 7 extractions.

2. **Page structure follows the `patterns/` convention**: Like
   `patterns/monitoring`, this page describes configuration-layer patterns
   rather than conceptual architecture. YAML configs are the primary artifact;
   prose explains when and why to use each.

3. **"See `dispatch-workflow` safe output" and "See `call-workflow` safe output"
   links**: The page references separate safe-output reference pages that
   detail the full YAML schemas. These sub-pages were not followed (they are
   API-reference-style, not patterns documentation). The YAML blocks on the
   orchestration page are representative configs, not full schema references.

4. **`max: 1` in the `call-workflow` example**: The `call-workflow` config
   shows `max: 1` — the orchestrator calls exactly one worker per run (the
   agent selects which). This is different from `dispatch-workflow`'s `max: 10`
   (up to 10 workers). Whether `call-workflow` supports `max > 1` is not
   stated on this page; the example only shows the single-selection case.

5. **No publication date**: Like other gh-aw documentation pages, this page
   does not carry an explicit publication date. `date_published` is left null.

6. **No contradictions to file**: Reviewed all existing source notes against
   all claims. No claims here materially oppose any existing source note at
   the MINER.md §4a filing threshold. The compile-time validation claim
   extends, not opposes, `docs-ghaw-how-they-work.md` Claim 3.
