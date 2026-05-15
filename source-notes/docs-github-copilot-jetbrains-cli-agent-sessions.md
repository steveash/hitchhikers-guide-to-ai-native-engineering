---
source_url: https://github.blog/changelog/2026-05-13-introducing-copilot-cli-agent-and-unified-sessions-view-in-github-copilot-for-jetbrains-ides
source_type: docs
title: "Introducing Copilot CLI agent and unified sessions view in GitHub Copilot for JetBrains IDEs"
author: GitHub (official changelog)
date_published: 2026-05-13
date_extracted: 2026-05-15
last_checked: 2026-05-15
status: current
confidence_overall: emerging
issue: "#744"
---

# Introducing Copilot CLI Agent and Unified Sessions View in GitHub Copilot for JetBrains IDEs

> GitHub's May 2026 changelog for JetBrains IDEs introduces five practitioner-relevant patterns:
> worktree isolation as an explicit agent safety mode, workspace isolation as the speed
> tradeoff, global user-level agent configuration via `~/.copilot/agents`, a unified sessions
> view as an in-IDE observability primitive, and an ask question tool for agent-human
> disambiguation — providing the clearest model yet of how GitHub envisions agentic work
> managed within an IDE.

## Source Context

- **Type**: docs (GitHub official product changelog, May 13, 2026)
- **Author credibility**: GitHub engineering team announcing production features in JetBrains
  IDEs. Authoritative for feature availability, configuration paths, behavioral semantics, and
  access requirements. Not a credible source for how well these features perform in practice,
  how isolation modes compare for different task types, or whether the unified sessions view
  scales to large numbers of concurrent sessions. No empirical data on effectiveness.
- **Scope**: Six new capabilities — Copilot CLI agent in public preview (with worktree and
  workspace isolation), unified sessions view, ask question tool, global `.agent.md`
  configuration, and GHES sign-in support — plus UX improvements and two removals (edit mode,
  plan agent auto-invoke). Does NOT cover: how the JetBrains CLI agent relates to or shares
  context with the Copilot CLI agent in the terminal; performance comparisons between worktree
  and workspace isolation; cost implications of agent sessions; whether the unified sessions view
  works for sessions initiated outside the IDE; or how `~/.copilot/agents` definitions interact
  with project-level agents.

## Extracted Claims

### Claim 1: The Copilot CLI agent is now available in JetBrains IDEs in public preview, enabling developers to delegate tasks to a locally running agent without leaving the editor

- **Evidence**: Official GitHub product changelog with explicit public-preview qualifier and
  specific "locally running" description.
- **Confidence**: settled (product fact — feature exists and is documented, qualified as public
  preview)
- **Quote**: "You can now delegate tasks from JetBrains IDEs to a locally running GitHub Copilot
  CLI agent in public preview."
- **Our assessment**: "Locally running" is the key qualifier — this is distinct from the CCA
  cloud agent dispatched from Visual Studio (`docs-github-copilot-vs-april-2026.md` Claim 7).
  The JetBrains model keeps execution local, meaning the agent runs in the developer's
  environment rather than on GitHub's remote infrastructure. Local execution implies different
  privacy, latency, and cost characteristics than CCA-based cloud execution. For Ch02: note the
  local vs. remote execution distinction when documenting agent integration options across IDEs.

### Claim 2: Worktree isolation runs the agent in a separate Git worktree, preventing branch contamination until changes are explicitly reviewed and applied

- **Evidence**: Official changelog with specific behavioral description of the worktree isolation
  mechanism.
- **Confidence**: settled (product behavior described in official changelog)
- **Quote**: "Worktree isolation runs the agent in a separate Git worktree, so changes don't
  affect your current branch until you choose to review and apply them."
- **Our assessment**: This is a concrete safety pattern for agent-driven changes. The worktree
  model is the Git-native equivalent of running the agent in a sandbox — changes accumulate in
  an isolated branch, and the developer decides what to merge. For practitioners cautious about
  agentic writes to their working tree, worktree isolation makes the agent review-first by
  default. The corroborating evidence from `blog-addyosmani-code-agent-orchestra.md` (Claim 11)
  recommends git worktrees for isolation as a best-practice pattern independent of any tool;
  this source shows GitHub implementing that recommendation directly in the IDE. For Ch03 (agent
  safety patterns): recommend worktree isolation as the default for agent tasks that touch
  production code, especially in long-running or multi-file tasks.

### Claim 3: Workspace isolation applies agent changes directly to the current workspace for faster iteration when safety isolation is not required

- **Evidence**: Official changelog description of the alternative isolation mode with explicit
  use-case qualifier.
