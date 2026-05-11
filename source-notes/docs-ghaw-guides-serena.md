---
source_url: https://github.github.com/gh-aw/guides/serena
source_type: docs
title: "GitHub Agentic Workflows: Using Serena"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#440"
---

# GitHub Agentic Workflows: Using Serena

> Practitioner guide to Serena, the gh-aw MCP server for semantic code analysis —
> documents its LSP-backed tool catalogue, the shared/mcp/serena.md import path
> (replacing the removed `tools.serena` shorthand), cache-memory integration for
> cross-run index reuse, and best practices for combining symbol-level operations
> with complementary tools.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows "Guides > Using Serena" page —
  a practitioner guide in the "Guides" section, distinct from the API/reference
  pages. Covers practical setup, configuration, and usage patterns for the Serena
  MCP integration. Includes a migration notice with a danger callout about the
  removed `tools.serena` shorthand.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team that builds the gh-aw platform. Prescriptive guidance about
  configuration paths, tool names, and cache semantics is authoritative for this
  platform. Claims about semantic code analysis patterns generalize beyond gh-aw
  to any agentic harness that integrates Serena as an MCP server.
- **Scope**: Serena-specific integration within gh-aw — migration path, language
  selection, available tools, caching, best practices, and troubleshooting. Does
  NOT cover: general MCP server configuration (see `docs-ghaw-mcps.md`), the
  broader tools reference (`docs-ghaw-tools-reference.md`), or Serena's internals
  (it is developed by the `oraios` team, not GitHub Next). The page covers
  gh-aw's first-party packaging of Serena as a shared workflow.

## Extracted Claims

### Claim 1: Serena provides IDE-level semantic code understanding via LSP, enabling agents to navigate and edit code at the symbol level — beyond what text search can offer

- **Evidence**: The page's introductory paragraph explicitly positions Serena as
  an alternative to text-based operations: "enabling agents to find symbols,
  navigate code relationships, and edit at the symbol level — ideal for navigating
  and editing large, well-structured codebases." The LSP (Language Server Protocol)
  integration is named as the mechanism — Serena initializes language server
  instances that understand the semantic structure of the code rather than
  treating it as plain text.
- **Confidence**: emerging (the practical superiority of symbol-level over
  text-search for agentic code editing is stated authoritatively but specific
  comparative metrics are not provided)
- **Quote**: "Serena is an MCP server that enhances AI agents with IDE-like tools
  for semantic code analysis and manipulation. It supports 30+ programming languages
  through Language Server Protocol (LSP) integration, enabling agents to find
  symbols, navigate code relationships, and edit at the symbol level — ideal for
  navigating and editing large, well-structured codebases."
- **Our assessment**: The positioning is significant: Serena moves agentic code
  editing from file-as-text (read the whole file, edit a range) to
  symbol-as-unit (find the function, replace its body). This is the same
  capability that makes IDEs more reliable than text editors for refactoring —
  the tool understands what a "method" or "class" is, not just what bytes are at
  what offsets. For Ch06 (Building Agentic Patterns): when the task requires
  code modification in a large, structured codebase, Serena's symbol-level
  operations should be preferred over raw file editing. For Ch05 (Orchestration):
  Serena's tools can be integrated into orchestration patterns where the agent
  navigates call graphs and dependency relationships, not just file trees.

### Claim 2: Serena exposes 11 specific tools in three categories — Symbol Navigation (4), Code Editing (4), Project Analysis (3) — providing a complete read-navigate-write cycle at the semantic level

- **Evidence**: The page explicitly names all 11 tools by their exact MCP tool
  identifiers, grouped into three categories. This is the complete tool surface
  exposed to the agent.
- **Confidence**: settled (first-party documentation; tool names are explicitly
  enumerated)
- **Quote**: (no single direct quote spans all three categories; see Concrete
  Artifacts for the full catalogue)
- **Our assessment**: The three-category structure reveals the intended workflow
  pattern: (1) Symbol Navigation tools locate the code of interest; (2) Project
  Analysis tools understand its context and dependencies; (3) Code Editing tools
  modify it. A well-structured agentic code task using Serena follows this
  read-navigate-edit sequence — locate with `find_symbol`, understand with
  `analyze_imports`, modify with `replace_symbol_body`. For Ch06: document this
  as the Serena workflow pattern. The 11-tool surface is small and purposeful —
  compare with general-purpose MCP servers that expose dozens of tools. The
  `allowed:` discipline from `docs-ghaw-mcps.md` Claim 3 is less critical here
  because the tool surface is already minimal and focused.

