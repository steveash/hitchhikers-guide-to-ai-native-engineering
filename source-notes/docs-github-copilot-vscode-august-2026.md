---
source_url: https://github.blog/changelog/2026-08-31-github-copilot-in-vs-code-august-2026-releases
source_type: docs
title: "GitHub Copilot in VS Code, August 2026 releases"
author: GitHub (official changelog)
date_published: 2026-08-31
date_extracted: 2026-09-01
last_checked: 2026-09-01
status: current
confidence_overall: settled
issue: "#3140"
---

# GitHub Copilot in VS Code, August 2026 Releases

> GitHub's August 31, 2026 monthly VS Code roundup (v1.132–v1.135) documents
> the first concrete product feature built on the Agent Host Protocol —
> connecting multiple VS Code windows to one running agent session and
> continuing Copilot/Claude sessions started in other applications — an
> experimental sign-in-free Agents window path for API-key-configured Claude,
> a reframing of Claude model switching around "Anthropic subscription" vs.
> "Copilot subscription" rather than BYOK, an experimental VS Code-native
> `/rubber-duck` command trailing the CLI's GA version, per-turn per-model
> token-usage visibility, and dictation gaining project-aware transcript
> cleanup and shell-aware terminal-command handling.

## Source Context

- **Type**: docs (GitHub official product changelog, August 31, 2026; "3
  minute read" monthly roundup covering VS Code v1.132 through v1.135,
  organized into four theme sections — Agent sessions and workflows, Chat
  and review, Integrated browser, and Dictation).
- **Author credibility**: GitHub engineering team announcing production,
  preview, and experimental features in VS Code Copilot. Authoritative for
  the existence of each feature, exact setting/command names, and the
  behavioral descriptions given in the article. Not a credible source for:
  adoption metrics, whether the Agent Host or sign-in-free access
  measurably change practitioner behavior, or effectiveness data for the
  dictation or `/rubber-duck` features.
- **Scope**: Monthly roundup of all VS Code Copilot updates released across
  August 2026 (v1.132–v1.135), organized into the four clusters above. Does
  NOT cover: CLI-specific features, Visual Studio (non-Code — that product's
  August 2026 update is a separate corpus note,
  `docs-github-copilot-vs-august-2026.md`), or JetBrains/Eclipse equivalents.
  As a monthly summary, it substantially overlaps with the two intervening
  weekly digests (`docs-github-copilot-weekly-releases-aug3-2026.md`,
  `docs-github-copilot-weekly-releases-aug10-2026.md`) for items shipped in
  early-to-mid August; several bullets here are corroborating restatements
  of those, not new information (see Cross-References). Does not name a
  rollout timeline for any experimental feature reaching Stable-default or
  GA, and does not link to a dedicated Agent Host documentation page beyond
  a YouTube introduction video (not fetched — see Extraction Notes).

## Extracted Claims

### Claim 1: Multiple chats within a session can now be arranged side by side in horizontal or vertical groups, with the layout restored when the practitioner returns to the session
- **Evidence**: "Agent sessions and workflows" section, first bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Arrange chats side by side: Keep multiple chats visible in
  horizontal or vertical groups to compare results or follow your agent’s
  work, with the layout restored when you return to the session."
- **Our assessment**: This is a layout-level extension of the multi-chat
  capability documented in `docs-github-copilot-vscode-july-2026.md` Claim 3
  (per-chat history/title/model within one session) and Claim 4 (forking a
  peer chat) — those claims established that a session can hold multiple
  independent chats, but said nothing about viewing more than one at a time.
  "Arrange chats side by side" adds simultaneous visual comparison (e.g., two
  peer chats exploring different approaches from the same fork point, viewed
  concurrently rather than tabbed), plus layout persistence across session
  revisits — a UX detail not previously documented for any Copilot
  multi-chat surface. For Ch04 (Agentic Workflows — Multi-Session): document
  side-by-side chat groups as the recommended way to compare parallel
  approaches from a forked conversation without switching tabs back and
  forth.

### Claim 2: A prompt timeline control in the transcript gutter lets practitioners navigate directly to specific prompts in a chat and review the file changes associated with each
- **Evidence**: "Agent sessions and workflows" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Navigate the chat conversation: Use the prompt timeline
  control from the transcript gutter to easily navigate to specific prompts
  in chat and review the related file changes."
