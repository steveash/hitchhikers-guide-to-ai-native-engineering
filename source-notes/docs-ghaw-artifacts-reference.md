---
source_url: https://github.github.com/gh-aw/reference/artifacts
source_type: docs
title: "GitHub Agentic Workflows: Artifacts Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#449"
---

# GitHub Agentic Workflows: Artifacts Reference

> The authoritative artifact taxonomy for gh-aw — defines 9 named artifacts
> (7 current + 2 legacy) tracked via typed constants, documents the critical
> separation of token usage data into `firewall-audit-logs` rather than `agent`,
> describes per-artifact directory structure and file contents, and covers
> backward-compatibility naming, hash-prefix handling for `workflow_call`
> invocations, schema versioning via `_schema` fields, and selective download
> via `--artifacts` flag.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/artifacts` page — in
  the "Reference" section, distinct from the `introduction/` conceptual pages and
  `guides/` practitioner pages. Reference pages document platform behavior
  authoritatively; this one is the canonical taxonomy for all artifacts produced
  during gh-aw workflow execution.)
- **Author credibility**: First-party from GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — the same team behind Peli de Halleux's agent factory
  blog series and the `gh aw` CLI). Artifact names, file paths, and download syntax
  are platform specifications; constant identifiers (e.g., `constants.AgentArtifactName`)
  confirm these are stable, typed references in the platform codebase.
- **Scope**: The complete artifact taxonomy for gh-aw workflows — all 9 named
  artifacts with their type (single-file / multi-file), contents, directory structure,
  legacy names, `workflow_call` hash-prefix handling, JSONL schema versioning, and
  selective download CLI syntax. Does NOT cover: the overall job lifecycle that
  produces these artifacts (see `docs-ghaw-compilation-process.md`), network
  configuration of the AWF firewall whose logs appear in `firewall-audit-logs` (see
  `docs-ghaw-network-reference.md`), the Safe Outputs specification that produces
  `agent_output.json` inside `agent` (see `docs-ghaw-safe-outputs-specification.md`),
  or the debugging methodology using these artifacts (see
  `docs-ghaw-troubleshooting-debugging.md`).

## Extracted Claims

### Claim 1: The gh-aw platform defines 9 named artifacts tracked via typed constants — 7 current and 2 legacy — providing stable, versioned identifiers for all workflow execution outputs

- **Evidence**: The reference page presents a table mapping each artifact name to
  its constant identifier (e.g., `constants.AgentArtifactName`, `constants.FirewallAuditArtifactName`),
  type (multi-file or single-file), and purpose. The constant identifiers signal that
  artifact names are stable, typed platform references, not ad-hoc strings.
- **Confidence**: settled (first-party reference documentation; the constant
  identifiers confirm these are authoritative platform names)
- **Quote**: (no direct prose quote; the table of artifact names, constants, types,
  and purposes is the evidence — see Concrete Artifacts)
- **Our assessment**: The 9-artifact taxonomy is more complete than any prior source
  note's description of gh-aw artifacts. Two additions are new to the corpus:
  `safe-outputs-items` (safe output manifest, single-file) and `code-scanning-sarif`
  (SARIF scan results, single-file). The constant identifiers are architecturally
  significant: artifact names are stable platform identifiers, not documentation
  labels. Tooling that reads gh-aw artifacts should use the constant values, not
  hardcoded strings, to remain resilient to name changes. For Ch02 (Harness
  Engineering): document the complete artifact taxonomy as the reference for
  teams building downstream tooling (cost dashboards, compliance readers, analysis
  pipelines).

### Claim 2: Token usage data (`token-usage.jsonl`) lives in `firewall-audit-logs/api-proxy-logs/`, NOT in the `agent` artifact — downloading `agent` to find token data silently returns no data

- **Evidence**: The documentation explicitly calls out this as a documented common
  error: "Downstream workflows sometimes download `agent-artifacts` or `agent`
  expecting to find `token-usage.jsonl`. This will silently return no data — the
  token usage file is only in the `firewall-audit-logs` artifact."
- **Confidence**: settled (first-party; the artifact is explicitly named and the
  common error is directly documented)
- **Quote**: "This artifact is **separate** from the `agent` artifact. Token usage
  data (`token-usage.jsonl`) lives here, not in the `agent` artifact."
- **Our assessment**: This is the highest-value operational claim in the note.
  The separation of token usage data from the agent artifact is non-obvious — the
  agent job produces both, and practitioners building cost dashboards or token
  accounting workflows naturally reach for the `agent` artifact. The silent
  failure (download succeeds but returns no `token-usage.jsonl`) makes this error
  particularly insidious. The reason for the separation is architectural: token
  usage is firewall-level telemetry (recorded by the AWF proxy as it intercepts
  API calls), not agent-level output. For Ch02: add a prominent callout when
  documenting artifact access for cost observability — direct practitioners to
  `firewall-audit-logs` for `token-usage.jsonl`. Cross-reference with
  `docs-ghaw-compilation-process.md` Claim 9 (which lists `firewall-audit-logs`
  as the token/network audit artifact) and `blog-ghaw-agent-observability.md`
  (Portfolio Analyst reads token usage to detect overuse).

### Claim 3: The `agent` artifact is multi-file and contains execution logs, structured safe output data (`agent_output.json`), GitHub API rate limits (`github_rate_limits.jsonl`), a token usage summary (`agent_usage.json`), and optional telemetry files

- **Evidence**: The reference describes the `agent` artifact's contents:
  "Agent execution logs, safe output data (`agent_output.json`), GitHub API rate
  limits (`github_rate_limits.jsonl`), token usage summary (`agent_usage.json`),
  and optional telemetry files (`otel.jsonl`, `copilot-otel.jsonl`)."
- **Confidence**: settled (first-party; file names within the artifact are
  explicitly listed)
- **Quote**: (no direct prose quote capturing the full contents list; file names
  are enumerated in the artifact table — see Concrete Artifacts)
- **Our assessment**: The distinction between `agent_usage.json` (aggregated
  summary, inside `agent`) and `token-usage.jsonl` (per-request detail, inside
  `firewall-audit-logs`) is architecturally important. Cost dashboards that
  need totals can use `agent_usage.json` from the `agent` artifact; compliance
  tools that need per-request breakdowns (with cache hit/miss analysis) need
  `firewall-audit-logs`. The optional OpenTelemetry files (`otel.jsonl`,
  `copilot-otel.jsonl`) are new to the corpus — they suggest gh-aw generates
  OTel-compatible telemetry for integration with existing observability stacks.
  For Ch04 (observability): document `otel.jsonl` as the integration point for
  teams with existing OTel-based observability infrastructure.

### Claim 4: The `firewall-audit-logs` artifact has a structured four-item directory layout — `api-proxy-logs/token-usage.jsonl` (token metrics), `squid-logs/access.log` (network decisions), `audit.jsonl` (firewall trail), and `policy-manifest.json` (config snapshot)

- **Evidence**: The reference documents the exact directory structure:
  ```
  firewall-audit-logs/
  ├── api-proxy-logs/token-usage.jsonl
  ├── squid-logs/access.log
  ├── audit.jsonl
  └── policy-manifest.json
  ```
  Each item's purpose is described: token usage (input/output/cache tokens per API
  request), network policy decisions, firewall audit trail, and policy configuration
  snapshot.
- **Confidence**: settled (first-party; directory structure is explicitly documented)
- **Quote**: "Token usage data (input/output/cache tokens per API request)"
- **Our assessment**: The four-file structure of `firewall-audit-logs` maps to four
  distinct use cases: (1) `api-proxy-logs/token-usage.jsonl` → cost accounting
  and token efficiency analysis; (2) `squid-logs/access.log` → network audit
  (which domains were accessed or blocked); (3) `audit.jsonl` → compliance
  reporting of firewall actions; (4) `policy-manifest.json` → configuration
  snapshot for change management. The `squid-logs/access.log` path here reconciles
  with `docs-ghaw-troubleshooting-debugging.md` Claim 11, which references firewall
  logs at `sandbox/firewall/logs/access.log` — the latter is the runtime container
  path; `squid-logs/access.log` is the path within the downloaded artifact. Both
  refer to the same squid proxy access log. For Ch02: document all four files with
  their specific use cases when practitioners need to build observability tooling.

### Claim 5: The `activation` artifact is multi-file and contains the engine configuration (`aw_info.json`), the generated prompt (`prompt.txt`), and rate limit data from the activation phase

- **Evidence**: The reference documents: "Configuration file (`aw_info.json`),
  generated prompt (`prompt.txt`), and rate limit data from activation phase
  (`github_rate_limits.jsonl`)."
- **Confidence**: settled (first-party; file names within the artifact are
  explicitly listed)
- **Quote**: (no direct prose quote; file contents are listed in the artifact table)
- **Our assessment**: The `activation` artifact stores the generated prompt (`prompt.txt`)
  rather than the `agent` artifact, which makes architectural sense: the prompt
  is assembled in the activation phase before the agent runs. `docs-ghaw-compilation-process.md`
  Claim 9 listed `prompt.txt` among the agent job's outputs without specifying which
  artifact it belongs to; this reference clarifies it resides in `activation`. For
  Ch02: direct practitioners to `activation/prompt.txt` (not `agent/prompt.txt`)
  when debugging "what did the agent receive?" questions. The `aw_info.json`
  configuration snapshot is also useful for confirming which engine version ran.

### Claim 6: The `experiment` artifact is only present when workflows declare A/B experiments in frontmatter — it stores per-variant invocation counters for load balancing across runs

- **Evidence**: The reference states the artifact contains a `state.json` file with
  "per-variant invocation counters used to balance A/B assignments across runs" and
  is "Present only when experiments declared in frontmatter."
- **Confidence**: settled (first-party; the conditionality and file purpose are
  explicitly stated)
- **Quote**: (no direct prose quote; presence condition and file purpose described
  in the artifact table)
- **Our assessment**: The `experiment` artifact is the persistence mechanism for
  gh-aw's A/B experiment state. By storing cumulative variant counts in an artifact
  (rather than in-memory state), the platform can balance variant assignment across
  runs without requiring a persistent database. Each run reads the current counters,
  determines which variant has fewer invocations, and updates the state. This is a
  stateless-storage pattern for variant load balancing. For Ch02: when documenting
  A/B experiment configuration, note that the `experiment` artifact appears only in
  experimental workflows and must be considered when auditing artifact retention.

### Claim 7: Two legacy artifact names (`safe-output` and `agent-output`) are preserved for backward compatibility; pre-v5 artifact names are automatically mapped to v5 naming by the CLI

- **Evidence**: The reference lists `safe-output` (constant: `constants.SafeOutputArtifactName`)
  and `agent-output` (constant: `constants.AgentOutputArtifactName`) as legacy artifacts.
  The backward compatibility section states: "Pre-v5 artifact names (`aw_info.json`,
  `safe_output.jsonl`, `threat-detection.log`) are automatically mapped to v5 naming."
- **Confidence**: settled (first-party; legacy names and v5 mapping are explicitly
  documented)
- **Quote**: "Pre-v5 artifact names (`aw_info.json`, `safe_output.jsonl`,
  `threat-detection.log`) are automatically mapped to v5 naming."
- **Our assessment**: The legacy artifact names are important for teams operating
  gh-aw workflows that predated v5. Old downstream tooling that downloads `safe-output`
  or `agent-output` will continue to work without modification. The automatic pre-v5
  mapping means even older filename conventions (`safe_output.jsonl` with underscore,
  `threat-detection.log`) are handled transparently. For Ch02: when documenting
  artifact access, note that teams migrating from pre-v5 configurations do not need
  to update downstream artifact consumers — the CLI handles the renaming automatically.

### Claim 8: When gh-aw workflows are invoked via `workflow_call`, GitHub prepends hash prefixes to artifact names (e.g., `abc123-firewall-audit-logs`), which the CLI recognizes and handles automatically

- **Evidence**: The reference documents: "When invoked via `workflow_call`, GitHub
  prepends hash prefixes (e.g., `abc123-firewall-audit-logs`), which the CLI
  recognizes automatically."
- **Confidence**: settled (first-party; the hash-prefix behavior and automatic
  handling are explicitly documented)
- **Quote**: "When invoked via `workflow_call`, GitHub prepends hash prefixes
  (e.g., `abc123-firewall-audit-logs`), which the CLI recognizes automatically."
- **Our assessment**: The hash-prefix behavior is a GitHub Actions platform behavior
  (not gh-aw-specific) that affects all artifact uploads within `workflow_call`
  contexts. The gh-aw CLI absorbs this complexity so practitioners can use the
  canonical artifact names (`firewall-audit-logs`, `agent`, etc.) regardless of
  invocation context. Without this handling, teams using `call-workflow` or
  `workflow_call` to compose gh-aw workflows would need to discover and strip the
  hash prefix themselves when downloading artifacts. For Ch02: when documenting
  artifact access for `call-workflow` compositions (see
  `docs-ghaw-orchestration-patterns.md`), note that the CLI handles the prefix
  transparently — practitioners should use canonical names in all contexts.

### Claim 9: JSONL records in `firewall-audit-logs` include a `_schema` field referencing versioned JSON schemas from the `github/gh-aw-firewall` repository — consumers should match by prefix for non-breaking updates

- **Evidence**: The reference documents: "JSONL records include `_schema` fields
  referencing versioned JSON schemas from the `github/gh-aw-firewall` repository,
  enabling consumers to validate record formats across AWF releases." The schema
  field value format is illustrated as `"audit/v0.26.0"`.
- **Confidence**: settled (first-party; the `_schema` field and versioning convention
  are explicitly documented)
- **Quote**: "Records include `_schema` field (e.g., `\"audit/v0.26.0\"`). Match
  by prefix for non-breaking updates."
