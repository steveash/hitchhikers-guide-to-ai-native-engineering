---
source_url: https://github.blog/changelog/2026-07-30-github-copilot-in-visual-studio-code-july-2026-releases
source_type: docs
title: "GitHub Copilot in Visual Studio Code, July 2026 releases"
author: GitHub (official changelog)
date_published: 2026-07-30
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: settled
issue: "#2352"
---

# GitHub Copilot in Visual Studio Code, July 2026 Releases

> GitHub's July 30, 2026 VS Code roundup (v1.127–v1.131) documents the Agents
> window's move toward supporting any coding-agent harness in isolated Git
> worktrees, a new sub-session "multiple chats" model with per-chat forking,
> Copilot vision's arrival specifically inside Agents-window chat, BYOK models
> extended into the Agents window, an experimental "modernized" VS Code UI,
> and the product's first built-in dictation and Markdown-editing-by-agent
> features.

## Source Context

- **Type**: docs (GitHub official product changelog, July 30, 2026; roundup
  covering VS Code releases v1.127 through v1.131 from July 2026; "3 minute
  read" organized into five theme sections — Agents window improvements,
  Multi-chat sessions, Chat and model updates, Editor/terminal/browser, and
  Accessibility/dictation).
- **Author credibility**: GitHub engineering team announcing production and
  preview features in VS Code Copilot. Authoritative for the existence of
  each feature, exact setting names (`dictation.enabled`,
  `dictation.experimental.llmCleanup`), and the behavioral descriptions given
  in the article. Not a credible source for: adoption metrics, whether the
  "modernized" UI or worktree-based sessions measurably improve outcomes, or
  any effectiveness data for the accessibility features.
- **Scope**: Roundup of all VS Code Copilot updates released in July 2026,
  organized into the five clusters above. Does NOT cover: CLI-specific
  features, Visual Studio (non-Code) features, or JetBrains/Eclipse
  equivalents — those have separate changelogs and separate corpus notes
  (e.g. `docs-github-copilot-jetbrains-otel-model-management-july2026.md`).
  Does not describe the internal implementation of worktree-based sessions,
  does not name which harnesses beyond Copilot/Claude/Codex can be started in
  a worktree, and does not specify a rollout timeline for the "modernized" UI
  reaching Stable by default.

## Extracted Claims

### Claim 1: The VS Code Agents window can now start Copilot, Claude, or Codex sessions inside an isolated Git worktree
- **Evidence**: "Agents window improvements" section, one of seven listed
  improvements to the (still public-preview) Agents window.
- **Confidence**: emerging (Agents window is explicitly still in public
  preview; feature is stated as shipped, not itself flagged preview, but
  inherits the surrounding preview status)
- **Quote**: "Use worktrees with any harness: Start Copilot, Claude, or
  Codex sessions in a Git worktree, so each session can work in an isolated
  copy of your repository."
- **Our assessment**: This is the first corpus documentation of GitHub's own
  VS Code surface explicitly naming worktree isolation as a first-class,
  cross-harness session mechanism — and the first to name Claude and Codex as
  interchangeable harnesses alongside Copilot within the same Agents window
  feature. "Any harness" is the operative phrase: it frames worktree
  isolation as a property of the Agents window container, not of a specific
  agent product. For Ch02 (Harness Engineering): document VS Code worktree
  sessions as a built-in, GitHub-native alternative to hand-rolled worktree
  scripting for running parallel isolated sessions — directly relevant to any
  guide section on multi-session workflows or harness-agnostic tooling, since
  this is presented as working the same way regardless of which of the three
  named agent products is running.

### Claim 2: The Agents window now lets practitioners see each running subagent's model, elapsed time, and active tool call, and open a subagent's conversation without losing the parent conversation
- **Evidence**: "Agents window improvements" section.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Track running subagents: See each subagent's model, elapsed
  time, and active tool call, then open its conversation without losing the
  parent conversation."
