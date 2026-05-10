---
source_url: https://github.github.com/gh-aw/reference/compilation-process
source_type: docs
title: "GitHub Agentic Workflows: Compilation Process"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#372"
---

# GitHub Agentic Workflows: Compilation Process

> The detailed technical reference for `gh aw compile` — documents the
> five-phase internal pipeline (parse → construct → resolve → pin → generate),
> the "Plan-Level Trust" rationale for job-level security isolation, action
> pinning as a supply-chain defense, artifact structure, and the key
> runtime/compile-time boundary where only frontmatter changes require
> recompilation.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/compilation-process`
  page — the "Reference" section, not the conceptual `introduction/` pages or
  practitioner `guides/`. Reference pages document internal mechanics and CLI
  behavior authoritatively. Distinct from `docs-ghaw-how-they-work.md`, which
  covers the compilation model at a conceptual level; this page is the detailed
  technical specification of what `gh aw compile` actually does.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team that operates Peli de Halleux's agent factory. CLI commands, job type
  names, artifact names, and phase descriptions are authoritative for the `gh aw`
  platform. Claims about security architecture and compilation behavior are
  settled for this platform; they do not automatically generalize to other agentic
  CI systems.
- **Scope**: Internal mechanics of `gh aw compile` — the five phases, job types,
  job dependency graphs, action pinning, MCP server initialization at compile
  time, artifact generation, compilation commands, debugging, and performance
  benchmarks. Does NOT cover: the conceptual "why" of the compilation model
  (see `docs-ghaw-how-they-work.md` Claim 7), the Safe Outputs mechanism in
  general (see `docs-ghaw-how-they-work.md` Claim 5), MCP server configuration
  (see `docs-ghaw-mcps.md`), or orchestration patterns (see
  `docs-ghaw-orchestration-patterns.md`).

## Extracted Claims

### Claim 1: `gh aw compile` executes a five-phase internal pipeline: parsing/validation → job construction → dependency resolution → action pinning → YAML generation

- **Evidence**: The page names and sequences five distinct compilation phases.
  Phase 1 (parsing/validation): extracts YAML frontmatter, validates against
  workflow schema, validates expression safety, and resolves imports via
  breadth-first traversal. Phases 2–5: construct specialized jobs, resolve
  dependencies, detect circular references, pin actions to SHAs, and assemble
  the final `.lock.yml`.
- **Confidence**: settled (first-party reference documentation; the phase names
  and sequence are authoritative for the platform)
- **Quote**: "The `gh aw compile` command transforms a markdown workflow file
  into a complete GitHub Actions `.lock.yml` by embedding frontmatter and
  setting up runtime loading of the markdown body."
- **Our assessment**: The five-phase description explains *why* compilation takes
  time (it is not a trivial template expansion) and *what* can fail at each stage.
  Phase 1 failing means structural or schema violations in the `.md` source. Phase
  3 (dependency resolution) failing means circular job dependencies in the
  workflow spec. Phase 4 (action pinning) taking longest (~2s) is because it may
  hit the GitHub API for SHA resolution. This is the canonical reference for
  understanding compiler errors in gh-aw workflows. For Ch02 (Harness Engineering):
  compiler errors are diagnostic signals — the phase names map to actionable
  failure categories.

### Claim 2: Import resolution uses a deterministic breadth-first traversal with cycle detection — imports from all workflow files are resolved before job construction begins

- **Evidence**: The page describes the import resolution mechanism explicitly:
  "Imports are resolved with a deterministic breadth-first traversal: starting
  from `imports:` in the main workflow, each file is loaded, its configurations
  are extracted, and any nested imports are appended to the queue." Cycle
  detection is part of Phase 1.
- **Confidence**: settled (first-party; the algorithm is named)
- **Quote**: "Imports are resolved with a deterministic breadth-first traversal:
  starting from `imports:` in the main workflow, each file is loaded, its
  configurations are extracted, and any nested imports are appended to the queue."
- **Our assessment**: The deterministic BFS traversal means import order is
  predictable and reproducible across machines — the same input always produces
  the same compilation output. Cycle detection prevents import loops from hanging
  the compiler. This matters for teams sharing workflow libraries (shared MCP
  configs, shared instruction modules): circular imports fail at compile time
  with a clear error, not at runtime with a hang. For Ch02: when designing shared
  workflow libraries, avoid circular import dependencies — they are caught at
  compile time, not at the point of error in a running workflow.

### Claim 3: Detection, Safe Output, and Conclusion jobs are kept as separate jobs because "GitHub Actions permissions are per-job and immutable for the duration of a job" — merging them would defeat least privilege

- **Evidence**: The page contains an explicit section titled "Why Detection, Safe
  Outputs, and Conclusion Are Separate Jobs." The rationale: "These three jobs
  form a sequential security pipeline rooted in Plan-Level Trust — AI reasoning
  (read-only) is separated from write operations. They cannot be merged because
  GitHub Actions permissions are per-job and immutable for the duration of a job."
  A merged job would hold write permissions while running threat detection,
  defeating least privilege.
- **Confidence**: settled (first-party documentation; the GitHub Actions
  permission model constraint is a platform fact, not an opinion)
- **Quote**: "These three jobs form a sequential security pipeline rooted in
  Plan-Level Trust — AI reasoning (read-only) is separated from write operations.
  They cannot be merged because GitHub Actions permissions are per-job and
  immutable for the duration of a job."
- **Our assessment**: "Plan-Level Trust" is the name for the architectural
  principle that AI reasoning (the agent job) is read-only and structurally
  isolated from write operations (safe output jobs). The technical constraint
  making this enforceable: GitHub Actions grants permissions at the job level,
  not the step level, and those permissions are fixed for the job's duration.
  This means the compiler cannot selectively grant write access for some steps
  within the agent job — it must route writes to a separate job. For Ch02 and
  Ch03: "Plan-Level Trust" is a named pattern worth adding to the guide. It
  explains *why* the job topology looks the way it does in compiled lock files,
  and gives practitioners a principle for designing their own multi-job harnesses
  on any CI platform.

### Claim 4: The pre-activation job runs gating checks (role checks, stop-after deadlines, skip-if-match deduplication, command triggers) before AI execution — failures set `activated=false` and skip all downstream jobs

- **Evidence**: The page describes the pre-activation job as running checks
  sequentially before AI execution, including role checks, stop-after deadlines,
  skip-if-match dedup, and command position validation. "Failures set
  `activated=false`, skipping downstream jobs."
- **Confidence**: settled (first-party documentation; the check types are named)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Pre-activation is the gating layer that prevents AI
  execution when conditions aren't met — a non-AI guard before the AI agent runs.
  The four named checks cover different misfire scenarios: role checks prevent
  unauthorized users from triggering the agent; stop-after deadlines prevent
  runaway recurring workflows; skip-if-match prevents duplicate runs on the same
  content; command triggers validate that the workflow was invoked with the right
  command (e.g., `/approve`). The `activated=false` pattern means downstream jobs
  check this output, not a complex `if:` expression per job. For Ch02: the
  pre-activation pattern is a recommended harness design principle — add a
  non-AI validation stage before AI execution that can abort cleanly.

### Claim 5: The agent job follows a fixed step sequence: repository checkout → runtime setup → cache restoration → MCP container initialization → prompt generation from markdown body → engine execution → output upload → cache persistence

- **Evidence**: The page documents the agent job step order: "The agent job runs:
  repository checkout and runtime setup (Node.js, Python, Go) → cache restoration
  → MCP container initialization → prompt generation from the markdown body →
  engine execution → output upload as a GitHub Actions artifact → cache
  persistence."
- **Confidence**: settled (first-party reference documentation; the step names
  are listed in order)
- **Quote**: "The agent job runs: repository checkout and runtime setup
  (Node.js, Python, Go) → cache restoration → MCP container initialization →
  prompt generation from the markdown body → engine execution → output upload as
  a GitHub Actions artifact → cache persistence."
- **Our assessment**: The fixed step sequence reveals where each type of problem
  occurs. MCP container initialization happens before prompt generation — meaning
  MCP server failures appear before the AI ever receives its prompt. Output is
  uploaded as a GitHub Actions artifact before cache persistence — meaning safe
  output jobs that download the artifact can proceed even if cache persistence
  fails. For Ch02: the step sequence is the diagnostic map for agent job failures.
  A timeout in "MCP container initialization" means a Docker startup problem, not
  an AI reasoning problem.

### Claim 6: All GitHub Actions are pinned to commit SHAs to defend against supply chain attacks — "tags can be moved, SHAs cannot" — with `actions-lock.json` as the resolution cache

- **Evidence**: The page states the action pinning rationale directly: "All
  GitHub Actions are pinned to commit SHAs (e.g., `actions/checkout@b4ffde6...11 # v6`)
  to defend against supply chain attacks — tags can be moved, SHAs cannot."
  Resolution order: cache → GitHub API → embedded pins. The `actions-lock.json`
  file "caches resolved `action@version` → SHA mappings so compilation produces
  consistent results." Users should "Commit `actions-lock.json` to version
  control" for reproducibility.
