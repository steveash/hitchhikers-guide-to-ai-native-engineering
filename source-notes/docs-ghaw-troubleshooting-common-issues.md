---
source_url: https://github.github.com/gh-aw/troubleshooting/common-issues
source_type: docs
title: "GitHub Agentic Workflows: Common Issues"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#421"
---

# GitHub Agentic Workflows: Common Issues

> The first dedicated common-issues troubleshooting reference in the gh-aw corpus —
> catalogues specific installation, compilation, tool configuration, permission,
> engine, GHES, timeout, integrity filtering, and network failure modes with exact
> error messages and resolution steps, complementing the debugging *methodology*
> documented in `docs-ghaw-troubleshooting-debugging.md` with a *symptom catalogue*
> practitioners can scan for known issues.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `troubleshooting/common-issues`
  page — a practitioner reference in the `troubleshooting/` section, distinct from
  the `reference/` section (authoritative field specs) and the `troubleshooting/debugging`
  page (investigation methodology). Common-issues pages document known failure modes
  with enumerated causes and fixes; they are symptom-first rather than methodology-first.)
- **Author credibility**: First-party from GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — same team operating Peli de Halleux's agent factory).
  Error messages, CLI commands, YAML configuration examples, and enterprise policy
  guidance are authoritative for the `gh aw` platform. The GHES error table and
  Copilot license/inference diagnosis steps are platform-specific; the general
  patterns (silent config misspellings, staged-mode gotchas, integrity filtering)
  transfer to other agentic platforms.
- **Scope**: Covers seventeen issue categories spanning the full workflow lifecycle:
  installation, enterprise org policy, workflow compilation, import resolution,
  tool configuration, MCP server connections, Playwright integration, permission
  model, safe outputs, GitHub Projects, engine-specific, GHES, context expressions,
  build/test, network/connectivity, cache, integrity filtering, timeout errors, and
  debug logging. Does NOT cover: the general debugging methodology (see
  `docs-ghaw-troubleshooting-debugging.md`), audit CLI reference (see
  `docs-ghaw-audit-with-agents.md`), network configuration reference (see
  `docs-ghaw-network-reference.md`), staged mode reference (see
  `docs-ghaw-staged-mode-reference.md`), or permissions model (see
  `docs-ghaw-permissions-reference.md`).

## Extracted Claims

### Claim 1: Enterprise organization policies may block gh-aw installation with a specific error about disallowed Actions; the fix is adding `github/gh-aw@*` to the org's allowed-actions list or a centralized policy file

- **Evidence**: The page documents two fix options. Option 1 is an org-level UI
  change (Settings → Actions → "Allow select actions" → add pattern). Option 2 is
  adding the pattern to a centralized `policies/actions.yml` file with an
  `allowed_actions:` block.
- **Confidence**: settled (first-party; the error message and fix path are
  authoritative for GitHub Enterprise organizations)
- **Quote**: "The action github/gh-aw/actions/setup@[hash] is not allowed in {ORG}
  because all actions must be from a repository owned by your enterprise, created by
  GitHub, or verified in the GitHub Marketplace."
- **Our assessment**: This is the most common enterprise deployment blocker — it
  surfaces before any workflow execution, during the Actions runner setup phase. The
  centralized policy file approach (Option 2) is the right choice for organizations
  managing many repositories, since it avoids per-repo settings drift. For Ch02
  (Harness Engineering): document the `github/gh-aw@*` allowlist entry as a
  prerequisite check for enterprise gh-aw deployments. The wildcard pattern covers
  all future action versions without requiring policy updates on each release.

### Claim 2: The gh-aw compiler silently ignores misspelled frontmatter fields without any warning — common mistakes include `agent:` instead of `engine:`, `mcp-servers:` instead of `tools:` with MCP config, `tool-sets:` instead of `toolsets:`, and `allowed_repos:` instead of `allowed-repos:`

- **Evidence**: The page states the cause explicitly: "Field name misspellings;
  compiler doesn't warn about unknown fields." Four specific misspelling examples
  are enumerated with the correct field names alongside each.
- **Confidence**: settled (first-party; the compiler behavior and correct field
  names are authoritative)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Silent field ignoring is a particularly treacherous failure
  mode because the workflow compiles and runs successfully — the configuration just
  has no effect. A practitioner who writes `agent: copilot` instead of
  `engine: copilot` will see the workflow run without the intended engine
  configuration, with no error to diagnose. The fix is `gh aw compile --verbose`
  to confirm parsed settings. For Ch02: document the exact misspelling table and
  recommend `--verbose` as a compile-time sanity check for new workflows. This is
  a configuration-layer hazard that generic YAML linters will not catch, since the
  unknown fields are syntactically valid YAML.

### Claim 3: `gh aw compile --purge` removes orphaned `.lock.yml` files that remain after their source `.md` workflows have been deleted

- **Evidence**: The page documents this as the fix for "Orphaned Lock Files" under
  the compilation issues section. No further detail on detection mechanism.
- **Confidence**: settled (first-party; CLI command is authoritative)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Orphaned lock files are a maintenance hazard — they reference
  workflow source files that no longer exist, but GitHub Actions may still attempt
  to run them if the lock file remains in `.github/workflows/`. `--purge` is the
  recommended cleanup command. This pairs with `docs-ghaw-compilation-process.md`
  Claim 13's benchmark context: even on large repos with many workflows, `--purge`
  runs at normal compilation speeds. For Ch02: document `gh aw compile --purge`
  as a recommended cleanup step when deleting workflows, analogous to removing
  compiled artifacts when deleting source files.

