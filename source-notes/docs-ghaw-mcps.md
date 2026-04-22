---
source_url: https://github.github.com/gh-aw/guides/mcps
source_type: docs
title: "GitHub Agentic Workflows: Using Custom MCP Servers"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: emerging
issue: "#297"
---

# GitHub Agentic Workflows: Using Custom MCP Servers

> The definitive configuration reference for custom MCP servers in gh-aw —
> documents the four server types (stdio, Docker, HTTP, registry), the
> `allowed:` tool-filter pattern as a minimal-privilege design, GitHub Actions
> OIDC as a secretless auth mechanism for HTTP MCP endpoints, and the
> platform's read-only MCP policy (policy stated but not enforced at the
> protocol level — compliance responsibility falls on the MCP server itself).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows guides page, "Guides > Using
  Custom MCP Servers" — prescriptive configuration reference, not a conceptual
  overview or blog post. Distinct from the "How They Work" architecture page and
  the blog series.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research — the
  same team behind Peli de Halleux's agent factory blog series and the gh-aw
  platform. Claims about YAML schema, CLI behavior, and platform policy are
  authoritative for this platform. Claims about generalizability of the OIDC
  pattern or the `allowed:` discipline to other MCP hosts require additional
  evidence and are assessed separately.
- **Scope**: MCP server integration configuration — transport types, auth
  mechanisms, tool filtering, network controls, CLI management, and the shared
  MCP configuration library. Does NOT cover: the Safe Outputs mechanism for write
  operations (that is `docs-ghaw-how-they-work.md`), MCP Scripts (inline tools in
  frontmatter, also in that note), general workflow compilation or the five-layer
  security architecture, or cost benchmarking. This page is the "how to configure
  external MCP servers"; the "how they work" page is the "why the security
  architecture is designed this way."

## Extracted Claims

### Claim 1: Custom MCP servers are required to be read-only; the platform states this as policy but does NOT enforce it at the protocol level

- **Evidence**: A Caution callout in the documentation states explicitly: "Custom
  MCP servers should be read-only. Write operations must go through safe outputs
  or Custom Safe Outputs. Ensure your MCP server implements authentication and
  authorization to prevent unauthorized write access." The phrasing "Ensure your
  MCP server implements" places compliance responsibility on the server author,
  not on the gh-aw runtime.
- **Confidence**: settled (stated platform policy; the compliance gap is explicit
  in the wording)
- **Quote**: "Custom MCP servers should be **read-only**. Write operations must
  go through safe outputs or Custom Safe Outputs. Ensure your MCP server
  implements authentication and authorization to prevent unauthorized write
  access."
- **Our assessment**: This is the most important safety finding on the page. The
  "should be read-only" combined with "Ensure your MCP server implements auth"
  means the platform trusts the server author to enforce the constraint — it does
  not inspect MCP responses for state mutations or block write-capable tool calls
  at the protocol level. The Safe Outputs channel (from `docs-ghaw-how-they-work.md`
  Claim 5) is the correct path for state mutation; MCP is the correct path for
  read/query. Practitioners building custom MCP servers for gh-aw must enforce
  this split themselves. For Ch03 (Safety and Verification): this is a concrete
  gap in the five-layer security model — Layer 5 (output sanitization) applies to
  Safe Outputs, but MCP tool responses that mutate state could bypass it if the
  server allows writes. The guidance is defensive: build your MCP servers to be
  read-only, and route writes through Safe Outputs.

### Claim 2: Four MCP server types have distinct trust and isolation profiles: stdio (local process), Docker container (sandboxed), HTTP (remote), registry-based (curated + containerized)

- **Evidence**: The page documents four configuration types with different fields
  and isolation properties. Stdio uses `command` + `args` for local process
  execution. Docker uses `container` + `args` (docker run options) + `entrypointArgs`
  (application parameters). HTTP uses `url` with optional `headers` or `auth`. Registry
  uses `registry` (metadata URL at `https://api.mcp.github.com/v0`) combined with
  `container` for the actual image.
- **Confidence**: settled (first-party documentation; the four schema variants are
  explicitly defined)
