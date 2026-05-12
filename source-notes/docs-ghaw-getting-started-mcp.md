---
source_url: https://github.github.com/gh-aw/guides/getting-started-mcp
source_type: docs
title: "GitHub Agentic Workflows: Getting Started with MCP"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#436"
---

# GitHub Agentic Workflows: Getting Started with MCP

> The beginner-facing tutorial guide to MCP integration in gh-aw — defines MCP
> conceptually, introduces the `toolsets:` vs. `allowed:` configuration split,
> documents the GitHub toolsets table with action-friendly defaults and the
> `users` exclusion, provides the three-step getting-started sequence, and gives
> concrete debugging and troubleshooting commands.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/getting-started-mcp`
  page — the "Guides" section, which provides practitioner how-to guidance.
  Distinct from the configuration reference page at `guides/mcps` covered in
  `docs-ghaw-mcps.md`. This page is the conceptual onboarding and tutorial
  entry point; that page is the complete configuration reference for advanced
  integration patterns.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's agent factory blog series and the
  gh-aw platform. Claims about platform behavior, available toolsets, operating
  modes, and CLI command semantics are authoritative.
- **Scope**: MCP integration from zero — what MCP is, the two configuration
  patterns (toolsets vs. allowed), the GitHub MCP server's toolset table,
  operating modes, practical workflow examples, and debugging/troubleshooting
  commands. Does NOT cover: the advanced configuration types (stdio, Docker,
  HTTP, registry) in depth (see `docs-ghaw-mcps.md`), the OIDC auth mechanism
  (see `docs-ghaw-mcps.md` Claim 4), Docker network controls (see
  `docs-ghaw-mcps.md` Claim 6), or the shared MCP configuration library in
  detail (linked via Next Steps → Imports).

## Extracted Claims

### Claim 1: MCP is a standardized protocol enabling agents to connect to external tools, databases, and APIs — MCP servers act as specialized adapters

- **Evidence**: The page opens with a direct definition stating the protocol's
  purpose and the role of MCP servers as adapters to concrete services (Notion,
  Slack, Datadog).
- **Confidence**: settled (first-party definition; consistent with the MCP
  standard)
- **Quote**: "Model Context Protocol (MCP) is a standardized protocol that
  enables agents to connect to external tools, databases, and APIs. MCP servers
  act as specialized adapters, giving agents access to GitHub, web search,
  databases, and third-party services like Notion, Slack, and Datadog."
- **Our assessment**: The "specialized adapters" framing is useful for
  practitioners: MCP servers translate the agent's tool-call interface to the
  target service's API. The concrete examples (Notion, Slack, Datadog) match
  the 17-server shared library in `docs-ghaw-mcps.md` Claim 9, confirming that
  the tutorial and the configuration reference are aligned on canonical MCP use
  cases. For Ch02 (Harness Engineering): this is the one-paragraph MCP concept
  summary to use when introducing MCP to practitioners who are new to it.

### Claim 2: The `toolsets:` configuration pattern is recommended for GitHub tools and remains stable across MCP server version changes — individual tool names may change but toolsets do not

- **Evidence**: The page explicitly recommends `toolsets:` and states the
  stability guarantee: "Toolsets remain stable across MCP server versions,
  while individual tool names may change."
- **Confidence**: settled (first-party documentation; stability is stated as a
  platform guarantee)
- **Quote**: "Toolsets remain stable across MCP server versions, while
  individual tool names may change."
- **Our assessment**: This is a significant operational detail not documented
  in `docs-ghaw-mcps.md`. That note documents `allowed:` (for custom servers)
  and `toolsets:` (implicitly via examples) but does not state the stability
  contract. For Ch02 (Harness Engineering): recommend `toolsets:` over
  individual tool names for GitHub MCP integration — the toolset names are
  the stable API surface; individual tool names are the unstable implementation
  detail that may change across platform releases.

### Claim 3: The `default` toolset expands to four action-friendly toolsets (`context`, `repos`, `issues`, `pull_requests`); the `users` toolset is excluded because GitHub Actions tokens do not support user operations

- **Evidence**: The page states the expansion and the exclusion reason
  explicitly: "The `default` toolset includes: `context`, `repos`, `issues`,
  `pull_requests`. When used in workflows, `[default]` expands to
  action-friendly toolsets that work with GitHub Actions tokens. Note: The
  `users` toolset is not included by default as GitHub Actions tokens do not
  support user operations."
- **Confidence**: settled (first-party; the expansion and the exclusion reason
  are explicitly documented)
- **Quote**: "The `default` toolset includes: `context`, `repos`, `issues`,
  `pull_requests`. When used in workflows, `[default]` expands to
  action-friendly toolsets that work with GitHub Actions tokens. Note: The
  `users` toolset is not included by default as GitHub Actions tokens do not
  support user operations."
- **Our assessment**: The `users` toolset exclusion is an important operational
  detail not documented in any existing source note. A practitioner who tries
  to use user-lookup tools (`get_me`, `get_user`, `list_users`) assuming they
  are in `[default]` will encounter a runtime capability gap with no obvious
  error message. The rationale — GitHub Actions tokens don't support user
  operations — explains why this is a token capability constraint, not just a
  scoping decision. For Ch02: document this as a gotcha in MCP toolset
  selection. The `users` toolset requires a different authentication context
  (PAT) rather than just adding it to `toolsets:`.

### Claim 4: The GitHub MCP server always operates read-only; write operations are handled through safe outputs in a separate permission-controlled job

- **Evidence**: The page states: "The GitHub MCP server always operates
  read-only. Write operations are handled through safe outputs, which run in a
  separate permission-controlled job."
- **Confidence**: settled (first-party; consistent with `docs-ghaw-mcps.md`
  Claim 1 and the safe-outputs architecture)
- **Quote**: "The GitHub MCP server always operates read-only. Write operations
  are handled through safe outputs, which run in a separate
  permission-controlled job."
- **Our assessment**: The read-only policy for the built-in GitHub MCP server is
  stated more definitively here ("always") than in `docs-ghaw-mcps.md` Claim 1,
  which focuses on custom servers and notes a compliance gap (policy stated but
  not protocol-enforced at the server boundary). The built-in GitHub MCP server
  appears to enforce read-only at the platform level, whereas custom servers
  rely on server-side enforcement. For Ch03 (Safety and Verification): this is
  the clearest statement of the information-flow architecture: read/query →
  GitHub MCP server (read-only, platform-enforced); write/mutate → safe outputs
  (permission-controlled separate job). The compliance gap from `docs-ghaw-mcps.md`
  Claim 1 applies to custom servers, not the built-in GitHub MCP server.

### Claim 5: The GitHub MCP server supports two operating modes: remote (hosted, no Docker, faster startup) and local (Docker, version-pinnable, for offline or restricted environments)

- **Evidence**: The page states: "Remote mode (`mode: remote`) connects to a
  hosted server for faster startup with no Docker required. Local mode
  (`mode: local`) runs in Docker, enabling version pinning for offline or
  restricted environments."
- **Confidence**: settled (first-party; modes are explicitly documented with
  their trade-offs)
- **Quote**: "Remote mode (`mode: remote`) connects to a hosted server for
  faster startup with no Docker required. Local mode (`mode: local`) runs in
  Docker, enabling version pinning for offline or restricted environments."
- **Our assessment**: The mode selection matches the practitioner's constraints:
  remote for speed and simplicity (no Docker dependency); local for
  reproducibility and air-gapped environments. For Ch02 (Harness Engineering):
  document the `mode:` field under the GitHub MCP server section. Recommend
  remote as the default; local for teams with strict environment controls
  (government, healthcare, GHE deployments). This connects to `docs-ghaw-mcps.md`
  Claim 2's four-type MCP server taxonomy — the GitHub MCP server's remote/local
  distinction corresponds to the HTTP (remote) vs. Docker (local) types applied
  to the platform's built-in server.

### Claim 6: The beginner MCP onboarding sequence has three steps: add `toolsets: [default]` to a workflow, compile with `gh aw compile`, then verify with `gh aw mcp inspect`

- **Evidence**: The page's "Quick Start" section provides explicit numbered
  steps. Step 1 creates a workflow with `toolsets: [default]`. Step 2 runs
  `gh aw compile my-workflow` followed by `gh aw mcp inspect my-workflow`.
  The outcome: "You now have a working MCP integration. The agent can read
  issues, search repositories, and access pull request information."
- **Confidence**: settled (first-party; explicit numbered quick-start steps)
- **Quote**: "You now have a working MCP integration. The agent can read issues,
  search repositories, and access pull request information."
- **Our assessment**: The three-step sequence for built-in GitHub MCP toolsets
  differs from the custom server onboarding sequence in `docs-ghaw-mcps.md`
  Claim 7 (`add` → `inspect` → `list-tools` → set `allowed:`). The appropriate
  sequence depends on which MCP server type is being configured. For Ch02:
  document both sequences separately — the GitHub MCP toolset path (add
  toolsets → compile → inspect) for built-in GitHub tools, and the custom
  server path (add → inspect → list-tools → set allowed:) for third-party
  integrations.

### Claim 7: The `registry` field in MCP configuration is informational and not enforced at runtime by gh-aw — the `container` or `command` fields specify the actual runtime behavior

- **Evidence**: The page explicitly states: "The `registry` field provides
  metadata for tooling while the `container` or `command` fields specify how
  to run the server. Registry usage is informational and not enforced by gh-aw."
- **Confidence**: settled (first-party direct quote; this upgrades
  `docs-ghaw-mcps.md` Claim 8 from "emerging" to settled evidence)
- **Quote**: "The `registry` field provides metadata for tooling while the
  `container` or `command` fields specify how to run the server. Registry usage
  is informational and not enforced by gh-aw."
- **Our assessment**: This is a direct quote confirming what `docs-ghaw-mcps.md`
  Claim 8 assessed as "emerging" — that the registry field is informational, not
  a runtime enforcement mechanism. The security implication: the gh-aw runtime
  does not validate that the container image matches the registry metadata.
  Practitioners using registry-based servers rely on the registry's curation
  signal as a trust indicator but must independently verify container provenance.
  For Ch02: update the registry-based server documentation to note that
  `registry:` is metadata only; the runtime pulls from the `container:` or
  `command:` field directly.

### Claim 8: `gh aw mcp add` does three things automatically: search the registry, add the server configuration to the workflow, and recompile

- **Evidence**: The page states: "The command searches the registry, adds the
  server configuration, and recompiles the workflow."
- **Confidence**: settled (first-party; explicitly stated)
- **Quote**: "The command searches the registry, adds the server configuration,
  and recompiles the workflow."
- **Our assessment**: The auto-recompile behavior of `gh aw mcp add` is
  operationally significant: adding a new MCP server does not require a separate
  `gh aw compile` step because `gh aw mcp add` handles recompilation
  automatically. This contrasts with manual frontmatter edits
  (`docs-ghaw-setup-creating-workflows.md` Claim 3 and
  `docs-ghaw-guides-editing-workflows.md` Claim 6), which require an explicit
  `gh aw compile`. For Ch02 (Harness Engineering): document this distinction —
  manual frontmatter edits require explicit `gh aw compile`; `gh aw mcp add`
  recompiles automatically.

### Claim 9: YAML validation errors for MCP configuration most commonly stem from format issues: `toolsets:` must use array format (`[default]` not `default`), and `allowed:` must be an array

- **Evidence**: The troubleshooting section states: "Check YAML syntax, ensure
  `toolsets:` uses array format (`[default]` not `default`), and verify
  `allowed:` is an array."
- **Confidence**: settled (first-party troubleshooting guidance; format
  requirements are specified)
- **Quote**: "Check YAML syntax, ensure `toolsets:` uses array format
  (`[default]` not `default`), and verify `allowed:` is an array."
- **Our assessment**: The scalar-vs-array distinction is a common YAML gotcha
  that causes validation failures without an obvious error message. For Ch02
  and any troubleshooting section: add this as a validation rule alongside
  the `gh aw compile --validate --strict` command. The `--strict` flag catches
  these format errors before deployment.

### Claim 10: The getting-started page links to five downstream resources in a pedagogical progression from tutorial to reference

- **Evidence**: The "Next Steps" section explicitly links to: "Using MCPs —
  Complete MCP configuration reference", "Tools Reference — All available tools
  and options", "Security Guide — MCP security best practices", "CLI Commands —
  Full CLI documentation including `mcp` commands", and "Imports — Shared MCP
  configurations in `.github/workflows/shared/mcp/`."
- **Confidence**: settled (first-party; link structure is directly observable
  in the page)
- **Quote**: (no direct quote; see Concrete Artifacts for the link targets)
- **Our assessment**: The link to the Imports documentation via "Next Steps"
  confirms that the shared MCP configuration library (17 pre-built servers
  documented in `docs-ghaw-mcps.md` Claim 9) is reachable from the
  getting-started path. Practitioners following the tutorial will encounter the
  shared library as a next step rather than discovering it independently. For
  Ch02: the recommended learning path encodes as: getting-started → shared
  library (check first) → custom configuration (only if needed). The page's
  link structure explicitly encodes this progression.

## Concrete Artifacts

### Quick Start: Step 1 — Minimal Workflow with `toolsets: [default]`

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  issues: read
tools:
  github:
    toolsets: [default]
---
# Issue Analysis Agent
Analyze the issue and provide a summary of similar existing issues.
```

