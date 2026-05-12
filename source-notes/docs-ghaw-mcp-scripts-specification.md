---
source_url: https://github.github.com/gh-aw/reference/mcp-scripts-specification
source_type: docs
title: "GitHub Agentic Workflows: MCP Scripts Specification"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#430"
---

# GitHub Agentic Workflows: MCP Scripts Specification

> The detailed specification for inline MCP tool definitions in gh-aw workflow
> frontmatter — documents the four-language runtime model (JavaScript/Node.js
> in-process; Shell/Python/Go containerized), the `mcp-scripts:` configuration
> schema (description, inputs, env, timeout, dependencies), the security model
> (explicit secret declaration, input validation, output sanitization,
> SIGTERM/SIGKILL termination), large-output file storage, recoverable vs.
> permanent error semantics, and MCP Gateway integration — the specification
> complement to the external MCP server configuration in `docs-ghaw-mcps.md`.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/mcp-scripts-specification`
  page — in the "Reference" section, not the conceptual `introduction/` pages or
  practitioner `guides/`. A technical specification page for the `mcp-scripts:`
  frontmatter block. Distinct from `docs-ghaw-mcps.md`, which documents *external*
  MCP server configuration; this page is the specification for *inline* MCP Scripts
  defined directly in workflow frontmatter.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind the Peli de Halleux agent factory blog series and the `gh aw`
  CLI. Configuration field names, language runtime behaviors, timeout semantics,
  and security model properties are authoritative for the `gh aw` platform. Claims
  about the platform's MCP scripting mechanism are settled for gh-aw; they do not
  automatically generalize to other agentic frameworks.
- **Scope**: The complete specification for MCP Scripts — the `mcp-scripts:`
  frontmatter block, all four language runtimes (JavaScript, Shell, Python, Go),
  input schema definition, secret handling, timeout behavior, large-output handling,
  error handling semantics, dependency management, and MCP Gateway integration.
  Does NOT cover: external MCP server configuration (see `docs-ghaw-mcps.md`),
  the Safe Outputs mechanism for write operations (see `docs-ghaw-how-they-work.md`),
  the general compilation model (see `docs-ghaw-compilation-process.md`), or
  built-in tool categories beyond MCP Scripts (see `docs-ghaw-tools-reference.md`).

## Extracted Claims

### Claim 1: MCP Scripts enable inline custom tool definition in workflow frontmatter without deploying a separate MCP server, providing "ephemeral, containerized tool execution with controlled secret access"

- **Evidence**: The page describes MCP Scripts as enabling developers to "define
  custom MCP tools inline in workflow frontmatter without requiring external MCP
  server implementations." The characterizing phrase for the execution model:
  "ephemeral, containerized tool execution with controlled secret access."
- **Confidence**: settled (first-party specification documentation)
- **Quote**: "ephemeral, containerized tool execution with controlled secret access"
- **Our assessment**: MCP Scripts lower the barrier to custom tool integration
  significantly. A practitioner who wants a workflow-specific tool does not need
  to deploy and maintain a separate MCP server process — they write the tool
  definition directly in the workflow frontmatter. The "ephemeral" qualifier is
  important: MCP Script tools are instantiated for the workflow run and do not
  persist as running services between invocations. "Controlled secret access"
  points to the explicit `env:` declaration model (Claim 5). This is the detailed
  specification of what `docs-ghaw-how-they-work.md` Claim 6 introduces at a
  high level ("custom MCP tools defined inline in workflow frontmatter").
  For Ch02 (Harness Engineering): MCP Scripts and external MCP servers form a
  two-tier tool integration model. Inline scripts for workflow-specific, ephemeral
  tools; external servers for shared, complex, or third-party integrations.

### Claim 2: Each MCP Script tool requires exactly one language implementation field — `script:` (JavaScript), `run:` (Shell), `py:` (Python), or `go:` (Go) — and the four runtimes have distinct isolation properties

- **Evidence**: The configuration structure requires exactly one of four
  implementation fields per tool. Runtime mappings: `script:` → JavaScript/Node.js
  CommonJS (in-process); `run:` → Bash in Docker containers; `py:` → Python 3.10+
  in Docker containers; `go:` → Go via `go run` in Docker containers. The
  mutual exclusivity ("exactly one") is a stated schema constraint.
- **Confidence**: settled (first-party specification; the four field names and their
  runtime mappings are explicitly documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The four-runtime model reflects a key isolation split:
  JavaScript is in-process (fast startup, no container overhead, but shares the
  workflow runner process); Shell, Python, and Go are containerized (isolated,
  with container startup latency but full process separation). The mutual
  exclusivity ensures unambiguous execution semantics per tool. For Ch02:
  recommend JavaScript for simple, fast invocations where GitHub API access
  is needed (pre-injected globals, Claim 3); recommend Shell/Python/Go for
  tools that need system utilities, language-specific libraries, or full isolation.
  The runtime choice has a direct effect on timeout enforcement (Claim 4).

### Claim 3: JavaScript MCP Scripts execute in-process in Node.js CommonJS with automatic access to GitHub Actions globals (`github`, `context`, `core`, `io`, `exec`, `glob`, `artifact`) without requiring imports

- **Evidence**: The page documents that JavaScript scripts "execute in Node.js with
  CommonJS format," are wrapped as "async function execute(inputs)," and have
  automatic access to GitHub Actions globals without requiring explicit imports.
  The documented globals: `github`, `context`, `core`, `io`, `exec`, `glob`,
  `artifact`.
- **Confidence**: settled (first-party specification)
- **Quote**: (no direct quote available for the full list; the globals list is from
  the summarized source content)
- **Our assessment**: The automatic injection of GitHub Actions globals is a
  significant productivity feature — practitioners can call GitHub API operations
  (`github.getOctokit`), access workflow context (`context.repo.owner`), and use
  Actions IO utilities (`core`, `io`) without setup code. The "wraps as async
  function execute(inputs)" structure means inputs are available as local variables
  from the function parameter destructuring. In-process execution makes JavaScript
  tools the fastest to invoke but also the least isolated — they share the runtime
  with the workflow engine. For Ch02: JavaScript is the right choice for tools that
  need direct GitHub API access; use the pre-injected `github` object rather than
  constructing Octokit clients manually (as shown in the Concrete Artifacts example).

### Claim 4: Container-based MCP Scripts (Shell, Python, Go) enforce timeouts via SIGTERM then SIGKILL — JavaScript is in-process with no timeout enforcement

- **Evidence**: The page states: "Timeout enforcement: Process MUST be terminated
  with SIGTERM, then SIGKILL after grace period." This applies to containerized
  tools. For JavaScript tools: "JavaScript tools execute in-process without timeout
  enforcement." The `timeout:` field allows per-tool override of the default.
- **Confidence**: settled (first-party specification; the JavaScript exception is
  explicitly noted; the SIGTERM/SIGKILL sequence is normative)
- **Quote**: "Timeout enforcement: Process MUST be terminated with SIGTERM, then
  SIGKILL after grace period."
- **Our assessment**: The timeout enforcement asymmetry is a significant operational
  difference between runtimes. JavaScript tools that hang will block the agent job
  indefinitely — there is no platform-level timeout mechanism. Shell, Python, and Go
  tools get SIGTERM (graceful shutdown attempt) followed by SIGKILL (forced
  termination), giving container-based tools a clear termination guarantee.
  For Ch02 and Ch03: if a JavaScript MCP Script performs a long-running or
  potentially blocking operation (e.g., a large GitHub API call with no client-side
  timeout), it could block the workflow run without recourse. Practitioners with
  long-running logic should prefer container-based runtimes with an explicit
  `timeout:` configuration. The per-tool `timeout:` field provides control —
  set conservative timeouts for network-dependent tools.

### Claim 5: Secrets require explicit `env:` declaration using `${{ secrets.NAME }}` syntax — no implicit access to the workflow's secret environment

- **Evidence**: The security model states that secrets "require explicit `env:`
  declaration using `${{ secrets.NAME }}` syntax." Tools execute in isolated
  processes or containers. Only secrets appearing in the tool's `env:` block
  are accessible to the tool's execution environment.
- **Confidence**: settled (first-party specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The explicit `env:` declaration model is consistent with the
  "zero capability by default" principle in `docs-ghaw-how-they-work.md` Claim 4
  and the read-only MCP policy in `docs-ghaw-mcps.md` Claim 1. No secret is
  available unless explicitly declared at the tool level — this is a minimal-secret-
  surface design: each tool receives only the secrets it explicitly requires. The
  pattern is the same as external MCP server secret injection (the `env:` block
  in `docs-ghaw-mcps.md` examples), ensuring consistency across inline and external
  MCP tools. For Ch03 (Safety and Verification): the explicit secret declaration
  model is the recommended pattern for any tool integration. It limits blast radius
  if a tool is compromised — a malicious or misbehaving MCP Script cannot access
  secrets that were not explicitly declared in its `env:` block.

### Claim 6: Input parameters use JSON Schema conventions and are validated against the schema before tool execution; each runtime exposes inputs in its idiomatic form

- **Evidence**: Inputs are defined per tool using JSON Schema conventions: `type`
  (string, number, boolean, array, object), `required` (true/false), `default`,
  `enum`, and `description`. Inputs are "validated against schema before execution."
  Runtime-specific input access: JavaScript — local variables (destructured from
  function parameter); Shell — environment variables with `INPUT_` prefix (e.g.,
  `repo` becomes `$INPUT_REPO`); Python — `inputs.get('param_name')` dictionary;
  Go — JSON map from stdin.
- **Confidence**: settled (first-party specification; the JSON Schema field names
  and runtime access patterns are explicitly documented)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: JSON Schema input validation catches type mismatches and
  missing required parameters before tool code runs, providing clear error signals
  to the agent when tool invocation parameters are wrong. The four runtime-specific
  input access patterns (local vars / `INPUT_` env vars / dict / stdin) give each
  language its idiomatic input handling without forcing generic JSON parsing.
  For Ch02: document the four input access patterns as a quick reference when
  writing MCP Scripts (see Concrete Artifacts). The `enum` field is particularly
  useful for constrained-choice inputs — it limits the agent's degrees of freedom
  and makes tool behavior more predictable.

### Claim 7: Outputs exceeding 500 characters are auto-saved to files; the agent receives a metadata response with the file path, size, and optional JSON schema preview

- **Evidence**: The page documents: "Outputs exceeding 500 characters saved to
  temporary files with metadata response including file path, size, and optional
  schema preview." Small outputs (≤500 chars) are returned directly in the
  MCP response.
- **Confidence**: settled (first-party specification; the 500-character threshold
  is explicit)
- **Quote**: "Outputs exceeding 500 characters saved to temporary files with
  metadata response including file path, size, and optional schema preview."
- **Our assessment**: The 500-character output threshold is a context-budget
  protection mechanism. Large tool outputs returned directly in the MCP response
  consume agent context — file storage with a metadata pointer allows the agent
  to decide whether to read the full output rather than having it forced into
  context. The "optional schema preview" in the metadata suggests the file storage
  system can include a type-annotated summary of the output structure, enabling
  the agent to understand what the output contains before deciding to read it.
  For Ch02 and Ch04 (Context Engineering): practitioners writing MCP Scripts that
  return large datasets (e.g., PR diffs, log outputs, database query results)
  should be aware that the full output will not appear inline — design tools to
  return focused, summary-first outputs when possible, reserving large outputs for
  cases where the agent needs the full content.

### Claim 8: Error handling uses `data.recoverable` boolean to classify failures as transient (retry may succeed) or permanent (retry won't help)

- **Evidence**: JSON-RPC error responses "must include a `data.recoverable` boolean
  field." Two values: recoverable `true` — "Transient failure, retry may succeed";
  recoverable `false` — "Permanent failure, retry won't help." The normative
  phrasing ("must") makes this a required implementation constraint.
- **Confidence**: settled (first-party specification; "must" indicates a normative
  requirement in the specification)
- **Quote**: (no direct quote; the must/recoverable formulation is from the
  summarized source content; exact wording not confirmed verbatim)
- **Our assessment**: The `data.recoverable` boolean is a structured error
  classification mechanism that enables the agent engine to implement sensible
  retry logic without heuristics. Transient failures (network timeout, rate-limited
  API, temporary unavailability) signal that the agent should retry; permanent
  failures (malformed input, non-existent resource, auth failure) signal that
  retrying is futile and the agent should change strategy instead. For Ch02:
  practitioners writing MCP Scripts must set `data.recoverable` accurately.
  A permanent failure reported as recoverable causes wasted retries; a transient
  failure reported as permanent prevents correct handling. This is a contract
  between the tool author and the agent engine.

### Claim 9: MCP Scripts compile to HTTP-based MCP server endpoints via MCP Gateway integration — the gateway routes JSON-RPC requests to a local MCP Scripts server on a configurable port (default 3000)

- **Evidence**: The page documents MCP Gateway Integration as: "MCP Scripts extends
  MCP Gateway configuration, generating HTTP server endpoints that accept JSON-RPC
  requests during workflow execution." The gateway "routes requests to MCP Scripts
  server running on configurable port (default 3000)."
- **Confidence**: emerging (the gateway integration details are from WebFetch
  summarized output rather than confirmed verbatim; the default port of 3000 is
  specific but unverified as a direct quote)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The compilation to HTTP-based MCP server endpoints explains
  why MCP Scripts appear identical to external MCP servers from the agent's
  perspective — both present as MCP tools via the same JSON-RPC protocol. The
  inline definitions are transformed into a running HTTP service during the
  agent job's "MCP container initialization" step (per `docs-ghaw-compilation-process.md`
  Claim 5). The gateway abstraction is a transparency layer: the AI engine calls
  all tools via MCP regardless of whether they are inline scripts or external
  servers. For Ch02: this implementation detail means practitioners can treat
  MCP Scripts and external MCP servers as interchangeable from the agent's
  perspective — the difference is in the *authoring* experience, not the *runtime*
  interface.

### Claim 10: Dependencies are installed by language-specific package managers before tool execution — npm (JavaScript), pip (Python), go get (Go), apt/yum (Shell)

- **Evidence**: The `dependencies:` field "installs packages via language-specific
  managers (npm, pip, go get, apt/yum) before execution." The documented example:
  `dependencies: [requests]` for a Python tool that uses the `requests` library.
- **Confidence**: settled (first-party specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The `dependencies:` field automates package installation at
  tool runtime — no pre-built container image is required. This keeps MCP Scripts
  lightweight to define (no Dockerfile authoring) while allowing full access to
  the language ecosystem. The tradeoff: dependency installation adds latency to
  tool startup, particularly for large dependency trees or slow package registries.
  Per-invocation installation is likely mitigated by caching within the agent
  job's container, but practitioners should prefer standard-library capabilities
  where possible to minimize startup latency. For Ch02: use `dependencies:` for
  specialized libraries that the tool genuinely requires; avoid pulling in heavy
  dependency trees for simple operations.

### Claim 11: MCP Scripts are the inline counterpart to external MCP servers — inline for workflow-specific ephemeral tools; external servers for shared, complex, or third-party integrations

- **Evidence**: The page's design establishes MCP Scripts as "custom MCP tools
  defined inline in workflow frontmatter without requiring external MCP server
  implementations." The scope notes in `docs-ghaw-mcps.md` confirm the
  complementary relationship: that note covers external servers; this page covers
  inline scripts. The Prospector's triage comment explicitly frames this as a
  "complementary reference."
- **Confidence**: emerging (the complementary relationship is implied by design and
  confirmed by the Prospector; a "when to use which" decision guide is not
  explicitly stated on this page)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The choice between MCP Scripts and external MCP servers
  comes down to three factors: (1) *scope* — MCP Scripts are per-workflow;
  external servers can be shared across many workflows via the shared MCP library
  (`docs-ghaw-mcps.md` Claim 9 — 17 pre-built configurations); (2) *lifecycle* —
  MCP Scripts are ephemeral (instantiated per run); external servers may be
  persistent services; (3) *complexity* — MCP Scripts are single-function tools;
  external servers can implement multi-tool servers with state.
  For Ch02: add a decision path: check the shared MCP library first (17 servers);
  use MCP Scripts for workflow-specific read/query logic not covered by the shared
  library; reserve custom external MCP servers for team-wide capabilities or tools
  that need complex state or are used across many workflows.

## Concrete Artifacts

### `mcp-scripts:` Configuration Schema

```yaml
# Under workflow frontmatter mcp-scripts: block
mcp-scripts:
  tool-name:
    description: "Human-readable tool description"  # required

    # Exactly ONE of the following (mutually exclusive):
    script: |                    # JavaScript/Node.js CommonJS
      # code here
    run: |                       # Shell/Bash (Docker container)
      # code here
    py: |                        # Python 3.10+ (Docker container)
      # code here
    go: |                        # Go via go run (Docker container)
      // code here

    # Optional fields:
    inputs:                      # JSON Schema parameter definitions
      param_name:
        type: string             # string|number|boolean|array|object
        required: true
        default: value
        enum: [value1, value2]
        description: "Help text"

    env:                         # Explicit secret declarations only
      SECRET_NAME: "${{ secrets.SECRET_NAME }}"

    timeout: 60                  # Seconds (containerized tools); JS not enforced

    dependencies:                # Package manager installs before execution
      - package-name             # npm/pip/go get/apt-yum by language
