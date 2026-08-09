---
source_url: https://github.blog/changelog/2026-08-07-github-copilot-weekly-releases-august-3
source_type: docs
title: "GitHub Copilot weekly releases — August 3"
author: GitHub (official changelog)
date_published: 2026-08-07
date_extracted: 2026-08-09
last_checked: 2026-08-09
status: current
confidence_overall: settled
issue: "#2587"
---

# GitHub Copilot Weekly Releases — August 3

> GitHub's August 7, 2026 weekly roundup covers three surfaces — the
> standalone Copilot app, Copilot CLI, and VS Code 1.132 — and documents a
> recurring "side conversation without losing primary context" pattern
> appearing independently on two surfaces (`/side` in the app, `/btw` in VS
> Code), a CLI `/rewind` command that converges on the same course-correction
> terminology already documented for Claude Code, and a multilingual
> extension of VS Code's July 2026 experimental dictation feature.

## Source Context

- **Type**: docs (GitHub official product changelog, August 7, 2026; "2
  minute read" weekly roundup organized into three sections — GitHub
  Copilot app, GitHub Copilot CLI, and VS Code 1.132 Release updates).
- **Author credibility**: GitHub engineering team announcing production and
  experimental features across three Copilot product surfaces. Authoritative
  for the existence of each feature, exact command names (`/side`,
  `/worktree`, `/rewind`, `/btw`), and the behavioral descriptions given in
  the article. Not a credible source for: adoption metrics, whether these
  features measurably improve outcomes, or effectiveness data for any
  accessibility or dictation feature.
- **Scope**: A weekly digest covering the period since the prior weekly
  release (week of August 3, 2026). Four short bullets per surface. Does
  NOT cover: JetBrains, Eclipse, Visual Studio (non-Code), or detailed
  configuration/settings documentation for any of the listed features — this
  is an announcement-level summary, not a how-to guide. Per the Prospector's
  triage guidance, individual items summarized here may also exist (or come
  to exist) as separate, more detailed standalone changelog entries and
  corpus source-notes.

## Extracted Claims

### Claim 1: The GitHub Copilot app's "Auto" model-selection mode now discloses which model actually handled each completed request, along with AI credit and cache information when available
- **Evidence**: "GitHub Copilot app" section, first bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Auto now shows which model handled each completed request, plus AI credit and cache details when they’re available."
- **Our assessment**: This is a transparency addition to Auto model
  selection specifically for the standalone Copilot app — it does not
  change routing behavior, only what the practitioner can see after the
  fact. The "when they're available" qualifier signals the credit/cache
  data is not guaranteed on every request, which the source does not
  explain further (e.g., whether cache misses or certain model providers
  omit this data). For Ch04 (Cost Management): document this as a
  post-hoc auditability improvement — a practitioner using Auto mode in the
  app can now confirm which model actually ran, rather than only seeing
  "Auto" as an opaque label in session history.

### Claim 2: The GitHub Copilot app lets users open shared sessions directly and start a parallel side conversation with `/side` without interrupting their primary task
- **Evidence**: "GitHub Copilot app" section, second bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Jump directly into shared sessions, or use /side to explore a parallel question without disrupting your main task."
- **Our assessment**: This bundles two distinct capabilities in one bullet:
  (1) direct navigation into a session that was shared with the user
  (implying a sharing mechanism exists elsewhere in the app that this note
  does not describe), and (2) `/side`, a parallel-question command. The
  `/side` half of this claim is functionally identical in stated purpose to
  VS Code's new `/btw` command in this same source (Claim 4 below) — "explore
  a parallel question without disrupting your main task" versus "open a side
  chat without interrupting the agent's current turn." For Ch01 (Daily
  Workflows): document `/side` in the Copilot app as the app-surface
  equivalent of the side-conversation pattern also shipping in VS Code this
  week, and flag that this note does not establish whether the two commands
  share an implementation or are independently built per-surface.

