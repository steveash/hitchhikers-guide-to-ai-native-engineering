---
source_url: https://github.github.com/gh-aw/reference/mcp-scripts-specification
source_type: docs
title: "GitHub Agentic Workflows: MCP Scripts Specification"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-26
last_checked: 2026-05-26
status: current
confidence_overall: emerging
issue: "#430"
---

# GitHub Agentic Workflows: MCP Scripts Specification

> The detailed specification for inline MCP tool definitions in gh-aw workflow
> frontmatter — documents the four-language runtime model, the `mcp-scripts:`
> configuration schema, security isolation properties, large-output file storage,
> JSON-RPC error classification, and MCP Gateway compilation, filling the gap
> between the conceptual mention in `docs-ghaw-how-they-work.md` and the
> full external-server reference in `docs-ghaw-mcps.md`.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/mcp-scripts-specification`
  page — the "Reference" section, Version 1.1.0 Draft. Distinct from the conceptual
  "How They Work" overview and the "Using Custom MCP Servers" guide. This page
  specifies the schema, runtime behavior, and security model for inline script tools;
  it does not cover external MCP server configuration.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind the Peli de Halleux agent factory blog series and the gh-aw
  platform. Schema field names, runtime behavior, and security markers (SM-*) are
  authoritative for the `gh aw` platform. Claims about language-specific execution
  environments and security constraints are settled for this platform; they do not
  automatically generalize to other MCP hosts.
- **Scope**: Inline MCP Scripts — configuration schema, four language runtimes (JS,
  Shell, Python, Go) with execution semantics, input parameter schema, secret
  isolation via `env:`, large-output handling, JSON-RPC error classification, MCP
  Gateway integration, and compliance test categories. Does NOT cover: external MCP
  server configuration (see `docs-ghaw-mcps.md`), the Safe Outputs mechanism for
  write operations (see `docs-ghaw-how-they-work.md`), general workflow compilation
  (see `docs-ghaw-compilation-process.md`), or cost benchmarking.

## Extracted Claims

### Claim 1: MCP Scripts enable inline custom tool definitions directly in workflow frontmatter, eliminating the need to deploy a separate MCP server for workflow-specific tools

- **Evidence**: The specification's stated purpose: "enables inline definition of
  custom MCP tools directly in workflow frontmatter using JavaScript, shell scripts,
  Python, or Go." Tools are defined under `mcp-scripts:` in the YAML frontmatter
  block, compiled alongside the workflow, and exposed to the AI engine via the MCP
  Gateway as HTTP endpoints.
- **Confidence**: settled (first-party specification; feature exists in platform)
- **Quote**: "enables inline definition of custom MCP tools directly in workflow
  frontmatter using JavaScript, shell scripts, Python, or Go"
- **Our assessment**: This is the core practitioner value proposition. A workflow
  author who needs a one-off tool (e.g., a script that queries an internal API, or
  parses a custom data format) can write it directly in the workflow file without
  provisioning, containerizing, or maintaining a separate MCP server process. The
  tradeoff: inline scripts are single-workflow; external servers can be shared across
  many workflows. For Ch02 (Harness Engineering): MCP Scripts are the lightweight
  path for workflow-specific tool integration. See Claim 11 for the decision model
  on when to use inline scripts vs. external servers.

### Claim 2: Four implementation languages are supported — JavaScript (in-process, no timeout), Shell, Python, and Go (all containerized, with timeout enforcement) — with distinct isolation profiles

- **Evidence**: The specification defines exactly one of four fields as the
  implementation: `script:` for JavaScript (CommonJS, Node.js), `run:` for Shell/Bash,
  `py:` for Python 3.10+, `go:` for Go (via `go run`). JavaScript executes in-process
  within the workflow runner with access to GitHub Actions global objects; Shell,
  Python, and Go execute in Docker containers. Timeout enforcement (the `timeout:`
  field) applies only to the containerized runtimes (`run:`, `py:`, `go:`) — not to
  `script:` (JavaScript).
- **Confidence**: settled (first-party specification; language options and container
  boundary are explicitly defined)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The in-process vs. containerized split is the most consequential
  isolation decision in the specification. JavaScript runs in the same process as the
  workflow runner, with V8 sandboxing (security marker SM-JS-01) but without process
  isolation. The three containerized runtimes have stronger isolation but incur Docker
  startup overhead and lack direct access to GitHub Actions globals. For Ch02: choose
  JavaScript when you need GitHub Actions context objects (github, context, core) with
  minimal overhead; choose containerized runtimes when you need stronger process
  isolation, language-specific libraries (pip, apt), or Go's type system. For Ch03:
  note that JavaScript has no timeout enforcement — long-running JavaScript tools can
  block the agent job indefinitely, which is a workflow-design risk to document.

### Claim 3: JavaScript tools execute in a sandboxed V8 context with injected GitHub Actions global objects — `github`, `context`, `core`, and others — available without explicit imports

- **Evidence**: The specification states JavaScript tools "execute in Node.js with
  access to GitHub Actions global objects (`github`, `context`, `core`, etc.) without
  explicit imports." Security marker SM-JS-01 states: "JavaScript tools execute in
  sandboxed V8 context; cannot access server internals."
- **Confidence**: settled (first-party specification; globals injection is a named
  design choice, SM-JS-01 is a stated security property)
- **Quote**: "JavaScript tools execute in Node.js with access to GitHub Actions
  global objects (`github`, `context`, `core`, etc.) without explicit imports"
- **Our assessment**: The globals injection is both a convenience (no import
  boilerplate for the most common GitHub API access pattern) and a security boundary
  (only the listed globals are injected; server internals are inaccessible per SM-JS-01).
  The `github.getOctokit(process.env.GITHUB_TOKEN)` pattern shown in the code examples
  means JavaScript tools can call the GitHub REST and GraphQL APIs directly. For Ch02:
  document the globals list as the effective API surface for JavaScript MCP Scripts.
  The injected objects are the same as those available in GitHub Actions JavaScript
  actions, making this pattern familiar to practitioners who have written GitHub Actions.

### Claim 4: The `mcp-scripts:` configuration schema requires a `description` and exactly one implementation field; `inputs`, `env`, `timeout`, and `dependencies` are optional

- **Evidence**: The specification defines the `mcp-scripts:` section schema with:
  - **Required**: `description` (human-readable tool description for agent guidance)
  - **Implementation** (exactly one required): `script:` (JavaScript), `run:` (Shell),
    `py:` (Python), `go:` (Go)
  - **Optional**: `inputs:` (JSON Schema parameter definitions), `env:` (environment
    variables and secret access), `timeout:` (duration limit, containers only),
    `dependencies:` (runtime packages to install)
- **Confidence**: settled (first-party specification; schema is explicitly defined)
- **Quote**: (no direct quote; see Concrete Artifacts for full schema template)
- **Our assessment**: The "exactly one implementation" constraint means the compiler
  can reject malformed tool definitions at compile time — a tool with both `script:`
  and `py:` is a compile-time error, not a runtime ambiguity. The `description` field
  is required because it is the text the AI engine uses to decide when to invoke the
  tool — an empty or vague description degrades tool selection quality. For Ch02: the
  `description` field functions like a system prompt for the tool — invest in clear,
  specific descriptions that tell the AI engine when and why to use each tool.

### Claim 5: Input parameters follow JSON Schema with types string/number/boolean/array/object; string inputs are capped at 10KB per parameter; language runtimes access inputs via different mechanisms

- **Evidence**: The specification defines input parameter schema: "Supported types:
  `string`, `number`, `boolean`, `array`, `object`. Constraints: `required`, `default`,
  `enum`, `description`. String inputs enforce maximum 10KB length per parameter."
  Security marker SM-IS-01: "Maximum 10KB per string input parameter (validation before
  execution)." Runtime access patterns: JavaScript accesses inputs as named local
  variables; Shell maps inputs to `INPUT_<NAME>` environment variables; Python accesses
  via `inputs` dictionary; Go receives inputs via stdin as JSON.
- **Confidence**: settled (first-party specification; input types, 10KB limit, and
  runtime access patterns are explicitly documented)
- **Quote**: "String inputs enforce maximum 10KB length per parameter"
- **Our assessment**: The 10KB cap per string parameter is an injection defense (SM-IS-01)
  — it bounds the size of attacker-controlled data that can reach the tool's execution
  environment. The enum constraint additionally provides a categorical guard: if a tool
  only accepts one of a fixed set of values, the spec can enforce this before execution.
  The different runtime access patterns (local vars / `INPUT_*` env / dict / stdin JSON)
  mean tool code must be written for the specific runtime — a Shell script using
  `$INPUT_PARAM` syntax cannot be pasted into a Python `py:` block. For Ch02: document
  the runtime-specific input access patterns as a migration consideration when changing
  a tool's language.

### Claim 6: Secrets are isolated via explicit `env:` declaration — only named secrets are accessible; undeclared secrets cannot be read even if they exist in the repository

- **Evidence**: The specification states: "explicit secret declaration prevents
  unauthorized access." The `env:` field maps environment variable names to secret
  references using the same `${{ secrets.SECRET_NAME }}` interpolation syntax as
  GitHub Actions. Secrets not listed in `env:` are not accessible to the tool's
  execution environment.
- **Confidence**: settled (first-party specification; the secret isolation model
  is a stated security design choice)
- **Quote**: "explicit secret declaration prevents unauthorized access"
- **Our assessment**: This is the MCP Scripts analog of the least-privilege principle
  applied to secret access. A tool definition that needs only a read-only API key
  cannot accidentally (or maliciously) access a deploy key or an org-wide token — the
  tool's env must explicitly name what it needs. This creates an auditable surface:
  the `env:` block in each tool definition is a complete declaration of that tool's
  secret access. For Ch03 (Safety and Verification): recommend that harness reviewers
  audit the `env:` block of each MCP Script alongside the tool implementation, treating
  secret declarations as part of the security posture. An `env:` block requesting
  broad write-capable tokens in a read-only tool is a red flag.

### Claim 7: Tool outputs exceeding 500 characters are saved to a file; a metadata response is returned instead, including path, size, and a structured preview for collection types

- **Evidence**: "When tool output exceeds 500 characters, implementations save
  complete results to files and return metadata containing file path, size, and
  optional preview information including JSON schema and item counts." The response
  format is a JSON object with `content.type: "file"`, `content.path`, `content.size`,
  `content.message`, and an optional `preview` block with `schema`, `first_item`,
  and `item_count`.
- **Confidence**: settled (first-party specification; threshold and response format
  are explicitly defined)
- **Quote**: "When tool output exceeds 500 characters, implementations save complete
  results to files and return metadata containing file path, size, and optional preview
  information including JSON schema and item counts."
- **Our assessment**: The 500-character threshold is deliberately low — it covers even
  a modest JSON array and forces file-based return for anything non-trivial. The
  metadata response (path + size + preview) is designed so the AI engine can decide
  whether to read the full file or proceed with the preview alone. The `first_item`
  and `item_count` fields in the preview block give the engine enough context to
  summarize a large collection result without loading the entire file. For Ch02: tool
  implementors should be aware that tools returning large responses do not stream or
  concatenate — the entire output is buffered and checked against the 500-char
  threshold. For Ch04 (Context Engineering): large-output tools require the AI engine
  to make a file-read decision, which costs additional tokens. Design tool APIs to
  return filtered/paginated results rather than bulk dumps where possible.

### Claim 8: JSON-RPC error responses include a required `data.recoverable` boolean — `true` for transient failures that may succeed on retry, `false` for permanent failures that must not be retried; default budget is 3 total attempts

- **Evidence**: The specification states: "Tools return JSON-RPC errors with a
  `data.recoverable` boolean field. Transient failures (timeouts, temporary startup
  issues) marked `true` may warrant retries, while permanent failures (syntax errors,
  invalid inputs) marked `false` should not. Default retry budget limits total attempts
  to three unless justified otherwise." The `data.recoverable` field "MUST only be
  used for transient failures where the same invocation MAY succeed on a subsequent
  attempt."
- **Confidence**: settled (first-party specification; the field semantics and retry
  budget are explicitly defined)
- **Quote**: "MUST only be used for transient failures where the same invocation MAY
  succeed on a subsequent attempt"
- **Our assessment**: The `data.recoverable` field shifts retry logic from the calling
  agent to the tool specification — the tool declares whether retry is appropriate,
  rather than leaving this judgment to the AI engine. This prevents the agent from
  retrying a syntax error (which will never succeed) while still allowing it to retry
  a Docker container startup timeout (which might). The 3-attempt default matches
  common retry patterns. For Ch02: tool implementors should set `recoverable: false`
  for all user-input validation errors and `recoverable: true` only for genuinely
  transient infrastructure failures (network hiccups, container startup delays). For
  Ch03: the recoverable=false guarantee prevents infinite retry loops on bad inputs,
  which is an agent safety property.

### Claim 9: MCP Scripts compile to HTTP MCP Gateway endpoints at runtime — the compiler translates `mcp-scripts:` frontmatter into gateway JSON served on localhost with API-key authentication

- **Evidence**: "MCP Scripts extends the MCP Gateway configuration format, translating
  workflow frontmatter into gateway JSON at compilation time. The system uses HTTP
  transport with API key authentication for server communication." The generated
  gateway configuration format specifies `type: "http"`, `url: "http://localhost:3000"`,
  and `headers: { Authorization: "api-key" }` under `mcpServers.safeinputs`.
- **Confidence**: emerging (the gateway integration description is based on
  AI-summarized WebFetch output; the exact gateway JSON format may contain additional
  fields not captured)
- **Quote**: "MCP Scripts extends the MCP Gateway configuration format, translating
  workflow frontmatter into gateway JSON at compilation time."
- **Our assessment**: The gateway integration means that from the AI engine's
  perspective, MCP Scripts are indistinguishable from external HTTP MCP servers —
  they appear as a standard MCP endpoint at localhost. The compilation step (from
  `docs-ghaw-compilation-process.md`) generates the gateway configuration alongside
  the `.lock.yml`, making MCP Script tools available to the engine without any runtime
  configuration discovery. For Ch02: this integration model means MCP Scripts are a
  zero-operational-overhead alternative to external servers for the AI engine — no
  server discovery, no network egress, no auth management beyond what the compiler
  generates. The localhost + API-key pattern is a standard MCP transport.

### Claim 10: Output sanitization (SM-01 through SM-03) passes all tool stdout through a redaction pipeline before returning to the MCP client — secret values are replaced with `"[REDACTED]"`

- **Evidence**: Security markers SM-01 through SM-03: "All tool stdout passed through
  redaction pipeline before MCP client return; secret values replaced with `[REDACTED]`."
  This applies to all four language runtimes.
- **Confidence**: settled (first-party specification; security markers are named
  constraints)
- **Quote**: (no direct quote for the redaction pipeline; see paraphrase in Our assessment)
- **Our assessment**: Output sanitization is the defense against accidental secret
  exposure — if a tool inadvertently prints an environment variable that contains a
  secret, the redaction pipeline masks it before the value reaches the AI engine's
  context. This is analogous to GitHub Actions' built-in secret masking in logs, but
  applied to MCP tool outputs. For Ch03: the SM-01-SM-03 output sanitization means
  practitioners should not rely on MCP Scripts to transmit secret values to the AI
  engine even intentionally — the redaction pipeline will mask them. Secret values
  should not appear in tool outputs; only derived, non-sensitive results should be
  returned.

### Claim 11: MCP Scripts are the right tool for workflow-specific, single-use tools; external MCP servers are better for shared, complex, or third-party integrations — the two are complementary, not competing

- **Evidence**: The scope of MCP Scripts (inline frontmatter, compiled per workflow)
  contrasts structurally with external MCP servers (deployed independently, referenced
  across workflows). The specification positions MCP Scripts as "lightweight," with
  `dependencies:` for runtime package installation enabling modest complexity.
  Cross-referencing `docs-ghaw-mcps.md`: the 17 shared MCP configurations cover common
  third-party services; MCP Scripts would be redundant for those and appropriate for
  workflow-specific logic not covered by shared configurations.
- **Confidence**: emerging (the decision model is inferred from the structural
  properties of both patterns; the specification does not state the decision criteria
  explicitly)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The three-path tool integration model for gh-aw practitioners:
  (a) **Safe Outputs** for pre-approved GitHub state mutations (write path, no MCP);
  (b) **MCP Scripts** for workflow-specific read/query tools defined inline;
  (c) **External MCP servers** for shared, third-party, or complex tools with multiple
  workflows. Ch02 should help practitioners navigate this decision. The key questions:
  Is this tool needed by one workflow or many? (one → MCP Script; many → external
  server). Is it a write operation or a read/query? (write → Safe Output; read →
  MCP Script or external server). Does a shared configuration already exist?
  (check `.github/workflows/shared/mcp/` from `docs-ghaw-mcps.md` Claim 9 first).

## Concrete Artifacts

### Full `mcp-scripts:` Configuration Schema

```yaml
# Source: MCP Scripts Specification v1.1.0 (Draft)
# under mcp-scripts: in workflow frontmatter