### Claim 4: GitHub tool access in gh-aw requires an explicit `toolsets:` declaration under `tools.github:` — omitting it means GitHub tools are not available to the agent

- **Evidence**: The page documents this under "GitHub Tools Not Available" with
  a YAML configuration example showing the required structure. The fix section
  additionally notes that `gh aw mcp inspect <workflow>` can diagnose which toolsets
  are configured.
- **Confidence**: settled (first-party; configuration requirement is authoritative)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `toolsets:` requirement means GitHub tool access is
  opt-in at a granular level — practitioners must specify which toolset groups
  (e.g., `[repos, issues]`) the agent needs. This is the per-capability expression
  of the zero-capability-by-default principle. For Ch02: document the `toolsets:`
  declaration as a required step when workflows need GitHub API access, and list
  the available toolset categories. The absence of an explicit `toolsets:` block is
  a common cause of "tool not found" errors without an obvious error message.

### Claim 5: The Playwright MCP server fails to initialize with an EOF error when running on versions before 0.41.0 due to missing Docker security flags that prevent Chromium from starting

- **Evidence**: Specific error message documented: "Failed to register tools
  error='initialize: EOF' name=playwright". Root cause identified: "Chromium crashes
  before tool registration; missing Docker security flags." Fix: upgrade to version
  0.41.0+ via `gh extension upgrade gh-aw`.
- **Confidence**: settled (first-party; the version fix and root cause are
  authoritative)
- **Quote**: "Failed to register tools error='initialize: EOF' name=playwright"
- **Our assessment**: The EOF error at tool registration time is opaque — it
  doesn't directly indicate "Chromium crashed" without knowing this documented root
  cause. The 0.41.0 version boundary is the critical diagnostic: if the error
  appears, check the installed version before any other investigation. For Ch02:
  document this as a known version-dependent failure and add version checking as
  the first step in Playwright MCP troubleshooting.

### Claim 6: "Cannot find module 'playwright'" indicates the workflow is incorrectly attempting to use Playwright as an npm package rather than through the MCP tools — the fix is using `mcp__playwright__` prefixed MCP tool calls instead

- **Evidence**: The error is named exactly as an npm module resolution failure.
  Cause documented: "Playwright provided as MCP tools, not npm package." Example
  fix: use `await mcp__playwright__browser_navigate()` instead of
  `require('playwright')`.
- **Confidence**: settled (first-party; the correct usage pattern is documented)
- **Quote**: "Error: Cannot find module 'playwright'"
- **Our assessment**: This error reflects the architectural difference between
  Playwright as a browser automation library (npm package) and Playwright as a gh-aw
  tool (MCP server exposing browser actions). The gh-aw Playwright integration is
  always via the MCP gateway — the agent cannot import npm packages directly in
  the agentic execution context. For Ch02: when documenting Playwright integration,
  explicitly note that the `mcp__playwright__` MCP tool call pattern is required,
  and that npm require/import will fail.

### Claim 7: OpenCode/Crush MCP integration requires specific configuration gotchas: API proxy on port 10004 with `MCP_GATEWAY_PORT` placeholder, `agent.build.permission` (singular not plural), `external_directory: allow` for outside-workspace access, no `/v1` suffix on Copilot-compatible endpoints, and `COPILOT_GITHUB_TOKEN` for `--enable-api-proxy` execution

- **Evidence**: Seven specific gotchas are enumerated on the page under "OpenCode/Crush
  MCP Tools Not Being Called." The symptom is runs completing without calling MCP
  tools or file tools despite correct-looking configuration.
- **Confidence**: emerging (first-party; this is a collection of configuration
  gotchas likely discovered through practitioner pain; the details are authoritative
  but may evolve as the integration matures)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The volume of configuration gotchas for OpenCode/Crush
  integration suggests this is a relatively complex integration requiring careful
  setup. The silent failure mode (runs complete without calling tools) makes it
  especially hard to diagnose without this reference. The `MCP_GATEWAY_PORT`
  placeholder requirement (rather than a hardcoded port) is architecturally
  important — it means the gateway port can be dynamically assigned at runtime.
  For Ch02: OpenCode/Crush integration deserves a dedicated configuration checklist
  given the number of independent failure points.

### Claim 8: All write operations in gh-aw workflows are blocked at the platform level — the `safe-outputs` system is the only path for creating issues, adding comments, updating PRs, or any other GitHub state modification

- **Evidence**: The page states the cause as "Agentic workflows have no direct write
  access" and documents the safe-outputs YAML configuration with four named output
  types: `create-issue`, `add-comment`, `update-issue`, with a `title-prefix` and
  `labels` for issue creation.
- **Confidence**: settled (first-party; this is a core platform architectural
  property, consistent with `docs-ghaw-permissions-reference.md` Claim 1 and
  `docs-ghaw-how-they-work.md` conceptual documentation)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This troubleshooting entry serves as the "learn by failure"
  path to the permissions model — practitioners who attempt direct GitHub API calls
  from within their agent instructions will hit this failure and arrive here.
  The platform blocks writes structurally, not conditionally; there is no flag to
  enable direct write access. For Ch03 (Safety and Verification): this platform
  constraint is a safety feature — it ensures every write is mediated by the
  Safe Outputs validation pipeline. Document it prominently as a "you will hit this"
  onboarding blocker.

