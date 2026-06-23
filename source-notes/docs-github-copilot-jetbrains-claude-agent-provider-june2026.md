---
source_url: https://github.blog/changelog/2026-06-22-new-features-and-claude-as-agent-provider-preview-in-jetbrains-ides
source_type: docs
title: "New features and Claude as agent provider preview in JetBrains IDEs"
author: GitHub (official changelog)
date_published: 2026-06-22
date_extracted: 2026-06-23
last_checked: 2026-06-23
status: current
confidence_overall: emerging
issue: "#1280"
---

# New features and Claude as agent provider preview in JetBrains IDEs

> GitHub's June 22, 2026 JetBrains changelog introduces Claude (via Claude Code CLI)
> as a selectable agent provider in public preview alongside Copilot, enables
> organization/enterprise agents in JetBrains IDEs, adds in-flight CLI message queuing
> with three steering options, enhances the Agent Debug Panel with a logs summary view,
> improves the model picker with a `/models` command and recently-used section, adds
> per-turn AI credit tracking, and promotes cloud agent to general availability — together
> establishing JetBrains as a multi-provider agent platform where practitioners actively
> select which AI agent backend handles each task.

## Source Context

- **Type**: docs (GitHub official product changelog, June 22, 2026; approximately 500 words
  covering eight distinct feature areas plus availability updates)
- **Author credibility**: GitHub engineering team announcing production feature releases for
  the JetBrains Copilot plugin. Authoritative for: the existence and described behavior of
  each feature, exact settings paths and slash command syntax, GA/preview status of each
  capability, and configuration requirements (e.g., Claude Code CLI path setup).
  Not authoritative for: how Claude performs compared to Copilot's native agent on real tasks
  in JetBrains, whether bypass permissions mode for Claude can be overridden by the enterprise
  `disableBypassPermissionsMode` setting in JetBrains (vs. VS Code and Copilot CLI), or
  latency/cost implications of using the Claude agent via this integration.
- **Scope**: Eight features in the June 22, 2026 JetBrains Copilot update — Claude as agent
  provider (public preview), organization/enterprise agent support, CLI in-flight message
  queuing, debug logs summary view, model picker enhancements, per-turn AI credits indicator,
  and cloud agent reaching GA. Does NOT cover: comparative performance data for Claude vs.
  Copilot native agent, pricing differences between agent providers, how the JetBrains Claude
  integration relates to the standalone Claude Code product, or whether enterprise
  bypass-permissions-mode controls apply to the JetBrains Claude agent integration.

## Extracted Claims

### Claim 1: Claude is now available as a selectable agent provider in JetBrains IDEs in public preview, set up by installing Claude Code CLI and configuring its path in IDE settings

- **Evidence**: Official GitHub product changelog. Setup is a two-step prerequisite: install
  Claude Code CLI, then configure its path at Settings > Tools > GitHub Copilot > Chat.
  This makes Claude a choice in the JetBrains agent picker alongside Copilot's native agent.
- **Confidence**: emerging (official claim; public preview designation means behavior may
  change before GA; "Editor preview features" policy must be enabled for Business/Enterprise)
- **Quote**: "Claude as agent provider is now available in public preview, giving you more
  flexibility to pick the agent that best fits your task, all without leaving your JetBrains
  IDE."
- **Our assessment**: This is the headline capability. Claude joining the JetBrains agent
  picker (alongside Gemini in CLI/cloud agent surfaces since June 2 — see
  `docs-github-copilot-gemini-cli-cloud-agent-app.md` Claim 1) confirms a multi-provider
  agent ecosystem strategy: GitHub Copilot is becoming a model/agent router, not just a
  single-vendor AI surface. The "without leaving your JetBrains IDE" framing is significant —
  practitioners previously had to switch between JetBrains Copilot and a separate Claude Code
  terminal session to use Claude for agentic tasks. This integration consolidates both into
  the IDE agent picker. For Ch02 (harness engineering): document Claude as a provider option
  in the JetBrains agent picker, and note the Claude Code CLI prerequisite — this means the
  integration is technically a JetBrains-to-Claude-Code-CLI delegation, not a direct Anthropic
  API call, which has implications for how tools, permissions, and context are handled.

