---
source_url: https://github.blog/changelog/2026-09-22-new-features-and-improvements-in-copilot-for-jetbrains
source_type: docs
title: "New features and improvements in Copilot for JetBrains"
author: GitHub (official changelog)
date_published: 2026-09-22
date_extracted: 2026-09-24
last_checked: 2026-09-24
status: current
confidence_overall: settled
issue: "#3655"
---

# New Features and Improvements in Copilot for JetBrains (1.18.0)

> GitHub's September 22, 2026 JetBrains changelog (Copilot for JetBrains 1.18.0)
> announces AI-assisted tool approvals in public preview (auto-approving
> low-risk tool calls while still prompting for higher-risk ones), the ability
> to re-edit an earlier chat message with conversation and file-change rewind,
> organization/enterprise skills and organization-managed custom instructions
> reaching "Local and Copilot agent sessions," plan mode for the Codex agent,
> and a settings toggle plus persistent per-tool controls for the built-in
> GitHub MCP Server. It also hides inline chat in JetBrains Gateway/remote
> development environments and gives advance deprecation notice for JetBrains
> IDE 2025.1.

## Source Context

- **Type**: docs (GitHub official product changelog, September 22, 2026; tagged
  "Release," "2 minute read," tagged `copilot`). No sub-pages were followed —
  the only two links in the article body are a JetBrains Marketplace plugin
  listing (`plugins.jetbrains.com/plugin/17718-...`) and a GitHub issues
  feedback repository (`github.com/microsoft/copilot-intellij-feedback/issues`),
  both navigational/feedback links rather than substantive documentation, per
  the same treatment given to equivalent links in every prior note in this
  family (see `docs-github-copilot-jetbrains-harness-ga-aug2026.md`,
  Extraction Notes §3).
- **Author credibility**: GitHub engineering team announcing a versioned
  plugin release (1.18.0, per the lede sentence) for the JetBrains Copilot
  plugin. Authoritative for the existence and stated behavior of each named
  feature. Not authoritative for implementation mechanics beyond what is
  stated — e.g., the changelog does not define the risk-classification logic
  behind "AI-assisted tool approvals" (Claim 1), nor does it name a specific
  managed-settings key for the new organization/enterprise skills and
  instructions support (Claim 3).
- **Scope**: Five "What's new" items (AI-assisted tool approvals, re-edit
  earlier messages, shared skills and instructions, Codex agent plan mode,
  MCP tool controls), a "User experience enhancements" section (one new
  side-by-side chat panel plus five discoverability bullets), a "Quality
  improvements" paragraph, a "Changed" item (inline chat hidden in JetBrains
  Gateway/remote dev), and a "Deprecation" notice (JetBrains IDE 2025.1). Does
  NOT cover: a settings path or exact UI location for AI-assisted tool
  approvals, a definition of what counts as "low-risk" vs. higher-risk for
  that feature, a managed-settings key name for organization/enterprise
  skills, or a JetBrains plugin version floor for any individual feature.

## Extracted Claims

### Claim 1: AI-assisted tool approvals ("assisted approvals") are now in public preview for Copilot agent sessions, automatically approving low-risk tool calls while continuing to prompt for higher-risk actions

- **Evidence**: Changelog "What's new" section, "AI-assisted tool approvals"
  heading — the lead announcement of the release.
