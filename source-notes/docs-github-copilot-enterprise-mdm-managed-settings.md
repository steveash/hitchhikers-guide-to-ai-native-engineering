---
source_url: https://github.blog/changelog/2026-07-08-deploy-managed-copilot-settings-via-mdm-in-vs-code-and-cli
source_type: docs
title: "Deploy managed Copilot settings via MDM in VS Code and CLI"
author: GitHub (official changelog; byline "Allison")
date_published: 2026-07-08
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: settled
issue: "#1720"
---

# Deploy Managed Copilot Settings via MDM in VS Code and CLI

> GitHub's July 8, 2026 changelog adds two new device-level delivery channels — native
> MDM (Intune, Jamf, Group Policy) and file-based (`managed-settings.json` at a
> well-known OS path) — for the enterprise-managed Copilot settings system, alongside
> the existing server-managed channel, with a defined precedence order (MDM > server >
> file) and a consolidated key list. Cross-checking the changelog's raw HTML against two
> independently fetched official docs pages surfaces a concrete schema-shape correction
> to two existing corpus notes (see Cross-References → Contradicts).

## Source Context

- **Type**: docs (GitHub official product changelog, July 8, 2026; ~2-minute read,
  ~300 words of primary text). Per MINER.md §1, followed the two documentation pages
  linked from the changelog's "Getting started" section — `code.visualstudio.com/docs/enterprise/ai-settings`
  ("Deploy Copilot managed settings" section) and `docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings`
  ("Configure enterprise managed settings") — both fetched as raw HTML/embedded JSON
  rather than through AI-summarizing WebFetch, to obtain character-verified quotes and
  the exact JSON schema. Also noted (but did not extract, since it is a separate,
  already-tracked source) a same-day companion changelog, "Enterprise-managed
  OpenTelemetry export for VS Code and CLI" (July 8, 2026), linked from the same
  "Getting started" section — that source is tracked under its own issue (#1721,
  closed) and is not duplicated here.
- **Author credibility**: GitHub engineering team announcing a GA feature extension to
  the enterprise-managed settings system already documented in the corpus (June 5, June
  17, and July 1, 2026 changelogs). Authoritative for: the existence and GA status of
  the MDM and file-based channels, their exact configuration paths and registry keys,
  the precedence order among channels, the consolidated list of supported setting keys,
  and file-permission requirements for the file-based channel. Not a credible source
  for: real-world MDM rollout friction, how organizations decide among the three
  channels in practice, or adoption data.
- **Scope**: The two new device-level delivery channels (native MDM, file-based) for
  Copilot managed settings, their precedence relative to the pre-existing server-managed
  channel, and the consolidated list of setting keys available through all three
  channels. Does NOT cover: the full JSON schema for every individual key (partially
  filled in from the linked docs pages below), Linux MDM support (explicitly absent —
  see Claim 5), or plan-tier/licensing requirements (not restated in this changelog;
  see prior notes for license-tier context).

## Extracted Claims

### Claim 1: Enterprise administrators can now deliver managed Copilot settings to devices via native MDM and file-based configuration, in addition to the existing server-managed channel, GA for both Copilot CLI and VS Code

- **Evidence**: Changelog's opening paragraph, official GA announcement.
- **Confidence**: settled (GA product fact in official changelog, raw-HTML-verified)
- **Quote**: "Enterprise administrators can now deliver managed GitHub Copilot settings
  directly to devices through native mobile device management (MDM) and file-based
  configuration, in addition to the existing server-managed channel. This is generally
  available for GitHub Copilot CLI and VS Code."
- **Our assessment**: This is a GA (not preview) announcement, distinguishing it from
  the June 5, 2026 plugin-distribution note (`docs-github-copilot-enterprise-managed-plugins-vscode.md`),
  which was explicitly public preview. The enterprise-managed settings system has
  matured from preview (June 5) to GA with an expanded delivery surface (July 8) in
  about five weeks. For Ch02: this is the point at which the guide can recommend
  device-level (MDM/file-based) deployment without a preview-status caveat.

### Claim 2: Device-level deployment lets administrators reuse existing endpoint-management tooling — Intune, Jamf, Group Policy for MDM, or Chef/Puppet/Ansible for file-based config — and settings apply consistently regardless of how a developer signs in

- **Evidence**: Changelog's second paragraph, explaining the rationale for device-level
  delivery.
