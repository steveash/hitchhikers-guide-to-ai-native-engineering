---
source_url: https://github.blog/changelog/2026-07-07-codex-as-agent-provider-and-agentic-enhancements-in-jetbrains-ides
source_type: docs
title: "Codex as agent provider and agentic enhancements in JetBrains IDEs"
author: GitHub (official changelog)
date_published: 2026-07-07
date_extracted: 2026-07-09
last_checked: 2026-07-09
status: current
confidence_overall: emerging
issue: "#1685"
---

# Codex as Agent Provider and Agentic Enhancements in JetBrains IDEs

> GitHub's July 7, 2026 JetBrains changelog adds Codex as a third selectable
> agent provider (alongside Copilot's native agent and the June 22 Claude
> integration), resolves the bypass-permissions-only limitation flagged for
> the Claude agent by adding permission-mode selection and debug-log support,
> extends the Agent Customizations editor to manage Hooks and MCP servers
> (including a new workspace-level `.github/mcp.json`), names three Copilot
> CLI approval levels (Default Approvals, Bypass Approvals, Autopilot
> Preview), adds admin-configured custom model support, fixes a BYOK/subagent
> billing bug, and promotes Inline Chat to general availability.

## Source Context

- **Type**: docs (GitHub official product changelog, "Improvement" tag, July 7,
  2026; self-tagged "3 minute read"; roughly 750 words across "New features,"
  "User experience," "Bug fixes," and "Availability updates" sections)
- **Author credibility**: GitHub engineering team announcing production feature
  releases for the JetBrains Copilot plugin — the same authorship pattern as
  the May 13, June 2, June 22, and June 30, 2026 JetBrains changelogs already
  in this corpus. Authoritative for: the existence and described behavior of
  each feature, exact settings paths and slash-command syntax, GA/preview
  status labels, and stated admin/policy requirements. Not authoritative for:
  how Codex performs relative to Copilot's native agent or Claude inside
  JetBrains, latency or cost of the new MCP server management actions, or
  whether the "Autopilot (Preview)" approval level introduces any observed
  safety incidents in practice.
- **Scope**: Covers Codex as a new agent provider (public preview), Agent
  Customizations editor enhancements (Hooks management, MCP server
  management, AI-generated customization files), approval settings for
  Copilot CLI sessions, permission-mode selection and debug-log support for
  the Claude agent, local model-picker view management, admin-configured
  custom model support, four user-experience/performance improvements, two
  bug fixes, and Inline Chat reaching GA. Does NOT cover: a comparative
  benchmark of Codex vs. Copilot's native agent or Claude inside JetBrains
  (contrast with `blog-jetbrains-codex-recommended-agent.md`, which benchmarks
  Codex vs. Junie in JetBrains AI Chat — a different product surface); which
  specific models are selectable as "custom models"; or a list of which
  JetBrains IDEs (IntelliJ IDEA, PyCharm, etc.) receive every feature.

## Extracted Claims

### Claim 1: Codex is now available as a new agent provider in public preview in JetBrains IDEs, installed and configured the same way as the June 22 Claude integration (install the CLI locally, then set its path in IDE settings)

- **Evidence**: Official GitHub changelog, first "New features" entry, describing both the
  capability and the exact setup steps.
- **Confidence**: emerging (explicitly labeled "public preview")
- **Quote**: "Codex is now available as an agent provider in public preview, giving you more flexibility to pick the agent that best fits your task. And you can do this without leaving your JetBrains IDE."
- **Our assessment**: This is the headline announcement and it reuses the exact integration pattern GitHub established for Claude on June 22, 2026 (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 1): install a third-party CLI locally, configure its path in Settings > Tools > GitHub Copilot > Chat, then select it from the agent picker. JetBrains' Copilot plugin agent picker now spans three distinct agent providers with three different underlying execution engines — Copilot's native agent, Claude (via Claude Code CLI), and now Codex (via Codex CLI) — while Ch04 (Agentic Workflows) and `blog-jetbrains-codex-recommended-agent.md` already document Codex as JetBrains' own AI Chat product's *recommended default* agent in a completely separate surface. Practitioners and the guide should keep these two Codex integrations (GitHub Copilot plugin's agent picker vs. JetBrains AI Chat's recommended-agent default) clearly distinct — they are different product surfaces with different selection models (explicit picker choice vs. vendor-curated default).

