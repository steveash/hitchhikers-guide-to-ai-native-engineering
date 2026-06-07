---
source_url: https://github.blog/changelog/2026-06-04-github-copilot-in-visual-studio-may-update
source_type: docs
title: "GitHub Copilot in Visual Studio — May 2026 Update"
author: GitHub (official changelog)
date_published: 2026-06-04
date_extracted: 2026-06-07
last_checked: 2026-06-07
status: current
confidence_overall: emerging
issue: "#1100"
---

# GitHub Copilot in Visual Studio — May 2026 Update

> GitHub's May 2026 changelog for Copilot in Visual Studio introduces five AI-native
> engineering patterns worth tracking: a Plan agent that formalises planning as a
> distinct phase before implementation (producing a versioned markdown artifact); a
> Skills panel that surfaces the multi-path skill discovery from April into a
> practitioner-visible UI; a multi-file summary diff with three-level accept/undo
> granularity; a context-window ring indicator that makes budget consumption explicit;
> and consolidation of commit-message instructions into the central Copilot custom
> instructions file, continuing the pattern of moving IDE settings into repository
> configuration.

## Source Context

- **Type**: docs (GitHub official product changelog, June 4, 2026)
- **Author credibility**: GitHub engineering team announcing production features in
  Visual Studio. Authoritative for the fact that these capabilities exist, the exact
  file path conventions (`.copilot/plans/plan-{title}.md`), the UI labels, and the
  workflow steps described. Not a credible source for how often the Plan agent
  produces useful plans, how the plan handoff to Agent mode behaves on large codebases,
  or whether context-window compaction produces semantically coherent summaries. No
  empirical data on effectiveness.
- **Scope**: Seven features in the May 2026 Visual Studio update: Plan agent, Skills
  panel, multi-file summary diff, context-window indicator, commit context attachment,
  commit message instructions migration, and @BuildPerfCpp incremental build
  refinement. The source also links to a companion Visual Studio blog post at
  `devblogs.microsoft.com/visualstudio/visual-studio-may-update-plan-review-refine`,
  which was followed as a sub-page and provides more detailed descriptions of several
  features (see Extraction Notes). Does NOT cover: how Plan agent interacts with
  CLAUDE.md or AGENTS.md project instructions, whether the plan artifact is committed
  to the repository, how the skills panel handles conflicting skills from workspace vs.
  user-profile paths, whether the context-window indicator applies to cloud agent
  sessions or only local chat, or any effectiveness or cost data.

## Extracted Claims

### Claim 1: The Plan agent introduces agentic planning as a discrete phase before implementation, producing a versioned markdown artifact

- **Evidence**: Official changelog and companion blog post both describe the Plan agent
  as explicitly separated from code execution: it runs before any code is written, using
  only read-only tools during the exploration phase, and produces a markdown file at a
  fixed path. The blog post provides step-level detail on the two phases and the handoff
  mechanism.
- **Confidence**: settled (product fact — phases, file path, and UI label documented in
  official changelog and companion blog post)
- **Quote**: "The new **Plan agent** lets you collaborate with Copilot on an
  implementation plan before code is written."
  (github.blog changelog)
- **Our assessment**: This is the most significant pattern in this changelog for Ch04.
  Prior agentic workflows documented in the corpus (debugger agent from
  `docs-github-copilot-vs-april-2026.md` Claim 3; cloud agent from the same note Claim
  7; CCA-based workflows) all start directly from an implementation or diagnosis task.
  The Plan agent introduces a new workflow shape: planning is a distinct agentic phase,
  not a preliminary step the user does manually before invoking the agent. The agent
  explores, clarifies, and drafts — then the practitioner reviews and refines before
  execution begins. This two-phase model (plan → implement) is architecturally different
  from single-phase "describe and execute" agents. For Ch04: document as the first
  concrete "plan-then-implement" agentic workflow pattern in the corpus, where planning
  itself is delegated to the agent with human review at the handoff point.

### Claim 2: The Plan agent operates in a two-phase model — read-only exploration and clarification, then plan drafting — before the practitioner triggers implementation

