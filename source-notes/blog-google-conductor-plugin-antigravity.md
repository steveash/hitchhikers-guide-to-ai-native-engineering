---
source_url: https://developers.googleblog.com/evolving-spec-driven-development-conductor-now-supports-antigravity/
source_type: blog-post
title: "Evolving Spec-Driven Development: Conductor Now Supports Antigravity"
author: Mahima Shanware, Sherzat Aitbayev, Jay Kornder (Google, Developer & Experiences team)
date_published: 2026-07-16
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: emerging
issue: "#1995"
---

# Evolving Spec-Driven Development: Conductor Now Supports Antigravity

> Google's first-party announcement that Conductor — its Spec-Driven
> Development (SDD) tool, previously a Gemini CLI-only extension — has
> become a portable plugin (skills, rules, MCP servers, hooks) that
> works across Antigravity CLI and Claude, trading strict command
> sequences for conversational interaction while keeping persistent
> `spec.md`/`plan.md` markdown artifacts as the underlying state, and
> citing an unquantified "higher success rate" on complex TerminalBench
> tasks.

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party
  product-evolution announcement, July 16, 2026)
- **Author credibility**: Three named Google engineers/PMs (Mahima
  Shanware and Sherzat Aitbayev, Senior Software Engineers; Jay Kornder,
  Group Product Manager — all "Developer & Experiences") writing on
  Google's own official developer blog about a Google-authored/maintained
  open-source tool. This is first-party vendor content describing a
  shipped feature transition, not independent practitioner evaluation.
  The tool itself (`gemini-cli-extensions/conductor` on GitHub) is
  publicly inspectable, which makes the architectural and command-level
  claims independently verifiable even though the "higher success rate"
  performance claim is not.
- **Scope**: Covers Conductor's transition from a Gemini-CLI-exclusive
  extension to a cross-tool plugin, the shift from command-driven to
  conversational interaction, cross-tool context portability, an
  installation command for Antigravity CLI, and a link to a hands-on
  Codelab. Does **not** cover: the TerminalBench methodology or
  percentage figures behind the "higher success rate" claim, MCP server
  or hook implementation details, or a walkthrough of the conversational
  UX in practice. To fill in the mechanics the blog post omits, this
  note also extracts the plugin's own GitHub README
  (`gemini-cli-extensions/conductor`), which documents the command
  reference, generated-artifact list, UX-adaptation layer, and token-cost
  caveat in more concrete detail than the announcement post.

## Extracted Claims

### Claim 1: Conductor has evolved from a Gemini CLI-only extension into a "Conductor Plugin" that packages skills, rules, MCP servers, and hooks, extending compatibility to tools such as Antigravity CLI
- **Evidence**: First-party product-evolution announcement in the post's
  opening section.
- **Confidence**: settled (a direct, falsifiable statement about what
  shipped — corroborated by the public GitHub repo's own README, which
  documents installation paths for both Antigravity and Claude Code)
- **Quote**: "Today, we are excited to announce the next phase of this
  journey: Conductor is evolving from a Gemini CLI extension into the
  Conductor Plugin. Plugins can include skills, rules, MCP servers, and
  hooks in a single package. Transitioning Conductor into a plugin
  creates a more fluid, conversational experience without sacrificing
  the procedural rigor of Spec-Driven Development (SDD). This also means
  Conductor is compatible with tools such as Antigravity CLI."
- **Our assessment**: This is the core, verifiable claim of the post —
  a packaging-format change (extension → plugin) that is the mechanism
  by which cross-tool support becomes possible. It is corroborated by
  the GitHub README's own "Repository Structure" section (`/skills`,
  `/rules`) and its explicit dual installation instructions for
  Antigravity and Claude Code (see Concrete Artifacts). This gives the
  claim a settled grade despite the source being vendor marketing,
  because the underlying artifact (the plugin repo) is public and
  matches the description.

### Claim 2: The plugin transition removes "the friction of strict command sequences," letting Conductor engage conversationally and dynamically generate context, specs, and plans as the user discusses feature requirements, rather than requiring memorized commands
- **Evidence**: First-party description under the "Driving SDD via a
  natural conversation" section heading.
