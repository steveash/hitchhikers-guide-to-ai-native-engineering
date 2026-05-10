---
source_url: https://claude.com/blog/new-in-claude-managed-agents
source_type: blog-post
title: "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration"
author: Anthropic (product announcement)
date_published: 2026-05-06
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: anecdotal
issue: "#550"
---

# New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

> Follow-up Anthropic product announcement (May 6, 2026) promoting outcomes and
> multiagent orchestration from research preview to public beta, and introducing
> dreaming — a scheduled cross-session pattern-extraction process — as the first
> mechanism in the corpus for platform-level agent self-improvement between sessions.

## Source Context

- **Type**: blog-post (official Anthropic product announcement, claude.com blog,
  May 6, 2026; feature update to Claude Managed Agents, which launched April 8, 2026)
- **Author credibility**: First-party Anthropic announcement — authoritative on what
  the platform provides and which features are in which access tier. Customer examples
  are from named companies (Harvey, Netflix, Spiral by Every, Wisedocs) without named
  individual testimonials, which lowers evidential weight relative to the April
  announcement's eight named executives. Performance benchmarks (docx/pptx task success)
  are Anthropic internal tests, not independently replicated.
- **Scope**: Covers four feature updates: dreaming (new, research preview), outcomes
  (promoted from research preview to public beta), multiagent orchestration (promoted
  from research preview to public beta), and webhooks (new, available). Also references
  memory (public beta, previously announced April 23 in a separate post) as the
  foundation dreaming extends. Does NOT cover: API design specifics, SDK integration
  code, memory architecture mechanics, or pricing updates.

## Extracted Claims

### Claim 1: Dreaming is a scheduled, asynchronous, cross-session process that reviews past agent sessions and memory stores, extracts patterns, and curates memories for self-improvement over time

- **Evidence**: First-party feature description with one customer data point (Harvey,
  ~6x completion rate improvement).
- **Confidence**: anecdotal (vendor feature description + single customer benchmark;
  no independent replication; research preview access required)
- **Quote**: "Dreaming is a scheduled process that reviews your agent sessions and
  memory stores, extracts patterns, and curates memories so your agents improve over time."
- **Our assessment**: Dreaming is the most architecturally novel feature in this
  announcement. It is not per-session learning (which memory handles) but a
  meta-learning layer that operates between sessions, synthesizing cross-agent patterns
  that no single agent session could surface. The Harvey result (~6x completion rate
  improvement) is the strongest single-feature improvement claim in the corpus if
  valid, but the mechanism ("filetype workarounds and tool-specific patterns") suggests
  the baseline was low — agents re-learning environment facts on every session rather
  than accumulating institutional knowledge. The research preview access requirement
  means most practitioners cannot validate this today.

### Claim 2: Dreaming surfaces cross-agent patterns invisible to individual sessions — recurring mistakes, shared workflows, and team preferences — then restructures memory to stay high-signal

- **Evidence**: First-party feature description; no independent corroboration.
- **Confidence**: anecdotal (vendor claim; mechanism is coherent but unverified)
- **Quote**: "Dreaming surfaces patterns that a single agent can't see on its own,
  including recurring mistakes, workflows that agents converge on, and preferences
  shared across a team. It also restructures memory so it stays high-signal as it evolves."
- **Our assessment**: The value proposition is clear: individual agents with memory
  learn from their own sessions; dreaming learns from all sessions across all agents
  in a workspace. This is a meaningful architectural distinction. The "restructures
  memory so it stays high-signal" claim addresses a real failure mode of unbounded
  memory accumulation — without curation, memory stores grow stale or noisy over
  time. The mechanism for identifying which memories to keep, update, or discard is
  not described; the claim is functional, not technical.

### Claim 3: Memory and dreaming form a two-layer memory system — memory captures learning during sessions, dreaming refines and synthesizes it between sessions

- **Evidence**: First-party architectural description of the relationship between
  memory (public beta, April 23 announcement) and dreaming (research preview, this
  post).
- **Confidence**: anecdotal (vendor architectural framing; no independent verification)
- **Quote**: "Together, memory and dreaming form a robust memory system for
  self-improving agents. Memory lets each agent capture what it learns as it works.
  Dreaming refines that memory between sessions, pulling shared learnings across
  agents and keeping it up-to-date."
- **Our assessment**: This two-layer framing gives practitioners a useful mental
  model: memory is the write path (what the agent captures during a session), dreaming
  is the background maintenance path (what the platform extracts and curates across
  sessions). The analogy to human learning is apt — session-level encoding plus
  offline consolidation. What's missing is any description of what triggers dreaming
  (schedule? threshold? manual?), what the output format looks like, or whether
  practitioners can inspect or edit curated memories.