*Source: `guides/getting-started-mcp` — "Quick Start: Step 1: Add GitHub Tools" section*

### Quick Start: Step 2 — Compile and Verify Commands

```bash
# Compile the workflow
gh aw compile my-workflow

# Verify MCP configuration
gh aw mcp inspect my-workflow
```

*Source: `guides/getting-started-mcp` — "Quick Start: Step 2: Compile and Test" section*

### Available GitHub MCP Toolsets (Full Table)

```
Toolset        | Description               | Example Tools
-------------- | ------------------------- | -------------------------------------------
context        | User and team information | get_teams, get_team_members
repos          | Repository operations     | get_repository, get_file_contents, list_commits
issues         | Issue management          | list_issues, create_issue, update_issue
pull_requests  | PR operations             | list_pull_requests, create_pull_request
actions        | Workflow runs/artifacts   | list_workflows, list_workflow_runs
discussions    | GitHub Discussions        | list_discussions, create_discussion
code_security  | Security alerts           | list_code_scanning_alerts
users          | User profiles             | get_me, get_user, list_users

Default toolset ([default]): context + repos + issues + pull_requests
Note: `users` excluded — GitHub Actions tokens do not support user operations
```

*Source: `guides/getting-started-mcp` — "GitHub MCP Server: Available Toolsets" section*