- **Our assessment**: The `_schema` versioning mechanism is the contract between
  gh-aw and downstream tooling that consumes `firewall-audit-logs`. Consumers
  that validate against the full version string (`"audit/v0.26.0"`) will break on
  patch updates; consumers that match by prefix (`"audit/"`) remain compatible across
  non-breaking changes. This is a standard schema-versioning pattern for append-only
  log formats. The `github/gh-aw-firewall` repository is where the JSON schemas are
  hosted — teams building compliance tooling that validates JSONL records can
  reference these schemas directly. For Ch02: when documenting `firewall-audit-logs`
  consumption, note the `_schema` field and recommend prefix-matching as the resilient
  parsing strategy.

### Claim 10: Artifacts can be selectively downloaded using `--artifacts` flags with named sets: `firewall`, `agent`, `detection`, `experiment`, and `github-api` are documented download targets

- **Evidence**: The reference documents download syntax:
  ```bash
  gh aw logs <run-id> --artifacts firewall
  gh aw logs <run-id> --artifacts agent --artifacts detection
  gh aw audit <run-id> --artifacts experiment
  ```
  Multiple `--artifacts` flags can be combined for selective multi-artifact downloads.
- **Confidence**: settled (first-party; CLI syntax is explicitly documented)
- **Quote**: (no direct prose quote; CLI commands are the evidence — see Concrete Artifacts)
- **Our assessment**: Selective download is the ergonomics improvement over
  `gh run download` (which downloads all artifacts). Cost observability workflows
  only need `--artifacts firewall`; debugging workflows may need `--artifacts agent
  --artifacts detection`. The named sets abstract over the artifact constant names,
  making CLI commands more memorable. For Ch02: prefer `gh aw logs --artifacts` over
  `gh run download` when building targeted artifact access into observability or
  debugging workflows — selective download reduces artifact transfer overhead in
  automation scripts.

