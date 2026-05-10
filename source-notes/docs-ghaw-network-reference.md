---
source_url: https://github.github.com/gh-aw/reference/network
source_type: docs
title: "GitHub Agentic Workflows: Network Permissions Reference"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#400"
---

# GitHub Agentic Workflows: Network Permissions Reference

> The concrete Layer 4 implementation reference for gh-aw network controls —
> documents the `network:` frontmatter field, the ecosystem identifier system
> (named collections of related domains), the Agent Workflow Firewall (AWF)
> with its log levels and SSL bump capability, content sanitization via URL
> redaction, and audit CLI commands — filling the gap between the conceptual
> five-layer security model and actionable network egress configuration.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `reference/network` page — in
  the "Reference" section, documenting platform behavior authoritatively rather than
  providing conceptual overview or practitioner case studies. This is the canonical
  reference for the `network:` frontmatter field and the Agent Workflow Firewall.)
- **Author credibility**: First-party from GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — the same team behind Peli de Halleux's agent factory
  series and the `gh aw` CLI). YAML schema, ecosystem identifier names, AWF
  behavior, and CLI commands are authoritative for the platform.
- **Scope**: Complete configuration reference for network egress control in gh-aw
  workflows — `network:` field syntax, access tiers, ecosystem identifiers,
  domain allowlisting/blocking, protocol filtering, per-engine AWF implementation,
  firewall configuration, SSL bump, content sanitization, strict mode validation,
  wildcard patterns, and audit tooling. Does NOT cover: the conceptual five-layer
  security model (see `docs-ghaw-how-they-work.md`), MCP server configuration
  in general (see `docs-ghaw-mcps.md`), Safe Outputs permission model, or the
  overall compilation model.

## Extracted Claims

### Claim 1: The `network:` frontmatter field controls domain egress for AI engines during workflow execution; unspecified, it defaults to `network: defaults`, allowing only basic infrastructure domains

- **Evidence**: Opening section of the reference page states the field's purpose and
  default behavior. The three-tier model is explicit.
- **Confidence**: settled (first-party reference documentation; default behavior
  of an unset field is a platform specification)
- **Quote**: "The `network` field controls domain access for AI engines during
  workflow execution. When unspecified, it defaults to `network: defaults`, allowing
  only basic infrastructure domains."
- **Our assessment**: The default-to-infrastructure-only behavior is the network
  expression of the "zero capability by default" principle documented in
  `docs-ghaw-how-they-work.md` Claim 4 — the agent gets the minimum required
  network access unless explicitly expanded. For Ch02 (Harness Engineering):
  teams that add external API calls to their workflows must explicitly declare
  the required domains. The default `network: defaults` will silently block
  undeclared domains, causing runtime failures that may be hard to diagnose without
  the audit log.

### Claim 2: Three privilege tiers exist for network access: default (infrastructure only), selective (named domains only), and none (all denied via `network: {}`)

- **Evidence**: The "Access Levels" section explicitly names and describes all three tiers.
- **Confidence**: settled (first-party reference; tier model is explicitly stated)
- **Quote**: "Three privilege tiers exist: default allow lists (infrastructure
  only), selective access (listed domains only), and no access (all denied)."
- **Our assessment**: The three-tier model provides a clear mental framework for
  harness engineers: start with the default (safe for internal-only workflows),
  expand selectively (for workflows that need external APIs), or completely lock
  down (for workflows processing sensitive data where any external egress is
  unacceptable). The `network: {}` empty-object syntax for "no access" is a
  non-obvious choice — practitioners may assume omitting the field means no access,
  but omitting it actually gives the default infrastructure access. For Ch02:
  document all three tiers with their use cases. For Ch03: `network: {}` is the
  maximum isolation option for high-sensitivity workflows.

### Claim 3: Domains automatically include subdomains; single leading wildcards (`*.example.com`) are supported but nested wildcards (`*.*.example.com`) are not permitted

- **Evidence**: "Access Levels" section on subdomain behavior; "Wildcard Patterns"
  section on the single-wildcard constraint.
- **Confidence**: settled (first-party reference; validation rules are platform specifications)
- **Quote**: "Only single leading wildcards are valid; `*.*.example.com` is not permitted."
- **Our assessment**: The automatic subdomain inclusion means allowing `example.com`
  also allows `api.example.com`, `cdn.example.com`, etc. — which may be broader
  than intended. Practitioners who want to restrict to a specific subdomain should
  use the explicit subdomain (`api.example.com` not `example.com`). The single-
  wildcard constraint prevents overly broad patterns — you cannot use `*.*.example.com`
  to match all subdomains of any subdomain, but `*.example.com` covers all first-level
  subdomains. For Ch02: document that domain entries include subdomains by default
  and that wildcard patterns are limited to a single leading wildcard.