### Claim 2: To use Codex as agent provider, practitioners must first install the Codex CLI locally, then enable it and set its CLI path at Settings > Tools > GitHub Copilot > Chat before selecting it from the agent picker

- **Evidence**: Official changelog, step-by-step setup instructions immediately following the Claim 1 announcement.
- **Confidence**: settled (direct, mechanical setup instructions)
- **Quote**: "To use it, first install the Codex CLI on your machine. Then go to Settings > Tools > GitHub Copilot > Chat, enable Codex and set the Codex CLI path. Once configured, select Codex from the agent picker in the Copilot Chat panel to start a session."
- **Our assessment**: This is functionally identical in structure to the Claude agent provider setup path documented in `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Concrete Artifacts ("Claude Agent Provider Setup"), down to the same settings path (Settings > Tools > GitHub Copilot > Chat). For Ch02: document a single generalized "third-party agent provider setup" pattern for JetBrains — install the provider's own CLI locally, set its path in the Copilot Chat settings, select it from the agent picker — rather than three separate provider-specific setup sections, since Claude and Codex (and presumably future providers) follow the identical mechanism.

### Claim 3: Business or Enterprise Copilot subscribers need an administrator to enable the editor preview features policy before Codex as agent provider can be used

- **Evidence**: Official changelog, admin-note callout immediately following the Codex setup instructions.
- **Confidence**: settled (access requirement stated directly in official changelog)
- **Quote**: "If you are a Copilot Business or Copilot Enterprise subscriber, an administrator will have to enable the editor preview features policy before you can use this feature."
- **Our assessment**: This reuses the exact "Editor preview features" policy bundle already documented for the Claude agent provider (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 1, "Admin requirement") and the original May 13 CLI agent launch (`docs-github-copilot-jetbrains-cli-agent-sessions.md` Claim 4). Enterprises that already enabled this bundled policy for Claude or the CLI agent do not need a separate admin action for Codex — but organizations that gated Claude specifically without enabling the broader "Editor preview features" toggle should confirm the same toggle also unlocks Codex, since GitHub continues to bundle unrelated preview features under one policy switch rather than gating each provider individually.

### Claim 4: The Agent Customizations editor now supports managing Hooks directly, for both local and Copilot CLI sessions

- **Evidence**: Official changelog, "Agent customizations enhancements" subsection, first bullet.
- **Confidence**: settled (direct feature-availability statement)
- **Quote**: "Hooks support: Hooks can now be managed directly in “Agent Customizations” in both local and Copilot CLI sessions."
- **Our assessment**: The Agent Customizations editor itself was introduced June 2, 2026 as a centralized UI for "creating and managing all your agent customizations in one place" (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 8), scoped at the time to custom agents, skills, instructions, and prompts. This July 7 update adds Hooks as a fifth customization type manageable from the same editor, extending its scope rather than introducing a new configuration surface. For Ch02: update the Agent Customizations editor documentation to list Hooks alongside agents/skills/instructions/prompts as a directly-editable customization type, applicable to both local and Copilot CLI sessions.

### Claim 5: MCP servers can now be browsed, added, and lifecycle-managed (start, stop, restart, uninstall) directly from the Agent Customizations editor for Copilot CLI sessions, and workspace-level MCP servers can be defined via a new `.github/mcp.json` file

- **Evidence**: Official changelog, "Agent customizations enhancements" subsection, second bullet — the most detailed single bullet in the announcement, naming the marketplace browsing flow, both supported connection types, four lifecycle actions, and the new workspace-scope configuration file.
- **Confidence**: emerging (shipped capability, but the changelog itself flags "Dedicated UX improvements are coming in a future update," signaling the current UI is not final)
- **Quote**: "MCP servers management: MCP servers can now be managed directly in “Agent Customizations” for Copilot CLI sessions. You can browse available servers through Browse Marketplace or add an MCP server directly from this view (both command and HTTP types are supported). For configured MCP servers, you can view each server’s status and perform key actions such as start, stop, restart, and uninstall. We also support workspace-level MCP servers. You can define and manage them with .github/mcp.json in your project. Dedicated UX improvements are coming in a future update."
- **Our assessment**: This is the most substantive engineering-relevant addition in the update. Prior MCP-related corpus coverage was governance-only: `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 5 documents that enterprises can define hooks and MCP configurations that are "always enabled" across the enterprise, but says nothing about a practitioner-facing UI for browsing, installing, or lifecycle-managing individual MCP servers. This note is the first in the corpus to document an in-IDE MCP server marketplace/lifecycle-management UI (start/stop/restart/uninstall) for JetBrains, and the first to name `.github/mcp.json` as a workspace-scope MCP configuration file — distinct from the user-scope `~/.copilot/agents` path (`docs-github-copilot-jetbrains-cli-agent-sessions.md` Claim 8) and project-scope `.github/agents/` path documented elsewhere in the corpus. For Ch02: add `.github/mcp.json` to the agent-configuration-scope model as the workspace-level MCP server definition path, and note that individual practitioners can now start/stop/restart/uninstall MCP servers from the IDE without editing that file directly — though the enterprise "always enabled" MCP governance control (if configured) likely constrains what a practitioner's UI-driven lifecycle actions can actually change. That interaction (enterprise-enforced MCP configs vs. per-server UI toggles) is not addressed by either source and is an open question for the guide to flag.

