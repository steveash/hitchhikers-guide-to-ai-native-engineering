---
source_url: https://github.github.com/gh-aw/troubleshooting/debugging
source_type: docs
title: "GitHub Agentic Workflows: Debugging Workflows"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#427"
---

# GitHub Agentic Workflows: Debugging Workflows

> The first source in the corpus specifically on debugging and troubleshooting
> agentic workflow failures — documents a three-step AI-assisted Copilot CLI
> debugging workflow as the recommended first-response, four CLI diagnostic
> commands (`gh aw audit`, `gh aw logs`, `gh aw health`, `gh aw mcp inspect`),
> five common error categories with root causes and fixes, and advanced
> techniques (`DEBUG=*` logging, `ACTIONS_STEP_DEBUG`, artifact inspection).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `troubleshooting/debugging`
  page — a practitioner how-to guide in the `troubleshooting/` section, distinct
  from the `reference/` and `patterns/` sections. This page is prescriptive
  (step-by-step debugging procedures), not declarative (reference for config
  options) or architectural (design pattern descriptions).)
- **Author credibility**: First-party from GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — the same team operating Peli de Halleux's agent
  factory). CLI commands, artifact paths, and error messages are authoritative
  for the `gh aw` platform. Debugging procedures are platform-specific; the
  general patterns (AI-assisted debugging, env-var debug logging, artifact
  inspection) transfer to other agentic platforms.
- **Scope**: Covers debugging agentic workflow failures from three angles: (1)
  AI-assisted debugging via the Copilot CLI's `agentic-workflows` agent; (2) CLI
  commands for investigation (`gh aw audit`, `gh aw logs`, `gh aw health`,
  `gh aw mcp inspect`); (3) advanced manual techniques (`DEBUG=*`, GitHub Actions
  debug logging, firewall log inspection, artifact downloading). Does NOT cover:
  monitoring configuration patterns (see `docs-ghaw-monitoring-patterns.md`),
  consuming audit data programmatically inside workflows (see
  `docs-ghaw-audit-with-agents.md`), network policy configuration (see
  `docs-ghaw-network-reference.md`), or compilation internals (see
  `docs-ghaw-compilation-process.md`).

## Extracted Claims

### Claim 1: AI-assisted debugging via the Copilot CLI is positioned as the fastest path to fixing agentic workflow failures

- **Evidence**: The guide opens with this recommendation before introducing any
  other debugging technique, framing it as the primary approach. The AI-first
  framing is consistent with the platform's philosophy of using agents to debug
  agents.
- **Confidence**: emerging (first-party recommendation; no production metrics on
  how often AI-assisted debugging succeeds vs. manual approaches)
- **Quote**: "The fastest path to a fix is to let an AI agent debug it for you.
  Launch the Copilot CLI, load the agentic-workflows agent, and paste the failing
  run URL."
- **Our assessment**: The guide practicing what it preaches — an agentic platform
  recommending that practitioners use an AI agent to debug their AI agents. This
  is architecturally coherent: the `agentic-workflows` agent has access to `gh aw
  audit`, `gh aw logs`, and other debugging tools that a practitioner would
  otherwise have to run manually. For Ch05 (Observability & Feedback Loops):
  add AI-assisted debugging as the recommended first-response for agentic
  workflow failures, noting it is itself an agentic workflow that leverages the
  same audit tooling available to practitioners.

### Claim 2: The three-step Copilot CLI debugging workflow is: launch `copilot`, load the `agentic-workflows` agent via `/agent`, then paste the failing run URL

- **Evidence**: The guide documents three explicit numbered steps. Step 2 explains
  why the agent selection step matters: it grants the Copilot access to debugging
  tools.
- **Confidence**: emerging (first-party procedure; the workflow is described
  prescriptively but without production success-rate data)
- **Quote**: "Once inside the Copilot CLI, run: `/agent` — Select
  **agentic-workflows** from the list. This gives Copilot access to the `gh aw
  audit`, `gh aw logs`, and other debugging tools."