### Claim 11: `safe-outputs-items` is a single-file artifact containing the safe output manifest — a typed constant (`constants.SafeOutputItemsArtifactName`) confirms its platform status

- **Evidence**: The reference table lists `safe-outputs-items` as a single-file
  artifact with constant `constants.SafeOutputItemsArtifactName` and purpose
  "Safe output manifest." No prior source note documents this artifact.
- **Confidence**: emerging (first-party reference; the artifact is listed but its
  exact contents and use cases are not elaborated in the reference text returned)
- **Quote**: (no direct prose quote; artifact table entry is the evidence)
- **Our assessment**: The `safe-outputs-items` artifact likely contains a manifest
  of the safe output operations declared and/or executed in a run — a structured
  index used by the Safe Output Processor (Component C3 in the Safe Outputs
  specification). This would complement `agent_output.json` inside `agent` (which
  contains the structured safe output data itself). Practitioners building audit
  tooling that needs to enumerate which safe output operations a run attempted
  should investigate this artifact. For Ch02: note this artifact exists alongside
  the `agent` artifact for safe-output-related auditing.

### Claim 12: `code-scanning-sarif` is a single-file artifact containing SARIF scan results — enables integration of gh-aw agent-generated code scans with GitHub's code scanning infrastructure

- **Evidence**: The reference table lists `code-scanning-sarif` as a single-file
  artifact with constant `constants.SarifArtifactName` and purpose "SARIF scan
  results." No prior source note documents this artifact.
