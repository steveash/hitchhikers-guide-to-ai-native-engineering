---
source_url: https://github.blog/changelog/2026-05-18-remote-control-for-copilot-cli-sessions-now-generally-available-on-mobile-web-and-vs-code
source_type: docs
title: "Remote control for Copilot CLI sessions now generally available on mobile, web, and VS Code"
author: GitHub (official changelog)
date_published: 2026-05-18
date_extracted: 2026-05-19
last_checked: 2026-05-19
status: current
confidence_overall: settled
issue: "#805"
---

# Remote Control for Copilot CLI Sessions Now Generally Available on Mobile, Web, and VS Code

> GitHub's May 2026 GA announcement of remote control for Copilot CLI sessions confirms
> the multi-platform async-agent workflow pattern in production: a CLI session started on
> a desktop terminal can now be monitored, steered, and approved from mobile, github.com,
> VS Code, or JetBrains — with a concrete administrative gate (Business/Enterprise) and
> a `/keep-alive` operational primitive for long-running sessions.

## Source Context

- **Type**: docs (GitHub official product changelog, May 18, 2026; approximately 300 words)
- **Author credibility**: GitHub engineering team announcing a production GA release. Authoritative
  for the fact that remote control is now generally available, which platforms are supported, what
  interactions remote control enables, the CLI commands and VS Code settings, and the administrative
  requirements. Not a credible source for: session latency or reliability data, how remote control
  interacts with model selection or rate limits, how well the permission approval UI works in
  practice, or what happens to a remote session if the mobile client disconnects.
- **Scope**: General availability of remote control for Copilot CLI sessions, covering supported
  platforms (mobile, github.com, VS Code, JetBrains), the six interaction capabilities, CLI/VS Code
  setup commands, the `/keep-alive` operational primitive, session visibility at
  github.com/copilot/agents, and the administrative enablement requirement for Business/Enterprise
  users. Also announces expanded support for non-GitHub repositories. Does NOT cover: how remote
  control interacts with auto model selection (see `docs-github-copilot-cli-auto-model-selection`),
  cost implications of remote sessions, session state recovery after disconnect, or how the
  permission approval flow differs from the local interactive flow.

## Extracted Claims

### Claim 1: Remote control for Copilot CLI sessions is now generally available across mobile, github.com, VS Code, and JetBrains — expanding beyond the prior limited release

- **Evidence**: Official GitHub product changelog explicitly announcing "generally available."
  The prior limited release supported mobile and github.com; VS Code and JetBrains are named as
  new additions in this GA announcement.
- **Confidence**: settled (product fact — GA stated in official changelog)
- **Quote**: "start work in your terminal and keep it moving from anywhere"
- **Our assessment**: This is the first confirmed GA remote-control-for-CLI feature in our corpus.
  Claude Code's analogous "Bridge" feature (documented in `blog-ccunpacked-claude-code-architecture`,
  Claim 15) remains unreleased as of the same date. GitHub has shipped this pattern before
  Anthropic. The multi-platform scope (four surfaces: mobile, web, VS Code, JetBrains) signals
  this is not a convenience UX feature but a first-class multi-environment workflow capability.

### Claim 2: Remote control enables six specific async interactions: track progress live, steer or queue messages, review/tweak plans, stop sessions, approve/deny permissions, and respond to questions

- **Evidence**: Official changelog enumerates the six capabilities as a bullet list. These are
  distinct interaction types: two are monitoring (track, steer/queue), one is pre-execution review
  (review/tweak plans), and three are control-plane operations (stop, approve/deny permissions,
  respond).
- **Confidence**: settled (capabilities enumerated in official changelog)
- **Quote**: "Track session progress live while you're away from your desk"
- **Our assessment**: The permission approval capability is the most significant for harness
  engineering: it means a long-running CLI agent that hits an interactive permission prompt
  does not halt permanently when the operator is away from the terminal — they can approve
  remotely. The "review and tweak plans before Copilot starts implementing" capability maps
  directly to the human-in-the-loop gate that guides like Osmani's recommend — remote control
  formalizes this gate as a product feature, not a workaround.

### Claim 3: CLI remote sessions are enabled at launch with the `copilot --remote` flag, or toggled mid-session with `/remote on`

- **Evidence**: Official changelog documents both paths: a start-time flag and a mid-session
  command. Changelog also instructs: "Run `/update` to make sure you're on the latest version"
  as a prerequisite.
- **Confidence**: settled (CLI syntax documented in official changelog)
- **Quote**: (no single verbatim quote for the full command syntax; both forms stated in
  changelog; see Concrete Artifacts)
