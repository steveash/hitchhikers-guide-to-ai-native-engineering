---
source_url: https://github.github.com/gh-aw/troubleshooting/debug-ghe
source_type: docs
title: "GitHub Agentic Workflows: Debugging GHE Cloud with Data Residency"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#426"
---

# GitHub Agentic Workflows: Debugging GHE Cloud with Data Residency

> Step-by-step setup and troubleshooting guide for deploying gh-aw on GitHub
> Enterprise Cloud (*.ghe.com) with data residency — the first corpus source
> specifically addressing GHE Cloud as a distinct deployment context, distinct
> from both github.com (existing corpus) and GHES/on-premise (Claim 12 of
> `docs-ghaw-troubleshooting-common-issues.md`).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `troubleshooting/debug-ghe`
  page — in the `troubleshooting/` section alongside `common-issues` and
  `debugging`. This page is specific to GHE Cloud with data residency; it is
  a practitioner how-to with both setup steps and a troubleshooting catalogue,
  distinct from the methodology-focused `troubleshooting/debugging` page.)
- **Author credibility**: First-party from GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  agent factory series and the `gh aw` CLI). GHE-specific configuration
  values, error messages, and domain tables are authoritative for this
  deployment context.
- **Scope**: Covers GHE Cloud with data residency deployment specifically
  (instances at `yourorg.ghe.com`) — init, workflow creation, the critical
  `engine.api-target` configuration, compilation, dispatch, Copilot CLI local
  debugging, three named common errors, two advanced diagnostic techniques
  (runner-level Copilot test; HTTP traffic capture via UNDICI_DEBUG), and a
  required-domains reference table. Does NOT cover: GHES on-premise (see
  `docs-ghaw-troubleshooting-common-issues.md` Claim 12), general
  troubleshooting methodology (see `docs-ghaw-troubleshooting-debugging.md`),
  or network configuration reference (see `docs-ghaw-network-reference.md`).

## Extracted Claims

### Claim 1: On GHE Cloud with data residency, setting `api-target` in the workflow's `engine:` frontmatter block is the single most important configuration difference from github.com — without it, authentication failures result

- **Evidence**: The page opens with an explicit callout elevating this as
  the single critical delta from standard github.com setup. The causal
  mechanism is documented: the AWF api-proxy routes Copilot requests to
  the wrong endpoint without this setting.
- **Confidence**: settled (first-party; the configuration requirement and
  its causal mechanism are explicitly documented with an authoritative note)
- **Quote**: "The one thing you must do differently from github.com is set
  `api-target` in your workflow frontmatter to `copilot-api.<yourorg>.ghe.com`.
  Everything else flows from that."
- **Our assessment**: This is the highest-priority claim in the source.
  Teams that copy a working github.com workflow to a GHE Cloud instance
  will have no visible compile error — the compiler does not catch the
  missing `api-target` at validation time — but every run will fail with
  an authentication error at inference time. The page's framing ("The one
  thing...") signals this is the most common failure point for GHE onboarding.
  For Ch02 (Harness Engineering): document `api-target` as a required
  frontmatter field for GHE Cloud deployments, with a note that its absence
  is not a compile error but causes runtime authentication failures.

### Claim 2: The correct `api-target` value for GHE Cloud with data residency is `copilot-api.yourorg.ghe.com` — the dedicated Copilot inference subdomain of the GHE instance, not the default `api.githubcopilot.com`

- **Evidence**: Configuration snippet is explicit. The "Why this is required"
  section documents the routing mechanism: GHE Cloud data residency runs
  Copilot inference on a tenant-specific subdomain rather than the shared
  global endpoint.
- **Confidence**: settled (first-party; the configuration value and its
  rationale are authoritative)
- **Quote**: "On GHE Cloud with data residency, Copilot inference runs on
  a dedicated subdomain (`copilot-api.yourorg.ghe.com`) rather than the
  default `api.githubcopilot.com`. Without `api-target`, the AWF api-proxy
  routes requests to the wrong host, resulting in authentication failures."
- **Our assessment**: The subdomain routing requirement is a data residency
  constraint — inference requests must stay within the tenant's data boundary.
  The `yourorg` portion is the enterprise slug (the subdomain of `yourorg.ghe.com`).
  This is architecturally distinct from the GHES api-target documented in
  `docs-ghaw-troubleshooting-common-issues.md` Claim 12 (`api.enterprise.githubcopilot.com`)
  — GHES is on-premise; GHE Cloud with data residency is a separate product
  with tenant-specific inference subdomains. For Ch02: include the GHE Cloud
  api-target value alongside the GHES value as two separate enterprise deployment
  contexts requiring different configuration.