- **Confidence**: emerging (first-party reference; the artifact is listed but the
  source text returned does not elaborate on when it is produced or by which job)
- **Quote**: (no direct prose quote; artifact table entry is the evidence)
- **Our assessment**: SARIF (Static Analysis Results Interchange Format) is the
  GitHub standard for code scanning results. The presence of a `code-scanning-sarif`
  artifact in the gh-aw taxonomy suggests gh-aw can produce agent-generated SARIF
  output for upload to GitHub Code Scanning — enabling AI-detected issues to appear
  in the Security tab of a repository. This is a novel integration point not
  documented in any prior gh-aw source note. For Ch04 (Building Agents): the
  `code-scanning-sarif` artifact is the mechanism by which gh-aw workflows
  contribute to GitHub's native security reporting infrastructure.

## Concrete Artifacts

### Complete Artifact Taxonomy (from source reference table)

```
Artifact Name          | Constant                              | Type        | Purpose
-----------------------|---------------------------------------|-------------|---------------------------
agent                  | constants.AgentArtifactName           | Multi-file  | Unified agent job outputs
activation             | constants.ActivationArtifactName      | Multi-file  | Activation job data
firewall-audit-logs    | constants.FirewallAuditArtifactName   | Multi-file  | AWF firewall logs
detection              | constants.DetectionArtifactName       | Single-file | Threat detection output
experiment             | constants.ExperimentArtifactName      | Multi-file  | A/B experiment state
safe-outputs-items     | constants.SafeOutputItemsArtifactName | Single-file | Safe output manifest
code-scanning-sarif    | constants.SarifArtifactName           | Single-file | SARIF scan results
safe-output            | constants.SafeOutputArtifactName      | Legacy      | Historical safe output
agent-output           | constants.AgentOutputArtifactName     | Legacy      | Historical agent output
```

