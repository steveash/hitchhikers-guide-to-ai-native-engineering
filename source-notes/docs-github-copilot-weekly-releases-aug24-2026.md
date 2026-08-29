---
source_url: https://github.blog/changelog/2026-08-28-github-copilot-weekly-releases-august-24
source_type: docs
title: "GitHub Copilot weekly releases — August 24"
author: GitHub (official changelog)
date_published: 2026-08-28
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: settled
issue: "#3052"
---

# GitHub Copilot Weekly Releases — August 24

> GitHub's August 28, 2026 weekly roundup covers six surfaces — Slack/Teams,
> the standalone Copilot app, Copilot CLI, JetBrains, VS Code 1.135, and
> Visual Studio — and documents a one-week-later restatement of the
> public-preview Slack/Teams team-session feature, the Customize tab
> reaching general availability, a native Rust runtime rewrite for Copilot
> CLI (while its terminal interface stays TypeScript-based), CLI session
> recovery for mid-turn interruptions, a six-day-later restatement of
> JetBrains' enterprise managed-settings launch, and four Visual Studio
> bullets that extend prior model-usage-visibility, Git-context, and
> custom-agent-sharing coverage.

## Source Context

- **Type**: docs (GitHub official product changelog, `github.blog/changelog`,
  published August 28, 2026; self-tagged "Release," "2 minute read," organized
  into six sections — GitHub Copilot in Slack and Microsoft Teams, GitHub
  Copilot app, GitHub Copilot CLI, GitHub Copilot for JetBrains, VS Code 1.135
  Release updates, and GitHub Copilot for Visual Studio).
- **Author credibility**: GitHub engineering team announcing production,
  general-availability, and experimental features across six Copilot product
  surfaces in one weekly digest. Authoritative for the existence of each
  feature, exact setting/command names (`defaultMode`, `defaultPermissionMode`,
  `/plugin`, `/mcp`, `/skills`), and the one-line behavioral descriptions given
  in the article. Not a credible source for: adoption metrics, comparative
  model quality, rollout percentages, or effectiveness data for any listed
  change — no customer quotes, usage metrics, or case studies appear anywhere
  in the digest.
- **Scope**: A weekly digest covering the period since the prior weekly
  release, with one to five short bullets per surface (Slack/Teams: one
  bullet; Copilot app: five; Copilot CLI: four; JetBrains: one; VS Code 1.135:
  four; Visual Studio: four). Does NOT cover: Eclipse, Xcode, GitHub Mobile,
  or detailed configuration/settings documentation for any listed feature
  beyond the one-line changelog description — this is an announcement-level
  summary, not a how-to guide. Per the Prospector's triage guidance and
  consistent with the two prior weekly digests already in this corpus
  (`docs-github-copilot-weekly-releases-aug3-2026.md`,
  `docs-github-copilot-weekly-releases-aug10-2026.md`), several bullets here
  restate or compress standalone changelog entries already published earlier
  the same week and separately mined into this corpus (Slack/Teams team
  sessions, JetBrains enterprise managed settings) — this is a known editorial
  pattern of the weekly-digest series, not evidence of new product changes
  each time a restatement appears.

## Extracted Claims

### Claim 1: Copilot in Slack and Microsoft Teams now lets users turn team conversations into shared agent sessions by mentioning `@GitHub` to investigate problems, plan work, and make changes the team can follow and guide together

- **Evidence**: "GitHub Copilot in Slack and Microsoft Teams" section, sole bullet.
- **Confidence**: settled (restates a feature already documented as public
  preview from a dedicated changelog one week earlier)