### Claim 2: The Claude agent in JetBrains runs in bypass permissions mode, meaning all file edits and tool calls are automatically approved without user confirmation

- **Evidence**: Official changelog explicitly states the permission behavior as a current
  limitation of the integration. The bypass permissions framing echoes the enterprise-managed
  settings control documented three days prior (June 17, 2026).
- **Confidence**: settled (behavioral fact stated definitively in official changelog as a
  current characteristic of the integration)
- **Quote**: "The Claude agent currently runs in bypass permissions mode, so all file edits
  and tool calls are automatically approved."
- **Our assessment**: This is the most significant limitation in the announcement. "Currently"
  suggests GitHub intends to add permission controls in a future release, but as of June 22,
  2026, practitioners who use Claude as agent provider in JetBrains cannot review or reject
  individual file edits or tool calls before they execute. The governance implication is
  acute when read alongside `docs-github-copilot-enterprise-bypass-permissions.md` Claim 1:
  that June 17 enterprise control (`disableBypassPermissionsMode: "disable"`) applies to
  "Copilot CLI and VS Code" but NOT to the JetBrains Claude agent integration (which was
  not yet announced). Enterprises that have deployed the bypass-permissions enterprise control
  may have a gap: Copilot CLI and VS Code are protected, but the new JetBrains Claude agent
  integration is not covered by the same control. For Ch02 and Ch05 (enterprise governance):
  document bypass permissions mode as a known limitation of the June 22 Claude agent
  integration; teams with strict permission-review requirements should not use this integration
  until explicit permission controls are added. Cross-reference `docs-github-copilot-enterprise-bypass-permissions.md`
  for the broader governance context.

### Claim 3: Organization and enterprise admins can publish custom agents that are now accessible directly within JetBrains IDEs

- **Evidence**: Official changelog documents the admin publishing workflow and the resulting
  member access. This extends the existing organization/enterprise agent capability (from
  GitHub.com and VS Code) to JetBrains.
- **Confidence**: emerging (official claim; Business/Enterprise admin-gated)
- **Quote**: "You can now use custom agents defined at the GitHub organization and enterprise
  level directly inside JetBrains IDEs."
- **Our assessment**: The process described is: "An organization or enterprise admin creates
  custom agents and publishes them so they are available to members." This is the same
  publish-and-discover model as the Agent Customizations editor documented in
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 8 for workspace/personal
  scope — now extended to the organizational tier. For Ch02 (harness engineering — agent
  configuration scope): the full JetBrains agent configuration scope model now spans: personal
  scope (`~/.copilot/agents/`), workspace scope, organizational scope (via admin publish),
  and enterprise scope (via admin publish). Teams that have defined org-level agents for
  github.com or VS Code should verify that those agents are now surfaced in JetBrains without
  additional configuration, or whether a separate publish step is required for each IDE.

### Claim 4: CLI sessions now support in-flight message queuing with three distinct interrupt modes — Add to Queue, Steer with Message, and Stop and Send — giving practitioners control over long-running agent tasks without canceling them

- **Evidence**: Official changelog documents all three modes by name, with the "Steer with
  Message" behavior described in detail. The framing ("you had to wait...or previously cancel
  it") establishes the prior friction and the specific improvement.
- **Confidence**: emerging (official claim; CLI agent still in public preview in JetBrains)
- **Quote**: "When working on longer tasks in Copilot CLI sessions, you had to wait for a
  response to complete or previously cancel it. Now you can send follow-up messages while a
  request is still running."
- **Our assessment**: The "Steer with Message" mode is the most substantive: "Tell the current
  request to yield once the active tool execution finishes, then process your new message
  immediately." This is a cooperative interrupt — the agent completes its current tool call,
  then yields to the practitioner's new instruction. "Add to Queue" is non-disruptive (the
  message waits until the current request finishes normally), and "Stop and Send" is a hard
  interrupt that cancels the current task and immediately starts processing the new message.
  Together, these three modes give practitioners fine-grained control over long-running agent
  tasks without losing the session. For Ch01 (daily workflows) and Ch04 (agentic workflows):
  document the three interrupt modes as a decision framework. "Add to Queue" for non-urgent
  follow-up; "Steer with Message" for redirecting mid-task when the agent is heading in the
  wrong direction but the current tool call should complete; "Stop and Send" for urgent course
  correction. This is the first documented in-flight steering capability for JetBrains CLI
  sessions in the corpus.