### Claim 3: All `gh aw` CLI operations against a GHE Cloud instance require the `GH_HOST=yourorg.ghe.com` environment variable prefix — the CLI does not auto-detect GHE instances

- **Evidence**: Every command in the setup procedure is prefixed with
  `GH_HOST=yourorg.ghe.com`. The common error "none of the git remotes point
  to a known GitHub host" is documented as caused specifically by `GH_HOST`
  not being set.
- **Confidence**: settled (first-party; every documented command carries this
  prefix, and its absence is the explicit cause of a named error)
- **Quote**: (no direct quote; see paraphrase in Our assessment — the prefix
  appears on every CLI command in the setup steps and its absence is named
  as an error cause)
- **Our assessment**: `GH_HOST` is the environment-level signal that tells the
  `gh` CLI which GitHub host to target. Without it, the CLI defaults to
  `github.com` authentication and repository resolution, which fails for
  `yourorg.ghe.com` repositories. This applies to all `gh aw` subcommands:
  `init`, `add-wizard`, `compile`, `workflow run`. Practitioners migrating from
  github.com workflows will not encounter this requirement and are likely to
  forget it. For Ch02: document `GH_HOST=yourorg.ghe.com` as a required prefix
  for all `gh aw` CLI operations in GHE Cloud deployments, and recommend
  adding it to the team's shell profile or `.envrc` for GHE-specific dev environments.

### Claim 4: The `gh aw` compiler (v0.61.1 or later) automatically configures three GHE-specific settings when `api-target` is set — adding GHE domains to the firewall allow-list, setting `--copilot-api-target` for the api-proxy, and configuring `GH_HOST` for the `gh` CLI in the runner

- **Evidence**: The "Step 4: Compile" section documents the three automatic
  behaviors of v0.61.1+ compilation with an explicit version boundary. The
  minimum version requirement (`gh aw` v0.61.1+) is stated in the prerequisites.
- **Confidence**: settled (first-party; the version boundary and three auto-configurations
  are explicitly enumerated)
- **Quote**: "The compiler (v0.61.1+) will automatically: Add your GHE domains
  (`api.yourorg.ghe.com`, `copilot-api.yourorg.ghe.com`) to the firewall
  allow-list; Set `--copilot-api-target` for the AWF api-proxy; Configure
  `GH_HOST` so the `gh` CLI targets the correct host"
- **Our assessment**: The v0.61.1 version boundary is a critical prerequisite
  check. Teams running an older `gh aw` version will need to manually configure
  all three settings that newer versions handle automatically. The auto-addition
  of GHE domains to the AWF firewall allow-list is particularly significant:
  it means practitioners do not need to manually enumerate GHE domains in
  `network.allowed` — the compiler derives them from `api-target`. This is
  analogous to ecosystem identifiers (e.g., `node`, `python`) automatically
  expanding to domain sets. For Ch02: document v0.61.1+ as the minimum version
  for GHE Cloud deployment and add `gh extension upgrade gh-aw` as the
  resolution for version-related GHE configuration failures. For Ch05 (Team
  Adoption): version pinning for the `gh aw` extension is important for GHE
  deployments since the auto-configuration behavior is version-dependent.

### Claim 5: The "Authentication failed" error on GHE Cloud is caused by missing or incorrect `api-target` in the engine frontmatter, causing the api-proxy to route Copilot requests to the wrong endpoint

- **Evidence**: The error message and its cause are explicitly documented in
  the "Common Errors" section with a concrete fix procedure.
- **Confidence**: settled (first-party; the error message, cause, and fix are
  authoritative)
- **Quote**: "Error: Authentication failed / Your GitHub token may be invalid,
  expired, or lacking the required permissions."
- **Our assessment**: The error message text is misleading — it suggests a token
  validity problem, but on GHE Cloud the actual cause is almost always incorrect
  routing (wrong `api-target`), not an invalid token. Practitioners who see this
  error and follow standard token troubleshooting steps (refresh token, check
  permissions via `gh auth status`) will not resolve it — the fix is verifying
  and correcting `api-target` in the frontmatter, then recompiling. For Ch02:
  document this as a GHE-specific error disambiguation: "Authentication failed"
  on GHE Cloud means "check `api-target` first, not the token."

