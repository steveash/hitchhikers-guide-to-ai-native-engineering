---
source_url: https://github.github.com/gh-aw/reference/audit
source_type: docs
title: "GitHub Agentic Workflows: Audit Command Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#450"
---

# GitHub Agentic Workflows: Audit Command Reference

> The authoritative CLI reference for `gh aw audit` and `gh aw logs` — documents
> command syntax, accepted input formats, all flags, single-run vs. multi-run diff
> modes, the complete report section catalogue (27+ sections), the Ambient Context
> Object for per-run LLM cost observability, and stdin batch-processing semantics;
> complementary to `docs-ghaw-audit-with-agents.md` which covers how to consume
> audit output inside autonomous workflows.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/audit` page — in
  the same `reference/` section as `reference/tools`, `reference/checkout`,
  `reference/artifacts`, `reference/awf-reflect`. Reference pages are
  specification-level documents, distinct from the practitioner `guides/` section.
  The existing `docs-ghaw-audit-with-agents.md` covers *consuming* audit output
  in workflows; this page documents the *audit commands themselves* — the CLI
  syntax, flags, modes, and output structure.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI.
  Flag names, defaults, mode descriptions, and output structure are authoritative
  for the `gh aw` platform. Claims are settled for this platform; they do not
  automatically transfer to other audit tooling.
- **Scope**: The `gh aw audit` and `gh aw logs` CLI commands — syntax, all flags
  with defaults, single-run mode, multi-run diff mode, stdin batch processing,
  report section names, and the Ambient Context Object. Does NOT cover: how to
  consume audit output in agent workflows (see `docs-ghaw-audit-with-agents.md`),
  the JSON field schema for programmatic consumers (see `docs-ghaw-audit-with-agents.md`
  Concrete Artifacts → JSON Field Schema), MCP tool invocation of the same
  commands inside GitHub Actions (see `docs-ghaw-audit-with-agents.md` Claim 1),
  the `agentic-workflows:` MCP tool configuration (see `docs-ghaw-tools-reference.md`
  Claim 7), or the observatory architecture built on top of these commands
  (see `blog-ghaw-agent-observability.md`).

## Extracted Claims

### Claim 1: `gh aw audit` operates in two distinct modes — single-run for detailed analysis and multi-run for diff-based comparison — activated solely by the number of run IDs provided

- **Evidence**: The page describes single-run mode as generating detailed Markdown
  reports; multi-run (diff) mode is activated when two or more run IDs are supplied.
  The `--format` flag controls diff output as `pretty` or `markdown`.
- **Confidence**: settled (first-party reference documentation; mode selection
  by argument count is a platform specification)
- **Quote**: (no direct quote capturing the mode-switching mechanic; see paraphrase
  in Our assessment)
- **Our assessment**: The implicit mode switch — one run ID → detailed analysis,
  two or more → diff — is the CLI design that makes `gh aw audit` a dual-purpose
  tool without subcommands. The `docs-ghaw-audit-with-agents.md` Claim 9 documents
  `audit diff` from the agent workflow side (using `workflow_dispatch` inputs
  `base_run_id` and `current_run_id`); this reference page clarifies that the same
  diff behavior is triggered simply by passing multiple run IDs, and the `--format`
  flag selects human-readable (`pretty`) vs. Markdown-renderable output. For Ch02
  (Harness Engineering): document this mode-switching behavior so practitioners
  know there is no separate `audit diff` subcommand — the number of arguments
  determines the mode.

### Claim 2: The multi-run diff mode output surfaces three specific comparison dimensions: new/removed network domains, domain status changes, and MCP tool invocation changes

- **Evidence**: The diff mode output description on the page explicitly names
  these three categories.
- **Confidence**: settled (first-party documentation; the three output dimensions
  are named explicitly)
- **Quote**: "New and removed network domains," "Domain status changes," and
  "MCP tool invocation changes."
- **Our assessment**: These three diff dimensions map directly to the three categories
  of agent regression identified in `docs-ghaw-audit-with-agents.md` Claim 9
  (efficiency/cost, safety/firewall, reliability/MCP tools). The CLI reference
  confirms the diff output structure: network domain changes surface firewall
  policy drift; MCP tool invocation changes surface tool reliability drift. The
  "domain status changes" dimension adds a category not mentioned in the audit
  consumer guide — it implies domains can transition between allowed/blocked/
  restricted states across runs, not just appear or disappear. For Ch03 (Safety
  and Verification): document "domain status changes" as a third network safety
  signal alongside "new blocked domains" from the consumer guide.

### Claim 3: `gh aw audit` accepts multiple input formats — numeric run IDs, GitHub Actions run URLs, job URLs with step anchors, short run URLs, and GitHub Enterprise URLs

- **Evidence**: The "Accepted Input Formats" section enumerates these five input
  types explicitly.
- **Confidence**: settled (first-party reference documentation; the accepted formats
  are enumerated as a specification)
- **Quote**: (no direct quote; the accepted formats are documented as a list without
  a single extractable sentence)
- **Our assessment**: The GHE URL support is operationally significant: teams on
  GitHub Enterprise Server can use `gh aw audit` against their GHE-hosted workflow
  runs without a separate tool or format conversion. The job URL + step anchor
  support enables targeted analysis — auditing a specific job within a multi-job
  workflow run rather than the entire run. For Ch02: practitioners who work across
  multiple GitHub deployments (public + GHE) can use the same audit command
  workflow without per-environment adaptation.

### Claim 4: The `--stdin` flag enables batch processing of run IDs from piped input or file redirect, with blank lines and `#`-prefixed comment lines silently ignored