### Claim 4: Ecosystem identifiers are named collections of related domains — preferred over listing individual domains — and include `defaults`, `github`, `local`, `dev-tools`, `containers`, `linux-distros`, `python`, `node`, `rust`, `go`, `java`, and `deno`

- **Evidence**: "Ecosystem Identifiers" section enumerates the valid identifiers.
  The strict mode section further reinforces using identifiers over individual
  domains.
- **Confidence**: settled (first-party; identifiers are explicitly listed with
  their meaning)
- **Quote**: (no direct quote covering the full list; see paraphrase in Our assessment)
- **Our assessment**: Ecosystem identifiers solve the maintainability problem of
  individual domain lists — package repositories (pypi.org, npmjs.com, etc.) may
  have multiple domains, CDNs, mirrors, and API endpoints. The `python` identifier
  captures all Python ecosystem domains; listing them individually would be both
  verbose and brittle as the ecosystem evolves. The language-specific identifiers
  (`python`, `node`, `rust`, `go`, `java`, `deno`) are the most practically useful
  for agent workflows that install dependencies. For Ch02: when a workflow needs
  package manager access, use the ecosystem identifier rather than individual
  domain entries. This is more maintainable and explicitly recommended by strict mode.

### Claim 5: `default-safe-outputs` is a compound ecosystem identifier that combines `defaults`, `dev-tools`, `github`, and `local` identifiers — intended as a baseline for safe output configuration

- **Evidence**: Documentation states the compound behavior of this special identifier.
- **Confidence**: emerging (the exact use cases where this should be preferred over
  specifying the components individually are not detailed on the page)
- **Quote**: "`default-safe-outputs` combines defaults, dev-tools, github, and local
  identifiers for baseline safe output configuration."
- **Our assessment**: This compound identifier is notable because it is scoped to
  the Safe Outputs use case — it bundles exactly the domains needed for a workflow
  that performs read operations (infrastructure + dev tools + GitHub) and writes
  back to GitHub via Safe Outputs. Practitioners configuring Safe Outputs workflows
  can start with `default-safe-outputs` as a single-identifier baseline rather
  than composing four identifiers. For Ch02: document this compound identifier
  in the harness configuration section for workflows that use Safe Outputs as the
  primary write path.

### Claim 6: Unrecognized single-word entries in `network.allowed` that match `[a-z][a-z0-9-]*` trigger compile-time validation errors listing the valid ecosystem identifier options

- **Evidence**: "Ecosystem Identifiers" section explicitly states the validation
  behavior and pattern.
- **Confidence**: settled (first-party; validation rule is a platform specification)
- **Quote**: "Unrecognized single-word entries matching `[a-z][a-z0-9-]*` trigger
  compile-time validation errors listing valid options."
- **Our assessment**: This is a significant compile-time safety net. A typo like
  `pytohn` instead of `python` is caught at compile time, not at runtime when the
  workflow fails to reach pypi.org. The pattern `[a-z][a-z0-9-]*` means
  single-word lowercase identifiers (like ecosystem names) are validated against
  the known list, while quoted multi-word or domain-format entries (`"api.example.com"`)
  pass through as custom domains. For Ch02: include the validation rule as
  explanation for why mixing quoted domains and unquoted ecosystem identifiers
  is intentional design — unquoted identifiers get validated, quoted strings do not.

### Claim 7: Protocol-specific filtering allows restricting a domain to HTTPS-only or HTTP-only by prefixing the entry with the protocol

- **Evidence**: "Protocol-Specific Filtering" section with YAML examples.
- **Confidence**: settled (first-party; YAML syntax is explicit in the examples)
- **Quote**: (no direct prose quote; see YAML artifact in Concrete Artifacts)
- **Our assessment**: Protocol-specific filtering adds a defense layer beyond domain
  allowlisting — it can enforce TLS for security-sensitive endpoints even if the
  domain appears in both HTTP and HTTPS contexts. A workflow that processes
  confidential data and calls an external API can specify `"https://secure.api.example.com"`
  to prevent accidental HTTP egress. The same domain without a protocol prefix
  allows both HTTP and HTTPS. For Ch03: protocol-specific filtering is a defense-
  in-depth option for high-sensitivity workflows where TLS enforcement is required.