mcp-scripts:
  tool-name:
    description: "Required: human-readable tool description for agent guidance"

    # Exactly ONE implementation field required:
    script: "JavaScript code (CommonJS, Node.js in-process)"
    run: "Shell/Bash script"              # mutually exclusive with script/py/go
    py: "Python 3.10+ code"              # mutually exclusive with script/run/go
    go: "Go code (executed via go run)"  # mutually exclusive with script/run/py

    # Optional fields:
    inputs:
      param-name:
        type: string | number | boolean | array | object
        required: true | false
        default: value
        enum: [allowed-value-1, allowed-value-2]
        description: "Parameter description for agent"
        # Note: string inputs capped at 10KB per parameter (SM-IS-01)

    env:
      VAR_NAME: "${{ secrets.SECRET_NAME }}"  # explicit secret declaration only
      # Undeclared secrets are not accessible even if present in the repository

    timeout: 30  # seconds; applies to run/py/go only; NOT to script (JavaScript)
                 # UNVERIFIED DEFAULT: two fetches returned 30s and 60s respectively;
                 # spec states "30-60 seconds (implementation-dependent)", min 1s.
                 # Treat default as ~30-60s; confirm against live source if authoritative.

    dependencies:
      - package-name   # npm (script:), pip (py:), apt/yum (run:), go get (go:)