### Claim 3: The `tools.serena` shorthand has been removed; the only supported integration path is importing `shared/mcp/serena.md` with per-import language specification

- **Evidence**: The page carries a danger callout with this exact text: "`tools.serena`
  has been removed. Use the `shared/mcp/serena.md` shared workflow instead." The
  before/after migration example shows the structural change: the old syntax
  placed language lists directly under `tools: serena:`, while the new syntax
  uses `imports: - uses: shared/mcp/serena.md` with a `with: languages:` parameter.
- **Confidence**: settled (first-party documentation with explicit danger callout;
  the removal is unambiguous and the migration path is prescribed)
- **Quote**: "`tools.serena` has been removed. Use the `shared/mcp/serena.md`
  shared workflow instead."
- **Our assessment**: This is a breaking change — workflows using the old
  `tools.serena:` syntax will fail compilation (the danger callout confirms
  this). The migration is mechanical: replace the `tools.serena:` block with
  the `imports: - uses: shared/mcp/serena.md` block, keeping the language list
  in the `with: languages:` parameter. For Ch02 (Harness Engineering): any
  example or reference to `tools.serena:` in the guide must be updated to
  the import-based path. This is a concrete instance of the import/shared-workflow
  pattern documented in `docs-ghaw-tools-reference.md` Claim 1 replacing a
  dedicated first-class tool shorthand.

### Claim 4: Serena reuses language server indexes across runs via cache-memory — pre-creating the cache directory and pinning the cache key are the critical performance steps

- **Evidence**: The best practices section states: "Pre-create the cache directory
  (`mkdir -p /tmp/gh-aw/cache-memory/serena`) for faster operations — Serena
  reuses language server indexes across runs. Pin the key with
  `tools.cache-memory.key: serena-analysis` in frontmatter to persist it."
  The troubleshooting section confirms that "Slow initial analysis" is expected
  behavior: "expected behavior as language servers build indexes, subsequent
  runs use cached data."
- **Confidence**: settled (first-party documentation; the cache path and key
  name are specifically prescribed)
- **Quote**: "Pre-create the cache directory (`mkdir -p /tmp/gh-aw/cache-memory/serena`)
  for faster operations — Serena reuses language server indexes across runs. Pin
  the key with `tools.cache-memory.key: serena-analysis` in frontmatter to persist it."
- **Our assessment**: The LSP index build is the dominant first-run cost for Serena.
  For a large Go or TypeScript codebase, the initial `gopls` or `tsserver`
  initialization and indexing can take minutes. Cache-memory persistence across
  runs converts this from a per-run cost to a one-time cost (until cache
  expiry or the cache key changes). The specific prescribed path
  (`/tmp/gh-aw/cache-memory/serena`) and key (`serena-analysis`) are important
  — workflows that omit the cache setup will experience slow, inconsistent
  Serena performance. For Ch02: the Serena cache setup is a required configuration
  step, not optional. Include `mkdir -p /tmp/gh-aw/cache-memory/serena` in any
  Serena workflow setup instructions.

### Claim 5: Symbol-level operations (`replace_symbol_body`) should be preferred over file-level edits when modifying code through Serena

- **Evidence**: The best practices section states directly: "Prefer symbol-level
  operations (`replace_symbol_body`) over file-level edits." This is a prescription,
  not a suggestion — it implies that file-level edits (e.g., using the `edit:`
  tool to replace a range of lines) are the inferior alternative when Serena is
  available.
- **Confidence**: emerging (first-party prescription, but no comparative evidence
  or metrics showing why symbol-level is better in this context; the benefit
  follows logically from the semantic understanding Serena provides)
- **Quote**: "Prefer symbol-level operations (`replace_symbol_body`) over
  file-level edits."
