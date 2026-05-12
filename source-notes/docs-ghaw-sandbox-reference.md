---
source_url: https://github.github.com/gh-aw/reference/sandbox
source_type: docs
title: "GitHub Agentic Workflows: Sandbox Configuration Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#411"
---

# GitHub Agentic Workflows: Sandbox Configuration Reference

> The authoritative configuration reference for gh-aw's `sandbox:` frontmatter
> field — documents the AWF (Agent Workflow Firewall) as the default coding agent
> sandbox, its three-tier filesystem access model (user read-write / system
> read-only / Docker socket hidden), environment variable handling via `--env-all`
> and `AWF_HOST_PATH`, the experimental MCP Gateway routing layer, and the complete
> timeout and build-artifact-caching configuration for long-running agent jobs.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/sandbox` page — in
  the "Reference" section, alongside `reference/network`, `reference/permissions`,
  `reference/tools`. Reference pages document platform configuration authoritatively.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI.
  Configuration field names, sandbox behavior, filesystem access rules, and
  environment variable handling are authoritative for this platform. The MCP Gateway
  is explicitly marked experimental; stability claims should not be assumed.
- **Scope**: The complete configuration reference for the `sandbox:` frontmatter
  field and its two sub-capabilities (AWF coding agent sandbox and MCP Gateway),
  plus the timeout (`timeout-minutes` and `tools.timeout`) and build-caching
  configuration relevant to long-running agent jobs. Does NOT cover: the
  `network:` field in depth (see `docs-ghaw-network-reference.md`), MCP server
  declarations in depth (see `docs-ghaw-mcps.md`), permissions model (see
  `docs-ghaw-permissions-reference.md`), or rate-limiting controls (see
  `docs-ghaw-rate-limiting-controls.md`).

## Extracted Claims

### Claim 1: The `sandbox:` field configures two independent capabilities — the coding agent sandbox (AWF firewall) and the MCP Gateway — and defaults to `sandbox.agent: awf` when omitted

- **Evidence**: Opening section of the reference page explicitly states: "If
  `sandbox` is not specified in your workflow, it defaults to `sandbox.agent: awf`."
  The page documents two distinct sub-fields: `sandbox.agent` (for the coding agent
  sandbox) and `sandbox.mcp` (for the MCP Gateway). The combined configuration
  example shows them coexisting independently.
- **Confidence**: settled (first-party reference documentation; default behavior of
  an unset field is a platform specification)
- **Quote**: "If `sandbox` is not specified in your workflow, it defaults to
  `sandbox.agent: awf`."
- **Our assessment**: The two-sub-field structure is architecturally significant:
  the agent firewall and the MCP Gateway are independently configurable, so
  disabling one does not affect the other. This separation enables hybrid
  configurations (e.g., firewall disabled for development, MCP Gateway enabled
  for routing). The default-to-AWF behavior means teams that omit `sandbox:`
  are protected by the firewall without needing to opt in — consistent with the
  "zero capability by default" principle in `docs-ghaw-how-they-work.md` Claim 4.
  For Ch02 (Harness Engineering): `sandbox:` is an optional field with a secure
  default; practitioners who need to change the default should understand both
  sub-fields before modifying.

### Claim 2: AWF is the default coding agent sandbox providing network egress control through domain-based access controls — it is the runtime isolation implementation for all engines

- **Evidence**: The page states: "AWF is the default coding agent sandbox that
  provides network egress control through domain-based access controls." AWF is
  configured via `sandbox.agent: awf` and integrates with the top-level `network:`
  field for domain allowlisting.
- **Confidence**: settled (first-party documentation; AWF as the default sandbox
  type for all engines is an explicit platform specification)
- **Quote**: "AWF is the default coding agent sandbox that provides network egress
  control through domain-based access controls."
- **Our assessment**: AWF is Layer 2 (Runtime Isolation) of the five-layer
  defense-in-depth pipeline named in `docs-ghaw-how-they-work.md` Claim 3. The
  network reference (`docs-ghaw-network-reference.md` Claim 8) confirms that AWF
  applies identically across all supported engines (Copilot, Claude, Codex,
  Gemini). This sandbox reference adds the filesystem and environment dimensions
  that the network reference omits — together, the two notes give the complete
  AWF security model: network egress control (network-reference) + filesystem
  access tiers + environment variable isolation (this note). For Ch03 (Safety and
  Verification): AWF is the concrete implementation of runtime isolation — not a
  conceptual layer but a running firewall process that enforces network and
  filesystem controls simultaneously.

### Claim 3: `sandbox.agent: false` disables only the agent firewall while keeping the MCP Gateway enabled — a documented partial security downgrade

- **Evidence**: The page states: "Setting `sandbox.agent: false` disables only the
  agent firewall while keeping the MCP gateway enabled."
- **Confidence**: settled (first-party documentation; this is a platform specification
  about the partial disablement semantics)
- **Quote**: "Setting `sandbox.agent: false` disables only the agent firewall while
  keeping the MCP gateway enabled."
- **Our assessment**: The "disables only" phrasing is deliberate — the platform
  documents this as a partial downgrade, not a full sandbox disable. The intended
  use case is not stated on the page, but disabling the firewall while keeping the
  MCP Gateway would be appropriate in controlled environments where network egress
  restrictions are enforced at a different layer (e.g., a self-hosted runner on a
  restricted network) or during local development where firewall blocking interferes
  with testing. For Ch03: document `sandbox.agent: false` as a flag that reduces
  the sandbox posture. Teams should have an explicit justification before using it;
  the default (`awf`) is the secure option.

### Claim 4: AWF implements a three-tier filesystem access model: user paths (read-write), system paths (read-only), and the Docker socket (hidden/blocked)

- **Evidence**: The page contains a filesystem access table with three rows:
  (1) User paths: Read-write, examples `$HOME`, `$GITHUB_WORKSPACE`, `/tmp`;
  (2) System paths: Read-only, examples `/usr`, `/opt`, `/bin`, `/lib`;
  (3) Docker socket: Hidden, `/var/run/docker.sock` with note "(security)".
- **Confidence**: settled (first-party reference; the table specifies platform
  behavior authoritatively)
- **Quote**: (no single prose quote; see table in Concrete Artifacts)
- **Our assessment**: The three-tier model maps directly to the threat hierarchy:
  user paths need read-write for the agent to do its work (read and write code,
  create temp files); system paths are read-only to prevent tampering with runtime
  binaries; the Docker socket is hidden entirely to block the highest-privilege
  escape vector. The read-only system paths constraint means agents cannot modify
  installed system packages or replace system utilities — even if an attacker's
  prompt instructs the agent to overwrite `/bin/sh`. For Ch03: the filesystem
  access table is the concrete isolation specification for Layer 2 (Runtime
  Isolation). The hidden Docker socket is the most important row — it is the reason
  AWF prevents privilege escalation via container spawning (see Claim 5).

### Claim 5: The Docker socket is hidden for security — agents cannot spawn containers, preventing a class of privilege escalation via recursive container creation

- **Evidence**: The page states: "Docker socket is hidden for security. Agents
  cannot spawn containers."
- **Confidence**: settled (first-party documentation; the capability prohibition is
  explicit)
- **Quote**: "Docker socket is hidden for security. Agents cannot spawn containers."
- **Our assessment**: Hiding the Docker socket (`/var/run/docker.sock`) removes the
  agent's ability to create new containers, which would otherwise be a significant
  privilege escalation vector — a container with `--privileged` or volume mounts
  could bypass the AWF restrictions applied to the agent process itself. Without
  Docker socket access, an agent cannot escape its filesystem and network boundaries
  by launching a sibling container with different permissions. This is a specific,
  named security countermeasure against a well-known container escape pattern. For
  Ch03: explicitly name Docker socket hiding as a privilege escalation countermeasure
  in the AWF security model. It belongs alongside the `allowed:` tool filter and
  `network:` egress controls as a named security primitive. For Ch02: practitioners
  who need container operations in their agent workflows must do so via pre-built
  setup steps (before the agent runs) rather than via agent-issued Docker commands.

### Claim 6: All host binaries are available inside the AWF sandbox without explicit configuration — system utilities, `gh`, language runtimes, build tools, and anything installed via `apt-get` or setup actions

- **Evidence**: The page states: "All host binaries are available without explicit
  mounts: system utilities, `gh`, language runtimes, build tools, and anything
  installed via `apt-get` or setup actions. Verify with `which <tool>`."
- **Confidence**: settled (first-party documentation; this is a platform specification
  about the default binary access model)
- **Quote**: "All host binaries are available without explicit mounts: system
  utilities, `gh`, language runtimes, build tools, and anything installed via
  `apt-get` or setup actions."
- **Our assessment**: This is a usability guarantee that distinguishes AWF from
  more restrictive container sandboxes that require explicit binary mounts. A
  workflow that installs Node.js via `actions/setup-node@v4` before the agent
  step will have `node` and `npm` available to the agent — no additional
  configuration is needed. The "Verify with `which <tool>`" tip is practical
  debugging advice. For Ch02: document that setup actions run before the agent
  step are the correct way to provision language runtimes and tools for agent
  use; the agent inherits the full host binary surface configured in `jobs.setup`.

### Claim 7: AWF passes all environment variables into the sandbox via `--env-all`; the host `PATH` is captured as `AWF_HOST_PATH` and restored inside the container, preserving setup action tool paths

- **Evidence**: The page states: "AWF passes all environment variables via
  `--env-all`. The host `PATH` is captured as `AWF_HOST_PATH` and restored inside
  the container, preserving setup action tool paths."
- **Confidence**: settled (first-party documentation; the specific mechanism
  (`--env-all`, `AWF_HOST_PATH`) is named explicitly)
- **Quote**: "AWF passes all environment variables via `--env-all`. The host `PATH`
  is captured as `AWF_HOST_PATH` and restored inside the container, preserving
  setup action tool paths."
- **Our assessment**: The `--env-all` behavior means environment variables set
  in `jobs.setup.env:` and `env:` frontmatter sections are automatically available
  inside the agent sandbox without additional plumbing. The `AWF_HOST_PATH`
  mechanism solves a non-obvious problem: when a setup action (e.g.,
  `actions/setup-python@v5`) modifies `PATH` to include `/home/runner/.local/bin`
  or similar tool directories, those additions would normally be lost when a new
  process starts in a container. AWF explicitly captures the host `PATH` after
  all setup steps complete and restores it inside the sandbox, ensuring the agent
  sees the same `PATH` as the setup step that just ran. For Ch02: this is an
  important implementation detail for practitioners who encounter "command not
  found" errors for tools that were installed in setup steps — the AWF PATH
  restoration handles this automatically, so the fix is not reconfiguring `PATH`
  but ensuring setup actions complete before the agent step.

### Claim 8: Go's "trimmed" binaries require `GOROOT` — AWF automatically captures `GOROOT` after `actions/setup-go`, handling this edge case transparently

- **Evidence**: The page states: "Go's 'trimmed' binaries require `GOROOT` - AWF
  automatically captures it after `actions/setup-go`."
- **Confidence**: settled (first-party documentation; the specific Go/GOROOT
  edge case is named explicitly)
- **Quote**: "Go's \"trimmed\" binaries require `GOROOT` - AWF automatically
  captures it after `actions/setup-go`."
- **Our assessment**: Go's "trimmed" binary builds strip the path prefix from
  binaries, requiring a valid `GOROOT` at runtime for certain runtime operations.
  Without AWF's explicit `GOROOT` capture, a Go workflow would silently fail when
  the agent attempts to run `go test` or `go build` inside the sandbox. AWF's
  special handling of `GOROOT` alongside `AWF_HOST_PATH` represents platform-level
  awareness of Go runtime requirements — practitioners using Go workflows do not
  need to add explicit `GOROOT` configuration. For Ch02: document this as a
  transparent AWF behavior for Go workflows; include it as a gotcha note for
  practitioners who are debugging Go tool failures inside agent sandboxes (if
  `GOROOT` errors appear, verify `actions/setup-go` runs before the agent step).

### Claim 9: MCP Gateway is an experimental feature that routes all MCP server calls through a unified HTTP gateway, enabling centralized management, logging, and authentication; requires the `mcp-gateway` feature flag

- **Evidence**: The page states: "The MCP Gateway routes all MCP server calls
  through a unified HTTP gateway, enabling centralized management, logging, and
  authentication for MCP tools." The feature is marked as Experimental and
  requires `features: mcp-gateway: true` in the frontmatter.
- **Confidence**: emerging (first-party documentation; the experimental label
  signals potential instability — configuration schema may change)
- **Quote**: "The MCP Gateway routes all MCP server calls through a unified HTTP
  gateway, enabling centralized management, logging, and authentication for MCP
  tools."
- **Our assessment**: The MCP Gateway is architecturally distinct from the individual
  MCP server configuration documented in `docs-ghaw-mcps.md`. That note covers how
  to declare individual servers (stdio, Docker, HTTP, registry) with per-server
  `allowed:` filtering and authentication. The MCP Gateway here is a routing layer
  above the individual servers — a single HTTP proxy through which all MCP traffic
  passes, enabling fleet-level logging and centralized auth enforcement. The
  `api-key:` field in `sandbox.mcp` suggests the gateway itself authenticates
  callers, adding an auth layer above the per-server auth patterns in `docs-ghaw-mcps.md`.
  For Ch04 (Tool Use — MCP Gateway configuration): this is the first corpus
  documentation of the MCP Gateway as a routing primitive. The experimental status
  warrants caution for production workflows; monitor for stability changes. For Ch02:
  document MCP Gateway as an advanced centralization pattern for teams operating
  many MCP servers that benefit from unified observability.

### Claim 10: The `timeout-minutes` frontmatter field sets maximum wall-clock time for the entire agent job — default is 20 minutes; GitHub Actions enforces a hard upper limit of 360 minutes (6 hours)

- **Evidence**: The page states: "The `timeout-minutes` frontmatter field sets the
  maximum wall-clock time for the entire agent job. The default is 20 minutes."
  and "GitHub Actions enforces a hard upper limit of 360 minutes (6 hours) for a
  single job."
- **Confidence**: settled (first-party documentation; the default value and hard
  limit are platform specifications)
- **Quote**: "The `timeout-minutes` frontmatter field sets the maximum wall-clock
  time for the entire agent job. The default is 20 minutes."
- **Our assessment**: The 20-minute default is intentionally conservative — it is
  appropriate for lightweight workflows (scripts, docs, fast builds) but will
  terminate agent jobs that involve compilation, test execution, or large dependency
  installs without explicit override. The 360-minute hard limit is a GitHub Actions
  platform constraint, not a gh-aw-specific one. Practitioners who need jobs longer
  than 6 hours must architect multi-job pipelines rather than single long-running
  agent jobs. For Ch02: `timeout-minutes` is the single most important long-build
  configuration — the 20-minute default will silently kill many real-world build
  tasks. Document it alongside `tools.timeout` (per-tool-call) and `stop-after`
  (scheduled deadline) as the three distinct timeout controls for agent job duration.

### Claim 11: The sandbox reference provides a four-category repository-type recommendation table for `timeout-minutes` values based on typical build times

- **Evidence**: The page includes a table with four repository types mapped to
  typical build time ranges and suggested `timeout-minutes` values:
  Small (scripts, docs) → <2 min build → 20 (default);
  Medium (Go, Python, Node) → 2–10 min → 30–60;
  Large (C++, Rust, Java monorepo) → 10–30 min → 60–120;
  Very large (distributed, full CI) → >30 min → 120–360.
- **Confidence**: settled (first-party documentation; the table is prescriptive
  guidance from the platform team with specific values)
- **Quote**: (no single prose quote; see table in Concrete Artifacts)
- **Our assessment**: The four-category table is the most prescriptive
  `timeout-minutes` guidance in the corpus. The language breakdown in the Medium
  category (Go, Python, Node) is notable — these are the three most common gh-aw
  workflow languages, and their 2-10 minute build time range suggests the 30-60
  minute budget window is the practical default for most teams. C++ and Rust in the
  Large category (10-30 minutes) reflect the longer compile times that often catch
  practitioners off-guard. For Ch02: include this table as a harness engineer's
  quick-reference for `timeout-minutes` selection. This is the first corpus source
  with explicit per-language-ecosystem timeout guidance.

### Claim 12: `timeout-minutes` accepts GitHub Actions expressions and can be parameterized in reusable workflows using `workflow_call` inputs, enabling caller-configurable timeout budgets

- **Evidence**: The page shows a `workflow_call` example with a `job-timeout`
  input of type `number` with a default of 60, consumed as
  `timeout-minutes: ${{ inputs.job-timeout }}`.
- **Confidence**: settled (first-party documentation; the expression syntax example
  is explicit)
- **Quote**: (no direct prose quote; see YAML in Concrete Artifacts)
- **Our assessment**: The expression syntax enables shared workflow templates where
  the calling workflow controls the timeout budget rather than the template author.
  This is consistent with `docs-ghaw-tools-reference.md` Claim 8 (tools.timeout
  also accepts GitHub Actions expressions). Together, the two timeout fields
  (`timeout-minutes` and `tools.timeout`) support fully parameterizable timeout
  configuration in reusable workflow libraries — a team can maintain one workflow
  template that accommodates both fast CI environments and slow monorepo builds
  by accepting caller-provided budgets. For Ch02: document expression syntax for
  `timeout-minutes` alongside the static value examples; this is the pattern for
  shared workflow libraries that serve multiple repository sizes.

### Claim 13: Build artifact caching via `actions/cache` in a `jobs.setup` block pre-caches build artifacts across agent runs — the agent job picks them up transparently, reducing effective build time

- **Evidence**: The page provides a concrete Gradle caching example using
  `actions/cache@v4` in a `jobs.setup` block with `path: ~/.gradle/caches` and
  `build/`, plus `key: gradle-${{ hashFiles('**/*.gradle*') }}` and
  `restore-keys: gradle-`. A pre-build step (`./gradlew build -x test --parallel`)
  runs before the agent, so the agent finds cached artifacts.
- **Confidence**: settled (first-party documentation; the pattern is explicitly
  shown with a concrete example)
- **Quote**: (no direct prose quote; see YAML artifact in Concrete Artifacts)
- **Our assessment**: The `jobs.setup` block runs before the agent and is the
  correct place for expensive, repeatable preparation — dependency installation,
  compilation, test fixture setup. Using `actions/cache` in `jobs.setup` means the
  agent job starts with artifacts already built, so its `timeout-minutes` budget
  is spent on reasoning and code changes rather than compilation. The Gradle example
  is representative — the same pattern applies to any build system with a
  cache-key-deterministic artifact graph (Maven, Cargo, pip with requirements lock,
  npm with lockfile). For Ch02: document the `jobs.setup` + `actions/cache` pattern
  as the standard approach for long-build workflows. The alternative (letting the
  agent run the build inside its tool budget) is wasteful — every tool call that
  triggers a full build repeats the compilation cost. For Ch03: caching build
  artifacts also improves reproducibility — cached builds are deterministic with
  respect to the cache key, reducing variance in agent behavior across runs.

### Claim 14: Self-hosted runners (`runs-on: [self-hosted, linux, x64, large]`) are recommended for builds exceeding 10 minutes on standard runners, providing dedicated hardware without shared-resource contention

- **Evidence**: The page states: "For builds exceeding 10 minutes on standard
  runners:" and shows a `runs-on: [self-hosted, linux, x64, large]` example.
- **Confidence**: settled (first-party documentation; the 10-minute threshold
  and the YAML example are explicit)
- **Quote**: (no direct prose quote; see YAML in Concrete Artifacts)
- **Our assessment**: The 10-minute self-hosted runner threshold is consistent with
  the repository-type table (Claim 11) where Large repositories have 10-30 minute
  builds — the recommendation aligns: Large+ builds warrant self-hosted hardware.
  Standard GitHub-hosted runners have limited CPU cores and shared I/O, which
  amplifies build times for compilation-heavy workloads. Self-hosted runners with
  more cores (`x64, large`) can reduce C++ or Rust compile times to within the
  standard timeout budget, deferring the need to raise `timeout-minutes` to extreme
  values. For Ch02: the 10-minute threshold is the practical trigger for evaluating
  self-hosted runners; document it alongside the `timeout-minutes` guidance as a
  complementary strategy. The two approaches are not mutually exclusive: a large
  monorepo may need both higher `timeout-minutes` and self-hosted hardware.

## Concrete Artifacts

### Sandbox Configuration: AWF Default and Variants

```yaml
# Default (AWF enabled) — same as omitting sandbox: entirely
sandbox:
  agent: awf

