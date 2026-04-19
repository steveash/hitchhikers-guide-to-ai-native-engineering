---
source_url: https://cursor.com/blog/security-agents
source_type: blog-post
title: "Securing our codebase with autonomous agents"
author: Travis McPeak (Cursor/Anysphere)
date_published: 2026-03-16
date_extracted: 2026-04-19
last_checked: 2026-04-19
status: current
confidence_overall: emerging
issue: "#161"
---

# Securing our codebase with autonomous agents

> Cursor's first-party account of deploying a fleet of four specialized security
> agents in production — covering new code review, legacy codebase scanning,
> dependency patching, and invariant monitoring — with concrete architecture
> decisions (MCP-based persistent state, Gemini Flash 2.5 deduplication, gradual
> trust rollout) and production metrics (3,000+ PRs reviewed weekly, 200+
> vulnerabilities caught per week).

## Source Context

- **Type**: blog-post (first-party practitioner report from Cursor/Anysphere, ~1,500
  words, published March 16, 2026)
- **Author credibility**: Travis McPeak is credited as author. Published on the
  official Cursor blog — this is Cursor writing about their own production use of
  Cursor Automations, making it simultaneously vendor marketing and first-person
  practitioner evidence. The specific architecture details (MCP as Lambda, Gemini
  Flash 2.5 classifier, Terraform deployment, canary pipeline) are concrete enough
  to indicate genuine engineering experience rather than marketing abstraction. The
  automation templates are publicly available in the marketplace, providing independent
  access to the implementation artifacts.
- **Scope**: Covers four distinct agent patterns (new code review, legacy scanning,
  dependency patching, invariant monitoring) and the shared MCP infrastructure that
  coordinates them. Does NOT cover: failure modes or false positive rates in practice,
  cost structure, how agents handle ambiguous findings, agent behavior on vulnerability
  types outside the specific threat models, or how long calibration took before moving
  from shadow mode to blocking.

## Extracted Claims

### Claim 1: A 5x PR velocity increase over nine months outpaced static analysis and code ownership tools

- **Evidence**: Author's direct statement: "Over the last nine months, our PR velocity
  has increased 5x. Security tooling based on static analysis or rigid code ownership
  remains helpful, but is not enough at this scale."
- **Confidence**: anecdotal (self-reported; no definition of "PR velocity" or baseline given)
- **Quote**: "Over the last nine months, our PR velocity has increased 5x. Security tooling
  based on static analysis or rigid code ownership remains helpful, but is not enough at
  this scale."
- **Our assessment**: This is the key motivation claim. The 5x velocity figure is plausible
  given that Cursor is one of the highest-adoption AI coding tools — their own engineers
  would naturally show the most dramatic velocity increase of any team. The framing
  ("not enough at this scale") is significant: static analysis and code ownership are not
  discarded, but are framed as insufficient when PR signal volume 5x's. This provides
  first-party evidence that PR velocity gains documented externally (Faros's 47% PR
  increase) translate into a genuine security review capacity problem even at the team that
  builds the tool. The velocity number is self-reported and lacks a baseline definition —
  treat directionally.

### Claim 2: A shared security MCP deployed as a Lambda solves the multi-agent coordination problem for a security agent fleet

- **Evidence**: Author's architectural description: a serverless Lambda with three
  functions — (1) persistent data storage for tracking security impact over time,
  (2) deduplication via Gemini Flash 2.5 classifier for semantically identical findings,
  (3) consistent output formatting via Slack messages and issue management. Deployed with
  Terraform. Reference code publicly available on GitHub.
- **Confidence**: emerging (self-described architecture; reference code available but
  not independently reviewed for this extraction)
- **Quote**: "The agent uses the MCP to store data, so we can track and measure security
  impact over time."