### Claim 4: The outcomes feature uses a separate grader that evaluates output against a rubric in its own context window, preventing the evaluator from being influenced by the generator's reasoning

- **Evidence**: First-party architectural description. Wisedocs customer example
  (reviews run 50% faster). Spiral customer example (rubric scoring against editorial
  principles). Benchmarks: +8.4% task success on docx and +10.1% on pptx.
- **Confidence**: emerging (specific architectural detail — separate context window —
  is novel; benchmarks are Anthropic-internal)
- **Quote**: "With outcomes, you write a rubric describing what success looks like and
  the agent works toward it. A separate grader evaluates the output against your
  criteria in its own context window, so it isn't influenced by the agent's reasoning.
  When something isn't right, the grader pinpoints what needs to change and the agent
  takes another pass."
- **Our assessment**: The "separate context window" detail is the key architectural
  addition over the April announcement (blog-anthropic-claude-managed-agents.md,
  Claim 5), which described the outcome-driven mode without explaining the evaluation
  isolation mechanism. A grader that shares the generator's context window would be
  susceptible to the positivity bias that blog-anthropic-harness-long-running.md
  (Claim 1) identifies as the core failure mode of self-evaluation. The isolated
  context window directly addresses this failure mode at the platform level. This
  is the most important architectural detail in the post for practitioners building
  their own generator/evaluator harnesses.

### Claim 5: Outcomes improved task success by up to 10 points over a standard prompting loop, with the largest gains on the hardest problems; internal benchmarks show +8.4% on docx and +10.1% on pptx

- **Evidence**: Anthropic internal benchmarks on structured file generation. More
  specific than the April announcement ("up to 10 points"), which lacked per-format
  breakdown.
- **Confidence**: anecdotal (internal benchmark from product team; methodology not
  disclosed; not independently replicated)
- **Quote**: "outcomes improved task success by up to 10 points over a standard
  prompting loop, with the largest gains on the hardest problems"
- **Quote (internal benchmarks)**: "+8.4% task success on docx and +10.1% on pptx
  in our internal benchmarks"
- **Our assessment**: The April announcement (blog-anthropic-claude-managed-agents.md,
  Claim 4) stated the same "+10 points" headline. This post adds format-specific
  granularity: docx gains are lower (8.4%) than pptx (10.1%), suggesting the rubric
  evaluation benefit varies with output complexity. Pptx is structurally more complex
  than docx (slides require layout, hierarchy, and content decisions), consistent
  with the "largest gains on hardest problems" framing. The "up to" qualifier still
  applies — these are ceiling figures, not average improvements.

### Claim 6: Multiagent orchestration (now public beta) lets a lead agent break work into pieces and delegate to specialists with their own model, prompt, and tools — specialists run in parallel on a shared filesystem

- **Evidence**: First-party architectural description. Netflix and Spiral customer
  examples.
- **Confidence**: emerging (promoted from research preview to public beta; two
  concrete customer examples; architecture is coherent and aligns with prior corpus)
- **Quote**: "When there is too much work for a single agent to do well, multiagent
  orchestration lets a lead agent break the job into pieces and delegate each one to
  a specialist with its own model, prompt, and tools. For example, a lead agent can
  run an investigation while subagents fan out through deploy history, error logs,
  metrics, and support tickets."
- **Our assessment**: The promotion from research preview (April 8) to public beta
  (May 6) is the key status change. The architecture — lead agent + bounded
  specialists + shared filesystem — is the orchestrator-subagent pattern from
  blog-anthropic-multi-agent-coordination-patterns.md (Claim 7: recommended default).
  The example (deploy history, error logs, metrics, support tickets fanning out in
  parallel) maps exactly to the Netflix use case. The "shared filesystem" as the
  coordination substrate is more concrete than the April announcement, which did not
  specify how inter-agent state is shared.

### Claim 7: Events are persistent and every agent remembers what it has done — the lead agent can check back with other agents mid-workflow, and all steps are traceable in Claude Console

- **Evidence**: First-party feature description; no independent verification of
  trace quality or granularity.
- **Confidence**: anecdotal (vendor feature claim; trace visibility is difficult to
  evaluate without hands-on access)
- **Quote**: "The lead agent can check back in with other agents mid-workflow because
  events are persistent and every agent remembers what it's done. You can also trace
  every step in the Claude Console: which agent did what, in what order, and why,
  giving you full visibility into how your task was delegated and executed."
