---
source_url: https://github.blog/changelog/2026-04-23-view-and-manage-agent-sessions-from-issues-and-projects
source_type: docs
title: "View and manage agent sessions from issues and projects"
author: GitHub (official changelog)
date_published: 2026-04-23
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#385"
---

# View and Manage Agent Sessions from Issues and Projects

> GitHub's April 2026 changelog that adds the GitHub Issues and Projects web UI
> as a native surface for monitoring and steering cloud agent sessions — extending
> the multi-surface agent management landscape beyond IDEs and APIs to the project
> planning layer where work is tracked.

## Source Context

- **Type**: docs (GitHub official product changelog, April 23, 2026; brief
  ~200-word announcement with two UI-surface descriptions)
- **Author credibility**: GitHub engineering team announcing a production feature
  change. Authoritative for the fact that these UI surfaces now exist and the
  described behavior. Not a credible source for how frequently practitioners use
  these surfaces, whether steering from the Issues/Projects UI produces different
  outcomes than steering from the IDE, or cost implications of agent sessions
  monitored this way.
- **Scope**: Two distinct UI enhancements — (1) an agent session visibility header
  on GitHub Issues, (2) default-enabled session visibility in GitHub Projects.
  Also includes a minor label-picker UX change unrelated to agent sessions. Does
  NOT cover: how steering controls work in detail (what inputs the sidebar accepts,
  what actions the agent takes in response), how this surfaces relates to the
  enterprise CCA enablement API, whether session visibility requires a specific
  Copilot tier, or latency/cost implications of steering mid-session.

## Extracted Claims

### Claim 1: GitHub Issues now shows a header pill listing all active and completed cloud agent sessions associated with that issue

- **Evidence**: Official GitHub product changelog describing new UI behavior on
  issue pages. The pill is always visible in the issue header, not buried in a
  sidebar or separate tab.
- **Confidence**: emerging (product fact — the feature is described in official
  changelog; no data on adoption or effectiveness)
- **Quote**: "all active and completed agent sessions at a glance"
- **Our assessment**: This is a meaningful visibility improvement for teams using
  cloud agents on GitHub issues. Previously, tracking which agent sessions were
  running against a given issue required navigating to separate dashboards, using
  the API, or checking the IDE. Putting that information directly in the issue
  header means any team member who can view the issue can immediately see whether
  an agent is actively working on it, has completed work, or failed — without
  context-switching. The "at a glance" framing suggests the pill shows session
  status at minimum, not just raw session IDs.

### Claim 2: Clicking an agent session in the issue header opens a sidebar with progress, logs, and agent steering controls

- **Evidence**: Official changelog describes the sidebar content: "progress, logs,
  and agent steering options."
- **Confidence**: emerging (UI behavior described in official changelog; no detail
  on what steering options are available or how they translate to agent behavior)
- **Quote**: (no direct quote for full sidebar description; see paraphrase in Our assessment)
- **Our assessment**: The steering controls are the operationally significant
  part. "Steering" implies the ability to redirect the agent mid-session — not
  just observe it. If this includes the ability to add instructions, stop the
  session, or approve actions, it is a meaningful human-in-the-loop mechanism
  at the work-item level (as opposed to the IDE level, where steering is done
  through the chat interface). The changelog does not specify what inputs the
  sidebar accepts, which is a gap that limits how concretely this can be
  recommended. The presence of logs in the sidebar complements the progress view
  — practitioners can check whether the agent is executing the right steps, not
  just that it is running.

### Claim 3: Agent session visibility is now enabled by default in GitHub Projects views for both new and existing projects

- **Evidence**: Official changelog statement about the default-enabled state.
  Prior to this change, enabling agent session visibility in Projects presumably
  required opt-in configuration.
- **Confidence**: emerging (product fact; no data on whether previous opt-in was
  widely used or why the default changed)
- **Quote**: "now enabled by default for both new and existing project views"
- **Our assessment**: Default-enabled is a deliberate product choice — GitHub is
  signaling that agent session visibility should be part of normal project
  workflow, not a power-user opt-in. For teams using GitHub Projects as their
  sprint/kanban board, this means agent sessions running against tracked issues
  become visible in the project view without any additional setup. The "existing
  project views" scope means this applies retroactively — teams that already use
  GitHub Projects will see session data without doing anything. This default
  change is more significant than it sounds: it normalizes AI agent activity as
  a first-class project management concern, not an adjacent developer tool.

### Claim 4: Agent sessions can be opened and monitored directly from the GitHub Projects board sidebar

- **Evidence**: Official changelog describes the workflow: users "can access
  session details directly from the project board sidebar."
- **Confidence**: emerging (behavior described in official changelog; no detail
  on how the sidebar is triggered or what information it shows)
- **Quote**: (no direct quote for the project board sidebar behavior; see paraphrase in Our assessment)
- **Our assessment**: The project-board sidebar is a different entry point from
  the issue-level sidebar (Claim 2). From the project board view, a project
  manager or team lead who is not the developer working on an issue can see which
  tasks have active agent sessions without opening each issue individually. This
  is meaningful for teams with high issue volumes — they can scan the project
  board for agent activity the same way they scan for PR status or assignee
  information. It also supports a workflow where project managers steer agents
  without switching into a developer context (IDE or API).