- **Our assessment**: This is the most architecturally novel claim in the source. The
  pattern is: a purpose-built MCP server as the shared substrate for a fleet of specialized
  agents, not as an agent itself. The three functions map cleanly to three distinct
  coordination problems: (1) persistence addresses the ephemeral-session problem (agents
  don't remember past runs); (2) deduplication addresses the semantic-noise problem
  (different agents, same finding, different words); (3) consistent output addresses the
  integration problem (humans and downstream systems need a uniform format regardless of
  which agent found what). The Lambda + Terraform deployment means the MCP is
  infrastructure with production reliability expectations, not a script.

### Claim 3: Cross-model LLM deduplication (Gemini Flash 2.5 alongside Claude agents) prevents finding noise at scale

- **Evidence**: Author's explicit description: "a classifier powered by Gemini Flash 2.5
  that determines when two semantically distinct findings describe the same problem."
  Used by the shared MCP tool across all agent runs.
- **Confidence**: anecdotal (no precision/recall figures for the deduplication classifier;
  no baseline comparison vs. rule-based deduplication)
- **Quote**: "a classifier powered by Gemini Flash 2.5 that determines when two semantically
  distinct findings describe the same problem"
- **Our assessment**: The choice to use Gemini Flash 2.5 as a fast classifier *within*
  a Claude-agent workflow is a concrete production example of multi-model routing. The
  motivation is architectural: when independent agents discover the same vulnerability but
  describe it differently, string matching fails. A semantic classifier that understands
  "SQL injection in the auth path" and "unsanitized input in auth.js:34" may refer to the
  same vulnerability resolves this at the meaning level. The choice of Flash (not a more
  expensive reasoning model) fits the multi-model routing principle: use the cheapest model
  that can reliably do the task. No precision/recall data is provided — we don't know how
  often the classifier correctly identifies duplicates vs. false-merges distinct findings.

### Claim 4: A gradual trust-building rollout (private Slack → PR commenting → blocking gate) is the right deployment pattern for autonomous agents entering critical paths

- **Evidence**: Author's explicit description of the Agentic Security Review rollout:
  "we first forwarded findings to a private Slack channel monitored by our security team.
  Once we were confident it was identifying genuine issues, we turned on PR commenting.
  [Then] we implemented a blocking gate check."
- **Confidence**: emerging (one team's experience; the logic is sound and independently
  corroborated by Osmani's conceptual framework)
- **Quote**: "we first forwarded findings to a private Slack channel monitored by our
  security team. Once we were confident it was identifying genuine issues, we turned on
  PR commenting."
- **Our assessment**: This is the most practically actionable claim for teams deploying
  autonomous agents into critical paths. The three-stage structure is correct in principle:
  shadow mode (Slack notification, no PR impact) validates signal quality before anything
  blocks anyone. Moving to PR commenting exposes the agent's output to wider scrutiny
  without blocking. Only after both stages does it gate merges. This prevents the "agent
  cried wolf" failure mode that causes engineers to dismiss legitimate findings. The fact
  that Cursor used this pattern for their own internal deployment (not just as a customer
  recommendation) gives it practitioner credibility. The length of each phase is not
  specified.

### Claim 5: Dedicated security agents prompt-tuned to specific threat models outperform general-purpose code review for security

- **Evidence**: Author's design rationale for Agentic Security Review: "dedicated
  automation replacing general-purpose code review for security contexts... prompt-tuned
  to specific threat models." Enables CI blocking on security findings independently
  from general code quality.
- **Confidence**: emerging (architecture rationale, not quantified; consistent with
  the distraction failure mode documented in discussion-hn-autofix-hybrid-review.md)
- **Quote**: "prompt-tuned to specific threat models"
- **Our assessment**: The independence claim is architecturally important: separating
  security review from general code review means both can be independently gated, tuned,
  and operated. A security agent doing general code quality review simultaneously has
  competing objectives — the distraction failure mode documented in DeepSource's benchmark
  (Claude Code recall 48.78% for security on full diffs) maps exactly to this problem.
  Prompt-tuning to specific threat models is the mechanism: rather than "review this code
  for security issues" (open-ended), the agent has a defined set of threat classes to
  check against. This is architecturally equivalent to Sentry's `sentry-security` skill
  (37 historical patches, 6 vulnerability classes), but automated rather than manually
  curated by a platform team.

### Claim 6: Reachability analysis narrows automated dependency patching to actually impactful vulnerabilities

- **Evidence**: Author's description of Anybump workflow: "reachability analysis narrows
  findings to those that are actually impactful, then traces through the relevant code
  paths, runs tests, checks for breakage, and opens a PR once tests pass."
- **Confidence**: emerging (described workflow, not benchmarked; reachability analysis is
  a known technique in static analysis)
- **Quote**: "reachability analysis narrows findings to those that are actually impactful,
  then traces through the relevant code paths"
- **Our assessment**: Dependency vulnerability patching has a notorious false-positive
  problem: most CVEs affect packages a codebase imports but whose vulnerable code paths
  are never exercised. Reachability analysis distinguishes real exposure from nominal.
  The automation sequence is sound: narrow by reachability → trace code paths → run
  tests → open PR only if tests pass. The novel element is running this as a fully
  autonomous agent rather than a scheduled scanner with human triage. The canary
  deployment as a final gate after tests pass is the right conservative safety layer
  for dependency changes that affect runtime behavior.

### Claim 7: Stateful subagents with memory can detect drift against security and compliance invariants over time

- **Evidence**: Author's description of Invariant Sentinel: "Runs daily monitoring
  against security and compliance properties... compares current state against previous
  runs using the automations memory feature. If it detects drift, it revalidates to
  ensure correctness, then updates its memory." Also: "executes code within full
  development environments for validation."
- **Confidence**: anecdotal (described architecture; no specifics on what invariants
  are tracked, how drift is defined, or false alarm rate)
- **Quote**: "compares current state against previous runs using the automations memory
  feature. If it detects drift, it revalidates to ensure correctness, then updates its
  memory."
- **Our assessment**: This is the most architecturally novel pattern in the source. An
  agent that maintains a memory of a previous baseline and alerts on drift is a continuous
  compliance assertion system. The "revalidate before alerting" step prevents ephemeral
  diffs (a file temporarily modified by a build process) from triggering false alarms.
  The memory persistence is at the framework level (automations memory), not an external
  database, which simplifies deployment. Executing code within full development
  environments (not just reading code) means the agent can verify runtime properties,
  not just static code properties. The gap: we don't know what invariants Cursor monitors,
  how they're specified, or how long the daily run takes. The pattern generalizes beyond
  security — any property expressible as "this should always be true" can be an invariant.

### Claim 8: Dividing a codebase into logical segments enables full-codebase scanning beyond single-context-window limits

- **Evidence**: Both Vuln Hunter and Invariant Sentinel use this pattern: "scans
  existing codebase by dividing into logical segments" (Vuln Hunter); "divides repos
  into logical segments with subagents validating code" (Invariant Sentinel).
- **Confidence**: emerging (described pattern; consistent with known context window limits)
- **Quote**: "Divides repos into logical segments with subagents validating code"
- **Our assessment**: This is the practical answer to "how do you apply an agent to a
  codebase larger than one context window?" Segment by module/package/directory
  (logical unit) rather than arbitrary file count, so each subagent has a coherent
  scope to reason about. The key design question — how to aggregate findings across
  segments to avoid missing cross-segment vulnerability patterns — is not addressed
  in the source. This pattern appears in TTal (worktree isolation per task) and
  Osmani's parallel decomposition, but Cursor is the first to describe it explicitly
  in a security scanning context.

### Claim 9: Agent-driven security review can catch 200+ vulnerabilities per week across 3,000+ PRs

- **Evidence**: Author's production metrics: "Security agents review 3,000+ internal
  PRs weekly. 200+ vulnerabilities caught per week." Also: "In the last two months,
  Agentic Security Review has run on thousands of PRs and prevented hundreds of issues
  from reaching production."
- **Confidence**: anecdotal (self-reported; no definition of "prevented," no baseline,
  no independent validation)
- **Quote**: "In the last two months, Agentic Security Review has run on thousands of
  PRs and prevented hundreds of issues from reaching production."
- **Our assessment**: The headline metrics lack denominator context. "Hundreds of
  issues" out of "thousands of PRs" could represent a high or low vulnerability rate
  depending on the codebase's baseline. The more useful signal is directional: the
  agent runs at production scale and finds actionable issues — not just noise. "200+
  per week" suggests the agent is not overly conservative (high precision / low recall
  would produce far fewer findings). Whether "hundreds prevented" means "blocked by
  the gate check" or "reported and fixed before merge" is unclear — the shadow mode
  phase means many early findings were informational, not blocked. Treat as
  directional evidence of operational viability at scale, not a precision/recall
  benchmark.

### Claim 10: The security agent fleet is designed to extend to vulnerability intake, privacy compliance, on-call triage, and access provisioning

- **Evidence**: Author's forward-looking statement listing planned extensions.
- **Confidence**: anecdotal (stated intentions, not yet implemented)
- **Quote**: N/A (paraphrased from plans section)
- **Our assessment**: The planned extensions are informative for understanding the
  trajectory. On-call alert triage means autonomous agents responding to production
  incidents — a significant trust escalation beyond pre-merge code review. Privacy
  compliance monitoring extends the Invariant Sentinel pattern to a new invariant class.
  Access provisioning is the most ambitious: it involves taking actions in external
  systems (IAM, RBAC), not just reading and reporting. Each step represents a trust
  escalation beyond current use cases. For the guide: the trajectory from "shadow mode
  review" to "blocking gate" to "access provisioning" maps the natural escalation of
  trust in autonomous agents, and each step should require the same gradual-confidence
  methodology described in Claim 4.

## Concrete Artifacts

### The Four-Agent Security Fleet Architecture

```
Cursor Security Agent Fleet (cursor.com/blog/security-agents, March 2026)
All agents share a common security MCP tool deployed as an AWS Lambda function.

1. Agentic Security Review
   Trigger:    new PR submitted
   Scope:      incoming code diff
   Mechanism:  prompt-tuned to specific threat models; independent CI blocking gate
   Rollout:    shadow (Slack) → PR commenting → blocking gate check
   Scale:      3,000+ PRs/week, 200+ vulnerabilities/week, hundreds prevented in 2 months
   Template:   marketplace/automations/find-vulnerabilities

2. Vuln Hunter
   Trigger:    on-demand (ad hoc codebase scan)
   Scope:      existing codebase, divided into logical segments
   Mechanism:  finds vulnerabilities in existing code;
               team triages findings and generates fixes via @Cursor from Slack
   Template:   marketplace/automations/scan-codebase-vulnerabilities

3. Anybump
   Trigger:    dependency vulnerability notification (filtered by reachability)
   Scope:      dependency tree → relevant code paths
   Mechanism:  reachability analysis → trace code paths → run tests → check breakage
               → open PR if tests pass → canary deployment as final safety gate
   Template:   marketplace/automations/remediate-dependency-vulnerabilities

4. Invariant Sentinel
   Trigger:    daily schedule
   Scope:      full codebase (divided into segments, subagents per segment)
   Mechanism:  run daily → compare current state vs. memory of previous run
               → detect drift → revalidate → update memory
               → Slack report with code location evidence on drift
   Note:       executes code in full dev environments (runtime verification, not just static)
   Template:   marketplace/automations/monitor-engineering-invariants
```

### Security MCP Tool Architecture

```
Security MCP Tool (shared coordination substrate for all four agents)

Deployed as:    AWS Lambda (serverless)
Provisioned:    Terraform
Reference code: public GitHub repository (linked from blog post)

Functions:
  1. Persistent State
     — stores findings data to track and measure security impact over time
     — enables "how many issues caught this week?" metrics across agent runs

  2. Deduplication
     — Gemini Flash 2.5 semantic classifier
     — identifies when two semantically distinct finding descriptions
       refer to the same underlying vulnerability
     — prevents noise: "same vulnerability, described in different words"

  3. Output Formatting + Actions
     — all agents report findings through this single channel
     — emits consistently formatted Slack messages
     — handles downstream actions: dismiss, snooze, create issue

Design principle: the MCP is infrastructure, not an agent.
It does not reason or take initiative. It provides coordination services
(persistent state, cross-run deduplication, output routing) to the agents
that call it.
```

### Anybump Reachability-Filtered Patching Workflow

```
Input: dependency vulnerability notification
  ↓
Reachability analysis: is the vulnerable code path actually callable?
  ↓ (if NOT reachable) → skip — no action needed
  ↓ (if reachable)
Trace code paths: which entry points reach the vulnerable function?
  ↓
Run tests against patched dependency version
  ↓ (if tests FAIL) → do not open PR; escalate to human review
  ↓ (if tests pass)
Check for breakage (side-effect analysis)
  ↓
Open PR with dependency patch
  ↓ (post-merge)
Canary deployment pipeline (final safety gate before full production)
```

### Gradual Trust Rollout Pattern (Shadow → Inform → Gate)

```
Pattern for deploying autonomous agents into critical paths

Stage 1: Shadow mode
  — Agent runs on all incoming events
  — Findings routed to a private Slack channel (security team only)
  — Zero PR impact; zero blast radius
  — Purpose: validate that the agent identifies genuine issues before anyone sees it

Stage 2: PR commenting
  — Agent posts findings as PR comments visible to the PR author
  — Engineers can act on or dismiss findings
  — Still no hard gate; engineer can merge despite findings
  — Purpose: expose agent to broader scrutiny; build wider confidence

Stage 3: Blocking gate check
  — Implemented as a CI gate check on PRs
  — Agent findings can block merge
  — Engineer must address or dismiss findings before PR lands
  — Purpose: enforce findings as a hard constraint

Progression criteria:
  Stage 1 → 2: "confident it was identifying genuine issues"
  Stage 2 → 3: not explicitly stated; implied by confidence continuing to build
```

## Cross-References

- **Corroborates**: `discussion-hn-autofix-hybrid-review.md` — DeepSource's hybrid
  architecture (static analysis + LLM) and Cursor's Agentic Security Review both
  address the same problem: LLM-only code review has insufficient recall for security
  issues (Claude Code recall 48.78% on the OpenSSF CVE benchmark). Cursor's response
  is specialization (prompt-tuned threat models, dedicated CI gate). DeepSource's
  response is anchoring (static findings as LLM anchors). Both sources agree that
  general-purpose LLM review is architecturally insufficient for security at scale;
  they represent different design responses to the same recall gap.

- **Corroborates**: `practitioner-getsentry-sentry.md` — Sentry's `sentry-security`
  skill (37 historical patches, 6 vulnerability classes, HIGH/MEDIUM confidence
  threshold) is the manually-curated practitioner equivalent of Cursor's Agentic
  Security Review. Both encode known vulnerability classes as structured agent context
  rather than relying on open-ended LLM security review. The shared principle: focused-
  scope security agents with explicit threat models outperform general-purpose code review
  for security. The difference is scale and automation: Sentry's approach requires a
  platform team to curate and maintain the patterns; Cursor deploys an autonomous agent.

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` — Osmani's thesis
  ("the bottleneck is no longer generation, it's verification") maps exactly to
  Cursor's scaling problem: 5x PR velocity increase → static security tooling insufficient
  → autonomous security agents as the verification layer. Osmani's gradual trust-building
  framework (shadow → inform → gate) is independently implemented by Cursor in identical
  stages. The multi-model routing pattern (Osmani Claim 9: route different tasks to
  different models based on capability and cost) is instantiated here as Gemini Flash 2.5
  for semantic classification within a Claude agent workflow.

- **Corroborates**: `paper-miller-speed-cost-quality.md` — Miller et al.'s finding that
  AI adoption increases static analysis warning volume (30.3% more warnings) provides
  independent evidence for Claim 1: when PR velocity 5x's, security tooling that worked
  at 1x velocity is insufficient. The Cursor source adds a practitioner-built response:
  the answer to "too many signals to review manually" is not better static analysis but
  autonomous agents that can triage and resolve signals at the same velocity as generation.

- **Extends**: `discussion-hn-ttal-multiagent-factory.md` — TTal's two-plane architecture
  (persistent Manager + ephemeral Workers) has structural parallels to Cursor's fleet:
  the security MCP acts as a persistent coordination plane; the four specialized agents
  are ephemeral task executors. The key difference: TTal's manager plane does task routing;
  Cursor's MCP does state persistence, deduplication, and output normalization — coordination
  at the data layer rather than the task-routing layer. Both patterns show that a multi-agent
  fleet needs persistent shared state that individual ephemeral agents cannot maintain.

- **Novel**:
  - The **security MCP as shared coordination substrate** (not as an agent itself but as
    infrastructure providing persistent state, cross-run deduplication, and consistent
    output for a fleet of specialized agents) is not documented in any other corpus source.
    This is a concrete design pattern: build the MCP to do what agents cannot do reliably
    across sessions.
  - The **cross-model deduplication** pattern (Gemini Flash 2.5 semantic classifier within
    a Claude agent workflow for a specific coordination subtask) is novel to the corpus.
    No other source documents routing a subtask of a Claude workflow to a different vendor's
    model for cost/latency reasons.
  - The **Invariant Sentinel** drift-detection pattern (daily stateful compliance monitoring
    with memory comparison) is not documented elsewhere in the corpus. It extends CI testing
    to continuous compliance monitoring — a distinct agent archetype.
  - The **reachability-analysis-as-filter** for autonomous dependency patching is novel to
    the corpus. No other source documents this technique for narrowing autonomous patch scope
    to genuinely impactful vulnerabilities.
  - The **gradual trust-building rollout** (shadow → inform → gate) as a concrete production
    deployment pattern is new. Osmani describes the concept; Cursor is the first corpus source
    to report implementing it in production for an agent fleet.

## Guide Impact

- **Chapter on Agentic Workflows / Multi-Agent Orchestration**: The four-agent fleet
  architecture should be the primary production example of autonomous security infrastructure.
  Extract the MCP-as-coordination-substrate pattern as a named design principle: "Build MCPs
  to provide what agents cannot do across sessions — persistence, deduplication, consistent
  output." The Invariant Sentinel is a new agent archetype (continuous compliance monitor)
  distinct from event-driven review agents — both archetypes deserve named treatment.

- **Chapter on Harness Engineering**: Add the gradual trust-building rollout pattern
  (shadow → inform → gate) as the canonical deployment pattern for any autonomous agent
  being introduced to a critical path. The three stages should be explicitly named with
  decision criteria. Any chapter section on deploying blocking CI agents should mandate
  this pattern or an equivalent calibration phase.

- **Chapter on Security**: The four-agent taxonomy (new code review, legacy scanning,
  dependency patching, invariant monitoring) covers the full security lifecycle and should
  anchor any section on AI-native security practices. The specialization principle
  (prompt-tuned to threat models; CI blocking independent from general code quality)
  is the design alternative to general-purpose LLM review and should be presented as
  such alongside the DeepSource recall-gap evidence.

- **Chapter on Tool Selection / Cost and Economics**: The cross-model routing pattern
  (Gemini Flash 2.5 for semantic classification within a Claude workflow) provides a
  concrete production example of using the cheapest capable model for a specific subtask.
  Applicable to any cost optimization section: "For high-frequency classification tasks
  within agent workflows, route to the cheapest model that meets the accuracy bar — don't
  use your primary reasoning model for every coordination subtask."

- **Chapter on Context Engineering**: The codebase-segmentation pattern (divide into
  logical segments, spawn subagent per segment) is the production answer to "how do you
  apply an agent to a codebase larger than one context window?" Cite Vuln Hunter and
  Invariant Sentinel as production-scale examples.

## Extraction Notes

1. **Source is vendor self-report**: This is Cursor writing about their own use of
   Cursor Automations. All metrics (5x velocity, 3,000+ PRs/week, 200+ vulnerabilities/week,
   hundreds prevented) are self-reported without independent verification. The architectural
   details (Lambda, Terraform, Gemini Flash 2.5, canary pipeline) are concrete and specific
   enough to indicate genuine implementation rather than marketing abstraction, but cannot
   be independently verified from the blog post alone.

2. **Reference artifacts not fetched**: The blog post notes reference code for the MCP tool
   is available on GitHub, and each agent has a publicly available template in the Cursor
   marketplace. These artifacts were not fetched for this extraction. Fetching them would
   provide higher-confidence architectural evidence and is recommended for a follow-up if
   deeper technical validation is needed.

3. **Author credibility**: Travis McPeak is credited as author. The Cursor/Anysphere
   organizational context and official blog publication provide the credibility baseline.
   McPeak is not independently identified as a security researcher or security leader
   within the post itself.

4. **No failure modes described**: The source is entirely positive — it describes what
   works, not what failed. The shadow mode phase implies the agent needed calibration
   before gaining sufficient confidence, but no specifics on false positive rates,
   calibration time, or types of issues the agent initially missed are given. This is
   typical of vendor blog posts.

5. **Gemini Flash 2.5 model choice**: The choice of Flash (not a more expensive reasoning
   model) for the deduplication classifier is consistent with a latency/cost-sensitive
   classification task within a high-throughput pipeline. This choice implies the team
   evaluated the cost/accuracy tradeoff explicitly — worth noting for the multi-model
   routing pattern.
