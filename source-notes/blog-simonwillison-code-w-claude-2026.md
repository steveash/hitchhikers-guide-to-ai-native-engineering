---
source_url: https://simonwillison.net/2026/May/6/code-w-claude-2026/
source_type: blog-post
title: "Live blog: Code w/ Claude 2026"
author: Simon Willison
date_published: 2026-05-06
date_extracted: 2026-05-15
last_checked: 2026-05-15
status: current
confidence_overall: anecdotal
issue: "#742"
---

# Live blog: Code w/ Claude 2026

> Simon Willison's independent live blog of Anthropic's May 6 2026 developer
> event — capturing platform growth metrics (17x API volume YoY), the advisor
> strategy cost pattern (Opus advising Sonnet at "5x lower cost" for frontier
> quality), enterprise adoption targets (Mercado Libre: 90% autonomous coding
> by Q3), an emerging organizational shift (executives returning to code), and
> editorial skepticism about inspirational framing that the official Anthropic
> announcements do not provide.

## Source Context

- **Type**: blog-post (Simon Willison's personal live blog of the Anthropic
  "Code w/ Claude 2026" event, May 6, 2026; published the same day as
  `blog-simonwillison-vibe-coding-agentic-engineering.md`. This is event
  coverage with editorial commentary, not an independent analysis post.)
- **Author credibility**: Simon Willison is the creator of Django, one of the
  most widely-read independent AI tooling commentators, and a 25-year software
  engineering practitioner. He has no vendor affiliation. His editorial
  commentary adds signal that official Anthropic announcements cannot provide:
  he names skepticism explicitly ("too inspirational for my liking") and
  provides environmental context that Anthropic omits (Colossus data center
  environmental record). His coverage is a practitioner's interpretation of
  vendor claims, not an endorsement of them.
- **Scope**: Covers the Anthropic developer event on May 6, 2026. Captures:
  platform growth metrics, infrastructure partnerships, Claude Code feature
  announcements (Code Review, Remote Agents, CI auto-fix, Security Reviews,
  doubled session limits), Managed Agents updates (Dreaming, Outcomes,
  multiagent orchestration), async development workflow patterns (Routines),
  enterprise adoption evidence (Mercado Libre, Shopify), the advisor strategy
  cost pattern, and organizational shift observations. Does NOT provide
  implementation depth — this is event coverage, not an engineering post.
  No code examples, config details, or API specifics appear in this source.

## Extracted Claims

### Claim 1: Opus can be used as an on-demand advisor to smaller models (Sonnet), achieving "frontier model quality at 5x lower cost" — the advisor strategy pattern

- **Evidence**: Single customer example (eve) reported by Willison from the
  event. The pattern is: run Sonnet for most work; invoke Opus only when advice
  is needed, on-demand.
- **Confidence**: anecdotal (single customer example from an event presentation;
  no methodology or cost breakdown provided)
- **Quote**: "frontier model quality at 5x lower cost"
- **Our assessment**: This is the most architecturally distinctive claim in the
  source and the primary novelty flagged by the Prospector. The advisor strategy
  differs from the model-mixing pattern documented in
  `blog-anthropic-managed-agents-dreaming-outcomes.md` (Claim 8: Haiku as
  orchestrator + Opus as drafter specialist). In the advisor pattern, Sonnet
  does the primary work and Opus is consulted on-demand — a consultation
  pattern rather than a role-based division. The cost benefit (5x) comes from
  using Sonnet (cheaper per token) for the majority of generation while drawing
  on Opus selectively for higher-capability moments. This pattern is not
  previously documented in the corpus. Practitioners building cost-sensitive
  multi-model systems should evaluate: does the task have clear "needs expert
  advice" decision points that can trigger Opus invocation? If yes, the
  advisor strategy may achieve near-Opus quality at Sonnet-level cost for most
  tokens.

### Claim 2: Mercado Libre (23,000 engineers) is targeting 90% autonomous coding by Q3 2026

- **Evidence**: Customer presentation at the Code w/ Claude 2026 event,
  reported by Willison.