- **Our assessment**: The mid-session `/remote on` toggle is operationally important: it means
  practitioners do not need to decide at session start whether they want remote visibility.
  A session that starts as a local interactive session can be made remotely observable later
  without restarting. The `/update` prerequisite implies the remote control feature was not
  available in earlier Copilot CLI versions — teams must keep the CLI updated to access GA
  functionality.

### Claim 4: The `/keep-alive` command prevents machine sleep during long-running remote CLI sessions

- **Evidence**: Official changelog recommends this command explicitly for remote use cases:
  practitioners using remote control are by definition away from the terminal, which means
  default OS sleep/screensaver behavior could interrupt the CLI session.
- **Confidence**: settled (command recommended in official changelog)
- **Quote**: "`/keep-alive` to help keep your machine awake"
- **Our assessment**: This is a small but operationally significant primitive. Without `/keep-alive`,
  a developer who starts a long CLI session and leaves their desk risks the machine sleeping mid-task,
  interrupting the session before the remote user can act. For harness engineering: any automated
  or unattended Copilot CLI workflow should invoke `/keep-alive` if the session may run longer
  than the default OS screen timeout. This is the kind of operational detail that practitioners
  discover through failure rather than documentation — the guide should surface it proactively.

### Claim 5: VS Code integration requires enabling the `github.copilot.chat.cli.remote.enabled` setting and entering `/remote on` in the Chat view

- **Evidence**: Official changelog documents both configuration steps as prerequisites for VS Code
  remote control. The setting name is exact; the `/remote on` command is entered in the Chat
  input, not the terminal.
- **Confidence**: settled (VS Code setup documented in official changelog)
- **Quote**: "Enable the `github.copilot.chat.cli.remote.enabled` setting"
- **Our assessment**: The VS Code path is distinct from the pure CLI path: it routes through the
  Copilot Chat view rather than the terminal. This means VS Code users get remote control
  integrated into their editor UI rather than as a separate terminal session — a lower-friction
  entry point for practitioners who primarily work in VS Code rather than a standalone terminal.
  The separate `github.copilot.chat.cli.remote.enabled` setting signals this is opt-in by default,
  consistent with the administrative gate (Claim 7).

### Claim 6: Remote sessions are visible on github.com/copilot/agents — not only in a specific repository's Agents tab

- **Evidence**: Official changelog specifies that remote sessions appear at github.com/copilot/agents
  (a global agents page), expanding beyond the prior per-repository Agents tab. For non-GitHub
  repositories, the global page is the only visibility surface since there is no associated repository
  Agents tab.
- **Confidence**: settled (page URL stated in official changelog)
- **Quote**: (no direct quote for the exact URL; inferred from changelog context about non-GitHub
  repo support)
- **Our assessment**: The global agents page (github.com/copilot/agents) is a new visibility
  surface that aggregates all remote sessions regardless of repository association. For teams
  with multiple concurrent CLI sessions or practitioners working across multiple repos simultaneously,
  this page becomes the operational dashboard. The fact that it works for non-GitHub directories
  removes a prior constraint that limited remote control to GitHub-hosted repositories.

### Claim 7: Copilot Business and Enterprise users require administrator enablement of remote control and CLI policies before the feature is accessible

- **Evidence**: Official changelog states this explicitly as an administrative prerequisite. The
  pattern is consistent with how GitHub has gated other Business/Enterprise CLI features (see
  `docs-github-copilot-cli-auto-model-selection`, Claim 7: auto model selection also honors
  administrator model settings).
- **Confidence**: settled (administrative requirement stated definitively in official changelog)
- **Quote**: "If you're a Copilot Business or Copilot Enterprise user, an administrator will have
  to enable remote control and CLI policies before you can use it."
- **Our assessment**: Individual/free-tier Copilot users can use remote control without admin
  action. Business/Enterprise users need admin approval — a two-step adoption path for team
  environments. This is the same governance pattern documented across multiple Copilot changelog
  entries: new capabilities are available to all plan tiers, but Business/Enterprise tiers layer
  in admin control as a governance primitive. For enterprise practitioners: remote control
  requires two separate policy enablements (remote control AND CLI policies), not just one flag.
  This suggests independent policy surfaces — an admin who wants to enable remote control but
  restrict the CLI more broadly may need to manage these separately.

### Claim 8: The GA release adds support for non-GitHub repositories and directories not associated with any repository

