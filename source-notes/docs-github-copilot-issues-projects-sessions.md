---
source_url: https://github.blog/changelog/2026-04-23-view-and-manage-agent-sessions-from-issues-and-projects
source_type: docs
title: "View and manage agent sessions from issues and projects"
author: GitHub (official changelog)
date_published: 2026-04-23
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: settled
issue: "#385"
---

# View and Manage Agent Sessions from Issues and Projects

> GitHub's April 2026 changelog makes GitHub issues and projects first-class
> web-native surfaces for monitoring and steering cloud agent sessions — adding a
> persistent "session pill" in issue headers and a session sidebar in both surfaces —
> complementing the CLI remote control, VS Code, and JetBrains management surfaces
> already documented in this corpus.

## Source Context

- **Type**: docs (GitHub official product changelog, April 23, 2026; approximately
  200 words, marked "1 minute read")
- **Author credibility**: GitHub engineering team announcing a production feature.
  Authoritative for the existence of these UI elements, how to access them, and what
  they enable. Not a credible source for: how often practitioners use these surfaces,
  whether steering via issues/projects differs from steering via CLI or VS Code, or
  what specific steering actions are available beyond what the changelog names.
- **Scope**: Two new agent-session surfaces — the issue header session pill and
  issue sidebar panel, plus agent session visibility in GitHub Projects boards with
  a matching sidebar. Also announces label picker prioritization (non-agentic UX).
  Does NOT cover: what "steer the agent" entails at the prompt level, whether CLI
  (local) agent sessions appear here or only cloud (CCA) sessions, how issue/project
  session visibility relates to the global `github.com/copilot/agents` dashboard,
  or cost implications of sessions.

## Extracted Claims

### Claim 1: GitHub issues and projects are now first-class surfaces for viewing and steering cloud agent sessions without leaving the GitHub web UI

- **Evidence**: Official GitHub product changelog announcing the feature as active.
  The introductory sentence states the integration goal directly.
- **Confidence**: settled (product fact — surfaces exist and are documented)
- **Quote**: "You can now view and steer cloud agent sessions directly from issues
  and projects, giving you better visibility into agent activity without leaving your
  workflow."
- **Our assessment**: The phrase "without leaving your workflow" signals the
  design intent: reduce context switching for practitioners managing agent sessions
  while triaging GitHub issues or running sprint boards. Previously, monitoring an
  agent session required navigating to `github.com/copilot/agents` or switching to
  an IDE. This integration surfaces agent state where the work lives. For Ch04
  (agentic workflows): document this as the "GitHub native context" for agent session
  management — distinct from the IDE-centric view (`docs-github-copilot-vs-april-2026`,
  `docs-github-copilot-jetbrains-cli-agent-sessions`) and the terminal-centric CLI
  (`docs-github-copilot-cli-remote-control-ga`).

### Claim 2: A "session pill" in the issue header shows all active and completed agent sessions at a glance

- **Evidence**: Official changelog describes the UI element explicitly as a "header
  pill" visible in the issue header, with defined scope (all active and completed
  sessions for that issue).
- **Confidence**: settled (UI element described in official changelog)
- **Quote**: "A new header pill on issues shows all active and completed agent sessions
  at a glance."
- **Our assessment**: The session pill is a passive observability primitive — it
  is always visible in the issue header regardless of what the user is doing, making
  agent activity on an issue legible without the user navigating anywhere. This
  changes the review workflow: when triaging issues, practitioners can see at a
  glance whether an agent is working on an issue (active session) or has completed
  work (completed session). For Ch02 (harness engineering): when cloud agents are
  assigned to GitHub issues, the session pill becomes part of the natural issue review
  workflow — reviewers see agent status before reading comments.

### Claim 3: Clicking any session from the issue pill or assignee area opens a sidebar where practitioners can view progress, review logs, or steer the agent

- **Evidence**: Official changelog describes both trigger points (pill and assignee
  area) and the three capabilities in the sidebar.
- **Confidence**: settled (UI interaction documented in official changelog)
- **Quote**: "Click any session from the pill or assignee area to open it in the
  sidebar, where you can view progress, review logs, or steer the agent."
- **Our assessment**: The sidebar is accessible from two locations (session pill
  and assignee area), indicating agent sessions are also threaded into the assignee
  metadata panel. The three named capabilities map to three practitioner needs:
  monitoring (view progress), forensics (review logs), and control-plane action
  (steer). "Steer" is not further specified in this changelog — based on
  `docs-github-copilot-cli-remote-control-ga` (Claim 2), steering likely includes
  queuing messages and guiding the agent's next steps, but this is inferred. For
  the guide: the log review capability directly in the issue panel is significant
  for post-session analysis — practitioners do not need a separate dashboard to see
  what the agent did on a given issue.

### Claim 4: "Show agent sessions" is enabled by default in GitHub Projects for both new and existing project views

- **Evidence**: Official changelog states this default behavior change explicitly,
  covering both new and existing views.
