---
source_url: https://github.github.com/gh-aw/reference/qmd
source_type: docs
title: "GitHub Agentic Workflows: QMD Documentation Search Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#454"
---

# GitHub Agentic Workflows: QMD Documentation Search Reference

> The reference specification for the `qmd:` tool — an experimental vector
> similarity search capability over documentation files that runs
> `tobi/qmd` as an MCP server, with a permission-separation design that
> isolates `contents: read` access to a dedicated indexing job and delivers
> the index to the agent job via GitHub Actions cache.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/qmd` page — in
  the "Reference" section. This is the dedicated configuration reference for
  `qmd:`, as distinct from the brief overview entry in
  `docs-ghaw-tools-reference.md` Claim 6 which names it as experimental but
  does not elaborate on configuration or design.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind the `gh aw` platform. Configuration options, permission
  semantics, and cache integration behavior are authoritative for this platform.
  The "experimental" label signals this API may change before stabilizing.
- **Scope**: Configuration reference for the `qmd:` tool — the five top-level
  configuration keys (`checkouts`, `searches`, `cache-key`, `gpu`, `runs-on`),
  the indexing-vs-agent job permission split, read-only mode semantics, GPU
  acceleration, and OTLP telemetry integration. Does NOT cover: how the agent
  queries the QMD index at runtime (the MCP tool names or query API), the
  `tobi/qmd` internals (embedding model beyond the `node-llama-cpp` reference),
  cost or latency characteristics, or how QMD interacts with the broader
  `network.allowed` or `allowed:` controls. This page is the configuration
  reference; the tool usage API is not documented here.

## Extracted Claims

### Claim 1: QMD provides vector similarity search over documentation files by running `tobi/qmd` as an MCP server, enabling agents to discover relevant documentation through natural language queries

- **Evidence**: The page states: "QMD Documentation Search provides vector
  similarity search over documentation files. It runs
  [tobi/qmd](https://github.com/tobi/qmd) as an MCP server so agents can find
  relevant documentation by natural language query." This is the opening
  definition — the capability is framed as semantic search (vector similarity)
  rather than exact text matching, accessible to agents via the MCP protocol.
- **Confidence**: emerging (first-party; but the tool is experimental, and
  the agent-side query experience — MCP tool names, response format — is not
  specified on this page)
- **Quote**: "QMD Documentation Search provides vector similarity search over
  documentation files. It runs [tobi/qmd](https://github.com/tobi/qmd) as an
  MCP server so agents can find relevant documentation by natural language
  query."
- **Our assessment**: QMD is the platform's RAG (retrieval-augmented
  generation) primitive for documentation. It addresses the context engineering
  problem of large documentation sets: rather than statically including docs
  in the system prompt, an agent can query at runtime for the most relevant
  fragments. Running as an MCP server means agents access it through the same
  `mcp-servers:` protocol as external tool integrations — but unlike external
  MCP servers (`docs-ghaw-mcps.md`), `qmd:` is a built-in tool declared in the
  `tools:` section. This confirms the brief description in
  `docs-ghaw-tools-reference.md` Claim 6 and adds the MCP server
  implementation detail and the `tobi/qmd` open-source reference.

### Claim 2: The QMD indexing job runs with `contents: read` permissions in a dedicated job, sharing the index with the agent job via GitHub Actions cache — the agent job does not require `contents: read` for QMD to function

- **Evidence**: The page describes the architecture: "The search index is built
  in a dedicated indexing job with `contents: read` permissions and shared with
  the agent job via GitHub Actions cache, eliminating the need for `contents:
  read` in the agent job itself."
- **Confidence**: settled (first-party; the permission-separation architecture
  is explicitly described)
- **Quote**: "The search index is built in a dedicated indexing job with
  `contents: read` permissions and shared with the agent job via GitHub Actions
  cache, eliminating the need for `contents: read` in the agent job itself."
- **Our assessment**: This is a notable security and capability design. The
  agent job typically runs with minimal permissions (consistent with
  `docs-ghaw-how-they-work.md` Claim 4's "no write access by default"
  principle). By offloading the index-build step to a separate job that holds
  `contents: read`, the platform avoids granting the agent job repository read
  access just to enable documentation search. The cache is the trust boundary:
  the indexing job reads files and produces an opaque vector index artifact;
  the agent job consumes only the pre-built index. For Ch03 (Safety and
  Verification): this is the first documented example of using GitHub Actions
  job isolation to narrow the permission scope of the agent job specifically —
  not just the workflow overall. For Ch02: teams that prefer to run agent jobs
  with zero repository permissions can still use QMD documentation search via
  this split-job pattern.

### Claim 3: The minimal QMD configuration requires only a `checkouts` block with file patterns — no other options are required to enable documentation indexing

- **Evidence**: The minimal configuration example from the page:
  ```yaml
  ---
  tools:
    qmd:
      checkouts:
        - pattern: "docs/**/*.md"
  ---
  ```
  Framed as the "minimal setup" with only `pattern` specified. All other
  options (`searches`, `cache-key`, `gpu`, `runs-on`) are optional.
- **Confidence**: settled (first-party; the example is labeled as minimal
  setup and no other required fields are indicated)
- **Quote**: (YAML reproduced verbatim above; no accompanying prose quote
  captures the minimal-setup framing as a single sentence)
- **Our assessment**: The single-field minimal configuration means `qmd:` has
  a low onboarding cost — a one-liner pattern like `"docs/**/*.md"` is
  sufficient to begin indexing. The glob pattern syntax (`**/*.md`) follows
  standard GitHub Actions glob conventions, making it familiar to practitioners.
  Multiple patterns can be listed to index across different directory structures.
  For Ch02: the minimal example is the starting point for any workflow that
  needs documentation search; add `cache-key` once the indexing cost needs
  to be amortized across runs.

### Claim 4: `checkouts` specifies named documentation collections built from checked-out repositories — each entry can index files from the current repo or a different repository using file glob patterns

- **Evidence**: The documentation describes `checkouts` as "A list of named
  documentation collections built from checked-out repositories. Each entry
  specifies which files to index from the current repository or a different
  repository." The example shows multiple patterns can be listed together:
  ```yaml
  checkouts:
    - pattern: "docs/**/*.md"
    - pattern: "README.md"
  ```
- **Confidence**: settled (first-party; description is explicit)
- **Quote**: "A list of named documentation collections built from checked-out
  repositories. Each entry specifies which files to index from the current
  repository or a different repository."
- **Our assessment**: The "different repository" capability implies QMD can
  index documentation from multiple repos — not just the workflow's own repo.
  This enables cross-repo documentation search within a single workflow, which
  is valuable for large organizations with documentation spread across many
  repos. The "named documentation collections" phrasing suggests individual
  `checkouts` entries can be given names (not shown in the example), possibly
  for filtering at query time. For Ch02: when indexing documentation from
  multiple repositories, the `checkouts` list is the aggregation mechanism.

### Claim 5: `searches` adds GitHub code search query results to the QMD index — enabling semantic search over code-search-discovered content, not just locally checked-out files

- **Evidence**: The documentation describes `searches` as "A list of GitHub
  code search queries whose results are downloaded and added to the qmd index."
  The example: `query: "repo:github/gh-aw language:markdown"`.
- **Confidence**: emerging (first-party; the mechanism is described but the
  fidelity of code-search-to-vector-index pipeline is not detailed — how
  results are chunked, deduped, or filtered before indexing is unspecified)
- **Quote**: "A list of GitHub code search queries whose results are downloaded
  and added to the qmd index."
- **Our assessment**: The `searches` option extends QMD's indexing beyond
  the current repository's checked-out files to include content discovered
  via GitHub's code search API. This enables building documentation indexes
  from public repositories without needing checkout access — the search
  query pulls the content, which is then added to the vector index. Combined
  with `checkouts`, this gives two complementary indexing paths: local files
  (checked-out content) and remote content (code search results). For Ch04
  (Context Engineering): this is a notable pattern for indexing documentation
  from open-source dependencies or third-party repositories that the agent
  might need to reference.

### Claim 6: `cache-key` persists the QMD vector index across workflow runs via GitHub Actions cache — when set without any indexing sources, QMD operates in read-only mode without running indexing steps

- **Evidence**: The documentation describes `cache-key` as "A GitHub Actions
  cache key used to persist the qmd index across workflow runs. When set
  without any indexing sources (`checkouts`/`searches`), qmd operates in
  read-only mode." The read-only mode example:
  ```yaml
  tools:
    qmd:
      cache-key: "qmd-docs-my-project"
  ```
  "In read-only mode, the index is restored from cache and no indexing steps
  are run. This is useful when the index is built separately and shared across
  workflows."
- **Confidence**: settled (first-party; the read-only mode behavior is
  explicitly described)
- **Quote**: "In read-only mode, the index is restored from cache and no
  indexing steps are run. This is useful when the index is built separately
  and shared across workflows."
- **Our assessment**: Read-only mode enables a "build once, use many" pattern
  for documentation indexes. An organization can build the QMD index in a
  scheduled or manually triggered workflow (with full `contents: read` and
  indexing configuration), then share that index across all agent workflows
  that need it via the cache key — without each workflow re-running the
  indexing job. This is an efficiency and cost pattern: indexing large
  documentation sets on every workflow run would be expensive and slow.
  Read-only mode trades freshness for speed. For Ch02: document the
  `cache-key`-only pattern as the recommended production deployment mode
  once an initial index is built. The cache key should encode the version
  or date of the documentation to control freshness.

### Claim 7: GPU acceleration for the `node-llama-cpp` embedding model can be enabled via `gpu: true`, but defaults to `false` and should only be set on runners with a GPU

- **Evidence**: The documentation describes `gpu` as: "Enable GPU acceleration
  for the embedding model (`node-llama-cpp`). Defaults to `false`... Set to
  `true` only when the indexing runner has a GPU."
- **Confidence**: settled (first-party; the field name, default, and
  constraint are all stated)
- **Quote**: "Enable GPU acceleration for the embedding model
  (`node-llama-cpp`). Defaults to `false`... Set to `true` only when the
  indexing runner has a GPU."
- **Our assessment**: The explicit `node-llama-cpp` reference reveals the
  embedding model implementation — a Node.js binding for llama.cpp, which
  supports GPU acceleration via CUDA/Metal/Vulkan backends. This means QMD
  embeds documents locally on the indexing runner rather than calling an
  external embedding API. The local embedding model approach has privacy
  implications: document content is not sent to an external API for
  vectorization. For practitioners with GPU-equipped runners (uncommon in
  standard GitHub Actions), `gpu: true` would significantly reduce indexing
  time for large documentation sets. For most practitioners, the default
  `false` is appropriate. For Ch02: document that QMD uses local embedding
  (no external API call) and that GPU is an optional performance enhancement
  for large indexing jobs.

### Claim 8: `runs-on` overrides the runner image for the QMD indexing job — defaulting to the same runner as the agent job but allowing a different image for indexing

- **Evidence**: The documentation describes `runs-on` as: "Override the runner
  image for the qmd indexing job. Defaults to the same runner as the agent job."
- **Confidence**: settled (first-party; behavior is explicitly stated)
- **Quote**: "Override the runner image for the qmd indexing job. Defaults to
  the same runner as the agent job."
- **Our assessment**: The `runs-on` override is relevant when the indexing
  workload has different requirements than the agent job — for example, using
  a GPU-equipped runner for indexing while the agent job runs on a standard
  runner. Combined with `gpu: true`, this allows the expensive GPU-accelerated
  indexing to run on a specialized runner without forcing the entire workflow
  onto that runner type. For Ch02: when optimizing QMD performance for large
  documentation sets, combine `gpu: true` with `runs-on` pointing to a
  GPU runner to isolate the expensive indexing step.

### Claim 9: QMD includes OTLP telemetry support for observability — tracking `qmd.index.size` and `qmd.search.hits` metrics through distributed tracing via shared import files

- **Evidence**: The page describes: "The feature includes OTLP telemetry
  support for tracking index size and search hits. Shared import files can
  record metrics like `qmd.index.size` and `qmd.search.hits` to the
  distributed trace."
- **Confidence**: emerging (first-party; the mechanism is described at a high
  level — the specific OTLP configuration, attribute names, and shared import
  pattern are mentioned but not fully specified on this reference page)
- **Quote**: (no single direct quote captures the full telemetry mechanism;
  see paraphrase in Our assessment)
- **Our assessment**: The OTLP telemetry integration connects QMD to the
  broader observability story in `blog-ghaw-agent-observability.md`. Two
  specific metrics are named: index size (how many documents/chunks are
  indexed) and search hits (how often the agent queries the index, and
  presumably, how many results are returned). These metrics enable
  practitioners to understand whether the documentation index is being used
  effectively — a workflow with zero `qmd.search.hits` is paying the indexing
  cost without benefit. The "shared import files" mechanism for telemetry
  configuration aligns with the import-merge semantics documented in
  `docs-ghaw-tools-reference.md` Claim 1. For Ch02: include QMD telemetry as
  a recommended practice when deploying QMD in production — use
  `qmd.index.size` to monitor index health and `qmd.search.hits` to validate
  that the agent is actually querying the documentation.

### Claim 10: QMD is marked as experimental in the platform documentation, indicating its API may evolve before stabilizing

- **Evidence**: Both the `reference/qmd` page and `docs-ghaw-tools-reference.md`
  Claim 6 mark the tool as experimental. The tools reference states it "Builds
  vector search indexes over documentation with pattern-based checkout support"
  and flags the experimental status.
- **Confidence**: settled (first-party; explicit experimental label)
- **Quote**: (from `docs-ghaw-tools-reference.md` Claim 6, which confirms the
  experimental label; the `reference/qmd` page's closing note: "This is marked
  as experimental, indicating the API may evolve in future releases.")
- **Our assessment**: The experimental label means the configuration schema
  (`checkouts`, `searches`, `cache-key`, `gpu`, `runs-on`) may change in
  future platform releases. Practitioners building workflows that depend on
  QMD should monitor the reference page for breaking changes. The experimental
  status is consistent with the Prospector's novelty assessment — this is a
  new, not-yet-stabilized capability. For the guide: recommend QMD for
  experimental or internal workflows, not for production workflows with
  strict stability requirements, until the tool's status changes.

## Concrete Artifacts

### Minimal QMD Configuration

```yaml
# Minimal setup — index all markdown files in docs/
---
tools:
  qmd:
    checkouts:
      - pattern: "docs/**/*.md"
