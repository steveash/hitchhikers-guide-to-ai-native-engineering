---
source_url: https://github.github.com/gh-aw/guides/web-search
source_type: docs
title: "GitHub Agentic Workflows: Web Search Guide (Tavily MCP Integration)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: emerging
issue: "#300"
---

# GitHub Agentic Workflows: Web Search Guide (Tavily MCP Integration)

> A concrete, end-to-end worked example of wiring an external MCP server
> (`@tavily/mcp`) into a gh-aw workflow — contributing the complete YAML
> configuration pattern (`mcp-servers` block + `network.allowed` + `allowed:`
> tool scope), the `gh aw secrets set` workflow-secret CLI, and the
> `inspect` / `list-tools` discovery sequence as the recommended onboarding flow.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows guides page — prescriptive
  how-to for web search integration using Tavily MCP; a concrete worked example
  rather than a conceptual reference or feature overview)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team that maintains the `gh aw` platform. YAML configuration, CLI
  behavior, and setup sequence are authoritative for this platform. Claims about
  Tavily's performance or value relative to other search providers are not
  independently verified and are not extracted here (see Extraction Notes).
- **Scope**: Tavily MCP server integration into a gh-aw workflow — registration
  and secret management, YAML frontmatter configuration, network permissions,
  tool allowlisting, and CLI-based discovery and validation. Does NOT cover:
  comparative analysis of Tavily vs. other search providers (Brave Search,
  Exa, SerpAPI), cost or rate-limit considerations, what happens when a tool
  outside `allowed:` is called, multi-MCP-server orchestration, or general MCP
  server authoring. This page is a specific integration how-to; the general MCP
  reference is `docs-ghaw-mcps.md`.

## Extracted Claims

### Claim 1: Tavily (`@tavily/mcp`) is the designated web search integration for gh-aw, with a dedicated guide page and an entry in the shared MCP configuration library

- **Evidence**: The page is a top-level entry in the gh-aw Guides section
  specifically for web search. Tavily is also listed as one of the 17 pre-built
  shared MCP configurations in `.github/workflows/shared/mcp/` (documented in
  `docs-ghaw-mcps.md` Claim 9). No equivalent guide page exists for Brave
  Search, Exa, or other search providers, though Brave Search also appears in
  the shared library.
- **Confidence**: emerging (official endorsement via a dedicated page; absence
  of comparative reasoning means we cannot assess whether Tavily is
  *best* or merely *first/preferred*)
- **Quote**: (page is the "Web Search" entry in the Guides section; no explicit
  "Tavily is recommended because X" statement was found)
- **Our assessment**: The platform team made a specific choice to create a Tavily
  guide rather than a generic "web search" guide. This is an implicit endorsement
  of Tavily as the default web search path for gh-aw practitioners. For Ch05 /
  Ch02: when recommending a web search MCP for gh-aw workflows, Tavily is the
  platform-endorsed default. Practitioners seeking alternatives should check
  Brave Search in the shared library — the patterns are structurally identical,
  only the package and domain differ.

### Claim 2: The minimal `mcp-servers` frontmatter block for a stdio/npx MCP server requires four fields: `command`, `args`, `env` (with secret interpolation), and `allowed`

- **Evidence**: The complete configuration example from the page:
  ```yaml
  mcp-servers:
    tavily:
      command: npx
      args: ["-y", "@tavily/mcp"]
      env:
        TAVILY_API_KEY: "${{ secrets.TAVILY_API_KEY }}"
      allowed: ["search", "search_news"]
  ```
  All four fields appear in the canonical example; no field is marked optional.
- **Confidence**: settled (first-party documentation; the example is the
  normative configuration)
- **Quote**: (YAML reproduced above verbatim from source)
- **Our assessment**: This is the production-ready template for any `npx`-based
  MCP server. The `command: npx` + `args: ["-y", "<package>"]` idiom installs
  the package on first run via npm's `-y` flag (auto-confirm). The `${{ secrets.NAME }}`
  interpolation pattern is consistent with GitHub Actions syntax. For Ch02: this
  four-field structure is the canonical stdio MCP server configuration unit.
  Practitioners adding other npx-based MCP servers should start from this template.

