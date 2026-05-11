---
source_url: https://github.github.com/gh-aw/guides/network-configuration
source_type: docs
title: "GitHub Agentic Workflows: Network Configuration Guide"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#439"
---

# GitHub Agentic Workflows: Network Configuration Guide

> The pedagogical companion to the `reference/network` page — provides use-case
> configuration patterns for gh-aw network access (Python+containers, full-stack
> web, DevOps automation), introduces six ecosystem identifiers not previously
> in the corpus (`python-native`, `dotnet`, `julia`, `ruby`, `terraform`,
> `playwright`), and documents strict mode as the default with hard-error behavior
> that contradicts the reference page's description of it as opt-in with warnings
> (see contradiction issue #660).

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/network-configuration`
  page — in the "Guides" section, providing walkthrough-style practical examples
  rather than formal field specification. Distinct from the `reference/network`
  page covered in `docs-ghaw-network-reference.md`, which provides authoritative
  field-level specification. Guide pages are complementary to reference pages:
  reference defines the contract, guides show how to use it.)
- **Author credibility**: First-party from GitHub Agentic Workflows team (GitHub
  Next / Microsoft Research — same team as `docs-ghaw-network-reference.md` and
  the Peli de Halleux agent factory series). YAML examples, ecosystem identifier
  names, and error messages are authoritative for the platform.
- **Scope**: Practical network configuration walkthrough — Quick Start patterns,
  ecosystem identifier table (15 entries), common configuration use cases (Python,
  full-stack web, DevOps), custom domain syntax, wildcard behavior, protocol-
  specific filtering, strict mode behavior (including default status and error
  messages), security best practices, and firewall troubleshooting. Does NOT
  cover: SSL bump, AWF log levels, content sanitization/URL redaction, audit CLI
  comparison commands, or the `default-safe-outputs` compound identifier
  (those are in `docs-ghaw-network-reference.md`).

## Extracted Claims

### Claim 1: The `defaults` identifier is required for all workflows and covers certificates, JSON schema, and Ubuntu mirrors — the Quick Start pattern is to always include it first

- **Evidence**: The Quick Start section leads with a YAML example where `defaults`
  is the first entry and is labeled "Required: Basic infrastructure." The
  "Available Ecosystems" table shows `defaults` as covering "Certificates, JSON
  schema, Ubuntu mirrors" with "All workflows (required)" in the use-for column.
- **Confidence**: settled (first-party documentation; the "required" designation
  is explicit and consistent with `docs-ghaw-network-reference.md` Claim 1)
- **Quote**: "Always include `defaults` for basic infrastructure"
- **Our assessment**: The "always required" framing provides more actionable
  guidance than the reference page's description of the default behavior — it
  gives practitioners a clear starting point. The actual infrastructure domains
  covered by `defaults` (certificates, JSON schema, Ubuntu mirrors) are more
  specific here than in the reference note. This is the foundational network
  configuration rule for any gh-aw workflow. For Ch02: "always start with
  `defaults`" should be the first line of network configuration guidance.

### Claim 2: The guide documents 15 ecosystem identifiers, including six not previously in the corpus: `python-native`, `dotnet`, `julia`, `ruby`, `terraform`, and `playwright`

- **Evidence**: The "Available Ecosystems" table lists all 15 identifiers with
  their included domains and use cases. The six new-to-corpus identifiers are
  each documented with concrete domain inclusions and specific use contexts.
- **Confidence**: settled (first-party; identifier names and domain associations
  are authoritative for the platform)
- **Quote**: (no direct prose quote; see the full identifier table in Concrete
  Artifacts — identifier names and domain columns are extracted verbatim)
- **Our assessment**: The 15-entry list here partially overlaps with but is
  distinct from the 13-entry list in `docs-ghaw-network-reference.md`. This
  source adds `python-native`, `dotnet`, `julia`, `ruby`, `terraform`, and
  `playwright`; the reference note adds `local`, `dev-tools`, `deno`, and
  `default-safe-outputs`. The differences may reflect documentation evolution
  rather than platform inconsistency, but the corpus now has two partially
  overlapping ecosystem identifier lists. For Ch02: use the combined list from
  both sources until a definitive authoritative list can be confirmed.

### Claim 3: `python-native` is a dedicated ecosystem identifier for Python packages with native Rust extensions — it covers all Python/PyPI domains plus `crates.io`

- **Evidence**: The "Available Ecosystems" table entry for `python-native`
  specifies: "PyPI, conda, pythonhosted.org + crates.io" with use case
  "Python packages with native extensions (pyo3/maturin)."
- **Confidence**: settled (first-party; identifier content and use case are
  explicitly documented)
- **Quote**: "PyPI, conda, pythonhosted.org + crates.io" (from the Includes
  column of the ecosystem table for `python-native`)
- **Our assessment**: `python-native` solves a real workflow configuration
  problem: Python packages that include compiled Rust extensions (using pyo3 or
  maturin) need both PyPI access and crates.io access during installation. Without
  `python-native`, a practitioner would need to list both `python` and `rust`
  identifiers, and might not know that crates.io is needed. `python-native` bundles
  both as a single identifier scoped to this exact use case. This is a novel
  ecosystem identifier not in any existing source note. For Ch02: document
  `python-native` in the harness engineering section for ML/AI workflows that
  commonly install packages like `tokenizers`, `pydantic-core`, or other
  Rust-backed Python libraries.

### Claim 4: Three common configuration patterns address distinct project types — Python+containers for data/ML pipelines, node+playwright+github for full-stack web, and terraform+containers+github for DevOps automation

- **Evidence**: The "Common Configuration Patterns" section provides three
  named, complete YAML examples with explanatory comments for each use case.
- **Confidence**: settled (first-party; the patterns are explicitly documented
  recommendations, not speculative)
- **Quote**: (no direct prose quote; see Concrete Artifacts for the three YAML
  patterns — they are extracted verbatim)
- **Our assessment**: These patterns are the most practically actionable content
  in the guides page. Rather than requiring practitioners to derive their own
  network configuration from first principles, the guide gives three ready-to-use
  starting points covering the most common project types in agentic workflows.
  The DevOps pattern (terraform+containers+github) is particularly notable because
  it establishes that infrastructure-as-code workflows using the Terraform registry
  have a supported network identifier. For Ch02: include these three patterns as
  starting templates for network configuration. Practitioners should identify which
  pattern closest matches their project and start from there.

### Claim 5: Strict mode is enabled by default for all workflows and all engines — it enforces ecosystem identifiers over individual domain names

- **Evidence**: The "Strict Mode and Ecosystem Identifiers" section states the
  default status explicitly: "Workflows use strict mode by default, which enforces
  ecosystem identifiers instead of individual domains for security. This applies
  to all engines."
- **Confidence**: emerging (first-party; but directly contradicts the reference
  page's description of strict mode as opt-in — see contradiction issue #660)
- **Quote**: "Workflows use strict mode by default, which enforces ecosystem
  identifiers instead of individual domains for security. This applies to all
  engines."
- **Our assessment**: If accurate, this is a significant operational reality —
  practitioners who configure `network.allowed: ["pypi.org"]` without knowing
  about strict mode will get a hard error, not a passing workflow. The "applies
  to all engines" qualification is important: strict mode is not a Copilot-only
  feature. This contradicts `docs-ghaw-network-reference.md` Claim 12, which
  treats strict mode as opt-in via `--strict` compile flag. See contradiction
  issue #660. For Ch02: if Side B (this source) is confirmed, the network
  configuration section must prominently explain strict mode as the starting
  state, not an optional enhancement. Do NOT treat this claim as settled until
  contradiction #660 is resolved.

### Claim 6: In strict mode, custom domains are blocked and produce hard errors — they require disabling strict mode via `strict: false` in the workflow frontmatter

- **Evidence**: The "Using Custom Domains" section shows a YAML example with
  `strict: false` as a required frontmatter field, and the error message for
  custom domains explicitly states: "Custom domains are not allowed for security.
  Set 'strict: false' to use custom domains." The Security Note adds: "Custom
  domains bypass ecosystem validation. Only disable strict mode when necessary
  and ensure you trust the custom domains you allow."
- **Confidence**: emerging (first-party; but directly contradicts the reference
  page's Claim 12 that "Custom domains pass validation without warnings" in strict
  mode — see contradiction issue #660)
- **Quote**: "Custom domains are not allowed for security. Set 'strict: false' to
  use custom domains."
- **Our assessment**: This is the most concrete evidence for the contradiction
  with `docs-ghaw-network-reference.md`. The reference note states custom domains
  "pass validation without warnings" in strict mode; this guide says custom domains
  trigger hard errors in strict mode and require `strict: false` to use. These two
  claims cannot both be true. `strict: false` as a frontmatter field is also new
  — the reference note documented `--strict` as a compiler flag (CI-level), not a
  per-workflow frontmatter setting. For Ch02/Ch03: do NOT give guidance on custom
  domain behavior in strict mode until contradiction #660 is resolved.

### Claim 7: Invalid protocol prefixes (e.g., `ftp://`) in `network.allowed` are rejected at compile time

- **Evidence**: The "Protocol-Specific Filtering" section notes: "Validation:
  Invalid protocols (e.g., `ftp://`) are rejected at compile time."
- **Confidence**: settled (first-party; compile-time validation rule is a platform
  specification)
- **Quote**: "Invalid protocols (e.g., `ftp://`) are rejected at compile time."
- **Our assessment**: This extends `docs-ghaw-network-reference.md` Claim 7
  (protocol-specific filtering exists) with the specific validation rule — only
  valid URL protocols (https://, http://) are accepted; other protocols are caught
  at compile time. This is a useful safety net: a misconfigured entry like
  `ftp://legacy.server.com` doesn't silently fail at runtime — it prevents
  compilation. For Ch02: document the protocol validation as part of the compile-
  time safety layer for network configuration.

### Claim 8: Protocol-specific filtering requires the AWF firewall sandbox (`sandbox: { agent: awf }`) to be enabled alongside the `engine: copilot` declaration

- **Evidence**: The protocol-specific filtering YAML example includes
  `sandbox: { agent: awf }` alongside `engine: copilot`. The section header
  adds a parenthetical: "(Copilot engine with AWF firewall)."
- **Confidence**: emerging (first-party; the parenthetical implies this is a
  Copilot+AWF specific feature, but the reference note documented protocol
  filtering without this prerequisite)
- **Quote**: "Restrict domains to specific protocols for enhanced security
  (Copilot engine with AWF firewall)"
- **Our assessment**: The `sandbox: { agent: awf }` requirement was not mentioned
  in `docs-ghaw-network-reference.md` Claim 7. That note presented protocol-
  specific filtering as generally available. This guide qualifies it as a
  Copilot+AWF feature, suggesting other engines may not support it (or it's
  automatically active for other engines without needing the sandbox declaration).
  For Ch02/Ch03: treat protocol-specific filtering as confirmed for Copilot+AWF;
  check engine-specific documentation before applying to Claude, Codex, or Gemini
  workflows.

### Claim 9: The wildcard `*.example.com` pattern matches the base domain `example.com` itself in addition to all subdomains — both forms produce identical access scope

- **Evidence**: The "Wildcard Pattern Behavior" section states: "`*.example.com`
  matches `sub.example.com`, `deep.nested.example.com`, and `example.com`" and
  "Both `example.com` and `*.example.com` match subdomains. Use wildcards when
  you want to explicitly document that subdomain access is expected."
- **Confidence**: settled (first-party; the matching behavior is explicitly
  documented)
- **Quote**: "`*.example.com` matches `sub.example.com`, `deep.nested.example.com`,
  and `example.com`"
- **Our assessment**: This extends and clarifies `docs-ghaw-network-reference.md`
  Claim 3. The reference note said "Domains automatically include subdomains" but
  this guide makes the wildcard base-domain inclusion explicit: `*.example.com`
  is not strictly narrower than `example.com` — both provide the same access
  scope. The practical guideline is: use `example.com` for brevity, use
  `*.example.com` when you want to explicitly signal that subdomain access is
  intentional documentation (not just a side effect of subdomain inclusion).
  For Ch02: the "both match subdomains" point should accompany any wildcard
  pattern documentation to prevent practitioners from thinking `*.example.com`
  is more restricted than `example.com`.

### Claim 10: The recommended incremental approach is to start with `defaults`, run the workflow, and add ecosystem identifiers based on firewall denial log output

- **Evidence**: Security Best Practice #4: "Add incrementally — Start with
  `defaults`, add ecosystems as needed based on firewall denials." The
  "Troubleshooting Firewall Blocking" section shows the `gh aw logs --run-id
  <run-id>` command and a sample firewall log output that maps blocked domains
  to ecosystem identifiers to add.
- **Confidence**: settled (first-party; this is an explicit recommended workflow)
- **Quote**: "Add incrementally — Start with `defaults`, add ecosystems as needed
  based on firewall denials"
- **Our assessment**: This iterative approach inverts the common failure mode of
  over-granting network access upfront. By starting with `defaults` only and
  letting the firewall tell you what to add, practitioners build minimal-permission
  configurations by construction rather than trying to predict all required domains
  in advance. The firewall log format (Concrete Artifacts) makes this feedback loop
  actionable — the log explicitly names the ecosystem identifier to add alongside
  each blocked domain. For Ch02: present this incremental pattern as the recommended
  network configuration workflow for new gh-aw projects.

### Claim 11: The firewall log format explicitly maps each blocked domain to the ecosystem identifier to add — the troubleshooting experience is self-directing

- **Evidence**: The "Troubleshooting Firewall Blocking" section shows a sample log:
  `registry.npmjs.org:443 (3 requests) → Add \`node\` ecosystem` and
  `pypi.org:443 (2 requests) → Add \`python\` ecosystem`.
- **Confidence**: emerging (the log format may be illustrative rather than an
  exact platform output; assessed as representative based on the guide's
  presentation)
- **Quote**: (no direct prose quote; see Concrete Artifacts for the log format
  extracted verbatim from the source)
- **Our assessment**: The ecosystem identifier suggestion in the firewall log is
  the runtime complement to the compile-time strict mode validation. Strict mode
  catches known ecosystem domains used individually at compile time; the firewall
  log catches actual runtime access to ecosystem domains at execution time. Both
  point the practitioner to the same solution: use the ecosystem identifier. For
  Ch02: the self-directing firewall log format reduces the cognitive load of
  network configuration debugging — it is not just a log, it is an actionable
  fix instruction.

### Claim 12: `network: {}` (empty object) disables external network access while keeping engine communication (to the AI provider) functional

- **Evidence**: "Advanced Options" section states: "Disable all external network
  access (engine communication still allowed)" with `network: {}` as the
  configuration.
- **Confidence**: settled (first-party; consistent with `docs-ghaw-network-reference.md`
  Claim 2 on the three privilege tiers)
- **Quote**: "Disable all external network access (engine communication still
  allowed)"
- **Our assessment**: The "engine communication still allowed" qualifier is more
  specific than the reference note's description of `network: {}` as "all denied."
  This clarifies that `network: {}` is not a complete network blackout — the AI
  engine must still communicate with its provider (Copilot API, Anthropic API,
  etc.) to function. Only external network access (package registries, custom
  APIs, etc.) is disabled. For Ch03: `network: {}` is the maximum isolation for
  non-AI-traffic, not complete air-gapping. This is important for security
  practitioners who might expect `network: {}` to create a fully isolated
  execution environment.

## Concrete Artifacts

### Quick Start YAML Pattern

```yaml
# From guides/network-configuration — Quick Start section
network:
  allowed:
    - defaults      # Required: Basic infrastructure
    - python        # PyPI, conda (for Python projects)
    - node          # npm, yarn, pnpm (for Node.js projects)
    - go            # Go module proxy (for Go projects)
    - containers    # Docker Hub, GHCR (for container projects)
```

*Source: gh-aw guides/network-configuration, "Quick Start" section*

### Available Ecosystems Table (full 15-identifier list)

```
Ecosystem        | Includes                                      | Use For
-----------------|-----------------------------------------------|--------------------------------
defaults         | Certificates, JSON schema, Ubuntu mirrors     | All workflows (required)
python           | PyPI, conda, pythonhosted.org                 | Python packages
python-native    | PyPI, conda, pythonhosted.org + crates.io     | Python packages with native extensions (pyo3/maturin)
node             | npm, yarn, pnpm, Node.js                      | JavaScript/TypeScript
go               | proxy.golang.org, sum.golang.org              | Go modules
containers       | Docker Hub, GHCR, Quay, GCR, MCR             | Container images
java             | Maven, Gradle                                 | Java dependencies
dotnet           | NuGet                                         | .NET packages
julia            | pkg.julialang.org, storage.julialang.net      | Julia packages
ruby             | RubyGems, Bundler                             | Ruby gems
rust             | crates.io                                     | Rust crates
github           | githubusercontent.com                          | GitHub resources
terraform        | HashiCorp registry                            | Terraform modules
playwright       | Browser downloads                             | Web testing
linux-distros    | Debian, Ubuntu, Alpine                        | Linux packages
```

*Source: gh-aw guides/network-configuration, "Available Ecosystems" section*

### Common Configuration Patterns (three use cases)

```yaml
# Python project with containers
network:
  allowed:
    - defaults
    - python
    - containers

# Full-stack web development
network:
  allowed:
    - defaults
    - node
    - playwright
    - github

# DevOps automation
network:
  allowed:
    - defaults
    - terraform
    - containers
    - github
```

*Source: gh-aw guides/network-configuration, "Common Configuration Patterns" section*

### Custom Domain Syntax

```yaml
network:
  allowed:
    - defaults
    - python
    - "api.example.com"        # Matches api.example.com and subdomains
    - "*.cdn.example.com"      # Wildcard: matches any subdomain of cdn.example.com
```

*Source: gh-aw guides/network-configuration, "Custom Domains" section*

### Protocol-Specific Filtering (Copilot + AWF)

```yaml
engine: copilot
network:
  allowed:
    - defaults
    - "https://secure.api.example.com"   # HTTPS-only
    - "http://legacy.internal.com"       # HTTP-only
    - "example.org"                      # Both protocols (default)
sandbox:
  agent: awf  # Firewall enabled
```

*Source: gh-aw guides/network-configuration, "Protocol-Specific Filtering" section.
Note: Section header specifies "(Copilot engine with AWF firewall)" — may be
Copilot-specific or require explicit sandbox declaration for other engines.*

### Strict Mode Error Messages

```
# Error when a known ecosystem domain is used directly (e.g., "pypi.org"):
error: strict mode: network domains must be from known ecosystems 
(e.g., 'defaults','python', 'node') for all engines in strict mode. 
Custom domains are not allowed for security. Did you mean: 'pypi.org' 
belongs to ecosystem 'python'?

# Error when a custom domain is used (e.g., "api.example.com"):
error: strict mode: network domains must be from known ecosystems 
(e.g., 'defaults','python', 'node') for all engines in strict mode. 
Custom domains are not allowed for security. Set 'strict: false' to 
use custom domains.
```

*Source: gh-aw guides/network-configuration, "Error Messages" subsection under
"Strict Mode and Ecosystem Identifiers." These messages are extracted verbatim.*

### Disabling Strict Mode for Custom Domains

```yaml
---
strict: false    # Required for custom domains
network:
  allowed:
    - python           # Ecosystem identifier
    - "api.example.com"  # Custom domain (only allowed with strict: false)
---
```

*Source: gh-aw guides/network-configuration, "Using Custom Domains" section.
Security Note from same section: "Custom domains bypass ecosystem validation.
Only disable strict mode when necessary and ensure you trust the custom domains
you allow."*

### Strict Mode: Rejected vs. Accepted Examples

```yaml
# ✗ Rejected in strict mode
network:
  allowed:
    - "pypi.org"       # Error: use 'python' ecosystem instead
    - "npmjs.org"      # Error: use 'node' ecosystem instead

# ✓ Accepted in strict mode
network:
  allowed:
    - python           # Ecosystem identifier
    - node             # Ecosystem identifier
```

*Source: gh-aw guides/network-configuration, "Strict Mode and Ecosystem Identifiers" section*

### Security Best Practices (verbatim from source)

```
1. Start minimal         — Only add ecosystems you actually use
2. Use ecosystem identifiers — Don't list individual domains (use `python` instead
                              of `pypi.org`, `files.pythonhosted.org`, etc.)
3. Keep strict mode enabled — Provides enhanced security validation (enabled by default)
4. Add incrementally     — Start with `defaults`, add ecosystems as needed based
                           on firewall denials
```

*Source: gh-aw guides/network-configuration, "Security Best Practices" section*

### Firewall Log Output Format

```
Firewall Log Analysis

Blocked Domains:
  ✗ registry.npmjs.org:443 (3 requests) → Add `node` ecosystem
  ✗ pypi.org:443 (2 requests) → Add `python` ecosystem
```

*Source: gh-aw guides/network-configuration, "Troubleshooting Firewall Blocking" section.
Command: `gh aw logs --run-id <run-id>` — shows firewall activity to identify
blocked domains. Common mappings noted in source: npm/Node.js → `node`,
PyPI/Python → `python`, Docker → `containers`, Go modules → `go`.*

### No-Network Configuration

```yaml
network: {}
```

*Source: gh-aw guides/network-configuration, "Advanced Options" section.
Effect: "Disable all external network access (engine communication still allowed)"*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-network-reference.md` Claim 1 (network field defaults to
    infrastructure only): Claim 1 here adds the specific content of `defaults`
    (certificates, JSON schema, Ubuntu mirrors) and the "always required" framing.
    Both sources agree `defaults` is the baseline. The guide adds actionability:
    "Always include `defaults` for basic infrastructure."
  - `docs-ghaw-network-reference.md` Claim 2 (`network: {}` for no access): Claim
    12 here corroborates but adds the qualifier "engine communication still allowed"
    — an important clarification that `network: {}` is not a complete network
    blackout for the workflow runner.
  - `docs-ghaw-network-reference.md` Claims 3 and 4 (subdomain inclusion, ecosystem
    identifiers): Claims 9 and 2 here corroborate from the guide perspective. The
    wildcard base-domain clarification (Claim 9) extends Claim 3 of the reference.
  - `docs-ghaw-network-reference.md` Claim 7 (protocol-specific filtering): Claim
    7 here corroborates and Claim 8 adds the `sandbox: { agent: awf }` prerequisite
    not mentioned in the reference note.
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 17 (ecosystem identifiers
    expand to curated domain sets): Claims 2 and 10 here corroborate from the guide
    angle — the firewall log drives the incremental pattern documented there.
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 18 (URL redaction as
    diagnostic indicator): Claim 11 here extends the troubleshooting note's URL
    redaction claim with the explicit firewall log format that provides ecosystem
    suggestions alongside blocked domain names.

- **Contradicts**:
  - **`docs-ghaw-network-reference.md` Claim 12** (strict mode behavior): The
    reference note states (a) strict mode requires opt-in via `strict: true` /
    `--strict`; (b) in strict mode, custom domains "pass validation without
    warnings." This guide states (a) strict mode is the DEFAULT; (b) custom
    domains are blocked in strict mode and require `strict: false` to use.
    **Contradiction issue #660 filed.** Do not treat either claim as settled for
    guide synthesis until #660 is resolved.

- **Extends**:
  - `docs-ghaw-network-reference.md` — That note covers the reference specification
    (field syntax, AWF, SSL bump, audit CLI, URL redaction). This note adds the
    pedagogical layer: common configuration patterns, the 15-identifier table with
    six new identifiers, the incremental workflow driven by firewall logs, and
    the strict mode error messages. Together the two notes give both the
    "what is possible" (reference) and "how to configure in practice" (guide).
  - `docs-ghaw-troubleshooting-common-issues.md` Claim 17 (ecosystem identifiers
    for package managers): that note documents four identifiers in troubleshooting
    context; this guide provides a structured 15-identifier table with domain
    inclusions and use cases, significantly expanding the ecosystem identifier
    coverage in the corpus.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer security model, Layer 4:
    network controls): this guide's incremental-permission workflow pattern
    (Claim 10) and ecosystem identifier system (Claims 2–3) fill in the practical
    "how do practitioners configure Layer 4" question that the conceptual note
    leaves open.

- **Novel**:
  - **`python-native` ecosystem identifier** (Claim 3): The first corpus entry
    documenting this identifier specifically for Python packages with Rust native
    extensions. `python-native` = `python` + `rust` (crates.io) as a bundled
    identifier for pyo3/maturin projects. Not in any existing source note.
  - **`dotnet`, `julia`, `ruby`, `terraform`, `playwright` ecosystem identifiers**
    (Claim 2): All six are new to the corpus. `playwright` is particularly notable
    — it explains how browser-automation workflows get network access for browser
    binary downloads, a question the corpus had not addressed.
  - **Three common configuration patterns** (Claim 4): The Python+containers,
    full-stack web, and DevOps automation use-case templates are the first
    corpus entries that give practitioners ready-to-use starting points for
    network configuration, rather than requiring derivation from first principles.
  - **Incremental "start with defaults, add from firewall logs" workflow** (Claim
    10): The iterative minimal-permission approach driven by runtime firewall
    denial feedback is not documented in any existing note. It inverts the
    common practice of trying to predict all needed domains upfront.
  - **Firewall log output format with ecosystem suggestions** (Claim 11): The
    specific log structure (`domain:port (N requests) → Add \`ecosystem\`
    ecosystem`) is not described in any existing note. The self-directing
    format (the log tells you what to add) is a novel operational pattern.
  - **Strict mode error messages verbatim** (Claims 5–6): The exact error message
    text including the "Did you mean:" ecosystem suggestion and the "Set 'strict:
    false'" directive are new to the corpus. These are the only verbatim platform
    error messages for network misconfiguration in the corpus.
  - **`strict: false` as a frontmatter field** (Claim 6): The reference note
    documented `--strict` as a compiler flag; this guide documents `strict: false`
    as a per-workflow frontmatter field. This may represent two different scopes
    (per-workflow vs. CI-wide enforcement), or it may be a complementary mechanism.
    Either way, the frontmatter field form is new to the corpus.
  - **`network: {}` keeps engine communication alive** (Claim 12): The "engine
    communication still allowed" qualifier is the first corpus entry clarifying
    the boundary of what `network: {}` locks down.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add the 15-identifier ecosystem table as the canonical network permissions
  reference** (Claim 2, Concrete Artifacts): The combined ecosystem identifier
  list from this note and `docs-ghaw-network-reference.md` gives practitioners
  the full set. Specifically add `python-native` (for ML/AI projects with Rust-
  backed Python packages), `playwright` (for browser automation workflows),
  `terraform` (for IaC automation), `julia`, `ruby`, and `dotnet` as new entries.

