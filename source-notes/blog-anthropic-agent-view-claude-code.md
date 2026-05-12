---
source_url: https://claude.com/blog/agent-view-in-claude-code
source_type: blog-post
title: "Agent view in Claude Code"
author: Anthropic
date_published: 2026-05-11
date_extracted: 2026-05-12
last_checked: 2026-05-12
status: current
confidence_overall: emerging
issue: "#693"
---

# Agent view in Claude Code

> Official Anthropic product announcement for "agent view" — a centralized CLI
> management interface for parallel Claude Code sessions, introducing peek-and-reply,
> background session commands, and four documented practitioner patterns — directly
> addressing the cognitive ceiling and terminal UX failure modes that practitioners
> reported when managing multi-session workflows without dedicated tooling.

## Source Context

- **Type**: blog-post (official claude.com blog, May 11, 2026; product announcement for
  a Research Preview feature)
- **Author credibility**: First-party Anthropic announcement. Maximum authority for
  what the feature does, how it is navigated, and which practitioner patterns Anthropic
  observed from early users. Research Preview status means the feature is available but
  behavior, commands, and availability details may change. No independent practitioner
  accounts accompany this announcement.
- **Scope**: Covers the agent view UI mechanics (how to open, row structure, peek-and-reply,
  background sessions), four early-user patterns, and plan availability. Does NOT cover:
  how agent view interacts with auto mode's escalation flow, what happens when a background
  session encounters a blocking permission, performance or latency characteristics of the
  agent view UI, or how agent view integrates with routines (scheduled/API/webhook sessions).
  The post is a short feature announcement (~400 words), not a technical deep-dive.

## Extracted Claims

### Claim 1: Agent view provides a single terminal interface to manage all Claude Code sessions, replacing ad-hoc tmux grids and mental ledgers

- **Evidence**: Explicit vendor framing in the post's opening. The problem statement
  names the prior state: "you've probably had to manage multiple terminal tabs, a tmux
  grid, and an overloaded mental ledger of what you need to tackle next."
- **Confidence**: emerging (vendor claim; the problem description accurately names
  the infrastructure practitioners actually use, raising credibility above generic marketing)
- **Quote**: "When running agents in parallel before, you've probably had to manage
  multiple terminal tabs, a tmux grid, and an overloaded mental ledger of what you need
  to tackle next."
- **Our assessment**: The problem is real. `failure-sukit-parallel-session-ceiling.md`
  documents exactly this: terminal UX degradation under multi-session load and a cognitive
  ceiling of ~2 interactive parallel sessions before context-switching collapse. Agent view
  is Anthropic's first-party UI response to these failure modes. Whether it fully resolves
  the cognitive ceiling is not tested in this announcement, but the problem diagnosis is
  accurate.

### Claim 2: Agent view is opened via left-arrow keypress from any active session, or by running `claude agents` from the terminal

- **Evidence**: Explicit navigation instruction in the "How it works" section.
- **Confidence**: settled (first-party feature description of a shipping interaction model)
- **Quote**: "Press the left arrow from any session or run `claude agents` from the
  terminal to open agent view."
- **Our assessment**: Two entry points (keyboard shortcut from within a session, CLI
  command from outside) cover the two primary practitioner contexts: mid-session navigation
  and fresh terminal launch. The left-arrow convention builds on existing Claude Code
  navigation idioms.

### Claim 3: Each row in agent view displays the session name, whether it needs user input, the last response contents, and the time since last interaction

- **Evidence**: Explicit feature description in the "See everything at once" section.
- **Confidence**: settled (first-party feature description; specific row fields named)
- **Quote**: "Each row shows the session, whether it needs your input, the contents of
  its last response, and when you last interacted with it."
- **Our assessment**: The four fields cover the essential triage information for parallel
  session management: identity (which session), urgency (needs input?), progress (last
  response content), and staleness (time since last interaction). This is a minimal but
  sufficient information model for deciding which session to attend to next. The
  "needs your input" indicator is the most operationally important — it is the signal
  that a session has hit a decision point and is blocked.

### Claim 4: The "peek and reply" interaction model enables responding to blocked sessions without fully attaching to them