### Claim 3: The GitHub Copilot app's "Impeccable" skill has been updated to target mobile interface design, including configuration troubleshooting and targeted design reviews
- **Evidence**: "GitHub Copilot app" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Apply the updated Impeccable skill to mobile interfaces, diagnose its setup, and run more focused design reviews."
- **Our assessment**: This is the first appearance of "Impeccable" as a
  named skill anywhere in our corpus — the changelog treats it as
  already-existing (calling it "the updated Impeccable skill" rather than
  introducing it), so this entry documents an incremental update to a skill
  this note gives no prior context for. The three listed capabilities
  (apply to mobile interfaces, diagnose setup, run focused design reviews)
  suggest Impeccable is a design-review-oriented skill, but the source does
  not define what it evaluates against or what "mobile interfaces" scope
  means concretely (native apps, responsive web, or both). For Ch02
  (Harness Engineering — Skills): flag as a named, shipped skill worth a
  dedicated follow-up source-note once GitHub publishes standalone Impeccable
  documentation — this weekly digest is too thin to document the skill
  itself, only that it exists and was updated.

### Claim 4: VS Code adds `/btw`, a side-chat command that shares context and prompt cache with the primary conversation, letting a practitioner ask about in-progress work without interrupting the agent's current turn
- **Evidence**: "VS Code 1.132 Release updates" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Ask side questions with /btw. Open a side chat without interrupting the agent’s current turn. The side chat shares the context and prompt cache from your primary conversation, so you can ask about the work already in progress. You can also select text from a response and ask a contextual question about it."
- **Our assessment**: The "shares context and prompt cache from your primary
  conversation" detail is the operationally significant part — this is not a
  fresh side conversation that has to be re-primed with context, and
  reusing the prompt cache implies the side question should be cheaper/faster
  than starting an entirely new session covering the same ground. The
  "select text from a response and ask a contextual question" capability
  extends this beyond a generic side-chat into an inline
  clarification-on-demand tool. For Ch04 (Agentic Workflows — Multi-Session):
  document `/btw` as a lower-friction alternative to VS Code's existing
  "quick chat" (`docs-github-copilot-vscode-july-2026.md` Claim 5) — quick
  chat explicitly starts a workspace-free conversation isolated from project
  sessions, whereas `/btw` explicitly inherits the primary conversation's
  context and cache, making it suited to questions *about* the ongoing
  session rather than unrelated one-offs.

### Claim 5: VS Code's integrated browser now supports element-level feedback — selecting and annotating specific page elements with comments before sending them to the agent
- **Evidence**: "VS Code 1.132 Release updates" section, first bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "The integrated browser now supports element-level feedback. Select specific elements on a web page, attach a comment to each one, and send that precise visual feedback to the agent. You can select and annotate multiple elements before submitting your message."
- **Our assessment**: This is a precision upgrade to the integrated browser
  tooling whose GA and trust model were previously documented in
  `docs-github-copilot-vscode-june-2026.md`. Prior browser-driven feedback
  in the corpus was page- or screenshot-level; this adds a per-element
  annotation layer (multiple elements, each with its own comment, batched
  into one message) before the agent sees any of it. For Ch01 (Daily
  Workflows — UI/Frontend Review): document element-level browser annotation
  as the recommended path for reporting multiple distinct visual issues on
  one page in a single turn, rather than describing element locations in
  prose or sending one message per issue.

### Claim 6: VS Code's dictation feature now defaults to a multilingual on-device model that can follow the configured language, system/browser locale, or auto-detect the spoken language, alongside a new microphone-selection onboarding flow
- **Evidence**: "VS Code 1.132 Release updates" section, second bullet.
- **Confidence**: emerging (this extends a feature that was explicitly
  labeled experimental — `dictation.enabled` — as of the July 2026 VS Code
  roundup; this source does not state the experimental flag has been
  removed)
- **Quote**: "Dictate in multiple languages. Dictation now uses a multilingual on-device model by default, keeping audio on your device. It can follow your configured language, use your system or browser locale, or automatically detect the language. A new onboarding experience also helps you select and test your microphone."
- **Our assessment**: This directly extends
  `docs-github-copilot-vscode-july-2026.md` Claim 13, which documented VS
  Code's first built-in dictation feature (the experimental
  `dictation.enabled` setting, covering chat/editor/terminal) one week
  earlier. That July claim said nothing about language support; this source
  adds multilingual capability "by default" as the notable delta — a
  practitioner who already enabled dictation gets multi-language,
  auto-detecting speech-to-text without additional configuration. The "keeping
  audio on your device" phrasing reiterates the on-device/local-processing
  property implied but not explicitly stated for the July feature. For Ch05
  (Team Adoption — Accessibility): update the dictation guidance from
  `docs-github-copilot-vscode-july-2026.md` to note multilingual, on-device,
  auto-detecting speech recognition as of this release, plus the new
  microphone setup onboarding — still without confirmation that the
  underlying `dictation.enabled` experimental flag itself has reached GA.