# Disable agent firewall only (keep MCP Gateway enabled):
sandbox:
  agent: false

# Combined: AWF + network controls
sandbox:
  agent: awf
network:
  firewall: true
  allowed:
    - defaults
    - python
    - "api.example.com"
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Coding Agent Sandbox section*

### MCP Gateway Configuration (Experimental)

```yaml
features:
  mcp-gateway: true

sandbox:
  mcp:
    port: 8080
    api-key: "${{ secrets.MCP_GATEWAY_API_KEY }}"
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — MCP Gateway section*

### Filesystem Access Table (verbatim from source)

```
| Path Type      | Mode       | Examples                                  |
|----------------|------------|-------------------------------------------|
| User paths     | Read-write | $HOME, $GITHUB_WORKSPACE, /tmp            |
| System paths   | Read-only  | /usr, /opt, /bin, /lib                    |
| Docker socket  | Hidden     | /var/run/docker.sock (security)           |
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Filesystem Access table*

### Runtime Tools Setup (Setup Actions with AWF PATH Preservation)

```yaml
---
jobs:
  setup:
    steps:
      - uses: actions/setup-go@v5
        with:
          go-version: '1.25'
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
---
Use `go build` or `python3` - both are available.
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Runtime Tools Example.
AWF captures PATH after setup steps and restores it inside the container via AWF_HOST_PATH.*

### Timeout Configuration: Job-Level and Per-Tool

```yaml
---
on: issues
timeout-minutes: 60   # 60-minute budget for the entire agent job
---
Fix the failing test in the C++ core library.
```

```yaml
tools:
  timeout: 600   # 10 minutes per tool call (seconds)
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Job Timeout and Per-Tool-Call Timeout sections*

