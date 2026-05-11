---
source_url: https://github.github.com/gh-aw/reference/tools
source_type: docs
title: "GitHub Agentic Workflows: Tools Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#416"
---

# GitHub Agentic Workflows: Tools Reference

> The authoritative catalogue of all built-in tool capabilities available to
> gh-aw workflows — documents twelve tool categories (edit, github, bash, web-fetch,
> web-search, playwright, cache-memory, repo-memory, qmd, agentic-workflows,
> cli-proxy, mcp-servers), their configuration options, engine-specific behavioral
> differences, timeout parameters, and the import-merging semantics that make
> shared tool libraries possible.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/tools` page — in the
  "Reference" section, documenting the complete tool surface available in workflow
  frontmatter. Distinct from `docs-ghaw-mcps.md`, which documents the configuration
  of custom MCP servers in detail; this page is the overview and reference for both
  built-in tools and MCP server declarations. Distinct from `docs-ghaw-how-they-work.md`,
  which explains the conceptual "why"; this page is the "what exists and how to
  configure it.")
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the `gh aw` CLI.
  Tool names, configuration fields, defaults, and engine-specific behaviors are
  authoritative for the `gh aw` platform. Claims about specific tool defaults and
  behaviors are settled platform facts for gh-aw; they do not automatically
  generalize to other agentic frameworks.
- **Scope**: Complete reference for the `tools:` frontmatter section — all twelve
  tool types, their parameters, defaults, and constraints; timeout configuration;
  import-merge semantics for shared tool libraries. Does NOT cover: custom MCP server
  configuration in depth (see `docs-ghaw-mcps.md`), network egress controls (see
  `docs-ghaw-network-reference.md`), permissions for write operations (see
  `docs-ghaw-permissions-reference.md`), or the GitHub-specific read-tool reference
  (issue #396, PR #647).

## Extracted Claims

### Claim 1: The `tools:` frontmatter section is the declarative capability sandbox for gh-aw workflows — all tools from imported shared components are merged into the final compiled workflow

- **Evidence**: The page states that "All tools declared in imported components are
  merged into the final workflow," and documents that tools are configured within the
  `tools:` section of the workflow frontmatter. This merge behavior enables reusable
  tool library components — a shared component can declare standard tools, and
  any workflow that imports it automatically gains those tools in the final compiled
  output.
- **Confidence**: settled (first-party documentation; the merge behavior is explicitly
  stated)
- **Quote**: "All tools declared in imported components are merged into the final workflow."
- **Our assessment**: The import-merge semantics transform the `tools:` section from
  a per-workflow declaration into a composable capability layer. A team can define a
  standard tool set in a shared component and have it available across all workflows
  that import it — reducing repetition and ensuring consistent tool access. This is
  the tool-layer complement to the import system for workflow structure (covered in
  `docs-ghaw-compilation-process.md` Claim 1, which documents the breadth-first
  import traversal during the parse phase). For Ch02 (Harness Engineering): shared
  tool components are an underused pattern for standardizing tool access across a
  workflow library. Define tool sets in shared components, import them, and maintain
  them in one place.

### Claim 2: The `bash:` tool defaults to a curated safe-command list and requires explicit wildcard or unrestricted grant to expand to additional shell capabilities

- **Evidence**: The documentation specifies that bash "Defaults to safe commands
  (`echo`, `printf`, `ls`, `pwd`, `cat`, `head`, `tail`, `grep`, `wc`, `sort`,
  `uniq`, `date`, `yq`)." Expansion mechanisms include wildcards for command families
  (e.g., `git:*`) or unrestricted access (`:*`).
- **Confidence**: settled (first-party documentation; the safe-command list is
  explicitly enumerated)
- **Quote**: "Defaults to safe commands (`echo`, `printf`, `ls`, `pwd`, `cat`,
  `head`, `tail`, `grep`, `wc`, `sort`, `uniq`, `date`, `yq`)."
- **Our assessment**: The default safe-command list is lean — 13 read-oriented
  commands covering file inspection, text processing, and time output. Notably absent
  from the safe list: `git`, `curl`, `wget`, `npm`, `pip`, `make`, any build tools,
  or any package managers. A workflow that needs to run `git log`, run tests, or
  install dependencies must explicitly expand bash access (e.g., `git:*` for all
  git subcommands). The `:*` unrestricted mode should be used only when the workflow
  requires arbitrary shell execution and the security posture permits it. For Ch02:
  document the default safe list as the baseline and name `git:*` + individual
  command families as the recommended expansion pattern over `:*`. For Ch03
  (Safety and Verification): the bash safe list is Layer 3 (permission separation)
  of the five-layer security model applied to shell commands — a practitioner who
  grants `:*` has effectively removed shell command isolation.

### Claim 3: `web-search:` has engine-specific behavior — disabled by default for the Codex engine (which runs with `-c web_search="disabled"`) and must be explicitly declared in workflow frontmatter to activate

- **Evidence**: The documentation states: "For the **Codex** engine, `web-search:`
  is disabled by default. Web search is only enabled when explicitly declared."
  The mechanism is described as running with `-c web_search="disabled"` in the
  absence of an explicit declaration.
- **Confidence**: settled (first-party documentation; engine-specific default behavior
  is a platform specification)
- **Quote**: "For the **Codex** engine, `web-search:` is disabled by default. Web
  search is only enabled when explicitly declared."
- **Our assessment**: This is the only built-in tool with documented
  engine-specific default behavior — all other tools appear to apply uniformly.
  Codex disabling web search by default is notable because web search can cause
  significant latency and token cost; requiring explicit declaration is a
  conservative default for a batch-oriented engine. For Ch04 (Context Engineering /
  Tool Choice): when porting a workflow from Copilot/Claude to Codex, practitioners
  must explicitly add `web-search:` to the frontmatter or web access silently fails.
  This is a common migration footgun. For Ch02: document the Codex web-search
  exception as a per-engine configuration difference in the tools reference.

### Claim 4: The `cli-proxy:` tool mounts configured MCP servers as standalone CLI commands on PATH, directly reducing the token consumption caused by large MCP tool schemas in the agent context

- **Evidence**: The documentation describes `cli-proxy: true` as a configuration
  option that "mount[s] each user-facing MCP server as a standalone CLI tool on
  `PATH`," with the explicit benefit of reducing token consumption from large tool
  schemas. When MCP servers are accessed via CLI rather than as JSON-schema-described
  tools, their full schema definitions are not loaded into the agent's system prompt.
- **Confidence**: settled (first-party documentation; the mechanism and token-cost
  benefit are stated explicitly)
- **Quote**: "mount[s] each user-facing MCP server as a standalone CLI tool on `PATH`"
- **Our assessment**: This is the platform-level structural answer to the MCP token
  cost problem documented in `blog-bswen-mcp-token-cost.md` — specifically Claim 1
  (every MCP server loads all its tool definitions before you type anything). The
  `cli-proxy:` mechanism provides a third tool access mode beyond the two documented
  in `docs-ghaw-mcps.md`: (1) native MCP tool protocol with full JSON schema loading,
  (2) `allowed:` filtering to reduce which schemas load, (3) `cli-proxy:` to bypass
  schema loading entirely and treat the server as a CLI tool. For Ch04: document
  `cli-proxy: true` as the maximum token-reduction option for MCP servers with
  large or numerous tool schemas. The trade-off is reduced discoverability for the
  agent — CLI tools are invoked by command, not selected from a typed tool list.
  For Ch02: document `cli-proxy: true` as a configuration option alongside
  `allowed:` for MCP token management.

### Claim 5: Two built-in memory tools serve distinct persistence scopes — `cache-memory:` for cross-run trend data and `repo-memory:` for repository-specific context — enabling explicit workflow state design

- **Evidence**: The documentation distinguishes: `cache-memory:` provides "Persistent
  memory storage across workflow runs for trends and historical data," while
  `repo-memory:` offers "Repository-specific memory storage for maintaining context
  across executions." These are two separate tool declarations with different
  persistence semantics.
- **Confidence**: settled (first-party documentation; the distinction is explicitly
  stated)
- **Quote**: (from `cache-memory:` description) "Persistent memory storage across
  workflow runs for trends and historical data"
- **Our assessment**: The two-memory-tool taxonomy implies meaningfully different
  use cases: `cache-memory:` is appropriate for cross-repository or organizational
  state (e.g., tracking error counts across all repos monitored by a central
  workflow), while `repo-memory:` is appropriate for repository-specific context
  that should not leak across repositories (e.g., tracking decisions made about
  specific files or issues in a repo). The distinction matters for both security
  (isolating repository state) and relevance (cross-repo trends vs. repo-specific
  context). For Ch02: when designing a workflow that needs memory, practitioners
  must choose between these two tools based on the scope of state they want to
  persist. For Ch04: `repo-memory:` is the tool for maintaining agent context between
  invocations on the same repository — a lightweight alternative to embedding full
  history in each workflow run's prompt.

### Claim 6: The `qmd:` tool is an experimental documentation search capability that builds vector search indexes over documentation files with pattern-based checkout support

- **Evidence**: The documentation describes `qmd:` as a tool that "Builds vector
  search indexes over documentation with pattern-based checkout support" and marks
  it as experimental.
- **Confidence**: emerging (first-party documentation; the "experimental" label
  signals the feature may not be production-stable, and technical details were not
  fully elaborated in the fetched content)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `qmd:` tool provides in-workflow semantic search over
  documentation — a workflow can index a documentation directory and then query it
  using vector similarity rather than exact text matching. The "pattern-based
  checkout" implies the tool can selectively check out portions of documentation
  matching a file pattern, enabling targeted indexing of large documentation sets
  without loading everything. The experimental status suggests practitioners should
  not build production workflows that depend on this tool until it stabilizes.
  For Ch04 (Context Engineering): `qmd:` is a context engineering tool — it
  allows an agent to retrieve semantically relevant documentation at runtime
  rather than statically including documentation in the system prompt. This is
  RAG (retrieval-augmented generation) as a first-class platform primitive.

### Claim 7: The `agentic-workflows:` introspection tool is the only built-in tool with a documented explicit permission requirement — `actions: read` — and provides workflow debugging and log analysis capabilities

- **Evidence**: The documentation states that `agentic-workflows:` "Requires
  `actions: read` permission" to function, and describes it as providing workflow
  debugging and log analysis. No other built-in tool in the reference carries an
  explicit permission prerequisite.
- **Confidence**: settled (first-party documentation; the permission requirement
  and tool purpose are explicitly stated)
- **Quote**: "Requires `actions: read` permission"
- **Our assessment**: The `actions: read` requirement is consistent with
  `docs-ghaw-permissions-reference.md` Claim 4 (ten standard read scopes include
  `actions` — workflow control). The introspection tool needs to read GitHub Actions
  run logs and workflow state, which requires this scope. The fact that no other
  built-in tool has an explicit permission requirement suggests the other tools
  either work with zero-permission (e.g., `bash:`, `edit:` operate on the local
  workspace) or use a platform-level default permission (e.g., `github:` may use
  the inherited workflow token). For Ch02: document `actions: read` as a required
  permission when including `agentic-workflows:` in a workflow. Without it, the
  tool silently fails or errors at runtime. For Ch03: the `agentic-workflows:`
  tool is the observability mechanism for diagnosing agent behavior — include it
  in development and debugging workflows, but evaluate whether it should be in
  production workflows that prefer minimal permissions.

### Claim 8: Two timeout parameters govern tool execution — `tools.timeout` (per-operation, Claude: 60s default, Codex: 120s default) and `tools.startup-timeout` (MCP initialization, 120s default) — both accept GitHub Actions expressions for parameterization

- **Evidence**: Documentation specifies: `tools.timeout` sets per-operation timeout
  with engine-specific defaults ("Defaults vary by engine (Claude: 60 s, Codex: 120
  s)"), and `tools.startup-timeout` controls MCP server initialization with a 120s
  default. Both parameters accept integers or GitHub Actions expressions.
- **Confidence**: settled (first-party documentation; specific default values and
  expression support are explicitly stated)
- **Quote**: "Defaults vary by engine (Claude: 60 s, Codex: 120 s)."
- **Our assessment**: The Codex-higher default for per-operation timeout (120s vs
  Claude's 60s) is consistent with Codex being a batch-processing engine designed
  for longer operations. Claude's 60s default may be too low for operations involving
  large file reads, web fetches, or complex bash commands — practitioners running
  Claude against slow operations may need to increase `tools.timeout` explicitly.
  The `tools.startup-timeout` (MCP initialization) at 120s is a hard ceiling for
  MCP server startup — if a Docker-based MCP server takes longer than 120s to
  become ready, the workflow fails. For Ch02: document that `tools.timeout` may
  need to be increased for workflows running operations that exceed 60s (network
  fetches, large file processing, long-running build commands). The expression
  support (e.g., `${{ inputs.timeout }}`) enables reusable workflow templates
  with caller-configurable timeout budgets.

### Claim 9: The `github:` tool provides GitHub API access with configurable toolsets, remote/local modes, and authentication — it is the primary mechanism for reading GitHub repository state within workflows

- **Evidence**: The documentation describes `github:` as configuring "GitHub API
  operations including toolsets, remote/local modes, and authentication." The
  tool is the standard mechanism for workflows that need to read issues, PRs, code,
  discussions, or other GitHub-hosted data.
- **Confidence**: settled (first-party documentation; the capability description
  is explicitly stated)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `github:` tool's configurable toolsets imply that the
  practitioner can restrict which GitHub API operations are exposed to the agent —
  the toolset configuration is the `allowed:` equivalent for GitHub API operations
  (analogous to `allowed:` for MCP servers in `docs-ghaw-mcps.md` Claim 3). The
  "remote/local modes" distinction suggests a local mode that works against a local
  git clone (useful for operations on checked-out content) vs. a remote mode that
  makes GitHub API calls. For Ch02: the `github:` tool is the foundational read
  access tool for any workflow that processes GitHub repository state. The
  toolsets configuration is the lever for scoping GitHub API access to the minimum
  needed. For Ch04: `github:` is the primary tool for reading context from GitHub
  into the agent; toolset configuration determines what GitHub context is available
  for the agent to work with.

### Claim 10: `playwright:` supports version pinning via an optional `version:` parameter, enabling reproducible browser automation at a specific Playwright library version

- **Evidence**: The documentation states that `playwright:` accepts an optional
  version specification (example: `version: "1.56.1"`) for browser automation.
- **Confidence**: settled (first-party documentation; the parameter and example are
  explicitly stated)
- **Quote**: (no direct quote; version parameter example is "1.56.1" per documentation)
- **Our assessment**: Version pinning for Playwright is the browser automation
  equivalent of action pinning in the compilation process (`docs-ghaw-compilation-process.md`
  Claim 4) — it prevents unexpected behavior from upstream library updates. Without
  version pinning, a Playwright update could change browser behavior, selector APIs,
  or screenshot formats and silently break a workflow that depends on them. For Ch02:
  recommend pinning the `playwright:` version in production workflows, especially
  those that interact with specific web interfaces or take screenshots for comparison.
  The version pin should be updated intentionally, with testing, rather than
  inheriting the platform's latest Playwright.

## Concrete Artifacts

### Complete Built-in Tool Catalogue (from reference page)

```
Built-in tools (configured in tools: frontmatter section):

