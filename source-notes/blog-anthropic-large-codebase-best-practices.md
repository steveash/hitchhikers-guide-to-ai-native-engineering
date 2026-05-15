---
source_url: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
source_type: blog-post
title: "How Claude Code works in large codebases: Best practices and where to start"
author: Anthropic
date_published: 2026-05-14
date_extracted: 2026-05-15
last_checked: 2026-05-15
status: current
confidence_overall: settled
issue: "#748"
---

# How Claude Code works in large codebases: Best practices and where to start

> First-party Anthropic post documenting the production deployment realities of
> Claude Code in enterprise codebases — with a seven-extension-point harness
> taxonomy, a five-item navigability checklist, specific configuration maintenance
> cadence (3–6 months), and the minimum viable organizational structure (DRI) for
> large-codebase deployments.

## Source Context

- **Type**: blog-post (official Anthropic claude.com blog, May 14, 2026; part of a
  "Claude Code at scale" series explicitly focused on engineering organizations at
  enterprise scale)
- **Author credibility**: First-party Anthropic. Maximum authority for what Claude
  Code does, how its harness is structured, and what patterns Anthropic observes
  across production deployments. The post reports on real large-codebase deployments
  rather than hypotheticals: "Claude Code is running in production across
  multi-million-line monorepos, decades-old legacy systems, distributed architectures
  spanning dozens of repositories." Claims about harness architecture, extension
  points, and configuration patterns are authoritative as first-party description.
- **Scope**: Covers how Claude Code navigates large codebases (agentic search vs.
  RAG), the full seven-extension-point harness taxonomy, five techniques for making
  codebases navigable, configuration maintenance cadence, and organizational ownership
  structures. Includes a "Getting Started Checklist" visual for enterprise setup.
  Does NOT cover: specific model version considerations, SDK-level API parameters,
  cost or token metrics for large-codebase use, or multi-agent coordination topology
  beyond subagents as an extension point.

## Extracted Claims

### Claim 1: Large codebases are the primary production environment for Claude Code — not an edge case

- **Evidence**: First-party production observation spanning monorepos, legacy systems,
  and distributed architectures. The article opens by establishing scope: "Claude Code
  is running in production across multi-million-line monorepos, decades-old legacy
  systems, distributed architectures spanning dozens of repositories."
- **Confidence**: settled (first-party claim about observed production deployments)
- **Quote**: "Claude Code is running in production across multi-million-line monorepos,
  decades-old legacy systems, distributed architectures spanning dozens of repositories"
- **Our assessment**: The framing resets the expectation that large-codebase use is
  specialized or advanced. Multi-million-line monorepos and legacy systems are the
  operational baseline, not the ceiling. This has direct implications for how the guide
  presents large-codebase guidance: it should be in the mainstream chapters, not an
  appendix.

### Claim 2: Claude Code uses agentic search rather than RAG-based retrieval — solving the index staleness problem by navigating the live codebase

- **Evidence**: First-party architectural description contrasting two approaches. The
  article describes RAG's failure mode ("The AI coding tools relied on RAG-based retrieval
  by embedding the entire codebase and retrieving relevant chunks at query time") and
  explains its staleness problem before presenting agentic search as the alternative.
- **Confidence**: settled (first-party architectural description with explicit failure
  mode comparison)
- **Quote**: "By the time a developer queries the index, it reflects the codebase as it
  existed days, weeks, or even hours ago."
- **Our assessment**: The staleness argument is the strongest technical case for agentic
  search over RAG in large, fast-moving codebases. RAG-based tools require embedding
  pipeline maintenance and are always behind the current state of the code; agentic
  search operates on the live filesystem at query time. For practitioners evaluating AI
  coding tools: an embedding-based tool will consistently produce stale context in codebases
  with active development. The agentic search failure mode (reading too many files, slow
  on first exploration) is different and manageable via the navigability techniques in
  later claims.

### Claim 3: Claude navigates codebases the way a developer does — traversing the file system, reading files, and using grep

- **Evidence**: First-party description of how agentic search operates. The article
  explains the mechanism directly.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Claude navigates a codebase the way a software engineer would: it traverses
  the file system, reads files, uses grep to find exactly what it needs"