### Repository Type Timeout Recommendations (verbatim table from source)

```
| Repository Type                      | Typical Build Time | Suggested timeout-minutes |
|--------------------------------------|--------------------|--------------------------|
| Small (scripts, docs)                | < 2 min            | 20 (default)             |
| Medium (Go, Python, Node)            | 2–10 min           | 30–60                    |
| Large (C++, Rust, Java monorepo)     | 10–30 min          | 60–120                   |
| Very large (distributed, full CI)    | > 30 min           | 120–360                  |

Hard limit: 360 minutes (6 hours) — enforced by GitHub Actions.
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Repository Type Recommendations table*

### Parameterized Timeout for Reusable Workflows

```yaml
on:
  workflow_call:
    inputs:
      job-timeout:
        type: number
        default: 60

---
timeout-minutes: ${{ inputs.job-timeout }}
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Per-Tool-Call Timeout section (expressions example)*

### Concrete C++ Long-Build Example (verbatim from source)

```yaml
---
on:
  issues:
    types: [opened, labeled]

engine: copilot
runs-on: [self-hosted, linux, x64, large]
timeout-minutes: 30

tools:
  bash: [":*"]
  timeout: 300   # 5-minute per-tool-call budget

network:
  allowed:
    - defaults
    - go
    - node
---
Reproduce the bug described in this issue, add a regression test, and fix it.
Build with `cmake --build build -j$(nproc)` and verify with `ctest --output-on-failure`.
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Concrete C++ Example*

### Build Artifact Caching via `jobs.setup` (Gradle Example)

```yaml
---
on: issues
timeout-minutes: 30