- **Our assessment**: "Events are persistent" and mid-workflow check-in capability
  address the information bottleneck failure mode identified in
  blog-anthropic-multi-agent-coordination-patterns.md (Claim 3): subagents completing
  bounded tasks may surface cross-cutting insights that the orchestrator cannot route
  efficiently. If the lead agent can re-engage a running subagent mid-workflow rather
  than only receiving final outputs, this addresses the bottleneck more directly than
  a hub-and-spoke design with single output collection. The tracing claim
  (who, what, order, why in Console) extends the April announcement's general
  observability description with more specific metadata.

### Claim 8: Mixing models across orchestration levels is a concrete cost-optimization pattern — Spiral uses Haiku for the lead orchestrator agent and Opus for specialist drafting subagents

- **Evidence**: Spiral (Every) customer use case. Explicit model names (Haiku, Opus)
  and role assignments.
- **Confidence**: anecdotal (single customer; no cost comparison provided)
- **Quote**: "The lead agent runs on Haiku: it fields incoming requests, poses quick
  follow-up questions when needed, then delegates the drafting to subagents running
  on Opus. When a user asks for multiple drafts, the subagents run in parallel."
- **Our assessment**: This is the most technically actionable customer example in
  the post. It demonstrates that the Managed Agents platform supports per-specialist
  model selection, and it names the economically rational assignment: cheap model
  (Haiku) for orchestration/routing where low latency and low cost matter most;
  expensive model (Opus) for generation where output quality is the primary metric.
  This is a concrete implementation of the guidance in
  blog-anthropic-multi-agent-coordination-patterns.md (Claim 7: orchestrator-subagent
  is the recommended default pattern). No prior corpus source had named a specific
  model pairing for this pattern with actual production customer evidence.

### Claim 9: Dreaming produced ~6x completion rate improvement for Harvey in tests, attributed to persistent cross-session memory of filetype workarounds and tool-specific patterns

- **Evidence**: Single customer benchmark (Harvey — legal AI) with no methodology
  details.
- **Confidence**: anecdotal (single company; no baseline described; research preview)
- **Quote**: "With dreaming, their agents remember what they learned between sessions,
  including filetype workarounds and tool-specific patterns. Completion rates went
  up ~6x in their tests."