- **Quote**: (from the four separate configuration examples — see Concrete Artifacts)
- **Our assessment**: The isolation hierarchy matters for security assessment: stdio
  servers run as a child process in the workflow runner — they can access the
  runner filesystem if volumes are mounted. Docker containers are sandboxed and
  can have their network access restricted via `network.allowed`. HTTP servers
  are fully remote — the workflow runner makes outbound HTTPS calls. Registry-based
  servers add a curation layer: the registry entry at `api.mcp.github.com/v0`
  provides verified metadata, while the `container:` field specifies the actual
  image. For Ch02 (Harness Engineering): the four-type taxonomy helps practitioners
  choose the appropriate transport for their security posture. Prefer Docker or HTTP
  for production harnesses that need network isolation and reproducibility.

### Claim 3: The `allowed:` field implements minimal-privilege tool access at the MCP protocol boundary — either an explicit named list or `["*"]` for unrestricted access

- **Evidence**: All four server type examples include an `allowed:` field. The Notion
  example uses a named list (`["search_pages", "get_page", "get_database",
  "query_database"]`); the deepwiki example uses `["read_wiki_structure",
  "read_wiki_contents", "ask_question"]`; simple integrations use `["*"]`. The
  `allowed:` field is per-server and per-workflow — each server declaration
  independently scopes which tools the agent may call.
- **Confidence**: settled (first-party; schema is explicit and consistent across all
  examples)
- **Quote**: (from Notion example) `allowed: ["search_pages", "get_page", "get_database", "query_database"]`
- **Our assessment**: The `allowed:` field is the structural answer to the token cost
  problem documented in `blog-bswen-mcp-token-cost.md` — if only named tools are
  allowed, only those tool definitions are loaded into the agent's context. The Notion
  example narrows a server with potentially many tools to four specific read operations.
  This is a minimal-privilege pattern at two levels simultaneously: (1) security —
  the agent cannot invoke tools outside the allowlist; (2) context budget — only
  allowed tool definitions are included in the system prompt. For Ch02 and Ch04:
  the `allowed:` field is the recommended discipline for MCP integration. Using
  `["*"]` is appropriate only for single-purpose servers; for multi-tool servers,
  name only the tools the workflow actually needs.

### Claim 4: GitHub Actions OIDC authentication for HTTP MCP servers acquires short-lived JWTs without static secrets, validated at the server endpoint

- **Evidence**: The OIDC example shows: `auth: type: github-oidc` with an `audience`
  field matching the server's base URL. Requires `id-token: write` in the workflow
  permissions block. The documentation states tokens are "validated at the MCP server
  endpoint rather than within the workflow runner" — the runner acquires the JWT from
  the OIDC endpoint and forwards it as a Bearer header; the receiving MCP server
  validates the token independently.
- **Confidence**: settled (OIDC is a standard protocol; the gh-aw integration with
  GitHub Actions OIDC tokens is first-party documented behavior)
- **Quote**: (from OIDC example)
  ```yaml
  permissions:
    id-token: write
  mcp-servers:
    my-secure-server:
      url: "https://my-server.example.com/mcp"
      auth:
        type: github-oidc
        audience: "https://my-server.example.com"
      allowed: ["*"]
  ```
- **Our assessment**: OIDC auth is the secure default for HTTP MCP integration. The
  advantages over static header auth (Claim 5): tokens are short-lived (typically 1
  hour TTL), scoped to the specific audience, and automatically rotated — no secrets
  to store, rotate, or leak. The same OIDC flow is used widely in GitHub Actions for
  cloud provider authentication (AWS, Azure, GCP), so practitioners familiar with
  Actions already understand the mechanism. For Ch03: recommend OIDC over static
  headers for any HTTP MCP server under team or organizational control. For stateless
  third-party services that don't support OIDC validation, static headers are the
  fallback.

### Claim 5: Static header authentication injects credentials via secret interpolation — simpler but carries static-credential risk

- **Evidence**: The HTTP example shows `headers: Authorization: "Bearer ${{ secrets.API_TOKEN }}"`.
  Secret interpolation uses the same `${{ secrets.NAME }}` syntax as GitHub Actions
  environment variables. The credential is injected at runtime from the repository
  or organization secrets store.