CORE TOOLS:
  edit:               — File editing in GitHub Actions workspace
  github:             — GitHub API operations (toolsets, remote/local, auth)
  bash:               — Shell commands; safe defaults; wildcard expansion
  web-fetch:          — Web content retrieval
  web-search:         — Web searching (Codex: disabled by default)
  playwright:         — Browser automation (version: pin optional)

MEMORY & SEARCH TOOLS:
  cache-memory:       — Cross-run persistent storage (trends, historical data)
  repo-memory:        — Repository-specific persistent context between executions
  qmd:                — [EXPERIMENTAL] Vector search over documentation files
                         (pattern-based checkout support)

ADVANCED TOOLS:
  agentic-workflows:  — Workflow introspection and log analysis
                         (requires: actions: read permission)
  cli-proxy:          — Mounts MCP servers as standalone CLI tools on PATH
                         (reduces token consumption from large tool schemas)

CUSTOM TOOLS (external):
  mcp-servers:        — Custom MCP server declarations (see docs-ghaw-mcps.md)
```

*Source: docs-ghaw-tools-reference, built-in tools overview*

### Bash Safe-Command Default List

```
Default safe commands for bash: tool (no explicit expansion needed):
  echo    printf    ls      pwd     cat
  head    tail      grep    wc      sort
  uniq    date      yq