- **Our assessment**: The ~6x figure is the largest single-feature improvement metric
  in the corpus. The mechanism — "filetype workarounds and tool-specific patterns" —
  suggests the baseline completion rate was low because agents were rediscovering
  the same environment constraints on every session rather than accumulating
  institutional knowledge. This is the classic "cold start" problem for agents: each
  new session begins with no knowledge of what worked or failed before. Dreaming
  directly addresses cold-start by curating a warm-start knowledge base. The legal
  domain (Harvey's use case) may be particularly sensitive to this because legal
  document work involves many format-specific constraints that repeat across sessions.
  The ~6x estimate with "~" notation suggests an approximation, not a precise
  controlled measurement.

### Claim 10: Webhooks enable asynchronous agent task notification — define an outcome, let the agent run to completion, receive a webhook when done

- **Evidence**: First-party feature description; minimal technical detail.
- **Confidence**: settled (standard webhook pattern; feature is straightforward)
- **Quote**: "You can also now define an outcome, let the agent run, and get notified
  by a webhook when it's done."
- **Our assessment**: Webhooks complete the async agent workflow pattern for
  long-running tasks: fire-and-forget with notification on completion. This is
  architecturally necessary for outcome-mode agents that may run for extended periods
  — polling for completion is wasteful and adds latency. The combination of outcomes
  (define success criteria) + webhooks (get notified when criteria are met) is
  the correct pattern for any asynchronous agent deployment where the caller cannot
  block waiting for results.

## Concrete Artifacts

### Feature Availability Matrix (May 6, 2026)

```
Claude Managed Agents — Feature Status (as of 2026-05-06):

NEW (this announcement):
  Dreaming:             research preview (requires separate access request)
  Webhooks:             available

PROMOTED from research preview → public beta:
  Outcomes:             public beta
  Multiagent orchestration: public beta

PREVIOUSLY ANNOUNCED (April 23, 2026):
  Memory:               public beta

AVAILABLE since April 8, 2026 (unchanged):
  Prompt-and-response mode: GA
  Long-running sessions:    GA
  Sandboxed execution:      GA
  Session tracing/Console:  GA
  Scoped permissions:       GA
  Pricing: $0.08/session-hour (confirmed unchanged)
```

### Outcomes Architecture (grader isolation mechanism)

```
Outcomes pattern — isolated evaluation architecture:

GENERATOR (agent):
  - Receives task + rubric
  - Produces output (e.g., docx, pptx)
  - Does NOT evaluate its own output

GRADER (separate context window):
  - Receives: output + rubric (no access to generator reasoning)
  - Evaluates: output against rubric
  - When criteria not met: "pinpoints what needs to change"
  - Returns: pass/fail + specific improvement directions

LOOP:
  - Generator takes another pass if grader signals failure
  - Continues until grader passes or iteration limit reached

Key architectural property: grader context is isolated from generator
reasoning — prevents positivity bias in self-evaluation.

Source: Anthropic product announcement (2026-05-06)

Internal benchmarks (task success vs. standard prompting loop):
  docx: +8.4%
  pptx: +10.1%
  Overall: "up to 10 points on hardest problems"
```

### Dreaming + Memory System Architecture

```
Two-layer memory system (as described in announcement):

SESSION LAYER — Memory (public beta):
  - What: captures what each agent learns as it works
  - When: during active sessions
  - Scope: per-agent, per-session learning
  - Mechanism: "filesystem-based" (per April 23 memory announcement)

BETWEEN-SESSION LAYER — Dreaming (research preview):
  - What: reviews past sessions + memory stores, extracts patterns
  - When: scheduled (not during active agent sessions)
  - Scope: cross-agent, cross-session synthesis
  - Output: curated/restructured memories
  - Side effect: "keeps memory high-signal as it evolves"

TOGETHER:
  "Memory lets each agent capture what it learns as it works.
   Dreaming refines that memory between sessions, pulling shared
   learnings across agents and keeping it up-to-date."

Harvey result: ~6x completion rate improvement
Mechanism: agents no longer rediscover filetype workarounds and
           tool-specific patterns from scratch each session
```

### Multiagent Orchestration — Customer Examples

```
Netflix (platform team):
  Task: process logs from hundreds of builds across different sources
  Pattern: analysis agent → multiagent orchestration
  Lead behavior: fan out log batches to specialist subagents
  Subagent behavior: analyze batches in parallel
  Output: "surface only the patterns worth acting on"
  Metrics: none reported

Spiral (by Every):
  Task: long-form drafting with parallel versions
  Lead agent: Haiku (orchestration, routing, follow-up questions)
  Specialist agents: Opus (drafting, running in parallel)
  Quality enforcement: outcomes with rubric (Every's editorial
    principles + user's voice)
  Trigger: "When a user asks for multiple drafts, the subagents
    run in parallel"
  Metrics: none reported

Key pattern: lead agent uses cheap model (Haiku) for routing;
subagents use expensive model (Opus) for quality-sensitive work.
Source: Anthropic product announcement (2026-05-06)
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-claude-managed-agents.md** (Claim 4): The April announcement
    stated "Managed Agents improved outcome task success by up to 10 points over a
    standard prompting loop, with the largest gains on the hardest problems." This
    post repeats the same headline and adds format-specific breakdowns (+8.4% docx,
    +10.1% pptx), corroborating the figure with additional granularity.
  - **blog-anthropic-harness-long-running.md** (Claim 2): The GAN-inspired
    generator/evaluator split "outperforms prompting a single agent to self-critique."
    The outcomes feature implements this at the platform level, with the architectural
    detail (separate context window) that explains *why* it works — grader isolation
    prevents the positivity bias documented in Claim 1 of that note.
  - **blog-anthropic-multi-agent-coordination-patterns.md** (Claim 7): "For most use
    cases, we recommend starting with orchestrator-subagent. It handles the widest
    range of problems with the least coordination overhead." The Managed Agents
    multiagent orchestration feature is the hosted implementation of this recommended
    pattern.

- **Extends**:
  - **blog-anthropic-claude-managed-agents.md** (Claim 5 and Claim 6): The April
    note described the outcome-driven mode and multi-agent coordination as research
    preview with separate access requests. This May post promotes both to public
    beta — a significant status change that makes both features accessible to all
    Managed Agents developers.
  - **blog-anthropic-claude-managed-agents.md** (Claim 5): The April note described
    outcomes conceptually ("define outcomes and success criteria, Claude self-evaluates
    and iterates"). This post adds the key architectural detail: the grader runs in
    a separate context window to prevent evaluation bias.
  - **blog-anthropic-multi-agent-coordination-patterns.md** (Claim 3): That note
    identified the information bottleneck as the core failure mode of orchestrator-
    subagent (subagents surface cross-cutting insights the orchestrator can't route
    back efficiently). The "events are persistent and every agent remembers what it's
    done" property of Managed Agents multiagent orchestration allows mid-workflow
    check-ins that partially address this failure mode — the lead agent doesn't have
    to wait for final outputs to re-engage with subagents.

- **Contradicts**: None filed. The April 8 note's research preview designations for
  outcomes and multiagent orchestration have been superseded by public beta status —
  this is a status update, not a factual contradiction.

- **Novel**:
  - **Dreaming as a concept**: No prior corpus source documents a platform-level
    scheduled background process that synthesizes learning across agent sessions and
    curates memory stores. This is qualitatively different from session-level learning
    (memory) and from model fine-tuning (Cursor real-time RL) — it is a persistent,
    curated knowledge base updated asynchronously between sessions.
  - **Grader context isolation as an explicit architectural principle**: Prior sources
    described the generator/evaluator pattern but did not name the "separate context
    window" as the mechanism preventing evaluation bias. This is the first corpus
    source to explicitly name isolation as the key architectural property.
  - **Model mixing with named models in production**: Spiral's Haiku (lead) + Opus
    (specialists) pattern is the first named, production-validated model-mixing
    deployment in the corpus with specific model assignments per role.
  - **Harvey's ~6x dreaming improvement**: The largest single-feature improvement
    metric in the corpus (subject to the research preview caveat and the ~6x
    approximation).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Update the "Build vs. Buy" framing from
  blog-anthropic-claude-managed-agents.md to reflect the May 6 status changes:
  outcomes and multiagent orchestration are now in public beta (not research preview),
  making the hosted platform materially more accessible. Practitioners who deferred
  evaluation pending research preview can now evaluate both features.

- **Chapter 02 (Harness Engineering)** — evaluator architecture: The "separate context
  window" architectural detail from Claim 4 should be added to the generator/evaluator
  pattern documentation alongside blog-anthropic-harness-long-running.md. The specific
  reason isolation matters (grader positivity bias prevention) should be stated
  explicitly, linking blog-anthropic-harness-long-running.md Claim 1 (self-evaluation
  failure mode) to the platform's architectural response.

- **Chapter 05 (Multi-Agent Orchestration)**: Add Spiral's model-mixing pattern
  (Haiku orchestrator + Opus specialists) as a named, production-validated cost
  optimization for orchestrator-subagent systems. This is the first concrete evidence
  from a production deployment that cheap-model orchestration + expensive-model
  generation is the correct assignment for this pattern, extending the theoretical
  guidance in blog-anthropic-multi-agent-coordination-patterns.md Claim 7.

- **Chapter 05 (Multi-Agent Orchestration)**: The "events are persistent" property
  that enables mid-workflow lead-agent check-ins is a platform-level solution to the
  information bottleneck failure mode (blog-anthropic-multi-agent-coordination-patterns.md
  Claim 3). The guide's discussion of this failure mode should note the platform
  mitigation alongside the DIY patterns for addressing it.

- **Chapter 03 (Long-Running Sessions & State)** or equivalent: Add dreaming as a new
  architectural pattern for cross-session knowledge accumulation. The Harvey ~6x
  completion improvement is the motivation; the two-layer model (memory = session
  capture, dreaming = between-session synthesis) is the design. Distinguish dreaming
  from session-level memory and from model fine-tuning (Cursor real-time RL). Note
  research preview access requirement.

## Extraction Notes

- The post references a separate April 23, 2026 memory announcement
  (https://claude.com/blog/claude-managed-agents-memory) as the foundation for
  dreaming. That post was fetched during extraction: it describes filesystem-based
  memory, audit logging, concurrent agent access to shared stores, and workspace-
  scoped boundaries. The Rakuten benchmark from that post (97% fewer first-pass
  errors, 27% cost reduction, 34% latency reduction) is notable context for the
  memory system's production performance. A separate extraction of the April 23 post
  would be warranted if the guide adds detail on the memory architecture.
- Customer examples (Harvey, Netflix, Spiral, Wisedocs) do not include named
  individual testimonials with titles, unlike the April 8 announcement. This reduces
  evidential weight slightly — the examples are company-level, not person-level.
- No pricing changes are mentioned. The $0.08/session-hour rate from the April 8
  announcement is presumed unchanged.
- Dreaming requires a separate access request (research preview). Practitioners
  evaluating the feature should treat the Harvey result as a directional signal,
  not a reproducible benchmark, until broader access enables independent validation.
- The blog post links to platform.claude.com/docs/en/managed-agents documentation
  but does not reproduce implementation details. Extraction focused on the announced
  capabilities and customer evidence. A documentation extraction would add the
  implementation-level detail missing here.