- **Our assessment**: The `/agent` selector step is significant: it loads a
  purpose-built debugging-capable agent, not the generic Copilot assistant.
  Without this step, the Copilot would lack the `gh aw` tool access needed to
  examine run artifacts and logs. For Ch05: document the exact three-step
  sequence, emphasizing Step 2 — selecting the `agentic-workflows` agent is what
  unlocks audit capabilities, not just launching the CLI.

### Claim 3: The agentic-workflows Copilot agent automatically downloads and audits run logs, identifies root causes, and can suggest targeted fixes or open a pull request

- **Evidence**: Three concrete deliverables are enumerated. The "open a pull
  request with the fix" capability is the highest-automation outcome described.
- **Confidence**: emerging (first-party claim; success of PR-opening is highly
  dependent on error type and workflow complexity)
- **Quote**: "Copilot will: Download and audit the run logs; Identify the root
  cause (missing tools, permission errors, network blocks, etc.); Suggest
  targeted fixes or open a pull request with the fix"
- **Our assessment**: The three deliverables span a spectrum from observation
  (download logs) to analysis (root cause) to remediation (suggest fix or open
  PR). The PR-opening capability represents the fully autonomous debugging loop:
  an agent that not only diagnoses but remediates. For Ch04 (Building Agent
  Systems): this is a concrete production example of an agent-debugging-agent
  system — the debugging agent has specialized tool access and a bounded task
  (investigate one run, produce one fix). Note the example follow-up questions
  the guide provides: "What domains were blocked by the firewall? Show me the
  safe-outputs from this run. Why did the MCP server fail to connect?" — these
  show that interactive follow-up is expected, not just one-shot interrogation.

### Claim 4: `gh aw audit` provides a comprehensive breakdown of a single run including failure analysis, behavior fingerprint, tool usage, MCP server status, firewall analysis, and token/cost metrics

- **Evidence**: The guide lists seven named output sections. The "behavior
  fingerprint" field is highlighted as a multi-dimensional run characterization.
- **Confidence**: settled (first-party documentation; consistent with the stable
  field schema documented in `docs-ghaw-audit-with-agents.md` Claim 3)
- **Quote**: "`gh aw audit` gives a comprehensive breakdown of a single run —
  overview, metrics, tool usage, MCP failures, firewall analysis, behavior
  fingerprint, and artifacts"
- **Our assessment**: "Behavior fingerprint" is the notable addition here — a
  multi-dimensional characterization of the run's network, tool, and cost profile
  that is not just a log but a semantic fingerprint enabling run comparisons.
  The `--parse` flag noted in `docs-ghaw-audit-with-agents.md` Claim 3 is what
  populates this field. For Ch05: `gh aw audit` should be the first investigative
  tool when a practitioner notices unexpected agent behavior — before writing any
  consumer workflow, run the audit CLI on the suspicious run.

### Claim 5: `gh aw audit` accepts run references in multiple formats: run ID, full Actions URL, job URL, and step URL, plus `--parse` for markdown output

- **Evidence**: Five command variants are documented on the page. The URL-based
  formats support deep-linking from the GitHub Actions UI directly into the
  audit CLI.
- **Confidence**: settled (first-party; specific CLI argument formats are
  authoritative)
- **Quote**: (no single prose quote; CLI command variants are the evidence —
  see Concrete Artifacts)
- **Our assessment**: The step URL format (`runs/123/job/456#step:7:1`) is
  particularly useful for debugging compilation or pre-activation failures where
  a specific step is the failure point. The `--parse` flag (format as markdown)
  is the bridge to the MCP consumption path documented in
  `docs-ghaw-audit-with-agents.md` — practitioners can use `--parse` output to
  understand what the audit-consuming workflow will receive. For Ch05: document
  the URL-based reference formats as the practitioner's shortcut — copy the
  failing step URL from the Actions UI, paste into `gh aw audit`, get the analysis.

### Claim 6: `gh aw logs` results are cached locally for 10–100× speedup on repeated runs against the same workflow

- **Evidence**: Stated directly in the CLI commands section. No further detail
  on cache mechanism or invalidation conditions.