Expansion options (configured in bash: block):
  git:*    — All git subcommands (family wildcard)
  :*       — Unrestricted shell access (use with caution)
```

*Source: docs-ghaw-tools-reference, bash: tool configuration section*

### Timeout Configuration

```yaml
tools:
  # Per-operation timeout (seconds); accepts GitHub Actions expressions
  # Engine defaults: Claude 60s, Codex 120s
  timeout: 90

  # MCP server startup timeout (seconds, default: 120)
  # Both accept GitHub Actions expressions for reusable workflows
  startup-timeout: "${{ inputs.mcp-timeout || 120 }}"
```

*Source: docs-ghaw-tools-reference, "Timeout Configuration" section*

### Codex Web Search Declaration

```yaml
# For Codex engine: web-search: must be explicitly declared
# Without this, Codex runs with -c web_search="disabled"
tools:
  web-search: {}
```

*Source: docs-ghaw-tools-reference, engine-specific web-search behavior*

### Tool Merging via Import (Conceptual)

```yaml
# Shared component: .github/workflows/shared/standard-tools.md
---
tools:
  github: {}
  bash:
    allow:
      - "git:*"
  cache-memory: {}
---

# Workflow that imports it inherits all declared tools:
# The final compiled workflow has github:, bash: (with git:*),
# and cache-memory: merged from the shared component.
```

*Source: docs-ghaw-tools-reference, import merging semantics*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-mcps.md` Claim 3 (`allowed:` as minimal-privilege tool filter and
    token-cost control) and Claim 10 (per-server `allowed:` granularity): the
    `cli-proxy:` mechanism (Claim 4 here) is the third tool in the same toolkit —
    `allowed:` restricts which tool schemas load; `cli-proxy:` bypasses schema
    loading entirely. Both are token management strategies at the MCP layer.
    `docs-ghaw-mcps.md` documents the former; this note documents the latter.
  - `blog-bswen-mcp-token-cost.md` Claim 1 (every MCP server loads all its tool
    definitions before you type anything): `cli-proxy:` (Claim 4 here) is the
    structural mitigation for this problem. Bswen identifies token cost from tool
    schemas as a first-class concern; the platform's `cli-proxy:` option eliminates
    schema loading by exposing MCP servers as CLI tools instead.
  - `docs-ghaw-how-they-work.md` Claim 4 (workflows run with minimal permissions,
    use tool allowlists): the tool catalogue here is the specific set of tools
    available to populate those allowlists. The "no write access by default"
    principle applies tool-by-tool: `bash:` defaults to safe commands; `github:`
    defaults to read operations; `agentic-workflows:` needs an explicit `actions: read`
    grant.
  - `docs-ghaw-permissions-reference.md` Claim 4 (ten standard read scopes include
    `actions`): the `agentic-workflows:` tool's `actions: read` requirement (Claim 7
    here) is a concrete instance of a workflow needing that scope. The permissions
    reference documents what `actions: read` unlocks; this note shows which tool
    triggers the need for it.
  - `docs-ghaw-compilation-process.md` Claim 1 (parse phase resolves imports via
    breadth-first traversal): the import-merge semantics for tools (Claim 1 here)
    are implemented during the parse phase. Together, the two notes explain both
    the mechanism (breadth-first import traversal) and the effect (all imported
    tools merge into the final workflow's tool list).

- **Extends**:
  - `docs-ghaw-mcps.md`: this note provides the reference-level overview of where
    `mcp-servers:` fits in the broader tool catalogue. Together, this reference
    note (all twelve tool types) + `docs-ghaw-mcps.md` (detailed MCP server
    configuration) give practitioners the full tool surface: built-in capabilities
    and custom MCP extensions.
  - `docs-ghaw-how-they-work.md` Claim 1 (YAML frontmatter constrains, markdown
    instructs): this note is the detailed specification for the `tools:` portion
    of that frontmatter. The how-they-work note names "tools" as a frontmatter key;
    this reference documents every valid tool declaration.
  - `docs-ghaw-web-search.md`: that note documents the Tavily MCP server as the
    web search integration (external MCP approach). This note documents `web-fetch:`
    and `web-search:` as built-in platform tools (no MCP server required). Together,
    practitioners have two web access paths: built-in `web-search:` for basic search,
    Tavily MCP (`docs-ghaw-web-search.md`) for enhanced/configurable search.
  - `docs-ghaw-network-reference.md` Claim 4 (ecosystem identifiers for network
    access): the `cache-memory:`, `web-fetch:`, and `web-search:` tools all
    make network calls and may require `network.allowed` configuration. The
    network reference provides the domain-allowlisting mechanism; this note
    identifies which tools trigger the need for it.

- **Contradicts**: None identified. No existing source note makes claims that
  conflict with the tool catalogue, bash defaults, or timeout parameters documented
  here. The `cli-proxy:` mechanism is mentioned briefly in `docs-ghaw-mcps.md`
  and is consistent with this page's description. The Codex web-search behavior
  is consistent with `docs-ghaw-how-they-work.md` Claim 9 (multi-engine support
  using the same workflow structure). No contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **Bash safe-command default list** (Claim 2): No existing source note documents
    the thirteen specific safe commands available to `bash:` by default. The
    `docs-ghaw-how-they-work.md` Claim 4 names "tool allowlists" as a mechanism
    but does not enumerate them. This is the first concrete specification of
    bash's default permission scope.
  - **Codex web-search disabled by default** (Claim 3): No existing source note
    documents this engine-specific behavioral difference. `docs-ghaw-how-they-work.md`
    Claim 9 covers multi-engine support but not per-engine tool defaults.
  - **`cache-memory:` vs `repo-memory:` as distinct persistence scopes** (Claim 5):
    The two memory tools and their scope distinction (cross-run/cross-repo vs.
    repo-specific) are not documented in any existing source note. Several pattern
    notes reference `cache-memory:` in examples but none explains the distinction
    between the two memory types.
  - **`qmd:` as experimental vector-search documentation tool** (Claim 6):
    Not mentioned in any existing source note.
  - **Engine-specific timeout defaults** (Claim 8): No existing source note
    documents the specific default timeout values for each engine (Claude: 60s,
    Codex: 120s) or the `tools.startup-timeout` parameter.
  - **Import-merge semantics for tools** (Claim 1): While the compilation process
    note documents import traversal, no existing source note explicitly states that
    tools from imported components merge into the final workflow's tool list —
    enabling shared tool library components.
  - **`playwright:` version pinning** (Claim 10): No existing source note documents
    that browser automation tool versions can be pinned via a `version:` parameter.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add complete built-in tool catalogue as the harness tool reference** (Claim 1,
  Concrete Artifacts): The guide currently lacks a complete enumeration of what
  built-in tools are available in gh-aw workflows. Add the twelve-tool catalogue
  as a reference table. This is the starting point for practitioners designing a
  new workflow's tool configuration.

- **Document bash safe-command defaults as the first shell permission decision**
  (Claim 2): When a workflow needs shell access, practitioners should start from
  the safe list and expand only as needed. Add: "bash: defaults to 13 safe
  commands (echo, printf, ls, pwd, cat, head, tail, grep, wc, sort, uniq, date,
  yq). Use `git:*` to add git access, specific command names for individual tools,
  or `:*` for unrestricted shell." Explicitly warn that `:*` removes the bash
  safety layer.

- **Document `cli-proxy: true` as the maximum token-reduction option for MCP
  servers** (Claim 4): Alongside `allowed:` filtering (`docs-ghaw-mcps.md` Claims
  3 and 10), `cli-proxy: true` eliminates MCP schema loading by treating servers
  as CLI tools. Add this as the third MCP token management strategy, appropriate
  when schema loading from a large multi-tool MCP server is prohibitive.

- **Add `actions: read` as a prerequisite for the `agentic-workflows:` tool**
  (Claim 7): When documenting the introspection tool, include the permission
  requirement explicitly. Practitioners who add `agentic-workflows:` without
  `permissions: actions: read` will see a runtime failure that may not clearly
  indicate the missing permission.

- **Document the import-merge semantics for shared tool libraries** (Claim 1):
  The merge behavior enables a shared-component pattern for standardizing tool
  access across a workflow library. Add as an advanced harness design pattern —
  define a shared tool set once, import it everywhere.

- **Add timeout configuration guidance** (Claim 8): Document `tools.timeout`
  as a tunable parameter: increase above 60s for Claude workflows that run
  slow operations (large file reads, web fetches, long shell commands). Note
  the Codex difference (120s default). Recommend expression syntax for reusable
  workflow templates.

### Chapter 04: Context Engineering / Tool Choice

- **Add `cli-proxy:` as a context budget management mechanism** (Claim 4):
  When a workflow uses MCP servers with large schemas, `cli-proxy: true` removes
  those schemas from the agent's context. Cross-reference with `blog-bswen-mcp-token-cost.md`
  (MCP token cost problem) and `docs-ghaw-mcps.md` `allowed:` filtering (partial
  mitigation). Present the three-lever model: prune servers (`allowed:` servers
  count), prune tools within servers (`allowed:` tool list), bypass schema loading
  (`cli-proxy: true`).

- **Add `qmd:` as a platform-native RAG primitive** (Claim 6): The experimental
  `qmd:` tool enables semantic search over documentation as a first-class tool —
  the agent can retrieve relevant documentation at query time rather than statically
  loading it into the system prompt. Present as a context engineering option for
  documentation-heavy workflows. Flag as experimental; monitor for stabilization.

- **Add `repo-memory:` as the primary mechanism for cross-invocation agent context**
  (Claim 5): When a workflow needs to maintain state between runs on the same
  repository (e.g., tracking which issues were processed, remembering previous
  decisions), `repo-memory:` is the platform-native solution. This avoids the
  context bloat of embedding full history in each invocation's system prompt.

- **Document `web-search:` vs. Tavily MCP as two distinct web search paths**
  (Claims 3, and `docs-ghaw-web-search.md`): The built-in `web-search:` tool
  is simpler to configure but has limited control over search behavior. Tavily
  MCP (`docs-ghaw-web-search.md`) provides richer configuration, tool-level
  control (`search` vs. `search_news`), and explicit engine selection. For Ch04:
  when choosing a web search approach, recommend built-in `web-search:` for
  simple retrieval needs, Tavily MCP for workflows requiring search configurability.

## Extraction Notes

1. **Source uses AI-mediated WebFetch**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch returns rendered text processed through an AI
   model. Two targeted fetches were made: one requesting structured content, one
   requesting verbatim reproduction. Quoted text that appears in quotation marks
   in the fetch output is assessed as verbatim; other descriptions are paraphrased.
   The bash safe-command list and timeout defaults are the most precisely extractable
   technical facts.

2. **`qmd:` is experimental**: The documentation marks `qmd:` as experimental.
   Its configuration options, indexing behavior, and checkout pattern syntax
   were not fully elaborated in the fetched content. Claim 6 is assessed as
   `emerging` accordingly.

3. **`github:` toolset configuration not fully detailed**: The `github:` tool
   references configurable toolsets, but the available toolsets and their
   corresponding API operations are covered in the separate `reference/github-tools`
   page (issue #396, PR #647). This note does not attempt to enumerate those;
   defer to that reference once it is merged.

4. **Tool interaction with `network:` not specified**: Which built-in tools
   require explicit `network.allowed` configuration (beyond the default
   infrastructure domains) is not specified on this page. `web-fetch:` and
   `web-search:` clearly make external network calls; `playwright:` likely does
   too depending on the target URL. The network reference (`docs-ghaw-network-reference.md`)
   is the companion document for that configuration.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is consistent with the current gh-aw platform state
   as of 2026-05-11.

6. **No contradictions filed**: Reviewed all existing corpus source notes. No
   claims in this source materially oppose existing notes. The `cli-proxy:` mention
   in `docs-ghaw-mcps.md` is consistent with this page's description. The
   Codex web-search behavior does not contradict the multi-engine support claim
   in `docs-ghaw-how-they-work.md`.
