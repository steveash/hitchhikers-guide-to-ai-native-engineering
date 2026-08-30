---
source_url: https://github.github.com/gh-aw/experimental/trace-graders
source_type: docs
title: "GitHub Agentic Workflows: Graders"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: emerging
issue: "#3107"
---

# GitHub Agentic Workflows: Graders

> Introduces `graders` — an experimental gh-aw feature that computes
> deterministic execution metrics (tool success rate, retries, loops,
> trajectory efficiency, and five others) as a post-agent step with zero
> additional LLM calls, plus a reserved `operational-value` grader that runs
> a compiler-frozen, SHA-256-digested Bash evaluator to score real-world
> repository outcomes and supports tamper-evident historical regrading. The
> normative `Graders Specification` (linked from the docs page and fetched as
> a companion source) formalizes all of this with MUST/MUST NOT requirements
> and — critically — defines how graders plug directly into gh-aw's A/B
> experiment system as `grader:<id>` metric references.

## Source Context

- **Type**: docs (a `github.github.com/gh-aw` page in the `/experimental/`
  section — same tier as `docs-ghaw-enclaves.md` and
  `docs-ghaw-drive-memory.md`. Explicitly marked "Graders are an experimental
  feature." This note also fetched the companion normative document, the
  **Graders Specification** at `github.github.com/gh-aw/specs/graders-specification`
  (Version 0.2.0, Status: Draft Specification, Feature Status: Experimental),
  which the docs page links to directly: "For normative requirements, see the
  Graders Specification." Both pages are treated as one combined source per
  MINER.md §1's "follow up to 5 linked pages" allowance — the docs page is
  the practitioner-facing quick-start; the spec is the formal contract.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind the `gh aw` CLI,
  the Effective Tokens and A/B Experiments specifications already in this
  corpus, and Peli de Halleux's "Agent Factory" blog series). The spec uses
  RFC 2119 requirement language (MUST, MUST NOT, SHOULD, MAY) throughout,
  the same normative style as `docs-ghaw-effective-tokens-specification.md`
  and `docs-ghaw-practices-experiments-specification.md`.
- **Scope**: The docs page covers configuration (quick start, built-in
  grader table, selective enable/disable, custom inline graders, the
  operational-value grader, historical regrading, output files, and
  execution timing). The specification adds conformance levels, formal
  configuration semantics, the full built-in grader ID list, custom-grader
  script constraints (including forbidden patterns the docs page only
  partially lists), the formal operational-value evaluator contract,
  security/isolation requirements, a compliance test suite (T-GRD-001
  through T-GRD-014), and — the single most consequential addition — §9
  "Experiment Metric References," which formally ties grader outputs into
  the gh-aw A/B experiment pipeline. Neither page covers: the trace
  preprocessing format itself (what fields a `trace` object exposes beyond
  `toolCalls`), UI visualization of grader results (explicitly out of scope
  per spec §1.2), or external metric backends (also explicitly out of scope).

## Extracted Claims

### Claim 1: Graders compute deterministic execution metrics without issuing any additional LLM calls, inspecting post-agent execution traces; a reserved `value` grader instead evaluates operational repository outcomes under a frozen function and explicit evidence cutoff, with all results persisted to the agent artifact for downstream tooling

- **Evidence**: Docs page opening paragraph; spec §1.1 "Purpose" states the
  same design goal in formal terms.
- **Confidence**: settled (first-party; this is the foundational framing
  repeated consistently across both the docs page and the specification)
- **Quote**: "Graders compute deterministic metrics without LLM calls.
  Built-in and custom inline graders inspect post-agent execution traces.
  The reserved value grader evaluates operational repository outcomes under
  a frozen function and explicit evidence cutoff. Results are persisted in
  the agent artifact for downstream tools." (docs page, opening paragraph)
- **Quote**: "The graders feature provides deterministic execution metrics
  and operational value observations without issuing additional LLM calls."
  (spec §1.1 Purpose)
- **Our assessment**: This is a distinct instance of the corpus's
  "deterministic computation vs. agentic reasoning" separation principle
  (`docs-ghaw-deterministic-agentic-patterns.md` Claim 1's three-stage
  pipeline), but applied to a fourth position that pipeline note does not
  cover: deterministic *evaluation of the agent's own completed run*, not
  pre-agent data fetching or post-agent output delivery. Graders are neither
  Stage 1 (precompute) nor Stage 3 (safe-outputs delivery) in that note's
  model — they run alongside/after Stage 3, grading the trace the agent
  already produced. For Ch02 (Harness Engineering): add "post-hoc
  deterministic grading" as a fourth pipeline position distinct from
  precomputation, agent reasoning, and safe-output delivery.

### Claim 2: Grader configuration has exactly two enable states with no partial middle ground — an empty map (`graders: {}`) enables every built-in grader with default settings, while omitting the `graders` key entirely disables grading completely (no grading step is emitted in the compiled workflow at all)

- **Evidence**: Docs page "Quick start" section; formalized as MUST
  requirements in spec §4.2 "Enable/Disable Semantics," which adds a third
  rule not stated in the docs page: if `graders` is present but ends up with
  zero enabled graders, configuration MUST fail outright (not silently
  no-op).
- **Confidence**: settled (first-party; both the docs example and the
  spec's normative §4.2 agree, and the compliance test suite includes
  T-GRD-001 and T-GRD-002 covering exactly these two states)
- **Quote**: "`graders: {}` — An empty map enables all built-in graders
  with default settings. Omitting the `graders` field entirely disables
  grading (no step is emitted)." (docs page, "Quick start")
- **Quote**: "If `graders` is omitted, grading MUST be disabled. If
  `graders: {}` is provided, all built-in graders MUST be enabled with
  defaults. If `graders` is present, at least one grader MUST be enabled;
  otherwise configuration MUST fail." (spec §4.2)
- **Our assessment**: The "at least one grader MUST be enabled or
  configuration MUST fail" rule is the practically important addition the
  docs page omits entirely — a workflow author who writes `graders:` with
  every built-in explicitly disabled (e.g., to scaffold custom graders
  later) and no custom graders yet defined will get a compile-time failure,
  not a silently-empty grading step. For Ch02: when documenting the
  `graders:` key, include the fail-fast rule for the "present but nothing
  enabled" case — it is a compile-time guard, not a runtime warning.

### Claim 3: Ten built-in grader IDs are reserved and MUST be recognized by any conforming implementation, spanning tool-call quality (success rate, failure count, retries, loops, trajectory efficiency), execution shape (step count, duration), and context-management health (working-set rebuild factor, context growth, artifact production)

- **Evidence**: Docs page "Built-in graders" table (9 rows with ID,
  description, and value type/range for each); spec §5 "Built-in Graders"
  lists the same set as a formal MUST-recognize requirement, with one
  additional entry (`execution-step-count`) present in the spec's ID list
  that the docs table also independently documents as row 6.
- **Confidence**: settled (first-party; the docs page table and the spec's
  formal enumeration agree on all ten IDs)
- **Quote** (docs page table, verbatim rows):

  | ID | Description | Value |
  |---|---|---|
  | `tool-success-rate` | Fraction of tool calls that succeeded | 0–1 |
  | `tool-failure-count` | Number of failed tool calls | integer |
  | `retries` | Count of retry events in MCP gateway logs | integer |
  | `loops` | Consecutive identical tool calls (same name + args) | integer |
  | `trajectory-efficiency` | Unique tool names / total tool calls | 0–1 |
  | `execution-step-count` | Total LLM request count | integer |
  | `execution-duration` | Total execution duration (ms) | integer |
  | `working-set-rebuild-factor` | Cumulative input tokens / peak invocation input tokens | ≥1 |
  | `context-growth` | Total tokens / first-request tokens | ≥1 |
  | `artifact-production` | Count of outputs in agent_output.json | integer |

- **Quote**: "The implementation MUST recognize the following built-in
  grader IDs: tool-success-rate, tool-failure-count, retries, loops,
  trajectory-efficiency, execution-step-count, execution-duration,
  working-set-rebuild-factor, context-growth, artifact-production. These
  IDs are reserved for built-ins. A built-in grader MUST NOT accept a
  custom script." (spec §5)
- **Our assessment**: `working-set-rebuild-factor` and `context-growth` are
  the two most novel metrics in this list relative to the rest of the
  corpus: both are ratios built directly on the token-class data that
  `docs-ghaw-effective-tokens-specification.md` formalizes (input tokens
  per invocation), but they measure a *shape* problem (is the agent
  repeatedly re-reading the same context, is context ballooning across
  turns) rather than a *cost* problem (ET's domain). `loops` (consecutive
  identical tool calls) is a direct, automatic, built-in detector for
  exactly the "some agents were way too chatty with their LLM calls"
  failure mode that `blog-ghaw-agent-observability.md` Claim 4 describes as
  something a human analyst (Portfolio Analyst) had to notice manually —
  graders make that detection a zero-LLM-cost, always-on metric instead of
  requiring a dedicated audit agent. For Ch02/Ch06 (Observability): present
  `loops` and `working-set-rebuild-factor` specifically as automatic,
  free replacements for what was previously manual trace inspection.

### Claim 4: Individual built-in graders can be selectively disabled while leaving the rest of the default set active, using a per-grader `enabled: false` override inside the `graders:` map

- **Evidence**: Docs page "Selective configuration" section, shown with a
  minimal YAML example disabling only `loops`.
- **Confidence**: settled (first-party; directly shown as a config example)
- **Quote**: "Disable a specific built-in: `graders: loops: enabled: false`"
  (docs page, "Selective configuration" — reconstructed from the page's
  rendered YAML block, which the text-extraction pass rendered as separate
  lines: `graders` / `loops` / `enabled` / `false`)
- **Our assessment**: This is the mechanism for tuning out a metric that is
  noisy or not meaningful for a specific workflow (e.g., a workflow that
  legitimately repeats identical tool calls by design would want `loops`
  disabled to avoid a metric that always reads as a false-positive
  concern) without losing the rest of the default grading surface. For
  Ch02: document per-grader `enabled: false` as the escape hatch for
  built-ins that don't fit a specific workflow's expected trace shape,
  rather than disabling grading entirely.

### Claim 5: Custom inline graders are trusted JavaScript expressions, capped at 4096 characters, that receive a preprocessed `trace` object and must return a value — with both the docs page and the spec independently listing forbidden patterns, and the spec's list being strictly longer (nine forbidden patterns vs. the docs page's five)

- **Evidence**: Docs page "Custom inline graders" section gives a worked
  example (`trace.toolCalls.filter(t => t.name === 'bash').length`) and
  states the constraint informally. Spec §6.2–6.3 gives the formal MUST
  requirements and the complete forbidden-pattern list.
- **Confidence**: settled (first-party; both sources agree on the core
  mechanism, and the spec's longer list is corroborating detail rather
  than a conflict — the docs page's list is a subset, not a contradiction)
- **Quote**: "Add a trusted inline JavaScript expression that receives the
  preprocessed trace object... Custom scripts must return a value and stay
  within 4096 characters (no require, import, fetch, eval, or
  process.exit)." (docs page, "Custom inline graders")
- **Quote**: "script MUST be non-empty. script MUST NOT exceed 4096
  characters... Inline scripts MUST be rejected if they contain any
  forbidden pattern, including: require(, import(, import, fetch(, eval(,
  process.exit, child_process, execSync, spawnSync, Function(" (spec
  §6.2–6.3)
- **Our assessment**: The three patterns present in the spec but absent
  from the docs page's abbreviated list — `child_process`, `execSync`,
  `spawnSync`, and `Function(` — are exactly the Node.js primitives that
  would let a "trusted inline JavaScript expression" spawn an actual
  subprocess or dynamically construct new executable code, defeating the
  "trusted" framing entirely. A practitioner who read only the docs page
  and reasoned "no `eval`, no `fetch`, so this is safe from arbitrary code
  execution" would be missing three-fifths of the actual guardrail. For
  Ch03 (Safety and Verification): when citing this feature, cite the
  spec's nine-pattern list, not the docs page's five-pattern shorthand —
  the docs page is not a complete security reference for what "custom
  inline grader" actually forbids.

### Claim 6: The reserved `operational-value` grader configures a repository-relative Bash evaluator script whose exact bytes the compiler freezes and SHA-256-digests at compile time; the evaluator returns an absolute operational-attainment score in [0,1] for the run's assigned case, and an optional frozen baseline lets gh-aw derive a `deltaFromBaseline` without ever replacing the primary value

- **Evidence**: Docs page "Operational value grader" section with a
  concrete YAML example; spec §7 gives the formal MUST requirements for
  the same mechanism, including the evaluator's required CLI interface
  (`--definition` and `--grade-run`).
- **Confidence**: settled (first-party; the freeze/digest mechanism and
  the [0,1] attainment scale are consistently described in both sources)
- **Quote**: "Configure the reserved operational-value grader with a
  repository-relative Bash evaluator: `graders: operational-value: run:
  .github/graders/daily-file-diet-operational-value.sh` The compiler
  freezes the evaluator bytes and records their SHA-256 digest. The
  evaluator returns absolute operational attainment in [0,1] for the run's
  assigned case. A frozen baseline is optional metadata; when present,
  gh-aw derives deltaFromBaseline without changing the primary value."
  (docs page, "Operational value grader")
- **Quote**: "The evaluator MUST implement --definition and --grade-run.
  Its primary value MUST be absolute operational attainment in [0,1] or
  null. A baseline MAY be frozen separately; gh-aw MUST derive
  deltaFromBaseline and MUST NOT replace the primary value with that
  delta." (spec §7)
- **Our assessment**: The "absolute value, delta is metadata only" design
  is a deliberate anti-gaming choice: if delta-from-baseline *were* the
  primary value, a team could reset or redefine the baseline to make
  stagnant or regressing performance look like continuous improvement.
  Freezing the primary metric as an absolute [0,1] score, with delta
  computed but never substituted, keeps historical comparisons honest
  across baseline changes. This is the first source in the corpus to
  describe an operational-outcome metric with this specific
  anti-gaming property. For Ch04/Ch05 (Measuring Impact / Team Adoption):
  when documenting operational-value grading, name "absolute score with
  non-substitutable delta" as the design pattern that prevents baseline
  gaming, and contrast it with metrics that only report relative
  improvement.

### Claim 7: An operational-value evaluator MAY query repositories declared by its own frozen evidence contract and receives a `GH_TOKEN` scoped to the agent job's explicitly declared permissions, but never receives workflow secrets, and enabling the grader does not itself add any evidence-access permissions to the agent job

- **Evidence**: Docs page "Operational value grader" section, final
  paragraph; spec §10 "Security and Isolation" states the same
  requirement normatively, with an added MUST NOT the docs page phrases
  only descriptively.
- **Confidence**: settled (first-party; both sources describe the same
  token-scoping and no-secrets rule)
- **Quote**: "They receive the workflow token through GH_TOKEN with the
  agent job's explicitly declared permissions, but do not receive
  workflow secrets. Enabling the grader does not add evidence permissions
  to the agent job." (docs page, "Operational value grader")
- **Quote**: "Operational-value graders MAY access declared repository
  evidence using GH_TOKEN; implementations MUST NOT add agent-job
  permission scopes on behalf of the evaluator, and evaluators MUST NOT
  receive workflow secrets." (spec §10)
- **Our assessment**: This is the same "provenance-scoped, narrowly-cast
  trust" pattern that `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 7
  documents for the CLI Consistency Checker's CLI-output trust boundary —
  but applied to a permissions question rather than a content-trust
  question. The evaluator does not get its own elevated grant; it inherits
  exactly what the surrounding agent job already declared, and explicitly
  never sees secrets even if the agent job's permissions are broad. This
  closes an obvious escalation path: a team cannot accidentally widen
  what a grading script can read just by turning grading on. For Ch03
  (Safety and Verification): document "grading configuration MUST NOT
  itself be a privilege-escalation vector" as a named requirement for any
  observability/evaluation feature added to an agentic harness — this is a
  second, independently-sourced instance of the pattern.

### Claim 8: A historical run can be re-graded after the fact via `gh aw graders operational-value <runId> --evidence-at <ISO-8601-timestamp> --json`, which downloads the original grader artifact, reuses its case/run-subject/frozen evaluator, verifies the archived evaluator's bytes against both the originally recorded digest AND the evaluator present at the recorded commit in the current checkout, and always emits a brand-new observation — it never mutates the original artifact

- **Evidence**: Docs page "Regrade a historical run" section with a
  concrete CLI example; spec §7 and §10 both restate the dual-verification
  and non-mutation requirements normatively; T-GRD-014 in the spec's
  compliance suite specifically tests "Historical regrading rejects
  evaluator or run identity mismatches."
- **Confidence**: settled (first-party; the CLI syntax, dual-digest
  verification, and immutability guarantee are consistent across the docs
  page, the specification's normative text, and the compliance test list)
- **Quote**: "The command downloads the original grader artifact and
  reuses its case, run subject, and frozen evaluator. The archived
  evaluator must match the digest recorded by both the original manifest
  and result and the evaluator at the recorded commit in the current
  repository checkout. Regrading emits a new observation identified by
  (runId, evaluatorDigest, evidenceAt) and never modifies the original
  artifact." (docs page, "Regrade a historical run")
- **Quote**: "It MUST verify that the archived evaluator matches the
  digest recorded by both the original manifest and result and the
  evaluator at the recorded commit in a trusted local checkout before
  execution. It MUST emit a new observation and MUST NOT mutate the
  original run artifact." (spec §7)
- **Our assessment**: The dual-digest check (archived-bytes-vs-recorded-digest,
  AND recorded-commit-bytes-vs-same-digest) is meaningfully stronger than a
  single hash comparison: it protects against both a corrupted/tampered
  artifact download *and* a repository history that has since rewritten
  the evaluator at that commit (e.g., a force-push or history rewrite).
  Either mismatch blocks the regrade rather than silently regrading
  against a different evaluator than the one that produced the original
  score. Combined with the immutability guarantee (new observation, never
  an overwrite), this gives operational-value scores the same
  tamper-evidence properties as an append-only audit log. For Ch06
  (Operations/Observability): document the regrade command as the
  mechanism for retroactively applying a corrected or improved evaluator
  to historical runs without losing the original scored observations —
  useful when a team refines their operational-value definition partway
  through a rollout and wants comparable before/after data using the
  *same* evaluator logic.

### Claim 9: Grading executes as a single `if: always()` post-agent step inside the existing agent job — running after log parsing and before the unified artifact upload — and performs one shared preprocessing pass over trace files that every enabled grader (built-in, custom, and operational-value) reuses, rather than each grader re-parsing the trace independently

- **Evidence**: Docs page "Execution" section; spec §3 "Architecture" gives
  the same five-step ordering (parse/validate frontmatter → build manifest
  and execution spec → preprocess trace artifacts once → execute enabled
  graders → write normalized outputs) with an added MUST that individual
  grader failures should not abort the whole step.
- **Confidence**: settled (first-party; the `if: always()` semantics, the
  single-preprocessing-pass design, and the step's position in the job are
  stated in both sources)
- **Quote**: "The graders step runs as an if: always() post-agent step in
  the existing agent job, after log parsing and before the unified
  artifact upload. It uses a single preprocessing pass over trace files
  shared by all graders." (docs page, "Execution")
- **Quote**: "The grading step MUST run with if: always() semantics and
  SHOULD continue even when individual graders fail, recording per-grader
  errors in results." (spec §3)
- **Our assessment**: `if: always()` is the specific guarantee that makes
  grading useful for failure analysis, not just success analysis — a run
  that crashes, times out, or is cancelled mid-agent-execution still gets
  graded (tool-success-rate, retries, and loops on a failed trajectory are
  arguably more diagnostically valuable than on a clean one). The shared
  single-pass preprocessing is a performance/cost detail worth noting for
  teams enabling many custom graders simultaneously: the marginal cost of
  an additional custom grader is just its own script execution, not a
  repeated trace-file parse. For Ch02: cite the `if: always()` execution
  guarantee explicitly when recommending graders for failure-mode
  diagnosis, not only for successful-run quality tracking.

### Claim 10: Conformance is defined at three levels with a distinct "partially conforming" middle category — Level 1 (Required: built-in graders plus manifest/results output) MUST be satisfied by any conforming implementation, Level 2 (Standard) adds custom inline graders with validation and isolation, and Level 3 (Complete) adds experiment metric references with validation — while an implementation that supports built-ins but skips custom inline grader execution entirely is formally "partially conforming," not simply "Level 1"

- **Evidence**: Spec §2.1 "Conformance Classes" and §2.3 "Compliance
  Levels."
- **Confidence**: settled (first-party normative specification; the
  conformance classes and levels are explicitly defined with section
  references)
- **Quote**: "Conforming implementation: Satisfies all MUST/SHALL
  requirements in this document. Partially conforming implementation:
  Supports built-in graders but omits custom inline grader execution."
  (spec §2.1)
- **Quote**: "Level 1 (Required): Built-in graders, manifest/results
  output. Level 2 (Standard): Custom inline graders with validation and
  isolation. Level 3 (Complete): Experiment metric references to graders
  with validation." (spec §2.3)
- **Our assessment**: This mirrors the three-level conformance structure
  already documented for both `docs-ghaw-effective-tokens-specification.md`
  Claim 7 and `docs-ghaw-practices-experiments-specification.md` Claim 2 —
  the gh-aw team consistently uses a Basic/Standard/Complete (or
  Required/Standard/Complete) three-tier conformance model across its
  formal specs. The "partially conforming" carve-out specific to this spec
  (built-ins-only implementations) is new: neither the ET spec nor the
  experiments spec name an explicit non-Level-1 partial-conformance
  category. For Ch04: when presenting graders' conformance levels
  alongside ET's and experiments', note the shared three-tier convention
  as a recognizable pattern across gh-aw's formal specs — practitioners
  evaluating third-party tooling can ask "which level/class does this
  implement?" using the same mental model across all three systems.

### Claim 11: Experiment metric fields may reference grader outputs directly via `grader:<id>` or `graders.<id>.value`; only valid numeric grader results count toward an experiment's `min_samples`, with missing artifacts, missing/failed graders, and invalid values excluded rather than treated as zero; a grader's `direction` field is normalized by the decision layer before applying the experiment system's `minimum_effect` policy and guardrails — and the spec explicitly warns that a grader measures only the behavior it encodes, not necessarily semantic task correctness

- **Evidence**: Spec §9 "Experiment Metric References" — not present on the
  docs page at all, which does not mention the A/B experiment system.
- **Confidence**: settled (first-party normative requirement; this is the
  section that formally connects two previously-separate corpus systems —
  graders and A/B experiments)
- **Quote**: "Experiment metric fields MAY reference grader outputs.
  Supported forms include: grader:<id>, graders.<id>.value. When a grader
  reference is used, <id> MUST resolve to a declared enabled grader.
  Unknown or empty grader references MUST fail validation." (spec §9)
- **Quote**: "gh aw experiments analyze reads the persisted assignment
  ledger and the run's grader_results.json; this path does not require
  historical trace replay or an additional evaluator model invocation.
  Only valid numeric grader results count toward min_samples. Missing
  artifacts, missing or failed graders, and invalid values are excluded
  rather than treated as zero." (spec §9)
- **Quote**: "A grader measures only the behavior encoded by that grader;
  not every grader represents semantic task correctness." (spec §9)
- **Our assessment**: This is the single most significant finding in this
  note relative to the rest of the corpus. `docs-ghaw-practices-experiments-specification.md`
  Claim 11 documents that reporting tools MUST NOT issue a PROMOTE
  recommendation until ALL variants reach `min_samples` — but that note's
  extraction predates graders and could not say *how* a run's metric value
  gets computed in the first place beyond a generic `metric:` field name.
  §9 here answers that: `grader:<id>` is now a first-class, spec-sanctioned
  metric source for an experiment, meaning a workflow can A/B test two
  prompt variants and use `graders.trajectory-efficiency.value` or a
  custom `operational-value` evaluator's score as the primary experiment
  metric — with zero additional LLM-judge calls to score each run. The
  "excluded rather than treated as zero" rule for missing/failed grader
  results is a specific, important statistical-integrity detail: a variant
  that crashes before a grader can compute (e.g., the agent times out) does
  not get penalized as a zero-value observation dragging down its average —
  it is dropped from the sample entirely, which is the statistically
  correct treatment for missing data but means teams must separately watch
  completion/crash rates (an operational-layer metric) alongside the
  experiment's chosen grader metric, since the experiment analysis alone
  will not surface "this variant crashes more often." The closing warning —
  a grader is not automatically semantic correctness — is the spec
  authors' own caveat against over-trusting a mechanical metric as a proxy
  for whether the agent actually did the right thing. For Ch04 (Agent
  Patterns / Experimentation): add "grader-backed experiment metrics" as
  the recommended default metric source for gh-aw A/B experiments over
  hand-rolled custom measurement code, but pair it with the "excluded not
  zeroed" caveat and the "not semantic correctness" warning as two
  necessary caveats when presenting this pattern.

## Concrete Artifacts

### Quick Start (docs page, verbatim YAML)

```yaml
graders: {}
```
*An empty map enables all built-in graders with default settings. Omitting
the `graders` field entirely disables grading (no step is emitted).*

### Built-in Grader Table (docs page, verbatim)

```
ID                            Description                                          Value
tool-success-rate             Fraction of tool calls that succeeded               0–1
tool-failure-count            Number of failed tool calls                         integer
retries                       Count of retry events in MCP gateway logs           integer
loops                         Consecutive identical tool calls (same name + args) integer
trajectory-efficiency         Unique tool names / total tool calls                0–1
execution-step-count          Total LLM request count                            integer
execution-duration             Total execution duration (ms)                      integer
working-set-rebuild-factor    Cumulative input tokens / peak invocation input     ≥1
                               tokens
context-growth                Total tokens / first-request tokens                 ≥1
artifact-production            Count of outputs in agent_output.json               integer
```

### Custom Inline Grader Example (docs page)

```yaml
graders:
  bash-calls:
    script: "return trace.toolCalls.filter(t => t.name === 'bash').length"
```
*Custom scripts must return a value and stay within 4096 characters (no
`require`, `import`, `fetch`, `eval`, or `process.exit` — spec §6.3 adds
`child_process`, `execSync`, `spawnSync`, and `Function(` to this list.)*

### Operational Value Grader Example (docs page)

```yaml
graders:
  operational-value:
    run: .github/graders/daily-file-diet-operational-value.sh
```

### Historical Regrade Command (docs page)

```bash
gh aw graders operational-value 123456789 \
  --evidence-at 2026-08-30T12:00:00.000Z \
  --json
# Use --repo [HOST/]OWNER/REPO to select the host for the checked-out repository.
```

### Output Files (docs page, verbatim table)

```
File                              Description
grader_manifest.json              Which graders were configured and their enabled state
grader_results.json               Normalized values, status, implementation identity,
                                   and value observations
operational_value_evaluator.sh    Exact frozen operational-value evaluator used for
                                   initial grading and historical replay

All files are included in the unified `agent` artifact.
```

### Spec: Compliance Levels and Checklist (spec §2.3, §11.2)

```
Level 1 (Required):  Built-in graders, manifest/results output.
Level 2 (Standard):  Custom inline graders with validation and isolation.
Level 3 (Complete):  Experiment metric references to graders with validation.

Requirement                                    Test ID              Level  Status
Frontmatter key is `graders`                   T-GRD-001            1      Required
Empty map enables built-ins                    T-GRD-002            1      Required
Custom graders require script                  T-GRD-003            2      Required
Script safety constraints enforced             T-GRD-004, T-GRD-005 2      Required
Required artifact files emitted                T-GRD-007, T-GRD-008 1      Required
Experiment grader references validate          T-GRD-010, T-GRD-011 3      Required
Operational-value evaluators/observations valid T-GRD-012, T-GRD-013 2      Required
Historical regrading preserves identity        T-GRD-014            2      Required
```

### Spec: Norms (§12, verbatim)

```
N-GRD-001: Implementations MUST treat graders as experimental.
N-GRD-002: Implementations MUST preserve built-in grader ID stability across
           patch releases.
N-GRD-003: Implementations SHOULD preserve deterministic output for
           identical trace inputs.
N-GRD-004: Implementations MUST fail fast on invalid custom grader scripts.
N-GRD-005: Implementations MUST keep grader artifact paths stable unless a
           major version change is issued.
N-GRD-006: Implementations MUST keep operational value separate from
           execution quality metrics.
```
*N-GRD-006 is the formal norm underlying this note's Claim 6 —
`operational-value` (outcome/impact) and the nine other built-ins
(execution quality/shape) are deliberately kept as distinct, non-blendable
metric families.*

### Spec: Output Directory and Required Files (§8.1–8.2)

```
Output directory: /tmp/gh-aw/agent/graders

Required files (implementation MUST produce):
  grader_manifest.json
  grader_results.json
  operational_value_evaluator.sh   (only when operational-value grader enabled)
```

### Confirmed Real-World Usage: CLI Consistency Checker imports `shared/graders.md`

```yaml
imports:
  - shared/otlp.md
  - shared/reporting.md
  - shared/graders.md
```
*Source: `.github/workflows/cli-consistency-checker.md` frontmatter, as
independently fetched and documented in
`blog-ghaw-agent-of-the-day-2026-08-26.md` Concrete Artifacts. This is a
production gh-aw workflow (in the `github/gh-aw` repository itself)
importing a shared graders configuration file, confirming the feature is
in active internal use rather than purely a documented-but-unused
experimental surface. Note: that source note's own extraction (dated
2026-08-29, filed under issue #2996) did not investigate what
`shared/graders.md` contains, since graders were outside that note's
scope — this is a candidate follow-up fetch for a future miner pass, not
resolved by this note.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-deterministic-agentic-patterns.md` Claim 1 (the three-stage
    deterministic → agent → safe-outputs pipeline as the named hybrid
    architecture): graders' "compute metrics without LLM calls" design
    (Claim 1 here) is the same deterministic-computation philosophy that
    note documents for pre- and post-agent jobs, now applied to a fourth
    position — grading the agent's own completed trace (see Claim 1's
    assessment for why this doesn't fit that note's three named stages).
  - `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 7 (provenance-scoped
    trust: the CLI Consistency Checker trusts CLI output specifically
    because it's deterministically derived in the same job): Claim 7 here
    documents the same narrow-trust design principle applied to a
    permissions question rather than a content-trust question — an
    operational-value evaluator inherits the agent job's exact declared
    permissions and never gets its own elevated grant or secrets access.
  - `docs-ghaw-artifacts-reference.md` Claim 3 (the `agent` artifact is
    multi-file, containing execution logs, `agent_output.json`,
    `github_rate_limits.jsonl`, `agent_usage.json`, and optional telemetry
    files): Claim 9 here and the Concrete Artifacts "Output Files" table
    add `grader_manifest.json`, `grader_results.json`, and
    `operational_value_evaluator.sh` to that same unified `agent` artifact
    — extending the known file inventory rather than introducing a
    separate artifact.
  - `docs-ghaw-effective-tokens-specification.md` Claim 7 (three
    conformance levels — Basic/Standard/Complete) and
    `docs-ghaw-practices-experiments-specification.md` Claim 2 (three
    conformance levels — Basic/Standard/Complete): Claim 10 here documents
    the same three-tier conformance convention (worded Required/Standard/
    Complete rather than Basic/Standard/Complete, but structurally
    identical) as a third instance of the same design pattern across
    gh-aw's formal specifications.
  - `blog-ghaw-agent-of-the-day-2026-08-26.md` Concrete Artifacts
    (CLI Consistency Checker frontmatter): that workflow's `imports:` list
    includes `shared/graders.md`, directly confirming production, in-repo
    usage of this experimental feature (see Concrete Artifacts above).

- **Extends**:
  - `docs-ghaw-practices-experiments-specification.md` and
    `docs-ghaw-practices-experiments.md`: Claim 11 here (spec §9,
    "Experiment Metric References") is the single most direct extension in
    this note — it formally defines `grader:<id>` / `graders.<id>.value` as
    metric sources for the A/B experiment system that
    `docs-ghaw-practices-experiments-specification.md` documents, and adds
    the "excluded rather than zeroed" missing-data rule that neither
    experiments note could state (graders did not yet exist, or were out
    of scope, when those notes were written on 2026-05-16/17). This closes
    an implicit gap: `docs-ghaw-practices-experiments.md` Claim 2 lists a
    generic `metric` field without specifying *how* a metric value is
    computed for a given run; graders (via §9) is the mechanism.
  - `docs-ghaw-effective-tokens-specification.md`: both this spec and the
    ET spec are deterministic, post-run, no-additional-LLM-call metric
    systems from the same team, but they measure orthogonal dimensions —
    ET measures computational cost intensity (token-class-weighted,
    model-multiplied); graders measure execution quality/shape
    (tool-success-rate, loops, context-growth) and operational/business
    outcomes (the `operational-value` grader). A complete measurement
    stack for a gh-aw workflow now spans both: ET answers "what did this
    run cost computationally," graders answer "did this run behave well
    and did it matter."
  - `docs-ghaw-measuring-impact.md`: that source's four-layer taxonomy
    (operational / cost-efficiency / outcome / long-term impact) now has
    concrete, automatic, zero-LLM-cost instrumentation for two of its four
    layers via this feature — the nine trace-based built-ins map to the
    *operational* layer (Claim 6 of that note: "tell you whether the
    workflow runs reliably"), and the `operational-value` grader maps
    directly to the *outcome* layer (Claim 8 of that note: "tell you
    whether the workflow produced something that mattered"). That note
    could only describe these layers abstractly; graders is the concrete
    mechanism that computes them without requiring a separate audit
    agent or manual review.
  - `blog-ghaw-agent-observability.md` Claim 4 (the Portfolio Analyst
    pattern manually noticing "some agents were way too chatty with their
    LLM calls"): the `loops` and `execution-step-count` built-ins (Claim 3
    here) automate exactly this class of detection as a standing,
    always-on metric rather than something a dedicated analysis agent must
    notice and report.

- **Contradicts**: None identified. Reviewed `CONTRADICTIONS.md` (no
  existing entries C-001 through C-008 touch graders, experiments, or
  execution metrics) and all gh-aw source notes cross-referenced above in
  full. No claim in this note materially opposes any existing corpus
  claim; the "excluded rather than zeroed" missing-data rule (Claim 11)
  and the fail-fast "at least one grader must be enabled" rule (Claim 2)
  are additive precision on top of the existing experiments and
  configuration documentation, not conflicts with it. No contradiction
  issue filed.

- **Novel** (what this note adds to the corpus that no prior source
  covers):
  - **The `graders` feature end to end** (Claims 1–10): entirely new to
    the corpus — no prior source note documents deterministic post-agent
    grading, the ten built-in metrics, custom inline JS graders, or the
    operational-value grader's frozen-evaluator/digest/regrade mechanism.
  - **Frozen-evaluator SHA-256 digest with dual-verification historical
    regrading** (Claim 8): the specific tamper-evidence design (verify
    against both the recorded digest and the evaluator at the recorded
    commit in a trusted checkout) is not documented anywhere else in the
    corpus for any gh-aw feature.
  - **"Absolute score, non-substitutable delta" anti-gaming pattern**
    (Claim 6): no prior corpus source documents a metric design that
    computes a delta-from-baseline but explicitly forbids it from
    replacing the primary reported value.
  - **`grader:<id>` / `graders.<id>.value` as A/B experiment metric
    sources, with "excluded not zeroed" missing-data handling** (Claim
    11): the direct, formal link between graders and the A/B experiment
    system — closing a gap left open by both experiments source notes.
  - **Nine forbidden custom-inline-script patterns (spec) vs. five (docs
    page)** (Claim 5): the docs-page/spec discrepancy in completeness for
    a security-relevant list is itself a new finding — a caution about
    which of the two pages to cite for security guidance.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "post-hoc deterministic
  grading" as a named pipeline position, distinct from precomputation and
  post-processing (Claim 1) — a `graders:` configuration block that scores
  the agent's already-completed trace at zero additional LLM cost. Include
  the two-state enable/disable model and its fail-fast "at least one
  grader enabled" rule (Claim 2) in any configuration reference. Present
  `loops`, `execution-step-count`, and `working-set-rebuild-factor` (Claim
  3) as automatic replacements for what previously required manual trace
  review (per `blog-ghaw-agent-observability.md` Claim 4).

- **Chapter 03 (Safety and Verification)**: When documenting custom inline
  graders, cite the specification's complete nine-pattern forbidden list,
  not the docs page's five-pattern shorthand (Claim 5) — flag this
  discrepancy explicitly since a reader of only the docs page would
  under-estimate the sandbox's actual restrictions. Add "grading
  configuration MUST NOT itself be a privilege-escalation vector" (Claim
  7) as a named requirement for observability features generally, citing
  this as a second corroborating instance of the pattern first seen in
  `blog-ghaw-agent-of-the-day-2026-08-26.md` Claim 7.

- **Chapter 04 (Agent Patterns / Experimentation)**: Add "grader-backed
  experiment metrics" (Claim 11) as the recommended default for gh-aw A/B
  experiment `metric:` fields — cite `grader:<id>` / `graders.<id>.value`
  as first-class metric sources requiring no LLM-judge calls, paired with
  the two caveats: missing/failed grader results are excluded from
  `min_samples`, not zeroed, and a grader measuring behavior is not the
  same as a grader measuring task correctness. Reference the shared
  three-tier conformance convention (Claim 10) alongside ET's and
  experiments' own conformance levels as a recognizable pattern across
  gh-aw's formal specs.

- **Chapter 05 / Chapter 06 (Team Adoption / Operations)**: Pair the
  built-in grader set with `docs-ghaw-measuring-impact.md`'s four-layer
  taxonomy — the nine trace-based built-ins instrument the operational
  layer automatically; the `operational-value` grader instruments the
  outcome layer. Document the historical regrade command (Claim 8) as the
  mechanism for applying a corrected evaluator to past runs without losing
  the original tamper-evident observations, useful when a team's
  operational-value definition matures mid-rollout.

## Extraction Notes

1. **Two pages fetched and combined, within MINER.md §1's "up to 5 linked
   pages" budget**: the docs page (`experimental/trace-graders`) and the
   normative Graders Specification
   (`specs/graders-specification`), which the docs page links to
   directly ("For normative requirements, see the Graders Specification").
   Both were fetched via direct `curl` and parsed with a Python
   regex-based tag-stripping pass (same approach as
   `blog-ghaw-agent-of-the-day-2026-08-26.md` Extraction Note 2 and
   `blog-ghaw-weekly-2026-08-24.md` Extraction Note 1) rather than
   WebFetch's AI-summarized output, so that all quotes above are copied
   character-for-character from the raw extracted text rather than
   reconstructed from a paraphrased summary. This departs from several
   earlier gh-aw notes in this corpus (e.g.
   `docs-ghaw-effective-tokens-specification.md`,
   `docs-ghaw-measuring-impact.md`) which relied on WebFetch's AI-processed
   output and marked many quotes "(no direct quote)" as a result — the
   direct-`curl` approach here yielded verbatim quotes for every claim.

2. **Third linked sub-page not followed**: the docs page also links to the
   "operational value designer" skill (`/operational-value-designer`,
   mentioned in the docs page's "Operational value grader" section:
   "Use the operational value designer skill (/operational-value-designer)
   to infer operational value from an agentic workflow and design and
   verify an operational-value evaluator"). This is a Claude Code / Copilot
   skill reference, not a fetchable documentation page, and was not
   pursued further — noted here as a candidate follow-up if a future
   source surfaces the skill's actual prompt/instructions.

3. **`shared/graders.md` not fetched**: the CLI Consistency Checker
   workflow (documented in `blog-ghaw-agent-of-the-day-2026-08-26.md`)
   imports `shared/graders.md`, confirming real production usage (see
   Concrete Artifacts), but that shared file's actual contents were not
   fetched as part of this extraction — it is outside the `/experimental/
   trace-graders` and `/specs/graders-specification` scope this note was
   filed to cover. Flagged as a candidate follow-up source rather than
   speculated about here.

4. **No contradictions filed**: reviewed `CONTRADICTIONS.md` in full (all
   eight existing entries) and every gh-aw source note cited in
   Cross-References above, in full, before writing this note. No claim
   here opposes any existing corpus claim at the MINER.md §4a filing
   threshold — see Cross-References → Contradicts.

5. **`confidence_overall` set to `emerging`, not `settled`**: despite the
   specification's extensive MUST/MUST NOT normative language (which on
   its own would suggest `settled`, consistent with how
   `docs-ghaw-practices-experiments-specification.md` was rated for its
   individual claims), the feature is explicitly and repeatedly marked
   experimental at the top of both source pages ("Graders are an
   experimental feature" on the docs page; "Feature Status: Experimental"
   and N-GRD-001 "Implementations MUST treat graders as experimental" in
   the spec itself), and the spec is Version 0.2.0 Draft with an explicit
   note that implementations "SHOULD expect iteration before final
   recommendation status." This matches the precedent set by
   `docs-ghaw-effective-tokens-specification.md`, which used the same
   `emerging` overall rating for a similarly formal but still-Draft
   specification. Individual claims quoting MUST/MUST NOT language are
   still marked `settled` at the claim level, since those requirements are
   normative for the current draft even though the feature as a whole may
   change before graduating out of experimental status.