### Claim 8: All AI engines (Copilot, Claude, Codex, Gemini) use the same Agent Workflow Firewall (AWF) with identical network configuration syntax — the `network:` field is engine-agnostic

- **Evidence**: "Engine-Specific Implementation" section shows identical configuration
  syntax for all engines, with the AWF as the shared implementation.
- **Confidence**: settled (first-party documentation; the same syntax applying to
  all supported engines is an explicit platform claim)
- **Quote**: "Same AWF firewall, identical configuration syntax." (describing
  Claude/Codex/Gemini relative to the Copilot example)
- **Our assessment**: Engine portability of network configuration means practitioners
  do not need separate network permission schemes when switching engines. The same
  `network:` frontmatter that restricts Copilot to `defaults + python` works
  identically for Claude. This is consistent with the `docs-ghaw-how-they-work.md`
  Claim 9 that all engines use the same workflow structure and tool protocol —
  network controls are another dimension of that uniformity. For Ch02: when
  documenting network configuration, no engine-specific exceptions are needed.

### Claim 9: The AWF firewall supports configurable log levels (debug, info, warn, error) — enabling operational tuning of firewall verbosity for development vs. production

- **Evidence**: Firewall configuration section with `log-level` field example.
- **Confidence**: settled (first-party; the field and valid values are explicit)
- **Quote**: (no direct quote; log-level values are documented in YAML example —
  see Concrete Artifacts)
- **Our assessment**: Log level configuration enables a practical operational pattern:
  use `debug` during development to understand what the firewall is blocking, switch
  to `warn` or `error` in production to reduce noise. The firewall logs feed into
  the `firewall-audit-logs` artifact documented in `docs-ghaw-compilation-process.md`
  Claim 9. For Ch02: the log level should be set intentionally — teams debugging
  network access failures need `debug`; production workflows should run at `warn`
  or higher to avoid artifact bloat.

### Claim 10: SSL bump enables HTTPS deep packet inspection but acts as a man-in-the-middle — use cautiously and only when path-level filtering (not just domain-level) is necessary

- **Evidence**: "SSL Bump for HTTPS Inspection" section with explicit MITM warning.
- **Confidence**: settled (first-party; the MITM characterization and caution are
  explicit in the documentation)
- **Quote**: "SSL bump enables deep packet inspection but acts as a man-in-the-middle—
  use cautiously and only when path-level filtering is necessary."
- **Our assessment**: SSL bump is the mechanism that allows filtering at the URL
  path level (e.g., allowing only `https://github.com/githubnext/*` but not all
  GitHub API endpoints) rather than just at the domain level. The MITM nature means
  the firewall decrypts, inspects, and re-encrypts HTTPS traffic — which breaks
  certificate pinning in client libraries and may violate terms of service for some
  third-party APIs. This is a high-power, high-risk configuration. For Ch03: SSL
  bump should be presented as a last-resort filtering option. If domain-level
  filtering is sufficient, it is always preferable. When path-level precision is
  required (e.g., restricting which GitHub repositories an agent can access), SSL
  bump is the only mechanism available.

### Claim 11: Domains not in the allowed list have their URLs replaced with `(redacted)` in workflow outputs — GitHub domains are always allowed by default regardless of configuration

- **Evidence**: "Content Sanitization" section.
- **Confidence**: settled (first-party; the redaction behavior and GitHub domain
  exemption are explicit platform behaviors)
- **Quote**: "Domains not in the allowed list have their URLs replaced with
  `(redacted)` in outputs to prevent data exfiltration. GitHub domains are always
  allowed by default."
- **Our assessment**: Content sanitization is Layer 5 (output sanitization) of
  the five-layer security model from `docs-ghaw-how-they-work.md` applied at the
  network dimension — not just cleaning prompt-injection artifacts, but preventing
  exfiltration of external URLs through the agent's visible output. An agent that
  retrieves URLs from an internal data store and emits them to comments would have
  those URLs replaced with `(redacted)` unless the domains are explicitly allowlisted.
  The GitHub domain exemption ensures core workflow operations (linking to issues,
  PRs, repos) always work regardless of `network:` configuration. For Ch03: content
  sanitization via URL redaction is a second data-exfiltration defense (the first
  being network egress blocking). Even if the agent receives a blocked URL in its
  context, it cannot emit it visibly in outputs. These two layers together create
  defense-in-depth against exfiltration via network and via output channels.

