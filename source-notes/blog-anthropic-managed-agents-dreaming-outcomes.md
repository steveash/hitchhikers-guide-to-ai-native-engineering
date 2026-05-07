---
source_url: https://claude.com/blog/new-in-claude-managed-agents
source_type: blog-post
title: "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration"
author: Anthropic (product announcement)
date_published: 2026-05-06
date_extracted: 2026-05-07
last_checked: 2026-05-07
status: current
confidence_overall: anecdotal
issue: "#550"
---

# New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

> Anthropic's May 2026 feature-update announcement for Claude Managed Agents, graduating
> outcome mode and multiagent orchestration from research preview to public beta, introducing
> dreaming (scheduled session-memory curation for cross-session agent improvement), adding
> webhooks for async outcome notification, and providing four new customer case studies with
> concrete performance figures — including Harvey's ~6x completion rate improvement from
> dreaming and Wisedocs' 50% faster document reviews from outcome grading.

## Source Context

- **Type**: blog-post (official Anthropic product update announcement, claude.com blog,
  May 6 2026; follow-up to the April 8 2026 launch of Claude Managed Agents)
- **Author credibility**: First-party Anthropic announcement — maximum authority on what
  the platform provides. Four named enterprise customer examples (Harvey, Netflix, Spiral
  by Every, Wisedocs) with specific deployment descriptions and performance figures, raising
  them above generic marketing copy. Performance figures are from internal or customer
  testing, not independently replicated. The blog post is marketing copy; no accompanying
  technical documentation was fetched for this extraction.
- **Scope**: Covers what graduated from research preview to public beta (outcomes, multiagent
  orchestration), what is newly added as research preview (dreaming), what new capabilities
  are available (memory, webhooks), and how four named customers are using the new features.
  Does NOT cover: API design specifics, SDK integration patterns, how dreaming determines
  what patterns to extract, how the separate-grader isolation works technically, or pricing
  updates. The April 8 2026 launch post (`blog-anthropic-claude-managed-agents.md`) remains
  the canonical reference for the full platform capability list and initial pricing.

## Extracted Claims

### Claim 1: Dreaming is a scheduled background process that reviews session history and memory stores to extract patterns, enabling agents to improve over time without developer intervention

- **Evidence**: First-party Anthropic feature description. Dreaming is in research preview
  at time of announcement and requires separate access request. Harvey's reported ~6x
  completion rate improvement is corroborating customer evidence.
- **Confidence**: anecdotal (vendor feature description + single customer test result;
  research preview, not broadly available)
- **Quote**: "Dreaming is a scheduled process that reviews your agent sessions and memory
  stores, extracts patterns, and curates memories so your agents improve over time."
- **Our assessment**: This is the most architecturally novel feature in the announcement.
  Every other approach to agent improvement in our corpus requires explicit developer action:
  updating prompts, revising CLAUDE.md, or rewriting harness logic. Dreaming is the first
  mechanism in the corpus that closes the improvement loop automatically from session history.
  The implication is significant: an agent deployed on Managed Agents will behave differently
  at month 2 than at month 1 without any developer code changes, because dreaming has updated
  its memory. This changes the baseline assumption for agent harness design — the agent is
  not a static artifact. The Harvey result (~6x completion rate improvement) is the strongest
  quantitative signal for what this mechanism can deliver, though it is a single customer's
  internal test.

### Claim 2: Dreaming actively restructures memory to maintain signal quality, not simply accumulate everything the agent has seen

- **Evidence**: Feature description from Anthropic. The specific framing of "restructures"
  (not "appends" or "logs") implies active pruning, reweighting, or synthesis of memories
  as the memory store grows.
- **Confidence**: anecdotal (vendor description; technical mechanism not explained)
- **Quote**: "restructures memory so it stays high-signal as it evolves"
- **Our assessment**: The distinction between accumulation and curation is architecturally
  important. A naive memory system that simply appends every session's outputs will degrade
  in quality as the memory grows — contradictory observations, outdated patterns, and noise
  accumulate. The claim that dreaming "restructures" memory suggests a synthesis or
  prioritization step, not just logging. The mechanism is not described in this announcement
  post; it likely lives in the platform documentation. For practitioners, the implication
  is that dreaming handles the memory hygiene problem they would otherwise need to solve
  themselves — analogous to how the orchestration harness handles context management.

