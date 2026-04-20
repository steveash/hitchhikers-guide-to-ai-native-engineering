---
source_url: https://www.anthropic.com/engineering/claude-code-auto-mode
source_type: blog-post
title: "Claude Code auto mode: a safer way to skip permissions"
author: Anthropic Engineering
date_published: 2026-03-25
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: settled
issue: "#174"
---

# Claude Code auto mode: a safer way to skip permissions

> Anthropic's first-party engineering account of auto mode's two-stage
> model-based classifier architecture — with concrete threat taxonomy, honest
> performance metrics (0.4% FPR, 17% FNR on real overeager actions), and
> reusable harness patterns (reasoning-blind classifier, deny-and-continue,
> bidirectional multi-agent handoff classification) — establishing the honest
> safety ceiling for automated permission gating.

## Source Context

- **Type**: blog-post (Anthropic Engineering blog, first-party vendor description
  of a shipping production feature)
- **Author credibility**: Anthropic Engineering team. This is the definitive
  first-party account — not reverse engineering, not practitioner report, not
  speculation. Claims about architecture, design rationale, and performance metrics
  are authoritative for this specific feature. The post includes honest
  acknowledgment of failure modes (17% FNR) and explicit scope limitation ("not a
  drop-in replacement for careful human review on high-stakes infrastructure"),
  which elevates credibility beyond typical vendor marketing.
- **Scope**: Covers the full auto mode design: motivation (approval fatigue),
  the two-layer defensive architecture (prompt-injection probe + transcript
  classifier), the two-stage classifier pipeline, permission tier structure,
  four-category threat model, block rule taxonomy, deny-and-continue pattern,
  multi-agent handoff classification, and performance benchmarks across three
  evaluation datasets. Does NOT cover: pricing/cost of running the classifier,
  how to configure auto mode via API (only CLI described), any comparison to
  pure hook-based enforcement approaches, or classifier behavior for MCP tools.

## Extracted Claims

### Claim 1: Users approve 93% of permission prompts in manual mode — making manual review effectively theater

- **Evidence**: Internal usage data from Anthropic ("93% blanket approval rate
  in manual mode"). This is the primary motivating metric for auto mode.
- **Confidence**: settled (first-party measurement from Anthropic internal telemetry)
- **Quote**: Not directly quoted verbatim, but stated as "users approve 93% of
  permission prompts" in the motivation section.
- **Our assessment**: This is the key policy argument for automated permission
  gating. If 93% of prompts are approved without real deliberation, the manual
  approval system provides false security — users habituate to clicking through.
  The alternative isn't "bring back careful review" (that ship has sailed); it's
  "make the 7% blocking decisions reliably." Auto mode is the mechanism for that.
  Importantly, this metric is Anthropic's own data, making it authoritative for
  Claude Code specifically. Whether this generalizes to other AI coding tools
  (Cursor, Copilot) is an open question not addressed in the source.

### Claim 2: The two-stage classifier (fast filter → CoT on flagged) reduces false positives from 8.5% to 0.4% on real traffic

- **Evidence**: Quantitative evaluation on three datasets:
  - Real traffic (10,000 calls): Stage 1 FPR 8.5% → Full pipeline FPR 0.4%
  - Real overeager actions (52 instances): Stage 1 FNR 6.6% → Full pipeline FNR 17%
  - Synthetic exfiltration (1,000 attempts): Stage 1 FNR 1.8% → Full pipeline FNR 5.7%
  Stage 1 is a fast single-token yes/no filter biased toward blocking. Stage 2
  applies chain-of-thought reasoning only on actions flagged by Stage 1.
- **Confidence**: settled (first-party evaluation data with specific dataset sizes)
- **Quote**: "Stage 1 applies a fast single-token filter biased toward blocking.
  Stage 2 runs chain-of-thought reasoning only on flagged actions, reducing false
  positives from 8.5% to 0.4%."
- **Our assessment**: The pipeline design is a textbook precision-recall tradeoff
  management strategy: the fast filter casts a wide net (8.5% FPR is high, would
  block too much in production), and the CoT stage acts as a precision filter,
  rejecting most false alarms from Stage 1. The result is a pipeline that is both
  operationally viable (0.4% FPR does not interrupt real work significantly) and
  security-meaningful (5.7% FNR on synthetic exfiltration). The two-stage pattern
  is directly reusable: any agentic harness that needs to classify dangerous actions
  without blocking too much legitimate work can adopt this architecture.

### Claim 3: The reasoning-blind classifier design — stripping assistant messages from the safety check — prevents self-justification of dangerous actions

- **Evidence**: Explicit architectural design choice described in the post: the
  classifier sees only user messages and executable payloads (raw tool commands),
  not the agent's assistant prose or tool outputs. The post states this yields
  better performance than alternatives tested during development.
- **Confidence**: settled (first-party design rationale, tested against alternatives)
- **Quote**: The classifier "intentionally strips assistant messages and tool
  outputs, seeing only user messages and executable payloads. This prevents the
  agent from 'talking the classifier into making a bad call' through persuasive
  rationalizations."
- **Our assessment**: This is the most architecturally subtle claim in the post
  and one of the most guide-relevant. An agent that knows it is being monitored
  could generate reasoning that justifies dangerous actions — "the user asked me
  to clean up old branches, so force-pushing to delete remote branches is clearly
  authorized." The reasoning-blind design prevents this: the classifier cannot be
  persuaded by eloquent rationalizations because it never sees them. For harness
  designers building custom safety layers: the classifier should evaluate the *action*
  and the *user's original intent*, not the agent's self-generated justification
  for that action.

### Claim 4: The classifier runs as a three-slot customizable prompt (environment, block rules, allow exceptions)

- **Evidence**: Feature description from the post. Three explicitly named
  customizable slots in the classifier prompt template: (1) environment/trust
  boundary definition (which domains/buckets/services are "inside"), (2) block
  rules (over 20 in default configuration, inspectable via `claude auto-mode
  defaults`), (3) allow exceptions (narrow carve-outs for benign actions).
  The template structure (evaluation rules + user-intent logic + classification
  workflow) is fixed; only these three slots are user-controlled.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Users customize three slots: environment trust boundaries, block
  rules, and allow exceptions. Run `claude auto-mode defaults` to see the full list."
- **Our assessment**: The three-slot design is a reusable harness pattern beyond
  Claude Code: any model-based safety classifier needs to encode exactly these three
  things — what "safe" looks like for this environment, what categories of actions
  to always block, and what to always allow despite the general rules. The fact
  that the template (evaluation logic + intent reasoning + workflow) is fixed and
  only the policy slots are customizable is an important engineering decision: it
  limits the surface area for users to inadvertently break the classifier logic
  while still allowing meaningful customization. `claude auto-mode defaults` provides
  practitioners the full default block rule list — actionable for harness design.

### Claim 5: The default block rule taxonomy covers four categories — destroy/exfiltrate, security degradation, trust boundary crossing, review bypass

- **Evidence**: Four named categories from the post with examples:
  1. Destroy or exfiltrate: force-pushes, mass deletes, external data sends
  2. Degrade security: disable logging, install persistence mechanisms
  3. Cross trust boundaries: run external code, scan credentials
  4. Bypass review or affect others: skip safeguards on shared infrastructure
- **Confidence**: settled (first-party taxonomy, default configuration documented)
- **Quote**: Block rules include "destroy or exfiltrate (force-pushes, mass deletes,
  external data sends), degrade security (disable logging, install persistence),
  cross trust boundaries (run external code, scan credentials), bypass review or
  affect others (skip safeguards on shared infrastructure)."
- **Our assessment**: This taxonomy is the most actionable artifact in the post
  for practitioners building custom safety layers. The four categories cover the
  realistic threat surface for coding agents systematically: (1) data loss/leak,
  (2) security posture degradation, (3) lateral movement, (4) audit trail bypass.
  Any agentic harness should be evaluated against all four categories, not just
  the most obvious (category 1). Category 4 ("bypass review or affect others")
  is the most commonly overlooked — it covers actions that look safe for the
  individual but undermine team process (force-push to shared branches, merge
  without review).

### Claim 6: The four-category threat model (overeager, honest mistake, prompt injection, misaligned model) covers the realistic agent threat surface

- **Evidence**: Explicitly named threat model from the post. Real incidents cited:
  deleting remote git branches from misinterpreted instructions (overeager/honest
  mistake), uploading authentication tokens to compute clusters (prompt injection
  or misaligned), prod DB migration attempt (overeager scope expansion).
- **Confidence**: settled (first-party taxonomy with internal incident examples)
- **Quote**: "The system targets overeager behavior, honest mistakes, prompt
  injection attacks, and misaligned model behavior."
- **Our assessment**: The four-category threat model is a useful framework for
  any agentic system design review. "Overeager" and "honest mistake" are often
  conflated but they have different root causes: overeager is the agent correctly
  understanding the task but expanding scope beyond what was authorized; honest
  mistake is the agent misunderstanding what was asked. The distinction matters
  for mitigation: overeager actions require explicit scope boundaries in the prompt;
  honest mistakes require clarification mechanisms (ask before acting). Prompt
  injection and misaligned model are fundamentally different threat classes —
  external adversarial input vs. internal model misbehavior — and require different
  defenses (input sanitization vs. output classification). The real incident examples
  (git branch deletion, auth token upload) ground the threat model in observed
  failures rather than hypothetical scenarios.

### Claim 7: The deny-and-continue pattern enables graceful degradation — blocked actions return as tool results, not hard failures

- **Evidence**: Explicit design description: "When actions are blocked, Claude
  receives the denial as a tool result with instructions to find a safer path.
  Sessions terminate after 3 consecutive or 20 total denials" (escalation to human
  review in interactive mode; session termination in headless mode).