### Configuration Pattern Decision Rule: Toolsets vs. Allowed

```yaml
# Toolsets pattern (recommended for GitHub built-in MCP — stable across versions):
tools:
  github:
    toolsets: [default]  # Expands to: context, repos, issues, pull_requests

# Allowed pattern (for custom non-GitHub MCP servers):
mcp-servers:
  notion:
    container: "mcp/notion"
    allowed: ["search_pages", "get_page"]
```

*Source: `guides/getting-started-mcp` — "Configuration Patterns" section*

### Custom MCP Server Types (Three Approaches)

```yaml
mcp-servers:
  # Command-based (stdio)
  markitdown:
    command: "npx"
    args: ["-y", "markitdown-mcp"]
    allowed: ["*"]

  # Docker container
  ast-grep:
    container: "mcp/ast-grep:latest"
    allowed: ["*"]

  # HTTP endpoint with auth
  slack:
    url: "https://api.slack.com/mcp"
    env:
      SLACK_BOT_TOKEN: "${{ secrets.SLACK_BOT_TOKEN }}"
    network:
      allowed: ["api.slack.com"]
    allowed: ["send_message", "get_channel_history"]
```

*Source: `guides/getting-started-mcp` — "Custom MCP Servers" section*

### Practical Example 1: Issue Triage with Safe Output

