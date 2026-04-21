---
source_url: https://github.github.com/gh-aw/blog/2026-04-20-weekly-update/
source_type: blog-post
title: "Weekly Update – April 20, 2026 (GitHub Agentic Workflows)"
author: Copilot (on behalf of GitHub Agentic Workflows team, gh-aw)
date_published: 2026-04-20
date_extracted: 2026-04-21
last_checked: 2026-04-21
status: current
confidence_overall: emerging
issue: "#290"
---

# Weekly Update – April 20, 2026 (GitHub Agentic Workflows)

> Five releases (v0.68.3–v0.68.7, April 14–17, 2026) deliver four high-novelty
> patterns: (1) `cache-memory` working-tree sanitization as an explicit
> supply-chain attack-surface acknowledgment — the first in the gh-aw corpus;
> (2) OpenCode as a fourth agentic engine option alongside Copilot, Claude, and
> Codex; (3) Time Between Turns (TBT) as the first prompt-caching effectiveness
> metric exposed by the CLI; and (4) `pre-agent-steps` as a declarative
> pre-flight initialization field — relationship to the existing `pre-steps`
> field (v0.67.3) is unresolved and flagged for follow-up.

## Source Context

- **Type**: blog-post (weekly changelog/release update from the GitHub Agentic
  Workflows blog; covers five releases v0.68.3–v0.68.7 and an "Agent of the Week"
  spotlight on `auto-triage-issues`; post is authored by Copilot on behalf of the
  gh-aw team — itself an example of agentic content generation)
- **Author credibility**: The gh-aw blog is the official publication of GitHub's
  Agentic Workflows platform team (Don Syme, Peli de Halleux, Mara Kiefer — see
  `blog-gh-aw-operations-release-workflows.md` for author background). Weekly
  updates report on shipped releases with specific PR numbers. Security claims
  explicitly name the attack vector addressed. High credibility for claims about
  their own platform. The post is notably authored by Copilot, making it a
  first-party example of gh-aw dogfooding for content creation.
- **Scope**: Five releases across four days (April 14–17, 2026). Covers a new
  agentic engine (OpenCode), security hardening (`cache-memory` sanitization),
  observability (TBT metric), pre-flight orchestration (`pre-agent-steps`),
  BYOK/offline Copilot, MCP configuration migration, model failure handling,
  cross-repo CI regression detection, and MCP-as-local-CLI. Does NOT cover:
  exact syntax for `pre-agent-steps` beyond field name; whether `pre-agent-steps`
  replaces or complements `pre-steps`; the full list of file types sanitized
  by `cache-memory`; OpenCode configuration options; or the specific mechanism
  by which BYOK Copilot enables offline support.

## Extracted Claims

### Claim 1: `cache-memory` working-tree sanitization (v0.68.6) closes a supply-chain attack vector where cached memory could plant executables or disallowed files in the working tree between runs

- **Evidence**: Described in the v0.68.6 feature list: "Scans and cleans planted
  executables and disallowed files from cached memory before each agent run."
  The blog post's opening sentence frames the release as delivering "key security
  improvements." Multiple Prospector triage assessments independently identified
  this as the highest-novelty security claim in the release.
- **Confidence**: emerging (described by the gh-aw team as closing "a real
  supply-chain attack vector" — team-self-reported; no independent exploitation
  report or CVE; the threat model is plausible and explicitly acknowledged, which
  gives it more weight than a generic claim)
- **Quote**: "cache-memory working-tree sanitization: Scans and cleans planted
  executables and disallowed files from cached memory before each agent run"
- **Our assessment**: This is the first explicit acknowledgment in the gh-aw
  corpus — and in our full source corpus — that cached memory state is an attack
  surface for supply-chain attacks. The threat model: an adversary (or a
  compromised earlier run) plants executable files or configuration overrides in
  the cached memory that the agent workspace loads at startup. Without sanitization,
  each subsequent agent run executes in a workspace that may have been poisoned by
  a previous run or by persistent memory. The gh-aw team's explicit naming of this
  as "a real supply-chain attack vector" elevates it above a theoretical risk to an
  acknowledged, addressed vulnerability class. For Ch03 (Safety and Verification):
  any agentic harness that caches memory or working-tree state between runs must
  treat that cached state as potentially untrusted and sanitize before execution.
  The gh-aw model (scan-and-clean at startup, before the agent reads the workspace)
  is the correct architecture: trust the live workspace, not the persisted one.