- **Our assessment**: This is the clearest one-sentence description of what "agentic
  search" means in practice. It is not a sophisticated semantic search — it is developer-
  idiomatic navigation applied at machine speed. The implication for harness design:
  anything that makes navigation easier for a developer (good directory structure, clear
  naming, explicit test commands) makes it easier for Claude. The five navigability
  techniques in Claim 5 are all extensions of this principle.

### Claim 4: Agentic search has no embedding pipeline or centralized index to maintain — surviving the commit velocity of thousands of engineers

- **Evidence**: First-party description of agentic search's maintenance advantage.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Agentic search avoids those failure modes. There's no embedding pipeline
  or centralized index to maintain as thousands of engineers commit new code."
- **Our assessment**: The maintenance argument complements the staleness argument (Claim
  2). RAG requires active pipeline maintenance (re-embedding on new commits); agentic
  search requires none. For teams evaluating infrastructure cost: the absence of an
  embedding pipeline is a meaningful operational simplification at enterprise scale.

### Claim 5: The Claude Code harness has seven extension points — five primary (CLAUDE.md files, hooks, skills, plugins, MCP servers) and two additional (LSP integrations, subagents)

- **Evidence**: First-party taxonomy from the article. The primary five are named
  explicitly as extension points; LSP integrations and subagents are listed as additional
  capabilities that "round out the setup."
- **Confidence**: settled (first-party harness taxonomy)
- **Quote**: "The harness is built from five extension points—CLAUDE.md files, hooks,
  skills, plugins, and MCP servers—each serving a different function." "LSP integrations
  and subagents, round out the setup."
- **Our assessment**: This is the most complete and authoritative harness taxonomy in the
  corpus. Prior corpus sources described some of these individually (CLAUDE.md design in
  multiple notes, skills in the MacLean note, subagents in the coordination patterns post)
  but no source presented all seven in a unified taxonomy. The two-tier structure (five
  primary extension points + two additional capabilities) maps cleanly to the architecture:
  the five extension points configure the environment; LSP and subagents enhance capabilities.

### Claim 6: CLAUDE.md files should be kept lean and layered — loaded additively as Claude moves from root to subdirectories

- **Evidence**: First-party configuration recommendation with explicit mechanism description.
- **Confidence**: settled (first-party architectural recommendation)
- **Quote**: "Keeping CLAUDE.md files lean and layered. Claude loads them additively as it
  moves through the codebase: root file for the big picture, subdirectory files for local
  conventions."
- **Our assessment**: The additive loading mechanism is the key architectural fact behind
  this recommendation. A lean root CLAUDE.md (big picture) + rich subdirectory CLAUDE.md
  files (local conventions) distributes context load without requiring every task to pull
  the full context. This is independently validated by the Sentry practitioner profile
  (thin redirect CLAUDE.md + rich subdirectory AGENTS.md files) and MacLean's "lay of
  the land" discipline. The failure mode when this is violated is documented in
  `failure-claudemd-ignored-compaction.md`: large CLAUDE.md files get marked "may or may
  not be relevant" by the harness and become unreliable.

### Claim 7: Initialize Claude Code in subdirectories rather than the repo root — scoping it to the task-relevant portion of the codebase

- **Evidence**: First-party recommendation with explicit rationale.
- **Confidence**: settled (first-party recommendation with specific problem statement)
- **Quote**: "Initializing in subdirectories, not at the repo root. Claude works best when
  it's scoped to the part of the codebase that's actually relevant to the task."
- **Our assessment**: This is an actionable inversion of the default pattern (start at root).
  For large monorepos where a developer is working on one service, starting Claude at the
  repo root loads entire codebase context that is irrelevant to the task. Starting in the
  relevant subdirectory keeps the exploration bounded from the outset. This is a direct
  analogy to how a developer opens their IDE focused on the relevant module, not the whole
  repo. The combination of subdirectory initialization + per-subdirectory CLAUDE.md files
  (Claim 6) + per-subdirectory test commands (Claim 8) creates a self-consistent scoped
  context that improves both efficiency and accuracy.

### Claim 8: Scoping test and lint commands per subdirectory prevents timeout waste and irrelevant output from running the full suite

