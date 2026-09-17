---
source_url: https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform/
source_type: blog-post
title: "Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform"
author: Achuth Narayan Rajagopal (Senior Software Engineer, Google)
date_published: 2026-09-16
date_extracted: 2026-09-17
last_checked: 2026-09-17
status: current
confidence_overall: emerging
issue: "#3508"
---

# Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform

> Google's first-party announcement of a post-deployment, out-of-band behavioral
> monitoring layer for ADK agents: a two-tier statistical + LLM-reasoning
> detection pipeline that reads existing OpenTelemetry traces to flag policy
> violations mapped to named OWASP Agentic Top 10 (2026) categories, with zero
> added runtime latency and a programmatic API for threshold-based blocking.

## Source Context

- **Type**: blog-post (official Google Developers Blog, product announcement,
  published Sept 16, 2026)
- **Author credibility**: Achuth Narayan Rajagopal, a named Google Senior
  Software Engineer, writing about a Google-built feature (Agent Anomaly
  Detection) on the Gemini Enterprise Agent Platform. This is first-party vendor
  announcement content for a feature currently in **Private Preview** — there is
  no independent (non-Google) validation of detection accuracy, false-positive
  rates, or the "zero added runtime latency" claim in this source. The post is a
  feature announcement, not an implementation guide or technical deep-dive: it
  names the architecture and gives one worked example, but does not publish
  code, configuration schemas, or the detection models/prompts used internally.
- **Scope**: Covers what Agent Anomaly Detection is, its layered detection
  pipeline (statistical pass → LLM reasoning pass → optional deep
  reconstruction), the OWASP Agentic Top 10 categories it targets, one worked
  example (an inventory-scraping scenario), and the programmatic blocking API.
  Does NOT cover: internal detector implementation, pricing, latency/accuracy
  benchmarks, false-positive handling, how findings are stored or retained, or
  general availability timeline (feature is Private Preview only, requiring ADK
  1.2+).

## Extracted Claims

### Claim 1: As agents become more autonomous, their risk shifts from their code to their behavior, and damage-causing sessions can look clean enough to clear standard metrics-based evaluation without a second look
- **Evidence**: Opening framing/motivation for why the product exists, presented
  as the general problem statement rather than tied to a specific incident.
- **Confidence**: emerging (a plausible, widely-echoed framing in the corpus's
  agent-safety sources, but stated here as unsupported assertion, not backed by
  incident data in this source)
- **Quote**: "The more decisions an agent makes at runtime, the more its risk
  shifts from its code to its behavior. The real damage often happens in
  sessions that look benign on the surface: the agent returns a clean answer
  and closes the ticket, and only afterward do you notice it reached for a tool
  it should never have touched, or acted on a request that quietly widened its
  own access. Because nothing failed outright, the session clears the usual
  metrics-based evaluations without any second look."
- **Our assessment**: This is the clearest single-sentence articulation in the
  corpus of *why* success-rate/task-completion metrics are insufficient for
  agent safety monitoring: a session can be metrically "successful" (task
  completed, no error thrown) while still being a policy violation. It
  motivates behavioral/intent-level monitoring as a distinct layer from
  outcome-level evaluation, independent of whether Google's specific product
  implementation lives up to the framing.

### Claim 2: Agent Anomaly Detection is a reasoning-based oversight and audit layer that examines an agent's reasoning traces, tool calls, and execution flow across a full session, using the OpenTelemetry traces and logs the agent already emits
- **Evidence**: Direct product definition, stated as the core description of the
  feature.
- **Confidence**: emerging (first-party product description; the underlying
  mechanism — reading existing OTel traces/logs rather than requiring new
  instrumentation — is a specific, checkable architectural claim, but not
  independently verified here)
- **Quote**: "Agent Anomaly Detection is a reasoning-based oversight and audit
  layer for autonomous agents deployed on the Gemini Enterprise Agent Platform.
  It examines what an agent actually does using its reasoning traces, tool
  calls, and execution flow across a session. It reads the logs and
  OpenTelemetry traces your agents already emit, evaluates that activity to
  decide whether an agent is operating outside its intended boundaries, and
  flags behavioral anomalies, suspicious intent, and policy violations."