### Claim 5: The label picker now surfaces frequently used labels first, reducing the time spent searching for common labels when labeling issues and PRs

- **Evidence**: Changelog mentions the label picker UX improvement alongside the
  agent session features.
- **Confidence**: emerging (claimed behavior; no data on the magnitude of
  efficiency gain or how "frequent" is measured — per-user history, per-repo
  aggregate, or per-org)
- **Quote**: "your most frequently used labels and surfaces them at the top"
- **Our assessment**: This is a minor UX improvement unrelated to agent session
  management. It is worth extracting because teams using label-heavy workflows
  (e.g., the agent-label patterns described in `blog-ghaw-issue-pr-mgmt.md`)
  will benefit from reduced friction. Not a primary signal for AI-native
  engineering patterns; included for completeness. The "your" phrasing implies
  personalized frequency tracking (per-user), not global repo-level suggestions.

### Claim 6: The GitHub web UI (Issues and Projects) is now a third orchestration surface for cloud agent sessions, alongside IDEs and APIs

- **Evidence**: Our synthesis across this source and related corpus notes.
  This source adds the GitHub web UI to the picture documented in
  `docs-github-copilot-vs-april-2026.md` (IDE as dispatch surface) and
  `docs-github-copilot-cca-custom-properties.md` (enterprise API as governance
  surface). No single quote captures this synthesis.
- **Confidence**: emerging (synthesis across sources, not a single stated claim)
- **Quote**: "view and steer cloud agent sessions directly from issues and projects"
- **Our assessment**: Before this changelog, cloud agent session management
  involved three surfaces: (1) the enterprise API for governance, (2) the GitHub
  CLI for operational management, and (3) IDE integrations for developer-facing
  control. This source adds a fourth: the GitHub web UI within the project
  management layer. The "steer" verb is significant — the Issues/Projects UI is
  not read-only monitoring; it is positioned as an active control surface. For
  teams where project managers are not in an IDE, this surface fills a meaningful
  gap. The complete surface inventory is now: enterprise API (governance), GitHub
  CLI (operational), IDE (developer), GitHub Issues/Projects UI (project
  management).

## Concrete Artifacts

### Agent Session Visibility — UI Entry Points (April 23, 2026)

```
GitHub Issues:
  Location: Issue header (above issue body, below issue title)
  Display:  Pill showing all active and completed agent sessions
  Action:   Click session → sidebar with progress, logs, steering controls

GitHub Projects:
  Location: Project board (sidebar accessible from board view)
  Display:  Agent sessions associated with issues on the board
  Status:   Enabled by default for new AND existing project views
  Action:   Click session → sidebar with session details

Prior to this change: session management required IDE, CLI, or API
After this change: sessions visible directly in project management UI
```

### Multi-Surface Agent Session Management Landscape (synthesized)

```
Surface                    Role               Entry Point
─────────────────────────────────────────────────────────────────────
Enterprise API             Governance         REST API (CCA policy)
  (CCA custom-properties)  Enable/disable     [docs-github-copilot-cca-custom-properties.md]

GitHub CLI                 Operational        Terminal
  (gh skill, gh aw)        Inspect sessions   [docs-github-copilot-agent-skills-cli.md]

IDE (Visual Studio,        Developer          Agent picker in IDE
  VS Code, etc.)           Initiate + steer   [docs-github-copilot-vs-april-2026.md]

GitHub Issues UI           Project member     Issue header pill → sidebar
  (this source)            Monitor + steer    All active/completed sessions shown

GitHub Projects UI         Project manager    Project board → sidebar
  (this source)            Monitor at scale   Default-enabled, no setup needed
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-vs-april-2026.md` Claim 7: That note documents cloud
    agents being initiated from the VS IDE picker, with output landing as GitHub
    issues and PRs on remote infrastructure. This source completes the loop: the
    agent sessions that VS IDE *initiates* can now be *monitored and steered*
    from the GitHub Issues and Projects web UI where those issues and PRs live.
    Together the two notes define the full lifecycle of a VS-initiated cloud agent
    session: start in IDE → work tracked in Issues → session observable from that
    same issue.
  - `docs-github-copilot-vs-april-2026.md` Claim 8: That note documents that
    cloud agents produce both a GitHub issue and a pull request as output artifacts.
    This source shows those output issues now carry agent-session visibility headers
    — the issue is not just a record of what was done, but also a live monitoring
    surface while the agent is still working.
  - `blog-ghaw-agent-observability.md` Claim 1: That note documents observability
    as a non-optional concern for multi-agent systems, implemented via dedicated
    observability workflows in GitHub's own agent factory. This source shows
    GitHub embedding observability directly into the native Issues/Projects UI —
    reducing the implementation burden for teams who want session visibility
    without building custom observability workflows.