### Claim 2: OpenCode is now a fourth agentic engine option alongside Copilot, Claude, and Codex, configurable via `engine: opencode` in workflow frontmatter (v0.68.6)

- **Evidence**: Listed as a major feature in v0.68.6: "Set `engine: opencode` to
  use OpenCode as agentic engine alongside Copilot, Claude, and Codex."
- **Confidence**: emerging (feature announced; no production usage patterns,
  performance data, or OpenCode-specific tooling in the corpus yet)
- **Quote**: "Set `engine: opencode` to use OpenCode as agentic engine alongside
  Copilot, Claude, and Codex."
- **Our assessment**: The addition of OpenCode matters for two reasons: (1) it
  confirms that gh-aw is explicitly multi-engine at the platform level — not
  converging on a single AI provider; (2) it updates the engine inventory from
  three engines (Copilot, Claude, Codex — as documented in `docs-ghaw-how-they-work.md`
  Claim 9 and the April 13 weekly note) to four. Practitioners reading the existing
  note on multi-engine configuration should be aware the engine list has expanded.
  For Ch02 (Harness Engineering): update the engine options table. The same-frontmatter
  portability claim holds: adding a new engine does not break existing workflow specs.

### Claim 3: The Time Between Turns (TBT) metric, now reported by `gh aw audit` and `gh aw logs`, is the first CLI-surfaced indicator of whether LLM prompt caching is working for a workflow (v0.68.3)

- **Evidence**: PR #26321, shipped in v0.68.3. The post states TBT is "a key
  indicator of whether LLM prompt caching is working for your workflows." The
  metric is described as appearing in both `gh aw audit` and `gh aw logs` output.
- **Confidence**: emerging (feature shipped and purpose-described; the causal
  mechanism between TBT and cache hit rate is stated but not quantified — no
  threshold values, no before/after comparison, no example TBT values are given)
- **Quote**: "Time Between Turns (TBT) metric: `gh aw audit` and `gh aw logs`
  now report TBT, indicating LLM prompt caching effectiveness."
- **Our assessment**: TBT is the first prompt-caching effectiveness metric
  exposed at the workflow level in our corpus. The rationale: when prompt caching
  is working, the LLM responds faster on cached turns (lower TBT); when caching
  is absent or cache misses dominate, TBT reflects cold-start latency. This gives
  workflow operators a concrete diagnostic signal without requiring them to
  instrument the LLM API directly. Combined with the per-tool-call metrics
  shipped in `blog-ghaw-weekly-2026-04-06.md` (v0.66.1), gh-aw now provides
  three observability axes: tool-call latency and token usage (v0.66.1), GitHub
  API quota per run (v0.67.0), and LLM-level turn latency (v0.68.3). For Ch02
  (observability section) and any future Ch04 section on multi-agent performance:
  TBT should be the first metric checked when diagnosing unexpected latency in
  agentic workflows — it separates caching-related slowness from agent reasoning
  slowness.

### Claim 4: `pre-agent-steps` (v0.68.6) is a new frontmatter field that runs custom GitHub Actions steps before the AI agent starts, intended for authentication, environment setup, and prerequisite initialization

- **Evidence**: Listed as a major feature in v0.68.6 with use cases: "authentication,
  environment setup, prerequisites." No PR number given. Named `pre-agent-steps`
  (hyphenated, distinct from `pre-steps`).
- **Confidence**: emerging (feature announced; syntax and semantics partially
  described; relationship to `pre-steps` from v0.67.3 is unresolved — see
  Extraction Notes)
- **Quote**: "New `pre-agent-steps` frontmatter field runs custom GitHub Actions
  before AI agent starts."
- **Our assessment**: `pre-agent-steps` enables declarative pre-flight
  initialization as a harness primitive. Instead of baking setup instructions
  into agent markdown (where the agent interprets them and may fail), operators
  can define deterministic setup steps in YAML frontmatter that run before the
  AI agent starts. This separates the orchestration concern (what the harness
  sets up) from the intelligence concern (what the agent does). For Ch02
  (Harness Engineering): `pre-agent-steps` is the gh-aw-native solution for
  authentication, environment setup, and prerequisite initialization. IMPORTANT:
  the April 13 note (`blog-ghaw-weekly-2026-04-13.md` Claim 2) documents a
  `pre-steps` field (v0.67.3) with overlapping semantics (in-job token minting
  before checkout). These may be the same field renamed, complementary fields
  (different execution phases), or parallel features for different use cases.
  The guide should not merge these claims until the relationship is verified
  against current gh-aw documentation.