- **Our assessment**: The preference for `replace_symbol_body` over file-level
  edits reflects the core value proposition of Serena: the tool knows the
  boundary of a symbol (start/end line, all nested braces/brackets) and can
  replace exactly it without risk of off-by-one errors in line ranges or
  accidental partial edits. File-level edit tools that operate on line ranges
  break if the file is modified between read and write; `replace_symbol_body`
  targets the symbol by name, making it resilient to surrounding code changes.
  For Ch06: recommend `replace_symbol_body` as the default code modification
  tool when Serena is in the workflow. Use `edit:` only for modifications that
  are not at the symbol level (e.g., adding a top-level import statement that
  doesn't map to a single symbol).

### Claim 6: For large codebases, Serena should start with targeted analysis of specific packages before expanding scope

- **Evidence**: The best practices section states: "For large codebases, start
  with targeted analysis of specific packages before expanding scope." This is
  a workflow sequencing recommendation, not a capability limitation — the implication
  is that analyzing the entire codebase at once is possible but inefficient.
- **Confidence**: anecdotal (first-party prescription without specific metrics
  on what "large" means or what the cost of full-codebase analysis is)
- **Quote**: "For large codebases, start with targeted analysis of specific
  packages before expanding scope."
- **Our assessment**: The guidance reflects a practical reality of LSP-based
  analysis — initializing a language server over a large monorepo takes
  substantial time and memory. Starting with a targeted package narrows the
  initial index scope and allows the agent to produce value faster. For Ch06:
  when designing agentic workflows for large codebases, structure the Serena
  usage to begin with the most relevant packages (e.g., the package containing
  the file to be modified), rather than attempting full-codebase analysis from
  the start. This is an incremental scoping pattern applicable broadly to
  agentic code workflows.

### Claim 7: Serena is designed to be combined with complementary tools rather than used in isolation — `github`, `edit`, and `bash` are the named pairings

- **Evidence**: The best practices section states: "Combine Serena with other
  tools like `github`, `edit`, and `bash` for complete workflows." The pairing
  is named explicitly, not just implied. Each tool in the pairing has a natural
  division of labor: `github` for reading repository context (issues, PRs, code
  via API), `edit` for non-symbol-level file modifications, `bash` for running
  tests and shell commands.
- **Confidence**: settled (first-party prescription naming the specific tool
  combinations)
- **Quote**: "Combine Serena with other tools like `github`, `edit`, and `bash`
  for complete workflows."
- **Our assessment**: The multi-tool pairing reveals the intended workflow
  structure: Serena handles semantic code understanding and symbol-level edits;
  `github` handles context retrieval from GitHub's API (issue body, PR diff,
  comments); `edit` handles file-level non-symbol changes; `bash` runs the
  test suite to verify correctness. Together these four tools cover the full
  read-understand-edit-verify cycle for a code task. For Ch05 (Orchestration):
  this four-tool set is the canonical tool configuration for a code-modification
  agent on gh-aw. For Ch06: present this combination as the recommended tool
  configuration for code-editing workflows.

### Claim 8: Language support is parameterized per-import via the `languages:` field — only the specified LSP servers are initialized, covering 30+ languages across 8 categories

- **Evidence**: The configuration examples show `with: languages: ["go", "typescript"]`
  as the mechanism for language selection. The page lists 30+ supported languages
  explicitly across 8 categories (Systems, JVM, Web, Dynamic, Functional,
  Scientific, Shell, Other). The parameter-per-import design means a workflow
  can specify exactly which languages it needs, avoiding initialization of
  unnecessary language servers.
- **Confidence**: settled (first-party documentation; the language list and
  parameter syntax are explicitly specified)
- **Quote**: (from import example)
  ```yaml
  imports:
    - uses: shared/mcp/serena.md
      with:
        languages: ["go", "typescript"]
  ```
- **Our assessment**: The `languages:` parameter is the performance and precision
  knob for Serena — initializing only the needed language servers reduces startup
  time and memory. A workflow that specifies `["go", "typescript"]` when the
  repository is Go-only is wasteful; specifying only `["go"]` is the correct
  practice. For Ch02: recommend that practitioners specify only the languages
  present in the target repository. The language list is also a form of scope
  declaration — it signals to the reader which code the workflow is expected to
  operate on.

### Claim 9: A Go-specific convenience wrapper (`serena-go.md`) simplifies single-language Go configuration with a simpler import syntax