### Claim 9: When staged mode is enabled, `safe-outputs` entries appear as step-summary previews but do not execute — workflows that should create issues will silently not do so until `staged: false` is explicitly set

- **Evidence**: The page documents "Safe Outputs Not Creating Issues" as a common
  issue, with staged mode as the cause and `staged: false` in the YAML as the fix.
  A complete YAML example shows the correct placement of `staged: false` at the
  root of `safe-outputs:` alongside the output type configuration.
- **Confidence**: settled (first-party; consistent with `docs-ghaw-staged-mode-reference.md`
  Claim 1 which establishes that staged mode replaces all writes with previews)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is the expected behavior of staged mode working as
  designed — the common-issues page surfaces it here because practitioners who
  enable staged mode for testing and then forget to disable it experience it as
  a failure. The "silent no-write" appearance is intentional (staged mode is a
  dry-run mechanism), but it becomes an issue when the practitioner has forgotten
  staged mode is active. For Ch02: document staged mode state as the first check
  when safe-outputs appear to be running but producing no GitHub output.

### Claim 10: GitHub Projects v2 reserves certain field names (including `REPOSITORY`) that cannot be used as custom project fields — workflows using these names must switch to alternatives like `repo`, `source_repository`, or `linked_repo`

- **Evidence**: The page documents "Project Field Type Errors" with `REPOSITORY`
  as the specific reserved name example. Three alternative field name suggestions
  are provided.
- **Confidence**: settled (first-party; the reserved field name is a GitHub Projects
  v2 API constraint)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is a GitHub Projects v2 API constraint that surfaces
  at workflow runtime, not at compile time — `gh aw compile` cannot validate field
  names against the Projects API. The practical implication for workflow authors:
  avoid using GitHub's internal entity names as custom field names. For Ch02:
  when documenting the `update-project` safe output, note the reserved field name
  constraint and recommend descriptive alternatives.

### Claim 11: Copilot engine failures caused by missing license or inference access produce silent workflow failures — diagnosis requires testing locally with `COPILOT_GITHUB_TOKEN` and running `copilot -p "write a haiku"` to verify the PAT owner's subscription status

- **Evidence**: The page documents "Copilot License or Inference Access Issues"
  with a specific local diagnosis command. Root cause: "PAT owner lacks Copilot
  license or inference access." Symptom: "Workflow fails at Copilot inference
  step despite correct token." Resolution: contact org admin for active subscription.
- **Confidence**: settled (first-party; the diagnosis procedure is authoritative)
- **Quote**: (no direct quote; the local test command uses
  `export COPILOT_GITHUB_TOKEN="<your-github-pat>"` and `copilot -p "write a haiku"`)
- **Our assessment**: The local test approach is significant: it allows practitioners
  to isolate whether the failure is in the gh-aw harness or in the Copilot
  subscription/license layer, without deploying a workflow. If the local `copilot`
  invocation fails with the same token, the issue is the subscription, not the
  workflow configuration. Organization-managed licenses may have additional API
  restrictions that affect inference access even when a seat is assigned. For Ch02:
  document the local Copilot inference test as the authentication isolation step
  for Copilot engine workflows.

### Claim 12: GitHub Enterprise Server deployments require `api-target` in the engine block plus GitHub Connect enabled, and have a specific error message table mapping GHES-specific failures to their causes and fixes

- **Evidence**: The page documents GHES prerequisites in two layers (site admin and
  enterprise/org admin) and provides a six-row error table. The workflow YAML example
  shows the `api-target: api.enterprise.githubcopilot.com` configuration alongside
  `network.allowed` entries for the enterprise Copilot endpoint.
- **Confidence**: settled (first-party; GHES requirements and error messages are
  authoritative)
- **Quote**: "Error loading models: 400 Bad Request" (GHES error: Copilot not
  licensed or GitHub Connect disabled)
- **Our assessment**: The GHES error table is high-value reference material because
  GHES deployments encounter a distinct failure surface from cloud GitHub — the same
  configuration that works on github.com may fail on GHES for unrelated reasons
  (GitHub Connect not enabled, enterprise-specific Copilot licensing, different API
  target). The "Could not resolve to a Repository" error caused by missing `GH_HOST`
  is particularly non-obvious. For Ch02: document GHES as a distinct deployment
  context requiring explicit `api-target` configuration and GitHub Connect as a
  prerequisite.

### Claim 13: Context expressions `secrets.*` and `env.*` are disallowed in gh-aw workflow frontmatter — only specific allowed expressions like `github.event.issue.number`, `github.repository`, and `steps.sanitized.outputs.text` can be used

- **Evidence**: The page documents this under "Unauthorized Expression" with specific
  examples of allowed expressions. The disallowed categories are named explicitly.
- **Confidence**: settled (first-party; expression allowlist is a compile-time
  validation constraint)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The expression restriction is a compile-time security control
  that prevents secrets exfiltration via context injection — an agent cannot access
  `secrets.MY_SECRET` directly through an expression because those expressions are
  blocked at the frontmatter level. Similarly, `env.*` is blocked to prevent
  environment variable leakage. For Ch03: document the expression allowlist as a
  compile-time injection defense, noting that the allowed set (`github.event.*`,
  `steps.sanitized.outputs.text`) is scoped to event data that has already gone
  through input sanitization.