- **Evidence**: First-party recommendation with specific failure mode description.
- **Confidence**: settled (first-party recommendation with explicit problem description)
- **Quote**: "Scoping test and lint commands per subdirectory. Running the full suite when
  Claude changed one service causes timeouts and wastes context on irrelevant output."
- **Our assessment**: The failure mode is specific and real: in large monorepos, running
  the full test suite for a change to one service is both slow (timeout risk) and noisy
  (thousands of irrelevant test results consuming context). Per-subdirectory test commands
  keep the feedback loop tight and the context clean. This is a configuration detail that
  significantly affects the quality of Claude's edit/test/fix iterations. Practitioners
  who experience Claude getting "stuck" in test loops in large codebases should check
  whether subdirectory-scoped test commands are configured.

### Claim 9: Codebase maps (lightweight markdown files) provide orientation when directory structure alone doesn't communicate the architecture

- **Evidence**: First-party recommendation with specific format description.
- **Confidence**: settled (first-party recommendation with concrete implementation detail)
- **Quote**: "Building codebase maps when the directory structure doesn't do the work...a
  lightweight markdown file at the repo root listing each top-level folder with a
  one-line description."
- **Our assessment**: The lightweight markdown format (one file, one line per folder) is
  the appropriate scope for a codebase map. It is not a full architectural document — it
  is a navigation aid that answers "what is in this directory?" for every top-level folder.
  This complements the CLAUDE.md root file (which covers "how to work in this codebase")
  with a separate "what is where" reference. The recommendation to build a map only "when
  the directory structure doesn't do the work" is important scope discipline: don't add
  a codebase map if the directory names are already self-explanatory.

### Claim 10: LSP integrations give Claude IDE-level symbol navigation — following definitions and tracing cross-file references

- **Evidence**: First-party feature description with specific capability list.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Language server protocol (LSP) integrations give Claude the same navigation
  a developer has in their IDE...it can follow a function call to its definition, trace
  references across files, and distinguish between identically named functions in different
  languages."
- **Our assessment**: LSP integration is the bridge between text-based search (grep) and
  semantic code understanding. Grep can find a string anywhere in the codebase; LSP can
  resolve what that string means — which specific function definition it refers to,
  which files use it, whether identically named functions in different languages are the
  same or different. For large codebases with extensive cross-file dependencies or
  polymorphism, LSP integration is a qualitative navigation upgrade. This corroborates
  the Serena guide (`docs-ghaw-guides-serena.md`) which documents the same LSP-backed
  capability in the gh-aw context.

### Claim 11: Plugins bundle skills, hooks, and MCP configurations into an installable package — ensuring consistent context from day one for new engineers

- **Evidence**: First-party feature description with specific day-one onboarding use case.
- **Confidence**: settled (first-party feature description)
- **Quote**: "A plugin bundles skills, hooks, and MCP configurations into a single
  installable package, so when a new engineer installs that plugin on day one, they will
  immediately have the same context."
- **Our assessment**: The plugin mechanism solves the configuration distribution problem
  in team settings. Without plugins, each engineer must manually replicate the full
  harness configuration (CLAUDE.md, hooks, skills, MCP servers) — a setup task that
  produces configuration drift and inconsistent behavior across the team. A plugin
  installed on day one eliminates that friction and ensures every engineer starts with
  the same context from the moment they first use Claude Code. This is the organizational
  equivalent of providing a standardized development environment (Docker compose, Nix
  flake) — but for the AI context layer.

### Claim 12: Subagents split exploration from editing by running as isolated instances with their own context windows

- **Evidence**: First-party architectural description with explicit purpose statement.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Subagents split exploration from editing. A subagent is an isolated Claude
  instance with its own context window that takes a task, does the work, and returns
  only the final result."
- **Our assessment**: The exploration/editing split is the key design insight for subagent
  use. A main agent accumulates context across the full task; exploration subtasks (reading
  unfamiliar files, searching for implementations, analyzing dependencies) are context-heavy
  but their intermediate state is not needed after the result is returned. Offloading
  exploration to subagents with their own context windows keeps the main agent's context
  clean for the editing work that follows. This complements the multi-agent coordination
  patterns post's framing of subagents as bounded task executors — here the purpose is
  specifically context hygiene, not just parallelism.

