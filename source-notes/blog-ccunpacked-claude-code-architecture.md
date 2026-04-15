---
source_url: https://ccunpacked.dev/
source_type: blog-post
title: "Claude Code Unpacked: A Visual Guide"
author: autocracy101 (zackautocracy)
date_published: 2026-04-01
date_extracted: 2026-04-14
last_checked: 2026-04-14
status: archived (site returning 403 as of extraction date; content preserved in Chinese
  translation at github.com/TUARAN/ccunpacked-zh and corroborated by HN discussion
  news.ycombinator.com/item?id=47597085)
confidence_overall: emerging
issue: "#22"
---

# Claude Code Unpacked: A Visual Guide

> An interactive visual architecture explorer built from Claude Code's leaked NPM
> source map, documenting the full 11-step agent execution loop, a taxonomy of 53+
> built-in tools across 8 functional categories, 95+ slash commands, unreleased
> features (Coordinator Mode, KAIROS, Bridge, Daemon, UltraPlan), and Personality &
> UX patterns — the most complete single-source map of Claude Code's internals
> available as of April 2026.

## Source Context

- **Type**: blog-post / interactive architecture explorer (visual guide with Framer
  Motion animations, dark-mode diagrams, hover helpers, and flow charts)
- **Author credibility**: autocracy101 (zackautocracy on GitHub) is an anonymous
  practitioner who built the interactive site from the leaked source maps. Author
  stated: "A 500K line codebase is a lot to navigate, so I mapped it visually to
  give myself a quick reference." The site is not a vendor document — it is a
  practitioner reverse-engineering effort. Claims are grounded in the leaked
  TypeScript source (file names and line counts corroborate the codebase).
  Community reception was very high (1,056+ HN points, 372 comments; the
  discussion thread reached 402 comments at peak). Key architectural claims
  (game-engine TUI rendering, tool permission system, 14-vector cache tracking)
  were confirmed by HN commenters, including Anthropic-adjacent readers. No
  substantive claims were contested.