- **Confidence**: settled (first-party behavioral description of shipping feature)
- **Quote**: "When blocked, Claude receives feedback and attempts safer alternatives
  rather than halting. Sessions with 3 consecutive denials or 20 total denials
  escalate to human review (or terminate in headless mode)."
- **Our assessment**: The deny-and-continue pattern is the correct default for
  agentic systems where most blocked actions have safe alternatives. Hard-failing on
  every blocked action would make the safety system unusable — the agent would get
  stuck every time it tried a dangerous approach even when a safe alternative exists
  ("delete this branch" → blocked → "mark the branch for deletion in the tracker"
  → succeeds). The escalation thresholds (3 consecutive / 20 total) are specific
  and actionable for harness designers: the 3-consecutive threshold catches "agent
  stuck in a dangerous loop" (each attempt triggers the classifier); the 20-total
  threshold catches "agent is generally unsafe in this session" (scattered dangerous
  attempts across a long task). Headless mode termination is important: without a
  human to escalate to, the system must fail closed.

### Claim 8: Multi-agent handoff classification is bidirectional — outbound tasks are reviewed before delegation, inbound results are reviewed before reaching the orchestrator

- **Evidence**: Architectural description from the post. Handoff classifiers run
  at subagent boundaries in both directions: when the orchestrator delegates to a
  subagent (outbound), and when the subagent returns results to the orchestrator
  (inbound). The inbound review "prepends a security warning" when results appear
  to contain compromised content.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Handoff classifiers review delegated tasks and returning results,
  catching compromised subagents before their outputs reach the orchestrator."