- **Confidence**: anecdotal (event presentation; the target is publicly stated
  but unverified by independent reporting)
- **Quote**: "23,000 engineers" aiming for "90% autonomous coding by Q3 this year"
- **Our assessment**: This is the most ambitious named enterprise adoption target
  in the corpus. "90% autonomous coding" means only 10% of coding tasks would
  require direct human execution. At 23,000 engineers, this represents one of
  the largest-scale agentic coding deployments reported anywhere. The Q3 2026
  timeline is specific and externally trackable. No prior corpus source
  documents a corporate target at this scale or specificity. The claim should
  be treated as a stated ambition, not a confirmed result; but the scale of
  the organization makes it a meaningful signal about enterprise-level
  commitment to agentic engineering adoption.

### Claim 3: Executives and managers are returning to hands-on coding because AI reduces the time investment required to contribute meaningfully

- **Evidence**: Event observation, reported by Willison. Framed as an
  organizational trend across adopting companies.
- **Confidence**: anecdotal (event-reported trend; no quantification provided)
- **Quote**: "execs and managers are getting their hands dirty with code again,
  because you don't need so much time to be able to usefully contribute"
- **Our assessment**: This is a significant organizational pattern. The time
  barrier to code contribution was previously the primary reason executives
  and managers step back from direct coding: maintaining coding fluency
  requires sustained investment that senior roles cannot sustain. AI
  assistance collapses the time-to-contribution for someone with
  historical coding background. The implication is two-directional:
  (1) technical managers can now validate implementations directly rather than
  relying purely on team reporting; (2) organizations may see blurred
  boundaries between "manager" and "individual contributor" roles when coding
  no longer requires sustained daily practice. No prior corpus source
  documents this organizational pattern from enterprise adoption evidence.

### Claim 4: Anthropic's platform API volume grew 17x year-on-year as of May 2026

- **Evidence**: Stated at the Code w/ Claude 2026 event.
- **Confidence**: emerging (vendor-stated metric; not independently verified;
  but specific enough to be a credible internal measurement)
- **Quote**: "API volume is up 17x year-on-year on the Anthropic platform"
- **Our assessment**: 17x YoY growth is extraordinary if accurate. This is the
  first corpus source to report Anthropic platform-level growth metrics. The
  metric does not distinguish between direct API usage and usage through
  Claude Code or Claude Managed Agents, so it captures aggregate platform
  adoption rather than any specific product's traction. Even with this
  ambiguity, the scale of growth is a useful signal for practitioners
  evaluating whether Anthropic's infrastructure and pricing will remain stable
  under continued adoption. The SpaceX/Colossus partnership (Claim 5) is
  likely a direct response to this growth rate.

### Claim 5: Anthropic is partnering with SpaceX to use all capacity of the Colossus data center to increase rate limits — but Willison notes Colossus has a particularly bad environmental record

- **Evidence**: Event announcement from Anthropic; editorial context added by
  Willison independently.
- **Confidence**: settled (factual infrastructure announcement; environmental
  record is independently documented about the Memphis Colossus facility)
- **Quote**: "We're partnering with SpaceX to use all of the capacity of their
  Colossus data center" / "(That's the same Colossus data center in Memphis
  with the particularly bad environmental record.)"
- **Our assessment**: The infrastructure announcement signals that rate limits
  were a real constraint on adoption (the partnership is the response), and
  that Anthropic is investing in significant capacity expansion. The
  environmental context from Willison is the only place in the corpus where
  the environmental cost of AI infrastructure is named with a specific
  facility citation. This is relevant for organizations with sustainability
  commitments who are evaluating AI infrastructure choices. Willison was also
  skeptical that this was the only news from the opening session:
  "(So far the only news in this session has been the SpaceX Colossus deal.)"
  — indicating the announcement landed as infrastructure logistics rather
  than a product capability unlock.

### Claim 6: Claude Code's five-hour session limit was doubled for Pro, Max, and Enterprise customers