### Claim 13: Configuration reviews every 3–6 months (or whenever performance plateaus) prevent outdated instructions from constraining newer model capabilities

- **Evidence**: First-party maintenance recommendation with specific cadence.
- **Confidence**: settled (first-party operational recommendation)
- **Quote**: "Teams should expect to do a meaningful configuration review every three to
  six months, but it's also worth doing one whenever performance feels like it's plateaued"
- **Our assessment**: The dual trigger (time-based AND performance-based) is the right
  maintenance policy. The time-based trigger catches drift even when performance doesn't
  obviously degrade; the performance trigger catches cases where the model improved and
  prior workarounds are now constraints. The underlying cause is that AI models improve
  between releases — instructions written to work around an older model's limitations
  may actively hinder a newer, more capable model. This maintenance cadence converts
  CLAUDE.md from a one-time setup artifact into a living configuration that improves
  with the model.

### Claim 14: The minimum viable organizational structure for large-codebase Claude Code deployment is a DRI with authority over the full configuration stack

- **Evidence**: First-party organizational recommendation with explicit scope definition.
- **Confidence**: settled (first-party recommendation)
- **Quote**: "The minimum viable version is a DRI: one person with ownership over the
  Claude Code configuration, the authority to make calls on settings, permissions policy,
  the plugin marketplace, and CLAUDE.md conventions."
- **Our assessment**: The DRI model solves the configuration fragmentation problem. Without
  a designated owner, every team member makes their own configuration decisions, producing
  tribal knowledge, inconsistent behavior, and gradual configuration drift. A DRI with
  explicit authority over settings, permissions, plugins, and CLAUDE.md conventions provides
  a single decision-making point without requiring a full infrastructure team. The DRI
  pattern is the minimum viable version; at larger scale, a small dedicated team takes
  this role.

### Claim 15: Successful large-codebase rollouts had infrastructure pre-wired before engineers first touched Claude Code — ensuring it fit developer workflows on day one

- **Evidence**: First-party observation about successful deployment patterns.
- **Confidence**: emerging (first-party observation; the pattern is described as common
  across successful deployments but without quantitative evidence)
- **Quote**: "A small team, sometimes even just one person, wired up the tooling so Claude
  already fit developer workflows when they first touched it"
- **Our assessment**: This is the most important team adoption finding in the post. The
  contrast is with "self-serve" deployments where each engineer configures from scratch —
  which produces slow adoption and configuration inconsistency. Pre-wiring requires upfront
  investment from a small team (or a dedicated DRI) but yields faster adoption and more
  consistent context quality. The "fit developer workflows" criterion is the quality bar:
  configuration is not done until Claude behaves correctly in the team's existing workflow,
  not just in isolation.

## Concrete Artifacts

### Seven-Extension-Point Harness Taxonomy

```
Claude Code Harness: Seven Extension Points
(Anthropic, "How Claude Code works in large codebases," May 14, 2026)

PRIMARY EXTENSION POINTS (five):
  CLAUDE.md files
    → Layered context: root file for big picture, subdirectory files for local conventions
    → Load additively as Claude moves through the codebase
    → Keep lean; large files get dropped during compaction

  Hooks
    → Scripts triggered on events for automation and continuous improvement
    → Operate outside the context window (cannot be reasoned away)

  Skills
    → Packaged, reusable expertise loaded on-demand
    → "Reference do not embed" pattern: point into docs, don't duplicate content

  Plugins
    → Bundle skills + hooks + MCP configurations into single installable package
    → Day-one onboarding mechanism: install once, get consistent context immediately

  MCP Servers
    → Connections to internal tools and data sources
    → Provide Claude real-time access to structured data (test results, tickets, monitoring)

ADDITIONAL CAPABILITIES (two):
  LSP Integrations
    → Language Server Protocol: IDE-level symbol navigation
    → Follow function calls to definitions, trace cross-file references
    → Distinguish identically named functions across languages

  Subagents
    → Isolated Claude instances with their own context windows
    → Split exploration from editing: subagent explores, returns final result only
    → Keep main agent context clean for editing work
```

### Five-Technique Navigability Checklist