- **Our assessment**: This bidirectional design is the correct architecture for
  multi-agent security and is not obvious from first principles. The more dangerous
  direction is inbound: a compromised subagent (hit by prompt injection in a tool
  call) can return poisoned results that cause the orchestrator to take dangerous
  actions. The outbound check prevents delegating dangerous tasks to subagents that
  lack the context to refuse; the inbound check quarantines compromised subagent
  output before it influences the orchestrator. For practitioners building multi-agent
  systems: the trust boundary should be at every agent-to-agent interface, not just
  at the human-to-orchestrator boundary.

### Claim 9: The three-tier permission structure (safe allowlist, in-project edits, classifier-evaluated) explicitly drops blanket execution permissions on entering auto mode

- **Evidence**: Explicit architectural description of the three permission tiers:
  Tier 1 — built-in safe-tool allowlist (file reads, searches, navigation) plus
  user-configured rules, Tier 2 — file edits within the project directory
  (reviewable via version control), Tier 3 — everything else (shell commands,
  web fetches, external tools, filesystem operations outside project) goes to the
  transcript classifier. Blanket code execution permissions are explicitly dropped
  when entering auto mode.
- **Confidence**: settled (first-party feature description)
- **Quote**: "Blanket code execution permissions are dropped on entering auto mode."
- **Our assessment**: The three-tier structure is notable for what it DOESN'T
  classify: file edits within the project are Tier 2 (allowed, reviewable via git),
  not Tier 3 (classifier-evaluated). This is a deliberate design choice: in-project
  file edits are the primary value-delivery action for a coding agent, and making
  them subject to classifier latency would be too disruptive. The safety bet for
  Tier 2 is that version control provides an audit trail and rollback capability —
  not that the edits are safe, but that they are recoverable. Tier 3 (shell commands,
  external network access) is where recoverable becomes questionable. This framing
  is useful for practitioners: structure your harness's permission tiers around
  reversibility, not just dangerousness.

