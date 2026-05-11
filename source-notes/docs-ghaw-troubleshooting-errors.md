---
source_url: https://github.github.com/gh-aw/troubleshooting/errors
source_type: docs
title: "GitHub Agentic Workflows: Error Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: settled
issue: "#428"
---

# GitHub Agentic Workflows: Error Reference

> The dedicated error-message reference for gh-aw — catalogues ~40 specific
> error strings organized by lifecycle stage (schema validation, compilation,
> runtime, engine-specific, file processing, safe outputs, and top user-facing
> errors), providing the exact compiler/runtime output, root cause, and fix for
> each; complements the debugging methodology in `docs-ghaw-troubleshooting-debugging.md`
> and the symptom catalogue in `docs-ghaw-troubleshooting-common-issues.md` by
> supplying the precise error text a practitioner sees in their terminal or CI log.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `troubleshooting/errors`
  page — a practitioner error reference in the `troubleshooting/` section.
  Distinct from `troubleshooting/common-issues` (symptom catalogue with
  context and configuration gotchas) and `troubleshooting/debugging`
  (investigation methodology). Error-reference pages are optimized for
  copy-paste searching: a practitioner pastes the exact error string into the
  page and finds the cause and fix immediately.)
- **Author credibility**: First-party from GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team operating Peli de
  Halleux's agent factory). Error message strings, valid enumeration values,
  and CLI commands are authoritative for the `gh aw` platform. These are
  platform-emitted strings, not editorial descriptions; they are stable
  identifiers for specific failure modes.
- **Scope**: Covers error messages across seven lifecycle stages: schema
  validation (frontmatter syntax, field types, typos, imports), compilation
  (file resolution, import resolution, workflow specification), runtime (time
  delta, date-time parsing, external dependencies, authentication), engine-
  specific (trigger keyword, manual approval, on: format), file processing
  (read, directory creation, file existence), safe output generation (MCP
  config JSON), and top user-facing errors (command/event conflicts, strict
  mode violations, MCP configuration, repository features, toolsets). Does NOT
  cover: debugging methodology (see `docs-ghaw-troubleshooting-debugging.md`),
  the broader symptom catalogue with context (see
  `docs-ghaw-troubleshooting-common-issues.md`), or the silently-ignored
  misconfiguration patterns — those are in common-issues Claim 2.

## Extracted Claims

### Claim 1: The compiler uses fuzzy-matching to suggest corrections for misspelled frontmatter field names, producing "Did you mean" errors for unknown properties

- **Evidence**: The schema validation section documents the exact error string
  with a concrete misspelling example: `permisions` instead of `permissions`.
  The compiler provides the correction rather than a generic "unknown field"
  message.
- **Confidence**: settled (first-party; the error string is authoritative for
  the platform)
- **Quote**: `"Unknown property: permisions. Did you mean 'permissions'?"`
- **Our assessment**: The fuzzy-match suggestion is important for practitioners
  because it distinguishes two classes of unknown-field behavior: fields that
  produce explicit errors with suggestions (typos that nearly match known
  fields, like `permisions`) vs. fields that are silently ignored (plausible
  but wrong field names like `agent:` instead of `engine:`, documented in
  `docs-ghaw-troubleshooting-common-issues.md` Claim 2). Practitioners who
  see no error and no effect should check common-issues Claim 2; practitioners
  who see a "Did you mean" error can follow the suggestion. Together these
  two mechanisms cover the full field-name error surface. For Ch02 (Harness
  Engineering): document this distinction explicitly — the compiler catches
  near-typos but silently ignores plausible-sounding but incorrect field names.

### Claim 2: Only one agent file is permitted per workflow — importing multiple files from `.github/agents/` produces a specific error naming both files

- **Evidence**: The schema validation section documents the exact error with
  a concrete example showing the two offending filenames.
- **Confidence**: settled (first-party; the constraint and error message are
  authoritative)
- **Quote**: `"multiple agent files found in imports: 'file1.md' and 'file2.md'. Only one agent file is allowed per workflow"`
- **Our assessment**: The constraint is architectural: the agent job is
  designed for one active agent persona per workflow. Practitioners attempting
  to combine multiple agent definitions (e.g., a security-scanner agent and
  a triage agent) must use separate workflows and orchestrate them, not merge
  them via imports. The error message naming both offending files makes
  identification straightforward. For Ch02: when documenting shared workflow
  libraries via imports, explicitly note the single-agent-file constraint —
  shared tooling files (MCP configs, instructions) are fine to import, but
  only one file from `.github/agents/` can be active per workflow.