- **Evidence**: Event product announcement, reported by Willison.
- **Confidence**: settled (product limit change; directly verifiable by users)
- **Quote**: (no direct verbatim quote; reported by Willison as a product change)
- **Our assessment**: Doubling the session limit from five hours to ten hours
  substantially extends the practical ceiling for long-running agentic tasks.
  The five-hour limit was the first hard boundary practitioners hit on
  compute-intensive workloads (large codebase migrations, comprehensive test
  suites, multi-stage deployments). A ten-hour limit accommodates significantly
  more complex tasks within a single session context window. This change is
  particularly relevant in combination with the Routines feature
  (`blog-anthropic-claude-code-routines.md` Claim 3) — scheduled nightly
  routines now have more headroom for complex end-to-end tasks.

### Claim 7: The Code Review feature is used by every team at Anthropic internally, signaling high internal confidence in the feature's reliability

- **Evidence**: Internal dogfooding claim stated at the event.
- **Confidence**: anecdotal (vendor self-report of internal adoption; not
  independently verifiable)
- **Quote**: "used by every team at Anthropic"
- **Our assessment**: Internal adoption at Anthropic across every team is a
  meaningful signal. If the Code Review feature were unreliable or produced
  low-signal output, engineering teams within Anthropic would not use it for
  production code review. The internal-use claim raises the feature's
  credibility above typical product announcements. However, the claim is
  self-referential: Anthropic employees are the most motivated to make
  Anthropic's tools succeed, and their codebases are presumably well-suited
  to Claude's capabilities. "Every team at Anthropic uses it" is a higher
  bar than "some teams at Anthropic use it" but a lower bar than "engineering
  teams at organizations with diverse codebase types use it reliably."

### Claim 8: Remote Agents enable developers to control their laptop from a phone, enabling mobile-initiated development

- **Evidence**: Feature announcement at the event, reported by Willison.
- **Confidence**: emerging (product announcement; feature behavior not
  independently documented)
- **Quote**: (no direct verbatim quote available)
- **Our assessment**: Remote Agents decouple the developer's physical location
  from the machine where agent execution happens. The practical implication:
  a developer can initiate, monitor, and interact with Claude Code sessions
  from a phone without being at their laptop. Combined with the agent view
  feature (`blog-anthropic-agent-view-claude-code.md` Claim 1), this creates
  a full async management workflow where the developer's interface is the
  phone and the execution environment is the development machine. This
  extends the async development pattern (Claim 10 below) to physical mobility.

### Claim 9: CI auto-fix provides automatic fixes against PRs in CI/CD pipelines

- **Evidence**: Feature announcement at the event, reported by Willison.
- **Confidence**: emerging (product announcement; implementation details not
  described)
- **Quote**: (no direct verbatim quote available)
- **Our assessment**: CI auto-fix is the natural extension of the Routines
  webhook-triggered pattern (`blog-anthropic-claude-code-routines.md` Claim 5)
  to CI failure events. When a PR triggers a CI failure, the auto-fix routine
  analyzes the failure and attempts to fix it — matching the alert triage
  pattern from the Routines announcement. The practical value is closing the
  loop on CI-gated PRs without developer intervention for common failure types
  (lint, formatting, straightforward test failures). The quality ceiling is
  the same as any automated fix: reliable for deterministic failures,
  uncertain for logic failures or flaky tests.

### Claim 10: The Routines async development pattern means developers "wake up to PRs that are ready to merge"

- **Evidence**: Event presentation, reported by Willison. The phrase captures
  the end-state goal of async development workflows.