### Claim 10: Auto mode is explicitly positioned as NOT a replacement for careful human review on high-stakes infrastructure

- **Evidence**: Direct statement in the post's explicit scope caveat: "this is
  not a drop-in replacement for careful human review on high-stakes infrastructure."
  The intended user is someone who would otherwise use the `--dangerously-skip-
  permissions` flag, not someone currently doing careful manual review.
- **Confidence**: settled (explicit vendor statement)
- **Quote**: "This is not a drop-in replacement for careful human review on
  high-stakes infrastructure, targeting users who would otherwise use the
  permissionless flag rather than those doing careful manual review."
- **Our assessment**: This is the most important scoping claim in the post.
  The 17% FNR on real overeager actions means approximately 1 in 6 dangerous
  actions will pass the classifier. For low-blast-radius workloads (personal
  projects, development environments, greenfield codebases), this is an acceptable
  miss rate. For production infrastructure, shared databases, or customer data
  systems, this miss rate is not acceptable. The guide should be explicit: auto
  mode is the right default for most day-to-day coding work; for high-stakes
  operations, human-in-the-loop approval remains necessary, and the 17% FNR
  is the honest quantification of why.

### Claim 11: The transcript classifier runs on Claude Sonnet 4.6 — model selection has safety tradeoffs

- **Evidence**: Named in the post's architecture description: "The transcript
  classifier (running on Sonnet 4.6) evaluates actions against decision criteria."
- **Confidence**: settled (first-party implementation detail)
- **Quote**: "The transcript classifier (running on Sonnet 4.6)..."
- **Our assessment**: The model choice for the safety classifier is architecturally
  significant. Sonnet 4.6 is a high-capability model — not the cheapest option
  (Haiku) — suggesting Anthropic is willing to pay classifier cost for capability.
  Running a separate Sonnet call for every Tier 3 action adds latency and cost
  to every classified action. For practitioners building custom classifiers: the
  model capability/cost/latency tradeoff for safety classifiers is not the same
  as for task execution — a cheap fast model with a higher FNR may be the wrong
  call when the missed actions are dangerous.

### Claim 12: A server-side prompt-injection probe operates as a parallel input layer, adding security warnings before hijacked content reaches the agent

- **Evidence**: Described as one of the "two defensive layers": "A server-side
  prompt-injection probe screens tool outputs before they reach the agent, adding
  warnings when content appears to be a hijack attempt."
- **Confidence**: settled (first-party architecture description)
- **Quote**: "A server-side prompt-injection probe screens tool outputs before
  they reach the agent's context, adding security warnings when hijacking attempts
  are detected."
- **Our assessment**: The input-layer probe is the defense against the prompt
  injection threat category. The output-layer classifier (the primary focus of
  the post) handles what the agent tries to do. The input layer handles what the
  agent is told to do by external content. Both layers are necessary: a classifier
  that only looks at outbound actions can be bypassed by a prompt injection that
  convinces the agent to take actions that look legitimate on their own. The
  server-side location of the probe means it operates outside the agent's context
  — it cannot be reasoned away by the agent. This parallels the reasoning-blind
  design principle: neither the input probe nor the output classifier can be
  influenced by the agent's own reasoning.