### Claim 6: Customization files (instructions, prompts, skills, agents, hooks) can now be generated with AI, either via a "New" button on the Overview page or via five dedicated chat slash commands

- **Evidence**: Official changelog, "Agent customizations enhancements" subsection, third bullet, naming all five slash commands explicitly.
- **Confidence**: settled (direct feature-availability statement naming exact command syntax)
- **Quote**: "Generate customization files with AI: In the “Overview” page, you can quickly create each customization file by clicking the New button. You can also scaffold files from chat with /create-instruction, /create-prompt, /create-skill, /create-agent, or /create-hook."
- **Our assessment**: No prior corpus source documents AI-assisted scaffolding of a team's own customization files (instructions, prompts, skills, agents, hooks) via dedicated slash commands. This lowers the authoring barrier for the harness-configuration files the guide already recommends maintaining (custom agents, skills, prompt files) — practitioners can now generate a first draft via `/create-skill` or `/create-agent` rather than hand-writing the file from a template. For Ch02: note that AI-generated customization files should still be reviewed before being committed, since they are LLM output describing the team's own conventions and could encode an incorrect or overly generic first draft of a policy that should reflect actual team practice.

### Claim 7: Copilot CLI sessions in JetBrains now support three named approval levels — Default Approvals, Bypass Approvals, and Autopilot (Preview) — selectable from a permissions dropdown in the chat input area

- **Evidence**: Official changelog, "Approval settings for Copilot CLI sessions" subsection, defining all three levels by name with distinct behavioral descriptions.
- **Confidence**: emerging (Autopilot explicitly labeled "(Preview)"; Default and Bypass Approvals are not preview-labeled)
- **Quote**: "Default Approvals: Copilot CLI Agent follows your configured approval settings and prompts for confirmation based on your current policy. Bypass Approvals: All tool calls are auto-approved without confirmation dialogs. When needed, Copilot CLI Agent still asks clarifying questions. Autopilot (Preview): All tool calls are auto-approved, and Copilot CLI Agent auto-responds to clarifying questions so it can continue iterating until the task is complete."
- **Our assessment**: This is the first corpus source to name three distinct, discrete approval levels for Copilot CLI sessions rather than a binary approve/bypass toggle. "Bypass Approvals" is the named-in-full version of the informally-referenced "bypass permissions mode" that `docs-github-copilot-enterprise-bypass-permissions.md` documents as controllable enterprise-wide via `disableBypassPermissionsMode: "disable"` for Copilot CLI and VS Code — this note gives that mode an explicit, user-facing name in the JetBrains permissions dropdown. "Autopilot (Preview)" is new to the corpus: it goes further than Bypass Approvals by having the agent *auto-respond to its own clarifying questions*, removing the human from the loop entirely for both tool-call approval and disambiguation. This directly conflicts in spirit with the Ask question tool's human-in-the-loop design documented in `docs-github-copilot-jetbrains-cli-agent-sessions.md` Claim 7 (the tool exists so agents can "ask focused clarifying questions when additional information is needed") — Autopilot mode auto-answers those same questions rather than surfacing them to the practitioner. For Ch02/Ch05 (governance): document Autopilot (Preview) as the highest-autonomy, lowest-oversight mode available for JetBrains CLI sessions to date, and flag that enterprises with `disableBypassPermissionsMode: "disable"` configured should verify whether that control also disables Autopilot, since Autopilot's auto-approval behavior is a superset of what "bypass permissions mode" describes.

