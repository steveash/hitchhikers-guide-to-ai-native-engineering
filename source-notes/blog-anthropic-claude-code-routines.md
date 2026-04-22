---
source_url: https://claude.com/blog/introducing-routines-in-claude-code
source_type: blog-post
title: "Introducing Routines in Claude Code"
author: Anthropic
date_published: 2026-04-14
date_extracted: 2026-04-22
last_checked: 2026-04-22
status: current
confidence_overall: emerging
issue: "#315"
---

# Introducing Routines in Claude Code

> Official Anthropic product announcement introducing a managed cloud scheduling
> layer for Claude Code — three-axis taxonomy (scheduled / API-triggered /
> webhook-triggered) with concrete practitioner patterns, plan-based daily quotas,
> and the explicit claim that routines replace self-managed cron + MCP server
> infrastructure for background AI automation.

## Source Context

- **Type**: blog-post (official Anthropic claude.com blog, April 14 2026;
  product announcement for a feature in research preview)
- **Author credibility**: First-party Anthropic announcement. Maximum authority
  for what the feature is, how it works, and what use cases Anthropic intends
  it for. Research preview status limits practitioner corroboration — no
  independent engineering posts or production case studies accompany this
  announcement. Claims about behavior (session persistence per PR, event
  routing, integration with external tools) are vendor descriptions of a feature
  that practitioners cannot yet fully test at scale.
- **Scope**: Covers what routines are, the three execution models and their
  mechanics, six concrete use case patterns, plan-based availability and daily
  quotas, and the infrastructure problem they replace (self-managed cron + MCP
  servers). Does NOT cover: how to configure connector credentials, how auto mode
  interacts with routines, what happens when a routine fails mid-execution, cost
  per session beyond the daily quota model, or API authentication setup details.
  No code examples are present; this is a capability announcement, not a
  technical engineering post.

## Extracted Claims

### Claim 1: Routines eliminate the local-machine infrastructure requirement for scheduled AI automation

- **Evidence**: Explicit vendor claim with specific infrastructure list. The
  article states that "until now, teams managed cron jobs, infrastructure, and
  additional tooling like MCP servers themselves." Routines run "on Claude Code's
  web infrastructure," eliminating the need to keep a laptop running.
- **Confidence**: emerging (vendor claim; the specific infrastructure list —
  cron, webhooks, MCP servers — accurately names the components practitioners
  actually manage, which raises credibility above generic marketing)
- **Quote**: "until now, teams managed cron jobs, infrastructure, and additional
  tooling like MCP servers themselves"
- **Our assessment**: The infrastructure problem is real. `blog-ghaw-pelis-agent-
  factory-intro.md` documents how GitHub Next solved exactly this problem
  self-hosted: 183+ workflows on GitHub Actions as the scheduling layer, requiring
  ongoing maintenance of that YAML + cron infrastructure. Routines propose to
  eliminate that layer entirely by moving it to Anthropic's cloud. Whether the
  trade-off (less control, daily quotas) is worth the infrastructure savings
  depends on team scale and the need for customization. For small teams running
  fewer than 25 routines/day, the managed option is likely the right default.

### Claim 2: Three execution models form a complete taxonomy for background AI automation: scheduled, API-triggered, and webhook-triggered

- **Evidence**: First-party product taxonomy. The three models are described with
  distinct mechanics, trigger sources, and example use cases. The post presents
  them as covering the full space of background automation needs.
- **Confidence**: emerging (the taxonomy is Anthropic's framing; whether it
  covers the complete space is a design claim rather than a tested claim)
- **Quote**: "A routine is a Claude Code automation you configure once — including
  a prompt, repo, and connectors — and then run on a schedule, from an API call,
  or in response to an event."
- **Our assessment**: The three-axis taxonomy is clean and reusable beyond
  routines themselves. Scheduled = recurring, time-predictable work. API-triggered
  = event-driven from systems that can POST HTTP. Webhook-triggered = event-driven
  from GitHub. This covers the three canonical trigger patterns for background
  automation. The missing axis is human-triggered (a developer running a routine
  manually), which the article doesn't name explicitly but is implied by the API
  model (a developer can POST the endpoint themselves). For practitioners
  deciding which routine type to configure, this taxonomy is the correct
  first-cut decision tree.