jobs:
  setup:
    steps:
      - uses: actions/cache@v4
        with:
          path: |
            ~/.gradle/caches
            build/
          key: gradle-${{ hashFiles('**/*.gradle*') }}
          restore-keys: gradle-
      - run: ./gradlew build -x test --parallel
---
Review the failing tests and apply a fix. Build artifacts are pre-cached.
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Build Artifact Caching Strategy section*

### Self-Hosted Runner Configuration

```yaml
---
on: issues
runs-on: [self-hosted, linux, x64, large]
timeout-minutes: 30
---
Run the full test suite and fix any failures.
```

*Source: `https://github.github.com/gh-aw/reference/sandbox` — Self-Hosted Runners section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth pipeline,
    Layer 2: Runtime Isolation): AWF is the concrete implementation of that layer.
    The how-they-work note names "runtime isolation" as a security layer without
    specifying its mechanism; this reference names it as AWF with filesystem tiers,
    Docker socket hiding, and environment variable sandboxing.
  - `docs-ghaw-network-reference.md` Claim 8 (all AI engines use the same AWF
    with identical network configuration syntax): This note corroborates that AWF
    is engine-agnostic and adds the non-network dimensions of the AWF sandbox
    (filesystem access, environment variable handling) that the network reference
    omits.
  - `docs-ghaw-tools-reference.md` Claim 8 (two timeout parameters: `tools.timeout`
    with Claude 60s/Codex 120s defaults, and `tools.startup-timeout` at 120s):
    This note corroborates the per-tool-call timeout mechanism and adds the job-level
    `timeout-minutes` complement. Both notes together give the complete timeout
    surface for gh-aw workflows.
  - `docs-ghaw-rate-limiting-controls.md` (mentions `timeout-minutes: 20` default
    and 360-minute cap): This note corroborates those values and adds the repository-type
    recommendation table that contextualizes when to raise the default.