- **Evidence**: Official changelog identifies this as an expansion of scope in the GA release,
  implying prior remote control was limited to GitHub-hosted repositories.
- **Confidence**: settled (stated as a new capability in the GA announcement)
- **Quote**: "non-GitHub repositories and directories not associated with a repository"
- **Our assessment**: This expansion is significant for practitioners who use Copilot CLI for
  local development outside a GitHub repository context (e.g., local monorepos, private
  non-GitHub repos, or bare directories). Remote control is no longer a GitHub-only feature — any
  Copilot CLI session can now be remotely monitored. For teams that use GitHub Copilot on
  non-GitHub infrastructure (e.g., GitLab, Bitbucket, or purely local work), this removes a
  prior architectural barrier.

## Concrete Artifacts

### CLI Setup Commands for Remote Control

```
# Prerequisites
/update          — update Copilot CLI to the latest version (required)

# Start a new session with remote control enabled
copilot --remote

# Enable remote control in an existing session
/remote on

# Keep machine awake during long remote sessions
/keep-alive

# Where sessions appear:
# - Repository Agents tab (for GitHub repos)
# - github.com/copilot/agents (global; works for non-GitHub repos too)
```

### VS Code Setup for Remote Control

```
# Step 1: Enable the setting in VS Code
github.copilot.chat.cli.remote.enabled = true

# Step 2: Enter in the Chat view input
/remote on

# Result: generates a linked task page for remote monitoring
```

### Supported Remote Control Platforms (GA, May 2026)

```
Platform                 Status
─────────────────────────────────
GitHub Mobile (iOS/Android)  GA (previously available)
github.com web               GA (previously available)
VS Code                      GA (new in this release)
JetBrains IDEs               GA (new in this release)
```

### Remote Control Capabilities

```
Interaction Type   Capability
─────────────────────────────────────────────────────────────────
Monitor            Track session progress live while away from desk
Async steer        Steer mid-session, or queue the next message
Plan review        Review and tweak plans before implementation starts
Control            Stop a session at any time
Permission gate    Approve or deny permission requests remotely
Q&A                Respond to Copilot's questions when it needs input
```

### Administrative Requirements

```
Copilot Plan        Admin Required?   What Admins Must Enable
─────────────────────────────────────────────────────────────
Individual/Free     No                (available immediately)
Pro/Pro+            No                (available immediately)
Copilot Business    Yes               remote control policy + CLI policies
Copilot Enterprise  Yes               remote control policy + CLI policies
```