- **Confidence**: emerging (explicitly public preview)
- **Quote**: "AI-assisted tool approvals, called assisted approvals, are now in public preview for Copilot agent sessions. Low-risk tool calls receive automatic approval, while higher-risk actions continue to prompt you for a decision."
- **Our assessment**: This is a materially different governance mechanism
  from the rule-based `permissions.deny`/`ask`/`allow` selector system
  documented in `docs-github-copilot-enterprise-agent-operations-permissions.md`
  (Claims 1, 6, 9-10): that system requires an administrator to author
  explicit `Shell(...)`/`Read(...)`/`Edit(...)`/`Domain(...)` rules in
  managed-settings, with unmatched operations defaulting to "ask" if any rule
  source is configured. "Assisted approvals" instead implies GitHub's own
  model or heuristic classifies a given tool call's risk level and decides
  automatically, without an administrator pre-authoring a matching rule. The
  changelog does not state whether assisted approvals defer to (or are
  overridden by) an enterprise's `permissions.ask`/`permissions.deny` rules
  when both are active, nor whether JetBrains's own bypass-mode control
  (`docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  Claim 5, `permissions.disableBypassPermissionsMode`) interacts with this
  feature at all. This is a genuine architectural gap worth flagging for a
  follow-up source, since practitioners and administrators reading both
  systems side by side would reasonably ask which one wins in a conflict.

### Claim 2: Practitioners can now re-edit a previous user message in a Copilot agent session, with Copilot rewinding both the conversation and file changes before the replacement message is sent

- **Evidence**: Changelog "What's new" section, "Re-edit earlier messages"
  heading.
- **Confidence**: settled (product fact, no preview qualifier stated)
- **Quote**: "You can now re-edit a previous user message in a Copilot agent session. Before sending your replacement message, Copilot rewinds both the conversation and file changes."
- **Our assessment**: This is the first JetBrains-specific source in this
  corpus family to document message-level rewind that also reverts file
  changes, not just conversation state. It functions as a JetBrains-native
  equivalent to "conversation forking" or checkpoint/rewind mechanics
  documented at the general product level elsewhere in the corpus (e.g.,
  `docs-github-copilot-vscode-may-2026.md` documents VS Code session
  mechanics but not an equivalent rewind-with-file-revert feature as of
  May 2026). The changelog does not state a limit on how far back a
  practitioner can re-edit, whether rewound file changes are recoverable if
  the re-edit is a mistake, or whether this applies to CLI-provider or
  Claude-provider sessions as well as the native Copilot agent — "Copilot
  agent session" is used without the three-way session-type qualification
  (local / CLI / Cloud Agent) this family's June 22 note established (see
  Cross-References → Extends).

### Claim 3: Local and Copilot agent sessions now support organization and enterprise skills, along with organization-managed custom instructions

- **Evidence**: Changelog "What's new" section, "Shared skills and
  instructions" heading.
- **Confidence**: emerging (no preview qualifier is stated in the text, but
  the underlying managed-settings key, if any, is unconfirmed — see Our
  assessment)
- **Quote**: "Local and Copilot agent sessions now support organization and enterprise skills, along with organization-managed custom instructions. You can use shared skills and organizational guidance in both types of sessions."
- **Our assessment**: This adds a JetBrains-specific rung to a corpus-wide
  instructions/skills hierarchy this extraction cross-checked in detail (see
  Cross-References → Extends). Two ambiguities are worth flagging rather than
  resolving here: (1) "Local and Copilot agent sessions" as a two-way split
  does not match the three-way session taxonomy (local / CLI / Cloud Agent)
  this family's June 22 note documented in its unified sessions view — it is
  unclear whether "Copilot agent sessions" here means the CLI-provider
  sessions, the Cloud Agent sessions, or is being used as an umbrella term
  distinct from "Local"; the source does not clarify. (2) As of the most
  recent enterprise managed-settings reference-page snapshot in this corpus
  (`docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`,
  Claim 6, Aug 18, 2026), the JetBrains-supported managed-settings keys list
  does not include any key governing skills — only `enabledPlugins`,
  `extraKnownMarketplaces`, `strictKnownMarketplaces`, `telemetry`,
  `allowedMcpServers`, `deniedMcpServers`, and
  `permissions.disableBypassPermissionsMode`. This changelog claims
  organization/enterprise-level skills governance now reaches JetBrains
  without naming a managed-settings key, which — given this same reference
  page's history of lagging changelog announcements for JetBrains coverage
  (issues #3334 and #2802, both filed from notes in this family) — is worth a
  targeted re-check of the reference page rather than treating "organization
  and enterprise skills" as necessarily implemented via `managed-settings.json`
  at all. Not filed as a contradiction per MINER.md §4a, since no existing
  note makes an opposing claim about skills specifically — this is a coverage
  gap, not two sources in tension.

### Claim 4: The Codex agent now supports plan mode in Copilot for JetBrains, letting practitioners review, refine, or approve a plan before implementation

- **Evidence**: Changelog "What's new" section, "Plan with the Codex agent"
  heading.
- **Confidence**: settled (product fact, no preview qualifier stated)
- **Quote**: "The Codex agent now supports plan mode. You can review, refine, or approve a plan before implementation, giving you an opportunity to shape the approach before the agent starts making changes."
- **Our assessment**: This confirms and extends a gap this extraction's
  cross-referencing surfaced in `docs-github-copilot-jetbrains-harness-ga-aug2026.md`
  (Claim 10, Aug 24, 2026), which found "Codex" named for the first time in
  this JetBrains family inside a bug-fix sentence ("restores file and folder
  # references in Copilot, Claude, and Codex chat inputs") with no dedicated
  feature announcement, and flagged this as "a likely gap in this corpus's
  JetBrains coverage" worth a targeted follow-up search. This September 22
  changelog is that follow-up: it confirms Codex is a named, first-class
  agent option in JetBrains Copilot (alongside the native Copilot agent, the
  Copilot CLI agent, and Claude as agent providers) and gives it a specific
  new capability — plan mode — comparable to the "Plan" mode already
  documented for the native agent picker in
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 1). The
  Aug 24 gap is now partially closed: Codex's existence as a JetBrains chat
  surface is confirmed, though the changelog announcing Codex's *initial*
  availability (as opposed to this plan-mode addition to it) still has not
  been identified in this corpus.

### Claim 5: A new setting lets practitioners turn the built-in GitHub MCP Server on or off without changing manually configured MCP servers, and Copilot agent sessions gain persistent per-tool controls for MCP servers including the built-in server

- **Evidence**: Changelog "What's new" section, "More control over MCP tools"
  heading, two paragraphs.
- **Confidence**: settled (product fact, no preview qualifier stated)
- **Quote**: "A new setting lets you turn the built-in GitHub MCP Server on or off without changing manually configured MCP servers. The built-in server remains enabled by default."
- **Quote**: "Copilot agent sessions also gain persistent per-tool controls for MCP servers. You can manage individual tools as well as control whether the built-in server is enabled."
- **Our assessment**: This is a different MCP capability from the JetBrains
  built-in MCP *server* documented in
  `docs-github-copilot-jetbrains-harness-ga-aug2026.md` (Claim 2, Aug 24,
  2026, public preview): that earlier claim described JetBrains itself
  *exposing* IDE capabilities *as* an MCP server for agents to call into.
  This claim describes a different, named entity — "the built-in GitHub MCP
  Server" — which by name and behavior (a pre-configured MCP *client*
  connection to GitHub's own MCP server, enabled by default, toggleable
  without touching manually configured servers) matches the "GitHub MCP
  Server" built into other Copilot surfaces, e.g. the Docker-based/hosted
  GitHub MCP Server documented for GitHub Actions-based coding agent sessions
  in `docs-ghaw-github-tools.md` (local/remote deployment modes). This
  changelog does not clarify whether the JetBrains "built-in GitHub MCP
  Server" is the same GitHub-hosted server referenced in the GHAW context or
  a JetBrains-specific instance — but the naming strongly suggests GitHub is
  standardizing "GitHub MCP Server" as one recurring, built-in tool surfaced
  across multiple Copilot clients, distinct from the "JetBrains-as-MCP-server"
  capability from the Aug 24 note. "Persistent per-tool controls" is new: no
  prior JetBrains note documents session-to-session persistence of individual
  tool enable/disable state.

### Claim 6: A new side-by-side chat panel switcher in the session toolbar lets practitioners chat in the editor while browsing sessions in the tool window

- **Evidence**: Changelog "User experience enhancements" section, "Chat
  alongside your sessions" heading.
- **Confidence**: settled (product fact, no preview qualifier stated)
- **Quote**: "A new side-by-side chat panel switcher in the session toolbar lets you chat in the editor while browsing sessions in the tool window. You can keep your conversation open alongside the session list."
- **Our assessment**: This is a layout enhancement to the same tool-window
  surface documented as the "unified sessions view" in
  `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claims 5-6, May 13,
  2026: a chat-window feature aggregating all agent sessions with title,
  agent type, elapsed time, and status). This claim adds the ability to keep
  an active chat panel open side-by-side with that session list, rather than
  navigating away from it to converse — a discoverability/ergonomics
  refinement, not a new session-tracking capability.