### Claim 8: Claude agent sessions in JetBrains now support permission-mode selection from a permissions dropdown, resolving the bypass-permissions-only limitation documented for the Claude integration in June

- **Evidence**: Official changelog, "Permission modes and debug logs support for the Claude agent" subsection, first sentence and instructions, plus a link to further documentation.
- **Confidence**: emerging (newly shipped; the changelog does not state whether this fully replaces the always-bypass behavior or adds a choice alongside it)
- **Quote**: "Claude agent sessions now support Permission modes selection, letting you choose the approval behavior that fits your workflow. To get started, select a permission mode from the permissions dropdown in the chat input area for Claude sessions. Learn more about permission modes."
- **Our assessment**: This directly resolves the most significant limitation flagged in `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 2: as of June 22, 2026, "the Claude agent currently runs in bypass permissions mode, so all file edits and tool calls are automatically approved," with that note's own analysis speculating that "currently" implied GitHub intended to add permission controls in a future release. This July 7 update is that future release. For Ch02 and Ch05: update guidance that previously told teams with strict permission-review requirements not to use the Claude agent integration in JetBrains — the bypass-only limitation is resolved as of July 7, 2026, and practitioners can now select a permission mode for Claude sessions the same way they can for Copilot CLI sessions (Claim 7). The exact set of selectable permission modes for Claude (whether it mirrors Copilot CLI's three-level Default/Bypass/Autopilot model or uses Claude Code's own native permission-mode vocabulary) is not stated in this changelog and should be verified directly in the product or the linked "Learn more" documentation before the guide asserts feature parity between the two agent providers' approval controls.

### Claim 9: Claude sessions are now included in the Agent Debug Panel / agent debug logs, making it easier to review and debug Claude session activity

- **Evidence**: Official changelog, same subsection as Claim 8, second sentence.
- **Confidence**: settled (direct feature-availability statement)
- **Quote**: "Claude sessions are now supported in agent debug logs, making it easier to review and debug session activity."
- **Our assessment**: The Agent Debug Panel was introduced June 2, 2026 as a "chronological event log of agent interactions during a Copilot CLI session" (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 5) and enhanced June 22 with a logs summary view (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 5) — but neither prior note states whether the debug panel covered Claude agent sessions specifically, since Claude was announced the same day as that summary-view enhancement. This note closes that gap explicitly: Claude sessions are now a supported source for agent debug logs. For Ch04: update the Agent Debug Panel documentation to confirm it now covers all three agent providers observable in JetBrains (Copilot native/CLI, Claude, and — not explicitly confirmed for Codex in this changelog — possibly Codex as well; the source does not state whether Codex sessions are included in agent debug logs, which is a gap worth flagging rather than assuming).

### Claim 10: The local model picker now includes a "Manage models…" view accessible from the model dropdown, giving practitioners more control over how models are listed and selected across sessions

- **Evidence**: Official changelog, "Model view management" subsection.
- **Confidence**: settled (direct feature-availability statement with exact UI path)
- **Quote**: "The local model picker now includes model view management, giving you more control over how models are listed and selected across sessions. In Local agent, click the model dropdown, then select Manage models… to open the model management view."
- **Our assessment**: This is scoped explicitly to "Local agent" sessions, distinct from the CLI/Claude model pickers already documented with `/models` slash-command support (`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 6). The changelog does not specify what can be configured inside the "model management view" beyond "how models are listed and selected" — this is a UI-organization improvement rather than a new model-access capability, and the guide should not overstate its scope beyond what is stated.

### Claim 11: GitHub Copilot for JetBrains IDEs now supports custom models configured by Business/Enterprise administrators in GitHub settings, which become automatically available to organization members once configured