- **Extends**:
  - `docs-ghaw-network-reference.md`: That note documents the network egress
    dimension of AWF comprehensively. This note extends the AWF picture to its
    non-network dimensions: three-tier filesystem access model, Docker socket
    hiding, `--env-all` environment passing, and `AWF_HOST_PATH` PATH restoration.
    Together the two notes give the complete AWF security model.
  - `docs-ghaw-mcps.md`: That note covers how to declare and configure individual
    MCP servers (four types, `allowed:` filtering, OIDC auth). This note adds the
    MCP Gateway as a routing layer above those individual server declarations —
    the Gateway is a centralized proxy through which all MCP calls flow, enabling
    fleet-level observability and authentication not available at the per-server level.
  - `docs-ghaw-rate-limiting-controls.md`: That note documents `timeout-minutes`
    alongside `rate-limit`, `stop-after`, and `safe-outputs.assign-to-agent.max`
    as rate controls. This note extends the `timeout-minutes` guidance specifically
    for long-build contexts: the repository-type table, the artifact caching strategy,
    and the self-hosted runner threshold are not covered in the rate-limiting note.
  - `docs-ghaw-how-they-work.md` Claims 4 and 3 (zero capability by default; five-layer
    security pipeline): This reference provides the configuration-level implementation
    of Layer 2 (Runtime Isolation) that how-they-work describes only conceptually.

