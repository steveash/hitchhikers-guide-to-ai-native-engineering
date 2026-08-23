---
source_url: https://claude.com/blog/ai-ci-cd-on-call
source_type: blog-post
title: "Claude on call: How Claude Tag serves as Anthropic's first responder for CI/CD failures"
author: Sachin Malhotra (Anthropic Continuous Integration team), with contributions from Michael Segner
date_published: 2026-08-18
date_extracted: 2026-08-23
last_checked: 2026-08-23
status: current
confidence_overall: anecdotal
issue: "#2881"
---

# Claude on call: How Claude Tag serves as Anthropic's first responder for CI/CD failures

> First-person walkthrough by an Anthropic CI engineer of a production Claude
> Tag deployment that acts as the on-call first responder for CI/CD
> incidents: detection tuning, a dynamic-workflow triage architecture
> (orchestration agent + executor subagents across six connected systems), an
> auto-appending `lessons.md` incident log, feature-flag-gated automated
> resolution, and a separate "ci-weather" reporting agent — packaged as a
> public `anthropics/oncall-kit` starter repo.

## Source Context

- **Type**: blog-post (official claude.com/blog, published August 18, 2026;
  bylined to a single named engineer, not published as generic "Anthropic")
- **Author credibility**: Sachin Malhotra is described in the post's byline
  block as "An engineer on our Continuous Integration team" who "walks
  through the agent he built that powers CI incident response at Anthropic,"
  with contributions credited to Michael Segner, also Anthropic staff. This
  is first-hand practitioner testimony about a system the author personally
  built and operates, comparable in evidentiary weight to the Slack CPO
  account in `blog-anthropic-slack-cpo-human-agent-teams.md` — a single
  named individual's internal account, not an audited or third-party-verified
  case study. Concrete architecture and workflow descriptions are credible
  first-hand reporting; the quantitative claims (median triage latency, "8x"
  code-shipping figure, "hours not days" setup time) are self-reported
  internal metrics with no disclosed methodology, sample size, or
  measurement window.
- **Scope**: Covers one specific operational deployment of Claude Tag: the
  on-call setup's four architectural requirements, detection (new-service
  alert tuning and an alert-fatigue rubric), triage (a dynamic-workflow
  orchestration-agent/executor-subagent architecture wired to six systems via
  MCP Connectors, and the `lessons.md` incident log), resolution (a separate
  Claude Code agent managing feature-flag canary rollouts, plus PR-based
  fixes), verification/handoff (reusing investigation tooling to confirm
  fixes, a "ci-weather" reporting agent, and daily/weekly summaries), and a
  closing "8x more code per quarter" framing for why agentic CI is now
  necessary. Does NOT cover: the underlying model or classifier behind
  Claude Tag's decisioning (see `blog-anthropic-claude-tag-context-awareness.md`
  for that), pricing or plan tiers, false-positive/false-negative rates for
  triage decisions, prompt-injection or untrusted-input handling for alert
  payloads (contrast with `blog-cognition-auto-triage.md`, which addresses
  this directly for a comparable feature — see Cross-References), or any
  metrics beyond what the author states in prose (no linked dashboard, eval
  report, or incident count).

## Extracted Claims

### Claim 1: Claude Tag has been Anthropic's on-call first responder for CI/CD failures for several months, authoring the first situation report for every recent incident that had one, typically within 15 minutes
- **Evidence**: Author's own summary framing of the deployment's track record,
  stated before any of the architectural detail that follows.
- **Confidence**: emerging (specific, first-party operational claim from the
  system's builder; "every recent incident that had one" is a claim about
  completeness that is not independently auditable from the post itself)
- **Quote**: "For the last several months Claude Tag has been the on-call
  first responder for CI/CD failures at Anthropic. Not only has this helped
  with our social lives, it has given every CI incident an instant first
  responder: Claude authored the first situation report in every recent
  incident that had one, typically publishing its first analysis within 15
  minutes."
- **Our assessment**: This is the headline claim the rest of the post
  substantiates with mechanism. "Every recent incident that had one" is doing
  real scoping work — it implies some incidents don't get a SITREP at all
  (consistent with the deterministic-vs-agentic escalation split in Claim 7),
  not that Claude authors a report for literally every incident.

### Claim 2: An effective on-call agent requires four capabilities — memory, connections/access, schedules, and instructions
- **Evidence**: Explicit enumeration framing the rest of the post's structure,
  given before any implementation detail.
- **Confidence**: settled (a structural taxonomy stated directly by the
  system's builder, and one that the rest of the post visibly follows section
  by section)
- **Quote**: "An on-call agent needs memory so it remembers what's been done;
  connections and access so it can investigate, understand, and act;
  schedules so it knows when to get back to work; and instructions so it
  knows what to do."
