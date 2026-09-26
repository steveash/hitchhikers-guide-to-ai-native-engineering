---
source_url: https://github.blog/changelog/2026-09-25-github-copilot-weekly-releases-september-21
source_type: docs
title: "GitHub Copilot weekly releases — September 21"
author: GitHub (official changelog)
date_published: 2026-09-25
date_extracted: 2026-09-26
last_checked: 2026-09-26
status: current
confidence_overall: emerging
issue: "#3722"
---

# GitHub Copilot Weekly Releases — September 21

> GitHub's September 25, 2026 weekly digest covers four Copilot model
> additions (Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, Grok 4.7), local
> sandboxing and OpenTelemetry in the standalone Copilot app (both already
> fully mined from their own dedicated changelogs), Slack/Teams
> conversation-management improvements, and — most substantively — a
> JetBrains 1.18.0 release that the digest itself compresses into three
> bullets but whose linked dedicated changelog discloses AI-assisted tool
> approvals, message-rewind editing, org-wide shared skills, Codex-agent
> plan mode, and new per-tool MCP server controls. The dedicated JetBrains
> changelog was fetched and mined in full per MINER.md §1's instruction to
> follow substantive linked pages, since — as with the HydraFusion post in
> the prior weekly note (`docs-github-copilot-weekly-releases-sept7-2026.md`)
> — the digest's own text on this item is thin relative to the linked
> source.

## Source Context

