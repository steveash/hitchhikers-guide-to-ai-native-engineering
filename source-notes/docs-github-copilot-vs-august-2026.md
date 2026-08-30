---
source_url: https://github.blog/changelog/2026-08-28-github-copilot-in-visual-studio-august-update-2
source_type: docs
title: "GitHub Copilot in Visual Studio — August 2026 Update"
author: GitHub (official changelog)
date_published: 2026-08-28
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: settled
issue: "#3099"
---

# GitHub Copilot in Visual Studio — August 2026 Update

> GitHub's August 28, 2026 changelog for Copilot in Visual Studio headlines five
> features — Low/Medium/High model thinking-effort controls, organization-published
> custom agents auto-detected in the agent picker, an in-IDE Copilot usage/plan
> view, a pin/collapse/"Manage models" picker upgrade, and a named "Git agent" that
> reviews uncommitted changes or commits before a PR exists — while the companion
> Visual Studio devblogs post adds two Git-workflow features the changelog omits
> entirely: native Git worktree support and first-class Git submodule management.

## Source Context

- **Type**: docs (GitHub official product changelog, "2 minute read," published
  August 28, 2026). One companion page was followed as a substantive linked
  sub-page per MINER.md §1: the devblogs.microsoft.com Visual Studio blog post
  ("Visual Studio August Update — Work Smarter Across Models and Branches"),
  linked from the changelog as "Visual Studio blog." A second outbound link,
  `learn.microsoft.com/visualstudio/releases/2026/release-notes`, is a general,
  non-Copilot-specific release-notes aggregator and was not followed, matching
  the precedent in `docs-github-copilot-vs-july-2026.md` Source Context and
  `docs-github-copilot-vs-june-2026.md` Extraction Note 1 for this exact category
  of link. A third link, `docs.github.com/copilot/get-started/plans`, is a
  general plans/pricing reference page, not feature-specific, and was likewise
  not followed.
- **Author credibility**: GitHub and Microsoft engineering teams (changelog +
  devblogs companion post) announcing production and preview features.
  Authoritative for feature existence, exact UI paths/labels, and plan-
  availability gating. Not a credible source for whether the Git agent's review
  findings are accurate, whether organization-published custom agents are
  adopted in practice, or any effectiveness data for thinking-effort controls —
  none of these are asserted with a disclosed methodology in either source.
- **Scope**: Five headline features from the changelog's own "Highlights" list
  (thinking effort controls, organization-level custom agents, Copilot usage
  access, better model control, Git agent code review) plus two features that
  exist only in the devblogs companion post and are entirely absent from the
  changelog (Git worktree support, Git submodule support). Does NOT cover:
  adoption or usage data for any feature; which specific models support
  thinking-effort controls; whether the Git agent's review engine is the same
  underlying "GitHub Copilot code review" engine named in prior VS updates or a
  distinct implementation (the source does not say); or parity with the same
  month's VS Code or JetBrains releases (not checked directly for this note).

## Extracted Claims

### Claim 1: Supported models in Visual Studio now offer Low, Medium, and High thinking-effort controls, letting practitioners trade reasoning depth against speed and token usage per task

- **Evidence**: Stated in the changelog Highlights list and elaborated with
  concrete task-type guidance in the devblogs companion post, which names which
  effort level to use for which kind of work.
- **Confidence**: settled (product fact, worded consistently across the
  changelog and companion post; specific supported-model list not disclosed in
  either source)
- **Quote**: "Adjust model thinking effort to match your task: Supported models
  now offer Low, Medium, and High thinking effort controls. Use lower effort
  for straightforward work or higher effort for complex debugging, algorithms,
  and architecture decisions. This enables you to balance reasoning depth with
  token usage."
  (github.blog changelog, raw HTML, retrieved 2026-08-30)
- **Quote (devblogs companion post, task-type guidance)**: "Use Low for
  straightforward questions and code suggestions, Medium for everyday
  development, and High when you are working through a tricky algorithm,
  architecture decision, or hard-to-debug problem. You can adjust the setting
  from the Model picker or the expanded Language Models view."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-30)