### Claim 6: The "none of the git remotes point to a known GitHub host" error occurs when `GH_HOST` is not set — fixed by upgrading to v0.61.1+ and recompiling rather than setting `GH_HOST` manually in the lock file

- **Evidence**: The error is documented with its cause (`GH_HOST` not set)
  and the preferred fix (upgrade + recompile, not manual lock file editing).
- **Confidence**: settled (first-party; the error, cause, and recommended
  resolution path are documented)
- **Quote**: "`GH_HOST` is not set. The `gh` CLI doesn't recognize your GHE
  instance as a GitHub host."
- **Our assessment**: The recommended fix (upgrade + recompile) is significant —
  it implies that manually setting `GH_HOST` in the lock file is a pattern to
  avoid. The compiled lock file (`.lock.yml`) should be generated by the compiler,
  not edited directly. This is consistent with the compilation model in
  `docs-ghaw-compilation-process.md` where the lock file is a generated artifact.
  For Ch02: document "upgrade + recompile" as the resolution path for `GH_HOST`
  errors rather than manual lock file editing, which would be fragile and reset
  on the next compilation.

### Claim 7: The "Not Found" during checkout steps error occurs when using a locally built compiler binary instead of the published `gh aw` extension — the local binary uses `actions/checkout` instead of `github/gh-aw-actions`, causing token scope mismatch

- **Evidence**: The error cause is documented precisely: local builds use a
  different checkout action, and the GHE-scoped token fails to access
  `github.com`-hosted action repositories.
- **Confidence**: settled (first-party; the root cause is explicitly named)
- **Quote**: "The lock file is trying to access `github.com` repositories with
  your GHE-scoped token. This can happen with local builds of the compiler that
  use `actions/checkout` instead of the published `github/gh-aw-actions` action
  reference."
- **Our assessment**: This is a developer-facing error that primarily affects
  team members building or testing local modifications to the `gh aw` toolchain.
  The published `github/gh-aw-actions` action is designed to handle GHE token
  scoping correctly; `actions/checkout` (used in local builds) is not. The fix —
  "always compile with the installed `gh aw` extension rather than a local binary"
  — is a strong recommendation to treat the extension as a black box rather than
  a patchable local tool. For Ch02: document this as a developer-only pitfall
  (not a production deployment issue) and add it to the GHE troubleshooting
  checklist for teams running custom compiler builds.

### Claim 8: Local Copilot CLI debugging against GHE Cloud requires `GH_HOST=yourorg.ghe.com copilot` to authenticate with the GHE instance, followed by the standard `/agent` + `agentic-workflows` agent selection and failing run URL

- **Evidence**: The "Debugging with Copilot CLI Locally" section documents
  an explicit four-step procedure with the `GH_HOST`-prefixed `copilot` command,
  then the `/agent agentic-workflows` selector, then a workflow run prompt.
- **Confidence**: settled (first-party; the `GH_HOST` prefix requirement is
  the GHE-specific delta from the standard three-step Copilot CLI debugging
  workflow)
- **Quote**: (no direct quote; see procedure in Concrete Artifacts)
- **Our assessment**: This is the GHE-specific extension of the three-step
  Copilot CLI debugging workflow documented in `docs-ghaw-troubleshooting-debugging.md`
  Claims 1–3. The only addition is the `GH_HOST` prefix on the initial `copilot`
  invocation. Once authenticated, the `/agent agentic-workflows` selector and
  workflow run prompt are identical to the standard flow. For Ch02 and Ch05:
  document the `GH_HOST`-prefixed Copilot CLI invocation as the GHE-specific
  entry point for the AI-assisted debugging workflow, referencing
  `docs-ghaw-troubleshooting-debugging.md` Claims 1–3 for the subsequent steps.

### Claim 9: HTTP traffic capture from the Copilot CLI on GHE Cloud requires `UNDICI_DEBUG=full` (not `NODE_DEBUG=http,https`) because the CLI uses Node.js `fetch()`/`undici` internally rather than the built-in `http`/`https` modules

- **Evidence**: The "Advanced: Capturing HTTP Traffic" section explicitly
  documents the incorrect approach (`NODE_DEBUG=http,https`) and the correct
  approach (`UNDICI_DEBUG=full`) with an explanation of why the standard
  approach fails.
- **Confidence**: settled (first-party; the internal implementation detail —
  undici as the HTTP client — and the resulting diagnosis requirement are
  authoritatively documented)