```yaml
---
on:
  issues:
    types: [opened]
permissions:
  contents: read
  issues: read
tools:
  github:
    toolsets: [default]
safe-outputs:
  add-comment:
---
# Issue Triage Agent
Analyze issue #${{ github.event.issue.number }} and add a comment with category, related issues, and suggested labels.
```

*Source: `guides/getting-started-mcp` — "Practical Examples: Example 1: Basic Issue Triage" section*

### Practical Example 2: Multi-Service Integration (Security Audit)

```yaml
---
on: weekly on sunday
permissions:
  contents: read
  security-events: read
  discussions: write
tools:
  github:
    toolsets: [default, code_security, discussions]
safe-outputs:
  create-discussion:
    category: "Security"
    title-prefix: "[security-scan] "
---
# Security Audit Agent
Review code scanning alerts and create weekly security discussions with findings.
```

*Source: `guides/getting-started-mcp` — "Practical Examples: Example 2: Multi-Service Integration" section*

### Debugging and Validation Commands

```bash
# View all configured MCP servers
gh aw mcp inspect my-workflow

# Get detailed server information
gh aw mcp inspect my-workflow --server github --verbose

# List available tools for a specific server
gh aw mcp list-tools github my-workflow

# Validate configuration with strict mode
gh aw compile my-workflow --validate --strict
```