*Source: GitHub Agentic Workflows reference/artifacts, artifact taxonomy table*

### Per-Artifact File Contents

```
agent (multi-file):
  ├── agent_output.json          — structured safe output data (create_issue, add_comment, etc.)
  ├── github_rate_limits.jsonl   — GitHub API rate limit data
  ├── agent_usage.json           — aggregated token usage summary
  ├── otel.jsonl                 — OpenTelemetry telemetry (optional)
  └── copilot-otel.jsonl         — Copilot-specific OTel telemetry (optional)

firewall-audit-logs (multi-file):
  ├── api-proxy-logs/
  │   └── token-usage.jsonl      — per-request token data (input/output/cache tokens)
  ├── squid-logs/
  │   └── access.log             — network policy decisions (TCP_TUNNEL / DENIED)
  ├── audit.jsonl                — firewall audit trail
  └── policy-manifest.json       — policy configuration snapshot

activation (multi-file):
  ├── aw_info.json               — engine configuration
  ├── prompt.txt                 — generated prompt sent to AI agent
  └── github_rate_limits.jsonl   — rate limit data from activation phase

detection (single-file):
  └── detection.log              — threat detection analysis results

experiment (multi-file, conditional):
  └── state.json                 — per-variant invocation counters for A/B load balancing
                                   (only present when experiments declared in frontmatter)
```

*Source: GitHub Agentic Workflows reference/artifacts, per-artifact contents sections*

### Critical Separation: Token Data Location