- **Quote**: "The Copilot CLI uses Node.js `fetch()`/`undici` internally, not
  the built-in `http`/`https` modules. Setting `NODE_DEBUG=http,https` will
  capture nothing. You must use `UNDICI_DEBUG=full`."
- **Our assessment**: This is a highly specific diagnostic fact with no
  alternative. Practitioners who know HTTP traffic capture patterns from
  other Node.js tools will naturally reach for `NODE_DEBUG=http,https` — which
  silently produces no output with the Copilot CLI. The `UNDICI_DEBUG=full`
  requirement is a non-obvious implementation detail. Combined with
  `NODE_DEBUG: fetch,undici`, it reveals the four domains the CLI contacts
  on GHE Cloud data residency. For Ch02 and Ch05: document `UNDICI_DEBUG=full`
  as the correct traffic capture mechanism for the Copilot CLI, and note that
  `NODE_DEBUG=http,https` is a common but ineffective alternative for this
  specific tool.

### Claim 10: GHE Cloud with data residency involves four distinct Copilot domains — `api.yourorg.ghe.com` (REST API, Copilot auth), `copilot-api.yourorg.ghe.com` (inference, models, MCP), `copilot-telemetry-service.yourorg.ghe.com` (telemetry), and `api.githubcopilot.com` (shared Copilot services)

- **Evidence**: The HTTP traffic capture section documents the four domains
  in a table with their purposes, extracted from live traffic analysis.
- **Confidence**: emerging (first-party; derived from traffic capture — the
  domain list is empirically observed rather than formally specified, so
  changes in the Copilot CLI implementation could alter it)
- **Quote**: (no direct quote; see domain table in Concrete Artifacts)
- **Our assessment**: The four-domain table is the most operationally specific
  finding in the source — it tells practitioners exactly which domains to
  allow in their corporate proxy/firewall configuration for GHE Cloud data
  residency deployments. The continued presence of `api.githubcopilot.com`
  (a non-GHE shared domain) is notable: even data-residency deployments
  reach the shared Copilot endpoint for some operations. For Ch02 and Ch05:
  document the four-domain table as the network requirements for GHE Cloud
  data residency. For teams with corporate proxy requirements that exceed
  the AWF sandbox's domain control, these are the four domains to allowlist
  at the infrastructure level.

### Claim 11: The `copilot-telemetry-service.yourorg.ghe.com` domain is NOT automatically added by the compiler — teams that need telemetry must manually add it to `network.allowed`

- **Evidence**: The "Required Domains Reference" table has an "Auto-added by
  compiler?" column; the telemetry domain is the only row with ✗ (not
  auto-added), and an explicit note says to add it manually if needed.
- **Confidence**: settled (first-party; the table is an authoritative reference
  for which domains are compiler-managed vs. manually required)
- **Quote**: (no direct quote; see domain table in Concrete Artifacts)
- **Our assessment**: The compiler auto-adds `yourorg.ghe.com`,
  `api.yourorg.ghe.com`, and `copilot-api.yourorg.ghe.com` but not the telemetry
  domain. Teams that suppress telemetry may not notice its absence. Teams that
  need telemetry data (for usage reporting, compliance, or license management)
  will need to add it explicitly. The manual addition uses the standard
  `network.allowed` pattern, extending the compiler's auto-configuration with
  one additional domain. For Ch02: document the telemetry domain as the only
  GHE-specific domain not handled automatically — present the manual addition
  YAML as the configuration pattern for teams that need it.

### Claim 12: A temporary diagnostic step before the Execute step in the lock file can isolate whether Copilot auth works on the Actions runner outside the AWF sandbox — success in the diagnostic step but failure in the Execute step points to firewall or api-proxy configuration, not Copilot auth

- **Evidence**: The "Advanced: Testing Copilot on the Runner Directly" section
  documents a concrete diagnostic step YAML with `GH_HOST`, `GH_TOKEN`, and
  a direct `copilot --prompt "Say hello" --log-level all` invocation, along
  with the interpretation rule for the results.
- **Confidence**: settled (first-party; the diagnostic step and its interpretation
  are explicitly documented)
- **Quote**: "If this step succeeds but the Execute step fails, the problem is
  in the firewall or api-proxy configuration, not in Copilot auth."