- **Our assessment**: This four-part taxonomy is a compact, reusable checklist
  for anyone designing a similar standing operational agent — it maps
  directly onto the rest of the post's concrete implementations: memory →
  `lessons.md`, access → the service account, schedules → natural-language
  routine scheduling in the channel, instructions → the `oncall.md` skill
  file. It is a generalizable requirements list, not specific to CI/CD.

### Claim 3: Claude Tag operates through its own service account with access to tools like Datadog and Grafana, provisioned once by a channel administrator
- **Evidence**: Direct architectural description of the access model for this
  specific deployment.
- **Confidence**: settled (concrete, specific first-party description of a
  shipped configuration)
- **Quote**: "Claude Tag has its own service account and access to the tools
  an Anthropic CI engineer needs such as Datadog or Grafana. This was set up
  one time by an administrator for the channel."
- **Our assessment**: This is a direct operational instance of the
  channel-scoped service-account identity model already documented at the
  product-architecture level in `blog-anthropic-agent-identity-access-model.md`
  (Claim 5: Claude "has its own account in each system it touches"). This
  post shows that architecture applied to a specific, named use case
  (on-call), with named tools (Datadog, Grafana), rather than describing the
  identity model in the abstract.

### Claim 4: Standing instructions live in version-controlled markdown skill files in a GitHub repository, and the whole on-call setup took hours, not days, to stand up
- **Evidence**: Direct description of the configuration mechanism, followed
  immediately by a self-reported setup-time claim.
- **Confidence**: settled for the mechanism (skills-as-markdown-in-git is a
  concrete, verifiable configuration pattern); anecdotal for the "hours, not
  days" figure (self-reported, no baseline stated for what "days" would have
  looked like)
- **Quote**: "Standing instructions are in markdown files as skills, committed
  in a GitHub repository. This way multiple teammates can iterate on them and
  we can manage changes just like we do code... This setup took us hours, not
  days."
- **Our assessment**: Version-controlling the agent's operating instructions
  alongside code (rather than storing them in a UI-only config panel) is the
  same "standing instructions as skills, committed to Git" pattern documented
  at the product level in `blog-anthropic-agent-identity-access-model.md`
  Claim 7 (standing instructions as one of four admin-configurable identity
  components). This post gives no team size, headcount, or engineer-hours
  breakdown to substantiate "hours, not days" beyond the author's own
  characterization.

### Claim 5: Anthropic published a generalized "on-call setup kit" on GitHub that converts a team's own incident history into triage playbooks and produces a read-only Claude presence in the incident channel
- **Evidence**: Direct description of a linked, public artifact
  (`github.com/anthropics/oncall-kit`), distinct from Anthropic's own
  internal deployment.
- **Confidence**: settled (the repository is a real, publicly accessible
  artifact — verified reachable at the time of extraction — independent of
  whether its claimed behavior has been independently validated by a third
  party)
- **Quote**: "We created a generalized on-call setup kit in GitHub that can
  help get you started with a similar agent. It transforms your team's own
  incident history into triage playbooks and leaves you with a read-only
  Claude in your incident channel that diagnoses, escalates, and learns."
- **Our assessment**: This is the most directly actionable artifact in the
  post for a reader trying to replicate the setup — a public starter kit
  rather than only a narrative description. The post links to specific paths
  inside the repo (`templates/ONCALL.md`, `test-fixtures/RUNBOOK.md`,
  `skills/triage/`), which corroborates that the kit's structure mirrors the
  `oncall.md`/skills architecture described narratively elsewhere in the
  post (Claims 4, 7, 9-10). "Read-only" is a notable scoping detail: the
  starter kit is explicitly positioned as diagnose/escalate/learn only, not
  as shipping with the automated-resolution capabilities (feature-flag
  management, PR authorship) the author built for Anthropic's own deployment
  (Claims 13-14).

### Claim 6: Claude analyzes a new service's incoming data and alerts during its first few days in production to suggest additional alert rules and tune existing ones
- **Evidence**: Direct description of one of "two major failure modes for
  detecting incidents" that Claude Tag addresses, framed as a fix for the
  difficulty of setting perfect static thresholds without traffic-pattern
  data.
- **Confidence**: settled (specific first-party description of a shipped
  practice within this deployment)
- **Quote**: "To address this, we have Claude analyze the data and incoming
  alerts for the first few days of a new service to suggest additional rules
  and to fine-tune any that are overly broad or narrow."
- **Our assessment**: This is a concrete instance of using an agent to
  bootstrap monitoring configuration for a system with no historical
  baseline — a genuinely different task from Claude *responding* to alerts;
  here Claude is tuning the alerting system itself during a cold-start
  window. No specifics are given on how many rules were suggested, accepted,
  or reverted.