---
```

*Source: docs-ghaw-qmd-reference, "Basic Configuration" section — verbatim*

### Multiple Pattern Configuration

```yaml
# Index docs/ directory and top-level README
tools:
  qmd:
    checkouts:
      - pattern: "docs/**/*.md"
      - pattern: "README.md"
```

*Source: docs-ghaw-qmd-reference, "checkouts configuration" section — verbatim*

### Multi-Source Configuration with Cache Key

```yaml
# Index docs/ + README, cache the index across runs
tools:
  qmd:
    checkouts:
      - pattern: "docs/**/*.md"
      - pattern: "*.md"
    cache-key: "qmd-docs-${{ github.repository }}-${{ github.run_id }}"
```

*Source: docs-ghaw-qmd-reference, "Multiple Sources" example — verbatim*

### Read-Only Mode (Index from Cache Only)

```yaml
# Restore pre-built index from cache, no indexing steps run
tools:
  qmd:
    cache-key: "qmd-docs-my-project"
```

*Source: docs-ghaw-qmd-reference, "Read-Only Mode" example — verbatim*

### GitHub Code Search Integration

```yaml
# Use GitHub code search results as an indexing source
tools:
  qmd:
    searches:
      - query: "repo:github/gh-aw language:markdown"
```

*Source: docs-ghaw-qmd-reference, "searches configuration" example — verbatim*

### OTLP Telemetry Metrics

```
qmd.index.size    — number of documents/chunks in the vector index
qmd.search.hits   — count of semantic search queries against the index
```

*Source: docs-ghaw-qmd-reference, "Telemetry" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-tools-reference.md` Claim 6: that note identifies `qmd:` as
    an experimental tool that "Builds vector search indexes over documentation
    with pattern-based checkout support." The `reference/qmd` page is the
    full specification that the tools reference summarizes in one line. Both
    sources agree: experimental, vector search, pattern-based checkout. This
    note extends Claim 6 with the full configuration schema, the
    permission-separation architecture (Claim 2), read-only mode (Claim 6
    here), and OTLP telemetry (Claim 9).
  - `docs-ghaw-mcps.md` Claim 1 (custom MCP servers should be read-only):
    QMD runs as an MCP server (Claim 1 here) and is implicitly read-only —
    it provides search/retrieval, not write operations. This is consistent
    with the platform's read-only MCP policy.
  - `blog-ghaw-agent-observability.md`: QMD's OTLP telemetry (Claim 9)
    connects to the broader observability patterns documented in that note.
    `qmd.index.size` and `qmd.search.hits` are QMD-specific signals within
    the distributed tracing infrastructure.