- **Our assessment**: This is the first corpus source to name exactly three
  discrete, labeled reasoning-effort tiers ("Low," "Medium," "High") for
  Visual Studio specifically. Prior corpus reasoning-level sources describe the
  same speed/depth tradeoff with different granularity and naming per surface:
  VS Code/CLI/Copilot app got an unnamed "dial in the right balance" control
  with a separate "extended thinking" mode
  (`docs-github-copilot-1m-context-reasoning-levels.md` Claims 2–3, June 4,
  2026); Copilot cloud agent got a per-task reasoning-level picker with no
  named tiers disclosed (`docs-github-copilot-cca-reasoning-level.md` Claims
  1–3); Copilot code review got exactly two named tiers, "Lite" and "Balanced"
  (`docs-github-copilot-code-review-effort-levels-ga.md` Claims 1–2, renamed
  from "Low"/"Medium"). Visual Studio's three explicit Low/Medium/High labels
  are a fourth distinct naming scheme for what is functionally the same
  cost/quality control across at least five Copilot surfaces now (VS Code,
  CLI, Copilot app, CCA, code review, and Visual Studio) — GitHub has not
  converged on one label set for this control across products. For Ch04
  (Context Engineering — Reasoning Controls): document Visual Studio's
  explicit three-tier Low/Medium/High labeling and task-type guidance as the
  most prescriptive of the corpus's reasoning-level sources, and flag the
  cross-surface naming inconsistency (dial / unnamed levels / Lite-Balanced /
  Low-Medium-High) as something a team standardizing "when to use high
  reasoning" guidance across tools will need to translate per surface.

### Claim 2: GitHub organization and enterprise owners can publish custom agents that Visual Studio automatically detects and adds to the agent picker for any eligible repository, without a per-repository import step

- **Evidence**: Stated in the changelog Highlights list; elaborated with UI
  detail (hover-to-preview, definition-file button) in the devblogs companion
  post.
- **Confidence**: settled (product fact, worded consistently across the
  changelog and companion post; requires a GitHub organization, stated
  explicitly in both)
- **Quote**: "Organization-level custom agents: GitHub organization and
  enterprise owners can publish custom agents for use across repositories in
  their organization. Visual Studio automatically detects these agents and
  shows both their descriptions and organization source in the agent picker.
  This functionality requires a GitHub organization."
  (github.blog changelog, raw HTML, retrieved 2026-08-30)
- **Quote (devblogs companion post, discovery UI)**: "Visual Studio
  automatically detects organization-level agents when you work in an
  eligible repository and adds them to the agent picker. Hover over an agent
  to see its description and organization source, or select the definition
  button to open its definition file."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-30)