```
Making Large Codebases Navigable for Claude Code
(Anthropic, "How Claude Code works in large codebases," May 14, 2026)

1. LEAN AND LAYERED CLAUDE.md
   "Keeping CLAUDE.md files lean and layered. Claude loads them additively as it
   moves through the codebase: root file for the big picture, subdirectory files
   for local conventions."

2. SUBDIRECTORY INITIALIZATION
   "Initializing in subdirectories, not at the repo root. Claude works best when
   it's scoped to the part of the codebase that's actually relevant to the task."

3. PER-SUBDIRECTORY TEST/LINT COMMANDS
   "Scoping test and lint commands per subdirectory. Running the full suite when
   Claude changed one service causes timeouts and wastes context on irrelevant output."

4. CODEBASE MAPS (when directory structure is insufficient)
   "Building codebase maps when the directory structure doesn't do the work...a
   lightweight markdown file at the repo root listing each top-level folder with
   a one-line description."

5. LSP SERVERS (for symbol-level navigation)
   "Language server protocol (LSP) integrations give Claude the same navigation a
   developer has in their IDE...it can follow a function call to its definition,
   trace references across files, and distinguish between identically named functions
   in different languages."
```

### Agentic Search vs. RAG Comparison

```
Codebase Navigation: Agentic Search vs. RAG-Based Retrieval
(Anthropic, "How Claude Code works in large codebases," May 14, 2026)

RAG-BASED RETRIEVAL:
  Mechanism:  Embed entire codebase → retrieve relevant chunks at query time
  Staleness:  "By the time a developer queries the index, it reflects the codebase
              as it existed days, weeks, or even hours ago."
  Maintenance: Requires embedding pipeline maintenance on every commit
  At scale:   "As thousands of engineers commit new code" → pipeline falls behind

AGENTIC SEARCH:
  Mechanism:  "Claude navigates a codebase the way a software engineer would: it
              traverses the file system, reads files, uses grep to find exactly
              what it needs"
  Staleness:  None — operates on live filesystem at query time
  Maintenance: "There's no embedding pipeline or centralized index to maintain"
  At scale:   Scales with filesystem; no pipeline to maintain

Decision: Agentic search is the correct approach for large, fast-moving codebases.
RAG-based tools are appropriate only where codebase change velocity is low and
embedding pipeline maintenance is acceptable overhead.
```

### Organizational Structure Options

```
Claude Code Organizational Structure for Large Codebases
(Anthropic, "How Claude Code works in large codebases," May 14, 2026)

MINIMUM VIABLE: DRI (Directly Responsible Individual)
  "The minimum viable version is a DRI: one person with ownership over the Claude
  Code configuration, the authority to make calls on settings, permissions policy,
  the plugin marketplace, and CLAUDE.md conventions."

  DRI owns:
    - Claude Code configuration (settings.json, permissions)
    - Plugin marketplace decisions
    - CLAUDE.md conventions
    - Authority to make calls when team members disagree

SCALED VERSION: Small Infrastructure Team
  "A small team, sometimes even just one person, wired up the tooling so Claude
  already fit developer workflows when they first touched it"

  Responsibilities:
    - Pre-wire tooling before engineers first touch Claude Code
    - Ensure configuration fits existing developer workflows on day one
    - Manage plugin distribution and configuration maintenance

CONFIGURATION MAINTENANCE CADENCE:
  Scheduled: "every three to six months"
  Reactive: "whenever performance feels like it's plateaued"
  Rationale: Models improve between releases; outdated instructions can constrain
             newer, more capable models
```

## Cross-References

- **Corroborates**: `blog-anthropic-maccoss-developer-onboarding.md` (Claim 4: CLAUDE.md
  as "lay of the land") — MacLean's "lay of the land, not the expertise itself" CLAUDE.md
  discipline is independently validated here by the "lean and layered" recommendation.
  Both sources arrive at the same architectural separation: CLAUDE.md handles orientation
  (big picture, environment setup, doc pointers) while skills and subdirectory files handle
  domain expertise. MacLean's implementation (separate pwiz-ai repo) and this post's
  recommendation (root + subdirectory CLAUDE.md hierarchy) are two implementations of the
  same underlying principle.