- **Evidence**: The stdin mode description explicitly states this filtering behavior.
- **Confidence**: settled (first-party documentation; the filtering rule is explicitly
  stated)
- **Quote**: "Blank lines and lines starting with `#` are ignored."
- **Our assessment**: The `#`-comment support in stdin mode enables annotated run
  ID lists — practitioners can maintain a file like:
  ```
  # Sprint 42 baseline runs
  1234567890
  # Post-deploy verification
  1234567891
  ```
  and pipe it directly to `gh aw audit --stdin` without stripping comments first.
  This is a small but useful ergonomic detail for teams that maintain run ID lists
  for recurring audit campaigns. The `cat run-ids.txt | gh aw audit --stdin` pattern
  documented in the examples makes audit scriptable in CI pipelines. For Ch02:
  document stdin batch mode as the integration pattern for scripted audit workflows
  that process multiple runs in sequence.

### Claim 5: The Ambient Context Object — available in run metrics when populated — captures the "first LLM inference footprint for the run" including input tokens, cached tokens, and effective tokens

- **Evidence**: The page describes the Ambient Context Object as an optional
  metrics component that captures specific token dimensions for the first LLM call.
- **Confidence**: emerging (first-party documentation; the "when available" qualifier
  implies this is not always present, and the conditions for population are not
  detailed on this page)
- **Quote**: "the first LLM inference footprint for the run"
- **Our assessment**: The Ambient Context Object provides per-run cost visibility
  at the first LLM inference level. The three token dimensions — input tokens,
  cached tokens, and effective tokens — align with the prompt caching metrics
  documented elsewhere in the corpus (cached tokens reduce cost by using the cache
  instead of re-processing context). "Effective tokens" is the cost-relevant metric:
  it accounts for cache hits by representing the tokens actually billed. This is
  not documented in `docs-ghaw-audit-with-agents.md`, which covers the stable JSON
  output schema but does not mention the Ambient Context Object specifically. For
  Ch02: document the Ambient Context Object as the per-run inference cost signal;
  it is the audit-side complement to the `gh aw logs` cross-run cost tracking that
  `docs-ghaw-audit-with-agents.md` Claim 4 documents at the fleet level. For Ch03
  (Safety and Verification): the effective tokens metric enables cost-anomaly
  detection: a run where effective tokens spike without a corresponding cache-hit
  increase may indicate context bloat or unexpected prompt expansion.

### Claim 6: `gh aw audit` generates reports with 27+ named sections spanning overview, metrics, tool usage, security, and session analysis dimensions