### Claim 5: Model-not-supported detection (v0.68.3) surfaces a clear error and stops retrying when a requested model is unavailable for a workflow plan

- **Evidence**: PR #26229, shipped in v0.68.3. Prior behavior (implicit): workflow
  would retry indefinitely when the requested model was unavailable. Post-fix
  behavior: clear error is surfaced and retrying stops.
- **Confidence**: emerging (fix described with specific symptom addressed; prior
  failure mode — infinite retry — is inferred from the fix description, not
  directly quoted)
- **Quote**: "Model-not-supported detection: When a model is unavailable, workflow
  surfaces clear error instead of infinite retry."
- **Our assessment**: Infinite retry on model unavailability is a silent resource
  sink: a workflow that cannot start because its requested model is absent will
  consume runner minutes indefinitely with no useful output and no actionable
  error. This is the same failure class as the Copilot CLI v1.0.22 hang documented
  in `blog-ghaw-weekly-2026-04-13.md` Claim 9 (zero-output / hang on engine
  misconfiguration), but for model availability specifically. For Ch02 (Harness
  Engineering): harness configurations should explicitly handle model-unavailability
  as a distinct failure mode. The fix moves this from a silent loop to a detectable
  error, enabling alert-on-error harness patterns. For Ch03: zero-output with
  infinite-retry is a diagnostic signature for engine/model configuration failure
  — not agent misbehavior.

### Claim 6: A daily Claude workflow (v0.68.7) auto-discovers repositories using gh-aw and runs compile checks against the latest build, catching cross-repo compatibility regressions before they reach users

- **Evidence**: PR #26802, shipped in v0.68.7. Described as a cross-repo
  compatibility check that auto-discovers gh-aw repositories and runs `gh aw compile`
  against the latest build on a daily schedule.
- **Confidence**: emerging (feature announced; specifics of repository discovery
  mechanism and failure handling are not described)
- **Quote**: "Cross-repo compatibility checks (PR #26802): Daily Claude workflow
  auto-discovers repositories using gh-aw and runs compile checks against latest
  build."
- **Our assessment**: This is a meta-CI pattern: using a Claude agent to validate
  the CI harness for the Claude/Copilot agent platform itself. The daily compile-check
  across all consuming repositories is a form of integration testing for platform
  changes before they break users downstream. It also demonstrates a use case for
  Claude as a CI component (not just a code-writing assistant) — the agent's task
  here is repository discovery and compile validation, both well-defined and
  verifiable. For Ch02: this is a novel CI meta-pattern — agentic regression
  detection across a repository ecosystem for a shared platform. It addresses a
  gap that static CI pipelines cannot fill: a single repository's CI cannot detect
  whether changes to a shared dependency break consumers in other repositories.

### Claim 7: BYOK Copilot mode (v0.68.4, `byok-copilot` feature flag) enables offline Copilot support by wiring bring-your-own-key access

- **Evidence**: PR #26544, shipped in v0.68.4 under a feature flag (`byok-copilot`).
  Described as enabling "offline Copilot support." No further technical detail is
  given in the post.
- **Confidence**: anecdotal (feature flag implies not yet GA; mechanism and
  security implications of BYOK are not described in the post)
- **Quote**: "BYOK Copilot mode (PR #26544): New feature flag enables offline
  Copilot support."
- **Our assessment**: BYOK for Copilot represents a new deployment topology: teams
  that cannot or will not connect to GitHub's Copilot service directly can wire
  their own key. This is relevant for enterprise deployments with network
  restrictions or for teams that want to use a Copilot-compatible API endpoint
  from a different provider. Being behind a feature flag suggests it is not
  production-ready; treat this as a roadmap signal rather than a deployable
  pattern. For Ch02: note the topology option exists; recommend waiting for GA
  before adopting in production.

### Claim 8: The MCP server configuration path changed from `.mcp.json` (repo root) to `.github/mcp.json` (v0.68.5, PR #26665), aligning with GitHub conventions; the init flow creates the new path