- **Confidence**: settled (first-party; syntax is consistent with GitHub Actions
  secret handling)
- **Quote**: `headers: { Authorization: "Bearer ${{ secrets.API_TOKEN }}" }`
- **Our assessment**: Static header auth is appropriate for third-party SaaS MCP
  servers that issue API keys (e.g., Brave Search, DataDog, Slack). The risk is
  that a compromised secret persists until manually rotated; a compromised OIDC
  token expires automatically. For Ch03: document static headers as the fallback
  auth pattern when the MCP server does not support OIDC. Recommend pairing with
  secret rotation and scoping API keys to read-only permissions at the issuing
  service.

### Claim 6: Docker container MCP servers support fine-grained network controls via a `network.allowed` domain allowlist

- **Evidence**: The Docker container example includes a `network` block:
  `network: allowed: [defaults, api.example.com]`. The `defaults` entry presumably
  permits standard GitHub Actions network access; additional domain entries extend
  the allowlist. Combined with `args: ["-v", "/host/data:/app/data"]` for volume
  mounts and `entrypointArgs` for application parameters, Docker servers offer the
  most granular isolation configuration of the four types.
- **Confidence**: settled (first-party; schema is explicit)
- **Quote**: `network: allowed: [defaults, api.example.com]`
- **Our assessment**: Docker container servers are the highest-isolation option:
  network egress is restricted to named domains, file system access is limited to
  explicitly mounted volumes, and the application runs in a reproducible, versioned
  container image. This is the right choice for MCP servers that access sensitive
  internal data or need strict network containment. The `network.allowed` field
  directly addresses Layer 4 of the five-layer security pipeline from
  `docs-ghaw-how-they-work.md` Claim 3 — network controls at the MCP server level,
  not just at the workflow runner level.

### Claim 7: The `gh aw mcp add` CLI integrates with the GitHub MCP registry at `https://api.mcp.github.com/v0` and supports transport, identity, and custom registry overrides

- **Evidence**: The documented CLI commands are:
  - `gh aw mcp add my-workflow makenotion/notion-mcp-server` — add from registry
  - `--transport stdio` — override the default transport
  - `--tool-id my-notion` — assign a custom server identity in the workflow
  - `--registry https://custom.registry.com/v1` — use a non-default registry
  - `gh aw mcp inspect my-workflow [--server <name> --verbose]` — inspect config
  - `gh aw mcp list-tools <server> my-workflow` — enumerate available tools
- **Confidence**: settled (first-party; CLI commands are explicitly documented)
- **Quote**: `gh aw mcp add my-workflow makenotion/notion-mcp-server`
- **Our assessment**: The `gh aw mcp` CLI family closes the tooling loop for MCP
  management: `add` installs (with transport customization), `inspect` validates
  the resulting configuration, and `list-tools` enumerates the tool surface before
  deciding what to put in `allowed:`. The `list-tools` command is especially useful
  for the `allowed:` discipline from Claim 3 — practitioners can enumerate available
  tools before choosing which to permit, rather than defaulting to `["*"]`. For Ch02:
  document the `inspect` + `list-tools` + `allowed:` workflow as the recommended
  onboarding sequence for any new MCP server.

### Claim 8: Registry-based servers combine a metadata pointer at `api.mcp.github.com/v0` with an explicit container image — the registry is informational, not a runtime dependency

- **Evidence**: The registry example shows: `registry: https://api.mcp.github.com/v0/servers/microsoft/markitdown`
  paired with `container: "ghcr.io/microsoft/markitdown"`. The source notes this is
  "primarily informational" — the registry entry provides metadata (provenance,
  versioning, trust signal) but the workflow runtime pulls from the container registry
  directly.
- **Confidence**: emerging (the "primarily informational" qualifier is from a
  summarized description; the exact role of the registry field in runtime behavior
  is not fully specified in the fetched content)