### Claim 14: `steps.sanitized.outputs.text` returns nothing unless the triggering event is an issue, pull request, or comment event — workflows triggered by `push:` or `workflow_dispatch:` will find this context variable empty

- **Evidence**: The page documents this under "Sanitized Context Empty" with explicit
  cause ("Requires issue/PR/comment events") and fix ("Use `on: issues:` trigger
  instead of `push:` or similar").
- **Confidence**: settled (first-party; event-type requirement is a platform
  constraint)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is a non-obvious constraint — the sanitized context output
  is scoped to event types where user-provided text is present (issue body, PR body,
  comment text). A workflow that triggers on `push:` doesn't have user-supplied
  content to sanitize, so the output is empty. For Ch02: when documenting the
  sanitized context variable, include the event type scope constraint as a primary
  qualifier, not a footnote.

### Claim 15: Public repositories automatically apply `min-integrity: approved` to GitHub tool access, which blocks unapproved external contributors' issues, PRs, and comments from being visible to triage workflows — teams must explicitly set `min-integrity: none` (for fully validating workflows) or `min-integrity: unapproved` as a middle ground

- **Evidence**: The page documents this under "Integrity Filtering Blocking Expected
  Content." The symptom is that triage workflows don't process community contributions.
  Cause: "Public repositories auto-apply `min-integrity: approved`."
- **Confidence**: settled (first-party; the auto-applied default is a platform
  specification for public repos)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This is a significant default behavior change for public repos
  — a triage workflow that works in a private repo may silently skip all external
  contributor input in a public repo because of this auto-applied filter. The default
  protects against prompt injection from untrusted contributors, but practitioners
  running legitimately open triage workflows need to explicitly opt out. The
  `min-integrity: unapproved` middle ground lets in unapproved content while still
  blocking anonymous contributions. For Ch03: document the `min-integrity` public
  repo default as a security behavior practitioners need to understand before
  deploying open-source triage workflows. For Ch02: document it as a deployment
  context difference between private and public repos.

### Claim 16: Timeout errors in gh-aw workflows require different configuration parameters depending on the failure type and engine — five distinct settings span the timeout surface: `timeout-minutes` (job level), `tools.timeout` (per tool call), `tools.startup-timeout` (MCP server startup), `max-turns` (Claude), and `max-continuations` (Copilot)

- **Evidence**: The page provides a six-row error table mapping specific error
  patterns to the correct setting for each engine. The default job timeout is 20
  minutes. The table covers All engines, Claude-specific, Codex-specific, and
  Copilot-specific timeout types.
- **Confidence**: settled (first-party; the timeout setting names and their scopes
  are authoritative configuration references)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the table maps:
  "Job exceeded maximum execution time" → `timeout-minutes: N`; "Bash tool timed
  out after 60 seconds" [Claude] → `tools: timeout: N`; "Reached maximum number
  of turns" [Claude] → `max-turns: N`; "Tool call timed out after 120 seconds"
  [Codex] → `tools: timeout: N`; "Task incomplete, workflow succeeds" [Copilot] →
  `max-continuations: N`; "Failed to register tools (timeout)" [Any] →
  `tools: startup-timeout: N`)
- **Our assessment**: The five-parameter timeout surface reflects the multi-layer
  execution model: the GitHub Actions job has its own timeout; within the job,
  individual tool calls have timeouts; MCP server startup has a separate timeout;
  and the AI engine itself has turn/continuation limits. A "job exceeded time limit"
  error may require raising `timeout-minutes`, but the right fix depends on which
  inner limit was actually hit. For Ch02: present the timeout settings as a
  structured table mapping error patterns to the correct parameter, not as an
  unordered list of knobs.

### Claim 17: Ecosystem identifiers (`node`, `python`, `containers`, `go`) in `network.allowed` expand to curated domain sets covering all commonly needed registries for each package manager — using these shorthands prevents needing to manually enumerate individual registry domains

- **Evidence**: The page documents four ecosystem identifiers with their package
  manager associations: `node` (npm), `python` (PyPI), `containers` (Docker),
  `go` (Go modules). Also documented: `defaults` for basic infrastructure domains.
- **Confidence**: settled (first-party; the ecosystem identifier names and their
  associations are documented in both this source and the network reference)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Ecosystem identifiers are the high-leverage approach for
  workflows that need package manager access — a single `node` identifier grants
  access to the full npm ecosystem rather than requiring practitioners to enumerate
  registry.npmjs.org, cdn.npmjs.com, and related domains individually. This
  corroborates the network reference (Claim 1 and the ecosystem identifier section)
  from the troubleshooting/common-issues context. For Ch02: recommend ecosystem
  identifiers as the default approach over individual domain allowlisting when
  standard package managers are needed.

### Claim 18: Domains not in the network allowed list appear as `(redacted)` in workflow logs — adding the domain to `network.allowed` reveals the actual URL in subsequent runs

- **Evidence**: The page documents this under "URLs Appearing as '(redacted)'" in
  the network issues section. The fix is adding the domain to `network.allowed`.