### Claim 12: Strict mode validation (`strict: true`) triggers warnings when individual ecosystem domain names (e.g., `pypi.org`, `npmjs.org`) are used directly, recommending ecosystem identifiers instead

- **Evidence**: "Strict Mode Validation" section.
- **Confidence**: settled (first-party; the strict mode behavior and the specific
  warning trigger are stated)
- **Quote**: "When `strict: true`, individual ecosystem domain names (e.g., `pypi.org`,
  `npmjs.org`) trigger warnings recommending ecosystem identifiers (`python`, `node`)
  instead. Custom domains pass validation without warnings."
- **Our assessment**: Strict mode is a governance tool — it enforces the ecosystem
  identifier discipline (Claim 4) at validation time. A team that requires consistent
  use of ecosystem identifiers in all workflows can enforce it by running
  `gh aw compile --strict` in their CI pipeline. The fact that custom domains
  (e.g., `api.example.com`) pass without warnings preserves flexibility for
  service-specific access while flagging lazy configurations that list known package
  registry domains individually. For Ch02: recommend `--strict` in CI validation
  steps for teams that want to enforce network configuration consistency.

### Claim 13: `gh aw logs --run-id <run-id>` shows AWF firewall activity and `gh aw audit <run-id>` provides detailed firewall analysis; two runs can be compared with `gh aw audit <run-id1> <run-id2>` to detect access changes between runs

- **Evidence**: "Best Practices" section lists the CLI commands explicitly.
- **Confidence**: settled (first-party; CLI commands are directly prescribed in
  the reference documentation)
- **Quote**: (no direct single quote; three commands listed in the best practices
  section — see Concrete Artifacts)
- **Our assessment**: The audit comparison command (`gh aw audit <run-id1> <run-id2>`)
  is particularly valuable for security investigations and change detection. If a
  workflow's network access pattern changes between versions (e.g., a new MCP server
  contacts domains not in the previous run), the diff surfaces it explicitly. This
  is an operational tool that the guide should recommend for post-deployment
  verification and security auditing. The `firewall-audit-logs` artifact from
  `docs-ghaw-compilation-process.md` Claim 9 is the underlying data source that
  these commands query. For Ch03: add the audit CLI workflow as a post-run
  verification practice for network-sensitive workflows.

## Concrete Artifacts

### Basic Network Configuration Syntax

```yaml
# Selective access: infrastructure + Python ecosystem + custom domain,
# with a specific domain blocked
network:
  allowed:
    - defaults              # Infrastructure domains
    - python                # Python ecosystem (pypi.org, etc.)
    - "api.example.com"     # Custom domain
  blocked:
    - "cdn.example.com"     # Exclude specific domain within an allowed set
```

*Source: docs-ghaw-network-reference, "Key Configuration Options" section*

### No Network Access Configuration

```yaml
# Complete network lockdown (no egress permitted)
network: {}
```

*Source: docs-ghaw-network-reference, "Key Configuration Options" section*

### Protocol-Specific Filtering

```yaml
network:
  allowed:
    - "https://secure.api.example.com"   # HTTPS only for this domain
    - "http://legacy.example.com"        # HTTP only for this domain
    - "example.org"                      # Both protocols permitted
```

*Source: docs-ghaw-network-reference, "Protocol-Specific Filtering" section*

### Engine-Specific Configuration (AWF applies to all engines identically)

```yaml
engine: copilot
network:
  firewall: true
  allowed:
    - defaults
    - python
```

*Source: docs-ghaw-network-reference, "Engine-Specific Implementation" section.
Note: `engine: claude`, `engine: codex`, and `engine: gemini` use the same
`network:` syntax — the AWF is engine-agnostic.*

### Firewall Log Level Configuration

```yaml
network:
  firewall:
    log-level: info  # Valid values: debug, info, warn, error
```

*Source: docs-ghaw-network-reference, "Firewall Configuration" section*

### SSL Bump Configuration for Path-Level HTTPS Inspection

```yaml
network:
  firewall:
    ssl-bump: true
  allow-urls:
    - "https://github.com/githubnext/*"
    - "https://api.github.com/repos/*/issues"
```