### Claim 7: Alert fatigue is addressed by having Claude apply a written, threshold-based rubric from `oncall.md` to every alert, deciding whether to page immediately or log it for the morning
- **Evidence**: Direct description with a concrete example rule quoted from
  the author's own configuration file.
- **Confidence**: settled (specific first-party description with a concrete,
  reproducible example rule)
- **Quote**: "Claude monitors every relevant alert in each alert channel and
  goes through the criteria in the root oncall.md file to determine if it can
  wait until the morning or if the on-call needs a page. For example, once
  tuned from analyzing the data, a rule in the file could be, 'If the error
  rate is greater than 2% for longer than 5 minutes AND it's not a known
  deploy window, page the on-call otherwise write it to lessons.md.'"
- **Quote** (deterministic/agentic split): "The key takeaway here is that the
  alerting process is deterministic, while on-call escalation has both
  deterministic and agentic paths."
- **Our assessment**: The example rule is a directly copyable template
  structure (metric threshold + duration + contextual exception → page or
  log), and the deterministic/agentic distinction is a useful framing for
  harness design: some escalation logic stays as a hard, auditable
  if-then rule (the example given), while other paths route through Claude's
  judgment (Claim 6's rule-tuning, and the two non-alert incident-open paths
  named later in the post — a team member reporting in-channel, or anyone
  opening an incident via an internal page).

### Claim 8: Claude posts its first evidence-grounded triage analysis a median of 14 minutes after an incident opens, and in the fastest observed cases names the root cause within 4 minutes
- **Evidence**: Specific, named latency figures presented as the payoff of
  the investigation architecture described next (Claim 9).
- **Confidence**: emerging (specific quantitative claims, but self-reported
  with no disclosed sample size, incident count, or measurement window —
  "median" implies some measured population, but that population is not
  described)
- **Quote**: "Claude posts its first evidence-grounded analysis a median of
  14 minutes after an incident opens, and in the fastest cases names the root
  cause within 4 minutes in its first report."
- **Our assessment**: These are the sharpest quantified performance figures
  in the post. Absent a stated sample size or time window, they should be
  treated as directional evidence of fast first-response, not a benchmark a
  reader could reproduce or audit — consistent with how this corpus treats
  other unsourced first-party percentage/latency claims (e.g., the ~30%
  proactivity-improvement figure in `blog-anthropic-claude-tag-context-awareness.md`
  Claim 1).

### Claim 9: When an alert escalates to an incident, Claude Tag starts a dynamic workflow in which an orchestration agent spins up executor subagents to investigate each of six connected systems in parallel, reducing MTTR
- **Evidence**: Direct architectural description naming the specific systems
  and the connection mechanism (MCP Connectors).
- **Confidence**: settled (specific, named architecture with an enumerated
  list of connected systems)
- **Quote**: "Claude Tag kicks off a dynamic workflow with an orchestration
  agent that spins up executor subagents to investigate each dependency and
  source of truth. For us that's Grafana, our log store, PagerDuty, GitHub,
  Kubernetes and Slack incident channels–all wired up via MCP Connectors.
  Claude can chase multiple leads in parallel, helping to reduce MTTR (mean
  time to resolution)."
- **Quote** (synthesis step): "Executors report the findings back to the
  orchestration agent which synthesizes and surfaces the information in a
  coherent SITREP."