- **Evidence**: The page lists all report sections explicitly.
- **Confidence**: settled (first-party documentation; section names are enumerated)
- **Quote**: "Overview, Comparison, Task/Domain, Behavior Fingerprint, Agentic
  Assessments, Metrics, Key Findings, Recommendations, Observability Insights,
  Performance Metrics, Engine Config, Prompt Analysis, Session Analysis, Safe Output
  Summary, MCP Server Health, Jobs, Downloaded Files, Missing Tools, Missing Data,
  Noops, MCP Failures, Firewall Analysis, Policy Analysis, Redacted Domains, Errors,
  Warnings, Tool Usage, MCP Tool Usage, Created Items."
- **Our assessment**: The section catalogue reveals the audit report's full scope:
  `Behavior Fingerprint` and `Agentic Assessments` appear here, confirming they are
  named sections in the standard report — not just `--parse` enrichment flags as
  `docs-ghaw-audit-with-agents.md` Claim 12 implied. The `Noops` section confirms
  that the `noop` safe output (from `docs-ghaw-audit-with-agents.md` Claim 6) is
  visible in audit output — a dedicated report section. `Redacted Domains` is a
  new section not described anywhere in the corpus — it implies some network domains
  are redacted from reports (possibly privacy-sensitive or policy-protected domains).
  `Engine Config` provides per-run engine configuration visibility. For Ch02: the
  section catalogue is the complete audit report reference; practitioners building
  markdown-based report parsers should use it. For Ch03: the `Safe Output Summary`
  section makes safe output operations directly visible in audit reports — enabling
  post-hoc verification that only intended state mutations occurred.

### Claim 7: `gh aw logs` detects cross-run anomalies including domain access spikes, elevated MCP error rates, and connection rate changes across a configurable number of recent runs

- **Evidence**: The page describes `gh aw logs` output and its anomaly detection
  capabilities explicitly.
- **Confidence**: settled (first-party documentation; the anomaly categories are
  explicitly named)
- **Quote**: "detects cross-run anomalies such as domain access spikes, elevated
  MCP error rates, and connection rate changes."
- **Our assessment**: "Connection rate changes" is a new anomaly category not
  mentioned in `docs-ghaw-audit-with-agents.md`, which describes the `gh aw logs`
  consumer patterns but focuses on `error_rate > 0.10` and `unreliable: true` flags.
  Connection rate changes would surface patterns like an agent suddenly making
  significantly more or fewer network connections than its historical baseline —
  a behavioral anomaly that could indicate prompt injection, scope creep, or
  configuration drift even when no domain policy violations occur. The default of
  10 recent runs (`-c, --count: 10`) provides a rolling window for baseline
  comparison. For Ch03: document "connection rate changes" as a third cross-run
  anomaly type alongside domain access spikes and MCP error rate spikes. All three
  are behavioral SLIs for the network and tool layers.

### Claim 8: Both `gh aw audit` and `gh aw logs` write artifacts to `./logs` by default via the shared `-o/--output` flag, providing a predictable artifact location for downstream consumers

- **Evidence**: The flag tables for both commands show `-o, --output` defaulting
  to `./logs`.
- **Confidence**: settled (first-party documentation; the shared default is
  explicitly specified)
- **Quote**: (no direct quote capturing the shared default; the flag tables
  document it for each command independently)
- **Our assessment**: A consistent default output directory across both commands
  simplifies local development workflows: running `gh aw audit` followed by
  `gh aw logs` against the same working directory accumulates all artifacts under
  `./logs` without per-command path configuration. For Ch02: document `./logs`
  as the conventional artifact directory for gh-aw audit tooling; practitioners
  should structure their audit-related scripts around this convention rather than
  overriding it arbitrarily. The `--repo` flag's `auto` default (which infers
  the repository from the current git context) combined with the `./logs` default
  makes both commands usable with zero flags in typical development scenarios.

## Concrete Artifacts

### `gh aw audit` Command Reference