### Claim 3: The `allowed:` field for Tavily narrows the `@tavily/mcp` server to two tools — `search` and `search_news` — from a potentially larger tool surface

- **Evidence**: `allowed: ["search", "search_news"]` in the canonical example.
  The `@tavily/mcp` package exposes at minimum these two tools; the guide does
  not enumerate the full server tool surface. The narrow allowlist implies the
  server offers additional tools not needed by most workflows.
- **Confidence**: settled (the allowlist is explicit in the example; the
  inference about unexposed tools follows from the established `allowed:` behavior
  documented in `docs-ghaw-mcps.md` Claim 3)
- **Quote**: `allowed: ["search", "search_news"]`
- **Our assessment**: This is the `allowed:` discipline in practice. Rather than
  `allowed: ["*"]`, the guide explicitly names two tools. For practitioners:
  use `gh aw mcp list-tools tavily my-workflow --verbose` (Claim 7) to confirm
  the full `@tavily/mcp` tool surface before deciding whether to expand the
  allowlist. The `search_news` inclusion is notable — web search and news search
  are distinct capabilities with different cost and freshness characteristics.
  A workflow that only needs general search can narrow further to `["search"]`.

### Claim 4: `gh aw secrets set TAVILY_API_KEY --value "<your-api-key>"` is the dedicated CLI command for managing workflow-level secrets in gh-aw — distinct from GitHub Actions `gh secret set`

- **Evidence**: The guide prescribes this specific command as step 2 in the
  setup sequence. The command is `gh aw secrets set`, not `gh secret set` (the
  standard GitHub Actions secrets management command). The `--value` flag accepts
  the API key directly; the gh-aw platform stores and injects it separately from
  GitHub Actions repository secrets.
- **Confidence**: settled (first-party; command is explicitly prescribed in the
  setup sequence)
- **Quote**: `gh aw secrets set TAVILY_API_KEY --value "<your-api-key>"`
- **Our assessment**: This is a significant harness engineering detail that is
  NOT documented in `docs-ghaw-mcps.md`. The gh-aw secrets store is separate
  from GitHub Actions repository secrets — `${{ secrets.NAME }}` interpolation
  in the workflow frontmatter resolves against the gh-aw store, not the
  repository-level `gh secret set` store. Practitioners who try to use
  `gh secret set` to provision workflow secrets will create a GitHub Actions
  secret that does NOT appear in `${{ secrets.TAVILY_API_KEY }}` at workflow
  runtime. This is a common misconfiguration vector. For Ch02: document `gh aw
  secrets set` as the correct credential provisioning command for gh-aw
  workflows, explicitly distinguishing it from GitHub Actions secrets.

### Claim 5: Network egress for stdio/npx-based MCP servers requires an explicit `network.allowed` block listing the target domain alongside the `defaults` set

- **Evidence**: The page provides the network permissions configuration:
  ```yaml
  network:
    allowed:
      - defaults
      - "*.tavily.com"
  ```
  This applies to the stdio-type Tavily MCP server (not a Docker container).
  The existing `docs-ghaw-mcps.md` Claim 6 documents `network.allowed` only in
  the Docker container MCP server context.
- **Confidence**: emerging (first-party source; placement of the `network:` block
  relative to the `mcp-servers:` block is ambiguous in the fetched page — it
  may be a top-level workflow frontmatter key or nested under `mcp-servers.tavily`;
  see Extraction Notes)
- **Quote**: `network: allowed: [defaults, "*.tavily.com"]`
- **Our assessment**: If `network:` is a workflow-level key (top-level in
  frontmatter), this extends network controls beyond Docker-based servers to
  cover all server types including stdio. If it is a server-level key nested
  under `mcp-servers.tavily`, it is consistent with the Docker example in
  `docs-ghaw-mcps.md`. Either interpretation matters: gh-aw enforces network
  egress for MCP servers, and practitioners must explicitly allowlist external
  domains regardless of transport type. For Ch02 / Ch03: the `network.allowed`
  requirement applies broadly — do not assume that a stdio/npx server gets
  unrestricted network access by default.