- **Confidence**: settled (first-party; action pinning to SHAs is a GitHub
  Actions security best practice — the gh-aw compiler enforces it automatically)
- **Quote**: "tags can be moved, SHAs cannot"
- **Our assessment**: Action pinning is a supply-chain security control that
  gh-aw enforces automatically at compile time — practitioners don't need to
  remember to pin actions manually. The `actions-lock.json` cache is analogous
  to a package manager's lockfile: it records the resolved SHA so every developer
  and CI run uses the same immutable artifact. Committing `actions-lock.json` to
  version control is the right practice — it ensures reproducible builds across
  machines. For Ch03 (Safety and Verification): gh-aw's automatic SHA pinning is
  a security default that teams building on other CI platforms should replicate
  manually. It directly addresses supply-chain risks from mutable action tags.

### Claim 7: Only frontmatter changes require recompilation — the markdown body is loaded at runtime, enabling instruction edits without running `gh aw compile`

- **Evidence**: The page makes this boundary explicit: "Compilation is only
  required when changing frontmatter configuration. The markdown body is loaded
  at runtime." This is reinforced in multiple places, including the debugging
  section.
- **Confidence**: settled (first-party; this is a stated design property of the
  compilation model)
- **Quote**: "Compilation is only required when changing **frontmatter
  configuration**. The **markdown body** is loaded at runtime."