- **Scope**: Full internal architecture of a specific Claude Code release (the NPM
  version where source maps were accidentally shipped via Bun issue #28001). Covers:
  the agent execution loop, the complete tool system, slash command inventory,
  codebase directory structure, unreleased features, and Personality & UX patterns
  including frustration detection, undercover mode, and the Buddy companion system.
  Does NOT cover Claude Code API integration, pricing, or model-level behavior.
  The site was live at ccunpacked.dev; as of extraction date it returns 403, likely
  due to a takedown. Content was recovered from a preserved Chinese translation
  (github.com/TUARAN/ccunpacked-zh, 74KB single-file HTML mirror of the original).
- **Relationship to related sources**: This source documents the *architecture
  explorer* built from the same leak as `failure-alex000kim-claudecode-source-leak`
  (issue #20). The alex000kim note focuses on four production failure/engineering
  findings (autoCompact runaway, cache economics, coordinator prompt, bash security).
  This note covers the comprehensive architecture map — the agent loop, tool
  taxonomy, command inventory, and UX patterns — which alex000kim.com does not
  systematically cover. These are complementary, not overlapping, extractions.

## Extracted Claims

### Claim 1: The Claude Code agent loop follows an 11-step pipeline with specific source file attribution for each stage

- **Evidence**: The ccunpacked.dev site extracted this from source maps; each step
  is attributed to a specific TypeScript file (TextInput.tsx, messages.ts, history.ts,
  context.ts, query.ts, QueryEngine.ts, tools.ts, StreamingToolExecutor.ts,
  autoCompact.ts). The Chinese translation preserves the complete step list. HN
  commenters did not dispute the pipeline structure; one noted the game-engine analogy
  for the rendering stage.
- **Confidence**: emerging (source-attributed; the specific file names are verifiable
  if the source becomes accessible again, but this is a snapshot of a leaked version)
- **Quote**: "A 500K line codebase is a lot to navigate, so I mapped it visually"
  (site intro); the loop is described as Input → Message Creation → History Append
  → System Prompt Assembly → API Stream → Token Parsing → Tool Detection → Tool
  Execution Loop → Response Rendering → Post-Sampling Hooks → REPL Wait.
- **Our assessment**: The 11-step pipeline is the clearest public documentation of
  how a production coding agent's inner loop actually works. Steps 4 (System Prompt
  Assembly: combines CLAUDE.md + tool definitions + context + memory from context.ts)
  and 10 (Post-Sampling Hooks: auto-compaction, memory extraction, dream mode from
  autoCompact.ts) are the most guide-relevant. Step 4 explains *why* CLAUDE.md
  content works at all — it is assembled into the system prompt on every turn.
  Step 10 explains why hooks fire after the model responds, not before, and why
  compaction is triggered there.

### Claim 2: The Tool Execution Loop (Step 8) re-invokes the API with accumulated results — it is not a single call

- **Evidence**: Source attribution to `StreamingToolExecutor.ts`: "Collects results,
  appends to history, re-invokes API." This is the mechanism behind multi-step tool
  use within a single turn.
- **Confidence**: emerging
- **Quote**: Step 8 — "Collects results, appends to history, re-invokes API
  (StreamingToolExecutor.ts)"
- **Our assessment**: This is the architectural explanation for why a single user
  message can trigger many API calls (each tool result triggers a new API invocation
  within the same "turn"). It directly explains the token cost pattern practitioners
  observe: a "simple" request that uses 5 tools makes 6 API calls (1 + 5 re-invocations).
  This is important context for the guide's cost/token budget sections.

### Claim 3: Claude Code ships 53+ built-in tools organized across 8 functional categories, with an additional set of feature-gated experimental tools

- **Evidence**: The ccunpacked.dev site exhaustively catalogued tools from the source.
  The Chinese translation preserves the full taxonomy with category names and tool
  lists. The total count of 53+ is corroborated by the subagent research that
  cross-checked multiple sources.
- **Confidence**: emerging (complete taxonomy from a specific version; tool count
  may change across releases)
- **Quote**: Site provides category labels — File Operations, Execution, Search &
  Fetch, Agents & Tasks, Planning, MCP Integration, System, Experimental — with
  tools listed per category.
- **Our assessment**: The taxonomy reveals the scope of what Claude Code can do
  out-of-the-box vs. what requires flags. The Planning category (EnterPlanMode,
  ExitPlanMode, EnterWorktree, ExitWorktree, VerifyPlanExecution) and Agents &
  Tasks category (Agent, SendMessage, TaskCreate/Get/List/Update/Stop, TeamCreate/
  Delete, ListPeers) are the most novel — they represent the orchestration surface
  that practitioners who have only used Claude Code interactively may not know
  exists. The feature-gated tools (marked 🔒 in the site) map to unreleased features:
  WEB_BROWSER_TOOL, KAIROS_GITHUB_WEBHOOKS flags are visible in the taxonomy.

### Claim 4: The agent loop's Post-Sampling Hooks step (Step 10) is where auto-compaction, memory extraction, and "dream mode" fire

- **Evidence**: Direct source attribution: "Post-Sampling Hooks: Auto-compaction,
  memory extraction, dream mode (autoCompact.ts)" — this is the same autoCompact.ts
  where the 250K-calls/day runaway bug was found (per the alex000kim note).
- **Confidence**: emerging
- **Quote**: Step 10 — "Post-Sampling Hooks: Auto-compaction, memory extraction,
  dream mode (autoCompact.ts)"
- **Our assessment**: The co-location of three fundamentally different operations
  (compaction, memory, dream) in one step is architecturally significant. It means
  all three can fire at the end of every turn — and the autoCompact bug described in
  `failure-alex000kim-claudecode-source-leak.md` (consecutive failures in this hook)
  could also have affected memory extraction and dream mode invocations. For harness
  authors: the post-sampling hook is the right injection point for custom behavior
  after the model responds.

### Claim 5: The System Prompt Assembly step explicitly combines CLAUDE.md, tool definitions, context, and memory on every turn

- **Evidence**: Source attribution: "Combines CLAUDE.md, tool definitions, context,
  and memory (context.ts)." This is at Step 4, before the API call, on every turn.
- **Confidence**: emerging
- **Quote**: Step 4 — "System Prompt Assembly: Combines CLAUDE.md, tool definitions,
  context, and memory (context.ts)"
- **Our assessment**: Confirms that CLAUDE.md is re-injected into the system prompt
  every turn, not just at session start. This is the mechanism behind why CLAUDE.md
  rules can "survive" mid-session — they are always present in the system prompt.
  However, it also explains the compaction interaction: when compaction fires, the
  assembled system prompt is what gets compressed, not just the conversation history.
  This aligns with `failure-claudemd-ignored-compaction.md`'s finding that
  CLAUDE.md instructions can get lost post-compaction.

### Claim 6: The terminal rendering engine is closer to a game engine than a TUI — Int32Array-backed ASCII pools, bitmask styles, patch optimizer achieving ~50x reduction in stringWidth calls

- **Evidence**: Source attribution to `ink/screen.ts` and `ink/optimizer.ts`. The
  site documents: "Int32Array-backed ASCII character pool, bitmask-encoded style
  metadata, patch optimizer merging cursor moves and canceling hide/show pairs,
  self-evicting line-width cache achieving ~50x reduction in stringWidth calls during
  token streaming." HN commenter confirmed: "most people's mental model...is 'just
  a TUI' but...closer to 'a small game engine.'"
- **Confidence**: emerging (source-attributed; 50x figure is from source comments)
- **Quote**: HN commenter: "most people's mental model...is 'just a TUI' but...
  closer to 'a small game engine.'"
- **Our assessment**: The game-engine architecture explains the 60fps-style smooth
  rendering and diff-based terminal updates that Claude Code is known for. For
  practitioners building alternative frontends or TUI integrations: the rendering
  layer is not a simple ANSI print loop — it is a scene graph compiled to ANSI. This
  is relevant for anyone building on Claude Code's terminal infrastructure.

### Claim 7: Frustration detection uses a regex pattern in userPromptKeywords.ts that classifies user messages by profanity and complaint keywords — no LLM inference required

- **Evidence**: Source attribution to `userPromptKeywords.ts`. Specific terms
  identified in the pattern: "wtf," "piss(ed|ing)? off," and related phrases. The
  HN discussion and alex000kim note both confirm this file exists with this purpose.
- **Confidence**: emerging (file name is concrete; exact regex pattern is inferred
  from partial disclosure)
- **Quote**: "A regex pattern in `userPromptKeywords.ts` detects user frustration
  via terms like 'wtf,' 'piss(ed|ing) off,' and 'this sucks' for sentiment analysis."
- **Our assessment**: Frustration detection without LLM inference is architecturally
  interesting: it is fast, deterministic, and does not consume tokens. What happens
  when frustration is detected is not disclosed in the site (response modification?
  UX change? internal telemetry?). The pattern is nonetheless relevant to harness
  design: practitioners can implement similar pre-processing to classify user inputs
  by sentiment before routing to the agent, without burning a model call.

### Claim 8: Undercover Mode (undercover.ts, ~90 lines) automatically strips internal Anthropic references in non-internal repositories — and has NO force-OFF mechanism

- **Evidence**: Source attribution to `undercover.ts`. The site and alex000kim note
  agree on the specific detail that "There is NO force-OFF. This guards against model
  codename leaks." Codenames suppressed include "Capybara" and "Tengu."
- **Confidence**: emerging (file confirmed in source; behavior inferred from comments
  in the code)
- **Quote**: Code comment: "There is NO force-OFF. This guards against model
  codename leaks."
- **Our assessment**: The most ethically notable finding from the leak. Undercover
  mode means Anthropic employees contributing to open-source repositories via Claude
  Code produce commits and PRs that appear fully human-authored — even the attribution
  headers are stripped. The "NO force-OFF" design choice (intentional, for codename
  leak protection) means this is not a user preference but an organizational policy
  baked into the tool. For practitioners: Claude Code's default commit attribution
  behavior (configurable via `~/.claude/settings.json`) is separate from undercover
  mode, which is only active in recognized internal-employee contexts.

### Claim 9: The Buddy/Companion system (buddy/companion.ts) generates deterministic creatures per user from their account ID using Mulberry32 PRNG — 18 species, rarity tiers, 1% shiny chance

- **Evidence**: Source attribution to `buddy/companion.ts`. Specific details:
  18 species (cats, dragons, phoenixes), rarity tiers (common to legendary), 1%
  shiny chance, RPG stats (DEBUGGING, SNARK), account-ID seed via Mulberry32 PRNG.
  Species names encoded with `String.fromCharCode()` to evade build-system detection.
  Confirmed as an April Fools' feature by HN insiders.
- **Confidence**: settled (multiple sources confirm; the April Fools' timing and
  encoding tricks are corroborated independently)
- **Quote**: Site: Buddy System — "18 species (cats, dragons, phoenixes), rarity
  tiers (common to legendary), account-ID derived" (from Chinese translation)
- **Our assessment**: The companion system is an April Fools' feature and not
  directly guide-relevant. However, the implementation detail — `String.fromCharCode()`
  encoding to evade build-system detectors — is genuinely interesting as an
  engineering pattern and reveals that Anthropic's build pipeline has automated
  content scanning that developers actively route around. This has implications for
  practitioners building their own harnesses with any such content filtering.

### Claim 10: The KAIROS unreleased feature adds cross-session memory consolidation and autonomous background operation with GitHub webhook subscriptions and 5-minute cron refresh

- **Evidence**: Source attribution to `main.tsx` with heavy feature gating.
  The site documents: "Kairos Mode: Cross-session memory integration, autonomous
  background operations." The alex000kim note adds: "/dream skill for nightly memory
  distillation, daily append-only logs, GitHub webhook subscriptions, background
  daemon workers, 5-minute cron refresh."
- **Confidence**: anecdotal (feature-gated; likely unreleased; behavior described
  from source without running the feature)
- **Quote**: Site: "Kairos Mode: Cross-session memory integration, autonomous
  background operations"
- **Our assessment**: KAIROS is the most ambitious unreleased feature — it would
  make Claude Code a persistent daemon rather than a session-based tool. The
  5-minute cron refresh and GitHub webhook subscriptions imply the agent can
  respond to repository events without human initiation. For practitioners: this is
  the upstream direction Claude Code is heading. The pattern (persistent memory +
  event-driven background workers) maps to what practitioners currently implement
  manually via external cron jobs and CI webhooks.

### Claim 11: Coordinator Mode (src/coordinator/) enables a primary agent to split tasks and spawn parallel workers in isolated git worktrees

- **Evidence**: Source attribution to `coordinator/` directory (1 file in the
  directory breakdown). The site documents the three-layer architecture: primary
  agent + task splitting + worker agents in isolated worktrees. The alex000kim note
  adds: coordinator system prompt directives ("Do not rubber-stamp weak work",
  "Never hand off understanding to another worker").
- **Confidence**: emerging (directory exists; behavior inferred from source)
- **Quote**: Site: "Coordinator Mode: Primary agent splits tasks, spawns workers
  in isolated git worktrees"
- **Our assessment**: Coordinator Mode is the built-in implementation of the
  multi-agent orchestration pattern practitioners are currently replicating manually.
  The notable finding (from alex000kim note) is that quality control is entirely
  prompt-based: the coordinator prompt contains explicit anti-rubber-stamping directives.
  No tool-call mechanism or structured schema enforces quality — only the system
  prompt. This validates prompt-based coordination as Anthropic's own approach.

### Claim 12: The codebase spans 1,900+ files and 519K+ lines of TypeScript — the utils/ directory alone has 564 files

- **Evidence**: Architecture explorer in the site with file counts per directory:
  utils/ (564), components/ (389), commands/ (189), tools/ (184), services/ (130),
  hooks/ (104), ink/ (96), bridge/ (31), and 15+ additional directories.
- **Confidence**: emerging (snapshot of a specific version; file counts change)
- **Quote**: Site architecture explorer heading: "1,900+ files, 519K+ lines of code"
- **Our assessment**: The scale is notable — Claude Code is larger than most
  practitioners would guess for a CLI tool. The utils/ directory being the largest
  (564 files, larger than tools/ at 184) suggests heavy internal shared-utility
  infrastructure. The bridge/ directory (31 files) and buddy/ (6 files) visible in
  the structure corroborate the unreleased feature inventory. For practitioners
  considering building on or extending Claude Code: this is not a small, easily
  forkable codebase.

### Claim 13: UltraPlan extends planning sessions to 10-30 minutes on Opus, with an editable output before execution

- **Evidence**: Site documents under unreleased features: "UltraPlan: 10-30 min
  planning sessions on Opus, editable before execution."
- **Confidence**: anecdotal (unreleased feature; described from source)
- **Quote**: Site: "UltraPlan: 10-30 min planning sessions on Opus, editable
  before execution"
- **Our assessment**: UltraPlan would be a formal implementation of the "extended
  planning before execution" pattern practitioners currently improvise. The
  "editable before execution" detail is critical — it implies a human review gate
  between planning and execution, addressing the core concern about autonomous
  agents making irrecoverable changes. The Opus model choice for planning aligns
  with Osmani's multi-model routing recommendation (planning to capable models).

### Claim 14: The permission system uses three levels (deny / check / prompt) and four context tiers (global → project → session → call-level)

- **Evidence**: Site documents: "3 permission levels (deny→check→prompt)" and
  "4 context tiers (global→project→session)." The check level implies a programmatic
  validation before the agent proceeds; prompt means human approval is required.
- **Confidence**: emerging (source-attributed permission architecture)
- **Quote**: Site: "3 permission levels (deny→check→prompt)" and "4 context tiers
  (global→project→session)"
- **Our assessment**: The three-level permission system (deny, check, prompt) is
  more nuanced than practitioners typically model. Most guide content treats
  permissions as binary (allowed/blocked), but the "check" tier (programmatic
  validation without human intervention) is the most interesting for harness design:
  it allows custom hooks or validators to approve/reject tool calls automatically.
  This maps to the hooks-based enforcement system in `failure-hooks-enforcement-2k.md`
  — that practitioner effectively reimplemented the "check" tier via hooks because
  they didn't know it existed.

### Claim 15: The Bridge unreleased feature provides remote control via mobile/browser using WebSocket with JWT auth and a permission approval UI

- **Evidence**: Site documents: "Bridge: Remote control via mobile/browser,
  WebSocket with JWT auth, permission approval UI." Source directory bridge/ has
  31 files.
- **Confidence**: anecdotal (unreleased; 31 files suggests substantial implementation)
- **Quote**: Site: "Bridge: Remote control via mobile/browser, WebSocket with JWT
  auth, permission approval UI"
- **Our assessment**: Bridge would enable approving Claude Code tool calls from a
  phone rather than sitting at a terminal. The "permission approval UI" detail is
  directly relevant to the remote/async agent workflows practitioners want. Combined
  with Daemon Mode (background sessions via tmux), Bridge would allow fully headless
  agent operation with mobile approval gates — the pattern many practitioners currently
  achieve with tmux + Slack bots. The JWT auth design is architecturally sounder than
  the ad-hoc webhook approaches in the community.

## Concrete Artifacts

### The 11-Step Agent Execution Loop

```
# Claude Code Agent Loop (ccunpacked.dev, from leaked source maps)
# Each step attributed to a specific TypeScript file.

Step 1  Input:              User inputs message or piped via stdin
                            Source: TextInput.tsx

Step 2  Message Creation:   createUserMessage() wraps text in Anthropic format
                            Source: messages.ts

Step 3  History Append:     Message pushed to in-memory conversation array
                            Source: history.ts

Step 4  System Prompt       Combines CLAUDE.md + tool definitions + context + memory
        Assembly:           Source: context.ts

Step 5  API Stream:         Server-Sent Events to Claude API with streaming
                            Source: query.ts

Step 6  Token Parsing:      Incoming tokens rendered in real-time to terminal
                            Source: QueryEngine.ts

Step 7  Tool Detection:     Identifies tool_use blocks, validates permissions,
                            executes tools
                            Source: tools.ts

Step 8  Tool Execution      Collects results, appends to history, re-invokes API
        Loop:               Source: StreamingToolExecutor.ts

Step 9  Response            Final response rendered with Markdown via Ink/Yoga
        Rendering:          Source: QueryEngine.ts

Step 10 Post-Sampling       Auto-compaction, memory extraction, dream mode
        Hooks:              Source: autoCompact.ts

Step 11 REPL Wait:          Returns to prompt idle state
                            Source: QueryEngine.ts
```

### Tool Taxonomy (53+ tools, 8 categories)

```
# Claude Code Built-in Tool Inventory (from ccunpacked.dev, April 2026 snapshot)

File Operations (6):
  FileRead, FileEdit, FileWrite, Glob, Grep, NotebookEdit

Execution (3):
  Bash, PowerShell, REPL (persistent session)

Search & Fetch (4):
  WebBrowser [🔒 WEB_BROWSER_TOOL flag], WebFetch, WebSearch, ToolSearch

Agents & Tasks (9):
  Agent, SendMessage (IPC via Unix sockets), TaskCreate, TaskGet, TaskList,
  TaskUpdate, TaskStop, TeamCreate, TeamDelete, ListPeers

Planning (5):
  EnterPlanMode, ExitPlanMode, EnterWorktree, ExitWorktree, VerifyPlanExecution

MCP Integration (4):
  mcp, ListMcpResources, ReadMcpResource, McpAuth

System (8):
  AskUserQuestion, TodoWrite, Skill, Config, RemoteTrigger,
  CronCreate, CronList, CronDelete

Experimental (7+) [🔒 feature-gated]:
  Sleep, SendUserMessage, StructuredOutput, LSP, SendUserFile,
  PushNotification, Monitor, SubscribePR [🔒 KAIROS_GITHUB_WEBHOOKS]
```

### Architecture Breakdown by Directory

```
# Claude Code Codebase Structure (leaked source map, ccunpacked.dev)
# Total: 1,900+ files, 519K+ lines of TypeScript/JavaScript

utils/        564 files  — shared utility modules
components/   389 files  — React/Ink terminal UI (Ink + Yoga flexbox)
commands/     189 files  — 95 CLI command handlers
tools/        184 files  — 42 built-in + 11 gated tools
services/     130 files  — API, MCP, compression, streaming
hooks/        104 files  — React state management
ink/           96 files  — Ink framework extensions
bridge/        31 files  — remote control infrastructure (unreleased)
constants/     21 files
skills/        20 files  — loadable prompt modules
cli/           19 files
keybindings/   14 files
tasks/         12 files
types/         11 files
migrations/    11 files
context/        9 files
memdir/         8 files
entrypoints/    8 files
state/          6 files
buddy/          6 files  — Tamagotchi companion (April Fools', unreleased)
vim/            5 files
remote/         4 files
query/          4 files
server/         3 files
coordinator/    1 file   — multi-agent coordinator (unreleased)
voice/          1 file   — voice input (unreleased)
```

### Unreleased Feature Inventory

```
# Unreleased features in Claude Code source (ccunpacked.dev, April 2026)

KAIROS:        Cross-session memory integration, autonomous background ops,
               /dream skill for nightly distillation, daily append-only logs,
               GitHub webhook subscriptions [🔒 KAIROS_GITHUB_WEBHOOKS],
               background daemon workers, 5-minute cron refresh

Coordinator:   Primary agent splits tasks, spawns workers in isolated git
               worktrees; orchestration via system prompt instructions
               (src/coordinator/ — 1 file)

Bridge:        Remote control from mobile/browser via WebSocket + JWT auth;
               permission approval UI for remote tool-call gates

Daemon Mode:   Background sessions via tmux containers; controllable via
               Bridge or Unix domain sockets

UDS Inbox:     Inter-session communication via Unix domain sockets

Auto-Dream:    Post-session knowledge consolidation into persistent memory

UltraPlan:     10-30 min planning sessions on Opus; editable output before
               execution begins

Buddy System:  Tamagotchi companion — 18 species, rarity tiers, 1% shiny,
               RPG stats (DEBUGGING, SNARK); Mulberry32 PRNG from user ID;
               species names encoded via String.fromCharCode()
```

### Permission and Context Tier Architecture

```
# Permission system (3 levels)
deny    → tool call is blocked, no user interaction
check   → programmatic validation runs before proceeding
prompt  → human must approve before the call executes

# Context tier hierarchy (4 levels, outer overrides inner)
global   → ~/.claude/settings.json
project  → .claude/settings.json (or CLAUDE.md)
session  → runtime configuration for the current session
call     → per-tool-invocation overrides
```

## Cross-References

- **Corroborates**:
  - **failure-alex000kim-claudecode-source-leak** (issue #20): This source and the
    alex000kim note are complementary extractions from the same leak. The alex000kim
    note covers four production findings (autoCompact circuit breaker, 14-vector
    cache tracking, coordinator prompt directives, bash security). This note covers
    the architectural map (agent loop, tool taxonomy, codebase structure, unreleased
    features). The autoCompact.ts attribution in Step 10 of the agent loop connects
    directly to alex000kim's Lesson 1. The coordinator/ directory (1 file) corroborates
    alex000kim's Lesson 3. The DANGEROUS_uncachedSystemPromptSection() finding from
    alex000kim maps to Step 4 (system prompt assembly) of this loop.
  - **research-wasnotwas-context-compaction**: Step 10 (Post-Sampling Hooks fires
    auto-compaction from autoCompact.ts) confirms wasnotwas's source-code-level
    findings on when compaction triggers. Step 5 (re-injection of recently-read
    files, plan file after compaction) described in wasnotwas Claim 5 maps to
    the context.ts role in Step 4 of each new turn.
  - **blog-addyosmani-code-agent-orchestra**: Osmani's Claim 4 (Agent Teams via
    `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) now has architectural grounding: the
    TeamCreate/TeamDelete tools in the Agents & Tasks category are the programmatic
    surface for that feature. The Ralph Loop's "reset context" step maps to REPL
    Wait (Step 11) + a new session start. The coordinator orchestration pattern
    Osmani describes matches Coordinator Mode's architecture.
  - **failure-hooks-enforcement-2k**: The meloncafe practitioner built 14 custom
    enforcement hooks because prose CLAUDE.md rules were unreliable. This source
    reveals the native "check" permission tier that provides programmatic validation
    at the permission level — the hook system effectively reimplements the check
    tier externally. Both sources confirm that prose rules alone are insufficient
    for enforcement.
  - **discussion-hn-kiln-orchestration**: Kiln's one-worktree-per-issue pattern
    maps exactly to Coordinator Mode's "spawns workers in isolated git worktrees."
    Kiln was a practitioner-built implementation of what Anthropic has implemented
    natively (but not yet released) in Coordinator Mode.

- **Contradicts**:
  - No direct contradictions with existing source notes. However, the permission
    system's "check" tier (programmatic validation without human approval) is a
    middle option that several existing notes ignore, treating permissions as
    binary (allow/deny). This is a gap in the corpus, not a contradiction.

- **Extends**:
  - **failure-alex000kim-claudecode-source-leak**: Provides the architectural
    context (agent loop, system prompt assembly) that explains *why* the four
    production failures in that note occurred. The autoCompact runaway (Lesson 1)
    makes more sense knowing it happens in the Post-Sampling Hooks step on every
    turn. The coordinator prompt directives (Lesson 3) now have a structural home:
    coordinator/ (1 file, isolated from the main agent loop).
  - **research-wasnotwas-context-compaction**: Adds step-level attribution (Step 4
    = system prompt re-injection, Step 10 = compaction trigger) that wasnotwas
    describes at a formula level without naming the agent loop steps. The two
    together give a formula-level AND step-level picture of compaction.

- **Novel**:
  - **The complete 11-step agent loop with source file attribution** is not
    documented anywhere else in our corpus. Every other source describes agent
    behavior at the output level; this is the only source that maps behavior to
    specific TypeScript files.
  - **The tool taxonomy with 8 categories and 53+ tools** is not systematically
    covered by any other source. Practitioners working from docs know 10-15 tools;
    this reveals 50+ including the entire orchestration surface (Agents & Tasks,
    Planning categories).
  - **The Planning tool category** (EnterPlanMode, ExitPlanMode, EnterWorktree,
    ExitWorktree, VerifyPlanExecution) as a native feature set is undocumented
    elsewhere in our corpus.
  - **The three-level permission system** (deny / check / prompt) and the 4-tier
    context hierarchy are not described in any existing source note.
  - **The Bridge, Daemon, UDS Inbox, Auto-Dream, and UltraPlan** unreleased features
    are partially documented in alex000kim but are mapped architecturally here for
    the first time.
  - **The game-engine TUI architecture** (~50x stringWidth reduction, Int32Array
    pools, patch optimizer) is unique to this source.
  - **The feature-gated tool flags** (WEB_BROWSER_TOOL, KAIROS_GITHUB_WEBHOOKS)
    visible in the taxonomy are not documented in any other corpus source.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: The 11-step agent loop should anchor the
  "How Claude Code works" conceptual section. Key additions:
  (1) Step 4 explains why CLAUDE.md is always in effect — it is assembled into the
  system prompt every turn, not loaded once. This justifies the emphasis on
  CLAUDE.md quality.
  (2) Step 10 explains when hooks fire (post-sampling) and why they are the right
  enforcement mechanism — they are structurally integrated into the loop, not
  bolted on externally.
  (3) The "check" permission tier should be highlighted as the enforcement primitive
  practitioners can use without building full hook systems.
  (4) The four-tier context hierarchy (global → project → session → call) is the
  canonical answer to "where should I put this configuration?" questions.

- **Chapter 02 (Tool System)**: Add a section on the full tool taxonomy, emphasizing
  the Agents & Tasks and Planning categories that practitioners typically don't know
  about. The SendMessage (IPC via Unix sockets) tool for inter-process communication
  is the native primitive behind both kiln-style orchestration and the UDS Inbox
  unreleased feature. The VerifyPlanExecution tool in the Planning category is worth
  calling out explicitly — it provides programmatic plan verification.

- **Chapter 03 (Safety and Verification)**: The three-level permission system
  (deny / check / prompt) should replace the binary allow/deny framing in any
  safety sections. The "check" tier is the architectural home for the verification
  patterns Osmani and others recommend. Update any section that treats permissions
  as binary to include the programmatic "check" option.

- **Chapter 04 (Context Engineering)**: The agent loop diagram should be the
  visual anchor for context engineering discussions. The key insight from Step 4
  (system prompt assembled from 4 sources every turn) is that context is not a
  fixed input — it is dynamically assembled. This changes the optimization target:
  you are tuning the assembly process, not editing a static file. The 4-tier context
  hierarchy is directly actionable: global settings persist across projects, project
  settings persist within a repo, session settings reset at /clear, call-level
  overrides are per-invocation.

- **Chapter 04 (Multi-Agent Orchestration)**: The Coordinator Mode architecture
  (1 file in coordinator/, prompt-only orchestration) is the production reference
  for prompt-based multi-agent coordination. The KAIROS feature (if released)
  would change the chapter's "persistent agent memory" section significantly —
  worth monitoring and updating when KAIROS ships.

- **Chapter 05 (Team Adoption / Future-Looking)**: The unreleased features (Bridge,
  Daemon, KAIROS, Coordinator, UltraPlan) represent the near-future trajectory of
  Claude Code. The chapter's "What's coming" section should describe these as
  confirmed-from-source rather than speculative:
  (1) Persistent agent daemons (KAIROS + Daemon Mode) will change session management
  (2) Mobile/remote approval gates (Bridge) will change the human-in-the-loop model
  (3) Built-in coordinator (Coordinator Mode) will reduce the custom orchestration
  work practitioners currently do manually
  (4) Extended planning (UltraPlan) will formalize the spec-before-implement pattern.

## Extraction Notes

- **Primary source inaccessible**: ccunpacked.dev returns HTTP 403 as of 2026-04-14,
  likely due to a DMCA takedown. Content was recovered from github.com/TUARAN/ccunpacked-zh
  (Chinese translation, 74KB single-file HTML mirror of the original site). The
  original site was accessible when it received 1,056 HN upvotes on April 1, 2026;
  the 403 post-dates the HN discussion.
- **Corroborated by multiple independent sources**: The architectural claims
  (file counts, tool names, loop steps, feature gating) are confirmed across:
  the Chinese translation, the HN discussion thread (47597085, 402 comments),
  the alex000kim blog post analysis, and the subagent research in this extraction.
  No single source had to be trusted in isolation.
- **Snapshot warning**: This is a snapshot of a specific leaked version. Tool
  counts, directory structure, and unreleased feature status will change across
  Claude Code releases. Before citing specific numbers (53 tools, 1900 files,
  19 categories of slash commands) in a printed guide edition, verify against
  current documentation or community reports.
- **Relationship to issue #20 (alex000kim)**: The Prospector's triage correctly
  identified these as distinct extractions. The alex000kim note (PR #95) focuses
  on production failure metrics and production-grade engineering patterns; this
  note focuses on the architecture map. A Smith synthesizing Chapter 02 should
  read both together.
- **Personality & UX category** (frustration detection, undercover mode, buddy
  system): The ccunpacked.dev site explicitly organized these as a distinct
  category — "Personality & UX" — alongside the functional tool categories. This
  framing is itself an insight: Anthropic treats personality and UX as first-class
  system concerns, not afterthoughts. The frustration detection being regex-based
  (not LLM-based) is the implementation detail most worth preserving.
- **April Fools' context**: The site launched April 1, 2026 (same day as the
  main HN leak discussion peak). The Buddy companion system is an April Fools'
  feature confirmed by Anthropic-adjacent HN commenters. The timing of the site
  launch and the companion system's presence may have been coordinated to maximize
  viral spread.
