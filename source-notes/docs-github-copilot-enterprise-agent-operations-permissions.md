---
source_url: https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations
source_type: docs
title: "Enterprise managed permissions for GitHub Copilot agent operations"
author: GitHub (official changelog; byline "Allison")
date_published: 2026-09-09
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: settled
issue: "#3348"
---

# Enterprise Managed Permissions for GitHub Copilot Agent Operations

> GitHub's September 9, 2026 changelog adds a `permissions.deny` / `permissions.ask` /
> `permissions.allow` operation-level rule engine to the enterprise `managed-settings.json`
> schema, replacing the June 17 note's single `disableBypassPermissionsMode` on/off toggle
> with granular `Shell()`/`Read()`/`Edit()`/`Domain()` selectors, deny-over-ask-over-allow
> precedence, and per-source intersection semantics for allow lists — enforced in Copilot
> CLI, GitHub Copilot app, and VS Code Agent Host sessions, but explicitly not in the
> Copilot cloud agent or JetBrains IDEs.

## Source Context

- **Type**: docs (GitHub official product changelog, September 9, 2026; category tag
  "Improvement", ~1-minute read, 4 short paragraphs). One linked documentation page
  followed per MINER.md §1: the "Enterprise managed settings" reference page
  (`docs.github.com/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings`,
  anchored at `#deny-ask-allow`), which supplied the full rule-engine schema, selector
  syntax, precedence rules, and client-support matrix that the changelog only summarizes
  in prose. The changelog's second linked resource, a GitHub Community discussion thread
  (`github.com/orgs/community/discussions/199139`, titled "Enterprise-Managed Settings for
  Copilot Business and Copilot Enterprise"), is the same general enterprise-managed-settings
  thread already characterized as off-topic-for-specific-features in
  `docs-github-copilot-enterprise-auto-model-default.md` (Extraction Note 3) and
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md` (Extraction Note
  5); not re-fetched in depth for this note since it is a general feedback thread that
  predates this specific feature within its own long history.
- **Author credibility**: GitHub engineering team announcing a production capability
  extension to the enterprise-managed-settings system already the subject of seven prior
  corpus source notes (June 5, June 17, June 25, July 1, July 30, August 3, August 6,
  2026 — see Cross-References). Authoritative for: the existence and scope of the new
  `permissions.deny`/`permissions.ask`/`permissions.allow` keys, the four selector types
  and their matching syntax, the deny/ask/allow precedence and multi-source combination
  rules, the `overridable` team-specialization support, and the per-client support matrix
  (both pages fetched as raw HTML via `curl` and stripped to plain text, not through
  AI-summarizing WebFetch — every quote below was located and copied from that raw text).
  Not a credible source for: real-world adoption data, whether GA or public-preview status
  applies (see Extraction Notes — no explicit status label was found in either fetched
  page), or how policy evaluation performs at scale.
- **Scope**: A new rule-engine capability (`permissions.deny`/`ask`/`allow`) added to the
  existing enterprise `managed-settings.json` `permissions` object, alongside the
  already-documented `permissions.disableBypassPermissionsMode`. Covers: the four
  selectors (`Shell`/`Bash`/`PowerShell`, `Read`, `Edit`/`Write`, `Domain`), precedence and
  multi-source combination semantics, the `{ "overridable": <VALUE> }` team-specialization
  syntax for these keys, and the per-client support table. Does NOT cover: the `sandbox`,
  `allowedMcpServers`/`deniedMcpServers`, `telemetry`, or `remoteControl` keys documented in
  sibling notes (out of scope for this changelog and not re-extracted here), or how deny/ask/allow
  operation rules interact with the MCP server-admission allow/deny rules from
  `docs-github-copilot-mcp-allowlists-enterprise.md` when both apply to an MCP tool call.

## Extracted Claims

### Claim 1: Enterprise administrators of GitHub Copilot Business or Enterprise can now centrally control which agent operations are blocked, require human approval, or can proceed without a prompt

- **Evidence**: Official changelog, opening sentence (and matching the page's own
  `og:description` meta tag).
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "If you administer GitHub Copilot Business or GitHub Copilot Enterprise, you can now centrally control which agent operations are blocked, require human approval, or can proceed without a prompt."
- **Our assessment**: This is the headline capability: a three-way operation-level
  disposition (block / ask / auto-proceed) applied centrally by an enterprise admin. It is
  a strictly more granular successor to the binary on/off
  `disableBypassPermissionsMode` control documented in
  `docs-github-copilot-enterprise-bypass-permissions.md` — that control could only force
  every prompt to require approval or leave bypass mode available; this control lets an
  admin route *specific* operations to *specific* dispositions (some always blocked, some
  always requiring approval, some always silently allowed) rather than one blanket setting.

### Claim 2: Managed permissions cover shell commands, file reads and edits, and network domains, giving fine-grained guardrails for sensitive operations without disabling agent workflows

- **Evidence**: Official changelog, second paragraph, first two sentences.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Managed permissions cover shell commands, file reads and edits, and network domains. This gives you fine-grained guardrails for sensitive operations without disabling agent workflows."
- **Our assessment**: The explicit framing "without disabling agent workflows" signals
  GitHub is positioning this as a scalpel rather than a kill switch — an admin can block
  `rm -rf` specifically while leaving the rest of an agent's shell access intact, rather
  than disabling shell access category-wide. This directly answers the Prospector's triage
  question about which operation categories are covered: exactly three (shell, file I/O,
  network), matching the three selector families documented in Claim 6 below (a fourth,
  `PowerShell`, is a case-insensitive variant of `Shell`, not a fourth category).

### Claim 3: Managed restrictions can't be weakened by user or workspace settings, auto-approval, or previously saved approvals

- **Evidence**: Official changelog, second paragraph, third sentence.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Managed restrictions can't be weakened by user or workspace settings, auto-approval, or previously saved approvals."
- **Our assessment**: This is the enforcement-floor guarantee that makes the control
  meaningful as a compliance mechanism rather than a suggestion — it explicitly closes the
  same three bypass vectors (workspace-level settings, auto-approval/bypass mode, and
  cached/persisted approvals) that the linked docs page's `ask` rule definition names
  individually (Claim 9). Without this guarantee, a developer could locally override a
  managed `deny` or `ask` rule, which would defeat the purpose of centralizing the control
  at the enterprise level.

### Claim 4: Administrators can also provide specialized policies for different enterprise teams

- **Evidence**: Official changelog, second paragraph, final sentence.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "You can also provide specialized policies for different enterprise teams."
- **Our assessment**: This confirms the deny/ask/allow rule engine plugs into the
  `overridable` team-specialization mechanism introduced August 3
  (`docs-github-copilot-enterprise-team-specialization-managed-settings.md` Claim 4) rather
  than being a separate, enterprise-uniform-only control. The linked docs page confirms the
  mechanics: "Each subkey is overridable for enterprise teams" (Claim 11 below), using the
  same `{ "overridable": <VALUE> }` syntax as `disableBypassPermissionsMode` and `model`.
  Because the August 3 note's Claim 10 established that overridable keys combine via
  "least restrictive value wins" across a multi-team user's memberships, that same
  governance risk (a user on both a locked-down team and a permissive team inherits the
  permissive team's rules) now applies specifically to `deny`/`ask`/`allow` operation
  rules — including, potentially, a team accidentally loosening a `deny` rule that blocks
  `rm -rf` or SSH key reads for another team's members.

### Claim 5: These controls are generally available in the GitHub Copilot app, GitHub Copilot CLI, and Visual Studio Code sessions that use Agent Host

- **Evidence**: Official changelog, third paragraph.
- **Confidence**: settled (client scope stated directly in official changelog; note this
  states availability, not an explicit "generally available [GA status]" product-maturity
  label — see Extraction Notes)
- **Quote**: "These controls are generally available in the GitHub Copilot app, GitHub Copilot CLI, and Visual Studio Code sessions that use Agent Host."
- **Our assessment**: The VS Code scope is narrower than it first appears: it is not "all
  of VS Code" but specifically "sessions that use Agent Host" — the linked docs page
  confirms this distinction explicitly (Claim 12 below) and contrasts it with the broader
  VS Code reach of `disableBypassPermissionsMode`. This client list (CLI, VS Code
  Agent Host, Copilot app) matches the raw-HTML-verified support table on the linked docs
  page (Claim 13), which additionally shows the Copilot cloud agent and JetBrains IDEs are
  explicitly *not* supported for `deny`/`ask`/`allow` — a gap the changelog prose alone
  does not make as clear as the table.

### Claim 6: Rules use four selector families — `Shell(...)` (with `Bash(...)` as a compatibility alias and a case-insensitive `PowerShell(...)` variant) for shell commands, `Read(...)` for file read/view paths, `Edit(...)` (aliased `Write(...)`) for file write/edit paths, and `Domain(...)` for network origins

- **Evidence**: Linked "Enterprise managed settings" reference page, "Supported
  Selectors"-equivalent subsection under the permissions documentation (raw-HTML-verified).
- **Confidence**: settled (selector syntax enumerated directly on official reference page)
- **Quote**: "Shell commands. Use <command> * (for example, git push *) to match a command prefix; otherwise the rule matches exact text. Bash(...) is a compatibility alias for Shell(...). PowerShell(...) uses the same selector family with case-insensitive command matching."
- **Our assessment**: The prefix-matching syntax (`<command> *`) is the mechanism that
  makes rules like the changelog's own worked examples practical — `Shell(git push *)`
  matches any `git push` invocation regardless of branch/remote arguments, rather than
  requiring an exact string match per invocation. `PowerShell(...)`'s explicit
  case-insensitivity is a deliberate accommodation for Windows shell conventions, where
  command casing is not meaningful the way it is on POSIX shells.

### Claim 7: `Read(...)` and `Edit(...)`/`Write(...)` support glob patterns and four path roots: `//` for the filesystem root, `/` for the workspace root, `~/` for the home directory, and `./` for the current working directory

- **Evidence**: Linked reference page, `Read(...)`/`Edit(...)` selector rows
  (raw-HTML-verified).
- **Confidence**: settled (path-root syntax enumerated directly on official reference page)
- **Quote**: "File read and view paths. Supports glob patterns and these roots: // for the filesystem root, / for the workspace root, ~/ for the home directory, and ./ for the current working directory."
- **Our assessment**: The distinction between `/` (workspace root) and `//` (filesystem
  root) is the detail most likely to trip up an administrator writing rules by hand —
  `Read(~/.ssh/**)` (Claim 8's own example) correctly targets a user's SSH directory
  regardless of workspace, whereas a rule intended to protect `/etc` must use the
  double-slash form `Edit(//etc/**)` rather than a bare `/etc/**`, which would instead
  resolve relative to the workspace root and silently fail to match the real filesystem
  path.

### Claim 8: The example configuration on the reference page denies `Shell(rm -rf *)`, `Read(~/.ssh/**)`, `Edit(//etc/**)`, and `Domain(*.unapproved.example)`; requires approval for `Shell(git push *)`, `Edit(/src/**)`, and `Domain(api.github.com)`; and auto-allows `Shell(npm test *)`, `Read(/src/**)`, and `Domain(registry.npmjs.org)`

- **Evidence**: Linked reference page, "Example configuration" JSON block
  (raw-HTML-verified; reproduced verbatim in Concrete Artifacts).
- **Confidence**: settled (verbatim JSON example on official reference page)
- **Quote**: "\"deny\": [ \"Shell(rm -rf *)\", \"Read(~/.ssh/**)\", \"Edit(//etc/**)\", \"Domain(*.unapproved.example)\" ]"
- **Our assessment**: This worked example is the single most concrete, citable artifact in
  the source — it demonstrates the intended threat model in one glance: destructive shell
  commands, credential file reads, system-path edits, and untrusted domains are the
  canonical `deny` cases; version-control pushes, source-directory edits, and the GitHub
  API domain are canonical `ask` cases (higher-stakes but not inherently malicious); and
  test runs, source reads, and the npm registry are canonical `allow` cases (routine,
  low-risk agent operations). This example is a ready-made starting policy for Ch02's
  enterprise configuration guidance.

### Claim 9: `deny`, `ask`, and `allow` rules combine using deny > ask > allow precedence; an unmatched operation defaults to requiring approval if any managed-settings source defines any permission rule or declares an `allow` list, otherwise it follows the ordinary permission flow

- **Evidence**: Linked reference page, deny/ask/allow precedence explanation
  (raw-HTML-verified).
- **Confidence**: settled (precedence rule stated directly on official reference page)
- **Quote**: "If an MDM-managed, server-managed, or file-based source defines any permission rule—or if any applicable source declares an allow list—an unmatched supported operation defaults to requiring approval. Otherwise, it follows the ordinary permission flow."
- **Our assessment**: This default-to-approval fallback for unmatched operations is an
  important, easy-to-miss operational detail: simply configuring *any* `deny`, `ask`, or
  `allow` rule (even a single one) at the enterprise level flips the default posture for
  every *other*, unmatched operation from "ordinary permission flow" to "requires
  approval." An administrator who adds one `deny` rule to block `rm -rf` could
  inadvertently make every other unmatched shell command, file operation, or domain
  request in the organization start requiring human approval, unless they also configure
  explicit `allow` rules for routine operations (as the worked example in Claim 8 does for
  `npm test`, `/src/**` reads, and the npm registry).

### Claim 10: A `deny` rule set by any managed-settings source blocks the operation for all users regardless of rules in the other sources; an `ask` rule requires fresh, one-time approval that can't be satisfied by bypass mode, an auto-approval setting, a hook or other approval shortcut, or a grant persisted from an earlier approval, and prompts again the next time the same operation is requested; an `allow` rule's effective allowlist is the intersection of all sources that declare one, and a source without an `allow` list places no restriction of its own on that key

- **Evidence**: Linked reference page, per-rule-type definitions (raw-HTML-verified).
- **Confidence**: settled (rule semantics stated directly on official reference page)
- **Quote**: "ask requires fresh, one-time approval before a specific operation can proceed, even if the operation would otherwise be allowed. A managed ask rule can't be satisfied by bypass mode (also known as allow-all or YOLO mode), an auto-approval setting, a hook or other approval shortcut, or a grant persisted from an earlier approval. The same operation prompts again the next time it's requested."
- **Our assessment**: The `ask` rule's list of things it explicitly cannot be satisfied
  by — bypass mode, auto-approval, hook shortcuts, and persisted grants — is a direct,
  named closure of every automation escape hatch a developer might otherwise use to avoid
  a human-in-the-loop approval, including automation mechanisms (hooks) that this same
  corpus documents elsewhere as legitimate developer productivity tools. This is a
  materially stronger guarantee than `disableBypassPermissionsMode` alone provided: that
  June 17 control only blocked bypass-mode activation; this `ask` semantics additionally
  guarantees no *other* mechanism (hook, cached approval) can silently satisfy a specific
  managed approval requirement. The `allow`-list-as-intersection rule mirrors the same
  "most-restrictive-operator-wins" pattern documented for `allowedMcpServers` in
  `docs-github-copilot-mcp-allowlists-enterprise.md` Claim 9 — both use intersection for
  multi-source allow combination, so a second settings source adding an allow list can
  only narrow, never widen, what is auto-approved.

### Claim 11: Each `permissions.deny`/`ask`/`allow` subkey is overridable for enterprise teams by wrapping the enterprise-level rule array in `{ "overridable": <VALUE> }`, then using ordinary array syntax to define replacement rules in each team's file

- **Evidence**: Linked reference page, team-override subsection following the selector
  documentation (raw-HTML-verified).
- **Confidence**: settled (mechanism stated directly on official reference page)
- **Quote**: "Each subkey is overridable for enterprise teams. Set the enterprise value to { \"overridable\": <VALUE> }, replacing <VALUE> with the rule array. Then use the regular syntax to define replacement rules in each team's file."
- **Our assessment**: This confirms the deny/ask/allow rule engine is the third named
  capability (after `permissions.model`/`permissions.disableBypassPermissionsMode` from
  August 3, and `allowedMcpServers`/`deniedMcpServers` from August 6) to plug into the
  `overridable` team-specialization mechanism, extending
  `docs-github-copilot-mcp-allowlists-enterprise.md` Claim 5's finding that `overridable`
  is not scoped to the `permissions` object alone. Note the semantics differ from the
  additive `enabledPlugins`/`extraKnownMarketplaces` keys documented in
  `docs-github-copilot-enterprise-team-specialization-managed-settings.md` Claim 7: an
  overridable `deny`/`ask`/`allow` array is *replaced* wholesale by a team's file, not
  merged with the enterprise array — a team that overrides `deny` must re-specify every
  rule it still wants blocked, or risk silently dropping an enterprise-level `deny` rule
  the team didn't intend to remove.

### Claim 12: In VS Code, the granular `deny`/`ask`/`allow` permission rules apply only to Copilot sessions that use Agent Host, while `permissions.disableBypassPermissionsMode` has broader VS Code support and isn't limited to Agent Host

- **Evidence**: Linked reference page, scope note immediately preceding the deny/ask/allow
  explanation (raw-HTML-verified).
- **Confidence**: settled (scope distinction stated directly on official reference page)
- **Quote**: "In VS Code, these granular permission rules apply to Copilot sessions that use Agent Host. The permissions.disableBypassPermissionsMode setting has broader VS Code support and isn't limited to Agent Host."
- **Our assessment**: This is a specific, citable caveat the changelog's own summary
  ("generally available in... Visual Studio Code sessions that use Agent Host," Claim 5)
  states but does not explain the significance of: an enterprise that has confirmed
  `disableBypassPermissionsMode` is active enterprise-wide in VS Code should not assume the
  new operation-level `deny`/`ask`/`allow` rules carry the same reach — a VS Code Copilot
  session that does not use Agent Host is bound by the bypass-mode toggle but not by the
  granular Shell/Read/Edit/Domain rules. For Ch02: flag this as a required verification
  step (confirm which VS Code Copilot session types in the organization use Agent Host)
  before treating the deny/ask/allow rules as enterprise-wide-enforced in VS Code.

### Claim 13: Per the reference page's client-support table, `permissions.deny`, `permissions.ask`, and `permissions.allow` are each supported in Copilot CLI, VS Code, and the GitHub Copilot app, but explicitly not supported in the Copilot cloud agent or in JetBrains IDEs; `permissions.disableBypassPermissionsMode` additionally is supported in JetBrains IDEs (but still not in the Copilot cloud agent)

- **Evidence**: Linked reference page, "Supported keys" table, per-column
  `octicon-check`/`octicon-x` icons with `aria-label="Supported"`/`"Not supported"` for
  each of the five client columns (Copilot CLI, VS Code, GitHub Copilot app, Copilot cloud
  agent, JetBrains IDEs), extracted directly from the table's raw HTML rather than its
  rendered/summarized text.
- **Confidence**: settled (support matrix directly observable in the official reference
  page's raw table markup)
- **Quote**: (no single prose sentence states the full matrix; the `aria-label` values are
  the source's own accessibility text for each checkmark/x icon, not a summarized
  reconstruction — see Extraction Notes for the exact per-cell values)
- **Our assessment**: This table is more precise than the changelog's prose summary
  (Claim 5), which names only three supported clients without stating that JetBrains
  support differs between `disableBypassPermissionsMode` (supported) and
  `deny`/`ask`/`allow` (not supported) — an administrator relying solely on the changelog
  text could reasonably but incorrectly assume JetBrains inherits the same permission
  model uniformly. For Ch02/Ch06: the guide's client-support reference for
  `managed-settings.json` permissions should be a per-key matrix, not a single "supported
  clients" list, since different keys in the same `permissions` object now have materially
  different client reach.

### Claim 14: The `model` key, previously documented as nested under `permissions.model`, is now a top-level key in `managed-settings.json`; clients still read the nested `permissions.model` value when the top-level `model` key is absent, but new configurations should use the top-level key

- **Evidence**: Linked reference page, note immediately following the "Example
  configuration" JSON block (raw-HTML-verified).
- **Confidence**: settled (schema migration stated directly on official reference page,
  with explicit backward-compatibility guarantee)
- **Quote**: "model was originally documented as permissions.model. Clients still read the nested permissions.model value when the top-level model key is absent, but you should use the top-level model key in new configurations."
- **Our assessment**: This is a schema evolution, not a contradiction between sources: the
  July 1 note (`docs-github-copilot-enterprise-auto-model-default.md`, Claim 8, rated
  `emerging`) and the August 6 note's own example JSON
  (`docs-github-copilot-mcp-allowlists-enterprise.md`, Concrete Artifacts) both correctly
  documented `model` as nested under `permissions` at the time they were written — that
  was accurate for the schema as it existed on July 1 and August 6, 2026. The reference
  page fetched today (September 10, 2026, reflecting content current as of at least the
  September 9 changelog) documents the same fact this note's own Concrete Artifacts JSON
  example shows: `model` now appears as a top-level sibling to `permissions`, not nested
  inside it. Because the source itself states the backward-compatibility path explicitly
  (old nested value still read when top-level key is absent), this does not rise to a
  MINER.md §4a filing-worthy contradiction — both prior notes were accurate for their own
  extraction date, and the current source reconciles the two states itself rather than
  disagreeing with either. For Ch02: update any guide JSON schema examples that show
  `permissions.model` to use the top-level `model` key, and add a note that the nested
  form remains valid only as a fallback.

## Concrete Artifacts

### Changelog full text (github.blog, September 9, 2026, raw HTML)

```
If you administer GitHub Copilot Business or GitHub Copilot Enterprise, you can now
centrally control which agent operations are blocked, require human approval, or can
proceed without a prompt.

Managed permissions cover shell commands, file reads and edits, and network domains.
This gives you fine-grained guardrails for sensitive operations without disabling
agent workflows. Managed restrictions can't be weakened by user or workspace settings,
auto-approval, or previously saved approvals. You can also provide specialized
policies for different enterprise teams.

These controls are generally available in the GitHub Copilot app, GitHub Copilot CLI,
and Visual Studio Code sessions that use Agent Host.

Learn more about enterprise managed permissions [links to
docs.github.com/enterprise-cloud@latest/copilot/reference/enterprise-administrators/enterprise-managed-settings#deny-ask-allow].

Share feedback and implementation questions in the GitHub Community discussion
[links to github.com/orgs/community/discussions/199139].
```
*Source: raw HTML of the changelog page, fetched via `curl`, tag-stripped. Byline
"Allison"; `datePublished` 2026-09-09T20:08:14+00:00 per the page's JSON-LD; category
tag "Improvement"; listed read time "1 minute read".*

### `permissions` rule-engine example (from the linked "Enterprise managed settings" reference page, raw HTML)

```json
{
  "model": "auto",
  "permissions": {
    "disableBypassPermissionsMode": "disable",
    "deny": [
      "Shell(rm -rf *)",
      "Read(~/.ssh/**)",
      "Edit(//etc/**)",
      "Domain(*.unapproved.example)"
    ],
    "ask": [
      "Shell(git push *)",
      "Edit(/src/**)",
      "Domain(api.github.com)"
    ],
    "allow": [
      "Shell(npm test *)",
      "Read(/src/**)",
      "Domain(registry.npmjs.org)"
    ]
  }
}
```
*Source: "Enterprise managed settings" reference page → "Example configuration"
section (full page example includes `enabledPlugins`/`extraKnownMarketplaces` keys
not shown here as out of scope for this note; abbreviated to the `model` and
`permissions` keys relevant to this changelog). Verified against raw page HTML, not a
WebFetch summary.*

### Selector reference (from the linked reference page, raw HTML)

```
Shell(...)   Shell commands. "<command> *" matches a command prefix (e.g. "git push *");
             otherwise matches exact text. Bash(...) is a compatibility alias.
             PowerShell(...) is the same family with case-insensitive matching.
Read(...)    File read/view paths. Supports globs and roots: // (filesystem root),
             / (workspace root), ~/ (home directory), ./ (current working directory).
Edit(...)    File write/edit paths, matched the same way as Read(...). Write(...) is
             an alias for Edit(...).
Domain(...)  Network origins. A bare host defaults to HTTPS, host matching is
             case-insensitive. "*." includes subdomains (e.g. *.example.com matches
             example.com and its subdomains).
```
*Source: reference page selector table, reproduced from raw HTML.*

### Client support matrix (from the linked reference page's "Supported keys" table, raw HTML `aria-label` values)

```
Key                                          CLI   VS Code  Copilot app  Cloud agent  JetBrains
permissions.disableBypassPermissionsMode     Yes   Yes      Yes          No           Yes
permissions.deny                             Yes   Yes      Yes          No           No
permissions.ask                              Yes   Yes      Yes          No           No
permissions.allow                            Yes   Yes      Yes          No           No
```
*Source: reference page "Supported keys" table, `<svg class="octicon-check"
aria-label="Supported">` / `<svg class="octicon-x" aria-label="Not supported">` icons
per cell, extracted from raw table HTML for the four `permissions.*` rows. "VS Code"
column applies specifically to Agent Host sessions for the deny/ask/allow rows per
Claim 12.*

### Enterprise-Managed Settings Capability Map (updated to September 9, 2026)

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
4. permissions.model: auto default (July 1, 2026; model later promoted to a
   top-level key — see Claim 14)
   Source: docs-github-copilot-enterprise-auto-model-default.md
5. remoteControl device restriction (July 30, 2026)
   Source: docs-github-copilot-cli-remote-control-managed-devices.md
6. Team-level specialization / overridable keys (August 3, 2026)
   Source: docs-github-copilot-enterprise-team-specialization-managed-settings.md
7. allowedMcpServers / deniedMcpServers, GA (August 6, 2026)
   Source: docs-github-copilot-mcp-allowlists-enterprise.md
8. permissions.deny / permissions.ask / permissions.allow operation-level rule
   engine (September 9, 2026) ← THIS NOTE
   - Shell()/Bash()/PowerShell(), Read(), Edit()/Write(), Domain() selectors
   - deny > ask > allow precedence; unmatched ops default to "requires approval"
     once any rule or allow-list exists; allow = intersection across sources
   - overridable (extends the Aug 3 team-specialization mechanism)
   - NOT supported on Copilot cloud agent or JetBrains IDEs (unlike
     disableBypassPermissionsMode, which JetBrains does support)
   Source: docs-github-copilot-enterprise-agent-operations-permissions.md
```
*Source: synthesis across all eight enterprise-managed-settings source notes to date,
in chronological order of changelog publication.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claims 1–2 and 6–8: the
    `permissions` object, `.github-private`/`copilot/managed-settings.json`
    configuration surface, and Copilot Business/Enterprise license gate are all
    reaffirmed unchanged as the substrate this new rule engine is added to.
  - `docs-github-copilot-mcp-allowlists-enterprise.md` Claim 9 (allow = intersection
    across multi-source combination): this note's Claim 10 documents the identical
    most-restrictive-wins intersection rule for `permissions.allow`, the second
    corpus instance of this specific combination operator applied to a different key
    pair in the same schema.
  - `docs-github-copilot-enterprise-team-specialization-managed-settings.md` Claim 4
    (the `overridable` mechanism) and `docs-github-copilot-mcp-allowlists-enterprise.md`
    Claim 5 (extending `overridable` beyond the `permissions.model`/
    `disableBypassPermissionsMode` pair): this note's Claim 11 is the third
    confirmation that `overridable` is a general-purpose mechanism applicable across
    the growing `managed-settings.json` schema, not scoped to any one key family.

- **Extends**:
  - `docs-github-copilot-enterprise-bypass-permissions.md`: that June 17 note
    documented a single binary control (`disableBypassPermissionsMode`) that could
    only force approval-for-everything or leave bypass mode available. This note adds
    a strictly more expressive operation-level rule engine on top of the same
    `permissions` object — an enterprise can now combine a coarse
    `disableBypassPermissionsMode: "disable"` floor with fine-grained per-operation
    `deny`/`ask`/`allow` rules, rather than choosing one or the other.
  - `docs-github-copilot-mcp-allowlists-enterprise.md`: that August 6 note documented
    allow/deny admission control at the *MCP server* level (whether a server may run
    at all). This note documents allow/deny/ask control at the *operation* level
    (shell/file/network) once an agent — using any tool, including an MCP server — is
    already running. Neither source states whether an operation performed *through* an
    allowed MCP server (e.g., a shell command issued via an MCP tool call) is
    additionally subject to the `permissions.deny`/`ask`/`allow` rules documented here,
    or whether MCP-mediated operations bypass this operation-level engine. This is
    flagged as an open interaction question below, not a contradiction.
  - `docs-github-copilot-enterprise-team-specialization-managed-settings.md`: adds
    `permissions.deny`/`ask`/`allow` as a third named example (after
    `permissions.model`/`disableBypassPermissionsMode` and
    `allowedMcpServers`/`deniedMcpServers`) of a key family eligible for the
    `overridable` mechanism — but with array-replacement rather than the additive
    semantics of `enabledPlugins`/`extraKnownMarketplaces` documented in that note's
    Claim 7 (see Claim 11's assessment above).

- **Contradicts**: None filed as a formal contradiction issue. Claim 14 documents a
  schema migration (`permissions.model` → top-level `model`) that superficially looks
  like a disagreement with two prior source notes, but the current reference page
  itself states the backward-compatibility path explicitly, and both prior notes were
  accurate as of their own extraction dates — per MINER.md §4a this is a documented
  evolution over time, not two sources making opposing claims about the same present
  state, so no contradiction issue was filed. One open interaction question is noted
  (not filed, consistent with the "gap, not disagreement" standard used throughout this
  source-note family): whether operations performed through an MCP tool call are
  additionally subject to the `permissions.deny`/`ask`/`allow` engine documented here,
  alongside the MCP server-admission rules from
  `docs-github-copilot-mcp-allowlists-enterprise.md`. Neither source states this
  interaction.

- **Novel**:
  - **Operation-level deny/ask/allow rule engine**: first corpus documentation of a
    rule-based (as opposed to single-flag) permission-governance mechanism for
    GitHub Copilot agent operations, with named selector types (`Shell`, `Read`,
    `Edit`, `Domain`) and glob/prefix matching syntax.
  - **`ask` as a named, non-bypassable rule type distinct from `deny`/`allow`**: first
    corpus documentation of a managed-settings rule type whose entire purpose is
    forcing a fresh human approval every time, with an explicit, itemized list of
    mechanisms (bypass mode, auto-approval, hooks, persisted grants) that cannot
    satisfy it.
  - **Per-key client-support divergence within the same `permissions` object**: first
    corpus documentation that different keys nested under the same top-level
    `permissions` object (`disableBypassPermissionsMode` vs. `deny`/`ask`/`allow`)
    have different client support (JetBrains supports the former, not the latter).
  - **VS Code scope limited to Agent Host sessions specifically for these keys**: first
    corpus documentation of a `managed-settings.json` key whose VS Code enforcement is
    explicitly narrower (Agent Host sessions only) than another key
    (`disableBypassPermissionsMode`) in the same object.
  - **`model` key promoted from nested to top-level with stated backward
    compatibility**: first corpus documentation of an in-place schema migration for
    an existing `managed-settings.json` key, with the vendor explicitly stating the
    fallback-read behavior for the old location.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Add `permissions.deny`/`permissions.ask`/`permissions.allow` as capability #8 in
    the `managed-settings.json` schema reference, using the capability map, selector
    reference, and client-support matrix in Concrete Artifacts as the suggested
    structure. This supersedes any prior guide text implying
    `disableBypassPermissionsMode` is the only operation-governance lever in the
    schema — it is now the coarse-grained complement to this fine-grained rule engine.
  - Reproduce the worked example (Claim 8) as a starting-point policy for readers
    configuring their first enterprise permission ruleset: deny destructive
    shell/credential/system-path/untrusted-domain operations, require approval for
    version-control pushes and source edits, auto-allow test runs and known-good
    registries.
  - Document the `Read(...)`/`Edit(...)` path-root distinction (`//` filesystem root
    vs. `/` workspace root) as a common misconfiguration risk (Claim 7) — a rule
    intended to protect `/etc` that omits the second slash will silently fail to match.
  - Document the default-to-approval fallback triggered by defining *any* rule (Claim
    9) as an operational gotcha: adding a single `deny` rule changes the default
    disposition for every other unmatched operation enterprise-wide.
  - Replace any guide JSON examples showing `permissions.model` (nested) with the
    top-level `model` key per Claim 14, noting the nested form as a legacy fallback
    only.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Add the per-key client-support matrix (Claim 13) as a required verification step
    before an organization relies on `deny`/`ask`/`allow` rules for compliance
    purposes on JetBrains IDEs or the Copilot cloud agent — neither client enforces
    these keys, unlike `disableBypassPermissionsMode`, which JetBrains does enforce.
  - Extend the existing "least restrictive value wins" multi-team governance-review
    guidance (from `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
    Claim 10) to explicitly include overridable `deny`/`ask`/`allow` arrays: because
    overriding these keys replaces the array wholesale rather than merging (Claim 11),
    a team override that forgets to re-specify an enterprise `deny` rule silently drops
    that protection for the team's members — a distinct, additional risk beyond the
    cross-team combination risk already documented.

- **Chapter 06/07 (Safety & Security / Enterprise Operations)**:
  - Add the `ask` rule's explicit non-bypassability list (bypass mode, auto-approval,
    hooks, persisted grants — Claim 10) to the enterprise security hardening
    checklist as the strongest available Copilot control for mandating human review of
    specific high-risk operations, stronger than the binary
    `disableBypassPermissionsMode` toggle alone.
  - Flag the open MCP-interaction question (does an MCP-mediated shell/file/network
    operation pass through this rule engine?) as a verification item for any
    enterprise that has both `allowedMcpServers` and `permissions.deny`/`ask`/`allow`
    configured, since neither source states how the two systems compose.
  - Flag the VS Code Agent Host scope limitation (Claim 12) as a required check for
    any security review claiming deny/ask/allow coverage across an organization's VS
    Code Copilot usage — sessions not using Agent Host are covered only by
    `disableBypassPermissionsMode`, not by the granular rules.

## Extraction Notes

1. **Raw HTML fetch for both pages, not AI-summarized WebFetch**: An initial WebFetch
   call to the changelog returned a plausible-looking but reconstructed summary
   (headers, "Summary"/"Key Capabilities" framing, and quoted sentences not present
   verbatim on the page). This was cross-checked against the changelog's raw HTML
   (fetched via `curl`) and the WebFetch output's quoted sentences did not match the
   raw page text character-for-character in places (e.g., it rendered the content as a
   dated "Summary" section rather than the source's actual four-paragraph prose). All
   quotes and artifacts in this note were instead located and copied directly from the
   raw HTML of both the changelog and the linked "Enterprise managed settings"
   reference page (tag-stripped via a Python script, not passed through an
   AI-summarization step). The Assayer can spot-check any quote against the live URLs
   with higher confidence than for sibling notes that relied on WebFetch summaries.
2. **No explicit GA/preview status label found**: unlike `docs-github-copilot-mcp-allowlists-enterprise.md`
   (which found and quoted "This capability is generally available"), neither the
   changelog nor the deny-ask-allow section of the reference page, as fetched, contains
   an explicit product-maturity label (GA vs. public preview) for the `deny`/`ask`/`allow`
   keys specifically. The changelog's category tag is "Improvement." This is noted as a
   gap rather than inferred either way.
3. **Reference page scope limited to permissions-relevant sections**: the linked
   "Enterprise managed settings" reference page also documents `enabledPlugins`,
   `extraKnownMarketplaces`, `strictKnownMarketplaces`, `telemetry`, `remoteControl`,
   `allowedMcpServers`/`deniedMcpServers`, and `sandbox` in detail. Those sections are
   already covered by seven sibling source notes (see capability map) and were not
   re-extracted here except where needed for schema-structure context supporting Claim
   14 (the `model` key migration).
4. **Community discussion thread not re-fetched in depth**: confirmed the linked
   thread (`github.com/orgs/community/discussions/199139`) is titled "Enterprise-Managed
   Settings for Copilot Business and Copilot Enterprise" — the same long-running general
   feedback thread already characterized as off-topic-for-specific-features by two prior
   notes in this family. Not re-read in full for this extraction; a future miner
   covering a subsequent changelog in this family should check whether
   deny/ask/allow-specific discussion has since accumulated there.
5. **Team-specialization file mechanics (`copilot/teams/`, `team-mappings.json`) not
   re-extracted**: this note's Claim 11 confirms `deny`/`ask`/`allow` participate in
   the `overridable` mechanism, but the file-location and routing mechanics
   (`copilot/teams/*.json`, `team-mappings.json`) are already fully documented in
   `docs-github-copilot-enterprise-team-specialization-managed-settings.md` and were
   not re-verified against the reference page for this note.