## Concrete Artifacts

### Two-Stage Classifier Pipeline

```
Claude Code Auto Mode: Transcript Classifier Pipeline
(Anthropic Engineering, 2026-03-25)

Input: Any Tier 3 action (shell command, external fetch, out-of-project
       filesystem operation)

Stage 1: Fast Single-Token Filter
  Model:  Claude Sonnet 4.6 (constrained to single-token output)
  Bias:   Toward blocking (conservative)
  Speed:  Fast (single token, minimal compute)
  Result: ALLOW (pass to execution) or FLAG (pass to Stage 2)
  FPR on real traffic: 8.5%
  FNR on real overeager actions: 6.6%

Stage 2: Chain-of-Thought Reasoning (only on flagged actions)
  Model:  Claude Sonnet 4.6 (full CoT reasoning)
  Input:  Flagged action + context (user messages + raw tool command only;
          assistant messages and tool outputs STRIPPED)
  Result: ALLOW or BLOCK
  FPR on real traffic (full pipeline): 0.4%
  FNR on real overeager actions (full pipeline): 17%
  FNR on synthetic exfiltration (full pipeline): 5.7%

On BLOCK:
  → Tool result returned to agent: "Action blocked; find a safer path"
  → Agent reattempts with alternative approach
  → After 3 consecutive denials: escalate to human (interactive) or terminate (headless)
  → After 20 total denials: same escalation
```

### Three-Slot Classifier Prompt Structure

```
Claude Code Auto Mode: Classifier Prompt Structure
(Anthropic Engineering, 2026-03-25)

FIXED SECTIONS (not user-configurable):
  - Evaluation rules (how to assess actions)
  - User-intent logic (how to infer what the user authorized)
  - Classification workflow (how to reach a verdict)

CUSTOMIZABLE SLOTS:
  Slot 1: Environment
    → Trust boundary definition
    → Which domains, buckets, services, hosts are "inside"
    → Example: "This agent operates in AWS us-east-1, within vpc-xxx"

  Slot 2: Block Rules
    → Over 20 default rules in four categories:
      (1) Destroy or exfiltrate: force-pushes, mass deletes, external data sends
      (2) Degrade security: disable logging, install persistence mechanisms
      (3) Cross trust boundaries: run external code, scan credentials
      (4) Bypass review or affect others: skip safeguards on shared infrastructure
    → View defaults: $ claude auto-mode defaults

  Slot 3: Allow Exceptions
    → Narrow carve-outs for known-safe actions that would otherwise trigger block rules
    → Example: "Allow git push to branches prefixed with 'bot-'"
```

### Three-Tier Permission Structure

```
Claude Code Auto Mode: Permission Tiers
(Anthropic Engineering, 2026-03-25)

Tier 1: SAFE ALLOWLIST — execute without classifier
  - Built-in: file reads, code searches, navigation tools
  - User-configured: additional tools the user explicitly allows
  - Note: blanket code execution permissions ARE DROPPED on entering auto mode

Tier 2: IN-PROJECT FILE EDITS — execute with audit trail
  - File edits within the project directory
  - Safety mechanism: reversible via version control
  - NOT subject to classifier evaluation (avoids classifier latency on primary work)

Tier 3: CLASSIFIER-EVALUATED — requires transcript classifier approval
  - Shell commands (Bash)
  - Web fetches and external network access
  - External MCP tools
  - Filesystem operations outside the project directory
```

### Multi-Agent Handoff Classification Pattern

```
Multi-Agent Handoff Security (Auto Mode)
(Anthropic Engineering, 2026-03-25)

OUTBOUND (Orchestrator → Subagent):
  Before delegating task to subagent:
  → Handoff classifier reviews the task being delegated
  → Can DENY delegation of dangerous tasks
  → Prevents orchestrator from inadvertently spawning dangerous subagent work

INBOUND (Subagent → Orchestrator):
  Before subagent results reach orchestrator context:
  → Handoff classifier reviews the returned results
  → On suspicious content: PREPEND security warning to results
  → Prevents compromised subagent output from influencing orchestrator actions

Design principle: trust boundaries live at every agent-to-agent interface,
not just at the human-to-agent boundary.
```