- **Confidence**: settled (product rationale stated in official changelog)
- **Quote**: "Device-level deployment lets you enforce Copilot governance using the same
  tools you already use to manage endpoints. You can push settings through Microsoft
  Intune, Jamf, or Group Policy, or deploy a configuration file with Chef, Puppet, or
  Ansible. Because settings are read from the device, they apply consistently across
  VS Code and Copilot CLI, regardless of how a developer signs in."
- **Our assessment**: This is the most consequential architectural claim in the source:
  device-level channels decouple policy enforcement from account sign-in state. The
  server-managed channel (documented in `docs-github-copilot-enterprise-managed-plugins-vscode.md`
  and `docs-github-copilot-enterprise-bypass-permissions.md`) resolves settings from
  "the developer's signed-in GitHub account" — meaning a developer who is signed out,
  or signed into a personal account instead of the enterprise one, would not receive
  server-managed policy. Device-level channels close that gap: a developer cannot evade
  governance simply by not signing into the enterprise account, because the policy is
  read from the OS or filesystem regardless of sign-in state. For Ch02/Ch04-05: this is
  a concrete answer to "what stops a developer from bypassing our Copilot governance
  policy?" — device-level delivery, not just account-level delivery.

### Claim 3: Three delivery channels are available, all using the same keys and values — native MDM, file-based, and server-managed

- **Evidence**: Changelog's "Delivery channels" section intro.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "You can deliver managed settings through any of three channels, all of
  which use the same keys and values."
- **Our assessment**: The shared-schema property is what makes the precedence system
  (Claim 6) tractable — administrators write the same JSON regardless of channel, and
  only the delivery mechanism differs. This is a meaningful simplification versus a
  world where each channel had its own key namespace.

### Claim 4: Native MDM reads OS-level managed preferences — the Windows Registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GitHubCopilot`, or macOS managed preferences for the `com.github.copilot` domain

- **Evidence**: Changelog's "Delivery channels" bulleted list, first item.
- **Confidence**: settled (specific technical identifiers in official changelog)
- **Quote**: "Native MDM reads OS-level managed preferences. On Windows, settings come
  from the `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GitHubCopilot` registry key. On macOS,
  they come from managed preferences for the `com.github.copilot` domain."
- **Our assessment**: The registry key and preference domain are concrete, actionable
  identifiers for IT teams already using Intune (Windows Registry policies) or Jamf/MDM
  profiles (macOS managed preferences). Notably, the changelog does not mention Linux
  under native MDM — corroborated as an explicit gap by the linked VS Code docs page
  (Claim 5).

### Claim 5: Native MDM delivery is available on Windows and macOS only; Linux administrators must use the file-based channel instead

- **Evidence**: `code.visualstudio.com/docs/enterprise/ai-settings`, "Deploy managed
  settings through native MDM" subsection, fetched as raw HTML (not present in the
  July 8 changelog itself, which is silent on Linux for the MDM channel).
- **Confidence**: settled (explicit statement in official VS Code enterprise docs,
  raw-HTML-verified)
- **Quote**: "Native MDM delivery of Copilot managed settings is available on Windows
  and macOS only. On Linux, use the file-based channel."
- **Our assessment**: This is a gap the changelog leaves implicit (by simply not
  mentioning a Linux native-MDM path) that the linked docs page states explicitly. For
  organizations with a significant Linux developer population — common in
  infrastructure/platform engineering teams — this means native MDM cannot be the sole
  deployment channel; file-based (via Chef/Puppet/Ansible, per Claim 2) is mandatory for
  Linux fleets specifically, not just an alternative option.

### Claim 6: File-based delivery reads a `managed-settings.json` file from a well-known per-OS path, and that file must be owned by root and cannot be world-writable or symlinked

- **Evidence**: Changelog's "Delivery channels" bulleted list, second item, stating the
  three OS paths and the file-permission requirements.
- **Confidence**: settled (specific paths and security requirements in official
  changelog)
- **Quote**: "File-based reads a `managed-settings.json` file from a well-known path
  (i.e, `/Library/Application Support/GitHubCopilot/managed-settings.json` on macOS,
  `%ProgramFiles%\GitHubCopilot\managed-settings.json` on Windows, and
  `/etc/github-copilot/managed-settings.json` on Linux). File-based settings must be
  owned by `root` and cannot be world-writable or symlinked."