```
gh aw audit <run-id-or-url> [<run-id-or-url>...]

Accepted input formats:
  - Numeric run ID (e.g., 1234567890)
  - GitHub Actions run URL
  - Job URL (with optional step anchors)
  - Short run URL
  - GitHub Enterprise URL (equivalent format)

Flags:
  -o, --output <dir>    Output directory for artifacts and reports  [default: ./logs]
  --json                JSON output to stdout                        [default: off]
  --parse               Run JavaScript parsers on logs              [default: off]
                        Populates: behavior_fingerprint, agentic_assessments
  --repo <repo>         Repository context                          [default: auto]
  --stdin               Read run IDs from stdin (one per line)      [default: off]
                        Note: blank lines and lines starting with # are ignored
  --verbose             Detailed progress output                    [default: off]
  --format <fmt>        Diff output format: pretty or markdown      [default: pretty]

Modes:
  Single run (1 ID):    Detailed Markdown report with 27+ sections
  Multi-run (2+ IDs):   Diff report comparing base run vs. others
                        Diff dimensions: new/removed network domains,
                        domain status changes, MCP tool invocation changes
```

*Source: GitHub Agentic Workflows reference/audit, `gh aw audit` command section*

### `gh aw logs` Command Reference

```
gh aw logs [workflow] --format <fmt>

Flags:
  -c, --count <n>       Number of recent runs to analyze            [default: 10]
  --format <fmt>        Output format: markdown or pretty
  --json                JSON output format                          [default: off]
  --repo <repo>         Repository context                          [default: auto]
  -o, --output <dir>    Artifact directory                          [default: ./logs]
  --stdin               Read run IDs from stdin                     [default: off]

Cross-run anomaly detection:
  - Domain access spikes
  - Elevated MCP error rates
  - Connection rate changes
```

*Source: GitHub Agentic Workflows reference/audit, `gh aw logs` command section*

### Example Commands

```bash
# Single-run audit
gh aw audit 1234567890

# Multi-run diff (pretty format)
gh aw audit 12345 12346

# Multi-run diff (markdown output)
gh aw audit 12345 12346 --format markdown

# Batch processing from file
cat run-ids.txt | gh aw audit --stdin

# Cross-run security/performance audit (last 10 runs, markdown)
gh aw logs --format markdown --count 10
```

*Source: GitHub Agentic Workflows reference/audit, examples section*

### Full Report Section Catalogue (`gh aw audit` single-run mode)

```
Overview              Comparison           Task/Domain
Behavior Fingerprint  Agentic Assessments  Metrics
Key Findings          Recommendations      Observability Insights
Performance Metrics   Engine Config        Prompt Analysis
Session Analysis      Safe Output Summary  MCP Server Health
Jobs                  Downloaded Files     Missing Tools
Missing Data          Noops                MCP Failures
Firewall Analysis     Policy Analysis      Redacted Domains
Errors                Warnings             Tool Usage
MCP Tool Usage        Created Items
```

*Source: GitHub Agentic Workflows reference/audit, report sections list*

### Ambient Context Object (in run metrics)

```
Ambient Context Object (populated when available in metrics):
  Captures: first LLM inference footprint for the run
  Fields:
    input_tokens    — tokens in the first LLM call's input
    cached_tokens   — tokens served from cache (cost reduction)
    effective_tokens — tokens actually billed (= input - cached)
```