### Claim 7: VS Code's experimental hybrid Markdown editor now displays Markdown diffs in-context with gutter indicators for additions, modifications, and deletions
- **Evidence**: "VS Code 1.132 Release updates" section, fourth bullet.
- **Confidence**: emerging (the hybrid Markdown editor is described as
  experimental in the source this claim extends)
- **Quote**: "Review Markdown changes in context. Markdown diffs can now open in the experimental hybrid Markdown editor. The modified document remains editable, while gutter indicators identify added, changed, and deleted content. You can switch between the text diff and hybrid Markdown views from the editor type dropdown."
- **Our assessment**: This extends `docs-github-copilot-vscode-july-2026.md`
  Claim 12 ("Edit Markdown with agents" — an experimental feature to view
  and edit Markdown files in place in the Agents window with
  agent-actionable comments). The July claim covered editing and
  commenting; this August claim adds diff review specifically — gutter
  indicators for add/change/delete plus a toggle between the classic text
  diff and the hybrid Markdown view. Together the two releases give
  practitioners an editing surface (July) and a review surface (August) for
  the same experimental hybrid Markdown editor. For Ch01 (Daily Workflows):
  document the hybrid Markdown diff view as the recommended way to review an
  agent's Markdown edits (specs, docs, planning files) in rendered form
  rather than raw text diff, with the editor-type dropdown as the
  switch point between the two views.

### Claim 8: Copilot CLI adds a Sessions sidebar for managing multiple concurrent sessions, opened with the `<` key and navigated with keyboard shortcuts for new (`n`) and close (`x`)
- **Evidence**: "GitHub Copilot CLI" section, first bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Easily manage multiple concurrent sessions from the Sessions sidebar. Simply click < (left arrow) to open the Sessions sidebar and use shortcuts to open new sessions (n), close current ones (x), and move between sessions with ease. Click > right arrow to close the sidebar."
- **Our assessment**: No prior corpus source documents a dedicated sidebar
  UI for concurrent Copilot CLI session management — the closest prior CLI
  session-management coverage (`docs-github-copilot-cli-remote-control-ga.md`)
  covers remote steering of a single session from another device, not local
  multi-session navigation within one terminal window. For Ch04 (Agentic
  Workflows — Multi-Session): document the Sessions sidebar as a built-in
  alternative to running multiple separate CLI processes (e.g., one per
  terminal tab or tmux pane) for practitioners who want to switch between
  concurrent Copilot CLI sessions without leaving a single terminal
  instance.

### Claim 9: Copilot CLI's experimental `/worktree` command creates an isolated workspace and starts a separate conversation for exploring changes without disrupting the current session
- **Evidence**: "GitHub Copilot CLI" section, second bullet.
- **Confidence**: emerging (explicitly labeled experimental in the source)
- **Quote**: "Create an isolated worktree and begin a separate conversation with the new experimental /worktree command. This gives you another workspace for exploring changes without disrupting your current work."
- **Our assessment**: This is a CLI-native counterpart to the VS Code
  Agents window's worktree support documented in
  `docs-github-copilot-vscode-july-2026.md` Claim 1 ("Use worktrees with any
  harness: Start Copilot, Claude, or Codex sessions in a Git worktree").
  That July claim was scoped to the VS Code Agents window UI; this August
  claim brings the same isolated-worktree-per-session pattern directly into
  the CLI as a slash command, without requiring VS Code. The two are
  parallel implementations of the same underlying pattern on different
  surfaces rather than one extending the other's mechanism. For Ch02
  (Harness Engineering): document `/worktree` as the CLI-native path to
  isolated parallel sessions, alongside the VS Code Agents window path,
  both still experimental/preview-labeled as of their respective
  announcements.

### Claim 10: Copilot CLI's `/rewind` command restores conversation and file changes without requiring Git
- **Evidence**: "GitHub Copilot CLI" section, third bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog, though the underlying mechanism's completeness — e.g., whether
  it survives arbitrary tool calls — is not detailed)