- **Confidence**: emerging (a described UX shift with no before/after
  demo, transcript, or independent trial in the post itself)
- **Quote**: "By transitioning Conductor to a plugin, we are removing the
  friction of strict command sequences. Conductor will now engage with
  you conversationally, dynamically generating context, specs, and plans
  organically as you discuss your feature requirements."
- **Our assessment**: This is the single most guide-relevant claim in
  the post: it asserts that a structured, artifact-producing workflow
  (SDD) and a conversational interface are not in tension — the rigor
  moves from "the user must invoke the right slash command in the right
  order" to "the tool infers which artifact-generating step applies from
  the conversation." We cannot independently verify how reliably this
  inference works (no failure-mode discussion, no example of the tool
  guessing wrong), so we grade this emerging rather than settled. The
  GitHub README's "Getting Started (Natural Language Triggering)"
  section corroborates the mechanism exists (see Concrete Artifacts) but
  likewise gives no reliability data.

### Claim 3: Persistent Markdown artifacts (`spec.md`, `plan.md`) are unchanged by the conversational shift — "they aren't going anywhere" — only the process of creating and iterating on them becomes conversational, with the AI managing project state (updating context, checking off completed plan tasks) in the background
- **Evidence**: First-party description in the same "Driving SDD via a
  natural conversation" section, explicitly framed as a reassurance that
  the underlying artifact model persists.