- **Our assessment**: This diagnostic technique isolates one of the most
  ambiguous failure modes in GHE Cloud deployments: "Authentication failed"
  errors that could originate from (a) the token being invalid, (b) the
  api-proxy routing to the wrong endpoint, or (c) the AWF firewall blocking
  the Copilot endpoint. The diagnostic step runs Copilot *outside* the AWF
  sandbox (before the Execute step), so success proves the token and Copilot
  auth are functional — narrowing the failure to the sandbox layer. This is
  the GHE-specific extension of the local Copilot inference test in
  `docs-ghaw-troubleshooting-common-issues.md` Claim 11, applied at the
  runner level rather than the local dev machine level. For Ch02: document
  this runner-level diagnostic step as the authoritative technique for
  isolating auth failures from sandbox configuration failures in GHE Cloud
  deployments.

## Concrete Artifacts

### Step-by-Step GHE Cloud Setup (verbatim from source)

```bash
# Step 1: Initialize the repository
GH_HOST=yourorg.ghe.com gh aw init

# Step 2: Add a workflow
GH_HOST=yourorg.ghe.com gh aw add-wizard githubnext/agentics/repo-assist

# Step 3: Configure the engine for GHE (critical)
# Open the generated .md file and ensure the frontmatter contains:
```

```yaml
engine:
  id: "copilot"
  api-target: "copilot-api.yourorg.ghe.com"
```

```bash
# Step 4: Compile (v0.61.1+ auto-adds GHE domains to firewall allow-list)
GH_HOST=yourorg.ghe.com gh aw compile repo-assist

# Step 5: Commit, push, and run
git add .github/workflows/repo-assist.md .github/workflows/repo-assist.lock.yml
git commit -m "Add repo-assist agentic workflow"
git push
GH_HOST=yourorg.ghe.com gh workflow run repo-assist.lock.yml --ref main
```

*Source: `https://github.github.com/gh-aw/troubleshooting/debug-ghe` — Setup Steps section*

### Common Errors Reference (GHE Cloud specific)

```
Error: "Authentication failed"
  Text:  "Your GitHub token may be invalid, expired, or lacking the required
          permissions."
  Cause: `api-target` missing or incorrect — api-proxy routing Copilot
         requests to the wrong endpoint.
  Fix:   Verify frontmatter contains:
           engine:
             id: "copilot"
             api-target: "copilot-api.yourorg.ghe.com"
         Then recompile: GH_HOST=yourorg.ghe.com gh aw compile

Error: "none of the git remotes point to a known GitHub host"
  Cause: GH_HOST is not set. gh CLI does not recognize the GHE instance.
  Fix:   Upgrade to gh aw v0.61.1+ and recompile. Compiler auto-configures
         GH_HOST for GHE instances.

Error: "Not Found" during checkout steps
  Cause: Lock file attempting to access github.com repos with GHE-scoped
         token. Occurs with local compiler builds using actions/checkout
         instead of published github/gh-aw-actions.
  Fix:   Always compile with the installed gh aw extension, not a local binary:
         GH_HOST=yourorg.ghe.com gh aw compile <workflow-name>
```

*Source: `https://github.github.com/gh-aw/troubleshooting/debug-ghe` — Common Errors section*

### Local Copilot CLI Debugging on GHE Cloud

```bash
# Step 1: Verify authentication
GH_HOST=yourorg.ghe.com gh auth status

# Step 2: Launch Copilot CLI (note: GH_HOST prefix required for GHE)
GH_HOST=yourorg.ghe.com copilot

# Step 3: Load the agentic-workflows debugging agent
/agent
# → Select "agentic-workflows" from the list

# Step 4: Ask Copilot to run and debug the workflow
# Example prompt:
# Run the repo-assist workflow and check if it succeeds.
# If it fails, help me debug the failure.
```

*Source: `https://github.github.com/gh-aw/troubleshooting/debug-ghe` — Debugging with Copilot CLI Locally section*

### HTTP Traffic Capture for GHE Cloud (UNDICI required)

```yaml
# Add to the Execute step's env block to capture Copilot CLI HTTP traffic:
env:
  NODE_DEBUG: fetch,undici
  UNDICI_DEBUG: full
```

```
NOTE: NODE_DEBUG=http,https captures NOTHING for the Copilot CLI.
      The CLI uses Node.js fetch()/undici internally, not http/https modules.
      You MUST use UNDICI_DEBUG=full.
```

*Source: `https://github.github.com/gh-aw/troubleshooting/debug-ghe` — Advanced: Capturing HTTP Traffic section*

### GHE Cloud Data Residency: Four Copilot Domains