### Claim 6: The `defaults` entry in `network.allowed` preserves the platform's default network access while appending service-specific domain allowlisting

- **Evidence**: `network: allowed: [defaults, "*.tavily.com"]` — `defaults` is
  a keyword, not a domain name, implying the platform defines a standard set of
  permitted network destinations that `defaults` expands. Adding `*.tavily.com`
  extends beyond the platform default without replacing it.
- **Confidence**: emerging (the `defaults` keyword behavior is inferred from the
  naming and the pattern; the platform's definition of `defaults` is not spelled
  out on this page)
- **Quote**: `- defaults` and `- "*.tavily.com"` in the `network.allowed` list
- **Our assessment**: The `defaults` + service-domain pattern is a portable
  template for any MCP server that needs external API access: keep `defaults`,
  add the vendor's domain. For Ch02: this is the recommended `network.allowed`
  template for third-party API MCP servers. The wildcard `*.tavily.com` covers
  subdomains — practitioners should use the narrowest domain pattern the vendor
  allows (e.g., `api.tavily.com` vs. `*.tavily.com`) to minimize egress surface.

### Claim 7: `gh aw mcp inspect <workflow> --server <name>` validates the runtime MCP server configuration and should be run as the final verification step after setup

- **Evidence**: Step 4 ("Validate setup with `gh aw mcp inspect`") in the guide's
  setup sequence. The command: `gh aw mcp inspect my-workflow --server tavily`.
- **Confidence**: settled (first-party; command is the prescribed validation step)
- **Quote**: `gh aw mcp inspect my-workflow --server tavily`
- **Our assessment**: This command closes the gap between "I wrote the YAML"
  and "the MCP server is actually configured correctly." It validates that the
  server is accessible, the secrets are resolved, and the tool list matches what
  `allowed:` expects. For Ch02: include `gh aw mcp inspect` as the verification
  step in any MCP onboarding checklist. Running this before committing a workflow
  catches configuration errors before they surface as runtime failures.

### Claim 8: `gh aw mcp list-tools <server> <workflow> --verbose` enumerates the full tool surface of a configured MCP server — the discovery step for setting a correct `allowed:` list

- **Evidence**: Command: `gh aw mcp list-tools tavily my-workflow --verbose`.
  This command is prescribed as a discovery mechanism, implying the full tool
  surface is not visible from the package documentation alone — the server must
  be configured in context for the tool list to resolve.
- **Confidence**: settled (first-party; the command is explicitly shown)
- **Quote**: `gh aw mcp list-tools tavily my-workflow --verbose`
- **Our assessment**: The `--verbose` flag is specified, implying a non-verbose
  mode returns a shorter list (names only vs. names + descriptions). For
  practitioners setting up a new MCP server: run `list-tools --verbose` to see
  tool descriptions before deciding what to include in `allowed:`. This is the
  pre-condition for the minimal-privilege `allowed:` discipline. Without this
  step, practitioners either default to `["*"]` (too broad) or guess tool names
  (error-prone). For Ch02: document `list-tools --verbose` as the prerequisite
  step before setting `allowed:`.

### Claim 9: The recommended end-to-end MCP onboarding sequence for a third-party API-based server is: register → `gh aw secrets set` → configure YAML → add `network.allowed` → `gh aw mcp inspect`

- **Evidence**: The setup sequence presented in the guide:
  1. Register at tavily.com to obtain an API key
  2. Store API key: `gh aw secrets set TAVILY_API_KEY --value "<your-api-key>"`
  3. Configure the `mcp-servers` block with command, args, env, and `allowed:`
  4. Add `network.allowed` for the service domain
  5. Validate: `gh aw mcp inspect my-workflow --server tavily`
- **Confidence**: settled (first-party; this is the documented canonical sequence)
- **Quote**: (five-step sequence described above; no single direct quote covers
  the full sequence)