- **Our assessment**: This is the most practically important claim on the page
  for daily development. The corollary: you can iterate on agent instructions
  (the natural language part of the workflow) without a compile step — just
  edit the `.md` file and re-run. Only structural changes (permissions, triggers,
  tool configurations, safe output definitions) require `gh aw compile`. For Ch02:
  this boundary should be prominently documented. Teams debugging agent reasoning
  (wrong instructions → edit markdown, re-run) vs. debugging harness structure
  (wrong permissions → edit frontmatter, compile, re-run) have different
  iteration loops.

### Claim 8: Hard gating via detection: the condition `needs.detection.outputs.success == 'true'` prevents safe output jobs from starting if threat detection fails

- **Evidence**: The page describes this explicitly: "Hard gating. The
  `safe_outputs` job condition `needs.detection.outputs.success == 'true'`
  prevents the runner from starting at all if detection fails."
- **Confidence**: settled (first-party; the job condition syntax is documented)
- **Quote**: "Hard gating. The `safe_outputs` job condition
  `needs.detection.outputs.success == 'true'` prevents the runner from starting
  at all if detection fails."
- **Our assessment**: "Hard gating" is the named implementation of the security
  constraint: safe output jobs don't just run after detection, they check
  detection's output before starting. If detection signals a threat, the runner
  for the safe output job never starts — no safe outputs execute. This is distinct
  from "soft" gates where a downstream job starts but early-exits; hard gating
  means zero execution of write operations on a detection failure. For Ch03:
  add "hard gating" as a named security pattern for any multi-phase agentic
  pipeline. The pattern: threat scan → boolean output → downstream jobs check
  output before starting.

### Claim 9: The agent job produces five artifact types: `agent_output.json` (structured safe output data), `agent_usage.json` (aggregated token counts), `prompt.txt` (the generated prompt), `firewall-audit-logs` (network audit trail), and `cache-memory/` (persistent agent memory)

- **Evidence**: The page documents each artifact's purpose:
  - `agent_output.json`: "AI agent output with structured safe output data
    (create_issue, add_comment, etc.)"
  - `agent_usage.json`: "Aggregated token counts"
  - `prompt.txt`: "Generated prompt sent to AI agent (includes markdown
    instructions, imports, context variables)"
  - `firewall-audit-logs`: "Dedicated artifact for AWF audit/observability logs
    (token usage, network policy, audit trail)"
  - `cache-memory/`: persistent memory between runs
  All are "Uploaded by agent job, downloaded by safe output jobs, auto-deleted
  after 90 days."
- **Confidence**: settled (first-party; artifact names and descriptions are
  explicitly listed)
- **Quote**: "AI agent output with structured safe output data (create_issue,
  add_comment, etc.)"