- **Confidence**: settled (a direct statement about what does *not*
  change, which is the easier half of a product-transition claim to
  verify, and matches the artifact list in the GitHub README's "Usage &
  Lifecycle" section)
- **Quote**: "You still get the benefits of persistent Markdown
  artifacts—your spec.md and plan.md aren't going anywhere—but the
  process of creating and iterating on them is now as simple as chatting
  with your AI assistant. It intelligently knows when to update your
  context or check off a completed task in your plan, letting you focus
  on the architecture while the AI manages the project state in the
  background."
- **Our assessment**: This is a direct instance of the "spec/plan file
  as compressed, persistent context" pattern already documented in the
  guide (`guide/04-context-engineering.md`, "Specs and Plans as
  Compressed Context," ~lines 145-194) — see Cross-References. The novel
  element here is not the persistence pattern itself (already well
  covered in the corpus) but that Google is explicitly designing the
  *authoring interface* to that persistent state to be conversational
  rather than command-driven, while keeping the artifact format
  (versioned markdown) constant.

### Claim 4: Becoming a plugin breaks Conductor out of Gemini CLI exclusivity, making it "a portable, ecosystem-wide capability" whose shared configuration and development tracks persist across tools, so a workflow started in one tool can continue in another "without losing a single beat of context"
- **Evidence**: First-party description under "Conductor for Antigravity
  CLI and beyond."
- **Confidence**: emerging (an architecturally plausible claim — the
  state lives in versioned repo files, which are tool-agnostic by
  construction — but the post gives no demonstrated example of a
  mid-track handoff from one tool to another)
- **Quote**: "A benefit of transitioning Conductor to a plugin is that it
  breaks the workflow out to support multiple tools. Until now, Conductor
  has been exclusively tied to the Gemini CLI as an extension. By
  becoming a plugin, Conductor is now a portable, ecosystem-wide
  capability. Regardless of which tool you choose, your AI agent will
  understand the foundational documents about your project's
  architecture, guidelines, and goals. Your shared configuration and
  ongoing development tracks will persist seamlessly, meaning an
  AI-assisted workflow started in one tool can be continued in another
  without losing a single beat of context."
- **Our assessment**: This is the most concrete cross-tool-portability
  claim in the corpus for a spec/plan-file-based workflow. It follows
  mechanically from Claim 3 (state lives in repo-committed markdown, not
  in a tool's proprietary session state) — the claim is really "because
  the state is just files in your git repo, any tool that can read files
  can pick up the track." We buy the *mechanism* (this is consistent
  with how `blog-simonwillison-gemini-spark-antigravity.md` Claim 6
  describes Antigravity's own SDK/CLI/IDE stack as sharing a common
  runtime) but the specific "not losing a single beat of context" framing
  is marketing language not backed by a worked example in this source.

### Claim 5: The Conductor Plugin achieved "a higher success rate across the most complex subset of TerminalBench tasks compared to a user not using SDD," but no percentage, sample size, or methodology is given
- **Evidence**: First-party bullet under "What this means for your
  team," the post's only quantitative-sounding performance claim.
- **Confidence**: anecdotal (the post gives literally no number,
  methodology, task count, or comparison-group description — this is
  weaker than a self-labeled "illustrative benchmark" with mock figures,
  because there isn't even an illustrative figure to evaluate)
- **Quote**: "Improved task completion: The Conductor Plugin achieved a
  higher success rate across the most complex subset of TerminalBench
  tasks compared to a user not using SDD."
- **Our assessment**: This is the weakest claim in the post and should
  not be cited in the guide as evidence that SDD improves task
  completion — it is a directional assertion with zero supporting data.
  Contrast with `blog-google-adk-2-0-deterministic-workflows.md` Claim 5,
  which at least gives concrete (self-labeled illustrative, mock-API)
  token and latency figures for its workflow-vs-agent comparison; this
  Conductor claim gives no figures at all, only "TerminalBench" as the
  named benchmark and "the most complex subset" as an unspecified
  filter. Treat as an unverified vendor assertion, not evidence.

### Claim 6: Antigravity CLI installs the Conductor Plugin with the single command `agy plugins install https://github.com/gemini-cli-extensions/conductor`
- **Evidence**: First-party installation instructions in the "How to get
  started" section, corroborated by the identical command in the GitHub
  README's "Antigravity → End-User Installation" section.
- **Confidence**: settled (a directly reproducible command matching two
  independent first-party sources — the blog post and the linked repo's
  own README)
- **Quote**: "agy plugins install https://github.com/gemini-cli-extensions/conductor"
- **Our assessment**: A concrete, directly actionable artifact — see
  Concrete Artifacts for the full installation matrix (Antigravity vs.
  Claude Code, end-user vs. developer/live-sync installation).

### Claim 7: Conductor's lifecycle is organized into three phases — Context → Spec & Plan → Implement — driven by three primary namespaced slash commands: `/conductor:conductor-setup`, `/conductor:conductor-new-track`, `/conductor:conductor-implement`
- **Evidence**: GitHub README "Usage & Lifecycle" section, with each
  phase's generated artifacts enumerated explicitly (e.g.
  `conductor/product.md`, `conductor/tracks/<track_id>/spec.md`,
  `conductor/tracks/<track_id>/plan.md`).
- **Confidence**: settled (directly reproducible from the public
  repository, not a marketing claim — this is the tool's own command
  reference)
- **Quote**: "Instead of just writing code, Conductor ensures a
  consistent, high-quality lifecycle for every task: Context -> Spec &
  Plan -> Implement."
- **Our assessment**: This is the concrete mechanism underneath the
  blog post's more abstract "conversational SDD" framing — the blog post
  describes the *interaction style* becoming conversational, but the
  README shows the *underlying phase structure and artifact set* is
  unchanged from a traditional command-driven SDD tool. This three-phase
  structure (Context → Spec & Plan → Implement) is a slightly more
  granular version of the "Specify → Plan → Tasks → Implement" workflow
  already in the corpus from Osmani's "Good Spec" post (see
  Cross-References).

### Claim 8: Conductor includes a "smart revert" feature — a git-aware revert command that understands logical units of work (tracks, phases, tasks) rather than raw commit hashes — alongside two other named recovery flows (in-flight chat corrections, and a review command that appends a "Review Fixes" phase to `plan.md`)
- **Evidence**: GitHub README "Features" list and the "Best Practices
  for Task Corrections" section, which names and describes all three
  recovery flows plus the `/conductor:conductor-revert` command's
  specific behavior (resets task state back to pending `[ ]`).
- **Confidence**: settled (a documented, reproducible command behavior
  in the public repo, not a marketing claim)
- **Quote**: "Smart revert: A git-aware revert command that understands
  logical units of work (tracks, phases, tasks) rather than just commit
  hashes."
- **Our assessment**: This is a genuinely novel artifact for the corpus
  — a revert mechanism that operates on the SDD tool's own task-tracking
  abstraction (track/phase/task) layered on top of git, rather than on
  raw commit hashes. It directly extends the corpus's git-worktree and
  quality-gate patterns (`blog-addyosmani-code-agent-orchestra.md` Claim
  11) with a structured "undo" primitive scoped to the plan file's own
  units of work, not just `git revert`.

### Claim 9: Conductor adapts its interaction surface to the host tool's visual capabilities — interactive GUI modal dialogs in IDEs that support them (e.g. Antigravity), and structured bracketed-number text menus (e.g. `[1] Option A, [2] Option B`) in plain-text terminals such as Claude Code — with "zero configuration required"
- **Evidence**: GitHub README "Adaptive User Experience (UX Layer)"
  section, naming the mechanism ("View Layer UX Adapter") and both
  fallback modes explicitly.
- **Confidence**: settled (a documented, named component in the public
  repo — the `rules/` directory is cited as holding the visual-IDE
  adapter rules)
- **Quote**: "Graceful CLI Fallback: If you are operating in a plain text
  terminal console (such as Claude Code), Conductor automatically detects
  the console environment and adapts all interactive steps into clean,
  structured text-based choice menus with bracketed numbers (e.g., [1]
  Option A, [2] Option B)."
- **Our assessment**: This is the concrete implementation detail behind
  the blog post's cross-tool portability claim (Claim 4) — cross-tool
  support is not just "the same commands work everywhere," it requires a
  UX-adaptation layer that changes *how* Conductor solicits decisions
  from the user depending on which tool is hosting it. This is a
  reusable design pattern for any plugin/skill author targeting multiple
  agent harnesses with different interaction surfaces (GUI-capable IDE
  vs. plain terminal).

### Claim 10: Conductor's spec-driven approach increases token consumption, "especially in larger projects or during extensive planning and implementation phases," and the README directs users to check per-session token consumption via `/stats model` in compatible clients
- **Evidence**: GitHub README explicit `[!NOTE]`-flagged callout in the
  "Usage & Lifecycle" section.
- **Confidence**: settled (a direct, self-disclosed cost caveat from the
  tool's own maintainers, not a third-party measurement — but notable
  precisely because it is a vendor admitting a cost tradeoff rather than
  only advertising benefits)
- **Quote**: "Conductor's spec-driven approach involves reading and
  analyzing your project's context, specifications, and plans. This can
  lead to increased token consumption, especially in larger projects or
  during extensive planning and implementation phases."
- **Our assessment**: This is a useful counterweight to the blog post's
  purely upside-framed announcement — the tool's own documentation
  acknowledges that persistent, richly-structured context (the same
  `conductor/` directory tree of product/tech-stack/track files) is not
  free, and that cost scales with project size and planning depth. No
  magnitude is given (no token count, no percentage), so this should be
  cited in the guide as a qualitative caveat, not a quantified cost
  claim.

### Claim 11: Conductor's plugin architecture explicitly credits Keith Ballinger's open-source `.conductor` project as "the groundwork" for the repository
- **Evidence**: GitHub README "Resources" section, final bullet.
- **Confidence**: settled (a direct attribution statement in the public
  repo)
- **Quote**: "The team gratefully acknowledges Keith Ballinger's original
  .conductor project as the groundwork for this repository."
- **Our assessment**: This is a minor but notable provenance detail: a
  major-vendor SDD tool (Google-maintained, promoted on the official
  developer blog) traces its origin to a named individual practitioner's
  open-source project rather than being built ground-up inside Google.
  Worth flagging for anyone researching the lineage of the "persistent
  markdown spec/plan file" pattern in the corpus, though this note does
  not extract Ballinger's original project directly — that would require
  a separate source note if judged substantive enough.

## Concrete Artifacts

### Installation commands (verbatim from blog post and GitHub README)
```
# Antigravity CLI — end-user installation
agy plugins install https://github.com/gemini-cli-extensions/conductor

# Antigravity CLI — developer / live-sync install
git clone https://github.com/gemini-cli-extensions/conductor.git
cd conductor
mkdir -p ~/.gemini/config/plugins/ && ln -sfn "$(pwd)" ~/.gemini/config/plugins/conductor

# Claude Code — end-user installation
/plugin marketplace add gemini-cli-extensions/conductor
/plugin install conductor
```
Source: developers.googleblog.com (blog post installation command) and
`gemini-cli-extensions/conductor` GitHub README, "Installation Guide."

### Conductor command reference and generated artifacts (verbatim from GitHub README)
```
Command                          | Description                                        | Generated Artifacts
/conductor:conductor-setup       | Scaffolds the project; run once per project.       | conductor/product.md
                                                                                        | conductor/product-guidelines.md
                                                                                        | conductor/tech-stack.md
                                                                                        | conductor/workflow.md
                                                                                        | conductor/tracks.md
/conductor:conductor-new-track   | Starts a new feature/bug track.                    | conductor/tracks/<id>/spec.md
                                                                                        | conductor/tracks/<id>/plan.md
                                                                                        | conductor/tracks.md
/conductor:conductor-implement   | Executes tasks defined in the current track's plan.| conductor/tracks.md
                                                                                        | conductor/tracks/<id>/plan.md
/conductor:conductor-status      | Displays current progress of tracks file.          | Reads conductor/tracks.md
/conductor:conductor-revert      | Reverts a track, phase, or task via git history.   | Reverts git history
/conductor:conductor-review      | Reviews completed work against guidelines/plan.    | Reads plan.md, product-guidelines.md
```
Source: `gemini-cli-extensions/conductor` GitHub README, "Commands
Reference" table.

### Natural-language triggering examples (verbatim from GitHub README)
```
To Scaffold a Project:  "Let's create a new Conductor project" /
                         "Run setup for Conductor"
To Plan a Feature:      "Let's start a new track to add a login screen" /
                         "Create a plan for the dark mode track"
To Execute the Plan:    "Start implementing the active plan" /
                         "Proceed with the implementation"
To Check Progress:      "How is our track progress going?" /
                         "Show the current project status"
To Revert or Fix:       "Revert the last completed task" /
                         "Let's review the completed phase"
```
Source: `gemini-cli-extensions/conductor` GitHub README, "Getting
Started (Natural Language Triggering)."

## Cross-References

- **Corroborates**:
  - `guide/04-context-engineering.md` "Specs and Plans as Compressed
    Context" (~lines 145-194, sourced from
    `blog-french-owen-coding-agents-feb-2026` Claim 3,
    `blog-osmani-good-spec` Claim 1, `research-wasnotwas-context-compaction`
    Claim 5, `blog-sankalp-claude-code-20` Claim 6): Claim 3 of this note
    (persistent `spec.md`/`plan.md` survive the conversational-UX shift
    unchanged) is a first-party vendor confirmation, from a shipped
    third tool, of the same "plan file as the artifact that persists"
    pattern the guide already documents for Claude Code specifically —
    Conductor generalizes the same pattern across Antigravity CLI and
    Claude.
  - `blog-simonwillison-gemini-spark-antigravity.md` Claim 6 (the
    Antigravity ecosystem — desktop app, Go CLI, Python SDK, VS Code
    fork IDE — is described as sharing one underlying runtime): this
    note's Claim 4/Claim 9 cross-tool portability and UX-adaptation
    claims are consistent with an ecosystem where multiple front-end
    surfaces share common underlying state and tooling.