- **Confidence**: emerging (the pattern is corroborated by blog-anthropic-
  claude-code-routines.md; the phrase is Willison's event summary)
- **Quote**: "developers can setup async automations and wake up to PRs that
  are ready to merge"
- **Our assessment**: This is the clearest single-sentence statement of the
  async development workflow's value proposition in the corpus. The shift from
  "developer executes task and waits for completion" to "developer sets intent,
  goes to sleep, reviews results in the morning" is a fundamental change in
  how development work is scheduled. The phrase "ready to merge" (rather than
  "ready for review") sets a high bar — the PRs have already been reviewed,
  tested, and deemed complete by the agent, not just initiated. Whether this
  bar is reliably met in practice is not documented by this source, but the
  aspiration is precisely stated.

### Claim 11: Willison found the opening of the event "too inspirational" and was explicitly hoping for product announcements rather than inspirational framing

- **Evidence**: Willison's editorial commentary in the live blog.
- **Confidence**: settled (first-person stated preference; direct quote)
- **Quote**: "This is all a little bit too inspirational for my liking, I'm
  hoping for some new model / product / feature announcements!"
- **Our assessment**: This is the calibration context for interpreting the
  event coverage. Willison's skepticism is professionally significant: a
  25-year practitioner with no vendor affiliation explicitly naming
  inspirational framing as a concern provides the kind of editorial signal
  that official announcements cannot. The quote establishes that the event
  leaned toward organizational adoption stories and vision before pivoting
  to product announcements — and that Willison was tracking this pattern
  in real time. For the guide: when citing event claims, distinguish between
  inspirational adoption narratives (Mercado Libre target, Shopify examples)
  and product announcements with verifiable specifications (session limit
  doubling, Code Review feature).

## Concrete Artifacts

### The Advisor Strategy Pattern

```
Advisor Strategy — Cost Optimization via On-Demand Model Consultation
(Reported by Simon Willison from Code w/ Claude 2026, May 6 2026)

Customer example: eve

Pattern:
  PRIMARY WORKER: Sonnet (runs most generation tasks)
  ADVISOR:        Opus (invoked on-demand for higher-capability consultation)

Result:
  "frontier model quality at 5x lower cost"

Comparison to model-mixing (blog-anthropic-managed-agents-dreaming-outcomes.md Claim 8):
  Model mixing:     Haiku (orchestrator/router) + Opus (specialist drafter)
                    — role-based division, each agent owns a workflow stage
  Advisor strategy: Sonnet (primary worker) + Opus (on-demand consultant)
                    — consultation pattern, Opus is invoked at decision points
                    within Sonnet's workflow

Decision criterion: Use advisor strategy when the task has identifiable
"needs expert input" moments that can trigger Opus invocation; use model
mixing when the task has distinct roles with clear handoffs.
```

### Enterprise Adoption Signals (May 2026)

```
Enterprise AI Coding Adoption — Code w/ Claude 2026 (Willison live blog)

MERCADO LIBRE:
  Engineers:  23,000
  Target:     90% autonomous coding
  Deadline:   Q3 2026
  Status:     Stated organizational target (not confirmed result)

SHOPIFY:
  Status: Mentioned as enterprise adopter (no specific target or metric reported)

API PLATFORM:
  Growth: 17x year-on-year (as of May 2026)

ORGANIZATIONAL SHIFT:
  "execs and managers are getting their hands dirty with code again,
   because you don't need so much time to be able to usefully contribute"
  Pattern: AI reduces time-to-meaningful-contribution, enabling lapsed
           coders (managers, executives) to re-engage with direct coding.
```

### Code w/ Claude 2026 Feature Announcement Summary

```
Claude Code Feature Announcements (May 6, 2026)
Source: Simon Willison live blog; Anthropic Code w/ Claude 2026 event

INFRASTRUCTURE:
  SpaceX/Colossus partnership: full data center capacity for rate limits
  (Note: Memphis Colossus has documented environmental concerns — Willison)
  Session limit: doubled from 5 hours for Pro, Max, Enterprise

CLAUDE CODE FEATURES (NEW OR ANNOUNCED):
  Code Review:     "used by every team at Anthropic"
  Remote Agents:   control laptop from phone
  CI auto-fix:     automatic fixes against PRs in CI
  Security Reviews: capability announced

MANAGED AGENTS UPDATES (covered in detail in
blog-anthropic-managed-agents-dreaming-outcomes.md):
  Dreaming:                 research preview
  Outcomes:                 public beta
  Multiagent orchestration: public beta

ASYNC DEVELOPMENT WORKFLOW (covered in
blog-anthropic-claude-code-routines.md):
  Routines: "developers can setup async automations and wake up
             to PRs that are ready to merge"
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-managed-agents-dreaming-outcomes.md` (Claims 1–10):
    Willison's live blog confirms the Dreaming, Outcomes, and multiagent
    orchestration announcements from the same May 6 event. The dreaming
    description ("inspect its previous sessions and figure out what it missed
    and self-improve") corroborates Claim 1 in that note. Willison's framing
    is simpler but consistent with the architectural description in the
    official announcement.
  - `blog-anthropic-claude-code-routines.md` (Claim 2, Claim 3): Willison's
    "wake up to PRs that are ready to merge" (Claim 10 here) is the
    practitioner-facing value statement for the Routines async pattern
    described in detail in that note. The Routines note documents how the
    pattern works; this source gives the clearest statement of why it matters.
  - `blog-anthropic-agent-view-claude-code.md` (Claim 1, Claim 6): Remote
    Agents (Claim 8 here) extends the parallel session management pattern.
    Agent view + Remote Agents = manage multiple Claude Code sessions from a
    phone without being at a laptop. These features compose into a full
    mobile-async development workflow.
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` (Claim 9, Claim 10):
    Willison's observation that software complexity remains "ferociously
    difficult" (Claim 10 there) and that AI is an amplifier of existing
    expertise (Claim 9 there) provides the grounding context for why the
    "90% autonomous coding" target (Claim 2 here) should be interpreted
    cautiously — the target is for coding volume, not for software complexity
    overall. Published the same day (May 6 2026).

- **Extends**:
  - `blog-anthropic-managed-agents-dreaming-outcomes.md` (Claim 8): That
    note documents the Spiral (Every) model-mixing example: Haiku as lead
    orchestrator + Opus as specialist drafter. This source adds the advisor
    strategy (Claim 1 here): Sonnet as primary worker + Opus as on-demand
    consultant. Together, the corpus now has two named, customer-validated
    model-mixing/advisor patterns for cost optimization — role-based
    division (model mixing) and consultation-on-demand (advisor strategy).
  - `blog-anthropic-claude-code-routines.md` (Claim 9): The Routines note
    documented six use case patterns. Claim 9 here (CI auto-fix against PRs)
    is a seventh pattern that extends the Routines taxonomy — applying the
    webhook-triggered pattern specifically to CI failure events rather than
    PR review events.

- **Novel**:
  - **Advisor strategy pattern (Opus as on-demand consultant to Sonnet)**:
    No prior corpus source documents the consultation-on-demand model
    where the smaller model does primary work and the larger model is invoked
    at specific decision points. The 5x cost claim with "frontier model
    quality" is the first cost-efficiency claim for this specific pattern
    in the corpus.
  - **Mercado Libre 90% autonomous coding by Q3 target**: The most ambitious
    named enterprise adoption target in the corpus, with a specific deadline.
    No prior corpus source documents a corporate autonomous coding target at
    this scale or specificity.
  - **Organizational shift — executives/managers returning to coding**: The
    observation that reduced implementation time is enabling lapsed coders
    in management roles to re-engage with direct coding is a named
    organizational pattern not documented in any prior corpus source.
  - **Anthropic platform 17x YoY API volume growth**: First corpus source
    to report an Anthropic platform-level growth metric.
  - **SpaceX/Colossus environmental context**: No other corpus source names
    the environmental record of an AI infrastructure facility. Willison's
    parenthetical is the only place in the corpus where this concern appears.
  - **Willison's live-blog editorial skepticism as calibration signal**: The
    "too inspirational" framing provides the only independent practitioner
    calibration of an Anthropic event's inspirational-to-technical ratio in
    the corpus.

- **Contradicts**: None filed. No claims in this source materially oppose
  claims in existing corpus notes on the same topic. The advisor strategy
  (Opus consulting Sonnet) and the model-mixing pattern (Haiku orchestrating
  Opus) are distinct patterns, not contradictory recommendations.

## Guide Impact

- **Chapter 02 (Cost Optimization / Model Selection)**: Add the advisor
  strategy pattern (Claim 1) as a named cost optimization pattern alongside
  the model-mixing pattern from `blog-anthropic-managed-agents-dreaming-
  outcomes.md` Claim 8. The guide currently documents role-based model
  division (cheap model routes, expensive model generates). The advisor
  strategy adds a different topology: primary model does the work, expert
  model consulted on-demand. For practitioners building cost-sensitive
  multi-model systems, present both patterns with the decision criterion:
  use model mixing when the task has distinct roles with clear handoffs;
  use advisor strategy when the task has identifiable "needs expert input"
  moments within a unified workflow.

- **Chapter 05 (Team and Organizational Adoption)**: Add the managers/
  executives returning to coding pattern (Claim 3) as an emerging
  organizational consequence of agentic adoption. The guide currently
  focuses on individual developer productivity; this is the first corpus
  evidence of an organizational-role-level consequence (blurring of
  manager/IC distinction). Frame it as an opportunity (technical leaders
  can validate directly) and a governance question (who is accountable
  for AI-generated code that a manager initiated and did not deeply review?).

- **Chapter 05 (Enterprise Adoption Evidence)**: Add Mercado Libre's 90%
  autonomous coding target by Q3 2026 (Claim 2) as the most ambitious
  enterprise adoption target in the corpus. Pair it with Willison's
  "too inspirational" calibration (Claim 11) as a reminder that publicly
  stated targets at developer events are aspirational, not confirmed
  results. The guide should present this as a directional signal about
  enterprise commitment, not a proven outcome.

- **Chapter 02 (Harness Engineering — Session Limits)**: Update any
  references to Claude Code's five-hour session limit (Claim 6) to reflect
  that it was doubled to ten hours for Pro/Max/Enterprise as of May 2026.
  Any harness patterns designed around the five-hour ceiling (sprint
  decomposition, session segmentation) should note the new limit.

- **Chapter 03 (Code Review and Quality Practices)**: Add the Code Review
  internal adoption claim (Claim 7 — "every team at Anthropic") as
  practitioner-credibility evidence for the feature alongside the feature
  description. Internal dogfooding across all Anthropic teams is a stronger
  reliability signal than a product announcement alone.

- **Chapter 01 (Async Development Workflows)**: The "wake up to PRs ready
  to merge" framing (Claim 10) is the clearest articulation of the async
  development shift's value proposition. Use it as the opening framing for
  any chapter or section on scheduled/background development workflows,
  paired with `blog-anthropic-claude-code-routines.md` for implementation
  patterns.

## Extraction Notes

- This is a live blog — content was written in real time as the event
  unfolded. The "too inspirational" quote and environmental aside
  ("particularly bad environmental record") reflect Willison's real-time
  reaction rather than considered post-event analysis. They carry the
  authenticity of unfiltered observation.
- WebFetch returned verbatim quotes from the source. Quotes were taken
  directly from the WebFetch output and not reconstructed. The "frontier
  model quality at 5x lower cost" quote is attributed to one customer (eve)
  as reported by Willison — it may be a speaker's direct quote or Willison's
  paraphrase of the claim; the source does not distinguish.
- For Claim 6 (session limit doubled), Claim 8 (Remote Agents), and Claim 9
  (CI auto-fix), no verbatim quote was recoverable from WebFetch. These
  claims are noted with explicit "(no direct verbatim quote available)" in
  their Quote fields and rated accordingly.
- The Managed Agents features (Dreaming, Outcomes, multiagent orchestration)
  were announced at the same event but are covered in much greater depth in
  `blog-anthropic-managed-agents-dreaming-outcomes.md`. This source note
  focuses on the practitioner and organizational context that Willison's
  independent commentary adds, not on re-extracting the product features
  already documented in the official announcement note.
- The source was read in full. No sub-pages were followed (the source is a
  single live blog page with no substantive linked content that was not
  already in the corpus).
- Confidence is set to `anecdotal` overall: this is event coverage with
  first-person editorial commentary. The platform growth metrics (17x YoY)
  and session limit doubling are the most verifiable claims; the advisor
  strategy cost figure and organizational shift observations are vendor-event
  claims reported by a practitioner with no independent verification.