- **Confidence**: emerging (first-party claim; specific speedup range
  (10–100×) is a rough estimate rather than a precise benchmark)
- **Quote**: "Results are cached locally for 10–100× speedup on subsequent
  runs."
- **Our assessment**: The caching behavior makes `gh aw logs` viable for
  interactive trend investigation — on first run it downloads and analyzes
  log data; on subsequent runs (e.g., filtering differently) it reuses the
  downloaded data. For Ch05: document the caching behavior as a reason to
  prefer `gh aw logs` over downloading artifacts manually for multi-run
  analysis.

### Claim 7: Authentication failures trace specifically to a missing, expired, or permission-insufficient Copilot token; verified via `gh auth status`

- **Evidence**: The error category section lists four diagnostics steps,
  including the specific permission name ("Copilot Requests") required on
  the token.
- **Confidence**: settled (first-party; token requirements are platform
  specifications)
- **Quote**: "The Copilot token is missing, expired, or lacks required
  permissions."
- **Our assessment**: The "Copilot Requests" permission is a non-obvious
  required permission — practitioners may have a valid GitHub token but miss
  this specific scope. `gh auth status` is the verification command. For Ch02
  (Harness Engineering): add authentication failure diagnosis as the first
  check when agentic workflows fail silently — verify Copilot subscription
  status and token scope before investigating workflow logic.

### Claim 8: Network/firewall blocks manifest as `DENIED CONNECT domain:port` log entries and are fixed by adding domains to `network.allowed` in workflow frontmatter or using ecosystem shorthands

- **Evidence**: Specific error log format is given. Fix options include both
  individual domain entries and ecosystem shorthands (node, python, etc.) that
  expand to curated domain sets.
- **Confidence**: settled (first-party; the log format and fix mechanism are
  platform-authoritative; consistent with `docs-ghaw-network-reference.md`
  Claim 1)
- **Quote**: "`DENIED CONNECT registry.npmjs.org:443`"
- **Our assessment**: The ecosystem shorthand approach is the lower-friction
  path for common package managers — rather than manually enumerating every
  npm registry domain, a single `ecosystem: node` shorthand grants the curated
  set. The `DENIED CONNECT` format is important to recognize: practitioners who
  see this in raw logs know immediately it is a firewall issue, not an MCP
  configuration issue or a code bug. For Ch02: document `DENIED CONNECT` as the
  canonical firewall-block signature, and add the ecosystem shorthand approach
  as the recommended fix for package-manager-dependent workflows.

### Claim 9: The `DEBUG` environment variable with namespace patterns enables detailed stderr logging for any `gh aw` command, with output captured via `2>&1 | tee debug.log`

- **Evidence**: Four namespace patterns are documented: `DEBUG=*` (all),
  `DEBUG=cli:*` (CLI-specific), `DEBUG=workflow:*` (workflow compilation),
  `DEBUG=workflow:*,cli:*` (multiple namespaces). The stderr destination and
  capture method are explicit.
- **Confidence**: settled (first-party; the `DEBUG` env-var pattern is a
  documented CLI feature)
- **Quote**: "The `DEBUG` environment variable enables detailed internal logging
  for any `gh aw` command" and "Debug output goes to `stderr`. Capture it with
  `2>&1 | tee debug.log`."
- **Our assessment**: The namespace pattern system (`workflow:*`, `cli:*`) allows
  targeted logging without being overwhelmed by all debug output. The `2>&1 |
  tee debug.log` pattern is the standard way to capture stderr for later
  analysis while still seeing it in the terminal. For Ch02: document the
  `DEBUG=workflow:*` pattern as the go-to for diagnosing compilation failures
  and `DEBUG=cli:*` for CLI-level issues. This is a consistent pattern with
  Node.js and Go tooling that many practitioners will recognize.

### Claim 10: GitHub Actions step-level debug logging for agentic workflows is activated via an `ACTIONS_STEP_DEBUG` repository secret set to `true`

- **Evidence**: Three-step procedure: Settings → Secrets → Add `ACTIONS_STEP_DEBUG=true`,
  then re-run the workflow. The secret-based approach (not a workflow config)
  is notable.