- **Evidence**: PR #26665, shipped in v0.68.5. Described as "aligning with GitHub
  conventions." The `init` flow creates the new path automatically.
- **Confidence**: settled (a specific, verifiable configuration change with a
  clear rationale)
- **Quote**: "MCP config location changed from `.mcp.json` (repo root) to
  `.github/mcp.json`, aligning with GitHub conventions."
- **Our assessment**: This is a migration-impacting change for any team with an
  existing `.mcp.json` at the repo root. The move to `.github/` aligns with
  GitHub's convention of placing workflow-related configuration under `.github/`
  (alongside `.github/workflows/`, `.github/CODEOWNERS`, etc.), making MCP
  configuration more discoverable in repository structure. For Ch02: teams
  migrating to v0.68.5+ must move `.mcp.json` to `.github/mcp.json`. New
  installs via `gh aw init` get the correct path automatically.

### Claim 9: MCP servers can now mount as local CLI commands in the agent environment after the MCP gateway starts (v0.68.4, PR #25928)

- **Evidence**: PR #25928, shipped in v0.68.4. Described as "MCP servers can
  mount as local CLI commands after gateway starts."
- **Confidence**: emerging (feature described at the concept level; what "mount
  as local CLI" means in terms of command syntax, path conventions, or security
  implications is not specified)
- **Quote**: "MCP servers as local CLIs (PR #25928): MCP servers can mount as
  local CLI commands after gateway starts."
- **Our assessment**: If MCP servers can present as local CLI commands, an agent
  can invoke MCP tools using shell command syntax rather than MCP protocol calls —
  this lowers the cognitive overhead of tool invocation in agent instructions and
  enables MCP-backed tools to appear natively in shell-based workflows. This could
  also be a security surface: a compromised MCP server that mounts as a local
  CLI could be invoked by any process in the agent environment, not just the AI
  agent. For Ch02: this is a new tool-integration surface worth documenting once
  the mechanism is clearer. For Ch03: the security implications of MCP-as-local-CLI
  should be verified before recommending this pattern.

### Claim 10: The `auto-triage-issues` agent demonstrates a graceful degradation pattern: when an integrity policy filters an issue before the agent reads it, the agent skips labeling, creates a summary discussion, and alerts maintainers (rather than failing silently or erroring)

- **Evidence**: "Agent of the Week" spotlight. The post describes two behaviors:
  (1) normal path — Issue #27290 was triaged and labeled `compiler` in 24 seconds;
  (2) integrity-policy-filtered path — agent skips labeling action, creates a
  summary discussion, alerts maintainers. Both behaviors are confirmed production
  observations.
- **Confidence**: anecdotal (one agent, observed in production; the graceful
  degradation path is described but the trigger frequency is unknown)
- **Quote**: "Behavior when integrity policy filters issues: skips labeling,
  creates summary discussion, alerts maintainers"
- **Our assessment**: The 24-second labeling time is a concrete latency benchmark
  for a simple classification task (single-label issue triage). More importantly,
  the integrity-policy fallback is an example of "leave a breadcrumb when you
  cannot act" — a safety pattern worth naming. An agent that silently skips filtered
  issues would leave maintainers with no visibility into why certain issues were
  not processed. Creating a summary discussion makes the skipped action visible
  and auditable. For Ch03 (Safety and Verification): agents operating under policy
  constraints should always emit a visible artifact when they cannot complete their
  task — the absence of action should be explicit, not implicit. For Ch01 (Daily
  Workflows): 24 seconds for single-issue triage is a practical latency benchmark
  for always-on classification agents.

## Concrete Artifacts

### Version Summary: v0.68.3–v0.68.7 (April 14–17, 2026)