```
WRONG: gh run download --name agent          # agent_usage.json is here (SUMMARY only)
                                              # token-usage.jsonl is NOT here

RIGHT: gh aw logs <run-id> --artifacts firewall
       # Downloads firewall-audit-logs containing:
       # api-proxy-logs/token-usage.jsonl  ← per-request token detail
```

*Source: GitHub Agentic Workflows reference/artifacts, firewall-audit-logs section.
Documented common error: "Downstream workflows sometimes download `agent-artifacts`
or `agent` expecting to find `token-usage.jsonl`. This will silently return no
data — the token usage file is only in the `firewall-audit-logs` artifact."*

### Selective Download CLI Syntax

```bash
# Download firewall logs only (for cost/network analysis)
gh aw logs <run-id> --artifacts firewall

# Download agent and detection artifacts
gh aw logs <run-id> --artifacts agent --artifacts detection

# Download experiment artifact (only useful when workflow uses A/B experiments)
gh aw audit <run-id> --artifacts experiment
```

*Source: GitHub Agentic Workflows reference/artifacts, download syntax section*

### JSONL Schema Versioning Pattern

```json
// Example record from audit.jsonl inside firewall-audit-logs:
{ "_schema": "audit/v0.26.0", ... }

// Consumer matching strategy:
// BAD:  if record["_schema"] == "audit/v0.26.0"  → breaks on patch updates
// GOOD: if record["_schema"].startswith("audit/") → survives non-breaking updates

// Schema definitions hosted at: github/gh-aw-firewall repository
```

*Source: GitHub Agentic Workflows reference/artifacts, schema versioning section*

### Backward Compatibility: Pre-v5 Name Mapping

```
Pre-v5 filename       → v5 artifact location
aw_info.json          → activation/aw_info.json
safe_output.jsonl     → agent/agent_output.json (inside agent artifact)
threat-detection.log  → detection/detection.log (inside detection artifact)

workflow_call prefix handling:
  GitHub prepends hash → e.g., abc123-firewall-audit-logs
  CLI strips prefix automatically → use canonical names regardless of context
```