- **Extends**:
  - `docs-ghaw-tools-reference.md` Claim 6: this note is the full reference
    for the one-line mention in the tools catalogue. Together, the two notes
    give practitioners the overview (where QMD fits in the tool catalogue)
    and the specification (how to configure it). When the guide covers QMD,
    cite this note for configuration details; cite the tools reference for
    the tool-catalogue context.
  - `docs-ghaw-mcps.md`: QMD uses the MCP protocol internally but is
    configured via `tools:` (not `mcp-servers:`). This note adds the
    built-in documentation search use case to the MCP ecosystem documented
    in `docs-ghaw-mcps.md`. The `reads: read` + job isolation architecture
    (Claim 2) is the QMD-specific implementation of the minimal-permissions
    principle that underpins the MCP design.
  - `docs-ghaw-how-they-work.md` Claim 4 (minimal permissions, no write
    access by default): the QMD permission-split architecture (Claim 2 here)
    is a concrete extension of that principle — not just limiting the overall
    workflow permissions, but using job-level isolation to scope `contents:
    read` only to the indexing step.

- **Contradicts**: None identified. The experimental status is consistent
  with `docs-ghaw-tools-reference.md` Claim 6. The MCP-server implementation
  is consistent with `docs-ghaw-mcps.md`. No existing source note makes claims
  about QMD that conflict with the reference page's description. No
  contradiction issue required.

