---
source_url: https://github.github.com/gh-aw/blog/2026-06-22-weekly-update/
source_type: blog-post
title: "Weekly Update – June 22, 2026 (GitHub Agentic Workflows)"
author: GitHub Agentic Workflows team (gh-aw)
date_published: 2026-06-22
date_extracted: 2026-06-22
last_checked: 2026-06-22
status: current
confidence_overall: emerging
issue: "#1274"
---

# Weekly Update – June 22, 2026 (GitHub Agentic Workflows)

> No versioned release this week — the June 22 update delivers four high-signal
> patterns: (1) a +320% compiler performance recovery by eliminating redundant
> `yaml.Unmarshal` calls in `validateTemplateInjection`; (2) `deferinloop`, a
> third linter-miner–family analyzer flagging `defer` in loops for resource-leak
> prevention; (3) `gh-aw-detection` feature-flag expansion to 50% of workflows
> (107 of 214); and (4) `delight`, a read-only UX audit agent sampling docs/CLI
> text/validation code for quality against five design principles.

## Source Context

- **Type**: blog-post (weekly changelog/update from the official GitHub Agentic
  Workflows blog; covers the week ending June 22, 2026; no versioned release —
  focuses on merged PRs across compiler performance, linting, feature rollout,
  reliability fixes, token cost optimization, and an Agent of the Week spotlight
  on `delight`)
- **Author credibility**: The gh-aw blog is the official publication of GitHub's
  Agentic Workflows platform team (Don Syme, Peli de Halleux, Mara Kiefer — see
  `blog-ghaw-agent-observability.md` for author background). PRs are cited with
  specific numbers, independently verifiable. High credibility for first-party
  platform claims.