- **Our assessment**: The artifact inventory explains the hand-off mechanism
  between the agent job and safe output jobs — the agent job doesn't directly
  invoke GitHub API operations; it writes structured output to `agent_output.json`,
  and safe output jobs read that file to execute the actual API calls. This is
  the concrete implementation of "Plan-Level Trust" from Claim 3. `prompt.txt`
  is significant for debugging: the generated prompt (which includes resolved
  imports and context variables, not just the raw markdown) is stored and
  accessible, enabling post-run inspection of exactly what the agent received.
  `firewall-audit-logs` is the network-level audit trail — token usage and
  network policy events, separate from the agent's logical output. For Ch02:
  document the artifact names for teams building tooling around gh-aw runs
  (e.g., cost dashboards reading `agent_usage.json`, compliance tools reading
  `firewall-audit-logs`).

### Claim 10: Local MCP servers run in Docker containers with auto-generated Dockerfiles and connect via stdio; HTTP servers connect directly with configured headers and authentication

- **Evidence**: The page documents: "Local servers run in Docker containers with
  auto-generated Dockerfiles and connect via stdio; HTTP servers connect directly
  with configured headers and authentication."
- **Confidence**: settled (first-party; transport types and connection mechanisms
  are described)
- **Quote**: "Local servers run in Docker containers with auto-generated
  Dockerfiles and connect via stdio; HTTP servers connect directly with configured
  headers and authentication."
- **Our assessment**: The auto-generated Dockerfile for stdio MCP servers means
  the compiler does the container setup work — practitioners write the MCP server
  command and the compiler wraps it in a container. This is a lower-friction path
  to containerized MCP isolation than manually writing Dockerfiles. It also means
  the compilation process touches more than just the YAML — it generates
  supporting infrastructure artifacts. For Ch02: note that stdio MCP servers
  run containerized automatically at compile time; practitioners do not need
  to write their own Docker configuration for simple stdio servers.

### Claim 11: `gh aw compile` supports security scanner integrations via `--actionlint`, `--zizmor`, and `--poutine` flags for additional static analysis of the generated lock file

- **Evidence**: The compilation commands section lists: `gh aw compile --actionlint
  --zizmor --poutine` as a command variant. The page also lists other key flags:
  `--verbose` (trace compilation), `--strict` (stricter validation), `--no-emit`
  (validate without writing), `--purge` (remove stale lock files).