- **Confidence**: settled (first-party; the `ACTIONS_STEP_DEBUG` secret is a
  standard GitHub Actions feature applied to the agentic workflow context)
- **Quote**: "Set the `ACTIONS_STEP_DEBUG` secret to `true` in your repository
  to enable verbose step-level logging"
- **Our assessment**: The `ACTIONS_STEP_DEBUG` secret is a standard GitHub
  Actions debugging mechanism, not an agentic-workflows-specific feature — any
  GitHub Actions workflow can use it. Its documentation here confirms it works
  for agentic workflow jobs. The "re-run the workflow" requirement means this
  adds some friction vs. the `DEBUG=*` CLI approach (which takes effect
  immediately). For Ch02: document `ACTIONS_STEP_DEBUG` as the GitHub Actions-
  level counterpart to `DEBUG=*` — use it when the failure is in a GitHub
  Actions job step rather than in a local CLI invocation.

### Claim 11: Firewall access logs reside at `sandbox/firewall/logs/access.log` within run artifacts, using `TCP_TUNNEL` to indicate allowed traffic and `DENIED` to indicate blocked traffic

- **Evidence**: Specific artifact path and two log entry formats are given.
  Companion CLI alternatives (`gh aw logs my-workflow --firewall` and
  `gh aw audit <run-id>`) are also documented as higher-level alternatives to
  manual inspection.
- **Confidence**: settled (first-party; artifact path and log format are
  authoritative)
- **Quote**: "Download the workflow run artifacts and look for
  `sandbox/firewall/logs/access.log`. Each line shows whether a domain was
  allowed (`TCP_TUNNEL`) or blocked (`DENIED`)"
- **Our assessment**: The `sandbox/firewall/logs/access.log` path gives
  practitioners direct access to the raw firewall audit trail — useful when
  the CLI abstractions are insufficient for compliance reporting or security
  audit. The `TCP_TUNNEL/200 api.github.com:443` vs `DENIED CONNECT
  blocked-domain.com:443` format is the standard squid proxy log format,
  which many practitioners will recognize from infrastructure work. For Ch03
  (Safety & Verification): document `sandbox/firewall/logs/access.log` as
  the canonical artifact for compliance-level network audit of agentic workflow
  runs — `gh aw audit` provides a processed summary; this path provides the
  complete raw log.

### Claim 12: Four artifact types are inspectable for post-run debugging: `prompt.txt`, `agent_output.json`, `agent-stdio.log`, and `firewall-logs/`, downloadable via `gh run download`

- **Evidence**: The guide documents a four-row artifact table with local paths
  and descriptions. The `agent-stdio.log` artifact is the raw stdin/stdout log
  for the agent process, which is not listed in `docs-ghaw-compilation-process.md`'s
  artifact inventory.
- **Confidence**: emerging (first-party; the four artifact types are documented
  but the `agent-stdio.log` artifact appears to be an addition not listed in
  the compilation reference — see Extraction Notes)
- **Quote**: (no single prose quote; artifact table is the evidence — see
  Concrete Artifacts)
- **Our assessment**: `agent-stdio.log` is the raw agent communication log,
  distinct from `agent_output.json` (structured safe-output data). For
  deeply confused agent behavior — where the structured output doesn't explain
  why the agent took an action — the raw stdin/stdout log may reveal the
  agent's intermediate reasoning steps. For Ch05: document the four artifacts
  with their specific debugging use cases: `prompt.txt` for "what did the agent
  receive?", `agent_output.json` for "what did the agent decide?", `agent-stdio.log`
  for "how did the agent communicate?", and `firewall-logs/` for "what network
  traffic was generated?"

### Claim 13: Compilation errors are diagnosed via `gh aw compile my-workflow --verbose` and can be auto-remediated with `gh aw fix --write`

- **Evidence**: Two CLI commands are documented for compilation failure handling.
  `--verbose` traces the compilation for diagnosis; `--write` applies auto-fixes.
  `gh aw compile --validate` is a third variant for validation-only.