- **Scope**: Covers compiler regression resolution (PR #40662), a new `deferinloop`
  linter (PR #40679), `gh-aw-detection` rollout expansion (PR #40698), JSON-RPC
  error serialization fix (PR #40715), Skillet sparse-checkout typing fix (PR
  #40684), daily observability report artifact fetching fix (PR #40705), FNV-1a
  heredoc delimiter hashing (PR #40696), ambient system-prompt trimming (PR #40695),
  and the `delight` Agent of the Week. Does NOT cover: the internal design of the
  `linter-miner` workflow (how it produces Go analysis passes from bug descriptions);
  the specific alphabetical-targeting algorithm for `gh-aw-detection` rollout; the
  full list of `delight`'s UX design principle definitions; or the complete set of
  JSON-RPC error codes now enforced.

## Extracted Claims

### Claim 1: A compiler regression in `validateTemplateInjection` caused redundant `yaml.Unmarshal` calls on every compilation pass, degrading `BenchmarkCompileComplexWorkflow` from 3 ms/op to 12.7 ms/op; PR #40662 eliminates the redundant calls and restores baseline performance

- **Evidence**: PR #40662. The post identifies the specific function
  (`validateTemplateInjection`), the specific cause (redundant YAML unmarshaling
  when validation was disabled), and the specific benchmark affected, with before
  and after measurements.
- **Confidence**: settled (specific PR, named function, named cause, named
  benchmark with before/after measurements)
- **Quote**: "resolved a critical compiler regression that had slowed compilation
  from 3 ms/op to 12.7 ms/op. The issue involved redundant YAML unmarshaling in
  `validateTemplateInjection` when validation was disabled."
- **Our assessment**: A 12.7/3.0 ≈ 4.2× slowdown (roughly +320% degradation) in
  the complex-workflow benchmark is a severe regression for a compiler that runs on
  every `gh aw compile` invocation. The root cause — unconditional YAML
  unmarshaling inside a validation function that was conditionally disabled — is a
  classic performance anti-pattern: coupling expensive parsing to code paths that
  don't actually use the result. The fix (guard the unmarshal behind the same
  condition that gates the validation) is the canonical fix for this class of
  regression. For Ch02 (Harness Engineering): document the
  `validateTemplateInjection` pattern as a concrete example of a harness toolchain
  performance regression caused by unconditional deserialization; the guard pattern
  (parse only if the result will be used) is directly applicable to any YAML/JSON
  pipeline that conditionally runs validation logic. For Ch05 (Cost/Performance
  Optimization): compiler performance directly affects developer feedback loops;
  a 4.2× slowdown on complex workflows would be perceptible as latency when
  iterating on harness configuration.

### Claim 2: The `deferinloop` linter (PR #40679) flags `defer` statements inside loops, preventing resource leaks and unpredictable cleanup ordering

- **Evidence**: PR #40679. The post names the linter, its detection target (`defer`
  inside loops), and the consequence of the pattern it catches (resource leaks,
  unpredictable cleanup ordering).
- **Confidence**: settled (specific PR, named detection rule, named failure modes)
- **Quote**: "introduced the `deferinloop` linter, which identifies `defer`
  statements inside loops—a pattern that causes resource leaks and unpredictable
  cleanup ordering."
- **Our assessment**: In Go, `defer` executes at function return, not at the end
  of the enclosing block or loop iteration. A `defer file.Close()` inside a
  `for` loop does not close the file after each iteration — it accumulates deferred
  calls that all fire when the surrounding function returns. For file handles,
  database connections, or mutex unlocks, this means holding resources until
  function exit rather than releasing them per-iteration — a resource leak in
  long-running loops. The `deferinloop` linter is the third member of the
  `linter-miner`-family analyzers documented in the gh-aw corpus (after
  `timeafterleak`, PR #39133, and `errorfwrapv`, PR #39263 from the June 15 week,
  `blog-ghaw-weekly-2026-06-15.md` Claims 2–3). The June 22 update does not
  explicitly attribute `deferinloop` to `linter-miner` the way June 15 did for
  its two linters; the attribution to the `linter-miner` family is the
  Prospector's inference. For Ch02 (Harness Engineering): the defer-in-loop
  pattern is a real and common Go reliability issue for harness CLI code that
  processes files or connections in loops. `deferinloop` can be adopted
  independently of the gh-aw platform as a standard Go lint rule. For Ch03
  (Safety and Verification): CI-enforced linting for this pattern prevents a
  class of silent resource-exhaustion failures that would appear only under load
  or long runtime.

### Claim 3: `gh-aw-detection` feature flag expanded from 20% to 50% of agentic workflows (PR #40698), adding approximately 64 newly targeted workflows for a total of ~107 of 214

- **Evidence**: PR #40698. The post states the before/after percentages and the
  approximate workflow counts.
- **Confidence**: settled (specific PR, named percentages, approximate counts that
  are independently checkable: 50% of 214 ≈ 107; 107 − 43 ≈ 64 newly added)
- **Quote**: "scaled `gh-aw-detection` from 20% to 50% of agentic workflows,
  adding approximately 64 newly included workflows to the rollout."
- **Our assessment**: The `gh-aw-detection` rollout is a structured incremental
  expansion following the pattern: ship at low percentage, validate, expand. The
  move from 20% (43 workflows) to 50% (107 of 214) more than doubles the active
  surface without a flag-day switch-over. The Prospector notes that alphabetical
  targeting determines which workflows are added at each stage, making the rollout
  deterministic and predictable. For Ch04 (Multi-Agent Orchestration): this is a
  concrete example of metrics-driven incremental feature flag adoption in an
  agent platform — the percentage and workflow counts are tracked explicitly. Teams
  deploying new agentic detection or classification features can use this pattern:
  define a target population, roll out by percentage with a deterministic targeting
  scheme, and measure before expanding.

### Claim 4: The `delight` Agent of the Week is a read-only UX audit agent that scans documentation, CLI help text, and validation code for UX quality against five design principles, filing targeted issues when problems are found

- **Evidence**: "Agent of the Week" spotlight. The post describes the workflow's
  scanning scope and notes that recent runs found no issues worthy of filing.
  One WebFetch pass returned five named design principles (clarity, professional
  communication, efficiency, trust, and documentation quality); see Extraction
  Notes for verbatim confidence.
- **Confidence**: anecdotal (single agent spotlight; no issue-filing data from
  current runs; operational parameters — sampling strategy, run frequency, per-run
  issue cap — are from the Prospector's triage analysis rather than the source text
  as returned by WebFetch)
- **Quote**: "scans documentation, CLI help text, and validation code for UX
  improvements, filing targeted issues when problems emerge. Recent runs found no
  issues worthy of filing—indicating well-maintained user-facing materials."
- **Our assessment**: `delight` is a novel agent type in the gh-aw corpus: an
  always-on, read-only quality auditor scoped to user-facing materials rather than
  code correctness or workflow reliability. Prior Agent of the Week spotlights
  covered task-execution agents (`auto-triage-issues`, `api-consumption-report`,
  `aw-failure-investigator`). `delight` is the first documented in this corpus
  that targets human-facing quality (documentation clarity, CLI message
  professionalism) rather than process automation. The "Recent runs found no
  issues worthy of filing" outcome is positive signal: it means the agent ran,
  evaluated the codebase, and concluded the UX bar was already met. This is a
  valid non-event outcome for a quality-gate agent. The Prospector's triage
  describes operational parameters: runs 3 times per 30 days; randomly samples
  1–2 docs, 1–2 CLI commands, 1–2 messages, and 1 validation file per run; capped
  at 2 issues per run. These operational parameters could not be independently
  verified from the WebFetch returns and are treated as triage analysis, not
  source quotes. For Ch04 (Multi-Agent Orchestration): `delight` establishes a
  new agent-type pattern — read-only UX auditors with scoped sampling — relevant
  for teams that want to maintain documentation and CLI message quality without
  scheduled manual reviews. The always-read-only constraint and per-run issue cap
  (2) are safety bounds that prevent audit agents from overwhelming maintainers
  with noise. For Ch02 (Harness Engineering): the sampling strategy
  (1–2 artifacts of each type per run) is a concrete example of bounded-scope
  agentic auditing that avoids exhaustive runs while providing continuous coverage
  over time.

### Claim 5: Unnecessary context was trimmed from the initial system prompt of high-traffic workflows, reducing token consumption on every invocation (PR #40695)

- **Evidence**: PR #40695. The post names the optimization approach (trimming
  unnecessary context from system prompts) and the scope (high-traffic workflows).
- **Confidence**: settled (specific PR, named optimization target, named scope)
- **Quote**: "trimmed unnecessary context from system prompts to reduce token
  consumption in high-traffic workflows."
- **Our assessment**: Ambient system-prompt reduction is a recurring optimization
  pattern in the gh-aw corpus: the June 15 week reduced ambient-context payload
  across daily and PR workflows (PR #39157, `blog-ghaw-weekly-2026-06-15.md`
  Claim 12); the June 22 week (PR #40695) continues with an initial system-prompt
  reduction focused on high-traffic workflows. The compounding effect is significant
  for frequently-invoked workflows: every token removed from the initial system
  prompt reduces cost on every single invocation. For Ch05 (Cost Optimization):
  initial system-prompt audits should be a periodic practice for high-traffic
  workflows — the token savings compound with invocation frequency. The June 22
  optimization (PR #40695) pairs with the June 15 optimization (PR #39157) as a
  two-week sustained reduction campaign; teams managing token costs should treat
  prompt compression as ongoing rather than one-time.

### Claim 6: SHA-256 was replaced with FNV-1a for heredoc delimiter generation, improving compiler performance where collision-resistance is not required (PR #40696)

- **Evidence**: PR #40696. The post names the algorithm change (SHA-256 → FNV-1a)
  and the target use case (heredoc delimiters).
- **Confidence**: settled (specific PR, named algorithm change, named use case;
  FNV-1a vs SHA-256 trade-offs are well-established: FNV-1a is significantly
  faster for short inputs, provides good distribution, but is not cryptographic)
- **Quote**: "replaced SHA-256 with FNV-1a for heredoc delimiters, improving
  compiler performance."
- **Our assessment**: Heredoc delimiters in shell scripts are uniqueness markers
  (e.g., `EOF_<hash>`) that must not collide with content but carry no
  cryptographic security requirement. Using SHA-256 for this purpose imposes the
  full cost of a cryptographic hash (SHA-256 is ~10–50× slower than FNV-1a for
  small inputs) for a non-cryptographic problem. The gh-aw compiler generates
  heredoc delimiters on every compile pass; for complex workflows with many
  heredoc blocks, the cumulative SHA-256 overhead is measurable. FNV-1a provides
  adequate collision avoidance for uniqueness-only use cases at a fraction of the
  CPU cost. For Ch02 (Harness Engineering): this is a clear example of
  performance-driven algorithm selection in harness toolchain internals. The
  principle — use collision-resistant hashing only where collision resistance is
  actually required — is applicable to any harness that uses hashing for
  non-cryptographic purposes (cache keys, identifier generation, deduplication).

### Claim 7: JSON-RPC error serialization was fixed to handle plain object throws in error responses and enforce valid error code ranges (PR #40715)

- **Evidence**: PR #40715. The post identifies the symptom (plain object throws
  were returning `[object Object]` in error responses) and the fix (corrected
  serialization + valid JSON-RPC error code enforcement).
- **Confidence**: settled (specific PR, named symptom `[object Object]`, named
  fix dimension)
- **Quote**: "Corrected error serialization for plain objects" (PR #40715)
- **Our assessment**: `[object Object]` in a JSON-RPC error response is a
  JavaScript/TypeScript serialization bug: when a thrown value is a plain object
  (not an `Error` instance with a `.message` property), calling `.toString()` or
  template-string interpolation produces `[object Object]` rather than the
  object's content. In an agent harness, this error response is what an agent
  model receives when a tool call fails — `[object Object]` is an opaque and
  non-actionable error that prevents the agent from diagnosing the failure. The
  fix (proper JSON serialization of the thrown object) ensures that agent models
  receive informative error payloads from failed tool calls. For Ch03 (Safety and
  Verification): JSON-RPC error responses in agent harnesses should serialize
  thrown values as structured JSON, not as coerced strings. A tool that returns
  `[object Object]` on failure is an observability blind spot: the agent model
  cannot recover gracefully from a failure it cannot interpret.

### Claim 8: Sparse checkout path type mismatches in Skillet's pre-activation skills were fixed to prevent type-level bugs at checkout (PR #40684)

- **Evidence**: PR #40684. The post names the component (Skillet pre-activation
  skills), the fix dimension (sparse checkout path type mismatches), and the
  benefit (type-level bug prevention).
- **Confidence**: emerging (specific PR and component named; the nature of the
  type mismatch — e.g., string vs. string[] vs. undefined — is not detailed in
  the changelog)
- **Quote**: "Fixed sparse checkout path type mismatches" (PR #40684)
- **Our assessment**: Sparse checkout in Git allows checking out a subset of a
  repository's file tree by specifying paths. A type mismatch in the path
  specification (e.g., passing a string where a string array is expected, or
  passing `undefined` for a required path) would cause incorrect checkout behavior
  at the pre-activation stage, potentially failing or checking out the wrong
  files. The fix closes a class of checkout configuration bugs at the type level.
  For Ch02 (Harness Engineering): sparse checkout configurations in harness
  pre-activation steps should be validated with typed inputs — type mismatches
  here produce checkout failures that are difficult to diagnose without knowing
  the type contract.

### Claim 9: Daily observability report artifact fetching was fixed to explicitly request artifact sets during log fetches (PR #40705)

- **Evidence**: PR #40705. The post states that artifact sets are now explicitly
  requested during log fetches for the daily observability report workflow.
- **Confidence**: emerging (specific PR; the prior behavior — implicit or missing
  artifact set requests — and its failure mode are not detailed)
- **Quote**: "Ensured artifact sets are explicitly requested" (PR #40705)
- **Our assessment**: Artifact fetching in GitHub Actions may require explicit
  set membership specification when multiple artifact sets exist for a run. The
  fix ensures the daily observability report workflow requests the correct artifact
  set rather than relying on a default that was inconsistently populated. For Ch04
  (Multi-Agent Orchestration/Operations): observability workflows that fetch
  artifacts from other runs should explicitly specify artifact set identifiers
  rather than relying on defaults — implicit artifact fetching is a source of
  intermittent data completeness issues.

## Concrete Artifacts

### PR Summary: Week Ending June 22, 2026

```
No versioned release this week.

Performance:
  Fix: Compiler regression resolved — validateTemplateInjection triggered redundant
       yaml.Unmarshal on every pass; eliminating the redundant calls restores
       BenchmarkCompileComplexWorkflow from 12.7 ms/op back to ~3 ms/op (PR #40662)
  Opt: SHA-256 → FNV-1a for heredoc delimiter generation (compiler performance,
       non-cryptographic use case, PR #40696)

New Linter:
  deferinloop (PR #40679): "identifies `defer` statements inside loops—a pattern
       that causes resource leaks and unpredictable cleanup ordering"

Feature Rollout:
  gh-aw-detection expanded: 20% (43 workflows) → 50% (~107 of 214 workflows)
       +64 newly included (PR #40698)

Reliability Fixes:
  JSON-RPC: "Corrected error serialization for plain objects" (PR #40715)
  Skillet:  "Fixed sparse checkout path type mismatches" (PR #40684)
  Reports:  "Ensured artifact sets are explicitly requested" (PR #40705)

Cost Optimization:
  Opt: "trimmed unnecessary context from system prompts to reduce token consumption
       in high-traffic workflows" (PR #40695)
```

### Agent of the Week: `delight` — June 22, 2026

```
Agent:          delight
Function:       Read-only UX quality auditor for user-facing materials
Scope:          Documentation, CLI help text, workflow messages, validation code
Design criteria (per WebFetch): five design principles:
                  clarity, professional communication, efficiency, trust,
                  and documentation quality
Run outcome:    Recent runs found no issues worthy of filing
                → indicates well-maintained user-facing materials

Operational parameters (from Prospector triage — not verified verbatim):
  Schedule:     3 runs per 30 days
  Sampling:     1–2 docs, 1–2 CLI commands, 1–2 messages, 1 validation file/run
  Issue cap:    2 issues per run
  Mode:         Always read-only (no writes, no PRs)

Pattern:        Read-only, scoped-sampling quality auditor
                Contrast with aw-failure-investigator (~1.57M tokens/run, writes issues):
                  delight uses lower token budget, bounded sampling, read-only scope
```

### Defer-in-Loop Anti-Pattern (PR #40679)

```go
// ANTI-PATTERN caught by deferinloop linter:
// defer fires at FUNCTION return, not end of loop iteration
func processFiles(paths []string) error {
    for _, path := range paths {
        f, err := os.Open(path)
        if err != nil {
            return err
        }
        defer f.Close()  // ← accumulates across all iterations; files held until return
        process(f)
    }
    return nil
}

// CORRECTED (close per-iteration):
func processFiles(paths []string) error {
    for _, path := range paths {
        if err := processFile(path); err != nil {
            return err
        }
    }
    return nil
}

func processFile(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()  // ← fires when processFile returns — correct per-resource cleanup
    return process(f)
}

// linter: deferinloop (PR #40679)
// Flags: defer statements inside for-loop bodies
// Risk: resource leaks + unpredictable cleanup ordering
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-06-15.md` Claim 4 (`linter-miner` auto-generates
    CI-enforced linters from identified bug patterns): The `deferinloop` linter (Claim
    2 here) is a further output attributed to the same `linter-miner` family, corroborating
    that this pattern is actively producing new analyzers in successive weeks. June 15
    delivered two linters (`timeafterleak`, `errorfwrapv`); June 22 adds a third
    (`deferinloop`). The meta-pattern of agentic toolchain augmentation via auto-generated
    linters is reinforced by continued output.
  - `blog-ghaw-weekly-2026-06-15.md` Claim 12 (ambient-context payload reduced across
    daily and PR workflows via cross-workflow optimization pass, PR #39157): PR #40695
    (Claim 5 here) continues the same token-optimization practice — trimming initial
    system-prompt content in high-traffic workflows. The two PRs, one week apart,
    corroborate that ambient-context and system-prompt compression are active ongoing
    practices rather than one-time fixes.

- **Extends**:
  - `blog-ghaw-weekly-2026-05-25.md` Claim 9 (`linter-miner` Agent of the Week:
    produced `fprintlnsprintf` linter in 39 turns, 10.8 minutes, over 1M tokens, 2
    failed attempts): `deferinloop` (Claim 2 here) is a subsequent output from the same
    `linter-miner` meta-workflow. May 25 first documented `linter-miner`'s existence
    and cost profile; June 15 documented its production of two linters in one week;
    June 22 extends the family with a third. Together these three notes trace the
    `linter-miner` pattern from its initial spotlight to an ongoing production
    linter-generation system.
  - `blog-ghaw-weekly-2026-06-15.md` Claims 2–3 (`timeafterleak` and `errorfwrapv`
    as the first two linter-miner–auto-generated linters): `deferinloop` (Claim 2
    here) extends the linter-miner family with a third member addressing a distinct
    Go anti-pattern class (resource cleanup ordering vs. timer goroutine leaks vs.
    error chain preservation). The three linters together cover three independent
    Go reliability failure modes detectable by static analysis.
  - `blog-ghaw-agent-observability.md` Claim 8 (observatory as a named architectural
    component, "the nerve center of Peli's Agent Factory"): `delight` (Claim 4 here)
    extends the observatory pattern with a new agent type — UX quality auditing of
    user-facing materials. The prior observatory spotlight covered performance
    (Metrics Collector), cost (Portfolio Analyst), and meta-audit (Audit Workflows).
    `delight` adds a fourth dimension: user experience quality of the harness itself.

- **Contradicts**: None found. The `deferinloop` linter extends but does not oppose
  prior linting guidance. The FNV-1a optimization (Claim 6) is performance-driven
  algorithm selection with no opposing recommendation in the corpus — no prior source
  advocates for SHA-256 in non-cryptographic contexts. No contradiction issue warranted.

- **Novel**:
  - **Compiler regression from unconditional deserialization in a disabled code path**
    (Claim 1): First corpus source to document a specific harness compiler regression
    caused by unconditional `yaml.Unmarshal` in a conditionally-disabled validation
    function, with concrete benchmark measurements (3 ms/op → 12.7 ms/op). The
    named cause and recovery provide a concrete example of this performance anti-pattern.
  - **`deferinloop` as third linter-miner output in the corpus** (Claim 2): The first
    two linter-miner outputs (`timeafterleak`, `errorfwrapv`) were documented in the
    June 15 note. `deferinloop` confirms the workflow is producing new linters across
    multiple weeks. Three documented outputs in three weeks establish a pattern, not
    a one-time event.
  - **`delight` as a read-only UX audit agent with scoped per-run sampling** (Claim 4):
    First corpus source to document an always-read-only audit agent focused on
    documentation and CLI message quality rather than code correctness, workflow
    reliability, or token cost. The bounded sampling strategy (1–2 artifacts per
    type per run, capped at 2 issues/run) is a new operational pattern in the corpus
    for quality-auditing agents.
  - **`gh-aw-detection` at 50% with explicit workflow counts** (Claim 3): First
    specific percentage-and-count data point for `gh-aw-detection` rollout. Structured
    feature flag progression (20% → 50%, ~64 newly added) with documented workflow
    counts provides a concrete incremental-rollout template.
  - **FNV-1a vs SHA-256 as performance-driven algorithm selection** (Claim 6): First
    corpus source to document an explicit algorithm substitution in harness toolchain
    internals based on the principle that collision-resistance requirements determine
    hash algorithm choice. Prior sources treat hashing as a security concern; this is
    the first performance-driven hashing decision documented.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Document the `validateTemplateInjection` regression pattern (Claim 1) as a
    concrete harness compiler performance example: unconditional deserialization
    inside a conditionally-disabled code path produced a 4.2× benchmark regression.
    Recommend guarding expensive parsing operations behind the same condition that
    determines whether the result is used.
  - Add `deferinloop` to the linter-miner family documentation (Claim 2). Update
    the running list of linter-miner outputs (May 25: `fprintlnsprintf`; June 15:
    `timeafterleak`, `errorfwrapv`; June 22: `deferinloop`) as evidence of an
    active linter-generation pipeline. The defer-in-loop pattern is a real Go
    reliability issue applicable beyond gh-aw harness code.
  - Add FNV-1a vs SHA-256 algorithm selection (Claim 6) as a harness toolchain
    optimization example. Present the principle: use cryptographic hashing only
    where collision resistance is required; for uniqueness-only use cases (cache
    keys, delimiter generation, deduplication), FNV-1a or similar is appropriate
    and significantly faster.

- **Chapter 03 (Safety and Verification)**:
  - Document the defer-in-loop resource leak pattern (Claim 2) as a reliability
    anti-pattern for Go harness code. Add `deferinloop` to the recommended linting
    ruleset alongside `timeafterleak` and `errorfwrapv`. The three linters together
    prevent distinct resource-leak and error-chain failure modes: timer goroutine
    leaks, deferred cleanup leaks, and silent error chain breakage.
  - Document JSON-RPC error serialization requirements for agent harnesses (Claim
    7): agent models receive tool-call error responses verbatim; `[object Object]`
    is an opaque, non-actionable payload that prevents graceful recovery. Recommend
    explicit JSON serialization of thrown objects in tool-call error paths.

- **Chapter 04 (Multi-Agent Orchestration)**:
  - Add `delight` as a named pattern for read-only UX audit agents with scoped
    sampling (Claim 4). Frame the bounded-sampling strategy (1–2 artifacts per
    type per run, 2-issue cap) as the mechanism that prevents audit agents from
    flooding maintainers. Contrast with `aw-failure-investigator`'s high-token
    deep investigation: `delight` demonstrates that periodic, shallow, read-only
    audits complement (but do not replace) deep investigation agents.
  - Add `gh-aw-detection` incremental rollout (Claim 3) as a concrete structured
    feature flag adoption example: define target population, measure at each
    percentage checkpoint (20% → 50%), use deterministic targeting to make rollout
    predictable and reversible.
  - Document artifact-set explicit requests (Claim 9) as a reliability requirement
    for observability workflows that fetch artifacts from other runs — implicit
    artifact fetching produces intermittent completeness gaps.

- **Chapter 05 (Cost Optimization)**:
  - Add initial system-prompt compression (Claim 5, PR #40695) as a periodic
    cost-optimization practice for high-traffic workflows. Frame alongside the
    June 15 ambient-context reduction (PR #39157) as a two-part campaign: the
    June 15 pass targeted ambient context payload; the June 22 pass targeted initial
    system-prompt size. Teams auditing token costs should treat both as distinct
    optimization surfaces.

## Extraction Notes

1. **Source depth**: Two WebFetch passes were made against the source URL. The
   second pass returned more granular detail on PR numbers and metrics; the first
   pass returned a fuller description of the `delight` agent including five named
   design principles. Both passes are used; where they agree (percentages, PR
   numbers, compiler benchmark metrics) confidence is higher. Where only one pass
   surfaced detail (`delight`'s five design principles appeared only in the first
   pass), this is flagged below.

2. **Verbatim confidence**: The following strings appear in both WebFetch returns
   in similar form and are treated as likely verbatim from the source:
   - "slowed compilation from 3 ms/op to 12.7 ms/op" / "redundant YAML unmarshaling
     in `validateTemplateInjection` when validation was disabled" (both passes agree
     on the function name and metric values)
   - "identifies `defer` statements inside loops—a pattern that causes resource
     leaks and unpredictable cleanup ordering" (second pass; verbatim dash included)
   - "scaled `gh-aw-detection` from 20% to 50% of agentic workflows, adding
     approximately 64 newly included workflows to the rollout" (second pass)
   - "trimmed unnecessary context from system prompts to reduce token consumption
     in high-traffic workflows" (second pass)
   - "replaced SHA-256 with FNV-1a for heredoc delimiters, improving compiler
     performance" (second pass)
   - "scans documentation, CLI help text, and validation code for UX improvements,
     filing targeted issues when problems emerge. Recent runs found no issues worthy
     of filing—indicating well-maintained user-facing materials." (second pass)
   Shorter attributed strings in Claims 7, 8, and 9 are labeled as such in the
   Quote fields; treat as paraphrase-class given their brevity and possible model
   extraction.

3. **`delight` design principles**: The five design principles (clarity, professional
   communication, efficiency, trust, documentation quality) appeared only in the
   first WebFetch pass. The Assayer should verify these against the source URL.
   If these are not verbatim from the source, they should be moved from Claim 4's
   body to the Extraction Notes with `(no direct quote; see paraphrase in Our
   assessment)`.

4. **`linter-miner` attribution for `deferinloop`**: The June 15 source explicitly
   stated that `timeafterleak` and `errorfwrapv` were "auto-generated by the
   `linter-miner` workflow and enforced in CI." Neither WebFetch pass for June 22
   included an equivalent explicit attribution for `deferinloop`. The Prospector's
   triage comment states the attribution as a continuation of the June 15 pattern.
   Claim 2's "Our assessment" notes this uncertainty; cross-references describe it
   as the "`linter-miner`-family" with the caveat flagged.

5. **`delight` operational parameters**: Run frequency (3 times per 30 days),
   sampling strategy (1–2 artifacts of each type per run), and issue cap (2/run)
   are from the Prospector's triage comment, not from the WebFetch returns. They
   are included in the Concrete Artifacts section with an explicit note and are
   NOT used as source quotes anywhere in the Claims section.

6. **No contradictions filed**: Reviewed all source notes in the corpus. The
   FNV-1a algorithm choice (Claim 6) has no opposing recommendation. The
   `deferinloop` linter (Claim 2) is additive to the linting guidance from June
   15 and May 25. The `delight` agent type (Claim 4) is novel with no prior corpus
   position to oppose. No contradiction issue warranted.