*Source: `guides/getting-started-mcp` — "Debugging MCP Configurations" section*

### Registry-Based MCP Server (with Informational `registry:` Field)

```yaml
mcp-servers:
  markitdown:
    registry: https://api.mcp.github.com/v0/servers/microsoft/markitdown
    container: "ghcr.io/microsoft/markitdown"
    allowed: ["*"]
```

*Source: `guides/getting-started-mcp` — "MCP Registry" section*

### Troubleshooting Quick Reference

```
Problem: Tool not found
→ Run: gh aw mcp inspect my-workflow
→ Ensure correct toolset is enabled or tool names in allowed: match exactly

Problem: Authentication errors
→ Verify the secret exists in repository settings with required scopes

Problem: Connection failures
→ Check URL syntax (HTTP servers), network config (containers), Docker image availability

Problem: Validation errors
→ toolsets: must use array format ([default] not default)
→ allowed: must be an array
→ Run: gh aw compile my-workflow --validate --strict
```

*Source: `guides/getting-started-mcp` — "Troubleshooting" section*

### Next Steps Link Map (Pedagogical Progression)

```
guides/getting-started-mcp  →  Next Steps:
  1. guides/mcps             — Complete MCP configuration reference
  2. reference/tools         — All available tools and options
  3. (Security Guide)        — MCP security best practices
  4. (CLI Commands)          — Full CLI documentation incl. mcp commands
  5. reference/imports       — Shared MCP configs in .github/workflows/shared/mcp/
```

