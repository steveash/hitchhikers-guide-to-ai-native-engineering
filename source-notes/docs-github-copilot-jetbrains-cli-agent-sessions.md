---
source_url: https://github.blog/changelog/2026-05-13-introducing-copilot-cli-agent-and-unified-sessions-view-in-github-copilot-for-jetbrains-ides
source_type: docs
title: "Introducing Copilot CLI agent and unified sessions view in GitHub Copilot for JetBrains IDEs"
author: GitHub (official changelog)
date_published: 2026-05-13
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#744"
---

# Introducing Copilot CLI agent and unified sessions view in GitHub Copilot for JetBrains IDEs

> GitHub's May 2026 JetBrains changelog introduces two novel practitioner patterns:
> user-selectable isolation modes (worktree vs. workspace) for agent-driven work as a
> first-class IDE UX control, and a unified sessions view as an observability primitive
> for tracking all concurrent agent sessions — plus a global `.agent.md` configuration
> path and a cross-mode Ask question tool that round out the agent interaction model.

## Source Context

- **Type**: docs (GitHub official product changelog, May 13, 2026)
- **Author credibility**: GitHub engineering team announcing a production feature in JetBrains
  IDEs. Authoritative for the fact that these capabilities exist, the exact directory paths and
  CLI flags documented, and the behavioral changes (plan agent no longer auto-invoked, Edit mode
  removed). Not a credible source for: how well the CLI agent performs in practice, whether the
  worktree isolation mode introduces friction compared to workspace isolation, or how the unified
  sessions view scales with many concurrent sessions.
- **Scope**: Five features in the May 2026 JetBrains Copilot update — the CLI agent in JetBrains
  with worktree/workspace isolation modes, the unified sessions view, the Ask question tool,
  global `.agent.md` configuration, and GHES sign-in support. Also covers UX improvements,
  reliability fixes, a behavioral change (plan agent), and a deprecation (Edit mode removal).
  Does NOT cover: model selection for the JetBrains CLI agent, how the CLI agent interacts
  with skills installed via `gh skill`, cost implications of CLI agent sessions, or how
  JetBrains CLI agent sessions relate to the remote control sessions documented in
  `docs-github-copilot-cli-remote-control-ga.md`.

## Extracted Claims

### Claim 1: The Copilot CLI agent can now be delegated to from JetBrains IDEs in public preview, with editor context already connected to the locally running CLI

- **Evidence**: Official GitHub product changelog. The feature is described as public preview
  with the CLI running locally on the developer's machine. "Editor context already connected"
  implies the IDE passes open file state and repo context to the CLI agent automatically.
- **Confidence**: emerging (product fact — the feature exists; public preview designation
  means behavior may change before GA)
- **Quote**: "You can now delegate tasks from JetBrains IDEs to a locally running GitHub
  Copilot CLI agent in public preview."
- **Our assessment**: This is the JetBrains complement to what the remote control source
  (`docs-github-copilot-cli-remote-control-ga.md`, Claim 1) documented for VS Code. That
  source added JetBrains as a remote *monitoring* surface for existing CLI sessions; this source
  adds JetBrains as a *launch* surface for new CLI agent sessions. Together they create a full
  loop for JetBrains practitioners: launch a task from within the IDE, monitor it remotely if
  needed. The "locally running" qualifier is significant — unlike Copilot Cloud Agent (CCA),
  which runs on GitHub's remote infrastructure, the CLI agent runs on the developer's machine,
  meaning the agent has access to local state not available to cloud agents.

### Claim 2: Worktree isolation mode runs the agent in a separate Git worktree, keeping changes isolated from the current branch until the practitioner explicitly chooses to review and apply them

- **Evidence**: Official changelog documents the worktree isolation mode with its behavioral
  guarantee. This is a safety pattern: the agent can take actions that modify files without
  immediately affecting the developer's active working tree.
- **Confidence**: emerging (official claim; public preview status means the implementation
  may evolve)
- **Quote**: "runs the agent in a separate Git worktree, so changes don't affect your current
  branch until you choose to review and apply them."