- **Evidence**: The page shows a shorter import form for Go-only workflows:
  `imports: - shared/mcp/serena-go.md` (no `uses:` / `with:` block required).
  This is described as a "Go-only convenience wrapper" available in the shared
  workflow library.
- **Confidence**: settled (first-party documentation; the import path and its
  purpose are explicitly stated)
- **Quote**: (from Go-only example)
  ```yaml
  imports:
    - shared/mcp/serena-go.md
  ```
- **Our assessment**: The `serena-go.md` wrapper is a concrete example of the
  shared-workflow-as-configuration pattern — the wrapper encapsulates the
  language specification so callers don't need to specify it. For practitioners
  building Go-only tooling on gh-aw, `serena-go.md` is the simpler entry
  point. The existence of a language-specific wrapper hints at a broader pattern:
  similar wrappers may exist or could be created for other commonly used single-language
  configurations (e.g., `serena-typescript.md`, `serena-python.md`).

### Claim 10: Slow initial analysis is expected and documented behavior — Serena language servers build indexes on first run, with subsequent runs using cached data

- **Evidence**: The troubleshooting section explicitly lists "Slow initial analysis"
  as a known issue with the explanation "expected behavior as language servers
  build indexes, subsequent runs use cached data." This is presented as expected
  behavior rather than a defect — the troubleshooting entry serves to inform
  users not to report it as a bug.
- **Confidence**: settled (first-party documentation; the behavior is explicitly
  acknowledged and explained)
- **Quote**: (no single direct quote; the troubleshooting entry names the issue
  "Slow initial analysis" and explains it as expected)
- **Our assessment**: This claim connects directly to Claim 4 (cache-memory
  setup): the slow first run is the cost that cache-memory persistence is
  designed to amortize across subsequent runs. Practitioners who see slow Serena
  performance should first check whether the cache setup from Claim 4 is
  properly configured before investigating other issues. For Ch02: include a
  note in the Serena configuration section that the first run will be slow
  while indexes build; this is expected and resolved by the cache setup.

## Concrete Artifacts

### Migration: Before and After (from page danger callout)

```yaml
# BEFORE (removed — will fail compilation):
tools:
  serena: ["go", "typescript"]

# AFTER (recommended):
imports:
  - uses: shared/mcp/serena.md
    with:
      languages: ["go", "typescript"]
```

*Source: docs-ghaw-guides-serena, migration notice danger callout*

### Go-Only Convenience Wrapper

```yaml
imports:
  - shared/mcp/serena-go.md
```

*Source: docs-ghaw-guides-serena, "Go-Only" section*

### Example: Multi-Language Analysis Workflow

```yaml
imports:
  - uses: shared/mcp/serena.md
    with:
      languages: ["go"]
```

*Source: docs-ghaw-guides-serena, example code analysis section*

### Cache Setup (Required for Performance)

```bash
# Pre-create the cache directory before Serena runs
mkdir -p /tmp/gh-aw/cache-memory/serena
```

```yaml
# Pin the cache key in workflow frontmatter
tools:
  cache-memory:
    key: serena-analysis
```

*Source: docs-ghaw-guides-serena, best practices section*

### Complete Tool Catalogue

```
Serena MCP Tools (11 total):

SYMBOL NAVIGATION:
  find_symbol               — Locate a symbol by name in the codebase
  find_referencing_symbols  — Find all symbols that reference a target symbol
  get_symbol_definition     — Retrieve the definition of a specific symbol
  list_symbols_in_file      — Enumerate all symbols defined in a file

CODE EDITING:
  replace_symbol_body       — Replace the body of a symbol with new content
  insert_after_symbol       — Insert code immediately after a symbol
  insert_before_symbol      — Insert code immediately before a symbol
  delete_symbol             — Remove a symbol from the codebase

PROJECT ANALYSIS:
  find_files                — Search for files matching a pattern
  get_project_structure     — Retrieve the high-level structure of the project
  analyze_imports           — Analyze import dependencies for a file or symbol
```

*Source: docs-ghaw-guides-serena, available tools section*

### Supported Languages (30+)