- **Evidence**: Explicit feature description in the "Peek and reply without leaving"
  section. Two distinct interaction modes described: peek (see last turn, answer inline)
  and attach (press enter to open full transcript).
- **Confidence**: settled (first-party feature description of a shipping interaction model)
- **Quote**: "Select a session to peek at the last turn. If a session is waiting on a
  decision, answer inline and the session picks back up."
- **Our assessment**: Peek-and-reply is the key interaction innovation in this feature.
  Without it, handling a blocked session requires switching to that session's terminal,
  reading context, answering, then switching back — re-incurring the context-switch cost
  that makes parallel sessions cognitively expensive. The inline answer model keeps the
  practitioner in the management view rather than re-immersing in each session's context.
  This directly addresses the cognitive ceiling documented in `failure-sukit-parallel-session-ceiling.md`
  (Lesson 2: "Once I go beyond that, my brain starts falling apart within minutes").

### Claim 5: Existing sessions can be sent to background via `/bg` slash command; new sessions can be launched directly in the background via `claude --bg [task]`

- **Evidence**: Explicit command documentation in the "Background anything" section.
- **Confidence**: settled (first-party feature description with specific command syntax)
- **Quote**: "users can take any existing session and add it to agent view using `/bg`
  or skip the foreground entirely using `claude --bg [task]` to launch a fresh session."
- **Our assessment**: Two background primitives cover the two session lifecycle points:
  `/bg` retrofits an existing foreground session into agent view; `--bg` launches directly
  into the background. The `--bg` flag is particularly significant: it enables the
  "dispatch and forget" pattern (start many sessions, return to agent view) without
  requiring a foreground interaction step. This is the core primitive for the "Scaling
  the number of concurrent sessions" pattern documented in Claim 6.

### Claim 6: Early users are dispatching multiple tasks simultaneously paired with skills, then returning to a list of PRs ready for review

- **Evidence**: Anthropic-reported early user pattern from "How developers are using
  agent view." Anthropic is reporting observed behavior, not hypothetical scenarios.
- **Confidence**: emerging (vendor-reported early user behavior; not independently
  corroborated by practitioner accounts yet given Research Preview timing)
- **Quote**: "Dispatch several ideas at once, each optionally paired with a skill, and
  return to a list of pull requests ready for review."
- **Our assessment**: This is the orchestrator-subagent pattern at the CLI level:
  dispatch → background → collect results. The "paired with a skill" detail is
  significant — it indicates that Skills (practitioner-authored instruction files) are
  the mechanism for specializing each dispatched agent, not just raw prompts. This maps
  directly to the orchestrator-subagent pattern from `blog-anthropic-multi-agent-coordination-patterns.md`
  (Claim 7: recommended default for its wide problem coverage and low coordination overhead).
  The "list of PRs ready for review" is the concrete output artifact that makes the
  pattern's value immediately visible.

### Claim 7: Long-running looping jobs (PR babysitters, dashboard updaters) surface their next run time directly in agent view

- **Evidence**: Anthropic-reported early user pattern: "PR babysitters, dashboard updaters,
  and other looping jobs show their next run time right in the list."
- **Confidence**: emerging (vendor-reported early user behavior; specific run-time display
  detail is noteworthy)
- **Quote**: "PR babysitters, dashboard updaters, and other looping jobs show their next
  run time right in the list."
- **Our assessment**: This establishes agent view as the monitoring surface for the
  Routines-style background automation patterns documented in
  `blog-anthropic-claude-code-routines.md`. The "next run time" display implies agent view
  has awareness of scheduled/looping sessions, not just one-shot sessions. This makes
  agent view the unified observability layer across both interactive and automated sessions.

### Claim 8: The left-arrow/right-arrow navigation pattern enables mid-session task context-switching and return without losing the original session's state

- **Evidence**: Anthropic-reported early user pattern: "When you're in the middle of a
  session, press the left arrow, start a related task or quick codebase question, then
  arrow right back into what you were doing."
- **Confidence**: emerging (vendor-reported pattern; the specific key-navigation idiom is
  consistent with the previously described left-arrow entry point)
- **Quote**: "When you're in the middle of a session, press the left arrow, start a
  related task or quick codebase question, then arrow right back into what you were doing.
  Peek shows the answer when it lands."