### Claim 7: This release adds browsable usage tips above the chat input, a simplified chat welcome screen with a direct feedback link, a labeled built-in GitHub MCP Server entry with a settings link in the tool configuration interface, restored shortcuts for updating agent instructions and viewing usage-based billing best practices, and a clarified `/init` tip grouped with customizations

- **Evidence**: Changelog "User experience enhancements" section, five
  bullet items following the "Chat alongside your sessions" item.
- **Confidence**: settled (UX polish items, no preview qualifiers)
- **Quote**: "Added browsable usage tips above the chat input with shortcuts to commands, customizations, and settings"
- **Quote**: "Labeled the built-in GitHub MCP Server in the tool configuration interface and added a direct link to its settings"
- **Our assessment**: The "Labeled the built-in GitHub MCP Server... and added a direct link to its settings" bullet directly supports Claim 5's built-in-server toggle — it is the discoverability counterpart, surfacing the server's identity and settings entry point inside the tool configuration UI where the new on/off setting presumably lives. "Restored shortcuts for updating agent instructions" implies these shortcuts existed before and had regressed, though no prior note in this family documents their original introduction or a prior removal — flagged as an unexplained regression/restoration, not independently verifiable from this corpus. "Clarified the `/init` tip and grouped it with customizations" ties `/init` (a command not otherwise defined in this changelog) to the existing Agent Customizations editor documented in `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 8).

### Claim 8: This update improves inline chat reliability — preserving edits when requests end and respecting selected thinking effort and context window settings — addresses Codex session startup issues, improves behavior across multiple project windows, and restores embedded editors and message re-editing on IntelliJ 2026.3 EAP builds

- **Evidence**: Changelog "Quality improvements" section, full paragraph.
- **Confidence**: settled (bug-fix/reliability list, stated as shipped, no
  preview qualifiers)
- **Quote**: "This update improves inline chat reliability, including preserving your edits when requests end and respecting selected thinking effort and context window settings. It also addresses Codex session startup issues, improves behavior across multiple project windows, and restores embedded editors and message re-editing on IntelliJ 2026.3 EAP builds."
- **Our assessment**: "Respecting selected thinking effort and context window settings" is a reliability fix to the configurable thinking-effort-per-request feature documented in
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 7,
  June 22, 2026) — implying inline chat requests were previously not
  consistently honoring a practitioner's chosen thinking-effort level before
  this fix. "Addresses Codex session startup issues" is notable set against
  Claim 4 above: Codex sessions apparently already had enough real-world
  usage in JetBrains by this release to accumulate startup reliability bugs,
  further corroborating that Codex was already a functioning (if
  under-documented in this corpus) JetBrains agent surface before this
  release's plan-mode addition. "Restores embedded editors and message
  re-editing on IntelliJ 2026.3 EAP builds" directly qualifies Claim 2 (the
  new re-edit-message feature): it did not work correctly on IntelliJ 2026.3
  Early Access Program builds and has now been fixed there specifically —
  the only EAP-specific regression named in this changelog.

### Claim 9: Inline chat and its entry points are now hidden in JetBrains Gateway and remote development environments

- **Evidence**: Changelog "Changed" section, sole item.
- **Confidence**: settled (product behavior change, stated definitively)
- **Quote**: "Inline chat and its entry points are now hidden in JetBrains Gateway and remote development environments."
- **Our assessment**: No prior note in this family documents inline chat's
  behavior specifically under JetBrains Gateway or remote development setups.
  The changelog gives no reason for the change (e.g., a known incompatibility
  or reliability issue with inline chat in remote/Gateway contexts) — it is
  recorded here as a scoped feature-visibility change, not a bug fix, since
  it appears in "Changed" rather than "Quality improvements." Practitioners
  working in JetBrains Gateway or other remote-development configurations
  should not expect to find inline chat's UI entry points at all going
  forward, as opposed to encountering a known bug.

### Claim 10: JetBrains IDE version 2025.1 users will now see advance notice to upgrade to 2026.1 or later, though support remains unchanged in this release

- **Evidence**: Changelog "Deprecation" section, sole item.
- **Confidence**: settled (deprecation notice, explicitly scoped: "Support remains unchanged in this release")
- **Quote**: "If you use a JetBrains IDE version 2025.1, you will see advance notice to upgrade to 2026.1 or later. Support remains unchanged in this release."
- **Our assessment**: This is the first explicit JetBrains IDE version-floor
  signal in this corpus family — every prior note flagged the *absence* of a
  stated plugin/IDE version floor (e.g.,
  `docs-github-copilot-jetbrains-harness-ga-aug2026.md`, Source Context: "or a
  JetBrains plugin version floor"). This changelog does not yet drop 2025.1
  support, but it is the first advance warning that a future release likely
  will. For a guide advising practitioners on JetBrains IDE version planning,
  this is actionable: organizations still on IDE 2025.1 should plan an
  upgrade path to 2026.1+ before support is actually withdrawn, even though
  no removal date is given here.

## Concrete Artifacts

### Full changelog body (verbatim, raw-HTML-extracted)

```
GitHub Copilot for JetBrains 1.18.0 brings AI-assisted tool approvals,
more control over agent conversations, and shared skills and
instructions for your organization. You can also review plans with
the Codex agent and manage MCP tools with persistent controls.