- **Our assessment**: This is the first corpus documentation of a
  timeline-style navigation control tied to a chat transcript's gutter (a
  UI element previously documented only for the hybrid Markdown
  editor's diff indicators, `docs-github-copilot-vscode-july-2026.md`
  Claim 12 / `docs-github-copilot-weekly-releases-aug3-2026.md` Claim 7).
  Coupling prompt navigation to "the related file changes" for each prompt
  is the operative detail — it implies each turn's file diffs are indexed
  and jumpable from a single control, rather than requiring the
  practitioner to scroll the transcript to find which prompt produced a
  given change. For Ch01 (Daily Workflows): document the prompt timeline as
  the recommended way to audit or revisit a long agent session's history of
  prompts and their corresponding file edits, one prompt at a time.

### Claim 3: An experimental setting lets practitioners open the Agents window without GitHub sign-in, when Claude is configured with an API key
- **Evidence**: "Agent sessions and workflows" section, fifth bullet.
- **Confidence**: emerging (explicitly labeled an "experimental setting")
- **Quote**: "Open the Agents window without GitHub sign-in: Enable the
  experimental setting to open the Agents window without GitHub sign-in when
  Claude is configured with an API key."
- **Our assessment**: This is a notable access-model change for the
  Agents window specifically — every prior corpus documentation of Agents
  window usage assumes an authenticated GitHub Copilot session as the entry
  point, with BYOK models (Anthropic among them, per
  `docs-github-copilot-byok-vscode.md` Claim 2) layered on top of that
  authenticated session rather than replacing it. This experimental setting
  decouples the Agents window from GitHub sign-in entirely when the model
  provider is Claude via a direct API key, suggesting VS Code's Agents
  window can now function as a thin, Copilot-account-independent client for
  an Anthropic API key. The source does not say whether other BYOK
  providers (Gemini, OpenAI, Ollama, etc. — per the BYOK note's Claim 2)
  get the same sign-in-free path, or whether this is Claude-specific by
  design. For Ch02 (Harness Engineering — Model Configuration): flag this
  as a potential onboarding path for practitioners who want to use VS
  Code's Agents window purely as an Anthropic API client without a GitHub
  Copilot subscription, pending confirmation of whether other providers are
  supported the same way.

### Claim 4: Claude sessions can now switch at any time between models drawn from the practitioner's Anthropic subscription and models from their Copilot subscription
- **Evidence**: "Agent sessions and workflows" section, sixth bullet.
- **Confidence**: emerging (the source does not clarify whether this is the
  same mechanism as the BYOK-based per-turn switching documented one release
  earlier, or a distinct subscription-based arrangement — see assessment)
- **Quote**: "Switch model providers in Claude sessions: Choose between
  models from your Anthropic subscription and Copilot subscription at any
  time."
- **Our assessment**: This closely parallels `docs-github-copilot-weekly-releases-aug10-2026.md`
  Claim 16 (VS Code 1.133, published three weeks earlier), which described
  "choosing between Claude BYOK and built-in Copilot models for each new
  turn" within a Claude session. The wording here is different in a
  potentially meaningful way: Claim 16 named "Claude BYOK" (implying an
  API-key-based bring-your-own-key arrangement) as one side of the switch,
  while this August 31 entry names "models from your Anthropic subscription"
  — a phrase that reads as a direct, billed Anthropic account relationship
  rather than a bare API key. Both sources agree the switch happens within
  a single Claude session and is available "at any time" / "for each new
  turn." Neither this source nor the August 10 one states whether "Anthropic
  subscription" and "Claude BYOK" refer to the same underlying integration
  described in different terms across two changelog entries, or whether
  GitHub introduced a second, subscription-based (as opposed to
  API-key-based) way to bring Anthropic models into a Copilot session
  between the two releases. This is flagged as a wording delta worth
  watching, not resolved by inference, and does not meet MINER.md §4a's bar
  for a contradiction (both readings lead to the same guide advice: Claude
  sessions in VS Code can now mix Anthropic-sourced and Copilot-sourced
  models mid-session). For Ch02: update model-provider-switching guidance to
  note this ambiguity and prefer citing the more detailed of the two
  sources if a practitioner needs to know exactly which account
  relationship (API key vs. subscription) governs the non-Copilot side of
  the switch.

### Claim 5: VS Code can now view and continue recent Copilot or Claude agent sessions that were created in other applications, from the VS Code Sessions list
- **Evidence**: "Agent sessions and workflows" section, seventh bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Continue external agent sessions: View and continue recent
  Copilot or Claude agent sessions created in other applications from the
  Sessions list in VS Code."
- **Our assessment**: This extends `docs-github-copilot-vscode-may-2026.md`
  Claim 5 (chat sessions sync automatically to the user's GitHub account,
  giving a "searchable history of your work across machines and
  workspaces") by adding cross-*application* continuity, not just
  cross-machine: a session started in a different app entirely (the
  standalone GitHub Copilot app is the obvious candidate, per the app
  features documented across the two weekly digests) can now be picked up
  and continued inside VS Code specifically. Naming both "Copilot" and
  "Claude" as session types that can be continued this way is consistent
  with the multi-provider framing established elsewhere in this note
  (Claim 4) and the corpus generally. The source does not specify which
  other applications are supported sources (the standalone Copilot app? a
  CLI session? another IDE?) beyond "other applications." For Ch04
  (Agentic Workflows — Multi-Session): document cross-application session
  continuation as extending the May 2026 cross-machine session-sync
  capability to a cross-surface one — a practitioner can now start a
  session in one Copilot surface and resume it in VS Code's Sessions list
  without re-establishing context.

### Claim 6: The Agent Host lets a practitioner connect multiple VS Code windows to the same running agent session
- **Evidence**: "Agent sessions and workflows" section, eighth bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog, naming "the Agent Host" as the mechanism)
- **Quote**: "Connect windows to the same session: Use the Agent Host to
  connect to the same agent session from multiple VS Code windows."
- **Our assessment**: This is the first corpus documentation of a concrete,
  named product feature built on the Agent Host Protocol (AHP), which
  `docs-github-copilot-vscode-may-2026.md` Claim 3 documented four months
  earlier as an in-progress, pre-GA effort ("continued investment in an open
  protocol for synchronizing agent session state across multiple clients")
  without describing any specific capability it enabled yet. This August
  entry both names the client-facing product ("the Agent Host," as opposed
  to "the Agent Host Protocol") and gives its first concrete practitioner
  workflow: connecting multiple VS Code *windows* — not just multiple
  client types — to a single running session, so the same live agent
  conversation and its state are visible from more than one window
  simultaneously. This is a narrower realization than the May claim's
  framing of AHP as a potential cross-client (VS Code, CLI, mobile,
  third-party) interoperability layer, but it is the first evidence AHP has
  shipped a usable feature rather than remaining an announced protocol
  investment. For Ch02 (Harness Engineering): update the AHP tracking note
  to record this as AHP's first shipped, named capability, and flag that
  the corpus still lacks confirmation of cross-*client-type* (not just
  cross-window) synchronization.

### Claim 7: An experimental `/rubber-duck` command in a Copilot Agent Host session asks a complementary model to surface missed details and edge cases
- **Evidence**: "Agent sessions and workflows" section, ninth bullet.
- **Confidence**: emerging (explicitly labeled experimental; contrast with
  the CLI version's GA status — see assessment)
- **Quote**: "Get a second opinion: Try the experimental /rubber-duck
  command in a Copilot Agent Host session to ask a complementary model to
  surface missed details and edge cases."
- **Our assessment**: `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`
  Claim 1 documented `/rubber-duck` reaching GA in Copilot CLI back in June
  2026, described there as "a built-in CLI agent that acts as a
  constructive critic" reviewing "plans, designs, implementations, or
  tests." This August 31 VS Code entry brings the same command name and
  broadly the same purpose (a second-opinion peer-review pass) to a second
  surface — the Agents window's Agent Host — but at an earlier maturity
  stage (experimental, not GA) and with a narrower stated scope ("surface
  missed details and edge cases" rather than the CLI version's four named
  artifact types). The source does not say whether this is the same
  underlying rubber-duck agent reimplemented for VS Code or an
  independently-built, VS Code-specific feature that happens to share a
  name and purpose — consistent with the corpus's general caution (see the
  `/rewind` naming-convergence discussion in
  `docs-github-copilot-weekly-releases-aug3-2026.md` Claim 10) about
  inferring shared implementation from shared command names across
  surfaces. For Ch04 (Agentic Workflows — Verification): document VS Code's
  `/rubber-duck` as the Agents-window counterpart to the CLI's GA
  peer-review agent, still experimental, and note practitioners should
  expect the CLI version's more developed feature set (four review target
  types) as a preview of where the VS Code version may head.

### Claim 8: Chat now supports full-text search across the complete conversation transcript, with case-matching, whole-word, and regular-expression options
- **Evidence**: "Chat and review" section, first bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Find text across a conversation: Avoid endless scrolling to
  find a search term with text search across the complete chat transcript
  with options for case matching, whole words, and regular expressions."
- **Our assessment**: This is the first corpus documentation of an
  in-transcript search feature for any Copilot chat surface — prior
  navigation aids in the corpus (quick chat, `/btw` side chats, the prompt
  timeline in Claim 2 above, sticky-scroll pinned prompts) all address
  finding or re-orienting around a specific *prompt*, not searching
  arbitrary *text* across an entire conversation's accumulated output. The
  three named options (case matching, whole words, regular expressions)
  match standard code-editor find-in-file semantics, suggesting GitHub
  reused VS Code's existing text-search UI conventions for the chat
  surface rather than building a bespoke search experience. For Ch01
  (Daily Workflows): document transcript search as the recommended tool
  for locating a specific fact, command, or file path mentioned earlier in
  a long-running agent session, rather than manually scrolling or relying
  on the prompt timeline (which navigates by prompt, not by arbitrary
  search term).

### Claim 9: Hovering over a chat response's footer now shows input, cached input, and output token usage broken down by model, for that specific chat turn
- **Evidence**: "Chat and review" section, sixth bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "View token usage by model: Hover over the response footer to
  see input, cached input, and output token usage for each model in a chat
  turn."
- **Our assessment**: This is a token-granularity complement to the
  credit-granularity visibility documented in
  `docs-github-copilot-vscode-june-2026.md` Claim 8 (total session credit
  cost and per-subagent credit inspection) — that claim covers *cost* in
  credits; this one covers the underlying *token* mechanics (input, cached
  input, output) that drive cost, broken down per model, per turn. The
  explicit "cached input" category is notable: it surfaces prompt-cache
  utilization directly in the chat UI, letting a practitioner see whether a
  given turn benefited from caching without needing external
  telemetry or API-level usage reports. This is also relevant alongside the
  per-chat, per-turn model-switching capabilities documented in this note
  (Claim 4) and `docs-github-copilot-vscode-july-2026.md` Claim 3 — as
  sessions increasingly mix models within one conversation, per-turn,
  per-model token visibility becomes necessary to attribute cost correctly
  across a mixed-model session. For Ch04 (Cost Management): document
  hover-based per-turn, per-model token visibility (input/cached
  input/output) as the most granular in-editor cost-attribution signal
  documented in the corpus so far, complementing the coarser
  session/subagent credit totals from June 2026.

### Claim 10: Practitioners can now set the integrated browser as the default editor for local HTML files via the editor associations setting
- **Evidence**: "Integrated browser" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Open HTML files in the browser by default: If you often
  preview local HTML files instead of editing them, you can now set the
  integrated browser as their default editor by configuring the editor
  associations setting."
- **Our assessment**: This is a workflow-default change for practitioners
  who primarily use HTML files as rendered output to preview (rather than
  as text to edit) — configuring the editor-associations setting means
  double-clicking or opening such a file routes straight to the integrated
  browser instead of the text editor by default, removing a manual "open
  in browser" step. It builds on the integrated browser's live-reload
  property (`docs-github-copilot-weekly-releases-aug10-2026.md` Claim 18,
  corroborated in this source's "Reload HTML files automatically" bullet)
  — together, a practitioner whose HTML files default-open in the browser
  and auto-reload on change gets a near-live-preview workflow with two
  fewer manual steps than before either feature existed. For Ch01 (Daily
  Workflows — UI/Frontend Review): document the editor-associations
  configuration as a one-time setup step for practitioners doing
  frontend/HTML review work, to pair with the auto-reload behavior already
  documented.

### Claim 11: Dictation transcript cleanup can now be customized with user-level or workspace-level instructions covering project terminology and formatting preferences
- **Evidence**: "Dictation" section, second bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Customize transcript cleanup: Add user-level or
  workspace-level instructions so dictation follows your project
  terminology and formatting preferences."
- **Our assessment**: This extends `docs-github-copilot-vscode-july-2026.md`
  Claim 13, which documented the `dictation.experimental.llmCleanup`
  setting as a binary on/off toggle for LLM-based transcript reformatting
  (removing filler words, adding formatting) with no customization
  mechanism described. This August entry adds a configuration layer on top
  of that toggle: instructions can be scoped per-user or per-workspace, so
  a team can standardize how dictated text is cleaned up for
  project-specific terminology (e.g., correctly capitalizing a product or
  API name that generic cleanup would not know) rather than relying on
  generic LLM cleanup alone. The source does not state whether these
  instructions live in a dedicated settings file, inline VS Code settings,
  or an existing customization mechanism (e.g., the instructions files
  already used for agent behavior). For Ch05 (Team Adoption —
  Accessibility): document workspace-level transcript-cleanup instructions
  as a way for teams to make dictation output consistent with existing
  project terminology, extending the July 2026 dictation feature.

### Claim 12: Dictation for terminal commands now applies shell-aware cleanup that preserves command syntax instead of literally inserting spoken punctuation
- **Evidence**: "Dictation" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Improve dictation for terminal commands: Shell-aware cleanup
  preserves command syntax instead of inserting spoken punctuation
  literally."
- **Our assessment**: This addresses a specific failure mode implied but
  not previously documented for dictation-in-terminal: without shell
  awareness, a practitioner dictating a command containing spoken
  punctuation (e.g., saying "pipe" or "dash dash") would risk having the
  literal word transcribed rather than the intended shell syntax (`|`,
  `--`). "Shell-aware cleanup" implies the transcript-cleanup layer (Claim
  11, and the July 2026 `dictation.experimental.llmCleanup` setting) now
  has context-sensitive behavior that differs for terminal input versus
  chat or editor input. `docs-github-copilot-vscode-july-2026.md` Claim 13
  named the terminal as one of three surfaces dictation covers (chat,
  editor, terminal) but described only generic filler-word/formatting
  cleanup, not shell-specific syntax handling. For Ch01 (Daily Workflows):
  document shell-aware dictation cleanup as removing a specific practical
  barrier (mistranscribed command syntax) to using voice input for running
  terminal commands, extending the July 2026 dictation baseline.

## Concrete Artifacts

### August 2026 VS Code Copilot Release — Full Section Breakdown (v1.132–v1.135)

```
GitHub Copilot in VS Code, August 2026 releases
Source: github.blog/changelog, published 2026-08-31, retrieved 2026-09-01
Coverage: VS Code v1.132 through v1.135, shipped throughout August 2026

AGENT SESSIONS AND WORKFLOWS
  - Arrange chats side by side — horizontal/vertical groups, layout
    restored on return                                           [Claim 1]
  - Open a side-conversation — /btw shares primary chat's context and
    prompt cache (corroborates
    docs-github-copilot-weekly-releases-aug3-2026.md Claim 4)
  - Navigate the chat conversation — prompt timeline control from
    transcript gutter, review related file changes                [Claim 2]
  - Install portable agent plugins — Agent Plugins 1.0 standard, VS Code
    and other compatible clients (corroborates
    docs-github-copilot-agent-plugins-1-0.md)
  - Open the Agents window without GitHub sign-in — experimental setting,
    Claude configured with an API key                              [Claim 3]
  - Switch model providers in Claude sessions — Anthropic subscription vs.
    Copilot subscription, at any time                              [Claim 4]
  - Continue external agent sessions — Copilot/Claude sessions from other
    applications, via VS Code Sessions list                        [Claim 5]
  - Connect windows to the same session — Agent Host, multiple VS Code
    windows                                                        [Claim 6]
  - Get a second opinion — experimental /rubber-duck in a Copilot Agent
    Host session                                                   [Claim 7]
  - Review session details next to chat — default single-pane layout,
    width-adaptive diffs
  - "See it in action in our Agent Host introduction YouTube video."
    (video link, not fetched)

CHAT AND REVIEW
  - Find text across a conversation — full transcript search, case/whole
    word/regex options                                             [Claim 8]
  - Keep the current prompt visible — chat sticky scroll (corroborates
    docs-github-copilot-weekly-releases-aug10-2026.md Claim 17, "pinned
    prompt")
  - Review rendered Markdown diffs — hybrid Markdown editor combines
    diff-viewing and editing (corroborates
    docs-github-copilot-vscode-july-2026.md Claim 12 and
    docs-github-copilot-weekly-releases-aug3-2026.md Claim 7)
  - Switch editor types from the breadcrumb bar — regular/diff editors,
    Agents window (relocates/refines
    docs-github-copilot-vscode-july-2026.md's "toolbar"-based toggle)
  - Resize terminal output in chat — reflows as view is resized
  - View token usage by model — hover response footer, input/cached
    input/output tokens per model per turn                        [Claim 9]

INTEGRATED BROWSER
  - Comment on web page elements — select/annotate multiple HTML elements,
    batch feedback (corroborates
    docs-github-copilot-weekly-releases-aug3-2026.md Claim 5)
  - Reload HTML files automatically — local file changes reflected without
    manual refresh (corroborates
    docs-github-copilot-weekly-releases-aug10-2026.md Claim 18)
  - Open HTML files in the browser by default — editor associations
    setting                                                       [Claim 10]

DICTATION
  - Dictate in multiple languages — on-device model, auto-detect or chosen
    language (corroborates
    docs-github-copilot-weekly-releases-aug3-2026.md Claim 6, narrower
    wording — no mention of system/browser locale or mic onboarding)
  - Customize transcript cleanup — user/workspace-level instructions for
    project terminology and formatting                            [Claim 11]
  - Improve dictation for terminal commands — shell-aware cleanup
    preserves command syntax                                      [Claim 12]
```

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-vscode-july-2026.md`,
`docs-github-copilot-vscode-june-2026.md`,
`docs-github-copilot-vscode-may-2026.md`,
`docs-github-copilot-weekly-releases-aug3-2026.md`,
`docs-github-copilot-weekly-releases-aug10-2026.md`,
`docs-github-copilot-byok-vscode.md`,
`docs-github-copilot-cli-rubber-duck-scheduling-voice.md`, and
`docs-github-copilot-agent-plugins-1-0.md` were re-read directly in those
notes (via `### Claim N:` headings) before citing, per MINER.md §4b; claim
numbers are counted top-to-bottom in document order as they appear in each
cited note.

- **Extends** `docs-github-copilot-vscode-july-2026.md` (Claim 3, per-chat
  history/title/model; Claim 4, forking a peer chat): Claim 1 of this note
  adds simultaneous side-by-side viewing and persisted layout to the
  multi-chat capability those claims established.

- **Extends** `docs-github-copilot-vscode-may-2026.md` (Claim 3, Agent Host
  Protocol as an in-progress "continued investment"): Claim 6 of this note
  is the first corpus documentation of a concrete, named feature ("the
  Agent Host") built on that protocol — connecting multiple VS Code windows
  to one session.

- **Extends** `docs-github-copilot-vscode-may-2026.md` (Claim 5, chat
  session sync across machines via GitHub account): Claim 5 of this note
  adds cross-*application* session continuation, not only cross-machine.

- **Extends and contrasts with**
  `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 1,
  `/rubber-duck` reaching GA in Copilot CLI, June 2026): Claim 7 of this
  note documents the same command name arriving on a second surface (VS
  Code's Agent Host) at an earlier maturity stage (experimental) and with a
  narrower stated scope, without confirming shared implementation.

- **Extends** `docs-github-copilot-vscode-june-2026.md` (Claim 8, total
  session and per-subagent credit visibility): Claim 9 of this note adds a
  finer-grained, per-turn, per-model token breakdown (input/cached
  input/output), complementing June's credit-level totals.

- **Extends** `docs-github-copilot-vscode-july-2026.md` (Claim 13,
  experimental `dictation.experimental.llmCleanup` toggle): Claims 11 and
  12 of this note add configurable user/workspace-level cleanup
  instructions and shell-aware terminal-command handling on top of that
  toggle.

- **Possible restatement, wording delta flagged, not resolved** —
  `docs-github-copilot-weekly-releases-aug10-2026.md` (Claim 16, per-turn
  switching between "Claude BYOK and built-in Copilot models" in VS Code
  1.133): Claim 4 of this note describes what may be the same capability
  three weeks later as switching between models from the practitioner's
  "Anthropic subscription" and "Copilot subscription." Both sources agree
  on the mechanics (mid-session, any-time/per-turn switching within a
  Claude session) but differ on whether the non-Copilot side is
  characterized as a bring-your-own-API-key arrangement or a subscription
  relationship. This does not meet MINER.md §4a's bar for a contradiction
  — both readings support identical guide advice — but is flagged for a
  future source to resolve.

- **Corroborates** `docs-github-copilot-weekly-releases-aug3-2026.md`
  (Claim 4, `/btw` side chat; Claim 5, element-level browser feedback;
  Claim 6, multilingual on-device dictation; Claim 7, hybrid Markdown
  editor diff review) and `docs-github-copilot-weekly-releases-aug10-2026.md`
  (Claim 17, pinned-prompt/sticky scroll; Claim 18, integrated-browser
  live HTML reload): this source restates each of these without adding
  new detail (the multilingual dictation restatement is narrower — it
  omits the earlier sources' system/browser-locale-following and
  microphone-onboarding details). Not given dedicated claims here; see
  Concrete Artifacts for verbatim restated bullets.

- **Corroborates** `docs-github-copilot-agent-plugins-1-0.md`: the "Install
  portable agent plugins" bullet restates that source's VS Code Agent
  Plugins 1.0 GA coverage without new detail.

- **Contradicts**: None identified that meet MINER.md §4a's filing bar. The
  Claim 4 wording delta (Anthropic subscription vs. Claude BYOK) is flagged
  above but not filed, per the same reasoning applied to the `/rewind`
  wording delta in `docs-github-copilot-weekly-releases-aug10-2026.md`
  Claim 9 — both readings lead to the same guide advice.

- **Novel**:
  - First corpus documentation of a concrete, named Agent Host feature
    (cross-window session connection) built on the Agent Host Protocol
    (Claim 6).
  - First corpus documentation of a sign-in-free Agents window access path
    for API-key-configured Claude (Claim 3).
  - First corpus documentation of cross-application (not just
    cross-machine) agent session continuation (Claim 5).
  - First corpus documentation of `/rubber-duck` on a second surface (VS
    Code Agent Host, experimental) after its CLI GA (Claim 7).
  - First corpus documentation of full-text search across a chat
    transcript (Claim 8).
  - First corpus documentation of per-turn, per-model token-usage
    visibility (input/cached input/output) in a chat UI (Claim 9).
  - First corpus documentation of shell-aware dictation cleanup for
    terminal commands (Claim 12).

## Guide Impact

### Chapter 01: Daily Workflows

- **Prompt timeline and transcript search**: Document the prompt timeline
  control (Claim 2) and full-text transcript search (Claim 8) together as
  two complementary navigation aids for long agent sessions — timeline for
  jumping by prompt/file-change, search for locating arbitrary text.
- **HTML preview workflow**: Document the editor-associations
  default-to-browser setting (Claim 10) alongside the already-documented
  auto-reload behavior as a two-part frontend-review workflow setup.
- **Dictation refinements**: Add shell-aware terminal dictation cleanup
  (Claim 12) as removing a specific mistranscription barrier for
  voice-driven terminal commands.

### Chapter 02: Harness Engineering

- **Agent Host Protocol tracking**: Update the AHP entry to record its
  first shipped, named capability — cross-window session connection via
  "the Agent Host" (Claim 6) — while noting cross-client-type
  synchronization (VS Code ↔ CLI ↔ mobile) remains undocumented.
- **Sign-in-free Agents window access**: Flag the experimental
  API-key-only Claude access path (Claim 3) as a potential lower-friction
  onboarding route, pending confirmation of whether it extends to other
  BYOK providers.
- **Model-switching terminology**: Note the "Anthropic subscription" vs.
  "Claude BYOK" wording delta (Claim 4) when documenting Claude model
  switching in VS Code, until a more detailed source resolves it.

### Chapter 04: Agentic Workflows — Multi-Session, Verification, and Cost Optimization

- **Side-by-side chat comparison**: Document arranging chats side by side
  (Claim 1) as the recommended way to visually compare parallel approaches
  from a forked conversation.
- **Cross-application session continuity**: Add continuing
  externally-created Copilot/Claude sessions from VS Code's Sessions list
  (Claim 5) as extending the May 2026 cross-machine sync to cross-surface
  continuity.
- **VS Code `/rubber-duck` (experimental)**: Document as the Agents-window
  counterpart to the CLI's GA peer-review agent (Claim 7), noting its
  earlier maturity stage and narrower scope.
- **Per-turn, per-model token visibility**: Add hover-based token usage by
  model (Claim 9) as the most granular in-editor cost-attribution signal
  documented so far, useful for sessions that mix models across turns.

### Chapter 05: Team Adoption — Accessibility

- **Dictation cleanup customization**: Document user/workspace-level
  transcript-cleanup instructions (Claim 11) as a way for teams to
  standardize dictated output around project terminology.

## Extraction Notes

1. **WebFetch avoided in favor of raw HTML, per established corpus
   precedent**: Following the precedent in
   `docs-github-copilot-vscode-july-2026.md` Extraction Note 1 and the two
   weekly-digest notes' Extraction Notes (all of which found WebFetch
   paraphrased or, in one case, fabricated content for this same
   changelog series), the article was fetched directly via `curl` with a
   browser user-agent, the `<article>` element was isolated, block-level
   tags were converted to line breaks, and remaining markup was stripped —
   producing a verbatim plain-text transcript of every heading and bullet.
   Every `Quote` field above was checked by exact substring match against
   that transcript, including curly-apostrophe punctuation (e.g.,
   "agent’s work").
2. **No substantive linked sub-pages followed**: The article's outbound
   links are same-page table-of-contents anchors, a YouTube video
   ("Agent Host introduction"), and a link to the general (non-Copilot
   -specific) VS Code 1.132–1.135 release notes at `aka.ms/VSCode/Release`.
   Consistent with the judgment call in the June/July 2026 VS Code notes,
   the general release notes were not followed. The YouTube video was not
   fetched — video content is outside this Miner pass's text-extraction
   scope, and the changelog's own prose (Claim 6) already states the
   Agent Host's core capability in text.
3. **Overlap with the two intervening weekly digests was expected and
   handled per the Prospector's triage guidance**: The Prospector's triage
   comments flagged `docs-github-copilot-weekly-releases-aug10-2026.md`
   and `docs-github-copilot-weekly-releases-aug3-2026.md` as overlapping
   notes and asked for "novel feature clusters or agent/harness
   improvements not already covered." Roughly half of this article's ~20
   bullets restate items already documented in one of the two weekly
   digests or the July 2026 roundup (see Concrete Artifacts for the
   restated bullets and Cross-References for corroboration mapping); these
   were deliberately not given dedicated Claim entries. The twelve claims
   above are either genuinely new to the corpus or add a materially new
   detail (granularity, surface, or access model) to an existing claim.
4. **Minor items not given dedicated claims**: "Review session details
   next to chat" (single-pane layout, width-adaptive diffs) and "Resize
   terminal output in chat" (reflow on view resize) were judged to be
   UI/ergonomics polish without enough distinct behavioral detail for an
   independent claim, consistent with how the July and August 10 notes
   handled comparably thin bullets. Both are preserved verbatim in
   Concrete Artifacts.
5. **One wording delta flagged, no contradiction filed**: Claim 4's
   "Anthropic subscription and Copilot subscription" framing versus
   `docs-github-copilot-weekly-releases-aug10-2026.md` Claim 16's "Claude
   BYOK and built-in Copilot models" framing was evaluated against
   MINER.md §4a's filing criteria. Both descriptions lead to the same
   guide advice (Claude sessions in VS Code support mid-session switching
   between Copilot-native and non-Copilot-sourced models), so this was
   treated as an open wording question to flag rather than a contradiction
   to file, consistent with how the `/rewind` wording delta was handled in
   `docs-github-copilot-weekly-releases-aug10-2026.md` Claim 9 and
   Extraction Note 4.