### Claim 3: Harvey's legal document coordination agents achieved approximately 6x completion rate improvement by using dreaming to retain cross-session learnings about tool-specific patterns and file format workarounds

- **Evidence**: Harvey customer case study. The figure is from Harvey's own tests, not
  Anthropic's internal benchmark. Harvey builds AI-native legal tools for enterprise law firms;
  their use case requires consistent handling of complex legal document formats. The specifics
  (filetype workarounds, tool-specific patterns) are concrete and credible for a document-
  intensive legal domain.
- **Confidence**: anecdotal (single customer, internal test, not independently replicated)
- **Quote**: "With dreaming, their agents remember what they learned between sessions,
  including filetype workarounds and tool-specific patterns. Completion rates went up ~6x
  in their tests."
- **Our assessment**: The ~6x figure is striking and deserves careful interpretation. The
  baseline (before dreaming) was likely a zero-memory agent that re-encountered the same
  file format problems on each session. If the agent previously failed on a specific filetype
  workaround 60% of the time and now succeeds near 100%, that produces the ~6x ratio. The
  "filetype workarounds" framing is important: these are edge cases that a developer cannot
  easily anticipate in advance but that recur in practice. This is exactly the class of
  problem dreaming is designed to address — patterns that emerge from production use and
  cannot be fully specified at design time. This is the largest performance improvement
  metric from a platform capability (not a base model improvement) in our corpus.

### Claim 4: The outcomes grader operates in a separate context window, architecturally isolated from the agent's reasoning chain to prevent evaluation contamination

- **Evidence**: Feature description from Anthropic. This is an explicit design choice —
  a separate context window means the grader cannot see the agent's intermediate reasoning,
  only the final output and the evaluation rubric. The April 2026 announcement described
  outcomes as self-evaluation but did not specify this isolation mechanism.
- **Confidence**: settled (explicit architectural design decision from first-party source)
- **Quote**: "A separate grader evaluates the output against your criteria in its own
  context window, so it isn't influenced by the agent's reasoning."
- **Our assessment**: This is the most technically important claim in the announcement for
  harness engineers. The failure mode it guards against is documented in
  `blog-anthropic-harness-long-running.md` and `blog-anthropic-multi-agent-coordination-patterns.md`:
  the "early victory problem" — an evaluator that shares context with the generator will
  rationalize acceptance rather than genuinely evaluate. By giving the grader its own context
  window, the platform enforces the generator-verifier separation at the execution level,
  not just the prompt level. Practitioners building DIY outcomes loops should replicate this
  architectural isolation: do not pass the agent's reasoning chain to the evaluator, only the
  output and the rubric.

### Claim 5: Outcomes graduated from research preview to public beta with more specific benchmarks — +8.4% task success on docx generation and +10.1% on pptx generation

- **Evidence**: Vendor benchmark metrics from internal testing. The April 8 2026
  announcement stated "up to +10 points" generically; the May 6 update provides per-filetype
  breakdowns on the same task class (structured file generation). These figures are
  consistent with and more specific than the April figures.
- **Confidence**: anecdotal (internal Anthropic benchmark; no independent replication;
  specific task type, not a general improvement figure)
- **Quote**: "outcomes improved task success by up to 10 points" with specific figures of
  "+8.4% task success on docx and +10.1% on pptx"
- **Our assessment**: The per-filetype breakdown is more useful than the general "+10 points"
  figure from April because it surfaces where the outcomes loop adds the most value: pptx
  (+10.1%) benefits more than docx (+8.4%), which is consistent with pptx being a more
  complex multi-element format with harder-to-specify correctness criteria. The "up to"
  qualifier still applies — these are ceiling figures, not averages. The public beta
  graduation means these features are now accessible to all Managed Agents developers, not
  just research preview participants. The April note flagged these as research preview claims
  that most practitioners couldn't test; this update removes that caveat.