- **Confidence**: settled (first-party; CLI commands are authoritative)
- **Quote**: (no single prose quote; CLI commands are the evidence — see
  Concrete Artifacts)
- **Our assessment**: The `gh aw fix --write` command implies a programmatic
  fix-application mechanism — the platform can identify and auto-correct certain
  categories of compilation errors. This is a higher-level automation than
  `--verbose` (which only diagnoses). For Ch02: document `gh aw fix --write` as
  the auto-remediation path for compilation errors, and note it as a model for
  other harness tooling: the compiler that can not only detect but fix its own
  output errors.

## Concrete Artifacts

### Three-Step Copilot CLI Debugging Workflow

```
Step 1: Launch the Copilot CLI
  $ copilot

Step 2: Load the agentic-workflows agent
  /agent
  → Select "agentic-workflows" from the list
  (This gives Copilot access to gh aw audit, gh aw logs, and other debugging tools)

Step 3: Paste the failing run URL and ask Copilot to investigate
  Debug this workflow run: https://github.com/OWNER/REPO/actions/runs/RUN_ID

  Copilot will:
  - Download and audit the run logs
  - Identify the root cause (missing tools, permission errors, network blocks, etc.)
  - Suggest targeted fixes or open a pull request with the fix

Example follow-up questions:
  "What domains were blocked by the firewall?"
  "Show me the safe-outputs from this run."
  "Why did the MCP server fail to connect?"
```

*Source: gh-aw troubleshooting/debugging, "Debug with Copilot" section*

### `gh aw audit` CLI Command Variants

```bash
# By run ID
gh aw audit 12345678

# By full Actions URL
gh aw audit https://github.com/OWNER/REPO/actions/runs/12345678

# By job URL
gh aw audit https://github.com/OWNER/REPO/actions/runs/123/job/456

# By step URL (deep-link from the Actions UI)
gh aw audit https://github.com/OWNER/REPO/actions/runs/123/job/456#step:7:1

# Parse output to markdown
gh aw audit 12345678 --parse

# Two-run diff (behavioral regression detection)
gh aw audit 12345678 12345679
gh aw audit 12345678 12345679 --format markdown
```

*Source: gh-aw troubleshooting/debugging, "Auditing a Specific Run" section*

### `gh aw logs` CLI Command Variants

```bash
# Download and analyze logs for a workflow
gh aw logs my-workflow

# Filter by count and date range
gh aw logs my-workflow -c 10 --start-date -1w

# Include firewall analysis
gh aw logs my-workflow --firewall

# Include safe-output details
gh aw logs my-workflow --safe-output

# JSON output for programmatic consumption
gh aw logs my-workflow --json

# Note: results are cached locally for 10–100× speedup on subsequent runs
```

*Source: gh-aw troubleshooting/debugging, "Analyzing Workflow Logs" section*

### MCP Inspection Commands

```bash
# List all workflow MCP configurations
gh aw mcp list

# Inspect MCP servers for a specific workflow
gh aw mcp inspect my-workflow

# Open web-based MCP inspector
gh aw mcp inspect my-workflow --inspector
```

*Source: gh-aw troubleshooting/debugging, "Inspecting MCP Configuration" section*

### Common Errors Reference

```
Error: "Authentication failed"
  Cause: The Copilot token is missing, expired, or lacks required permissions.
  Fix:
    1. Verify active Copilot subscription
    2. Check token has "Copilot Requests" permission
    3. gh auth status    # verify token validity
    4. Reference authentication documentation

Error: "Tool not found" / Missing tool calls
  Cause: Workflow references a tool that isn't configured or MCP server failed to connect.
  Fix:
    1. gh aw mcp inspect my-workflow    # verify configuration
    2. Check MCP server version compatibility
    3. Verify tools: section includes required tool
    4. gh aw audit <run-id>             # see available vs. requested tools

Error: Network / Firewall Block
  Symptom: DENIED CONNECT registry.npmjs.org:443
  Cause: Agent tried to reach a domain not in the firewall allow-list.
  Fix: Add the domain to the network.allowed list in workflow frontmatter
       OR use an ecosystem shorthand (node, python, etc.)

Error: Safe-outputs not creating issues/comments
  Cause: safe-outputs job failed, agent didn't produce expected output,
         or permissions are missing.
  Fix:
    1. gh aw audit <run-id>    # check safe-outputs section
    2. Reference safe outputs documentation

Error: Compilation errors
  Cause: Workflow frontmatter has schema validation errors or unsupported fields.
  Fix:
    1. gh aw compile my-workflow --verbose
    2. gh aw fix --write
    3. gh aw compile --validate
    4. Reference error documentation
```