### Claim 3: Scheduled routines operate on practitioner-configured cadences (hourly, nightly, weekly) without requiring local infrastructure

- **Evidence**: Feature description with a concrete example prompt. The example
  ("Every night at 2am: pull the top bug from Linear, attempt a fix, and open a
  draft PR") demonstrates the nightly cadence pattern with an end-to-end task.
- **Confidence**: emerging (first-party feature description; cadences are stated
  explicitly; example is specific enough to be believable as a real tested pattern)
- **Quote**: "Every night at 2am: pull the top bug from Linear, attempt a fix,
  and open a draft PR."
- **Our assessment**: The Linear → draft PR pattern is the canonical scheduled
  routine use case. It is the practitioner equivalent of a nightly build: a
  recurring task that humans would otherwise need to remember to start. The three
  cadences (hourly, nightly, weekly) cover most recurrence patterns. Hourly is
  the smallest granularity mentioned — sub-hourly automations are not supported
  by this model. The `blog-ghaw-pelis-agent-factory-intro.md` GHAW factory uses
  GitHub Actions cron for equivalent scheduling; routines propose to replace that
  with a simpler, Claude-native interface.

### Claim 4: API routines provide per-routine HTTP endpoints with per-routine auth tokens, enabling standard REST integration into any system that can send a POST request

- **Evidence**: Explicit feature description. Each routine "receives its own
  endpoint and authentication token." Developers POST messages and receive session
  URLs in response.
- **Confidence**: emerging (vendor feature description; endpoint + auth token per
  routine is standard API design; session URL response is specific and plausible
  as the implementation pattern)
- **Quote**: "Each routine receives its own endpoint and authentication token.
  Teams can integrate them into alerting systems, deployment hooks, and internal
  tools."
- **Our assessment**: The per-routine endpoint model is the right design for
  integrating AI automation into existing tooling. Any system that can make an
  HTTP POST can trigger a Claude Code session: alerting platforms (Datadog,
  PagerDuty), CD systems (GitHub Actions, Spinnaker), internal dashboards. The
  session URL response is the mechanism for tracking progress or retrieving
  results. The auth token means the endpoint is not publicly accessible —
  practitioners need to securely store and rotate tokens, which is the same
  credential management burden they have for any external API integration.
  Compared to the Managed Agents model (`blog-anthropic-claude-managed-agents.md`),
  API routines are simpler (no sandboxing, no checkpointing, just an endpoint)
  but more limited (scoped to Claude Code sessions, not arbitrary agent programs).

### Claim 5: Webhook routines create persistent sessions per PR that receive ongoing event updates (comments, CI failures) — not fire-and-forget

- **Evidence**: Feature description. Claude "creates new sessions per PR and
  processes updates like comments and CI failures." The example shows the routine
  filtering on PR scope ("PRs that touch the /auth-provider module") and posting
  updates to a shared channel (#auth-changes).
- **Confidence**: emerging (the persistent-session-per-PR model is architecturally
  significant; the claim is specific enough to be vendor-tested, but production
  behavior on edge cases — PR merge, force push, large PR volume — is undocumented)
- **Quote**: "Flag PRs that touch the /auth-provider module...summarized and posted
  to #auth-changes."
- **Our assessment**: The persistent-session model is the most architecturally
  interesting claim in the post. A fire-and-forget webhook (Claude reads the PR
  once, posts a comment, done) is straightforward. A persistent session that
  receives subsequent events (reviewer comments, CI result changes, new commits)
  requires the session to maintain state about what it has already done and
  respond to delta events. This is significantly more complex to implement
  correctly — and more powerful: a routine can track a PR through its entire
  lifecycle, not just react to the opening event. Whether the session is a
  single long-lived Claude context or a series of related context windows is not
  documented. For high-volume repos with many concurrent PRs, the per-PR session
  model could consume a significant share of the daily quota.

### Claim 6: The CLI `/schedule` command now creates scheduled routines on Anthropic's cloud infrastructure

- **Evidence**: Stated in the Prospector's triage (sourced from the article).
  The `/schedule` command, previously a local scheduling primitive, is now backed
  by cloud-hosted routines.
- **Confidence**: emerging (vendor claim; the association of an existing CLI
  command with the new infrastructure is specific and plausible)
- **Quote**: (from Prospector's triage comment, attributing to the article) "CLI
  `/schedule` commands are now backed by scheduled routines"
- **Our assessment**: This is a backwards-compatible evolution of an existing
  Claude Code primitive. Practitioners who already use `/schedule` get cloud
  hosting automatically (assuming web access is enabled on their plan). New
  practitioners have a CLI-native path to creating routines without needing to
  configure them through a web interface. The migration from "local `/schedule`"
  to "cloud-backed routine" is a significant infrastructure shift masquerading as
  a familiar command.

### Claim 7: Usage is constrained by plan-based daily quotas; extra usage draws from the same subscription pool as interactive sessions

- **Evidence**: Explicit plan-by-plan quota table (Pro=5/day, Max=15/day,
  Team/Enterprise=25/day). The article also states "Extra routines may be
  purchased beyond daily limits using extra usage credits."
- **Confidence**: settled (plan-tier quotas are explicitly stated as product
  limits; the credit-pool mechanism is stated; these are verifiable by users
  against their account)
- **Quote**: "Pro: 5 routines daily; Max: 15 routines daily; Team/Enterprise:
  25 routines daily. Additional routines may be purchased beyond daily limits
  using extra usage credits."
- **Our assessment**: The daily quota model has significant implications for
  production adoption. A team running 25 routines/day on Team/Enterprise fills
  the quota immediately with no headroom for burst. The webhook-per-PR model
  (Claim 5) could consume multiple quota units per PR if the session count is
  high. More importantly, "extra credits from subscription pool" means routine
  usage competes with interactive session usage — heavy routine days could
  deplete credits available for human developers. Teams need to budget routine
  usage against interactive usage, not treat them as separate pools. This
  constraint makes Routines more suitable for low-frequency, high-value automations
  than for high-frequency, low-stakes ones. The `blog-ghaw-pelis-agent-factory-
  status.md` GHAW factory runs 183+ workflows — that volume is not feasible
  under a 25/day quota without purchasing large additional credit pools.

### Claim 8: Routines are in research preview status as of April 2026

- **Evidence**: Stated in the article header ("research preview").
- **Confidence**: settled (research preview is a formal Anthropic status designation)
- **Quote**: "Claude Code now offers routines in research preview."
- **Our assessment**: Research preview means practitioners can use the feature but
  should not depend on API stability, quota structure, or exact behavior in
  production-critical systems. The `blog-anthropic-claude-managed-agents.md`
  note also covered research-preview features (multi-agent coordination, outcome
  mode) — in that case, research preview features were restricted behind access
  requests. Routines appear more broadly available (no access request mentioned)
  but are still subject to change. Any guide recommendation for routines should
  include the research-preview caveat.

### Claim 9: The six documented use case patterns cover backlog management, docs drift, deploy verification, alert triage, library porting, and bespoke PR review

- **Evidence**: All six are named in the article with brief descriptions.
  Backlog management and docs drift are scheduled patterns; deploy verification
  and alert triage are API-triggered; library porting and PR review are webhook-
  triggered (GitHub).
- **Confidence**: emerging (Anthropic-documented patterns; these are the patterns
  Anthropic chose to feature, implying they were tested or validated before
  announcement)
- **Quote**: "Every night at 2am: pull the top bug from Linear, attempt a fix,
  and open a draft PR." / "Read the alert payload, find the owning service, and
  post a triage summary to #oncall."
- **Our assessment**: The six patterns are the clearest signal of what Anthropic
  thinks routines are good for. They cluster around recurring maintenance tasks
  (backlog, docs drift), reactive operations tasks (alert triage, deploy
  verification), and code quality tasks (library porting, PR review). Notably
  absent from the patterns: data pipeline processing, customer communication,
  cross-system data sync. Whether routines are suitable for those use cases is
  not documented — practitioners exploring outside the six patterns should
  expect less Anthropic guidance on the behavior.

### Claim 10: The alert triage pattern (Datadog → routine endpoint → trace correlation + draft fix) enables pre-triage before on-call opens the page

- **Evidence**: Example described in the article: Datadog alert posts to the
  routine endpoint; Claude performs trace correlation and creates a draft fix
  before the on-call engineer responds.
- **Confidence**: anecdotal (the pattern is named; no production incident report
  corroborates it; trace correlation is a complex task that may vary in quality)
- **Quote**: "Read the alert payload, find the owning service, and post a triage
  summary to #oncall."
- **Our assessment**: This is the most operationally significant use case in the
  post and the hardest to implement correctly. Alert triage requires the routine
  to have access to logs, traces, and service ownership data — which means
  connectors to these systems must be configured. The "draft fix before on-call
  opens the page" claim implies the routine can both diagnose and propose a
  solution within the time between alert and human response. Whether Claude can
  reliably perform trace correlation on real production incidents (noisy signals,
  multi-service causality chains) at the quality level needed for pre-triage is
  an open question. The `blog-anthropic-claude-code-auto-mode.md` note's 17% FNR
  on overeager actions suggests model-based automation on high-stakes tasks
  (production incidents) still requires human verification before acting.

## Concrete Artifacts

### Three-Axis Routine Execution Taxonomy

```
Routines: Three-Axis Execution Taxonomy
(Anthropic, "Introducing Routines in Claude Code," April 14 2026)

SCHEDULED
  Cadence:       hourly / nightly / weekly (practitioner-configured)
  Trigger:       wall clock
  Infrastructure: Anthropic cloud (no local machine required)
  Example:       "Every night at 2am: pull the top bug from Linear, attempt a
                 fix, and open a draft PR."
  Use cases:     Backlog management, documentation drift detection

API-TRIGGERED
  Trigger:       HTTP POST to per-routine unique endpoint
  Auth:          per-routine auth token (stored and rotated by practitioner)
  Response:      session URL (for tracking / retrieval)
  Example:       "Read the alert payload, find the owning service, and post a
                 triage summary to #oncall."
  Use cases:     Deploy verification, alert triage (Datadog → endpoint),
                 feedback resolution, any HTTP-accessible event

WEBHOOK-TRIGGERED (currently: GitHub repository events only)
  Trigger:       GitHub repository event (PR open, comment, CI result)
  Scope filter:  practitioner-defined (e.g., "PRs touching /auth-provider")
  Session model: one persistent session per matching PR; receives ongoing
                 event updates (comments, CI failures) — not fire-and-forget
  Example:       "Flag PRs that touch the /auth-provider module...summarized
                 and posted to #auth-changes."
  Use cases:     Library porting across SDKs, bespoke PR code review checklists,
                 module-scoped change monitoring
```

### Plan Quotas and Credit Model

```
Routines: Daily Usage Limits
(Anthropic, "Introducing Routines in Claude Code," April 14 2026)

Plan              Routines/day   Extra usage source
----------------  -------------  ------------------------------------------
Pro               5              Subscription credit pool (shared with
Max               15             interactive sessions)
Team/Enterprise   25

Note: "Extra routines may be purchased beyond daily limits using extra
      usage credits" — credits shared with interactive session budget.
      High routine volume competes with developer interactive usage.
```

### Documented Use Case Patterns by Trigger Type

```
Routines: Practitioner Use Case Patterns
(Anthropic, "Introducing Routines in Claude Code," April 14 2026)

SCHEDULED (recurring maintenance):
  Backlog management:
    "Every night at 2am: pull the top bug from Linear, attempt a fix,
     and open a draft PR."
  Documentation drift:
    "Every week: scan merged PRs, flag docs referencing changed APIs."

API-TRIGGERED (reactive operations):
  Deploy verification:
    CD pipeline POST → Claude runs smoke checks → posts go/no-go signal
  Alert triage:
    Datadog alert → routine endpoint → trace correlation + draft fix
    before on-call opens the page
  Feedback resolution:
    Any external alert/event system that can POST HTTP

GITHUB WEBHOOK (code quality):
  Library porting:
    Merged Python SDK PR → routine ports change to Go SDK + opens
    matching PR
  Bespoke PR review:
    Run team checklist (security/performance criteria) before human
    reviewer — posts checklist results as PR comment
  Module monitoring:
    "Flag PRs that touch the /auth-provider module...summarized and
     posted to #auth-changes."
```

### Infrastructure Shift: Self-Hosted vs. Managed Scheduling

```
Background AI Automation: Infrastructure Comparison
(Based on: Anthropic routines announcement + GHAW factory pattern)

SELF-HOSTED (GHAW model):
  Scheduling:     GitHub Actions cron + workflow YAML
  Trigger layer:  GitHub webhook → Actions runner
  Execution env:  Self-managed runner (Linux VM / container)
  Scale:          Unlimited (bounded only by Actions runner capacity)
  Control:        Full (custom env, secrets, tool access)
  Maintenance:    Actions YAML, runner infra, token rotation

MANAGED (Anthropic Routines model):
  Scheduling:     Anthropic cloud (via /schedule CLI or web config)
  Trigger layer:  Per-routine HTTP endpoint or GitHub webhook integration
  Execution env:  Anthropic-managed (Claude Code web infrastructure)
  Scale:          5–25 routines/day (plan-gated) + purchased credits
  Control:        Limited (prompt + repo + connectors; no env customization)
  Maintenance:    Auth token rotation; connector credential management

Decision axis: control + unlimited scale (self-hosted) vs.
               low maintenance + fast setup (managed)
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agent-factory-status.md` and `blog-ghaw-pelis-agent-factory-intro.md`
    — The GitHub Agentic Workflows factory demonstrates what a mature self-hosted
    scheduling layer looks like at scale: 183+ workflows on defined cadences via
    GitHub Actions, covering the full SDLC. Routines are Anthropic's managed
    alternative to exactly this infrastructure. The GHAW factory uses GitHub Actions
    as the scheduling and trigger layer; routines eliminate that dependency by
    moving scheduling to Anthropic's cloud. Both sources address the same underlying
    problem (reliable background AI automation); they represent different points on
    the control/convenience spectrum.
  - `blog-anthropic-claude-managed-agents.md` — Managed Agents introduced
    Anthropic-hosted agent execution infrastructure (sandboxing, checkpointing,
    multi-agent coordination) as a platform service. Routines introduce a parallel
    and distinct managed infrastructure layer: the scheduling and trigger layer.
    Where Managed Agents handles *what happens inside* a long-running agent session,
    Routines handle *when and why a session starts*. Both represent Anthropic's
    expansion from tool (Claude Code) to managed infrastructure. They are
    complementary, not competing.

- **Extends**:
  - `blog-anthropic-claude-code-auto-mode.md` — Auto mode's two-stage permission
    classifier is a likely prerequisite for unattended routine execution. Without
    automated permission handling, routines that use shell commands (Tier 3 actions)
    would block awaiting human approval, defeating the "runs without you watching"
    property. This note does not document the auto mode dependency explicitly —
    that gap is a guide impact item. Auto mode's 17% FNR on real overeager actions
    applies to routine execution too: unattended runs have no human fallback when
    the classifier misses a dangerous action.
  - `blog-anthropic-harness-long-running.md` — That note documents the harness
    architecture inside a long-running agent session (generator/evaluator,
    sprint decomposition, context management). Routines operate at the layer above:
    they determine when sessions are initiated and how they are triggered. The
    combination of routines (scheduling/triggering layer) + a well-designed session
    harness (architectural layer) is the complete background automation stack.
    Routines do not replace harness engineering — they determine when the harness
    runs.
  - `blog-anthropic-multi-agent-coordination-patterns.md` — The message bus
    coordination pattern (agents subscribe to events and trigger on routing) is
    the manual implementation of what webhook routines automate. Routines make
    GitHub-event-triggered automation a first-class primitive; the multi-agent
    coordination patterns post describes the architectural patterns to use inside
    the sessions those events trigger.

- **Contradicts**: None found. The closest tension is with `docs-ghaw-agent-factory-
  status.md` on the scale question: the GHAW factory runs 183+ workflows under a
  self-hosted model that Routines' 25/day quota cannot match. This is not a
  contradiction — it is a conditioning variable (quota-constrained managed service
  vs. unlimited self-hosted) that the guide should document as a tradeoff.

- **Novel**:
  - **Three-axis execution taxonomy for background AI automation** (scheduled /
    API-triggered / webhook-triggered with persistent sessions): not documented in
    any prior corpus source. The GHAW factory uses scheduling and triggers but not
    under this taxonomy.
  - **Per-routine HTTP endpoint + auth token as a primitive**: the API routine
    endpoint model (each routine addressable via REST) is new to the corpus.
    No prior source describes AI automation sessions initiated by HTTP POST to a
    unique endpoint.
  - **Persistent webhook sessions per PR with ongoing event updates**: qualitatively
    different from fire-and-forget webhook patterns. No prior corpus source
    documents a Claude Code session that spans the lifecycle of a PR and receives
    multiple event updates.
  - **Plan-tier daily quota model for AI automation** (5/15/25 routines/day):
    first quota model for background automation in the corpus. Prior sources treat
    automation as unlimited (self-hosted) or session-cost-bounded (Agent SDK).
  - **Managed CLI scheduling (`/schedule` → cloud-hosted routine)**: CLI-native
    path to creating cloud-backed scheduled automations, replacing local cron +
    MCP server infrastructure. First in corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Scheduling infrastructure**: Add a
  "Managed vs. Self-Hosted Scheduling" subsection contrasting Routines (managed,
  quota-constrained, Anthropic cloud) with the GHAW factory model (self-hosted,
  unlimited, GitHub Actions). Decision axis: teams that need >25 automations/day
  or need full environment control should self-host (GHAW model); teams that
  want fast setup with no infrastructure maintenance should use Routines. Present
  both as valid answers to the same problem.

- **Chapter 01 (Daily Workflows)**: Add the three-axis taxonomy (scheduled /
  API-triggered / webhook-triggered) as the first-cut decision tree for "what
  background automation should I build?" The taxonomy applies beyond Routines —
  it is the right frame for classifying any recurring AI automation regardless
  of the infrastructure layer. Practitioners should classify their automation
  by trigger type before choosing an infrastructure model.

- **Chapter 02 (Harness Engineering) — Safety for unattended execution**: Routines
  require auto mode (or equivalent permission gating) for any session that uses
  Tier 3 actions (shell commands, web fetches, external tools). Without it,
  unattended sessions block on permission prompts with no human present. Add a
  note to the Routines/scheduling section: "Unattended sessions require automated
  permission handling. Use auto mode for Claude Code web sessions that execute
  shell commands or external tool calls. The auto mode 17% FNR on overeager
  actions applies to routine execution — design routines to operate on reversible
  actions (draft PRs, draft comments) rather than irreversible ones (force pushes,
  production deploys) where possible."

- **Chapter 05 (Team Adoption)**: The webhook routine model (one routine
  monitoring a module, posting to a shared Slack/GitHub channel) is a concrete
  team coordination primitive that requires no per-member configuration. Add the
  auth-changes channel pattern as an example of team-shared automation: one
  routine configured by one engineer provides PR monitoring to the entire team
  through shared notification channels.

- **Chapter 02 (Harness Engineering) — Quota planning**: The credit-pool sharing
  between routine usage and interactive session usage is a hidden cost constraint.
  Teams on Pro or Max plans should budget routine usage against interactive
  developer usage. Recommend establishing a routine budget (e.g., reserve 50%
  of daily quota for routines) and monitoring credit consumption to prevent
  routine usage from depleting interactive session availability.

## Extraction Notes

- The article is a research preview product announcement (April 14 2026) without
  code examples, API documentation, or engineering implementation details. The
  WebFetch of the source URL returned a summarized version rather than full
  verbatim article text. The Prospector's three triage comments in issue #315
  provided additional specific detail about article content, including quoted
  prompt examples and the `/schedule` CLI association. These were treated as
  supplementary sources of article detail for extraction.
- No contradiction with existing corpus notes was found that would require a
  separate contradiction issue. The scale limitation (25/day quota vs. GHAW
  factory's 183+ workflows) is a tradeoff, not a factual contradiction.
- `registry/sources.json` is empty (`{"sources": {}, "last_updated": null}`)
  and was left alone per instructions.
- Confidence is set to `emerging` rather than `settled`: Anthropic is authoritative
  on the feature specification, but research preview status means production
  behavior on edge cases (PR lifecycle events, high-volume webhook scenarios,
  routine failure handling) has not been publicly documented or independently
  tested. Individual claims are rated within the note based on their specific
  evidence quality.
- A follow-up extraction of the Routines configuration documentation (likely at
  platform.claude.com) would provide implementation-level detail missing here:
  connector configuration, credential management, auto mode dependency, and
  failure/retry behavior.