- **Our assessment**: This is a direct, named instance of the
  orchestrator-subagent coordination pattern already documented as
  Anthropic's own recommended default in
  `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 7), and it is
  also the first corpus source to show Claude Code's "dynamic workflows"
  feature (`blog-anthropic-dynamic-workflows-claude-code.md`) — orchestration
  scripts Claude writes for itself, executing tens to hundreds of parallel
  subagents — applied specifically to incident triage rather than to code
  migration (that note's only prior corpus example was the Bun Zig-to-Rust
  rewrite). Six named systems as parallel investigation targets is a
  concrete scale reference for a production orchestrator-subagent
  deployment. Note the shared structural risk named in the coordination
  patterns note (Claim 3): orchestrator-subagent's core failure mode is an
  information bottleneck when a subagent surfaces a cross-cutting insight
  the orchestrator can't efficiently route — this post does not address
  whether or how that failure mode has shown up in the on-call deployment.

### Claim 10: Executor subagents are guided by "investigation skills" — detailed reference markdown files per bug class — exemplified by a 617-line shadow-divergence investigation skill the author built by having Claude turn a real troubleshooting session into a reusable file
- **Evidence**: Concrete named artifact (line count, bug class, authorship
  method) distinct from the general "investigation skill" framing.
- **Confidence**: anecdotal (a single, specific, self-reported artifact —
  its length and effectiveness are not independently verifiable from the
  post, and no other bug-class skill is given comparable detail)
- **Quote**: "They are guided by an investigation skill with more detailed
  reference markdown files for each bug class... For example, a 617 line
  investigation skill for shadow divergence bugs encodes every step I take
  during a typical investigation. I built it by troubleshooting with Claude
  turn-by-turn during one of the incidents and then had it create the file
  from that experience."
- **Our assessment**: The authoring method described — work through a real
  incident turn-by-turn with Claude, then have Claude distill that session
  into a standing reference skill — is a concrete, reusable technique for
  building investigation playbooks from lived experience rather than writing
  them from scratch, distinct from (and a specific implementation of) the
  general "promote a repeated pattern into a skill" mechanism named in Claim
  11 below.

### Claim 11: `lessons.md` is a running, auto-appended log of every resolved incident (root cause, fix, and a memorable gotcha) that every new investigation reads first, and recurring patterns get promoted into investigation skills
- **Evidence**: Direct description of the memory mechanism, plus a specific
  self-deprecating personal anecdote about an entry Claude wrote referencing
  the author's own mistake.
- **Confidence**: settled for the mechanism description; anecdotal for the
  specific personal example (a single self-reported entry, offered as
  illustration)
- **Quote**: "This markdown file is a running log of every incident we've
  resolved: what happened, the root cause, the fix, and the gotcha worth
  remembering. Claude appends to it on its own automatically. Every new
  investigation starts by reading it, so Claude's first hypothesis starts
  with what has happened recently."
- **Quote** (promotion mechanism): "If the same pattern shows up enough
  times, we promote it into the investigation skill itself."
- **Quote** (personal example): "My favorite entry is one Claude wrote about
  me. I'd made an assumption from a config file before checking the metrics,
  and the lessons.md file now states, 'query the data first, then theorize.
  Config tells you what could go wrong; metrics tell you what did.'"
- **Our assessment**: The two-tier memory architecture — a flat, ever-growing
  incident log that gets read first, with recurring entries later "promoted"
  into a curated investigation skill — is a specific, implementable pattern
  distinct from a single undifferentiated memory file: it separates
  "everything that happened" from "the subset worth encoding as a standing
  procedure." The self-deprecating example is a genuinely concrete
  illustration of self-updating memory closing a loop on a specific human
  mistake, not just a generic claim that "Claude learns."

### Claim 12: Claude Tag lets humans and Claude troubleshoot incidents together in real time, with either party able to steer the investigation or add a hypothesis
- **Evidence**: Direct statement following the description of the
  investigation-skill/lessons.md tooling, framed as a caveat that Claude
  "doesn't always get it right the first time."
- **Confidence**: settled (specific, first-party description of a shipped
  collaboration capability, consistent with Claude Tag's channel-based
  design documented elsewhere in the corpus)
- **Quote**: "Even with these tools and context, Claude doesn't always get it
  right the first time. Human intuition and experience matter. Claude Tag
  allows the team to troubleshoot incidents in multi-player mode. Either of
  us can steer the investigation or add a hypothesis in real-time, together."
- **Our assessment**: This is a direct, incident-response-specific instance
  of the "multiplayer" framing already documented generally in
  `blog-anthropic-human-agent-teams.md` (Claim 1: "teams of humans setting
  the strategy, and Claude executing the work") — here applied narrowly to
  co-investigating a live incident, with an explicit acknowledgment that
  Claude's investigations are not always correct on the first pass, which
  the author frames as the reason human steering remains part of the loop
  rather than a residual gap to be engineered away.

### Claim 13: Progressive, feature-flag-gated deployment is managed by a separate Claude Code agent, running under the author's own permissions, that handles canary traffic and automatically ramps flags up or down
- **Evidence**: Direct first-person description of a second, distinct agent
  (not Claude Tag) built specifically for the resolution/rollout stage.
- **Confidence**: anecdotal (a single engineer's personally built and
  permissioned agent, not described as a team-wide or company-wide standard
  configuration)
- **Quote**: "Most deployments within our team happen behind a feature flag.
  I have created a separate agent in Claude Code, with my permissions,
  capable of progressive deployment behind each of these feature flags. The
  first stage of our rollout process usually involves Claude managing canary
  traffic, monitoring for issues, and automatically ramping a given feature
  flag up or down."
- **Our assessment**: This is architecturally distinct from Claude Tag itself
  — it is a Claude Code agent, running under the author's personal
  credentials rather than a channel service account, dedicated specifically
  to deployment mechanics. The post explicitly declines to go deeper ("this
  could be an entirely separate article"), so this claim should be treated
  as an existence claim for the pattern (a dedicated canary/flag-ramping
  agent with human-owner permissions) rather than a detailed architecture
  description.

### Claim 14: Beyond direct fixes, Claude Tag's most frequent resolution path is opening a PR for the on-call engineer to review, merge, and deploy; it also gives Kubernetes drain/cordon guidance and infrastructure-scaling instructions during demand surges
- **Evidence**: Enumerated list of resolution paths, with the PR path
  explicitly marked as most common.
- **Confidence**: emerging (specific first-party enumeration; "most
  frequently" is a relative-frequency claim with no counts given)
- **Quote**: "Other resolution paths that Claude Tag helps my team with are:
  Letting us know if we need to drain or cordon off certain sections of our
  Kubernetes cluster;. Giving us instructions on how to scale up some of our
  infrastructure in responses to demand-surges (this is rare but it's very
  helpful when Claude comes back with exactly what we can do for
  mitigation); and, most frequently, Fixes in the form of a PR that the
  on-call can review, merge, and then deploy for a swift resolution."
- **Our assessment**: This keeps a human decisively in the loop for the
  highest-stakes resolution actions (Kubernetes cluster changes, PR
  merge/deploy) — Claude proposes, a human executes — in contrast to the
  fully automated canary-ramping described in Claim 13. The parenthetical
  "this is rare but it's very helpful" for the scaling-instructions path is
  a useful honest qualifier the author volunteers rather than folding into
  an inflated "Claude handles infrastructure scaling" claim.

### Claim 15: Verification reuses the same investigation tooling to confirm a fix worked; a separate "ci-weather" agent compiles per-incident, build, merge-queue, and deploy-lag data into a newsroom-style report for a public company-wide channel, and the report format required several iterations because readability is a matter of team-specific taste, not a solved technical problem
- **Evidence**: Direct description of the verification mechanism and a
  distinct downstream reporting agent, plus an explicit self-critical note
  about the report format's development.
- **Confidence**: settled for the mechanism description; anecdotal for the
  "several iterations" claim (no count or timeline given)
- **Quote**: "Claude uses many of the same MCP Connectors and tools that it
  did for its investigation to verify the fix worked as intended... To
  communicate the full picture across multiple incidents, we created an
  agent called ci-weather. It compiles information from each incident Slack
  channel, build metrics, merge queue stats, and deploy lag. Then it posts a
  newsroom-style report to one public channel anyone in the company can
  read."
- **Quote** (honest caveat): "One honest note: we needed to iterate the
  report format several times. Claude can one-shot a skill that generates a
  status report, but what makes it readable is team-specific taste. It's
  human communication, not plumbing."
- **Our assessment**: The "one-shot the mechanics, iterate the taste" caveat
  is a specific, transferable lesson distinct from the rest of the post's
  mostly-successful framing: generating a *correct* report is a one-shot
  skill-authoring task, but generating a *readable* one required repeated
  human tuning because readability is a team-specific communication
  judgment, not a fact the agent can look up. This corroborates, from a
  reporting-artifact angle, the broader "felt not mandated" and
  human-communication-taste themes already documented in
  `blog-anthropic-slack-cpo-human-agent-teams.md`.

### Claim 16: Anthropic's software engineers now ship roughly 8x as much code per quarter as during 2021-2025 while holding the same quality bar (named PR owner, required approval, same CI gates); the author frames this as the reason agentic CI is now necessary to match agentic coding
- **Evidence**: Closing framing claim, presented as the article's thesis for
  why this system exists at all.
- **Confidence**: emerging (specific quantitative claim — "8x," a five-year
  baseline window — stated without methodology, measurement definition, or
  citation to an internal dashboard)
- **Quote**: "Our software engineers on average ship 8x as much code per
  quarter as they did from 2021 to 2025. And while we have kept the quality
  bar high (every PR has a named human owner, every change requires approval
  to merge, every change goes through the same set of CI gates), the only
  way to keep up with agentic coding is agentic CI."
- **Our assessment**: This is the article's causal thesis: rising
  AI-accelerated code-shipping volume is what necessitates an AI-accelerated
  incident-response system, not incident response as an isolated
  improvement. The three named quality-bar controls (named owner, required
  approval, same CI gates) are a concrete, specific claim that automation
  hasn't relaxed governance even as volume rose — worth preserving distinctly
  from the "8x" headline figure, since a reader could otherwise assume
  higher output implies looser review.

## Concrete Artifacts

### On-call agent requirements taxonomy (verbatim)
```
Source: claude.com/blog/ai-ci-cd-on-call, Aug 18, 2026