- **Our assessment**: This is the "interrupt-and-resume" workflow — temporarily spawning
  a side task without losing the main session's context. Previously this required a new
  terminal (and its associated UX overhead). The agent view navigation idiom makes
  the pattern ergonomically accessible. The "Peek shows the answer when it lands" detail
  is key: the practitioner does not need to actively wait for the side task to complete —
  peek provides the result asynchronously when they next visit agent view.

### Claim 9: Status indicators in agent view make it easy to scan which sessions produced a PR, enabling post-hoc result review

- **Evidence**: Anthropic-reported early user pattern: "Status indicators on each row
  plus the title in peek make it easy to scan which sessions produced a PR."
- **Confidence**: emerging (vendor-reported pattern)
- **Quote**: "Status indicators on each row plus the title in peek make it easy to scan
  which sessions produced a PR."
- **Our assessment**: The "see what shipped" pattern is the post-dispatch triage step
  in the parallel session workflow. When many sessions run in background, the practitioner
  needs to quickly identify which completed successfully (PR opened), which need attention
  (blocked on decision), and which failed. Status indicators at the row level support this
  triage. This complements `blog-anthropic-multi-agent-coordination-patterns.md`'s point
  about orchestrator-subagent requiring a synthesis step — agent view makes that synthesis
  step a visual scan rather than a terminal-by-terminal review.

### Claim 10: Agent view is in Research Preview as of May 11, 2026, available on Pro, Max, Team, Enterprise, and Claude API plans via opt-in

- **Evidence**: Explicit availability statement in the "Getting started" section.
- **Confidence**: settled (first-party plan availability statement; research preview is a
  formal Anthropic designation)
- **Quote**: "Agent view is available today as a Research Preview on Pro, Max, Team,
  Enterprise, and Claude API plans. Opt-in by running `claude agents`. Usual rate limits
  apply."
- **Our assessment**: Research Preview means the feature is accessible but not API-stable.
  The "Usual rate limits apply" note signals that background sessions consume the same
  resource pool as interactive sessions — parallel session scaling is bounded by plan
  rate limits, not just practitioner cognitive capacity. Teams planning to rely on agent
  view for multi-session workflows should factor rate limits into their scaling plans.
  Notably, no additional tier or add-on is required — unlike Routines, agent view is
  included in existing plan tiers.

## Concrete Artifacts

### Agent View Feature Summary

```
Agent View in Claude Code (Anthropic, May 11 2026)
Research Preview — available on Pro, Max, Team, Enterprise, Claude API

ENTRY POINTS:
  From any active session: press ← (left arrow)
  From terminal:           claude agents

SESSION ROW FIELDS:
  - Session identity
  - Input-needed indicator (blocked vs. running)
  - Last response contents
  - Time since last interaction

INTERACTION MODES:
  Peek:    Select a session to view its last turn
  Reply:   Answer inline if session is waiting on a decision (session resumes immediately)
  Attach:  Press Enter to open the full transcript

BACKGROUND COMMANDS:
  /bg                   — Send existing foreground session to background (adds to agent view)
  claude --bg [task]    — Launch new session directly in background (never takes foreground)
```

### Four Documented Early User Patterns

```
Agent View: Early User Patterns
(Anthropic, "Agent view in Claude Code," May 11 2026)

1. PARALLEL TASK DISPATCH
   Workflow: Dispatch several tasks at once, each optionally paired with a Skill,
             return to agent view to find a list of PRs ready for review.
   Value:    Orchestrator-subagent pattern at the CLI level.
   Key:      Skills specialize each dispatched agent; `--bg` skips foreground entirely.

2. LONG-RUNNING JOB MONITORING
   Workflow: PR babysitters, dashboard updaters, looping jobs show their next run
             time in agent view.
   Value:    Single observability surface for both interactive and scheduled sessions.
   Key:      "Next run time" implies agent view is schedule-aware.

3. SESSION INTERRUPT-AND-RESUME
   Workflow: Mid-session, ← arrow, start a quick side task or codebase question,
             → arrow back; Peek shows the answer when it lands.
   Value:    Asynchronous side-task pattern without terminal context-switch cost.
   Key:      Enables non-blocking parallel exploration without losing main session.

4. POST-DISPATCH RESULT TRIAGE ("SEE WHAT SHIPPED")
   Workflow: Status indicators on each row + peek title → scan to identify which
             sessions produced a PR.
   Value:    Visual triage of parallel session results without per-session attachment.
   Key:      Turns parallel session completion into a reviewable dashboard.
```