- **Quote**: "/rewind now restores conversation and file changes without requiring Git."
- **Our assessment**: The phrase "now restores... without requiring Git"
  implies `/rewind` already existed in some form and previously depended on
  Git for its file-restoration behavior; this source documents the
  Git-independent version without describing what the prior Git-dependent
  behavior was. This is notable for cross-vendor terminology convergence:
  `blog-anthropic-session-management-1m-context.md` Claim 4 documents
  Claude Code's own `/rewind` (double-Esc) as its "superior correction
  mechanism," and `blog-humanlayer-context-forking.md` Claim 7 notes that
  fork/rewind implementations vary by agent in whether they touch code/disk
  state alongside conversation state. GitHub Copilot CLI shipping a command
  with the identical `/rewind` name, for the identical
  conversation-plus-files restoration purpose, is a second data point (after
  Claude Code) for `/rewind` becoming a shared naming convention across
  competing agent CLIs for this course-correction mechanic — not evidence
  of shared implementation, since neither this source nor the cited notes
  describe Copilot CLI's internals. For Ch04 (Correction Patterns): add
  Copilot CLI `/rewind` alongside Claude Code `/rewind` as evidence that
  rewind-to-a-prior-turn is converging into a standard primitive across
  major agent CLIs, distinct from Git-based undo.

### Claim 11: Copilot CLI's session timeline now displays real-time duration metrics for each tool call as it executes
- **Evidence**: "GitHub Copilot CLI" section, fourth bullet.
- **Confidence**: settled (product fact stated directly in official
  changelog)
- **Quote**: "Timeline displays real-time tool-call execution duration metrics."
- **Our assessment**: This is a thin but concrete observability addition —
  a practitioner watching the CLI timeline can now see how long each tool
  call is taking as it runs, rather than only after completion or not at
  all. The source gives no further detail (e.g., whether this is visible
  only in the redesigned terminal from `docs-github-copilot-cli-terminal-ga.md`,
  or a display threshold for "slow" calls). For Ch04 (Agentic Workflows —
  Debugging): document live per-tool-call duration as a debugging aid for
  identifying which specific tool invocation is stalling a session, without
  needing to wait for the call to finish first.

## Concrete Artifacts

### Full Weekly Digest — August 3, 2026 (published August 7, 2026)