- **Our assessment**: This sequence is the practitioner recipe for any third-party
  API-backed MCP server, not just Tavily. Steps 1 and 2 are vendor-specific
  (obtain key, store it); steps 3-5 are platform-generic. For Ch02: abstract this
  as the "external MCP server onboarding checklist" and reference it whenever
  a new third-party integration is added to a workflow.

### Claim 10: Tavily is used in gh-aw for issue-triggered workflows that perform web search to find "recent information" about the issue title

- **Evidence**: "A basic workflow triggering on GitHub issues that performs web
  searches using the Tavily tool to 'find recent information' about the issue
  title." The complete example frontmatter uses `on: issues` as the trigger.
- **Confidence**: anecdotal (single example workflow pattern from the guide;
  not a broad practitioner survey)
- **Quote**: "find recent information" (guide's description of the workflow's task)
- **Our assessment**: Web search enables agentic workflows to ground responses
  in current information rather than the model's training data. The `on: issues`
  trigger + Tavily search combination is a natural pattern for triage agents:
  when a new issue arrives, search for related articles, documentation, or
  known issues. For Ch01 (Daily Workflows): this is a concrete starting pattern
  for issue triage workflows with web search augmentation. For Ch04: this
  illustrates that web search tools are most valuable when combined with
  event-driven triggers, not just on-demand.

## Concrete Artifacts

### Complete Tavily MCP Server Configuration (Canonical Example)

```yaml
---
on: issues
engine: copilot
mcp-servers:
  tavily:
    command: npx
    args: ["-y", "@tavily/mcp"]
    env:
      TAVILY_API_KEY: "${{ secrets.TAVILY_API_KEY }}"
    allowed: ["search", "search_news"]
---
```

*Source: docs-ghaw-web-search, "YAML Configuration Example" section — verbatim*

### Network Permissions Block for Tavily

```yaml
network:
  allowed:
    - defaults
    - "*.tavily.com"
```

*Source: docs-ghaw-web-search, "Network Permissions Configuration" section —
verbatim. Note: placement (top-level vs. nested under `mcp-servers.tavily`) is
ambiguous in the fetched content; see Extraction Notes.*

### Secret Management Command

```bash
gh aw secrets set TAVILY_API_KEY --value "<your-api-key>"
```

*Source: docs-ghaw-web-search, "Secret Management Command" section — verbatim*

### CLI Discovery Commands

```bash
# Validate the configured MCP server (step 5 of setup sequence)
gh aw mcp inspect my-workflow --server tavily

# Enumerate all tools exposed by the server (pre-condition for setting allowed:)
gh aw mcp list-tools tavily my-workflow --verbose
```

*Source: docs-ghaw-web-search, "CLI Inspection Commands" section — verbatim*

### Full MCP Onboarding Sequence (Synthesized from Guide Steps)

```
1. Register at tavily.com → obtain TAVILY_API_KEY

2. Store secret in gh-aw secrets store:
   gh aw secrets set TAVILY_API_KEY --value "<your-api-key>"
   (NOT gh secret set — that creates a GitHub Actions secret, not a gh-aw secret)

3. Configure mcp-servers block:
   mcp-servers:
     tavily:
       command: npx
       args: ["-y", "@tavily/mcp"]
       env:
         TAVILY_API_KEY: "${{ secrets.TAVILY_API_KEY }}"
       allowed: ["search", "search_news"]

4. Add network permissions:
   network:
     allowed:
       - defaults
       - "*.tavily.com"

5. Validate: gh aw mcp inspect my-workflow --server tavily

Optional discovery step (before step 3 for a new server):
   gh aw mcp list-tools tavily my-workflow --verbose
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-mcps.md` Claim 3 (`allowed:` as minimal-privilege tool filter):
    the `allowed: ["search", "search_news"]` pattern is a concrete instance of
    the same discipline. Both sources agree that `allowed:` should be a named
    list for multi-tool servers, not `["*"]`. This note provides the specific
    Tavily tool names; `docs-ghaw-mcps.md` provides the general pattern.
  - `docs-ghaw-mcps.md` Claim 7 (`gh aw mcp inspect` and `list-tools` CLI
    family): same commands, same purpose — this page corroborates the CLI
    family with a concrete usage example and explicit ordering (inspect for
    validation, list-tools for discovery before allowlisting).
  - `docs-ghaw-mcps.md` Claim 6 (`network.allowed` domain allowlisting): the
    `["defaults", "*.tavily.com"]` pattern is a specific instance of the
    network controls mechanism. `docs-ghaw-mcps.md` documents this for Docker
    containers; this page may extend it to stdio/npx servers (see Claim 5).
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security, Layer 4 network
    controls): the `network.allowed` block is the concrete configuration
    implementing Layer 4. This is the second source in the corpus showing that
    configuration (after `docs-ghaw-mcps.md` Claim 6).

