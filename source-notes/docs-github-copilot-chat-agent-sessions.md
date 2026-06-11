---
source_url: https://github.blog/changelog/2026-06-10-copilot-chat-now-sees-your-agent-sessions
source_type: docs
title: "Copilot Chat now sees your agent sessions"
author: GitHub (official changelog)
date_published: 2026-06-10
date_extracted: 2026-06-11
last_checked: 2026-06-11
status: current
confidence_overall: settled
issue: "#1145"
---

# Copilot Chat now sees your agent sessions

> GitHub's June 10, 2026 changelog adds Copilot Chat as a session management
> surface for cloud agent work: two new tools — "Get agent logs" and "Session
> search" — let users retrieve logs from a cloud agent's PR work and find past
> sessions by topic, title, or recency, completing the expansion of agent session
> visibility from the global dashboard and IDE views to the chat interface itself.

## Source Context

- **Type**: docs (GitHub official product changelog, June 10, 2026; a short
  changelog entry of approximately 150 words with two named tool additions and
  a description of the real-time status integration)
- **Author credibility**: GitHub engineering team announcing a production feature
  addition to Copilot Chat. Authoritative for: the existence and names of the two
  new tools, their stated capabilities, and the live session status behavior in
  chat when a session is started via chat. Not a credible source for: which plan
  tiers can access these tools (not specified), whether the "Get agent logs" tool
  covers CLI agent sessions or only Copilot cloud agent (CCA) sessions, token or
  rate-limit costs of session log retrieval, or what "session search" returns for
  sessions with very long histories.
- **Scope**: The announcement covers two new Copilot Chat tools (Get agent logs,
  Session search) and the in-chat live status integration for sessions initiated
  via chat. Does NOT cover: plan-tier availability for the new tools, whether
  the tools apply to all agent session types (CLI vs. CCA vs. custom), how the
  session log content is presented in chat, API access to these tools, how session
  search is scoped (personal sessions only, or team sessions), or whether the chat
  history retains retrieved logs after the conversation ends.

## Extracted Claims

### Claim 1: Copilot Chat is now a surface for querying and searching past cloud agent sessions, not just for initiating new sessions

- **Evidence**: Official GitHub product changelog announcing the feature as active.
  The headline states the capability directly: chat "now sees" agent sessions,
  implying a capability that did not exist before.
- **Confidence**: settled (product fact — feature announced in official changelog)
- **Quote**: (no direct quote captures this framing exactly; see paraphrase in
  Our assessment)
- **Our assessment**: This completes a surface expansion pattern that has been
  building since April 2026. The April changelog added issues and project boards
  as session visibility surfaces (`docs-github-copilot-issues-projects-sessions.md`,
  Claim 1). The May JetBrains changelog added a unified sessions view in the IDE
  chat window (`docs-github-copilot-jetbrains-cli-agent-sessions.md`, Claim 5).
  This June changelog adds the Copilot Chat interface (web and IDE) as a session
  visibility and log-retrieval surface. The progression is deliberate: GitHub is
  embedding agent session awareness into every surface practitioners already use,
  rather than requiring them to navigate to a dedicated session dashboard. For
  Ch02 (Harness Engineering): update the multi-surface session management
  inventory to include chat as the newest surface alongside the global dashboard,
  issues, projects, IDE sessions view, and remote control.

### Claim 2: A new "Get agent logs" tool lets users pull session logs from a Copilot cloud agent's work on a pull request directly into the chat conversation

- **Evidence**: Official changelog describing the tool's function. The tool name
  and its PR-scoped log retrieval capability are stated explicitly.
- **Confidence**: settled (feature described in official changelog)
- **Quote**: "Pull in session logs from a Copilot cloud agent's work on a pull
  request"