What's new

AI-assisted tool approvals
AI-assisted tool approvals, called assisted approvals, are now in
public preview for Copilot agent sessions. Low-risk tool calls
receive automatic approval, while higher-risk actions continue to
prompt you for a decision.
This gives you fewer approval interruptions for low-risk actions
while keeping higher-risk decisions in your hands.

Re-edit earlier messages
You can now re-edit a previous user message in a Copilot agent
session. Before sending your replacement message, Copilot rewinds
both the conversation and file changes.
This lets you revise an earlier request and continue from that
point, rather than adding another message to correct the direction
of the conversation.

Shared skills and instructions
Local and Copilot agent sessions now support organization and
enterprise skills, along with organization-managed custom
instructions. You can use shared skills and organizational guidance
in both types of sessions.

Plan with the Codex agent
The Codex agent now supports plan mode. You can review, refine, or
approve a plan before implementation, giving you an opportunity to
shape the approach before the agent starts making changes.

More control over MCP tools
A new setting lets you turn the built-in GitHub MCP Server on or off
without changing manually configured MCP servers. The built-in
server remains enabled by default.
Copilot agent sessions also gain persistent per-tool controls for
MCP servers. You can manage individual tools as well as control
whether the built-in server is enabled.

User experience enhancements

Chat alongside your sessions
A new side-by-side chat panel switcher in the session toolbar lets
you chat in the editor while browsing sessions in the tool window.
You can keep your conversation open alongside the session list.
Other updates make features and settings easier to discover:
- Added browsable usage tips above the chat input with shortcuts to
  commands, customizations, and settings