*Source: docs-ghaw-network-reference, "SSL Bump for HTTPS Inspection" section.
Warning: SSL bump acts as a man-in-the-middle — use only when path-level filtering
is necessary and domain-level allowlisting is insufficient.*

### Wildcard Pattern Examples

```yaml
network:
  allowed:
    - "*.cdn.example.com"       # All first-level subdomains of cdn.example.com
    - "*.storage.example.com"   # All first-level subdomains of storage.example.com
    # "*.*.example.com"         # INVALID — nested wildcards not permitted
```

*Source: docs-ghaw-network-reference, "Wildcard Patterns" section*

### Ecosystem Identifiers Reference

```
Named ecosystem identifiers (valid in network.allowed without quotes):

  defaults        — Basic infrastructure domains
  github          — GitHub domains
  local           — Local/localhost addresses
  dev-tools       — Development tool domains
  containers      — Container registry domains
  linux-distros   — Linux distribution package repositories

  python          — Python ecosystem (PyPI, Python CDN, etc.)
  node            — Node.js ecosystem (npm registry, etc.)
  rust            — Rust ecosystem (crates.io, etc.)
  go              — Go ecosystem (pkg.go.dev, sum.golang.org, etc.)
  java            — Java ecosystem (Maven Central, etc.)
  deno            — Deno ecosystem

  default-safe-outputs — Compound: combines defaults + dev-tools + github + local
                         (designed for baseline Safe Outputs workflow configuration)

Validation: unquoted single-word entries matching [a-z][a-z0-9-]* are validated
against this list at compile time. Typos trigger errors listing valid options.
Custom domains must be quoted (e.g., "api.example.com") to bypass validation.
```

*Source: docs-ghaw-network-reference, "Ecosystem Identifiers" and "Strict Mode
Validation" sections*

### Audit CLI Commands

```bash
# View AWF firewall activity for a specific run
gh aw logs --run-id <run-id>

# Detailed firewall analysis for a run
gh aw audit <run-id>

# Compare network access between two runs (detect access changes)
gh aw audit <run-id1> <run-id2>
```

*Source: docs-ghaw-network-reference, "Best Practices" section*

### Best Practices Summary (from source)

```
1. Follow least privilege — allow only necessary domains
2. Prefer ecosystem identifiers over individual domain listings
3. Use `gh aw logs --run-id <run-id>` to view firewall activity
4. Use `gh aw audit <run-id>` to inspect detailed firewall analysis
5. Compare two runs with `gh aw audit <run-id1> <run-id2>` to detect access changes
```

*Source: docs-ghaw-network-reference, "Best Practices" section*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth pipeline,
    Layer 4: network controls): this source is the complete configuration reference
    for what that layer says only at a conceptual level. The existing note names
    "network controls" as a named security layer that "limits egress from agent
    runtime" and "prevents exfiltration via unexpected network calls" — this
    reference documents the exact YAML that configures those controls and the AWF
    that enforces them.
  - `docs-ghaw-github-actions-primer.md` Claim 5 (traditional Actions have
    unrestricted network access; agentic workflows restrict to allowlisted domains
    only): the primer states the contrast; this reference provides the configuration
    syntax that implements it. Together they give practitioners both the motivation
    (why allowlisting exists) and the mechanism (how to configure it).
  - `docs-ghaw-mcps.md` Claim 6 (Docker container MCP servers support
    `network.allowed` domain allowlisting): the MCP network controls documented in
    that note are a per-server application of the same AWF mechanism documented
    here. Both use `network.allowed` with `defaults` + specific domains as the
    pattern — consistent syntax, different scopes (MCP server level vs. workflow
    level).
  - `docs-ghaw-web-search.md` Claim 5 and 6 (`network.allowed: [defaults, "*.tavily.com"]`
    as a network permissions template): that note documented `defaults` as a keyword
    without knowing its exact scope; this source confirms `defaults` is an ecosystem
    identifier covering "basic infrastructure domains." The `defaults` + service-
    domain pattern seen in the Tavily example is a specific instance of the general
    `network.allowed` configuration documented here.

