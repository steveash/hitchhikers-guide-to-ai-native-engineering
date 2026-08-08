---
source_url: https://github.blog/changelog/2026-08-06-mcp-allowlists-in-enterprise-managed-settings
source_type: docs
title: "MCP allowlists in enterprise managed settings"
author: GitHub (official changelog)
date_published: 2026-08-06
date_extracted: 2026-08-08
last_checked: 2026-08-08
status: current
confidence_overall: settled
issue: "#2564"
---

# MCP Allowlists in Enterprise Managed Settings

> GitHub's August 6, 2026 changelog adds `allowedMcpServers` and `deniedMcpServers`
> keys to the enterprise `managed-settings.json` schema (generally available),
> letting enterprise owners gate which MCP servers Copilot clients may run at all —
> by remote URL (with wildcard + anti-evasion canonicalization), local command, or
> user-assigned name — with fail-closed policy evaluation, asymmetric multi-source
> combination rules (allow = intersection, deny = union), and per-key `overridable`
> support for the team-specialization model introduced three days earlier.

## Source Context

- **Type**: docs (GitHub official product changelog, August 6, 2026; ~1-minute
  read, tagged `copilot`). One linked documentation page followed per MINER.md §1:
  the "Enterprise managed settings reference" page
  (`docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings`),
  specifically its `allowedMcpServers`/`deniedMcpServers` sections and the
  "Example configuration" JSON block, which supplied the schema detail the
  changelog only describes in prose. Both pages were fetched as raw HTML (via
  `curl`, converted to plain text) rather than through AI-summarizing WebFetch —
  every quote below was located and copied from that raw text, not reconstructed
  from a model-generated summary (contrast with several sibling notes in this
  family; see Extraction Notes).
- **Author credibility**: GitHub engineering team announcing a production
  (generally available, not preview) capability extension to the
  enterprise-managed-settings system already the subject of six prior corpus
  source notes (June 5, June 17, June 25, July 1, July 30, August 3, 2026 — see
  Cross-References). Authoritative for: the existence, syntax, and GA status of
  `allowedMcpServers`/`deniedMcpServers`, the three matcher types and their
  scope, the fail-closed and multi-layer-AND policy semantics, the
  `overridable` extension to these keys, the supported-client list, and the
  full matcher/canonicalization schema on the linked reference page. Not a
  credible source for: real-world adoption data, how the "GitHub Copilot app"
  client (which does not spawn local stdio processes the way CLI/VS Code do)
  specifically enforces `serverCommand` matching, or performance/latency of
  matcher evaluation at scale — this is a day-one feature announcement.