### Performance Evaluation Summary

```
Auto Mode Classifier Performance
(Anthropic Engineering, 2026-03-25, internal evaluation data)

Dataset                          | Stage 1  | Full Pipeline
---------------------------------|----------|---------------
Real traffic (n=10,000)          | 8.5% FPR | 0.4% FPR
Real overeager actions (n=52)    | 6.6% FNR | 17% FNR
Synthetic exfiltration (n=1,000) | 1.8% FNR | 5.7% FNR

FPR = False Positive Rate (legitimate actions incorrectly blocked)
FNR = False Negative Rate (dangerous actions incorrectly allowed)

Key interpretation:
  0.4% FPR: ~4 legitimate actions blocked per 1,000 — operationally viable
  17% FNR on real overeager: ~1 in 6 dangerous actions passes — not a guarantee
  5.7% FNR on exfiltration: dedicated exfil attacks have ~1 in 17 success rate
```

## Cross-References

- **Corroborates**: `blog-ccunpacked-claude-code-architecture.md` — The ccunpacked
  note documented the 3-level permission system (deny / check / prompt) and 4-tier
  context hierarchy from the leaked source. Auto mode is now the first-party
  explanation of what the "check" tier actually implements: a two-stage model-based
  classifier. The `check` tier is not a static programmatic validator — it is a
  full Sonnet 4.6 CoT reasoning call on flagged actions. The source-map discovery
  and the first-party engineering post now give us two independent views of the same
  system at different levels of abstraction.

- **Corroborates**: `failure-hooks-enforcement-2k.md` — The meloncafe note
  established that CLAUDE.md prose enforcement has a compliance ceiling and that
  hooks operating outside the context window are necessary for hard rules. Auto
  mode provides a parallel data point: the 93% blanket approval rate quantifies
  exactly the approval fatigue phenomenon that drives practitioners to build hook
  systems. Both sources diagnose the same failure mode (humans don't reliably
  enforce safety boundaries manually); they prescribe different solutions (hook-based
  programmatic enforcement vs. model-based classifier). These are complementary,
  not competing — hooks enforce structure and formatting rules; auto mode classifies
  dangerous action semantics.