```

### Language-Specific Code Examples

```javascript
// JavaScript (script:) — in-process, GitHub Actions globals injected
script: |
  const octokit = github.getOctokit(process.env.GITHUB_TOKEN);
  const { data } = await octokit.rest.issues.create({
    owner: context.repo.owner,
    repo: context.repo.repo,
    title,
    body
  });
  return { number: data.number, url: data.html_url };
```

```bash
# Shell (run:) — containerized; inputs mapped to INPUT_<NAME> env vars
run: |
  gh pr list --repo "$INPUT_REPO" --state "$INPUT_STATE" --json number,title
env:
  GH_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
```

```python
# Python (py:) — containerized; inputs available via `inputs` dictionary
py: |
  import json
  numbers = [float(x.strip()) for x in inputs.get('numbers', '').split(',')]
  result = {"count": len(numbers), "sum": sum(numbers)}
  print(json.dumps(result))
dependencies:
  - requests
```

```go
// Go (go:) — containerized; inputs provided via stdin as JSON
go: |
  a := inputs["a"].(float64)
  result := map[string]any{"sum": a + b}
  json.NewEncoder(os.Stdout).Encode(result)
```

*Source: MCP Scripts Specification v1.1.0 — language-specific execution sections*

### Runtime Input Access Patterns

```
Runtime       | Implementation | Input Access                           | Process Model
--------------|----------------|----------------------------------------|--------------------
JavaScript    | script:        | Named local variables                  | In-process (V8)
Shell/Bash    | run:           | INPUT_<NAME> environment variables     | Containerized
Python 3.10+  | py:            | inputs dictionary                      | Containerized
Go            | go:            | stdin as JSON                          | Containerized (go run)