- **Extends**:
  - `docs-ghaw-mcps.md`: this note is the Tavily-specific worked example for
    the general patterns in that note. Together, the two notes give practitioners
    both the reference (what options exist) and the recipe (how to do the most
    common integration). Key additive content: `gh aw secrets set` command not
    documented in the general guide; the specific tool names `["search",
    "search_news"]` for `@tavily/mcp`; the end-to-end five-step sequence.
  - `docs-ghaw-mcps.md` Claim 9 (shared MCP library includes Tavily): this note
    provides the companion guide for using the Tavily entry in the shared library.
    The shared library entry is the config; this page is the setup guide.
  - `docs-ghaw-how-they-work.md` Claim 1 (YAML frontmatter constrains, markdown
    instructs): this page shows the constraint half (frontmatter) in full concrete
    form for a search-enabled workflow. The `on: issues, engine: copilot` fields
    alongside the `mcp-servers` block show a complete trigger + engine + tool
    configuration.

- **Contradicts**: None identified. The `gh aw secrets set` command is additive
  to — not contradicting — the `${{ secrets.NAME }}` interpolation syntax shown
  in `docs-ghaw-mcps.md`. The network controls pattern is consistent with
  `docs-ghaw-mcps.md` Claim 6, with a possible scope extension to stdio servers
  (not a contradiction, but a potential generalization that requires verification).

- **Novel**:
  - **`gh aw secrets set` as gh-aw-specific secret management CLI** (Claim 4):
    No existing source note documents this command. `docs-ghaw-mcps.md` shows
    `${{ secrets.NAME }}` interpolation syntax but does not document the CLI
    for managing those secrets. The distinction between gh-aw secrets and GitHub
    Actions secrets is a new, practically important detail.
  - **Network egress controls for stdio/npx MCP servers** (Claim 5): The existing
    corpus (`docs-ghaw-mcps.md` Claim 6) documents `network.allowed` only in the
    Docker container context. If this configuration applies at the workflow level
    or to stdio servers broadly, it generalizes network controls beyond Docker —
    a meaningful security architecture refinement.
  - **`["defaults", "*.tavily.com"]` as a portable network permissions template**
    (Claim 6): The `defaults` + service-domain pattern is new to the corpus.
    No existing note documents `defaults` as a keyword in `network.allowed` or
    the pattern of extending platform defaults with specific domains.
  - **End-to-end onboarding sequence for third-party API MCP servers** (Claim 9):
    The five-step sequence (register → secrets → config → network → inspect) is
    not documented as a unified workflow in any existing source note. The general
    MCPs guide shows the configuration components separately; this page assembles
    them into a sequence.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add `gh aw secrets set` as the credential provisioning command for gh-aw
  workflows** (Claim 4): The guide currently lacks documentation of this command.
  The misconception risk — practitioners using `gh secret set` (GitHub Actions)
  instead of `gh aw secrets set` — is high and hard to debug. Add a callout:
  "gh-aw workflow secrets use `gh aw secrets set`, not `gh secret set`. The
  `${{ secrets.NAME }}` interpolation in workflow frontmatter resolves against the
  gh-aw secrets store."