```

*Source: `reference/mcp-scripts-specification` — Configuration Structure section*

### JavaScript MCP Script — GitHub API Example

```yaml
mcp-scripts:
  analyze-pr:
    description: "Analyze PR complexity"
    inputs:
      pr_number:
        type: number
        required: true
    script: |
      const octokit = github.getOctokit(process.env.GITHUB_TOKEN);
      const { data: pr } = await octokit.rest.pulls.get({
        owner: context.repo.owner,
        repo: context.repo.repo,
        pull_number: pr_number
      });
      return { complexity: pr.changed_files * 2 };
    env:
      GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
```

*Source: `reference/mcp-scripts-specification` — JavaScript runtime example*

### Runtime Input Access Patterns

```
JavaScript:  inputs.param_name         (local variable, destructured from function param)
             async function execute(inputs) { ... }

Shell:       $INPUT_PARAM_NAME         (INPUT_-prefixed environment variable)
             e.g., param "repo" → $INPUT_REPO

Python:      inputs.get('param_name')  (inputs dictionary)
             # inputs is a pre-populated dict available in execution scope

Go:          map[string]any from stdin (JSON map, parsed from stdin)
             // inputs provided as JSON via os.Stdin
```

*Source: `reference/mcp-scripts-specification` — Language Runtimes section*

### Security and Execution Model

```
Secret isolation:
  - Only env:-declared secrets are accessible
  - Syntax: env: { KEY: "${{ secrets.NAME }}" }
  - No implicit access to the workflow's full secret environment