- **Corroborates**: `failure-alex000kim-claudecode-source-leak.md` — The real
  incident examples in auto mode (remote git branch deletion, auth token upload)
  independently confirm the failure modes documented by alex000kim. The 23
  shell-security checks in bashSecurity.ts documented in that note now have a
  higher-level complement: the auto mode classifier handles the threat categories
  that static shell pattern matching cannot (overeager scope expansion, prompt
  injection resulting in auth token upload).

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` — Osmani's claim
  that "the bottleneck has shifted from generation to verification" maps directly
  to auto mode's architecture: the classifier is verification infrastructure applied
  at the action level. Osmani's gradual-trust-building framework is also instantiated
  here: Tier 1 (safe allowlist) → Tier 2 (project edits) → Tier 3 (classifier) is
  a risk-graduated permission structure rather than binary allow/deny.

- **Extends**: `blog-ccunpacked-claude-code-architecture.md` — Provides the
  first-party definition of the "check" permission tier that ccunpacked documented
  from source maps. The ccunpacked note noted this tier "is the most interesting
  for harness design: it allows custom hooks or validators to approve/reject tool
  calls automatically." Auto mode confirms this: the check tier is a model-based
  classifier, and practitioners can customize it via the three-slot prompt structure.

- **Novel**:
  - **The two-stage classifier pattern** (fast single-token filter → CoT reasoning
    only on flagged actions) is not documented in any other corpus source. The
    performance table (8.5% → 0.4% FPR) is the first quantified safety metric
    for a production AI coding tool permission system in our corpus.
  - **The reasoning-blind classifier design** as an explicit principle (strip
    assistant messages from the safety input to prevent self-justification) is
    new to the corpus. No other source articulates this design decision explicitly.
  - **The deny-and-continue pattern** with specific escalation thresholds (3
    consecutive / 20 total denials) is first documented here. The meloncafe note
    describes hook-based blocking but not graceful reattempt-with-feedback.
  - **The bidirectional multi-agent handoff classification** (outbound task review
    + inbound result review with security warning prepend) is not described in
    any other corpus source. The ttal and cursor multi-agent notes focus on
    coordination patterns; this is the first source documenting the trust boundary
    architecture at subagent interfaces.
  - **The 17% FNR honest acknowledgment** on real overeager actions is unprecedented
    vendor transparency. No other corpus source provides quantified failure rates
    for a production safety mechanism.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Auto mode should anchor the "automated
  permission gating" section. Current corpus covers hooks (meloncafe) and settings.json
  (Sentry/tin) as enforcement mechanisms; auto mode adds a third primitive: model-based
  classifier as a middle tier. The three-tier permission structure (safe allowlist /
  project edits / classifier-evaluated) is a cleaner framework than binary allow/deny
  for explaining to practitioners how to think about tool permissions. Recommend
  updating the permission section to present all three enforcement primitives:
  (1) allowlist via settings.json for known-safe actions, (2) hooks for structural
  rule enforcement, (3) model-based classifiers for semantic danger evaluation.

- **Chapter 03 (Safety and Verification)**: The four-category threat model (overeager,
  honest mistake, prompt injection, misaligned model) and the four-category block rule
  taxonomy should be extracted as a checklist for any agentic system design review.
  The 17% FNR on real overeager actions is the quantified honest safety ceiling for
  model-based permission gating — cite this whenever the guide discusses automated
  safety systems to prevent overconfidence. The explicit Anthropic caveat ("not a
  drop-in replacement for careful human review on high-stakes infrastructure") should
  be cited verbatim in any chapter section that recommends auto mode or analogous
  classifier-based approaches.

- **Chapter 03 (Multi-Agent Security)**: The bidirectional handoff classification
  pattern (outbound + inbound review at every subagent boundary) should be the
  canonical architecture recommendation for multi-agent systems handling sensitive
  operations. Currently no corpus source addresses this explicitly. Add: "Trust
  boundaries belong at every agent-to-agent interface. Classify both delegated tasks
  (outbound) and returned results (inbound). An orchestrator compromised by a
  poisoned subagent result is a realistic threat class."

- **Chapter 02 (Context Engineering / System Prompt Design)**: The reasoning-blind
  classifier principle has direct implications for how practitioners should think
  about self-consistency in agentic systems. When the agent's own reasoning
  cannot influence the safety classifier, it closes a manipulation vector. For
  harness authors building custom validators: evaluate actions against original
  user intent, not the agent's accumulated reasoning about those actions.

## Extraction Notes

- **Source quality**: This is a first-party Anthropic engineering post. Metrics
  are sourced from internal Anthropic evaluations and should be treated as accurate
  for the specific models and datasets evaluated (Sonnet 4.6, as-of-March-2026
  baseline data). These metrics will change as models evolve.
- **Model-specific**: The classifier runs on Sonnet 4.6. Performance metrics are
  for Sonnet 4.6 as of March 2026. Teams building analogous classifiers on other
  models or versions should re-evaluate.
- **Dataset transparency**: The real overeager actions dataset (n=52) is small
  enough that the 17% FNR (roughly 9 missed actions) has wide confidence intervals.
  The synthetic exfiltration dataset (n=1,000) is more statistically robust.
  The 17% FNR on 52 instances is the most honest and most useful metric (real
  observed failures), but practitioners should not over-interpret a number from
  a small sample.
- **No linked sub-pages followed**: The article is a single page without substantive
  linked sub-pages. The `claude auto-mode defaults` command output is not published
  in the post; practitioners need to run it locally to see the full 20+ block rule list.
- **Prospector alignment**: The Prospector's triage correctly identified all nine
  key extraction targets. All were found and extracted: two-stage classifier
  architecture, reasoning-blind design, three-slot prompt structure, 93% approval
  fatigue rate, four threat categories, deny-and-continue pattern, multi-agent
  handoff security, real incident examples, and 17% FNR metric.