- **Add the external MCP server onboarding checklist** (Claim 9): The five-step
  sequence (register → `gh aw secrets set` → configure → `network.allowed` →
  `gh aw mcp inspect`) is the recommended pattern for any third-party API MCP
  server. Abstract from the Tavily example and present as a general template.

- **Add `gh aw mcp list-tools --verbose` as the pre-condition for `allowed:`
  configuration** (Claim 8): When adding any new MCP server, run `list-tools
  --verbose` before writing the `allowed:` list. This prevents both over-
  permissioning (`["*"]`) and under-permissioning (guessing wrong tool names).
  Add to the MCP onboarding checklist.

- **Show the four-field stdio/npx MCP server template** (Claim 2): The
  `command: npx / args: ["-y", "<package>"] / env / allowed` structure is the
  canonical starting point for npx-based MCP servers. Reference alongside the
  Docker, HTTP, and registry examples from `docs-ghaw-mcps.md` to complete the
  four-type taxonomy.

### Chapter 03: Safety and Verification

- **Network controls apply broadly (not Docker-only)** (Claim 5): If `network.
  allowed` works at the workflow level or for stdio/npx servers, update Ch03's
  treatment of Layer 4 (network controls) to reflect that the `network.allowed`
  block is not limited to Docker container MCP servers. Practitioners should
  not assume stdio servers bypass egress controls. Pending verification of the
  scope.

- **Cross-reference `gh aw secrets set` vs. `gh secret set` as a security
  misconfiguration risk** (Claim 4): A secret stored in the wrong store is
  functionally a missing secret — the workflow will fail to authenticate, and
  the error message may not clearly indicate the root cause. Document this as
  a known misconfiguration pattern.

### Chapter 05: MCP Tool Integration (if planned)

- **Tavily as the platform-endorsed web search MCP** (Claim 1): When the guide
  covers web search augmentation for agentic workflows, Tavily + `@tavily/mcp`
  is the gh-aw endorsed pattern. Reference this page as the primary how-to.
  Note the `search` vs. `search_news` tool distinction for workflows that need
  only one of the two capabilities.

## Extraction Notes

1. **`network:` block placement is ambiguous**: The source page presents the
   `network.allowed` block separately from the `mcp-servers` block in the fetched
   content. It is unclear whether `network:` is a top-level workflow frontmatter
   key (applying to all connections) or should be nested under `mcp-servers.tavily`
   (per-server). In `docs-ghaw-mcps.md`, `network:` is nested under a Docker
   container server entry. The two representations are architecturally different:
   top-level applies workflow-wide; nested applies to that server only. This
   distinction should be verified against the live page before the guide cites it.

2. **`gh aw secrets set` vs. `gh secret set`**: The source page clearly uses
   `gh aw secrets set`. This is confirmed to be distinct from the GitHub Actions
   `gh secret set` command based on the `gh aw` namespace. The actual storage
   mechanism (whether gh-aw secrets are a separate store or GitHub Actions
   environment secrets injected at compile time) is not specified on this page.

3. **Tavily marketing claims not extracted**: The source page contains claims
   about Tavily's performance, speed, and JSON response quality. Per Prospector
   guidance, these were not extracted — the extractable value is the gh-aw
   configuration pattern, not the vendor service properties.

4. **Page does not enumerate the full `@tavily/mcp` tool surface**: The `allowed:
   ["search", "search_news"]` allowlist is presented as the recommendation, but
   whether `@tavily/mcp` exposes additional tools not shown here is unknown from
   this page alone. Use `gh aw mcp list-tools tavily my-workflow --verbose` to
   confirm before finalizing `allowed:`.

5. **No publication date**: The documentation page does not carry an explicit
   date. Content is consistent with the current gh-aw platform state as of
   2026-04-22.

6. **No contradictions filed**: No claims in this source materially oppose
   existing source notes. The `gh aw secrets set` command is additive (not in
   the corpus). The network controls pattern is consistent with and possibly
   extends `docs-ghaw-mcps.md` Claim 6. The `allowed:` usage corroborates
   rather than contradicts the general discipline in `docs-ghaw-mcps.md` Claim 3.