- **Our assessment**: This is the most significant pattern in the source for harness engineering.
  Worktree isolation provides a human review gate at the filesystem level — the agent can't
  accidentally break the current branch. The pattern maps to the broader "verify before merge"
  principle recommended in agentic workflow literature: the agent does the work in an isolated
  context; the human reviews the delta before it lands. For Ch02: document worktree isolation
  as the recommended mode when the agent is performing writes that could break the current
  development environment (e.g., refactors, file deletions, dependency updates). The cost is
  a merge/apply step; the benefit is recoverability. This is functionally analogous to the
  worktree isolation described in the third triage comment — it is confirmed verbatim here.

### Claim 3: Workspace isolation mode applies changes directly to the current workspace for faster iteration when isolation overhead is not required

- **Evidence**: Official changelog documents workspace isolation as the complement to worktree
  isolation. The tradeoff is explicit: speed vs. safety.
- **Confidence**: emerging (official claim; public preview status applies)
- **Quote**: "applies changes directly to your current workspace, allowing for faster iteration
  when isolation isn't required."
- **Our assessment**: Workspace isolation is the appropriate default when the risk of the
  agent's changes is low (e.g., adding tests, updating docs, formatting) or when the
  practitioner wants tight feedback loops where reviewing a separate worktree would introduce
  friction. The existence of two explicit modes — rather than a single default — signals that
  GitHub recognizes the safety/speed tradeoff as a practitioner decision point, not a product
  default. For the guide: frame the choice as "isolation mode = risk level of the task."
  High-risk tasks (file deletions, API surface changes) → worktree. Low-risk tasks (doc
  updates, test additions) → workspace. This is the first source in corpus to document
  this isolation mode toggle as a user-facing control.

### Claim 4: Copilot Business and Enterprise users must have the "Editor preview features" policy enabled by an administrator before they can use the CLI agent in JetBrains

- **Evidence**: Official changelog: "Note: If you are a Copilot Business or Copilot Enterprise
  subscriber, an administrator will have to enable the Editor preview features policy before
  you can use this feature."
- **Confidence**: settled (access requirement stated directly in official changelog)
- **Quote**: "If you are a Copilot Business or Copilot Enterprise subscriber, an administrator
  will have to enable the Editor preview features policy before you can use this feature."