## Cross-References

- **Corroborates** `failure-sukit-parallel-session-ceiling.md`: That note documents
  the exact failure modes that agent view is designed to address. Sukit reported (1)
  terminal UX degradation making multi-session management painful, (2) a cognitive
  ceiling of ~2 interactive parallel sessions before context-switching collapse, and
  (3) a "demo gap" where tool-author multi-session demos were not replicable by average
  practitioners. Agent view directly targets all three: it consolidates sessions into
  a single interface (terminal UX), peek-and-reply reduces full context-switch to an
  inline answer (cognitive ceiling), and it packages the parallel-dispatch workflow as
  a first-class CLI feature (demo gap). This is the strongest corroborating relationship
  in the cross-reference set — the failure was documented first, the fix arrives second.

- **Extends** `blog-anthropic-claude-code-routines.md`: Routines handle the scheduling
  and triggering layer (when sessions start, how they're triggered). Agent view handles
  the monitoring and interaction layer (how running sessions are managed). They are
  complementary: the "Manage long running agents" pattern (Claim 7 in this note) shows
  agent view surfaces "next run time" for looping jobs — implying direct awareness of
  routines-style scheduled sessions. Together, routines + agent view is the complete
  background automation stack: routines start the sessions, agent view monitors and
  unblocks them. The routines note (Claim 5 there) identified that persistent webhook
  sessions per PR "could consume a significant share of the daily quota" — agent view
  provides the visibility layer to track and manage that quota consumption in practice.

- **Corroborates** `blog-anthropic-claude-code-auto-mode.md`: Auto mode's deny-and-continue
  pattern (Claim 7 there) results in blocked sessions when the classifier denies an action
  and the agent cannot find a safe alternative. In interactive mode, those escalations
  reach the practitioner for resolution. Agent view's "needs your input" indicator and
  peek-and-reply mechanism are the UX layer for handling these escalations without
  re-attaching to the full session. The two features compose: auto mode handles the
  automated permission gating, agent view handles the escalation UI when auto mode needs
  human input. Auto mode's escalation threshold (3 consecutive denials → human review in
  interactive mode) becomes operationally manageable when the practitioner can respond
  from agent view without losing their place in the management flow.