- **Our assessment**: The key design choice is that it consumes telemetry the
  agent *already* emits rather than requiring new instrumentation — this is
  what makes the "zero added runtime latency" and "no code changes" claims
  (Claim 3) architecturally plausible: the detector is a downstream consumer of
  existing OTel data, not a component in the live request path.

### Claim 3: Analysis runs asynchronously and out of band from the live request path, so it adds no latency to agent responses
- **Evidence**: Direct architectural claim, listed as the first of the feature's
  "key features."
- **Confidence**: emerging (architecturally plausible given Claim 2's
  telemetry-consumption design, but "zero added runtime latency" is a vendor
  claim with no published benchmark in this source)
- **Quote**: "No added runtime latency: The analysis runs asynchronously and out
  of band from the live request path, so it does not slow your agents'
  responses."
- **Our assessment**: This is the central production-viability claim of the
  whole feature — a security monitoring layer that requires zero latency
  tradeoff is unusually attractive compared to inline guardrails (e.g., the
  regex/heuristic gateway pattern in `blog-google-adk-zero-trust-agents.md`
  Claim 8, which runs inline before the model/database call). The tradeoff is
  temporal: out-of-band detection necessarily means the anomaly is caught
  *after* the tool call already executed, not before — this source does not
  claim to prevent the first occurrence of an anomalous action, only to detect
  and (via the API in Claim 8) block *subsequent* actions in the session.

### Claim 4: Every anomaly finding carries a severity level, a plain-language explanation of what triggered it, and recommended next steps, and is published to Security Command Center for triage
- **Evidence**: Direct feature description under "Clear, actionable findings."
- **Confidence**: emerging (product feature description; format not independently
  verified, but consistent with the worked example in Claim 6)
- **Quote**: "Clear, actionable findings: Every anomaly finding carries a
  severity, a plain-language explanation of what triggered it, and recommended
  next steps. Each anomaly finding is also published to your Security Command
  Center deployment, so your team can triage it alongside other findings."