### Claim 5: The Agent Debug Panel has been enhanced with a logs summary view that provides a consolidated overview of agent activity

- **Evidence**: Official changelog describes the enhancement as an addition to the existing
  Agent Debug Panel, framed as a summary complement to the existing chronological event log.
- **Confidence**: emerging (official claim; capability enhancements in public preview context)
- **Quote**: "We've enhanced the Agent Debug panel with a new logs summary view that gives
  you a consolidated overview of agent activity."
- **Our assessment**: The June 2 note (`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
  Claim 5) introduced the Agent Debug Panel as "a chronological event log of agent interactions
  during a Copilot CLI session." This June 22 update adds a summary layer above the event log —
  a consolidated overview vs. a detailed chronological list. The two views serve different
  debugging needs: the event log is for step-by-step trace analysis; the summary view is for
  quickly assessing what happened during a session. For Ch04 (agentic workflows — debugging):
  update the Agent Debug Panel documentation to note the two views: event log (detailed trace)
  and logs summary (consolidated overview). Practitioners debugging sub-agent workflows should
  start with the summary view to identify anomalous areas, then drill into the event log for
  the specific sequence of events.

### Claim 6: The model picker gained a /models slash command that opens the picker directly with support for both Copilot CLI and Claude agent, plus a recently-used models section and context window selection

- **Evidence**: Official changelog lists three discrete enhancements to the model picker, each
  with a specific capability description. The /models command is the most novel addition.
- **Confidence**: emerging (official claim; model picker enhancements in preview context)
- **Quote**: "Open the model picker directly, with support for both Copilot CLI and Claude agent"
  (for /models) / "Recently used model section, so you can quickly select the models you use
  the most" / "Select a larger context window directly from the model picker"
- **Our assessment**: The /models slash command is significant for two reasons: (1) it adds a
  keyboard-accessible entry point to the model picker (faster than clicking through UI), and
  (2) it explicitly supports both Copilot CLI and the new Claude agent — confirming the picker
  is the unified control surface for agent provider selection. The recently-used models section
  addresses friction for practitioners who alternate between two or three models depending on
  task type (e.g., Claude for complex reasoning, a faster model for quick lookups). Context
  window selection from the picker formalizes what was previously a model-specific detail into
  a practitioner-visible choice point. For Ch02 (harness engineering): document /models as the
  slash command equivalent of the model picker UI — practitioners who prefer keyboard-driven
  workflows can use /models to switch providers mid-session without breaking flow.

### Claim 7: Per-turn AI credits consumption is now visible inline during local, CLI, and Claude agent sessions

- **Evidence**: Official changelog states the three session types that now display the indicator.
  This makes per-request cost visible at the moment of consumption rather than requiring
  post-hoc dashboard review.
- **Confidence**: settled (product fact stated definitively in official changelog)
- **Quote**: "Local, CLI, and Claude agent sessions now display a per-turn AI credits indicator."
- **Our assessment**: Per-turn credit visibility closes the cost feedback loop that was
  previously available only in aggregate metrics
  (`docs-github-copilot-cli-activity-usage-metrics.md`). Practitioners can now observe credit
  consumption per request and adapt behavior in real time (e.g., switching to a lower-cost
  model for routine tasks). The inclusion of the "Claude agent" session type confirms that the
  Claude agent integration is metered through GitHub's AI credit system, not through separate
  Anthropic API billing — practitioners on plans with AI credit budgets need to account for
  Claude agent usage within their existing Copilot credit pool. For Ch02: document per-turn
  cost visibility as a session-level feedback primitive. For Ch04: note that the AI credits
  indicator enables real-time cost management during long agent sessions, where accumulated
  per-turn costs may exceed expectations without inline visibility.

### Claim 8: Cloud agent has reached general availability, no longer requiring the Editor Preview feature flag in JetBrains

- **Evidence**: Official changelog "Availability updates" section explicitly removes the
  preview qualifier for cloud agent. Claude as agent provider remains in public preview.
- **Confidence**: settled (GA promotion stated definitively in official changelog)
- **Quote**: "Cloud agent is now generally available (no longer behind the `Editor Preview`
  feature flag)."
- **Our assessment**: Cloud agent (Copilot Coding Agent / CCA) in JetBrains has followed the
  same graduation trajectory as other Copilot features: preview → GA, shedding the Editor
  Preview feature flag requirement. The contrast with Claude as agent provider (remaining in
  public preview) is meaningful: cloud agent (GitHub-native) is stable and GA; Claude
  (third-party integration) is preview. For Ch02 (harness engineering): update any language
  describing cloud agent as "preview" or "flag-gated" for JetBrains. Administrators no longer
  need to enable the Editor Preview features policy specifically for cloud agent access — though
  they still need to enable "Enable Coding Agent" at Settings > Tools > GitHub Copilot > Chat.
  The Claude agent and new model picker features still require the Editor Preview features
  policy for Business/Enterprise users.

## Concrete Artifacts

### Claude Agent Provider Setup (JetBrains, June 22, 2026)

```
Prerequisites:
  1. Install Claude Code CLI on your local machine
  2. Configure Claude Code CLI path:
     Settings > Tools > GitHub Copilot > Chat > [set Claude Code CLI path]

Selection:
  Select Claude from the agent picker in JetBrains Copilot Chat

Behavior:
  - "The Claude agent currently runs in bypass permissions mode,
    so all file edits and tool calls are automatically approved."
  - Per-turn AI credits consumption shown inline

Admin requirement (Copilot Business/Enterprise):
  Editor preview features policy must be enabled by administrator

Status: public preview as of June 22, 2026
```

*Source: New features and Claude as agent provider preview in JetBrains IDEs, GitHub changelog, June 22, 2026*

### CLI Message Queuing — Interrupt Modes

```
Available when a CLI session request is running:

Add to Queue
  Message waits in queue; processed after current request completes normally.

Steer with Message
  "Tell the current request to yield once the active tool execution
   finishes, then process your new message immediately."
  → Cooperative interrupt: current tool call completes, then yields.

Stop and Send
  Hard interrupt: cancels the current request immediately, then
  processes your new message.

Use case guidance:
  Add to Queue      → non-urgent follow-up, let task finish
  Steer with Message → redirect mid-task without losing current progress
  Stop and Send      → urgent course correction needed immediately
```

*Source: New features and Claude as agent provider preview in JetBrains IDEs, GitHub changelog, June 22, 2026*

### Model Picker Enhancements (JetBrains, June 22, 2026)

```
New capabilities:
  /models            Open the model picker directly; supports both
                     Copilot CLI and Claude agent.
  Context window     Select a larger context window directly from
                     the model picker.
  Recently used      Recently used model section for quick re-selection.

Per-turn indicator:  AI credits consumption shown inline for local,
                     CLI, and Claude agent sessions.
```

*Source: New features and Claude as agent provider preview in JetBrains IDEs, GitHub changelog, June 22, 2026*

### Availability Status Summary (JetBrains, June 22, 2026)

```
Feature                           Status
──────────────────────────────────────────────────────────────────────
Cloud agent                       Generally available (GA)
                                  No longer requires Editor Preview flag
Claude as agent provider          Public preview
                                  Requires Editor Preview flag (B/E)
Organization/enterprise agents    Generally available (implied; not
                                  explicitly flagged as preview)
CLI message queuing               Generally available (implied)
Debug logs summary view           Available (panel enhancement)
Model picker enhancements         Generally available
Per-turn AI credits indicator     Generally available
```

*Source: New features and Claude as agent provider preview in JetBrains IDEs, GitHub changelog, June 22, 2026*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-gemini-cli-cloud-agent-app.md` (Claim 1): Gemini 3.1 Pro and 3.5
    Flash were added to Copilot CLI and cloud agent on June 2, 2026. The June 22 source adds
    Claude as a JetBrains IDE agent provider. Together, these two sources confirm a multi-provider
    agent strategy where GitHub Copilot routes to different underlying AI agents: Claude (via
    Claude Code CLI) and Gemini in developer-facing surfaces, alongside Copilot's native agent.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (Claim 5): The June 2 note
    introduced the Agent Debug Panel as "a chronological event log of agent interactions during
    a Copilot CLI session." Claim 5 in this note corroborates and extends that by adding the
    logs summary view as a higher-level overlay on the same panel — same feature, enhanced.
  - `docs-github-copilot-enterprise-bypass-permissions.md` (Claim 2): The June 17 enterprise
    note documented that bypass permissions mode applies to "Copilot CLI and VS Code" and can
    be disabled enterprise-wide via `disableBypassPermissionsMode: "disable"`. Claim 2 in
    this note corroborates that bypass permissions mode exists as a named behavior in GitHub
    Copilot tooling — and specifically confirms that the Claude agent in JetBrains ALSO runs
    in bypass mode. However, the enterprise control covers Copilot CLI and VS Code; its
    applicability to the JetBrains Claude agent integration is not addressed by either source.

- **Extends**:
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` (all claims): The May 13 foundation
    introduced the Copilot CLI agent in JetBrains with worktree/workspace isolation. This June
    22 note builds on that foundation by adding Claude as a second agent provider option in
    the same picker, and adding in-flight message queuing as a new control during CLI sessions.
  - `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` (all claims): The June 2
    enhancements note added the agent picker, /chronicle, /compact, cloud agent in unified
    sessions view, thinking effort control, and Agent Customizations editor. This June 22 note
    adds Claude as a provider to that same picker, enhances the debug panel, and enriches the
    model picker. The progression is: May 13 (CLI agent foundation) → June 2 (session management
    + debug panel) → June 22 (multi-provider + cost visibility + message control).
  - `docs-github-copilot-enterprise-bypass-permissions.md` (Claims 1, 2): The June 17
    enterprise governance note documented bypass permissions mode control for Copilot CLI and
    VS Code. This June 22 note reveals a third surface — the JetBrains Claude agent integration
    — that runs in bypass mode but is NOT yet covered by the enterprise `disableBypassPermissionsMode`
    control. This extends the governance gap analysis: organizations that have deployed the
    enterprise bypass permissions control should audit whether the JetBrains Claude agent
    integration creates a new ungoverned bypass-permissions surface.

- **Contradicts**: None identified. No existing corpus source makes a conflicting claim about
  Claude's availability as an agent provider in JetBrains. The Gemini note's multi-provider
  framing is complementary, not contradictory. No contradiction issue filed.

- **Novel**:
  - **Claude as a selectable agent provider in a GitHub Copilot IDE surface** (Claim 1): No
    prior corpus source documents Claude being selectable as an agent provider within JetBrains
    (or any IDE) through the GitHub Copilot plugin interface. All prior cross-provider entries
    in the corpus involve model selection (e.g., Claude Sonnet, Claude Haiku as model options)
    — not agent provider selection, where Claude Code CLI handles tool calls and file edits.
  - **Bypass permissions mode as a known characteristic of the Claude agent integration**
    (Claim 2): While bypass permissions mode has been documented as an enterprise control
    target (`docs-github-copilot-enterprise-bypass-permissions.md`), this is the first corpus
    source documenting that a specific GitHub Copilot agent integration ALWAYS runs in bypass
    mode by design, with no current per-request override available in JetBrains.
  - **In-flight CLI message queuing with three distinct interrupt semantics** (Claim 4): No
    prior corpus source documents a message queue or interrupt mechanism for running CLI
    sessions. The three-mode model (Add to Queue / Steer with Message / Stop and Send) is
    the first documented cooperative interrupt control for in-progress agent tasks in JetBrains.
  - **Organization/enterprise agents surfacing in JetBrains IDEs** (Claim 3): Prior corpus
    notes documented org/enterprise agents in the context of the GitHub web UI and agent
    customizations editor — this is the first explicit documentation of org/enterprise agents
    being accessible from JetBrains as an IDE-native experience.
  - **Per-turn AI credits indicator inline in sessions** (Claim 7): While aggregate AI credits
    usage metrics have been documented, this is the first corpus source documenting per-turn
    inline credit visibility during active sessions. This converts cost from a post-hoc metric
    into a real-time behavioral signal.

## Guide Impact

- **Chapter 02 (Harness Engineering — Agent Provider Selection)**:
  - Add Claude as a provider option in the JetBrains agent picker, documenting the prerequisite
    (Claude Code CLI installation + path configuration at Settings > Tools > GitHub Copilot > Chat).
  - Document the bypass permissions limitation: practitioners who need to review file edits or
    tool calls before approval should not use the Claude agent integration in JetBrains until
    explicit permission controls are added.
  - Document the `/models` slash command as the keyboard-accessible entry point to the model
    picker, which now serves as the unified control surface for agent provider selection.
  - Add organization/enterprise agent support in JetBrains to the agent configuration scope
    model: personal scope → workspace scope → organizational scope (admin-published) → enterprise
    scope (admin-published).

- **Chapter 02 (Harness Engineering — Enterprise Governance)**:
  - Add a governance gap note: the enterprise `disableBypassPermissionsMode` control covers
    Copilot CLI and VS Code but does NOT explicitly cover the JetBrains Claude agent integration
    (announced June 22). Organizations using the June 17 enterprise bypass permissions control
    should assess whether the new Claude agent integration creates an ungoverned bypass-permissions
    surface in JetBrains.
  - Update cloud agent governance notes: cloud agent in JetBrains is now GA, no longer requiring
    the Editor Preview feature flag. Claude agent still requires the flag for Business/Enterprise
    users.

- **Chapter 04 (Agentic Workflows — Tooling Landscape)**:
  - Document the three CLI interrupt modes (Add to Queue / Steer with Message / Stop and Send)
    as a practitioner decision framework for managing long-running CLI agent sessions. These
    convert session management from an all-or-nothing choice (wait or cancel) into a nuanced
    control surface.
  - Update the Agent Debug Panel documentation: add the logs summary view as a new view
    alongside the chronological event log. Recommend summary-first → event-log-drill workflow
    for debugging complex agent interactions.

- **Chapter 01 (Daily Workflows — Cost Awareness)**:
  - Document the per-turn AI credits indicator as a real-time cost feedback mechanism for
    local, CLI, and Claude agent sessions. Practitioners can use this to identify expensive
    requests and adapt (e.g., switch to a lower-cost model for simpler follow-ups) without
    waiting for monthly usage dashboard review.

## Extraction Notes

1. **Source is a changelog (~500 words)**: All eight substantive engineering-relevant features
   are captured in the claims above. Standard UI/UX polish items (if any) were not surfaced by
   the WebFetch extraction.
2. **Two WebFetch calls made**: The first call returned a structured summary with feature
   headings and key quotes. The second call requested verbatim text for each section, yielding
   additional exact phrases used as quotes in Claims 1–5. The WebFetch model processes HTML and
   returns AI-processed content, not raw HTML verbatim. All quote fields use text returned in
   quotation marks by WebFetch. The Assayer should spot-check all quotes against the live source
   URL, especially the Claim 4 "Steer with Message" description and the Claim 7 per-turn credits
   indicator quote.
3. **Bypass permissions governance gap**: The interaction between the June 17 enterprise bypass
   permissions control and the June 22 Claude agent bypass mode is an inference from reading
   both notes together. Neither source explicitly addresses this combination. The Assayer should
   flag if this inference is over-stated, but the governance risk appears real and worth surfacing.
4. **Organization/enterprise agents GA status**: The changelog does not explicitly label
   organization/enterprise agent support in JetBrains as "public preview" — unlike Claude
   agent provider and other features. The status table in Concrete Artifacts marks this as
   "Generally available (implied)" but the Assayer should verify whether a preview qualifier
   appears in the source for this feature.
5. **"Currently" qualifier in bypass permissions claim**: The source says Claude agent
   "currently runs in bypass permissions mode" — the word "currently" strongly implies GitHub
   intends to add per-request permission controls in a future update. This is NOT extracted as
   a claim (it is speculative) but noted here for the guide maintainers.
6. **No contradictions to file**: No existing corpus source makes a claim that directly opposes
   any claim in this note. The bypass permissions governance gap is a synthesis observation
   about scope coverage, not a factual contradiction between opposing source claims.