- **Our assessment**: This extends `docs-github-copilot-vscode-june-2026.md`
  Claim 8 (per-subagent *credit* visibility) with a distinct, complementary
  form of subagent introspection — execution state (model, elapsed time,
  active tool call) rather than cost. Together the two releases give
  practitioners running delegation-heavy workflows two independent lenses on
  subagent activity: what it's costing (June) and what it's doing right now
  (July). The "without losing the parent conversation" detail is the
  concrete UX claim — a practitioner can drill into a subagent's live
  conversation and return to the orchestrating session without having to
  re-navigate. For Ch04 (Agentic Workflows — Multi-Session): document this
  as the debugging complement to per-subagent cost inspection, useful when a
  subagent appears stalled or is calling an unexpected tool.

### Claim 3: A single Agents-window session can now hold multiple related chats, each with its own history, title, and model, instead of one linear conversation
- **Evidence**: "Multi-chat sessions" section header ("Multi-chat support for
  Claude") plus the section's opening framing.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Multi-chat support for Claude: A single agent session can now
  hold multiple related chats, each with its own history, title, and model,
  instead of just one linear conversation."
- **Our assessment**: This is a refinement of, not a new capability beyond,
  `docs-github-copilot-vscode-june-2026.md` Claim 7, which already documented
  "multiple chats within a single session" as a June 2026 feature. What this
  July article adds is two specifics the June note did not have: each chat
  within a session carries its own *model* (not just its own history/title),
  and the feature is explicitly labeled "for Claude" in this rollout — though
  the body text does not restrict which models can populate the per-chat
  slots, only that per-chat model selection now exists. For Ch04: update the
  sub-session-parallelism guidance to note that chats within one session can
  now run different models from each other, not just cover different
  workstreams (implementation/review/testing/docs) on a shared model.

### Claim 4: Practitioners can fork a conversation into a peer chat from any point, and the new peer chat retains the original conversation's context without needing to repeat it
- **Evidence**: "Multi-chat sessions" section, second bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Fork into a peer chat: Explore a different approach from any
  point in your conversation. The new peer chat keeps the original context,
  so you don't have to repeat it."
- **Our assessment**: This is a novel branching primitive not previously
  documented in the corpus for GitHub Copilot: rather than starting a new
  chat from scratch or editing/regenerating a message in place, a
  practitioner can split an existing conversation into two independent
  chats that share a common history up to the fork point. This directly
  supports an "explore N approaches from the same starting context" pattern
  without manually re-pasting context into parallel sessions. For Ch04:
  document conversation forking as a lower-friction alternative to spinning
  up an entirely separate session when a practitioner wants to try a second
  approach without abandoning the first.

### Claim 5: A new "quick chat" lets practitioners ask a question without opening a workspace, and quick chats remain separate from project sessions
- **Evidence**: "Agents window improvements" section.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Start a quick chat: Ask a question without opening a
  workspace. Quick chats stay separate from your project sessions."
- **Our assessment**: This targets a specific friction point — needing a
  quick answer or sanity check without the overhead of opening/selecting a
  project workspace first — and explicitly isolates that lightweight
  interaction from tracked project sessions (so it presumably does not
  pollute session history, worktree state, or per-project subagent tracking
  described in Claims 1–2). For Ch01 (Daily Workflows): document quick chat
  as the recommended path for one-off questions that shouldn't be
  attributed to (or tracked within) a specific project's agent session
  history.

### Claim 6: The Agents window now surfaces failed CI checks and new pull request review comments in a banner above the chat input, so practitioners can act on them from chat
- **Evidence**: "Agents window improvements" section, final bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Handle pull request updates from chat: Act on failed CI checks
  and new review comments from a banner above the chat input."
- **Our assessment**: This extends `docs-github-copilot-vscode-june-2026.md`
  Claim 12 ("smarter pull request creation" — generating a PR's title and
  description from session context) by covering the step *after* PR
  creation: once a PR exists and CI fails or a reviewer comments, the
  practitioner is surfaced that update directly in the originating chat
  session rather than needing to switch to the PR on github.com. For Ch01
  (Daily Workflows): document this as closing the loop between VS Code
  session-based PR creation and post-creation PR maintenance — a
  practitioner can now create a PR and continue responding to review/CI
  outcomes without leaving the Agents window session that produced it.

### Claim 7: Copilot Business and Enterprise users can now check their total AI credit usage for the current billing cycle directly from the Copilot status menu
- **Evidence**: "Chat and model updates" section.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Check your AI credit usage: Copilot Business and Enterprise
  users can see their total credit usage for the current billing cycle in
  the Copilot status menu."
- **Our assessment**: This extends
  `docs-github-copilot-usage-metrics-ai-credits-per-user.md` Claim 1 (the
  `ai_credits_used` REST API field added to per-user usage metrics reports)
  by adding a self-service UI surface for the same underlying signal. The
  two are for different audiences: the REST API field (Claim 1 there,
  Claim 6 there) requires enterprise-admin or org-owner access; this status
  menu view is end-user-facing, letting an individual developer check their
  own current-cycle consumption without needing metrics API access. For
  Ch04 (Cost Management): document the Copilot status menu as the
  lowest-friction way for an individual practitioner to self-monitor credit
  consumption, distinct from the admin-facing usage metrics API.

### Claim 8: BYOK models, previously usable throughout VS Code Chat but not the Agents window specifically, are now also usable with the Copilot agent inside the Agents window
- **Evidence**: "Chat and model updates" section, explicitly referencing the
  original March 2025 (v1.99) BYOK-in-editor availability as the baseline
  this extends.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Use BYOK models in the Agents window: BYOK models have been
  available in the VS Code editor since the 1.99 (March 2025) release. Now
  you can also use them with the Copilot agent in the Agents window."
- **Our assessment**: This extends `docs-github-copilot-byok-vscode.md`
  Claim 3, which documented BYOK models as available "anywhere in VS Code
  Chat, including the built-in plan agent and custom agents" as of the
  April 2026 BYOK GA announcement — the Agents window (a Copilot-specific,
  session-oriented UI first documented in the May/June 2026 roundups) was
  either not yet released or not yet BYOK-compatible at that time. This
  closes that gap: practitioners using external-provider models via BYOK
  (Anthropic, Gemini, OpenAI, OpenRouter, Azure, Ollama, Foundry Local per
  the BYOK note's Claim 2) can now use them for Agents-window sessions, not
  only classic VS Code Chat. For Ch02 (Harness Engineering — Model
  Configuration): update BYOK guidance to note Agents-window compatibility
  as of this July 2026 release, removing any earlier caveat that BYOK was
  chat-only and excluded the newer session-based Agents window.

### Claim 9: Chat messages in the Agents window can be prefixed with "!" to run their contents directly as a terminal command
- **Evidence**: "Chat and model updates" section, final bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Run commands with the ! prefix: Start a chat message with ! to
  run its contents as a terminal command in the Agents window."
- **Our assessment**: This is a novel low-level workflow shortcut not
  previously documented in the corpus for GitHub Copilot — it collapses the
  context switch between "ask the agent something" and "run a shell command
  myself" into the same input box, without invoking the agent's own
  reasoning or tool-use loop for that message. For Ch01 (Daily Workflows):
  document the `!` prefix as a fast path for practitioners who want to run
  an ad hoc command inline while working in an Agents-window chat, without
  switching focus to a separate terminal panel or asking the agent to run it
  on their behalf.

### Claim 10: A "modernized" VS Code user interface is available as an opt-in experimental feature in Stable and is enabled by default in Insiders
- **Evidence**: "Editor, terminal, and browser" section, first bullet.
- **Confidence**: emerging (explicitly experimental/preview; default-on only
  in the pre-release Insiders channel)
- **Quote**: "Modern UI preview: Try the modernized VS Code user interface,
  available as an experimental feature in Stable and enabled by default in
  Insiders. Share your feedback with us."
- **Our assessment**: This is a general-editor UI change, not
  Copilot-specific, but is included in the Copilot changelog roundup
  presumably because it affects how the Agents window and chat surfaces are
  rendered. The changelog gives no detail on what specifically changes
  visually or interactionally — only that it exists and its default-on
  status differs by release channel. For Ch01: flag this as a
  forward-looking UI change practitioners on Insiders will see by default
  and Stable users can opt into; without further detail, no specific
  guide recommendation beyond awareness is warranted yet.

### Claim 11: VS Code can now turn existing prompt files into reusable skills via a migration path in the AI Customizations overview
- **Evidence**: "Editor, terminal, and browser" section.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Migrate prompt files to skills: Turn existing prompt files
  into reusable skills from the AI Customizations overview."
- **Our assessment**: This extends
  `docs-github-copilot-jetbrains-cli-enhancements-june2026.md` Claim 9
  ("Agent skills, agent hooks, prompt files, and Anthropic Thinking all
  reach general availability in the June 2026 JetBrains update") by adding a
  concrete migration mechanism between two of those GA'd primitives in VS
  Code specifically: rather than leaving prompt files and skills as two
  parallel, independently-authored customization formats, VS Code now offers
  a direct conversion path from one to the other. For Ch02 (Harness
  Engineering — Customization): document this migration path for teams that
  built up a library of prompt files before skills existed and want to
  consolidate onto the skills format without hand-rewriting each one.

### Claim 12: An experimental feature lets practitioners view and edit Markdown files in place within the Agents window, including adding comments an agent can act on
- **Evidence**: "Editor, terminal, and browser" section, final bullet.
- **Confidence**: emerging (explicitly labeled experimental)
- **Quote**: "Edit Markdown with agents: This experimental feature lets you
  view and edit Markdown files in place in the Agents window, and add
  comments that an agent can act on."
- **Our assessment**: The "add comments that an agent can act on" mechanism
  parallels `docs-github-copilot-vscode-june-2026.md` Claim 11 (Gutter
  feedback — leaving comments on an agent's changes from the editor gutter),
  but inverts the direction: gutter feedback is a human commenting on
  agent-authored changes for the agent to potentially revise, while this
  Markdown-editing feature is a human leaving comments in a Markdown
  document itself (not necessarily agent-authored) as instructions for an
  agent to act on. For Ch01 (Daily Workflows): document this as an
  experimental, document-centric complement to gutter feedback — useful for
  practitioners editing specs, docs, or planning documents in place and
  wanting to hand off specific sections to an agent via inline comments,
  rather than restating instructions in a separate chat message.

### Claim 13: VS Code has added built-in, experimental dictation for chat, the editor, and the integrated terminal, with an optional LLM-based transcript cleanup setting
- **Evidence**: "Accessibility and dictation" section, first two bullets,
  each naming a specific experimental setting.
- **Confidence**: emerging (both settings explicitly labeled experimental)
- **Quote**: "Built-in dictation: Enable the experimental dictation.enabled
  setting to use dictation in chat, the editor, and the integrated
  terminal." / "Optional transcript cleanup: Enable the experimental
  dictation.experimental.llmCleanup setting to let Copilot tidy your
  transcript as you speak by adding formatting and removing filler words."
- **Our assessment**: This is the first documented native, built-in
  dictation feature for GitHub Copilot in this corpus (prior
  voice-related corpus entries, e.g.
  `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`, cover a
  different CLI-specific voice feature). The two settings are independent:
  `dictation.enabled` turns on speech-to-text across three surfaces (chat,
  editor, terminal), and `dictation.experimental.llmCleanup` is an
  opt-in second layer that has Copilot itself reformat the raw transcript
  (removing filler words, adding formatting) rather than inserting raw
  speech-to-text output. For Ch05 (Team Adoption — Accessibility): document
  both settings as concrete accessibility levers, and note the LLM-cleanup
  setting implies transcript text is passed through a model before
  insertion — a data-handling detail this changelog does not elaborate on
  (e.g., which model, whether the same privacy/retention terms as chat
  apply).

### Claim 14: Practitioners can now choose where integrated browser tabs open — the active editor group, a dedicated side group, or a separate window
- **Evidence**: "Editor, terminal, and browser" section.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Configurable browser tab placement: Choose where integrated
  browser tabs open: the active group, a dedicated side group, or a separate
  window."
- **Our assessment**: This is a workspace-layout refinement to the
  integrated browser tooling whose GA and trust model were documented in
  `docs-github-copilot-vscode-june-2026.md` Claim 1 (agentic browser tools
  reaching GA, enabled by default) and Claims 2–4 (the private-tabs/
  isolated-sessions trust model). This July release does not change the
  trust model; it adds display-placement flexibility so a practitioner
  running a browser-driving agent session can keep the browser tab visible
  alongside code (side group) or fully out of the way (separate window)
  rather than only inline with other editor tabs. For Ch02: document this
  as a workspace-ergonomics option for teams that have already adopted the
  June 2026 browser-tools GA and want to control screen layout during
  browser-driven agent testing.

## Concrete Artifacts

### July 2026 VS Code Copilot Release — Full Section Breakdown (v1.127–v1.131)

```
GitHub Copilot in VS Code, July 2026 releases
Source: github.blog/changelog, published 2026-07-30, retrieved 2026-07-31
Coverage: VS Code v1.127 through v1.131, shipped throughout July 2026

AGENTS WINDOW IMPROVEMENTS (public preview)
  - Review code alongside chat — redesigned editor panel; open files/diffs
    next to conversation; shared tab bar
  - Review changes faster — addition/deletion counts per file, compact diff
    view, inline/side-by-side diff switch
  - Use worktrees with any harness — Copilot, Claude, or Codex sessions in
    an isolated Git worktree                                    [Claim 1]
  - Start a quick chat — question without opening a workspace    [Claim 5]
  - Group and reorder sessions — drag items/groups/workspace headers
  - Track running subagents — model, elapsed time, active tool call,
    open conversation without losing parent                     [Claim 2]
  - Handle pull request updates from chat — banner for failed CI checks
    and new review comments                                      [Claim 6]

MULTI-CHAT SESSIONS
  - Multi-chat support for Claude — multiple chats per session, each with
    own history/title/model                                      [Claim 3]
  - Fork into a peer chat — branch from any point, retains context [Claim 4]
  - Close, reopen, and delete chats — via tab / Conversations dropdown /
    tab menu
  - Keyboard-driven navigation — create/switch/reopen/close chats via
    shortcuts scoped to the Agents window

CHAT AND MODEL UPDATES
  - Add images and PDFs to chat — Copilot vision GA (corroborates
    docs-github-copilot-vision-ga.md, published 2026-07-01)
  - Check your AI credit usage — Copilot status menu, current billing
    cycle, Business/Enterprise                                   [Claim 7]
  - Use BYOK models in the Agents window — extends March 2025 (v1.99)
    editor-level BYOK availability                                [Claim 8]
  - Run commands with the ! prefix — terminal command from chat input
    in the Agents window                                         [Claim 9]

EDITOR, TERMINAL, AND BROWSER
  - Modern UI preview — experimental in Stable, default-on in Insiders
                                                                   [Claim 10]
  - Open files from git diff — click Git-prefixed paths (i/, w/) in
    terminal diff output
  - Configurable browser tab placement — active group / side group /
    separate window                                              [Claim 14]
  - Use shortcuts when VS Code is in the background — OS-level keyboard
    shortcuts run VS Code commands while another app has focus
  - Migrate prompt files to skills — via AI Customizations overview
                                                                   [Claim 11]
  - Switch editor type from the toolbar — e.g. preview a diff in the
    Markdown editor instead of default diff view
  - Edit Markdown with agents (experimental) — view/edit Markdown in
    place in Agents window; add comments an agent can act on     [Claim 12]

ACCESSIBILITY AND DICTATION
  - Built-in dictation (experimental dictation.enabled) — chat, editor,
    integrated terminal                                          [Claim 13]
  - Optional transcript cleanup (experimental
    dictation.experimental.llmCleanup) — formatting, filler-word removal
                                                                   [Claim 13]
  - Terminal screen reader control — cursor stays in place in Accessible
    View as new output arrives; read at own pace without interruption
```

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-vscode-june-2026.md`,
`docs-github-copilot-byok-vscode.md`,
`docs-github-copilot-jetbrains-cli-enhancements-june2026.md`, and
`docs-github-copilot-usage-metrics-ai-credits-per-user.md` were re-read
directly in those notes before citing (per MINER.md §4b); claim numbers are
counted top-to-bottom in document order as they appear in each cited note.

- **Corroborates** `docs-github-copilot-vision-ga.md` (Claim 1, Claim 3):
  this source's "Add images and PDFs to chat: Copilot vision is now
  generally available" bullet restates the July 1, 2026 GA announcement
  (Claim 1 there) and its VS Code agent-mode availability (Claim 3 there)
  without adding new detail — included in the "also new" roundup rather than
  extracted as a dedicated claim here since it introduces nothing beyond
  what the dedicated vision-GA note already documents in depth.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 7, multi-chat
  sessions): Claim 3 of this note adds per-chat model selection and the
  "for Claude" rollout labeling to the multi-chat-within-a-session capability
  the June note first documented.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 8, per-subagent
  cost visibility): Claim 2 of this note adds a second, execution-state
  (model/elapsed-time/tool-call) lens on running subagents, complementary to
  June's cost lens.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 12, smarter PR
  creation): Claim 6 of this note covers the post-creation step — surfacing
  CI failures and review comments in chat — that June's PR-creation claim
  does not address.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 11, Gutter
  feedback): Claim 12 of this note (Edit Markdown with agents) documents an
  inverse-direction comment mechanism — a human annotating a Markdown
  document for an agent to act on, rather than a human commenting on an
  agent's already-produced changes.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 1, browser
  tools GA): Claim 14 of this note (configurable browser tab placement) is a
  workspace-layout addition to the browser tooling whose GA and trust model
  June's Claims 1–4 documented; the trust model itself is unchanged.

- **Extends** `docs-github-copilot-byok-vscode.md` (Claim 3, BYOK surface
  coverage): Claim 8 of this note closes a gap that note left open — BYOK
  models are now usable in the Agents window specifically, not only "VS Code
  Chat" as scoped in the April 2026 BYOK GA announcement.

- **Extends** `docs-github-copilot-jetbrains-cli-enhancements-june2026.md`
  (Claim 9, prompt files/skills GA): Claim 11 of this note adds a concrete
  VS Code migration path between the two customization formats that note
  documented reaching GA together in JetBrains.

- **Extends** `docs-github-copilot-usage-metrics-ai-credits-per-user.md`
  (Claim 1, `ai_credits_used` REST API field): Claim 7 of this note adds a
  self-service, end-user-facing UI surface (Copilot status menu) for
  current-cycle credit usage, distinct from the admin/API-facing metrics
  field that note documents.

- **Contradicts**: None identified. No claim in this source opposes an
  existing corpus position. No contradiction issue filed.

- **Novel**:
  - First documentation of GitHub's own VS Code Agents window supporting
    worktree-isolated sessions across three named harnesses (Copilot,
    Claude, Codex) as a single feature (Claim 1).
  - First documentation of conversation forking ("peer chat") as a branching
    primitive for GitHub Copilot (Claim 4).
  - First documentation of a native, built-in Copilot dictation feature with
    an LLM-based transcript-cleanup option (Claim 13).
  - First documentation of per-chat model selection within a single Agents
    window session (Claim 3), beyond the session-level and chat-level
    parallelism already in the corpus.
  - First documentation of an inline "run this chat message as a terminal
    command" shortcut (`!` prefix) for GitHub Copilot (Claim 9).

## Guide Impact

### Chapter 01: Daily Workflows

- **Quick chat and the `!` prefix**: Document quick chat (Claim 5) as the
  recommended path for one-off questions outside project session tracking,
  and the `!` prefix (Claim 9) as a fast inline path for running a command
  without invoking agent reasoning.
- **PR lifecycle inside chat**: Add "Handle pull request updates from chat"
  (Claim 6) as closing the loop with the existing PR-creation-from-session
  guidance (`docs-github-copilot-vscode-june-2026.md` Claim 12) — a
  practitioner can now create and maintain a PR without leaving the
  originating Agents-window session.
- **Markdown editing with agents**: Note the experimental in-place Markdown
  editing + agent-actionable comments feature (Claim 12) as a
  document-centric complement to gutter feedback, still experimental.

### Chapter 02: Harness Engineering

- **Worktree-based multi-harness sessions**: Document VS Code's built-in
  worktree support for Copilot/Claude/Codex sessions (Claim 1) as a
  GitHub-native alternative to custom worktree scripting for parallel
  isolated sessions.
- **BYOK now covers the Agents window**: Update BYOK guidance
  (`docs-github-copilot-byok-vscode.md`) to remove any Agents-window
  exclusion caveat — BYOK models are usable there as of this release
  (Claim 8).
- **Prompt-file-to-skill migration**: Document the AI Customizations
  overview's migration path (Claim 11) for teams consolidating older
  prompt-file libraries onto the skills format.
- **Browser workspace layout**: Add configurable browser tab placement
  (Claim 14) as a layout option for teams using the June 2026 browser-tools
  GA.

### Chapter 04: Agentic Workflows — Multi-Session and Cost Optimization

- **Per-chat model selection**: Update sub-session parallelism guidance to
  note that chats within a single session can now each use a different
  model (Claim 3), not only split by workstream.
- **Conversation forking**: Add peer-chat forking (Claim 4) as a
  lower-friction alternative to a new session for exploring a second
  approach from shared context.
- **Subagent execution-state visibility**: Add live subagent tracking
  (model, elapsed time, active tool call — Claim 2) as a debugging
  complement to the existing per-subagent cost visibility.

### Chapter 05: Team Adoption

- **Self-service credit visibility**: Add the Copilot status menu credit
  view (Claim 7) as the individual-practitioner-facing complement to the
  admin-facing `ai_credits_used` metrics API field.
- **Dictation accessibility settings**: Document `dictation.enabled` and
  `dictation.experimental.llmCleanup` (Claim 13) as concrete accessibility
  levers, flagging both as experimental and noting the open question of
  which model processes cleanup transcripts and under what data-handling
  terms.

## Extraction Notes

1. **WebFetch summary discarded in favor of raw HTML**: An initial WebFetch
   call to the article URL returned a plausible but paraphrased summary
   (e.g., rendering "Modern UI preview" as "Modern UI preview (experimental)"
   with restructured bullet text, and compressing several distinct bullets
   into single sentences). Per MINER.md §2a, this was not treated as
   quote-safe. The raw article HTML was fetched via `curl` (following one
   redirect from the bare slug to its canonical form), the `<article>`
   element was isolated, and block-level tags were converted to line breaks
   before stripping remaining markup — producing a verbatim plain-text
   transcript of every heading and bullet in the article. All `Quote` fields
   above are copied character-for-character from that raw-HTML transcript,
   not from the WebFetch summary.
2. **No substantive linked sub-pages**: The article's only outbound links
   are same-page table-of-contents anchors, a link to the `aka.ms/VSCode/Release`
   aggregator for the underlying VS Code 1.127–1.131 release notes, a link
   to `code.visualstudio.com`, and the `copilot`-label changelog listing.
   The VS Code version release notes are general-purpose (not
   Copilot-specific) and, consistent with the June 2026 note's judgment call
   on the same category of link, were not followed — the roundup itself is
   the complete Copilot-specific record of this release cycle.
3. **Minor items not given dedicated claims**: Of the ~26 individual bullets
   across the five sections, twelve were judged to have UI/workflow detail
   too thin for an independent claim or to be pure ergonomics refinements
   with minimal distinct guide impact (editor panel redesign, diff-view
   polish, session grouping/reordering, chat close/reopen/delete, keyboard
   navigation, opening files from git-diff terminal output, background
   OS-level shortcuts, switching editor type from the toolbar, and terminal
   screen-reader cursor behavior). These are preserved verbatim in the
   Concrete Artifacts section for corpus completeness but were not expanded
   into full Claim entries, consistent with the precedent set in
   `docs-github-copilot-vscode-june-2026.md` Extraction Note 3.
4. **No contradictions identified**: Cross-referencing against the June 2026
   VS Code roundup, the BYOK note, the vision-GA note, the JetBrains June
   2026 enhancements note, and the AI-credits-per-user usage-metrics note
   found no claims in this source that oppose an existing corpus position.
   Claim 3 (multi-chat per-model, "for Claude") refines rather than
   contradicts June's Claim 7 (multi-chat sessions existed already; this adds
   a per-chat model dimension). No contradiction issue filed.
5. **"Multi-chat support for Claude" heading ambiguity**: The section
   heading names Claude specifically, but the body sentence describes the
   capability generically ("each with its own history, title, and model")
   without restricting which models can be used in a multi-chat session.
   This note does not resolve that ambiguity — it is flagged in Claim 3's
   assessment as an open question (is this a Claude-specific rollout stage,
   or is "for Claude" simply the headline example) rather than resolved with
   speculation.