- **Our assessment**: This is the same admin-policy-gate pattern documented across multiple
  Copilot features: new capabilities are broadly available to individual-tier users but require
  explicit admin enablement for Business/Enterprise. The specific policy name ("Editor preview
  features") is notable — it suggests GitHub is bundling experimental IDE features under a
  single admin toggle, which means enabling or disabling it affects multiple features, not just
  the CLI agent. Enterprise practitioners who want selective feature rollouts should be aware
  that this is a bundle policy, not a per-feature gate. Corroborates the admin governance
  pattern in `docs-github-copilot-cli-auto-model-selection.md` (Claim 7) and
  `docs-github-copilot-cli-remote-control-ga.md` (Claim 7).

### Claim 5: A unified sessions view in the chat window aggregates all agent sessions in one place, showing title, agent type, elapsed time, and status for each session

- **Evidence**: Official changelog describes the unified sessions view as a new feature
  providing filterable session tracking across all agent types and sessions.
- **Confidence**: emerging (official claim; public preview context)
- **Quote**: "The chat window now includes a unified sessions view, making it easier to track
  all agent sessions in one place."
- **Our assessment**: This is the first documented IDE-level observability primitive for
  concurrent agent session management in our corpus. As practitioners run more agent sessions
  simultaneously (agent mode, sub-agents, CLI agent, custom agents), the question "what is
  currently running?" becomes non-trivial. The unified sessions view answers it with a
  structured display: title, agent type, elapsed time, status. The filtering capability (by
  agent type or status) adds operational utility for practitioners debugging a specific session
  or tracking which sessions have completed vs. are still running. For Ch04: document this
  as a practitioner observability pattern — the IDE is surfacing agent runtime state that was
  previously invisible or required terminal monitoring to track.

### Claim 6: Each session in the unified sessions view shows title, agent type, elapsed time, and status — and can be filtered by agent type or status

- **Evidence**: Official changelog: "Each session shows its title, agent type, elapsed time,
  and status. You can also filter sessions by agent type or status to quickly find what
  you're looking for."
- **Confidence**: emerging (official claim)
- **Quote**: "Each session shows its title, agent type, elapsed time, and status."
- **Our assessment**: The four fields (title, agent type, elapsed time, status) constitute
  a minimal operational dashboard for agent work. "Elapsed time" is particularly relevant for
  practitioners tracking whether a long-running task is progressing or has stalled; "status"
  is the completion gate. The filter by agent type enables practitioners who run many
  concurrent sessions to isolate "show me only Copilot CLI agent sessions" or "show me only
  failed sessions." For practitioners designing multi-agent workflows: this view is evidence
  that GitHub expects practitioners to have multiple concurrent agent sessions in JetBrains
  — the UX investment in a filterable aggregated view would not make sense for single-session
  use patterns.

### Claim 7: The Ask question tool enables agents to ask focused clarifying questions when additional information is needed — and is supported across agent mode, custom agents, sub-agents, and Copilot CLI agent, but not Ask mode

- **Evidence**: Official changelog explicitly enumerates supported and unsupported modes.
  The exclusion of "Ask mode" is explicitly stated in the source.
- **Confidence**: emerging (official claim; public preview context)
- **Quote**: "Agent mode now includes an Ask question tool, enabling agents to ask focused
  clarifying questions when additional information is needed."
- **Our assessment**: The Ask question tool operationalizes human-in-the-loop disambiguation:
  when an agent lacks sufficient context to proceed safely, it can surface a targeted question
  rather than making an assumption. The cross-mode support (agent, custom, sub, CLI) is
  broad — this is a capability available everywhere the agent is autonomous. The deliberate
  exclusion from Ask mode is consistent: Ask mode is conversational (the human is already
  asking), so the tool would be redundant there. For Ch02 (agent design): the Ask question
  tool reduces the cost of ambiguous task specifications — practitioners can write broader
  initial prompts and let the agent surface what it needs, rather than front-loading all
  context in the original instruction. This shifts the interaction model from "fully specify
  upfront" to "specify broadly and answer follow-ups."

### Claim 8: Custom agents can be defined globally using `.agent.md` files in `~/.copilot/agents/`, making them available across all workspaces without per-project configuration

- **Evidence**: Official changelog: "You can now define custom agents at the global level
  using the `.agent.md` file under `~/.copilot/agents`, making them available across all
  your workspaces."
- **Confidence**: settled (file path and scope stated definitively in official changelog)
- **Quote**: "You can now define custom agents at the global level using the `.agent.md` file
  under `~/.copilot/agents`, making them available across all your workspaces."
- **Our assessment**: This introduces a user-scope custom agent configuration path for
  JetBrains that complements the project-scope `.github/agents/` directory documented in
  `docs-ghaw-copilot-agent-files.md`. The `~/.copilot/agents` path travels with the developer's
  machine configuration, not with any repository — it is the equivalent of what VS April 2026
  (`docs-github-copilot-vs-april-2026.md`, Claim 5) introduced for Visual Studio at
  `%USERPROFILE%/.github/agents/`. Note the difference in path conventions: VS uses the
  `.github` namespace even at user scope; JetBrains uses `.copilot/agents` at user scope.
  Two different paths, same pattern. For Ch02: practitioners who want personal productivity
  agents (e.g., a "context summarizer" or "commit message generator" agent that they use
  across all projects) should use the global path. Agents that encode project-specific
  knowledge should stay in `.github/agents/`. The governance implication is the same as
  noted in the VS source: user-scope agents are outside enterprise admin policy controls.

### Claim 9: The plan agent is no longer auto-invoked in sub-agent workflows — it must now be explicitly triggered

- **Evidence**: Official changelog under "Changed": "The plan agent is no longer auto-invoked
  in sub-agent workflows."
- **Confidence**: settled (behavioral change stated definitively)
- **Quote**: "The plan agent is no longer auto-invoked in sub-agent workflows."
- **Our assessment**: This is a breaking change for practitioners who relied on the plan agent
  being automatically triggered in sub-agent workflows. The plan agent presumably generated a
  plan before the sub-agent executed tasks — removing auto-invocation shifts the responsibility
  to the practitioner (or the parent agent) to explicitly invoke planning when needed. Without
  explicit invocation, sub-agent workflows now proceed directly to execution, which may be
  faster but skips the planning step. For Ch04: document this behavioral change and update
  any patterns that assumed the plan agent would auto-invoke in sub-agent contexts. Teams
  using JetBrains Copilot sub-agent workflows should audit their workflows to determine whether
  they relied on plan agent auto-invocation and whether explicit invocation is now needed.

### Claim 10: Edit mode support has been removed from GitHub Copilot for JetBrains

- **Evidence**: Official changelog under "Deprecation": "Edit mode support has been removed."
- **Confidence**: settled (stated definitively in changelog)
- **Quote**: "Edit mode support has been removed."
- **Our assessment**: The removal of Edit mode without explanation in the changelog suggests it
  was superseded by agent mode (which provides similar capabilities with more control) or was
  too low-usage to maintain. The omission of an explicit migration path in the changelog implies
  users should move to agent mode with workspace isolation (Claim 3) as the functional
  equivalent — direct workspace edits in agent mode with workspace isolation replicates
  what Edit mode provided. For any guide section that referenced Edit mode as a JetBrains
  Copilot interaction model: remove or update.

## Concrete Artifacts

### CLI Agent Isolation Modes

```
GitHub Copilot CLI Agent — JetBrains IDE (Public Preview, May 2026)

Isolation Modes:

WORKTREE (safe, slower):
  - Agent runs in a separate Git worktree
  - Changes do NOT affect the current branch
  - Practitioner reviews and applies changes explicitly
  - Best for: high-risk tasks (refactors, deletions, API changes)

WORKSPACE (fast, direct):
  - Agent applies changes directly to the current workspace
  - No intermediate review step
  - Best for: low-risk tasks (docs, tests, formatting)

Administrative requirement:
  - Copilot Business/Enterprise: requires admin to enable
    "Editor preview features" policy before use
  - Individual tiers: available without admin action
```

*Source: Introducing Copilot CLI agent and unified sessions view, May 13, 2026*

### Unified Sessions View — Session Fields and Filtering

```
Unified Sessions View (JetBrains Copilot Chat Window)

Per session displayed:
  - Title
  - Agent type
  - Elapsed time
  - Status

Filter by:
  - Agent type
  - Status

Scope: All agent sessions in one place
(agent mode, custom agents, sub-agents, Copilot CLI agent)
```

*Source: Introducing Copilot CLI agent and unified sessions view, May 13, 2026*

### Ask Question Tool — Mode Support Matrix

```
Ask Question Tool Availability (May 2026):

Agent mode:          ✓ supported
Custom agents:       ✓ supported
Sub-agents:          ✓ supported
Copilot CLI agent:   ✓ supported
Ask mode:            ✗ NOT supported (conversational mode — tool is redundant)
```

*Source: Introducing Copilot CLI agent and unified sessions view, May 13, 2026*

### Global Agent Configuration Path (JetBrains)

```
User-scope custom agent definition (JetBrains):
  ~/.copilot/agents/<agent-name>.agent.md

Characteristics:
  - Available across ALL workspaces (not project-specific)
  - Not version-controlled (outside any repository)
  - Not subject to enterprise admin policy controls (inferred)
  - Complement to project-scope: .github/agents/ (project-specific)

Compare:
  Visual Studio (April 2026): %USERPROFILE%/.github/agents/
  JetBrains (May 2026):       ~/.copilot/agents/
  (Same user-scope concept, different directory conventions per IDE)
```

*Source: Introducing Copilot CLI agent and unified sessions view, May 13, 2026*

### Changed / Removed Behaviors

```
Behavioral change (May 2026):
  Plan agent: no longer auto-invoked in sub-agent workflows
  → Must now be explicitly triggered if planning is required

Deprecation (May 2026):
  Edit mode: support has been removed
  → Functional equivalent: agent mode with workspace isolation
```

*Source: Introducing Copilot CLI agent and unified sessions view, May 13, 2026*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-cli-remote-control-ga.md` (Claim 1, Claim 7): The remote
    control GA source established JetBrains as a remote monitoring surface for CLI sessions,
    with the same admin policy gate (Business/Enterprise require admin enablement). This source
    adds the CLI agent launch capability from JetBrains, completing the loop: launch from
    JetBrains (this source), monitor/steer from JetBrains (remote control source). Both feature
    the same admin policy pattern for Business/Enterprise users.
  - `docs-github-copilot-cli-auto-model-selection.md` (Claim 7): The admin governance
    pattern is consistent — new Copilot CLI capabilities require admin enablement for
    Business/Enterprise users. The "Editor preview features" policy here is a different
    gate name than the auto model selection policy but reflects the same governance structure.
  - `docs-github-copilot-vs-april-2026.md` (Claim 5): Both this source (JetBrains,
    `~/.copilot/agents`) and the VS April 2026 source (Visual Studio, `%USERPROFILE%/.github/agents/`)
    introduce user-scope custom agent configuration paths that travel across projects. The
    pattern is identical; the paths differ by IDE convention.

- **Extends**:
  - `docs-github-copilot-vs-april-2026.md` (Claim 5, Claim 6): The VS source introduced
    user-level agent definitions as a new governance gap (user-scope agents outside enterprise
    policy controls). This source extends that finding to JetBrains — the same governance gap
    exists at `~/.copilot/agents`. Together the two sources confirm that GitHub's user-scope
    agent config model is IDE-agnostic in pattern, even if the paths differ. Enterprise AI
    policies that address the VS gap should also address the JetBrains path.
  - `docs-ghaw-copilot-agent-files.md` (Claim 1, Claim 8): That source documents the
    project-scope custom agent file model (`.github/agents/` with organization-level library
    patterns). This source adds the user-scope tier (`~/.copilot/agents`). The full agent
    configuration scope model now has: user-level (`~/.copilot/agents`), project-level
    (`.github/agents/`), and organization-level (shared library via remote `@ref` imports).
  - `docs-github-copilot-agent-skills-cli.md` (Claim 1): That source established the
    Copilot CLI as a growing feature surface for agent capabilities. This source adds the
    JetBrains IDE integration as another CLI feature surface, extending the pattern that the
    Copilot CLI is GitHub's primary execution layer for agent work (running locally on the
    developer's machine) with IDEs as dispatch and monitoring surfaces.

- **Contradicts**: None identified. The `~/.copilot/agents` path (JetBrains) and
  `%USERPROFILE%/.github/agents/` (Visual Studio) use different directories — this is a
  per-IDE convention difference, not a conceptual contradiction. Both provide user-scope
  custom agent config; the different paths reflect separate IDE integration implementations.
  No contradiction issue filed.

- **Novel**:
  - **Worktree vs. workspace isolation as a user-selectable IDE mode** (Claims 2, 3):
    No prior source in corpus documents isolation mode selection as an interactive user
    control in an IDE. Prior sources discuss isolation at the infrastructure level (CCA runs
    on GitHub infrastructure; gh-aw workflows run in GitHub Actions). This is the first
    documented practitioner-facing isolation toggle for local agent execution.
  - **Unified sessions view as an IDE observability primitive** (Claims 5, 6): No prior
    source documents an IDE-level aggregated view for monitoring concurrent agent sessions.
    This is the first corpus evidence that IDE vendors are building purpose-built observability
    UI for multi-session agent work management.
  - **Ask question tool scoping (all agent modes except Ask mode)** (Claim 7): The
    explicit cross-mode support matrix (supported: agent, custom, sub, CLI; not supported:
    Ask mode) is a novel behavioral specification not previously documented.
  - **Plan agent no longer auto-invoked in sub-agent workflows** (Claim 9): A behavioral
    change that practitioners with existing sub-agent workflows need to account for.
  - **Edit mode removed** (Claim 10): First corpus documentation of this deprecation.

## Guide Impact

- **Chapter 02 (Harness Engineering — Agent Configuration)**:
  - Add a "Global vs. project-scope agent configuration" section covering all documented
    user-scope paths: `~/.copilot/agents` (JetBrains), `%USERPROFILE%/.github/agents/`
    (Visual Studio). Distinguish from project-scope `.github/agents/`. Practical guidance:
    use global paths for personal productivity agents (re-used across all projects);
    use project paths for project-specific agents that should be checked in and shared.
  - Add worktree isolation vs. workspace isolation as a decision framework for CLI agent
    tasks (Claims 2, 3). The recommendation: default to worktree for any task that modifies
    existing files; workspace for additive tasks (new files, doc updates) where rollback
    complexity is low.
  - Document the "Editor preview features" policy (Claim 4) as an admin enablement
    requirement for JetBrains Copilot CLI agent access in Business/Enterprise environments.

- **Chapter 04 (Agentic Workflows)**:
  - Add the unified sessions view (Claims 5, 6) as an example of IDE-level observability
    for concurrent agent work. Practitioners running multiple agent sessions should monitor
    elapsed time and status to detect stalled sessions proactively.
  - Add the Ask question tool (Claim 7) as a human-in-the-loop disambiguation pattern:
    design agent tasks broadly and let the agent surface clarifying questions, rather than
    requiring exhaustive upfront specification. Contrast with Ask mode (not supported).
  - Update any sub-agent workflow guidance to reflect that the plan agent is no longer
    auto-invoked (Claim 9) — practitioners who want planning in sub-agent workflows must
    now trigger it explicitly.

- **Chapter 05 (Team Adoption — Enterprise Governance)**:
  - Extend the governance gap analysis from `docs-github-copilot-vs-april-2026.md` (Claim 6)
    to cover JetBrains: user-scope agents at `~/.copilot/agents` are outside enterprise policy
    controls. Organizations with strict AI governance policies should explicitly address both
    `%USERPROFILE%/.github/agents/` (Windows/VS) and `~/.copilot/agents` (JetBrains) in their
    AI usage policies, as project-scope and org-scope CCA controls do not cover these paths.

## Extraction Notes

1. **Source is a short changelog (~500 words including UX/reliability items)**: All
   substantive AI-native engineering claims are covered in the ten claims above. UX
   improvements (confirmation dialogs, sub-agent rendering, code review apply behavior,
   hover states, drag-and-drop) and reliability fixes (multi-screen code completions, keyboard
   navigation, drag-and-drop) were noted but not extracted as they carry no harness engineering
   signal.
2. **Public preview caveat throughout**: The CLI agent feature is explicitly "public preview."
   Behavioral details, isolation mode semantics, and the admin policy gate may change before GA.
   Claims 1–4 are marked "emerging" to reflect this. Claims 5–10 cover features without a
   preview qualifier (unified sessions view, Ask question tool, global agents, plan agent
   behavior, Edit mode removal) and are marked settled or emerging based on their evidence type.
3. **No sub-pages followed**: The source is a self-contained changelog entry. It does not link
   to in-depth documentation pages for the CLI agent or unified sessions view. If such docs
   exist (e.g., JetBrains plugin documentation), they would contain additional behavioral
   detail not present here. A follow-up mining of the JetBrains plugin documentation is
   recommended once the CLI agent feature reaches GA.
4. **Two WebFetch calls made**: Content was fetched twice with different prompts. The second
   fetch returned fuller verbatim quote coverage, which was used for all quote fields.
   Results were consistent between fetches.
5. **No contradictions to file**: The `~/.copilot/agents` vs. `%USERPROFILE%/.github/agents/`
   path difference is a per-IDE convention, not a claim contradiction. Both represent the same
   user-scope pattern; no existing source note claims that user-scope agents are impossible
   or use a different path in JetBrains. No contradiction issue filed.