- **Our assessment**: The ownership/permission constraints (root-owned, not
  world-writable, not symlinked) are a concrete security control preventing a
  non-privileged local user or process from tampering with enterprise policy by editing
  or symlink-swapping the settings file. This is the kind of local-privilege-escalation
  defense that is easy to omit from a "just drop a JSON file" feature and worth calling
  out explicitly in any guide coverage of this channel — deploying the file via a
  config-management tool that doesn't preserve root ownership (or that leaves it
  group-writable) would silently defeat this protection.

### Claim 7: Server-managed settings resolve from the developer's signed-in GitHub account via `managed-settings.json` in the organization's `.github-private` repository

- **Evidence**: Changelog's "Delivery channels" bulleted list, third item.
- **Confidence**: settled (consistent with prior corpus notes; raw-HTML-verified in
  this source)
- **Quote**: "Server-managed resolves settings from the developer's signed-in GitHub
  account via `managed-settings.json` in your organization's `.github-private`
  repository."
- **Our assessment**: This corroborates and reaffirms the `.github-private/copilot/managed-settings.json`
  path already established by `docs-github-copilot-enterprise-bypass-permissions.md`
  (Claim 4, the new preferred path superseding `.github/copilot/settings.json`) and
  `docs-github-copilot-enterprise-auto-model-default.md` (Claim 6, corroborating the
  same path). No new information here beyond confirming the channel name
  ("server-managed") used throughout this note's precedence discussion (Claim 8).

### Claim 8: When more than one channel provides a setting, the highest-precedence channel wins outright (no merging) in the order: native MDM, then server-managed, then file-based

- **Evidence**: Changelog states the precedence order directly beneath the delivery
  channels list.
- **Confidence**: settled (explicit precedence rule in official changelog, and
  independently corroborated with additional detail by the VS Code docs page)
- **Quote**: "When more than one channel provides settings, the highest-precedence
  channel wins outright, in this order:" followed by an ordered list: "Native MDM",
  "Server-managed", "File-based".
- **Our assessment**: "Wins outright" (not "merges") is an important operational detail
  — an administrator cannot assume that setting a key via file-based config will apply
  if native MDM is also configured and provides *any* managed setting, even a different
  key. This is confirmed with more precision by `code.visualstudio.com/docs/enterprise/ai-settings`:
  "When the same setting is available from more than one channel, VS Code uses a single
  authoritative channel rather than merging the channels. The channel with the highest
  precedence that provides any managed settings wins outright, and the other channels
  are ignored... if native MDM delivers any managed settings, VS Code uses the native
  MDM channel and ignores the server-managed and file-based channels entirely." The
  same VS Code docs page adds a version gate not present in the changelog: "Precedence
  is enforced starting in VS Code version 1.128." For Ch02: document the all-or-nothing
  precedence behavior explicitly — a team that partially configures native MDM (e.g.,
  only for `model`) on a device that also has file-based settings for
  `disableBypassPermissionsMode` would silently lose the file-based setting entirely,
  not just have the overlapping key overridden.

### Claim 9: The consolidated list of supported managed-setting keys is `permissions.disableBypassPermissionsMode`, `model`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`, and `telemetry.*`

- **Evidence**: Changelog's "Supported settings" section, a bulleted list of six keys
  (five scalar/named keys plus a `telemetry.*` wildcard for OpenTelemetry export
  config), extracted from raw HTML `<code>` tags (not AI-summarized).
- **Confidence**: settled (key names extracted verbatim from raw HTML `<li><code>...</code></li>`
  markup, cross-checked against two independent official docs pages — see Claim 10 and
  Cross-References → Contradicts)
- **Quote**: "The device-level channels support the same managed setting keys as the
  server-managed channel, including:" followed by a bulleted list: `permissions.disableBypassPermissionsMode`,
  `model`, `enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`,
  `telemetry.* for OpenTelemetry export configuration`.
- **Our assessment**: This list is the first place in the corpus where all currently
  known managed-setting keys are enumerated together in one official source. Critically,
  the bypass-permissions key is listed here with an explicit `permissions.` dot-path
  prefix — `permissions.disableBypassPermissionsMode`, not the bare `disableBypassPermissionsMode`
  used in `docs-github-copilot-enterprise-bypass-permissions.md`'s Concrete Artifact.
  See Cross-References → Contradicts for the schema-shape discrepancy this surfaces
  with two existing corpus notes, and contradiction issue #1737 filed to resolve it.