Timeout enforcement: run: / py: / go: only — script: (JavaScript) has NO timeout
Security: SM-JS-01 (V8 sandbox, no server internals); SM-IS-01 (10KB max per string input)
```

### Large Output Response Format

```json
// Triggered when tool output exceeds 500 characters
// Source: MCP Scripts Specification v1.1.0 — "Large Output Handling" section
{
  "content": {
    "type": "file",
    "path": "/tmp/tool-output-abc123.json",
    "size": 15234,
    "message": "Output too large (15234 bytes). Saved to file."
  },
  "preview": {
    "schema": { "type": "array" },
    "first_item": {},
    "item_count": 42
  }
}
```

### JSON-RPC Error Schema

```json
// Source: MCP Scripts Specification v1.1.0 — "Error Handling" section
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32603,
    "message": "Internal error",
    "data": {
      "error": "Tool execution timeout",
      "recoverable": false,
      "timeout_seconds": 60
    }
  }
}
// data.recoverable: true  → transient failure (timeout, temp startup); retry eligible
// data.recoverable: false → permanent failure (syntax error, invalid input); do not retry
// Default retry budget: 3 total attempts
```

### MCP Gateway Integration — Generated Configuration

```json
// Generated at compilation time from mcp-scripts: frontmatter
// Source: MCP Scripts Specification v1.1.0 — "MCP Gateway Integration" section
{
  "mcpServers": {
    "safeinputs": {
      "type": "http",
      "url": "http://localhost:3000",
      "headers": { "Authorization": "api-key" }
    }
  }
}
```

### Security Architecture Summary

```
Security Properties of MCP Scripts (from specification security markers):