- **Confidence**: settled (product behavior stated in official changelog)
- **Quote**: "Workspace isolation applies changes directly to your current workspace, allowing
  for faster iteration when isolation isn't required."
- **Our assessment**: Workspace isolation is the speed-over-safety tradeoff. "When isolation
  isn't required" implies this is appropriate for low-stakes or exploratory work where the
  developer is comfortable reviewing inline changes as they appear. Claims 2 and 3 together
  establish an explicit safety/speed tradeoff that practitioners must consciously make when
  configuring the agent — a per-session decision, not a global setting. For Ch03: frame the
  choice as: worktree for unattended or production-branch tasks; workspace for exploratory,
  low-stakes, or actively monitored tasks.

### Claim 4: Copilot Business and Enterprise subscribers require administrator enablement of the "Editor preview features" policy before using the Copilot CLI agent in JetBrains

- **Evidence**: Official "Note:" callout in the changelog, explicitly naming the policy gate.
- **Confidence**: settled (access requirement stated directly in official changelog)
- **Quote**: "If you are a Copilot Business or Copilot Enterprise subscriber, an administrator
  will have to enable the Editor preview features policy before you can use this feature."
- **Our assessment**: The "Editor preview features policy" is a distinct governance gate from
  the Anthropic Claude or OpenAI Codex agent policies documented in
  `docs-github-copilot-agent-model-selection.md` (Claim 5). Teams planning to roll out the
  JetBrains CLI agent must pre-enable this specific policy at the org admin level — individual
  developers cannot self-enable. For Ch05: add this policy requirement to the enterprise Copilot
  governance checklist as a separate item from the Claude/Codex agent policies.

### Claim 5: The unified sessions view tracks all agent sessions in one place with per-session metadata — title, agent type, elapsed time, and status — and supports filtering by type or status

- **Evidence**: Official changelog description of the unified sessions view UI and its four
  per-session attributes.
- **Confidence**: settled (UI behavior described in official changelog)
- **Quote**: "The chat window now includes a unified sessions view, making it easier to track
  all agent sessions in one place. Each session shows its title, agent type, elapsed time, and
  status. You can also filter sessions by agent type or status to quickly find what you're
  looking for."
- **Our assessment**: The unified sessions view is an observability primitive for multi-session
  agent work. The four-attribute model (title, agent type, elapsed time, status) gives
  developers a lightweight status board for concurrent agent tasks. "Elapsed time" is
  particularly notable — it surfaces the temporal dimension of agent work, helping practitioners
  develop intuitions about how long different agent types take. This is complementary to, but
  distinct from, the Claude Code agent view documented in `blog-anthropic-agent-view-claude-code.md`
  (which tracks sessions in a terminal interface). For Ch04 (agentic workflows): the four-
  attribute session model is a design template for any team building agent dashboards or session
  management UIs.

### Claim 6: The ask question tool enables agents to request clarifying information mid-task, and is supported across agent mode, custom agents, sub-agents, and the Copilot CLI agent — but not Ask mode

- **Evidence**: Official changelog description of the ask question tool scope and explicit
  exclusion.
- **Confidence**: settled (feature scope and exclusion stated in official changelog)
- **Quote**: "Agent mode now includes an Ask question tool, enabling agents to ask focused
  clarifying questions when additional information is needed. This is supported across agent
  mode, custom agents, sub agents, and Copilot CLI agent, and it's not available in Ask mode."
- **Our assessment**: The ask question tool is a structured disambiguation mechanism — rather
  than agents proceeding on incomplete information and producing wrong output, they can surface
  gaps to the developer. The exclusion from Ask mode is logical (Ask mode is already a
  question-asking interface). The breadth of support across four agent contexts suggests this
  is a platform-level capability, not feature-specific. For Ch04: frame this as a best-practice
  agent-design pattern — agents should prefer asking when ambiguous rather than proceeding with
  the most plausible interpretation. The ask question tool is the platform mechanism that
  enforces this principle.

### Claim 7: Global custom agents can be defined via `.agent.md` files in `~/.copilot/agents`, making them available across all workspaces

- **Evidence**: Official changelog with specific configuration path and cross-workspace scope.
- **Confidence**: settled (configuration path and scope described in official changelog)
- **Quote**: "you can now define custom agents at the global level using the `.agent.md` file
  under `~/.copilot/agents`, making them available across all your workspaces."