```
Domain                                      | Purpose
--------------------------------------------|---------------------------------------
api.yourorg.ghe.com                         | REST API, Copilot auth
                                            | (/copilot_internal/user)
copilot-api.yourorg.ghe.com                 | Inference, model listing, MCP
copilot-telemetry-service.yourorg.ghe.com   | Telemetry
api.githubcopilot.com                       | Shared Copilot services
```

*Source: `https://github.github.com/gh-aw/troubleshooting/debug-ghe` — Advanced: Capturing HTTP Traffic section (from traffic analysis)*

### Required Domains Reference Table

```
Domain                                          | Auto-added   | Required for
                                                | by compiler? |
------------------------------------------------|--------------|------------------
yourorg.ghe.com                                 |      ✓       | Git, web UI
api.yourorg.ghe.com                             |      ✓       | REST API,
                                                |              | Copilot auth
copilot-api.yourorg.ghe.com                     |      ✓       | Inference,
                                                |              | models, MCP
copilot-telemetry-service.yourorg.ghe.com       |      ✗       | Telemetry
                                                |  (add manually if needed)
```

Manual addition for telemetry domain:
```yaml
network:
  allowed:
    - defaults
    - copilot-telemetry-service.yourorg.ghe.com
```

*Source: `https://github.github.com/gh-aw/troubleshooting/debug-ghe` — Required Domains Reference section*

### Runner-Level Diagnostic Step (isolates auth vs. firewall failures)

```yaml
- name: Test Copilot CLI directly
  env:
    GH_HOST: yourorg.ghe.com
    GH_TOKEN: ${{ github.token }}
  run: |
    echo "GH_HOST=$GH_HOST"
    echo "GITHUB_SERVER_URL=$GITHUB_SERVER_URL"
    /usr/local/bin/copilot --version
    /usr/local/bin/copilot --prompt "Say hello" --log-level all 2>&1 | head -50
```

Interpretation: If this step succeeds but the Execute step fails, the problem
is in the firewall or api-proxy configuration, not in Copilot auth.