```
v0.68.7 (April 17) — CI Meta-Pattern + QoL:
  - New: on.roles single-string support — roles: write accepted alongside
         roles: [write] (PR #26789)
  - Fix: Codex chroot — runtime state uses /tmp on restricted filesystems
         (PR #26787)
  - New: Cross-repo compatibility checks — daily Claude workflow discovers
         gh-aw repos and runs compile checks against latest build (PR #26802)

v0.68.6 (April 17) — New Engine + Security + Pre-flight Initialization:
  - New: OpenCode engine — engine: opencode (fourth engine option)
  - New: engine.bare mode — engine.bare: true skips AGENTS.md loading
         (for triage, reporting, ops workflows; see also v0.68.1 in
          blog-ghaw-weekly-2026-04-13.md)
  - New: pre-agent-steps — frontmatter field for custom GitHub Actions
         steps before AI agent starts (auth, env setup, prerequisites)
  - Security: cache-memory working-tree sanitization — scans and cleans
              planted executables and disallowed files before each agent run

v0.68.5 (April 16) — Configuration + Reliability:
  - Breaking: MCP config path: .mcp.json → .github/mcp.json (PR #26665)
  - New: shared/reporting-otlp.md import bundle (PR #26655)
  - Fix: environment: frontmatter now correctly propagates to activation job
         (PR #26650)

v0.68.4 (April 16) — BYOK + MCP Integration:
  - New (feature flag): byok-copilot — offline Copilot with bring-your-own-key
                        (PR #26544)
  - New: SideRepoOps maintenance workflow — compiler auto-generates
         agentics-maintenance.yml for target repos (PR #26382)
  - New: MCP servers mountable as local CLI commands after gateway starts
         (PR #25928)
  - Closes 21 community-reported issues

v0.68.3 (April 14) — Observability + Reliability:
  - New: Model-not-supported detection — clear error instead of infinite retry
         when requested model is unavailable (PR #26229)
  - New: Time Between Turns (TBT) metric in gh aw audit and gh aw logs —
         indicates LLM prompt caching effectiveness (PR #26321)
  - New: env and checkout fields in shared imports (PRs #26113, #26292)
```

### Time Between Turns (TBT) — Observability Signal for Prompt Caching

```
Metric:  Time Between Turns (TBT)
Where:   gh aw audit  /  gh aw logs  (v0.68.3, PR #26321)
Purpose: Indicates whether LLM prompt caching is working for a workflow.

Interpretation:
  Low TBT  → cache hits are reducing LLM response latency per turn
  High TBT → cache misses or caching disabled; each turn starts cold

Relationship to existing observability stack (gh-aw):
  Tool-call metrics (latency, token usage, failure counts) → v0.66.1
  GitHub API quota per run and per resource                → v0.67.0
  OTel distributed traces (cross-job span hierarchy)       → v0.67.1 / v0.68.0
  Time Between Turns (LLM-level caching signal)            → v0.68.3  ← new

Diagnostic use: check TBT first when diagnosing unexpected workflow latency.
If TBT is high, caching configuration is the bottleneck; if TBT is normal,
look at tool-call latency or OTel spans for the slowdown.
```

### `pre-agent-steps` — Pre-flight Initialization Field

```yaml
# In a gh-aw workflow spec (.md frontmatter):
pre-agent-steps:
  - name: Configure environment
    uses: actions/some-setup@v1
    with:
      token: ${{ secrets.SETUP_TOKEN }}
  # Steps run as custom GitHub Actions before the AI agent starts.
  # Use cases: authentication, environment setup, prerequisites.
  # v0.68.6

# CAUTION: Relationship to pre-steps (v0.67.3) is unresolved.
# pre-steps (April 13 note): runs before checkout and agent, in same job
#   — specifically designed for in-job token minting (octo-sts, create-github-app-token)
# pre-agent-steps (this note): runs before AI agent starts
#   — authentication, environment setup, prerequisites
# These may be the same field renamed, complementary fields, or parallel features.
# Verify against current gh-aw documentation before using both in the same workflow.
```

### OpenCode Engine — Frontmatter Configuration

```yaml
# In a gh-aw workflow spec (.md frontmatter):
engine: opencode
# Alternatives: copilot (default), claude, codex, opencode
# Same workflow structure and MCP tool protocol works across all engines.
# v0.68.6
```

### `cache-memory` Sanitization — Threat Model

```
Attack vector (now mitigated):
  1. Adversary or compromised run plants executable in working-tree via
     cached memory (e.g., a malicious AGENTS.md entry referencing a planted binary,
     or a cached file that overrides a trusted tool path)
  2. Next agent run loads cached working-tree state
  3. Agent executes in poisoned workspace

Mitigation (v0.68.6):
  Before each agent run:
    → scan working tree for planted executables and disallowed files
       sourced from cached memory
    → remove any found
    → agent starts in a clean workspace

Classification: supply-chain attack via persistent cached state.
Team's framing: "closes a real supply-chain attack vector"
Confidence: emerging — acknowledged by gh-aw team; no independent exploitation.
```

