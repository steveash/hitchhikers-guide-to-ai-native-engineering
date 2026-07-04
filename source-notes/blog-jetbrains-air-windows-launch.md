---
source_url: https://blog.jetbrains.com/air/2026/06/jetbrains-air-lands-on-windows/
source_type: blog-post
title: "JetBrains Air lands on Windows"
author: Ivan Tiutiundzhi
date_published: 2026-06-29
date_extracted: 2026-07-04
last_checked: 2026-07-04
status: current
confidence_overall: anecdotal
issue: "#1494"
---

# JetBrains Air lands on Windows

> JetBrains announces Windows availability for Air, its dedicated agent-first
> development environment, and uses the launch post to restate Air's three
> core workflow primitives — plan-mode task specs saved to markdown, parallel
> agent execution in isolated Git worktrees, and cross-agent code review where
> one agent implements and another leaves inline comments — as a single
> coherent product surface rather than three separate features.

## Source Context

- **Type**: blog-post (JetBrains AI blog, product/release announcement,
  published June 29, 2026; author Ivan Tiutiundzhi)
- **Author credibility**: JetBrains staff writer announcing JetBrains' own
  product (Air). Authoritative for what Air's UI does and what JetBrains
  chose to ship for Windows. Not an independent or third-party account of
  how well these workflows perform in practice — no user metrics, adoption
  numbers, or comparative data are given. This is marketing copy for a
  platform-availability milestone, not a practitioner report.
- **Scope**: Covers the Windows release of Air (x64/ARM64 downloads),
  restates three existing Air workflow features (plan mode, parallel
  worktree execution, cross-agent review) as context for why the release
  matters, and describes Windows-specific stability investment. Does NOT
  cover: pricing, which underlying agents are supported, benchmark or
  adoption data, macOS/Linux-specific differences, or any first-hand account
  of using these workflows on a real task. A linked companion post
  (`blog-jetbrains-air-agent-first-journey.md`, see below) supplies the
  first-hand account this post lacks.

## Extracted Claims

### Claim 1: Air is positioned as "agent-agnostic," letting a developer use multiple leading AI coding agents inside one dedicated agent-first environment rather than one agent tied to one tool
- **Evidence**: Direct framing statement in the article's product description.
- **Confidence**: anecdotal (vendor product positioning, not independently measured)
- **Quote**: "Air is built for agent-agnostic development – you can use leading AI coding agents to implement features, fix bugs, investigate code, generate changes, and review results in a dedicated agent-first development environment."
- **Our assessment**: This is consistent with the pattern already documented in
  `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` and
  `blog-jetbrains-codex-recommended-agent.md`, where JetBrains' own IDE
  plugins increasingly support multiple agent backends (Codex, Junie,
  Claude) behind a single picker. Air appears to be JetBrains betting on the
  same agent-agnostic positioning at the level of a standalone product
  rather than an IDE plugin.

### Claim 2: JetBrains frames Air as filling a gap between running agents in a bare terminal and working inside a full traditional IDE
- **Evidence**: Direct framing statement describing the product's niche.
- **Confidence**: anecdotal (positioning claim, no comparative evidence offered)
- **Quote**: "The Air desktop app fills the gap between running agents in the terminal and working in a full IDE."
- **Our assessment**: This names a real practitioner pain point (terminal
  agent sessions lack code-navigation context; full IDEs weren't designed
  around agent-first workflows) but the post gives no evidence — no user
  testimony, no feature comparison table — that Air actually closes this
  gap better than existing IDE-plugin approaches (e.g., the GitHub Copilot
  JetBrains plugin documented across three prior source notes in this
  corpus). Treat as a positioning claim to be weighed against practitioner
  reports, not a settled product fact.