- **Corroborates**: `practitioner-getsentry-sentry.md` (Pattern 1: Thin CLAUDE.md redirect
  + Pattern 2: context-aware subdirectory loading) — Sentry's 11-byte CLAUDE.md redirect
  to AGENTS.md, combined with subdirectory AGENTS.md files for backend/frontend/tests,
  is the production implementation of this post's "lean and layered" recommendation. Both
  arrive at the same architecture independently. The "subdirectory files for local
  conventions" pattern here is exactly what Sentry's `src/AGENTS.md` (~700 lines),
  `tests/AGENTS.md` (~200 lines), and `static/AGENTS.md` (~600 lines) implement.

- **Corroborates**: `failure-claudemd-ignored-compaction.md` — The "lean" requirement
  for CLAUDE.md files is supported by the compaction failure report. That note documented
  that long CLAUDE.md files get marked "may or may not be relevant" and can be dropped
  entirely during context compaction. This post's "lean and layered" recommendation is
  the architectural response to exactly that failure mode: keep the root file short enough
  that it is never a compaction target.

- **Corroborates**: `docs-ghaw-guides-serena.md` (Claim 1: LSP-backed symbol navigation
  for large codebases) — The Serena guide documents LSP-based semantic code analysis
  ("enabling agents to find symbols, navigate code relationships, and edit at the symbol
  level") as a capability in the gh-aw context. This post independently recommends LSP
  integrations as a harness extension point for the same purpose. Both confirm that
  LSP-backed navigation is a distinct capability tier above text search for large
  codebases.

- **Corroborates**: `blog-anthropic-claude-code-auto-mode.md` — The "wired up the tooling
  before engineers first touched it" pattern (Claim 15) aligns with auto mode's pre-wiring
  approach: both require upfront infrastructure investment (configuration, classifier setup)
  that yields better baseline behavior for engineers using Claude Code. Auto mode's
  three-tier permission structure requires the same DRI-level configuration decisions
  (environment trust boundaries, block rules, allow exceptions) as the harness structure
  described here.

- **Extends**: `blog-anthropic-multi-agent-coordination-patterns.md` — Subagents appear
  in that post as coordination participants in multi-agent topologies (orchestrator-subagent
  pattern). This post adds a second framing: subagents as a harness extension point for
  context hygiene (exploration/editing separation). The two framings are complementary:
  orchestrator-subagent is the coordination architecture; exploration/editing separation
  is one specific pattern for why you'd use subagents.

- **Extends**: `blog-anthropic-maccoss-developer-onboarding.md` — MacLean's post covers
  context architecture for a single practitioner on a legacy codebase. This post covers
  the enterprise-scale deployment patterns that MacLean's individual practices require
  when scaled to teams: plugin distribution (instead of individual skill libraries),
  DRI ownership (instead of solo configuration), configuration reviews (instead of ad-hoc
  maintenance). This post is the team-scale version of MacLean's individual-scale advice.

- **Extends**: `blog-anthropic-claude-code-routines.md` — Routines add the scheduling
  and trigger layer for automated Claude Code sessions. This post adds the configuration
  and navigation layer that those sessions operate within. Together they form a more
  complete picture: routines determine when Claude Code runs; this post determines how
  Claude Code navigates when it does.

- **Novel**:
  - **Agentic search vs. RAG framing for codebase navigation**: No prior corpus source
    explicitly names the contrast between agentic search (filesystem traversal) and
    RAG-based retrieval (embedding index) as the fundamental architectural distinction
    for large-codebase AI coding tools. The staleness argument against RAG is new.
  - **Subdirectory initialization as a named best practice**: No prior corpus source
    explicitly recommends initializing Claude Code in subdirectories rather than at the
    repo root. The rationale (scope to task-relevant portion) is new to the corpus.
  - **Per-subdirectory test/lint command scoping**: The specific recommendation to scope
    test and lint commands per subdirectory (with the timeout/irrelevant-output failure
    mode) is new to the corpus.
  - **Codebase maps (lightweight markdown) as a navigability technique**: A dedicated,
    minimal markdown file listing top-level folders with one-line descriptions is a
    distinct artifact type not documented in any prior corpus source.
  - **Plugin bundles as day-one onboarding mechanism**: The plugin-as-consistent-context
    pattern (install once → same configuration for every engineer) is not documented in
    any prior source.
  - **Seven-extension-point taxonomy in unified form**: While individual extension points
    appear in various corpus sources, the seven-point unified taxonomy (CLAUDE.md files,
    hooks, skills, plugins, MCP servers, LSP integrations, subagents) is first organized
    here.
  - **Configuration review cadence (3–6 months)**: The specific recommendation for
    a meaningful configuration review every 3–6 months (plus reactive review on plateau)
    is not documented in any prior corpus source.
  - **DRI as minimum viable organizational structure**: The DRI model (one person,
    explicit authority over four configuration domains) as the minimum viable structure
    is new. Prior corpus sources describe team patterns (Sentry's DevEx team, GHAW
    factory ownership) but not this specific minimum-viable framing.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Extension Points**: Add a "Seven Extension
  Points" section using this taxonomy as the organizational frame for the chapter.
  Current corpus covers CLAUDE.md design, hooks, skills, and MCP servers in scattered
  sections. Unifying them under this taxonomy (five primary + two additional capabilities)
  gives practitioners a complete mental model before diving into each extension point's
  details.

- **Chapter 02 (Harness Engineering) — Making Large Codebases Navigable**: Add a
  dedicated "Large Codebase Navigability" subsection with the five-technique checklist
  (lean/layered CLAUDE.md, subdirectory initialization, per-subdirectory test/lint,
  codebase maps, LSP integration). These are currently undocumented as a unified
  checklist. Practitioners working in monorepos or legacy systems need this section
  before anything else.

- **Chapter 02 (Harness Engineering) — Plugin Distribution**: Add a "Plugin Bundles"
  section documenting the day-one onboarding pattern (bundle skills + hooks + MCP
  configurations → install once → consistent context). This is the team-scale
  complement to the individual-practitioner skills guidance from the MacLean note.

- **Chapter 02 (Harness Engineering) — Configuration Maintenance**: Add a
  "Configuration Maintenance" section with the 3–6 month scheduled review cadence
  and the performance-plateau trigger. Frame: "CLAUDE.md files are living
  configuration, not one-time setup. AI models improve between releases; instructions
  written to work around an older model's limitations may actively constrain a newer
  model."

- **Chapter 05 (Team Adoption) — Organizational Structure**: Add an "Organizational
  Structure" section covering the DRI model (minimum viable: one person, explicit
  authority) and the infrastructure team pattern (scaled version). The "pre-wired
  before engineers first touch it" finding should be the chapter's central team
  adoption recommendation: successful deployments invested in configuration quality
  before rollout, not after.