- **Add `python-native` as a distinct ecosystem identifier for ML/AI workflows**
  (Claim 3): Workflows that install packages like `tokenizers`, `pydantic-core`,
  `polars`, or `safetensors` need `python-native` rather than `python` to also
  get crates.io access for their Rust extension builds. Currently no guide content
  documents this.

- **Add the three common configuration patterns as starting templates** (Claim 4):
  Python+containers for data/ML pipelines, node+playwright+github for full-stack
  web, terraform+containers+github for DevOps automation. These are copy-paste
  starting points that practitioners can adapt.

- **Add the incremental "start with defaults, iterate via firewall logs" workflow**
  (Claim 10): Present this as the recommended approach for new workflows. It is
  safer than trying to predict all domains upfront and produces minimal-permission
  configurations as a natural outcome.

- **Hold strict mode guidance pending contradiction #660 resolution** (Claims 5–6):
  Once resolved, add either: (a) strict mode is default — document `strict: false`
  as an escape hatch for custom domains; or (b) strict mode is opt-in — recommend
  `--strict` for CI enforcement. Until then, present both behaviors as platform
  variations without prescribing a single approach.

### Chapter 03: Safety and Verification

- **Add the firewall log pattern as operational security feedback** (Claim 11):
  The self-directing firewall log (blocked domains with ecosystem suggestions)
  is an operational security tool. Document it in the network control section
  as the runtime complement to compile-time strict mode validation.

