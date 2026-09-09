---
source_url: https://github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains
source_type: docs
title: "Enterprise-managed sandbox in Copilot for JetBrains"
author: GitHub (official changelog)
date_published: 2026-09-08
date_extracted: 2026-09-09
last_checked: 2026-09-09
status: current
confidence_overall: emerging
issue: "#3320"
---

# Enterprise-Managed Sandbox in Copilot for JetBrains

> GitHub's September 8, 2026 JetBrains changelog announces enterprise-managed
> sandbox policies (public preview) — administrators can now centrally control
> sandbox enablement, filesystem/network access, proxy settings, dev-tool
> access, and macOS Keychain access for JetBrains — alongside cross-file
> cursor jumps in next edit suggestions, global project context in chat,
> enterprise policy diagnostics, a `/ide`-command bridge between terminal
> Copilot CLI sessions and the IDE, and GA for OpenTelemetry chat settings.
> The changelog's managed-sandbox claim directly conflicts with the linked
> "Enterprise managed settings reference" page's own "Supported keys" table,
> which — fetched the same day — still marks the `sandbox` key "Not supported"
> for JetBrains IDEs (Supported only for Copilot CLI); this is filed as
> **issue #3334** rather than resolved here.

## Source Context

- **Type**: docs (GitHub official product changelog, September 8, 2026;
  labeled "3 minute read," tagged `copilot`, `enterprise management tools`).
  One linked page was followed per MINER.md §1: "Configuring local sandbox
  settings for GitHub Copilot"
  (`docs.github.com/copilot/how-tos/cloud-and-local-sandboxes/configuring-local-sandbox-settings`),
  cited in the changelog as "For more information." A second page not linked
  directly from the changelog but load-bearing for Claim 1 — the "Enterprise
  managed settings reference" page
  (`docs.github.com/copilot/reference/enterprise-managed-settings-reference`,
  the same reference page fetched by the Aug 18, 2026 predecessor note in this
  family) — was also fetched, to check whether the `sandbox` key's
  per-client support matrix had been updated to reflect this changelog's
  claim. Both pages were fetched as raw HTML via `curl` and parsed from each
  page's embedded `__NEXT_DATA__` JSON payload (`articleContext.renderedPage`),
  the same method the Aug 18 predecessor note used, after an initial WebFetch
  pass on the changelog itself returned a paraphrased reproduction (see
  Extraction Notes).
- **Author credibility**: GitHub engineering team announcing a production
  capability extension to the same `managed-settings.json`-adjacent enterprise
  sandbox system documented across nine prior corpus source notes in this
  family. Authoritative for: the existence and stated behavior of each named
  JetBrains capability (sandbox policies, cursor jumps, global project
  context, policy diagnostics, `/ide` bridge) and the OpenTelemetry GA
  announcement. Not a credible source, on its own, for exactly which
  managed-settings schema key (if any) now implements the sandbox claim —
  that requires the reference page, which as fetched does not corroborate it
  (see Cross-References → Contradicts).
- **Scope**: The changelog's five "What's new" feature groups (enterprise-managed
  sandbox policies, cross-file cursor jumps, global project context in chat,
  enterprise policy diagnostics, terminal-to-IDE `/ide` bridge), its "User
  experience enhancements" and "Quality improvements" lists, and its one GA
  announcement (OpenTelemetry chat settings). Cross-checked against the
  "Configuring local sandbox settings" docs page (which turned out to
  describe the Copilot CLI `/sandbox` slash-command interface, not a
  JetBrains-native settings panel — see Claim 2) and the "Enterprise managed
  settings reference" page's `sandbox`-key table row and prose section. Does
  NOT cover: JetBrains-specific UI screenshots for the new `GitHub Copilot >
  Sandbox` settings panel, a JetBrains plugin version floor (none is stated,
  consistent with the pattern noted in the Aug 18 predecessor note), or the
  mechanics of `/ide`'s diagnostics/selection-sharing beyond the one-sentence
  description given.

## Extracted Claims