### MCP Config Migration (v0.68.5)

```
Before v0.68.5:  .mcp.json  (repository root)
After  v0.68.5:  .github/mcp.json  (PR #26665)

Migration: move file manually or re-run `gh aw init` (creates new path).
Rationale: alignment with GitHub's .github/ convention for workflow config.
```

### Agent of the Week: auto-triage-issues Performance Data

```
Agent:    auto-triage-issues
Function: Reads every unlabeled issue, applies correct labels on a schedule.
Period:   Week of April 20, 2026

Normal path:
  Issue #27290: labeled `compiler` in 24 seconds

Graceful degradation path (integrity policy filtering):
  Trigger:  Integrity policy filters an issue before agent reads it
  Behavior: (1) skip labeling action
            (2) create summary discussion documenting the skip
            (3) alert maintainers
  Pattern:  "leave a breadcrumb when you cannot act"

Usage recommendation: pair with `notify` workflow on high-priority labels
(security, breaking-change) for team notification.
```

## Cross-References

- **Corroborates**:
  - `blog-ghaw-weekly-2026-04-06.md` Claim 3 (OTLP payload sanitization for
    exfiltration prevention) and Claim 9 (observability agent meta-failure): The
    `cache-memory` supply-chain sanitization (Claim 1 here) is a further instance
    of the gh-aw team's systematic attack-surface hardening campaign. March 31–
    April 6: secrets interpolation and OTLP exfiltration. April 6–10 (weekly-04-13):
    log file permissions and heredoc injection. April 14–17 (this note): cached
    memory as a working-tree attack surface. Together these document a progression
    from credential-leakage hardening to memory-persistence attack hardening.
  - `blog-ghaw-weekly-2026-04-13.md` Claim 9 (Copilot CLI v1.0.22 hang / zero-
    output failure): Model-not-supported detection (Claim 5 here) is the same
    failure class — an engine configuration problem that produces a silent or
    spinning failure instead of an actionable error — applied to model availability
    rather than CLI version incompatibility. The fix pattern is the same: surface
    a clear error, stop retrying.
  - `blog-ghaw-agent-observability.md` Claim 4 ("chatty LLM calling invisible
    without instrumentation") and `blog-ghaw-weekly-2026-04-06.md` Claim 7
    (per-tool-call metrics): The TBT metric (Claim 3 here) extends the gh-aw
    observability stack with a new LLM-level signal. All three sources converge
    on the same principle: workflow cost and performance problems are invisible
    without purpose-built instrumentation at the right granularity.
  - `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support as a first-class
    design): OpenCode joining Copilot, Claude, and Codex (Claim 2 here) confirms
    and extends the multi-engine architecture. That note documented three engines;
    this release adds a fourth.
  - `blog-ghaw-weekly-2026-04-13.md` Claim 10 (`auto-triage-issues` 100% coverage
    rate): The Agent of the Week data here (Claim 10) extends the same agent's
    performance picture. April 13: coverage metric (100% label coverage, 4 labels
    in single pass). April 20: latency benchmark (24s per issue) and graceful
    degradation path. Together: a more complete operational profile of the agent.

- **Extends**:
  - `blog-ghaw-weekly-2026-04-06.md` Claim 1 (OTLP tracing) and `blog-ghaw-
    weekly-2026-04-13.md` Claim 5 (cross-job parent span propagation via
    `aw_context`): The `shared/reporting-otlp.md` import bundle (v0.68.5) further
    operationalizes the distributed tracing stack by packaging the two OTel imports
    into a single import. The observability onboarding path now has three levels:
    manual `observability.otlp` block (April 6), cross-job span propagation
    (April 13), and a bundled import for full reporting pipelines (this note).
  - `blog-ghaw-weekly-2026-04-13.md` Claim 1 (`engine.bare: true` context
    suppression, v0.68.1): The April 20 post re-describes `engine.bare` in v0.68.6.
    The April 13 note covers the original introduction and the full suppression
    semantics (AGENTS.md + user instructions + CLAUDE.md); the April 20 post
    highlights it alongside OpenCode. Whether v0.68.6 expands `engine.bare`
    semantics (e.g., to cover OpenCode's context system) or simply re-describes
    the v0.68.1 feature is unresolved. The full semantics should be read from
    the April 13 note until verified otherwise.
  - `blog-ghaw-weekly-2026-04-13.md` Claim 2 (`pre-steps` in-job token minting):
    `pre-agent-steps` (Claim 4 here) occupies overlapping semantic territory.
    The April 13 note covers `pre-steps` (v0.67.3); this post covers `pre-agent-steps`
    (v0.68.6). See Extraction Notes for the unresolved question about their
    relationship.

- **Contradicts**: None filed. No existing source note makes claims that are
  materially opposed by this release. The `pre-agent-steps` / `pre-steps` name
  discrepancy is flagged as an unresolved question, not a contradiction: both
  could coexist as separate features. The `engine.bare` re-appearance in v0.68.6
  is consistent with the April 13 note; no semantic contradiction.

- **Novel**:
  - **`cache-memory` supply-chain attack acknowledgment** (Claim 1): First source
    in the corpus to explicitly name cached working-tree state as a supply-chain
    attack vector in an agentic harness, with a mitigation strategy. No prior note
    addresses cached memory as a persistence-based attack surface.
  - **OpenCode as fourth agentic engine** (Claim 2): First appearance of OpenCode
    in the corpus. Prior engine coverage: Copilot, Claude, Codex. Now four options.
  - **Time Between Turns (TBT) metric** (Claim 3): First prompt-caching
    effectiveness metric exposed at the workflow CLI level in the corpus. Prior
    observability coverage (tool-call metrics, OTel spans, GitHub API quota) does
    not include LLM-level caching signals.
  - **Model-not-supported detection** (Claim 5): First documented fix for infinite-
    retry-on-model-unavailability in the corpus. Extends the engine-error-handling
    picture beyond CLI version pinning (April 13 note) to model availability.
  - **Cross-repo Claude CI agent** (Claim 6): First example in the corpus of a
    Claude agent used as a daily cross-ecosystem CI regression detector for a
    shared platform. The pattern (agent discovers consuming repositories and
    validates them against the platform's latest build) is novel.
  - **BYOK Copilot topology** (Claim 7): First appearance of bring-your-own-key
    for Copilot as a deployment topology. No prior note covers offline or BYOK
    Copilot configurations.
  - **`pre-agent-steps` pre-flight initialization primitive** (Claim 4): First
    description of a declarative pre-agent initialization field in this release
    cycle; relationship to `pre-steps` unresolved but the use-case framing
    (authentication, environment setup) is incrementally more explicit than the
    April 13 `pre-steps` description (focused on token minting).
  - **Graceful degradation breadcrumb pattern** (Claim 10): First corpus source
    to document an explicit "skip + summarize + alert" pattern for policy-filtered
    agent tasks. Prior failure-mode coverage documents failures; this documents the
    correct non-failure response to a constrained execution path.

## Guide Impact

- **Chapter 03 (Safety and Verification)**:
  - Add `cache-memory` supply-chain attack as a named threat model for agentic
    harnesses that persist memory or working-tree state between runs. Frame: any
    persistent state that the agent workspace loads at startup is a trust boundary.
    The gh-aw mitigation (scan-and-clean before agent starts) is the reference
    pattern. Cross-reference `blog-ghaw-weekly-2026-04-13.md` Claims 3 and 4 (log
    file hardening, heredoc injection) as a hardening cluster spanning three release
    cycles.
  - Add "leave a breadcrumb when you cannot act" as a named design pattern for
    agents operating under integrity policy or permission constraints. The `auto-
    triage-issues` behavior (skip + summary discussion + alert) is the concrete
    reference. Contrast with silent failure, which leaves no audit trail. Cite
    Claim 10.
  - Add model-not-supported detection as a harness error-handling pattern: surfacing
    a clear error and stopping retry when the configured model is unavailable. Pair
    with the Copilot CLI regression case (April 13 note, Claim 9) as two failure
    modes in the same category: engine/model configuration failures should produce
    actionable errors, not silent hangs or infinite loops.

- **Chapter 02 (Harness Engineering)**:
  - Update the engine options inventory: Copilot, Claude, Codex, OpenCode. The
    multi-engine design (`engine:` frontmatter field) means existing workflow specs
    remain portable. Cite `docs-ghaw-how-they-work.md` as the base reference;
    this note as the source for OpenCode addition.
  - Add TBT as a first-line diagnostic for workflow latency. Recommended diagnostic
    sequence: check TBT first (caching) → tool-call latency (v0.66.1 metrics) →
    OTel spans (cross-job trace hierarchy). Frame TBT as the LLM-level caching
    signal in the observability stack.
  - Add `.mcp.json` → `.github/mcp.json` migration note for teams on v0.68.4 or
    earlier. New installs use new path automatically. Existing installs must migrate
    manually.
  - Add `pre-agent-steps` as a declarative pre-flight initialization pattern;
    note the unresolved relationship with `pre-steps` and recommend verification
    before using both in the same workflow.
  - Add cross-repo CI agent (Claim 6) as a novel CI meta-pattern: using Claude to
    run daily compile validation across all repositories consuming a shared
    platform. Frame as applicable when a team maintains a tool or library used by
    many repositories and needs regression detection that per-repo CI cannot provide.

- **Chapter 01 (Daily Workflows)**:
  - Add 24-second issue triage latency as a concrete latency benchmark for
    well-scoped classification agents. Pair with `blog-ghaw-weekly-2026-04-13.md`
    Claim 10 (100% label coverage) to give a two-dimensional quality picture for
    `auto-triage-issues`: coverage (accuracy proxy) + latency (throughput signal).

## Extraction Notes

1. **Source depth**: Weekly changelog post covering five releases. Content is
   structured as bullet summaries with feature flags and PR numbers. "Agent of the
   Week" section is brief but provides concrete behavioral examples. Ten claims
   extracted; no substantive content skipped.

2. **`pre-steps` vs. `pre-agent-steps` unresolved**: The April 13 note documents
   `pre-steps` (v0.67.3) for in-job token minting before checkout. This post
   documents `pre-agent-steps` (v0.68.6) for pre-flight initialization. Version
   numbers differ by three releases (v0.67.3 vs. v0.68.6). Both describe steps
   running within the same job before the agent. Use cases overlap (authentication
   is cited for both). Possible explanations: (a) `pre-steps` was renamed to
   `pre-agent-steps`; (b) they are separate fields with different execution
   phases (pre-checkout vs. pre-agent-start); (c) `pre-agent-steps` is an expanded
   version with additional capabilities. The Prospector's triage specifically flagged
   this discrepancy for the Miner. A contradiction issue was NOT filed because no
   source makes a mutually exclusive claim — the ambiguity is about naming and
   scope, not about conflicting guidance. Verify against current gh-aw documentation
   before merging these claims in the guide.

3. **`engine.bare` re-described in v0.68.6**: The April 13 note introduced
   `engine.bare: true` (v0.68.1, PR #25661) with full semantics (suppresses
   AGENTS.md, user instructions, CLAUDE.md). This post lists `engine.bare` again
   under v0.68.6 features. The post's description ("skip loading AGENTS.md for
   triage, reporting, and ops workflows") is a simplified re-description, not a
   semantic expansion. This note does not re-extract `engine.bare` as a novel
   claim; the authoritative extraction remains in `blog-ghaw-weekly-2026-04-13.md`
   Claim 1.

4. **Multiple concurrent Prospector triage comments**: Three independent triage
   passes all converged on the same high-priority claims (`cache-memory`
   sanitization, OpenCode, TBT, `pre-agent-steps`). Convergence across independent
   passes increases confidence in claim selection.

5. **Registry left unchanged**: `registry/sources.json` is in minimal/stub state
   (`{"sources": {}, "last_updated": null}`). No entry added per instructions for
   minimal registry state.

6. **No contradictions filed**: Reviewed all existing source notes with gh-aw
   coverage (`blog-ghaw-weekly-2026-03-23.md`, `blog-ghaw-weekly-2026-03-30.md`,
   `blog-ghaw-weekly-2026-04-06.md`, `blog-ghaw-weekly-2026-04-13.md`,
   `blog-ghaw-agent-observability.md`, `blog-gh-aw-operations-release-workflows.md`,
   `docs-ghaw-how-they-work.md`). No existing claim materially opposes any claim
   in this source. The `pre-steps` / `pre-agent-steps` discrepancy does not meet
   the §4a filing threshold because it is a naming ambiguity, not conflicting
   guidance on what to do.