- **Contradicts**: None identified. No existing source note makes claims that conflict
  with the AWF sandbox model, the filesystem access tiers, the Docker socket behavior,
  or the timeout defaults. The Docker socket hiding is consistent with (and complementary
  to) the Docker MCP server type in `docs-ghaw-mcps.md` — the MCP Docker server
  type launches containers as MCP server processes (before the agent runs, as part of
  the harness), not as agent-issued Docker commands (which would be blocked by the
  hidden socket). These are different actors at different points in the workflow
  lifecycle; no contradiction. No contradiction issue filed.

- **Novel** (what this note adds that no prior source covers):
  - **Filesystem access tier model for AWF** (Claim 4): No existing source note
    documents the three-tier filesystem access model (user read-write, system
    read-only, Docker socket hidden). `docs-ghaw-how-they-work.md` names runtime
    isolation as a security layer; this is the first specification of what that
    isolation enforces at the filesystem level.
  - **Docker socket hiding as a privilege escalation countermeasure** (Claim 5):
    The explicit "Agents cannot spawn containers" prohibition and its security
    rationale are entirely new to the corpus.
  - **AWF environment variable handling: `--env-all` and `AWF_HOST_PATH`** (Claim 7):
    The specific mechanism by which AWF preserves setup-action-modified `PATH`
    across the sandbox boundary is not documented in any existing source note.
    This resolves a common confusion for practitioners debugging tool availability.
  - **Go `GOROOT` automatic capture** (Claim 8): The Go-specific AWF behavior
    (capturing `GOROOT` after `actions/setup-go`) is a platform implementation
    detail not documented anywhere in the corpus.
  - **MCP Gateway as an experimental HTTP routing layer** (Claim 9): While
    `docs-ghaw-mcps.md` documents individual MCP server configuration, the MCP
    Gateway as a centralized routing proxy with its own `sandbox.mcp.port` and
    `api-key` configuration is entirely new to the corpus. These are different
    levels of the MCP stack.
  - **Repository-type timeout recommendation table** (Claim 11): The four-category
    table (Small/Medium/Large/Very large with specific `timeout-minutes` ranges)
    is the most prescriptive timeout guidance in the corpus. No other source provides
    language-ecosystem-specific timeout recommendations.
  - **`jobs.setup` + `actions/cache` as the build artifact caching pattern** (Claim 13):
    The specific strategy of pre-caching build artifacts in a setup job so the agent
    finds them ready is not documented in any existing source note.
  - **10-minute self-hosted runner trigger threshold** (Claim 14): The explicit
    threshold (builds >10 minutes → consider self-hosted runners) is not stated
    in any existing source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add AWF sandbox as the complete runtime isolation specification** (Claims 1–8):
  Currently, the corpus has the conceptual description (how-they-work) and the
  network dimension (network-reference) but not the full sandbox model. Ch02 should
  add: (1) the `sandbox:` field as a two-sub-field configuration (`agent` + `mcp`),
  (2) the filesystem access table, (3) Docker socket hiding as a named constraint,
  (4) `--env-all` + `AWF_HOST_PATH` as the environment bridge, (5) Go GOROOT as
  a known edge case handled transparently. Together these give harness engineers
  the complete picture of what the AWF sandbox does and does not restrict.