### Claim 3: Remote imports require exact `owner/repo/path[@ref]` format — deviations produce a specific compilation error

- **Evidence**: The compilation section documents the exact format requirement
  in the error string itself.
- **Confidence**: settled (first-party; the format constraint is authoritative)
- **Quote**: `"invalid workflowspec: must be owner/repo/path[@ref]"`
- **Our assessment**: The `[@ref]` portion is optional (square brackets
  indicate optionality) but the `owner/repo/path` prefix is required. The
  error fires at compilation, not at runtime — remote imports are resolved
  during the compilation phase (Phase 1, BFS traversal per
  `docs-ghaw-compilation-process.md` Claim 2). For Ch02: when documenting
  shared workflow libraries published in external repos, show the exact format
  string and note the optional `@ref` for pinning to a specific commit or tag.

### Claim 4: The `stop-after` field has four distinct runtime error types covering format, unit restriction, value ceiling, and unit deduplication

- **Evidence**: The runtime section documents four separate errors, each with
  a distinct error string. The format error specifies supported units
  explicitly within the string.
- **Confidence**: settled (first-party; four named error strings are
  authoritative)
- **Quote** (format error): `"invalid time delta format: +[value]. Expected format like +25h, +3d, +1w, +1mo, +1d12h30m"`
- **Quote** (minutes error): `"minute unit 'm' is not allowed for stop-after. Minimum unit is hours 'h'. Use +[hours]h instead of +[minutes]m"`
- **Quote** (ceiling error): `"time delta too large: [value] [unit] exceeds maximum of [max]"`
- **Quote** (duplicate error): `"duplicate unit '[unit]' in time delta: +[value]"`
- **Our assessment**: The format error string reveals that compound time
  deltas are valid (`+1d12h30m` mixes days, hours, and minutes), but the
  minutes-error string then reveals that minutes are NOT valid for `stop-after`
  specifically. This creates a subtle inconsistency: the format example shows
  `30m` as a valid component, yet the error says minutes are disallowed for
  `stop-after`. The ceiling values are specific: 12 months, 52 weeks, 365 days,
  8760 hours (all equivalent to approximately one year). For Ch02: present the
  `stop-after` constraints as a table: supported units (h/d/w/mo for
  `stop-after`), maximum value per unit, and the compound format syntax. The
  minutes-in-format-example issue may confuse practitioners — note it
  explicitly.

### Claim 5: The `stop-after` date-time alternative supports multiple human-readable formats including ordinal dates

- **Evidence**: The runtime section documents the exact error string with a
  list of supported format examples.
- **Confidence**: settled (first-party; the supported format list in the error
  string is authoritative)