Input validation:
  - JSON Schema validation before execution
  - Type checking, required field enforcement, enum constraint

Output sanitization:
  - ≤500 chars → returned inline in MCP response
  - >500 chars → saved to temporary file
  - Agent receives: { file_path, size, optional_schema_preview }

Timeout enforcement (containerized tools only):
  - Default: 60 seconds (configurable via timeout: field)
  - Termination: SIGTERM → grace period → SIGKILL
  - JavaScript: in-process, no timeout enforcement

Error classification (data.recoverable):
  - true  → transient failure; retry may succeed
  - false → permanent failure; retry won't help
```

*Source: `reference/mcp-scripts-specification` — Security Model and Error Handling sections*

### MCP Gateway Integration

```
Compilation: mcp-scripts: definitions → HTTP-based MCP server endpoints
Runtime:     MCP Gateway routes JSON-RPC requests → MCP Scripts server
Port:        Configurable (default 3000)

Result: From the AI engine's perspective, MCP Scripts and external MCP
        servers are identical — both present as MCP tools via JSON-RPC.
        The difference is in authoring, not in the runtime interface.
```

*Source: `reference/mcp-scripts-specification` — MCP Gateway Integration section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 6 ("Custom MCP tools defined inline in
    workflow frontmatter"): This source is the detailed specification of what
    Claim 6 describes in one sentence. The inline tool concept is confirmed and
    fully specified here — schema, runtimes, security model, and gateway integration.
  - `docs-ghaw-mcps.md` Claim 1 (read-only policy for external MCP servers, stated
    but not protocol-enforced): The explicit secret isolation model in MCP Scripts
    (Claim 5 here) follows the same "only explicitly declared" principle that the
    read-only policy applies to external servers. Both inline scripts and external
    servers implement minimal-access by default.
  - `docs-ghaw-compilation-process.md` Claim 5 (agent job step sequence includes
    "MCP container initialization"): Claim 9 here explains what that initialization
    step produces for MCP Scripts — the compilation to HTTP-based MCP server
    endpoints via the MCP Gateway.
  - `docs-ghaw-how-they-work.md` Claim 4 ("no write access by default"): The
    explicit `env:` declaration model for secrets (Claim 5 here) is the MCP Scripts
    expression of zero-capability-by-default — no secret is available unless
    explicitly declared.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts introduction): This source
    provides the full specification that Claim 6 only briefly introduces. Read
    together: Claim 6 establishes that inline custom tools exist; this source
    specifies everything about how to configure and use them.
  - `docs-ghaw-mcps.md` (external MCP server configuration): This source is the
    complementary reference for the *inline* case. The two together give the
    complete MCP tool integration picture for gh-aw: inline scripts (`mcp-scripts:`
    block, this source) and external servers (`mcp-servers:` block, `docs-ghaw-mcps.md`).
    The three-path model: (a) Safe Outputs for pre-approved GitHub state mutations;
    (b) MCP Scripts for workflow-specific inline read/query tools; (c) external MCP
    servers for shared, complex, or third-party integrations.
  - `docs-ghaw-compilation-process.md` Claim 10 (auto-generated Dockerfiles for
    stdio MCP servers): The containerized runtimes in MCP Scripts (Shell, Python,
    Go) are subject to the same auto-generated Dockerfile mechanism. Together,
    Claims 2–4 here and Claim 10 in the compilation process give a complete picture
    of how container-based MCP tools are provisioned without manual Docker authoring.

- **Contradicts**: None identified. No existing source note makes claims that
  materially oppose the MCP Scripts configuration schema, language runtime model,
  secret isolation model, or timeout behavior described here. The security model
  (explicit declarations, input validation, output sanitization) is additive to
  and consistent with the five-layer security architecture in
  `docs-ghaw-how-they-work.md` Claim 3. No contradiction issue required.

- **Novel**:
  - **Full MCP Scripts configuration schema** (Claim 2): No existing source note
    documents the `mcp-scripts:` block schema — `description`, `script`/`run`/`py`/
    `go` (mutually exclusive), `inputs`, `env`, `timeout`, `dependencies`. The
    `docs-ghaw-how-they-work.md` Claim 6 mentions MCP Scripts in one sentence;
    this is the first complete schema reference.
  - **Four-runtime model with isolation split** (Claims 2–4): The JavaScript
    in-process vs. Shell/Python/Go containerized split, with its direct consequence
    for timeout enforcement and isolation properties, is new to the corpus.
  - **Timeout enforcement asymmetry** (Claim 4): The explicit statement that
    JavaScript tools have no timeout enforcement while containerized tools have
    SIGTERM/SIGKILL enforcement is not documented in any existing source note.
    This is a material operational risk for JavaScript MCP Scripts with long-running
    operations.
  - **Runtime-specific input access patterns** (Claim 6): The four idiomatic
    input access patterns (local vars / `INPUT_` env / dict / stdin JSON) are
    new to the corpus.
  - **Large-output file storage at 500-char threshold** (Claim 7): The specific
    500-character threshold, file storage mechanism, and metadata response
    structure are new to the corpus.
  - **`data.recoverable` error classification** (Claim 8): The structured
    transient/permanent error distinction is not documented in any existing source
    note.
  - **MCP Gateway integration and port configuration** (Claim 9): The compilation
    of MCP Scripts to HTTP-based MCP server endpoints via the gateway is not
    described in `docs-ghaw-compilation-process.md` or any other existing note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add MCP Scripts as the third tool integration path** (Claims 1, 11): Ch02
  currently lacks a structured decision path for tool integration. Add the three-path
  model: (a) Safe Outputs for pre-approved GitHub state mutations
  (`docs-ghaw-how-they-work.md`); (b) MCP Scripts for workflow-specific inline
  read/query tools (this source); (c) external MCP servers for shared, complex, or
  third-party integrations (`docs-ghaw-mcps.md`). The decision criteria: check the
  17-server shared MCP library first; use MCP Scripts for gaps not covered by shared
  servers; build custom external servers only for team-wide capabilities.

- **Add `mcp-scripts:` schema as a reference artifact** (Claim 2, Concrete Artifacts):
  The configuration schema (description, mutually exclusive language fields, inputs,
  env, timeout, dependencies) and the four runtime input access patterns are the
  practical references practitioners need when writing inline tools. Add to the
  harness reference section.

- **Warn about JavaScript timeout gap** (Claim 4): JavaScript MCP Scripts have no
  platform-level timeout enforcement. Practitioners writing JavaScript tools with
  network calls or long-running operations must implement client-side timeouts or
  switch to containerized runtimes. Add this as a prominent caution in the MCP
  Scripts guidance.

- **Document `data.recoverable` as a tool implementation requirement** (Claim 8):
  Practitioners writing MCP Scripts must set `data.recoverable` accurately in
  error responses — this enables correct agent retry behavior. Add to the tool
  authoring guidelines alongside the schema reference.

### Chapter 03: Safety and Verification

- **Add explicit secret declaration as a tool-level isolation pattern** (Claim 5):
  The `env:` declaration model for MCP Scripts is a concrete instance of the
  zero-capability-by-default principle. No secret is available unless explicitly
  declared at the tool level. Add this as a named security practice for any inline
  tool definition: declare only the secrets the tool requires, at the tool level,
  not at the workflow level.

- **Add large-output file storage as a context-budget protection mechanism** (Claim 7):
  The 500-character output threshold means MCP Scripts cannot accidentally flood
  the agent's context with large tool outputs. This is a built-in context
  protection mechanism — document it as a safety design property of MCP Scripts.

### Chapter 04: Context Engineering / Tool Choice

- **Cross-reference the 500-character output threshold with context budget guidance**
  (Claim 7): Practitioners choosing between returning full outputs vs. summaries from
  MCP Scripts should know the threshold: outputs >500 chars are file-stored and the
  agent receives only metadata. Design tools to return focused outputs (with the agent
  requesting full content when needed) rather than bulk data dumps.

## Extraction Notes

1. **WebFetch returns AI-summarized content**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch returns rendered text with AI-assisted summarization,
   not raw page source. Two targeted fetches were performed to maximize content
   coverage. YAML examples and technical field names are assessed as accurate based
   on consistency across both fetches. However, direct quotes are only used when the
   text appears in a form that is clearly verbatim from the source (specification-style
   language, technical syntax). Claims where the phrasing is uncertain are marked
   "(no direct quote; see paraphrase in Our assessment)."

2. **Default timeout discrepancy between fetches**: The first WebFetch returned
   "default 30s for containers" while the second returned "Default 60 seconds for
   containerized tools." This inconsistency is likely an artifact of AI summarization
   of the same source page. The 60-second figure is used here (more specific; appeared
   in the second fetch which requested more detail), but the Assayer should verify
   the actual default against the source URL. Claims about the specific default
   timeout value should be treated as `emerging` confidence.

3. **JavaScript globals list from summarized content**: The list of injected GitHub
   Actions globals (`github`, `context`, `core`, `io`, `exec`, `glob`, `artifact`)
   is from the first WebFetch summarized output. The list is internally consistent
   with GitHub Actions toolkit capabilities, but exact completeness cannot be
   guaranteed from a summarized fetch. The Assayer should verify the complete list
   against the source.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-12.

5. **No contradictions filed**: Reviewed all existing source notes. No claims in
   this source materially oppose existing source notes at the MINER.md §4a filing
   threshold. The MCP Scripts specification is additive to and consistent with the
   existing security architecture and compilation model documented in other gh-aw
   source notes.

6. **Sub-pages not followed**: The page is a single specification reference. No
   linked sub-pages were identified that would be substantive for extraction.
   The five-linked-page budget from MINER.md §1 was not needed.