- **Our assessment**: This is the user-scope agent configuration pattern for JetBrains/Copilot
  CLI agent, analogous to the `%USERPROFILE%/.github/agents/` path documented for Visual Studio
  in `docs-github-copilot-vs-april-2026.md` (Claim 5). Both features extend agent configuration
  to the user scope outside any repository, but use different paths for different platforms:
  `~/.copilot/agents` (Unix-style for JetBrains/Linux/macOS) vs. `%USERPROFILE%/.github/agents/`
  (Windows/VS). This is not a contradiction — it is per-platform user-scope agent configuration.
  The governance gap identified in `docs-github-copilot-vs-april-2026.md` (Claim 6) applies
  equally here: `~/.copilot/agents` is outside org-level policy controls. For Ch02: add a
  "user-scope vs. project-scope agent configuration" section cross-referencing both platforms.

### Claim 8: Edit mode support has been removed from GitHub Copilot for JetBrains

- **Evidence**: Official changelog removal notice with no documented migration path.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Edit mode support has been removed."
- **Our assessment**: This is a breaking change for practitioners who relied on edit mode. The
  changelog provides no migration path or replacement guidance. Teams who built workflows around
  edit mode need to migrate to agent mode or workspace isolation mode. The removal may be related
  to the introduction of the CLI agent with workspace isolation, which covers similar ground more
  flexibly. For Ch02: if the guide currently mentions edit mode for JetBrains Copilot, remove
  that reference entirely.

### Claim 9: The plan agent no longer auto-invokes in sub-agent workflows, requiring explicit invocation

- **Evidence**: Official changelog behavioral change notice.
- **Confidence**: settled (behavioral change stated in official changelog)
- **Quote**: "The plan agent is no longer auto-invoked in sub-agent workflows."
- **Our assessment**: This changes multi-agent workflow behavior in JetBrains. Previously,
  sub-agent workflows automatically invoked the plan agent for task decomposition or planning.
  Now practitioners who want plan agent behavior in sub-agent contexts must invoke it explicitly.
  For Ch04 (multi-agent orchestration): note this as a breaking behavioral change. Any JetBrains
  sub-agent workflow that relied on automatic plan agent invocation must be updated to invoke it
  explicitly.

### Claim 10: A confirmation prompt is now required when starting a new command that would cancel an active agent session, preventing accidental interruption of in-progress work

- **Evidence**: UX improvement described in official changelog.
- **Confidence**: settled (UX behavior stated in official changelog)
- **Quote**: "Added confirmation when starting a new command to cancel the active one."
- **Our assessment**: This is a safety guard against inadvertent cancellation of running agent
  tasks. The implicit prior behavior — new command silently cancels active one — was a
  potential source of data loss or incomplete agent output. For Ch03 (agent reliability): the
  confirmation-before-interruption pattern is a good design principle for any agent
  orchestration UI. Practitioners building custom agent UIs should adopt a similar guard.

## Concrete Artifacts

### Copilot CLI Agent Isolation Modes (JetBrains, Public Preview)

```
GitHub Copilot CLI Agent — JetBrains IDEs

WORKTREE ISOLATION:
  Mechanism: agent runs in a separate Git worktree
  Effect:    changes don't affect your current branch
             until you choose to review and apply them
  Use case:  production-branch tasks, unattended execution,
             multi-file changes requiring review

WORKSPACE ISOLATION:
  Mechanism: applies changes directly to your current workspace
  Effect:    changes appear in-place immediately
  Use case:  exploratory work, low-stakes tasks,
             actively monitored short sessions

GOVERNANCE GATE (Business/Enterprise subscribers):
  Required policy: "Editor preview features"
  Who enables it:  org/enterprise administrator
  (separate from Claude/Codex agent policies)
```

### Unified Sessions View Attributes

```
Per-session attributes in the unified sessions view:
  1. title        (name of the agent session/task)
  2. agent type   (which agent type is running)
  3. elapsed time (how long the session has been running)
  4. status       (current execution state)

Filtering capabilities:
  - Filter by agent type
  - Filter by status
```

### Global Agent Configuration Paths (User-Scope, Cross-Platform)

```
JetBrains / Copilot CLI agent (this source, May 2026):
  ~/.copilot/agents/
  File type: .agent.md
  Platform:  Linux/macOS (Unix-style path)
  Scope:     available across all workspaces

Visual Studio (docs-github-copilot-vs-april-2026.md, April 2026):
  %USERPROFILE%\.github\agents\
  Platform:  Windows
  Scope:     personal agents across all VS projects

Both: user-scope, outside any repository,
      not documented as covered by enterprise/org policy controls.
```

### Ask Question Tool Scope