- **Corroborates** `blog-anthropic-multi-agent-coordination-patterns.md`: The "Scaling
  concurrent sessions" pattern (Claim 6 in this note) is the practitioner-facing
  implementation of the orchestrator-subagent pattern (Claim 7 in that note: "recommended
  default for widest range of problems with least coordination overhead"). Agent view
  makes the orchestrator role ergonomically viable at the CLI: the practitioner acts as
  orchestrator, dispatches sessions as subagents (via `claude --bg`), and monitors/unblocks
  them via peek-and-reply. Previously the orchestrator role required tmux discipline and
  context-switching overhead that raised the cognitive cost above casual use. Agent view
  reduces that cost.

- **Corroborates** `blog-addyosmani-code-agent-orchestra.md`: Osmani (Claim 8 there)
  recommended 3-5 concurrent agents as the WIP limit and described management skills
  (task scoping, delegation, async check-ins, verification loops) as the new leverage
  point. Agent view is the first-party tooling that operationalizes those management
  patterns: async check-ins become peek interactions, delegation becomes `--bg` dispatch,
  verification becomes post-dispatch triage (the "see what shipped" pattern). Osmani
  predicted that management tooling would be the limiting factor; agent view is
  Anthropic's answer to that prediction.

- **Novel**:
  - **Peek-and-reply as a named interaction primitive**: The specific UX model — view
    last turn in a session, answer inline without full attachment, session resumes
    automatically — is new to the corpus. No prior source documents this interaction
    pattern for Claude Code parallel sessions.
  - **`/bg` and `claude --bg` as background session commands**: The specific command
    syntax for backgrounding existing sessions and launching new sessions directly to
    background is first documented here.
  - **"Needs your input" indicator as session status type**: The explicit blocked/running
    distinction surfaced in agent view row data is new to the corpus. Prior sources
    describe parallel sessions as undifferentiated workers; this introduces a blocking
    status model.
  - **Left-arrow/right-arrow as session navigation idiom**: The keyboard navigation model
    for moving between agent view and individual sessions is new to the corpus.
  - **Agent view as a unified observability surface for scheduled and interactive sessions**:
    The claim that looping jobs surface "next run time" in agent view means it spans both
    session types. No prior corpus source describes a unified monitoring layer across
    interactive and scheduled Claude Code sessions.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add a "Parallel session management with agent view"
  section documenting the four early-user patterns (parallel dispatch, long-running
  monitoring, interrupt-and-resume, post-dispatch triage). This is the first-party answer
  to the parallel session scaling challenge documented in `failure-sukit-parallel-session-ceiling.md`.
  The guide currently recommends git worktrees as the infrastructure for parallel sessions;
  agent view is the complementary UX layer. Recommend presenting both: worktrees for
  isolation, agent view for management. Cite the cognitive ceiling evidence from sukit
  and contrast with the agent view peek-and-reply mechanism as the mitigation.

- **Chapter 01 (Daily Workflows)**: Update the "demo gap" discussion to note that
  agent view makes the parallel-dispatch workflow (previously accessible only to
  practitioners with deep tmux + workflow discipline) a first-class CLI feature. The
  gap between tool-author demos and practitioner workflows is narrower now. Set the
  expectation: agent view reduces the UX friction; task atomicity and skills design
  still require practitioner investment.

- **Chapter 02 (Harness Engineering)**: Add agent view to the "unattended execution"
  section alongside auto mode and routines. The three-layer background automation stack
  is: (1) routines schedule/trigger sessions, (2) auto mode handles permission gating,
  (3) agent view monitors and unblocks escalations. All three are Research Preview as
  of May 2026. The "needs your input" indicator is the signal that auto mode has escalated
  and human input is required — practitioners should factor this into their unattended
  execution design.

- **Chapter 03 (Multi-Agent Patterns)**: Add agent view as the CLI-level UX layer for
  the orchestrator-subagent pattern. The four patterns in this note (dispatch, monitor,
  interrupt-resume, triage) are the practitioner workflow for the orchestrator role.
  Currently the multi-agent coordination patterns chapter describes what the patterns
  are; agent view is how a practitioner manages them interactively. Connect the
  orchestrator-subagent recommendation from `blog-anthropic-multi-agent-coordination-patterns.md`
  to the agent view UX with: "When acting as orchestrator, use `claude --bg [task]` to
  dispatch subagents and agent view to monitor and unblock them."

## Extraction Notes

- The source article is a short product announcement (~400 words) — the source is thin
  by design; it is a feature introduction, not a technical engineering post. The claims
  are mostly feature descriptions with limited engineering depth. Confidence is set to
  `emerging` rather than `settled` because Research Preview status means behavior and
  commands may change, and no independent practitioner corroboration exists yet given
  the May 11, 2026 publication date (same day as this extraction).
- The article does not describe: how agent view interacts with auto mode escalations,
  whether session history is persistent across CLI restarts, rate limit behavior for
  background sessions, or the technical implementation of "next run time" display for
  looping jobs.
- No verbatim quotes were unavailable — all quotes above appear character-for-character
  in the source article as fetched.
- The Prospector's three triage comments identified slightly different relevance angles
  (Ch01 dev workflow, Ch02 harness engineering, Ch03 multi-agent UI/UX). All three are
  represented in the Guide Impact section. The second and third triage comments identify
  novelty as high; this extraction confirms that assessment: the peek-and-reply primitive,
  background session commands, and unified observability surface are all new to the corpus.
- No contradiction with existing corpus notes was identified that would require a
  separate contradiction issue. The cognitive ceiling evidence from `failure-sukit-parallel-session-ceiling.md`
  is addressed by (not contradicted by) agent view — the failure was real; agent view
  is Anthropic's fix.