- **Confidence**: settled (first-party; this is a described platform behavior, not
  a workaround)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: URL redaction is a privacy/security feature of the Agent
  Workflow Firewall — domains not in the allow list have their URLs scrubbed in
  logs to prevent information leakage about external services the workflow attempted
  to reach. Practitioners who see `(redacted)` in their logs have an indicator that
  network access was attempted to an unlisted domain. For Ch03: document URL
  redaction as an intended security behavior that also serves as a diagnostic
  indicator — it reveals that the workflow is attempting outbound access to an
  unlisted domain.

### Claim 19: The `DEBUG` namespace system supports negation syntax (`DEBUG=*,-workflow:test`) to exclude specific loggers, in addition to multi-namespace patterns — output shows namespace, message, and elapsed time on stderr

- **Evidence**: The page documents the negation syntax alongside the standard
  patterns (`DEBUG=*`, `DEBUG=workflow:*`, `DEBUG=workflow:*,cli:*`). Common
  namespaces listed: `cli:compile_command`, `workflow:compiler`,
  `workflow:expression_extraction`, `parser:frontmatter`.
- **Confidence**: settled (first-party; the namespace syntax is a documented CLI
  feature)
- **Quote**: (no direct quote; see paraphrase in Our assessment — one fetch
  returned: "Output goes to stderr; shows namespace, message, and elapsed time")
- **Our assessment**: The negation syntax (`-namespace:pattern`) extends the basic
  namespace filtering in a practically important way: when `DEBUG=*` is too noisy,
  practitioners can exclude specific verbose namespaces without needing to enumerate
  all the ones they want. The `parser:frontmatter` namespace is particularly useful
  for diagnosing the silent field-misspelling issue (Claim 2) — it shows exactly
  which frontmatter fields were parsed. This claim extends `docs-ghaw-troubleshooting-debugging.md`
  Claim 9's documentation of the basic `DEBUG` patterns by adding the negation form
  and the named common namespaces.

### Claim 20: The AI-assisted debugging command on the common-issues page uses a direct command syntax (`/agent agentic-workflows debug <url>`) as well as a generic agent path referencing a `debug.md` runbook URL, as alternative debugging entry points

- **Evidence**: The page documents two specific debugging invocation forms under
  "Why Did My Workflow Fail?": the Copilot Chat form
  `/agent agentic-workflows debug https://github.com/OWNER/REPO/actions/runs/RUN_ID`
  and the generic agent form
  `Debug this workflow run using https://raw.githubusercontent.com/github/gh-aw/main/debug.md`.
- **Confidence**: emerging (first-party command syntax; the `debug.md` runbook URL
  is specific but may change; the direct `/agent` command form is more stable)
- **Quote**: "/agent agentic-workflows debug https://github.com/OWNER/REPO/actions/runs/RUN_ID"
- **Our assessment**: The `debug.md` runbook URL approach is notable because it
  enables AI-assisted debugging without the Copilot CLI — any coding agent that
  can fetch URLs can use it. This is the generic/portable version of the Copilot
  CLI procedure documented in `docs-ghaw-troubleshooting-debugging.md` Claims 1–3.
  For Ch04 (Building Agent Systems): the `debug.md` runbook pattern is an example
  of encoding debugging procedures as agent-consumable markdown — a transferable
  design pattern for operational runbooks across agentic platforms.

## Concrete Artifacts

### Extension Installation Standalone Installer

```bash
# Install gh-aw extension (when gh extension install github/gh-aw fails)
curl -sL https://raw.githubusercontent.com/github/gh-aw/main/install-gh-aw.sh | bash

# Install specific version
curl -sL https://raw.githubusercontent.com/github/gh-aw/main/install-gh-aw.sh | bash -s -- v0.40.0

# Verify installation
gh extension list
```

*Source: gh-aw troubleshooting/common-issues, "Extension Installation Fails" section*

### Enterprise Organization Policy Fix

```yaml
# Option 2: Centralized policy file (policies/actions.yml)
allowed_actions:
  - "actions/*"
  - "github/gh-aw@*"
```

Fix via UI: Organizations/{ORG}/settings/actions → Allow select actions → Add `github/gh-aw@*`

*Source: gh-aw troubleshooting/common-issues, "Custom Actions Not Allowed in Enterprise Organizations" section*

### Frontmatter Field Misspelling Reference

```
Common misspellings (all silently ignored by compiler):

  WRONG              → CORRECT
  agent:             → engine:
  mcp-servers:       → tools: (with MCP configuration nested inside)
  tool-sets:         → toolsets: (under tools.github:)
  allowed_repos:     → allowed-repos: (under tools.github:)

Diagnosis: gh aw compile --verbose  # confirms parsed settings
```

*Source: gh-aw troubleshooting/common-issues, "Frontmatter Field Not Taking Effect" section*

### GitHub Tools Configuration

```yaml
tools:
  github:
    toolsets: [repos, issues]
```

Inspect: `gh aw mcp inspect <workflow>`

*Source: gh-aw troubleshooting/common-issues, "GitHub Tools Not Available" section*

### Safe Outputs Configuration (Staged Mode Disabled)

```yaml
safe-outputs:
  staged: false
  create-issue:
    title-prefix: "[bot] "
    labels: [automation]
  add-comment: {}
  update-issue: {}
```