- **Extends**:
  - `docs-github-copilot-cca-custom-properties.md`: That note covers the
    enterprise-level API for enabling CCA (governance layer). This source adds
    the developer and project manager-facing web UI for session monitoring
    (operational layer). A complete picture of CCA management now requires both:
    the API for policy (who can run agents, in which orgs) and the Issues/Projects
    UI for runtime visibility (what sessions are running, what they are doing).
  - `docs-github-copilot-agent-model-selection.md`: That note covers model
    selection at the moment of agent task initiation. This source covers the
    complementary post-initiation phase — monitoring and steering sessions once
    they are running. Together they document the full operator-facing session
    lifecycle: select model → initiate task → monitor via Issues/Projects UI →
    steer if needed.
  - `docs-github-copilot-vs-april-2026.md`: That note establishes the VS IDE as
    a "dispatch and continue" surface. This source adds a parallel "check in and
    steer" surface in the project management layer, enabling non-IDE users (project
    managers, other team members) to participate in agent oversight.

- **Contradicts**: None identified. No existing source note claims that agent
  session management should be confined to IDE or API surfaces, or that the
  GitHub web UI is unsuitable for this role.

- **Novel**:
  - First source in corpus documenting the GitHub Issues/Projects web UI as a
    native surface for cloud agent session monitoring and steering. Prior sources
    document IDEs, CLIs, and enterprise APIs as management surfaces; the project
    management web UI is new.
  - The "default-enabled in Projects" change establishes a new product-level
    stance: agent session visibility is a standard project management feature,
    not an opt-in developer tool. No prior source documents a GitHub product
    decision that makes AI agent activity visible by default in project management
    surfaces.
  - The issue-level header pill is a novel UI pattern in the corpus: a persistent,
    always-visible indicator of agent activity attached to a work item. This
    differs from notification-based approaches (where you find out when the agent
    finishes) and dashboard approaches (where you navigate to a separate view) —
    the pill integrates agent status into the work item itself.

## Guide Impact

- **Chapter 01 (Daily Workflows — Multi-Agent Orchestration)**:
  - The "delegate and continue" pattern documented in the VS source note can now
    be strengthened with a concrete monitoring step: after delegating a task to
    a cloud agent, practitioners can check session progress directly from the
    GitHub issue without leaving the GitHub web UI or opening the IDE. Add this
    as a concrete workflow step: delegate → assign issue → continue other work →
    check issue header pill for session progress → steer from sidebar if needed.
  - Update the "15-minute cadence" concept: the Issues/Projects UI provides a
    low-friction "check in" mechanism that supports cadenced oversight without
    requiring IDE or CLI access.

- **Chapter 02 (Harness Engineering — Tooling Landscape)**:
  - Add the GitHub Issues/Projects web UI to the agent session management surface
    inventory. Teams building their AI engineering harness should account for all
    four surfaces (enterprise API, CLI, IDE, web UI) and document which team
    members use which surface. Project managers and team leads who do not use
    IDEs now have a native monitoring surface — harness documentation should
    explain how each role accesses session information.
  - Note that Projects session visibility is default-enabled and requires no
    additional configuration — it is "free" visibility that teams get without any
    harness engineering investment.

- **Chapter 04 (Context Engineering)**:
  - The sidebar steering controls (Claim 2) represent a mid-session context
    injection point: a human can add guidance to a running agent session from the
    issue UI. If steering translates to injected instructions (the mechanism is
    not documented), this is a form of context engineering at the session layer —
    practitioners are shaping the agent's behavior by injecting context mid-run.
    This is worth flagging as a novel context engineering surface once steering
    mechanics are better documented.

## Extraction Notes

1. **Source is very brief (~200 words)**: This is a short feature-announcement
   changelog. All substantive content is exhausted in 6 claims above. The source
   does not describe steering mechanics, tier requirements, or how session visibility
   integrates with GitHub's existing notification/webhook system.
2. **WebFetch returned a processed summary, not raw HTML**: The verbatim quotes
   used above (in double quotes) were returned inside quotation marks by the
   WebFetch tool, indicating they are likely verbatim from the source page. The
   Assayer should verify these against the source URL directly. Claims where no
   verbatim quote was available are marked "(no direct quote; see paraphrase in
   Our assessment)".
3. **Steering mechanics undocumented**: The changelog mentions "agent steering
   options" without specifying what inputs are accepted or how they affect the
   running agent. Until steering mechanics are documented (in a follow-on
   changelog or docs page), the guide should describe this as "steering controls
   available via sidebar" without specifying what actions are supported.
4. **Tier requirements absent**: The changelog does not state which Copilot
   subscription tiers have access to this feature. It may be available only to
   Business/Enterprise tiers (consistent with other CCA features), but this is
   not confirmed in the source. Guide guidance should note this gap.
5. **No contradictions to file**: No existing source note claims that agent
   session management should not be available from the GitHub web UI, or that
   only IDEs/APIs are appropriate management surfaces. The multi-surface pattern
   here extends existing notes rather than contradicting them.
6. **Label picker improvement excluded from primary claims**: The label picker
   change (Claim 5) is included for completeness but is not an AI-native
   engineering pattern. It is a minor UX improvement that may benefit teams
   using label-heavy agentic workflows.