- **Novel** (what this note adds that no prior source covers):
  - **QMD permission-split architecture** (Claim 2): No existing source note
    documents the indexing-job/agent-job separation pattern or the
    `contents: read` isolation via GitHub Actions cache. This is a new
    security architecture pattern — job-level permission scoping for a built-in
    tool — that has implications beyond QMD (any tool that needs elevated
    permissions during setup but not during agent operation could use this
    pattern).
  - **Read-only mode via `cache-key` without indexing sources** (Claim 6):
    Not documented in any existing source note. The "build once, reuse many"
    pattern enabled by `cache-key` alone is a practical deployment optimization.
  - **`searches` option for GitHub code search integration** (Claim 5):
    Not documented anywhere in the corpus. The ability to build a QMD index
    from GitHub code search results (not just locally checked-out files) is a
    novel indexing capability.
  - **`node-llama-cpp` as the local embedding model** (Claim 7): No existing
    source note identifies the specific embedding technology used by QMD. The
    local (non-API) embedding approach has privacy implications not documented
    elsewhere.
  - **OTLP metrics `qmd.index.size` and `qmd.search.hits`** (Claim 9): The
    specific metric names for monitoring QMD usage are new to the corpus.
  - **Full configuration schema** (`checkouts`, `searches`, `cache-key`,
    `gpu`, `runs-on`): No existing note documents these five configuration
    keys and their semantics. The tools reference mentions `qmd:` exists;
    only this note specifies what can be configured.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add QMD as the platform-native documentation RAG tool** (Claims 1, 3):
  The guide currently lacks documentation of `qmd:` as a built-in tool (the
  tools reference note covers it briefly). Add a section documenting the
  minimal configuration (`checkouts` with a pattern), the permission-split
  architecture, and when to prefer QMD over static context injection. Cite
  the `reference/qmd` page for the full configuration reference.