- **Our assessment**: Routing findings into Security Command Center (Google
  Cloud's existing security posture/SIEM product) rather than a bespoke agent
  dashboard is a notable integration choice — it treats agent behavioral
  anomalies as first-class security findings alongside infrastructure and
  network security findings, rather than as a separate "AI observability"
  silo. This is the same "triage alongside other findings" philosophy as
  `blog-ghaw-agent-observability.md`'s Audit Workflows agent raising GitHub
  issues into the team's existing issue tracker rather than a separate system.

### Claim 5: Agent Anomaly Detection ships with detectors grounded in a named, specific subset of the OWASP Top 10 for Agentic Applications (2026) — tool misuse (ASI02), identity and privilege abuse (ASI03), cascading failures (ASI08), rogue agents (ASI10) — plus resource exhaustion and token usage escalation
- **Evidence**: Direct feature description under "Grounded in the OWASP Agentic
  Top 10," naming specific ASI-numbered categories and linking to the OWASP
  standard.
- **Confidence**: settled (a factual claim about which named taxonomy the
  product's detectors map to; the taxonomy itself, OWASP Top 10 for Agentic
  Applications 2026, is an external, independently-published standard, though
  this source does not describe how the mapping was validated)
- **Quote**: "Grounded in the OWASP Agentic Top 10: Agent Anomaly Detection
  ships with detectors for a focused set of risks from the OWASP Top 10 for
  Agentic Applications (2026): tool misuse (ASI02), identity and privilege
  abuse (ASI03), cascading failures (ASI08), and rogue agents (ASI10), plus
  operational risks like resource exhaustion and token usage escalation. Its
  findings map to these recognized industry categories rather than a bespoke
  set of rules."
- **Our assessment**: This is the first source in the corpus to name specific
  ASI-numbered categories from OWASP's Top 10 for Agentic Applications (2026).
  The existing corpus reference to OWASP (`blog-anthropic-zero-trust-ai-agents.md`
  Claim 5) cites OWASP only for the "least agency" term, not for a numbered
  risk taxonomy. Mapping detector output to an external, recognized taxonomy
  (rather than a vendor-specific rule ID scheme) is valuable for teams that
  need to report agent security findings in a vendor-neutral vocabulary — e.g.,
  for cross-vendor compliance reporting or when an org runs agents on more than
  one platform.

### Claim 6: A future capability, not yet available, will let users define enterprise-specific anomaly detectors in natural language combined with deterministic rules, and validate the accuracy of new custom rules against past traffic before enabling them
- **Evidence**: Direct statement under "Custom business logic in anomaly
  detections coming soon," describing planned (not shipped) functionality.
- **Confidence**: anecdotal (this is a stated future roadmap item, not a shipped
  feature — it should not be treated as currently available even though it is
  described in the same announcement as Private Preview features)
- **Quote**: "We are actively working on the ability for users to define what
  anomalies mean in the context of their business. This will enable users to
  write flexible anomaly detectors in natural language together with
  deterministic rules, which flag when agents operate beyond enterprise-specific
  business guidelines. In addition, users will be able to validate the accuracy
  of their new custom business logic on past traffic."
- **Our assessment**: The "validate against past traffic" capability is the
  interesting design detail — it implies Google retains enough historical
  session/trace data to backtest a new custom detector before enabling it live,
  which is the anomaly-detection equivalent of replaying traffic against a new
  filter rule before deploying it (the same principle behind the CI-tested
  gateway regression suite in `blog-google-adk-zero-trust-agents.md` Claim 9,
  applied to a natural-language rule instead of a regex/code rule). Because
  this is explicitly unreleased, guide text should flag it as directional, not
  actionable today.

### Claim 7: The detection pipeline balances speed, cost, and coverage by running in layers — a lightweight statistical first pass scans all traffic for outliers, then an LLM-based reasoning layer deeply examines only the flagged sessions
- **Evidence**: Direct architectural description under "Inside the detection
  pipeline."
- **Confidence**: emerging (architecturally sound tiered-triage design, a
  well-established pattern for balancing cost against coverage at scale, but no
  published figures on what fraction of sessions get escalated to the LLM tier
  or at what cost)
- **Quote**: "Agent Anomaly Detection balances detection speed, cost, and
  coverage. To strike that balance, it analyzes traces and logs in layers: a
  lightweight first pass scans all traffic to surface statistical anomalies and
  flag those sessions for further analysis. Then, an LLM-based reasoning layer
  deeply examines the flagged sessions."
- **Our assessment**: This two-tier design (cheap statistical filter → expensive
  LLM reasoning only on flagged subset) is the same "lightweight first pass,
  deep pass on outliers" shape as `blog-cursor-continual-harness-improvement.md`
  Claim 6's per-tool per-model anomaly baselines, but applied to a different
  target: Cursor's baselines detect *tool-call error rate* deviations (a
  reliability signal), while this pipeline's statistical layer detects
  *behavioral volume/pattern* deviations (a security signal) that get escalated
  to LLM-based intent classification. The two are complementary layers a team
  could run simultaneously (reliability anomaly detection + behavioral security
  anomaly detection) rather than substitutes for one another.

