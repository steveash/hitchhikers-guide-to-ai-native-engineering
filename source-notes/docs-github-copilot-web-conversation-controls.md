---
source_url: https://github.blog/changelog/2026-08-10-copilot-on-web-expands-conversation-controls
source_type: docs
title: "Copilot on web expands conversation controls"
author: GitHub (official changelog)
date_published: 2026-08-10
date_extracted: 2026-08-11
last_checked: 2026-08-11
status: current
confidence_overall: settled
issue: "#2619"
---

# Copilot on Web Expands Conversation Controls

> GitHub's August 10, 2026 changelog adds three ergonomic controls to Copilot Chat on
> github.com — minimizing the chat overlay to browse GitHub while a response is pending,
> easier access to recent conversations, and per-session/per-message token spend
> indicators — framed as improvements to the "chat overlay experience" introduced by the
> May 18, 2026 contextual chat panel launch, and shipped GA for all Copilot plans with no
> new spend controls (visibility only, unlike the CLI/SDK's session credit caps).

## Source Context

- **Type**: docs (GitHub official product changelog, August 10, 2026; labeled
  "Improvement," ~120 words of primary content across an intro paragraph and two named
  sub-sections, "1 minute read")
- **Author credibility**: GitHub engineering team announcing a production GA release.
  Authoritative for the existence of the three controls, their described behavior, and
  the plan-tier availability statement. Not a credible source for: adoption data, why
  these three controls were bundled together, whether "per-session" and "per-message"
  quota figures are AI credits or raw tokens, whether the token spend indicator links to
  the underlying `ai_credits_used` usage-metrics field, or any UI screenshots beyond the
  one captioned image of the token spend indicator.
- **Scope**: Three named improvements to Copilot Chat on github.com: (1) minimize the
  chat window during an in-progress conversation and resume browsing GitHub, (2) easier
  access to view and continue recent conversations, (3) token spend indicators showing
  per-session and per-message quota, accessible by clicking a new icon in chat. States
  GA availability for all Copilot plans. Does NOT cover: the underlying credit-to-token
  conversion, whether "recent conversations" spans the immersive and contextual-panel
  modes documented in `docs-github-copilot-web-contextual-chat.md`, whether minimized
  conversations continue to consume tokens or accumulate navigation context while
  minimized, or any interaction between the token spend indicator and admin-level usage
  metrics/budget alerts.

## Extracted Claims

### Claim 1: GitHub shipped three named improvements to Copilot Chat on github.com in this release — easier access to recent conversations, the ability to minimize and resume the chat window, and token spend indicators

- **Evidence**: Official GitHub product changelog, framed as a single "Improvement"
  entry bundling three distinct UI changes under one release.
- **Confidence**: settled (product fact — stated as the entry's opening summary)
- **Quote**: "We've made improvements to Copilot Chat on github.com that make it easier
  to use. These include easier access to your recent conversations in chat, the ability
  to minimize the chat window and return to an in-progress conversation, and indicators
  that help you track your Copilot token spend."
- **Our assessment**: All three changes are ergonomic/session-management improvements
  to the existing chat surface rather than new capabilities (no new model access, no new
  agent behavior). They read as iterative polish on the in-page "chat overlay" UX that
  the May 18, 2026 contextual chat launch introduced (`docs-github-copilot-web-contextual-chat.md`),
  84 days earlier. The changelog's own phrase "chat overlay experience" (Claim 2) ties
  this release directly to that prior launch's terminology.

### Claim 2: The chat window can now be minimized during an in-progress conversation, allowing the user to browse other GitHub pages while waiting for a Copilot response

- **Evidence**: Official changelog stating the behavior explicitly under the "Minimize
  and resume conversations" sub-heading.
- **Confidence**: settled (product fact — stated in official changelog)
- **Quote**: "The first is the ability to minimize the screen during a conversation.
  This allows you to browse GitHub while waiting for a Copilot response."
- **Our assessment**: This addresses a real friction point in the May 18 contextual
  panel model: before this release, an in-progress chat response likely held the panel
  open (or at least the user's attention) while waiting. Minimizing decouples "waiting
  for Copilot" from "blocked on Copilot" — the user can keep browsing GitHub, which
  matters for the cross-navigation context accumulation behavior documented in
  `docs-github-copilot-web-contextual-chat.md` Claim 5: if navigation while a response is
  pending continues to accumulate references, minimizing effectively lets a user build
  more context into the same session while waiting. The changelog does not state whether
  minimized-state navigation continues to accumulate references — this is an open
  question the guide should flag rather than assume either way.

### Claim 3: Users can now more easily view and continue their recent conversations in Copilot Chat on the web

- **Evidence**: Official changelog stating this as the second feature under "Minimize
  and resume conversations," with no further elaboration on the UI mechanism.
- **Confidence**: settled (product fact stated in changelog); mechanism-level detail
  (where the recent-conversations list appears, how far back it goes, whether it spans
  contextual-panel and immersive modes) is not specified
- **Quote**: "The second is the ability to more easily view and continue your recent
  conversations."
- **Our assessment**: This is a lighter-weight, chat-surface-local counterpart to the
  "Session search" and "Get agent logs" tools that `docs-github-copilot-chat-agent-sessions.md`
  (June 10, 2026) added for finding and inspecting past *agent* sessions. That June 10
  feature was scoped to cloud agent work (PRs, logs); this August 10 feature reads as
  scoped to ordinary chat conversations (Q&A, not necessarily agent-escalated). The
  changelog does not clarify whether "recent conversations" here overlaps with or is
  distinct from the June 10 session search surface — practitioners should not assume
  they are the same feature until this is confirmed.

### Claim 4: Copilot Chat on the web now shows token spend indicators; clicking the token spend icon reveals per-session and per-message quota

- **Evidence**: Official changelog under the "Monitor your token usage" sub-heading,
  with an accompanying screenshot captioned to match.
- **Confidence**: settled (product fact — UI element and its two quota granularities
  stated explicitly in official changelog)
- **Quote**: "We've also added token spend indicators in chat. Clicking on the token
  spend icon lets you see your per-session and per-message quota, allowing you greater
  visibility into your token spend and budget."
- **Our assessment**: This is the most operationally significant claim in the source.
  It is a *visibility* feature, not a *control* feature — despite the changelog entry's
  title ("expands conversation controls"), the token spend indicator does not cap,
  throttle, or warn-and-block spend; it only displays it on click. This is a materially
  different governance model from `docs-github-copilot-cli-sdk-session-credit-limits.md`,
  which added an enforced soft cap (`/limits`, `--max-ai-credits`) that stops an agent
  session when a credit ceiling is reached. Web chat gets a dashboard; CLI/SDK gets a
  circuit breaker. For Ch04 (Context/Cost Engineering): practitioners working in web
  chat can now self-monitor spend per session and per message, but nothing in this
  source prevents them from exceeding a budget — the guide should not describe this as
  a "limit" or "cap," only as a transparency feature.

### Claim 5: The token spend indicator distinguishes between per-session quota and per-message quota as two separate figures

- **Evidence**: The quote in Claim 4 names both granularities explicitly ("per-session
  and per-message quota"), and the screenshot caption independently confirms both.
- **Confidence**: settled (both granularities named in official changelog and image
  caption)
- **Quote**: "Copilot Chat token spend indicators showing per-session and per-message
  quota" (image caption)
- **Our assessment**: The two-granularity split (session-level vs. message-level) is
  the first corpus evidence of GitHub exposing message-level token accounting to end
  users in any Copilot surface — prior usage-metrics sources
  (`docs-github-copilot-usage-metrics-ai-credits-per-user.md`) expose per-user,
  per-day aggregate AI credit consumption via API for admins, not per-message figures
  visible to the end user in the chat UI itself. This is a new, finer-grained
  self-service cost visibility layer distinct from the admin-facing usage metrics API.

### Claim 6: All three improvements (minimize/resume, recent conversations, token spend indicators) are generally available to all Copilot plans, with no tier restriction

- **Evidence**: Official changelog's closing availability statement, applying to the
  full set of features described in the entry.
- **Confidence**: settled (plan availability stated explicitly in official changelog)
- **Quote**: "These features are generally available to all Copilot plans."
- **Our assessment**: Consistent with the May 18 contextual chat launch
  (`docs-github-copilot-web-contextual-chat.md` Claim 7), which was also GA for all
  plans with no tier gate. Together the two web-chat UX releases suggest GitHub is
  treating web chat interaction/session ergonomics (panel UX, minimize/resume, spend
  visibility) as broadly available baseline functionality, in contrast to compute- or
  admin-oriented features (CCA task creation, usage metrics API access) that carry
  Business/Enterprise or admin-role gates elsewhere in the corpus.

## Concrete Artifacts

### Verbatim Text of Source Changelog (August 10, 2026)

```
Title: Copilot on web expands conversation controls
Label: Improvement | August 10, 2026 • 1 minute read

We've made improvements to Copilot Chat on github.com that make it easier to
use. These include easier access to your recent conversations in chat, the
ability to minimize the chat window and return to an in-progress conversation,
and indicators that help you track your Copilot token spend.

Minimize and resume conversations

We've improved the chat overlay experience by adding two new features.

The first is the ability to minimize the screen during a conversation. This
allows you to browse GitHub while waiting for a Copilot response.

The second is the ability to more easily view and continue your recent
conversations.

Monitor your token usage

We've also added token spend indicators in chat. Clicking on the token spend
icon lets you see your per-session and per-message quota, allowing you greater
visibility into your token spend and budget.

[Image caption: Copilot Chat token spend indicators showing per-session and
per-message quota]

These features are generally available to all Copilot plans.

Try it out at github.com/copilot.
```

Source: https://github.blog/changelog/2026-08-10-copilot-on-web-expands-conversation-controls
Retrieved: 2026-08-11 via WebFetch (two independent fetches — one summarized, one
requested verbatim reproduction; content consistent between both)

### Feature Summary: Copilot Web Conversation Controls (August 10, 2026)

```
Feature: Copilot Web Conversation Controls
Published: 2026-08-10
Availability: All GitHub Copilot plans (no tier restriction)

1. Minimize/resume:
   - Minimize chat overlay while a response is pending -> browse GitHub freely
   - View + continue recent conversations more easily

2. Token spend visibility:
   - New "token spend icon" in chat
   - Click -> shows per-session quota AND per-message quota
   - Visibility only -- no cap, no throttle, no block described

Governance model contrast:
   Web chat (this source):        visibility only, no enforcement
   CLI/SDK (session-credit-limits, 2026-07-01): enforced soft cap via
     /limits or --max-ai-credits, stops session at ceiling
```

## Cross-References

- **Extends**:
  - **`docs-github-copilot-web-contextual-chat.md`** (issue #817, May 18, 2026): That
    source introduced the in-page "contextual chat panel" as the default web Copilot
    UX, replacing navigation to a separate immersive page. This source's own language —
    "we've improved the chat overlay experience" — directly references that same UX
    surface, 84 days later. This source adds session-management ergonomics (minimize,
    resume, recent conversations) and cost visibility (token spend indicators) on top
    of the panel model that source established. Both are GA for all plans with no tier
    gate (this source's Claim 6 vs. that source's Claim 7).
  - **`docs-github-copilot-chat-agent-sessions.md`** (issue #1145, June 10, 2026): That
    source added "Session search" and "Get agent logs" tools scoped to past *cloud
    agent* sessions (PR work, logs). This source's "recent conversations" feature
    (Claim 3) is a lighter-weight, chat-surface-local counterpart scoped to ordinary
    conversations rather than agent sessions specifically. The changelog for this
    source does not clarify overlap between the two — flagged as an open question in
    Claim 3's assessment.
  - **`docs-github-copilot-usage-metrics-ai-credits-per-user.md`** (issue #1251, June
    19, 2026): That source added an `ai_credits_used` field to the admin-facing usage
    metrics API, exposing per-user, per-day aggregate credit consumption. This source
    adds a distinct, finer-grained, end-user-facing visibility layer: per-session and
    per-message quota, visible by clicking an icon in the chat UI itself rather than
    via an API call. Together they show GitHub building cost visibility at two levels:
    admin/API (aggregate, per-user, per-day) and end-user/UI (per-session, per-message).
    Neither source documents whether the two are numerically reconcilable (e.g.,
    whether the API's `ai_credits_used` figure would match the sum of a user's
    in-chat per-session indicators).

- **Contradicts**: None identified directly, but see the note below on the changelog's
  own title. The entry is titled "Copilot on web expands conversation *controls*," yet
  Claim 4/5 (token spend indicators) provide visibility, not control (no cap or
  enforcement mechanism is described). This is not a contradiction with another source
  — it is an internal framing tension worth flagging: the title implies a governance
  capability the body does not actually describe. Not filed as a formal contradiction
  issue per MINER.md §4a guidance, since this is a single source's own title-vs-body
  framing gap, not an opposing claim between two sources or notes.

- **Novel**:
  - **Session-scoped minimize/resume for web chat**: No prior corpus source documents
    a minimize-and-resume interaction pattern for GitHub Copilot's web chat overlay.
  - **In-chat, per-message token spend visibility**: No prior corpus source documents
    end-user-visible, message-level token/credit spend accounting inside a chat UI.
    Prior cost-visibility sources are either admin-facing (usage metrics API) or
    enforcement-facing (CLI/SDK session credit limits), not end-user informational
    displays at message granularity.

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Update the web Copilot workflow pattern (added per
  `docs-github-copilot-web-contextual-chat.md`) to note that, as of August 10, 2026,
  users can minimize an in-progress chat response and keep browsing/reviewing without
  losing the pending response, then resume from recent conversations. This removes a
  minor "must wait or lose the response" friction point from the browser-based review
  workflow.

- **Chapter 04 (Context/Cost Engineering)**: Add the per-session/per-message token
  spend indicator as a self-service cost-visibility tool available to all web Copilot
  users. Explicitly note the distinction from enforcement: this indicator does not cap
  or throttle spend the way the CLI/SDK's `--max-ai-credits` / `/limits` mechanism
  does (`docs-github-copilot-cli-sdk-session-credit-limits.md`) — it is read-only
  visibility a user must actively click to check. Practitioners who want their web
  chat spend actually bounded, not merely visible, still need admin-level controls or
  the CLI/SDK's session-limit mechanism; web chat has no equivalent enforcement as of
  this source.

- **Chapter 05 (Team Adoption)**: Note that all three controls are GA with no plan-tier
  gate, consistent with GitHub's pattern (also seen in the May 18 contextual chat
  launch) of shipping web chat UX/ergonomics improvements broadly rather than gating
  them to Business/Enterprise. Teams onboarding practitioners to web Copilot can point
  to the token spend indicator as a built-in, no-setup-required way for individual
  contributors to self-monitor usage, complementing (not replacing) org-level usage
  metrics dashboards.

## Extraction Notes

1. **Very short source (~120 words)**: This is among the shortest changelog entries
   in the corpus, comparable in length to the May 18 and May 20 web Copilot changelog
   entries already in the corpus. All substantive claims are exhausted in the six
   claims above; a seventh possible claim (the title's "controls" framing vs. the
   body's visibility-only content) is discussed under Cross-References rather than
   given its own claim, since it is an interpretive observation about the source's own
   internal framing rather than an independent factual claim.

2. **Verbatim quotes verified across two fetches**: One WebFetch call returned a
   structured summary; a second, explicitly requesting verbatim character-for-character
   reproduction, returned the full body text reproduced in Concrete Artifacts. The two
   fetches were consistent in content; all quotes used in claims are drawn from the
   verbatim-reproduction fetch, not the summarized one.

3. **No sub-pages followed**: The changelog entry contains no links to further
   documentation pages beyond the "Try it out at github.com/copilot" call-to-action,
   which points to the product itself rather than a documentation page. No sub-pages
   were followed.

4. **Open questions the guide should not resolve from this source alone**: (a) whether
   minimized-conversation state continues to accumulate navigation context per the
   mechanism in `docs-github-copilot-web-contextual-chat.md` Claim 5; (b) whether
   "recent conversations" (Claim 3) overlaps with the June 10 "Session search" feature;
   (c) whether per-session/per-message quota figures are denominated in AI credits or
   raw tokens, and whether they reconcile with the admin-facing `ai_credits_used`
   field. None of these are answerable from this source; flagged rather than guessed.

5. **No contradictions filed**: Reviewed all Copilot-web and Copilot-cost/usage-metrics
   source notes in the corpus for conflicts. No existing note claims web chat has (or
   lacks) spend enforcement, so there is no opposing claim to contradict — this source
   is the first to establish that web chat spend visibility, specifically, is
   click-to-reveal and not enforced. No contradiction issue required per MINER.md §4a.