- **Extends**:
  - `docs-ghaw-compilation-process.md` Claim 9 (`firewall-audit-logs` artifact
    contains "AWF audit/observability logs: token usage, network policy, audit
    trail"): this source provides the AWF configuration side; the compilation process
    note provides the artifact output side. Together they give a complete picture:
    network policy is configured in the `network:` frontmatter, enforced by the AWF,
    and its activity is recorded in `firewall-audit-logs`. The `gh aw audit`
    commands (Claim 13 here) are the query interface for those logs.
  - `docs-ghaw-mcps.md` Claim 2 (four MCP server types with distinct isolation
    profiles): this source generalizes network controls to the workflow level (not
    just Docker MCP servers). Together: Docker MCP servers get per-server
    `network.allowed` nested under `mcp-servers.<name>`; the overall workflow gets
    top-level `network:` for all other network access. Both scopes use the AWF.
  - `docs-ghaw-web-search.md` Claim 5 (Extraction Notes: ambiguity about whether
    `network:` is a top-level frontmatter key or nested under `mcp-servers.tavily`):
    this reference resolves that ambiguity. The `network:` field is a top-level
    workflow frontmatter key (shown as a sibling of `engine:` in all examples here),
    distinct from the per-server `network:` nested under `mcp-servers.<name>` in
    `docs-ghaw-mcps.md`. Two distinct scopes, same field name.
  - `docs-ghaw-how-they-work.md` Claim 11 (best practices: compile → watch → run
    → review, with `gh aw logs` for cost monitoring): this source extends the `gh aw logs`
    command to network/firewall activity monitoring via `--run-id`. The Claim 11
    recommendation to monitor with `gh aw logs` now has a concrete application to
    network egress auditing.

- **Contradicts**: None identified. The network controls in this reference are
  consistent with all existing corpus notes. The MCP-level `network.allowed` in
  `docs-ghaw-mcps.md` and the workflow-level `network:` here are two different
  scopes of the same AWF — not a contradiction. The `docs-ghaw-web-search.md`
  ambiguity about `network:` placement is resolved (not contradicted) by this
  source.

- **Novel** (what this note adds that no prior source covers):
  - **Complete `network:` frontmatter field reference** (Claims 1–3): No prior
    corpus note documents the full network field syntax (allowed/blocked, access
    tiers, subdomain behavior). `docs-ghaw-how-they-work.md` names network controls
    as a security layer; this reference provides the YAML.
  - **Ecosystem identifier system** (Claims 4–6): The complete list of named
    ecosystem identifiers (`defaults`, `github`, `local`, `python`, `node`, `rust`,
    `go`, `java`, `deno`, `dev-tools`, `containers`, `linux-distros`,
    `default-safe-outputs`) and their validation at compile time is entirely new.
    `docs-ghaw-mcps.md` and `docs-ghaw-web-search.md` use `defaults` but do not
    document the system.
  - **`default-safe-outputs` compound identifier** (Claim 5): This special compound
    identifier (defaults + dev-tools + github + local) is new to the corpus.
  - **Protocol-specific filtering** (Claim 7): HTTPS-only or HTTP-only domain
    entries via URL prefix are not documented in any existing note.
  - **AWF firewall configuration details** (Claims 8–10): The AWF name, log-level
    options (debug/info/warn/error), and SSL bump capability are new to the corpus.
    `docs-ghaw-compilation-process.md` Claim 9 mentions `firewall-audit-logs` but
    does not document AWF configuration.
  - **Content sanitization via URL redaction** (Claim 11): The `(redacted)` output
    behavior for non-allowlisted URLs is a novel data-exfiltration defense layer not
    documented in any existing note, including `docs-ghaw-how-they-work.md`'s
    five-layer security model.
  - **Strict mode for network configuration** (Claim 12): `--strict` validation
    warnings for individual ecosystem domains (recommending identifiers instead) are
    new to the corpus.
  - **Audit CLI commands for network analysis** (Claim 13): `gh aw audit` and the
    cross-run diff comparison (`gh aw audit <id1> <id2>`) are not documented in any
    existing source note.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add concrete `network:` field configuration as a required harness step** (Claims
  1–3): The primer (`docs-ghaw-github-actions-primer.md` Claim 5) warns that domain
  allowlisting is required; this note provides the YAML. Ch02 should include the
  three-tier model (defaults / selective / none) with examples of each and guidance
  on when to use each tier. Any workflow that calls external APIs must configure
  `network.allowed` explicitly — failing to do so means the default infrastructure-
  only access silently blocks external requests.

- **Add ecosystem identifier system as the recommended allowlisting approach** (Claims
  4–6): When a workflow needs package manager access, use `python`, `node`, etc.
  rather than listing individual domains. Document the compile-time validation rule
  (unquoted identifiers must match the known list). Reference `default-safe-outputs`
  for Safe Outputs workflows as a single-identifier baseline configuration.

- **Add protocol-specific filtering as a defense-in-depth option** (Claim 7): For
  workflows handling sensitive data that must call external APIs, `https://` prefix
  enforces TLS at the network control level. Add as an advanced security hardening
  option in the harness engineering section.

- **Add AWF log level as an operational tuning parameter** (Claim 9): Recommend
  `log-level: debug` during development, `log-level: warn` in production. This
  pattern reduces debugging friction while keeping production artifact sizes manageable.

- **Add `--strict` to the recommended CI compile command** (Claim 12): Alongside
  `--actionlint --zizmor --poutine` (from `docs-ghaw-compilation-process.md` Claim
  11), add `--strict` to enforce ecosystem identifier discipline in CI validation.

### Chapter 03: Safety and Verification

- **Expand Layer 4 (network controls) with concrete implementation** (Claims 1–3,
  11): Currently `docs-ghaw-how-they-work.md` names Layer 4 without showing
  configuration. Ch03 should add the concrete YAML and describe the two complementary
  mechanisms: egress blocking (non-allowlisted domains are unreachable) and content
  sanitization (non-allowlisted domain URLs are replaced with `(redacted)` in output).
  These are two independent defenses against data exfiltration via network and output
  channels.

- **Add SSL bump as a last-resort path-level control with explicit MITM caution**
  (Claim 10): For workflows where domain-level filtering is insufficient and path-
  level precision is required, SSL bump enables URL-pattern filtering of HTTPS
  traffic. Frame clearly as high-power/high-risk: breaks certificate pinning, may
  violate third-party API terms. Only use when domain-level allowlisting cannot
  achieve the required granularity.

- **Add content sanitization (URL redaction) as a defense layer** (Claim 11): The
  `(redacted)` behavior means that even if an agent receives blocked domain URLs
  in its context (e.g., from a document it reads), it cannot emit them into GitHub
  comments or PR bodies. This is the output-channel complement to egress blocking.

- **Add audit CLI workflow as post-run verification practice** (Claim 13): After
  deploying a workflow or updating its network configuration, run `gh aw audit <run-id>`
  to verify the firewall activity matches expectations. Use `gh aw audit <id1> <id2>`
  to detect unexpected network access changes between workflow versions.

## Extraction Notes

1. **Source access via WebFetch AI model**: The gh-aw documentation is an
   Astro/Starlight SPA. WebFetch returns rendered text processed through an AI
   model before returning results. Two fetch passes were made: the first returned
   structured content including YAML examples, ecosystem identifier lists, and
   section prose; the second pass requested more verbatim content but declined
   full reproduction citing copyright constraints. Technical strings (YAML field
   names, ecosystem identifier lists, CLI commands) from the first fetch are
   assessed as accurate — they are technical specifications unlikely to be
   misrepresented by the AI model. Prose quotes are marked "(no direct quote;
   see paraphrase in Our assessment)" where verbatim accuracy cannot be confirmed.