*Source: gh-aw troubleshooting/common-issues, "Write Operations Fail" and "Safe Outputs Not Creating Issues" sections*

### GitHub Projects Reserved Field Fix

```yaml
safe-outputs:
  update-project:
    fields:
      repo: "myorg/myrepo"   # NOT: REPOSITORY (reserved)
      # alternatives: source_repository, linked_repo
```

*Source: gh-aw troubleshooting/common-issues, "Project Field Type Errors" section*

### Copilot Local Inference Test

```bash
# Test whether PAT owner has active Copilot subscription
export COPILOT_GITHUB_TOKEN="<your-github-pat>"
copilot -p "write a haiku"
# If this fails, the issue is Copilot subscription/licensing, not workflow config
```

*Source: gh-aw troubleshooting/common-issues, "Copilot License or Inference Access Issues" section*

### GHES Engine Configuration

```yaml
engine:
  id: copilot
  api-target: api.enterprise.githubcopilot.com
network:
  allowed:
    - defaults
    - api.enterprise.githubcopilot.com
```

*Source: gh-aw troubleshooting/common-issues, "Copilot Engine Prerequisites on GHES" section*

### GHES Error Reference Table

```
Error                                          | Cause                                         | Fix
-----------------------------------------------|-----------------------------------------------|--------------------------------
Error loading models: 400 Bad Request          | Copilot not licensed or GitHub Connect off    | Enable GitHub Connect + enterprise Copilot
403 "unauthorized: not licensed to use Copilot"| No Copilot seat for PAT owner                 | Assign seat to token owner
403 "Resource not accessible by personal       | Wrong token type or missing permissions       | Use fine-grained PAT with
    access token"                              |                                               | Copilot Requests: Read scope
Could not resolve to a Repository             | GH_HOST not set in custom jobs                | Recompile or set explicitly
Firewall blocking API                         | Domain not in allowed list                    | Add to network.allowed
gh aw add-wizard creates PR on github.com     | Not inside GHES repo clone                    | Run from GHES repo
```

*Source: gh-aw troubleshooting/common-issues, "Copilot GHES - Common Error Messages" section*

### Integrity Filtering Configuration

```yaml
# Public repos auto-apply min-integrity: approved (blocks external contributors)
# For triage workflows that process community input:
tools:
  github:
    min-integrity: none      # Allow all contributors (use only when validating input)
    # OR
    min-integrity: unapproved  # Middle ground: allows unapproved but not anonymous
```

*Source: gh-aw troubleshooting/common-issues, "Integrity Filtering Blocking Expected Content" section*

### Timeout Configuration Reference

```yaml
timeout-minutes: 60     # GitHub Actions job-level timeout (default: 20)
tools:
  timeout: 600          # Per-tool-call timeout in seconds
  startup-timeout: 300  # MCP server startup timeout in seconds
max-turns: 30           # Claude max turns (engine-specific)
max-continuations: 5    # Copilot max continuations (engine-specific)
```

Error → Setting mapping:
```
"Job exceeded maximum execution time"          → timeout-minutes: N    (all engines)
"Bash tool timed out after 60 seconds"         → tools: timeout: N     (Claude)
"Reached maximum number of turns"             → max-turns: N          (Claude)
"Tool call timed out after 120 seconds"       → tools: timeout: N     (Codex)
"Task incomplete, workflow succeeds"           → max-continuations: N  (Copilot)
"Failed to register tools (timeout)"          → tools: startup-timeout: N (any)
```

*Source: gh-aw troubleshooting/common-issues, "Timeout Errors" section*

### Network Ecosystem Identifiers

```yaml
network:
  allowed:
    - defaults     # Basic infrastructure domains
    - node         # npm registry (npmjs.org, cdn.npmjs.com, etc.)
    - python       # PyPI (pypi.org, files.pythonhosted.org, etc.)
    - containers   # Docker Hub and registries
    - go           # Go module proxy and sum database
```

*Source: gh-aw troubleshooting/common-issues, "Firewall Denials for Package Registries" section*

### Cache Configuration Reference

```yaml
# Cache not restoring (key mismatch or 7-day expiry)
cache:
  key: deps-${{ hashFiles('package-lock.json') }}
  restore-keys: deps-

# Cache memory not persisting across runs
tools:
  cache-memory:
    key: memory-${{ github.workflow }}-${{ github.run_id }}
```

*Source: gh-aw troubleshooting/common-issues, "Cache Not Restoring" and "Cache Memory Not Persisting" sections*

### Advanced DEBUG Patterns

```bash
# Standard patterns
DEBUG=* gh aw compile                             # all logs
DEBUG=workflow:* gh aw compile my-workflow       # workflow compilation only
DEBUG=workflow:*,cli:* gh aw compile my-workflow  # multiple namespaces
DEBUG=*,-workflow:test gh aw compile              # exclude specific namespace (negation)
DEBUG_COLORS=0 DEBUG=* gh aw compile 2>&1 | tee debug.log  # capture without colors

# Common namespaces:
#   cli:compile_command
#   workflow:compiler
#   workflow:expression_extraction
#   parser:frontmatter
```

*Source: gh-aw troubleshooting/common-issues, "Enable Debug Logging" section*

### AI-Assisted Debugging Entry Points