### Claim 6: Multiagent orchestration graduated from research preview to public beta, enabling a lead agent to delegate to specialists that each carry their own model, system prompt, and toolset

- **Evidence**: Feature description from Anthropic. The architecture described — lead
  agent plans and delegates, specialists execute with dedicated configurations — is the
  orchestrator-subagent pattern from `blog-anthropic-multi-agent-coordination-patterns.md`,
  now available as a first-class platform primitive.
- **Confidence**: anecdotal (vendor feature description; public beta status is
  authoritative from first-party source)
- **Quote**: "When there is too much work for a single agent to do well, multiagent
  orchestration lets a lead agent break the job into pieces and delegate each one to a
  specialist with its own model, prompt, and tools."
- **Our assessment**: The critical architectural detail is "its own model, prompt, and
  tools" — each specialist is independently configured, not a clone of the lead agent.
  This enables cross-model delegation patterns (Claim 8 below: Haiku lead → Opus workers)
  and task-specialized configurations that would require complex harness engineering in a
  DIY system. The platform handles the wiring: how do specialists receive work, how do they
  return outputs, and how does the lead agent integrate them. This was previously available
  only as a research preview with separate access request; the graduation to public beta is
  the key status change from the April announcement.

### Claim 7: Specialist subagents in the multiagent architecture share a common filesystem, enabling coordination through shared state rather than requiring all inter-agent communication to pass through the lead agent

- **Evidence**: Feature description from Anthropic. The shared filesystem model allows
  one specialist to write output that another specialist can read directly, without round-
  tripping through the orchestrator — this directly addresses the information bottleneck
  failure mode for orchestrator-subagent identified in
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 3.
- **Confidence**: anecdotal (vendor feature description; mechanism is described but not
  technically detailed in the announcement)
- **Quote**: "These specialists work in parallel on a shared filesystem and contribute to
  the lead agent's overall context."
- **Our assessment**: The shared filesystem is a partial implementation of the
  orchestrator-subagent + shared state hybrid documented in
  `blog-anthropic-multi-agent-coordination-patterns.md` Claim 11 as "the common production
  pattern." Files written by one specialist are visible to others and feed back into the
  lead agent's context. This means cross-cutting findings from one specialist are not lost
  in the handoff — the specific failure mode the multi-agent coordination patterns post
  identified for pure orchestrator-subagent. The "contribute to the lead agent's overall
  context" phrase is important: outputs don't just go to a final synthesis step; they
  continuously update what the lead agent knows as work progresses.

### Claim 8: Cross-model delegation — using a cheaper/faster model as lead orchestrator and a more capable model for specialist execution — is a validated production pattern in the multiagent architecture