- **Add MCP Gateway as an advanced centralization pattern** (Claim 9): Document
  the MCP Gateway as a routing layer above individual MCP server declarations,
  useful for teams that operate many servers and want unified observability or
  centralized authentication. Note its experimental status.

- **Add `timeout-minutes` configuration guidance with the repository-type table**
  (Claims 10–12): The 20-minute default will kill most real-world build workflows.
  Publish the four-category table (Small → 20 / Medium → 30-60 / Large → 60-120 /
  Very large → 120-360) as a harness engineering quick-reference. Add expression
  syntax for reusable workflow templates.

- **Add `jobs.setup` + `actions/cache` as the standard long-build pattern** (Claim 13):
  For workflows with build times >2 minutes, pre-caching artifacts in the setup
  job is the recommended approach. This extends `timeout-minutes` budget for
  the agent's actual reasoning task rather than build overhead.

- **Add self-hosted runner guidance with the 10-minute threshold** (Claim 14):
  For Large and Very large repository types (Claim 11), self-hosted runners reduce
  compile times and reduce the need for extreme `timeout-minutes` values.

### Chapter 03: Safety and Verification

- **Add the AWF filesystem tier model to Layer 2 (Runtime Isolation)** (Claim 4):
  The five-layer security model in `docs-ghaw-how-they-work.md` names Layer 2 as
  "runtime isolation." Ch03 should expand that with the three-tier table: user paths
  (read-write), system paths (read-only), Docker socket (hidden). Each tier has
  a distinct threat it addresses.