- **Evidence**: Official changelog, "Custom model support" subsection, describing the admin-configuration flow and linking to "Use your own API keys" for setup details.
- **Confidence**: emerging (newly announced; the changelog does not use a GA/preview qualifier for this specific item, and it links to BYOK documentation without stating whether "custom models" and BYOK models are the identical mechanism)
- **Quote**: "GitHub Copilot for JetBrains IDEs now supports custom models configured by GitHub Copilot Business and Enterprise administrators in GitHub settings. Custom models are automatically available to members once configured by an admin. For setup details, see Use your own API keys."
- **Our assessment**: This describes a centrally-administered model-provisioning path, distinct from both individual practitioner-configured BYOK (each user adds their own provider/key, as documented for the standalone Copilot app in `docs-github-copilot-byok-app.md` Claims 1–2) and enterprise `targeted model rules` (which govern availability of GitHub-*hosted* models per organization, per `docs-github-copilot-org-targeted-model-rules.md` Claim 1, not externally-hosted custom models). The "For setup details, see Use your own API keys" link strongly suggests "custom models" here is an admin-configured BYOK variant that is pushed out automatically to all org members, rather than requiring each JetBrains user to configure their own provider connection — but this note does not confirm that inference and the Assayer should verify against the linked BYOK documentation before the guide asserts the two are the same underlying mechanism. For Ch05: if confirmed, this is a fourth distinct model-governance surface (after per-user BYOK, targeted model rules, and enterprise-wide default availability) worth adding to the enterprise model-governance layer stack documented in `docs-github-copilot-org-targeted-model-rules.md` Concrete Artifacts.

### Claim 12: A BYOK-session bug where Copilot subagents could be triggered and consume Copilot usage credits — even though the session was configured to use a BYOK provider — has been fixed so the subagent logic now respects the active BYOK provider

- **Evidence**: Official changelog, "Bug fixes" section, first item, describing both the symptom and the fix.
- **Confidence**: settled (concrete bug description and stated fix in official changelog)
- **Quote**: "Fixed an issue where BYOK sessions could trigger Copilot subagents and consume Copilot usage. The subagent logic now respects the active BYOK provider."
- **Our assessment**: This is a genuine billing-integrity bug, not a cosmetic UI fix: practitioners who configured BYOK specifically to route inference (and its cost) to their own provider — one of the explicit BYOK use cases documented in `docs-github-copilot-byok-app.md` Claim 4 ("keeping your existing billing, quotas...") — could have unknowingly consumed metered Copilot usage anyway via an internally-triggered subagent call that ignored the BYOK configuration. For Ch04/Ch05 (cost management, enterprise governance): flag this as a concrete example of why practitioners and administrators relying on BYOK for cost or data-boundary control should audit historical usage reports for unexpected Copilot-metered subagent consumption during the window this bug was live, since the BYOK-cost-avoidance guarantee documented elsewhere in the corpus did not hold in this specific subagent-triggering scenario prior to the fix.

### Claim 13: Inline Chat has transitioned from preview to general availability in JetBrains IDEs

- **Evidence**: Official changelog, "Availability updates" section.
- **Confidence**: settled (GA promotion stated definitively in official changelog)
- **Quote**: "Inline Chat is now generally available."
- **Our assessment**: No prior corpus source documents Inline Chat's preview status or GA promotion specifically for JetBrains (the two corpus hits for "Inline Chat" concern VS Code BYOK and PR chat context, not JetBrains). This is a one-line availability update with no further detail in the source — the guide should record the GA status change but has no additional behavioral detail to add beyond what was presumably already true of Inline Chat while in preview.

## Concrete Artifacts

### JetBrains Copilot Plugin — Agent Provider Picker (as of July 7, 2026)

```
Agent Provider          Execution engine              Status (JetBrains Copilot plugin picker)
────────────────────────────────────────────────────────────────────────────────────────────
Copilot native agent     GitHub Copilot                 Stable (baseline)
Claude                   Claude Code CLI (local)        Public preview since June 22, 2026;
                                                         now supports permission-mode selection
                                                         and debug logs (this source, Claims 8-9)
Codex                    Codex CLI (local)               Public preview as of July 7, 2026
                                                         (this source, Claims 1-3)

Setup pattern (common to Claude and Codex):
  1. Install the provider's own CLI locally
  2. Settings > Tools > GitHub Copilot > Chat > enable provider, set CLI path
  3. Select provider from the agent picker in Copilot Chat panel

Admin gate (Business/Enterprise): "Editor preview features" policy must be
enabled by an administrator for both Claude and Codex agent providers.
```