### Claim 10: Scalar settings use their dot-separated key directly (e.g. `permissions.disableBypassPermissionsMode`); structured settings such as `enabledPlugins` are supplied as a JSON string value; more keys will be added over time

- **Evidence**: Changelog's final sentence of the "Supported settings" section.
- **Confidence**: settled (product fact in official changelog)
- **Quote**: "Scalar settings use their dot-separated key directly, while structured
  settings such as `enabledPlugins` are supplied as a JSON string value. Additional
  keys will be added over time."
- **Our assessment**: This sentence itself uses `permissions.disableBypassPermissionsMode`
  as its example of a dot-separated scalar key, reinforcing Claim 9's nested-key shape.
  The "additional keys will be added over time" line signals that this key list is a
  snapshot, not a closed schema — any guide coverage should be dated and flagged as
  subject to expansion, consistent with the July 1, 2026 `model: auto` key
  (`docs-github-copilot-enterprise-auto-model-default.md`) having been added after the
  June 17 `disableBypassPermissionsMode` key.

### Claim 11: The full consolidated `managed-settings.json` schema places `permissions.disableBypassPermissionsMode` nested under a `permissions` object, while `model` is a separate top-level key — not nested inside `permissions`

- **Evidence**: `docs.github.com/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/configure-enterprise-managed-settings`
  ("Configure enterprise managed settings"), "Consolidated schema reference" section,
  extracted from the page's embedded `__NEXT_DATA__` JSON payload (the site's own
  rendered-markdown content, not an AI-generated summary). Independently corroborated
  by `code.visualstudio.com/docs/enterprise/ai-settings`'s "Available managed settings"
  table, which lists `model` and `permissions.disableBypassPermissionsMode` as two
  separate rows (not one nested pair) and its file-based example JSON, which shows the
  same top-level `model` / nested `permissions.disableBypassPermissionsMode` shape.
- **Confidence**: settled (two independent official GitHub sources, both extracted from
  raw HTML/embedded JSON rather than AI-summarized, agree exactly on this shape)