### Claim 8: In the worked example, a three-layer analysis of an inventory agent's large-batch, offset-jumping `list_inventory` calls correctly distinguishes systematic scraping from normal browsing and produces a Critical-severity, 95%-probability "resource exhaustion" finding with a plain-language rationale and specific recommended fixes
- **Evidence**: A single detailed worked example: a user prompt ("I want to see
  your inventory. List 100 items at a time"), the agent's resulting large-batch
  offset-jumping tool-call pattern, and the three-layer analysis that follows
  (statistical outlier flag → LLM reasoning verdict → optional per-call
  reconstruction).
- **Confidence**: anecdotal (a single illustrative scenario provided by the
  vendor to explain the feature, not a report of a real customer incident or a
  representative sample of detection accuracy across many sessions)
- **Quote**: "Nothing here throws an error. The agent is only doing things it’s
  capable of, and there may be no policy preventing it. But Agent Anomaly
  Detection flags the anomalous behavior, working through the session in
  layers: the first layer flags the session as a statistical outlier from the
  volume and the repeated calls. The second layer reasons through the full
  exchange, recognizes the large-batch, offset-jumping pattern as systematic
  scraping rather than normal browsing, and returns a verdict with a
  plain-language explanation. Where a case needs a closer look, a third layer
  reconstructs the individual tool calls and their offsets to show exactly what
  was pulled."
- **Our assessment**: This example is the concrete instantiation of Claim 1's
  thesis — the session "clears" in the sense that no tool call errors, no
  refused requests, nothing crashes; the agent is "only doing things it's
  capable of." The finding is behavioral/intent-level (systematic scraping vs.
  normal browsing), which is exactly the class of anomaly that outcome-based
  metrics (did the tool call succeed?) cannot detect. Worth noting: this is a
  three-layer pipeline (statistical → LLM reasoning → optional reconstruction),
  one layer more than the two-layer description in Claim 7 — the third,
  per-call reconstruction layer is invoked only "where a case needs a closer
  look," i.e., it is itself conditionally triggered rather than run on every
  flagged session.

### Claim 9: Findings can be consumed programmatically via an API that exposes anomalies for a given session, so an ADK callback or plugin can check severity and probability and block subsequent tool calls or halt the next turn once a team-defined threshold is crossed
- **Evidence**: Direct feature description under a section following the worked
  example.
- **Confidence**: emerging (a described API capability; no code sample, request/
  response schema, or latency characteristics for the API call itself are given
  in this source)
- **Quote**: "Beyond review, you can act on findings programmatically. Agent
  Anomaly Detection exposes an API to pull the anomalies for a given session,
  so an ADK callback or plugin can check a finding's severity and probability
  and block subsequent tool calls or halt the next turn when it crosses a
  threshold you set."
- **Our assessment**: This closes the loop between out-of-band detection
  (Claim 3, which by design cannot prevent the *first* anomalous action) and
  actual containment: a team can wire the anomaly API into an ADK callback so
  that, once a session is flagged with sufficiently high severity/probability,
  the *next* turn or tool call is blocked — bounding the blast radius of an
  already-flagged session even though the detection itself lags the action.
  This is architecturally distinct from purely inline gateways (like the
  semantic gateway in `blog-google-adk-zero-trust-agents.md` Claim 8, which
  blocks before every call): here, normal calls proceed uninspected in real
  time, and only a session already flagged by the async pipeline gets
  subsequent calls gated. Teams adopting this should treat the threshold
  (severity × probability) as a tunable tradeoff between false-positive session
  interruption and exposure window before containment.

### Claim 10: The feature requires ADK 1.2 or later on the Gemini Enterprise Agent Platform, is available only in Private Preview, and is enabled via one-click provisioning after prerequisites are met
- **Evidence**: Direct statement under "Get started."
- **Confidence**: settled (a factual, checkable statement of current
  availability and requirements as of the publish date)
- **Quote**: "Agent Anomaly Detection is currently in Private Preview for teams
  deploying agents on the Gemini Enterprise Agent Platform with ADK 1.2 or
  later. To get started, review the documentation for the prerequisites and
  setup. Once the prerequisites are met, you can turn on Agent Anomaly
  Detection with one-click provisioning."
- **Our assessment**: Practically important gating fact: this is not generally
  available, requires a specific ADK version floor, and is scoped to Google's
  own Gemini Enterprise Agent Platform — it is not a portable pattern a team
  can adopt on another agent platform today, only a concrete architecture
  worth borrowing (Claims 2, 3, 7) if building an equivalent capability
  in-house.

## Concrete Artifacts