*Source: this changelog entry, cross-referenced against
`docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`.*

### Copilot CLI Approval Levels (JetBrains, July 7, 2026, verbatim)

```
Default Approvals
  "Copilot CLI Agent follows your configured approval settings and prompts
   for confirmation based on your current policy."

Bypass Approvals
  "All tool calls are auto-approved without confirmation dialogs. When
   needed, Copilot CLI Agent still asks clarifying questions."

Autopilot (Preview)
  "All tool calls are auto-approved, and Copilot CLI Agent auto-responds
   to clarifying questions so it can continue iterating until the task is
   complete."

Selection: permissions dropdown in the chat input area, Copilot CLI sessions.
```

*Source: "Codex as agent provider and agentic enhancements in JetBrains IDEs,"
GitHub changelog, July 7, 2026.*

### Agent Customizations Editor — MCP Server Management (new, July 7, 2026)

```
Location: "Agent Customizations" editor, Copilot CLI sessions

Discovery:    Browse Marketplace (in-editor)
Add manually: command-type or HTTP-type MCP server
Lifecycle actions per configured server: start, stop, restart, uninstall
Status:       viewable per server

New workspace-scope configuration file: .github/mcp.json (project-level)

Compare to existing agent-config scope model:
  ~/.copilot/agents/            user scope   (custom agents)
  .github/agents/               project scope (custom agents)
  .github/mcp.json              project scope (MCP servers) ← NEW, this source

Note (verbatim): "Dedicated UX improvements are coming in a future update."
```

*Source: "Codex as agent provider and agentic enhancements in JetBrains IDEs,"
GitHub changelog, July 7, 2026.*

### Bug Fixes (verbatim, July 7, 2026)

```
Fixed an issue where BYOK sessions could trigger Copilot subagents and
consume Copilot usage. The subagent logic now respects the active BYOK
provider.

Fixed multiple UI freeze issues.
```

*Source: "Codex as agent provider and agentic enhancements in JetBrains IDEs,"
GitHub changelog, July 7, 2026.*

## Cross-References

### Cross-reference verification notes
All claim numbers cited below were re-read directly in the cited source notes
before citing, per MINER.md §4b. Claim numbers are counted top-to-bottom in
document order as they appear in each cited note.

- **Corroborates**:
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 1:
    both sources document the identical third-party-agent-provider setup
    pattern (install the provider's own CLI locally, set its path at
    Settings > Tools > GitHub Copilot > Chat, select from the agent picker) —
    this note's Claims 1-2 confirm the pattern generalizes from Claude to Codex.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 8: that
    note documents the Agent Customizations editor as a centralized UI for
    agents, skills, instructions, and prompts. This note's Claims 4-6
    corroborate the editor as GitHub's continuing single surface for
    customization management by adding Hooks and MCP servers to the same UI.
  - `docs-github-copilot-enterprise-bypass-permissions.md` Claim 1: that note
    documents the enterprise `disableBypassPermissionsMode` control governing
    "bypass permissions mode" for Copilot CLI and VS Code. This note's Claim 7
    corroborates that bypass-style auto-approval is a named, user-facing
    Copilot CLI behavior ("Bypass Approvals") in the JetBrains permissions
    dropdown specifically, and extends it with a more permissive "Autopilot
    (Preview)" level not previously documented anywhere in the corpus.

- **Contradicts**: None identified as a factual conflict. This note's Claim 8
  (Claude permission-mode selection now available) resolves — rather than
  contradicts — the limitation flagged in
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 2,
  whose own "Our assessment" predicted GitHub "intends to add permission
  controls in a future release" based on the word "currently." This is a
  predicted-and-confirmed product evolution, not two sources disagreeing about
  the same point in time. No contradiction issue filed.