- **Evidence**: Spiral by Every customer case study. The lead agent runs on Haiku
  (Anthropic's fastest, lowest-cost model); specialist subagents that produce drafts run on
  Opus (Anthropic's most capable model). Quality enforcement is handled by outcomes grading
  against editorial principles and user voice from memory. The cost-capability tradeoff is
  deliberate: orchestration tasks (planning, delegating, routing) fit Haiku; generation tasks
  (drafting to quality standards) require Opus.
- **Confidence**: anecdotal (single named customer case study)
- **Quote**: (no direct verbatim quote for this specific claim; described as narrative in
  the source — the lead agent runs on Haiku, specialists delegate drafting to Opus, outcomes
  enforce quality against editorial principles and user voice pulled from memory)
- **Our assessment**: This is the most architecturally specific customer example in the
  announcement and the most useful for practitioners designing cost-aware multiagent systems.
  The pattern — cheap model for coordination overhead, expensive model for quality-critical
  execution — is economically rational but requires the platform to support per-agent model
  configuration. The combination with outcomes grading means Haiku orchestrates, Opus drafts,
  and outcomes enforce quality standards — three distinct layers with three different
  model/mechanism choices. This is more sophisticated than any DIY harness example in our
  existing corpus, and it uses the three new features (multiagent orchestration, outcomes,
  and memory for user voice) in combination.

### Claim 9: Netflix built a multiagent analysis pipeline on Managed Agents that processes logs from hundreds of builds in parallel to identify recurring issues affecting thousands of applications

- **Evidence**: Netflix customer case study. The scale (hundreds of builds, thousands of
  applications) is specific. The use case (parallel log analysis for recurring issue
  identification) is a classic large-scale data analysis task where multiagent parallelization
  produces meaningful throughput gains.
- **Confidence**: anecdotal (named customer, no performance figures provided)
- **Quote**: "Netflix's platform team built an analysis agent that processes logs from
  hundreds of builds across different sources"
- **Our assessment**: The Netflix case study validates multiagent orchestration at production
  infrastructure scale. Processing hundreds of builds simultaneously with a single-agent
  approach would either be too slow (sequential) or require complex DIY parallelization
  infrastructure. Managed Agents' shared filesystem and per-specialist tool configuration
  make the parallel log analysis architecture feasible without custom orchestration code.
  The absence of performance metrics (throughput, time-to-insight) makes this a qualitative
  validation rather than a quantitative one.

### Claim 10: Wisedocs achieved 50% faster document quality reviews by using outcome grading against internal guidelines, without sacrificing alignment with team standards

- **Evidence**: Wisedocs customer case study. The 50% speed improvement is from the
  customer's own measurements, not an Anthropic benchmark. The "while staying aligned with
  their team's standards" qualifier addresses the common concern that automated grading
  produces different results than human review.
- **Confidence**: anecdotal (single named customer, self-reported figure)
- **Quote**: "Reviews now run 50% faster, while staying aligned with their team's
  standards."
- **Our assessment**: The Wisedocs case study is the cleanest before/after figure in the
  announcement: 50% faster with maintained quality. The use of outcomes for document quality
  review (grade each document against internal guidelines) is a direct application of the
  pattern Anthropic demonstrated in internal benchmarks (+8.4%/+10.1% task success). The
  "while staying aligned" qualifier is significant: it implies Wisedocs tested whether the
  automated grading matched what human reviewers would say. The mechanism is not described
  (did they validate the rubric against historical human reviews?) but the claim is specific
  enough to be credible.

### Claim 11: Webhooks enable an asynchronous fire-and-forget pattern for long-running outcome-driven tasks

- **Evidence**: Feature description. The pattern described — define outcome, trigger agent,
  receive webhook notification when done — removes the requirement for the calling system
  to poll or maintain an open connection during agent execution.
- **Confidence**: settled (explicit feature description from first-party source)
- **Quote**: "You can also now define an outcome, let the agent run, and get notified by
  a webhook when it's done."
- **Our assessment**: Webhooks are the correct integration pattern for long-running agents
  in web application contexts. Polling for agent completion burns resources and creates
  unnecessary dependencies on session persistence at the calling application level. The
  webhook model is architecturally important because it decouples the triggering application
  from the agent's execution time — the caller doesn't need to stay alive or connected.
  This is particularly valuable for the long-running sessions that Managed Agents supports
  (multi-hour autonomous operation per the April announcement). Combined with outcomes,
  the webhook pattern is: "tell the agent what success looks like, fire and forget, get
  notified when it gets there."

### Claim 12: Memory enables agents to capture and retain what they learn during a session, which dreaming then refines between sessions

- **Evidence**: Feature description. The two-tier model — memory for in-session capture,
  dreaming for cross-session refinement — is an explicit architectural design choice.
  Memory is in public beta; dreaming is in research preview.
- **Confidence**: anecdotal (vendor feature description; mechanism for how dreaming
  selects what to refine is not described)
- **Quote**: Memory enables agents to "capture what it learns as it works," while dreaming
  refines that memory between sessions.
- **Our assessment**: The two-tier architecture is important for understanding what dreaming
  requires: memory must be populated (session learning captured) before dreaming has anything
  to process. An agent deployed without memory enabled would have nothing for dreaming to
  curate. This means the adoption path is: enable memory first, run sufficient sessions to
  build a signal-rich memory store, then enable dreaming to begin refinement. The Harvey
  result implies the compound effect of memory + dreaming is large; memory alone (without
  dreaming refinement) would produce a different (likely lower) improvement trajectory.

## Concrete Artifacts

### Feature Status Matrix (May 6, 2026 vs. April 8, 2026)

```
# Claude Managed Agents feature availability change
# Source: claude.com/blog/new-in-claude-managed-agents, May 6 2026
# Baseline: claude.com/blog/claude-managed-agents, April 8 2026

Feature                    | April 8 Status         | May 6 Status
---------------------------|------------------------|------------------
Outcome mode               | Research preview       | Public beta
Multiagent coordination    | Research preview       | Public beta
Memory                     | (not announced)        | Public beta
Dreaming                   | (not announced)        | Research preview
Webhooks                   | (not announced)        | Available

NOTES:
- Research preview = separate access request required
- Public beta = available to all Managed Agents developers
- Dreaming requires access request through Managed Agents form
```

### Multiagent Architecture (from announcement)

```
# Multiagent orchestration pattern as implemented in Managed Agents
# Source: claude.com/blog/new-in-claude-managed-agents, May 6 2026

LEAD AGENT:
  - Plans and decomposes the task
  - Delegates subtasks to specialists
  - Maintains overall context (fed by specialist outputs)
  - Model: configurable (can use cheaper model — e.g., Haiku per Spiral case study)

SPECIALIST SUBAGENTS:
  - Each has: own model, own system prompt, own toolset
  - Work in parallel
  - Share a common filesystem (can read each other's outputs)
  - Contribute outputs to lead agent's context
  - Model: configurable (can use capable model — e.g., Opus per Spiral case study)

OBSERVABILITY:
  - Claude Console traces: which agent did what, in what order, why
  - "Full visibility into how your task was delegated and executed"

CROSS-MODEL DELEGATION PATTERN (Spiral by Every):
  Lead:        Haiku (planning, orchestration)
  Specialists: Opus  (drafting, quality work)
  Quality:     Outcomes (rubric = editorial principles + user voice from memory)
```

### Dreaming + Memory Architecture (from announcement)

```
# Two-tier agent learning model in Managed Agents
# Source: claude.com/blog/new-in-claude-managed-agents, May 6 2026

TIER 1: MEMORY (Public Beta)
  Scope:     In-session
  Mechanism: Agent captures what it learns as it works
  Output:    Memory store (persists across sessions)

TIER 2: DREAMING (Research Preview)
  Scope:     Cross-session (scheduled background process)
  Input:     Agent sessions + memory stores
  Operations:
    - Reviews sessions for patterns
    - Extracts recurring patterns (mistakes, converged workflows, team preferences)
    - Curates memories for high signal
    - Restructures memory store (prunes low-signal, reinforces high-signal)
  Output:    Refined memory store

ADOPTION PATH:
  1. Enable memory (in-session capture)
  2. Run sufficient sessions to build memory store
  3. Enable dreaming (request access) for cross-session refinement
  4. Dreaming fires on schedule; agent improves between sessions automatically

HARVEY OUTCOME:
  Memory content: filetype workarounds, tool-specific patterns
  Result after dreaming: ~6x completion rate improvement in their tests
```

### Outcomes Benchmark (May 2026 refinement)

```
# Outcome mode performance figures
# Source: claude.com/blog/new-in-claude-managed-agents, May 6 2026
# Compare: April 8 2026 announcement ("up to +10 points" generic)

Task class:      Structured file generation
Comparison:      Outcomes loop vs. standard prompting loop
Overall figure:  Up to +10 points task success improvement (consistent with April)
Per-file-type:
  - docx:  +8.4% task success
  - pptx:  +10.1% task success

Isolation mechanism:
  - Separate grader in its own context window
  - Grader not influenced by agent's reasoning chain
  - Developer provides success rubric; grader scores output against rubric
  - Agent iterates until rubric criteria met (or iteration limit reached)
```

### Customer Deployment Evidence (May 2026)

```
# Customer cases from May 6 announcement
# Source: claude.com/blog/new-in-claude-managed-agents, May 6 2026

Company        | Feature Used              | Outcome                           | Domain
---------------|---------------------------|-----------------------------------|----------------
Harvey         | Dreaming + Memory         | ~6x completion rate improvement   | Legal documents
Netflix        | Multiagent orchestration  | Parallel log analysis, 100s builds| Platform/infra
Spiral/Every   | Multiagent + Outcomes     | Haiku→Opus delegation + quality   | Publishing/media
Wisedocs       | Outcomes                  | 50% faster document review        | Document review

HARVEY DETAIL:
  Use case: Complex legal document coordination
  Memory captures: Filetype workarounds, tool-specific patterns
  Mechanism: Dreaming retains cross-session learnings
  Metric: Completion rates ~6x in internal tests

NETFLIX DETAIL:
  Use case: Build log analysis across distributed sources
  Scale: Hundreds of builds, thousands of applications
  Mechanism: Multiagent orchestration (parallelizes across build sources)
  Metric: None provided

SPIRAL BY EVERY DETAIL:
  Use case: Content drafting with consistent editorial quality
  Architecture: Haiku lead → Opus specialist drafters
  Quality enforcement: Outcomes grading against editorial principles + user voice from memory
  Metric: None provided (qualitative improvement)

WISEDOCS DETAIL:
  Use case: Document quality review against internal guidelines
  Mechanism: Outcomes grading against internal guidelines rubric
  Metric: 50% faster while maintaining alignment with team standards
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-managed-agents.md` Claim 4 — The April "+10 points task success"
    on structured file generation is confirmed and refined: May provides per-filetype
    breakdown (+8.4% docx, +10.1% pptx) that is consistent with but more specific than
    the April figure. The figures are not in tension; the May post is a refinement within
    the same benchmark. April described the outcome loop as "improving task success by up
    to 10 points"; May confirms this holds and adds task-specific granularity.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 11 — "Production systems
    often combine patterns. A common hybrid uses orchestrator-subagent for overall workflow
    with shared state for collaboration-heavy subtasks." The multiagent architecture here
    (shared filesystem, specialists contributing to lead agent context) is a platform-level
    implementation of exactly this hybrid. Specialists coordinate through the shared
    filesystem (shared state), while the lead agent maintains overall workflow control
    (orchestrator-subagent). The Anthropic coordination patterns post described this hybrid
    as the "common" production pattern; the Managed Agents update embeds it as the default
    architecture.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 4 — "Agent teams differ
    from subagents in context persistence — subagents are bounded; teammates are persistent
    and accumulate context." Dreaming's effect on memory aligns with this: agents using
    dreaming develop persistent cross-session context (accumulated and refined by dreaming),
    moving toward the agent-teams end of the subagent↔teammate spectrum even though they
    are implemented as session-bounded agents.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2 — "The verifier is only
    as good as its criteria." The outcomes grader's isolated context window (Claim 4 above)
    is the platform-level enforcement of the explicit-criteria requirement. The "early
    victory problem" — verifier rubber-stamps without explicit criteria — is the failure mode
    outcomes guards against by requiring developers to write a success rubric before the
    agent runs.

- **Contradicts**: None filed. The most significant status changes in this post (research
  preview → public beta for outcomes and multiagent orchestration) are updates to
  availability, not contradictions of prior claims. The April note accurately described
  the status as of April 8; this post documents the subsequent graduation. No prior corpus
  source makes claims about dreaming, memory, or webhooks that this post contradicts.
  
  The nearest conceptual tension is with `blog-cursor-real-time-rl.md`: Cursor's approach
  to agent improvement is real-time RL weight updates from production user signals; Managed
  Agents' approach is memory curation via dreaming from session history. These are different
  mechanisms for "agents improve over time" — one modifies model weights, the other modifies
  the memory context. They serve different agent deployment contexts (a hosted model training
  pipeline vs. a deployed agent runtime) and are not contradictions; they are parallel
  solutions at different system layers.

- **Extends**:
  - `blog-anthropic-claude-managed-agents.md` — This post is the direct sequel to the
    April 8 launch. It extends the April note in four concrete ways: (1) graduates outcomes
    and multiagent orchestration from research preview to public beta, removing the "most
    practitioners can't test this" caveat in the April extraction notes; (2) adds dreaming
    as a new capability not present in April; (3) adds memory as a new public beta capability;
    (4) adds webhooks for async integration patterns. The April note's Extraction Notes
    flagged: "The self-evaluation outcome loop and multi-agent coordination are both in
    research preview with separate access requests." This post resolves that caveat.
  - `blog-anthropic-multi-agent-coordination-patterns.md` — The Spiral by Every case study
    (Haiku lead → Opus workers, outcomes quality enforcement, memory for user voice) is the
    most sophisticated multi-pattern combination in our corpus. It extends the patterns
    post by providing a live production example that combines orchestrator-subagent
    (Haiku→Opus delegation), outcomes (grading against editorial rubric), and memory (user
    voice persistence) — three of the platform's most complex capabilities together.
  - `blog-anthropic-harness-long-running.md` — Dreaming is a platform-level implementation
    of the cross-session learning that the harness-long-running post identified as a design
    challenge for production long-running agents. That post documented the need for agents
    to improve from their own run history; dreaming is the Managed Agents answer to that
    need. The April note made this connection at the pattern level; this post provides
    quantitative evidence (Harvey's ~6x) of what the mechanism can deliver.

- **Novel**:
  - **Dreaming: scheduled memory curation as a first-class platform feature** — No prior
    corpus source describes an automated background process that reviews agent session
    history and curates memory to improve future agent behavior. This is the first mechanism
    in the corpus that closes the agent improvement loop without developer action.
  - **~6x completion rate improvement from cross-session memory retention** — Harvey's
    result is the largest documented performance improvement in the corpus from a platform
    infrastructure feature (not a base model improvement). Prior platform infrastructure
    improvements are measured in percentage points ("+10 points on structured file
    generation"); Harvey's result is a multiplier.
  - **Cross-model delegation (Haiku orchestrator → Opus workers) as a named production
    pattern** — No prior corpus source documents the deliberate pairing of a
    cheap/fast model for orchestration overhead with a capable/expensive model for
    quality-critical execution in a single multiagent system. Spiral by Every is the
    first production implementation with named models.
  - **Isolated grader context window as an architectural countermeasure against evaluator
    contamination** — The Anthropic multi-agent coordination patterns post named the
    "early victory problem"; this post documents the platform-level countermeasure
    (separate context window for the grader). The mechanism — not the problem — is new.
  - **Webhook-triggered async outcome completion** — The fire-and-forget pattern for
    long-running agent tasks (define outcome, trigger, receive webhook when done) is not
    documented in any other corpus source as a named integration pattern.
  - **Two-tier agent memory architecture (in-session capture via memory + cross-session
    refinement via dreaming)** — No prior corpus source describes a staged memory system
    where the first tier captures and the second tier curates. This is architecturally
    distinct from simple persistence (which just stores everything).

## Guide Impact

- **Chapter 04 or Chapter 05 (Agent Orchestration)**: Add dreaming as the platform-level
  answer to cross-session agent improvement — the first mechanism in the guide's corpus
  that closes the improvement loop without developer code changes. Frame it as: "on Managed
  Agents, dreaming handles what you would otherwise have to engineer yourself: extracting
  recurring patterns from session history and refining agent memory." The Harvey ~6x
  improvement should anchor this section as the strongest available evidence for the
  mechanism's impact. Note the adoption prerequisite: memory must be enabled first.

- **Chapter 02 (Harness Engineering)**: The isolated grader context window (Claim 4) should
  update any section on outcome-loop or generator-verifier harness design. The architectural
  principle is: **do not pass the agent's reasoning chain to the evaluator; only pass the
  output and the rubric.** This is a concrete implementation requirement that the existing
  corpus identified as a problem (early victory problem) but did not specify a countermeasure
  for. Any DIY outcomes loop should implement this isolation.

- **Chapter 02 (Harness Engineering / Build-vs-Buy)**: The public beta graduation of
  outcomes and multiagent orchestration removes the "research preview only" caveat from the
  April source note. The guide's build-vs-buy framing should update: these are now generally
  available features, not forward-looking capabilities. Practitioners evaluating Managed
  Agents today can access outcome grading and multiagent delegation without requesting
  separate access. The Wisedocs (+50% speed), Harvey (~6x completion), and Spiral (cross-
  model delegation with outcome quality) cases provide the strongest production evidence
  for the platform's value in May 2026.

- **Chapter 04 (Multi-Agent Patterns)**: Add the Haiku-orchestrator/Opus-worker pattern
  (Claim 8) as a named cost-aware multiagent design pattern. Frame it as: "use a cheaper,
  faster model for orchestration overhead (planning, routing, coordination) and reserve
  expensive model capacity for the quality-critical execution work." This pattern is
  enabled by per-specialist model configuration in Managed Agents and is a generalizable
  design principle for any multiagent system with heterogeneous task requirements. Combine
  with outcomes grading to enforce quality standards on the capable-model outputs.

- **Chapter 04 (Multi-Agent Patterns)** or **Chapter 06 (Production Deployment)**:
  Document the shared filesystem as the solution to the orchestrator-subagent information
  bottleneck. The multi-agent coordination patterns post named the failure mode; this post
  documents the platform-level countermeasure. The principle: "cross-cutting specialist
  findings should be accessible to other specialists through a shared artifact layer, not
  exclusively through the orchestrator." The shared filesystem is the implementation; the
  principle applies to DIY systems too (shared git worktree, shared database, shared cache).

- **Chapter 06 (Production Deployment)**: Add the webhook fire-and-forget pattern (Claim 11)
  as the recommended integration pattern for long-running outcome-driven agents. "Poll for
  completion" is the naive pattern; "define outcome + webhook on completion" is the
  production-grade pattern. Any guide section on integrating long-running agents into
  existing web applications should specify this pattern.

- **Chapter 02 (Harness Engineering)** or **Chapter 05 (Long-Running Sessions)**: Update the
  April note's claim that outcome mode and multi-agent coordination require separate access
  requests. As of May 6 2026, both are in public beta and accessible to all Managed Agents
  developers. The guide should reflect the current availability status.

## Extraction Notes

- This is a product feature update announcement, not an engineering post. Mechanism-level
  details (how dreaming selects patterns to extract, how the outcomes grader is implemented,
  how specialists coordinate through the shared filesystem) live in the platform documentation
  at platform.claude.com/docs and were not fetched for this extraction. A follow-up
  extraction of the updated Managed Agents documentation would be warranted.
- The source was fetched via WebFetch across multiple calls to verify verbatim quotes.
  All quotes used in this note were confirmed across at least two independent fetches.
  Customer case study descriptions for Netflix and Spiral by Every were provided in
  narrative form in the source; no direct customer quotes were available for those cases.
- The April 8 2026 source note (`blog-anthropic-claude-managed-agents.md`) contains an
  Extraction Notes caveat: "The self-evaluation outcome loop and multi-agent coordination
  are both in research preview with separate access requests." This caveat is now outdated
  as of May 6. The guide should note the status change.
- Dreaming remains in research preview at time of extraction (May 7 2026). Harvey's ~6x
  figure is from an early adopter in the research preview cohort. The figure should be
  presented as the best available evidence, not a guaranteed result for all users.
- The Prospector's triage noted to check `blog-cursor-real-time-rl.md` for overlaps with
  dreaming/outcomes features. That note covers real-time RL weight updates from production
  user signals — a different mechanism from dreaming's in-context memory curation. The
  conceptual family resemblance (both improve agents from their own past performance) is
  noted in Cross-References but does not rise to a contradiction.
- `registry/sources.json` was checked; existing entries follow the schema shown. This
  source's entry was added following that schema.
- Overall confidence is set to `anecdotal` because all performance figures are either
  Anthropic's own internal benchmarks or single-customer self-reported results. No
  independent replication of any metric in this announcement is available at time of
  extraction.
