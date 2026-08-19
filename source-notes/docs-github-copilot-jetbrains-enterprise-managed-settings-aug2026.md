---
source_url: https://github.blog/changelog/2026-08-18-enterprise-managed-settings-in-github-copilot-for-jetbrains
source_type: docs
title: "Enterprise managed settings in GitHub Copilot for JetBrains"
author: GitHub (official changelog)
date_published: 2026-08-18
date_extracted: 2026-08-19
last_checked: 2026-08-19
status: current
confidence_overall: settled
issue: "#2775"
---

# Enterprise Managed Settings in GitHub Copilot for JetBrains

> GitHub's August 18, 2026 changelog extends the enterprise `managed-settings.json`
> system — previously documented in this corpus for VS Code, Copilot CLI, the
> GitHub Copilot app, and Copilot cloud agent — to JetBrains IDEs, adding plugin
> governance (`enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`),
> an MCP server allowlist (`allowedMcpServers`/`deniedMcpServers`), managed
> OpenTelemetry, and `permissions.disableBypassPermissionsMode` (there named against
> JetBrains' own "Bypass Approvals"/"Autopilot" terminology). Critically, JetBrains
> uses the *same* `managed-settings.json` schema and the *same* deployment
> mechanisms (server-managed via `.github-private`, MDM-managed, or file-based at
> shared OS-level paths) as VS Code/CLI — not a JetBrains-specific configuration
> file — but does not support every key: `permissions.model`, `remoteControl`, and
> `sandbox` remain unsupported for JetBrains per the reference doc's client matrix.

## Source Context

- **Type**: docs (GitHub official product changelog, August 18, 2026; ~1-minute read,
  tagged `copilot`, `enterprise management tools`). Two linked documentation pages were
  followed per MINER.md §1: the "Enterprise managed settings reference"
  (`docs.github.com/copilot/reference/enterprise-managed-settings-reference`), which
  supplied the per-key client support matrix and full schema detail, and "Configuring
  enterprise-managed settings"
  (`docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings`),
  which supplied the deployment-method and file-path detail. Both pages were fetched
  as raw HTML via `curl` and parsed from the page's embedded `__NEXT_DATA__` JSON
  payload (the site's own rendered-content data, not an AI-summarized WebFetch
  reproduction) — the client-support table was parsed directly from its `<svg
  aria-label="Supported"|"Not supported">` markup rather than transcribed by eye or
  by an intermediate summarizer.
- **Author credibility**: GitHub engineering team announcing a production capability
  extension to the enterprise-managed-settings system, which has been the subject of
  seven prior corpus source notes (June 5, June 17, June 25, July 1, Aug 3, Aug 6,
  2026 — see Cross-References). Authoritative for: the existence and behavior of each
  named JetBrains capability, the settings UI path for developer-visible OTel
  configuration, and (via the reference page) the definitive per-key, per-client
  support matrix. Not a credible source for: real-world JetBrains admin-console
  UX, whether `enabledPlugins`/`strictKnownMarketplaces` enforcement differs
  mechanically between the JetBrains plugin runtime and VS Code's extension runtime,
  or adoption data.
- **Scope**: Four JetBrains-specific capabilities announced in the changelog
  (enterprise-managed plugin governance, MCP server allowlist, managed OpenTelemetry,
  organization-controlled permission modes), cross-checked against the reference
  page's exhaustive "Supported keys" table (10 keys × 5 clients) and the "Configuring
  enterprise-managed settings" page's deployment-method and file-path documentation.
  Does NOT cover: JetBrains-specific UI screenshots or exact settings-panel layout
  beyond the stated `Settings > Tools > GitHub Copilot > Chat > OpenTelemetry` path,
  or whether the four newly-announced capabilities reached JetBrains simultaneously
  with a specific plugin version floor (no JetBrains plugin version number is stated
  in the changelog, unlike the VS Code 1.122+/1.126+ floors documented in prior notes
  in this family).

## Extracted Claims

### Claim 1: GitHub Copilot for JetBrains now supports enterprise managed settings for plugin governance, MCP server access, OpenTelemetry, and permission modes, letting administrators apply consistent controls across the enterprise's Copilot plan

- **Evidence**: Changelog lead paragraph, stated as the single-sentence summary of
  the entire release.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "GitHub Copilot for JetBrains now supports enterprise managed settings for plugin governance, MCP server access, OpenTelemetry, and permission modes. Administrators can now apply consistent controls for everyone on your enterprise's Copilot plan."
- **Our assessment**: This confirms, in full detail, what `docs-github-copilot-weekly-releases-aug10-2026.md` (Claim 13) could only report at a distance eight days earlier: "these enterprise managed settings cover plugin availability, MCP server access, permission bypass behavior, and OpenTelemetry settings," sourced from a link that note explicitly did not fetch. The four category names match exactly between the two sources. For Ch02 (Harness Engineering — Enterprise Configuration): JetBrains joins VS Code, Copilot CLI, the GitHub Copilot app, and Copilot cloud agent as a client governed by the same `managed-settings.json` system — this is the fifth (and, per the reference page's table, final-listed) client to gain enterprise-managed-settings coverage in the corpus's timeline.

### Claim 2: Administrators can require a JetBrains plugin to be enabled or disabled via `enabledPlugins`, make approved plugin sources available via `extraKnownMarketplaces`, and limit installation to approved sources via `strictKnownMarketplaces`

- **Evidence**: Changelog "Enterprise-managed plugin governance" section, naming all
  three keys against JetBrains explicitly.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Administrators can manage Copilot plugins and their marketplaces in JetBrains IDEs. The supported settings provide three controls: Enabled plugins: Use enabledPlugins to require a plugin to be enabled or disabled. Additional marketplaces: Use extraKnownMarketplaces to make approved plugin sources available. Restricted marketplaces: Use strictKnownMarketplaces to limit installation to approved sources."
- **Our assessment**: These three keys were previously documented in this corpus scoped only to VS Code and Copilot CLI (`docs-github-copilot-enterprise-managed-plugins-vscode.md` for `enabledPlugins`/`extraKnownMarketplaces`; `docs-github-copilot-enterprise-strict-known-marketplaces.md` for `strictKnownMarketplaces`, whose Claim 3 frames the control as supply-chain governance operating "prior to tool execution"). This changelog extends the identical key names, with identical semantics, to JetBrains — confirmed independently by the reference page's table, which marks all three keys `Supported` for JetBrains IDEs. No new key names or JetBrains-specific variants are introduced; the schema is reused verbatim. For Ch02: the supply-chain framing established for VS Code/CLI (whitelist marketplace restriction, install-time enforcement) now applies equally to JetBrains plugin installs.

### Claim 3: Administrators can use `allowedMcpServers` and `deniedMcpServers` to centrally control which MCP servers JetBrains developers can connect to, bringing centrally managed MCP governance into JetBrains IDEs and preventing connections to servers outside the enterprise allowlist

- **Evidence**: Changelog "MCP server allowlist" section.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Administrators can use allowedMcpServers and deniedMcpServers to centrally control which MCP servers developers can connect to from GitHub Copilot for JetBrains. This brings centrally managed MCP governance into JetBrains IDEs and prevents connections to servers outside the enterprise allowlist."
- **Our assessment**: This extends `docs-github-copilot-mcp-allowlists-enterprise.md` (GA as of Aug 6, 2026; that note's Claim 6 explicitly listed the supported-client set as "the GitHub Copilot app, Copilot CLI and VS Code" — JetBrains was absent). This Aug 18 changelog closes that gap 12 days later. The reference page's table confirms `allowedMcpServers`/`deniedMcpServers` = `Supported` for JetBrains. That note's Claims 2, 3, and 12 documented the `serverUrl`/`serverCommand`/`serverName` matcher types and URL-canonicalization anti-evasion rules; this changelog does not restate those mechanics for JetBrains specifically, so it is reasonable to assume — but not independently confirmed by this source — that the same matcher schema applies uniformly. For Ch02 (MCP Configuration): update the client-support note in the MCP allowlist section from "GitHub Copilot app, Copilot CLI, VS Code" to include JetBrains IDEs as of Aug 18, 2026.

### Claim 4: Administrators can centrally configure OpenTelemetry for JetBrains, including collector endpoint, protocol, service name, resource attributes, and content-capture policy, and managed values take precedence over developer settings; developers can review the applied configuration under Settings > Tools > GitHub Copilot > Chat > OpenTelemetry

- **Evidence**: Changelog "Managed OpenTelemetry" section, including the specific
  settings-UI path where the *effective* (administrator-applied) configuration is
  surfaced to the individual developer.
- **Confidence**: settled (product fact, official changelog) — see Extraction Notes
  and the filed contradiction (issue #2802) for a caveat on whether this is fully
  reflected in the reference doc's per-key prose.
- **Quote**: "Administrators can centrally configure OpenTelemetry for Copilot in JetBrains IDEs, including the collector endpoint, protocol, service name, resource attributes, and content-capture policy. Managed values take precedence over developer settings, so telemetry is consistently routed to the approved collector. Developers can review the applied configuration under Settings > Tools > GitHub Copilot > Chat > OpenTelemetry."
- **Our assessment**: This is the enterprise-governed counterpart to
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md` (Claim 1), which
  documented OpenTelemetry as an individually-configurable, practitioner-facing
  setting at the identical UI path (`Settings > Tools > GitHub Copilot > Chat`) three
  weeks earlier (July 27, 2026) — that note explicitly flagged the underlying export
  schema as undocumented at the time. This changelog both names the schema fields
  (endpoint, protocol, service name, resource attributes, content-capture policy —
  matching the `telemetry` key's sub-properties documented on the reference page: `endpoint`,
  `protocol`, `serviceName`, `resourceAttributes`, `captureContent`) and establishes
  that an administrator's `telemetry` block now overrides whatever a JetBrains
  developer configures locally at that same settings path. For Ch02 (Observability):
  the July 27 note's "practitioner-configurable" framing needs a caveat added — as of
  Aug 18, an enterprise administrator's managed value silently takes precedence over
  the developer-visible setting at the same UI location, so the panel is now a
  read-only view of the effective policy for governed organizations, not necessarily
  a developer-editable control.

### Claim 5: Administrators can set `permissions.disableBypassPermissionsMode` to `disable` to prevent the Copilot agent in JetBrains from using Bypass Approvals or Autopilot

- **Evidence**: Changelog "Organization-controlled permission modes" section — the
  only claim in the changelog naming specific JetBrains UI feature names ("Bypass
  Approvals", "Autopilot") for what the key restricts.
- **Confidence**: settled (product fact, official changelog)
- **Quote**: "Administrators can set permissions.disableBypassPermissionsMode to disable to prevent the Copilot agent in JetBrains from using Bypass Approvals or Autopilot."
- **Our assessment**: `disableBypassPermissionsMode` was already documented in this
  corpus (`docs-github-copilot-enterprise-bypass-permissions.md`) as a VS Code/CLI
  control against what that note called "bypass permissions mode"/informally "yolo
  mode." This changelog is the first corpus source to give the *JetBrains-specific*
  UI names for the behavior the key suppresses — "Bypass Approvals" and "Autopilot" —
  which are not the same terms used in the VS Code/CLI note. Whether "Bypass
  Approvals" and "Autopilot" are two distinct JetBrains features both gated by one
  key, or two different UI labels for the same underlying behavior, is not
  disambiguated by the changelog text itself. For Ch02/Ch06 (Safety & Security):
  document that the single `disableBypassPermissionsMode` key maps to differently
  named UI affordances per client — VS Code/CLI's "bypass permissions mode," and
  JetBrains' "Bypass Approvals"/"Autopilot" — a terminology mismatch practitioners
  should be aware of when auditing whether a client-side auto-approval feature is
  actually covered by this enterprise control.

### Claim 6: Per the reference doc's "Supported keys" table, JetBrains IDEs support `permissions.disableBypassPermissionsMode`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`, `telemetry`, `allowedMcpServers`, and `deniedMcpServers`, but do NOT support `permissions.model`, `remoteControl`, or `sandbox`

- **Evidence**: "Enterprise managed settings reference" page, "Supported keys" table,
  columns for Copilot CLI / VS Code / GitHub Copilot app / Copilot cloud agent /
  JetBrains IDEs, parsed directly from the table's `<svg aria-label="Supported">` /
  `aria-label="Not supported">` markup (10 keys × 5 clients).
- **Confidence**: settled (structural table data on the official reference page,
  verified programmatically against raw markup — not a prose sentence or
  AI-summarized reproduction)
- **Quote**: (no single prose sentence states this; the support/non-support values
  are rendered as icons in a table, not text — see Concrete Artifacts for the full
  parsed matrix, reproduced from the table's own cell contents)
- **Our assessment**: This directly answers the Prospector's triage question: JetBrains
  is *not* uniformly covered by every `managed-settings.json` key. The three gaps —
  `permissions.model` (the July 1, 2026 auto-model-selection default documented in
  `docs-github-copilot-enterprise-auto-model-default.md`), `remoteControl` (documented
  in `docs-github-copilot-cli-remote-control-managed-devices.md`), and `sandbox` —
  mean JetBrains enterprises cannot yet enforce a default model-selection mode, cannot
  restrict remote session control, and cannot enforce minimum local sandbox
  restrictions through this mechanism, even though VS Code and/or Copilot CLI can for
  at least some of these keys. For Ch02: the guide's `managed-settings.json`
  capability table should be a per-key × per-client matrix, not a single "supported
  clients" list — this table is the authoritative source for exactly which cells are
  filled for JetBrains specifically, and should be cited rather than assuming
  uniform coverage from the Aug 18 changelog's four-category summary alone.

### Claim 7: Enterprise managed settings can be deployed via three methods — server-managed (a `.github-private` repository, applied hourly with immediate refresh on re-authentication), MDM-managed (native OS policy on Windows/macOS only, not Linux), or file-based (a `managed-settings.json` file placed at a fixed OS-level path) — and these are the same three deployment mechanisms and, for file-based deployment, the same OS-level file paths used for every supported client on that operating system, not a JetBrains-specific configuration file or path

- **Evidence**: "Configuring enterprise-managed settings" page, "Choosing a
  deployment method" and "Deploying file-based settings" sections.
- **Confidence**: settled (deployment mechanics and file paths stated directly on the
  official docs page, raw-HTML/JSON-verified)
- **Quote**: "Place managed-settings.json in the following location: macOS: /Library/Application Support/GitHub Copilot/managed-settings.json. Windows: %ProgramFiles%\GitHub Copilot\managed-settings.json. Linux: /etc/github-copilot/managed-settings.json. [...] Distribute the file to the platform-specific location using your standard device management process. Machines that don't receive the file are not restricted by this policy."
- **Our assessment**: This is the direct answer to the Prospector's key question —
  "What is the JetBrains-specific configuration mechanism... how does it relate to
  the VS Code/CLI model?" The answer is that there is no JetBrains-specific
  mechanism: file-based deployment writes one `managed-settings.json` file per
  machine, at a path keyed to the *operating system*, not the *client application* —
  the same file a VS Code install and a JetBrains install on the same machine would
  both read. Server-managed deployment (the `.github-private`/`copilot/managed-settings.json`
  repository pattern documented across all seven prior notes in this family) is
  likewise client-agnostic — "any user on your enterprise's Copilot plan using
  Copilot CLI or supported clients is governed by those settings, whether or not
  they have access to the `.github-private` repository." For Ch02: the guide should
  state explicitly that `managed-settings.json` is a single governance surface
  shared across all Copilot clients on a device/enterprise, with per-*key* client
  support (Claim 6) rather than per-*client* configuration files being the axis
  administrators need to reason about.

### Claim 8: When multiple settings sources are present, MDM-managed settings take precedence over server-managed settings, which take precedence over file-based settings, which take precedence over user-level settings (with the `sandbox` key as an exception in Copilot CLI, where restrictions from all sources combine in the most restrictive direction instead)

- **Evidence**: "Enterprise managed settings reference" page, "Precedence rules"
  section (opening paragraph of the page).
- **Confidence**: settled (precedence order stated directly on official reference
  page, raw-HTML/JSON-verified)
- **Quote**: "When multiple settings sources are present, settings earlier in this list take precedence over settings later in the list: MDM-managed settings, Server-managed settings, File-based settings, User-level settings. In Copilot CLI, the sandbox key is an exception to these precedence rules. Managed sandbox restrictions from MDM-managed, server-managed, and file-based settings combine with one another and with the user's sandbox settings in the most restrictive direction."
- **Our assessment**: This precedence order was not explicitly stated as a fixed list in any prior corpus note in this family — prior notes documented individual deployment methods but not a single ranked precedence order across all three (plus user-level). Since `sandbox` is not supported for JetBrains at all (Claim 6), the stated exception for `sandbox`'s combine-restrictively behavior is moot for JetBrains specifically, but matters for any guide passage that generalizes precedence rules across all `managed-settings.json` keys and clients. For Ch02: document the four-tier precedence order (MDM > server > file > user) as the general rule, with the `sandbox`-key combination exception scoped explicitly to Copilot CLI, not JetBrains.

## Concrete Artifacts

### Full "What's new" section content (changelog, verbatim, raw-HTML-extracted)

```
GitHub Copilot for JetBrains now supports enterprise managed settings
for plugin governance, MCP server access, OpenTelemetry, and permission
modes. Administrators can now apply consistent controls for everyone on
your enterprise's Copilot plan.

Enterprise-managed plugin governance
Administrators can manage Copilot plugins and their marketplaces in
JetBrains IDEs. The supported settings provide three controls:
- Enabled plugins: Use enabledPlugins to require a plugin to be enabled
  or disabled.
- Additional marketplaces: Use extraKnownMarketplaces to make approved
  plugin sources available.
- Restricted marketplaces: Use strictKnownMarketplaces to limit
  installation to approved sources.

MCP server allowlist
Administrators can use allowedMcpServers and deniedMcpServers to
centrally control which MCP servers developers can connect to from
GitHub Copilot for JetBrains. This brings centrally managed MCP
governance into JetBrains IDEs and prevents connections to servers
outside the enterprise allowlist.

Managed OpenTelemetry
Administrators can centrally configure OpenTelemetry for Copilot in
JetBrains IDEs, including the collector endpoint, protocol, service
name, resource attributes, and content-capture policy. Managed values
take precedence over developer settings, so telemetry is consistently
routed to the approved collector.
Developers can review the applied configuration under Settings > Tools
> GitHub Copilot > Chat > OpenTelemetry.

Organization-controlled permission modes
Administrators can set permissions.disableBypassPermissionsMode to
disable to prevent the Copilot agent in JetBrains from using Bypass
Approvals or Autopilot.

Try the latest version of the GitHub Copilot plugin for JetBrains and
share your feedback. For more details on enterprise managed settings,
see enterprise managed settings reference.
```
Source: GitHub Copilot for JetBrains changelog, github.blog, August 18, 2026
(raw HTML fetched via `curl`, tags stripped, HTML entities decoded).

### `managed-settings.json` Supported Keys × Client Matrix (from linked reference page, parsed from table markup)

```
Key                                      CLI  VSCode  CopilotApp  CloudAgent  JetBrains
permissions.disableBypassPermissionsMode  Y     Y         Y           N          Y
permissions.model                         Y     Y         Y           Y          N
enabledPlugins                            Y     Y         Y           Y          Y
extraKnownMarketplaces                    Y     Y         Y           Y          Y
strictKnownMarketplaces                   Y     Y         Y           Y          Y
telemetry                                 Y     Y         N           N          Y  (see Extraction Notes / issue #2802)
remoteControl                             Y     Y         Y           N          N
allowedMcpServers                         Y     Y         Y           N          Y
deniedMcpServers                          Y     Y         Y           N          Y
sandbox                                   Y     N         N           N          N
```
Source: "Enterprise managed settings reference"
(docs.github.com/copilot/reference/enterprise-managed-settings-reference),
"Supported keys" table, parsed from the page's embedded `__NEXT_DATA__` JSON
(`articleContext.renderedPage`) by matching each row's `<code>` key name
against its five `<svg aria-label="Supported"|"Not supported">` cells, not
transcribed from a rendered screenshot or AI summary. Fetched 2026-08-19.

### File-based deployment paths (from "Configuring enterprise-managed settings" page, verbatim)

```
Operating system | File location
macOS             /Library/Application Support/GitHub Copilot/managed-settings.json
Windows           %ProgramFiles%\GitHub Copilot\managed-settings.json
Linux             /etc/github-copilot/managed-settings.json

"For Copilot CLI on macOS and Linux, make the file a regular file owned
by root, and ensure it is not group-writable or world-writable. Do not
use a symbolic link. The CLI rejects files that do not meet these
requirements."

Native MDM delivery (Windows/macOS only, not Linux):
  Windows: String (REG_SZ) values under
    HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GitHubCopilot
  macOS: String values in forced managed preferences for the
    com.github.copilot preference domain
  "All native MDM values must be strings. For nested settings, use a
  dot-separated key such as permissions.disableBypassPermissionsMode or
  sandbox.enabled. Store ordinary string values directly. Store
  booleans, arrays, and objects as JSON text within a string value."
```
Source: "Configuring enterprise-managed settings" page
(docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings),
raw HTML/JSON-extracted, fetched 2026-08-19. Note: these file locations and
MDM registry/preference-domain keys are not scoped to a specific client
application anywhere on the page — they are described purely per operating
system, corroborating Claim 7.

### Enterprise-Managed Settings Capability Map (updated to August 18, 2026)

```
Configuration surface: .github-private source-org repository
Enterprise file:  copilot/managed-settings.json  (legacy compat: .github/copilot/settings.json)

Capabilities and client rollout to date (chronological):
1. Plugin distribution + hooks/MCP-always-enabled (June 5, 2026) — VS Code, CLI
2. disableBypassPermissionsMode (June 17, 2026) — VS Code, CLI
3. strictKnownMarketplaces, public preview (June 25, 2026) — VS Code, CLI
4. permissions.model: auto default (July 1, 2026) — VS Code 1.126+, CLI
5. remoteControl device restriction (July 30, 2026) — VS Code, CLI, Copilot app
6. Team-level specialization / overridable keys (Aug 3, 2026) — VS Code, CLI,
   Copilot app, Copilot cloud agent
7. allowedMcpServers / deniedMcpServers, GA (Aug 6, 2026) — Copilot app, CLI, VS Code
8. JetBrains IDEs added as a supported client (Aug 18, 2026) ← THIS NOTE
   - enabledPlugins, extraKnownMarketplaces, strictKnownMarketplaces: Supported
   - allowedMcpServers, deniedMcpServers: Supported
   - telemetry: Supported (per table; contradicted by reference-page prose — see issue #2802)
   - permissions.disableBypassPermissionsMode: Supported
   - permissions.model, remoteControl, sandbox: NOT supported for JetBrains
   Source: docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md
```
Source: synthesis across all eight enterprise-managed-settings source notes to
date, in chronological order of changelog publication.

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-weekly-releases-aug10-2026.md` (Claim 13): that note's
    four-category summary ("plugin availability, MCP server access, permission
    bypass behavior, and OpenTelemetry settings"), extracted from a link the note
    explicitly did not fetch, is confirmed in full by this dedicated changelog —
    the category names match exactly.
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` (Claim 3) and
    `docs-github-copilot-enterprise-strict-known-marketplaces.md` (Claims 1-4): the
    plugin-governance key names (`enabledPlugins`, `extraKnownMarketplaces`,
    `strictKnownMarketplaces`) and their VS Code/CLI semantics are reused verbatim
    for JetBrains, with no JetBrains-specific variant introduced.
  - `docs-github-copilot-mcp-allowlists-enterprise.md` (Claim 1): the
    `allowedMcpServers`/`deniedMcpServers` admission-gate model ("Approve the MCP
    servers your developers depend on and block untrusted or non-compliant ones
    across your enterprise") is reused for JetBrains without any stated schema
    change.
  - `docs-github-copilot-enterprise-bypass-permissions.md` (Claim 1): the
    `disableBypassPermissionsMode` key and `"disable"` value are unchanged; only the
    UI-facing feature names it suppresses differ by client (see Claim 5 above).

- **Contradicts**: **Issue #2802** (filed by this extraction). The "Enterprise
  managed settings reference" page's structured "Supported keys" table marks
  `telemetry` = Supported for JetBrains IDEs (Claim 6/Concrete Artifacts), directly
  consistent with this changelog's "Managed OpenTelemetry" section (Claim 4). But
  the same reference page's own prose description of the `telemetry` key states
  verbatim: "This property is supported for Copilot CLI and VS Code" — omitting
  JetBrains. This is a self-contradiction within the linked reference doc, not a
  disagreement between two independent sources. No verdict is picked here; see
  issue #2802 for the full Side A/Side B framing.

- **Extends**:
  - `docs-github-copilot-jetbrains-otel-model-management-july2026.md` (Claim 1):
    that note documented JetBrains OpenTelemetry as an individually-configurable
    setting at `Settings > Tools > GitHub Copilot > Chat`, with the export schema
    explicitly flagged as undocumented. This note both supplies the schema field
    names (endpoint, protocol, service name, resource attributes, content-capture
    policy) and establishes that administrator-managed values now override the
    developer-facing setting at that same path — a governance layer the July 27
    note could not have anticipated.
  - `docs-github-copilot-enterprise-team-specialization-managed-settings.md`
    (Claim 11): that Aug 3 note's supported-client list for `managed-settings.json`
    enforcement ("VS Code, Copilot CLI, the Copilot App, and Copilot cloud agent")
    did not include JetBrains. This changelog adds JetBrains as a fifth enforced
    client 15 days later — though Claim 6 above shows JetBrains support is
    per-key, not blanket, unlike that note's claim about the other four clients.
  - `docs-github-copilot-mcp-allowlists-enterprise.md` (Claim 6): that Aug 6 note's
    client list for the MCP allowlist ("the GitHub Copilot app, Copilot CLI and VS
    Code") is extended to include JetBrains IDEs, 12 days later.
  - `docs-github-copilot-enterprise-bypass-permissions.md`: extends the
    `disableBypassPermissionsMode` control's client reach from VS Code/CLI to
    JetBrains, while introducing JetBrains-specific terminology ("Bypass Approvals",
    "Autopilot") for what it suppresses — not previously documented anywhere in the
    corpus.

- **Novel**:
  - **First corpus source with a definitive, structurally-verified per-key ×
    per-client support matrix** for the entire `managed-settings.json` schema
    (Claim 6/Concrete Artifacts) — prior notes documented client support piecemeal,
    per capability, as each was announced; this is the first single authoritative
    table covering all 10 keys against all 5 clients simultaneously.
  - **First corpus confirmation that file-based deployment paths are OS-scoped, not
    client-scoped** (Claim 7) — directly resolves the Prospector's triage question
    of whether JetBrains uses a distinct configuration mechanism from VS Code/CLI.
    It does not; JetBrains reads the same `managed-settings.json` file at the same
    OS-level path as every other supported client on that machine.
  - **First corpus documentation of the explicit four-tier precedence order** (MDM
    > server-managed > file-based > user-level) as a single ranked list (Claim 8),
    rather than three independently-described deployment methods without a stated
    relative precedence.
  - **First corpus documentation of client-specific UI terminology for a single
    enterprise-managed key**: `disableBypassPermissionsMode` maps to "bypass
    permissions mode" in VS Code/CLI documentation but to "Bypass Approvals"/
    "Autopilot" in the JetBrains changelog (Claim 5) — the same governance key, two
    different practitioner-facing vocabularies.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Add JetBrains IDEs as the fifth client governed by `managed-settings.json`,
    using the per-key × per-client support matrix (Concrete Artifacts) as the
    authoritative reference — explicitly noting the three gaps (`permissions.model`,
    `remoteControl`, `sandbox` not supported for JetBrains) rather than implying
    uniform coverage from the changelog's four-category summary alone.
  - State explicitly that `managed-settings.json` and its three deployment methods
    (server-managed, MDM-managed, file-based) are shared across all supported
    clients on a device/enterprise — there is no JetBrains-specific configuration
    file or path. Cite the OS-level file-based paths (Concrete Artifacts) as the
    concrete evidence.
  - Document the four-tier precedence order (MDM > server-managed > file-based >
    user-level) as a general `managed-settings.json` rule, noting the `sandbox`-key
    exception is scoped to Copilot CLI only (and moot for JetBrains, which doesn't
    support `sandbox` at all).

- **Chapter 02 (Harness Engineering — Observability)**:
  - Update the JetBrains OpenTelemetry guidance from
    `docs-github-copilot-jetbrains-otel-model-management-july2026.md` to note that,
    as of Aug 18, 2026, an enterprise-managed `telemetry` configuration overrides
    whatever a developer sets locally at the same `Settings > Tools > GitHub
    Copilot > Chat > OpenTelemetry` panel — flag the table-vs-prose discrepancy
    from issue #2802 rather than asserting JetBrains `telemetry` support as
    unconditionally settled until that issue resolves.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Add JetBrains to the enterprise Copilot governance stack alongside VS Code and
    CLI: plugin marketplace whitelisting, MCP server allow/deny, and
    bypass-permission control now all reach JetBrains developers through the same
    administrator workflow (edit `copilot/managed-settings.json` in
    `.github-private`, commit to default branch).
  - Flag the JetBrains-specific "Bypass Approvals"/"Autopilot" terminology (Claim 5)
    as a practical audit note: security reviewers checking whether
    `disableBypassPermissionsMode` actually suppresses JetBrains auto-approval
    behavior should look for these two UI labels, not "bypass permissions mode."

## Extraction Notes

1. **Raw HTML/JSON extraction throughout, not AI-summarized WebFetch**: An initial
   WebFetch call to the changelog URL returned a plausible-looking but
   AI-summarized reproduction (paraphrased headings, e.g. "Enterprise-Managed
   Plugin Governance" rendered as a bolded label rather than the page's actual
   section heading). Per MINER.md §2a, this extraction instead fetched the changelog
   and both linked docs pages via `curl`, and for the two `docs.github.com` pages
   (which are React/Next.js single-page apps whose body text is not present as
   static HTML) parsed the page's own embedded `__NEXT_DATA__` JSON payload
   (`articleContext.renderedPage`) rather than reading the pre-hydration HTML shell.
   The client-support table was parsed programmatically by matching each row's
   `<code>` key name against its `<svg aria-label="Supported"|"Not supported">`
   cells — this is a stronger provenance than manually eyeballing a rendered table
   screenshot or trusting an AI-summarized reproduction. All quotes above were
   copied character-for-character from this raw-extracted text.

2. **Self-contradiction found and filed, not silently resolved**: The reference
   page's `telemetry` key support, per the structural table, includes JetBrains;
   per the key's own prose paragraph, it does not (see Claim 6, Concrete Artifacts,
   and Cross-References → Contradicts). This extraction did not pick a winner —
   contradiction issue #2802 was filed per MINER.md §4a, with both the table
   reading and the prose reading laid out as Side A/Side B for human or Smith
   resolution.

3. **Two linked pages followed, three navigational links skipped**: The "Enterprise
   managed settings reference" and "Configuring enterprise-managed settings" pages
   were both fetched in full per MINER.md §1. The changelog's other links — the
   JetBrains plugin marketplace listing, the `microsoft/copilot-intellij-feedback`
   issue tracker, and the in-product feedback channel — are navigational/
   feedback-channel links, not substantive documentation, and were not followed.

4. **No JetBrains plugin version floor stated**: Unlike the VS Code 1.122+/1.126+
   version floors documented in `docs-github-copilot-enterprise-managed-plugins-vscode.md`
   and `docs-github-copilot-enterprise-auto-model-default.md`, this changelog does
   not state a minimum JetBrains plugin version required for any of the four new
   capabilities. This is a gap relative to the VS Code-side documentation pattern,
   not an inferred "no version requirement" — practitioners should verify against
   the JetBrains Marketplace listing or in-plugin version info before assuming
   universal availability across older plugin installs.

5. **One contradiction filed**: See Cross-References → Contradicts and issue #2802.
   No other contradictions were found against the seven prior notes in this family
   — all other cross-references in this note are corroborating or extending, not
   opposing, claims.