- **Quote**: `registry: https://api.mcp.github.com/v0/servers/microsoft/markitdown`
- **Our assessment**: The registry + container pairing suggests a two-layer trust
  model: the registry entry vouches for the server (curated, reviewed), while the
  container field specifies the actual runtime artifact. This is analogous to a
  package manager with verified metadata — the index says the package is trustworthy;
  the artifact store provides the actual bytes. For Ch02: the registry-based pattern
  is the recommended starting point for well-known integrations; manual `container:`
  or `url:` declarations are appropriate when no registry entry exists or the
  practitioner needs a custom build.

### Claim 9: A library of 17 pre-built shared MCP configurations exists in `.github/workflows/shared/mcp/` covering major platforms and services

- **Evidence**: The documentation lists the following available shared configurations:
  AST-Grep, Azure, Brave Search, Context7, DataDog, DeepWiki, Drain3, Fabric RTI,
  Jupyter, MarkItDown, Microsoft Docs, Notion, Sentry, Serena, Server Memory, Slack,
  Tavily.
- **Confidence**: settled (explicit directory listing from first-party documentation)
- **Quote**: (shared configuration list — see above)
- **Our assessment**: The shared MCP library means practitioners can integrate common
  services (Sentry for error monitoring, Slack for notifications, Context7 for library
  docs, DataDog for observability) without writing custom MCP server configurations.
  The list also reveals which services the gh-aw team considers canonical for agentic
  workflows. Notable inclusions: Context7 (documentation lookup), Serena (code analysis),
  DeepWiki (codebase understanding) — all read-only knowledge tools consistent with
  Claim 1's read-only policy. For Ch02: practitioners should check the shared library
  before writing custom MCP configurations; many common integrations are already
  available.

### Claim 10: The `allowed:` tool filter operates at per-server granularity, enabling different tool scopes for different MCP servers within the same workflow

- **Evidence**: The basic configuration template in the documentation shows two
  servers in the same workflow frontmatter with different `allowed:` configurations:
  `microsoftdocs` uses `allowed: ["*"]`; `notion` uses a four-item named list.
  This demonstrates that tool scoping is independent per server — a workflow can
  grant broad access to a documentation server while tightly restricting access to
  a database integration.
- **Confidence**: settled (shown explicitly in the template; schema is per-server)
- **Quote**:
  ```yaml
  mcp-servers:
    microsoftdocs:
      url: "https://learn.microsoft.com/api/mcp"
      allowed: ["*"]
    notion:
      container: "mcp/notion"
      allowed: ["search_pages", "get_page", "get_database", "query_database"]
  ```
- **Our assessment**: Per-server `allowed:` granularity enables a layered trust
  model within a single workflow: trusted, purpose-built servers (e.g., a
  documentation lookup server with a small, well-defined tool surface) can use
  `["*"]`; servers with broad capabilities (e.g., a general-purpose database MCP)
  should be restricted to the specific tools the workflow actually requires. This
  is a workflow-level implementation of least privilege. For Ch02: recommend that
  workflow authors audit each server's tool surface via `gh aw mcp list-tools`
  before setting `allowed:`.

## Concrete Artifacts

### Basic Configuration Template (Two Servers, Different `allowed:` Scopes)

```yaml
---
on: issues
permissions:
  contents: read
mcp-servers:
  microsoftdocs:
    url: "https://learn.microsoft.com/api/mcp"
    allowed: ["*"]
  notion:
    container: "mcp/notion"
    env:
      NOTION_TOKEN: "${{ secrets.NOTION_TOKEN }}"
    allowed:
      - "search_pages"
      - "get_page"
      - "get_database"
      - "query_database"
---
```

*Source: docs-ghaw-mcps "Basic Configuration Template" section*

### Stdio MCP Server

```yaml
mcp-servers:
  serena:
    command: "uvx"
    args: ["--from", "git+https://github.com/oraios/serena", "serena"]
    allowed: ["*"]
```

*Source: docs-ghaw-mcps "Stdio MCP Server Example" section*

### Docker Container MCP Server (with Volume Mount and Network Controls)