- **Type**: docs (GitHub official product changelog, September 25, 2026;
  self-tagged "Release," "2 minute read"; four sections — "GitHub Copilot,"
  "GitHub Copilot app," "GitHub Copilot in Slack and Microsoft Teams,"
  "GitHub Copilot in JetBrains," and "GitHub Copilot in VS Code 1.139
  release"). Fetched via `curl` with a browser user-agent (following a
  301 redirect) rather than relying solely on WebFetch AI summarization,
  per the precedent set in `docs-github-copilot-weekly-releases-aug31-2026.md`
  Extraction Note 1 and `docs-github-copilot-weekly-releases-sept7-2026.md`
  Extraction Note 2, both of which found WebFetch prone to inventing
  headings not present in the source. (A WebFetch pass was run first for
  triage purposes and its section labels and bullet text matched the raw
  HTML closely in this case, but the curl transcript is the one quoted
  below.) One linked page was followed in full: "New features and
  improvements in Copilot for JetBrains"
  (`github.blog/changelog/2026-09-22-new-features-and-improvements-in-copilot-for-jetbrains/`,
  published September 22, 2026, "2 minute read"). Three other linked pages
  were deliberately not followed: the Copilot app download link
  (`github.com/features/ai/github-app`, not substantive — a download CTA),
  the generic Slack/Teams integration how-to docs
  (`docs.github.com/copilot/how-tos/copilot-integrations/integrate-cloud-agent-with-slack`
  and `.../integrate-cloud-agent-with-teams`, evergreen reference docs not
  tied to this week's specific changes), and the VS Code 1.139 general
  release notes (`code.visualstudio.com/updates/v1_139`), consistent with
  this family's established treatment of non-Copilot-specific VS Code
  release notes as out of scope (e.g.
  `docs-github-copilot-weekly-releases-aug31-2026.md` Extraction Note 2).
- **Author credibility**: GitHub engineering team (changelog, both the
  weekly digest and the linked JetBrains post are unsigned/team-authored
  changelog entries, not individually bylined). Authoritative for: the
  existence of each named feature, its availability tier/status (public
  preview, GA, or unstated), and plan-tier gating for the four newly
  listed models. Not authoritative for: independent verification of any
  claim, real-world production behavior of preview features, or any
  detail beyond what each changelog entry states (e.g., the digest states
  no specific model pricing for the new Copilot model additions).
- **Scope**: A weekly digest covering the period since the prior weekly
  release (week of September 21, 2026), plus the fully-followed JetBrains
  1.18.0 dedicated changelog. Local sandboxing and OpenTelemetry in the
  Copilot app, and Claude Opus 5.5's availability, are each restated here
  with no new detail beyond what dedicated source notes already cover
  (see Cross-References). Does NOT cover: Visual Studio, Eclipse, Xcode,
  GitHub Mobile, pricing for GPT-6 Sol/Luna or Grok 4.7 in Copilot,
  configuration mechanics for any Slack/Teams feature, or JetBrains
  version-number specifics beyond "1.18.0" and the "2025.1 → 2026.1"
  deprecation notice.

## Extracted Claims

### Claim 1: Four new models became available in GitHub Copilot this week — Claude Opus 5.5 (Pro+/Max/Business/Enterprise), GPT-6 Sol (Pro+/Max/Business/Enterprise), GPT-6 Luna (Pro/Pro+/Max/Business/Enterprise), and Grok 4.7 (Pro/Pro+/Max/Business/Enterprise)

- **Evidence**: Changelog "GitHub Copilot" section, four bullets, one per
  model.
- **Confidence**: settled (direct first-party plan-tier availability
  statement; no pricing or capability claims made)
- **Quote**: "Claude Opus 5.5 is available to Copilot Pro+, Max, Business, and Enterprise plans." / "GPT-6 Sol is available to Copilot Pro+, Max, Business, and Enterprise plans." / "GPT-6 Luna is available to Copilot Pro, Pro+, Max, Business, and Enterprise plans." / "Grok 4.7 is available to Copilot Pro, Pro+, Max, Business, and Enterprise plans."
- **Our assessment**: Claude Opus 5.5's availability is a restatement of
  `docs-github-copilot-opus55-availability.md` (already fully mined,
  issue #3627) with no new detail — same plan-tier gating (Pro+/Max/
  Business/Enterprise, not Pro/Free/Student, per that note's Claim 6).
  GPT-6 Sol and GPT-6 Luna are new to the corpus's Copilot-availability
  tracking: they carry over the Sol/Terra/Luna tier-naming convention
  documented for the GPT-5.6 series in `blog-simonwillison-gpt56-sol-launch.md`
  (Claim 1) and `blog-simonwillison-gpt56-luna-price-drop.md`, but this
  changelog states no pricing and does not mention a "Terra" tier for
  GPT-6 in Copilot. Grok 4.7 is a newer point release than the Grok 4.5
  covered in `blog-cursor-grok-4-5.md` (a different vendor integration —
  Cursor, not GitHub Copilot); no corpus note yet covers Grok 4.7
  specifically on any platform. GPT-6 Luna and Grok 4.7 are notably gated
  to the same four-tier list (Pro and up), while Opus 5.5 and GPT-6 Sol
  are withheld from the base Pro tier — consistent with the corpus's
  general pattern of gating flagship/frontier models above entry-level
  Copilot plans. For Ch04 (Model Selection): add GPT-6 Sol/Luna and Grok
  4.7 to the Copilot model-availability tracking table; flag pricing and
  capability detail as unconfirmed pending dedicated changelogs (the
  pattern this family produces for major individual model launches, e.g.
  the dedicated Opus 5.5 post).

### Claim 2: Local sandboxing in the Copilot app and OpenTelemetry export from the Copilot app both reached this week's digest with no new detail beyond their own dedicated changelogs

- **Evidence**: Changelog "GitHub Copilot app" section, first two bullets.
- **Confidence**: settled for existence/status (both already confirmed
  public preview in dedicated notes); this claim is about restatement,
  not new information
- **Quote**: "Limit agents’ access to files, networks, and credentials with local sandboxing, now in public preview." / "Track agent activity in your existing monitoring tools with OpenTelemetry, configured through enterprise-managed settings."
- **Our assessment**: This is a verbatim-equivalent restatement of
  `docs-github-copilot-app-local-sandboxing.md` (issue #3689, public
  preview, OS-level restriction of filesystem/network/credential access,
  off by default, fail-closed) and `docs-github-copilot-app-opentelemetry.md`
  (issue #3656, `telemetry` property in enterprise `managed-settings.json`
  — a note that already documents a same-day contradiction between the
  changelog's claim and the live managed-settings reference doc's support
  table, see Cross-References). No new detail follows from either bullet
  here; both dedicated notes remain the authoritative extraction.

### Claim 3: GitHub Copilot in Slack and Microsoft Teams now supports switching models mid-conversation (persisted for the rest of the thread, with Slack channel defaults), duplicate-issue prevention, clearer implementation-plan status with better recovery from interrupted or stale replies, and sharing supported files/attachments/message links as context

- **Evidence**: Changelog "GitHub Copilot in Slack and Microsoft Teams"
  section, four bullets.
- **Confidence**: emerging (no explicit GA/preview tag stated for any of
  the four items — unusual for this digest family, where most items state
  a tier explicitly)
- **Quote**: "Choose the best model for each task. Switch models mid-conversation, and Copilot keeps your choice for the rest of the thread. In Slack, you can also set channel defaults." / "Avoid duplicate issues since Copilot now checks for similar existing issues before creating a new one." / "Follow longer-running tasks more easily with clearer implementation-plan status, better recovery from interrupted or stale replies, and more predictable reconnection when a conversation goes idle." / "Give Copilot more context in Slack by sharing supported files, attachments, and message links."
- **Our assessment**: `docs-github-copilot-slack-shared-agentic-work.md`
  and `docs-github-copilot-teams-shared-agentic-work.md` (both from the
  August 21, 2026 "new experience" launch changelogs) establish the
  baseline shared-agentic-work surface for Slack and Teams; this week's
  bullets are incremental refinements on top of that baseline —
  per-conversation model switching, duplicate-issue detection, and
  reconnection/recovery robustness — rather than a new surface. None of
  these four items states an availability tier, which is atypical for
  this digest family and worth flagging rather than assuming GA. For Ch01
  (Daily Workflows) and Ch05 (Team Adoption): note per-thread model
  switching and duplicate-issue prevention as maturing the Slack/Teams
  agent surface toward parity with IDE/CLI conversation controls; flag
  availability tier as unconfirmed.

### Claim 4: AI-assisted tool approvals ("assisted approvals") reached public preview for Copilot agent sessions in JetBrains, automatically approving low-risk tool calls while continuing to prompt for higher-risk actions

- **Evidence**: Weekly digest "GitHub Copilot in JetBrains" section (one
  sentence); elaborated in the dedicated JetBrains changelog's "AI-assisted
  tool approvals" subsection with a stated rationale.
- **Confidence**: emerging (explicitly public preview)
- **Quote**: "AI-assisted tool approvals, called assisted approvals, are now in public preview for Copilot agent sessions, automatically approve low-risk tool calls while prompting you for higher-risk actions." / "This gives you fewer approval interruptions for low-risk actions while keeping higher-risk decisions in your hands."
- **Our assessment**: This is the first corpus documentation of an
  automated (model-assisted, not purely rule-based) tool-approval
  triage system in Copilot for JetBrains. It sits in contrast to
  `docs-github-copilot-enterprise-bypass-permissions.md` (Claim 1), which
  documents an enterprise *administrator*-level control
  (`disableBypassPermissionsMode`) that prevents CLI/VS Code from
  *automatically skipping* permission prompts entirely — a coarse on/off
  switch. Assisted approvals is a different mechanism: a per-call,
  risk-graded auto-approval aimed at the individual practitioner's
  friction, not an administrator's blanket policy, and JetBrains-specific
  rather than CLI/VS Code. The dedicated post does not disclose how "risk"
  is assessed (which tool categories or actions count as low- vs.
  higher-risk), which is the open question that would determine how much
  practitioners should trust the automatic approvals. For Ch02 (Harness
  Engineering — Permission Models): document assisted approvals as a new
  risk-graded approval pattern, distinct from the enterprise-level bypass
  toggle already in the corpus; flag the undisclosed risk-classification
  criteria as an open question for teams evaluating whether to enable it.

### Claim 5: Editing an earlier message in a JetBrains Copilot agent session now rewinds both the conversation and file changes before sending the replacement request

- **Evidence**: Weekly digest "GitHub Copilot in JetBrains" section (one
  sentence); elaborated in the dedicated JetBrains post's "Re-edit earlier
  messages" subsection.
- **Confidence**: settled (direct first-party feature description, no
  preview/experimental tag — appears to be GA as part of the 1.18.0
  release, though the digest and dedicated post do not use the word "GA"
  explicitly for this item)
- **Quote**: "Edit an earlier message to redirect an agent session and Copilot rewinds both the conversation and file changes before sending the replacement request." / "This lets you revise an earlier request and continue from that point, rather than adding another message to correct the direction of the conversation."
- **Our assessment**: This is a materially different redirect mechanism
  from the Cascade/Critique escalation patterns documented in
  `docs-github-copilot-weekly-releases-sept7-2026.md` Claim 3 (Project
  HydraFusion) — this is a practitioner-initiated rewind of both chat
  history *and* already-applied file edits back to a chosen point, not an
  automated model-routing decision. It is the first corpus documentation
  of a coding-agent surface that rewinds file-system state (not just
  conversational context) when a user edits an earlier message. For Ch01
  (Daily Workflows): document as a new recovery pattern — "rewind and
  redirect" — distinct from simply sending a follow-up correction message,
  since it undoes file changes made after the edited message rather than
  layering a correction on top of them.

### Claim 6: Local and Copilot agent sessions in JetBrains now support organization and enterprise skills, along with organization-managed custom instructions

- **Evidence**: Weekly digest "GitHub Copilot in JetBrains" section (one
  sentence); dedicated JetBrains post's "Shared skills and instructions"
  subsection (near-identical wording).
- **Confidence**: settled (no preview/experimental tag stated)
- **Quote**: "Local and Copilot agent sessions now support organization and enterprise skills, along with organization-managed custom instructions. You can use shared skills and organizational guidance in both types of sessions."
- **Our assessment**: This extends organization-level skill/instruction
  sharing — already documented for other surfaces in
  `blog-addyosmani-audit-agent-files.md` and the general skills-file
  corpus — to JetBrains specifically, and explicitly to *both* "local"
  sessions (presumably inline/non-agentic chat) and "Copilot agent"
  sessions. Neither the digest nor the dedicated post defines the
  distinction between "local" and "Copilot agent" sessions beyond this
  phrase; this ambiguity is left unresolved rather than inferred. For Ch05
  (Team Adoption — Governance): note JetBrains as now supporting the same
  org/enterprise skill-sharing model as other IDE surfaces, closing a
  platform gap.

### Claim 7: The Codex agent in JetBrains now supports a plan mode — reviewing, refining, or approving a plan before implementation begins

- **Evidence**: Dedicated JetBrains post only, "Plan with the Codex agent"
  subsection; not mentioned in the weekly digest's own compressed
  three-bullet summary of the JetBrains release.
- **Confidence**: settled (no preview/experimental tag stated for this
  item specifically)
- **Quote**: "The Codex agent now supports plan mode. You can review, refine, or approve a plan before implementation, giving you an opportunity to shape the approach before the agent starts making changes."
- **Our assessment**: This is exactly the kind of item MINER.md §1 flags
  as a reason to follow a linked page — it does not appear in the digest
  text at all. `docs-github-copilot-gpt53codex-base-model.md` documents
  GPT-5.3-Codex as GitHub's LTS default base model; this claim is the
  first corpus documentation of a Codex-specific *agent* (as a distinct,
  named agent entity in the JetBrains agent picker, alongside "Copilot
  harness" per `docs-github-copilot-jetbrains-harness-ga-aug2026.md` Claim
  1) gaining a plan-before-implementation review step. This is the same
  "review before execution" shape the guide already recommends generally,
  now confirmed for the Codex agent specifically in JetBrains. For Ch02
  (Harness Engineering): add Codex-agent plan mode to the corpus's
  running list of plan-before-execute implementations across agent
  surfaces (alongside e.g. reasoning-level controls in
  `docs-github-copilot-cca-reasoning-level.md`).

### Claim 8: JetBrains Copilot agent sessions gained a setting to disable the built-in GitHub MCP Server independently of manually configured MCP servers (enabled by default), plus persistent per-tool controls for MCP servers

- **Evidence**: Dedicated JetBrains post only, "More control over MCP
  tools" subsection; not itemized in the weekly digest text.
- **Confidence**: settled (no preview/experimental tag stated)
- **Quote**: "A new setting lets you turn the built-in GitHub MCP Server on or off without changing manually configured MCP servers. The built-in server remains enabled by default." / "Copilot agent sessions also gain persistent per-tool controls for MCP servers. You can manage individual tools as well as control whether the built-in server is enabled."
- **Our assessment**: This extends, at the individual-practitioner/IDE
  level, the same class of control that
  `docs-github-copilot-mcp-allowlists-enterprise.md` (Claim 1) documents
  at the enterprise-administrator level via `allowedMcpServers`/
  `deniedMcpServers` managed-settings keys. The two are complementary, not
  overlapping: the enterprise note gates *which* MCP servers are allowed
  to run at all, org-wide; this JetBrains setting lets an individual
  developer toggle the built-in GitHub MCP server specifically, and
  persist per-tool enable/disable choices, within whatever the enterprise
  policy already permits. Neither source states whether the JetBrains
  per-tool toggle is overridden by an enterprise deny-list if one exists.
  For Ch02 (Harness Engineering — Tool Permissions): document the
  JetBrains per-tool/built-in-server toggle as the individual-level
  counterpart to the enterprise allowlist/denylist mechanism, and flag the
  interaction between the two (which one wins) as unconfirmed.

### Claim 9: The JetBrains 1.18.0 release also ships quality fixes (inline chat reliability, Codex session startup, multi-window behavior, IntelliJ 2026.3 EAP restorations), hides inline chat entry points in JetBrains Gateway and remote development environments, and gives advance deprecation notice to JetBrains IDE 2025.1 users to upgrade to 2026.1 or later (support unchanged this release)

- **Evidence**: Dedicated JetBrains post, "Quality improvements,"
  "Changed," and "Deprecation" sections; not mentioned in the weekly
  digest text at all.
- **Confidence**: settled (direct first-party changelog statement of
  scope and deprecation timeline; "support remains unchanged in this
  release" is an explicit non-immediate-action signal)
- **Quote**: "This update improves inline chat reliability, including preserving your edits when requests end and respecting selected thinking effort and context window settings." / "Inline chat and its entry points are now hidden in JetBrains Gateway and remote development environments." / "If you use a JetBrains IDE version 2025.1, you will see advance notice to upgrade to 2026.1 or later. Support remains unchanged in this release."
- **Our assessment**: The Gateway/remote-development inline-chat hiding
  is a scope narrowing (removing an entry point rather than adding a
  capability) that the weekly digest omits entirely — a reminder that
  this digest family's own three-bullet compressions of a linked release
  can drop non-feature changes (fixes, removals, deprecation notices)
  that a practitioner upgrading JetBrains would still need to know. No
  prior corpus note tracks JetBrains IDE version-support deprecation
  windows. For Ch05 (Team Adoption — Maintenance): flag the 2025.1
  deprecation notice for any team still on that JetBrains IDE version,
  noting support is "unchanged in this release" (i.e., not yet an
  enforced cutoff).

### Claim 10: VS Code 1.139 adds gradually-rolling-out support for running agents in Dev Containers over SSH, Tunnel, and WSL hosts, using the remote project's own tools and dependencies

- **Evidence**: Changelog "GitHub Copilot in VS Code 1.139 release"
  section, first bullet.
- **Confidence**: emerging ("Support is rolling out gradually" — an
  explicit partial/staged-rollout statement, distinct from a clean public
  preview or GA tag)
- **Quote**: "Run agents in Dev Containers on SSH, Tunnel, and WSL hosts, using your remote project’s tools and dependencies. Support is rolling out gradually."
- **Our assessment**: This is the first corpus documentation of Dev
  Containers support for Copilot agent sessions in VS Code across these
  three remote-host types specifically. No existing source note in this
  corpus covers Dev Containers agent support, so this is genuinely novel
  rather than an extension. The "rolling out gradually" phrasing is
  notably softer than this family's usual "public preview" / "GA" /
  "experimental" tags, and should not be read as equivalent to a
  publicly-toggleable preview flag — practitioners may see it appear
  without any opt-in action on their part, or not see it yet at all. For
  Ch02 (Harness Engineering — Remote/Containerized Development): add Dev
  Containers agent support (SSH/Tunnel/WSL) as a new remote-development
  capability; flag the staged-rollout status as meaning availability may
  vary by account/timing rather than being a simple opt-in toggle.

### Claim 11: VS Code 1.139 adds a Compact View for session lists (with filters to hide empty groups and inline session/chat renaming) and a preview layout option to choose between separate chat tabs or a single active-chat view within a session

- **Evidence**: Changelog "GitHub Copilot in VS Code 1.139 release"
  section, second and third bullets.
- **Confidence**: emerging (the chat-tabs-vs-single-view layout option is
  explicitly tagged "now in preview"; Compact View itself carries no
  explicit tag)
- **Quote**: "Keep busy session lists organized with Compact View, filters to hide empty groups, and the ability to rename sessions and chats directly in the list." / "Choose between separate chat tabs or a single active-chat view within a session, without losing your conversations. This layout option is now in preview."
- **Our assessment**: Both items are session-list/UI ergonomics
  improvements for practitioners running many concurrent or historical
  Copilot sessions in VS Code — relevant to, but distinct from, the
  session-search capability in `docs-github-copilot-chat-agent-sessions.md`
  (which covers *finding* past sessions, not organizing or viewing the
  active session list). No prior corpus note documents VS Code's
  session-list UI density/organization controls specifically. For Ch01
  (Daily Workflows): note Compact View and the chat-tabs-vs-single-view
  toggle as incremental multi-session ergonomics improvements, relevant to
  practitioners running many parallel Copilot sessions per the guide's
  general multi-session workflow guidance.

## Concrete Artifacts

### Full weekly digest — September 21, 2026 (published September 25, 2026), verbatim transcript

Extracted from raw HTML via `curl` with a browser user-agent (following a
301 redirect), not WebFetch summarization alone, per MINER.md §2a and this
family's established precedent.

```
GitHub Copilot weekly releases — September 21
Source: github.blog/changelog, published 2026-09-25, retrieved 2026-09-26
Release, 2 minute read

INTRO
  This week's releases add new models to Copilot, local sandboxing in the
  Copilot app, and updates to Copilot in Slack, Microsoft Teams,
  JetBrains, and VS Code.

GITHUB COPILOT
  [Claim 1]
  - Claude Opus 5.5 is available to Copilot Pro+, Max, Business, and
    Enterprise plans.
  - GPT-6 Sol is available to Copilot Pro+, Max, Business, and Enterprise
    plans.
  - GPT-6 Luna is available to Copilot Pro, Pro+, Max, Business, and
    Enterprise plans.
  - Grok 4.7 is available to Copilot Pro, Pro+, Max, Business, and
    Enterprise plans.

GITHUB COPILOT APP
  [Claim 2]
  - Limit agents' access to files, networks, and credentials with local
    sandboxing, now in public preview.
  - Track agent activity in your existing monitoring tools with
    OpenTelemetry, configured through enterprise-managed settings.
  (Link: "Download the Copilot app" — github.com/features/ai/github-app,
   not fetched, non-substantive download CTA)

GITHUB COPILOT IN SLACK AND MICROSOFT TEAMS
  [Claim 3]
  - Choose the best model for each task. Switch models mid-conversation,
    and Copilot keeps your choice for the rest of the thread. In Slack,
    you can also set channel defaults.
  - Avoid duplicate issues since Copilot now checks for similar existing
    issues before creating a new one.
  - Follow longer-running tasks more easily with clearer
    implementation-plan status, better recovery from interrupted or stale
    replies, and more predictable reconnection when a conversation goes
    idle.
  - Give Copilot more context in Slack by sharing supported files,
    attachments, and message links.
  (Links: "Slack" and "Teams" how-to docs — docs.github.com/copilot/
   how-tos/copilot-integrations/integrate-cloud-agent-with-slack and
   .../integrate-cloud-agent-with-teams, not fetched, evergreen reference
   docs not specific to this week's changes)

GITHUB COPILOT IN JETBRAINS
  [Claims 4-6, elaborated via linked dedicated post as Claims 4-9]
  - Assisted approvals, now in public preview for Copilot agent sessions,
    automatically approve low-risk tool calls while prompting you for
    higher-risk actions.
  - Edit an earlier message to redirect an agent session and Copilot
    rewinds both the conversation and file changes before sending the
    replacement request.
  - Shared organization and enterprise skills, along with
    organization-managed custom instructions, now work in local and
    Copilot agent sessions.
  (Link: "full Copilot in JetBrains changelog" —
   github.blog/changelog/2026-09-22-new-features-and-improvements-in-
   copilot-for-jetbrains/ — followed in full, see separate transcript
   below)

GITHUB COPILOT IN VS CODE 1.139 RELEASE
  [Claims 10-11]
  - Run agents in Dev Containers on SSH, Tunnel, and WSL hosts, using
    your remote project's tools and dependencies. Support is rolling out
    gradually.
  - Keep busy session lists organized with Compact View, filters to hide
    empty groups, and the ability to rename sessions and chats directly
    in the list.
  - Choose between separate chat tabs or a single active-chat view within
    a session, without losing your conversations. This layout option is
    now in preview.
  (Link: "full release notes" — code.visualstudio.com/updates/v1_139, not
   fetched, general non-Copilot-specific VS Code release notes)
```

### "New features and improvements in Copilot for JetBrains" (September 22, 2026) — verbatim transcript

Extracted from raw HTML via `curl` with a browser user-agent, same method
as above.

```
New features and improvements in Copilot for JetBrains
Source: github.blog/changelog, published 2026-09-22, retrieved 2026-09-26
Release, 2 minute read

INTRO
  GitHub Copilot for JetBrains 1.18.0 brings AI-assisted tool approvals,
  more control over agent conversations, and shared skills and
  instructions for your organization. You can also review plans with the
  Codex agent and manage MCP tools with persistent controls.

WHAT'S NEW

  AI-assisted tool approvals [Claim 4]
    AI-assisted tool approvals, called assisted approvals, are now in
    public preview for Copilot agent sessions. Low-risk tool calls
    receive automatic approval, while higher-risk actions continue to
    prompt you for a decision.
    This gives you fewer approval interruptions for low-risk actions
    while keeping higher-risk decisions in your hands.

  Re-edit earlier messages [Claim 5]
    You can now re-edit a previous user message in a Copilot agent
    session. Before sending your replacement message, Copilot rewinds
    both the conversation and file changes.
    This lets you revise an earlier request and continue from that
    point, rather than adding another message to correct the direction
    of the conversation.

  Shared skills and instructions [Claim 6]
    Local and Copilot agent sessions now support organization and
    enterprise skills, along with organization-managed custom
    instructions. You can use shared skills and organizational guidance
    in both types of sessions.

  Plan with the Codex agent [Claim 7]
    The Codex agent now supports plan mode. You can review, refine, or
    approve a plan before implementation, giving you an opportunity to
    shape the approach before the agent starts making changes.

  More control over MCP tools [Claim 8]
    A new setting lets you turn the built-in GitHub MCP Server on or off
    without changing manually configured MCP servers. The built-in
    server remains enabled by default.
    Copilot agent sessions also gain persistent per-tool controls for
    MCP servers. You can manage individual tools as well as control
    whether the built-in server is enabled.

USER EXPERIENCE ENHANCEMENTS

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

QUALITY IMPROVEMENTS [Claim 9]
  This update improves inline chat reliability, including preserving
  your edits when requests end and respecting selected thinking effort
  and context window settings. It also addresses Codex session startup
  issues, improves behavior across multiple project windows, and
  restores embedded editors and message re-editing on IntelliJ 2026.3
  EAP builds.

CHANGED [Claim 9]
  Inline chat and its entry points are now hidden in JetBrains Gateway
  and remote development environments.

DEPRECATION [Claim 9]
  If you use a JetBrains IDE version 2025.1, you will see advance notice
  to upgrade to 2026.1 or later. Support remains unchanged in this
  release.
```

*Sources: raw HTML of
https://github.blog/changelog/2026-09-25-github-copilot-weekly-releases-september-21
and
https://github.blog/changelog/2026-09-22-new-features-and-improvements-in-copilot-for-jetbrains/,
both fetched directly via `curl` with a browser user-agent on 2026-09-26,
block-level tags converted to line breaks, remaining markup stripped. All
`Quote` fields above were checked by exact substring match against these
transcripts. The source HTML for both pages uses typographic curly
apostrophes (e.g. "week’s," "agents’ access," "project’s tools"); per the
apostrophe-normalization precedent in
`docs-github-copilot-weekly-releases-sept7-2026.md` Extraction Note 7,
quotes in this note are normalized to straight ASCII apostrophes — a
typographic substitution only, no wording or punctuation altered.*

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-opus55-availability.md`,
`docs-github-copilot-app-local-sandboxing.md`,
`docs-github-copilot-app-opentelemetry.md`,
`docs-github-copilot-slack-shared-agentic-work.md`,
`docs-github-copilot-teams-shared-agentic-work.md`,
`docs-github-copilot-enterprise-bypass-permissions.md`,
`docs-github-copilot-mcp-allowlists-enterprise.md`,
`docs-github-copilot-jetbrains-harness-ga-aug2026.md`,
`docs-github-copilot-gpt53codex-base-model.md`,
`docs-github-copilot-cca-reasoning-level.md`,
`docs-github-copilot-chat-agent-sessions.md`,
`blog-simonwillison-gpt56-sol-launch.md`,
`blog-simonwillison-gpt56-luna-price-drop.md`, and
`blog-cursor-grok-4-5.md` were re-read directly in those notes (via
`### Claim N:` headings, counted top-to-bottom in document order) before
citing, per MINER.md §4b.

- **Corroborates** `docs-github-copilot-opus55-availability.md` (Claim 6,
  Opus 5.5 gated to Pro+/Max/Business/Enterprise): Claim 1 of this note
  restates the identical plan-tier gating with no new detail.

- **Corroborates** `docs-github-copilot-app-local-sandboxing.md` (full
  note) and `docs-github-copilot-app-opentelemetry.md` (full note): Claim
  2 of this note restates both public-preview announcements verbatim,
  three days later, adding nothing new.

- **Extends** `docs-github-copilot-slack-shared-agentic-work.md` and
  `docs-github-copilot-teams-shared-agentic-work.md` (both document the
  August 21, 2026 baseline shared-agentic-work launch for their
  respective surfaces): Claim 3 of this note documents incremental
  refinements (model switching, duplicate-issue prevention, reconnection
  robustness, richer context sharing) on top of that baseline, without
  stating availability tiers for the new refinements.

- **Extends and contrasts with** `docs-github-copilot-enterprise-bypass-permissions.md`
  (Claim 1, enterprise `disableBypassPermissionsMode` control over CLI/VS
  Code auto-skipped permission prompts): Claim 4 of this note (JetBrains
  "assisted approvals," a per-call risk-graded auto-approval) is a
  different mechanism at a different level — individual-session,
  risk-classified, JetBrains-only — not a contradiction, but a related
  permission-model concept worth juxtaposing for Ch02.

- **Extends** `docs-github-copilot-mcp-allowlists-enterprise.md` (Claim 1,
  enterprise-level `allowedMcpServers`/`deniedMcpServers` managed-settings
  keys): Claim 8 of this note documents an individual/IDE-level
  counterpart — a JetBrains setting to toggle the built-in GitHub MCP
  Server and persistent per-tool controls — operating at a different
  layer than the enterprise allowlist/denylist. The interaction between
  the two (which wins in a conflict) is not stated by either source and
  is flagged as an open question in Claim 8's assessment.

- **Extends** `docs-github-copilot-jetbrains-harness-ga-aug2026.md` (Claim
  1, "Copilot harness" as a named, agent-picker-selectable entity; Claim
  2, built-in JetBrains MCP server support in public preview): Claim 7 of
  this note documents "Codex agent" as another named, distinct entity in
  the same JetBrains agent picker gaining a plan-mode capability, and
  Claim 8 extends that prior note's Claim 2 (built-in MCP server support)
  with the new on/off toggle and per-tool persistent controls.

- **Extends** `docs-github-copilot-gpt53codex-base-model.md` (Claim 1,
  GPT-5.3-Codex as GitHub's LTS default base model): Claim 7 of this note
  is the first corpus documentation of a *Codex agent* (distinct from the
  Codex base model) gaining an agent-level capability (plan mode) in
  JetBrains specifically.

- **Extends** `docs-github-copilot-cca-reasoning-level.md` (reasoning-level
  controls as a plan-before-execute-adjacent lever for cloud agent tasks):
  Claim 7 of this note adds Codex-agent plan mode to the corpus's running
  list of "review/shape before the agent acts" implementations across
  different agent surfaces.

- **Distinct from** `docs-github-copilot-chat-agent-sessions.md` (searching
  past chat sessions): Claim 11 of this note (VS Code session-list
  Compact View and chat-tabs-vs-single-view layout) is about organizing
  and viewing the *current* session list, not searching or retrieving
  past sessions — a different capability on a related surface.

- **Corroborates (naming convention only)** `blog-simonwillison-gpt56-sol-launch.md`
  (Claim 1, GPT-5.6 series introduced as a three-tier Sol/Terra/Luna
  naming scheme) and `blog-simonwillison-gpt56-luna-price-drop.md`: Claim
  1 of this note shows GitHub Copilot adopting "Sol" and "Luna" tier names
  again for the GPT-6 series, without a "Terra" tier mentioned in this
  changelog and without any pricing disclosed for the Copilot integration.

- **Distinct from** `blog-cursor-grok-4-5.md` (Grok 4.5 in Cursor, a
  different vendor/product integration): Claim 1 of this note documents
  Grok 4.7 in GitHub Copilot specifically — a newer point release on a
  different platform; no corpus note yet covers Grok 4.7 on any platform.

- **Contradicts**: None identified. No claim in this note materially
  opposes an existing source note's claim on the same fact; all
  cross-references above are corroboration, extension, or juxtaposition
  of related-but-distinct mechanisms (e.g., enterprise vs. individual
  permission/MCP controls), which MINER.md §4a treats as a conditioning
  variable rather than a contradiction.

- **Novel**:
  - First corpus documentation of GPT-6 Sol, GPT-6 Luna, and Grok 4.7
    availability in GitHub Copilot (Claim 1).
  - First corpus documentation of JetBrains "assisted approvals" — a
    risk-graded automatic tool-approval mechanism (Claim 4).
  - First corpus documentation of a coding-agent surface rewinding both
    conversation *and* file-system state when an earlier message is
    edited (Claim 5).
  - First corpus documentation of the Codex agent (as a distinct named
    agent, not just the Codex base model) supporting plan mode (Claim 7).
  - First corpus documentation of an individual/IDE-level toggle for a
    built-in MCP server plus persistent per-tool MCP controls (Claim 8).
  - First corpus documentation of JetBrains IDE version-support
    deprecation windows for the Copilot plugin (Claim 9).
  - First corpus documentation of Dev Containers agent support in VS
    Code across SSH, Tunnel, and WSL remote hosts (Claim 10).
  - First corpus documentation of VS Code session-list density/
    organization controls (Compact View, chat-tabs-vs-single-view layout)
    (Claim 11).

## Guide Impact

### Chapter 02: Harness Engineering — Permission Models & Tool Control

- **Risk-graded auto-approval as a new permission-model pattern**: Add
  JetBrains "assisted approvals" (Claim 4) alongside the existing
  enterprise-level bypass-permissions control
  (`docs-github-copilot-enterprise-bypass-permissions.md`) as a second,
  complementary layer in the corpus's permission-model coverage —
  individual-session risk grading vs. administrator-level blanket
  toggles. Flag the undisclosed risk-classification criteria as an open
  question.
- **Two-layer MCP server control**: Document the JetBrains built-in-server
  toggle and per-tool persistent controls (Claim 8) as the
  individual/IDE-level counterpart to the enterprise `allowedMcpServers`/
  `deniedMcpServers` mechanism (`docs-github-copilot-mcp-allowlists-enterprise.md`).
  Flag the conflict-resolution question (which layer wins) as unconfirmed.
- **Plan-before-execute checklist addition**: Add Codex-agent plan mode
  in JetBrains (Claim 7) to the running list of "review before the agent
  acts" implementations across surfaces.
- **New remote-development capability**: Add VS Code Dev Containers agent
  support over SSH/Tunnel/WSL (Claim 10) as a new entry under
  remote/containerized development guidance; flag the staged-rollout
  status (not a simple opt-in toggle).

### Chapter 01: Daily Workflows

- **Rewind-and-redirect recovery pattern**: Document JetBrains's
  edit-earlier-message-to-rewind-conversation-and-files behavior (Claim
  5) as a new recovery pattern distinct from sending a follow-up
  correction message.
- **Multi-session ergonomics**: Note VS Code's Compact View and
  chat-tabs-vs-single-view layout option (Claim 11) as incremental
  improvements relevant to practitioners running many parallel Copilot
  sessions.
- **Slack/Teams conversation maturity**: Note per-thread model switching
  and duplicate-issue prevention (Claim 3) as maturing the Slack/Teams
  agent surface.

### Chapter 04: Model Selection

- **Model-availability tracking update**: Add GPT-6 Sol, GPT-6 Luna, and
  Grok 4.7 (Claim 1) to the Copilot model-availability tracking table,
  alongside the already-documented Claude Opus 5.5; flag pricing and
  capability detail as unconfirmed pending dedicated changelogs.

### Chapter 05: Team Adoption — Governance & Maintenance

- **JetBrains shared-skills parity**: Note JetBrains now supports
  organization/enterprise skills and custom instructions in both local
  and agent sessions (Claim 6), closing a platform gap with other IDE
  surfaces.
- **JetBrains IDE version deprecation window**: Flag the 2025.1 → 2026.1
  advance-notice deprecation (Claim 9) for any team running an older
  JetBrains IDE version with the Copilot plugin.

## Extraction Notes

1. **JetBrains dedicated changelog followed per MINER.md §1**: The weekly
   digest compresses the JetBrains 1.18.0 release into three sentences;
   the linked dedicated changelog (~600 words) was fetched and mined in
   full, since two of its most substantive items — Codex-agent plan mode
   (Claim 7) and MCP built-in-server/per-tool controls (Claim 8) — do not
   appear in the digest text at all. This follows the precedent set by
   `docs-github-copilot-weekly-releases-sept7-2026.md`, which followed the
   HydraFusion announcement post for the same reason (digest text thinner
   than the linked source).
2. **Raw HTML fetched via `curl`, not WebFetch summarization alone**: Both
   pages were fetched with a browser user-agent (following a 301 redirect
   on the first request) and parsed by isolating the `<article>` element,
   converting block-level tags to line breaks, and stripping remaining
   markup. A WebFetch pass was also run on the weekly digest for triage
   and its section labels and bullet text matched the curl transcript
   closely in this instance (unlike some prior weeks in this family), but
   the curl transcript is the one quoted throughout this note, per
   established precedent and to guarantee exact substring matches for all
   `Quote` fields.
3. **Three linked pages deliberately not followed**: the Copilot app
   download CTA (non-substantive), the generic Slack/Teams
   integration how-to docs (evergreen reference material, not specific to
   this week's changes), and the VS Code 1.139 general release notes
   (non-Copilot-specific), consistent with this family's established
   scope boundaries.
4. **No new contradictions filed**: Extraction surfaced several
   related-but-distinct mechanisms (enterprise vs. individual permission
   and MCP controls) that were weighed against MINER.md §4a's filing bar
   and judged to be complementary layers rather than opposing claims about
   the same fact — see Cross-References for detail on each.
5. **Cross-reference verification performed**: All `Claim N` citations
   above were checked against each cited note's actual claim numbering by
   re-reading the note in full before citing, per MINER.md §4b.
6. **Apostrophe normalization**: Both source pages use typographic curly
   apostrophes; consistent with this family's established precedent, all
   quotes in this note are normalized to straight ASCII apostrophes — a
   typographic substitution only, no wording, word order, or punctuation
   altered.