*Source: GitHub Agentic Workflows reference/artifacts, backward compatibility section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 9 ("The agent job produces five artifact
    types: `agent_output.json`, `agent_usage.json`, `prompt.txt`, `firewall-audit-logs`,
    and `cache-memory/`"): this reference corroborates the separation of `firewall-audit-logs`
    as distinct from the `agent` artifact. The compilation process note listed them as
    separate outputs of the agent job; this reference provides the authoritative artifact
    containers they reside in. The main extension: this reference clarifies that `prompt.txt`
    lives in `activation` (not `agent`), and adds 4 previously undocumented artifacts
    (`experiment`, `safe-outputs-items`, `code-scanning-sarif`, plus legacy names).
  - `docs-ghaw-network-reference.md` Claim 9 ("AWF firewall supports configurable log
    levels... The firewall logs feed into the `firewall-audit-logs` artifact"): the network
    reference identifies `firewall-audit-logs` as the destination for AWF logs; this
    artifacts reference provides the complete internal structure (`api-proxy-logs/`,
    `squid-logs/`, `audit.jsonl`, `policy-manifest.json`) and confirms the separation from
    `agent`. Both sources are consistent; this reference provides the artifact internals that
    the network reference lacks.
  - `docs-ghaw-safe-outputs-specification.md` Claim 3 (AR2: "Agent-to-processor communication
    MUST occur through GitHub Actions artifact storage"): this artifacts reference is the
    inventory of the GitHub Actions artifacts that implement AR2. The `agent` artifact
    (containing `agent_output.json`) is the NDJSON communication channel between the agent
    job (Component C2) and the Safe Output Processor (Component C3) described in the spec.
    Both sources are consistent; this reference makes AR2 concrete by naming the artifact.

- **Extends**:
  - `docs-ghaw-troubleshooting-debugging.md` Claim 11 (firewall logs at `sandbox/firewall/logs/access.log`)
    and Claim 12 (four artifact types for debugging): this reference extends both claims with
    the canonical artifact taxonomy. The `sandbox/firewall/logs/access.log` runtime path
    referenced in the debugging note corresponds to `squid-logs/access.log` within the
    downloaded `firewall-audit-logs` artifact — the same log, accessed via different paths
    (runtime container path vs. downloaded artifact path). The four artifacts listed in the
    debugging note (`prompt.txt`, `agent_output.json`, `agent-stdio.log`, `firewall-logs/`)
    are now mapped to their canonical artifact containers by this reference.
  - `blog-ghaw-agent-observability.md` Claim 4 ("Cost optimization agents can identify
    unnecessarily expensive LLM calling patterns" — Portfolio Analyst reads token data):
    this reference identifies the specific artifact (`firewall-audit-logs/api-proxy-logs/token-usage.jsonl`)
    that the Portfolio Analyst and similar cost-analysis workflows must download. The
    observability blog showed the use case; this reference provides the artifact name and path.
  - `docs-ghaw-safe-outputs-specification.md` Claim 2 (three-component architecture: Workflow
    Compiler, MCP Gateway Server, Safe Output Processor): this reference extends by showing
    the artifacts each phase produces — `activation` from the activation job (pre-agent),
    `agent` from the agent job (Component C2 → C3 handoff), and the safe output execution
    artifacts.

- **Contradicts**: None identified. The `prompt.txt` location (compilation process note
  lists it among agent job outputs; this reference places it in `activation`) is a
  clarification, not a contradiction — the compilation process note described files produced
  during the workflow without specifying artifact container names. No existing source note
  makes claims that materially oppose the artifact taxonomy, the firewall-audit-logs
  separation, or the backward compatibility model. No contradiction issue filed.

- **Novel** (what this note adds to the corpus that no prior source covers):
  - **Complete 9-artifact taxonomy with typed constants**: Prior notes mention specific
    artifacts (`agent`, `firewall-audit-logs`, `prompt.txt`) in context; no prior note
    provides the full enumeration with constant identifiers. The constants confirm these
    are stable platform identifiers, not documentation labels.
  - **`safe-outputs-items` artifact**: Not mentioned in any existing source note. This
    single-file safe output manifest is a new artifact type in the corpus.
  - **`code-scanning-sarif` artifact**: Not mentioned in any existing source note. The
    ability to produce SARIF output from gh-aw workflows for GitHub Code Scanning
    integration is entirely new to the corpus.
  - **OpenTelemetry telemetry files in `agent`**: `otel.jsonl` and `copilot-otel.jsonl`
    as optional files inside the `agent` artifact are not documented in any prior note.
    This is the OTel integration point for gh-aw.
  - **Per-artifact internal directory structure**: The explicit file layout for each
    multi-file artifact (especially `firewall-audit-logs`'s four-item structure) is not
    documented in any prior source note at this level of specificity.
  - **Token usage: summary vs. detail split**: The distinction between `agent_usage.json`
    (aggregated, in `agent`) and `token-usage.jsonl` (per-request, in `firewall-audit-logs`)
    is not articulated in any prior note. The compilation process note mentions both
    without explaining they are in different artifacts.
  - **`workflow_call` hash-prefix handling**: The automatic stripping of GitHub-prepended
    hash prefixes in `workflow_call` invocations is not documented in any prior note.
  - **`_schema` versioning in JSONL records**: The schema versioning mechanism (with prefix-
    match recommendation) is not mentioned in any existing source note.
  - **Legacy artifact names with backward compatibility mapping**: The pre-v5 filename
    mapping is not documented in any prior note, including `docs-ghaw-compilation-process.md`.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the complete artifact taxonomy as a reference table** (Claim 1, Concrete
  Artifacts): Teams building gh-aw integration tooling need a complete inventory.
  Currently no guide chapter documents all 9 artifact names, their types, and
  purposes. The taxonomy table (with constant identifiers) is the definitive reference
  for downstream tooling authors.

- **Add a prominent callout: token usage data is in `firewall-audit-logs`, not `agent`**
  (Claim 2): The documented common error — silently downloading the wrong artifact for
  token data — warrants explicit guide coverage. Direct practitioners to
  `firewall-audit-logs/api-proxy-logs/token-usage.jsonl` for per-request token detail
  and `agent/agent_usage.json` for aggregated summaries. Pair with the Portfolio Analyst
  pattern from `blog-ghaw-agent-observability.md` Claim 4.

- **Document per-artifact file layouts** (Claims 3–6, Concrete Artifacts): The internal
  structure of each multi-file artifact determines how practitioners navigate and query
  them. For cost observability: `api-proxy-logs/token-usage.jsonl`. For network audit:
  `squid-logs/access.log`. For prompt debugging: `activation/prompt.txt` (not in `agent`).
  For A/B experiments: `experiment/state.json` (conditional on frontmatter).

- **Add selective download pattern using `--artifacts`** (Claim 10): Prefer
  `gh aw logs --artifacts firewall` over `gh run download` in automation scripts that
  need only specific artifacts. This reduces transfer overhead in CI and observability
  pipelines.

- **Document legacy and `workflow_call` compatibility** (Claims 7–8): Teams with pre-v5
  gh-aw configurations or `call-workflow` compositions need to know that artifact names
  are handled transparently by the CLI. No source change required when migrating from
  pre-v5 naming or composing workflows via `workflow_call`.

### Chapter 04: Building Agents

- **Add `code-scanning-sarif` as the SARIF integration artifact** (Claim 12): If gh-aw
  workflows generate code scanning results (e.g., security analysis agents), the
  `code-scanning-sarif` artifact is the integration point with GitHub's native Code
  Scanning infrastructure. Document this as an advanced pattern for security-focused
  agent workflows.

- **Add OTel telemetry files as the observability integration point** (Claim 3): Teams
  with existing OpenTelemetry infrastructure can consume `otel.jsonl` and
  `copilot-otel.jsonl` from the `agent` artifact. This extends the observability
  options beyond the gh-aw-native `gh aw audit` tooling.

### Chapter 02 (or Chapter 03): Schema versioning for compliance tooling

- **Add `_schema` prefix-matching as the resilient JSONL parsing strategy** (Claim 9):
  Compliance tooling that consumes `firewall-audit-logs/audit.jsonl` should match schema
  by prefix (`"audit/"`) rather than exact version string. Document schema definitions
  location (`github/gh-aw-firewall` repository) for teams that need to validate record
  formats programmatically.

## Extraction Notes

1. **Source accessed via WebFetch (three passes)**: The gh-aw documentation is an
   Astro/Starlight SPA. Three WebFetch passes were made with different prompts:
   a first-pass overview, a verbatim extraction pass (which returned a copyright
   refusal for full reproduction), and a targeted technical-detail pass. Technical
   strings (artifact names, file paths, constant identifiers, CLI commands, schema
   version strings) are assessed as accurately captured across passes and consistent
   with established gh-aw corpus conventions. First-pass prose quotes are treated
   as likely-verbatim for short, technical passages; they are flagged where the
   verbatim accuracy cannot be independently confirmed.

2. **`safe-outputs-items` and `code-scanning-sarif` not elaborated in source text**:
   Both appear in the artifact table from the third fetch but no additional prose
   describing their use cases was returned. Confidence is marked `emerging` for
   these two claims. Their existence is settled (typed constants confirm them);
   their exact contents and production triggers are inferred from artifact names
   and platform context.

3. **`prompt.txt` location clarification**: The compilation process note
   (`docs-ghaw-compilation-process.md` Claim 9) listed `prompt.txt` among agent
   job artifacts. This reference places it in `activation`. This is assessed as a
   clarification (the compilation process note described files without specifying
   artifact containers) rather than a contradiction. No contradiction issue filed.

4. **Firewall log path reconciliation**: `docs-ghaw-troubleshooting-debugging.md`
   Claim 11 references `sandbox/firewall/logs/access.log` while this reference
   shows `squid-logs/access.log` within the `firewall-audit-logs` artifact. These
   are the same log accessed via the runtime container path (during job execution)
   vs. the artifact download path (after job completion). Not a contradiction.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null.

6. **No contradictions filed**: Reviewed all existing corpus source notes. No
   existing claim materially opposes the artifact taxonomy, the token usage
   separation, or the backward compatibility model. Cross-references are verified
   against actual claim content in the cited notes before writing.