- **Confidence**: settled (first-party; CLI flags are documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `--actionlint`, `--zizmor`, and `--poutine` flags
  integrate established GitHub Actions security scanners into the compile step —
  actionlint validates Actions syntax, zizmor checks for security anti-patterns
  in GitHub Actions YAML, and poutine detects pinning and injection issues. Running
  these at compile time means security analysis happens before the lock file is
  committed, not after a PR is raised. `--no-emit` is particularly useful for
  CI validation — compile and validate without writing output (e.g., in a PR
  check that verifies the workflow spec is valid). For Ch03: recommend
  `gh aw compile --actionlint --zizmor --poutine` as the security-aware compile
  command in harness CI pipelines.

### Claim 12: Dependabot pin updates must come from `gh aw compile`, not from direct edits — the compiler auto-inserts a Dependabot ignore rule to prevent pin drift

- **Evidence**: The page states: "Pin updates must come from `gh aw compile`,
  which coordinates pins across all compiled workflows from a single release.
  `gh aw compile` automatically inserts an ignore rule when a `github-actions`
  update block exists."
- **Confidence**: settled (first-party; the automatic ignore rule insertion is
  a stated compiler behavior)
- **Quote**: "Pin updates must come from `gh aw compile`, which coordinates pins
  across all compiled workflows from a single release."
- **Our assessment**: This claim explains why the `actions-lock.json` approach
  differs from raw Dependabot — Dependabot updates one action at a time, but
  gh-aw's pin coordination updates all actions across all compiled workflows
  simultaneously from a single `gh aw compile` run. The auto-inserted ignore rule
  prevents Dependabot from creating conflicting pin PRs that bypass the
  compiler-coordinated update mechanism. For Ch02: teams should not manually edit
  `actions-lock.json` or override the Dependabot ignore rule — pin management
  is the compiler's responsibility.

### Claim 13: Compilation performance benchmarks: ~100ms for simple workflows, ~500ms for workflows with imports, ~2s for workflows that resolve action SHAs dynamically

- **Evidence**: The performance section states: "Simple workflows compile in
  ~100ms; workflows with imports in ~500ms; workflows that resolve action SHAs
  dynamically in ~2s."
- **Confidence**: settled (first-party benchmarks; representative, not guarantees)
- **Quote**: "Simple workflows compile in ~100ms; workflows with imports in
  ~500ms; workflows that resolve action SHAs dynamically in ~2s."
- **Our assessment**: The ~2s figure for dynamic SHA resolution is the bottleneck
  for new or updated workflows — it requires a GitHub API call per action version
  not already in `actions-lock.json`. After the first compile (which populates
  the cache), subsequent compiles for frontmatter-only changes run in the ~100ms
  range. The performance profile suggests: commit `actions-lock.json` to avoid
  the 2s penalty on CI; keep imports shallow to stay in the ~100ms range for
  quick iteration. For Ch02: the compile-time SLA is low enough that `gh aw
  compile --watch` is viable as a real-time development loop (sub-500ms feedback
  for most workflows).

### Claim 14: The job dependency graph executes safe output jobs in parallel when they have no cross-dependencies; all safe outputs depend on both the agent and detection jobs when threat detection is enabled

- **Evidence**: The page describes: "Pre-activation validates permissions →
  Activation prepares context → Agent executes AI → Detection scans output →
  Safe outputs run in parallel → Add comment waits for created items → Conclusion
  summarizes results." And: "When threat detection is enabled, safe outputs depend
  on both agent and detection jobs."
- **Confidence**: settled (first-party; dependency rules are explicitly stated)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Parallel safe output execution means multiple GitHub API
  operations (e.g., creating an issue and adding a label) can run concurrently,
  reducing overall workflow duration. The sequential constraint only applies where
  there is data dependency (e.g., an "add comment" job that needs a created issue
  ID to reference). The detection gate (Claim 8) is the serialization point:
  all safe outputs wait for detection to complete before starting. For Ch02: the
  parallelism opportunity in safe output jobs is a harness optimization — design
  safe outputs to be independent where possible, and they run concurrently
  automatically.

## Concrete Artifacts

### Five-Phase Compilation Pipeline

```
Input: workflow-name.md

Phase 1: Parsing and Validation
  - Extract YAML frontmatter
  - Validate against workflow schema
  - Validate expression safety
  - Resolve imports via BFS traversal (with cycle detection)
  Timing contribution: minimal (parse only)

Phase 2: Job Construction
  - Build: pre-activation, activation, agent, detection, safe output, custom, conclusion jobs

Phase 3: Dependency Resolution
  - Validate job dependencies
  - Detect circular references
  - Compute topological order

Phase 4: Action Pinning
  Resolution order: cache (actions-lock.json) → GitHub API → embedded pins
  Timing: ~100ms (cache hit) → ~2s (API call for new SHAs)

Phase 5: YAML Generation
  - Assemble final .lock.yml
  - Embed metadata, dependency graphs, and generated prompt

Output: workflow-name.lock.yml
```

*Source: `reference/compilation-process` — "Compilation Phases" section*

### Job Types and Execution Roles

```
Job              | Trigger / Condition                          | Purpose
-----------------|----------------------------------------------|-----------------------------
pre_activation   | Always (runs first)                          | Role checks, deadlines,
                 |                                              | skip-if-match dedup,
                 |                                              | command position validation
activation       | activated=true (pre_activation output)       | Context prep, event sanitization,
                 |                                              | lock file freshness check
agent            | activated=true                               | Core AI execution: engine,
                 |                                              | tools, MCP servers
detection        | threat-detection configured                  | Scans output for security threats
safe output jobs | Corresponding safe-output configured         | GitHub API operations
                 | (+ needs.detection.outputs.success='true'    | (write operations)
                 |  when detection is enabled)                  |
conclusion       | always() — if safe outputs exist             | Aggregates results and summary
```

*Source: `reference/compilation-process` — "Job Types" section*

### Plan-Level Trust — Job Isolation Rationale

```
Why detection, safe outputs, and conclusion are separate jobs:

"These three jobs form a sequential security pipeline rooted in Plan-Level
Trust — AI reasoning (read-only) is separated from write operations. They
cannot be merged because GitHub Actions permissions are per-job and immutable
for the duration of a job."

Properties enabled by job-level isolation:
  1. Hard gating: safe_outputs depends on detection.outputs.success == 'true'
     → runner never starts if detection fails
  2. always() semantics: conclusion can run even if safe outputs fail
  3. Right-sized runners: different jobs can use different runner sizes
  4. Concurrency isolation: safe output jobs run in parallel
  5. Artifact-based handoff: output passed via artifact, preventing
     in-process tampering between phases
```

*Source: `reference/compilation-process` — "Why Detection, Safe Outputs, and
Conclusion Are Separate Jobs" section*

### Agent Job Step Sequence

```
Step 1: Repository checkout + runtime setup (Node.js, Python, Go)
Step 2: Cache restoration
Step 3: MCP container initialization
         └─ Stdio servers: Docker containers with auto-generated Dockerfiles
         └─ HTTP servers: direct connection with configured headers/auth
Step 4: Prompt generation from markdown body
         └─ Includes: markdown instructions + resolved imports + context variables
         └─ Stored as: prompt.txt artifact
Step 5: Engine execution (configured AI engine)
Step 6: Output upload as GitHub Actions artifact (agent_output.json)
Step 7: Cache persistence (cache-memory/)
```

*Source: `reference/compilation-process` — "Agent Job Steps" section*

### Artifact Inventory

```
Artifact              | Producer    | Consumer(s)         | Retention | Description
----------------------|-------------|---------------------|-----------|------------------
agent_output.json     | agent job   | safe output jobs    | 90 days   | Structured safe
                      |             |                     |           | output data
                      |             |                     |           | (create_issue,
                      |             |                     |           | add_comment, etc.)
agent_usage.json      | agent job   | observability tools | 90 days   | Aggregated token
                      |             |                     |           | counts
prompt.txt            | agent job   | debugging           | 90 days   | Generated prompt
                      |             |                     |           | (instructions +
                      |             |                     |           | imports + context)
firewall-audit-logs   | agent job   | compliance/audit    | 90 days   | AWF audit logs:
                      |             |                     |           | token usage,
                      |             |                     |           | network policy,
                      |             |                     |           | audit trail
cache-memory/         | agent job   | future agent runs   | varies    | Persistent agent
                      |             |                     |           | memory across runs
```

*Source: `reference/compilation-process` — "Artifacts Created" and
"firewall-audit-logs Artifact Structure" sections*

### Compilation Commands Reference

```bash
# Basic compilation
gh aw compile                     # compile all workflows
gh aw compile my-workflow         # compile specific workflow

# Development and validation
gh aw compile --verbose           # trace compilation (job creation, pin resolution)
gh aw compile --strict            # stricter validation
gh aw compile --no-emit           # validate without writing (CI check)

# Security analysis
gh aw compile --actionlint --zizmor --poutine   # additional security scanners

# Maintenance
gh aw compile --purge             # remove stale lock files

# Output customization
gh aw compile --output /path/to/output
gh aw compile --action-mode action --actions-repo owner/repo

# Validation only (no compilation)
gh aw validate
gh aw validate --json

# Debugging with full trace
DEBUG=workflow:* gh aw compile my-workflow --verbose
```

*Source: `reference/compilation-process` — "Compilation Commands" and
"Debugging Compilation" sections*

### Runtime vs Compile-Time Boundary

```
REQUIRES gh aw compile:             DOES NOT require gh aw compile:
───────────────────────────         ────────────────────────────────
- permissions block changes         - Editing markdown instruction body
- triggers block changes            - Changing natural language task descriptions
- tools / mcp-servers changes       - Adding/removing markdown imports
- safe-outputs definitions          - Tweaking prompt wording
- Any frontmatter YAML change       (markdown loaded at runtime, not embedded)

Key: The .md file is the editable source of truth.
     The .lock.yml embeds the frontmatter and references the markdown for runtime load.
```

*Source: `reference/compilation-process` — multiple sections*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 7 (`.md` → `.lock.yml` compilation model):
    this source is the detailed technical specification of the compilation mechanism
    that Claim 7 describes at a conceptual level. Both establish that the compilation
    step is where security hardening happens; this source adds the five-phase
    breakdown and the specific security behaviors (action pinning, job isolation,
    artifact generation) that constitute that hardening.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth pipeline,
    Layer 1: compilation-time validation): Claim 1 here specifies what Phase 1
    validation actually checks (schema, expression safety, import cycle detection).
    Together they give the complete picture of what "compile-time validation" means
    in practice.
  - `docs-ghaw-how-they-work.md` Claim 4 ("no write access by default"):
    Claim 3 here (Plan-Level Trust, job-level permission isolation) is the concrete
    mechanism enforcing that principle. The agent job has read-only permissions;
    write permissions exist only in separate safe output jobs. The permission model
    is per-job and immutable, making this isolation structurally guaranteed, not
    policy-dependent.
  - `docs-ghaw-orchestration-patterns.md` Claim 5 (compile-time validation for
    orchestration targets): that source describes the compiler validating dispatch
    and call targets; Claim 1 here provides the phase structure (Phase 1:
    parsing/validation) that contains those checks. The two together give the full
    scope of Phase 1: schema validation + expression safety + import cycles +
    orchestration target validation.
  - `blog-gh-aw-operations-release-workflows.md` Claim 4 (`gh aw compile` +
    lock file separation from a practitioner perspective): this source is the
    canonical technical reference for what that practitioner observation describes.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 11 (compile → watch → run → review
    development workflow): Claim 13 here adds the performance benchmarks
    (~100ms/~500ms/~2s by workflow complexity) that explain why `gh aw compile
    --watch` is viable as a real-time development loop — sub-500ms compile times
    make it practical.
  - `docs-ghaw-mcps.md` Claim 2 (four MCP server types with distinct isolation
    profiles): Claim 10 here adds that the compilation process auto-generates
    Docker infrastructure for stdio MCP servers — the containerization of local
    MCP servers is a compile-time product, not a runtime configuration. This
    resolves the question of how stdio servers get sandboxed without manual
    Dockerfile authoring.
  - `docs-ghaw-orchestration-patterns.md` Claim 3 (call-workflow generates typed
    MCP tools per worker at compile time): this source's Phase 2 (job construction)
    is where those typed MCP tools are generated. The two together give a complete
    picture of what Phase 2 produces: not just the named job types, but also
    per-worker MCP tool schemas for call-workflow orchestration.
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as permission-separated
    state mutation): Claim 9 here adds the artifact-based handoff mechanism —
    the agent writes `agent_output.json`; safe output jobs read and execute it.
    This is the concrete implementation of how Safe Outputs maintains permission
    separation without real-time inter-process communication.