- **Our assessment**: This is a distribution mechanism for a *named,
  interactive Copilot Chat agent surfaced in the agent picker* — distinct from
  the org-level custom agent mechanism `docs-ghaw-copilot-agent-files.md`
  Claim 8 already documents for GitHub Agentic Workflows: that source's
  "centralized agent file libraries" require each importing workflow to
  declare an explicit `imports: - owner/repo/path@ref` reference pinned to a
  tag or commit (Claims 2–4 of that note), a deliberate, per-workflow,
  version-pinned pull. Visual Studio's organization-level custom agents are
  automatically detected and pushed into the agent picker for any eligible
  repository with no import declaration at all — a push/auto-discovery model
  rather than gh-aw's explicit-pin/pull model, for a different kind of agent
  (interactive IDE chat agent vs. gh-aw's automated-workflow agent). Neither
  source states whether these are the same underlying "Copilot Agent File"
  format (`.github/agents/*.md`, per `docs-ghaw-copilot-agent-files.md` Claim
  1) — this is a documentation gap worth flagging rather than assuming
  either way. For Ch02 (Harness Engineering — Custom Agent Distribution):
  document organization-level custom agents as a fourth agent/skill
  distribution model in the corpus (alongside directory-path discovery,
  registry installation, and built-in workload-gated skills from
  `docs-github-copilot-vs-july-2026.md` Claim 2's cross-reference chain),
  and note the open question of format compatibility with gh-aw's
  `.github/agents/` convention as something the guide should not assert
  without further sourcing.

### Claim 3: Practitioners can open the Copilot Usage window from the context window in the prompt box and select "View all Copilot usage" to jump to full plan details, with refined notifications for approaching a usage limit

- **Evidence**: Stated in the changelog Highlights list and the devblogs
  companion post, worded consistently across both.
- **Confidence**: settled (product fact, worded consistently across the
  changelog and companion post)
- **Quote**: "Access your Copilot usage: Open the context window from the
  Copilot prompt box, then select View all Copilot usage to see your full
  plan details. Refined notifications also make it clearer when you are
  approaching a limit and what options are available."
  (github.blog changelog, raw HTML, retrieved 2026-08-30)
- **Quote (devblogs companion post, framing)**: "Curious how much of your
  Copilot plan you have used? Open the context window from the prompt box,
  then select View all Copilot usage to jump to your full plan details.
  Usage notifications are easier to act on too, so you will know when you
  are close to your limit and what options you have to keep working."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-30)
- **Our assessment**: This is an incremental refinement to the "refreshed
  Copilot Usage window" `docs-github-copilot-vs-june-2026.md` Claim 1 already
  documents for the June 2026 Visual Studio update (real-time, token-based
  usage against usage-based billing, with proactive limit alerts). The change
  here is the entry point — accessible directly from the context-window
  indicator in the prompt box (the same ring/context UI element
  `docs-github-copilot-vs-may-2026.md` Claim 7 documents) rather than only
  via "Copilot badge menu > Copilot Usage" as June's source stated — plus
  "refined notifications." Neither source quantifies what "refined" changed
  concretely. For Ch01 (Daily Workflows): update the existing "budget
  visibility habits" guidance (context ring + Copilot Usage window) to note
  the two are now reachable from the same UI entry point, reinforcing them as
  a single combined habit rather than two separate checks.

### Claim 4: The model picker now supports pinning favorite models and collapsing less-used ones, plus a "Manage models" view showing capabilities, context window sizes, cost information, and controls for both Copilot and custom models

- **Evidence**: Stated in the changelog Highlights list only — the devblogs
  companion post does not mention this feature (confirmed by direct
  inspection of the companion post's raw-HTML-derived text, which covers
  thinking effort, organization-level agents, Copilot usage, worktrees, and
  submodules, but not model-picker pinning/collapsing).
- **Confidence**: settled (product fact, from the official changelog only)
- **Quote**: "Better model control: Pin favorite models, collapse models you
  use less often, and select Manage models for a detailed view. The
  management view includes model capabilities, context window sizes, cost
  information, and controls for Copilot and custom models."
  (github.blog changelog, raw HTML, retrieved 2026-08-30)
- **Our assessment**: "Manage models" as a picker entry point already exists
  in VS Code, but for a different purpose: `docs-github-copilot-byok-vscode.md`
  (Concrete Artifacts, "BYOK Setup in VS Code") documents "Manage Models" as
  the VS Code Chat language-model-picker action used to *add* a BYOK provider
  model. Visual Studio's August "Manage models" view is broader in stated
  scope — it surfaces capability, context-window-size, and cost metadata for
  models already available (Copilot and custom/BYOK alike), not only a
  provider-addition flow. The identical UI label across two different
  Copilot IDE surfaces, doing overlapping but not identical jobs, is worth
  noting for practitioners who move between VS Code and Visual Studio and
  expect "Manage models" to mean the same thing in both. For Ch01 (Daily
  Workflows): document pin/collapse plus the "Manage models" detail view as
  the recommended way to curate a large model roster in Visual Studio,
  cross-referencing cost/context-window visibility that previously required
  checking vendor documentation separately.

### Claim 5: A named "Git agent" can review uncommitted changes or commits before a pull request is opened, surfacing inline editor findings and a navigable list in Git Changes, with results discussable in Copilot Chat, and works with both GitHub and Azure DevOps repositories

- **Evidence**: Stated in the changelog Highlights list only — the devblogs
  companion post does not mention this feature at all (confirmed by direct
  inspection of the companion post's raw-HTML-derived text).
- **Confidence**: settled (product fact, from the official changelog); the
  source does not state whether the "Git agent" is the same review engine as
  "GitHub Copilot code review" named in prior VS updates or a separately
  branded feature, so that detail is unconfirmed
- **Quote**: "Review changes and commits with the Git agent: Ask the Git
  agent to review uncommitted changes or commits before you open a pull
  request. Findings appear inline in the editor with a navigable list in Git
  Changes. You can continue the Copilot Chat conversation to understand or
  address each suggestion. Reviews work with GitHub and Azure DevOps
  repositories."
  (github.blog changelog, raw HTML, retrieved 2026-08-30)
- **Our assessment**: This is a fourth distinct Copilot review surface in the
  corpus for Visual Studio specifically, and broader in scope than the third:
  PR-level review (`docs-github-copilot-code-review-comment-ux.md`,
  `docs-github-copilot-code-review-config-controls.md`), the July 2026
  selection-scoped "Review Selection" feature explicitly stated to be
  "powered by GitHub Copilot code review" (`docs-github-copilot-vs-july-2026.md`
  Claim 3, scoped to a single editor selection), and now this Git agent,
  scoped to the full set of uncommitted changes or a specific commit —
  broader than a selection, narrower than a PR diff, and explicitly framed as
  a pre-PR gate ("before you open a pull request"). Unlike Claim 3 of the
  July note, this changelog entry does not state the underlying engine is
  "GitHub Copilot code review" — it uses the distinct name "Git agent"
  throughout, which this note treats as a genuinely open question rather than
  assuming continuity with the code-review engine. The "GitHub and Azure
  DevOps repositories" scope parallels the platform-expansion pattern
  `docs-github-copilot-code-review-azure-repos.md` documents for PR-triggered
  Azure Repos code review (technical preview, June 2026), extending
  cross-platform review support to this new pre-PR, local-changes surface.
  For Ch01 (Daily Workflows): document the Git agent as the recommended
  pre-PR review step for the full set of uncommitted changes or a specific
  commit — broader coverage than Review Selection, still local and prior to
  PR creation, distinct from the eventual PR-triggered review. For Ch04:
  flag the "Git agent" naming as an open question for a future source note —
  whether GitHub is introducing a new named agent product (joining Plan
  agent, the SDK-based Agent (Preview), and the C++ Modernization agent) or
  reusing the code-review engine under new branding is not resolved by this
  source.

### Claim 6: Visual Studio now natively supports Git worktrees — creating an isolated working directory per branch from the Git Repository window, openable in the current window or a new Visual Studio instance, and listed alongside branches throughout the Git UI

- **Evidence**: Stated only in the devblogs companion post's dedicated
  "Worktrees: work on multiple branches at once" section; entirely absent
  from the changelog (confirmed by direct inspection of the raw-HTML-derived
  changelog transcript — no "worktree" text appears anywhere in it).
- **Confidence**: settled (product fact, from the official companion blog
  post, with a concrete UI mechanism described)
- **Quote**: "Git worktree support gives each branch its own working
  directory, so your current changes stay in place while you switch to
  another task. In the Git Repository window, right-click a branch and
  select New Worktree From. You can create the worktree from a new or
  existing branch, or start from a commit in the history graph. Open it in
  the current window or a new Visual Studio instance when you want both
  branches side by side. When the extra working directory is no longer
  needed, right-click it and select Delete Worktree. Your worktrees appear
  alongside branches in the Git Repository window, branch picker, and
  repository picker."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-30)
- **Our assessment**: This is a third distinct worktree-for-agentic-work
  surface in the corpus, but with a materially different framing than the
  other two: the VS Code Agents window's worktree support is explicitly
  agent-session-scoped ("Start Copilot, Claude, or Codex sessions in a Git
  worktree, so each session can work in an isolated copy of your repository,"
  `docs-github-copilot-vscode-july-2026.md` Claim 1), and Copilot CLI's
  `/worktree` is explicitly framed as starting "a separate conversation"
  (`docs-github-copilot-weekly-releases-aug3-2026.md` Claim 9). Visual
  Studio's worktree feature, by contrast, is presented in both the devblogs
  post and (by its complete absence) the changelog as a general Git
  productivity feature — "so your current changes stay in place while you
  switch to another task" — with no stated connection to Copilot agent
  sessions at all. A practitioner could use it identically whether or not
  Copilot is involved. For Ch02 (Harness Engineering — Parallel Sessions):
  document Visual Studio's worktree support as a general-purpose enabler for
  running parallel agent sessions on different branches (open one worktree
  per branch in its own VS window, run an independent Copilot session in
  each) even though the source itself does not frame it that way — the
  practitioner value is the same isolation property the VS Code and CLI
  worktree features name explicitly for agent sessions, just reached via a
  Git-first rather than agent-first feature.

### Claim 7: Visual Studio now provides first-class Git submodule management — a dedicated Submodules section in the Git Repository window with add/update/delete actions, automatic discovery on open, and read-only-by-default access requiring an explicit opt-in setting to enable edits

- **Evidence**: Stated only in the devblogs companion post's dedicated "Git
  submodule support" section; entirely absent from the changelog (confirmed
  by direct inspection of the raw-HTML-derived changelog transcript).
- **Confidence**: settled (product fact, from the official companion blog
  post, with a concrete configuration mechanism and default-state described);
  the post itself calls this "the first milestone for the experience, with
  more improvements planned," so scope is explicitly partial
- **Quote**: "Visual Studio now gives submodules a dedicated section in the
  Git Repository window, better visibility in Git Changes, and a repository
  picker that clearly shows the parent-child hierarchy. From the Submodules
  section, you can add, update, and delete submodules. Visual Studio
  discovers them automatically when you open a solution or folder and keeps
  them out of the general local repositories list, reducing clutter."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-30)
- **Quote (read-only default and opt-in)**: "Submodules are read-only by
  default. To make changes inside them, go to Tools > Options > Source
  Control > Git, find Automatically activate multiple repositories, and
  select Yes, include submodules. This is the first milestone for the
  experience, with more improvements planned."
  (devblogs.microsoft.com companion post, raw HTML, retrieved 2026-08-30)
- **Our assessment**: No prior corpus source documents IDE-level Git
  submodule management as a Copilot-adjacent or general developer-experience
  feature; the corpus's only prior submodule mentions
  (`docs-ghaw-checkout-reference.md`) are in an unrelated context — a
  `checkout:` frontmatter field controlling `actions/checkout` submodule
  fetching in automated gh-aw workflow jobs, not interactive IDE submodule
  browsing or editing. This is not an AI feature at all — like the MSVC
  toolset-discovery fix `docs-github-copilot-vs-july-2026.md` Claim 6
  documents, it is a general IDE capability bundled into the same monthly
  Copilot-branded changelog cycle via the devblogs companion post, and
  further evidence (per that note's Claim 6 assessment) that GitHub uses the
  Visual Studio blog as a general product-update channel that the curated
  github.blog Copilot changelog then edits down from. The read-only-by-default
  posture is a deliberate safety default: a practitioner opening a solution
  with submodules cannot accidentally modify submodule content without an
  explicit opt-in setting change. For teams whose repositories use
  submodules and who are evaluating whether an agent working in Visual
  Studio could inadvertently modify submodule content: this default should
  mean no, unless "Automatically activate multiple repositories" has been
  explicitly enabled — though this changelog source does not state whether
  Copilot agent sessions (Plan agent, Agent mode, the new Git agent) respect
  this same read-only default or operate through a different file-write path
  that bypasses it.

## Concrete Artifacts

### August 2026 Visual Studio Copilot Release — Feature/Source Map

```
Source: github.blog changelog (2026-08-28) + devblogs.microsoft.com companion
        post ("Visual Studio August Update — Work Smarter Across Models and
        Branches"), both retrieved 2026-08-30

FROM CHANGELOG "HIGHLIGHTS" (all five; also present in devblogs post unless noted):
  - Thinking effort controls (Low/Medium/High)         [Claim 1]
  - Organization-level custom agents                   [Claim 2]
  - Access your Copilot usage                          [Claim 3]
  - Better model control (pin/collapse/Manage models)  [Claim 4] — changelog only
  - Git agent code review (pre-PR, uncommitted/commits) [Claim 5] — changelog only

FROM DEVBLOGS COMPANION POST ONLY (not in changelog Highlights list):
  - Git worktree support                                [Claim 6]
  - Git submodule support (first milestone)             [Claim 7]

AVAILABILITY (changelog, applies to all five Highlights items):
  "This update is available to users on all GitHub Copilot plans, including
  Copilot Free, Student, Pro, Pro+, Max, Business, and Enterprise."

"WHAT'S NEXT" SECTION (changelog): no concrete roadmap items disclosed —
points to the Visual Studio blog for future roadmap updates and feedback
channels. No claim extracted; content-free beyond a pointer.

CHANGELOG INTRO SENTENCE (not itself a claim, but frames the release):
  "August 2026 brought more control over how GitHub Copilot reasons, which
  models you use, how teams share specialized agents, and when you ask for a
  code review."
```

### Git Worktree Workflow (Visual Studio, August 2026)

```
Source: devblogs.microsoft.com companion post, retrieved 2026-08-30

Entry point: Git Repository window → right-click a branch → "New Worktree From"

Create from: a new branch, an existing branch, or a commit in the history graph
Open in:     the current Visual Studio window, OR a new Visual Studio instance
             (side-by-side branch work)
Remove:      right-click the worktree → "Delete Worktree"
Visibility:  worktrees appear alongside branches in the Git Repository window,
             the branch picker, and the repository picker
Stated motivation (verbatim): "Ever stashed half-finished work just to
investigate another branch? Git worktree support gives each branch its own
working directory, so your current changes stay in place while you switch to
another task."
```

### Git Submodule Support (Visual Studio, August 2026 — "first milestone")

```
Source: devblogs.microsoft.com companion post, retrieved 2026-08-30

Discovery:   automatic, on opening a solution or folder; kept out of the
             general local repositories list
UI:          dedicated "Submodules" section in Git Repository window;
             visibility in Git Changes; repository picker shows parent-child
             hierarchy
Actions:     add, update, delete submodules (from the Submodules section)
Default:     READ-ONLY
Enable edits: Tools > Options > Source Control > Git >
              "Automatically activate multiple repositories" >
              "Yes, include submodules"
Explicitly partial: "This is the first milestone for the experience, with
more improvements planned."
```

## Cross-References

### Cross-reference verification notes

Claims cited from `docs-github-copilot-1m-context-reasoning-levels.md`,
`docs-github-copilot-cca-reasoning-level.md`,
`docs-github-copilot-code-review-effort-levels-ga.md`,
`docs-ghaw-copilot-agent-files.md`, `docs-github-copilot-vs-june-2026.md`,
`docs-github-copilot-vs-may-2026.md`, `docs-github-copilot-byok-vscode.md`,
`docs-github-copilot-vs-july-2026.md`,
`docs-github-copilot-code-review-comment-ux.md`,
`docs-github-copilot-code-review-config-controls.md`,
`docs-github-copilot-code-review-azure-repos.md`,
`docs-github-copilot-vscode-july-2026.md`,
`docs-github-copilot-weekly-releases-aug3-2026.md`, and
`docs-ghaw-checkout-reference.md` were re-read directly in those notes before
citing (per MINER.md §4b); claim numbers are counted top-to-bottom in
document order as they appear in each cited note.

- **Extends**:
  - `docs-github-copilot-1m-context-reasoning-levels.md` (Claims 2–3),
    `docs-github-copilot-cca-reasoning-level.md` (Claims 1–3), and
    `docs-github-copilot-code-review-effort-levels-ga.md` (Claims 1–2): Claim
    1 (Low/Medium/High thinking effort) is a fourth distinct reasoning-level
    naming scheme across the corpus's now five-plus documented Copilot
    surfaces with this control.
  - `docs-ghaw-copilot-agent-files.md` (Claim 8, centralized agent file
    libraries via explicit `@ref`-pinned imports): Claim 2 (organization-level
    custom agents, auto-detected with no import step) is a contrasting
    push/auto-discovery distribution model for a different kind of agent
    (interactive IDE chat agent vs. gh-aw automated-workflow agent).
  - `docs-github-copilot-vs-june-2026.md` (Claim 1, Copilot Usage window) and
    `docs-github-copilot-vs-may-2026.md` (Claim 7, context-window ring icon):
    Claim 3 (Copilot usage access from the context window) links the two
    previously separate budget-visibility UI elements to a single entry
    point.
  - `docs-github-copilot-byok-vscode.md` (Concrete Artifacts, "Manage Models"
    VS Code picker action): Claim 4 (Visual Studio's pin/collapse/"Manage
    models" view) uses the identical "Manage models" label for a broader,
    not-BYOK-specific purpose.
  - `docs-github-copilot-vs-july-2026.md` (Claim 3, Review Selection,
    explicitly "powered by GitHub Copilot code review") and
    `docs-github-copilot-code-review-azure-repos.md` (Claim 1, Azure Repos
    technical preview): Claim 5 (Git agent) is a fourth VS review surface,
    broader in scope than Review Selection and explicitly cross-platform
    (GitHub + Azure DevOps) like the Azure Repos preview, but the source
    does not confirm it shares the code-review engine Review Selection names
    explicitly.
  - `docs-github-copilot-vscode-july-2026.md` (Claim 1, VS Code Agents
    window worktree support) and
    `docs-github-copilot-weekly-releases-aug3-2026.md` (Claim 9, Copilot CLI
    `/worktree`): Claim 6 (Visual Studio Git worktree support) is a third
    worktree surface, framed as a general Git feature rather than an
    agent-session feature, unlike the other two.

- **Corroborates**: None beyond the "Extends" relationships above — no
  existing corpus note makes an independent, separately-sourced claim that
  this source's claims directly restate without adding new detail.

- **Contradicts**: None identified and none filed. No claim in this source
  opposes an existing corpus position; the "Manage models" label reuse
  (Claim 4) and the ambiguous "Git agent" vs. "Copilot code review" engine
  naming (Claim 5) are flagged as open documentation questions in their
  respective assessments, not as contradictions — no existing source note
  makes an affirmative claim that these two labels/engines are identical or
  distinct, so there is nothing to contradict.

- **Novel**:
  - **Low/Medium/High as Visual Studio's explicit thinking-effort tier
    labels** (Claim 1): the corpus's most prescriptive reasoning-level
    naming and task-type guidance to date.
  - **Organization-published custom agents auto-detected in the agent
    picker with no import step** (Claim 2): first corpus documentation of a
    push-model agent distribution mechanism for an interactive Copilot Chat
    agent, distinct from gh-aw's explicit-import model.
  - **A named "Git agent" reviewing uncommitted changes or commits before a
    PR exists** (Claim 5): first corpus documentation of a pre-PR review
    surface broader than a single selection but scoped to local Git state
    rather than a diff, under a name not previously used in the corpus.
  - **Native Git worktree support in Visual Studio, framed as a general Git
    feature rather than an agent-session feature** (Claim 6): first corpus
    Visual Studio worktree documentation, and the first worktree feature in
    the corpus with no stated connection to agent sessions at all.
  - **First-class Git submodule management in an IDE, read-only by default**
    (Claim 7): first corpus documentation of interactive IDE submodule
    tooling of any kind (the only prior corpus submodule mention is an
    unrelated `actions/checkout` config field for automated workflows).

## Guide Impact

- **Chapter 04 (Context Engineering — Reasoning Controls)**: Add Visual
  Studio's Low/Medium/High thinking-effort labels and task-type guidance
  (Claim 1) to the guide's cross-surface reasoning-level comparison, and
  explicitly flag that GitHub has not standardized naming for this control
  across VS Code/CLI/app, CCA, code review, and Visual Studio — a team
  writing "when to use high reasoning" guidance needs a per-surface
  translation table, not one universal instruction.

- **Chapter 02 (Harness Engineering — Custom Agent Distribution)**: Add
  organization-level custom agents (Claim 2) as a distribution model distinct
  from gh-aw's explicit `@ref`-pinned agent file imports, and note the open
  question of whether the two share a file format — do not assert
  compatibility without further sourcing.

- **Chapter 01 (Daily Workflows)**:
  - Update budget-visibility guidance to note the Copilot usage view and the
    context-window ring are now reached from the same UI entry point (Claim
    3).
  - Add the Git agent (Claim 5) as the recommended pre-PR review step for
    the full set of uncommitted changes or a specific commit, positioned
    between Review Selection (single-selection scope) and PR-triggered
    review (full-diff scope, requires an open PR).
  - Add pin/collapse and the "Manage models" detail view (Claim 4) as the
    recommended way to curate a large model roster in Visual Studio, noting
    the same UI label means something narrower (BYOK provider setup only) in
    VS Code.

- **Chapter 02 (Harness Engineering — Parallel Sessions)**: Document Visual
  Studio's native Git worktree support (Claim 6) as a general-purpose
  enabler for running parallel Copilot sessions on separate branches (one
  worktree per branch, each in its own VS window), even though the source
  itself frames it as a Git productivity feature rather than an agent
  feature — the practical isolation property is the same one VS Code and
  Copilot CLI name explicitly for agent sessions.

- **Chapter 07 (Security & Governance)**: Note the read-only-by-default
  posture for Git submodules (Claim 7) as a relevant safety default for
  teams evaluating whether an agent session in Visual Studio could modify
  submodule content — flag as an open question whether Copilot agent write
  operations (Plan agent, Agent mode, the new Git agent) respect this same
  default, since the source does not address agent-initiated writes
  specifically.

## Extraction Notes

1. **Raw HTML fetched via `curl`, not WebFetch's AI-summarized output**: An
   initial WebFetch call to the primary changelog returned a condensed,
   restructured summary that fabricated structural framing not present in
   the source (e.g., a "Reading time: 2 minutes" / "Author: Not listed"
   metadata block styled like a generic article template, and a "What's
   Next" section rendered as if the changelog's actual "What's next for
   Copilot in Visual Studio" heading had different content). Following the
   precedent in `docs-github-copilot-vs-july-2026.md` Extraction Note 1 and
   `docs-github-copilot-weekly-releases-aug3-2026.md` Extraction Note 1, both
   the changelog and the devblogs companion post were re-fetched via `curl`
   with a browser user-agent, and body text was extracted from the raw HTML
   using BeautifulSoup (isolate the `<article>` element, strip
   `<script>`/`<style>`/`<nav>`/`<footer>`, convert to newline-joined plain
   text). All quotes in this note are taken from that raw-HTML-derived plain
   text, cross-checked against the canonical URLs. On a side-by-side
   comparison, the WebFetch summary's five bullet claims turned out to be
   substantively accurate paraphrases of the real Highlights list (no
   fabricated features), but the surrounding framing (reading time, author
   line, "What's Next" content) was templated filler not present in the
   actual page — a caution for future extractions that WebFetch summaries
   can mix accurate paraphrase with invented structural elements in the same
   response.

2. **One companion page followed; two other links were not**: The changelog
   links to three pages — the devblogs.microsoft.com Visual Studio blog post
   (Copilot- and Git-feature-specific, followed and extracted above), a
   general GitHub Copilot plans/pricing page
   (`docs.github.com/copilot/get-started/plans`), and
   `learn.microsoft.com/visualstudio/releases/2026/release-notes` (general
   Visual Studio release notes, not Copilot-specific). Consistent with the
   precedent set in the June and July 2026 VS notes for this same
   release-notes link, neither general-purpose link was followed — the
   changelog plus its Copilot/Git-specific companion post is the complete
   AI-and-Git-feature record for this release cycle.

3. **Two features exist only in the companion post, not the changelog's own
   Highlights list**: Git worktree support (Claim 6) and Git submodule
   support (Claim 7) do not appear anywhere in the github.blog changelog
   text — confirmed by direct inspection of the raw-HTML-derived changelog
   transcript (searched for "worktree" and "submodule," zero matches in the
   changelog). This mirrors the same devblogs-only pattern documented in
   `docs-github-copilot-vs-july-2026.md` Extraction Note 3 (branch
   attachment, MSVC toolset discovery) and `docs-github-copilot-vs-june-2026.md`
   Extraction Note (color-emoji rendering) — GitHub's github.blog Copilot
   changelog continues to be edited down to a curated subset of what the
   fuller Visual Studio devblogs post covers, in this case omitting two
   entire Git-workflow features that are not AI/Copilot features at all.

4. **"Git agent" naming not resolved against prior "Copilot code review"
   terminology**: Claim 5's assessment explicitly treats the relationship
   between the new "Git agent" name and the "GitHub Copilot code review"
   engine named in `docs-github-copilot-vs-july-2026.md` Claim 3 as an open
   question rather than assuming identity or difference — the August 2026
   source simply does not say, and MINER.md §2a/§4b both caution against
   reconstructing claims the source does not make.

5. **No contradictions identified**: Cross-referenced against all existing
   VS/VS Code Copilot notes, the reasoning-level notes (1M-context, CCA,
   code-review effort levels), the code-review governance and Azure Repos
   notes, the gh-aw custom-agent-files note, and the BYOK/VS Code
   model-management note. No claim in this source opposes an existing
   corpus position. No contradiction issue filed.

6. **Three Prospector triage comments, all considered**: The issue carries
   three triage comments from the same day (2026-08-30), rating novelty
   "high," "medium," and "high" respectively, with progressively more
   specific extraction guidance (the third asks explicitly for parallels to
   `docs-github-copilot-vs-may-2026.md` and for platform-scope flags on
   breaking changes/deprecations). This extraction follows the combined
   guidance from all three: Ch01/02/04 relevance, extraction of concrete
   capabilities/UI changes with specificity, and comparison against the May
   2026 update where relevant (Claim 3's cross-reference to the May context-
   window ring icon). No breaking changes or deprecations were found in
   either source for this release.