- **Quote**: (JSON schema, not prose — see Concrete Artifacts → "Consolidated
  managed-settings.json schema" for the full verbatim example from the docs page)
- **Our assessment**: This directly contradicts the JSON schema shown in two existing
  corpus notes' Concrete Artifacts. See Cross-References → Contradicts for the full
  comparison; contradiction issue #1737 filed per MINER.md §4a rather than silently
  correcting those notes here.

### Claim 12: Managed settings are loaded locally when the client starts, even without network connectivity, so controls like disabled bypass mode apply before sign-in or any server round trip and persist across account switches

- **Evidence**: `docs.github.com` "Configure enterprise managed settings" page,
  introductory paragraph, extracted from `__NEXT_DATA__` JSON.
- **Confidence**: settled (official docs statement, raw-JSON-extracted)
- **Quote**: "Managed settings are loaded locally when the client starts, even if the
  device has no network connection. This means controls such as disabled bypass mode
  and restricted plugin configuration still apply before sign in or any server round
  trip, and remain active when users switch accounts."
- **Our assessment**: This is a meaningful availability/security property that the July
  8 changelog itself does not mention — it comes entirely from the linked docs page,
  underscoring the value of following linked pages per MINER.md §1. "Loaded locally...
  before sign in" means device-level channels (MDM, file-based) are enforced even for
  an offline laptop that has never contacted GitHub in the current session — a stronger
  guarantee than the server-managed channel, which by definition requires the developer
  to be signed into the enterprise account. This is a second, independent argument (in
  addition to Claim 2) for why device-level channels close governance gaps that
  server-managed alone leaves open, particularly for air-gapped or intermittently
  connected developer environments.

### Claim 13: Disabling bypass mode blocks specific Copilot CLI flags (`--yolo`, `--allow-all`, `--allow-all-tools`, `--allow-all-paths`, `--allow-all-urls`) and slash commands (`/yolo`, `/allow-all`), and turns off VS Code's `chat.tools.global.autoApprove` setting so it cannot be re-enabled

- **Evidence**: `docs.github.com` "Configure enterprise managed settings" page, "What
  disabling bypass mode prevents" subsection, extracted from `__NEXT_DATA__` JSON.
- **Confidence**: settled (official docs statement, raw-JSON-extracted; not present in
  the July 8 changelog, which only lists the key name)
- **Quote**: "In Copilot CLI, the `--yolo`, `--allow-all`, `--allow-all-tools`,
  `--allow-all-paths`, and `--allow-all-urls` command-line options and the `/yolo` and
  `/allow-all` slash commands are blocked." / "In VS Code, the global auto-approve
  setting (`chat.tools.global.autoApprove`), also known as \"YOLO mode,\" is turned off
  and cannot be re-enabled."
- **Our assessment**: This substantially extends `docs-github-copilot-enterprise-bypass-permissions.md`,
  which documented the existence of the `disableBypassPermissionsMode` control but
  explicitly could not confirm its enforcement mechanism ("no direct verbatim quote
  available... WebFetch AI-summarized the source content"). This source (via the linked
  docs page, followed per MINER.md §1) supplies the concrete enforcement surface: five
  named CLI flags, two slash commands, and one VS Code setting, all blocked
  simultaneously. For Ch02/Ch06-07 (Safety/Security): this is now a checklist an
  enterprise can use to verify bypass-mode is actually closed — e.g., confirming
  `copilot --yolo` fails with a policy error on a managed device, rather than just
  trusting the settings file was applied.

## Concrete Artifacts

### Consolidated managed-settings.json schema (from docs.github.com, "Consolidated schema reference")

```json
{
  "extraKnownMarketplaces": {
    "agent-skills": {
      "source": {
        "source": "github",
        "repo": "OWNER/REPO"
      }
    }
  },
  "strictKnownMarketplaces": [
    {
      "source": "github",
      "repo": "OWNER/REPO"
    }
  ],
  "enabledPlugins": {
    "PLUGIN-NAME@MARKETPLACE-NAME": true
  },
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "model": "auto"
}
```
*Source: docs.github.com "Configure enterprise managed settings", extracted from the
page's `__NEXT_DATA__` embedded JSON, 2026-07-10. Note that `model` is a top-level
sibling of `permissions`, not nested inside it — see Cross-References → Contradicts.*

### Delivery channel reference table

```
Channel        | Config surface                                            | Platforms
---------------|------------------------------------------------------------|------------------
Native MDM     | Windows: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GitHubCopilot | Windows, macOS only
               | macOS: managed preferences, com.github.copilot domain      | (not Linux)
Server-managed | managed-settings.json in org's .github-private repo,       | all (requires
               | resolved via developer's signed-in GitHub account          | account sign-in)
File-based     | managed-settings.json at a well-known OS path:             | Windows, macOS,
               |   macOS:   /Library/Application Support/GitHubCopilot/     | Linux
               |            managed-settings.json
               |   Windows: %ProgramFiles%\GitHubCopilot\managed-settings.json
               |   Linux:   /etc/github-copilot/managed-settings.json
               | Must be root-owned, not world-writable, not symlinked      |

Precedence (highest to lowest, winner-take-all, no merging): Native MDM > Server-managed > File-based
Precedence enforcement requires VS Code 1.128+ (per code.visualstudio.com/docs/enterprise/ai-settings)
```
*Source: github.blog changelog, 2026-07-08, combined with code.visualstudio.com/docs/enterprise/ai-settings,
retrieved 2026-07-10.*

### Bypass-mode enforcement surface (from docs.github.com, "What disabling bypass mode prevents")

```
Setting: permissions.disableBypassPermissionsMode = "disable"

Blocked in Copilot CLI:
  --yolo
  --allow-all
  --allow-all-tools
  --allow-all-paths
  --allow-all-urls
  /yolo            (slash command)
  /allow-all        (slash command)

Blocked in VS Code:
  chat.tools.global.autoApprove ("YOLO mode") — turned off, cannot be re-enabled
```
*Source: docs.github.com "Configure enterprise managed settings", "Disabling bypass
mode for your enterprise" section, extracted from `__NEXT_DATA__` JSON, 2026-07-10.*

### Deployment method selection guidance (from docs.github.com, "Choosing a deployment method")

```
Server-managed: "Default for most enterprises and best for review workflows and audit history"
MDM-managed:    "Best when IT teams need device-group targeting through existing MDM tooling
                 on macOS and Windows"
File-based:     "Available on all platforms, and useful when server-managed and MDM-managed
                 deployment are not available, including developer environments such as
                 containers and Codespaces"
```
*Source: docs.github.com "Configure enterprise managed settings", quoted verbatim per
bullet from the "Choosing a deployment method" section, extracted from `__NEXT_DATA__`
JSON, 2026-07-10.*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 3: The
    `.github-private/.github/copilot/settings.json` configuration surface is reaffirmed
    as the server-managed channel's source (this note's Claim 7), now explicitly named
    "server-managed" as one of three channels rather than the only channel.
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claim 4: The
    `copilot/managed-settings.json` preferred path (vs. legacy `.github/copilot/settings.json`)
    is reaffirmed by the `docs.github.com` linked page (this note's Concrete Artifacts),
    which states both paths remain accepted for server-managed deployment.
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 2 and
    `docs-github-copilot-enterprise-bypass-permissions.md` Claim 2 (dual-client
    enforcement across VS Code and Copilot CLI): this note's Claim 1 and Claim 2 extend
    the "same settings, both clients" pattern to two additional delivery channels, not
    just the account-based server-managed channel.
  - `docs-github-copilot-cli-settings-command.md` (developer self-service `/settings`
    vs. enterprise-enforced settings boundary, discussed in that note's Guide Impact):
    this note's device-level channels (MDM, file-based) reinforce that boundary further
    — a developer using `/settings` to configure their local CLI has no visibility into
    or control over device-level managed settings, which are enforced beneath the
    account layer entirely.

- **Contradicts**:
  - **`docs-github-copilot-enterprise-bypass-permissions.md` Claim 1 and its "Enterprise
    Settings Configuration" Concrete Artifact**, which state `disableBypassPermissionsMode`
    is a flat top-level key (`{"disableBypassPermissionsMode": "disable"}`). This
    source's Claim 9 (the changelog's own verbatim key list) and Claim 11 (the linked
    docs pages' consolidated schema) show the key is nested under a `permissions` object
    (`permissions.disableBypassPermissionsMode`).
  - **`docs-github-copilot-enterprise-auto-model-default.md` Claim 8 and its Concrete
    Artifact**, which state `model` is nested *inside* the `permissions` object as a
    sibling of `disableBypassPermissionsMode`. This source's Claim 11 (corroborated by
    two independent raw-HTML/JSON-extracted docs pages) shows `model` is a top-level
    key, a sibling of `permissions`, not nested inside it.
  - Filed as **contradiction issue #1737** per MINER.md §4a. Both existing notes
    self-flagged their conflicting claims as based on AI-summarized (not
    raw-HTML-verified) WebFetch content, while this note's claims are raw-HTML/JSON
    extracted and cross-corroborated by two independent official sources — but per the
    Miner process, no verdict is picked here; see issue #1737 for resolution status.

- **Extends**:
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md`,
    `docs-github-copilot-enterprise-bypass-permissions.md`, and
    `docs-github-copilot-enterprise-auto-model-default.md`: together these four notes
    now document the enterprise-managed-settings system's evolution across five weeks —
    June 5 (plugin distribution + hooks/MCP governance, preview), June 17 (bypass
    permissions control), July 1 (auto model default), July 8 (device-level delivery
    channels, GA). This note adds the delivery-mechanism layer (how settings reach a
    device) on top of the prior notes' schema layer (what settings exist).
  - `docs-github-copilot-cca-rest-api-audit-config.md`: that note covers REST
    API-based auditing of Copilot Cloud Agent configuration; this note covers
    client-side (VS Code/CLI) settings delivery. Together they show GitHub building
    enterprise governance at both the CCA/API layer and the developer-client layer,
    each with its own delivery and audit mechanisms.

- **Novel**:
  - **Device-level (non-account-bound) policy enforcement**: no prior corpus source
    documents an AI coding tool governance mechanism that applies independent of user
    sign-in state. All prior enterprise-managed-settings coverage (June–July notes)
    resolved settings via "the developer's signed-in GitHub account." This is the first
    corpus evidence of settings enforcement that survives being offline, signed out, or
    signed into the wrong account.
  - **Winner-take-all precedence across configuration channels**: no prior corpus
    source documents a non-merging, highest-precedence-channel-wins model for reconciling
    multiple simultaneous configuration sources for the same AI tool. This is a distinct
    design choice from, e.g., typical cascading/merging config systems (like `.eslintrc`
    or shell profile sourcing) and has a specific practical trap (Claim 8's assessment).
  - **File-integrity requirements (root-owned, non-symlinked, non-world-writable) for
    AI-tool policy files**: no prior corpus source documents filesystem-permission
    hardening requirements specifically for an enterprise AI governance config file.
  - **Concrete CLI-flag/slash-command enforcement list for bypass mode** (Claim 13):
    the specific set of blocked flags and commands is new to the corpus; prior coverage
    (`docs-github-copilot-enterprise-bypass-permissions.md`) named the setting but not
    its enforcement surface.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration)**:
  - Add the three-channel delivery model (native MDM, server-managed, file-based) as
    the enterprise deployment reference, replacing/extending any prior guide text that
    only described the server-managed (`.github-private`) path. Use the "Delivery
    channel reference table" Concrete Artifact above as a starting structure.
  - Document the winner-take-all precedence rule (native MDM > server-managed >
    file-based) explicitly, with the specific trap noted in Claim 8: partial
    configuration in a higher-precedence channel silently discards all settings from
    lower-precedence channels, not just the overlapping keys.
  - Add the file-based channel's security requirements (root-owned, non-world-writable,
    non-symlinked) as a hardening checklist item for teams deploying via
    Chef/Puppet/Ansible.
  - Flag Linux as native-MDM-unsupported (Claim 5) — Linux fleets require the
    file-based channel specifically, not a matter of administrator preference.
  - Do NOT yet update the JSON schema example in the guide to nest `model` under
    `permissions`, or to use a flat `disableBypassPermissionsMode` key — pending
    resolution of contradiction issue #1737, use this note's raw-HTML-verified schema
    (Concrete Artifacts → "Consolidated managed-settings.json schema") as the interim
    reference.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Add device-level (MDM/file-based) delivery as the answer to "how do we ensure
    Copilot governance applies even to offline or non-enterprise-signed-in developers?"
    — a governance gap that server-managed-only coverage left open. This is a concrete
    differentiator for organizations already invested in MDM infrastructure (Intune,
    Jamf, Group Policy).
  - Add the specific bypass-mode enforcement surface (Claim 13: blocked CLI flags,
    slash commands, and VS Code setting) to any enterprise security/compliance
    checklist that references `disableBypassPermissionsMode`, replacing the vaguer
    "prevents automatic approval" language available before this source.

## Extraction Notes

1. **Raw HTML extraction, not WebFetch AI summarization**: Unlike several prior
   Copilot-changelog notes in the corpus (which relied on WebFetch's AI-summarizing
   layer and self-flagged low confidence as a result), this note's primary source and
   both linked docs pages were fetched with `curl` and parsed directly from raw
   HTML/embedded JSON (`__NEXT_DATA__` for the docs.github.com page). All quotes in this
   note are copied character-for-character from that raw extraction, including
   preserving the source's typographic apostrophe (’) in "developer’s" and
   "organization’s."
2. **Linked pages followed**: two of the "Getting started" section's two links were
   followed in full (`code.visualstudio.com/docs/enterprise/ai-settings` and
   `docs.github.com/.../configure-enterprise-managed-settings`), per MINER.md §1. A
   third linked page — the same-day companion changelog "Enterprise-managed
   OpenTelemetry export for VS Code and CLI" — was read for context (confirming the
   `telemetry.*` key in Claim 9) but not extracted as claims, since it is tracked under
   its own source issue (#1721, already closed/mined) and duplicating its extraction
   here would be out of scope for issue #1720.
3. **Contradiction filed, not resolved here**: per MINER.md §4a, the schema-shape
   discrepancy described in Claims 9 and 11 was filed as contradiction issue #1737
   rather than silently corrected in this note or in the two existing notes it
   conflicts with (Miners cannot edit merged source notes or the guide). The Assayer and
   Smith should treat both existing notes' JSON schema artifacts as unverified pending
   that issue's resolution.
4. **No GitHub Community discussion followed**: the changelog links to
   `github.com/orgs/community/discussions/199139`, the same general enterprise-managed-settings
   discussion thread already partially covered in `docs-github-copilot-enterprise-auto-model-default.md`
   Claim 10. Not re-extracted here to avoid duplicating that note's work; see that note
   for the one substantive staff reply found in that thread.