```
GitHub Copilot weekly releases — August 3
Source: github.blog/changelog, published 2026-08-07, retrieved 2026-08-09
2 minute read

GITHUB COPILOT APP
  - Auto now shows which model handled each completed request, plus AI
    credit and cache details when they're available.                [Claim 1]
  - Jump directly into shared sessions, or use /side to explore a
    parallel question without disrupting your main task.            [Claim 2]
  - Apply the updated Impeccable skill to mobile interfaces, diagnose
    its setup, and run more focused design reviews.                 [Claim 3]
  - Sessions now start and switch more efficiently.        [not independently
                                                              claimed — see
                                                              Extraction Notes]

GITHUB COPILOT CLI
  - Easily manage multiple concurrent sessions from the Sessions
    sidebar (< to open, n new, x close, > to close sidebar).         [Claim 8]
  - Create an isolated worktree and begin a separate conversation with
    the new experimental /worktree command.                          [Claim 9]
  - /rewind now restores conversation and file changes without
    requiring Git.                                                  [Claim 10]
  - Timeline displays real-time tool-call execution duration metrics. [Claim 11]

VS CODE 1.132 RELEASE UPDATES
  - The integrated browser now supports element-level feedback —
    select and annotate multiple page elements before sending.       [Claim 5]
  - Dictate in multiple languages — multilingual on-device model by
    default, configured language / system locale / auto-detect,
    plus new microphone setup onboarding.                            [Claim 6]
  - Ask side questions with /btw — side chat sharing context and
    prompt cache with the primary conversation.                      [Claim 4]
  - Review Markdown changes in context — diffs open in the
    experimental hybrid Markdown editor with gutter indicators.      [Claim 7]
```

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-vscode-july-2026.md`,
`docs-github-copilot-vscode-june-2026.md`,
`docs-github-copilot-cli-remote-control-ga.md`,
`docs-github-copilot-cli-terminal-ga.md`,
`blog-anthropic-session-management-1m-context.md`, and
`blog-humanlayer-context-forking.md` were re-read directly in those notes
before citing (per MINER.md §4b); claim numbers are counted top-to-bottom in
document order as they appear in each cited note.

- **Extends** `docs-github-copilot-vscode-july-2026.md` (Claim 1, VS Code
  Agents window worktree support): Claim 9 of this note documents a
  CLI-native `/worktree` command implementing the same
  isolated-worktree-per-session pattern as a parallel, separately-shipped
  surface rather than the same mechanism.

- **Extends** `docs-github-copilot-vscode-july-2026.md` (Claim 5, VS Code
  quick chat): Claim 4 of this note (`/btw`) is contrasted against quick
  chat — quick chat is workspace-free and isolated from project sessions,
  `/btw` explicitly inherits the primary conversation's context and prompt
  cache.

- **Extends** `docs-github-copilot-vscode-july-2026.md` (Claim 13,
  experimental `dictation.enabled`): Claim 6 of this note adds multilingual,
  auto-detecting, on-device dictation as the notable delta one week after
  the feature's first appearance in the corpus.

- **Extends** `docs-github-copilot-vscode-july-2026.md` (Claim 12, "Edit
  Markdown with agents"): Claim 7 of this note adds a diff-review mode
  (gutter indicators, text-diff/hybrid toggle) to the same experimental
  hybrid Markdown editor that July's claim covered from the editing side.

- **Extends** `docs-github-copilot-cli-remote-control-ga.md` (Claim 1,
  remote control of CLI sessions across devices): Claim 8 of this note
  (Sessions sidebar) is a *local*, single-terminal multi-session UI —
  distinct from remote control's cross-device session steering. The two are
  complementary, not overlapping: remote control lets you steer one session
  from another device; the Sessions sidebar lets you manage several
  sessions from the same terminal.

- **Corroborates** `blog-anthropic-session-management-1m-context.md`
  (Claim 4, Claude Code `/rewind`) and `blog-humanlayer-context-forking.md`
  (Claim 7, per-agent variance in whether rewind touches code/disk state):
  Claim 10 of this note is a second named-vendor instance of a `/rewind`
  command performing conversation-plus-file restoration, supporting the
  cross-vendor naming-convergence observation already flagged in the
  humanlayer note, without establishing shared implementation.

- **Contradicts**: None identified. No claim in this source opposes an
  existing corpus position. No contradiction issue filed.

- **Novel**:
  - First corpus mention of "Impeccable" as a named GitHub Copilot app skill
    (Claim 3).
  - First corpus documentation of a dedicated Sessions sidebar for local
    multi-session management in Copilot CLI (Claim 8).
  - First corpus documentation of Copilot CLI's `/rewind` command by name
    (Claim 10) — prior corpus `/rewind` coverage was Claude Code-specific.
  - First corpus documentation of a Copilot CLI worktree command
    (`/worktree`) as distinct from the VS Code Agents window's worktree
    support (Claim 9).
  - First corpus documentation of real-time, in-timeline tool-call duration
    metrics for Copilot CLI (Claim 11).

## Guide Impact

### Chapter 01: Daily Workflows

- **Element-level browser feedback**: Document the integrated browser's
  new per-element annotation (Claim 5) as the recommended path for
  reporting multiple distinct visual issues in one message, superseding
  page-level or prose-based descriptions for that use case.
- **Markdown diff review**: Add the hybrid Markdown diff view (Claim 7) as
  the recommended way to review an agent's Markdown edits in rendered form.

### Chapter 02: Harness Engineering

- **CLI-native worktree isolation**: Document Copilot CLI's experimental
  `/worktree` command (Claim 9) as a CLI-only alternative to VS Code's
  Agents-window worktree support, for practitioners who work primarily in a
  terminal rather than VS Code.
- **Impeccable skill (flag for follow-up)**: Note the existence of an
  "Impeccable" skill for mobile interface design review (Claim 3); this
  digest is too thin to document its actual behavior — recommend a
  dedicated source-note once GitHub publishes standalone documentation.

### Chapter 04: Agentic Workflows — Multi-Session and Correction Patterns

- **Sessions sidebar**: Document the Copilot CLI Sessions sidebar (Claim 8)
  as a built-in local multi-session manager, distinct from and
  complementary to remote control (cross-device single-session steering).
- **`/rewind` without Git, and cross-vendor convergence**: Add Copilot CLI
  `/rewind` (Claim 10) to the guide's correction-patterns section alongside
  Claude Code `/rewind`, framing rewind-to-a-prior-turn as a converging
  standard primitive across major agent CLIs rather than a
  single-vendor feature.
- **`/btw` side questions**: Add `/btw` (Claim 4) as VS Code's
  context-and-cache-preserving side-question mechanism, distinct from quick
  chat, and note the Copilot app's `/side` (Claim 2) as the same pattern
  shipping on a second surface in the same week.
- **Live tool-call duration**: Add real-time per-tool-call timing (Claim 11)
  as a debugging aid for identifying stalled tool calls mid-session.

### Chapter 05: Team Adoption — Accessibility

- **Multilingual on-device dictation**: Update the dictation guidance
  sourced from `docs-github-copilot-vscode-july-2026.md` Claim 13 to note
  multilingual, auto-detecting, on-device speech recognition as of this
  release (Claim 6), plus the new microphone setup onboarding flow.

## Extraction Notes

1. **WebFetch summary discarded in favor of raw HTML**: An initial WebFetch
   call to the article URL returned a paraphrased, and in one respect
   fabricated, summary — it invented a "Related Updates" list (referencing
   "Copilot impact dashboard ROI section," "Kimi K3 model availability," and
   other items) that does not appear anywhere in the actual article. Per
   MINER.md §2a, this was discarded entirely. The raw article HTML was
   fetched via `curl`, the `<article>` element was isolated, and block-level
   tags were converted to line breaks before stripping remaining markup —
   producing a verbatim plain-text transcript of every heading and bullet in
   the article, confirmed against the canonical URL
   (`.../2026-08-07-github-copilot-weekly-releases-august-3/`). All `Quote`
   fields above are copied character-for-character from that raw-HTML
   transcript, including original curly-quote punctuation, not from the
   WebFetch summary. The Assayer should treat the fabricated "Related
   Updates" list as a WebFetch artifact, not a source claim — it is not
   referenced anywhere in this note.
2. **No substantive linked sub-pages**: The article's only outbound links
   are same-page table-of-contents anchors, a "Try the Copilot app" link, an
   "Install the Copilot CLI" link, and an "Explore everything that's new in
   the full release notes" link (to the general VS Code 1.132 release
   notes, not Copilot-specific). Consistent with the precedent in
   `docs-github-copilot-vscode-july-2026.md` Extraction Note 2, the general
   VS Code release notes were not followed — this weekly digest is the
   complete Copilot-specific record for the period.
3. **One bullet not given a dedicated claim**: "Sessions now start and
   switch more efficiently" (GitHub Copilot app section, fourth bullet) is a
   bare performance claim with no quantification, mechanism, or measurable
   detail — too thin for an independent Claim entry. Preserved verbatim in
   Concrete Artifacts for corpus completeness.
4. **No contradictions identified**: Cross-referencing against the June and
   July 2026 VS Code roundups, the CLI terminal GA note, the CLI remote
   control GA note, the Claude Code session-management note, and the
   HumanLayer context-forking note found no claims in this source that
   oppose an existing corpus position. No contradiction issue filed.
5. **Weekly-digest scope per Prospector guidance**: Per the triage comment,
   this Miner pass extracted the concrete feature changes present in the
   digest itself (per triage comment 1's "Key question") rather than
   treating the digest as requiring no further extraction (per triage
   comments 2/3's "assess whether... worth extracting"). All twelve bullets
   across the three sections were read and evaluated; eleven were judged
   substantive enough for individual Claim entries, and one — the app's
   bare "sessions start and switch more efficiently" performance bullet —
   was folded into Concrete Artifacts only, per Extraction Note 3.