- **Quote**: "Turn team conversations into shared agent sessions. Mention @GitHub to investigate problems, plan work, and make changes your team can follow and guide together."
- **Our assessment**: This is a compressed, cross-platform restatement of the
  public-preview Slack and Teams integrations already documented in detail in
  `docs-github-copilot-slack-shared-agentic-work.md` and
  `docs-github-copilot-teams-shared-agentic-work.md`, both published August
  21, 2026 — one week before this digest. The wording here ("Turn team
  conversations into shared agent sessions") is closest in spirit to the
  Teams changelog's "Turn a Microsoft Teams discussion into a collaborative
  agent session everyone can see and help direct" (that note's Claim 1), but
  is generic enough to cover both Slack and Teams in a single sentence rather
  than repeating either platform's specific wording. No new capability,
  setting, or behavioral detail is added beyond what the two dedicated
  sources already document (thread-as-context capture, app-identity
  attribution for shared-context PRs, the Slack-specific "Slack Code" channel
  mechanic, ruleset approval escalation). For a guide update: no change
  beyond confirming the feature remains active and is now being surfaced in
  the general weekly digest alongside other surfaces, consistent with the
  pattern (already noted in `docs-github-copilot-weekly-releases-aug10-2026.md`
  Claim 3's "Our assessment") of major standalone announcements re-appearing
  in the following week's roundup.

### Claim 2: The GitHub Copilot app's Customize tab has reached general availability, bringing MCP servers, plugins, skills, and canvases together in one place

- **Evidence**: "GitHub Copilot app" section, first bullet.
- **Confidence**: settled (GA status stated directly in the official changelog)
- **Quote**: "The Customize tab is now generally available, bringing MCP servers, plugins, skills, and canvases together in one place."
- **Our assessment**: This is the first corpus documentation of "canvases" as
  one of four artifact types unified under a single Customize tab in the
  standalone Copilot app, alongside MCP servers, plugins, and skills.
  `docs-github-copilot-agent-plugins-1-0.md` (August 12, 2026) documented
  Agent Plugins 1.0 reaching GA across VS Code, Copilot CLI, the GitHub
  Copilot SDK, and the GitHub Copilot app, and separately noted (Claim 4's
  "Our assessment" reference to the `com.github.copilot/` namespace
  directory) that Copilot-specific plugin extras include "custom agents,
  commands, rules, hooks, canvases" — but that note's Scope section
  explicitly flagged the Copilot app's own plugin-management UI as
  unfetched/undocumented. This claim is the first to confirm, at the product
  level, that the app's Customize tab is where plugins, MCP servers, skills,
  and canvases are now jointly surfaced and managed, and that this
  consolidated tab has reached GA (not preview). The changelog does not
  state whether "Customize tab" GA is a distinct milestone from Agent
  Plugins 1.0 GA or a UI-level packaging of it — the two GA announcements are
  16 days apart (August 12 vs. this digest's August 28 publication) and this
  source does not cross-reference the earlier one. For Ch02 (Harness
  Engineering — Extensibility): document the Customize tab as the standalone
  Copilot app's unified extensibility management surface, now GA, covering
  four distinct artifact types in one place.

### Claim 3: Azure DevOps issues and pull requests can now be turned into Copilot sessions from the Customize tab in the GitHub Copilot app

- **Evidence**: "GitHub Copilot app" section, second bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Turn Azure DevOps issues and pull requests into Copilot sessions from the Customize tab."
- **Our assessment**: No prior corpus source documents Azure DevOps
  issue/PR-to-Copilot-session conversion from the standalone Copilot app
  specifically. The closest prior corpus precedent is
  `docs-github-copilot-vs-april-2026.md` (Claim 4), which documented Visual
  Studio's debugger agent ingesting Azure DevOps work items as a starting
  point — a different surface (Visual Studio IDE) and a different mechanism
  (debugging pipeline input vs. session-creation trigger). This claim is the
  first evidence that Azure DevOps issue/PR ingestion has reached the
  standalone Copilot app's Customize tab as a session-creation entry point,
  parallel to how GitHub issues/PRs are already used to trigger cloud agent
  sessions elsewhere in the corpus. The changelog gives no detail on
  authentication, organization-linking, or whether this requires a separate
  Azure DevOps integration setup step. For Ch01 (Daily Workflows): note Azure
  DevOps issue/PR-to-session conversion as a cross-platform entry point for
  teams whose work tracking lives outside GitHub Issues.

### Claim 4: The GitHub Copilot app now has experimental support for Windows Subsystem for Linux (WSL), enabling work in a Linux environment

- **Evidence**: "GitHub Copilot app" section, third bullet.
- **Confidence**: emerging (explicitly labeled experimental in the source)
- **Quote**: "Work in your Linux environment with experimental support for Windows Subsystem for Linux (WSL)."
- **Our assessment**: This is the first corpus documentation of WSL support
  in the standalone Copilot app specifically. WSL appears elsewhere in the
  corpus only as a bug-fix target: `docs-github-copilot-jetbrains-harness-ga-aug2026.md`
  (Claim 10) documents a fix for "worktree session startup failures for
  projects opened from WSL" in JetBrains, four days before this digest —
  implying WSL project support already existed in JetBrains prior to this
  digest, whereas here the Copilot app is gaining WSL support for the first
  time, and as an explicitly experimental feature rather than a bug fix to
  existing support. The two sources describe different surfaces at different
  maturity stages for the same underlying platform (WSL), not the same
  feature. The changelog gives no detail on what "work in your Linux
  environment" concretely enables (a full Linux-backed session execution
  environment, or just filesystem/terminal access) or how a practitioner
  opts in. For Ch02 (Harness Engineering — Environment Configuration): flag
  experimental WSL support in the Copilot app as a new option for
  Windows-based practitioners who prefer a Linux execution environment,
  pending a more detailed source once the feature matures past experimental.

### Claim 5: The GitHub Copilot app now supports splitting and moving any tab to keep related work side by side

- **Evidence**: "GitHub Copilot app" section, fourth bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Split and move any tab to keep related work side by side."
- **Our assessment**: A thin but concrete UI-layout capability with no prior
  corpus documentation for the standalone Copilot app specifically. This is
  a different mechanism from the Copilot CLI's tab bar customization
  documented in `docs-github-copilot-cli-terminal-ga.md` (Claim 5: reorder,
  hide, or turn off the CLI's Session/Gists/Issues/Pull requests tab bar) —
  that CLI feature reorders a fixed tab bar within a single terminal pane,
  whereas this claim describes splitting the app's own tabs into separate,
  side-by-side panes. The changelog gives no further detail (how many tabs
  can be split simultaneously, whether the layout persists across sessions).
  Not significant enough for a dedicated guide section beyond a passing
  mention alongside Claim 6 as evidence of continued Copilot app UI polish.

### Claim 6: The GitHub Copilot app can now send any browser preview straight to an external browser from the tab's context menu

- **Evidence**: "GitHub Copilot app" section, fifth bullet.
- **Confidence**: settled (product fact stated directly in official changelog)
- **Quote**: "Send any browser preview straight to your external browser from the tab's context menu."
- **Our assessment**: This is a narrow but concrete workflow shortcut: a
  browser preview generated inside the Copilot app (presumably from an
  agent's front-end changes) can now be escalated to the practitioner's own
  external browser without a separate copy/paste or manual URL-navigation
  step. No prior corpus source documents this specific hand-off mechanism
  for the standalone Copilot app's browser preview feature. Thematically
  adjacent to, but a different surface from, the integrated-browser
  live-reload property documented in `docs-github-copilot-weekly-releases-aug10-2026.md`
  Claim 18 (VS Code's integrated browser reflecting HTML changes without a
  manual refresh) — that claim is about VS Code's embedded browser staying
  current; this one is about moving a Copilot-app preview out to a full
  external browser. Not significant enough for a dedicated guide section
  beyond a passing mention alongside Claim 5.

### Claim 7: Copilot CLI adds `defaultMode` and `defaultPermissionMode` settings so a practitioner can start every new session with their preferred execution and permission modes

- **Evidence**: "GitHub Copilot CLI" section, first bullet.
- **Confidence**: settled (product fact stated directly in official changelog,
  naming both setting keys explicitly)
- **Quote**: "Start every new session with your preferred execution and permission modes using `defaultMode` and `defaultPermissionMode`."
- **Our assessment**: This extends `docs-github-copilot-cli-settings-command.md`,
  which documented the `/settings` command consolidating "previously
  scattered Copilot CLI configuration commands — including `/theme`,
  `/streamer-mode`, and `/experimental` — into a single unified interface"
  (that note's Claim 1) with a self-documenting, tab-completable key
  inventory (Claim 3). Neither `defaultMode` nor `defaultPermissionMode` is
  named in that note's own inventory, so this is the first corpus
  documentation of these two specific keys. Naming them "default" implies
  each new CLI session previously started from a fixed, non-configurable
  mode/permission baseline that a practitioner had to change manually every
  session (e.g., via `/mode` or an equivalent per-session toggle not
  independently documented in this corpus); these two settings let that
  baseline be set once and persist. This also connects to the "autopilot"
  naming convergence already tracked in `docs-github-copilot-weekly-releases-aug10-2026.md`
  Claim 8 (`--mode autopilot` in CLI headless mode) — a `defaultMode` setting
  could plausibly default a session straight into autopilot-equivalent
  execution, though the source does not name autopilot or any other mode
  value explicitly. For Ch02 (Harness Engineering — CLI Configuration): add
  `defaultMode`/`defaultPermissionMode` to the guide's `/settings`
  documentation as a way to standardize a practitioner's (or, via
  `managed-settings.json`, an organization's) preferred session-start
  behavior without per-session reconfiguration.

### Claim 8: Copilot CLI's plugin, MCP server, and skill management gained updated experiences through `/plugin`, `/mcp`, and `/skills`

- **Evidence**: "GitHub Copilot CLI" section, second bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog) — though the specific nature of the update is not described
- **Quote**: "Manage plugins, MCP servers, and skills more easily with new experiences in `/plugin`, `/mcp`, and `/skills`."
- **Our assessment**: This extends, without replacing, the in-session
  management commands already documented in `docs-github-copilot-cli-terminal-ga.md`:
  `/mcp add`/`/mcp search` for guided MCP server setup with no-restart
  availability (Claim 6), `/skills` for toggling installed skills via arrow
  keys and spacebar (Claim 7), and `/plugin` for browsing/installing from a
  marketplace, repository, or local path (Claim 8) — all three introduced at
  the terminal's June 23, 2026 GA. This August 28 bullet states only that
  "new experiences" now exist for all three commands, "more easily," without
  specifying what changed (a redesigned UI, additional options, a different
  interaction model). Given the terse one-line treatment, this should be
  read as an incremental refinement to the three June-established commands
  rather than a new capability — a future, more detailed changelog entry
  would be needed to document the specific UI/UX delta. For Ch02: note that
  `/plugin`, `/mcp`, and `/skills` continue to receive iterative UX
  investment roughly two months after their initial GA, without asserting
  specific new mechanics beyond "easier."

### Claim 9: Copilot CLI now supports session recovery, letting a practitioner pick up where they left off by restoring sessions that did not exit cleanly, including sessions interrupted mid-turn

- **Evidence**: "GitHub Copilot CLI" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog, including the mid-turn-interruption detail)
- **Quote**: "Pick up where you left off by restoring sessions that did not exit cleanly, including sessions interrupted mid-turn."
- **Our assessment**: No prior corpus source documents Copilot CLI recovering
  a session that crashed, was killed, or otherwise exited uncleanly — prior
  session-continuity coverage in this corpus (e.g., the CLI's `/app` command
  preserving session/folder context when bridging to the standalone app, per
  `docs-github-copilot-weekly-releases-aug10-2026.md` Claim 10, or the
  cloud-sandbox three-state active/stopped/deleted lifecycle documented in
  `docs-github-copilot-teams-shared-agentic-work.md` Claim 10) concerns
  deliberate session hand-off or explicit stop/resume, not recovery from an
  unclean exit. The explicit callout of "mid-turn" interruption is the most
  operationally significant detail: it implies the CLI now persists enough
  in-flight state (not just completed-turn history) to resume a session that
  was killed while a tool call or model response was still in progress,
  rather than only being able to restore to the last cleanly-completed turn.
  The source does not state what triggers automatic recovery (does the CLI
  detect an unclean prior exit on next launch and prompt to restore, or does
  a practitioner invoke a command explicitly?) or what happens to a tool call
  that was mid-execution when the interruption occurred. For Ch03
  (Verification — Environment Reliability) and Ch04 (Agentic Workflows —
  Session Continuity): document CLI session recovery as a reliability
  improvement for practitioners running long or unattended CLI sessions
  (e.g., in scripted or CI-adjacent contexts) where a crash, terminal close,
  or SSH disconnect previously meant losing an in-progress turn entirely.

### Claim 10: Copilot CLI now runs on a native Rust runtime, providing significantly faster performance, while its terminal interface remains built in TypeScript

- **Evidence**: "GitHub Copilot CLI" section, fourth bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog, including the explicit TypeScript-terminal/Rust-runtime split)
- **Quote**: "Get significantly faster performance now that Copilot CLI runs on a native Rust runtime, while its terminal interface remains built in TypeScript."
- **Our assessment**: This is a significant architectural disclosure with no
  prior corpus precedent — no earlier source in this corpus states what
  language or runtime Copilot CLI's core execution engine was built in
  before this change, though the explicit "while its terminal interface
  remains built in TypeScript" clause confirms the CLI was, at minimum,
  TypeScript-based at the UI/terminal layer (consistent with
  `docs-github-copilot-cli-terminal-ga.md`'s documentation of a
  Node/TypeScript-flavored terminal redesign with tabs, color modes, and
  screen-reader support). The claim states the underlying runtime — the part
  responsible for whatever makes performance "significantly faster" — has
  moved to Rust, while the terminal UI layer was NOT rewritten and stays
  TypeScript. This is a partial-rewrite/hybrid-architecture pattern
  (native-language execution core, scripting-language UI layer) rather than
  a full ground-up rewrite. The source gives no benchmark, percentage, or
  specific operation type (startup time, tool-call latency, token
  throughput) for "significantly faster," and does not state whether this
  changes CLI installation/distribution (e.g., whether Copilot CLI now ships
  as a compiled binary rather than an npm package) or has any compatibility
  implications for existing configuration, plugins, or MCP servers. For Ch02
  (Harness Engineering — CLI Architecture): document the Rust-runtime
  migration as a performance-motivated internal rewrite that a practitioner
  should not expect to change CLI behavior or configuration surface, per the
  source's framing as purely a performance improvement — but flag the
  installation/distribution question as unconfirmed and worth a follow-up
  source if GitHub publishes a more detailed engineering writeup.

### Claim 11: GitHub Copilot for JetBrains now supports consistent enterprise controls across plugins, MCP servers, telemetry, and agent permission modes

- **Evidence**: "GitHub Copilot for JetBrains" section, sole bullet.
- **Confidence**: settled (restates a feature already documented in detail
  from a dedicated changelog six days earlier)
- **Quote**: "Apply consistent enterprise controls for Copilot in JetBrains, including plugins, MCP servers, telemetry, and agent permission modes."
- **Our assessment**: This is a near-exact restatement of
  `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  (August 18, 2026, ten days before this digest's publication), whose Claim
  1 quotes the dedicated changelog's identical four-category framing:
  "GitHub Copilot for JetBrains now supports enterprise managed settings for
  plugin governance, MCP server access, OpenTelemetry, and permission
  modes." The category names match one-to-one (plugins↔plugin governance,
  MCP servers↔MCP server access, telemetry↔OpenTelemetry, agent permission
  modes↔permission modes), consistent with the established weekly-digest
  pattern (already documented for the JetBrains-managed-settings restatement
  in `docs-github-copilot-weekly-releases-aug10-2026.md` Claim 13 and for
  Agent Plugins 1.0 in that same note's Claim 3) of major standalone
  JetBrains/enterprise announcements re-surfacing in the following weekly
  roundup. No new key names, client-support-matrix detail, or deployment
  mechanics are added beyond what the dedicated source already documents
  (`enabledPlugins`, `extraKnownMarketplaces`, `strictKnownMarketplaces`,
  `allowedMcpServers`/`deniedMcpServers`, `telemetry`,
  `permissions.disableBypassPermissionsMode` — with `permissions.model`,
  `remoteControl`, and `sandbox` still unsupported for JetBrains per that
  note's Claim 6). For a guide update: no new material beyond confirming
  this remains an active, current capability as of this digest.

### Claim 12: VS Code 1.135 lets a practitioner continue recent Copilot or Claude agent sessions from other applications directly within VS Code

- **Evidence**: "VS Code 1.135 Release updates" section, first bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Continue recent Copilot or Claude agent sessions from other applications in VS Code."
- **Our assessment**: This is the inverse direction of the cross-surface
  session continuity already documented for Slack and Teams — those sources
  describe a session started in a chat platform being continued "from your
  terminal, the GitHub Copilot app, or your preferred IDE"
  (`docs-github-copilot-teams-shared-agentic-work.md` Claim 2; corroborated
  for Slack in `docs-github-copilot-slack-shared-agentic-work.md` Claim 4).
  This claim instead documents VS Code as the *landing* surface for a
  session that began in an unnamed "other application," and explicitly names
  both Copilot and Claude agent sessions as continuable — the first corpus
  mention of VS Code resuming a *Claude* agent session that originated
  elsewhere, as opposed to VS Code's existing per-turn Claude BYOK/built-in
  model switching documented in `docs-github-copilot-weekly-releases-aug10-2026.md`
  Claim 16 (which concerns model choice within one continuous VS Code
  session, not resuming a session that started outside VS Code). The source
  does not name which "other applications" are supported, nor whether this
  relies on the same GitHub-hosted cloud-sandbox session-state substrate
  documented for Teams/Slack (`docs-github-copilot-teams-shared-agentic-work.md`
  Claim 10) or a separate mechanism specific to VS Code. For Ch04 (Agentic
  Workflows — Multi-Session): document VS Code as another node in the
  corpus's growing set of session-continuation surfaces (CLI remote control,
  VS Code, JetBrains, issues/projects sidebar, Teams, Slack, and now VS Code
  as an explicit landing point for Claude sessions specifically), while
  flagging the unnamed "other applications" as an open question.

### Claim 13: VS Code 1.135 lets a practitioner get a second opinion from a complementary model to surface missed details and edge cases

- **Evidence**: "VS Code 1.135 Release updates" section, second bullet.
- **Confidence**: emerging (no mechanism, invocation method, or model-pairing
  detail is given — the source states only the capability's existence and
  purpose)
- **Quote**: "Get a second opinion from a complementary model to surface missed details and edge cases."
- **Our assessment**: No prior corpus source documents a dedicated
  "complementary model second opinion" feature in VS Code Chat. This is
  conceptually adjacent to, but mechanically distinct from, two prior
  corpus items: `docs-github-copilot-weekly-releases-aug10-2026.md` Claim 16
  (per-turn switching between Claude BYOK and built-in Copilot models within
  one Claude session, a practitioner-driven model *choice*) and the general
  multi-model-review pattern documented outside the Copilot corpus family
  (e.g., `blog-simonwillison-csrf-multimodel-review.md`, not re-read in
  detail for this claim beyond its title). Neither of those describes an
  explicit "second opinion" affordance whose stated purpose is surfacing
  *missed details and edge cases* — this framing implies a review/critique
  role for the complementary model (checking the primary model's work)
  rather than a free choice of which model executes the task. The source
  does not state how a practitioner invokes this (a button, a slash command,
  automatic triggering), which model(s) serve as the "complementary" one, or
  whether it consumes additional AI credits/model quota. For Ch01 (Daily
  Workflows — Verification): flag this as a first-party, in-product
  verification aid worth cross-referencing against the guide's existing
  multi-model-review guidance once a more detailed source describes the
  invocation mechanism.

### Claim 14: VS Code 1.135 introduces a single-pane Agents layout with simpler session controls and session details that are easier to find

- **Evidence**: "VS Code 1.135 Release updates" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog) — though the specific UI change is thinly described
- **Quote**: "Stay focused on your work with a new single-pane Agents layout, simpler session controls, and session details that are easier to find."
- **Our assessment**: A UX/navigation restructuring of the VS Code Agents
  window with no prior corpus documentation of what the pre-1.135 layout
  looked like to contrast against. "Single-pane" implies the Agents window
  previously used a multi-pane layout, but no prior corpus source describes
  that prior state in enough detail to characterize the delta precisely. Not
  significant enough for a dedicated guide section beyond noting that VS
  Code's Agents window UI continues to be actively revised roughly monthly,
  consistent with the cadence already visible across this weekly-digest
  source-note family.

### Claim 15: VS Code 1.135 now shows detailed chat usage by model for every chat turn

- **Evidence**: "VS Code 1.135 Release updates" section, fourth bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "See detailed chat usage by model for every chat turn."
- **Our assessment**: This extends the corpus's cost/usage-visibility
  coverage to VS Code Chat specifically, at per-turn, per-model granularity.
  Prior corpus precedent for this kind of granular usage visibility comes
  from a different Copilot surface: `docs-github-copilot-vs-june-2026.md`
  (Claim 1) documented Visual Studio's "refreshed Copilot Usage window"
  showing "real-time, token-based usage against GitHub's usage-based billing
  model, with proactive alerts" — that is a session/window-level aggregate
  view, not the per-turn, per-model breakdown this claim describes for VS
  Code. It is also conceptually adjacent to
  `docs-github-copilot-weekly-releases-aug3-2026.md` Claim 1, which
  documented the standalone Copilot app's "Auto" mode disclosing "which
  model handled each completed request, plus AI credit and cache details" —
  that is Auto-mode-specific model disclosure in the app, whereas this claim
  is usage-metric detail (not just which model ran) for every turn in VS
  Code Chat, regardless of whether Auto mode is in use. The source gives no
  detail on what "usage" is measured (tokens, AI credits, both) or where in
  the UI this is surfaced. For Ch04 (Cost Management): add VS Code's
  per-turn, per-model usage detail as a third distinct usage-visibility
  mechanism in the corpus, alongside the app's Auto-mode model disclosure
  and Visual Studio's aggregate Copilot Usage window — noting these three
  are documented as separate surfaces with different granularity, not one
  unified usage-reporting feature.

### Claim 16: GitHub Copilot for Visual Studio now lets a practitioner pin favorite models, hide unused ones, compare capabilities and costs, and adjust reasoning effort for each task

- **Evidence**: "GitHub Copilot for Visual Studio" section, first bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog, naming four distinct model-management actions)
- **Quote**: "Pin favorite models, hide unused ones, compare capabilities and costs, and adjust reasoning effort for each task."
- **Our assessment**: This bundles four distinct model-management actions
  into one bullet, none of which is documented for Visual Studio in any
  prior corpus source note — the four prior Visual Studio notes in this
  corpus (`docs-github-copilot-vs-april-2026.md` through
  `docs-github-copilot-vs-july-2026.md`) document agent skills, custom
  agents, cloud agent launching, MCP trust dialogs, and Copilot usage
  visibility, but no model-picker curation (pin/hide) or per-task reasoning
  effort control. "Adjust reasoning effort for each task" is the most
  operationally notable of the four: it implies Visual Studio now exposes a
  reasoning-effort parameter (a concept generally associated with
  reasoning-capable models trading inference cost/latency for answer
  quality) as a per-task, not global, setting — but the source does not name
  which models support this, what the effort levels are, or how they map to
  cost (connecting to "compare capabilities and costs" in the same bullet).
  For Ch02 (Harness Engineering — Model Configuration): add
  pin/hide/compare/reasoning-effort as Visual Studio's model-management
  surface, the first corpus documentation of per-task reasoning-effort
  control for this IDE specifically.

### Claim 17: GitHub Copilot for Visual Studio now lets a practitioner share custom agents across their organization to standardize workflows and improve discovery

- **Evidence**: "GitHub Copilot for Visual Studio" section, second bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Share custom agents across your organization to standardize workflows and improve discovery."
- **Our assessment**: This extends, and is in some tension with,
  `docs-github-copilot-vs-april-2026.md` (Claims 5-6), which documented
  Visual Studio's user-level custom agents stored in
  `%USERPROFILE%/.github/agents/` as "travel[ing] across projects without
  per-project configuration" and explicitly flagged that surface as "an
  ungoverned configuration surface that enterprise AI policies should
  explicitly account for." This August 28 claim describes the opposite
  direction — organization-level sharing intended specifically to
  standardize workflows, i.e., a governed distribution mechanism rather than
  an individual, ungoverned personal-agent path. The source does not state
  whether org-shared custom agents in Visual Studio use the same
  `.github/agents/` file convention documented for the user-level path, a
  separate repository-level convention, or an entirely new distribution
  mechanism, so it cannot be confirmed whether this closes the April note's
  governance gap or is a parallel, additive sharing feature that leaves the
  ungoverned personal path unchanged. For Ch02 (Harness Engineering — Agent
  Configuration) and Ch05 (Team Adoption): add org-wide custom-agent sharing
  in Visual Studio as a workflow-standardization mechanism, and flag the
  open question of whether it supersedes or coexists with the
  previously-documented ungoverned user-level agent path.

### Claim 18: GitHub Copilot for Visual Studio now lets a practitioner view Copilot plan consumption and manage premium model usage before reaching limits

- **Evidence**: "GitHub Copilot for Visual Studio" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "View Copilot plan consumption and manage premium model usage before reaching limits."
- **Our assessment**: This directly extends
  `docs-github-copilot-vs-june-2026.md` Claim 1, which documented the
  "refreshed Copilot Usage window" showing "real-time, token-based usage
  against GitHub's usage-based billing model, with proactive alerts as a
  user approaches, hits, and exceeds their limit" (June 2026). This August
  28 bullet restates the same proactive-limit-awareness framing
  ("before reaching limits" here vs. "proactive alerts as a user
  approaches... their limit" there) two months later, and adds "manage
  premium model usage" as an explicit action verb not present in the June
  wording — suggesting the feature may have grown from a read-only usage
  display into one with an active management/control affordance, though the
  source does not describe what "manage" concretely allows (throttling,
  disabling specific premium models, switching to non-premium alternatives).
  For Ch04 (Cost Management): update the Visual Studio Copilot Usage window
  guidance sourced from the June note to note the added "manage premium
  model usage" capability as of this digest, while flagging the specific
  management mechanism as unconfirmed pending a more detailed source.

### Claim 19: GitHub Copilot for Visual Studio's Git agent can now review uncommitted changes or individual commits before a pull request is opened

- **Evidence**: "GitHub Copilot for Visual Studio" section, fourth bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Review uncommitted changes or individual commits with the Git agent before opening a pull request."
- **Our assessment**: This extends two distinct pieces of prior Visual
  Studio Git-context coverage. `docs-github-copilot-vs-july-2026.md` Claim 5
  documented attaching a Git branch to Copilot Chat as context (alongside
  "the previously existing ability to attach commits, changes, and pull
  requests"), and `docs-github-copilot-vs-may-2026.md` Claim 10 documented
  Git commit history as "a first-class context source in Copilot Chat,"
  attachable from Git History, File History, or Annotate views. Both of
  those describe *attaching* Git artifacts as context for a general Copilot
  Chat conversation. This claim instead names a specific, dedicated "Git
  agent" performing a review action — distinct from the code-selection
  review action documented in `docs-github-copilot-vs-july-2026.md` Claim 3
  ("Copilot Actions > Review Selection," scoped to an editor code selection,
  powered by GitHub Copilot code review). Whether this "Git agent" is a
  newly-named, dedicated agent or a repackaging of the existing
  attach-as-context mechanism into a guided pre-PR review workflow is not
  stated by the source. For Ch01 (Daily Workflows — PR Preparation):
  document the Git agent's uncommitted-changes/individual-commit review as a
  recommended pre-PR self-review step in Visual Studio, distinct from both
  the general Git-context-attachment pattern and the editor-selection
  review action already in the corpus.

## Concrete Artifacts

### Full weekly digest — August 24, 2026 (published August 28, 2026), verbatim transcript

Extracted from raw HTML (not AI-summarized WebFetch output) to guarantee verbatim quotes, per MINER.md §2a and the precedent set in `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 1 and `docs-github-copilot-weekly-releases-aug10-2026.md` Extraction Note 1.

```
GitHub Copilot weekly releases — August 24
Source: github.blog/changelog, published 2026-08-28, retrieved 2026-08-29
2 minute read

INTRO
  This week's updates give you more control over how Copilot runs, from
  team sessions in Slack and Teams to customization across the app, CLI,
  and your IDE.

GITHUB COPILOT IN SLACK AND MICROSOFT TEAMS
  [Claim 1]
  - Turn team conversations into shared agent sessions. Mention @GitHub
    to investigate problems, plan work, and make changes your team can
    follow and guide together.

GITHUB COPILOT APP
  [Claim 2]
  - The Customize tab is now generally available, bringing MCP servers,
    plugins, skills, and canvases together in one place.
  [Claim 3]
  - Turn Azure DevOps issues and pull requests into Copilot sessions
    from the Customize tab.
  [Claim 4]
  - Work in your Linux environment with experimental support for
    Windows Subsystem for Linux (WSL).
  [Claim 5]
  - Split and move any tab to keep related work side by side.
  [Claim 6]
  - Send any browser preview straight to your external browser from
    the tab's context menu.

GITHUB COPILOT CLI
  [Claim 7]
  - Start every new session with your preferred execution and
    permission modes using defaultMode and defaultPermissionMode.
  [Claim 8]
  - Manage plugins, MCP servers, and skills more easily with new
    experiences in /plugin, /mcp, and /skills.
  [Claim 9]
  - Pick up where you left off by restoring sessions that did not exit
    cleanly, including sessions interrupted mid-turn.
  [Claim 10]
  - Get significantly faster performance now that Copilot CLI runs on
    a native Rust runtime, while its terminal interface remains built
    in TypeScript.

GITHUB COPILOT FOR JETBRAINS
  [Claim 11]
  - Apply consistent enterprise controls for Copilot in JetBrains,
    including plugins, MCP servers, telemetry, and agent permission
    modes.

VS CODE 1.135 RELEASE UPDATES
  [Claim 12]
  - Continue recent Copilot or Claude agent sessions from other
    applications in VS Code.
  [Claim 13]
  - Get a second opinion from a complementary model to surface missed
    details and edge cases.
  [Claim 14]
  - Stay focused on your work with a new single-pane Agents layout,
    simpler session controls, and session details that are easier to
    find.
  [Claim 15]
  - See detailed chat usage by model for every chat turn.

GITHUB COPILOT FOR VISUAL STUDIO
  [Claim 16]
  - Pin favorite models, hide unused ones, compare capabilities and
    costs, and adjust reasoning effort for each task.
  [Claim 17]
  - Share custom agents across your organization to standardize
    workflows and improve discovery.
  [Claim 18]
  - View Copilot plan consumption and manage premium model usage
    before reaching limits.
  [Claim 19]
  - Review uncommitted changes or individual commits with the Git
    agent before opening a pull request.
```

## Cross-References

### Cross-reference verification notes

Claims cited from `docs-github-copilot-slack-shared-agentic-work.md`,
`docs-github-copilot-teams-shared-agentic-work.md`,
`docs-github-copilot-agent-plugins-1-0.md`,
`docs-github-copilot-vs-april-2026.md`,
`docs-github-copilot-jetbrains-harness-ga-aug2026.md`,
`docs-github-copilot-cli-terminal-ga.md`,
`docs-github-copilot-cli-settings-command.md`,
`docs-github-copilot-weekly-releases-aug10-2026.md`,
`docs-github-copilot-weekly-releases-aug3-2026.md`,
`docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`,
`docs-github-copilot-vs-june-2026.md`,
`docs-github-copilot-vs-july-2026.md`, and
`docs-github-copilot-vs-may-2026.md` were re-read directly in those notes
(via `### Claim N:` headings) before citing, per MINER.md §4b; claim numbers
are counted top-to-bottom in document order as they appear in each cited
note.

- **Corroborates** `docs-github-copilot-slack-shared-agentic-work.md` (Claim
  1, `@GitHub`-mention public preview) and `docs-github-copilot-teams-shared-agentic-work.md`
  (Claim 1, "collaborative agent session everyone can see and help direct"):
  Claim 1 of this note is a one-week-later, cross-platform-compressed
  restatement of both dedicated sources, with no new capability added.

- **Corroborates** `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  (Claim 1, "enterprise managed settings for plugin governance, MCP server
  access, OpenTelemetry, and permission modes"): Claim 11 of this note
  restates the identical four-category framing ten days later, matching the
  established pattern already documented for this same restatement type in
  `docs-github-copilot-weekly-releases-aug10-2026.md` (Claim 13, restating
  the same JetBrains source at a one-week lag) and (Claim 3, restating Agent
  Plugins 1.0 GA one day after its dedicated announcement).

- **Extends** `docs-github-copilot-agent-plugins-1-0.md` (Claim 4's "Our
  assessment," which lists "custom agents, commands, rules, hooks, canvases"
  as Copilot-specific plugin extras housed in the `com.github.copilot/`
  namespace directory, and that note's Scope section, which flagged the
  Copilot app's plugin-management UI as unfetched): Claim 2 of this note
  documents the Copilot app's Customize tab reaching GA as the surface where
  MCP servers, plugins, skills, and canvases are jointly managed, partially
  filling that documented gap.

- **Extends** `docs-github-copilot-vs-april-2026.md` (Claim 4, Azure DevOps
  work items as Visual Studio debugger-agent input): Claim 3 of this note
  documents a different surface (the standalone Copilot app's Customize tab)
  and a different mechanism (session-creation trigger from Azure DevOps
  issues/PRs, not debugging pipeline input) for Azure DevOps integration.

- **Extends and contrasts with** `docs-github-copilot-jetbrains-harness-ga-aug2026.md`
  (Claim 10, WSL worktree-startup-failure fix in JetBrains): Claim 4 of this
  note documents experimental, first-time WSL support in the standalone
  Copilot app — a different surface at an earlier maturity stage (new/
  experimental) than JetBrains' pre-existing (bug-fixed) WSL project
  support.

- **Extends** `docs-github-copilot-cli-terminal-ga.md` (Claim 5, CLI tab
  bar reorder/hide/off): Claim 5 of this note documents a mechanically
  distinct tab-splitting capability in the standalone Copilot app, not the
  CLI's terminal tab bar.

- **Extends** `docs-github-copilot-cli-settings-command.md` (Claim 3, every
  setting key surfaced via tab completion): Claim 7 of this note adds two
  setting keys (`defaultMode`, `defaultPermissionMode`) not named in that
  note's own inventory.

- **Extends** `docs-github-copilot-cli-terminal-ga.md` (Claims 6-8, `/mcp
  add`/`/mcp search`, `/skills`, `/plugin` at their June 23, 2026 GA): Claim
  8 of this note documents an unspecified "easier" refinement to all three
  commands roughly two months later, without describing the specific delta.

- **Extends** `docs-github-copilot-weekly-releases-aug10-2026.md` (Claim
  10, CLI `/app` context preservation) and `docs-github-copilot-teams-shared-agentic-work.md`
  (Claim 10, cloud-sandbox active/stopped/deleted lifecycle): Claim 9 of
  this note (CLI session recovery from unclean exits, including mid-turn)
  documents a distinct reliability mechanism — recovery from an *unplanned*
  interruption, not a deliberate stop/resume or cross-surface hand-off.

- **Extends** `docs-github-copilot-teams-shared-agentic-work.md` (Claim 2,
  continuing Teams-originated work "from your terminal, the GitHub Copilot
  app, or your preferred IDE") and `docs-github-copilot-slack-shared-agentic-work.md`
  (Claim 4, the same continuation model for Slack): Claim 12 of this note
  documents the reverse direction — VS Code as the landing surface for a
  session (Copilot or Claude) that began in an unnamed other application.

- **Extends** `docs-github-copilot-weekly-releases-aug10-2026.md` (Claim 16,
  per-turn Claude BYOK/built-in model switching within one VS Code session):
  Claim 13 of this note (complementary-model "second opinion") is a
  mechanically distinct, review-oriented capability rather than a
  free choice of execution model.

- **Extends** `docs-github-copilot-vs-june-2026.md` (Claim 1, refreshed
  Copilot Usage window with proactive limit alerts) and
  `docs-github-copilot-weekly-releases-aug3-2026.md` (Claim 1, the app's
  Auto mode disclosing which model handled a request): Claim 15 of this
  note (VS Code per-turn, per-model chat usage detail) is a third,
  differently-scoped usage-visibility mechanism in the corpus.

- **Extends** `docs-github-copilot-vs-june-2026.md` (Claim 1): Claim 18 of
  this note restates and appears to extend that note's proactive-limit-alert
  framing with an added "manage premium model usage" action verb, two
  months later.

- **Extends and is in tension with** `docs-github-copilot-vs-april-2026.md`
  (Claims 5-6, ungoverned user-level custom agents at
  `%USERPROFILE%/.github/agents/`): Claim 17 of this note documents
  org-level custom-agent sharing aimed at standardization — the opposite
  governance direction from the April note's flagged ungoverned personal
  path — without stating whether the two coexist or the new mechanism
  supersedes the old one.

- **Extends** `docs-github-copilot-vs-july-2026.md` (Claim 5, attaching a
  Git branch as chat context; Claim 3, "Review Selection" code-review
  action) and `docs-github-copilot-vs-may-2026.md` (Claim 10, Git commit
  history as a first-class context source): Claim 19 of this note names a
  dedicated "Git agent" performing pre-PR review of uncommitted
  changes/commits, distinct from both the general context-attachment
  pattern and the editor-selection review action.

- **Contradicts**: None identified. No claim in this source opposes an
  existing corpus position at the MINER.md §4a filing threshold. No
  contradiction issue filed.

- **Novel**:
  - First corpus documentation of "canvases" as a named artifact type
    jointly managed alongside MCP servers, plugins, and skills in the
    Copilot app's Customize tab, now GA (Claim 2).
  - First corpus documentation of Azure DevOps issue/PR-to-session
    conversion from the standalone Copilot app (Claim 3).
  - First corpus documentation of WSL support in the standalone Copilot app
    (Claim 4, experimental).
  - First corpus documentation of Copilot CLI session recovery from unclean
    exits, including mid-turn interruptions (Claim 9).
  - First corpus disclosure that Copilot CLI's core runtime has moved to
    Rust while its terminal interface remains TypeScript-based (Claim 10).
  - First corpus documentation of VS Code resuming a Claude agent session
    that originated in another (unnamed) application (Claim 12).
  - First corpus documentation of a "complementary model second opinion"
    review affordance in VS Code Chat (Claim 13).
  - First corpus documentation of per-task reasoning-effort control and
    model pin/hide/compare in Visual Studio's model picker (Claim 16).
  - First corpus documentation of organization-wide custom-agent sharing in
    Visual Studio (Claim 17).
  - First corpus documentation of a named "Git agent" performing dedicated
    pre-PR review of uncommitted changes and individual commits in Visual
    Studio (Claim 19).

## Guide Impact

### Chapter 01: Daily Workflows

- **Azure DevOps session creation (Copilot app)**: Document turning Azure
  DevOps issues/PRs into Copilot sessions from the Customize tab (Claim 3)
  as a cross-platform entry point for teams tracking work outside GitHub
  Issues.
- **Git agent pre-PR review (Visual Studio)**: Add the Git agent's
  uncommitted-changes/individual-commit review (Claim 19) as a recommended
  pre-PR self-review step, distinct from the existing Git-context-attachment
  and editor-selection-review patterns already documented for Visual Studio.
- **VS Code Agents layout refresh**: Note the single-pane Agents layout
  (Claim 14) as a UI change without asserting specific behavioral detail
  beyond what the source states.

### Chapter 02: Harness Engineering

- **Customize tab GA (Copilot app)**: Document the Customize tab's GA
  status and its four unified artifact types — MCP servers, plugins,
  skills, canvases (Claim 2) — as the standalone app's central
  extensibility-management surface.
- **CLI session-start defaults**: Add `defaultMode` and
  `defaultPermissionMode` (Claim 7) to the guide's `/settings` coverage as
  a way to standardize a practitioner's or organization's preferred
  session-start execution/permission baseline.
- **CLI Rust runtime**: Note the CLI's native Rust runtime migration (Claim
  10) as an internal performance rewrite that the source frames as
  behavior-preserving, while flagging the installation/distribution
  question as unconfirmed.
- **WSL support (Copilot app)**: Add experimental WSL support in the
  Copilot app (Claim 4) to the guide's environment-configuration options,
  distinguishing it from JetBrains' more mature, already-supported WSL
  project handling.
- **Visual Studio model management**: Add pin/hide/compare-models and
  per-task reasoning-effort control (Claim 16) to the guide's Visual Studio
  model-configuration coverage.
- **Visual Studio custom-agent governance**: Add org-wide custom-agent
  sharing (Claim 17) to the guide's Visual Studio agent-configuration
  section, flagging the open question of whether it supersedes the
  previously-documented ungoverned user-level agent path.

### Chapter 03: Verification and Safety

- **CLI session recovery**: Document mid-turn session recovery (Claim 9) as
  a reliability improvement relevant to long-running or unattended CLI
  sessions, where a crash or disconnect previously meant losing in-progress
  work.

### Chapter 04: Agentic Workflows — Multi-Session, Cost Management

- **VS Code as a session-landing surface**: Add VS Code's ability to
  continue Copilot or Claude sessions from other applications (Claim 12) to
  the guide's cross-surface session-continuity coverage, flagging the
  unnamed "other applications" as an open question.
- **Complementary-model second opinion**: Document the VS Code "second
  opinion" affordance (Claim 13) as an in-product verification aid, pending
  a more detailed source on its invocation mechanism.
- **Three distinct usage-visibility surfaces**: Note VS Code's per-turn,
  per-model chat usage detail (Claim 15) as a third, separately-documented
  usage-visibility mechanism alongside the Copilot app's Auto-mode model
  disclosure and Visual Studio's Copilot Usage window — not a single
  unified reporting feature.
- **Visual Studio premium usage management**: Update the Visual Studio
  Copilot Usage window guidance (sourced from
  `docs-github-copilot-vs-june-2026.md`) to note the added "manage premium
  model usage" action verb (Claim 18), flagging the specific mechanism as
  unconfirmed.

### Chapter 05: Team Adoption

- **Slack/Teams team sessions remain active**: No new rollout guidance
  beyond confirming `docs-github-copilot-slack-shared-agentic-work.md` and
  `docs-github-copilot-teams-shared-agentic-work.md` remain the
  authoritative sources (Claim 1).
- **JetBrains enterprise controls remain active**: No new governance
  guidance beyond confirming
  `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  remains the authoritative source (Claim 11).
- **Visual Studio custom-agent standardization**: Cite org-wide custom-agent
  sharing (Claim 17) as a rollout tool for teams wanting to standardize
  Visual Studio agent configurations across an organization.

## Extraction Notes

1. **WebFetch discarded in favor of raw HTML, per established corpus
   precedent**: Following the precedent in
   `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 1 and
   `docs-github-copilot-weekly-releases-aug10-2026.md` Extraction Note 1, the
   article was fetched as raw HTML via `curl` with a browser user-agent, then
   converted to plain text with `html2text` (link/structure-preserving,
   non-summarizing conversion) to produce a verbatim transcript of every
   heading and bullet. An initial WebFetch pass was also run for orientation;
   comparing its output against the raw-HTML transcript confirmed it
   consistently paraphrased bullets (e.g., rendering Claim 8's "Manage
   plugins, MCP servers, and skills more easily with new experiences in
   /plugin, /mcp, and /skills" as "Enhanced plugin, MCP server, and skill
   management through updated /plugin, /mcp, and /skills experiences") without
   inventing new content. None of the WebFetch pass's paraphrased text was
   used in any `Quote` field; all quotes above were copied character-for-
   character from the raw-HTML-derived transcript, including the curly
   apostrophe in Claim 6's "tab's context menu" (confirmed present in the raw
   HTML as the `&rsquo;` entity before conversion).
2. **No linked sub-pages followed**: Unlike several prior notes in the
   weekly-digest and JetBrains families (e.g.,
   `docs-github-copilot-weekly-releases-aug10-2026.md`'s JetBrains
   sub-changelog, `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`'s
   two reference pages), this digest's only outbound links are same-page
   table-of-contents anchors, "Try the Copilot app," "Install the Copilot
   CLI," "the full VS Code 1.135 release notes" (general, non-Copilot-specific
   VS Code notes — not followed, consistent with the precedent in
   `docs-github-copilot-weekly-releases-aug10-2026.md` Extraction Note 2),
   and "Install the latest version of Visual Studio." None link to a deeper,
   Copilot-specific sub-page for any of this digest's 19 bullets — every
   bullet here is a terminal, standalone statement with no further linked
   detail to follow, unlike the JetBrains sub-changelog precedent in the
   August 10 note.
3. **Broad surface coverage, no bullets folded into Concrete Artifacts
   only**: Unlike the two prior weekly-digest notes, which each folded one
   thin, unquantified bullet (a bare "sessions start and switch more
   efficiently" performance claim in the August 3 note, and five UX-polish
   bullets in the August 10 note's linked sub-changelog) into Concrete
   Artifacts without a dedicated Claim, every one of this digest's 19
   bullets received an individual Claim entry — including several thin ones
   (Claims 5, 6, 14) — because each names a specific, distinct, previously
   undocumented UI or product capability rather than a bare unquantified
   performance/quality assertion. This digest is broader (six surfaces, 19
   bullets total) than either prior weekly digest (three and five surfaces,
   12 and 18 bullets respectively), reflecting the growing scope of the
   weekly-release series over the roughly three-week gaps between mined
   entries in this corpus.
4. **Two restatement claims (Claims 1, 11) confirmed against dedicated
   sources, not treated as new information**: Per the established pattern
   documented in `docs-github-copilot-weekly-releases-aug10-2026.md`
   Extraction Note and Claim 3/Claim 13, this digest's Slack/Teams and
   JetBrains bullets were each verified against their dedicated,
   already-mined source notes (published one and ten days earlier,
   respectively) before writing Claims 1 and 11 — both were confirmed as
   restatements with no new capability, not independently re-assessed as if
   novel.
5. **No contradictions identified**: Cross-referencing against thirteen
   existing source notes (see Cross-reference verification notes) found no
   claim in this source that materially opposes an existing corpus position
   leading to different guide advice. No contradiction issue filed.
6. **Several claims flagged as thin/underspecified rather than resolved by
   inference**: Claims 8 (CLI `/plugin`/`/mcp`/`/skills` "new experiences"),
   13 (VS Code "second opinion" invocation mechanism), 16 (Visual Studio
   reasoning-effort levels and model support), 17 (whether org-shared
   custom agents supersede the ungoverned user-level path), and 18 (what
   "manage premium model usage" concretely allows) each name a real
   capability without enough source detail to fully specify its mechanism.
   Each is flagged explicitly in its own "Our assessment" as an open
   question rather than resolved by plausible-sounding inference, consistent
   with MINER.md's instruction to extract specific claims rather than
   paraphrase into generic bullets.