## Cross-References

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` (Claim 7): That source
  documents that auto model selection in the Copilot CLI honors all administrator model settings.
  This source adds remote control to the list of Copilot CLI features gated behind admin policy
  for Business/Enterprise users. Together, both sources evidence GitHub's consistent pattern:
  new CLI capabilities are broadly available to individual-tier users but wrapped in admin policy
  controls for Business/Enterprise. The governance model is the same across features.

- **Extends** `blog-ccunpacked-claude-code-architecture.md` (Claim 15): That source documents
  "Bridge" — Claude Code's unreleased remote control feature (WebSocket + JWT auth + permission
  approval UI). This source provides the first **GA production instance** of the remote-control-
  for-CLI pattern in our corpus. Copilot CLI's remote control has shipped (May 2026); Claude Code's
  Bridge remains unreleased as of the same date. For the guide: the Bridge feature is no longer
  a novel concept — practitioners can now point to a live production implementation of the same
  pattern. The permission approval UI described for Bridge maps directly to the "Approve or deny
  permission requests" capability in this source.

- **Extends** `docs-github-copilot-cca-rest-api-tasks.md` (issue #734): That source documents
  programmatic invocation of Copilot Cloud Agent tasks via REST API. This source adds a distinct
  but complementary remote interaction model: while the REST API enables programmatic *starting*
  of CCA tasks, remote control enables human *steering* of Copilot CLI sessions after they start.
  Together they show GitHub building two separate remote interaction primitives for two different
  use cases: automated batch orchestration (REST API) vs. human-in-the-loop async oversight
  (remote control).

- **Extends** `docs-github-copilot-agent-skills-cli.md` (Claim 1): That source established the
  Copilot CLI as a primary surface for new GitHub agent feature development. This source confirms
  the pattern: remote control ships on the CLI surface first, with mobile/web/VS Code as monitoring
  clients, not as primary execution surfaces. The CLI remains the execution engine; the other
  platforms are observation/control surfaces.

- **Novel**:
  - First corpus source to document CLI session remote control as a **GA feature** in a production
    AI coding tool. Prior corpus sources treated remote control as a future/unreleased pattern
    (Claude Code's Bridge) or as a workaround (tmux + Slack bots for async approval gates).
  - First documentation of `/keep-alive` as a practitioner operational primitive for long-running
    unattended CLI sessions.
  - First documentation of github.com/copilot/agents as a centralized session dashboard spanning
    repositories and non-repository directories.
  - First confirmation that remote control works for non-GitHub repositories — removing a prior
    architectural constraint that limited async CLI workflows to GitHub-hosted codebases.
  - First documentation of the two-policy admin requirement (remote control policy AND CLI policies
    separately) for Business/Enterprise users, suggesting a more granular admin control surface
    than a single "enable remote" toggle.

## Guide Impact

### Chapter 01: Daily Workflows

- **Async agent workflow pattern**: Remote control formalizes a workflow practitioners currently
  achieve via workarounds (tmux sessions, screen multiplexers, Slack webhook bots). Add a pattern:
  "start a CLI task, enable `/remote on`, switch to mobile or VS Code to monitor and steer." The
  `/keep-alive` command should be mentioned as required for any task expected to run longer than
  the machine's default screen timeout.
- **Plan review gate**: The "review and tweak plans before Copilot starts implementing" capability
  aligns with best-practice recommendations in the guide (verify before execute). Practitioners
  who start sessions remotely can now use plan review as a mobile approval step — this reduces
  the friction of the review-before-execute pattern for async workflows.

### Chapter 02: Harness Engineering

- **Tooling configuration**: Add `copilot --remote` and `github.copilot.chat.cli.remote.enabled`
  to the CLI configuration reference. Document `/keep-alive` as a required command for unattended
  or long-running sessions. Reference github.com/copilot/agents as the session visibility surface.
- **Permission handling**: The remote permission approval capability changes the harness design
  consideration for interactive permission prompts: previously, an unattended agent that hit a
  permission prompt would block until a human returned to the terminal; with remote control
  enabled, the same prompt can be approved from a phone. Guide advice around "avoid permission
  prompts in automated flows" should now distinguish between truly unattended headless sessions
  (where prompts still block) and remotely-supervised sessions (where prompts can be handled
  asynchronously).
- **Bridge pattern confirmed**: Claude Code's unreleased Bridge feature (`blog-ccunpacked-claude-
  code-architecture.md`, Claim 15) is no longer a purely speculative future pattern — GitHub has
  shipped an equivalent today. Update any forward-looking Bridge references to note that
  Copilot CLI's GA remote control is the live reference implementation of the pattern.

### Chapter 05: Enterprise Governance

- **Admin policy surface**: Add a note that remote control requires two separate admin enablements
  (remote control policy + CLI policies) for Business/Enterprise users. Teams planning to adopt
  remote CLI workflows should confirm both policies are enabled before testing — enabling only one
  may produce confusing partial functionality.
- **Remote control as a governance consideration**: Unlike CCA tasks (which run in GitHub's cloud
  infrastructure), Copilot CLI runs on the developer's machine. Remote control extends the
  governance surface: an admin enabling CLI remote control is also enabling the operator's machine
  to receive steering from any device the developer can access. For enterprises with strict
  endpoint security policies, the interaction between remote control and MDM/endpoint controls
  deserves evaluation.

## Extraction Notes

1. **Source is a short changelog (~300 words)**: All substantive claims are exhausted in the eight
   claims above. The source is deliberately brief; it does not cover implementation details,
   session state management, or latency characteristics of the remote control connection.
2. **Verbatim quotes confirmed across two fetches**: The specific bullet points and command syntax
   were cross-verified across two WebFetch calls to the same URL. The quote "If you're a Copilot
   Business or Copilot Enterprise user, an administrator will have to enable remote control and
   CLI policies before you can use it." is verbatim from the changelog.
3. **JetBrains mentioned but underspecified**: The changelog names JetBrains as a supported
   platform but provides no setup instructions equivalent to the VS Code section. The JetBrains
   integration may require a separate extension or plugin not described in this changelog.
4. **QR code flow not confirmed**: The initial triage summary mentioned a QR code scan step,
   but this was not present in the verbatim content extracted. It may have appeared in a prior
   beta version of the feature or in supplemental documentation not captured in this changelog.
5. **No contradictions to file**: Bridge (Claude Code's unreleased remote control) and Copilot
   CLI's GA remote control describe the same architectural pattern from different vendors at
   different release states. This is not a contradiction — it is a corroboration with different
   GA timelines.