```yaml
mcp-servers:
  custom-tool:
    container: "mcp/custom-tool:v1.0"
    args: ["-v", "/host/data:/app/data"]
    entrypointArgs: ["serve", "--port", "8080"]
    env:
      API_KEY: "${{ secrets.API_KEY }}"
    allowed: ["tool1", "tool2"]
    network:
      allowed:
        - defaults
        - api.example.com
```

*Source: docs-ghaw-mcps "Docker Container MCP Server Example" section*

### HTTP MCP Server — Static Header Auth

```yaml
mcp-servers:
  deepwiki:
    url: "https://mcp.deepwiki.com/sse"
    allowed:
      - read_wiki_structure
      - read_wiki_contents
      - ask_question
  authenticated-api:
    url: "https://api.example.com/mcp"
    headers:
      Authorization: "Bearer ${{ secrets.API_TOKEN }}"
    allowed: ["*"]
```

*Source: docs-ghaw-mcps "HTTP MCP Server Examples" section*

### HTTP MCP Server — GitHub Actions OIDC Auth

```yaml
permissions:
  id-token: write
mcp-servers:
  my-secure-server:
    url: "https://my-server.example.com/mcp"
    auth:
      type: github-oidc
      audience: "https://my-server.example.com"
    allowed: ["*"]
```

*Source: docs-ghaw-mcps "GitHub Actions OIDC Authentication" section*

### Registry-Based MCP Server

```yaml
mcp-servers:
  markitdown:
    registry: https://api.mcp.github.com/v0/servers/microsoft/markitdown
    container: "ghcr.io/microsoft/markitdown"
    allowed: ["*"]
```

*Source: docs-ghaw-mcps "Registry-based MCP Server Example" section*

### `gh aw mcp` CLI Commands

```bash
# Browse and add from registry
gh aw mcp add
gh aw mcp add my-workflow makenotion/notion-mcp-server

# Customize transport or identity at add time
gh aw mcp add my-workflow makenotion/notion-mcp-server --transport stdio
gh aw mcp add my-workflow makenotion/notion-mcp-server --tool-id my-notion

# Use a non-default registry
gh aw mcp add my-workflow server-name --registry https://custom.registry.com/v1

# Inspect and enumerate tools
gh aw mcp inspect my-workflow
gh aw mcp inspect my-workflow --server <name> --verbose
gh aw mcp list-tools <server> my-workflow
```

*Source: docs-ghaw-mcps "CLI Management" section*

### Read-Only Policy Caution (Verbatim)

```
CAUTION: Custom MCP servers should be read-only. Write operations must go
through safe outputs or Custom Safe Outputs. Ensure your MCP server implements
authentication and authorization to prevent unauthorized write access.
```

*Source: docs-ghaw-mcps — Caution callout*

### Shared MCP Configuration Library (`.github/workflows/shared/mcp/`)

```
Available pre-built configurations (17 servers):
  AST-Grep       — code pattern search
  Azure          — Azure cloud services
  Brave Search   — web search
  Context7       — library/documentation lookup
  DataDog        — observability/monitoring
  DeepWiki       — codebase understanding
  Drain3         — log clustering
  Fabric RTI     — (real-time intelligence)
  Jupyter        — notebook execution
  MarkItDown     — document conversion
  Microsoft Docs — learn.microsoft.com lookup
  Notion         — Notion workspace access
  Sentry         — error monitoring
  Serena         — code analysis
  Server Memory  — persistent memory store
  Slack          — team messaging
  Tavily         — web search/research
```

*Source: docs-ghaw-mcps "Shared Configurations" section*

## Cross-References

- **Corroborates**:
  - `blog-bswen-mcp-token-cost.md` Claim 1 (every MCP server loads all its tool
    definitions before you type anything): the `allowed:` field (Claims 3 and 10)
    is the direct structural mitigation. By restricting to a named list of tools,
    gh-aw prevents the full tool catalog from loading into the agent's system prompt.
    The Notion example (4 allowed tools from a server with potentially many more)
    is a concrete instance of Bswen's recommended discipline ("be ruthless about
    necessity"). Both sources agree that tool surface control is a first-class
    design concern.
  - `docs-ghaw-how-they-work.md` Claim 4 (workflows run with minimal permissions,
    no write access by default): the read-only MCP caution (Claim 1) is the
    MCP-layer expression of the same principle. Safe Outputs is the write path for
    GitHub state changes; read-only MCP is the read/query path. The two together
    implement the information-flow separation that makes the security architecture
    coherent.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth pipeline):
    Docker network controls (Claim 6, `network.allowed`) correspond directly to
    Layer 4 (network controls) of the security pipeline. This page provides the
    concrete configuration mechanism for that layer at the MCP-server level.