```
# Using Copilot Chat (requires agentic-workflows agent):
/agent agentic-workflows debug https://github.com/OWNER/REPO/actions/runs/RUN_ID

# Using any coding agent with the debug.md runbook:
Debug this workflow run using https://raw.githubusercontent.com/github/gh-aw/main/debug.md

# Manual investigation commands:
gh aw audit <run-id>
gh aw logs
# Inspect .lock.yml for compiled configuration
```

*Source: gh-aw troubleshooting/common-issues, "Why Did My Workflow Fail?" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-permissions-reference.md` Claim 1 ("GitHub Agentic Workflows uses
    read-only permissions by default for security, with write operations handled
    through safe outputs"): Claim 8 here surfaces the same constraint from the
    troubleshooting angle — practitioners who attempt direct writes encounter a
    platform-level block. Both sources confirm write operations are exclusively
    routed through safe-outputs. The common-issues page adds the YAML fix pattern
    for practitioners arriving via the failure path.
  - `docs-ghaw-staged-mode-reference.md` Claim 1 (staged mode "runs the workflow
    completely while skipping every write operation, replacing each with a structured
    preview"): Claim 9 here documents the troubleshooting manifestation of this
    behavior — practitioners who forget staged mode is active see safe-outputs that
    appear to run but create no GitHub output. The two sources together give the
    complete lifecycle: "how staged mode works" (reference) and "why your issues
    aren't being created" (common issues).
  - `docs-ghaw-network-reference.md` Claim 1 ("The `network` field controls domain
    access for AI engines during workflow execution. When unspecified, it defaults
    to `network: defaults`, allowing only basic infrastructure domains"): Claims
    17 and 18 here document the troubleshooting surface of the same behavior —
    practitioners see package download failures (ecosystem identifiers) and URL
    redaction in logs (unallowed domain access). The three claims together give
    configuration reference + troubleshooting symptoms + diagnostic indicator.
  - `docs-ghaw-troubleshooting-debugging.md` Claim 9 (DEBUG env var namespace
    patterns `cli:*`, `workflow:*` for targeted logging): Claim 19 here extends
    this with the negation syntax (`DEBUG=*,-namespace`) and documents the common
    useful namespace names (`parser:frontmatter`, `workflow:expression_extraction`).
    Both sources confirm `DEBUG` namespaces as the primary local diagnostic tool.
  - `docs-ghaw-troubleshooting-debugging.md` Claims 1–3 (AI-assisted debugging
    via Copilot CLI as primary recommendation): Claim 20 here documents the
    compact `/agent agentic-workflows debug <url>` command form and the
    agent-agnostic `debug.md` runbook alternative. Both sources converge on
    AI-assisted debugging as the recommended first-response for workflow failures.

- **Extends**:
  - `docs-ghaw-troubleshooting-debugging.md` — that note documents the debugging
    *methodology* (three-step Copilot CLI workflow, CLI diagnostic commands,
    advanced manual techniques). This source documents the *symptom catalogue*
    (known failure modes with specific causes and fixes). Together they form a
    complete troubleshooting guide: "here is how to investigate failures" (debugging)
    and "here are the specific failures you may encounter" (common issues).
  - `docs-ghaw-network-reference.md` — that note documents the `network:` field
    configuration reference. Claims 17 and 18 here add the troubleshooting
    perspective: what practitioners see when network access fails (firewall denials
    for package managers, URL redaction) and which ecosystem identifiers to use for
    each package manager type.
  - `docs-ghaw-compilation-process.md` — that note documents compilation internals
    and performance. Claim 2 here adds a critical runtime hazard not documented in
    the compilation reference: the compiler silently ignores unknown frontmatter
    fields. `--verbose` is the recommended diagnostic. This gap between "how
    compilation works" and "what can go wrong silently" is important for Ch02.
  - `docs-ghaw-staged-mode-reference.md` — that note documents staged mode syntax
    and behavior. Claim 9 here documents the operational gotcha: staged mode
    preventing issue creation is a common source of confusion, not an error state.
    The two together give the full practitioner picture.

- **Contradicts**: None identified. All claims are consistent with existing source
  notes. Two items worth noting for the Assayer without rising to the contradiction
  threshold:
  - **`gh aw compile --purge` not in `docs-ghaw-compilation-process.md`**: The
    compilation reference documents `--verbose`, `--strict`, `--no-emit`, and
    security scanner flags but does not mention `--purge`. This source adds `--purge`
    as a maintenance command. Not contradictory — an omission in the reference, not
    a conflict.
  - **Cache 7-day expiry not documented in `docs-ghaw-compilation-process.md`**:
    The compilation reference documents `cache-memory/` as an artifact retained
    for 90 days. The 7-day cache expiry here refers to the GitHub Actions cache
    (via the `cache:` configuration block), not the `cache-memory/` artifact — these
    are different cache mechanisms. Not contradictory — different systems.

- **Novel**:
  - **Silent frontmatter field misspelling** (Claim 2): No existing source note
    documents that the compiler silently ignores unknown frontmatter fields. The
    specific misspelling table (`agent:` → `engine:`, `tool-sets:` → `toolsets:`,
    etc.) is entirely new to the corpus and has direct Ch02 harness engineering
    implications.
  - **`gh aw compile --purge`** (Claim 3): Not documented in
    `docs-ghaw-compilation-process.md` or any other existing note. New maintenance
    command for the corpus.
  - **Playwright EOF initialization failure and version boundary** (Claim 5):
    No existing note documents the `error='initialize: EOF' name=playwright` error
    or the v0.41.0 fix. This is the first corpus entry for Playwright MCP
    troubleshooting.
  - **Playwright `Cannot find module` error** (Claim 6): No existing note
    distinguishes Playwright as MCP tools vs. npm package. This is a first corpus
    entry for this architectural clarification.
  - **OpenCode/Crush MCP configuration gotchas** (Claim 7): No existing note
    documents the seven-point configuration checklist for OpenCode/Crush
    integration. New to corpus.
  - **`min-integrity` public repo default and community contribution blocking**
    (Claim 15): The `min-integrity` feature is mentioned in weekly blog notes
    but no existing source note documents the auto-applied `min-integrity: approved`
    default for public repos and its impact on open-source triage workflows. Novel
    and high-impact for Ch03 safety documentation.
  - **Five-parameter timeout surface with engine-specific error-to-setting mapping**
    (Claim 16): No existing note documents the full timeout configuration space or
    the error-to-setting mapping table. Novel reference material for Ch02.
  - **URL redaction as diagnostic indicator** (Claim 18): The `(redacted)` log
    behavior is not documented in `docs-ghaw-network-reference.md` (first 60 lines
    read). Novel to corpus.
  - **GHES error table** (Claim 12): No existing note documents GHES-specific
    error messages with their causes. Novel deployment context documentation.
  - **Context expression restrictions** (Claims 13–14): No existing note explicitly
    documents the `secrets.*` / `env.*` disallowed expression set or the
    `steps.sanitized.outputs.text` event-type scope constraint. Novel to corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add silent frontmatter misspelling table (Claim 2) as a "common configuration
    gotchas" reference. This is the single highest-impact onboarding hazard: invalid
    config silently ignored with no error. Recommend `--verbose` as a development
    practice. Specific field name corrections (`engine:` not `agent:`, `toolsets:`
    not `tool-sets:`) should appear in the guide alongside the configuration reference.
  - Add the five-parameter timeout table (Claim 16) as a structured reference.
    Currently no guide chapter documents the full timeout surface. Practitioners
    diagnosing slow or incomplete workflows need to match their error message to the
    right parameter.
  - Document staged mode as the first check for "safe-outputs running but no output
    appears" (Claim 9). The guide should explicitly connect staged mode → no-write
    behavior as expected, not broken.
  - Add `gh aw compile --purge` (Claim 3) to workflow maintenance procedures.
  - Add GHES deployment as a distinct configuration context (Claim 12) requiring
    `api-target` and GitHub Connect. The current corpus has no GHES-specific guide
    content.
  - Add `min-integrity` public/private default difference (Claim 15) as a deployment
    context note — the same workflow may behave differently on public vs. private
    repos without any code change.

- **Chapter 03 (Safety and Verification)**:
  - Add `min-integrity: approved` public repo default (Claim 15) to the safety
    defaults section. This is a platform-enforced protection against prompt injection
    from untrusted external contributors that practitioners need to understand before
    deploying open-source workflows. Document `min-integrity: none` as the deliberate
    opt-out for fully validating triage workflows.
  - Add URL redaction (Claim 18) as a documented security behavior — blocked domains
    have their URLs scrubbed in logs, serving as both a privacy control and a
    diagnostic indicator.
  - Add expression allowlist (Claim 13) as a compile-time injection defense mechanism.

- **Chapter 04 (Building Agent Systems)**:
  - Use the `debug.md` runbook pattern (Claim 20) as an example of encoding
    operational procedures as agent-consumable markdown. This is transferable to any
    agentic platform: write debugging/runbook procedures as markdown that AI agents
    can consume via URL, not as static documentation only humans read.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The gh-aw documentation is a rendered
   SPA. WebFetch processes through an AI model rather than returning raw HTML. Three
   fetches were used: one summary-level fetch and two detail-focused fetches. The
   second detailed fetch returned structured section-by-section content. Error
   messages (EOF, module not found, GHES error table) are treated as verbatim since
   they are specific technical strings. Prose descriptions are marked with "(no direct
   quote)" per MINER.md §2a guidance.

2. **`gh aw compile --purge` gap**: This command is documented here but not in
   `docs-ghaw-compilation-process.md`'s compilation commands section. Not filed as
   a contradiction — it is an omission in the reference, not a conflicting claim.
   The Assayer should note this as a source note update opportunity for the
   compilation reference.

3. **Cache `7-day expiry` vs. `90-day artifact retention`**: These refer to different
   systems — GitHub Actions cache (configured via `cache:` key/restore-keys, expires
   in 7 days) vs. GitHub Actions artifact retention for `cache-memory/` (90 days per
   `docs-ghaw-compilation-process.md` Claim 9). Both systems are present in gh-aw
   but serve different persistence needs. Not a contradiction.

4. **No publication date**: The documentation carries no explicit publication date.
   `date_published` left null. Content is consistent with current gh-aw platform
   state as of 2026-05-11.

5. **Sub-pages not followed**: The guide references separate documentation pages
   (Error Reference, Frontmatter Documentation, authentication docs, safe outputs
   docs). These were not followed; the focus was on the main common-issues reference
   page. The Operational Runbooks section references a "Workflow Health Monitoring
   Runbook" not followed due to scope constraints.