- **Our assessment**: This is the first documented tool in Copilot Chat that gives
  post-hoc access to cloud agent session logs. The PR scope is important: the logs
  are tied to a specific pull request, which means the retrieval is structured
  around the artifact the agent worked on, not just a time range or session ID.
  This aligns with how sessions are already surfaced in issues (the session pill
  shows sessions associated with a specific issue — `docs-github-copilot-issues-projects-sessions.md`,
  Claim 2). Practitioners can now ask natural-language questions about what the
  agent did to a PR ("why did the agent make this change?", "what validation steps
  did it take?") without leaving chat. For Ch04 (Agentic Workflows): document this
  as a post-session forensics primitive — useful both for understanding agent
  reasoning and for debugging unexpected outputs. The PR-scoped retrieval means
  practitioners reviewing a PR can ask for agent logs in the same chat session
  where they are also using the PR richer context feature
  (`docs-github-copilot-chat-pr-richer-context.md`).

### Claim 3: A new "Session search" tool finds and summarizes past agent sessions by topic, title, or recency

- **Evidence**: Official changelog describing the tool's function and its three
  search dimensions (topic, title, recency).
- **Confidence**: settled (feature described in official changelog; three search
  dimensions named explicitly)
- **Quote**: "Find and summarize past agent sessions by topic, title, or recency"
- **Our assessment**: Session search is a continuity primitive: practitioners who
  have run many agent sessions across days or weeks can locate prior work without
  remembering exact session names. The three search dimensions cover different
  recall strategies: "topic" covers semantic intent search (what the session was
  about), "title" covers exact-name retrieval (if the practitioner assigned a
  descriptive title), "recency" covers temporal lookup (what ran recently). The
  "summarize" capability implies the tool returns not just a session identifier but
  a natural-language summary of what the session did — this reduces the need to
  open and read raw logs. For Ch04: document this as the chat-based counterpart to
  the unified sessions view in JetBrains (`docs-github-copilot-jetbrains-cli-agent-sessions.md`,
  Claims 5–6), which displays sessions visually. Session search is the NL query
  layer on top of the same session data, enabling recall rather than browsing.

### Claim 4: When a user initiates an agent session through chat, live session status updates appear in the chat conversation as the session runs

- **Evidence**: Official changelog describing the in-chat status integration
  as part of the same feature release.
- **Confidence**: settled (behavior described in official changelog)
- **Quote**: (no direct quote available; the behavior was described in
  paraphrased form across multiple fetches with consistent meaning; see Our
  assessment)
- **Our assessment**: Prior to this change, starting an agent session via chat
  would send the user to the session's output view (a separate surface) or leave
  the chat without visible progress. The live status integration closes this loop:
  the chat conversation that started the agent session is also the monitoring
  surface for it while it runs. This is the chat-native version of what the
  JetBrains unified sessions view provides for IDE sessions
  (`docs-github-copilot-jetbrains-cli-agent-sessions.md`, Claims 5–6): live
  status, elapsed time, and state visible without navigating away. For Ch04: this
  is a practitioner-facing pattern — "the conversation that spawns the session
  also monitors it" — that reduces context switching for users who prefer chat as
  their primary Copilot interface over the IDE sessions view or the global dashboard.

### Claim 5: After a session completes, users can ask follow-up questions about the session results directly within the same chat conversation

- **Evidence**: Official changelog stating this follow-up capability as part of
  the same feature release.
- **Confidence**: settled (capability described in official changelog)
- **Quote**: (no direct quote available; see Our assessment)
- **Our assessment**: The post-completion follow-up capability makes the chat
  conversation a closed loop: initiate → monitor (Claim 4) → follow-up in the same
  thread. This contrasts with prior workflows where the post-session analysis
  required navigating to the issue page (for session pill interaction:
  `docs-github-copilot-issues-projects-sessions.md`, Claim 3) or to the
  `github.com/copilot/agents` dashboard. The follow-up capability is
  complementary to the web contextual chat agent escalation path
  (`docs-github-copilot-web-contextual-chat.md`, Claim 6): that source documented
  chat → agent escalation; this source adds agent completion → chat follow-up,
  creating a full cycle in the chat interface. For Ch01 (Daily Workflows): document
  this as the "chat-first agent workflow" pattern: start the request in chat, see
  status in chat, ask follow-up in chat — all without switching surfaces.

## Concrete Artifacts

### New Copilot Chat Tools — June 10, 2026

```
Copilot Chat: New Agent Session Tools (June 10, 2026)

Get agent logs
  Function: Pull in session logs from a Copilot cloud agent's work on a pull request
  Scope:    PR-associated cloud agent sessions
  Use case: Forensic review — ask questions about agent reasoning and changes
            within the chat conversation

Session search
  Function: Find and summarize past agent sessions by topic, title, or recency
  Scope:    Past sessions (personal scope unclear; team scope not documented)
  Use case: Session continuity — locate prior agent work without exact session names
  Search dimensions:
    - Topic     (semantic / intent-based search)
    - Title     (exact or partial session name match)
    - Recency   (most recent sessions first)
```

*Source: "Copilot Chat now sees your agent sessions," GitHub Changelog, June 10, 2026*

### Copilot Chat — Agent Session Integration: Before/After

```
Agent Session Visibility in Copilot Chat

BEFORE (prior to June 10, 2026):
  - Chat could initiate agent sessions (via contextual chat agent escalation)
  - No in-chat status while session ran
  - No in-chat follow-up after session completed
  - Log review required: navigate to github.com/copilot/agents or issue page

AFTER (from June 10, 2026):
  - Chat can initiate AND monitor agent sessions (live status in-conversation)
  - After completion: follow-up questions in same chat thread
  - Get agent logs tool: pull PR-session logs into chat for NL query
  - Session search tool: find past sessions by topic/title/recency from chat
```

*Synthesized from "Copilot Chat now sees your agent sessions," GitHub Changelog, June 10, 2026*

### Agent Session Management Surfaces — GitHub (as of June 2026)

```
Surface                          Access Path                  Source
────────────────────────────────────────────────────────────────────────────────────
github.com/copilot/agents        Direct URL navigation        docs-github-copilot-cli-remote-control-ga.md
GitHub mobile                    Mobile app                   docs-github-copilot-cli-remote-control-ga.md
Issue header (session pill)      Issues page                  docs-github-copilot-issues-projects-sessions.md
Projects board                   Projects page                docs-github-copilot-issues-projects-sessions.md
JetBrains unified sessions view  IDE chat window              docs-github-copilot-jetbrains-cli-agent-sessions.md
Copilot Chat (new, June 2026)    Chat conversation            this source
  - Live status while running
  - Follow-up after completion
  - Get agent logs (PR-scoped)
  - Session search (by topic/title/recency)
```

*Synthesized from this source and cross-referenced corpus notes*

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-issues-projects-sessions.md` (Claim 1): That source
    established GitHub issues and project boards as agent session visibility
    surfaces (April 2026). This source adds Copilot Chat as the next surface
    in the same expansion pattern. Both reflect GitHub's consistent strategy:
    embed agent session awareness into every surface practitioners already use.
  - `docs-github-copilot-jetbrains-cli-agent-sessions.md` (Claims 5–6): The
    JetBrains unified sessions view (May 2026) introduced an IDE-level
    observability primitive for concurrent sessions. The "Session search" tool
    in this source provides a complementary NL-query layer over the same session
    data — browsing (JetBrains view) vs. querying (chat session search) over the
    same session corpus.

- **Extends**:
  - `docs-github-copilot-web-contextual-chat.md` (Claim 6): That source documented
    the chat → agent escalation path (ask Copilot to create a PR or conduct deep
    research → agent session starts). This source adds the return path: agent
    session running → live status in chat, agent session complete → follow-up in
    chat. Together the two sources define a full cycle in the chat interface:
    initiation, monitoring, and post-session analysis without leaving chat.
  - `docs-github-copilot-issues-projects-sessions.md` (Claim 3): That source
    documented that clicking a session in the issue sidebar allows log review
    within the GitHub web UI. The "Get agent logs" tool in this source extends
    the same log-review capability to the chat interface, with the additional
    affordance of natural-language querying over the logs rather than raw log
    inspection.
  - `docs-github-copilot-chat-pr-richer-context.md`: That source (June 4, 2026)
    documented Copilot Chat in pull requests going GA, with PR diff context and
    inline edit from chat. This source extends the PR chat integration to include
    agent session log retrieval — users reviewing a PR in Copilot Chat can now
    also query what the cloud agent did to that PR.

- **Contradicts**: None identified. All session management surfaces documented
  across the corpus are additive — each source adds a new surface without
  claiming exclusivity. No contradiction issue filed.

- **Novel**:
  - **"Get agent logs" as a chat-native PR log retrieval tool**: No prior corpus
    source documents a tool within Copilot Chat that pulls cloud agent session
    logs for natural-language querying. The PR-scoped log retrieval primitive is
    new to the corpus.
  - **"Session search" as a NL query interface over past sessions**: No prior
    corpus source documents a tool that finds and summarizes past agent sessions
    by semantic topic from within a chat conversation. The JetBrains unified
    sessions view (filterable by type and status) is visually browsable; this
    tool is query-driven.
  - **In-chat live status for sessions initiated via chat**: While live session
    status has been documented for IDEs (JetBrains unified view) and web surfaces
    (issues, projects), this is the first corpus documentation of live status
    surfaced within the Copilot Chat conversation thread itself.
  - **Chat as a full agent session lifecycle surface**: The combination of
    initiation (from contextual chat), monitoring (live status), and post-completion
    follow-up in a single chat thread is a new end-to-end pattern in the corpus.
    No prior note documents chat as the container for the complete session
    lifecycle — prior surfaces are either initiation-only (VS Code agent picker,
    issue assignment) or monitoring-only (remote control dashboard, unified
    sessions view).

## Guide Impact

- **Chapter 02 (Harness Engineering — Session Management Surfaces)**:
  - Update the multi-surface session management inventory to add Copilot Chat
    as the newest surface (June 2026), with four specific capabilities: live
    status, post-completion follow-up, Get agent logs, and Session search.
    The full surface map now spans: global dashboard, mobile, issues, projects,
    JetBrains IDE, and chat. Practitioners should choose surfaces based on
    context: chat for conversation-native workflows; issues for work-item-centric
    review; global dashboard for cross-session operational monitoring.
  - Document "Get agent logs" as the chat-native post-session forensics path
    for CCA sessions associated with a PR. When a cloud agent creates a PR,
    the reviewing practitioner can use this tool to query agent reasoning
    without navigating to the session dashboard.

- **Chapter 04 (Agentic Workflows)**:
  - Add the "chat-first agent workflow" pattern combining the contextual chat
    escalation path (from `docs-github-copilot-web-contextual-chat.md`) with
    this source's in-chat monitoring and follow-up: initiate in chat → live
    status in chat → follow-up in chat. Document this as the lowest-friction
    path for practitioners whose primary Copilot surface is web chat rather
    than an IDE.
  - Add Session search as a session continuity tool: when returning to a
    long-running project with many prior agent sessions, use session search
    to locate the relevant context before starting a new session, avoiding
    duplication of prior agent work.

- **Chapter 01 (Daily Workflows)**:
  - Add the chat-first agent lifecycle pattern (initiate → monitor → follow-up
    in a single chat thread) as an alternative to the IDE-centric agent workflow
    documented from JetBrains and VS Code sources. Practitioners who work
    primarily in the browser now have an end-to-end agentic workflow without
    requiring an IDE.

## Extraction Notes

1. **Short source (~150 words, typical GitHub changelog)**: All substantive claims
   are covered in the five claims above. The source is brief by design — a feature
   announcement for a changelog entry. The short length does not indicate a lack of
   depth; the feature scope is genuinely narrow (two tools + in-chat status).

2. **No verbatim quotes available for Claims 1, 4, 5**: Three separate WebFetch
   calls to the source URL returned consistent content but as AI-paraphrased
   summaries rather than character-for-character transcriptions. The two
   verbatim quotes used (Claims 2 and 3) appeared with explicit quotation marks
   in the fetched content and are consistent across fetches. Claims 1, 4, and 5
   use "no direct quote" markers rather than reconstructed quotes, per MINER.md
   §2a requirements.

3. **Plan-tier availability not stated**: The changelog does not specify which
   Copilot plan tiers can access the Get agent logs and Session search tools.
   Based on the pattern established across the corpus (CCA features are typically
   Business/Enterprise-gated), the Get agent logs tool may require Business or
   Enterprise access since it retrieves CCA session data. This is an inference,
   not a stated fact, and is not included as a claim.

4. **Session scope for "Session search" unclear**: The changelog does not specify
   whether session search covers the current user's sessions only or team/org-level
   sessions. Given that CCA sessions can be associated with organizational
   repositories, this distinction matters for enterprise practitioners but is not
   documented in this changelog.

5. **No contradictions found**: Reviewed all corpus source notes for claims
   that this source would contradict. The pattern across all agent session
   surface sources is additive — each new surface extends the inventory without
   contradicting prior claims about existing surfaces. No contradiction issue filed.