- **Chapter 01 (Fundamentals) or Chapter 04 (Context Engineering)**: The agentic
  search vs. RAG contrast is the right framing for explaining WHY Claude Code handles
  large codebases differently from embedding-based tools. Add a "How Claude Code
  Navigates" section contrasting the two approaches (with the staleness argument)
  as foundational context for everything that follows.

## Extraction Notes

- The source URL returns a JavaScript-rendered page. WebFetch provided summarized
  content across multiple fetches; verbatim quotes were extracted across several
  targeted fetch requests. All quotes marked as verbatim were confirmed via multiple
  targeted fetches against the source URL. The article contains a visual "Get started
  with Claude Code for Enterprise" checklist (described as "figure 3") whose exact
  contents could not be extracted via WebFetch due to the visual format.
- The article is described as part of a "Claude Code at scale" series — there may
  be companion posts in the series that would warrant follow-up source submissions.
- No contradiction with existing corpus notes was found that would require a
  contradiction issue. The agentic search vs. RAG comparison is new to the corpus
  rather than contradicting an existing position.
- Confidence is set to `settled` because: the claims are first-party Anthropic
  descriptions of their own product architecture and configuration recommendations,
  backed by observed production deployments. The organizational patterns (DRI, pre-
  wiring) are described as "what successful deployments did" rather than as untested
  theory, though they lack quantitative support.
- The three separate Prospector triage comments on issue #748 are consistent on
  novelty (high), type (blog-post, first-party), and chapters (Ch02 Harness
  Engineering, Ch04 Context Engineering, Ch05 Team Adoption). All key extraction
  targets across the three triage comments were found in the source.