- **Document the QMD permission-split architecture as a harness design pattern**
  (Claim 2): The indexing-job isolation pattern — using a dedicated job for
  operations that need `contents: read`, sharing output via GitHub Actions
  cache — is generalizable beyond QMD. Document it as a Ch02 principle: if
  an agent workflow needs elevated permissions for setup but not for operation,
  use job-level isolation to scope the elevated permissions to the setup phase.

- **Add `cache-key` read-only mode as the recommended production deployment
  pattern** (Claim 6): For production workflows, building the QMD index in a
  scheduled workflow and consuming it via read-only mode in agent workflows
  is the efficient pattern. Document the two-workflow approach (index builder
  + agent consumer) as a best practice once an organization is past the
  exploratory phase.

### Chapter 04: Context Engineering / Tool Choice

- **Add QMD as a first-class RAG alternative to static context injection**
  (Claim 1): When covering context engineering strategies, present QMD as
  the platform-native RAG option: instead of including documentation in the
  system prompt, let the agent query a pre-built vector index at runtime.
  Document the trade-off: static injection is simpler and more predictable;
  QMD-based retrieval is more scalable for large doc sets but adds indexing
  overhead and is currently experimental.

- **Document `searches` + `checkouts` as complementary indexing sources for
  multi-repo documentation** (Claim 5): Workflows that need to reference
  documentation from external repositories (dependencies, third-party APIs)
  can combine local `checkouts` (own repo docs) with `searches` (public
  repository content via GitHub code search) to build a comprehensive
  documentation index without requiring checkout access to external repos.

