---
source_url: https://claude.com/blog/dispatch-and-computer-use
source_type: blog-post
title: "Put Claude to work on your computer"
author: Anthropic (Claude.com blog)
date_published: 2026-03-23
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#177"
---

# Put Claude to work on your computer

> Anthropic's product announcement introducing computer use (mouse/keyboard/screen
> control as a fallback when no connector exists) and Dispatch (async multi-device
> task delegation), establishing a connector-first → computer-use graceful-degradation
> hierarchy for agent harness design and a three-safeguard safety model practitioners
> should replicate.

## Source Context

- **Type**: blog-post (Anthropic product announcement, March 2026)
- **Author credibility**: First-party Anthropic announcement published on claude.com.
  This is vendor communication describing a released research preview — not an
  engineering retrospective with controlled benchmarks, but authoritative on intended
  behavior and design intent. Claims about safety architecture and the tool hierarchy
  carry maximum credibility since Anthropic is describing their own system. Claims
  about reliability and speed are self-reported and optimistic by nature.
- **Scope**: Covers two capabilities: (1) computer use — Claude controlling mouse,
  keyboard, and screen in Claude for Work and Claude Code when connectors are absent;
  (2) Dispatch — async task delegation from mobile to desktop with one continuous
  conversation thread. Available to Claude Pro and Max subscribers on macOS and
  Windows. Does NOT cover cost characteristics, token usage for computer use sessions,
  failure modes or error recovery, or how prompt injection detection works at a
  technical level.

## Extracted Claims

### Claim 1: Claude prioritizes precise connectors over computer use — computer use is explicitly the fallback, not the default

- **Evidence**: Direct product design statement from Anthropic: "Claude will reach
  for the most precise tool first, starting with connectors to services like Slack or
  Google Calendar. When there isn't a connector, Claude can directly control your
  browser, mouse, keyboard, and screen."
- **Confidence**: settled (first-party architectural statement of intended behavior)
- **Quote**: "Claude will reach for the most precise tool first, starting with
  connectors to services like Slack or Google Calendar. When there isn't a connector,
  Claude can directly control your browser, mouse, keyboard, and screen to complete
  tasks."
- **Our assessment**: This is a named design principle with direct harness engineering
  implications. The hierarchy is: direct API integration > connector > computer use.
  Practitioners building agent harnesses should replicate this same triage logic
  when choosing how an agent will interact with an external service. Computer use is
  powerful but slower and less reliable than a connector; it should be the last resort,
  not the first. This formalizes "graceful degradation by integration type" as an
  explicit pattern, not just a cost optimization.

### Claim 2: Computer use requires no setup — Claude can open files, use the browser, and run dev tools automatically from within Claude Code

- **Evidence**: Product description: "In Claude Code, Claude can open files, use the
  browser, and run dev tools automatically — with no setup required."
- **Confidence**: emerging (product claim; behavior may vary across platforms and
  configurations; research preview status means this can change)
- **Quote**: "In Claude Code, Claude can open files, use the browser, and run dev
  tools automatically — with no setup required."
- **Our assessment**: "No setup required" distinguishes computer use from MCP server
  configuration or connector setup, which require developer configuration. For Claude
  Code users, this means any desktop application is potentially accessible without
  writing a plugin — at the cost of reliability and speed. The claim is conditionally
  credible: the capability works without configuration, but "works" is qualified by
  the acknowledged limitations (slower, more error-prone than connectors).

### Claim 3: Three concrete safety safeguards gate computer use — permission before new app access, activation-level prompt-injection scanning, and a default app denylist

- **Evidence**: Post names all three: "Claude will always request permission before
  accessing new applications"; "our system will automatically scan activations within
  the model to detect for such activity" (re: prompt injection); "certain apps are
  off-limits by default." Users can stop Claude at any point.
- **Confidence**: emerging (design intent stated clearly; actual scanning
  implementation is opaque — no detail given on what "scan activations" means
  technically or what triggers a detection)
- **Quote**: "Claude will always request permission before accessing new applications";
  "our system will automatically scan activations within the model to detect for such
  activity"