- **Confidence**: settled (product default documented in official changelog)
- **Quote**: "'Show agent sessions' is now enabled by default."
- **Our assessment**: Changing to a default-on setting means all existing GitHub
  Projects views will show agent sessions without any opt-in action from project
  administrators. Teams that already use GitHub Projects for sprint management will
  see agent session data in their boards automatically. For Ch05 (team adoption):
  this is a default behavior change affecting all GitHub Projects users — teams not
  using cloud agent sessions will see blank/empty sections; teams using CCA will see
  session data immediately. Advise teams to evaluate whether this default is
  appropriate before rolling out to non-technical stakeholders who may be confused
  by agent session entries in sprint boards.

### Claim 5: Clicking an agent session from a project board opens the same sidebar panel available in issues

- **Evidence**: Official changelog describes the project board entry point, implying
  the same sidebar interaction model from issues is reused in projects.
- **Confidence**: settled (documented in official changelog)
- **Quote**: "Click on an agent session from your project board to open it directly."
- **Our assessment**: The consistency between issues and projects is deliberate — a
  uniform interaction model (click session → open sidebar with progress/logs/steer)
  works across both GitHub surfaces. This reduces cognitive load: wherever practitioners
  see an agent session indicator in GitHub, the same sidebar opens. For Ch04: document
  this uniform pattern — practitioners do not need to learn different UX for managing
  sessions in issues vs. projects.

### Claim 6: The label picker now surfaces frequently used labels first, reducing search friction (non-agentic improvement)

- **Evidence**: Official changelog includes this as an additional improvement in the
  same release.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "The label picker now remembers your most frequently used labels and
  surfaces them at the top."
- **Our assessment**: This is a non-agentic UX improvement included in the same
  release. It has minimal signal for the guide's AI-native engineering focus.
  Extracted for completeness; not a primary claim for guide chapter recommendations.

## Concrete Artifacts

### Issue Header Session Pill — Interaction Model

```
GitHub Issue Page:
  [Issue Title]
  [Session Pill in header: shows count/status of all active + completed sessions]
  [Assignee area: also shows agent session entry points]

Access paths to sidebar:
  1. Click session in header session pill
  2. Click session in assignee area

Sidebar capabilities:
  • View progress    (live status monitoring)
  • Review logs      (forensic / post-session analysis)
  • Steer the agent  (control-plane steering)
```

*Source: View and manage agent sessions from issues and projects, GitHub Changelog,
April 23, 2026*

### GitHub Projects — Agent Session Integration

```
GitHub Projects board view:
  Project cards now show agent session indicators

"Show agent sessions" setting:
  → Default: ENABLED for new AND existing project views
  → Override: disable in project view settings if desired

Clicking session on project board:
  → Opens same sidebar panel as issues
     (progress, logs, steer)
```

*Source: View and manage agent sessions from issues and projects, GitHub Changelog,
April 23, 2026*

### Agent Session Access Surfaces — GitHub Web UI (as of April 2026)

```
Surface                        Access Path                    Scope
────────────────────────────────────────────────────────────────────────────
github.com/copilot/agents      Direct URL navigation          All sessions, global
Issue header — session pill    Click pill on any issue        Sessions for that issue
Issue header — assignee area   Click session in assignee      Sessions for that issue
Projects board card            Click session on project card  Sessions for that issue
```

*Synthesized from this source and docs-github-copilot-cli-remote-control-ga.md
(global dashboard surface)*

## Cross-References

- **Corroborates** `docs-github-copilot-cli-remote-control-ga.md` (Claim 1, Claim 2):
  That source documents remote control for Copilot CLI sessions across mobile,
  github.com, VS Code, and JetBrains — enabling practitioners to track progress,
  steer, review plans, stop sessions, approve permissions, and respond to questions.
  This source adds GitHub issues and project boards as additional access points to
  equivalent session monitoring and steering capabilities. Both sources reflect
  GitHub's consistent strategy: make agent session management available from any
  surface practitioners are already working in, rather than requiring dedicated
  session dashboards.

- **Extends** `docs-github-copilot-cli-remote-control-ga.md` (Claim 6): That source
  documents `github.com/copilot/agents` as the global session dashboard (spanning
  repositories and non-repository directories). This source adds two embedded
  web surfaces — issues and projects — where session state is visible *in context*,
  adjacent to the work items the sessions are operating on. The two access models are
  complementary: `github.com/copilot/agents` for cross-session operational dashboarding;
  issue/project integration for per-work-item contextual monitoring.