### Claim 3: Air lets a developer run multiple agents simultaneously, each in its own isolated Git worktree and branch, so concurrent agent changes cannot conflict with each other
- **Evidence**: Direct feature description of parallel execution.
- **Confidence**: settled (concrete, verifiable product feature description; the worktree-isolation mechanism itself is a well-established pattern independently corroborated elsewhere in the corpus — see Cross-References)
- **Quote**: "Run agents simultaneously in separate Git worktrees. Each agent gets its own working directory and branch, so their changes stay independent and don't conflict."
- **Our assessment**: This is the most guide-relevant claim in the post. It
  matches the worktree-isolation mode already documented as a GitHub
  Copilot JetBrains-plugin feature in
  `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claim 2) and the
  general "git worktrees for isolation" pattern catalogued in
  `blog-addyosmani-code-agent-orchestra.md` (Claim 11). What's new here is
  that Air treats worktree isolation as the default mechanism for *all*
  parallel agent execution in a purpose-built environment, not an optional
  mode bolted onto an existing IDE's agent plugin.

### Claim 4: Air supports a cross-agent review workflow where one agent implements a task and a second, different agent reviews the result and leaves comments directly in the code
- **Evidence**: Direct feature description with a named example pairing.
- **Confidence**: settled (concrete product feature description)
- **Quote**: "Use one agent to implement a task and another to review the result. For example, you can ask Claude to handle the implementation and Codex to review the changes. The reviewing agent leaves comments directly in code."
- **Our assessment**: This is a concrete instance of the "agent-as-reviewer"
  pattern using two *different* named agent backends (Claude implementing,
  Codex reviewing) inside one product's UI, with comments surfaced as
  inline code annotations rather than a separate chat transcript. No prior
  source note in this corpus documents a single tool orchestrating a named
  cross-vendor implement/review pairing (Claude ↔ Codex) as a first-class,
  UI-supported workflow — see Cross-References → Novel.

### Claim 5: Air's plan mode lets a developer describe an implementation goal, which Air saves as an editable markdown execution plan before any agent begins implementing, supporting comments, references to code symbols/files, and uploaded context files
- **Evidence**: Direct feature description of the plan-mode workflow.
- **Confidence**: settled (concrete product feature description)
- **Quote**: "Start in _Plan_ mode and describe what you want to implement. Air saves your execution plan to a markdown file before implementation begins, so you can iterate on it, leave comments, reference classes, folders, files, docs, symbols, or exact lines, and upload files from your computer as additional context."
- **Our assessment**: This is a UI-native implementation of the "write a
  plan file before letting an agent execute" pattern that recurs
  throughout the corpus in ad hoc form (e.g., practitioners hand-maintaining
  a `PLAN.md` or task file for Ralph-loop-style agents). Air's contribution
  is making the plan artifact a first-class, structured, referenceable
  markdown file inside the IDE rather than a convention teams have to
  invent themselves.

### Claim 6: JetBrains invested specifically in Windows app stability over "the past few months" so Windows developers would not need workarounds to use Air reliably
- **Evidence**: Direct statement about engineering investment ahead of the Windows launch.
- **Confidence**: anecdotal (self-reported engineering effort, no stability metrics, crash rates, or before/after data given)
- **Quote**: "Over the past few months, we invested heavily in app stability. The goal was simple: make sure Windows developers can start using Air without workarounds."
- **Our assessment**: A bare assertion of investment with no supporting
  metric (crash-free session rate, bug count, beta feedback score). This
  reads as standard release-announcement language rather than evidence the
  guide should cite as a claim about actual reliability.

### Claim 7: Air for Windows is available as separate x64 and ARM64 downloads at the time of this post
- **Evidence**: Direct download links included in the post for both architectures.
- **Confidence**: settled (directly verifiable distribution fact at time of publication)
- **Quote**: "Download for x64 / Download for ARM64" (linked download buttons; exact button URLs point to `download.jetbrains.com` with `distribution=windows_x64` and `distribution=windows_aarch64` query parameters)
- **Our assessment**: Minor but concrete — confirms Air ships native ARM64
  builds alongside x64 at Windows launch, not an x64-only release with
  emulation. Low guide relevance beyond noting platform/architecture
  support.

## Concrete Artifacts

### Air's three restated workflow primitives (JetBrains, June 29, 2026)

```
1. Plan mode
   - Describe implementation goal in natural language
   - Air saves the plan to a markdown file before implementation starts
   - Plan supports: comments, references to classes/folders/files/docs/
     symbols/exact lines, uploaded context files
   - Developer selects which agent executes, and whether it runs locally
     or in a Git worktree

2. Parallel agent execution
   - Multiple agents run simultaneously
   - Each agent gets its own working directory (Git worktree) and branch
   - Changes stay independent; no conflicts between concurrent agent runs

3. Cross-agent review
   - One agent implements a task (example given: Claude)
   - A second, different agent reviews the result (example given: Codex)
   - Reviewing agent leaves comments directly in the code (inline, in-editor)
   - Developer can iterate and reassign work between agents

Source: "JetBrains Air lands on Windows," JetBrains AI blog, June 29, 2026
(Ivan Tiutiundzhi).
```

### Download availability

```
Windows x64:   download.jetbrains.com/product?code=AIR&latest&distribution=windows_x64&type=preview
Windows ARM64: download.jetbrains.com/product?code=AIR&latest&distribution=windows_aarch64&type=preview
```

## Cross-References

### Cross-reference verification notes
Claims cited from other source notes below were re-read directly in those
notes before citing (per MINER.md §4b); claim numbers are counted
top-to-bottom in document order as they appear in each cited note.

- **Corroborates**:
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` Claim 2: that note
    documents "worktree isolation mode runs the agent in a separate Git
    worktree, keeping changes isolated from the current branch" as a GitHub
    Copilot JetBrains-plugin feature (May 2026). This post's Claim 3
    describes the same underlying mechanism (agent-per-worktree isolation)
    as Air's default parallel-execution model, corroborating that
    worktree-per-agent isolation is becoming a standard pattern across
    JetBrains-adjacent tooling, not a one-off feature of a single product.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 11: that note lists "git
    worktrees for isolation" as one of five patterns practitioners should
    adopt immediately for multi-agent workflows. This post's Claim 3 is a
    vendor product shipping that exact pattern as a built-in, default
    feature rather than something a practitioner has to configure manually.
  - `blog-cursor-faire-cloud-agents.md` Claim 1: that note quotes a named
    engineer contrasting "running local agents with worktrees" (described
    as complicated to manage at scale) against Cursor's cloud-agent
    offering. This post's Claim 3 confirms worktrees remain the reference
    local-isolation mechanism that cloud-agent vendors position themselves
    against — Air is building a first-class UI around the same mechanism
    Cursor's case study treats as the thing worth escaping from at scale.