*Source: `guides/getting-started-mcp` — "Next Steps" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-mcps.md` Claim 1 (custom MCP servers should be read-only; write
    operations must go through safe outputs): Claim 4 here independently states
    the same read-only + safe-outputs architecture for the built-in GitHub MCP
    server — "The GitHub MCP server always operates read-only. Write operations
    are handled through safe outputs, which run in a separate
    permission-controlled job." The distinction: the mcps.md note applies to
    custom servers and notes a compliance gap (server-side enforcement required);
    this note applies to the built-in server and states it "always" operates
    read-only (stronger, platform-level enforcement implied).
  - `docs-ghaw-mcps.md` Claim 8 (registry field is "primarily informational"):
    Claim 7 here provides a direct quote confirming this — "Registry usage is
    informational and not enforced by gh-aw." This upgrades the confidence of
    `docs-ghaw-mcps.md` Claim 8 from "emerging" to settled-by-direct-quote. The
    Assayer may wish to note this upgrade when reviewing.
  - `docs-ghaw-mcps.md` Claim 3 (`allowed:` field implements minimal-privilege
    access for custom MCP servers): the `allowed:` pattern in Claim 6 and
    Concrete Artifacts here is consistent with that note's detailed treatment.
  - `docs-ghaw-mcps.md` Claim 7 (`gh aw mcp add` CLI integrates with the
    GitHub MCP registry): Claim 8 here extends that claim by documenting the
    auto-recompile behavior — the mcps.md note documented the commands but did
    not specify that `gh aw mcp add` triggers automatic recompilation.

- **Extends**:
  - `docs-ghaw-mcps.md` (complete MCP configuration reference): this note
    provides the conceptual onboarding path and tutorial walkthrough that
    `docs-ghaw-mcps.md` presupposes. The two together give the complete MCP
    integration story: getting-started (this note, tutorial) → configuration
    reference (mcps.md, advanced configuration). Together they cover the full
    range from first integration to production harness.
  - `docs-ghaw-mcps.md` Claim 7 (`gh aw mcp` CLI family): Claim 8 here adds
    the operationally significant detail that `gh aw mcp add` recompiles
    automatically — no separate `gh aw compile` step needed after adding a
    registry server.
  - `docs-ghaw-setup-creating-workflows.md` Claim 3 (manual editing requires
    explicit `gh aw compile`): Claim 8 here adds the contrast — `gh aw mcp add`
    recompiles automatically, whereas manual frontmatter edits require explicit
    compile. The two together define when recompilation is automatic vs. manual.
  - `docs-ghaw-guides-editing-workflows.md` Claim 6 (adding a `tools:` block
    requires recompilation): the Quick Start sequence (Claim 6) confirms this
    in practice — Step 1 adds `toolsets: [default]` to frontmatter; Step 2
    requires running `gh aw compile`. The editing-workflows note states the
    rule; this note shows the complete operational procedure.

- **Contradicts**: None identified. No claims in this source materially oppose
  existing source notes. The framing difference between built-in GitHub MCP
  server policy ("always operates read-only," platform-enforced) and custom
  server policy ("should be read-only," server-side enforcement required) is a
  distinction based on server type, not a contradiction — both lead to
  consistent guide advice. No contradiction issue required.

- **Novel**:
  - **`toolsets:` stability contract** (Claim 2): The explicit statement that
    toolset names are stable across MCP server version changes while individual
    tool names may change is not documented in any other source note. This is a
    platform guarantee with direct implications for workflow maintenance and
    upgrade planning.
  - **`users` toolset excluded from `default` due to GitHub Actions token
    limitations** (Claim 3): No existing source note documents this specific
    exclusion or its rationale. The `users` toolset requiring a non-Actions-token
    auth context is a capability constraint that would surprise practitioners
    expecting all GitHub MCP toolsets to work uniformly.
  - **Remote vs. local operating modes for the built-in GitHub MCP server**
    (Claim 5): The `mode: remote` / `mode: local` distinction for the built-in
    GitHub MCP server is not documented in any existing source note.
  - **`gh aw mcp add` auto-recompile behavior** (Claim 8): The explicit
    statement that `gh aw mcp add` automatically recompiles is not present in
    `docs-ghaw-mcps.md` or any other source note. This clarifies when `gh aw
    compile` is and is not needed.
  - **YAML format troubleshooting rules** (Claim 9): The specific scalar-vs-array
    format requirements for `toolsets:` and `allowed:` as a troubleshooting
    pattern are not documented in any existing note.
  - **Direct quote confirming registry field as informational** (Claim 7):
    While `docs-ghaw-mcps.md` Claim 8 assessed this as "emerging," this source
    provides the first direct verbatim quote confirming it.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add toolsets stability contract as a selection criterion** (Claim 2): When
  introducing MCP tool configuration, recommend `toolsets:` over individual
  tool names for GitHub MCP integration. The rationale: toolset names are the
  stable API surface; individual tool names may change. Cite: "Toolsets remain
  stable across MCP server versions, while individual tool names may change."

- **Document the `users` toolset exclusion from `default`** (Claim 3): Add a
  note to the toolset documentation that `users` is excluded from `[default]`
  because GitHub Actions tokens do not support user operations. Practitioners
  who need user lookup must configure a different authentication context.

- **Add remote vs. local mode selection for the GitHub MCP server** (Claim 5):
  Document the `mode: remote` (default, hosted, no Docker) vs. `mode: local`
  (Docker, version-pinned) distinction. Recommend remote as the default; local
  for GHE, air-gapped, or strict reproducibility environments.

- **Separate the two MCP onboarding sequences** (Claim 6 + `docs-ghaw-mcps.md`
  Claim 7): The correct sequence depends on which MCP type is being configured:
  (1) GitHub MCP toolset path: add `toolsets:` → `gh aw compile` → `gh aw mcp
  inspect`; (2) custom server path: `gh aw mcp add` (auto-recompiles) →
  `inspect` → `list-tools` → set `allowed:`. Both should be documented
  separately.

- **Document `gh aw mcp add` auto-recompile** (Claim 8): When adding a new MCP
  server via `gh aw mcp add`, recompilation is automatic — no separate
  `gh aw compile` step needed. Contrast with manual frontmatter edits, which
  require explicit compile.

- **Add YAML format validation rules to troubleshooting** (Claim 9): `toolsets:`
  requires array format (`[default]` not `default`); `allowed:` must be an
  array. Pair with `gh aw compile my-workflow --validate --strict` as the
  validation command.

### Chapter 03: Safety and Verification

- **Clarify read-only enforcement difference between built-in and custom MCP
  servers** (Claim 4 vs. `docs-ghaw-mcps.md` Claim 1): The built-in GitHub MCP
  server "always operates read-only" (platform-level enforcement); custom MCP
  servers "should be read-only" (policy-level guidance, server-side enforcement
  required). Ch03's treatment of the MCP compliance gap should apply this
  distinction — the gap is a custom-server concern, not a built-in-server
  concern.

## Extraction Notes

1. **Two WebFetch passes for completeness**: Two separate WebFetch passes were
   used to maximize content capture from the gh-aw documentation SPA
   (Astro/Starlight). The passes returned consistent content for key sections.
   Quotes marked as verbatim were confirmed consistent across both passes.

2. **Toolsets table content verified**: The full toolsets table (8 toolsets with
   descriptions and example tools) was consistent across both WebFetch passes
   and is treated as accurate to the source.

3. **Quick Start sequence verified**: The three-step Quick Start sequence (add
   toolsets → compile → inspect) was confirmed verbatim across both fetches.

4. **No publication date**: The documentation does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-12.

5. **No contradictions to file**: Reviewed all existing source notes and
   CONTRADICTIONS.md. No claims in this source materially oppose any existing
   source note at the MINER.md §4a filing threshold. The framing difference
   between built-in GitHub MCP server policy ("always read-only") and custom
   server policy ("should be read-only") is a distinction by server type, not
   a contradiction — both lead to identical guide advice.

6. **Registry field confidence upgrade**: This source provides a direct quote
   ("Registry usage is informational and not enforced by gh-aw") that confirms
   what `docs-ghaw-mcps.md` Claim 8 assessed as "emerging." The Assayer may
   wish to note this when reviewing `docs-ghaw-mcps.md`.