- **Extends** `docs-github-copilot-cca-custom-properties.md` (#172, Claim 1): That
  source documents enterprise API controls for *enabling* Copilot Cloud Agent across
  organizations. This source documents the *monitoring and steering UI* for the
  resulting sessions. The enterprise rollout pattern from that source (enable CCA →
  orgs run sessions) now has a web-native management layer: team members can observe
  and guide agent sessions from within the GitHub issues and projects they are already
  managing, without needing CLI or IDE access.

- **Complements** `docs-github-copilot-vs-april-2026.md` (#475, Claim 7, Claim 8):
  That source documents cloud agent sessions launched from the Visual Studio IDE agent
  picker, with sessions creating GitHub issues and pull requests as output artifacts.
  This source provides the complementary view: once an agent session is running and
  associated with a GitHub issue, that issue page now has native session monitoring UI
  (session pill + sidebar). The VS source shows how sessions are *created* from the
  IDE; this source shows how they are *monitored from the web* once underway.

- **Complements** `docs-github-copilot-jetbrains-cli-agent-sessions.md` (#744, Claim 5):
  That source documents a unified sessions view inside the JetBrains IDE chat window
  as an in-IDE observability primitive. This source documents the web-based equivalent:
  the session pill in issue headers and the project board integration. Both serve the
  same need (aggregate agent session visibility), but from different contexts (IDE chat
  window vs. GitHub web page).

- **Novel**:
  - **GitHub issues as an agent session management surface**: No prior source in corpus
    documents the GitHub issue page (as distinct from the global
    `github.com/copilot/agents` dashboard) as a surface for monitoring and steering
    agent sessions. The session pill in the issue header is a new UI primitive that
    makes agent activity visible in the work-item context.
  - **GitHub Projects as an agent session visibility surface**: No prior source
    documents project boards as a place where agent session status is displayed
    alongside issue cards.
  - **"Session pill" as a persistent ambient session indicator**: The persistent
    header element on issues that always shows session state (active/completed at
    a glance) is a novel UX pattern not described in any other corpus source. It
    makes agent activity passively legible — no navigation required.
  - **Default-on `Show agent sessions` in Projects**: The default-on behavior for
    existing projects is the first documented default behavior change in GitHub
    Projects specifically relating to AI agent session visibility.

## Guide Impact

- **Chapter 01 (Daily Workflows)**:
  - Add the GitHub issues session pill as a practitioner UX pattern: when working
    through GitHub issues, the session pill signals whether an agent is active or
    has completed work without navigating to a separate dashboard. Practitioners
    doing issue triage now have ambient agent awareness baked into the issue list.
  - Add the project board integration: teams doing sprint reviews in GitHub Projects
    can now see active/completed agent sessions alongside their cards — a lightweight
    monitoring touchpoint that requires no additional tooling.

- **Chapter 02 (Harness Engineering)**:
  - Add issues and projects to the agent session surface inventory. A complete
    multi-surface monitoring strategy as of April 2026 has four web-accessible
    surfaces: `github.com/copilot/agents` (global), mobile (GitHub app), issue pages
    (per-issue contextual), and project boards (per-project contextual). The guide
    should map use cases to surfaces: use `github.com/copilot/agents` for operational
    dashboarding across all sessions; use issue pages for contextual review during
    triage; use project boards during sprint review.

- **Chapter 04 (Agentic Workflows)**:
  - When documenting cloud agent workflows that operate on GitHub issues, note that
    the issue page now shows session state natively via the session pill. Teams using
    "assign CCA to issue" patterns (e.g., via the CCA custom properties API) should
    expect team members to find and manage agent sessions from the issue page itself,
    not just from the CLI, IDE, or global agents dashboard.

- **Chapter 05 (Team Adoption)**:
  - Document the `Show agent sessions` default-on behavior change for GitHub Projects.
    Teams should evaluate whether this default is appropriate for their project views
    before rolling out to non-technical stakeholders who may encounter agent session
    entries in sprint boards unexpectedly.

## Extraction Notes

1. **Source is very short** (~200 words, "1 minute read"): All substantive claims
   are exhausted in the six claims above. The source is deliberately brief — a
   product changelog announcement with minimal technical detail.
2. **"Steer" is unspecified**: The changelog uses the word "steer" without defining
   what steering actions are available in the sidebar. Based on
   `docs-github-copilot-cli-remote-control-ga.md` (Claim 2), steering likely includes
   sending messages and queuing instructions, but this is inferred from that source,
   not stated in this one. Claim 3 reflects only what this changelog actually says.
3. **Three WebFetch calls made**: The page was fetched three times to capture verbatim
   quotes. All fetches returned consistent body text. Quotes in this note are
   character-for-character from the fetched content.
4. **Cloud-agent-only scope is likely but unconfirmed**: The changelog context (copilot
   tag, "cloud agent sessions" framing) implies these surfaces cover CCA sessions, not
   local Copilot CLI sessions. The CLI remote control source separately documents CLI
   sessions appearing at `github.com/copilot/agents`. Whether CLI sessions also appear
   in the issue/project session pill is not confirmed by this changelog.
5. **No contradictions found**: No existing source note claims that GitHub issues lack
   agent session integration or that project boards do not show agent activity. This
   source is purely additive. No contradiction issue filed.
