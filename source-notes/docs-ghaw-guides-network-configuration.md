---
source_url: https://github.github.com/gh-aw/guides/network-configuration
source_type: docs
title: "GitHub Agentic Workflows: Network Configuration (Guides)"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#439"
---

# GitHub Agentic Workflows: Network Configuration (Guides)

> The pedagogical companion to the `reference/network` page — provides practical
> use-case patterns (Python+containers, full-stack web, DevOps automation),
> documents that strict mode is **on by default** (contradicting the reference
> note's opt-in framing — see contradiction issue #660), shows the incremental
> firewall-denial workflow for discovering required ecosystems, and clarifies
> that `network: {}` blocks external traffic but preserves engine communication.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/network-configuration`
  page — the "Guides" section provides practitioner how-to guidance as distinct
  from the "Reference" section's technical specification. This page is explicitly
  framed as providing "practical examples," while the reference page (issue #400,
  `docs-ghaw-network-reference.md`) documents platform behavior authoritatively.
  The two pages cover the same topic from different pedagogical angles.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind all gh-aw documentation. Claims about default platform
  behavior, error message syntax, and configuration patterns are authoritative
  for the platform. The guides section may reflect a more current state of the
  platform than older reference page extractions.
- **Scope**: Practical walkthrough of network configuration for gh-aw workflow
  authors — quick start configuration, common use-case patterns, custom domain
  setup, strict mode behavior (including default-on status and error messages),
  protocol-specific filtering, troubleshooting via firewall logs, and security
  best practices. Does NOT cover: the complete ecosystem identifier list (links
  to reference), AWF firewall internals (SSL bump, log levels), content
  sanitization, or the three-tier access model in abstract terms. The companion
  reference page (issue #400) covers those.

## Extracted Claims

### Claim 1: This guide is explicitly framed as providing "practical examples" for network configuration, distinct from the technical reference page for the same topic

- **Evidence**: Opening sentence directly states the scope and framing.
- **Confidence**: settled (first-party documentation)
- **Quote**: "This guide provides practical examples for configuring network access in GitHub Agentic Workflows while maintaining security."
- **Our assessment**: The guides/reference distinction matters for how each page should be used. The reference page (issue #400) is the authoritative specification for YAML syntax, firewall behavior, and platform guarantees. This guides page is the practitioner-facing "how to actually do it" walkthrough with worked examples. Both should be cited in the guide — reference for "what is X" claims, guides for "how to set up X" recommendations. The framing also explains why this page provides use-case templates rather than exhaustive identifier lists.

### Claim 2: The recommended quick-start configuration adds ecosystem identifiers to `network.allowed` starting with `defaults`, then extends with project-specific ecosystems

- **Evidence**: "Quick Start" section with YAML example. Direct quote establishes the instruction.
- **Confidence**: settled (first-party guide documentation with YAML example)
- **Quote**: "Configure network access by adding ecosystem identifiers to the `network.allowed` list. Always include `defaults` for basic infrastructure:"
- **Our assessment**: This is the actionable starting recipe for any gh-aw workflow author. "Always include `defaults`" is a clear imperative — the platform's basic infrastructure (GitHub, CDNs, core registries) requires `defaults` to be reachable. Practitioners who forget `defaults` will see basic infrastructure failures. Corroborates `docs-ghaw-network-reference.md` Claim 1 (defaults to `network: defaults` when unspecified) but this phrasing is more direct as a how-to instruction. For Ch02: use this exact quote as the opening instruction for the network configuration section.

### Claim 3: Three practical use-case configuration templates are provided — Python+containers, full-stack web (node + playwright), and DevOps automation (terraform + containers)

- **Evidence**: "Common Configuration Patterns" section with three named YAML examples.
- **Confidence**: settled (first-party guide documentation; templates are explicitly presented)
- **Quote**: (no single prose quote covers all three; see Concrete Artifacts for YAML)
- **Our assessment**: These three templates encode the platform team's judgment about which combinations of ecosystems are coherent use cases. The `playwright` identifier in the full-stack web template (vs. the reference note's ecosystem list) is notable — it appears as a recognized ecosystem for browser automation workflows. The DevOps template bundles `terraform + containers + github`, reflecting that infrastructure-as-code workflows need registry access (containers), IaC tooling (terraform), and GitHub API access (github). For Ch02: these templates are ready-to-use starting points for the three most common workflow types; include them as copy-paste configurations.

### Claim 4: Both base domains and wildcard patterns are supported for custom domains; base domains automatically include subdomains; wildcards must be single-leading only

- **Evidence**: "Custom Domains" section with YAML example and explicit behavioral note.
- **Confidence**: settled (corroborates reference page Claim 3; guides page provides explicit behavioral note)
- **Quote**: "Both `example.com` and `*.example.com` match subdomains. Use wildcards when you want to explicitly document that subdomain access is expected."
- **Our assessment**: The guides page adds a behavioral nuance absent from the reference: wildcards serve as *documentation of intent*, not just access expansion. Since `example.com` already matches subdomains, `*.example.com` is semantically equivalent for access purposes but explicitly signals that subdomain access is expected. This is a governance-oriented distinction — it helps reviewers understand when subdomain access is deliberate vs. accidental. The single-wildcard constraint ("Only single wildcards at the start are supported (e.g., `*.*.example.com` is invalid)") corroborates the reference page Claim 3 exactly.

### Claim 5: Strict mode is ON BY DEFAULT for all workflows, enforcing ecosystem identifiers over individual domains and applying to all engines

- **Evidence**: "Strict Mode and Ecosystem Identifiers" section; direct statement about the default.
- **Confidence**: emerging (first-party guide documentation; contradicts reference page Claim 12 which describes strict mode as opt-in — see **Contradicts** below and contradiction issue #660)
- **Quote**: "Workflows use strict mode by default, which enforces ecosystem identifiers instead of individual domains for security. This applies to all engines."
- **Our assessment**: This is the most significant claim in this source relative to the existing corpus. The reference page (Claim 12) describes strict mode as opt-in (`strict: true` / `--strict` compiler flag). This guide states it is on BY DEFAULT. If the guides page reflects current platform behavior, practitioners starting fresh do not need to do anything to get strict mode — it is already active. This directly changes the onboarding instructions for Ch02 and Ch03. Marked `emerging` pending resolution of contradiction issue #660. Do NOT use either note's strict mode framing in guide synthesis until the contradiction is resolved.

### Claim 6: In strict mode, using individual ecosystem domain names (e.g., `pypi.org`, `npmjs.org`) in `network.allowed` produces hard errors with "Did you mean:" suggestions pointing to the correct ecosystem identifier

- **Evidence**: "Strict Mode and Ecosystem Identifiers" section with verbatim error message.
- **Confidence**: emerging (first-party guide documentation; error message syntax is likely accurate but AI-mediated extraction)
- **Quote**: "error: strict mode: network domains must be from known ecosystems (e.g., 'defaults','python', 'node') for all engines in strict mode. Custom domains are not allowed forsecurity. Did you mean: 'pypi.org' belongs to ecosystem 'python'?"
- **Our assessment**: The error message reveals two things: (1) strict mode produces "error" (not "warning" as the reference page Claim 12 says), confirming a hard rejection; (2) the error includes a "Did you mean:" suggestion that names the correct ecosystem identifier for the rejected domain. This "Did you mean:" feature makes strict mode significantly more usable — a practitioner who writes `pypi.org` gets an immediately actionable error rather than a cryptic failure. Corroborates reference page Claim 6 (compile-time validation errors for unrecognized identifiers) but extends it to individual domain entries. Note: reference page Claim 12 says these produce "warnings," not "errors" — another dimension of contradiction issue #660.

### Claim 7: In strict mode, custom domains (non-ecosystem domains) also produce hard errors; using custom domains requires `strict: false` as a workflow frontmatter field

- **Evidence**: Second error message in "Strict Mode" section plus YAML showing `strict: false` frontmatter.
- **Confidence**: emerging (first-party guide documentation; directly contradicts reference page Claim 12's statement that "custom domains pass validation without warnings" in strict mode)
- **Quote**: "error: strict mode: network domains must be from known ecosystems (e.g., 'defaults','python', 'node') for all engines in strict mode. Custom domains are not allowed forsecurity. Set 'strict: false' to use custom domains."
- **Our assessment**: This contradicts the reference page (Claim 12) which states: "Custom domains pass validation without warnings." The two claims cannot both be true — either custom domains fail in strict mode (this guide) or pass without warnings (reference page). The `strict: false` frontmatter field is also novel — the reference page discusses `--strict` as a CI compile flag, while this guide shows `strict: false` as a per-workflow field in the frontmatter `---` block. These may be two complementary mechanisms. **See contradiction issue #660; do not use either note's custom domain behavior claim in guide synthesis until resolved.**

### Claim 8: The security note for disabling strict mode warns about trust implications of custom domains

- **Evidence**: Security callout below the `strict: false` YAML example.
- **Confidence**: settled (first-party guidance; content is advisory, not behavioral specification)
- **Quote**: "Custom domains bypass ecosystem validation. Only disable strict mode when necessary and ensure you trust the custom domains you allow."
- **Our assessment**: This guidance establishes the security model: ecosystem identifiers are validated by the platform (the platform team maintains the domain lists), while custom domains bypass that validation. When a practitioner uses `"api.example.com"`, they are asserting that they trust that domain. This is appropriate security framing — it explains *why* strict mode exists as a default (to prevent practitioners from accidentally adding untrusted custom domains), not just *what* it does. For Ch03: include this as the rationale for recommending strict mode.

### Claim 9: The incremental configuration workflow is to start with `defaults`, then add ecosystems based on firewall denial logs that include explicit ecosystem suggestions

- **Evidence**: Best practices list item plus "Troubleshooting Firewall Blocking" section with firewall log format.
- **Confidence**: settled (first-party guide documentation; firewall log format is explicit)
- **Quote**: "Add incrementally - Start with `defaults`, add ecosystems as needed based on firewall denials"
- **Our assessment**: This operationalizes the "start minimal" principle with a concrete workflow: run with just `defaults`, observe which domains the firewall blocks, then add the suggested ecosystem identifier. The firewall log format makes this concrete — it shows the blocked domain, the request count, and a "→ Add `X` ecosystem" suggestion. This is the discovery mechanism for unknown dependencies: you don't need to know in advance what ecosystems a tool needs; you let the firewall tell you. For Ch02: include the incremental workflow as the recommended approach for new workflows, especially when the full dependency surface is unknown.

### Claim 10: Invalid protocols (e.g., `ftp://`) in protocol-prefixed domain entries are rejected at compile time

- **Evidence**: "Protocol-Specific Filtering" section note.
- **Confidence**: settled (first-party; compile-time rejection is a platform specification)
- **Quote**: "Invalid protocols (e.g., `ftp://`) are rejected at compile time."
- **Our assessment**: This is a defense against protocol confusion attacks — a workflow author cannot accidentally allow `ftp://` access by using an unsupported protocol prefix. Only `https://` and `http://` are valid protocol prefixes; any other protocol string causes a compile-time failure rather than silent runtime behavior. Corroborates the reference page's protocol-specific filtering (Claim 7) and adds the compile-time validation constraint. For Ch03: the compile-time protocol validation is part of the harness safety net — invalid configurations fail at compile time rather than at runtime.

### Claim 11: `network: {}` (empty object) disables all external network access, but engine communication remains available

- **Evidence**: "Advanced Options" section with explicit behavioral note.
- **Confidence**: settled (first-party; the engine communication carve-out is explicitly stated)
- **Quote**: "Disable all external network access (engine communication still allowed):"
- **Our assessment**: This clarifies a subtle but important point about the reference page's `network: {}` documentation. The reference page (Claim 2) describes `network: {}` as "no access (all denied)" without mentioning the engine communication carve-out. This guide makes explicit that the agent can still receive instructions and return results when `network: {}` is set — the "no access" is for external egress only, not for the agent's communication channel with the orchestration infrastructure. For Ch02/Ch03: document this carve-out when explaining `network: {}` — practitioners who think `network: {}` means complete isolation may be surprised that the agent can still communicate with the platform.

### Claim 12: Security best practices are four explicit items covering minimal scope, ecosystem identifiers, strict mode retention, and incremental addition

- **Evidence**: "Security Best Practices" section with numbered list.
- **Confidence**: settled (first-party recommendations)
- **Quote**: "Start minimal - Only add ecosystems you actually use"
- **Our assessment**: The four-item best practice list is the platform team's distilled guidance for practitioners. Items 1 and 4 (start minimal, add incrementally) reinforce each other as a workflow pattern. Item 2 (use ecosystem identifiers, not individual domains) is the practical enforcement mechanism for the strict mode policy. Item 3 (keep strict mode enabled) is directly actionable: it tells practitioners not to add `strict: false` unless necessary, even if they find it restrictive. Together these four items are a complete decision framework for network configuration. For Ch02: use this list directly as the conclusion of the network configuration section.

## Concrete Artifacts

### Quick Start Configuration

```yaml
# Source: guides/network-configuration, "Quick Start" section
network:
  allowed:
    - defaults      # Required: Basic infrastructure
    - python        # PyPI, conda (for Python projects)
    - node          # npm, yarn, pnpm (for Node.js projects)
    - go            # Go module proxy (for Go projects)
    - containers    # Docker Hub, GHCR (for container projects)
```

### Common Configuration Patterns (Three Use-Case Templates)

```yaml
# Python project with containers
# Source: guides/network-configuration, "Common Configuration Patterns"
network:
  allowed:
    - defaults
    - python
    - containers
```

```yaml
# Full-stack web development
# Source: guides/network-configuration, "Common Configuration Patterns"
network:
  allowed:
    - defaults
    - node
    - playwright
    - github
```

```yaml
# DevOps automation
# Source: guides/network-configuration, "Common Configuration Patterns"
network:
  allowed:
    - defaults
    - terraform
    - containers
    - github
```

### Custom Domain Configuration

```yaml
# Source: guides/network-configuration, "Custom Domains" section
network:
  allowed:
    - defaults
    - python
    - "api.example.com"        # Matches api.example.com and subdomains
    - "*.cdn.example.com"      # Wildcard: matches any subdomain of cdn.example.com
```

### Protocol-Specific Filtering

```yaml
# Source: guides/network-configuration, "Protocol-Specific Filtering"
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

### Strict Mode Behavior — Rejected vs. Accepted

```yaml
# ✗ Rejected in strict mode (using individual domain names)
# Source: guides/network-configuration, "Strict Mode" section
network:
  allowed:
    - "pypi.org"       # Error: use 'python' ecosystem instead
    - "npmjs.org"      # Error: use 'node' ecosystem instead
```

```yaml
# ✓ Accepted in strict mode
# Source: guides/network-configuration, "Strict Mode" section
network:
  allowed:
    - python           # Ecosystem identifier
    - node             # Ecosystem identifier
```

### Disabling Strict Mode for Custom Domains

```yaml
# Source: guides/network-configuration, "Strict Mode" section
---
strict: false    # Required for custom domains
network:
  allowed:
    - python           # Ecosystem identifier
    - "api.example.com"  # Custom domain (only allowed with strict: false)
---
```

### Strict Mode Error Messages (Verbatim)

```
# Error: individual ecosystem domain name used
# Source: guides/network-configuration, "Strict Mode" section
error: strict mode: network domains must be from known ecosystems (e.g., 'defaults','python', 'node') for all engines in strict mode. Custom domains are not allowed forsecurity. Did you mean: 'pypi.org' belongs to ecosystem 'python'?

# Error: custom domain used without strict: false
error: strict mode: network domains must be from known ecosystems (e.g., 'defaults','python', 'node') for all engines in strict mode. Custom domains are not allowed forsecurity. Set 'strict: false' to use custom domains.
```

### Firewall Denial Log Format (Troubleshooting)

```
Firewall Log Analysis
Blocked Domains:
  ✗ registry.npmjs.org:443 (3 requests) → Add `node` ecosystem
  ✗ pypi.org:443 (2 requests) → Add `python` ecosystem
```

*Source: guides/network-configuration, "Troubleshooting Firewall Blocking" section.
Access via: `gh aw logs --run-id <run-id>`*

### Complete Network Lockdown

```yaml
# Disable all external network access (engine communication still allowed)
# Source: guides/network-configuration, "Advanced Options" section
network: {}
```

### Security Best Practices (Verbatim)

```
Source: guides/network-configuration, "Security Best Practices" section

1. Start minimal - Only add ecosystems you actually use
2. Use ecosystem identifiers - Don't list individual domains
   (use `python` instead of `pypi.org`, `files.pythonhosted.org`, etc.)
3. Keep strict mode enabled - Provides enhanced security validation (enabled by default)
4. Add incrementally - Start with `defaults`, add ecosystems as needed based on firewall denials
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-network-reference.md` Claims 1–11 (network field syntax, access tiers,
    wildcard behavior, ecosystem identifiers, protocol filtering, AWF behavior): the guides
    page's practical patterns are consistent with the reference page's technical
    specifications on all topics except strict mode (see Contradicts below).
  - `docs-ghaw-network-reference.md` Claim 3 (single-leading wildcard only; `*.*.example.com`
    not permitted): the guides page confirms "Only single wildcards at the start are
    supported (e.g., `*.*.example.com` is invalid)" — same constraint stated in both sources.
  - `docs-ghaw-how-they-work.md` Claim 3 (five-layer defense-in-depth pipeline, Layer 4:
    network controls): this guides page is the practical walkthrough for configuring Layer 4.
    The how-they-work page names network controls as a security layer; this page shows
    practitioners how to configure it and why strict mode exists.
  - `docs-ghaw-how-they-work.md` Claim 4 ("zero capability by default" principle): the
    guides page's "Start minimal" best practice and the strict mode default reinforce this
    principle at the network configuration level.

- **Contradicts**:
  - `docs-ghaw-network-reference.md` Claim 12 (strict mode behavior) — **see contradiction
    issue #660**. The reference note states: "When `strict: true`, individual ecosystem
    domain names (e.g., `pypi.org`, `npmjs.org`) trigger *warnings* recommending ecosystem
    identifiers instead. *Custom domains pass validation without warnings.*" This guides
    page states: strict mode is ON BY DEFAULT; individual domain names produce hard *errors*
    (not warnings); custom domains are "not allowed for security" in strict mode and require
    `strict: false`. Three independent disagreements: (a) default vs. opt-in, (b)
    warning vs. error, (c) custom domains allowed vs. hard blocked. Do not synthesize
    either note's strict mode claims into the guide until contradiction issue #660 is
    resolved.

- **Extends**:
  - `docs-ghaw-network-reference.md` (issue #400): the reference page documents the
    technical specification; this guides page adds three concrete use-case templates
    (Python+containers, full-stack web, DevOps automation) not present in the reference.
    It also adds the incremental discovery workflow (start with `defaults`, iterate via
    firewall denial logs) and the `strict: false` per-workflow frontmatter field (vs.
    the reference's `--strict` compiler flag).
  - `docs-ghaw-how-they-work.md` Claim 11 (best practice workflow: compile → watch →
    run → review): this guides page adds the network-configuration-specific loop
    variant — configure `defaults`, run, check firewall logs, add ecosystems, repeat.
    The two loops are complementary: how-they-work describes the general development
    cycle; this page describes the network-specific iteration within that cycle.

- **Novel** (what this note adds that no prior source covers):
  - **Three named use-case configuration templates** (Claim 3): Python+containers,
    full-stack web (node+playwright), DevOps automation (terraform+containers+github)
    are not documented in any existing source note. These encode the platform team's
    view of coherent ecosystem groupings.
  - **`playwright` as a recognized ecosystem identifier** (Claim 3): The reference
    page's ecosystem identifier list does not include `playwright`; this guides page
    uses it in the full-stack web template as a first-class ecosystem. This is either
    a new identifier added after the reference page was extracted or an omission in the
    reference note's extraction.
  - **Firewall denial log format with ecosystem suggestions** (Claim 9): The "→ Add
    `X` ecosystem" format in firewall logs that makes the incremental discovery
    workflow actionable is not documented in any existing source note.
  - **`strict: false` as a per-workflow frontmatter field** (Claim 7): The reference
    page discusses `--strict` as a compile command flag; this guides page shows
    `strict: false` as a frontmatter field within the `---` block of individual
    workflows. These are different mechanisms (CI-wide vs. per-workflow).
  - **Engine communication carve-out in `network: {}`** (Claim 11): The reference
    page's Claim 2 describes `network: {}` as "no access (all denied)" without
    mentioning the engine communication carve-out. This guides page explicitly
    states "engine communication still allowed."
  - **Strict mode error message syntax with "Did you mean:"** (Claim 6): The specific
    error format including the "Did you mean:" suggestion and the `strict: false`
    remediation directive are new to the corpus.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add three named use-case templates as copy-paste starting points** (Claim 3):
  The Python+containers, full-stack web, and DevOps automation templates are immediately
  actionable. Ch02 should include them in the network configuration section as named
  starting points. Practitioners can select the template closest to their use case and
  extend it.

- **Add the incremental discovery workflow** (Claim 9): The "start with `defaults`,
  run, check firewall denials, add ecosystems" loop is the recommended approach when
  the full dependency surface is unknown. This should be the canonical workflow for
  new harness authors. The firewall log format (showing "→ Add `X` ecosystem"
  suggestions) makes this concrete and actionable.

- **Clarify `network: {}` behavior** (Claim 11): The existing corpus describes
  `network: {}` as "no access (all denied)" (reference page Claim 2). Add the
  clarification that engine communication is preserved — `network: {}` is not
  complete isolation, just external egress lockdown.

- **Add `strict: false` as a per-workflow frontmatter field** (Claim 7, pending
  contradiction resolution): Once contradiction issue #660 is resolved, document whether
  custom domains require a per-workflow `strict: false` frontmatter field or only a
  `--strict` CI flag. If both exist, document when to use each.

### Chapter 03: Safety and Verification

- **Use strict mode default framing** (Claim 5, pending contradiction resolution):
  If contradiction issue #660 resolves in favor of the guides page (strict mode default),
  update Ch03's network configuration section to say practitioners start in a stricter
  posture and must explicitly opt out to use custom domains. This changes the default
  security posture documentation significantly.

- **Add security rationale for strict mode** (Claim 8): Include the explicit rationale —
  "Custom domains bypass ecosystem validation" — as the explanation for why strict mode
  is recommended. The ecosystem identifier system provides platform-level validation;
  custom domains rely solely on practitioner judgment.

- **Add compile-time protocol validation** (Claim 10): Document that invalid protocols
  (`ftp://` etc.) are rejected at compile time as part of the harness safety net.

- **Include security best practices list verbatim** (Claim 12): The four-item list
  (start minimal, use ecosystem identifiers, keep strict mode, add incrementally) is
  concise, complete, and directly from the platform team. Include it as the recommended
  network security checklist.

## Extraction Notes

1. **AI-mediated WebFetch**: The gh-aw documentation is an Astro/Starlight SPA.
   WebFetch returns rendered text processed through an AI model. Two fetch passes
   were made with different prompts to maximize verbatim content capture. Error
   messages, YAML snippets, and prose are assessed as accurate for technical strings;
   prose quotes are marked as such. The firewall log format was returned consistently
   across passes.

2. **Contradiction issue #660 already filed**: The previous Miner run (PR #661, now
   closed) filed contradiction issue #660 before opening that PR. This note references
   that issue; no new contradiction filing is required.

3. **`playwright` ecosystem identifier**: The guides page uses `playwright` in the
   full-stack web template without explaining what domains it covers. The reference
   page's ecosystem identifier list (Claim 4) does not include `playwright`. This may
   be a newer addition to the platform. Treat as `emerging` — the identifier appears
   to be valid but its domain coverage is not documented in the extracted content.

4. **No publication date**: The documentation page does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   current gh-aw platform state as of 2026-05-25.

5. **"Available Ecosystems" section deferred to reference**: The guides page notes
   "For the full list of ecosystem identifiers and the domains they include, see the
   Ecosystem Identifiers reference" rather than listing all identifiers. The extraction
   therefore does not attempt to document the complete identifier list — that is covered
   in `docs-ghaw-network-reference.md` Claim 4.

6. **PR #661 closed without merge**: The previous Miner run opened PR #661 for this
   issue, which was closed without merging. This note is filed fresh with a new branch.
   The contradiction issue #660 from that run is still open and referenced here.