- **Cross-reference QMD telemetry with agent observability** (Claim 9):
  When covering observability for documentation-search workflows, cite
  `qmd.index.size` and `qmd.search.hits` as the specific OTLP signals
  to monitor. A workflow with a large index but zero search hits may indicate
  the agent is not invoking QMD effectively — a context engineering problem.

## Extraction Notes

1. **Experimental tool**: `qmd:` is explicitly labeled experimental. The
   configuration schema may change before stabilization. All claims are
   based on the current reference page state (2026-05-12) and should be
   re-verified when the experimental label is removed.

2. **Agent-side query API not documented**: The reference page specifies how
   to configure and build the QMD index, but does not document how the agent
   queries it — the MCP tool names (e.g., `qmd_search` or similar), the
   query parameter format, or the response structure. The agent-facing API
   may be discoverable via `gh aw mcp list-tools` once a workflow with `qmd:`
   is configured. This is a gap in this source note; it may be covered in a
   separate `tobi/qmd` README or an undiscovered sub-page.

3. **Source fetched via WebFetch with AI mediation**: The gh-aw documentation
   is an Astro/Starlight SPA. WebFetch returns rendered text. Two fetches were
   performed to maximize fidelity. Quoted text in quotation marks in the fetch
   output is assessed as verbatim from the source; YAML examples are reproduced
   as rendered. Minor formatting differences from the live page are possible.

4. **No publication date**: The documentation page does not carry an explicit
   date. Content is assessed as current as of 2026-05-12.

5. **No contradictions filed**: Reviewed all existing source notes. No claims
   in this source materially oppose existing notes. The experimental status is
   consistent with `docs-ghaw-tools-reference.md` Claim 6. The MCP-server
   implementation is consistent with `docs-ghaw-mcps.md`.

6. **`searches` key format**: The example shows `query:` as a field within
   a `searches` list entry (like `checkouts` uses `pattern:`). Whether
   additional fields (e.g., pagination limits, result count) are supported
   within each `searches` entry is not specified on this page.