- **Our assessment**: The three-safeguard model (consent gating, injection scanning,
  denylist) is the most important pattern in this post for practitioners designing
  their own computer-use or agentic-browser agents. These three layers form a
  minimum viable safety model:
  (1) Consent gating before new resource access — stops scope creep before it starts.
  (2) Activation-level injection scanning at the model level — catches prompt
  injection attempts that bypass system-prompt rules.
  (3) Default-deny sensitive apps — limits blast radius without per-request decisions.
  Any practitioner building computer-use or browser-control agents should implement
  all three, not just one or two. The denylist detail ("certain apps are off-limits
  by default") implies Anthropic has categorized app sensitivity — the specific list
  is not published, but the pattern (categorical app risk classification) is
  reproducible.

### Claim 4: Dispatch enables a single continuous conversation across phone and desktop — users assign tasks on mobile and collect results on desktop

- **Evidence**: Product description: "Dispatch lets you have one continuous
  conversation with Claude from your phone or your desktop." Example: "you can assign
  Claude a task on your phone, turn your attention to something else, then open up
  the finished work on your computer."
- **Confidence**: emerging (product claim for a research preview; continuity guarantees
  and failure behavior unstated)
- **Quote**: "Dispatch lets you have one continuous conversation with Claude from your
  phone or your desktop."
- **Our assessment**: Dispatch is the first officially documented async multi-device
  agent delegation pattern from Anthropic. The key properties: single conversation
  thread (not a copy), mobile-assignment + desktop-pickup, background execution while
  the user is not monitoring. This is the "fire-and-forget with trusted pickup" pattern.
  It formalizes what practitioners currently achieve with tmux + Slack bots + manual
  monitoring. The "one continuous conversation" framing implies session state is
  preserved across devices — not just output delivery, but the full interaction
  history. This matters for context: the agent's entire working thread is available
  at pickup, not just the final result.

### Claim 5: Dispatch enables routine automation workflows — morning email briefings, weekly metrics pulls, async PR workflows — as concrete daily use patterns

- **Evidence**: Three specific use case examples described: (1) "automatically check
  emails each morning and write a morning briefing while you commute"; (2) "pull your
  weekly metrics"; (3) "make changes to your IDE and submit a pull request."
- **Confidence**: anecdotal (illustrative examples from Anthropic; not practitioner
  reports with real usage data)
- **Quote**: "automatically check emails each morning and write a morning briefing
  while you commute"
- **Our assessment**: The three examples are canonical instances of high-ROI agentic
  automation: scheduled data pull (email briefing), periodic reporting (weekly
  metrics), and developer workflow automation (IDE changes + PR submission). The
  IDE-changes-and-PR example is particularly notable — it is the Claude Code core
  workflow (code generation + PR opening) wrapped in the async delegation model.
  Together these define the "ambient assistant" usage pattern: Claude running as a
  background process on recurring tasks, not an interactive session.

### Claim 6: Computer use is described as early, slower, and less reliable than direct integrations — Anthropic explicitly recommends limiting initial use to trusted apps and non-sensitive data

- **Evidence**: "Computer use is still early compared to Claude's ability to code or
  interact with text. Claude can make mistakes." Speed comparison: computer use is
  "slower than using a direct integration." Recommendations: "starting with the apps
  you trust and not working with sensitive data."
- **Confidence**: settled (Anthropic self-reporting a limitation explicitly and
  providing usage guidance)
- **Quote**: "Computer use is still early compared to Claude's ability to code or
  interact with text. Claude can make mistakes."
- **Our assessment**: This is a candid limitation statement from the vendor, which
  makes it more credible than typical product copy. The three-axis limitation is
  clear: accuracy ("can make mistakes"), speed ("slower than direct integration"),
  and maturity ("still early"). The "trusted apps, no sensitive data" recommendation
  is the practical deployment guide for practitioners adopting computer use today.
  This claim directly tempers the "no setup required" claim (Claim 2) — accessible
  but not production-grade. Practitioners should treat computer use as a prototyping
  and low-stakes automation tool, not a replacement for connector-based integrations
  in critical workflows.

### Claim 7: Computer use requires the desktop app to be "awake and running" — it is not a headless or serverless capability

- **Evidence**: Availability requirements: "Claude's desktop app must be awake and
  running." Platform support: macOS and Windows only (no Linux, no server).
- **Confidence**: settled (stated technical requirement)
- **Quote**: "Claude's desktop app must be awake and running"
- **Our assessment**: This constraint has significant architectural implications.
  Computer use is tethered to an active desktop session — it is not deployable as
  a headless server process, a CI/CD agent, or a cloud-hosted automation.
  Practitioners building computer-use workflows need an attended (or always-on)
  desktop machine as the execution environment. This distinguishes computer use
  from MCP server-based automation (which can run headlessly) and from API-based
  agents (which run anywhere). The Linux absence is also notable for server-side
  practitioners who default to Linux development environments.

## Concrete Artifacts

### Tool Hierarchy (Connector-First Graceful Degradation)

```
# Claude tool hierarchy for external service interaction
# Source: Anthropic, "Put Claude to work on your computer" (2026-03-23)

Level 1: Direct connectors (Slack, Google Calendar, etc.)
  - Precise, reliable, fast
  - Requires connector setup by developer/user
  - Preferred whenever available

Level 2: Computer use (browser, mouse, keyboard, screen)
  - Generic fallback when no connector exists
  - Requires: desktop app awake and running, macOS or Windows
  - Slower and less reliable than Level 1
  - No setup required beyond enabling in settings
  - Requires user permission before accessing each new application

# Design principle: "Claude will reach for the most precise tool first"
# Computer use is the last resort, not the first
```

### Computer Use Safety Model (Three-Layer)

```
# Minimum viable safety model for computer-use / agentic-browser agents
# Source: Anthropic, "Put Claude to work on your computer" (2026-03-23)

Layer 1: Permission gating
  - Claude requests explicit user permission before accessing any new application
  - Not opt-in globally; per-application consent is required
  - Users can stop Claude at any point

Layer 2: Activation-level prompt injection scanning
  - System scans model activations to detect prompt injection attempts
  - Operates at the model level, not just the input text level
  - Catches injections that would bypass system-prompt rules

Layer 3: Application denylist (default deny for sensitive apps)
  - Certain apps are "off-limits by default"
  - Categorical risk classification; specific list not published
  - Default deny forces explicit allowlisting for sensitive surfaces

# Usage guidance from Anthropic:
# "Starting with the apps you trust and not working with sensitive data"
```

### Dispatch Async-Delegation Workflow

```
# Dispatch multi-device async delegation pattern
# Source: Anthropic, "Put Claude to work on your computer" (2026-03-23)

PATTERN: Fire-and-forget with trusted pickup
  1. User assigns task on mobile (phone)
  2. Claude executes on desktop (background, while user is elsewhere)
  3. User picks up finished result on desktop (or phone)
  4. One continuous conversation thread preserved across devices

EXAMPLE WORKFLOWS:
  Scheduled briefing: "Automatically check emails each morning and write
                       a morning briefing while you commute"
  Periodic reporting: "Pull your weekly metrics"
  Dev workflow:       "Make changes to your IDE and submit a pull request"

REQUIREMENTS:
  - Desktop app must be awake and running
  - Claude Pro or Max subscription
  - macOS or Windows
  - Mobile app for task assignment phase
```

## Cross-References

- **Corroborates**:
  - **blog-ccunpacked-claude-code-architecture** (issue #22): The "Bridge" unreleased
    feature documented in the leaked source maps (remote control via mobile/browser,
    WebSocket + JWT auth, permission approval UI) is the plausible infrastructure
    layer under Dispatch's mobile-to-desktop delegation. Bridge's "permission approval
    UI" for remote tool calls maps directly to Claim 3's permission gating layer.
    Dispatch may represent a user-facing product built on top of Bridge's
    infrastructure. The ccunpacked note's prediction that Bridge would "change the
    human-in-the-loop model" is confirmed by Dispatch shipping a simplified version
    of that pattern for Pro/Max users.
  - **blog-addyosmani-code-agent-orchestra** (no issue): Osmani's Claim 6 (Ralph
    Loop — stateless-but-iterative cycle with context resets) describes async agent
    work from the *developer-orchestrating-agent* perspective. Dispatch describes it
    from the *user-delegating-to-agent* perspective. Both formalize the fire-and-forget
    + pickup pattern for non-interactive agent workflows. Osmani's daily task file
    pattern and Dispatch's morning briefing example are the same user story from
    different abstraction layers.

- **Contradicts**:
  - None. The Prospector confirmed no existing source notes cover computer use as an
    agentic capability or the Dispatch pattern.

- **Extends**:
  - **blog-anthropic-harness-long-running** (issue #173): That post establishes that
    harness components should be pruned as model capabilities improve. This post
    extends that principle to the *tool selection* layer: the connector-first hierarchy
    is itself a harness decision. When a connector exists, using it instead of computer
    use IS the harness pruning the slow/unreliable component in favor of the precise
    one. The "graceful degradation" framing extends the harness simplification principle
    downward to individual tool selection.
  - **blog-cursor-security-agents** (issue #161): Cursor's three-layer security model
    (shadow mode, canary pipeline, gradual trust rollout) for their security agents is
    a practitioner implementation of the same layered-consent philosophy that Anthropic
    encodes in the computer use safety model. This post provides the vendor-level
    version of what Cursor built from scratch.

- **Novel**:
  - **Connector-first → computer-use fallback hierarchy as a named principle**: No
    other source in the corpus names this tool-selection hierarchy explicitly. The
    principle "reach for the most precise tool first" is new.
  - **Dispatch as a released multi-device async delegation product**: ccunpacked.dev
    predicted Bridge (remote control infrastructure); Dispatch is the first confirmed,
    released implementation of cross-device agent delegation in the corpus.
  - **Three-layer computer use safety model**: The specific combination of permission
    gating + activation-level injection scanning + app denylist is new to the corpus.
    Activation-level scanning (not just input-text scanning) is a technically distinct
    claim that no other source documents.
  - **"Ambient assistant" daily workflow patterns**: The morning briefing, weekly
    metrics pull, and async PR workflow as first-party example patterns for Dispatch
    are new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "Tool Selection Hierarchy" section
  anchored by this source's connector-first → computer-use principle. The guide
  should teach practitioners to choose the integration type before writing any
  harness code: (1) Does an API connector exist? Use it. (2) Does an MCP server
  exist? Use it. (3) No integration available? Computer use is the fallback. This
  hierarchy should be explicit, not implicit, in any section covering how to connect
  agents to external services.

- **Chapter 02 (Harness Engineering)**: The Dispatch pattern is a concrete
  implementation of the "long-running async agent" workflow the harness chapter should
  cover. The fire-and-forget + pickup model (assign on mobile, collect on desktop)
  formalizes the async delegation use case. Practitioners building similar patterns
  outside the Anthropic product (e.g., with CI triggers, cron jobs, or webhook-driven
  agents) should model their UX on this: single conversation thread preserved,
  status available on pickup, user not blocked while agent runs.

- **Chapter 03 (Safety and Verification)**: Add the three-layer computer use safety
  model as the reference architecture for any agentic capability that touches user
  applications or browser sessions. The three layers — per-app consent, activation
  injection scanning, default app denylist — should be the minimum bar for
  practitioners building computer-use or browser-control agents. This is the first
  source in the corpus to document activation-level injection scanning as a production
  safeguard; the guide should highlight that input-text filtering alone is insufficient
  for computer-use threat models.

- **Chapter 01 (Daily Workflows)**: The Dispatch use cases (morning briefing, weekly
  metrics, async PR submission) are concrete daily workflow stories. The morning
  briefing example specifically (assign task during commute, pick up result at desk)
  is the clearest published description of the "ambient assistant" usage pattern for
  non-developer users of Claude. Add as a workflow story in the daily-workflows
  section, contrasting it with the interactive (synchronous) usage pattern.

## Extraction Notes

- The blog post is a product announcement for a research preview, not an engineering
  post with benchmarks or controlled comparisons. Claims about safety mechanisms are
  design intent, not independently verified behavior. The three-safeguard model is
  what Anthropic states they built — not what practitioners have stress-tested.
- "Activation-level prompt injection scanning" is an unusual technical claim. Standard
  injection defenses operate at the input-text or output-text level. "Scan activations
  within the model" suggests an internal representation-level scanner, which would be
  a novel defense mechanism. The post does not explain the technical implementation.
  This claim warrants a confidence downgrade from the default: we flag it as emerging
  because the mechanism is opaque, even though the claim comes from a first-party source.
- The specific app denylist was not published. Practitioners implementing their own
  denylist should look for Anthropic documentation on which app categories are
  considered high-risk (financial apps, credential managers, communication apps
  carrying sensitive data are likely candidates based on standard computer-use threat
  models).
- Two fetches of the URL were performed to ensure completeness. Both returned
  consistent content. The post is relatively short (~600 words) for a product
  announcement — it describes what the features do and the safety model without
  architecture depth. Deeper technical documentation (if it exists) would be in
  Anthropic's API/model documentation, not this blog post.