- **Evidence**: Companion blog post (devblogs.microsoft.com) describes the two phases
  explicitly, with the read-only constraint named for the exploration phase and the
  "Implement plan" button as the handoff trigger.
- **Confidence**: settled (two phases and UI trigger described in companion blog post)
- **Quote**: "First it explores and clarifies, using read-only tools to understand your
  codebase and asking questions when it needs to. Then it drafts a detailed plan you can
  review, discuss, and refine together."
  (devblogs.microsoft.com companion post)
- **Our assessment**: The read-only constraint in the exploration phase is a meaningful
  safety property: the agent cannot make premature changes while still understanding the
  problem. This is a trust-building design — practitioners who are uncomfortable with
  agents that immediately start modifying files can use the Plan agent as a lower-risk
  entry point to agentic workflows. The "review, discuss, and refine" step before
  implementation means the plan artifact is collaborative, not just agent-generated.
  For Ch04: the two-phase model is a workflow template worth prescribing for complex
  changes where a "describe and execute" approach risks costly mistakes. The agent plans
  without risk; the practitioner reviews; then execution begins with shared understanding.

### Claim 3: Plan artifacts are saved to `.copilot/plans/plan-{title}.md` as markdown files, making plans versionable and inspectable alongside source code

- **Evidence**: Both the changelog and companion blog post specify the exact file path
  format. The path is under `.copilot/` (the same namespace as Copilot custom
  instructions), implying co-location with other Copilot configuration.
- **Confidence**: settled (file path documented in both official sources)
- **Quote**: "Every plan is saved as a markdown file at `.copilot/plans/plan-{title}.md`."
  (devblogs.microsoft.com companion post)
- **Our assessment**: The plan-as-file pattern means the plan artifact participates in
  version control. If `.copilot/plans/` is committed, teams have a record of what was
  planned before each implementation, providing an audit trail of AI-assisted design
  decisions. If it is git-ignored, the plan is ephemeral and per-developer. The source
  does not specify which convention GitHub recommends. For Ch02 (Harness Engineering):
  the `.copilot/plans/` directory is a new configuration surface practitioners should
  decide whether to commit. For Ch04: the plan file is the handoff artifact — the
  practitioner can edit it directly before clicking "Implement plan," making it a
  writable intermediate state in the plan-to-execute pipeline.

### Claim 4: "Implement plan" hands off the plan to Agent mode for execution, creating a structured plan-to-execute pipeline

- **Evidence**: Companion blog post names the explicit trigger and target mode: "click
  **Implement plan** to hand it off to **Agent** mode for execution."
- **Confidence**: settled (UI trigger and target mode named in companion blog post)
- **Quote**: "When you're ready, click **Implement plan** to hand it off to **Agent**
  mode for execution."
  (devblogs.microsoft.com companion post)
- **Our assessment**: The handoff to Agent mode means the Plan agent and Agent mode are
  distinct operational modes in VS Copilot, not a single continuous agent. The
  practitioner explicitly chooses when to cross the plan-to-implement boundary. This
  design preserves human control at the most consequential moment in the workflow: the
  moment the agent starts modifying files. For Ch04: this handoff point is where the
  practitioner's review of the plan serves as an implicit approval gate. Teams that want
  audit trails of agent-driven changes should ensure the plan artifact is committed
  before "Implement plan" is clicked — the plan then becomes pre-change documentation
  analogous to a RFC or ADR.

### Claim 5: The Skills panel provides a centralized UI to view, search, and edit agent skills discovered from both workspace paths and user profile

- **Evidence**: Official changelog describes the panel as discovering skills from "your
  workspace and user profile" — combining project-scope and user-scope discovery into a
  single visible interface. The panel offers search and context-menu actions.
- **Confidence**: settled (panel capabilities and discovery scope stated in official
  changelog)
- **Quote**: "A new **Skills** panel in the chat window lists every agent skill
  discovered from your workspace and user profile. You can edit a skill, open its file
  location, or search across skills by name or keyword, all from a single place."
  (github.blog changelog)