- **Extends**:
  - `docs-ghaw-how-they-work.md` Claim 6 (MCP Scripts as inline custom tools):
    this note adds the complementary picture — external MCP servers (all four
    types). The two together give the complete MCP integration story for gh-aw:
    inline scripts (MCP Scripts) for workflow-specific tools; external servers
    for shared, complex, or third-party integrations. The choice is: scope of use
    (one workflow vs. many) and complexity (simple script vs. deployed server).
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as the write path):
    this note clarifies that MCP is explicitly the read path — not just by
    convention, but by stated policy (Claim 1 Caution). Safe Outputs handles
    write; MCP handles read/query. Read together, practitioners have a clear
    information-flow diagram.
  - `blog-bswen-mcp-token-cost.md` Claim 4 (recommended MCP budget: 3-6 servers,
    "be ruthless about necessity"): this note adds that ruthlessness is architecturally
    supported via `allowed:` tool filtering. Bswen recommends pruning the server
    list; gh-aw additionally recommends pruning the tool list within each server.
    Both levers reduce the baseline token load.

- **Contradicts**: None identified. No existing source note makes claims that
  contradict the four-type taxonomy, `allowed:` discipline, OIDC mechanism, or
  read-only policy described here. The read-only policy is consistent with (and
  extends) the "no write access by default" principle in `docs-ghaw-how-they-work.md`.

- **Novel**:
  - **Read-only policy stated but not protocol-enforced** (Claim 1): No existing
    source note documents this compliance gap — that gh-aw's MCP security depends
    on server-side enforcement, not platform-level enforcement. This is a Ch03
    finding: the five-layer security model has an assumption at the MCP boundary
    that practitioners must implement themselves.
  - **Four-type MCP server taxonomy with distinct isolation profiles** (Claim 2):
    No existing source documents the four types as a taxonomy with different
    security/isolation properties. `docs-ghaw-how-they-work.md` mentions MCP as
    a tool integration mechanism but does not distinguish server types.
  - **GitHub Actions OIDC for MCP HTTP auth** (Claim 4): The specific `auth: type:
    github-oidc` mechanism with `audience` field and `id-token: write` permission
    requirement is new to the corpus. No existing note documents OIDC as an MCP
    authentication pattern.
  - **Docker `network.allowed` domain allowlisting** (Claim 6): Per-server network
    egress controls at the domain level are not documented in any existing source
    note. This extends the network controls layer of the security architecture to
    the MCP-server level.
  - **`gh aw mcp` CLI family** (Claim 7): The `add`, `inspect`, and `list-tools`
    commands as a MCP management workflow are new to the corpus.
  - **`allowed:` filter as a token-cost mitigation** (Claim 3 + 10, cross-reference
    with bswen): While the `allowed:` field is a security mechanism, its secondary
    effect on context token cost (only allowed tools load into the system prompt)
    is a new connection not drawn in any existing note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add four-type MCP server taxonomy** (Claim 2): The guide currently lacks a
  taxonomy of MCP server types with their respective trust and isolation profiles.
  Add: stdio (local process, filesystem access via volumes), Docker (sandboxed,
  network-controlled), HTTP (remote, auth required), registry-based (curated +
  containerized). Help practitioners choose the right type for their security posture.

- **Name the `allowed:` discipline** (Claims 3 and 10): When integrating any MCP
  server, the workflow author should: (1) run `gh aw mcp list-tools <server>` to
  enumerate the tool surface, (2) identify the specific tools the workflow requires,
  (3) set `allowed:` to that named list. Defaulting to `["*"]` is acceptable only
  for single-purpose servers with a small, well-defined tool surface.