SM-JS-01:  JavaScript tools execute in sandboxed V8 context; cannot access
           server internals
SM-IS-01:  Maximum 10KB per string input parameter — validated before execution
           (prevents large-payload injection attacks)
SM-01–03:  All tool stdout passed through redaction pipeline before MCP client
           return; secret values replaced with "[REDACTED]"

Process isolation:  Shell/Python/Go tools run in Docker containers (separate
                    process, separate filesystem from workflow runner)
Secret isolation:   Only secrets named in env: are accessible — undeclared
                    secrets are not in scope even if present in the repo
Timeout enforcement: SIGTERM + grace period → SIGKILL (containerized runtimes only)
                    Default: 30–60 seconds implementation-dependent (see Extraction Note 1)
                    Minimum: 1 second
```

### Compliance Test Categories

```
T-CFG-*     Configuration validation (tool definitions, input schemas, timeout values)
T-VAL-*     Input validation (required params, type coercion, enum constraints)
T-EXE-*     Language-specific execution (JS, Shell, Python, Go; secrets; timeouts; JSON parsing)
T-SEC-*     Security boundaries (secret isolation, process isolation, output sanitization,
            Go sandbox network restrictions)
T-MCP-050   (Additional security test — specific content not captured in fetch)
T-OUT-*     Large output handling (500-char threshold, metadata format, file accessibility)
T-DEP-*     Dependency management (installation, caching, failure handling)
T-INT-*     Gateway integration (config generation, HTTP startup, auth)
T-MS-NEG-*  Negative tests (missing implementation field rejection, invalid schema type rejection)
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 6: "Custom MCP tools defined inline in
    workflow frontmatter" — that note introduces MCP Scripts in one sentence; this
    source is the full specification of the mechanism Claim 6 names. Both confirm
    that MCP Scripts are an inline, frontmatter-defined tool pattern distinct from
    external MCP servers.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth security
    architecture): the MCP Scripts security model maps directly to three of those
    five layers — input validation (SM-IS-01) implements Layer 3 (permission
    separation / input control), secret isolation via `env:` implements Layer 3
    (permission separation), and output sanitization (SM-01–03) implements Layer 5
    (output sanitization). The MCP Scripts specification is additive to and consistent
    with the five-layer architecture described in that claim.
  - `docs-ghaw-how-they-work.md` Claim 4 ("no write access by default"): the
    read-only constraint on MCP Scripts (tools return data; writes go through Safe
    Outputs) is the MCP-layer expression of the same zero-capability-by-default
    principle. The `env:` secret isolation additionally ensures that even secrets
    needed for read operations are explicitly scoped.
  - `docs-ghaw-mcps.md` Claim 1 (custom MCP servers should be read-only): MCP Scripts
    share the same read-only design philosophy. Both inline scripts and external servers
    are expected to be read/query tools; write operations route through Safe Outputs.
    The two sources together establish read-only as the platform-wide MCP policy, not
    just an external-server constraint.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts as inline custom tools):
    this note is the complete specification of what Claim 6 names in a single sentence.
    Claim 6 establishes existence ("custom MCP tools defined inline in workflow
    frontmatter"); this source adds the full schema, four language runtimes, security
    model, error protocol, and gateway integration.
  - `docs-ghaw-mcps.md` (external MCP server reference): the two together complete
    the tool integration picture for gh-aw. The decision axis: scope of use (one
    workflow → MCP Script; many workflows → external server) and complexity (simple
    inline logic → MCP Script; deployed service with shared state → external server).
    `docs-ghaw-mcps.md` Claim 9 (17 shared MCP configurations) should be consulted
    before writing a new MCP Script — a shared config may already cover the need.
  - `docs-ghaw-compilation-process.md` Claim 5 (agent job step sequence: MCP container
    initialization occurs before prompt generation): MCP Scripts that use containerized
    runtimes (Shell, Python, Go) are initialized in the "MCP container initialization"
    step documented in that claim. Startup failures for containerized MCP Scripts
    appear in that step, before the AI engine receives its prompt.
  - `docs-ghaw-compilation-process.md` Claim 10 (local MCP servers run in Docker
    containers with auto-generated Dockerfiles): MCP Scripts using `run:`, `py:`, or
    `go:` are local MCP servers by this definition — their container infrastructure is
    auto-generated at compile time by the same mechanism.

- **Contradicts**: None identified. No existing source note makes claims that conflict
  with the four-language runtime model, `mcp-scripts:` schema, security markers, or
  gateway integration described here. The read-only philosophy is consistent with
  `docs-ghaw-how-they-work.md` Claim 4 and `docs-ghaw-mcps.md` Claim 1. The security
  model is additive to (not contradicting) the five-layer architecture in
  `docs-ghaw-how-they-work.md` Claim 3.

- **Novel**:
  - **Full `mcp-scripts:` configuration schema** (Claim 4): No existing source note
    documents the complete field-level schema for inline MCP tools. `docs-ghaw-how-they-work.md`
    Claim 6 names the feature; no note provides the schema.
  - **Four-language runtime model with distinct isolation profiles** (Claim 2): The
    in-process-JavaScript vs. containerized-Shell/Python/Go split, and its implication
    for timeout enforcement asymmetry, is new to the corpus.
  - **JavaScript globals injection without explicit imports** (Claim 3): The pattern
    of accessing `github`, `context`, `core` as pre-injected globals (not imported
    modules) in JavaScript MCP Scripts is new.
  - **10KB string input cap as an injection defense** (Claim 5): Security marker
    SM-IS-01 and the 10KB per-parameter limit are not documented in any existing note.
  - **Explicit secret isolation model** (Claim 6): The `env:`-declaration-only access
    pattern for secrets (undeclared secrets are inaccessible) is not documented in any
    existing note beyond the general "no write access by default" principle.
  - **Large-output file storage at 500-char threshold with metadata response** (Claim 7):
    The 500-character threshold and structured metadata response format (file path,
    size, schema, first_item, item_count) are new to the corpus.
  - **`data.recoverable` error classification in JSON-RPC** (Claim 8): The named
    field with MUST-level semantics ("MUST only be used for transient failures") and
    3-attempt default retry budget are new to the corpus.
  - **MCP Gateway compilation to localhost HTTP endpoint** (Claim 9): The specific
    gateway integration mechanism (frontmatter → gateway JSON → localhost:3000 +
    API-key) is not documented in any existing source note.
  - **Output redaction pipeline SM-01–03** (Claim 10): The named security markers for
    stdout redaction before MCP client return are new. `docs-ghaw-how-they-work.md`
    Claim 3 names "output sanitization" as Layer 5 but does not document the
    MCP-Scripts-specific redaction mechanism.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add MCP Scripts as the third tool integration path** (Claim 1, 11): The guide
  currently references the Safe Outputs / external MCP server dichotomy. Add MCP
  Scripts as the inline, workflow-specific tool path. Document the three-path decision
  model: Safe Outputs (write operations) → MCP Scripts (workflow-specific read tools)
  → external MCP servers (shared/third-party tools). Consult the 17 shared configs in
  `docs-ghaw-mcps.md` Claim 9 before writing a new inline script.

- **Document the `mcp-scripts:` schema in the harness reference** (Claim 4):
  The full schema template (see Concrete Artifacts) should appear in Ch02's harness
  engineering reference. Key emphasis: `description` quality determines tool-selection
  quality by the AI engine; exactly one implementation field is required; `timeout:`
  applies only to containerized runtimes.

- **Document the language selection decision** (Claim 2, 3): Add a decision table:
  use `script:` (JavaScript) when GitHub Actions globals (github, context, core) are
  needed and process isolation is not a priority; use `run:` (Shell), `py:` (Python),
  or `go:` (Go) when stronger process isolation or language-specific libraries are
  needed. Note that JavaScript has no timeout enforcement — a consideration for tools
  calling external APIs.

- **Document runtime-specific input access patterns** (Claim 5): Add the four access
  patterns (local vars / `INPUT_*` env / dict / stdin JSON) as a reference for tool
  implementors. This prevents copy-paste errors when changing a tool's runtime.

### Chapter 03: Safety and Verification

- **Add `env:` secret isolation as a harness security practice** (Claim 6): The
  explicit-declaration-only model means each tool's secret access is auditable from
  the frontmatter. Recommend that harness reviewers audit `env:` blocks alongside
  tool implementations. Flag any tool requesting write-capable tokens for a read-only
  purpose.

- **Document SM-01–03 output redaction** (Claim 10): MCP Script tool outputs are
  redacted before reaching the AI engine — secret values become "[REDACTED]". This
  means practitioners cannot use MCP Scripts to pass secrets to the agent even
  intentionally. Tool outputs should contain derived, non-sensitive results only.

- **Document JavaScript timeout gap** (Claim 2): JavaScript `script:` tools have no
  timeout enforcement. A JavaScript tool calling a slow external API can block the
  agent job indefinitely. For Ch03: recommend explicit timeout handling within
  JavaScript tool code (e.g., `Promise.race` with a timeout promise) as a defensive
  practice.

- **Document `data.recoverable` as a retry safety property** (Claim 8): The `false`
  value prevents infinite retry loops on bad inputs. Ch03 should name this as an agent
  safety property: tool specifications constrain retry behavior, reducing the risk of
  runaway loops from misconfigured or malicious inputs.

### Chapter 04: Context Engineering / Token Budget

- **Cross-reference large-output handling with context budget guidance** (Claim 7):
  Tools returning >500 characters trigger file storage and metadata responses.
  Practitioners should design tool APIs to return filtered, paginated results rather
  than bulk dumps. The metadata response's `first_item` + `item_count` preview is
  useful context for the AI engine without loading the full file — a token-efficient
  pattern to recommend.

## Extraction Notes

1. **Timeout default discrepancy across fetches**: Two separate WebFetch calls of
   the source URL returned different default timeout values. The first fetch returned
   "default 60 seconds for containerized tools." The second fetch returned
   "30–60 seconds (implementation-dependent), minimum 1 second." The schema artifact
   in this note uses a comment annotation (`# UNVERIFIED DEFAULT`) rather than
   presenting either value as definitive. The Assayer should verify the current
   default against the live source URL. The timeout behavior documented as certain:
   timeout applies only to `run:`, `py:`, `go:` (not `script:`); enforcement is
   SIGTERM + grace period + SIGKILL; minimum is 1 second.

2. **WebFetch returns AI-summarized content**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch returns rendered text processed by a small AI model,
   not raw page source. Two targeted fetches were used. Direct quotes are used only
   where both fetches returned consistent text. Claims with no reliable verbatim
   passage are marked "(no direct quote; see paraphrase in Our assessment)" per
   MINER.md §2a guidance.

3. **JavaScript globals list may be incomplete**: The second WebFetch listed
   `github`, `context`, `core` as examples with "etc." The specification may inject
   additional globals (e.g., `exec`, `io`, `glob` from `@actions/core` or similar).
   Claim 3 marks the globals list as "(github, context, core, etc.)" rather than an
   exhaustive enumeration.

4. **No publication date**: The documentation does not carry an explicit date.
   `date_published` is left null. Version 1.1.0 (Draft) is the stated version.

5. **No contradictions to file**: Reviewed all existing source notes. No claims in
   this source materially oppose any existing source note at the MINER.md §4a filing
   threshold. The MCP Scripts security model is additive to the five-layer
   architecture in `docs-ghaw-how-they-work.md` Claim 3; the read-only philosophy
   is consistent with `docs-ghaw-mcps.md` Claim 1.