- **Our assessment**: The Skills panel is the UI layer on top of the multi-path skill
  discovery announced in the April 2026 update. April's Claim 1
  (`docs-github-copilot-vs-april-2026.md`) documented discovery from `.github/skills/`,
  `.claude/skills/`, and `.agents/skills/`, but the practitioner had no way to inspect
  what was being discovered without knowing to look in those directories. The panel
  makes the discovered skill set visible and actionable. The "workspace and user profile"
  scope language confirms that user-profile skills (corresponding to April's Claim 5 on
  user-level definitions in `%USERPROFILE%/.github/agents/`) are also surfaced here.
  For Ch02: the Skills panel is now the recommended first step for practitioners
  onboarding to an existing codebase — browse the panel to understand what agent skills
  are available before starting work.

### Claim 6: Skills panel actions include direct editing and file-system navigation, making skills modifiable from the IDE without separate file browsing

- **Evidence**: Companion blog post names the specific context-menu actions: "Edit" opens
  the skill file in VS; "Open in file explorer" jumps to its location on disk.
- **Confidence**: settled (menu actions named in companion blog post)
- **Quote**: "From the panel you can act on any skill via the **⋯** menu: **Edit** opens
  the skill file directly in Visual Studio, and **Open in file explorer** jumps to its
  location on disk."
  (devblogs.microsoft.com companion post)
- **Our assessment**: The in-IDE edit capability for skills reduces friction for
  practitioners who want to modify skill files without switching to a file browser.
  This is a meaningful UX improvement for skill maintenance: discover that a skill is
  wrong or outdated, edit it directly from the same panel where you saw it. For Ch02:
  document the Skills panel edit workflow as the recommended skill maintenance path in
  VS — no need to know the file path in advance. The file-explorer shortcut is useful
  for skills that require adjacent file changes (e.g., scripts referenced by a skill).

### Claim 7: A ring icon in the Copilot Chat prompt box displays context-window usage as a mini donut chart, making budget consumption visible during the conversation

- **Evidence**: Both the changelog and companion blog post describe the ring icon
  consistently. The changelog names the "Summarize conversation" action; the blog post
  describes the visual metaphor (mini donut chart fills as conversation grows).
- **Confidence**: settled (UI element and visual metaphor described in official sources)
- **Quote**: "A new ring icon at the top right of the Copilot Chat prompt shows how much
  of the context window you've used. Click to see a detailed breakdown and use
  **Summarize conversation** to compact earlier turns and free up space."
  (github.blog changelog)
- **Our assessment**: This is the first documented context-budget visibility mechanism
  in the VS Copilot corpus. Prior sources document context engineering patterns
  (what to include, how to structure CLAUDE.md, etc.) but none document a UI element
  that actively shows practitioners when they are approaching context limits. The
  indicator changes the practitioner's relationship with context: rather than
  discovering "conversation exceeded limit" errors reactively, practitioners can
  proactively compact before hitting the ceiling. For Ch01 (Daily Workflows): add
  context monitoring as a routine habit — check the ring icon during long debugging
  sessions or multi-file change workflows, and use "Summarize conversation" preemptively
  rather than reactively. For Ch04 (Context Engineering): the ring icon makes the
  context budget a first-class workflow concern, not just a configuration parameter.

### Claim 8: "Summarize conversation" compacts earlier turns to free context-window space, enabling continuation of long sessions without starting fresh

- **Evidence**: Changelog describes "Summarize conversation" as the action to "compact
  earlier turns and free up space." The devblogs companion names this `/compact` as well.
- **Confidence**: settled (feature named in official changelog; mechanism described)
- **Quote**: "use **Summarize conversation** to compact earlier turns and free up space"
  (github.blog changelog)