*Source: GitHub Agentic Workflows reference/audit, Ambient Context section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-audit-with-agents.md` Claim 12 (`--parse` flag populates
    `behavior_fingerprint` and `agentic_assessments` as optional, non-stable
    enrichment): this reference page confirms `--parse` runs "JavaScript parsers
    on logs" and adds these fields. The consumer guide accurately characterizes
    them as non-stable enrichment; the reference page confirms the mechanism.
  - `docs-ghaw-audit-with-agents.md` Claim 3 (audit output has stable top-level
    fields and extensible nested sub-fields): the report sections catalogue
    (Claim 6 here) confirms the section-level structure of audit reports.
    `Key Findings`, `Metrics`, `Firewall Analysis`, `MCP Tool Usage` appear
    both in the section catalogue and in the consumer guide's JSON schema — they
    are the stable fields at both the human-readable and machine-readable levels.
  - `docs-ghaw-tools-reference.md` Claim 7 (`agentic-workflows:` tool requires
    `actions: read` permission): the CLI-level audit command documented here
    is what the `agentic-workflows:` MCP tool exposes inside GitHub Actions.
    The permission requirement for the MCP tool mirrors what the CLI needs to
    access GitHub Actions run data.
  - `blog-ghaw-agent-observability.md` Claim 5 (observability can close the
    feedback loop autonomously — 93 audit reports → 9 issues → 4 PRs): the audit
    commands documented here are the foundation of that loop. The `gh aw audit`
    reports (from `blog-ghaw-agent-observability.md` Claim 3) are produced by
    `gh aw audit` single-run mode; the 9 issues were triggered by findings in
    the `Key Findings` section.

- **Extends**:
  - `docs-ghaw-audit-with-agents.md`: this reference page is the upstream CLI
    specification for the commands that note covers from the consumer side. Together:
    reference/audit = what the commands are and produce; guides/audit-with-agents =
    how to wire the output into autonomous workflows. The two notes are designed to
    be read together.
  - `blog-ghaw-agent-observability.md` Claim 3 (the Audit Workflows agent is
    the most prolific agent in the factory): the section catalogue (Claim 6 here)
    shows why that volume is possible — a single `gh aw audit` run produces
    27+ report sections covering everything from engine config to created items.
    The richness of the output is what makes it useful for meta-auditing.
  - `docs-ghaw-audit-with-agents.md` Claim 9 (regression detection via `audit diff`
    with `run_metrics_diff`, `firewall_diff`, `mcp_tools_diff`): this reference
    clarifies that "audit diff" is activated by supplying two or more run IDs
    to `gh aw audit`, not a separate subcommand. The diff dimensions documented
    here (network domains, domain status, MCP invocations) are the human-visible
    counterpart to those JSON fields.

- **Contradicts**: None identified. No existing source note makes claims that
  conflict with the command syntax, flag defaults, modes, or output structure
  documented here. The `--parse` flag's JavaScript parser mechanism is new
  detail that extends (not contradicts) `docs-ghaw-audit-with-agents.md` Claim 12.
  The "connection rate changes" anomaly type in `gh aw logs` is new information
  not contradicted by any existing note. No contradiction issue filed.

- **Novel** (what this note adds that no prior source covers):
  - **Complete flag tables for both commands** (Claims 1, 7, 8, Concrete
    Artifacts): No existing source note documents the full flag set for
    `gh aw audit` or `gh aw logs` at the reference level. `docs-ghaw-audit-with-agents.md`
    documents these commands through the lens of workflow specs; this is the
    first CLI-level flag reference in the corpus.
  - **Multi-run diff mode activated by argument count** (Claim 1): The implicit
    mode-switching mechanic (one run → detailed analysis; two+ runs → diff) is
    not documented in any existing source note.
  - **Diff output dimensions: "domain status changes"** (Claim 2): The domain
    status changes category — domains transitioning between allowed/blocked/
    restricted states — is not described in `docs-ghaw-audit-with-agents.md` or
    any other note. It adds a third network safety signal beyond new domains and
    MCP error rates.
  - **stdin batch mode with comment filtering** (Claim 4): The `--stdin` flag
    behavior including the `#`-comment-line filtering rule is not documented
    in any existing source note.
  - **Ambient Context Object with three token fields** (Claim 5): The Ambient
    Context Object (input tokens, cached tokens, effective tokens for the first
    LLM inference) is not described in any existing source note. It is the
    per-run LLM cost observability primitive.
  - **Complete 27+ section catalogue** (Claim 6): No existing source note
    enumerates all audit report sections. `Noops`, `Redacted Domains`,
    `Session Analysis`, `Prompt Analysis`, `Engine Config`, and several others
    are new to the corpus.
  - **"Connection rate changes" as a cross-run anomaly type** (Claim 7):
    The third anomaly category for `gh aw logs` (alongside domain access spikes
    and MCP error rates) is not described in `docs-ghaw-audit-with-agents.md`
    or `blog-ghaw-agent-observability.md`.
  - **Accepted input formats including GHE URLs** (Claim 3): The multi-format
    input support including GitHub Enterprise URLs is not documented in any
    existing source note.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the complete flag tables for `gh aw audit` and `gh aw logs` as the CLI
    reference for practitioners setting up audit tooling locally. The existing
    corpus covers these commands only through workflow YAML specs — this adds
    the local development dimension.
  - Document the implicit mode-switching (one ID → analysis, two+ IDs → diff)
    to help practitioners understand that "audit diff" is not a separate subcommand.
    Cross-reference `docs-ghaw-audit-with-agents.md` Claim 9 which shows the
    same command used in a `workflow_dispatch` workflow spec.
  - Add `./logs` as the standard artifact directory convention for gh-aw audit
    tooling; recommend not overriding it in local development scripts.
  - Document stdin batch mode (`--stdin`) as the scriptable audit pattern for
    processing multiple run IDs from a file, noting the comment-line filtering.