- Simplified the chat welcome screen and added a direct feedback link
- Labeled the built-in GitHub MCP Server in the tool configuration
  interface and added a direct link to its settings
- Restored shortcuts for updating agent instructions and viewing
  usage-based billing best practices
- Clarified the /init tip and grouped it with customizations

Quality improvements
This update improves inline chat reliability, including preserving
your edits when requests end and respecting selected thinking effort
and context window settings. It also addresses Codex session startup
issues, improves behavior across multiple project windows, and
restores embedded editors and message re-editing on IntelliJ 2026.3
EAP builds.

Changed
Inline chat and its entry points are now hidden in JetBrains Gateway
and remote development environments.

Deprecation
If you use a JetBrains IDE version 2025.1, you will see advance
notice to upgrade to 2026.1 or later. Support remains unchanged in
this release.
```
Source: "New features and improvements in Copilot for JetBrains," github.blog
changelog, September 22, 2026 (raw HTML fetched via `curl`, tags stripped,
HTML entities decoded; the article body was present directly in the served
HTML rather than requiring `__NEXT_DATA__` JSON parsing).

### Page metadata (as fetched)

```
Title: "New features and improvements in Copilot for JetBrains - GitHub Changelog"
Tag: Release
Published: September 22, 2026 (datetime="2026-09-22")
Read time: 2 minute read
Section anchors: #whats-new, #user-experience-enhancements,
  #quality-improvements, #changed, #deprecation, #try-it-out,
  #share-your-feedback
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 7,
    configurable thinking effort per request): Claim 8 above's inline-chat
    reliability fix ("respecting selected thinking effort and context window
    settings") confirms thinking-effort configuration is a real, still-live
    JetBrains setting that had a reliability gap now fixed.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claims 5-6,
    unified sessions view) and
    `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 6,
    local/CLI/Cloud Agent session types in that view): Claim 6 above's
    side-by-side chat panel switcher confirms the unified sessions view tool
    window remains the active development surface for session-management UX.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 8,
    Agent Customizations editor): Claim 7 above's "/init tip... grouped with
    customizations" ties into the same editor.

- **Contradicts**: None filed. Claim 3's organization/enterprise skills
  announcement is in tension with the JetBrains-supported managed-settings
  key list from `docs-github-copilot-jetbrains-enterprise-managed-settings-aug2026.md`
  (Claim 6), which lists no skills-governance key as of Aug 18, 2026 — but
  this extraction does not treat it as a filable contradiction under
  MINER.md §4a, since no existing note makes an *opposing claim about skills
  specifically* (the Aug 18 note's Claim 6 is a supported-keys snapshot, not
  a claim that skills governance will never reach JetBrains). It is recorded
  as an open coverage gap in Claim 3's Our assessment and flagged for a
  Prospector follow-up (re-check the reference page's current "Supported
  keys" table for a skills-related key), consistent with the pattern already
  established by issues #3334 and #2802 in this same family.

- **Extends**:
  - `docs-github-copilot-jetbrains-harness-ga-aug2026.md` (Claim 10, Codex
    named incidentally in a bug-fix sentence, flagged as a likely JetBrains
    coverage gap) — Claim 4 above is the direct follow-up this extraction's
    Prospector-flagged gap called for: Codex is now confirmed as a
    first-class, named JetBrains agent option with its own feature additions
    (plan mode) and its own bug fixes (Claim 8's "Codex session startup
    issues").
  - `docs-github-copilot-jetbrains-harness-ga-aug2026.md` (Claim 2, JetBrains
    exposing IDE capabilities as a built-in MCP server, public preview) —
    Claim 5 above documents a related but distinct MCP capability (the
    built-in GitHub MCP *Server* as an outbound client connection with a new
    on/off setting and per-tool controls), not the same feature; both are
    now part of JetBrains's growing MCP surface.
  - `docs-ghaw-github-tools.md` (local/remote GitHub MCP Server deployment
    modes for GitHub Actions-based coding agent sessions) — Claim 5 above
    extends the corpus's coverage of "the GitHub MCP Server" as a recurring,
    named built-in tool to a third Copilot surface (JetBrains), alongside the
    GHAW/coding-agent context already documented.
  - `docs-github-copilot-vs-july-2026.md` (Claim 4, Visual Studio
    organization-level custom instructions, explicitly scoped as
    "preferences, not policy," Business/Enterprise-gated, individually
    opt-out-able) and `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md`
    (Claim 3, Claude-provider-specific customizations support for skills and
    instructions, Pro-and-higher, public preview) — Claim 3 above extends
    this corpus's multi-tier instructions/skills hierarchy (personal/workspace
    scope per `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
    Claim 8 → Claude-provider skills per the July 14 note → org-level chat
    instructions in Visual Studio) with an organization/enterprise skills and
    instructions tier now reaching JetBrains specifically, though without the
    governance-mechanism detail (managed-settings key, opt-out mechanism,
    plan-tier gating) those two prior notes each supplied for their
    respective surfaces.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 1,
    "Plan" as an existing agent-picker mode for the native Copilot agent) —
    Claim 4 above extends plan-mode availability to the Codex agent
    specifically, a second agent provider now offering the same
    review-before-execute pattern.