- **Quote**: `"unable to parse date-time: [value]. Supported formats include: YYYY-MM-DD HH:MM:SS, MM/DD/YYYY, January 2 2006, 1st June 2025, etc"`
- **Our assessment**: The format list covers ISO-style, American-style, Go
  reference time format, and ordinal dates — a broad set reflecting the range
  of human inputs practitioners might use. The `January 2 2006` format is Go's
  reference time (the specific date `Jan 2, 2006` is Go's layout specifier);
  practitioners who know Go will recognize it immediately. The `1st June 2025`
  format includes ordinal suffixes. The `etc` in the error suggests there are
  additional supported formats not enumerated. For Ch02: when documenting
  `stop-after` with an absolute date, provide examples in the most common
  formats (`YYYY-MM-DD HH:MM:SS` for unambiguous international use and
  `1st June 2025` for readable scheduled workflows).

### Claim 6: `jq` is an external runtime dependency — its absence produces a specific "not found" error rather than a degraded capability

- **Evidence**: The runtime section lists `"jq not found in PATH"` as a named
  error with a specific cause (jq not installed) and platform-specific
  installation commands.
- **Confidence**: settled (first-party; the dependency and error are documented)
- **Quote**: `"jq not found in PATH"`
- **Our assessment**: The `jq` dependency means gh-aw runtime environments
  require jq to be available. In cloud-hosted GitHub Actions runners, jq is
  typically pre-installed; in custom or enterprise runners, this may not hold.
  The error fires at runtime (not at compile time), so workflows pass
  compilation successfully but fail when executed. For Ch02: when documenting
  custom runner configuration for gh-aw workflows, include jq installation
  verification alongside Docker, Node.js, and GitHub CLI requirements.

### Claim 7: Using `triggers:` instead of `on:` produces an explicit error — unlike silently-ignored misspellings, this trigger-keyword mistake is caught by the engine

- **Evidence**: The engine-specific errors section documents the exact error
  string with a correction hint embedded in the message.
- **Confidence**: settled (first-party; the error string is authoritative)
- **Quote**: `"invalid frontmatter key 'triggers:' — use 'on:' to define workflow triggers"`
- **Our assessment**: This is a significant contrast with the silently-ignored
  field behavior documented in `docs-ghaw-troubleshooting-common-issues.md`
  Claim 2. The fields `agent:`, `mcp-servers:`, `tool-sets:`, and
  `allowed_repos:` are silently ignored by the compiler; `triggers:` is not.
  The difference is likely that `triggers:` is specifically flagged as a common
  mistake from GitHub Actions vocabulary, while the silently-ignored fields are
  completely unknown to the schema. For Ch02: the `triggers:` → `on:` correction
  is the most visible example of a GitHub Actions vocabulary mismatch in
  gh-aw; document it alongside the distinction from silently-ignored fields.

### Claim 8: Strict mode produces three specific compile-time errors covering network configuration, write permissions, and wildcard domain usage

- **Evidence**: The top user-facing errors section documents three distinct
  strict-mode error strings.
- **Confidence**: settled (first-party; the error strings are authoritative
  compile-time signals)
- **Quote** (network): `"strict mode: 'network' configuration is required"`
- **Quote** (write perm): `"strict mode: write permission 'contents: write' is not allowed"`
- **Quote** (wildcard): `"strict mode: wildcard '*' is not allowed in network.allowed domains"`
- **Our assessment**: The three strict-mode errors define what "strict" actually
  enforces at compile time: (1) network must be declared — `network: defaults`
  is the minimum; (2) write permissions are blocked — all writes go through
  safe-outputs; (3) the catch-all network wildcard is forbidden — practitioners
  must name specific domains or use ecosystem identifiers. These three
  constraints together express the principle of least privilege at the
  compilation surface. For Ch03 (Safety and Verification): these three errors
  are the compile-time security checklist for strict mode compliance. Document
  them as the specific failure modes `gh aw compile --strict` catches, not
  just as "stricter validation."

### Claim 9: Public repositories enforce strict mode at runtime — workflows compiled without `--strict` produce a specific error when executed on public repos

- **Evidence**: The top user-facing errors section documents the exact error
  string and its resolution.
- **Confidence**: settled (first-party; this is a platform enforcement behavior)
- **Quote**: `"This workflow is running on a public repository but was not compiled with strict mode."`
- **Our assessment**: This is a runtime enforcement that supplements compile-
  time opt-in. A workflow that compiles successfully without `--strict` will
  fail at execution time if deployed to a public repository. The platform
  treats public repos as inherently higher-risk (prompt injection surface from
  untrusted external contributors) and mandates strict mode regardless of
  developer intent. The fix is recompile with `gh aw compile --strict`. For
  Ch02: document strict mode as a required step for any workflow deployed to a
  public repository, not just a recommended security hardening. For Ch03:
  this runtime enforcement means public-repo deployments have a security floor
  that cannot be bypassed by omitting `--strict` at compile time.

### Claim 10: MCP tool configuration produces four distinct error types covering URL fields, dual-specification conflicts, type/transport mismatches, and strict-mode network requirements

- **Evidence**: The top user-facing errors section documents four MCP-specific
  error strings.
- **Confidence**: settled (first-party; the error strings are authoritative
  configuration validation messages)
- **Quote** (missing url): `"http MCP tool 'my-tool' missing required 'url' field"`
- **Quote** (dual spec): `"tool 'my-tool' mcp configuration cannot specify both 'container' and 'command'"`
- **Quote** (type mismatch): `"tool 'my-tool' mcp configuration with type 'http' cannot use 'container' field"`
- **Quote** (network req): `"strict mode: custom MCP server 'my-server' with container must have network configuration"`
- **Our assessment**: The four error types map to the two MCP transport modes
  (http vs. stdio/container) and their mutually exclusive configuration fields.
  HTTP servers need `url` and cannot use `container`; stdio servers use
  `container` or `command` but not both. The strict-mode network requirement
  for containerized servers adds a fourth dimension: stdio servers in strict
  mode must have explicit network configuration. For Ch02: when documenting
  MCP server configuration, present the HTTP vs. container configuration paths
  as distinct and mutually exclusive, and show the required fields for each.
  These four errors are the compile-time validators for MCP configuration
  correctness.

### Claim 11: The toolset name validator enforces an enumerated list of 21 valid values — any name outside this set produces an explicit error

- **Evidence**: The toolsets configuration section documents the error string
  and the complete valid-name list.
- **Confidence**: settled (first-party; the enumerated list is authoritative)
- **Quote**: `"invalid toolset: 'action' is not a valid toolset"`
- **Valid names** (verbatim from source): `context`, `repos`, `issues`,
  `pull_requests`, `users`, `actions`, `code_security`, `discussions`,
  `labels`, `notifications`, `orgs`, `projects`, `gists`, `search`,
  `dependabot`, `experiments`, `secret_protection`, `security_advisories`,
  `stargazers`, `default`, `all`
- **Our assessment**: The error example uses `action` (without the `s`) as the
  invalid name, while `actions` is in the valid list — a one-character typo
  that produces a clear error. The `default` toolset and `all` toolset are
  meta-identifiers that expand to curated subsets, complementing the specific
  capability names. The `experiments` toolset name suggests features under
  active development. For Ch02: publish the complete 21-name list as a
  reference table alongside toolset configuration examples — practitioners
  need the exact names, not approximations.

### Claim 12: The GitHub MCP server's read-only mode cannot be disabled — attempting `read-only: false` produces an explicit error

- **Evidence**: The toolsets section documents the error string and its cause.
- **Confidence**: settled (first-party; this is a platform architectural
  constraint)
- **Quote**: `"GitHub MCP server read-only mode cannot be disabled"`
- **Our assessment**: The GitHub MCP server enforces read-only access at the
  platform level — this is consistent with the broader gh-aw principle that
  write operations route through safe outputs, not through direct tool calls.
  An agent cannot acquire write access to GitHub by configuring the MCP server
  differently; the write surface is structurally bounded. For Ch03: document
  this as the tool-layer enforcement of write isolation — even if a practitioner
  explicitly attempts `read-only: false`, the platform rejects it. This
  reinforces that Plan-Level Trust (from `docs-ghaw-compilation-process.md`
  Claim 3) is enforced at the MCP configuration layer as well as the job
  permission layer.

### Claim 13: Safe output types have repository-feature prerequisites — using them on repositories with the corresponding features disabled produces a named runtime error

- **Evidence**: The top user-facing errors section documents the exact error
  string with a concrete example for `create-issue` when issues are disabled.
- **Confidence**: settled (first-party; the error is documented with a specific
  repository example)
- **Quote**: `"workflow uses safe-outputs.create-issue but repository owner/repo does not have issues enabled"`
- **Our assessment**: This error fires at runtime when the safe output job
  attempts to execute an operation the repository doesn't support. The fix is
  enabling the feature in repository settings or using a different safe output
  type. This is a deployment-context check: the same workflow may succeed on
  one repository and fail on another depending on which features are enabled.
  For Ch02: when documenting safe output types, note their repository-feature
  prerequisites. `create-issue` requires issues to be enabled; by extension,
  `create-pr` may require the repository to allow PRs. Document this as a
  pre-deployment checklist item for new workflow deployments.

### Claim 14: File initialization conflict errors include an explicit `--force` resolution path in the error string itself

- **Evidence**: The file processing errors section documents the error string
  with the `--force` flag embedded in the message.
- **Confidence**: settled (first-party; the error string with embedded solution
  is authoritative)
- **Quote**: `"workflow file '[path]' already exists. Use --force to overwrite"`
- **Our assessment**: The error is self-documenting — practitioners who see
  it do not need to consult documentation to find the fix. The `--force` flag
  in `gh aw init my-workflow --force` overwrites an existing compiled workflow
  file. This matters during workflow restructuring or when re-initializing a
  workflow from a different template. For Ch02: the `--force` flag is the
  standard resolution for overwrite-conflict errors in the gh-aw CLI; document
  it as part of the workflow initialization reference.

### Claim 15: Command triggers cannot coexist with certain event triggers in the same workflow — the conflict produces a specific error

- **Evidence**: The top user-facing errors section documents the exact
  conflict error string.
- **Confidence**: settled (first-party; the trigger compatibility constraint
  is authoritative)
- **Quote**: `"cannot use 'command' with 'issues' in the same workflow"`
- **Our assessment**: `command` triggers (slash-command style, e.g., `/approve`)
  and `issues` event triggers (fires on issue opened, edited, etc.) are
  mutually exclusive in the same workflow. The fix is either removing the
  conflicting event trigger or restructuring with the `events:` field within
  the command block. This constraint reflects that command-triggered workflows
  have a distinct activation path from event-triggered workflows and the two
  paths cannot be combined in a single workflow definition. For Ch02: document
  this as a workflow design constraint — command and event triggers require
  separate workflows, not a combined trigger block.

## Concrete Artifacts

### Complete Error Message Reference by Category

```
SCHEMA VALIDATION ERRORS
  "frontmatter not properly closed"
  "failed to parse frontmatter: [yaml error details]"
  "timeout-minutes must be an integer"
  "Unknown property: permisions. Did you mean 'permissions'?"
  "imports field must be an array of strings"
  "multiple agent files found in imports: 'file1.md' and 'file2.md'. Only one agent file is allowed per workflow"

COMPILATION ERRORS
  "workflow file not found: [path]"
  "failed to resolve import 'path': [details]"
  "invalid workflowspec: must be owner/repo/path[@ref]"
  "section 'name' not found"

RUNTIME ERRORS
  "invalid time delta format: +[value]. Expected format like +25h, +3d, +1w, +1mo, +1d12h30m"
  "minute unit 'm' is not allowed for stop-after. Minimum unit is hours 'h'. Use +[hours]h instead of +[minutes]m"
  "time delta too large: [value] [unit] exceeds maximum of [max]"
  "duplicate unit '[unit]' in time delta: +[value]"
  "unable to parse date-time: [value]. Supported formats include: YYYY-MM-DD HH:MM:SS, MM/DD/YYYY, January 2 2006, 1st June 2025, etc"
  "jq not found in PATH"
  "authentication required"

ENGINE-SPECIFIC ERRORS
  "manual-approval value must be a string"
  "invalid frontmatter key 'triggers:' — use 'on:' to define workflow triggers"
  "invalid on: section format"

FILE PROCESSING ERRORS
  "failed to read file [path]: [details]"
  "failed to create .github/workflows directory: [details]"
  "workflow file '[path]' already exists. Use --force to overwrite"

SAFE OUTPUT ERRORS
  "failed to parse existing mcp.json: [details]"
  "failed to marshal mcp.json: [details]"

TOP USER-FACING ERRORS
  "cannot use 'command' with 'issues' in the same workflow"
  "strict mode: 'network' configuration is required"
  "strict mode: write permission 'contents: write' is not allowed"
  "strict mode: wildcard '*' is not allowed in network.allowed domains"
  "http MCP tool 'my-tool' missing required 'url' field"
  "job name cannot be empty"
  "unable to determine MCP type for tool 'my-tool': missing type, url, command, or container"
  "tool 'my-tool' mcp configuration cannot specify both 'container' and 'command'"
  "tool 'my-tool' mcp configuration with type 'http' cannot use 'container' field"
  "strict mode: custom MCP server 'my-server' with container must have network configuration"
  "workflow uses safe-outputs.create-issue but repository owner/repo does not have issues enabled"
  "strict mode: engine does not support firewall"
  "This workflow is running on a public repository but was not compiled with strict mode."

TOOLSETS CONFIGURATION ERRORS
  "invalid toolset: 'action' is not a valid toolset"
  "GitHub MCP server read-only mode cannot be disabled"
```

*Source: gh-aw troubleshooting/errors — all error categories*

### Valid Toolset Names (Complete List)

```
context, repos, issues, pull_requests, users, actions, code_security,
discussions, labels, notifications, orgs, projects, gists, search,
dependabot, experiments, secret_protection, security_advisories,
stargazers, default, all
```

*Source: gh-aw troubleshooting/errors — Toolsets Configuration Issues section*

### Time Delta Constraints Reference

```
stop-after time delta rules:
  Supported units: h (hours), d (days), w (weeks), mo (months)
  Unsupported:     m (minutes) — minimum unit is hours
  Compound format: +1d12h (days + hours, minutes NOT allowed in stop-after)
  Maximum values:
    8760 hours  (~1 year)
    365 days    (~1 year)
    52 weeks    (~1 year)
    12 months   (1 year)

stop-after date-time supported formats:
  YYYY-MM-DD HH:MM:SS      (ISO-style, unambiguous)
  MM/DD/YYYY               (American-style)
  January 2 2006           (Go reference time format)
  1st June 2025            (ordinal date)
  etc.
```

*Source: gh-aw troubleshooting/errors — Runtime Errors section*

### Strict Mode Compliance Checklist

```yaml
# All three strict mode requirements must be satisfied:

# 1. Network configuration is required
network:
  allowed:
    - defaults         # minimum: basic infrastructure only
    # OR specify explicit domains/ecosystem identifiers

# 2. Write permissions are blocked — use safe-outputs instead
safe-outputs:
  create-issue: {}    # write operations go here, not in permissions block

# 3. No wildcard in network.allowed
network:
  allowed:
    - node             # OK: ecosystem identifier
    - api.example.com  # OK: specific domain
    # NOT: - "*"       # ERROR: standalone wildcard disallowed
```

*Source: gh-aw troubleshooting/errors — Top User-Facing Errors section*

### MCP Server Configuration: HTTP vs. Container Paths

```yaml
# HTTP MCP server (requires 'url', cannot use 'container')
tools:
  my-http-tool:
    type: http
    url: https://my-mcp-server.example.com   # REQUIRED for http type
    # container: ...                          # ERROR: http cannot use container

# Stdio MCP server (uses 'container' OR 'command', not both)
tools:
  my-stdio-tool:
    container: ghcr.io/my-org/my-mcp:latest  # use container OR command
    # command: python my_server.py            # ERROR: cannot specify both
    # In strict mode, also requires:
    # network configuration must be present
```

*Source: gh-aw troubleshooting/errors — Top User-Facing Errors section*

### Toolsets vs. Allowed Configuration

```yaml
# Recommended: use only toolsets (most cases)
tools:
  github:
    toolsets: [issues]

# Advanced: restrict with allowed within a toolset
tools:
  github:
    toolsets: [issues]
    allowed: [create_issue]
```

*Source: gh-aw troubleshooting/errors — Toolsets Configuration Issues section*

### CLI Commands Referenced

```bash
# Force-overwrite existing workflow file
gh aw init my-workflow --force

# Compile with strict mode (required for public repos)
gh aw compile --strict

# Inspect MCP server configuration for a workflow
gh aw mcp inspect <workflow>

# Verbose compilation for diagnosing compilation errors
gh aw compile --verbose
```

*Source: gh-aw troubleshooting/errors — resolution steps across sections*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-compilation-process.md` Claim 1 (Phase 1 parsing/validation
    validates against workflow schema and validates expression safety): the
    schema validation errors (Claims 1–2) and compilation errors (Claim 3)
    here are the visible manifestation of Phase 1 failures. The compilation
    reference names the phase; this source gives the exact error strings
    practitioners see when Phase 1 rejects their workflow.
  - `docs-ghaw-compilation-process.md` Claim 11 (`--strict` flag for stricter
    validation via security scanner integrations): the three strict-mode errors
    (Claim 8) here document what the `--strict` flag enforces at compile time.
    Both sources agree that `--strict` adds meaningful security validation
    beyond the default compilation path.
  - `docs-ghaw-compilation-process.md` Claim 2 (BFS import resolution with
    cycle detection): the compilation error `"failed to resolve import 'path':
    [details]"` and `"invalid workflowspec: must be owner/repo/path[@ref]"`
    (Claim 3) are the Phase 1 import resolution failures described conceptually
    in Claim 2. The two together give the algorithm (BFS + cycle detection) and
    the exact error strings its failures produce.
  - `docs-ghaw-compilation-process.md` Claim 3 (Plan-Level Trust — job-level
    permission isolation, read-only AI reasoning separated from write operations):
    Claim 12 here (GitHub MCP read-only enforcement) and the strict-mode write
    permission error (Claim 8) are the MCP-layer and compile-layer enforcement
    of the same Plan-Level Trust principle. The compilation reference names the
    principle; this source shows two specific error strings that enforce it.
  - `docs-ghaw-troubleshooting-debugging.md` Claim 13 (`gh aw compile
    my-workflow --verbose` and `gh aw fix --write` for compilation errors):
    the compilation errors in Claims 1–3 here are exactly the categories that
    `--verbose` helps diagnose and `gh aw fix --write` may auto-remediate.
    The debugging guide's recommended fix commands map to this source's error
    catalog.

- **Extends**:
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 2 (silently ignored
    misspelled frontmatter fields — `agent:`, `mcp-servers:`, `tool-sets:`,
    `allowed_repos:`): this source documents the complementary case — which
    frontmatter mistakes DO produce explicit errors. Together, Claim 2 from
    common-issues and Claims 1 and 7 here give a complete picture of the
    compiler's error surface: near-typos of known fields get fuzzy-match errors;
    keyword mistakes (`triggers:`) get specific errors; plausible-sounding but
    wrong field names are silently ignored. This three-way distinction is
    critical for harness engineering.
  - `docs-ghaw-troubleshooting-debugging.md` (debugging methodology): the
    debugging guide documents HOW to investigate failures; this source documents
    WHAT the specific error strings look like. Practitioners who arrive here
    via copy-paste searching get the cause and fix; practitioners who need to
    investigate a less obvious failure should move to the debugging guide.
  - `docs-ghaw-tools-reference.md` (tools reference): the tools reference
    documents what each valid toolset contains and how to configure tools.
    The toolset name validation here (Claim 11) gives the complete list of
    valid names and the error that fires for invalid ones — the practical
    validation layer for the reference documentation.
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 15 (public repo auto-
    applies `min-integrity: approved`): Claim 9 here (public repo strict mode
    enforcement) is a companion deployment-context difference — the same
    workflow may behave differently on public vs. private repos. Together,
    these two claims (from different troubleshooting pages) establish the full
    set of public-repo behavioral differences: strict mode is required (this
    source); integrity filtering is stricter (common-issues).

- **Contradicts**: None identified. The explicit error-producing behaviors
  documented here are consistent with the silently-ignored behaviors in
  `docs-ghaw-troubleshooting-common-issues.md` Claim 2 — they cover
  non-overlapping cases (near-typos and recognized-wrong-keywords vs.
  plausible-but-unknown fields). No contradiction issue filed.

- **Novel**:
  - **Complete enumerated toolset name list** (Claim 11): The 21 specific valid
    toolset names (`context`, `repos`, `issues`, `pull_requests`, `users`,
    `actions`, `code_security`, `discussions`, `labels`, `notifications`, `orgs`,
    `projects`, `gists`, `search`, `dependabot`, `experiments`, `secret_protection`,
    `security_advisories`, `stargazers`, `default`, `all`) appear nowhere else in
    the corpus. This is the authoritative enumeration.
  - **Fuzzy-match "Did you mean" error behavior** (Claim 1): No existing source
    note documents that the compiler uses fuzzy matching for typos in field names
    and provides "Did you mean" suggestions. This is new to the corpus.
  - **Single-agent-file constraint with specific error string** (Claim 2): The
    constraint that only one `.github/agents/` file can be imported per workflow
    is not documented in `docs-ghaw-tools-reference.md` or any other existing note.
  - **Time delta format with compound units and per-unit ceilings** (Claim 4):
    The specific compound format (`+1d12h30m`), the minutes-disallowed-in-stop-after
    restriction, and the four ceiling values (12mo/52w/365d/8760h) are not
    documented in any existing source note.
  - **Date-time supported format list** (Claim 5): No existing source note
    documents the supported date-time formats for `stop-after` absolute dates,
    including the Go reference time and ordinal date forms.
  - **`jq` external runtime dependency** (Claim 6): No existing source note
    identifies jq as an external runtime dependency for gh-aw workflows.
  - **`triggers:` produces explicit error** (Claim 7): The distinction between
    keywords that produce errors (`triggers:`) and fields that are silently
    ignored (`agent:`) is new to the corpus as a named distinction.
  - **Public repo strict mode runtime enforcement** (Claim 9): While strict mode
    itself is documented, no existing source note documents that public repos
    enforce strict mode at runtime even when not compiled with `--strict`.
  - **MCP configuration validation error strings** (Claim 10): Four specific
    MCP configuration error strings covering URL requirements, dual-spec
    conflicts, and type/transport mismatches are new to the corpus.
  - **Repository feature prerequisites for safe outputs** (Claim 13): No existing
    source note documents that safe output types have repository-feature
    prerequisites that can cause runtime failures.
  - **`--force` flag for workflow file conflict resolution** (Claim 14): No
    existing source note documents `gh aw init --force` as the resolution for
    file existence conflicts.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add the three-way error surface distinction (Claim 1 + `docs-ghaw-troubleshooting-
    common-issues.md` Claim 2 + Claim 7): near-typos produce fuzzy-match errors;
    recognized-but-wrong keywords (`triggers:`) produce specific errors; plausible-
    but-unknown field names are silently ignored. This is the most practically
    important configuration failure taxonomy for practitioners. Currently no guide
    chapter synthesizes these three behaviors into a coherent framework.
  - Add the complete toolset name list (Claim 11) as a reference table in the
    GitHub tools configuration section. The 21 names are the authoritative
    enumeration; practitioners configuring `toolsets:` need them without
    guesswork.
  - Add `stop-after` time delta constraints as a structured reference table
    (Claim 4): supported units, maximum values per unit, compound format, and the
    minutes-in-stop-after restriction. The current common-issues note documents
    the timeout error table; this source adds the scheduling-deadline error table.
  - Add `jq` to the custom runner prerequisites checklist (Claim 6): GitHub-
    hosted runners have jq pre-installed; custom and enterprise runners may not.
    Add as a deployment prerequisite alongside Docker and the GitHub CLI.
  - Add `--force` for workflow file overwrite conflicts (Claim 14): document as
    part of the workflow initialization reference.
  - Document MCP configuration as HTTP-path vs. container-path (Claim 10):
    the four error types define two mutually exclusive configuration paths.

- **Chapter 03 (Safety and Verification)**:
  - Add strict mode's three specific enforcement areas (Claim 8) as the concrete
    compliance checklist for `--strict`: network required, write permissions
    blocked, wildcards forbidden. Currently no guide chapter lists what strict
    mode specifically rejects.
  - Add public-repo strict mode runtime enforcement (Claim 9): strict mode is
    not optional for public repos — it is enforced at runtime even if omitted
    at compile time. Document this as a security floor for public deployments.
  - Add GitHub MCP read-only enforcement as a tool-layer security control
    (Claim 12): the read-only constraint cannot be overridden by configuration.
    This reinforces Plan-Level Trust at the MCP tool layer.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The gh-aw documentation is a
   rendered SPA. WebFetch processes through an AI model rather than returning
   raw HTML. Three fetches were used: one general extraction, one targeted at
   verbatim content, and one focused on specific enumeration values (toolset
   names, time delta ceilings, date-time formats). Error message strings were
   consistent across all three fetches and are treated as verbatim since they
   are specific technical identifiers, not editorial prose.

2. **"section 'name' not found" may indicate bug**: The compilation errors
   section documents this error as having a cause of "Referenced section missing
   from frontmatter" with the note "(may indicate bug)." This suggests the
   error can fire both from valid practitioner mistakes and from internal
   compiler state issues. Not treated as a separate claim due to ambiguity —
   the Assayer should note it for future investigation.

3. **Compound time delta with minutes**: The format error string shows `+1d12h30m`
   as a valid compound format, but the minutes-restriction error explicitly says
   minutes are not allowed in `stop-after`. This may mean: (a) `m` (minutes) is
   valid in the general time delta format but not for `stop-after` specifically,
   or (b) the format example is aspirational for future support. This ambiguity
   is preserved in Claim 4 rather than resolved.

4. **No publication date**: The documentation carries no explicit publication date.
   `date_published` left null. Content is consistent with current gh-aw platform
   state as of 2026-05-11.

5. **Sub-pages not followed**: The error reference page links to Quick Start,
   Creating Workflows, CLI Commands, Guides, Design Patterns, and Reference
   sections. These were not followed; the focus was on the error reference content
   itself. The troubleshooting section's three pages (errors, debugging,
   common-issues) were treated as a coordinated reference set; the other two
   are already in the corpus.