- **Contradicts**: None identified. No existing source note makes a claim
  that opposes anything asserted here.

- **Extends**:
  - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` and
    `blog-jetbrains-codex-recommended-agent.md`: both notes document
    JetBrains-adjacent tooling (the Copilot plugin, JetBrains AI Chat)
    supporting multiple selectable agent backends (Claude, Codex, Junie).
    This post's Claim 4 (Claude implements, Codex reviews, in the same
    session) extends that picture from "pick one agent per session" to "use
    two different agents in complementary roles within a single workflow" —
    a materially different interaction pattern than a single-agent picker.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md`: that note
    documents worktree/workspace isolation as a mode toggle inside an
    existing IDE's agent plugin. This post extends the same mechanism into
    a purpose-built, agent-first product (Air) where worktree-per-agent
    parallelism is the default rather than an opt-in mode.

- **Novel**:
  - **Named, cross-vendor implement/review agent pairing as a first-class
    UI workflow** (Claim 4: Claude implements, Codex reviews, in one tool):
    no prior source note documents a single product's UI explicitly
    demonstrating a *named* cross-vendor agent pairing (as opposed to two
    instances of the same agent, or a generic "an agent reviews another
    agent" description) for the implement/review split.
  - **Plan mode as a structured, referenceable, IDE-native markdown
    artifact** (Claim 5): the corpus has ad hoc `PLAN.md`/task-file
    conventions practitioners invent themselves (e.g., in Ralph-loop
    discussions), but no prior note describes an IDE building this as a
    structured feature with symbol/file/line referencing and file uploads
    built into the plan-authoring UI itself.

## Guide Impact

- **Chapter 03 (or wherever multi-agent workflow patterns live)**: Add
  Claim 4 (named cross-vendor implement/review pairing — Claude implements,
  Codex reviews, inline in-code comments) as a concrete example of the
  "agent reviews agent" pattern moving from ad hoc practitioner setups
  (chaining CLI sessions manually) to vendor-supported, named,
  cross-provider workflows inside one tool. Caveat clearly: this is a
  product capability description from JetBrains' own announcement post,
  with no practitioner outcome data (no metrics on review quality, defect
  catch rate, or time saved) — flag as anecdotal/emerging until a
  first-hand practitioner account is mined (see companion post below).

- **Chapter 04 (Developer experience / harness engineering)**: Add Claim 3
  (worktree-per-agent as the default parallel-execution mechanism in a
  purpose-built agent IDE) alongside the existing worktree-isolation
  citations from `docs-github-copilot-jetbrains-cli-agent-sessions.md` and
  `blog-addyosmani-code-agent-orchestra.md` as further evidence that
  worktree-per-agent isolation is converging into a standard convention
  across independently-built tools (a GitHub Copilot plugin, a general
  practitioner pattern list, and now a standalone product), not a
  one-vendor idiosyncrasy.

## Extraction Notes

1. **This is a thin, marketing-oriented release post**: it is a Windows
   platform-availability announcement, not a deep technical or practitioner
   piece. Most of its substantive content (Claims 1, 3, 4, 5) is a
   restatement of Air features already announced elsewhere by JetBrains,
   repackaged as context for the Windows release. This matches the
   Prospector's "medium novelty" / "product announcement" framing in the
   triage comments.
2. **One linked sub-page followed**: the post links to
   "My Journey to Agent-First Development With Air"
   (https://blog.jetbrains.com/air/2026/04/my-journey-to-agent-first-development-with-air/),
   a first-hand practitioner account with more substantive workflow detail
   (a 140-message chat exchange building a Gemini CLI feature, an explicit
   claim that "agents [are] extremely bad at code design, architecture, and
   following project patterns," and productivity commentary on working
   several tasks in parallel). That companion post is a stronger
   mining candidate in its own right — it was read here only far enough to
   confirm it doesn't change the claims extracted from the Windows-launch
   post itself, and its content is deliberately NOT claimed as this note's
   own extraction (no claims above are sourced to it). Recommend filing it
   as a separate source-submission issue if it isn't already queued, since
   its first-hand, concrete-metric content (140-message exchange,
   multi-day/dozens-of-comments review cycle) clears MINER.md's "specific
   claims with specific evidence" bar more convincingly than this launch
   post does.
3. **No download-link content beyond URLs was quotable as prose**: Claim 7's
   quote is the button label text, included for completeness per MINER.md
   §3 (concrete artifacts), not because it carries independent analytical
   weight.
4. **Two Prospector triage comments were present on the issue** (apparently
   a duplicate triage pass), both converging on the same novelty
   assessment (medium) and largely the same relevant chapters and
   overlapping notes; this note treats their union as the triage guidance
   and cites the overlapping notes named in both.