*Source: gh-aw troubleshooting/debugging, "Common Errors" section*

### DEBUG Environment Variable Patterns

```bash
# All debug logs
DEBUG=* gh aw compile my-workflow

# CLI-specific logs
DEBUG=cli:* gh aw audit 12345678

# Workflow compilation logs
DEBUG=workflow:* gh aw compile my-workflow

# Multiple packages
DEBUG=workflow:*,cli:* gh aw compile my-workflow

# Capture stderr output
DEBUG=* gh aw compile my-workflow 2>&1 | tee debug.log
```

*Source: gh-aw troubleshooting/debugging, "Enable Debug Logging" section*

### GitHub Actions Debug Logging

```
1. Go to Settings → Secrets and variables → Actions
2. Add secret: ACTIONS_STEP_DEBUG = true
3. Re-run the workflow

This produces much more detailed logs in the Actions UI.
```

*Source: gh-aw troubleshooting/debugging, "Enable GitHub Actions Debug Logging" section*

### Artifact Inspection Reference

```
Artifact           | Local Path              | Contents
-------------------|-------------------------|--------------------------------------
prompt.txt         | /tmp/gh-aw/aw-prompts/  | Full prompt sent to the AI agent
agent_output.json  | /tmp/gh-aw/safeoutputs/ | Structured safe-output data
agent-stdio.log    | /tmp/gh-aw/             | Raw agent stdin/stdout log
firewall-logs/     | /tmp/gh-aw/firewall-logs| Network access logs

Download all artifacts:
  gh run download <run-id> --repo OWNER/REPO

Firewall log format (sandbox/firewall/logs/access.log):
  TCP_TUNNEL/200 api.github.com:443         ← allowed
  DENIED CONNECT blocked-domain.com:443     ← blocked
```

*Source: gh-aw troubleshooting/debugging, "Inspecting Artifacts" and
"Inspecting Firewall Logs" sections*

### Recompile-and-Push Fix Procedure

```bash
# After identifying and fixing an issue in the .md file:
gh aw compile my-workflow
git add .github/workflows/my-workflow.md .github/workflows/my-workflow.lock.yml
git commit -m "fix: update workflow configuration"
git push
```