- **Add `gh aw mcp inspect` + `list-tools` as the MCP onboarding workflow** (Claim 7):
  When adding a new MCP server: `add` → `inspect` → `list-tools` → set `allowed:`.
  This four-step pattern closes the gap between "the server is configured" and
  "the workflow uses it with appropriate scope."

- **Document shared MCP library as the starting point** (Claim 9): Before writing
  a custom MCP configuration, check `.github/workflows/shared/mcp/` for existing
  definitions. 17 common services are already pre-built. Cite the list as a
  practitioner reference.

### Chapter 03: Safety and Verification

- **Document the MCP read-only compliance gap** (Claim 1): The five-layer security
  model from `docs-ghaw-how-they-work.md` has an implicit assumption at the MCP
  boundary — that MCP servers are read-only. The platform states this as policy but
  does not enforce it at the protocol level. Ch03 should name this assumption
  explicitly: if a custom MCP server allows writes, it bypasses the Safe Outputs
  permission-separation model. Practitioners building custom MCP servers must enforce
  read-only behavior themselves.

- **Add OIDC as the preferred auth pattern for HTTP MCP** (Claim 4): For MCP servers
  under team or organizational control, `auth: type: github-oidc` with a matching
  `audience` is the secure default — no static secrets, automatic token expiry, same
  mechanism as cloud provider auth in GitHub Actions. Document static headers (Claim 5)
  as the fallback for third-party services.

- **Add Docker `network.allowed` as a Layer 4 configuration** (Claim 6): For MCP
  servers that handle sensitive data or need strict network containment, Docker
  container type with `network.allowed` domain allowlisting implements Layer 4
  (network controls) of the security pipeline at the server level. Recommend for
  any MCP server accessing internal APIs or proprietary data.

### Chapter 04: Context Engineering / Tool Choice

- **Cross-reference `allowed:` with the MCP token cost finding** (Claim 3 +
  `blog-bswen-mcp-token-cost.md`): The `allowed:` filter is a dual-purpose
  mechanism — security (restrict tool invocation) and context budget (restrict tool
  definitions loaded into the system prompt). Update the MCP token cost guidance to
  note that `allowed:` is the architectural solution, not just server-count pruning.
  The two levers together: prune the server list (Bswen) AND prune the tool list
  within each server (this source).

## Extraction Notes

1. **WebFetch returns summarized content**: The gh-aw documentation is an Astro/Starlight
   SPA. WebFetch returns rendered text with AI summarization, not raw page source.
   Configuration examples were extracted via two targeted fetches to maximize fidelity.
   The YAML examples match consistent patterns across both fetches and are assessed as
   accurate to the source. Any minor formatting variations in the YAML are possible.

2. **Registry field semantics are partially uncertain**: The description of `registry:`
   as "primarily informational" comes from the summarized description, not a direct
   quote. The exact runtime role of the registry field (whether it is used for integrity
   verification, version resolution, or purely for tooling metadata) is not fully
   confirmed. Claim 8 is assessed as `emerging` for this reason.

3. **Shared config list may not be exhaustive**: The 17 shared configurations listed in
   Claim 9 are from the documentation's enumeration; the actual directory may contain
   additional entries not shown on this page. Treat the list as representative, not
   definitive.

4. **No publication date**: The documentation does not carry an explicit publication
   date. `date_published` is left null. Content is consistent with current gh-aw
   platform state as of 2026-04-22.

5. **No contradictions to file**: Reviewed all existing source notes. No claims in this
   source materially oppose existing source notes. The read-only MCP policy is consistent
   with the "no write access by default" principle in `docs-ghaw-how-they-work.md`. The
   `allowed:` field is additive to the token-cost guidance in `blog-bswen-mcp-token-cost.md`.

6. **Skipped per Prospector guidance**: The navigation text, site chrome, and CLI
   reference details for `gh aw mcp inspect` / `gh aw mcp list-tools` beyond what is
   captured in the Concrete Artifacts section were de-emphasized. The configuration
   schema examples and safety/auth constraints were the extraction priority.