"An on-call agent needs memory so it remembers what's been done;
connections and access so it can investigate, understand, and act;
schedules so it knows when to get back to work; and instructions so
it knows what to do."

Mapped onto this deployment:
  memory        -> lessons.md (auto-appended incident log)
  access        -> Claude Tag service account (Datadog, Grafana, etc.)
  schedules      -> natural-language routine scheduling in-channel
                    (example given elsewhere in the post: "run CI handoff
                    every Monday at 9:00am EST")
  instructions   -> oncall.md + skills, committed to a GitHub repo
```

### Example alert-fatigue rubric rule (verbatim)
```
Source: claude.com/blog/ai-ci-cd-on-call, Aug 18, 2026, "Detection" section

"If the error rate is greater than 2% for longer than 5 minutes AND
it's not a known deploy window, page the on-call otherwise write it
to lessons.md."

File: root oncall.md
Applied to: every relevant alert in each alert channel
```

### Triage architecture: dynamic workflow, orchestration agent, executor subagents
```
Source: claude.com/blog/ai-ci-cd-on-call, Aug 18, 2026, "Triage" section

Trigger: alert escalates to an incident
Mechanism: Claude Tag kicks off a "dynamic workflow" with an
  orchestration agent that spins up executor subagents

Six connected investigation targets (all via MCP Connectors):
  1. Grafana
  2. Log store
  3. PagerDuty
  4. GitHub
  5. Kubernetes
  6. Slack incident channels

Flow: executors investigate in parallel -> report findings to the
  orchestration agent -> orchestration agent synthesizes into a
  coherent SITREP

Guidance for executors: "investigation skills" -- per-bug-class
  reference markdown files. Named example: a 617-line shadow
  divergence investigation skill, authored by having Claude convert a
  real turn-by-turn troubleshooting session into a reusable file.

Stated benefit: "Claude can chase multiple leads in parallel, helping
  to reduce MTTR (mean time to resolution)."
```

### lessons.md memory loop
```
Source: claude.com/blog/ai-ci-cd-on-call, Aug 18, 2026, "Triage" section

Content per entry: what happened, root cause, fix, "gotcha worth
  remembering"
Write path: Claude appends automatically
Read path: every new investigation starts by reading it
Promotion rule: patterns repeated "enough times" get promoted from
  lessons.md into a standing investigation skill

Example entry (verbatim, quoted by the author):
  "query the data first, then theorize. Config tells you what could
  go wrong; metrics tell you what did."
```

### Public starter kit
```
Source: claude.com/blog/ai-ci-cd-on-call, Aug 18, 2026

Repository: https://github.com/anthropics/oncall-kit (verified
  reachable at extraction time, 2026-08-23)