- **Our assessment**: Context compaction in an IDE chat session is a significant
  operational primitive. Long debugging or planning sessions accumulate context that
  may exhaust the window before the task is complete. "Summarize conversation" extends
  session longevity without losing the thread of the current problem. The trade-off:
  compaction is lossy — earlier turns are summarized, not preserved verbatim. For
  practitioners who need full fidelity of earlier decisions (e.g., "the agent said X
  three turns ago"), compaction discards that fidelity. For Ch01: document this as the
  prescribed action when the ring icon signals a nearly-full context window, with the
  caveat that compaction is irreversible and lossy. Teams with compliance requirements
  around audit trails of AI-assisted decisions should note that compacted conversation
  history may not meet those requirements.

### Claim 9: The multi-file summary diff enables batch review of all Copilot-generated changes in one view, with accept/undo at three granularity levels (all-files, per-file, per-chunk)

- **Evidence**: Official changelog describes the "Open change summary view" entry point
  and three-level accept/undo. Companion blog post confirms the three levels explicitly.
- **Confidence**: settled (feature and granularity levels described in official sources)
- **Quote**: "Accept or undo at the all-files, per-file, or per-chunk level, with
  controls to collapse files or step through diff chunks."
  (github.blog changelog)
- **Our assessment**: The three-level accept/undo model is a meaningful improvement
  over binary accept-all/reject-all for multi-file agent edits. Practitioners who use
  agentic workflows on large tasks commonly receive changes spanning many files; the
  ability to accept some files and reject others (or accept some chunks and reject
  others within a file) allows fine-grained human control over the agent's output
  without forcing a complete redo. For Ch04 (Agentic Workflows): document this as the
  prescribed review workflow after any multi-file agent operation. The "Implement plan"
  workflow (Claim 4) will produce multi-file changes that can be reviewed in this view.
  For Ch01 (Daily Workflows): the "Open change summary view" button is the entry point
  for post-agent change review — analogous to `git diff --staged` but with accept/undo
  controls built in.

### Claim 10: Git commit history is now a first-class context source in Copilot Chat, attachable by right-clicking in Git History, File History, or Annotate views

- **Evidence**: Official changelog describes right-click attachment from three specific
  Git views with multi-select support.
- **Confidence**: settled (right-click action and source views named in official
  changelog)
- **Quote**: "Right-click a commit in **Git History**, **File History**, or the
  **Annotate (Blame)** view and attach it directly as context in Copilot Chat."
  (github.blog changelog)
- **Our assessment**: This is the first documented mechanism in the corpus for using
  git blame and commit history as explicit context in an agent chat session. Prior
  sources discuss providing context via CLAUDE.md, AGENTS.md, skills files, and
  automatic page attachment; none document a direct gesture for injecting historical
  commit context. The three source views (Git History, File History, Annotate/Blame)
  cover the three most common ways practitioners inspect code history in VS. For Ch01
  (Daily Workflows): document the right-click-to-attach gesture as the workflow for
  questions like "why was this changed?" or "what was the intent of this commit?"
  For Ch04 (Context Engineering): commit history is now an explicit context injection
  pathway — practitioners can select relevant commits (multi-select) and attach them
  to provide temporal context for a current task.

### Claim 11: Commit message custom instructions have been consolidated from IDE settings into the repository's Copilot custom instructions file, continuing the pattern of centralizing Copilot configuration in the repository

- **Evidence**: Official changelog explicitly names the source location removed
  ("old GitHub > Copilot > Source Control Integration setting") and the target
  location (repository's Copilot custom instructions file). This follows the same
  centralization pattern seen in previous Copilot changelog entries.
- **Confidence**: settled (migration stated in official changelog)
- **Quote**: "Commit message custom instructions now live in your repository's Copilot
  custom instructions file instead of the old setting."
  (github.blog changelog)
- **Our assessment**: This migration is part of a consistent trend: GitHub is moving
  Copilot configuration from per-developer IDE settings into repository-level files
  (`.github/copilot-instructions.md` or equivalent). The implication for teams: commit
  message standards (e.g., "always reference the issue number," "use conventional
  commits format") can now be version-controlled alongside the code, reviewed in PRs,
  and applied consistently across all team members without each developer needing to
  configure their IDE manually. For Ch02 (Harness Engineering): document this migration
  explicitly. Teams with existing commit message standards in IDE settings must
  migrate to the repository instructions file to maintain those standards. The fact that
  the OLD location (a personal IDE setting) is being removed means this is not additive —
  it requires active migration for any team already using commit message instructions.

### Claim 12: The @BuildPerfCpp agent now reruns comparable incremental builds when full rebuild analysis detects a regression, providing more accurate incremental-vs-full build comparisons

- **Evidence**: Official changelog describes the specific condition (regression detected
  in full rebuild analysis) and the action (rerun comparable incremental build).
- **Confidence**: settled (behavior change described in official changelog)
- **Quote**: "When **@BuildPerfCpp** detects a regression in full rebuild analysis, it
  now reruns a comparable incremental build."
  (github.blog changelog)
- **Our assessment**: This is a narrow refinement to the @BuildPerfCpp agent
  introduced in a prior update. The signal is primarily that GitHub is continuing
  to iterate on domain-specific build optimization agents in production. For the
  guide corpus: this has minimal cross-chapter impact beyond confirming that
  agent-assisted build optimization is a maturing pattern. The specific behavior
  (rerun on regression detection) is a correction to a previous limitation where
  full rebuild regressions were being compared against incremental builds that were
  not comparable. The fix makes the agent's regression signal more reliable.

## Concrete Artifacts

### Plan Agent Workflow (Visual Studio, May 2026)

```
Entry: Practitioner describes a task to the Plan agent (labeled "Plan" in agent picker)

Phase 1 — Explore and Clarify (read-only):
  Agent explores codebase with read-only tools
  Agent asks clarifying questions when needed
  No code is modified in this phase

Phase 2 — Draft Plan:
  Agent drafts a detailed implementation plan
  Plan saved to: .copilot/plans/plan-{title}.md  (markdown file)
  Practitioner can review, discuss, and refine the plan
  Direct editing of the markdown file is supported

Handoff:
  Practitioner clicks "Implement plan"
  → Hands off to Agent mode for execution
  → Agent mode begins making code changes per the plan

Key property: No code is written until the practitioner explicitly approves
the plan and clicks "Implement plan"
```

Source: github.blog changelog + devblogs.microsoft.com companion post,
both retrieved 2026-06-07

### Context Window Indicator and Compaction

```
UI element: Ring icon at top right of Copilot Chat prompt box
Visual:     Mini donut chart — fills as conversation grows
Action:     Click ring → detailed context breakdown
Compaction: "Summarize conversation" → compacts earlier turns to free space

Note: Compaction is lossy (earlier turns are summarized, not preserved verbatim)
Alternative command: /compact
```

Source: github.blog changelog + devblogs.microsoft.com companion post,
both retrieved 2026-06-07

### Multi-File Summary Diff Accept/Undo Levels

```
Trigger:  Click "Open change summary view" in working set after multi-file edits

Accept/undo levels:
  1. All files at once   — accepts/reverts entire changeset
  2. Per file            — accepts/reverts one file's changes independently
  3. Per diff chunk      — accepts/reverts individual hunks within a file

Additional controls:
  - Collapse files in the summary view
  - Step through diff chunks

Also available in: Git Changes, commit details in branch history, pull request lists
```

Source: github.blog changelog + devblogs.microsoft.com companion post,
both retrieved 2026-06-07

### Commit Context Attachment (Visual Studio)

```
Sources that support right-click → "Attach to Copilot Chat":
  - Git History view
  - File History view
  - Annotate (Blame) view

Multi-select: supported (attach multiple commits as context simultaneously)

Use cases:
  - "Why was this changed?" → attach relevant commit(s) as context
  - "What was the original intent?" → attach blame entry
  - Historical context for current task → attach commits covering related code
```

Source: github.blog changelog, retrieved 2026-06-07

### Commit Message Instructions Migration

```
BEFORE (May 2026): GitHub > Copilot > Source Control Integration setting
                   (per-developer IDE setting, not version-controlled)

AFTER (May 2026):  Repository's Copilot custom instructions file
                   (version-controlled, shared across team)

Migration required: Teams with existing commit message instructions in IDE
settings must manually migrate to the repository instructions file.
```

Source: github.blog changelog, retrieved 2026-06-07

## Cross-References

- **Corroborates**:
  - **docs-github-copilot-vs-april-2026.md** (Claim 5): April documented user-level
    agent definitions at `%USERPROFILE%/.github/agents/`. The May Skills panel's
    "workspace and user profile" discovery scope confirms that user-profile-level skills
    are surfaced alongside workspace skills — the user-scope concept introduced in April
    is now visibly integrated into the practitioner UI.
  - **docs-github-copilot-agent-skills-cli.md** (Claim 1): The `gh skill` note
    documented skills as a managed, distributable artifact. The May Skills panel is the
    IDE-side consumption UI for those skills: practitioners install via `gh skill install`
    (documented in that note) and then view/manage the results in the Skills panel.
    Together the two sources show the complete skills lifecycle: distribute via CLI →
    inspect and manage via IDE panel.

- **Extends**:
  - **docs-github-copilot-vs-april-2026.md** (Claim 1): April announced multi-path
    skill discovery (`.github/skills/`, `.claude/skills/`, `.agents/skills/`). The May
    Skills panel is the visibility layer on top of that discovery — practitioners can now
    see what was discovered across those paths without knowing to look manually. The panel
    makes the multi-path discovery a first-class practitioner experience rather than an
    implicit background process.
  - **docs-github-copilot-vs-april-2026.md** (Claim 7): April documented cloud agent
    sessions launched from the VS agent picker. The May Plan agent is a new entry in the
    same agent picker ("labeled **Plan** in the agent picker"), extending the picker's
    agent roster from cloud/debugger to include the Plan agent as a local planning mode.
  - **docs-github-copilot-agent-skills-cli.md** (Claim 5): The agentskills.io spec
    claims cross-agent portability; the May Skills panel surfacing "workspace and user
    profile" discovery shows that the VS IDE is the practitioner-facing UI for the
    multi-host skill ecosystem described in that note. The panel search across skills
    by name/keyword is a discovery UX for the broader portfolio of installed skills.
  - **docs-github-copilot-chat-pr-richer-context.md**: The multi-file summary diff
    (Claim 9 here) extends into Git Changes, branch history commit details, and pull
    request lists — connecting to the PR context enrichment documented in that note.
    The two sources together complete the picture of how Copilot-assisted changes are
    reviewed: multi-file diff view for the agent's edits; PR chat with richer context
    for the resulting pull request.

- **Contradicts**: None identified. The May update extends April patterns without
  reversing any documented claims. The commit message instructions migration (Claim 11)
  is a removal of an old location, not a contradiction of any existing source note claim.
  No contradiction issue filed.

- **Novel**:
  - **Plan agent as planning-phase workflow**: No prior corpus source documents an
    agentic workflow specifically for the planning phase, with a read-only exploration
    phase, a markdown plan artifact, and an explicit human approval gate before
    implementation begins. Prior agentic workflows (debugger agent, cloud agent, CCA)
    all start from an implementation task.
  - **`.copilot/plans/plan-{title}.md` as a plan artifact path**: This is a new
    repository-level file path convention for agent-generated plan artifacts. No prior
    source documents it. The convention places plans alongside `.github/copilot-
    instructions.md` in the `.copilot/` namespace.
  - **Context-window ring indicator**: No prior corpus source documents a real-time
    visual indicator of context budget consumption in a practitioner-facing chat UI.
    Context management has been discussed conceptually (CLAUDE.md size constraints,
    etc.) but not as a live metric during active chat sessions.
  - **Multi-file summary diff with three-level granularity**: The ability to accept/undo
    agent-generated changes at all-files, per-file, or per-chunk levels is a new change
    management workflow. Prior sources discuss agent-generated changes as atomic
    (accept or reject), not granularly composable.
  - **Git history as explicit chat context source**: Commit history as a named,
    gesture-accessible context source (right-click to attach) is new to the corpus.
    Prior context injection mechanisms (page attachment, skills, MCP) do not include
    a direct gesture for attaching historical commits.

## Guide Impact

- **Chapter 04 (Agentic Workflows — Planning Phase)**:
  - Add the Plan agent pattern as the first documented "plan-before-implement" agentic
    workflow. The two-phase model (read-only explore → plan draft → human review →
    implement) should be documented as the recommended workflow for complex tasks where
    a "describe and execute" approach risks costly mistakes. Contrast with the single-
    phase debugger agent (`docs-github-copilot-vs-april-2026.md` Claim 3) and cloud
    agent (Claim 7 of same note) — both of which execute without a planning phase.
  - Document the "Implement plan" handoff as an explicit human approval gate: the
    practitioner's review of the plan before clicking the button is where AI-assisted
    design decisions are validated. For teams with AI governance requirements, the plan
    artifact at `.copilot/plans/plan-{title}.md` should be committed as pre-change
    documentation (analogue to an ADR or RFC).
  - Add the multi-file summary diff (Claim 9) as the prescribed post-implementation
    review step: after "Implement plan" executes, use "Open change summary view" to
    review all generated changes at the desired granularity before accepting.

- **Chapter 01 (Daily Workflows)**:
  - Add context budget monitoring as a practitioner habit: check the ring icon (Claim 7)
    during long debugging or planning sessions; use "Summarize conversation" (Claim 8)
    before the context ceiling is hit, not reactively after. Note that compaction is
    lossy — for sessions requiring full fidelity of earlier decisions, start a fresh
    session rather than compacting.
  - Add commit context attachment (Claim 10) as the workflow for historical questions:
    right-click in Git History / File History / Blame → attach commit(s) → ask "why was
    this changed?" This is faster than copy-pasting commit messages into chat manually.

- **Chapter 02 (Harness Engineering — Configuration Management)**:
  - Update the Copilot custom instructions coverage to include commit message instructions
    (Claim 11). Teams should migrate any commit message standards from the IDE Source
    Control Integration setting to the repository instructions file immediately — the old
    location is deprecated. Document the repository instructions file as the single
    configuration surface for all Copilot custom instructions, now including commit
    message formatting.
  - Add the `.copilot/plans/` directory as a new configuration surface teams should
    decide whether to version-control. Recommended: commit plans that precede significant
    agent-driven changes; gitignore plans from exploratory or throwaway sessions.
  - Document the Skills panel (Claims 5–6) as the recommended IDE entry point for
    practitioners onboarding to an existing codebase: browse the panel to see what
    agent skills are installed before starting work, edit skills in-IDE when updates
    are needed.

- **Chapter 02 (Harness Engineering — Skills)**:
  - Update the skills discovery section (from `docs-github-copilot-vs-april-2026.md`)
    to add that the Skills panel now makes discovered skills visible and actionable
    from a single panel. The panel + the multi-path discovery together form the complete
    picture: paths determine what is discovered; panel determines what is visible.

## Extraction Notes

1. **Two sources fetched**: The primary source is the github.blog changelog. The
   companion blog post at devblogs.microsoft.com was followed as a linked sub-page (per
   MINER.md §1: follow up to 5 linked pages that seem substantive). Both sources are
   treated as authoritative for the features they describe; the companion post provides
   more detailed descriptions of the Plan agent and Skills panel.

2. **WebFetch verbatim limitations**: The WebFetch tool processes content through an AI
   model and does not return raw HTML. All quotes in this note were surfaced within
   quotation marks by the WebFetch responses and are attributed to the source from which
   they were retrieved. Quotes that appeared consistently across multiple independent
   fetches of the same page are treated with higher confidence. The Assayer should spot-
   check quotes against the live source URLs. All claims for which no reliable verbatim
   text was available are marked `(no direct quote; see paraphrase in Our assessment)`.

3. **No effectiveness data**: This changelog makes no claims about Plan agent output
   quality, context-window compaction fidelity, or multi-file diff acceptance rates.
   Confidence ratings reflect the existence and described behavior of features, not
   their effectiveness in practice.

4. **@BuildPerfCpp** (Claim 12): Minimal AI-native engineering signal. Included for
   corpus completeness as an iteration on a domain-specific build agent pattern, but
   the guide impact is narrow.

5. **No contradictions to file**: Cross-referencing all VS Copilot, skills, and agentic
   workflow notes found no opposing claims. The commit message instructions migration
   (Claim 11) removes an old configuration location; no corpus source claims that
   location remains the current one.

6. **VS-only scope**: All features documented here are for Visual Studio specifically.
   Whether VS Code, JetBrains, or CLI equivalents receive the Plan agent, Skills panel,
   context ring, or multi-file summary diff is not addressed by this changelog.