*Source: `https://github.github.com/gh-aw/troubleshooting/debug-ghe` — Advanced: Testing Copilot on the Runner Directly section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-troubleshooting-debugging.md` Claims 1–3 (AI-assisted debugging
    via Copilot CLI as primary recommendation — launch `copilot`, select
    `/agent agentic-workflows`, paste failing run URL): Claim 8 here documents
    the GHE-specific extension of that three-step procedure. The only addition
    is the `GH_HOST=yourorg.ghe.com` prefix on the initial `copilot` invocation;
    the `/agent` selector and workflow run prompt are identical. Both sources
    converge on the Copilot CLI + `agentic-workflows` agent as the recommended
    first-response for workflow debugging.
  - `docs-ghaw-troubleshooting-debugging.md` Claim 11 (firewall access logs
    at `sandbox/firewall/logs/access.log`, with `TCP_TUNNEL` for allowed
    traffic and `DENIED` for blocked traffic): the source's "Advanced: Checking
    Firewall Logs" section recommends downloading run artifacts and inspecting
    this same path to verify GHE domains appear as `TCP_TUNNEL`. Both sources
    confirm this as the canonical path for raw firewall audit on any gh-aw
    deployment.
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 11 (local Copilot
    inference test via `COPILOT_GITHUB_TOKEN` + `copilot -p "write a haiku"`
    for diagnosing license/inference access failures): Claim 12 here is the
    runner-level extension of this technique — instead of a local machine
    test, it adds a diagnostic step to the lock file before the Execute step.
    Both techniques isolate Copilot auth from surrounding infrastructure; this
    source adds the runner-scoped variant.
  - `docs-ghaw-network-reference.md` Claim 1 ("The `network` field controls
    domain access for AI engines during workflow execution. When unspecified,
    it defaults to `network: defaults`, allowing only basic infrastructure
    domains."): Claims 10 and 11 here document the GHE-specific domain surface
    that must be reachable from within the AWF sandbox. The compiler auto-adds
    three GHE domains (Claim 4); the telemetry domain must be added manually
    via `network.allowed` (Claim 11). Together, the two sources give the
    configuration reference (network-reference) + the GHE-specific additions
    (this note).
  - `docs-ghaw-sandbox-reference.md` Claim 2 (AWF is the default coding agent
    sandbox providing network egress control through domain-based access controls):
    Claim 4 here confirms that the compiler auto-adds GHE-specific domains to
    the AWF firewall allow-list at compile time. The GHE compilation is the
    first corpus documentation of the compiler modifying the AWF allow-list
    automatically rather than requiring manual `network.allowed` entries.

- **Extends**:
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 12 (GHES on-premise
    deployments require `api-target: api.enterprise.githubcopilot.com` plus
    GitHub Connect enabled, with a GHES-specific error table): this note adds
    GHE Cloud with data residency as a distinct enterprise deployment context
    with its own `api-target` value (`copilot-api.yourorg.ghe.com`), own domain
    requirements (four specific subdomains), and own error catalogue. GHES
    (on-premise) and GHE Cloud (data residency cloud) are separate products
    with different infrastructure topologies — this note extends the enterprise
    deployment documentation to cover the second context.
  - `docs-ghaw-agentic-authoring.md` Claim 1 (`gh aw init` bootstraps a
    repository for agentic authoring): this note adds the GHE Cloud-specific
    requirement that `gh aw init` must be prefixed with `GH_HOST=yourorg.ghe.com`.
    The underlying initialization mechanism is the same (`install.md` prompt);
    the GHE context adds the `GH_HOST` env var to all CLI commands throughout
    the workflow.
  - `docs-ghaw-network-reference.md` Claims 1–4 (network field, access tiers,
    ecosystem identifiers): this note extends network documentation with the
    four specific domains required for GHE Cloud data residency, the compiler's
    auto-add behavior for three of them, and the manual addition pattern for the
    telemetry domain. The GHE domain table fills a gap in the network reference:
    it covers custom enterprise infrastructure not captured by the standard
    ecosystem identifiers.
  - `docs-ghaw-troubleshooting-debugging.md` Claims 1–3 (three-step Copilot
    CLI debugging): this note extends that procedure with the `GH_HOST`-prefixed
    Copilot invocation for GHE Cloud, and adds the runner-level diagnostic step
    (Claim 12) as a technique for isolating auth failures from firewall failures
    that is not documented in the general debugging guide.

- **Contradicts**: None identified. The GHE Cloud api-target
  (`copilot-api.yourorg.ghe.com`) and the GHES api-target
  (`api.enterprise.githubcopilot.com`) are for different products — not
  contradictory values. The authentication failure cause (wrong `api-target`
  routing) is consistent with `docs-ghaw-troubleshooting-debugging.md`
  Claim 7 (auth failures trace to missing/expired/permission-insufficient
  token) — the GHE case adds a third cause (correct token but wrong endpoint)
  that resolves differently. No contradiction issue filed.

- **Novel** (what this note adds that no prior corpus source covers):
  - **GHE Cloud with data residency as a distinct deployment context** (Claims
    1–4, 10–11): No existing source note covers GHE Cloud (`*.ghe.com`) as
    separate from GHES (on-premise). The entire GHE Cloud setup procedure,
    `api-target` value, compiler auto-configuration behavior, and domain table
    are new to the corpus.
  - **`api-target: copilot-api.yourorg.ghe.com` as the GHE Cloud engine
    configuration** (Claims 1–2): The exact api-target value and the causal
    mechanism (dedicated inference subdomain for data residency) are entirely
    new.
  - **`GH_HOST=yourorg.ghe.com` as a required prefix for all `gh aw` CLI
    operations** (Claims 3, 6, 8): No existing note documents the `GH_HOST`
    requirement for GHE CLI operations.
  - **Compiler v0.61.1+ auto-configuration of GHE domains** (Claim 4): The
    compiler automatically adding three GHE domains to the AWF firewall
    allow-list at compile time (and `--copilot-api-target`, and `GH_HOST`)
    is not documented in `docs-ghaw-compilation-process.md` or any other note.
  - **Four-domain GHE Cloud data residency network surface** (Claim 10): The
    specific four domains and their purposes, empirically observed via traffic
    capture, are not documented anywhere in the corpus.
  - **Telemetry domain as the only non-auto-added GHE domain** (Claim 11):
    The compiler vs. manual distinction for the telemetry domain is entirely new.
  - **`UNDICI_DEBUG=full` for Copilot CLI HTTP traffic capture** (Claim 9):
    The specific requirement to use `UNDICI_DEBUG=full` rather than
    `NODE_DEBUG=http,https` for the Copilot CLI — and the reason (undici
    implementation) — is a non-obvious implementation detail not documented
    anywhere in the corpus.
  - **Runner-level diagnostic step pattern** (Claim 12): Testing Copilot
    directly on the runner (outside the AWF sandbox) as a technique to isolate
    auth failures from firewall/api-proxy failures is a novel diagnostic pattern.
  - **"Not Found" during checkout error and local compiler binary cause**
    (Claim 7): The specific error caused by local compiler builds using
    `actions/checkout` instead of `github/gh-aw-actions` is a developer-workflow
    pitfall not documented elsewhere.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Add a "GHE Cloud deployment" subsection to the GHAW harness configuration
    reference (alongside the GHES subsection from `docs-ghaw-troubleshooting-common-issues.md`
    Claim 12). The subsection should include: (1) `api-target: copilot-api.yourorg.ghe.com`
    as a required frontmatter field (Claim 1); (2) `GH_HOST=yourorg.ghe.com` as a
    required prefix for all `gh aw` CLI commands (Claim 3); (3) v0.61.1+ as the
    minimum extension version for auto-configuration (Claim 4); (4) the required
    domains table (Claims 10–11) for teams with corporate proxy requirements.
  - Document the runner-level Copilot diagnostic step (Claim 12) as the canonical
    pattern for isolating auth failures from firewall failures in any enterprise
    deployment (GHE Cloud or GHES).
  - Add `UNDICI_DEBUG=full` (Claim 9) to the traffic analysis toolbox for
    Copilot CLI — distinguish from `NODE_DEBUG=http,https` which is commonly
    attempted but ineffective for this tool.

- **Chapter 05 (Team Adoption)**:
  - Add a "GHE Cloud data residency" deployment context to the team adoption
    guide, covering the three prerequisites that differ from github.com: (a) the
    `api-target` engine configuration, (b) the `GH_HOST` CLI prefix, and (c) the
    v0.61.1+ extension version requirement (Claim 4). Frame these as a "GHE
    deployment checklist" that teams moving from github.com pilot to GHE Cloud
    production need to verify before their first run.
  - The four-domain network surface (Claim 10) is relevant for team adoption in
    enterprise environments with corporate proxies or strict egress controls —
    document it as the "GHE Cloud network requirements" for infrastructure and
    security team approval workflows.

## Extraction Notes

1. **WebFetch returns AI-processed content**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch processes content through an AI model rather
   than returning raw HTML. Two fetches were used with different verbatim-extraction
   prompts. Technical strings (YAML field values, error messages, domain names,
   environment variable names, CLI commands) are assessed as accurate — they are
   specific technical identifiers that the AI model is unlikely to misrepresent.
   Prose quotes that match the specificity of technical documentation (the "key tip"
   callout, the UNDICI caution, the "If this step succeeds but the Execute step
   fails" verdict) are used as quotes with high confidence. All other prose
   descriptions are marked with "(no direct quote; see paraphrase)" per MINER.md
   §2a guidance.

2. **GHES vs. GHE Cloud distinction**: This source specifically covers GHE Cloud
   with data residency (`*.ghe.com`), which is GitHub's enterprise cloud product
   with tenant-specific data isolation. `docs-ghaw-troubleshooting-common-issues.md`
   Claim 12 covers GHES (GitHub Enterprise Server, on-premise). These are distinct
   products with different api-target values and domain topologies. The guide should
   document both as separate enterprise deployment contexts.

3. **Compiler version boundary confirmed**: The v0.61.1+ version requirement appears
   in the prerequisites section and is consistent with the auto-configuration behavior
   described in Claim 4. Pre-v0.61.1 behavior (manual configuration required) is
   not separately documented in the source; the page assumes practitioners will
   upgrade.

4. **No contradictions filed**: Reviewed all existing corpus source notes. The
   GHE Cloud api-target is complementary to (not contradictory with) the GHES
   api-target in `docs-ghaw-troubleshooting-common-issues.md` Claim 12. The
   "Authentication failed" error interpretation (Claim 5 here: wrong api-target
   routing) adds a third cause to `docs-ghaw-troubleshooting-debugging.md` Claim 7
   (missing/expired token) without contradicting it — in GHE Cloud deployments,
   the api-target cause is more common. Not a contradiction; a GHE-specific
   disambiguation. No contradiction issue required.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` left null. Content is consistent with
   the current gh-aw platform state as of 2026-05-12.

6. **Linked page followed**: The source references "Copilot GHES: Common Error
   Messages" at `/gh-aw/troubleshooting/common-issues/` — this page is already
   covered by `docs-ghaw-troubleshooting-common-issues.md` (issue #421). The
   link to GitHub issue `github/gh-aw#18480` (debugging discussion) was not
   followed; it is an internal issue tracker reference, not a public documentation
   page.