- **Chapter 03 (Safety and Verification)**:
  - Add "domain status changes" as a third network safety signal in the diff
    mode output — alongside new blocked domains and MCP error rate changes.
    Update any discussion of `audit diff` dimensions to include this category.
  - Add the `Safe Output Summary` report section as the audit mechanism for
    verifying that only intended state mutations occurred in a workflow run.
    This is a concrete post-hoc safety check: after a run, inspect `Safe Output
    Summary` to confirm the agent wrote only to expected targets.
  - Add the Ambient Context Object (effective tokens = input - cached) as the
    per-run cost anomaly detection signal. A run where effective tokens spike
    while cached tokens drop may indicate context bloat or prompt injection
    that bypassed the cache.
  - Add "connection rate changes" as a behavioral anomaly type for `gh aw logs`
    cross-run analysis, alongside domain access spikes and MCP error rate spikes.

## Extraction Notes

1. **Source is AI-mediated WebFetch**: The gh-aw documentation is an Astro/Starlight
   SPA. Two WebFetch calls were made with different prompts (structured extraction
   and verbatim reproduction). Text appearing in quotation marks in the fetch output
   is assessed as verbatim from the source; other descriptions are paraphrased.
   The section catalogue, flag names, defaults, and quoted anomaly/description
   phrases are the most reliably verbatim content.

2. **`Behavior Fingerprint` and `Agentic Assessments` appear as full report sections**:
   These appear in the section catalogue for standard (non-`--parse`) audit reports.
   `docs-ghaw-audit-with-agents.md` Claim 12 characterizes them as `--parse`-enriched
   optional fields. These are not contradictory — they may exist as sections with
   minimal content in standard mode and become fully populated with `--parse`. The
   distinction warrants further verification but does not rise to a contradiction
   requiring filing.

3. **`Redacted Domains` section is undocumented elsewhere**: This section name
   appeared in the section catalogue. The conditions under which domains are redacted
   (privacy policy, enterprise configuration, or other reasons) are not described on
   this page. This is noted for the Assayer and Smith as an area requiring further
   investigation from other reference pages (e.g., network reference or policy
   reference).

4. **Connection rate changes anomaly type**: This is a distinct anomaly from domain
   access changes — it implies volume-based detection rather than domain-identity
   detection. The specific fields that surface this in `gh aw logs` JSON output are
   not named on this page; they may be in the `per_run_breakdown` section described
   in `docs-ghaw-audit-with-agents.md`.

5. **No publication date**: The documentation does not carry an explicit publication
   date. Content is consistent with the current gh-aw platform state as of 2026-05-12.

6. **No contradictions to file**: Reviewed `docs-ghaw-audit-with-agents.md`,
   `blog-ghaw-agent-observability.md`, `docs-ghaw-tools-reference.md`, and all
   related source notes. No claims in this reference page materially oppose existing
   notes. The `--parse` mode detail (JavaScript parsers on logs) extends rather than
   contradicts the consumer guide's characterization of `--parse` output. No
   contradiction issue filed.