- **Novel**:
  - **First corpus source naming "AI-assisted tool approvals" / "assisted
    approvals"** (Claim 1) — a risk-classification-based auto-approval
    mechanism distinct from the rule-based `permissions.deny`/`ask`/`allow`
    selector system documented for enterprise-managed agent operations. No
    prior source in the corpus describes an approval decision being made by
    an automatic risk assessment rather than a pre-authored rule or a human
    prompt.
  - **First corpus source documenting message-level rewind that reverts both
    conversation and file changes** (Claim 2) for a JetBrains Copilot agent
    session.
  - **First confirmed, dedicated feature announcement for the Codex agent in
    JetBrains** (Claim 4) — resolving (in part) a gap this same extraction's
    cross-referencing surfaced from the Aug 24, 2026 note in this family.
  - **First corpus source distinguishing "the built-in GitHub MCP Server" (an
    outbound client connection) from "JetBrains-as-MCP-server" (an inbound
    capability-exposure feature)** (Claim 5) as two separate MCP surfaces
    within the same product.
  - **First explicit JetBrains IDE version-floor deprecation notice** in this
    corpus family (Claim 10).

## Guide Impact

- **Chapter 02 (Harness Engineering — Permissions & Approval Models)**: Add
  "AI-assisted tool approvals" (Claim 1) as a second, architecturally
  distinct approval mechanism alongside the rule-based
  `permissions.deny`/`ask`/`allow` system already documented — flag the
  unresolved interaction question (which one governs when both are
  configured) as an open item for practitioners and administrators to verify
  directly in-product rather than assume from either source.