- **Extends**:
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claims 2
    and 5: Claim 8 in this note extends Claim 2 by adding permission-mode
    selection to the Claude agent (previously always bypass-mode-only); Claim 9
    in this note extends Claim 5 by confirming Claude sessions are now a
    supported source for the Agent Debug Panel's logs.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` Claim 8: that note
    documents `~/.copilot/agents/` as the JetBrains user-scope custom-agent
    configuration path. This note's Claim 5 extends the agent-configuration
    scope model with a new project-scope path specifically for MCP servers,
    `.github/mcp.json` — a workspace-level configuration file distinct from
    the existing agent-definition paths.
  - `docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 5: that
    note documents enterprise-level governance ("always enabled" hooks and MCP
    configurations across the enterprise). This note's Claim 5 extends that
    governance surface with a practitioner-facing UI for browsing, adding, and
    lifecycle-managing (start/stop/restart/uninstall) individual MCP servers —
    the enterprise note controls what is *always on*; this note documents the
    UI practitioners use to manage servers *within* that governance boundary.
    Neither source states how the two interact when they conflict (e.g., can a
    practitioner "uninstall" an enterprise-enforced "always enabled" MCP
    server?) — flagged as an open question for the guide.
  - `docs-github-copilot-byok-app.md` Claims 1, 4, 7 and
    `docs-github-copilot-org-targeted-model-rules.md` Claim 1: this note's
    Claim 11 (admin-configured custom models, auto-available to members)
    describes a governance surface that resembles both individual BYOK
    (external-provider models) and targeted model rules (per-org model
    availability) but is not confirmed to be identical to either. Flagged in
    Claim 11's "Our assessment" as requiring verification against the linked
    "Use your own API keys" documentation before the guide treats it as a
    fourth distinct governance layer or folds it into an existing one.
  - `docs-github-copilot-byok-app.md` Claim 4: this note's Claim 12 (BYOK
    subagent billing bug fix) is a direct, concrete counter-example to that
    claim's "keeping your existing billing, quotas" framing — the bug being
    fixed shows that guarantee did not universally hold prior to this release
    for JetBrains sessions with subagent-triggering behavior.

- **Novel**:
  - **Three named Copilot CLI approval levels, including "Autopilot
    (Preview)"** (Claim 7): no prior corpus source documents more than a
    binary approve/bypass distinction for Copilot CLI sessions. "Autopilot"
    (auto-approve tool calls AND auto-answer the agent's own clarifying
    questions) is the first fully-unattended agentic mode documented for any
    GitHub Copilot surface in this corpus.
  - **In-IDE MCP server marketplace and lifecycle management** (Claim 5):
    first corpus documentation of a practitioner-facing UI for browsing,
    adding, and starting/stopping/restarting/uninstalling MCP servers, and
    first documentation of `.github/mcp.json` as a workspace-scope MCP
    configuration file.
  - **AI-generated customization files via dedicated slash commands** (Claim
    6): no prior corpus source documents `/create-instruction`,
    `/create-prompt`, `/create-skill`, `/create-agent`, or `/create-hook` as
    scaffolding commands for a team's own harness configuration files.
  - **Resolution of the Claude-agent bypass-permissions-only limitation**
    (Claim 8): first corpus confirmation that the June 22 limitation has been
    addressed with actual permission-mode selection, roughly two weeks after
    it was first flagged as a likely-temporary "currently" state.
  - **Admin-configured "custom models" auto-provisioned to JetBrains members**
    (Claim 11): a governance mechanism not clearly matching either of the two
    existing model-governance patterns already in the corpus (individual BYOK,
    targeted model rules) — genuinely new terminology requiring follow-up
    verification.

## Guide Impact

- **Chapter 02 (Harness Engineering — Agent Provider Selection)**:
  - Add Codex as a third selectable agent provider in the JetBrains Copilot
    plugin's agent picker (Claims 1-3), using the same setup pattern already
    documented for Claude — generalize the setup instructions into one
    "third-party agent provider setup" pattern rather than duplicating it per
    provider.
  - Update the Claude agent provider section to remove the standing caution
    ("do not use until permission controls are added") — Claim 8 resolves the
    bypass-permissions-only limitation as of July 7, 2026. Note that the exact
    permission-mode vocabulary for Claude is unconfirmed against Copilot CLI's
    three-level model and should be verified before asserting parity.
  - Add `.github/mcp.json` (Claim 5) to the agent-configuration-scope model
    as the workspace-level MCP server definition path, alongside the existing
    `~/.copilot/agents/` (user scope) and `.github/agents/` (project scope)
    paths.
  - Add the five `/create-*` scaffolding slash commands (Claim 6) as an
    AI-assisted starting point for authoring custom agents, skills,
    instructions, prompts, and hooks — with a review-before-commit caveat.

- **Chapter 02 / Chapter 05 (Harness Engineering & Enterprise Governance —
  Approval Controls)**:
  - Add the three named Copilot CLI approval levels (Claim 7) as a decision
    framework: Default Approvals for standard oversight, Bypass Approvals for
    trusted low-risk tasks, and Autopilot (Preview) — flagged explicitly as
    the highest-autonomy mode in the corpus — for fully unattended iteration.
    Cross-reference `docs-github-copilot-enterprise-bypass-permissions.md` and
    recommend that enterprises with `disableBypassPermissionsMode: "disable"`
    configured verify whether that control also constrains Autopilot mode,
    since the source does not state this explicitly.
  - Add the MCP server management UI (Claim 5) to enterprise MCP governance
    documentation, flagging the open question of how per-server UI actions
    interact with enterprise-enforced "always enabled" MCP configurations
    (`docs-github-copilot-enterprise-managed-plugins-vscode.md` Claim 5).

- **Chapter 04 (Agentic Workflows — Debugging & Observability)**:
  - Update Agent Debug Panel documentation to confirm Claude sessions are now
    a supported log source (Claim 9); flag that Codex session debug-log
    support is not confirmed either way by this source.

- **Chapter 04 / Chapter 05 (Cost Management)**:
  - Add the BYOK/subagent billing bug (Claim 12) as a concrete cautionary
    example: teams relying on BYOK for cost or data-boundary control should
    periodically audit Copilot usage reports for unexpected metered
    consumption during BYOK sessions, since the "your billing stays with your
    provider" guarantee has at least one documented historical exception.
  - Flag Claim 11 (admin-configured custom models) for follow-up verification
    against the linked BYOK documentation before assigning it a place in the
    enterprise model-governance layer stack.

## Extraction Notes

1. **WebFetch returned a paraphrased summary on the first call; raw HTML was
   fetched directly to recover verbatim text.** The initial WebFetch call
   returned an AI-condensed summary not usable for direct quotes per MINER.md
   §2a. The full article HTML was retrieved directly via `curl` with a
   browser user-agent, the `<article>` element was isolated, and markup was
   stripped programmatically to produce plain text. All `Quote` fields in this
   note were copied character-for-character from that raw-text extraction,
   not from the WebFetch summary.
2. **No sub-pages followed.** The changelog links to a "Learn more about
   permission modes" documentation page (Claim 8) and a "Use your own API
   keys" page (Claim 11) that were not fetched separately for this note — both
   are flagged as open verification items in their respective claims rather
   than extracted speculatively. A follow-up mining pass on either linked page
   would be reasonable if the guide comes to depend heavily on the exact
   Claude permission-mode vocabulary or the "custom models" vs. BYOK
   distinction.
3. **Relationship to `blog-jetbrains-codex-recommended-agent.md` clarified in
   Claim 1's "Our assessment."** That note documents Codex as JetBrains AI
   Chat's vendor-curated *recommended default* agent — a completely different
   product surface (JetBrains' own AI Assistant/AI Chat) from the GitHub
   Copilot plugin's agent picker this changelog describes. The two "Codex in
   JetBrains" stories are easy to conflate; this note makes the distinction
   explicit so the guide does not merge them.
4. **User-experience and minor reliability items not extracted as separate
   claims.** The "User experience" section's four bullets (usage-based billing
   tips, Copilot panel loading stability, NES suggestion caching, file watcher
   performance/memory) were judged low-signal for harness engineering beyond
   the one item folded into Claim 12's surrounding context; they were not
   given their own claims to avoid diluting the 5-15 target with low-value
   entries. The "Fixed multiple UI freeze issues" bug fix is included verbatim
   in Concrete Artifacts but not broken out as its own claim, since it carries
   no specificity beyond "some UI freezes were fixed."
5. **No contradictions filed.** The one candidate — Claim 8 appearing to
   "contradict" the June 22 bypass-permissions claim — is a resolved
   limitation, not a factual disagreement between two sources describing the
   same point in time (see Cross-References → Contradicts). No contradiction
   issue filed per MINER.md §4a.