- **Contradicts**: None identified. No existing source note makes claims that
  conflict with the five-phase pipeline, job isolation model, action pinning
  approach, or runtime/compile-time boundary described here. The compilation
  model in `docs-ghaw-how-they-work.md` Claim 7 and practitioner accounts in
  `blog-gh-aw-operations-release-workflows.md` Claim 4 are consistent with the
  technical details in this reference page. No contradiction issue required.

- **Novel**:
  - **Five-phase compilation pipeline with timing benchmarks** (Claim 1, 13):
    No existing source note names the five internal phases or provides performance
    benchmarks. `docs-ghaw-how-they-work.md` Claim 7 describes the `.md` →
    `.lock.yml` model conceptually; this is the first technical enumeration of
    what the compiler does in those phases.
  - **"Plan-Level Trust" as a named security principle** (Claim 3): The phrase
    "Plan-Level Trust" and its precise definition (AI reasoning is structurally
    isolated from write operations via GitHub Actions' per-job permission model)
    appear nowhere else in the corpus. This is the named architectural principle
    behind the job topology in compiled lock files.
  - **Import resolution algorithm** (Claim 2): BFS traversal with cycle detection
    as the import resolution mechanism is new to the corpus.
  - **Hard gating pattern** (Claim 8): The named "hard gating" pattern
    (`needs.detection.outputs.success == 'true'` as a job start condition) is not
    described in any existing source note. `docs-ghaw-how-they-work.md` Claim 3
    names output sanitization as a security layer but does not name or describe
    the gating mechanism that prevents safe output job execution.
  - **Artifact inventory with descriptions** (Claim 9): `agent_output.json`,
    `agent_usage.json`, `prompt.txt`, `firewall-audit-logs`, `cache-memory/`
    as named artifacts with their specific contents are new to the corpus. No
    existing note documents the artifact-based handoff between agent and safe
    output jobs.
  - **Action pinning with `actions-lock.json` and Dependabot coordination** (Claims
    6, 12): The automatic SHA pinning, `actions-lock.json` as a committed lockfile,
    and the compiler-inserted Dependabot ignore rule are new. No existing note
    covers supply-chain defense at the action-reference level.
  - **Security scanner CLI flags** (Claim 11): `--actionlint --zizmor --poutine`
    as compile-time security analysis integration is new to the corpus.
  - **Runtime/compile-time boundary** (Claim 7): While `docs-ghaw-how-they-work.md`
    Claim 7 mentions the compilation model, no existing note explicitly states
    that only frontmatter changes require recompilation and that markdown body edits
    take effect at runtime without recompiling.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add "Plan-Level Trust" as a named harness design principle** (Claim 3): The
  architectural reason job-level permission isolation is enforced in gh-aw —
  GitHub Actions permissions are per-job and immutable — generalizes to any CI
  harness that uses job-level trust boundaries. The principle: read-only AI
  reasoning and write operations must live in separate jobs. Add this as a named
  pattern alongside the five-layer security model.

- **Document the runtime/compile-time boundary** (Claim 7): This is the most
  actionable daily-use guidance on the page. When debugging: if the agent's
  reasoning is wrong, edit the markdown body and re-run — no compile needed.
  If permissions/triggers/tools are wrong, edit frontmatter and compile. The
  guide should state this boundary explicitly and prominently.

- **Add artifact inventory as a debugging reference** (Claim 9): Teams building
  tooling around gh-aw runs (cost dashboards, compliance reports) should know
  the artifact names and their contents. `prompt.txt` is particularly valuable
  for debugging — it shows exactly what the agent received, including resolved
  imports. Add the artifact inventory to Ch02's reference material.

- **Add auto-generated MCP container behavior** (Claim 10): Stdio MCP servers
  are containerized automatically at compile time via auto-generated Dockerfiles.
  Practitioners do not need to write Docker configuration for simple stdio servers.
  Update the MCP integration guidance to reflect this compile-time behavior.

- **Add compile-time security scanners to recommended CI pipeline** (Claim 11):
  `gh aw compile --actionlint --zizmor --poutine` should be the recommended
  command in CI pipelines that validate workflow changes. `--no-emit` is the
  CI-safe variant that validates without writing output.

### Chapter 03: Safety and Verification

- **Add "Plan-Level Trust" to the defense-in-depth section** (Claim 3): The
  five-layer model in `docs-ghaw-how-they-work.md` covers the pipeline; this
  source names the principle that mandates separate jobs for AI reasoning vs.
  write operations. Add to Ch03 as the architectural reason why job separation
  is a security property, not just a workflow organization choice.

- **Add "hard gating" as a named safety pattern** (Claim 8): The pattern:
  threat detection → boolean output → downstream jobs check output before
  starting (runner never starts if gate fails). This is a stronger guarantee
  than soft gates (job starts but exits early). Recommend for any agentic
  pipeline where a threat detection phase precedes write operations.

- **Add action pinning to SHA as a supply-chain control** (Claim 6): gh-aw
  enforces this automatically; other CI platforms require manual discipline.
  Ch03 should name SHA pinning as a recommended harness security practice,
  cite this as the reference, and recommend committing `actions-lock.json` (or
  equivalent lockfiles) to version control.

### Chapter 01: Daily Workflows / Iteration Loops

- **Update development loop to include compile-time benchmarks** (Claim 13):
  The compile → watch → run → review loop from `docs-ghaw-how-they-work.md`
  Claim 11 can be enriched with timing context: simple workflows compile in
  ~100ms, making `--watch` viable as a real-time feedback loop. Workflows
  resolving new action SHAs take ~2s on first compile (cache warm thereafter).

## Extraction Notes

1. **WebFetch returns AI-summarized content**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch returns rendered text, not raw HTML. Three
   targeted fetches were used to maximize content coverage — one overview fetch
   and two detail-focused fetches. The YAML examples, phase descriptions, job
   type table, and artifact descriptions are assessed as accurate based on
   consistency across fetches.

2. **Some section text was paraphrased in extraction**: Where WebFetch returned
   clear paraphrases rather than direct quotes (notably the pre-activation job
   checks and job dependency graph description), claims are marked "(no direct
   quote; see paraphrase in Our assessment)" per MINER.md §2a guidance. Direct
   quotes are used only for text confirmed as verbatim.

3. **Advanced Topics and Related Documentation sections not followed**: The page
   references sub-pages from "Related Documentation." These were not followed
   per scope constraints — the focus was on the main compilation reference content.

4. **No publication date**: The documentation does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-10.

5. **No contradictions to file**: Reviewed all existing source notes. No claims
   in this source materially oppose any existing source note at the MINER.md
   §4a filing threshold. The "Plan-Level Trust" principle and hard gating
   pattern are additive to the existing security architecture in
   `docs-ghaw-how-they-work.md`; they do not contradict it.