2. **Firewall log level values confirmed**: The four log levels (debug, info, warn,
   error) are a standard set consistent with the gh-aw observability tooling
   documented across the corpus. Assessed as accurate technical values.

3. **Ecosystem identifier list completeness**: The twelve identifiers documented
   here represent what was returned in the first fetch. The list may not be
   exhaustive — the documentation may include additional identifiers not surfaced
   in the rendered output. Treat the list as representative, not definitively
   complete.

4. **`default-safe-outputs` identifier**: The description that it "combines
   defaults, dev-tools, github, and local identifiers" was extracted from the
   first fetch. It appears in quotation in the fetch output as part of a larger
   description — assessed as likely verbatim, though marked `emerging` given the
   AI-mediated extraction.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   the current gh-aw platform as of 2026-05-10.

6. **No contradictions filed**: Reviewed all existing corpus source notes.
   No claims in this source materially oppose any existing source note at the
   MINER.md §4a filing threshold. The `docs-ghaw-web-search.md` ambiguity about
   `network:` placement is resolved (not contradicted) by this source. No
   contradiction issue required.

7. **Related resource links noted but not followed**: The page references related
   documentation on network configuration guides, frontmatter configuration, tool-
   specific access, Playwright browser automation, audit commands, and security
   architecture. Per scope constraints, sub-pages were not followed — the focus
   was on the main network reference content. The Playwright automation link may
   contain additional network configuration patterns for browser-based agents
   that are out of scope for this extraction.