- **Scope**: A single new capability pair (`allowedMcpServers`, `deniedMcpServers`)
  added to the existing enterprise `managed-settings.json` system. Covers: the
  three matcher types (`serverUrl`, `serverCommand`, `serverName`) and their
  applicable server types, fail-closed policy evaluation, multi-source
  combination rules for each key, the `overridable` capability, supported
  clients, the `.github-private`/`copilot/managed-settings.json` configuration
  surface, and (from the linked reference page) the full JSON schema and the
  URL-canonicalization anti-evasion rules. Does NOT cover: how this control
  interacts with the June 5 note's "MCP configurations that are always enabled"
  distribution mechanism beyond what can be inferred (see Extends), UI-based
  verification tooling for the new keys (unlike `remoteControl`, no "Agents
  page" verification step is mentioned in either fetched page), or GA rollout
  timeline/percentage.

## Extracted Claims

### Claim 1: Enterprise owners can now centrally gate which MCP servers GitHub Copilot clients are allowed to run at all, using new `allowedMcpServers` and `deniedMcpServers` keys in enterprise managed settings; the capability is generally available (not preview)

- **Evidence**: Official changelog, opening paragraph.
- **Confidence**: settled (product fact, official changelog; explicitly states GA status)
- **Quote**: "Enterprise owners can now centrally control which Model Context Protocol (MCP) servers GitHub Copilot clients are allowed to run by using the new allowedMcpServers and deniedMcpServers keys in enterprise managed settings. Approve the MCP servers your developers depend on and block untrusted or non-compliant ones across your enterprise. This capability is generally available."
- **Our assessment**: This closes a governance gap distinct from the two prior
  MCP-adjacent controls in the corpus: the June 5 note
  (`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 5) covers
  enforcing that specific MCP *configurations* are always enabled (a
  distribution/enforcement mechanism for approved configs), while this control
  is an admission gate — it decides whether an MCP server may run *at all*,
  regardless of how a developer configured it locally. GA status (not public
  preview, unlike `strictKnownMarketplaces` at launch) signals GitHub considers
  this control production-ready from day one.

### Claim 2: Each key is a list of matchers identifying MCP servers by remote URL, local command, or user-assigned name — `serverUrl` for remote (HTTP/SSE) servers with wildcard and anti-evasion canonicalization, and `serverCommand` for local (stdio) servers by exact command and arguments

- **Evidence**: Official changelog, "How it works" section.
- **Confidence**: settled (mechanism stated directly in official changelog)
- **Quote**: "Each key is a list of matchers that identify MCP servers by remote URL, local command, or name: serverUrl: Matches remote (HTTP/SSE) servers. It supports * wildcards and canonicalizes URLs to prevent evasion. serverCommand: Matches local (stdio) servers by exact command and arguments."
- **Our assessment**: The explicit "canonicalizes URLs to prevent evasion" language in the changelog itself (not just the linked reference) signals GitHub anticipated adversarial bypass attempts (e.g., percent-encoding, case variation) against a naive string/wildcard matcher — see Claim 12 for the specific canonicalization rules from the reference page. `serverUrl` and `serverCommand` are mutually exclusive in scope (remote vs. local transport), consistent with the stdio/HTTP transport split documented in `docs-ghaw-mcp-gateway-reference.md` Claim 2 for the unrelated gh-aw MCP Gateway product.

### Claim 3: `serverName` matches the user-assigned label but is explicitly documented as a convenience only, not a security control, because users can rename servers

- **Evidence**: Official changelog, "How it works" section, third matcher bullet.
- **Confidence**: settled (explicit security caveat stated directly in official changelog)
- **Quote**: "serverName: Matches the user-assigned label. This is only supplied as a convenience, not a security control, since users can rename servers."
- **Our assessment**: This is the most security-significant single sentence in the changelog: GitHub is proactively warning administrators against relying on `serverName` matchers where enforcement matters, because the label is developer-controlled and spoofable by renaming. An enterprise that allowlists by `serverName` alone (e.g., to permit "internal-search-server") could be bypassed by a developer connecting an untrusted server renamed to the same label. For Ch02/Ch06: the guide should state this as a hard rule — `serverUrl` or `serverCommand` (identity-bound matchers) must be used wherever the allowlist/denylist is a genuine security boundary; `serverName` is only appropriate for UX/organizational bookkeeping.

### Claim 4: Policies fail closed — a malformed or unverifiable configuration is blocked rather than allowed — and when policies come from multiple layers, a server must pass every layer

- **Evidence**: Official changelog, "How it works" section.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Policies fail closed, meaning a malformed or unverifiable configuration is blocked rather than allowed. When policies come from multiple layers, a server must pass every layer."
- **Our assessment**: Fail-closed is the safer default for a security-relevant admission control — an administrator who introduces a JSON syntax error or an unrecognized matcher field gets a stricter posture (server blocked), not a silent bypass (server allowed). "Must pass every layer" describes an AND across settings *layers* (MDM-managed, server-managed, file-based, user-level, per the reference page's precedence list) — this is a different combination axis from the *multi-source* intersection/union rules for the two keys individually (Claims 9 and 11) and from the *multi-team* "least restrictive wins" rule documented in `docs-github-copilot-enterprise-team-specialization-managed-settings.md` Claim 10. See Cross-References for the open question these three distinct combination rules raise when they interact.

### Claim 5: In server-managed deployments, both keys can be marked `overridable` so enterprise teams can define their own allow and deny lists on top of the enterprise baseline

- **Evidence**: Official changelog, "How it works" section.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "In server-managed deployments, both keys can be marked overridable so enterprise teams can define their own allow and deny lists on top of your baseline."
- **Our assessment**: This is the first corpus documentation of a named key beyond `permissions.model` and `permissions.disableBypassPermissionsMode` being eligible for the `overridable` mechanism introduced three days earlier in `docs-github-copilot-enterprise-team-specialization-managed-settings.md` (Claim 4). That note's Claim 12 flagged an open question about whether `overridable` was scoped to the `permissions` object only; this changelog answers it — `overridable` extends to `allowedMcpServers`/`deniedMcpServers`, which are top-level keys, not nested under `permissions` (see Claim 13). For Ch02: update the `overridable`-eligible key list to include these two.

### Claim 6: MCP allowlists are currently enforced on the GitHub Copilot app, Copilot CLI, and VS Code

- **Evidence**: Official changelog, "Supported clients" section.
- **Confidence**: settled (client list stated directly in official changelog)
- **Quote**: "MCP allowlists are currently enforced on the GitHub Copilot app, Copilot CLI and VS Code."
- **Our assessment**: This matches the three-client support level `remoteControl` achieved (`docs-github-copilot-cli-remote-control-managed-devices.md` Claim 8), and is broader than `telemetry`'s CLI+VS-Code-only support documented in that same note. Unresolved: the changelog does not explain how the GitHub Copilot app — which does not run local stdio child processes the way CLI/VS Code do — enforces `serverCommand` matching, since that matcher is scoped to "local (stdio) servers" (Claim 2). This is a gap worth flagging for future verification rather than assuming uniform enforcement mechanics across all three clients.

### Claim 7: Enterprises implement this by adding the keys to `copilot/managed-settings.json` in the source organization's `.github-private` repository and committing to the default branch

- **Evidence**: Official changelog, "Getting started" section.
- **Confidence**: settled (implementation path stated directly in official changelog; consistent with prior corpus notes in this family)
- **Quote**: "In your source organization's .github-private repository, add the keys to copilot/managed-settings.json and commit to the default branch."
- **Our assessment**: Confirms `.github-private` + `copilot/managed-settings.json` remains the single configuration surface for all enterprise Copilot governance additions in this family — the seventh capability added to that same file/repository since June 5, 2026 (see Concrete Artifacts capability map).

### Claim 8: `allowedMcpServers` defines an allowlist where, once set, only servers matching at least one entry are permitted and any unmatched server is blocked; omitting the key entirely allows all servers subject to `deniedMcpServers`, while setting it to an empty array blocks all servers except built-in defaults

- **Evidence**: "Enterprise managed settings reference" page, `allowedMcpServers` section.
- **Confidence**: settled (schema semantics stated directly on official reference page, raw-HTML-verified)
- **Quote**: "Defines an allowlist of MCP servers permitted to run. When set, only servers matching at least one entry are allowed. Any server that is not matched is blocked."
- **Our assessment**: The omit-vs-empty-array distinction is operationally important and easy to get backwards: omitting the key is permissive (allow all, subject to deny rules), while an explicit empty array `[]` is maximally restrictive (block all except built-in servers like the first-party GitHub MCP server). An administrator who intends "no restriction yet" but writes `"allowedMcpServers": []` instead of omitting the key entirely would inadvertently lock out every non-built-in MCP server enterprise-wide. For Ch02: document this omit/empty distinction explicitly as a common misconfiguration risk.

### Claim 9: When multiple settings sources define `allowedMcpServers`, the effective allowlist is the intersection of all sources — a server must be permitted by every source to run

- **Evidence**: "Enterprise managed settings reference" page, `allowedMcpServers` section.
- **Confidence**: settled (combination rule stated directly on official reference page, raw-HTML-verified)
- **Quote**: "When multiple settings sources define allowedMcpServers, the effective allowlist is the intersection of all sources. A server must be permitted by every source to run."
- **Our assessment**: Intersection (AND) is the most-restrictive combination operator — adding a second allowlisting source can only narrow, never widen, what is permitted. This is architecturally the opposite of the "least restrictive value wins" rule documented for multi-*team* combination of overridable keys generally in `docs-github-copilot-enterprise-team-specialization-managed-settings.md` Claim 10. The two rules operate on different axes (multi-source-layer vs. multi-team-membership) and are not stated to interact by either source — see Cross-References for why this is flagged as an open question rather than a contradiction.

### Claim 10: `deniedMcpServers` defines MCP servers that are unconditionally blocked — a match here overrides a match in `allowedMcpServers`, and deny rules always take precedence over allow rules — but first-party Copilot servers cannot be blocked

- **Evidence**: "Enterprise managed settings reference" page, `deniedMcpServers` section.
- **Confidence**: settled (schema semantics and precedence stated directly on official reference page, raw-HTML-verified)
- **Quote**: "Defines MCP servers that are unconditionally blocked. A server matching any entry is blocked even if it also matches an entry in allowedMcpServers. Deny rules always take precedence over allow rules."
- **Our assessment**: Standard deny-overrides-allow precedence, consistent with `docs-ghaw-mcp-gateway-reference.md` Claim 5's "blocked-users MUST take precedence over all other policy fields" rule in the unrelated gh-aw MCP Gateway guard policy — two independent GitHub-adjacent MCP governance systems converge on the same deny-wins design. The linked reference page separately states first-party Copilot servers (e.g., the built-in GitHub MCP server) "are exempt from deny rules and cannot be blocked" — an unblockable, vendor-owned exception carved out of an otherwise unconditional denylist, a new precedent in this corpus for a governance control with a built-in bypass tier.

### Claim 11: When multiple settings sources define `deniedMcpServers`, the effective denylist is the union of all sources — a server blocked by any source is blocked for all

- **Evidence**: "Enterprise managed settings reference" page, `deniedMcpServers` section.
- **Confidence**: settled (combination rule stated directly on official reference page, raw-HTML-verified)
- **Quote**: "When multiple settings sources define deniedMcpServers, the effective denylist is the union of all sources. A server blocked by any source is blocked for all."
- **Our assessment**: Union (OR) for deny and intersection (AND) for allow (Claim 9) are both most-restrictive-wins operators, but they are mathematically different operations applied to companion keys in the same schema — the first documented instance in this corpus of two distinct combination operators paired deliberately within one governance control. Practically: any single settings layer (MDM, server-managed, file-based) can add a server to the denylist and it is blocked everywhere, but every layer must independently agree to allow a server before it is permitted anywhere.

### Claim 12: `serverUrl` canonicalizes both the pattern and the server URL before comparison — lowercasing scheme/host, converting Unicode hosts to Punycode, stripping default ports, decoding percent-encoded host octets, removing fragments/trailing dots, and preventing authority wildcards from matching across the path boundary

- **Evidence**: "Enterprise managed settings reference" page, "URL canonicalization" subsection under `allowedMcpServers`.
- **Confidence**: settled (canonicalization steps enumerated directly on official reference page, raw-HTML-verified)
- **Quote**: "Decodes percent-encoded host octets. For example, %65vil becomes evil."
- **Our assessment**: This is the first documented anti-evasion technical detail for any enterprise-managed-settings matcher in the corpus. The `%65vil` → `evil` example is a concrete illustration of a real bypass class (percent-encoding the hostname to slip past a naive substring/regex allowlist check) that the client-side matcher is explicitly hardened against. Combined with Punycode normalization (blocking homograph/IDN lookalike domains) and the authority/path wildcard boundary rule (preventing `https://mcp.example.com/*` from unexpectedly matching `https://evil.com/mcp.example.com/`-style path tricks), this represents meaningfully more adversarial threat modeling than a simple string-prefix match. For Ch02/Ch06: cite this as a concrete example of what a production-grade MCP allowlist matcher needs to defend against — teams building their own MCP gateways or admission controls (e.g., `docs-ghaw-mcp-gateway-reference.md`) should canonicalize URLs equivalently before pattern matching.

### Claim 13: `allowedMcpServers`/`deniedMcpServers` are top-level keys in `managed-settings.json`, sibling to `permissions`, `remoteControl`, and `sandbox` — not nested under the `permissions` object

- **Evidence**: "Enterprise managed settings reference" page, "Supported keys" table and "Example configuration" JSON block, where `allowedMcpServers` and `deniedMcpServers` appear as top-level object keys alongside `permissions`, `enabledPlugins`, `remoteControl`, and `sandbox` (raw-HTML-verified; full JSON reproduced in Concrete Artifacts).
- **Confidence**: settled (schema structure directly observable in official example JSON and keys table)
- **Quote**: (no prose sentence states this structurally; see the verbatim JSON in Concrete Artifacts, which is the source's own example configuration)
- **Our assessment**: This directly corroborates `docs-github-copilot-cli-remote-control-managed-devices.md` Claim 7, which established that `remoteControl` is a top-level key distinct from the nested `permissions.model`/`permissions.disableBypassPermissionsMode` pair. `allowedMcpServers`/`deniedMcpServers` follow the same top-level pattern, reinforcing that `permissions` groups only behavior-modifying flags while every other governance capability (plugins, marketplaces, remote control, sandbox, and now MCP allow/deny) lives as its own top-level key. For Ch02: the guide's `managed-settings.json` schema reference should keep growing this two-tier structure rather than treating the schema as flat or uniformly nested.

## Concrete Artifacts

### Example configuration excerpt (from "Enterprise managed settings reference", raw HTML)

```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable",
    "model": "auto"
  },
  "remoteControl": {
    "mode": "requireSSO",
    "githubDotComOrganizations": ["ORG-NAME"]
  },
  "allowedMcpServers": [
    { "serverUrl": "https://api.githubcopilot.com/*" },
    { "serverCommand": ["npx", "@playwright/mcp@latest"] },
    { "serverCommand": ["cmd", "/c", "uvx", "markitdown-mcp"] }
  ],
  "deniedMcpServers": [
    { "serverUrl": "https://learn.microsoft.com/*" }
  ],
  "sandbox": {
    "enabled": true,
    "allowBypass": false,
    "sandboxMcpServers": true,
    "sandboxLspServers": true
  }
}
```
*Source: "Enterprise managed settings reference" → "Example configuration" section
(full page example; abbreviated here to the keys relevant to this note —
`permissions` and `sandbox` are documented in sibling notes
`docs-github-copilot-enterprise-bypass-permissions.md` and
`docs-github-copilot-enterprise-auto-model-default.md`). Verified against raw
page HTML, not a WebFetch summary.*

### Matcher property reference (from "Enterprise managed settings reference")

```
serverName
  Matching behavior: Matches the user-assigned server label exactly. Wildcards
    are not supported. "Because users choose server names, use serverUrl or
    serverCommand when you need to enforce the identity of a server."
  Applicable servers: Any server. In-memory servers can only use serverName.

serverUrl
  Matching behavior: Matches a remote server URL. Supports * wildcards for
    subdomains or path prefixes — e.g. https://mcp.example.com/* or
    https://*.internal.example.com/*.
  Applicable servers: Remote servers connecting over HTTP or server-sent
    events (SSE). Does not apply to local servers, even if they have a URL.

serverCommand
  Matching behavior: Matches the exact command and each argument for a local
    server — e.g. ["npx", "-y", "my-mcp-server"]. Wildcards and command-line
    expansion are not supported.
  Applicable servers: Local servers using stdio. Does not apply to remote
    servers, even if they have a command.
```
*Source: "Enterprise managed settings reference" → `allowedMcpServers` matcher
property table, reproduced from raw HTML.*

### URL canonicalization steps (from "Enterprise managed settings reference")

```
Before comparing a serverUrl pattern with a server URL, the client normalizes
both values:
  - Converts the scheme and host to lowercase.
  - Converts internationalized or Unicode host names to Punycode.
  - Removes the default port, :80 for HTTP or :443 for HTTPS.
  - Decodes percent-encoded host octets. For example, %65vil becomes evil.
  - Removes URL fragments and trailing dots from DNS names.
  - Prevents wildcards in the authority component from matching across the /
    boundary into the path.
```
*Source: "Enterprise managed settings reference" → "URL canonicalization"
subsection, reproduced verbatim from raw HTML.*

### Enterprise-Managed Settings Capability Map (updated to August 6, 2026)

```
Configuration surface: .github-private source-org repository
Enterprise file:  copilot/managed-settings.json  (legacy compat: .github/copilot/settings.json)

Capabilities announced to date:
1. Plugin distribution + hooks/MCP-always-enabled (June 5, 2026)
   Source: docs-github-copilot-enterprise-managed-plugins-vscode.md
2. disableBypassPermissionsMode (June 17, 2026)
   Source: docs-github-copilot-enterprise-bypass-permissions.md
3. strictKnownMarketplaces, public preview (June 25, 2026)
   Source: docs-github-copilot-enterprise-strict-known-marketplaces.md
4. permissions.model: auto default (July 1, 2026)
   Source: docs-github-copilot-enterprise-auto-model-default.md
5. remoteControl device restriction (July 30, 2026)
   Source: docs-github-copilot-cli-remote-control-managed-devices.md
6. Team-level specialization / overridable keys (August 3, 2026)
   Source: docs-github-copilot-enterprise-team-specialization-managed-settings.md
7. allowedMcpServers / deniedMcpServers, GA (August 6, 2026) ← THIS NOTE
   - serverUrl / serverCommand / serverName matchers
   - fail-closed, multi-layer AND; allow=intersection, deny=union across sources
   - overridable (extends the Aug 3 team-specialization mechanism)
   Source: docs-github-copilot-mcp-allowlists-enterprise.md
```
*Source: synthesis across all seven enterprise-managed-settings source notes
to date, in chronological order of changelog publication.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-cli-remote-control-managed-devices.md` Claim 7
    (`remoteControl` is a top-level key, not nested under `permissions`): this
    source's Claim 13 shows `allowedMcpServers`/`deniedMcpServers` following the
    same top-level pattern, reinforcing that `permissions` is reserved for a
    narrow set of behavior flags rather than the whole schema.
  - `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
    Claim 4 (the `overridable` mechanism) and Claim 12 (open question of whether
    `overridable` is scoped only to `permissions.model`/
    `permissions.disableBypassPermissionsMode`): this source's Claim 5 answers
    that open question — `overridable` extends to `allowedMcpServers`/
    `deniedMcpServers`, two keys outside the `permissions` object.
  - `docs-ghaw-mcp-gateway-reference.md` Claim 5 ("blocked-users MUST take
    precedence over all other policy fields" in the gh-aw MCP Gateway's guard
    policy): this source's deny-overrides-allow rule (Claim 10) is the same
    deny-wins design principle, independently arrived at in a separate
    GitHub-adjacent MCP governance system (Copilot's client-side allowlist vs.
    gh-aw's server-side guard policy).

- **Extends**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 5
    ("strengthen your governance strategy by defining hooks and MCP
    configurations that are always enabled across your enterprise"): that
    control ensures specific *approved* MCP configurations are always present
    and active; this source adds the complementary admission gate — deciding
    whether an MCP server, however configured, is permitted to run at all. The
    two are different governance mechanisms on the same underlying resource
    (MCP servers) added two months apart to the same configuration file.
  - `docs-github-copilot-enterprise-strict-known-marketplaces.md` (whitelist
    restriction on plugin *marketplaces*, install-time, "prior to tool
    execution"): this source applies the same whitelist-governance philosophy
    to MCP *servers* specifically, rather than plugin distribution sources.
    Together they form a three-layer Copilot enterprise governance stack:
    (1) which plugin marketplaces are trusted (`strictKnownMarketplaces`),
    (2) which MCP servers may run at all (this note), (3) whether tool-call
    approval can be auto-bypassed at runtime
    (`docs-github-copilot-enterprise-bypass-permissions.md`).
  - `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
    Claim 10 ("least restrictive value wins" when combining overridable keys
    across a multi-team user's team memberships): this source's Claims 9 and 11
    document a *different* combination rule — intersection/union across
    settings *layers* (MDM/server-managed/file-based), not across team
    memberships. Neither source states how these two combination axes interact
    for an `overridable`, multi-team, multi-layer `allowedMcpServers` value.
    This is flagged as an open question (see below), not a contradiction.
  - `blog-simonwillison-sean-lynch-mcp-auth-gateway.md` (MCP's primary security
    value is isolating auth flows outside the agent's context window): Lynch's
    framing addresses *where credentials live*; this source addresses a
    different MCP security axis — *which servers may run at all*. An
    enterprise could adopt MCP purely for the auth-isolation benefit Lynch
    describes while still needing this admission control to prevent developers
    from connecting untrusted or non-compliant servers.

- **Contradicts**: None filed as a formal contradiction issue. One open
  interaction question is noted (not filed, per MINER.md §4a's guidance that
  unstated interactions between complementary mechanisms are gaps, not
  disagreements, unless they would lead to materially different guide advice):
  whether the multi-*team* "least restrictive wins" combination rule
  (`docs-github-copilot-enterprise-team-specialization-managed-settings.md`
  Claim 10) and this source's multi-*layer* intersection (allow) / union (deny)
  combination rules (Claims 9, 11) are evaluated in a defined order when an
  enterprise makes `allowedMcpServers`/`deniedMcpServers` `overridable` for
  multi-team users under a multi-layer (MDM + server-managed + file-based)
  deployment. Neither source describes this three-axis interaction. If a future
  source clarifies an evaluation order that conflicts with either rule as
  independently stated, that would warrant a contradiction issue at that point.

- **Novel**:
  - **Server-level MCP admission control**: first corpus documentation of an
    allow/deny mechanism gating which MCP *servers* (as opposed to plugin
    marketplaces, hooks, or runtime permission prompts) a Copilot client may
    run at all.
  - **Asymmetric multi-source combination operators for a companion key pair**:
    first documentation in the corpus of two different combination operators
    (intersection for allow, union for deny) deliberately paired within one
    governance control.
  - **URL canonicalization as an explicit anti-evasion mechanism**: first
    corpus documentation of concrete matcher-hardening techniques (percent-decode,
    Punycode, port/fragment normalization, wildcard authority/path boundary) for
    any enterprise-managed-settings control.
  - **Explicit "convenience label, not a security control" caveat**: first
    corpus documentation of a vendor explicitly warning that one of several
    matcher types in a security-relevant allowlist is not itself a security
    boundary.
  - **Unblockable first-party server exemption**: first corpus documentation of
    a denylist with a built-in, vendor-owned exemption tier that cannot be
    blocked by any configuration.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration / MCP
  integration)**:
  - Add `allowedMcpServers`/`deniedMcpServers` as capability #7 in the
    `managed-settings.json` schema reference, using the capability map and
    matcher-property table above as the suggested structure.
  - Document the omit-vs-empty-array distinction for `allowedMcpServers`
    (Claim 8) explicitly as a common-misconfiguration warning.
  - Document the three matcher types with their security caveat: `serverUrl`
    and `serverCommand` are identity-bound and appropriate for security
    boundaries; `serverName` is a convenience label only and must not be relied
    on where enforcement matters (Claim 3).
  - Cite the URL canonicalization rules (Claim 12) as a concrete reference
    point for practitioners building or evaluating any MCP admission-control
    matcher, including custom or gh-aw-based gateways.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Add server-level MCP allow/deny as the third leg of the Copilot enterprise
    governance stack (marketplace whitelisting → MCP server allow/deny →
    runtime permission-bypass control), per the Extends section above.
  - Flag the fail-closed policy behavior (Claim 4) as an operational note:
    administrators should validate `managed-settings.json` schema correctness
    before rollout, since malformed configuration blocks servers rather than
    silently permitting them — a safe default, but one that can cause
    unexpected outages if a syntax error ships unnoticed.
  - Flag the open multi-axis combination question (team-membership
    "least-restrictive-wins" vs. multi-layer intersection/union) as an
    unresolved interaction worth a security review before an enterprise
    combines `overridable` MCP allow/deny lists with multi-team users across
    MDM + server-managed + file-based layers.

- **Chapter 06/07 (Safety & Security / Enterprise Operations)**:
  - Add `allowedMcpServers`/`deniedMcpServers` to the enterprise security
    hardening checklist for Copilot deployments as the supply-chain control
    specifically for MCP servers, distinct from `strictKnownMarketplaces`
    (plugin marketplaces) and `disableBypassPermissionsMode` (runtime
    approval).
  - Add the first-party-server deny-exemption (Claim 10) as a documented,
    intentional exception administrators should be aware of when auditing
    denylist coverage — it is not a misconfiguration if the built-in GitHub
    MCP server appears reachable despite a broad denylist.

## Extraction Notes

1. **Raw HTML fetch, not AI-summarized WebFetch**: Both the changelog and the
   linked "Enterprise managed settings reference" page were fetched via `curl`
   and converted to plain text with a script that strips tags, rather than
   through WebFetch's AI-summarization pipeline. Every quote in this note was
   located and copied character-for-character from that raw text. This is a
   stronger provenance than several sibling notes in this family — e.g.
   `docs-github-copilot-enterprise-bypass-permissions.md` (Extraction Note 1)
   and `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
   (Extraction Note 1) both relied on WebFetch's AI-summarized output and
   explicitly asked the Assayer to spot-check quotes against the live page.
   That spot-check should still pass here, but was already performed during
   extraction rather than deferred.
2. **Docs page scope limited to MCP-relevant sections**: The "Enterprise
   managed settings reference" page also documents `permissions`,
   `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`,
   `telemetry`, `remoteControl`, `sandbox`, and the team-specialization
   `overridable` mechanism in detail. Those sections are already covered by
   six sibling source notes (see capability map) and were not re-extracted
   here except where needed for schema-structure context supporting Claim 13
   (top-level key placement) and the example-configuration excerpt in Concrete
   Artifacts, which is trimmed to the keys relevant to this note.
3. **GitHub Copilot app enforcement mechanics unconfirmed**: Neither the
   changelog nor the reference page explains how the GitHub Copilot app —
   which, unlike CLI/VS Code, does not spawn local stdio child processes in the
   same way — enforces `serverCommand` matching in practice. Flagged in Claim 6
   as an open question rather than assumed.
4. **No contradiction issue filed**: per MINER.md §4a, the multi-axis
   combination-rule interaction described under Cross-References →
   Contradicts is an unstated interaction between complementary mechanisms
   (a gap), not two sources making opposing claims about the same fact. Filing
   a contradiction issue was judged premature; it is flagged prominently for a
   future source or Smith synthesis pass.