*Source: gh-aw troubleshooting/debugging, "Recompiling for a Quick Fix" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-monitoring-patterns.md` Claim 7 (`gh aw audit <run-id>` as per-run
    practitioner CLI command): this source provides additional detail on the audit
    output contents (behavior fingerprint, failure analysis, safe-outputs section)
    and adds URL-based reference formats not documented in the monitoring note.
    Both confirm `gh aw audit` as the primary diagnostic CLI command.
  - `docs-ghaw-monitoring-patterns.md` Claim 8 (`gh aw audit <id1> <id2>` two-run
    diff form): this source documents the same command, confirming behavioral
    regression detection is available from the debugging path as well as the
    monitoring path.
  - `docs-ghaw-compilation-process.md` Claim 9 (artifact inventory including
    `agent_output.json`, `prompt.txt`, and `firewall-audit-logs`): this source
    confirms these artifacts are downloadable for debugging and adds
    `agent-stdio.log` (raw stdin/stdout) not in the compilation reference —
    see Extraction Notes for the naming discrepancy.
  - `docs-ghaw-network-reference.md` Claim 1 (`network:` field controls domain
    access; unspecified defaults to infrastructure-only): this source confirms
    the firewall-block debugging path (`DENIED CONNECT` log entries → add domain
    to `network.allowed`), consistent with the network reference's configuration
    guidance.
  - `docs-ghaw-audit-with-agents.md` Claim 1 (inside GitHub Actions, agents
    consume audit commands via the MCP tool, not the CLI directly): this source
    documents the CLI path for the same operations — confirming the two-path
    architecture: CLI for human practitioners, MCP tool for agent workflows in
    Actions.

- **Extends**:
  - `docs-ghaw-audit-with-agents.md` — that note documents how autonomous agent
    workflows consume `gh aw audit` JSON output via the MCP tool, with workflow
    specs and field schemas. This source documents the complementary CLI path
    for human practitioners doing active failure investigation. Together they
    give the full picture of the audit surface: automated consumption (MCP) and
    manual investigation (CLI).
  - `docs-ghaw-monitoring-patterns.md` — that note covers monitoring
    configuration (safe outputs for failure tracking, no-op control, Projects
    v2 integration). This source covers active debugging when those configurations
    signal a failure. Together they span the operational lifecycle: configure
    monitoring → observe failures → debug failures.
  - `docs-ghaw-compilation-process.md` — that note documents the agent job's
    artifact production (what artifacts are created and why). This source
    documents how practitioners download and use those artifacts for debugging
    (what artifacts to look at and how to interpret them). Together they give
    complete artifact lifecycle coverage.
  - `docs-ghaw-network-reference.md` — that note documents `network:` frontmatter
    for configuring domain egress. This source documents what to do when egress
    fails (look for `DENIED CONNECT` in `sandbox/firewall/logs/access.log`; add
    to `network.allowed` or use ecosystem shorthands). Configuration and debugging
    are complementary layers.

- **Contradicts**: None identified. The `gh aw health` command documented here
  ("a quick overview of workflow status across all workflows in a repository")
  sounds similar to `gh aw status` documented in `docs-ghaw-monitoring-patterns.md`
  Concrete Artifacts. Both provide repository-wide workflow status overviews. This
  could reflect two commands for similar purposes or possibly a renamed/updated
  command; the difference is not material enough to file a contradiction — it is
  noted here for the Assayer. No contradiction issue filed.

- **Novel**:
  - **AI-assisted debugging as primary recommended workflow** (Claims 1–3): No
    existing source note documents using the Copilot CLI `agentic-workflows` agent
    for debugging failures. The three-step procedure (launch → `/agent` → paste
    URL) is the first debugging workflow spec in the corpus.
  - **`gh aw mcp list` and `gh aw mcp inspect [--inspector]`** (no equivalent in
    `docs-ghaw-mcps.md` or any other note): CLI commands for listing and inspecting
    MCP server configurations are new to the corpus.
  - **`gh aw health`** (not in `docs-ghaw-monitoring-patterns.md`): Quick
    repository-wide workflow health overview command is new to the corpus.
  - **`agent-stdio.log` artifact** (not in `docs-ghaw-compilation-process.md`
    Claim 9's artifact inventory): The raw agent stdin/stdout log at
    `/tmp/gh-aw/` is a fifth artifact type not documented in the compilation
    reference — useful for debugging opaque agent reasoning.
  - **`sandbox/firewall/logs/access.log` path** (Claims 11): The specific path
    within the downloaded artifact for raw firewall access logs is new. The
    compilation doc documents the `firewall-audit-logs` artifact upload; this
    source adds the internal path for accessing the log file itself.
  - **`DEBUG` namespace system** (Claim 9): The specific namespace patterns
    (`cli:*`, `workflow:*`) for targeted debug logging are not documented in any
    other source note.
  - **`ACTIONS_STEP_DEBUG` for agentic workflows** (Claim 10): While
    `ACTIONS_STEP_DEBUG` is a standard GitHub Actions feature, no existing note
    applies it to the agentic workflow debugging context.
  - **`gh aw fix --write`** (Claim 13): Auto-remediation of compilation errors is
    not mentioned in `docs-ghaw-compilation-process.md` — which documents
    `--verbose` and `--strict` but not `--write` for fix application.

## Guide Impact

- **Chapter 05 (Observability & Feedback Loops)**:
  - Add the three-step Copilot CLI debugging workflow (Claims 1–3) as the
    recommended first-response procedure for agentic workflow failures. Frame
    it as practicing the platform's own agentic philosophy: use an agent to debug
    an agent. Document the exact `/agent` selector step — selecting
    `agentic-workflows` is what grants audit tool access.
  - Add the four-artifact inspection guide (Claim 12) as the systematic
    escalation path when AI-assisted debugging is insufficient: `prompt.txt` →
    `agent_output.json` → `agent-stdio.log` → `firewall-logs/`. This gives
    practitioners a clear escalation ladder from high-level to raw.

- **Chapter 02 (Harness Engineering)**:
  - Add `DEBUG=workflow:*` and `DEBUG=cli:*` (Claim 9) as the recommended local
    debugging commands for compilation failures. Document the stderr capture
    pattern (`2>&1 | tee debug.log`).
  - Add `gh aw fix --write` (Claim 13) as the auto-remediation path for
    compilation errors — document it alongside `--verbose` for the full
    compile-debug-fix loop.
  - Add `DENIED CONNECT domain:port` (Claim 8) as the canonical firewall-block
    symptom to document. Note the ecosystem shorthand approach (`ecosystem: node`,
    `ecosystem: python`) as the lower-friction fix for package-manager-dependent
    workflows.
  - Document `sandbox/firewall/logs/access.log` (Claim 11) as the raw firewall
    audit artifact path for compliance-level network review of runs.

- **Chapter 03 (Safety & Verification)**:
  - Add `sandbox/firewall/logs/access.log` as the canonical artifact for
    compliance-level network audit evidence. `gh aw audit` produces a summary;
    this file contains the complete raw log for security review or audit
    reporting.

- **Chapter 04 (Building Agent Systems)**:
  - Use the Copilot CLI `agentic-workflows` agent (Claims 1–3) as a concrete
    example of an agent-debugging-agent system in production: a purpose-built
    debugging agent with specialized tool access (`gh aw audit`, `gh aw logs`)
    and a bounded task (investigate one run, produce one fix). This pattern
    illustrates how to design specialized agents for operational tasks rather
    than building monolithic assistants.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The gh-aw documentation is a
   rendered SPA. WebFetch processes through an AI model rather than returning
   raw HTML. Three fetches were used to maximize content coverage and identify
   verbatim text. Verbatim quotes are used only where the processed output
   indicated direct quotation. CLI command examples are reproduced as-is since
   command syntax is not subject to paraphrasing.

2. **`agent-stdio.log` vs. `docs-ghaw-compilation-process.md` artifact inventory**:
   This page lists `agent-stdio.log` as an inspectable artifact; the compilation
   reference (Claim 9) lists five artifacts (`agent_output.json`, `agent_usage.json`,
   `prompt.txt`, `firewall-audit-logs`, `cache-memory/`) without mentioning
   `agent-stdio.log`. These are likely consistent — the compilation doc covers
   artifacts uploaded as named GitHub Actions artifacts; the debugging doc covers
   files at local paths within the runner. `agent-stdio.log` may be a local-only
   artifact not surfaced as a downloadable artifact in the compilation pipeline.
   Not filed as a contradiction but worth noting for the Assayer.

3. **`gh aw health` vs. `gh aw status`**: The debugging page documents `gh aw health`
   as providing "a quick overview of workflow status"; the monitoring-patterns note
   Concrete Artifacts documents `gh aw status` as "Status of all workflows in the
   repository." These may be the same command (renamed or aliased) or two commands
   for similar purposes. Both are documented by first-party sources. No contradiction
   filed — not enough detail to determine if these are conflicting claims or
   complementary commands.

4. **No publication date**: The documentation carries no explicit publication date.
   `date_published` left null. Content is consistent with current gh-aw platform
   state as of 2026-05-10.

5. **Sub-pages not followed**: The guide may link to referenced documentation
   (authentication docs, safe outputs docs, error docs). These were not followed;
   the focus was on the main debugging reference page.