- **Add `network: {}` clarification for maximum isolation scenarios** (Claim 12):
  `network: {}` is the appropriate configuration for sensitive workflows that
  should have no external package registry access — but it does not disable AI
  engine communication. Security architects designing maximum-isolation environments
  need to understand this boundary.

- **Add protocol-specific filtering + `sandbox: { agent: awf }` prerequisite**
  (Claim 8): For Copilot+AWF workflows where TLS enforcement is required at the
  network layer, document the `sandbox: { agent: awf }` prerequisite that the
  reference note omitted.

## Extraction Notes

1. **Source is AI-processed**: The gh-aw documentation is an Astro/Starlight SPA.
   WebFetch processes through an AI model before returning content. Verbatim claims
   (error messages, YAML examples, ecosystem identifier table, best practice list)
   are treated as accurate — they are specific technical strings unlikely to be
   misrepresented. Prose descriptions are marked "(no direct quote)" where verbatim
   accuracy cannot be confirmed. The ecosystem identifier table and error messages
   are treated as verbatim because they contain specific technical terms that AI
   processing would not alter.

2. **Contradiction #660 filed**: The strict mode claims (Claims 5–6) directly
   contradict `docs-ghaw-network-reference.md` Claim 12. A contradiction issue
   was filed (#660) before opening this PR, per MINER.md §4a. Do not pick a
   verdict in the source note — that is for the human resolver.

3. **Ecosystem identifier lists differ across sources**: This guide lists 15
   identifiers; the reference note lists 13. The differences may reflect
   documentation evolution (the reference note was extracted 2026-05-10, this
   guide on 2026-05-11) or different editorial focuses (reference completeness
   vs. guide common-case coverage). Neither list should be treated as definitively
   complete. The combined list has 19 unique identifiers.

4. **`sandbox: { agent: awf }` in protocol filtering**: The protocol-specific
   filtering YAML includes `sandbox: { agent: awf }` which was absent from the
   reference note's coverage of the same topic. This may be a prerequisite the
   reference note omitted or a Copilot-specific requirement that doesn't apply
   to other engines. Not filed as a contradiction because the omission in the
   reference note is more likely an oversight than a conflicting claim.

5. **No publication date**: The page carries no explicit publication date.
   `date_published` left null. Content is consistent with current gh-aw platform
   state as of 2026-05-11.

6. **Related pages not followed**: The page links to the Network Permissions
   Reference (`/gh-aw/reference/network/`), Playwright Reference, Security Guide
   (`/gh-aw/introduction/architecture/`), and Troubleshooting. The reference page
   and troubleshooting page are already covered in the corpus. The architecture
   page (security guide link) was not followed per scope constraints.