### Feature summary (paraphrased structure, quotes verbatim per claims above)
```
Agent Anomaly Detection — Gemini Enterprise Agent Platform (Private Preview, Sept 16, 2026)

INPUT:      Existing OpenTelemetry traces + logs agents already emit (no new instrumentation)
LATENCY:    Zero added runtime latency (async, out-of-band from live request path)
PIPELINE:   Layer 1 — lightweight statistical pass (scans all traffic, flags outliers)
            Layer 2 — LLM-based reasoning pass (deep analysis of flagged sessions only)
            Layer 3 — per-call reconstruction (conditional, "where a case needs a closer look")
TAXONOMY:   OWASP Top 10 for Agentic Applications (2026):
              - ASI02 tool misuse
              - ASI03 identity and privilege abuse
              - ASI08 cascading failures
              - ASI10 rogue agents
              - + resource exhaustion, token usage escalation (operational risks)
OUTPUT:     Finding = { severity, plain-language explanation, recommended actions }
            → published to Security Command Center for triage
ACTION:     API exposes per-session anomalies (severity + probability)
            → ADK callback/plugin can block subsequent tool calls or halt next turn
              once a team-set threshold is crossed
ROADMAP:    Custom natural-language + deterministic business-logic detectors,
            backtestable against past traffic (not yet available)
REQUIRES:   ADK 1.2+, Gemini Enterprise Agent Platform, Private Preview enrollment
```

### Worked example: inventory-scraping finding (paraphrased from source, quote in Claim 8)
```
Setup:   Inventory Agent with a `list_inventory` tool
Trigger: User: "I want to see your inventory. List 100 items at a time."
Agent behavior: pages through in large batches, jumps across offsets to pull
                the whole catalog. No tool errors; no policy technically violated.

Layer 1 (statistical): flags session as outlier — volume + repeated calls
Layer 2 (LLM reasoning): classifies pattern as "systematic scraping" (not
                normal browsing) based on large-batch, offset-jumping shape;
                returns plain-language verdict
Layer 3 (reconstruction, conditional): reconstructs individual tool calls +
                offsets to show exactly what was pulled

Finding:  Resource exhaustion, Critical severity, 95% probability
Recommended fixes:
  - rate-limit or block the list_inventory tool for that user
  - add authorization checks to restrict bulk inventory access
  - alert on large-offset pagination patterns
Also surfaces in: Security Command Center (for triage)
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-continual-harness-improvement.md` Claim 6 ("We compute
    baselines per-tool and per-model, because different models may mess up
    tool calls at different rates... anomaly detection alerts fire when
    expected errors significantly exceed the baseline"): both sources use a
    baseline-deviation statistical layer as the first tier of anomaly
    detection. The key distinction: Cursor's baselines target *tool-call error
    rate* (a reliability signal, per tool per model), while this source's
    statistical layer targets *behavioral volume/pattern* deviations (a
    security signal, per session) that get escalated to an LLM reasoning tier.
    These are complementary detection targets, not competing implementations
    of the same signal — see this note's Claim 7 assessment for the full
    distinction.
  - `blog-ghaw-agent-observability.md` Claim 4 (Portfolio Analyst finding "some
    agents were way too chatty with their LLM calls" via fleet-wide token
    profiling) and `docs-ghaw-agentic-ops.md` Claim 9 (fleet-level cost
    anomaly thresholds: >30% of total tokens, >100K avg tokens per run): both
    are fleet/cost-monitoring patterns that, like this source's "token usage
    escalation" detector category (Claim 5), treat runaway token/resource
    consumption as a detectable anomaly signal. The GHAW sources monitor cost
    *across a fleet of workflows* at fixed thresholds; this source monitors
    resource exhaustion *within a single agent session* via statistical +
    LLM-reasoning layers, a finer-grained and more behaviorally-aware
    detection target than a fixed fleet-level threshold.
  - `blog-jetbrains-agentic-ai-governance.md` Claim 7 (a meaningful agent audit
    trail should capture, among other elements, "whether policy was
    violated"): this source's product is a concrete technical mechanism for
    populating exactly that audit-trail element — Agent Anomaly Detection's
    findings *are* the "policy violated" signal JetBrains' audit trail
    specification calls for, generated automatically rather than requiring a
    human or a separate compliance process to determine post hoc whether a
    session violated policy.
  - `blog-anthropic-zero-trust-ai-agents.md` Claim 5 ("least agency," the
    OWASP-coined extension of least privilege to agentic systems, restricting
    what each agent tool can do, how often, and where): this source's ASI02
    (tool misuse) and resource-exhaustion detector categories are runtime
    *detection* mechanisms for violations of exactly the constraints "least
    agency" prescribes designing in *statically* (how often a tool can be
    called, in what volume). The two sources describe complementary control
    types: least agency is a preventive design-time constraint; Agent Anomaly
    Detection is a detective runtime control that catches violations of
    constraints that were not (or could not be) fully specified in advance —
    the inventory-scraping example (Claim 8) is explicitly a case where "there
    may be no policy preventing it."

- **Contradicts**: No material contradictions identified with existing corpus
  source notes. This source's "zero added runtime latency" framing (Claim 3)
  might appear to be in tension with inline-gateway approaches like
  `blog-google-adk-zero-trust-agents.md`'s Semantic Gateway (which necessarily
  adds latency by inspecting every prompt/tool call before it executes), but
  this is a genuine architectural tradeoff (detect-after vs. block-before), not
  a factual disagreement between the two sources — both are valid, complementary
  controls addressing different threat windows (see Claim 3 and Claim 9
  assessments). Not filed as a contradiction per MINER.md §4a.