```
Ask question tool availability:
  ✓ Agent mode
  ✓ Custom agents
  ✓ Sub agents
  ✓ Copilot CLI agent
  ✗ Ask mode  (excluded — Ask mode is itself question-based)
```

### Removals and Breaking Changes

```
Removals in this update:
  - Edit mode support: REMOVED
    No replacement path documented in changelog.

  - Plan agent auto-invocation in sub-agent workflows: REMOVED
    Impact: sub-agent workflows previously relying on automatic
    plan agent invocation now require explicit invocation.

UX changes:
  - NEW: confirmation prompt when starting a command that
         would cancel the active one
  - IMPROVED: sub-agent rendering and styling for current file context
  - IMPROVED: code review apply behavior (full-line replacements)
  - FIXED: code completions not working on second screen (multi-monitor)
  - FIXED: Shift+Home and Shift+End inline selection behavior
```

## Cross-References

- **Corroborates**:
  - **docs-github-copilot-vs-april-2026.md** (#475, Claim 5): VS note documents user-level agent
    definitions at `%USERPROFILE%/.github/agents/` for cross-project personal agents. This source
    documents the same user-scope pattern at `~/.copilot/agents` for JetBrains. Both corroborate
    GitHub's trend of expanding agent configuration to the user scope across IDE platforms.
  - **docs-github-copilot-vs-april-2026.md** (#475, Claim 6): VS note identifies the governance
    gap for user-level agents (no admin controls documented). This source corroborates that gap:
    `~/.copilot/agents` is similarly outside repo and org governance controls.
  - **docs-github-copilot-cli-auto-model-selection.md** (#203, Claim 1): Both sources document
    GitHub expanding the Copilot CLI feature surface in 2026 — auto model selection (April) and
    CLI agent in JetBrains (May). GitHub is consistently building the CLI as a first-class feature
    development surface alongside the web UI.
  - **blog-addyosmani-code-agent-orchestra.md** (Claim 11): Osmani recommends "git worktrees for
    isolation" as one of five concrete patterns for agent work. This source shows GitHub
    implementing that recommendation as a named isolation mode inside an IDE — validating the
    worktree-isolation recommendation with a production platform implementation.

- **Extends**:
  - **docs-github-copilot-vs-april-2026.md** (#475): That note establishes VS-specific cloud
    agent dispatch from the IDE. This source adds the JetBrains-specific local CLI agent
    execution model, completing a two-IDE picture of GitHub's IDE-agent strategy: VS dispatches
    to remote CCA infrastructure; JetBrains runs a locally-executing CLI agent. The contrast is
    architecturally significant — different execution models, different governance requirements,
    different privacy and cost profiles.
  - **docs-github-copilot-agent-skills-cli.md** (#189): That note documents `gh skill` and the
    Copilot CLI ecosystem. This source extends by documenting the Copilot CLI agent (distinct from
    CLI skills) now embedded in JetBrains — showing the CLI agent model expanding from
    terminal-only to IDE-integrated.
  - **docs-github-copilot-agent-model-selection.md** (#171): That note documents the two-layer
    governance model for Claude/Codex agents (Copilot Business/Enterprise + admin policy). This
    source extends the governance picture with a third policy gate: the "Editor preview features
    policy" required for the JetBrains CLI agent — separate from the Claude/Codex policies.
  - **blog-anthropic-agent-view-claude-code.md**: That note documents Claude Code's agent view as
    a terminal-based multi-session management primitive (title, input-needed status, last response,
    elapsed time). This source shows GitHub building a parallel in-IDE primitive with the unified
    sessions view — same four-attribute observability model applied to a different execution
    environment.

- **Contradicts**: None identified. The `~/.copilot/agents` path (JetBrains) vs.
  `%USERPROFILE%/.github/agents/` (VS) difference is platform-specific, not contradictory. No
  contradiction issue filed.

- **Novel**:
  - **Worktree isolation as an explicit IDE agent safety mode**: No prior source in the corpus
    documents worktree isolation as a named, selectable IDE mode. Prior sources recommend git
    worktrees for agent isolation as a general practice; this is the first platform implementation
    of that recommendation as a first-class UI option.
  - **Unified sessions view as an in-IDE agent observability primitive**: No prior source
    documents a multi-session agent tracking UI embedded in an IDE with per-session elapsed time,
    type, and status. The Claude Code agent view is terminal-based; this is the first IDE-native
    equivalent.
  - **JetBrains-specific Copilot agent integration**: All prior Copilot IDE sources in the corpus
    cover GitHub.com, Visual Studio, or VS Code. This is the first source to document
    JetBrains-specific Copilot agent integration patterns.
  - **Ask question tool as a platform-provided disambiguation mechanism**: This is the first
    source to document a platform-provided mid-task clarification mechanism with documented scope
    across four agent contexts. Prior sources discuss agent disambiguation conceptually; this is
    the concrete platform primitive.
  - **`~/.copilot/agents` as a JetBrains user-scope agent configuration path**: Distinct from
    the VS-specific `%USERPROFILE%/.github/agents/`, this introduces a platform-specific
    user-scope convention for JetBrains/Copilot.

## Guide Impact

- **Chapter 02 (Harness Engineering — Agent Configuration)**:
  - Add a "User-scope vs. project-scope agent configuration" section consolidating the VS
    (`%USERPROFILE%/.github/agents/`) and JetBrains (`~/.copilot/agents`) user-scope patterns.
    Frame these as personal agent toolkits that travel with the developer but are invisible to org
    governance — useful for individual productivity tools, not appropriate for shared team
    workflows. Cross-reference `docs-github-copilot-vs-april-2026.md` for the VS side.
  - Add the worktree vs. workspace isolation choice as a practitioner configuration decision:
    document the tradeoff explicitly with use-case guidance (worktree for production/unattended
    /multi-file; workspace for exploratory/low-stakes/monitored).
  - Add the "Editor preview features policy" to the enterprise Copilot policy enablement checklist
    as a distinct requirement for JetBrains CLI agent access.
  - Remove any mention of edit mode in JetBrains Copilot — it has been removed with no
    documented replacement.

- **Chapter 03 (Agent Safety and Verification)**:
  - Add worktree isolation as a first-class safety pattern for IDE-based agent work. Recommend
    as default for agent tasks that modify production-branch code or run without active developer
    monitoring. Frame as the IDE-native implementation of the broader "git worktrees for isolation"
    recommendation corroborated in `blog-addyosmani-code-agent-orchestra.md` (Claim 11).
  - Add the ask question tool as a disambiguation pattern: the principle is "when in doubt, ask,
    don't guess" — GitHub now provides a platform mechanism to enforce it. Note that this requires
    active developer availability to answer questions; purely unattended agent runs may stall on
    clarification requests.
  - Document the confirmation-before-cancellation guard as a UX safety pattern worth replicating
    in custom agent UIs.

- **Chapter 04 (Agentic Workflows)**:
  - Add the unified sessions view four-attribute model (title, agent type, elapsed time, status)
    as a reference design for agent session observability. Teams building custom agent
    orchestration UIs should capture at minimum these four dimensions. Compare to Claude Code
    agent view's terminal-based equivalent (`blog-anthropic-agent-view-claude-code.md`).
  - Note the plan agent auto-invocation removal as a breaking change for JetBrains multi-agent
    workflows. Practitioners must update any sub-agent orchestration that relied on implicit plan
    agent invocation to invoke it explicitly.

- **Chapter 05 (Enterprise Governance)**:
  - Extend the Copilot governance checklist with the "Editor preview features policy" gate for
    JetBrains CLI agent — a third distinct policy alongside Claude and Codex agent policies.
  - Extend the user-scope governance gap section (from `docs-github-copilot-vs-april-2026.md`)
    to cover `~/.copilot/agents` in JetBrains. Enterprise AI policies that rely solely on
    org-level Copilot policy controls do not cover user-scope agent definitions on either platform.

## Extraction Notes

1. **Source is a changelog (~500 words)**: All substantive content is exhausted in 10 claims
   above. The source covers six new features, several UX improvements, and two removals — all
   extracted.
2. **"Locally running" CLI agent**: The source explicitly says "locally running," distinguishing
   the JetBrains CLI agent from CCA cloud execution. The guide should consistently use this
   distinction when comparing IDE-agent execution models.
3. **Worktree isolation implementation details are thin**: The changelog does not specify how
   the Git worktree is named, where it is created, or how the apply/merge process works. The
   claims above reflect what is stated; deeper evaluation requires hands-on testing or a
   follow-on source.
4. **Public preview caveat**: The CLI agent feature is in public preview — behavior, API surface,
   and policy names may change before GA. Treat specific configuration details (policy name,
   isolation mode names) as potentially subject to change.
5. **JetBrains multi-IDE scope**: "JetBrains IDEs" covers IntelliJ IDEA, PyCharm, WebStorm,
   GoLand, and others. The changelog does not specify which JetBrains IDEs are supported —
   practitioners should verify support for their specific IDE.
6. **No effectiveness data**: The source makes no claims about task success rates, time savings,
   or quality improvements. No comparison between isolation modes is provided.