- **Chapter 02 (Harness Engineering — MCP Configuration)**: Document the new
  built-in GitHub MCP Server on/off setting and persistent per-tool controls
  (Claim 5) as a JetBrains-specific refinement; note it as a distinct
  capability from JetBrains's own IDE-as-MCP-server feature (already in the
  guide via the Aug 24 note) to avoid conflating the two.

- **Chapter 02 (Harness Engineering — Agent Configuration / Governance)**:
  Add organization/enterprise skills and organization-managed custom
  instructions reaching JetBrains (Claim 3) to the guide's multi-surface
  instructions hierarchy coverage, explicitly flagging the unconfirmed
  governance mechanism and recommending administrators verify against the
  current enterprise managed-settings reference page before relying on it
  for compliance purposes.

- **Chapter 04 (Agentic Workflows — Multi-Agent / Provider Choice)**: Add
  Codex plan mode (Claim 4) to JetBrains agent-provider coverage; note Codex
  is now a confirmed, actively-developed (per its own bug fixes in Claim 8)
  JetBrains agent surface.

- **Chapter 01 (Daily Workflows)**: Note message re-edit with conversation
  and file-change rewind (Claim 2) as a recovery mechanism for course-
  correcting an agent session without accumulating corrective follow-up
  messages.

- **Chapter 04/05 (Governance & Team Adoption — Version Planning)**: Flag the
  JetBrains IDE 2025.1 deprecation advance notice (Claim 10) for
  organizations planning IDE upgrade cadences alongside Copilot plugin
  updates.

- **Prospector follow-up**: Re-check the "Enterprise managed settings
  reference" page's JetBrains "Supported keys" table for any
  skills-governance key that might implement Claim 3's organization/
  enterprise skills claim — this reference page has now lagged JetBrains
  changelog announcements twice before (issues #3334, #2802) in this same
  source family, so a third potential gap is worth a dedicated check rather
  than assuming the claim is either confirmed or unimplemented.

## Extraction Notes

1. **Raw HTML extraction, not WebFetch summarization**: Per MINER.md §2a and
   the established pattern in this source family, the changelog was fetched
   directly via `curl` rather than relying on a summarizing fetch tool. In
   this case the full article body (`<div class="PostContent-main">`) was
   present as a complete, pre-rendered HTML fragment directly in the served
   page — not embedded in a `__NEXT_DATA__` JSON payload as with some
   `docs.github.com` reference pages fetched by earlier notes in this family.
   All quotes above were copied character-for-character from that raw HTML
   after tag-stripping and entity decoding.
2. **No sub-pages followed**: the only two links in the article body are a
   JetBrains Marketplace plugin listing and a GitHub issues feedback
   repository — both navigational, not documentation, consistent with the
   treatment of equivalent links in every prior note in this family.
3. **Ten claims extracted from a compact (~2-minute-read) changelog**: five
   "What's new" items, one multi-part UX item plus a five-bullet
   discoverability list (split as Claims 6-7), one "Quality improvements"
   paragraph, one "Changed" item, and one "Deprecation" item.
4. **Coverage gap flagged, not resolved, for Claim 3**: this extraction
   deliberately did not re-fetch the enterprise managed-settings reference
   page to check for a skills-governance key, since doing so was outside the
   scope of a single Prospector-flagged changelog entry and the existing
   corpus already documents this reference page's tendency to lag JetBrains
   announcements (issues #3334, #2802) — re-checking it is recommended as
   Prospector follow-up work instead (see Guide Impact).
5. **No contradictions filed**: see Cross-References → Contradicts above for
   the reasoning on why Claim 3's coverage gap does not meet the MINER.md
   §4a bar for a formal contradiction issue.