- **Extends**:
  - `blog-google-adk-zero-trust-agents.md`: that source documents three
    pre-deployment hardening layers for state-mutating agents (cryptographic
    write signatures, gVisor sandboxing, a deterministic Semantic Gateway) —
    all designed in *before* the agent runs and enforced inline. This source
    is the operational-monitoring complement: a *post-deployment*, *out-of-band*
    layer that observes an already-running, already-hardened agent's behavior
    over the course of a session and detects violations the static layers
    did not anticipate or could not prevent (e.g., a technically-authorized
    but abusive usage pattern like the inventory-scraping example, which no
    static permission check would catch since the agent has legitimate access
    to `list_inventory`).
  - `docs-ghaw-agentic-ops.md`: that pattern documents fleet-level monitoring
    (cost, failure rate, "other unhealthy patterns" across many workflows) with
    fixed absolute/change-detection thresholds. This source extends the fleet
    monitoring concept down to the level of a single agent *session*, adding
    an LLM-based reasoning tier that can distinguish *intent* (systematic
    scraping vs. normal browsing) rather than only flagging threshold breaches.

- **Novel**:
  - **A named, published OWASP Agentic Top 10 (2026) taxonomy with specific
    ASI-numbered categories mapped to a shipping product's detectors** (Claim
    5): the corpus's prior OWASP reference (`blog-anthropic-zero-trust-ai-agents.md`
    Claim 5) cites OWASP only for the "least agency" term; this is the first
    source to name specific numbered categories (ASI02, ASI03, ASI08, ASI10)
    from a 2026 OWASP standard and show a production detector mapped to them.
  - **A statistical-first-pass → LLM-reasoning-second-pass → conditional
    per-call-reconstruction three-tier pipeline specifically for behavioral/
    intent anomaly detection** (Claims 7, 8): distinct from the corpus's prior
    anomaly-detection examples (Cursor's per-tool/per-model error-rate
    baselines, GHAW's fleet cost thresholds), which are single-tier statistical
    threshold systems without an LLM reasoning escalation tier that classifies
    *intent* (e.g., "systematic scraping" as a semantic label, not just "volume
    exceeded N").
  - **A severity × probability programmatic threshold API for post-hoc,
    subsequent-turn blocking** (Claim 9): no prior corpus source describes an
    anomaly-detection API specifically designed to be wired into an agent
    callback to gate *future* turns/tool calls in an *already-flagged* session,
    as distinct from inline pre-call gateways that gate *every* call.
  - **Backtestable natural-language custom anomaly detectors** (Claim 6,
    roadmap item): validating a new natural-language + deterministic detection
    rule against historical session traffic before enabling it live is not
    described in any existing corpus source, though it is explicitly unreleased
    and should be flagged as directional only.

## Guide Impact

- **Chapter 06 (Security Threat Model), "Bounding Your Own Agents" / sandbox
  sections**: add Agent Anomaly Detection as a concrete example of a
  **detective, post-deployment runtime control** distinct from the
  **preventive, pre-deployment controls** the chapter currently covers
  (sandbox egress scope, least agency). The inventory-scraping worked example
  (Claim 8) is a good illustration for the guide of *why* preventive controls
  alone are insufficient: the agent had legitimate, policy-compliant access to
  the tool it abused, so no static permission check would have caught the
  pattern — only session-level behavioral analysis could. Frame this as a third
  control category alongside sandboxing and gateways: detect-after with
  bounded exposure via threshold-gated blocking of subsequent actions (Claim 9),
  not prevent-before.

- **Chapter 06 (Security Threat Model)**: cite the OWASP Top 10 for Agentic
  Applications (2026) ASI-numbered taxonomy (Claim 5) as a vendor-neutral
  vocabulary for categorizing agent security findings, useful for teams that
  need to report across multiple agent platforms or align with the corpus's
  existing "least agency" (OWASP) reference in
  `blog-anthropic-zero-trust-ai-agents.md`.

- **Chapter 02 (Harness Engineering), observability/monitoring content**: note
  the "consume existing OpenTelemetry traces, add no new instrumentation, run
  fully out-of-band" architecture (Claims 2, 3) as a reusable design pattern
  for teams building their own behavioral anomaly detection, independent of
  whether they use Google's specific product: a detector that's a pure
  downstream consumer of telemetry the harness already emits avoids the
  latency/complexity cost of inline monitoring, at the cost of a detection lag
  that must be bounded by a separate containment mechanism (Claim 9) for
  already-flagged sessions.

## Extraction Notes

- The blog post was fetched twice: once via the WebFetch tool's AI summarizer
  (which returned only a condensed, paraphrased summary insufficient for
  verbatim quoting), and once via a direct `curl` fetch of the raw HTML,
  followed by a Python script that stripped `<script>`/`<style>` tags and
  converted the remaining HTML to plain text while preserving paragraph
  boundaries. All `Quote` fields above were verified against this second,
  raw-text extraction, not the summarizer output.
- The post is short (~700 words) and single-page; no linked sub-pages were
  substantive enough to follow per MINER.md §1 beyond the referenced OWASP Top
  10 standard itself (an external standards document, not a Google page, and
  not fetched separately — the specific category names/numbers ASI02/ASI03/
  ASI08/ASI10 are taken directly from this source's own text, not verified
  against the OWASP document itself).
- One related post was noted in the page's "Related Posts" section — "Build
  zero-trust AI agents that judge intent, not just syntax" (Sept 15, 2026) —
  which corresponds to the existing corpus source note
  `blog-google-adk-zero-trust-agents.md` (published Aug 17, 2026 per that
  note's frontmatter; the Sept 15 date on the related-posts teaser may reflect
  a republish/index date rather than original publish date — this discrepancy
  is noted for the Assayer but does not affect this note's claims, none of
  which depend on the zero-trust post's exact publish date).
- No contradictions with existing corpus source notes were identified during
  cross-referencing (see Cross-References → Contradicts); none filed per
  MINER.md §4a.
- Given the source is a vendor announcement of a Private Preview feature with
  one illustrative example and no independently-verified metrics (latency,
  accuracy, false-positive rate), most claims are graded "emerging"; only the
  literal factual statements (the OWASP taxonomy mapping as stated by the
  vendor, and the ADK 1.2+/Private Preview availability requirement) are
  graded "settled," and the single worked example is graded "anecdotal."
  Overall confidence is "emerging" for the source as a whole.