### Claim 1: Enterprise administrators can now centrally configure sandbox behavior for GitHub Copilot in JetBrains IDEs, with managed policies controlling sandbox enablement, filesystem and network access, proxy settings, developer-tool access, and macOS Keychain access, in public preview

- **Evidence**: Changelog "What's new" section, "Enterprise-managed sandbox
  policies in public preview" heading — the lead announcement of the release.
- **Confidence**: emerging (explicitly framed as public preview; also see
  Cross-References → Contradicts for a same-day conflict with the reference
  page's schema table)
- **Quote**: "Enterprise administrators can now centrally configure sandbox behavior for GitHub Copilot in JetBrains IDEs. Managed policies can control sandbox enablement, filesystem and network access, proxy settings, developer-tool access, macOS Keychain access, and more."
- **Our assessment**: This is the single highest-signal claim in the source,
  and it directly answers the Prospector's triage question across all three
  triage comments: does JetBrains now support the `sandbox` managed-settings
  key, previously documented as unsupported (`docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`,
  Claim 6, Aug 18, 2026: "JetBrains IDEs... do NOT support... `sandbox`")? The
  changelog's plain-language answer is yes, in public preview. But this
  extraction independently checked the reference page it points to for more
  detail, and found the "Supported keys" table there still marks `sandbox`
  "Not supported" for JetBrains — a genuine same-day discrepancy, not a
  stale-note artifact on this extraction's part. Filed as contradiction issue
  #3334. Until that resolves, the guide should present this as an announced,
  public-preview capability whose exact governance mechanism (a new
  `sandbox`-key value for JetBrains vs. a separate, not-yet-schematized
  JetBrains-specific managed setting) is unconfirmed.

### Claim 2: Managed sandbox restrictions take precedence over user settings; Copilot locks affected controls in the IDE and identifies which settings are administrator-managed

- **Evidence**: Changelog "What's new" section, second paragraph of the
  "Enterprise-managed sandbox policies" item.
- **Confidence**: emerging (public preview; consistent with the general
  managed-vs-user-settings precedence model documented for other keys)
- **Quote**: "Managed restrictions take precedence over user settings. Copilot locks affected controls in the IDE and identifies settings managed by your organization, helping administrators enforce consistent development environment boundaries."
- **Our assessment**: This "locks the control and labels it as managed" UX
  pattern matches the `(managed)` label documented for the Copilot CLI
  `/sandbox` interface on the linked "Configuring local sandbox settings"
  page (Concrete Artifacts, below: "A managed setting is labeled (managed) in
  the /sandbox interface and can't be changed"). That page, however, is
  written entirely in terms of the Copilot CLI's interactive `/sandbox`
  slash-command configuration screen — it never mentions JetBrains, an IDE
  settings panel, or a `GitHub Copilot > Sandbox` menu path anywhere in its
  body. The changelog cites this CLI-focused page as its "For more
  information" link for a claim about JetBrains IDE settings, which is either
  a sign the underlying policy schema and precedence model are shared across
  clients (as `managed-settings.json` generally is, per the Aug 18 note's
  Claim 7) with the JetBrains-specific UI documentation not yet published, or
  a mismatched link. Practitioners should not expect this docs page to show
  them the actual JetBrains `Sandbox` settings screen.

### Claim 3: The sandbox settings under GitHub Copilot > Sandbox are visible in JetBrains when the organization enables the Editor Preview feature flag or configures a managed setting to enable or disable the sandbox; otherwise the sandbox settings do not appear

- **Evidence**: Changelog "What's new" section, third paragraph of the
  "Enterprise-managed sandbox policies" item — the only sentence in the
  changelog naming the exact settings-menu path and its visibility gating.
- **Confidence**: emerging (public preview; specific UI-gating logic stated
  directly in the changelog)
- **Quote**: "The sandbox settings under GitHub Copilot > Sandbox are visible when your organization enables the Editor Preview feature flag or configures a managed setting to enable or disable the sandbox. If neither condition applies, the sandbox settings do not appear."
- **Our assessment**: This is the strongest textual evidence for Claim 1's
  "managed setting" framing — it names two independent gates (an Editor
  Preview feature flag, previously documented for Claude-as-agent-provider
  Business/Enterprise policy gating in
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`, and "a
  managed setting to enable or disable the sandbox"). This confirms a managed
  setting for JetBrains sandbox enablement exists as a product behavior,
  independent of whether the reference page's schema table has been updated
  to list it. Our assessment is that the discrepancy in issue #3334 is more
  likely a documentation lag on the reference page than a changelog error,
  given how specific and mechanically detailed this UI-gating description is
  — but this extraction does not pick that verdict; it is recorded as
  "filer's recommended verdict: unresolved" pending a later reference-page
  re-check.

### Claim 4: You can now use `/ide` in GitHub Copilot CLI to connect a terminal session to your JetBrains IDE context, including selections, diagnostics, and file references, in public preview

- **Evidence**: Changelog "What's new" section, "Connect terminal Copilot CLI
  sessions to your IDE" heading.
- **Confidence**: emerging (explicitly labeled public preview)
- **Quote**: "You can now use /ide in GitHub Copilot CLI to connect a terminal session to your JetBrains IDE context, including selections, diagnostics, and file references. This integration is in public preview and helps terminal-based workflows stay grounded in what you are viewing and editing in the IDE."
- **Our assessment**: This is a new bridge direction not previously documented
  in this corpus's JetBrains family: prior notes covered Copilot CLI
  *becoming* the default in-IDE agent provider
  (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim 11) and
  CLI-provider policy decoupling from standalone CLI
  (`docs-github-copilot-jetbrains-byok-sandboxing-july2026.md`, Claim 6), but
  not a *standalone terminal* CLI session reaching into a running JetBrains
  window's selection/diagnostic state via a slash command. This is a distinct
  capability from the in-IDE CLI provider — it targets a CLI session run
  outside the IDE, in an ordinary terminal, that then attaches to IDE
  context.

### Claim 5: Copilot shell commands invoked via the `/ide` bridge can use environment variables from the IDE terminal and the Python interpreter configured for the project, including the project's standard local virtual environment

- **Evidence**: Changelog "What's new" section, second paragraph of the
  "Connect terminal Copilot CLI sessions to your IDE" item.
- **Confidence**: emerging (public preview feature, stated as part of the
  `/ide` bridge)
- **Quote**: "Copilot shell commands can also use environment variables from the IDE terminal and the Python interpreter configured for your project. They can activate the project's standard local Python virtual environment, making connected command execution more consistent with your development environment."
- **Our assessment**: This is a specific interoperability claim — it means a
  `/ide`-connected CLI session's shell commands inherit the IDE's configured
  Python interpreter and can activate its venv automatically, rather than
  requiring the practitioner to manually re-activate a virtual environment in
  the terminal session. No other language runtimes (Node, Ruby, Go, etc.) are
  named as receiving the same treatment — this is stated as Python-specific.

### Claim 6: You can now use enterprise policy diagnostics to verify that policies are correctly detected and enforced on your device

- **Evidence**: Changelog "What's new" section, "Enterprise policy
  diagnostics" heading.
- **Confidence**: settled (product fact, no preview qualifier stated)
- **Quote**: "You can now use enterprise policy diagnostics to verify that policies are correctly detected and enforced on your device. This makes it easier to confirm that your Copilot configuration follows your organization's requirements."
- **Our assessment**: No prior JetBrains note in this corpus documents a
  self-service policy-diagnostics tool; prior enterprise-management notes
  documented policy *authoring* (managed-settings deployment methods,
  precedence rules) but not a practitioner- or admin-facing verification
  surface for confirming those policies actually took effect on a given
  device. This complements the "locks the control and identifies it as
  managed" UX from Claim 2 — diagnostics presumably let an admin or developer
  confirm the lock is actually active, though the changelog does not describe
  the diagnostic tool's output format, invocation path, or scope (single
  policy vs. full policy set).

### Claim 7: OpenTelemetry settings in GitHub Copilot – Chat are now generally available to all users

- **Evidence**: Changelog "Generally Available" section — a standalone
  one-line GA announcement, separate from the "What's new" preview features.
- **Confidence**: settled (GA announcement, no preview qualifier; this is the
  one non-preview claim in the release)
- **Quote**: "OpenTelemetry settings in "GitHub Copilot – Chat" are now generally available to all users."
- **Our assessment**: This closes a maturity arc spanning three prior notes.
  `docs-github-copilot-jetbrains-otel-model-management-july2026.md` (Claim 1,
  July 27, 2026) documented OpenTelemetry export as a newly-configurable
  practitioner setting at `Settings > Tools > GitHub Copilot > Chat`, with the
  export schema flagged as undocumented at the time and no stated
  preview/GA status. `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  (Claim 4, Aug 18, 2026) then documented an enterprise-managed `telemetry`
  key overriding that same developer-facing setting at the same UI path — but
  that note also flagged a same-page self-contradiction over whether
  `telemetry` was even supported for JetBrains (table said supported, prose
  said CLI/VS Code only; filed as issue #2802, unresolved). This Sep 8
  changelog is the first source to state a GA milestone for the underlying
  OpenTelemetry *setting itself* ("to all users," i.e. no longer
  preview-gated) — though it does not resolve, or even mention, the
  enterprise-managed `telemetry`-key support question from issue #2802.
  "Generally available" here should be read as scoped to the practitioner
  setting's preview status, not as new evidence resolving whether the
  managed `telemetry` key covers JetBrains.

### Claim 8: This release includes UX improvements to the ask-user card for long questions, the model picker and BYOK grouping, a new option to select the session model for built-in subagents in the Copilot agent harness, agent debug log section-copy support, MCP configuration opening in the originating project window, and plugin update-reminder improvements

- **Evidence**: Changelog "User experience enhancements" section, six bullet
  items.
- **Confidence**: settled (product facts, no preview qualifiers stated for
  any of the six items)
- **Quote**: "Subagent models: Added support for selecting the session model used by built-in subagents in the Copilot agent harness."
- **Our assessment**: The "built-in subagents in the Copilot agent harness"
  phrasing is notable set against `docs-github-copilot-jetbrains-harness-ga-aug2026.md`,
  which documented "Copilot harness" reaching GA on Aug 24, 2026 as an
  agent-picker-selectable entity, while explicitly noting the changelog it
  was drawn from "does not define what distinguishes 'Copilot harness'
  architecturally from the 'Agent' mode, Claude agent provider, or Copilot
  CLI provider." This Sep 8 item is the first source to describe "built-in
  subagents" as a component *within* the Copilot agent harness with their own
  independently selectable session model — a concrete architectural detail
  (the harness delegates to subagents, each potentially running a different
  model) that the Aug 24 note could not supply. It still does not clarify how
  "Copilot harness" relates to "Agent" mode or the other named providers.

### Claim 9: This release improves reliability across MCP servers and agent sessions, including BYOK provider persistence, OAuth challenge continuity, restored server state, and GitHub Enterprise authentication, and fixes blank local chat sessions, incorrect working-set counts, working-set zoom/model-picker interaction issues, read-only file editing issues, Claude plan stop behavior, misleading diagnostics for unopened files, stale global instructions in "Agent Customizations," and chats becoming unresponsive after automatic compaction

- **Evidence**: Changelog "Quality improvements" section, verbatim bug-fix
  list.
- **Confidence**: settled (bug-fix list, stated as shipped, no preview
  qualifiers)
- **Quote**: "chats becoming unresponsive after automatic compaction"
- **Our assessment**: The "chats becoming unresponsive after automatic
  compaction" fix is the most guide-relevant item in this list — it is a
  concrete JetBrains-specific failure mode for automatic context compaction
  (a mechanism documented at the general Claude/Copilot level elsewhere in
  the corpus) freezing the chat UI, now fixed. "Stale global instructions in
  'Agent Customizations'" is also notable: it implies the Agent Customizations
  editor (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, Claim
  8) had a bug where global instruction edits did not reliably propagate,
  now resolved. None of these nine fixes are described with enough
  reproduction detail to write as a failure-report-style claim; they are
  recorded here as a bug-fix inventory, not independently assessed for root
  cause.

## Concrete Artifacts

### Full "What's new" and "Generally Available" section content (changelog, verbatim, raw-HTML-extracted)

```
This update brings support for enterprise-managed sandbox policies,
cross-file cursor jumps for next edit suggestions, global project
context in chat, enterprise policy diagnostics, and a new connection
between terminal Copilot CLI sessions and JetBrains IDEs. It also
improves model selection, the chat experience, and reliability across
MCP servers and agent sessions.

What's new

Enterprise-managed sandbox policies in public preview
Enterprise administrators can now centrally configure sandbox behavior
for GitHub Copilot in JetBrains IDEs. Managed policies can control
sandbox enablement, filesystem and network access, proxy settings,
developer-tool access, macOS Keychain access, and more.
Managed restrictions take precedence over user settings. Copilot locks
affected controls in the IDE and identifies settings managed by your
organization, helping administrators enforce consistent development
environment boundaries.
The sandbox settings under GitHub Copilot > Sandbox are visible when
your organization enables the Editor Preview feature flag or
configures a managed setting to enable or disable the sandbox. If
neither condition applies, the sandbox settings do not appear.
For more information, see Configuring local sandbox settings for
GitHub Copilot.

Cross-file cursor jumps in next edit suggestions
Next edit suggestions can now move your cursor across files, helping
you navigate and apply coordinated code suggestions throughout a
project. When a suggested change continues in another file, you can
jump directly to the relevant location instead of finding it manually.

Global project context in chat
You can now add global files and folders to chat context, making it
faster to include information that applies across your project. This
reduces repetitive context setup and helps Copilot provide more
relevant responses for changes that span multiple areas.

Enterprise policy diagnostics
You can now use enterprise policy diagnostics to verify that policies
are correctly detected and enforced on your device. This makes it
easier to confirm that your Copilot configuration follows your
organization's requirements.

Connect terminal Copilot CLI sessions to your IDE
You can now use /ide in GitHub Copilot CLI to connect a terminal
session to your JetBrains IDE context, including selections,
diagnostics, and file references. This integration is in public
preview and helps terminal-based workflows stay grounded in what you
are viewing and editing in the IDE.
Copilot shell commands can also use environment variables from the IDE
terminal and the Python interpreter configured for your project. They
can activate the project's standard local Python virtual environment,
making connected command execution more consistent with your
development environment.

User experience enhancements
- Background agent prompts: Improved the ask-user card to better
  accommodate long questions.
- Model selection: Refined model picker behavior and BYOK grouping to
  make model choices easier to scan and select.
- Subagent models: Added support for selecting the session model used
  by built-in subagents in the Copilot agent harness.
- Agent debug logs: Added section copy support so you can share
  diagnostics and troubleshooting context faster.
- MCP configuration: Opened MCP configuration in the originating
  project window for better continuity.
- Plugin updates: Improved update reminders to make new plugin
  versions easier to discover.

Quality improvements
This release improves reliability across MCP servers and agent
sessions, including BYOK provider persistence, OAuth challenge
continuity, restored server state, and GitHub Enterprise
authentication. It also resolves blank local chat sessions, incorrect
working-set counts, working-set zoom and model picker interaction
issues, and read-only file editing issues. Additional fixes address
Claude plan stop behavior, misleading diagnostics for unopened files,
stale global instructions in "Agent Customizations," and chats
becoming unresponsive after automatic compaction.

Generally Available
OpenTelemetry settings in "GitHub Copilot – Chat" are now generally
available to all users.
```
Source: "Enterprise-managed sandbox in Copilot for JetBrains", github.blog
changelog, September 8, 2026 (raw HTML fetched via `curl`, tags stripped,
HTML entities decoded).

### `sandbox` key: reference-page table row and prose section (raw-HTML/JSON-extracted, contradicts Claim 1)

```
"Supported keys" table row for `sandbox`, fetched 2026-09-09 from
docs.github.com/copilot/reference/enterprise-managed-settings-reference:

Key      | Copilot CLI | VS Code      | GitHub Copilot app | Copilot cloud agent | JetBrains IDEs
sandbox  | Supported    | Not supported | Not supported      | Not supported        | Not supported

Prose section, heading "sandbox":
"Enforces minimum local sandbox restrictions for Copilot CLI. Managed
sandbox settings impose restrictions rather than defaults: [...]"

The full `sandbox` key documentation on this page (sub-properties
`enabled`, `failIfUnavailable`, `allowBypass`, `addCurrentWorkingDirectory`,
`sandboxMcpServers`, `sandboxLspServers`, `gitAuth`, `ghAuth`,
`allowDevToolAccess`, `sandbox.userPolicy.filesystem`,
`sandbox.userPolicy.network`, `sandbox.userPolicy.seatbelt`) is written
entirely in terms of Copilot CLI mechanics (the `/sandbox disable`
command, the `--no-sandbox` CLI flag) and never mentions JetBrains.
```
Source: "Enterprise managed settings reference"
(docs.github.com/copilot/reference/enterprise-managed-settings-reference),
parsed from the page's embedded `__NEXT_DATA__` JSON
(`articleContext.renderedPage`) by matching the `sandbox` row's `<code>` key
name against its five `<svg aria-label="Supported"|"Not supported">` cells,
and by locating the `id="sandbox"` heading's following prose. Fetched
2026-09-09. See Cross-References → Contradicts and issue #3334.

### Copilot CLI `/sandbox` interface (from linked "Configuring local sandbox settings" page, condensed, verbatim quotes preserved)

```
"Local sandboxes for GitHub Copilot are in public preview and subject
to change." / "Local sandboxing on Windows requires a Windows Insiders
build."

"You can use the /sandbox slash command to grant extra paths, adjust
network access, or turn sandboxing on or off."

"If you get your Copilot license from an enterprise, some or all
sandbox settings may be controlled by enterprise managed settings. A
managed setting is labeled (managed) in the /sandbox interface and
can't be changed."

Four-tab interactive configuration interface: General, Auth,
Filesystem, Network (opened via /sandbox in a Copilot CLI session).

General tab settings: Enable sandbox, Allow sandbox bypass (default
on), Sandbox MCP servers (default on), Sandbox LSP servers (default on).

Auth tab settings: Authenticate git (default on), Authenticate gh
(default on), Allow keychain access (macOS only, default off).

Filesystem tab: default read/write to CWD and .git directory, read-only
to the rest of the repo above CWD; "Include working directory" and
"Allow dev tool access" toggles; manual path-rule addition
(Read/Write | Read-Only | Denied, absolute paths, no wildcards).

Network tab: Allow outbound connections (default on), Allow local
network (default on), HTTP Proxy (org-enforceable via managed
settings, shown as (managed), user credentials still stored locally).

Settings are stored in settings.json under the sandbox key in the
Copilot CLI configuration directory. /sandbox policy shows the
effective (combined) filesystem policy.
```
Source: "Configuring local sandbox settings"
(docs.github.com/copilot/how-tos/cloud-and-local-sandboxes/configuring-local-sandbox-settings),
parsed from the page's embedded `__NEXT_DATA__` JSON, fetched 2026-09-09.
Note: this page is written entirely around the Copilot CLI's `/sandbox`
slash command and never names JetBrains — it is the changelog's cited "For
more information" link for a JetBrains sandbox claim, but its content
describes a different client's interface (see Claim 2's assessment).

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-jetbrains-otel-model-management-july2026.md` (Claim
    1): confirms OpenTelemetry as a real, shipping JetBrains setting at
    `Settings > Tools > GitHub Copilot > Chat`, now reaching GA (Claim 7
    above) after being introduced there July 27, 2026.
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`: the
    "Editor Preview feature flag" gating named in Claim 3 above reuses the
    same policy mechanism that note documented gating Claude-as-agent-provider
    availability for Business/Enterprise organizations.
  - `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` (Claim 4):
    that note's July 14, 2026 "local sandboxing support" (public preview,
    new sandbox settings and configuration flows in the JetBrains plugin) is
    the practitioner-facing feature that this changelog's enterprise-managed
    layer now governs — the same relationship as OpenTelemetry's
    practitioner-setting-then-managed-override arc (Claim 7 above; see
    `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
    Claim 4).

- **Contradicts**: **Issue #3334** (filed by this extraction). Claim 1's
  statement that JetBrains sandbox behavior is now centrally manageable
  directly conflicts with the "Enterprise managed settings reference" page's
  "Supported keys" table and `sandbox`-key prose (Concrete Artifacts, above),
  fetched the same day, which mark `sandbox` "Not supported" for JetBrains
  and scope the key's entire documented behavior to Copilot CLI. This is
  also in tension with `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  (Claim 6, Aug 18, 2026), which documented the identical "not supported"
  state for `sandbox` on JetBrains five weeks earlier, sourced from the same
  reference page. No verdict is picked here; see issue #3334 for the full
  Side A/Side B framing. Note also the structurally similar, still-open
  **issue #2802** (filed from the Aug 18 note) documenting a separate
  table-vs-prose self-contradiction on the same reference page for the
  `telemetry` key — this is the second time this specific reference page has
  been found internally or externally inconsistent regarding JetBrains
  client support, which is itself worth flagging to the Assayer/Smith as a
  pattern, not just two isolated incidents.

- **Extends**:
  - `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
    (Claim 6, Concrete Artifacts "Supported Keys × Client Matrix"): if Claim
    1 above is eventually confirmed as a genuine schema update (pending issue
    #3334), it would flip the `sandbox` column for JetBrains from "N" to "Y"
    in that note's matrix — the first change to any cell of that matrix since
    it was recorded Aug 18, 2026. Until confirmed, the Aug 18 matrix should
    be read as still accurate per the reference page's current content.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 11,
    "multiple isolation modes" as a phased-default-rollout differentiator)
    and `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` (Claim 4,
    naming "local" sandboxing specifically): this changelog extends that
    lineage by adding an enterprise-governance layer on top of the
    practitioner-configurable local sandbox those notes described.
  - `docs-github-copilot-jetbrains-harness-ga-aug2026.md`: Claim 8 above
    ("built-in subagents in the Copilot agent harness") adds a concrete
    architectural detail — harness-managed subagents with independently
    selectable session models — to a "Copilot harness" concept that note
    explicitly flagged as undefined relative to "Agent" mode, Claude agent
    provider, and Copilot CLI provider. It still does not resolve that
    definitional gap.

- **Novel**:
  - **First corpus source describing a `/ide`-command bridge from a
    standalone terminal Copilot CLI session into a running JetBrains
    window's context** (Claims 4-5) — distinct from Copilot CLI running as
    the in-IDE agent provider (already documented) or from the Agent Debug
    Panel (an observability surface, not a context bridge).
  - **First corpus source naming an "enterprise policy diagnostics" tool**
    (Claim 6) for JetBrains — no prior note documents a self-service
    mechanism for confirming managed-settings enforcement status on a
    device.
  - **First corpus source describing "built-in subagents" as an
    independently model-selectable component of the Copilot agent harness**
    (Claim 8) — a new architectural detail for the still-underspecified
    "Copilot harness" concept.
  - **Second same-page table-vs-external-source discrepancy found on the
    "Enterprise managed settings reference" page regarding JetBrains client
    support** (issue #3334, alongside the pre-existing issue #2802) — worth
    treating as a pattern when the guide cites this reference page for
    JetBrains-specific claims.

## Guide Impact

- **Chapter 02 (Harness Engineering — Enterprise Configuration / Sandbox &
  Isolation)**:
  - Do NOT yet update the JetBrains `sandbox`-key cell in the per-key ×
    per-client support matrix (established in
    `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`)
    from "Not supported" to "Supported" on the strength of this changelog
    alone — the reference page it cites still shows "Not supported" as of
    the same day. Present this as an announced, public-preview capability
    with an unresolved schema-documentation discrepancy (issue #3334), and
    revisit once the reference page is re-checked.
  - Note the specific UI-visibility gating for JetBrains sandbox settings
    (Claim 3: Editor Preview feature flag OR a managed setting) as a
    concrete detail administrators can act on regardless of the #3334
    resolution — the settings panel's existence and gating logic are stated
    plainly, even if the exact managed-settings key name is unconfirmed.

- **Chapter 02 (Harness Engineering — Observability)**:
  - Update JetBrains OpenTelemetry guidance to note GA status (Claim 7,
    "generally available to all users") as of Sep 8, 2026, while continuing
    to flag the still-unresolved table/prose contradiction (issue #2802)
    over whether the enterprise-managed `telemetry` key itself covers
    JetBrains — GA status of the practitioner setting and enterprise-key
    support are separate questions this source does not conflate but the
    guide should keep distinct too.

- **Chapter 04/05 (Governance & Team Adoption — Enterprise Controls)**:
  - Flag for administrators that GitHub's own reference documentation may
    lag changelog announcements for JetBrains-specific `managed-settings.json`
    coverage (this is now the second observed instance, per issue #3334 and
    #2802) — recommend that admins verify a newly-announced JetBrains
    managed-settings capability against the in-product "enterprise policy
    diagnostics" tool (Claim 6) rather than relying solely on either the
    changelog or the reference page in isolation.

- **Chapter 04 (Agentic Workflows — CLI/IDE Interop)**:
  - Add the `/ide` command (Claims 4-5) as a documented pattern for bridging
    a standalone terminal Copilot CLI session into JetBrains IDE context
    (selections, diagnostics, file references) plus automatic Python
    virtual-environment activation for connected shell commands, public
    preview as of Sep 8, 2026.

## Extraction Notes

1. **Initial WebFetch paraphrased section headings; raw HTML/JSON extraction
   used instead, per MINER.md §2a and the pattern established in the Aug 18
   predecessor note**: A first WebFetch pass on the changelog URL returned a
   plausible but reworded summary (e.g., rendering "Enterprise-managed
   sandbox policies in public preview" as "centrally configure sandbox
   behavior... with managed policies" framing, and omitting the exact
   `GitHub Copilot > Sandbox` menu path and the two-condition visibility gate
   entirely). This extraction instead fetched the changelog and two related
   docs pages via `curl`, decoded entities, and stripped tags from the raw
   response (for the changelog) or parsed the embedded `__NEXT_DATA__` JSON
   payload (for the two `docs.github.com` React/Next.js pages, matching the
   Aug 18 note's method). All quotes above were copied character-for-character
   from this raw-extracted text.
2. **A second reference page was fetched beyond the one the changelog links
   to, to test the Prospector's key question**: the changelog's own "For more
   information" link points only to "Configuring local sandbox settings"
   (which turned out to be Copilot-CLI-scoped, not JetBrains-scoped — see
   Claim 2 and the third Concrete Artifacts block). To actually test the
   Prospector's question ("does this contradict Claim 6 of the Aug 18 note?"),
   this extraction independently re-fetched the "Enterprise managed settings
   reference" page (not linked from this changelog, but the same page the
   Aug 18 note relied on) and found the contradiction described above. This
   is a deliberate deviation from "follow only the source's own links" in
   order to directly verify a triage-flagged contradiction risk; it is
   consistent with MINER.md §4/§4a's instruction to cross-reference against
   the existing corpus before writing claims.
3. **Contradiction filed, not silently resolved**: per MINER.md §4a, issue
   #3334 was filed with Side A (this changelog) and Side B (the reference
   page, corroborated by the Aug 18 note) laid out separately, with a
   "filer's recommended verdict: unresolved" rather than this extraction
   picking a winner.
4. **Nine claims extracted from a compact (~3-minute-read) changelog**: the
   source is denser than its read-time estimate suggests — five "What's new"
   items, one GA line, and two summarized-but-quoted list sections (UX
   enhancements, quality improvements) yielded nine claims total, slightly
   above the "5-15 claims" target floor but reflecting genuinely distinct,
   independently verifiable facts rather than artificial claim-splitting.
5. **No JetBrains plugin version floor stated**, consistent with every prior
   note in this family — flagged, not inferred as "no requirement."