- **Contradicts**: None filed. See Extraction Notes for a considered,
  non-filed naming collision against
  `blog-addyosmani-code-agent-orchestra.md`, and a considered,
  non-filed nuance against that same note's Claim 7 (ETH Zurich
  AGENTS.md findings).

- **Extends**:
  - `blog-addyosmani-code-agent-orchestra.md` Linked Source 4 ("How to
    Write a Good Spec for AI Agents," which documents a "Specify → Plan
    → Tasks → Implement" spec-driven workflow and a three-tier
    Always/Ask-First/Never boundary system): this note's Claim 7
    (Conductor's Context → Spec & Plan → Implement lifecycle, with three
    namespaced slash commands and enumerated generated artifacts) is a
    concrete, shipped tool implementing the same generic SDD workflow
    shape that post described abstractly — Conductor is the first source
    in the corpus to show that workflow as an installable product with a
    public command reference rather than a described methodology.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 11 (git worktrees for
    isolation and quality gates as two of five recommended adoption
    patterns): this note's Claim 8 (`/conductor:conductor-revert`'s
    track/phase/task-scoped git-aware revert) is a more structured,
    product-shipped version of the "safe undo" half of that
    recommendation — reverting by the SDD tool's own logical work units
    rather than by raw commit hash.
  - `blog-google-io-2026-developer-keynote.md` Claim 4 (the Antigravity
    SDK provides "programmatic control over the Antigravity agent
    harness... deploy it on your own infrastructure") and Claim 2
    (Antigravity 2.0's built-in security controls): this note extends
    that broader Antigravity-platform picture with one specific
    plugin-ecosystem capability (Conductor) that now runs on top of it,
    and corroborates the general pattern of Google building a portable
    plugin/skill layer (skills, rules, MCP servers, hooks) across its
    agent tooling.

- **Novel**:
  - **A shipped, publicly-installable SDD tool that trades command-driven
    interaction for conversational triggering while keeping the same
    underlying markdown-artifact state model** (Claims 2, 3, 9): no
    prior corpus source documents a concrete product doing this — prior
    SDD-adjacent sources (Osmani's "Good Spec" post, the guide's own
    "Specs and Plans as Compressed Context" section) describe the
    artifact pattern or a command-driven workflow, not a natural-language
    trigger layer sitting on top of the same commands.
  - **Cross-agent-tool track portability as a stated design goal** (Claim
    4): the specific claim that a track (spec + plan + progress state)
    started in one CLI tool can be picked up in a different tool (e.g.
    started in Antigravity CLI, continued in Claude) without loss is new
    to the corpus — prior sources document single-tool state persistence
    (Claude Code's post-compaction plan-file re-injection) but not
    cross-tool handoff of the same persistent state.
  - **A named git-aware "smart revert" scoped to SDD logical work units**
    (Claim 8): distinct from the corpus's existing git-worktree-based
    isolation patterns, this is a revert mechanism aware of the SDD
    tool's own track/phase/task hierarchy, not just commit boundaries.
  - **An explicit, named UX-adaptation layer for a single plugin targeting
    both GUI-capable and plain-terminal agent hosts** (Claim 9): no prior
    corpus source documents a single tool/plugin author explicitly
    building and naming a component ("View Layer UX Adapter") whose job
    is to render the same underlying interaction as either GUI modals or
    bracketed-number text menus depending on host capability.

## Guide Impact

- **Chapter 04 (Context Engineering), "Specs and Plans as Compressed
  Context"** (`guide/04-context-engineering.md`, ~lines 145-194): add
  this source's Claim 3 and Claim 4 as evidence that the
  persistent-spec/plan-file pattern is now being generalized by a major
  vendor across multiple agent tools (Antigravity CLI, Claude), not just
  observed as an emergent practitioner workflow or a single harness's
  compaction-survival mechanism. Frame it as: "Google's Conductor plugin
  operationalizes this pattern as a shipped, cross-tool product —
  `spec.md`/`plan.md` generated and updated conversationally, but
  persisted as committed markdown that any supporting tool can read,"
  with the explicit caveat (Claim 5) that the tool's own quantified
  performance claim is unsubstantiated in the source and should not be
  cited as evidence the pattern improves task success.

- **Chapter 01 (Daily Workflows), "Carrying prior research into the
  session"** (`guide/01-daily-workflows.md`, ~lines 51-77, currently
  sourced from `blog-simonwillison-liteparse-browser` Claim 5): add
  Conductor's natural-language-triggering mechanism (this note's Claim 2
  and the "Getting Started (Natural Language Triggering)" artifact) as a
  named, productized alternative to Willison's manual `notes.md` → 
  `plan.md` handoff pattern — where Willison pastes prior-session output
  into a file and tells Claude Code to read it, Conductor's conversational
  layer is designed to infer when to create/update the equivalent
  artifacts from the ongoing conversation itself.

- **Chapter 02 (Harness Engineering)**: if this chapter is extended to
  cover plugin/skill authoring for multiple agent hosts, add Claim 9
  (the UX-adaptation layer rendering the same interaction as GUI modals
  vs. bracketed-number text menus depending on host) as a concrete
  design pattern for any team building a single plugin that must target
  both IDE-hosted and plain-terminal agent harnesses.

## Extraction Notes

- Read the full blog post via two independent extraction methods: (1)
  the WebFetch tool's small-model summarizer for an initial overview
  pass, and (2) a direct `curl` fetch of the raw HTML (stripped to plain
  text with a Python regex script), used to verify every `Quote` field
  above character-for-character against the source's own wording before
  use. The two passes agreed on substance; quotes above are taken from
  the raw-fetched plain text, not the summarizer output.
- Followed one linked resource beyond the blog post itself: the plugin's
  own GitHub repository README (`gemini-cli-extensions/conductor`,
  fetched via raw.githubusercontent.com), which is the primary source
  for Claims 7-11 and most of the Concrete Artifacts. This was judged
  substantive per MINER.md's "follow up to 5 linked pages that seem
  substantive" guidance, since the blog post itself gives almost no
  command-level or artifact-level detail — nearly all of the tool's
  actual mechanics live in the README, not the announcement. Did not
  follow the linked hands-on Codelab
  (`codelabs.developers.google.com/conductor-plugin`) — it is an
  interactive walkthrough format that extracts poorly via text fetch and
  would likely duplicate the README's command reference rather than add
  new claims.
- **Considered but did not file a contradiction** between this source
  and `blog-addyosmani-code-agent-orchestra.md`: that post's Claim 1
  uses "conductor" as a metaphorical mental model for *single-agent,
  real-time pairing* ("You used to pair with one AI. Now you manage an
  agent team" — conductor vs. orchestrator as two modes of human-AI
  interaction), whereas this source's "Conductor" is a specific,
  capitalized, Google-maintained product name for a spec-driven-development
  tool, unrelated in mechanism to Osmani's metaphor. This is the same
  category of naming collision already handled without a contradiction
  filing in `blog-google-adk-2-0-deterministic-workflows.md`'s
  Extraction Notes (for "Dynamic Workflows" as a name shared by an
  Anthropic feature and a Google ADK feature) — a term reused by two
  unrelated sources for two different things, not a factual disagreement
  about the same mechanism. No contradiction issue filed.
- **Considered but did not file a contradiction** between this source's
  Claim 2/Claim 3 (Conductor conversationally, automatically generates
  and updates `spec.md`/`plan.md`/context files) and
  `blog-addyosmani-code-agent-orchestra.md` Claim 7 (ETH Zurich finding
  that LLM-*generated* AGENTS.md/context files reduce success ~3% and
  increase cost 20%+, versus developer-written files improving success
  ~4%). These are not the same claim under conditioning variables removed:
  the ETH study concerns a single, largely-static, whole-repo context
  file (AGENTS.md) generated once and read repeatedly; Conductor's
  `spec.md`/`plan.md` are per-track, task-specific working documents
  that the user reviews and iterates on conversationally before
  implementation begins (the README's "Review plans before code is
  written, keeping you firmly in the loop" feature bullet), and Conductor
  additionally provides a review/revert loop absent from a passively-read
  AGENTS.md file. Treated as a conditioning-variable difference (document
  type and human-review-loop presence), not a contradiction, per
  MINER.md §4a's "conditioning variable" exclusion — flagged here for
  the Assayer/Smith to reconsider if either source is revisited.
- The blog post's TerminalBench claim (Claim 5) is the thinnest evidence
  in this note; flagged prominently above and in Guide Impact so it is
  not accidentally cited in the guide as a quantified result.