- **Name Docker socket hiding explicitly as a privilege escalation countermeasure**
  (Claim 5): This belongs in Ch03's security model alongside network egress controls
  and permission separation. The specific threat (recursive container creation as
  a sandbox escape) should be named.

- **Document `sandbox.agent: false` as a security downgrade requiring justification**
  (Claim 3): Ch03 should note that disabling the AWF firewall removes network egress
  control and weakens filesystem isolation. Teams should have explicit architecture
  justification (e.g., restricted network at runner level) before using this flag.

### Chapter 04: Tool Use / MCP Gateway Configuration

- **Add MCP Gateway as the first entry point for the MCP Gateway sub-topic** (Claim 9):
  The triage comment identifies this as a Ch04 relevance. MCP Gateway centralizes
  MCP routing — document it as the fleet-level routing pattern that complements
  per-server `allowed:` filtering from `docs-ghaw-mcps.md`.

## Extraction Notes

1. **Source access via WebFetch AI model**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch returns rendered text processed through an AI model.
   Two fetch passes were made with different prompts to maximize verbatim coverage.
   Technical content (YAML field names, table values, specific CLI flags like
   `--env-all` and `AWF_HOST_PATH`) is assessed as accurate — these are technical
   strings unlikely to be mistranslated. Prose quotes are marked verbatim where
   returned consistently across both fetches.

2. **Filesystem access table confirmed verbatim**: The three-row table (User paths /
   System paths / Docker socket) appeared identically across both fetch passes. The
   column values (Read-write / Read-only / Hidden) and the specific path examples
   are assessed as accurate.

3. **MCP Gateway experimental status**: The page marks MCP Gateway as "(Experimental)".
   This label is not defined further on the page — it is unclear whether experimental
   means "in preview with breaking changes possible" or "opt-in with stable API."
   Confidence for MCP Gateway claims is downgraded to emerging accordingly.

4. **`tools.timeout` engine defaults confirmed from separate source**: The
   per-tool-call timeout defaults (Claude 60s, Codex 120s) appear in both this
   sandbox reference and `docs-ghaw-tools-reference.md` Claim 8, which extracted
   them verbatim from the tools reference page. The sandbox page cites these values
   in passing; the tools-reference note is the primary source for the full
   `tools.timeout` + `tools.startup-timeout` specification.

5. **No contradictions filed**: Reviewed all existing corpus source notes.
   No claims in this source materially oppose any existing source note at the
   MINER.md §4a filing threshold. The Docker MCP server type in `docs-ghaw-mcps.md`
   (which runs containers as MCP servers) is not contradicted by the Docker socket
   hiding (Claim 5) — these operate at different workflow lifecycle stages (setup
   vs. agent execution). No contradiction issue required.

6. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   the current gh-aw platform state as of 2026-05-12.

7. **Related documentation followed selectively**: The page references: Network
   Permissions, AI Engines, Tools, Self-Hosted Runners, Frontmatter Reference.
   The network reference is already in the corpus (`docs-ghaw-network-reference.md`).
   The tools reference is already in the corpus (`docs-ghaw-tools-reference.md`).
   Self-hosted runners documentation was not separately fetched as the sandbox page
   provides the key threshold (10 minutes) and YAML example sufficient for
   cross-referencing.