Linked paths cited in the post:
  - templates/ONCALL.md
  - test-fixtures/RUNBOOK.md
  - skills/triage/
Stated function: "transforms your team's own incident history into
  triage playbooks and leaves you with a read-only Claude in your
  incident channel that diagnoses, escalates, and learns."
Scope note: explicitly "read-only" -- diagnose/escalate/learn only,
  not the automated feature-flag/PR resolution capabilities described
  for Anthropic's own internal deployment (Claims 13-14 above).
```

### "How to get started" checklist (verbatim)
```
Source: claude.com/blog/ai-ci-cd-on-call, Aug 18, 2026

"You'll need a Claude Team or Claude Enterprise plan
The organization owner needs to add Claude to the on call Slack
channel via Claude Tag
The org owner also needs to help connect Claude in the on-call Slack
channel to the appropriate connectors, GitHub repo, and set up Claude
Code Remote.
Add Claude to your incident channel and instruct it to monitor for
incidents and immediately triage"
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-agent-identity-access-model.md` (Claim 5 — Claude
    "has its own account in each system it touches," e.g. posting in Slack
    as the Claude app, opening PRs as the Claude GitHub App): Claim 3 here is
    a direct operational instance of that architecture, naming the specific
    tools (Datadog, Grafana) provisioned to a single channel's service
    account for the on-call use case.
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 7 — Anthropic
    recommends orchestrator-subagent as the default multi-agent coordination
    pattern): Claim 9 here is a named, production instance of exactly that
    pattern — an orchestration agent plus executor subagents — applied to
    incident triage, with a concrete count (six connected systems) and a
    named benefit (parallel investigation reducing MTTR).
  - `blog-anthropic-human-agent-teams.md` (Claim 1 — "teams of humans setting
    the strategy, and Claude executing the work," the single-player-to-
    multiplayer framing; Claim 9 — trust built by granting autonomy
    proportional to demonstrated reliability): Claim 12 here ("Either of us
    can steer the investigation or add a hypothesis in real-time, together")
    is a specific incident-response instance of that multiplayer framing, and
    the split between fully-automated canary ramping (Claim 13, high trust)
    versus PR-based human-approved fixes (Claim 14, lower trust for
    higher-stakes changes) mirrors that note's trust-proportional-autonomy
    model concretely, without the post naming it as such.
  - `blog-cognition-auto-triage.md` (Claim 3 — Devin's Auto-Triage "spins up
    parallel sub-Devins to investigate simultaneously"; Claim 4 — Devin
    routes outcomes by confidence: summary, human-owner tag, or PR; Claims
    6-7 — Devin builds long-running memory across investigations to
    deduplicate incidents and learn routing conventions): this is an
    independent vendor (Cognition/Devin) building a structurally near-identical
    product — parallel-subagent investigation, confidence-routed outcomes
    (summary/tag-human/PR), and a persistent cross-incident memory — for the
    same problem (agentic incident triage). The convergence between two
    independent vendors on parallel-subagent investigation, PR-as-resolution,
    and persistent incident memory (Claims 9, 11, 14 here vs. Auto-Triage
    Claims 3, 4, 6-7) is corroborating evidence that this is becoming a
    settled architecture pattern for the problem, not one company's
    idiosyncratic design.

- **Contradicts**: None filed. See "Novel" below for one notable *omission*
  relative to `blog-cognition-auto-triage.md` — not a contradiction, since
  this post simply doesn't address the topic rather than asserting the
  opposite position.

- **Extends**:
  - `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 2 — dynamic
    workflows let Claude "dynamically write orchestration scripts" rather
    than following a user-defined coordination graph; Claim 4 — three primary
    use cases named at launch: codebase-wide bug hunts/security audits, large
    migrations, and critical work needing independent verification): that
    post's only concrete example was a code-migration case study (the Bun
    Zig-to-Rust rewrite). Claim 9 here is the first corpus source to show
    dynamic workflows applied to a different domain entirely — live incident
    triage — extending the use-case evidence beyond migrations to
    operational/on-call automation, a use case that post's own "three primary
    use cases" list did not explicitly name.
  - `blog-anthropic-slack-cpo-human-agent-teams.md` (Claim 3 — the "handoff
    cycle": agents do production work, a human reviews/decides, then hands
    work back; Claim 6 — activity metrics like token usage don't prove
    value): Claim 14 here (PR-based fixes as the most frequent resolution
    path, requiring human review/merge/deploy) is a concrete CI/CD-specific
    instance of that handoff cycle. Claim 15's "one-shot the mechanics,
    iterate the taste" caveat about the ci-weather report format is a second,
    independent illustration of that note's broader point that agent output
    quality for human-facing communication is a matter of taste requiring
    iteration, not a solved technical problem — extending that claim from
    general team communication to a specific reporting-agent artifact.
  - `blog-anthropic-claude-tag-context-awareness.md` (Claim 3 — Claude Tag
    chooses among four response modes including "route the message to work
    it has in flight, when it adds to a workstream Claude already has open"):
    this post doesn't discuss the response-mode mechanism directly, but Claim
    1 here (Claude authoring "the first situation report in every recent
    incident that had one") is a concrete outcome of that underlying
    proactivity architecture applied to the on-call channel specifically.

- **Novel**:
  - **A named, six-system orchestrator-subagent architecture for incident
    triage** (Claim 9) — the specific enumeration (Grafana, log store,
    PagerDuty, GitHub, Kubernetes, Slack incident channels) as parallel
    investigation targets via MCP Connectors is new to the corpus.
  - **The two-tier `lessons.md` → investigation-skill memory promotion
    mechanism** (Claim 11) — a flat, auto-appended incident log that gets
    read first, with recurring patterns manually promoted into a curated,
    reusable investigation skill, is a specific memory architecture not
    previously documented in the corpus.
  - **The "turn a real troubleshooting session into a skill" authoring
    method** (Claim 10) — building an investigation-skill reference file by
    working an actual incident turn-by-turn with Claude and then having
    Claude distill that session into a standing document is a concrete,
    reusable skill-authoring technique new to the corpus.
  - **A public, reusable starter kit** (`anthropics/oncall-kit`, Claim 5) —
    the first corpus source pointing to a shipped, public repository a reader
    could directly clone and adapt, rather than only a narrative description
    of an internal-only system.
  - **Notable omission, not a contradiction**: unlike `blog-cognition-auto-triage.md`
    (Claim 8), which explicitly states its comparable feature "treats alert
    payloads, Slack messages, tickets, logs, and webhooks as untrusted input"
    and runs in a network-sandboxed environment specifically to guard against
    prompt injection during automated triage, this post never discusses
    untrusted-input handling for the alert/log/ticket data Claude Tag
    ingests during triage, despite describing a comparably automated,
    tool-wielding triage agent. This is worth flagging for Ch06 (Security):
    a reader replicating this pattern should not assume the security posture
    described for Devin's Auto-Triage is present here — this source is
    silent on the question, not confirming or denying it.

## Guide Impact

- **Chapter 02 (Harness Engineering — Multi-Agent Architecture)**: Add this
  post's orchestrator-subagent triage deployment (Claim 9) as a concrete,
  named production example of the pattern already recommended as Anthropic's
  default in `blog-anthropic-multi-agent-coordination-patterns.md` — six
  connected systems investigated in parallel via MCP Connectors is a
  specific scale/topology reference practitioners can benchmark their own
  designs against. Add the `lessons.md` two-tier memory-promotion mechanism
  (Claim 11) as a concrete pattern for any standing operational agent that
  needs to accumulate and later curate experience across many bounded
  invocations.

- **Chapter 02 (Harness Engineering — Skill Authoring)**: Add the
  "troubleshoot a real incident turn-by-turn, then have Claude distill it
  into a skill" method (Claim 10) as a specific, actionable technique for
  building investigation/runbook skills from lived experience rather than
  writing them from a blank page.

- **Chapter 04 (Tools / CI-CD Integration)**: Add this post as the guide's
  first detailed worked example of an agent embedded in the on-call/incident-
  response loop specifically, including the deterministic-vs-agentic
  escalation split (Claim 7) and the public `anthropics/oncall-kit` starter
  repository (Claim 5) as a directly actionable starting point for readers.
  Note the kit's "read-only" scope explicitly — it ships the
  diagnose/escalate/learn capability, not the automated-resolution
  capabilities (feature-flag ramping, PR authorship) described for
  Anthropic's own internal deployment.

- **Chapter 06 (Security / Threat Model)**: Flag the gap identified in
  Cross-References → Novel: this post describes an agent that ingests alert
  payloads, logs, and Slack messages from multiple systems during automated
  triage but never addresses untrusted-input handling for that data, in
  contrast to `blog-cognition-auto-triage.md`'s explicit sandboxing and
  prompt-injection mitigations for a structurally similar feature. Any guide
  section recommending this pattern should pair it with the untrusted-input
  guidance from the Cognition source rather than assume it by default.

## Extraction Notes

- **Fetch method**: WebFetch's AI-summarized rendering of this page was cross-
  checked against the raw page HTML (fetched via `curl`, tags stripped to
  plain text) before any quote was finalized. Every `Quote` field above was
  verified character-for-character against that flat-text extraction, not
  reconstructed from the WebFetch summary — the summary and the flat-text
  extraction were consistent in substance but the flat-text version was used
  as the source of truth for exact wording, consistent with the practice
  used in `blog-simonwillison-cat-thariq-fireside-chat.md` and
  `blog-anthropic-claude-tag-context-awareness.md`.
- **Full source read**: The entire article was read in full (opening
  anecdote through the closing "How to get started" checklist and the
  author/contributor note). No linked sub-pages required following for the
  narrative content; the one external link followed for verification was the
  `anthropics/oncall-kit` GitHub repository (confirmed publicly reachable,
  HTTP 200, at extraction time), whose linked file paths
  (`templates/ONCALL.md`, `test-fixtures/RUNBOOK.md`, `skills/triage/`) are
  recorded in Concrete Artifacts as evidence the kit's structure but were not
  themselves fetched or extracted — nothing in this note is sourced from
  their contents.
- **Cross-references verified**: `blog-anthropic-agent-identity-access-model.md`,
  `blog-anthropic-multi-agent-coordination-patterns.md`,
  `blog-anthropic-human-agent-teams.md`,
  `blog-anthropic-slack-cpo-human-agent-teams.md`,
  `blog-anthropic-dynamic-workflows-claude-code.md`,
  `blog-anthropic-claude-tag-context-awareness.md`, and
  `blog-cognition-auto-triage.md` were each read in full (or, for the longest
  notes, checked claim-by-claim via heading search) before citing; every
  `Claim N` reference above was located and confirmed against that note's
  actual numbered claims, not guessed.
- **No contradiction filed**: The Cognition Auto-Triage comparison (see
  Cross-References → Novel) is an *omission* on this source's part, not a
  claim that opposes an existing source-note claim — this post simply never
  discusses untrusted-input handling one way or the other, so there is no
  material contradiction to file under MINER.md §4a.
- **Three duplicate Prospector triage comments**: The issue carries three
  separate triage comments with slightly different chapter groupings
  (Ch02/03/04/05/06 variously named across the three). This note's Guide
  Impact section synthesizes across all three rather than picking one; the
  shared thread across all three comments — concrete detection/triage/
  resolution mechanism detail for an operational Claude Tag deployment — is
  represented above in Chapters 02, 04, and 06.
- **Confidence rationale**: Overall confidence is set to `anecdotal` because
  every claim in this source rests on one named engineer's first-person
  account of a system he personally built, with no independent audit,
  third-party validation, or disclosed measurement methodology for any of
  the quantitative figures (15-minute/14-minute/4-minute latencies, "hours
  not days," "8x" code volume). Individual claims are marked `settled` where
  the underlying mechanism is a specific, verifiable architectural
  description (e.g., the six-system orchestrator-subagent wiring, the
  publicly reachable starter-kit repository) and `anecdotal` or `emerging`
  where the claim is a self-reported metric or a single illustrative
  example without a stated sample or baseline.