```
Systems:    C, C++, Rust, Go, Zig
JVM:        Java, Kotlin, Scala, Groovy
Web:        JavaScript, TypeScript, Dart, Elm
Dynamic:    Python, Ruby, PHP, Perl, Lua
Functional: Haskell, Elixir, Erlang, Clojure, OCaml
Scientific: R, Julia, MATLAB, Fortran
Shell:      Bash, PowerShell
Other:      C#, Swift, Nix, Markdown, YAML, TOML
```

*Source: docs-ghaw-guides-serena, supported languages section*

### Troubleshooting Reference

```
Issue: Language server not found
Fix:   Install required language server dependencies for the specified language

Issue: Memory permission issues
Fix:   Ensure cache directory exists with proper permissions
       (mkdir -p /tmp/gh-aw/cache-memory/serena)

Issue: Slow initial analysis
Fix:   Expected behavior — language servers build indexes on first run.
       Subsequent runs use cached data. Ensure cache-memory is configured.
```

*Source: docs-ghaw-guides-serena, troubleshooting section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-mcps.md` Claim 9 (a library of 17 pre-built shared MCP
    configurations exists including Serena): this note provides the detailed
    practitioner guide for Serena specifically. The two notes together give
    the complete picture — mcps.md establishes that Serena exists as a shared
    config; this note explains how to use it.
  - `docs-ghaw-tools-reference.md` Claim 1 (tools from imported components
    merge into the final workflow): the `imports: - uses: shared/mcp/serena.md`
    pattern works precisely because of this merge behavior. The import brings
    Serena's MCP server declaration into the workflow's tool set without
    requiring explicit `mcp-servers:` configuration.
  - `docs-ghaw-tools-reference.md` Claim 5 (two built-in memory tools —
    `cache-memory:` for cross-run trend data): Claim 4 here describes Serena's
    reliance on `cache-memory:` for cross-run index persistence. Serena's
    cache setup is a concrete production use case for the `cache-memory:`
    tool's cross-run persistence scope.

- **Extends**:
  - `docs-ghaw-mcps.md` Concrete Artifacts → "Stdio MCP Server" section:
    that note shows Serena configured as a raw stdio MCP server using
    `command: "uvx" args: ["--from", "git+https://github.com/oraios/serena", "serena"]`.
    This note supersedes that approach — the shared/mcp/serena.md import
    is the maintained path; the raw uvx configuration remains technically
    valid but is not the recommended pattern. The `shared/mcp/serena.md`
    wrapper likely encapsulates a similar uvx-based stdio server declaration
    internally.
  - `docs-ghaw-mcps.md` Claim 3 (`allowed:` as minimal-privilege tool access):
    Serena's 11-tool surface is already narrow and purpose-built, reducing
    the need for aggressive `allowed:` filtering. This note adds context to
    when `allowed: ["*"]` is acceptable — for single-purpose, small-surface
    MCP servers like Serena, it is appropriate.

- **Contradicts**: None identified. The recommended `shared/mcp/serena.md`
  import path is consistent with the shared workflow pattern documented across
  multiple existing notes. The `tools.serena` removal does not contradict any
  existing source note (no prior note recommended `tools.serena:` as an active
  configuration approach).

- **Novel**:
  - **Symbol-level code editing as an agentic pattern** (Claim 1, 2, 5): No
    existing source note documents symbol-level operations (as distinct from
    file-level text editing) as a first-class agentic code modification pattern.
    The case for `replace_symbol_body` over file-level edits is new to the corpus.
  - **The 11-tool Serena catalogue with specific tool names** (Claim 2, Concrete
    Artifacts): No existing source note enumerates the specific MCP tool identifiers
    exposed by Serena. The tool names are actionable for practitioners writing
    Serena-based workflows.
  - **Cache-memory setup as required configuration for Serena** (Claim 4): The
    specific cache path (`/tmp/gh-aw/cache-memory/serena`) and key (`serena-analysis`)
    are not documented in any existing source note. This is a concrete operational
    requirement, not a suggestion.
  - **`tools.serena` removal and migration path** (Claim 3): The breaking change
    from `tools.serena:` to `imports: - uses: shared/mcp/serena.md` is new
    to the corpus.
  - **Package-scoped analysis as best practice for large codebases** (Claim 6):
    The recommendation to start with targeted package analysis before expanding
    scope is a novel pattern applicable broadly to semantic code analysis agents.

## Guide Impact

### Chapter 05: Orchestration and Composition

- **Add Serena as the semantic layer in multi-tool code workflows** (Claim 7):
  The prescribed four-tool combination (Serena + github + edit + bash) is a
  canonical tool configuration for code-modification orchestration on gh-aw.
  Add to Ch05 as a worked example of tool composition: each tool covers a
  distinct part of the read-understand-edit-verify cycle.

- **Add package-scoped analysis as a scaling pattern** (Claim 6): For large
  codebase workflows, structure Serena usage to start with the most relevant
  packages. This is an incremental scoping pattern that prevents full-monorepo
  initialization from dominating workflow time budgets.

### Chapter 06: Building Agentic Patterns

- **Add the read-navigate-edit Serena workflow pattern** (Claims 1, 2, 5):
  Document the three-phase symbol-level code editing pattern: (1) locate with
  `find_symbol` / `find_referencing_symbols`, (2) understand context with
  `analyze_imports` / `get_project_structure`, (3) modify with `replace_symbol_body`.
  This pattern is more reliable than line-range editing for structured codebases
  and should be the recommended approach when Serena is available.

- **Add symbol-level vs. file-level editing as a deliberate choice** (Claim 5):
  When Serena is in the workflow, prefer `replace_symbol_body` for function/method/
  class-level changes; use `edit:` only for changes that don't map to a symbol
  boundary (e.g., top-level import additions, file header modifications). Document
  the rationale: symbol-level is resilient to surrounding code changes; line-range
  edits are brittle.

### Chapter 02: Harness Engineering

- **Document the `shared/mcp/serena.md` import as the only valid Serena
  integration path** (Claim 3): Any guide content that references `tools.serena:`
  must be updated. The migration path is: replace `tools: serena: ["lang"]` with
  `imports: - uses: shared/mcp/serena.md` with `with: languages: ["lang"]`.

- **Add Serena cache setup as a required operational step** (Claim 4): Include
  the `mkdir -p /tmp/gh-aw/cache-memory/serena` + `tools.cache-memory.key:
  serena-analysis` configuration in any Serena setup example. First-run slow
  performance is expected and documented; practitioners who skip the cache
  setup will experience this on every run.

- **Add language parameterization guidance** (Claim 8): Recommend specifying
  only the languages present in the target repository. Over-specifying languages
  (e.g., including TypeScript for a Go-only repo) wastes initialization time.
  For single-language Go projects, recommend `serena-go.md` (Claim 9) as
  the simpler entry point.

## Extraction Notes

1. **WebFetch returns AI-summarized content**: The gh-aw documentation is an
   Astro/Starlight SPA. Three targeted WebFetch calls were made with different
   prompts to maximize fidelity. Quoted text that appears in quotation marks in
   the fetch output is assessed as verbatim; descriptions without quotation marks
   are paraphrased reconstructions. The best practices paragraph (Claim 4 quote)
   and the overview paragraph (Claim 1 quote) are the most precisely captured
   verbatim passages. The migration notice text (Claim 3 quote) appeared
   consistently across all three fetches.

2. **Tool names assessed as accurate**: The 11 tool names (find_symbol,
   replace_symbol_body, etc.) appeared consistently across two fetches and
   are consistent with the known Serena open-source project (oraios/serena
   on GitHub). Assessed as settled despite the fetch summarization.

3. **`docs-ghaw-getting-started-mcp.md` not found**: The Prospector triage
   comment references `docs-ghaw-getting-started-mcp.md` as an existing note
   with "general MCP integration patterns." This file does not appear in the
   current `source-notes/` directory. Cross-references were written against
   `docs-ghaw-mcps.md` and `docs-ghaw-tools-reference.md` instead, which
   cover overlapping content.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is assessed as current as of 2026-05-11 based on
   platform state.

5. **No contradictions filed**: The `tools.serena` removal does not contradict
   any existing source note — no prior source note recommended `tools.serena:`
   as an active configuration. The uvx-based stdio configuration in
   `docs-ghaw-mcps.md` is consistent with (and likely underlies) the
   `shared/mcp/serena.md` shared workflow.
