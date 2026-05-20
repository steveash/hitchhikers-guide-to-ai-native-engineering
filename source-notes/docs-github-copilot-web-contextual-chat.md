---
source_url: https://github.blog/changelog/2026-05-18-ask-questions-in-context-with-copilot-on-web
source_type: docs
title: "Ask questions in context with Copilot on web"
author: GitHub (official changelog)
date_published: 2026-05-18
date_extracted: 2026-05-20
last_checked: 2026-05-20
status: current
confidence_overall: settled
issue: "#817"
---

# Ask Questions in Context with Copilot on Web

> GitHub's May 18, 2026 changelog announcing that Copilot chat on github.com now opens as
> an in-page contextual panel on the current GitHub page rather than navigating to a separate
> URL, automatically attaches the current page (PR, issue) as context, and accumulates
> references across pages as the user navigates — introducing passive context accumulation
> via navigation and a contextual-to-agent escalation path, generally available for all
> Copilot plans.

## Source Context

- **Type**: docs (GitHub official product changelog, May 18, 2026; approximately 150 words
  of primary content across three sections: "What's changed," "Automatic context addition as
  you navigate," and "Try it out")
- **Author credibility**: GitHub engineering team announcing a production GA release.
  Authoritative for the feature's existence, the UI change (panel vs. navigation), the
  automatic context attachment behavior, the cross-navigation accumulation behavior, the
  agent escalation path, and the plan-tier availability. Not a credible source for: which
  specific GitHub surfaces trigger automatic context attachment beyond PR and issue examples,
  how many references can accumulate in one session, what happens when session context becomes
  large, cost implications of attaching context vs. plain chat, or how the contextual panel
  behaves for repository pages, code views, or other GitHub surfaces beyond PRs and issues.
- **Scope**: The announcement covers: the new in-page panel UX (replacing navigate-to-URL),
  the availability of the full immersive experience via More menu, automatic context attachment
  on GitHub surfaces (PRs and issues cited as examples), cross-navigation reference accumulation,
  the contextual-to-agent escalation path (create PR / deep research), and GA availability for
  all Copilot plans. Does NOT cover: context window or token limits for accumulated references,
  how the feature interacts with Copilot Memory (user preferences), whether the panel persists
  across browser tabs or page reloads, mobile browser behavior, which GitHub surfaces other
  than PRs and issues trigger automatic context attachment, or the Deep Research feature itself.

## Extracted Claims

### Claim 1: Copilot chat on the web now opens as an in-page panel on the current GitHub page rather than navigating to github.com/copilot

- **Evidence**: Official GitHub product changelog announcing this as a GA release. The prior
  behavior (navigating away to a separate URL) is the implicit contrast; the new behavior
  (panel on the current page) is the announced change.
- **Confidence**: settled (product fact — GA stated in official changelog)
- **Quote**: "Copilot chat on the web now opens on the page you are viewing. This helps you
  get fast answers to your questions with reduced context switching."
- **Our assessment**: The UX shift from navigate-away to in-page panel is architecturally
  significant for web-based Copilot workflows. Prior web Copilot required abandoning the
  current GitHub page (PR, issue, code view) to engage in chat — a context switch that
  mirrored the cognitive cost of alt-tabbing to a different application. The panel model
  keeps the source artifact visible alongside the chat, enabling a side-by-side working
  mode that IDE Copilot has long offered but web Copilot did not. For Ch01 (Daily Workflows):
  the panel model is directly relevant to practitioners who primarily work on GitHub.com
  for code review, issue triage, or PR management. They can now ask Copilot questions
  without losing their place in the review workflow.

### Claim 2: The prior navigate-to-URL experience (github.com/copilot) is preserved as the "immersive chat" option, accessible via More menu or via an arrow icon on the contextual panel

- **Evidence**: Official changelog explicitly preserving backward compatibility by describing
  the two access paths to the immersive experience.
- **Confidence**: settled (both access paths stated in official changelog)
- **Quote**: "You can still navigate to a full-page, immersive chat experience by clicking the
  More menu next to the Copilot icon and selecting In immersive chat, or by clicking the arrow
  icon on the contextual chat panel."
- **Our assessment**: The preservation of the immersive experience matters for use cases where
  full-screen chat is preferable — extended conversations, multi-turn agent sessions, or when
  the user wants to focus entirely on the chat without the surrounding GitHub UI. The default
  is now contextual (in-page); immersive is opt-in. For practitioners: understanding which
  mode is active matters because they have different context behaviors. The contextual panel
  accumulates references from navigation (Claim 5); it is unclear whether the immersive mode
  inherits those references or starts fresh.

### Claim 3: Clicking the Copilot icon in the top navigation now opens the in-page panel — the top navigation icon is the trigger for the contextual experience

- **Evidence**: Official changelog specifying the UI entry point for the new behavior.
- **Confidence**: settled (UI entry point stated in official changelog)
- **Quote**: "When you click the Copilot icon in the top navigation, Copilot opens a panel
  instead of navigating to github.com/copilot."
- **Our assessment**: The top navigation icon is a persistent UI element present on every
  GitHub page — its behavior change affects how practitioners access Copilot from anywhere
  on GitHub, not just from a specific workflow. This is a meaningful discoverability improvement:
  previously, a user on an arbitrary GitHub page needed to navigate to the Copilot URL to
  start chat; now, the icon on every page opens chat in-context. For Ch02 (Tool Configuration):
  practitioners onboarding team members to Copilot web should update their documentation — the
  prior "navigate to github.com/copilot" instruction is now the non-default path.

### Claim 4: When chat is opened on a GitHub surface such as a pull request or issue, the current page is automatically attached as context to the chat session — no manual attachment required

- **Evidence**: Official changelog stating automatic context attachment as a feature property
  for named GitHub surfaces (pull request, issue cited as examples).
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "When you open chat on a GitHub surface, like a pull request or issue, it is
  automatically attached as context to your chat session."
- **Our assessment**: Automatic context attachment is the most operationally significant claim
  in this changelog. Unlike IDE Copilot chat (where context is the open editor file) or prior
  web Copilot chat (where context was manually attached via `@` or file picker), the contextual
  panel automatically injects the current GitHub page's artifact as context. A developer
  reviewing a PR opens chat and immediately has the PR's diff, description, and metadata
  available to Copilot — without any explicit action. This is "zero-effort context injection"
  for structured GitHub artifacts. For Ch04 (Context Engineering): this represents a new
  context sourcing model — context is determined by page location rather than by explicit
  user selection. The implicit assumption is that "what you're looking at is what you're
  asking about" — a reasonable heuristic for PR review and issue triage. Practitioners should
  understand that Copilot's answers in this mode are shaped by the page's content even if
  they don't mention it explicitly.

### Claim 5: As users navigate through GitHub, references continue to accumulate in the active chat session, enabling questions that span multiple pull requests, issues, and repositories within a single conversation

- **Evidence**: Official changelog explicitly describing the cross-navigation context accumulation
  behavior as a feature property. The list of artifact types (pull requests, issues, repositories)
  is provided as examples of what can accumulate.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "As you navigate through GitHub, references continue to attach to chat, allowing
  you to ask questions over multiple pull requests, issues, and repositories."
- **Our assessment**: Cross-navigation context accumulation is architecturally novel in the
  Copilot corpus. It introduces "context as a side effect of navigation" — browsing GitHub
  is also context-building for the chat session. A developer who visits PR #123, then navigates
  to Issue #456, then navigates to a different repository's PR #789 accumulates references to
  all three artifacts in a single chat session without explicit attachment actions. This enables
  cross-artifact queries ("based on the three PRs I've looked at, what's the common pattern?")
  that would otherwise require tedious manual context injection. For Ch04 (Context Engineering):
  this is a novel context-accumulation pattern — "navigation as context" — distinct from
  static context (CLAUDE.md, AGENTS.md), manual injection (@ mentions, file attachment), and
  persistent memory (user-level preferences in [[docs-github-copilot-memory-user-preferences]]).
  The key practitioner implication: the chat session's effective context grows invisibly as
  the user navigates. Practitioners asking questions late in a browsing session may be getting
  answers influenced by earlier page visits they have forgotten about.

### Claim 6: A contextual chat session can be escalated to a full agent session by asking Copilot to perform an agentic task such as creating a pull request or conducting deep research

- **Evidence**: Official changelog describing the escalation path as triggered by task intent
  expressed in natural language (no special command syntax described).
- **Confidence**: settled (escalation path stated in official changelog; the specific trigger
  mechanism — natural language intent — is implied rather than explicitly stated)
- **Quote**: "You can also turn your conversation into an agent session by asking Copilot to
  create a pull request or asking a deep research question."
- **Our assessment**: The escalation path from contextual chat to agent session is significant
  for practitioners who begin a web session in Q&A mode and discover mid-conversation that
  they want agentic action. The natural-language trigger (no special command) means the
  transition is implicit — the user does not need to restart in a different mode. "Create a
  PR" and "deep research question" are the two canonical triggers cited. The first maps to
  Copilot cloud agent (CCA) task creation — consistent with the CCA pattern documented in
  [[docs-github-copilot-cca-fix-failing-actions]] and [[docs-github-copilot-cca-cost-efficient-models]];
  the second maps to a deep research capability not previously documented in the corpus for
  web-based Copilot interactions. For Ch04: the contextual-to-agent escalation path means
  web Copilot now follows the same progression model as IDE Copilot — start with a question,
  escalate to action when ready. The accumulated navigation context (Claim 5) is the input
  that makes this escalation potentially more useful than starting an agent session cold.

### Claim 7: The contextual chat feature is generally available for all GitHub Copilot plans — no tier restriction applies

- **Evidence**: Official changelog stating general availability without plan qualification.
  The "all GitHub Copilot plans" phrasing is the strongest possible availability statement
  (individual, Pro, Pro+, Business, Enterprise all included).
- **Confidence**: settled (plan availability stated explicitly in official changelog)
- **Quote**: "This feature is now generally available for all GitHub Copilot plans."
- **Our assessment**: The absence of tier restriction is notable in the context of recent
  GitHub Copilot changelog entries, many of which are gated to Business/Enterprise
  (CCA features) or Pro/Pro+ (Copilot Memory user preferences per
  [[docs-github-copilot-memory-user-preferences]] Claim 5). Web contextual chat is not
  gated — all subscribers can access it immediately. This is consistent with UI interaction
  features being broadly available while compute-intensive features (CCA tasks, agent sessions)
  are tier-gated. The escalation to agent session (Claim 6) may be subject to different
  tier requirements — the changelog does not specify whether the agent session escalation
  is available to all plans or only to Business/Enterprise users who have CCA enabled.

## Concrete Artifacts

### Verbatim Text of Source Changelog (May 18, 2026)

```
Title: Ask questions in context with Copilot on web

[Header image: Contextual chat window on a GitHub repository]

Copilot chat on the web now opens on the page you are viewing. This helps you get
fast answers to your questions with reduced context switching.

What's changed

When you click the Copilot icon in the top navigation, Copilot opens a panel instead
of navigating to github.com/copilot.

You can still navigate to a full-page, immersive chat experience by clicking the More
menu next to the Copilot icon and selecting In immersive chat, or by clicking the arrow
icon on the contextual chat panel.

Automatic context addition as you navigate

When you open chat on a GitHub surface, like a pull request or issue, it is automatically
attached as context to your chat session. As you navigate through GitHub, references
continue to attach to chat, allowing you to ask questions over multiple pull requests,
issues, and repositories.

You can also turn your conversation into an agent session by asking Copilot to create a
pull request or asking a deep research question.

Try it out

This feature is now generally available for all GitHub Copilot plans.

Join the discussion within GitHub Community.
```

Source: https://github.blog/changelog/2026-05-18-ask-questions-in-context-with-copilot-on-web
Retrieved: 2026-05-20 via WebFetch (two independent fetches; content consistent)

### Feature Summary: Copilot Web Contextual Chat (May 18, 2026)

```
Feature: Copilot Web Contextual Chat (in-page panel)
Published: 2026-05-18
Availability: All GitHub Copilot plans (no tier restriction)

UX change:
  Before:  Clicking Copilot icon → navigate to github.com/copilot (separate page)
  After:   Clicking Copilot icon → in-page panel on current GitHub page
  Escape:  More menu → "In immersive chat" (or arrow icon on panel) → full-page experience

Context attachment behavior:
  On GitHub surfaces (PR, issue, etc.):
    - Current page automatically attached as context when panel opens
    - No manual attachment required
  As user navigates:
    - References accumulate in active chat session
    - Works across: pull requests, issues, repositories

Agent escalation:
  Trigger:  Natural language intent in conversation
  Examples: "create a pull request" / "deep research question"
  Result:   Contextual chat converts to an agent session

Entry points to contextual panel:
  Primary:  Copilot icon in top navigation (every GitHub page)
  
Entry points to immersive chat:
  Option A: More menu → "In immersive chat"
  Option B: Arrow icon on contextual chat panel
```

### Copilot Web Interaction Model (Comparison Before/After)

```
                         Before (prior to May 18, 2026)
─────────────────────────────────────────────────────────
Trigger:       Copilot icon in top nav
Action:        Navigate to github.com/copilot (leaves current page)
Context:       Manual attachment (@ mentions, file picker)
Mode:          Full-page immersive chat only
Cross-page:    Not supported (each visit to github.com/copilot starts fresh)
Agent access:  Available in immersive mode

                         After (from May 18, 2026, GA)
─────────────────────────────────────────────────────────
Trigger:       Copilot icon in top nav (same entry point)
Action:        Opens panel on current page (no navigation away)
Context:       Automatic attachment for PR/issue surfaces
               + accumulates as user navigates
               + manual @ injection still available
Mode:          Contextual panel (default) or immersive (opt-in via More menu)
Cross-page:    Supported — references from multiple PRs/issues/repos accumulate
Agent access:  Available via natural-language escalation ("create a PR")
```

## Cross-References

- **Corroborates**:
  - **`docs-github-copilot-cli-remote-control-ga.md`**: That source (also published May 18,
    2026) documents GitHub investing in the web interface as a control/monitoring surface for
    CLI agent sessions. This source adds the web interface as an autonomous Q&A and agentic
    interaction surface in its own right. Together, the two May 18 announcements establish the
    web surface as a first-class Copilot interaction platform: remote control uses web as a
    supervisory surface; contextual chat uses web as a direct interaction surface. Both corroborate
    that GitHub is actively building web-based Copilot interaction beyond the prior immersive chat.

- **Extends**:
  - **`docs-github-copilot-memory-user-preferences.md`**: That source documents user-level
    memory preferences (commit style, PR structure, tone) that persist across all sessions and
    repositories — a cross-session, cross-project persistence mechanism. This source adds
    a second distinct persistence dimension: within-session context accumulation via navigation.
    Together, they reveal two complementary Copilot persistence layers: (1) cross-session
    user preferences (memory); (2) within-session navigation context (this source). A practitioner
    using both simultaneously has a layered context model: long-term preferences from memory +
    short-term current-session references from recent navigation. The interaction between these
    two layers is not documented in either changelog — how Copilot ranks or composes user
    preference memory against accumulated navigation context is unknown.
  - **`docs-github-copilot-cca-fix-failing-actions.md`** (Claim 1): That source documents
    CCA invocation via a "Fix with Copilot" UI button on workflow run logs, creating a new
    event-triggered CCA path. This source documents agent session escalation from contextual
    chat as another new CCA invocation path — via natural-language intent in web chat.
    Together they extend the CCA invocation taxonomy: users can trigger CCA from failure
    events (fix button) or from conversational intent (contextual chat escalation). The two
    paths differ in trigger (event vs. intent) and starting context (failure log vs.
    accumulated navigation context), but both result in an agent session.

- **Contradicts**: None identified. No existing corpus source documents Copilot web chat
  behavior that this source changes — prior notes document CLI, IDE, or plan-tier features;
  none document the specific web chat UX that this source changes. No contradiction issue filed.

- **Novel**:
  - **In-page contextual panel as the default web Copilot UX**: No prior corpus source
    documents the contextual panel as a Copilot web interaction mode. Prior references to
    web-based Copilot interaction describe the immersive chat at github.com/copilot or
    discuss web as a remote control surface for CLI sessions, not as an in-page chat surface.
  - **Automatic context attachment for GitHub artifact pages**: No prior corpus source
    documents automatic context injection based on page location. Prior context engineering
    notes cover explicit mechanisms (CLAUDE.md, AGENTS.md, @ injection, file attachment);
    this is the first "implicit context from current page" pattern in the corpus.
  - **Cross-navigation reference accumulation within a chat session**: No prior corpus source
    documents a Copilot feature where browsing GitHub builds context in an active chat session
    without explicit user action. This "navigation as context accumulation" pattern is new to
    the corpus — distinct from both static configuration and active injection models.
  - **Natural-language agent escalation from conversational chat**: No prior corpus source
    documents a mechanism for transitioning from Q&A chat to agent mode via natural language
    intent (without a UI mode switch or API call). The implicit escalation path (say "create
    a PR" → Copilot switches to agent mode) is a new interaction model in the corpus.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add a "Copilot web contextual chat" daily workflow
  pattern for practitioners whose primary GitHub workflow is browser-based code review and
  issue management. The pattern: open a PR → panel opens automatically with PR as context
  → ask review questions → navigate to related issue → context accumulates → ask cross-artifact
  questions → if action is needed, say "create a PR [with fix]" to escalate to agent mode.
  This workflow complements the IDE-based Copilot workflow for practitioners doing review
  work in the browser. Note that automatic context attachment eliminates the manual step that
  was previously required to give Copilot awareness of the current PR or issue.

- **Chapter 04 (Context Engineering)**: Add a new context pattern — "implicit context from
  navigation" — to the context engineering taxonomy alongside static configuration (CLAUDE.md,
  AGENTS.md), active injection (@ mentions, file attachment), and persistent memory (user
  preferences). Document the cross-navigation accumulation behavior as a practitioner-visible
  effect: the chat session's effective context grows silently as the user browses. Practitioners
  debugging unexpected Copilot answers in web chat should consider whether earlier page visits
  have accumulated references influencing the response. Recommend practitioners who want a
  clean context to open a new chat session rather than continuing an accumulated one.

- **Chapter 02 (Copilot as Interface / Harness Engineering)**: Update any documentation that
  instructs users to navigate to github.com/copilot for web-based Copilot chat — this is now
  the non-default (immersive) mode. The default is the contextual panel accessible via the
  top navigation icon on any GitHub page. For teams onboarding practitioners to Copilot web,
  the instruction is now "click the icon in the top nav while on the page you want to discuss"
  rather than "go to github.com/copilot and attach a file." Document the agent escalation
  path as an entry point to CCA for practitioners working in the browser who do not want to
  use the issue-assignment or workflow-failure UI paths.

- **Chapter 05 (Team Adoption)**: Note that the contextual chat feature is universally
  available (all plans, no admin gate required), making it the lowest-friction Copilot
  web capability for teams adopting Copilot. Unlike CCA features (which require admin
  enablement) or Copilot Memory (which requires opt-in), the contextual panel is active by
  default for all Copilot subscribers who visit github.com. Teams should include the
  contextual panel behavior in their Copilot onboarding documentation, particularly for
  practitioners who primarily work in the browser rather than in an IDE.

## Extraction Notes

1. **Brief source (~150 words)**: The changelog entry is among the shorter entries in the
   corpus. All substantive claims are exhausted in the seven claims above. The source
   contains no linked sub-pages beyond the GitHub Community discussion link and changelog
   navigation; no sub-pages were followed, as the discussion forum was not yet populated
   at the time of extraction and would not contain authoritative product information.

2. **Verbatim quotes verified across two fetches**: Two separate WebFetch calls to the
   same URL returned consistent content. The complete verbatim text is reproduced in the
   Concrete Artifacts section. All quotes used in claims are drawn directly from that
   verbatim text.

3. **"Deep research" capability underspecified**: The changelog mentions "asking a deep
   research question" as an agent escalation trigger but provides no further detail on
   what "deep research" entails, which model is used, what its cost implications are, or
   whether it is the same capability as other "deep research" features in GitHub Copilot.
   This is a meaningful gap — practitioners who trigger agent escalation expecting Q&A
   may encounter a significantly more expensive agentic task. The guide should flag this
   uncertainty.

4. **Agent escalation plan-tier scope unclear**: Claim 6 notes the contextual panel itself
   is available to all plans (Claim 7), but the agent session escalation may invoke CCA,
   which is Business/Enterprise-only per existing corpus notes. The changelog does not
   clarify whether the "create a pull request" escalation path is available to individual
   plan users or only to Business/Enterprise users with CCA enabled. This gap should be
   flagged in any guide content describing the escalation path.

5. **Context window limits for accumulated references not documented**: The changelog
   does not specify how many references can accumulate in a session before they are
   truncated or how GitHub manages the context window when many artifacts have been
   attached via navigation. This is practically important for practitioners conducting
   extended review sessions spanning many artifacts.

6. **No contradictions filed**: Examined all Copilot-prefixed source notes in the corpus
   for potential conflicts. No existing note documents web Copilot chat behavior that
   contradicts this announcement. The closest adjacent notes (remote control GA, memory
   user preferences) extend rather than contradict.
