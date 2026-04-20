---
source_url: https://claude.com/blog/multi-agent-coordination-patterns
source_type: blog-post
title: "Multi-agent coordination patterns: Five approaches and when to use them"
author: Anthropic (Claude team)
date_published: 2026-04-10
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: settled
issue: "#251"
---

# Multi-agent coordination patterns: Five approaches and when to use them

> First-party Anthropic taxonomy of five multi-agent coordination patterns —
> generator-verifier, orchestrator-subagent, agent teams, message bus, and
> shared state — with explicit failure modes per pattern, pairwise decision
> criteria for when to evolve from one pattern to the next, and the recommended
> default (orchestrator-subagent) for practitioners starting out.

## Source Context

- **Type**: blog-post (official claude.com blog, April 10, 2026)
- **Author credibility**: Published on Anthropic's Claude blog. This is a
  first-party Anthropic post — the stated intent for how Claude should be used
  in multi-agent systems. It carries higher authority than practitioner
  synthesis posts because it reflects Anthropic's own framing of correct usage.
  Treat as authoritative on coordination topology; treat engineering trade-off
  claims as first-party design guidance rather than controlled experiment
  results.
- **Scope**: Covers five coordination topologies for multi-agent systems with
  concrete mechanics, failure modes, and pairwise decision criteria for choosing
  between patterns. Explicitly references a companion post on when NOT to use
  multi-agent systems vs. a single agent. Does NOT cover CLAUDE.md authoring,
  settings.json, or session-level tooling. Not SDK-specific — patterns apply
  to any multi-agent harness.

## Extracted Claims

### Claim 1: Five coordination patterns form a complete taxonomy for multi-agent system design

- **Evidence**: First-party Anthropic framing. The five named patterns —
  generator-verifier, orchestrator-subagent, agent teams, message bus, shared
  state — are presented as the complete decision space for multi-agent
  coordination topology.
- **Confidence**: settled (vendor taxonomy; authoritative for how Anthropic
  intends Claude to be used)
- **Quote**: N/A (structural taxonomy)
- **Our assessment**: This is the clearest and most authoritative multi-agent
  taxonomy in our corpus. Practitioner taxonomies (Osmani's three patterns,
  TTal's seven patterns) were derived empirically; this taxonomy is
  Anthropic-sanctioned and first-party. The five patterns map well onto the
  practitioner-derived patterns but add generator-verifier, message bus, and
  shared state as named patterns with explicit mechanics that no prior corpus
  source provided under those names.

### Claim 2: Generator-verifier requires explicit, formal acceptance criteria — vague criteria produce the "early victory problem"

- **Evidence**: First-party failure mode description. The verifier can only
  evaluate what is formally specified; "is this good?" fails silently because
  the verifier will rationalize acceptance rather than reject.
- **Confidence**: settled (corroborated by blog-anthropic-harness-long-running
  which documented the same failure mode from practitioner experience: "Claude
  is a poor QA agent" out of the box; evaluator "identifies legitimate issues,
  then talks itself into deciding they weren't a big deal")
- **Quote**: "The verifier is only as good as its criteria."
- **Our assessment**: This is the most operationally important claim in the
  post. The "early victory problem" — verifier rubber-stamps without genuine
  evaluation — is the failure mode every practitioner building a generator-
  verifier harness will hit if criteria are vague. It maps directly to the
  evaluator prompt-tuning development loop documented in harness-long-running
  (Claim 6 there). The fix is not better prompting — it is making criteria
  explicit and behavioral before any generation starts (see also: sprint
  contracts in harness-long-running, Claim 4).

### Claim 3: Orchestrator-subagent's core failure mode is information bottleneck when subagents discover cross-cutting insights

- **Evidence**: First-party failure mode description. The orchestrator
  synthesizes outputs from subagents, but subagents completing bounded tasks
  may surface findings that cross task boundaries — findings the orchestrator
  cannot efficiently route back to other subagents without extra coordination.
- **Confidence**: settled (structural failure mode of the hub-and-spoke pattern)
- **Quote**: N/A (described in failure modes section)
- **Our assessment**: This is the named failure mode for the most commonly
  recommended pattern. Practitioners building orchestrator-subagent systems
  should design explicitly for cross-cutting finding propagation — either by
  having the orchestrator route discoveries back into ongoing subagent tasks,
  or by adding a shared state layer for cross-cutting context (the common
  hybrid described in Claim 11). The TTal source independently arrived at
  this problem (Manager plane unblocking workers) via a different path.

### Claim 4: Agent teams differ from subagents in context persistence — subagents are bounded; teammates are persistent and accumulate context

- **Evidence**: First-party definitional distinction. Subagents complete work
  within a single bounded invocation and terminate; teammates in an agent
  team are persistent, accumulate domain-specific context across assignments,
  and improve performance over time on their area of the codebase.
- **Confidence**: settled (first-party architectural distinction)
- **Quote**: N/A (from pattern mechanics section)
- **Our assessment**: This is the clearest formalization of the subagent vs.
  teammate distinction in the corpus. Osmani's Agent Teams note described
  teammates as workers who "self-claim tasks and message peer-to-peer" but
  did not articulate the persistence/context-accumulation axis as the
  defining characteristic. The decision criterion that follows (Claim 8)
  makes this concrete: if the task requires multi-step sustained engagement
  where familiarity with the codebase improves quality, use agent teams, not
  subagents. This distinction directly informs the Ch02 harness architecture
  decision between spawning fresh agents vs. maintaining persistent specialists.

### Claim 5: Shared state requires first-class termination conditions — without them, agents enter reactive token-burning loops

- **Evidence**: First-party failure mode description. Agent A writes, B
  responds, A reacts — without a convergence criterion, agents loop indefinitely.
  The pattern requires at minimum: a time budget, a convergence threshold, or
  a designated judge agent that can declare completion.
- **Confidence**: settled (structural failure mode; corroborated by engineering
  intuition and the difficulty of convergence detection documented in
  discussion-hn-ttal-multiagent-factory Claim 8)
- **Quote**: "Shared state removes the intermediary by letting agents coordinate
  through a persistent store that all can read and write directly."
- **Our assessment**: The termination problem is real and frequently
  underspecified in practitioner harnesses. TTal's discussion-hn note surfaced
  this as the "stuck-vs-slow" open problem — but that was about individual
  agents. This claim extends it to multi-agent shared-state systems: the
  convergence question is even harder when multiple agents are all writing
  to shared state, because no single agent has global visibility into whether
  the system as a whole has converged. The three termination mechanisms
  (time budget, threshold, judge agent) are concrete design requirements for
  any shared-state implementation.

### Claim 6: Message bus routing introduces silent failures — misclassified or dropped events cause invisible system failure

- **Evidence**: First-party failure mode description. LLM-based routers that
  misclassify events cause downstream agents to never receive work; there is
  no error — the system simply fails to produce output.
- **Confidence**: settled (structural failure mode of publish-subscribe systems,
  intensified by LLM routing variability)
- **Quote**: N/A (failure mode section)
- **Our assessment**: Silent failures are the hardest category of failure to
  detect in production. The message bus pattern's debuggability is lower than
  the orchestrator-subagent pattern precisely because there is no orchestrator
  trace to follow — you must trace event propagation across all agents. This
  is a strong argument for adding explicit event logging at the router level.
  The guidance to use message bus only when workflow structure is genuinely
  unpredictable (Claim 9) follows directly from this failure mode: if the
  workflow is known, use orchestrator-subagent and get the debuggability
  benefit.

### Claim 7: The recommended default pattern is orchestrator-subagent

- **Evidence**: First-party recommendation. Described as handling "the widest
  range of problems with the least coordination overhead."
- **Confidence**: settled (explicit vendor recommendation)
- **Quote**: "For most use cases, we recommend starting with orchestrator-
  subagent. It handles the widest range of problems with the least coordination
  overhead."
- **Our assessment**: This is the actionable default for Ch02. Practitioners
  who are unsure which pattern to use should start here. The other patterns
  are evolution paths that add complexity to solve specific failure modes
  (Claim 3: information bottleneck → shared state hybrid; Claim 4: bounded
  context ceiling → agent teams; Claim 6: fixed workflow assumption → message
  bus). The recommendation is consistent with the evolution-first philosophy
  (Claim 12) — start simple, observe failure modes, upgrade deliberately.

### Claim 8: How long workers must maintain context determines orchestrator-subagent vs. agent teams

- **Evidence**: First-party decision criterion. Orchestrator-subagent when
  subtasks are short, focused, and produce clear outputs within a single
  invocation; agent teams when subtasks benefit from sustained, multi-step
  engagement where familiarity develops.
- **Confidence**: settled (explicit decision criterion, vendor-authored)
- **Quote**: N/A (decision framework section)
- **Our assessment**: This criterion is more useful than the
  "simple vs. complex tasks" framing that practitioners typically use.
  "Context duration" is directly measurable: does the subtask require the
  agent to remember what it did in step 1 while executing step 5? If no,
  subagent. If yes, teammate. The harness-long-running post's Opus 4.5
  sprint decomposition pattern is the orchestrator-subagent answer to context
  duration; agent teams are the architectural answer.

### Claim 9: Whether workflow structure is predictable or event-driven determines orchestrator-subagent vs. message bus

- **Evidence**: First-party decision criterion. Use orchestrator-subagent when
  the sequence of steps is known in advance; message bus when workflow
  emerges from events and routing varies based on discoveries.
- **Confidence**: settled (explicit decision criterion)
- **Quote**: N/A (decision framework section)
- **Our assessment**: The "known in advance" criterion is the correct question.
  Most coding workflows (implement, review, test, merge) are known in advance
  — orchestrator-subagent is appropriate. Security operations workflows
  (alert → triage → investigation → response, where response type depends on
  triage findings) are event-driven — message bus is appropriate. The
  practical signal: if you can write down the DAG of your workflow before
  it runs, use orchestrator-subagent. If the DAG must be discovered at runtime
  from intermediate outputs, use message bus.

### Claim 10: Whether agents need each other's intermediate findings determines agent teams vs. shared state

- **Evidence**: First-party decision criterion. Use agent teams when agents work
  on separate partitions and results combine at the end; shared state when
  findings must flow between agents in real-time as the work progresses.
- **Confidence**: settled (explicit decision criterion)
- **Quote**: N/A (decision framework section)
- **Our assessment**: This is the correct architectural question for parallel
  workloads. A service-by-service codebase migration where each team member
  owns a service has no inter-agent finding dependency — agent teams. A
  multi-agent research task where one agent's discovery changes what another
  agent should investigate requires real-time finding propagation — shared
  state. The TTal source's P2P mesh topology (workers alerting manager when
  blocked) is a partial implementation of the shared-state finding-propagation
  pattern via a different mechanism.

### Claim 11: Production systems commonly combine patterns — a documented hybrid pairs orchestrator-subagent overall with shared state for collaboration-heavy subtasks

- **Evidence**: First-party design guidance. The hybrid is described as the
  common production pattern, not an edge case.
- **Confidence**: settled (explicit vendor-documented pattern)
- **Quote**: "Production systems often combine patterns. A common hybrid uses
  orchestrator-subagent for overall workflow with shared state for
  collaboration-heavy subtask."
- **Our assessment**: This is important guidance for practitioners who observe
  that no single pattern fits all of their system's needs. The hybrid described
  — orchestrator-subagent as the outer shell, shared state as the inner
  collaboration layer for tasks that need inter-agent finding propagation —
  is architecturally sound and avoids the worst failure modes of both: the
  orchestrator provides termination control (mitigating shared state's
  convergence failure mode) while shared state solves the orchestrator's
  information bottleneck for the collaboration-heavy subtask.

### Claim 12: Start with the simplest pattern and evolve based on observed failure modes

- **Evidence**: Explicit first-party guidance on the evolution strategy.
- **Confidence**: settled (explicit vendor guidance; the pairwise decision
  criteria in the post are framed as evolution triggers, not initial design
  choices)
- **Quote**: "Start with the simplest pattern that could work, watching where
  it struggles, and evolving from there."
- **Our assessment**: This is the meta-principle behind the entire five-pattern
  framework. The patterns are not alternative designs to evaluate upfront —
  they are a progression where each adds coordination complexity to solve a
  specific failure mode of the simpler pattern. This aligns with the harness-
  long-running post's principle (Claim 9 there) that harness components encode
  model limitation assumptions and should be pruned when unnecessary. The
  inverse also applies here: add coordination complexity only when you
  observe the failure mode that requires it.

### Claim 13: Context decomposition should follow context needs, not work type

- **Evidence**: First-party design principle labeled "Context-Centric
  Decomposition."
- **Confidence**: settled (explicit vendor principle)
- **Quote**: "Divide work by what context each agent needs rather than by what
  type of work it does."
- **Our assessment**: This principle reframes the decomposition question. The
  common decomposition approach ("agent A handles frontend, agent B handles
  backend") is work-type decomposition — but if frontend and backend agents
  need overlapping context to make coordinated decisions, work-type boundaries
  generate information bottlenecks. Context-needs boundaries ask: what does
  each agent need to know to do its work? Decompose so each agent holds the
  minimal context it actually needs. This is directly applicable to Ch02's
  harness architecture guidance.

## Concrete Artifacts

### Five-Pattern Decision Table

```
# Pattern selection by situation
# Source: "Multi-agent coordination patterns," Anthropic, April 10, 2026

Situation                                           | Recommended Pattern
----------------------------------------------------|---------------------
Quality-critical output, explicit eval criteria     | Generator-Verifier
Clear task decomposition, bounded subtasks          | Orchestrator-Subagent
Parallel workload, long-running independent tasks   | Agent Teams
Event-driven pipeline, growing agent ecosystem      | Message Bus
Collaborative research, agents share discoveries    | Shared State
No single point of failure required                 | Shared State
```

### Pairwise Evolution Decision Criteria

```
# When to evolve between patterns
# Source: "Multi-agent coordination patterns," Anthropic, April 10, 2026

Orchestrator-Subagent → Agent Teams
  When: Subtasks require sustained, multi-step engagement
  Test: Do workers develop familiarity that improves performance over time?

Orchestrator-Subagent → Message Bus
  When: Workflow structure is unpredictable; steps emerge from events
  Test: Can you write the workflow DAG before it runs? Yes → stay. No → message bus.

Agent Teams → Shared State
  When: Agents need each other's intermediate findings in real-time
  Test: Do agent results combine at end, or must findings flow between agents mid-work?

Message Bus → Shared State
  When: Agents need to build on accumulated findings over time
  Test: Are agents completing discrete pipeline stages, or accumulating a shared knowledge base?
```

### Pattern Mechanics Summary

```
# Mechanics and failure modes per pattern
# Source: "Multi-agent coordination patterns," Anthropic, April 10, 2026

1. GENERATOR-VERIFIER
   Mechanics: Generator → Verifier criteria check → feedback loop until accept or max iters
   Failure mode: Vague criteria → verifier rubber-stamps (early victory problem)
   Guard: Make criteria explicit and behavioral before generation starts

2. ORCHESTRATOR-SUBAGENT
   Mechanics: Lead plans + dispatches → subagents complete bounded work → orchestrator synthesizes
   Failure mode: Information bottleneck; cross-cutting insights lost in handoffs
   Guard: Design explicitly for cross-cutting propagation; consider shared state hybrid

3. AGENT TEAMS
   Mechanics: Coordinator spawns persistent workers from shared queue; workers retain context
   Failure mode: Strict independence required; shared resource conflicts; completion detection hard
   Guard: Partition tasks to minimize inter-worker dependencies

4. MESSAGE BUS
   Mechanics: Agents publish/subscribe via router; new agents join without rewiring
   Failure mode: Silent failures if router misclassifies; cascading events hard to trace
   Guard: Explicit event logging at router; don't use for predictable workflows

5. SHARED STATE
   Mechanics: Agents read/write persistent store autonomously; no central coordinator
   Failure mode: Token-burning reactive loops without convergence
   Guard: Require explicit termination: time budget OR convergence threshold OR judge agent
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-harness-long-running.md` — The generator-verifier pattern
    here is the formal taxonomy name for the generator/evaluator split in that
    post. The "early victory problem" (Claim 2) is the same failure mode as
    harness-long-running's Claim 6 ("Claude is a poor QA agent out of the box;
    identifies legitimate issues, then talks itself into deciding they weren't
    a big deal"). The sprint contract pattern (harness-long-running Claim 4)
    is the mechanism that operationalizes the "explicit criteria" requirement
    for generator-verifier. The two posts are complementary: this post names
    the pattern; harness-long-running documents how to build it.
  - `blog-addyosmani-code-agent-orchestra.md` — Osmani's Claim 4 (Agent Teams
    feature: Team Lead + Teammates) maps to the agent teams pattern here.
    Osmani's Claim 5 (bottleneck shifted to verification) is the practitioner
    articulation of why generator-verifier is the first pattern in this
    taxonomy. Osmani's Ralph Loop (context resets between iterations) is a
    solo-agent analog to the generator-verifier loop mechanic.
  - `discussion-hn-ttal-multiagent-factory.md` — TTal's two-plane architecture
    (persistent Manager + ephemeral Workers) maps to the orchestrator-subagent
    pattern. TTal's Executor-Reviewer (Pattern 1 in TTal taxonomy) maps to
    generator-verifier. The "stuck-vs-slow" open problem (TTal Claim 8)
    corroborates the termination requirement for shared state (Claim 5 here).
  - `blog-anthropic-harnessing-claude-intelligence.md` — Subagent spawning
    for fresh context windows (+2.8% BrowseComp) aligns with and quantifies
    the orchestrator-subagent pattern here. The context-centric decomposition
    principle (Claim 13) aligns with that post's framing of subagents as
    context hygiene, not parallelism.

- **Contradicts**: None filed. The TTal seven-pattern taxonomy and Osmani's
  three-pattern taxonomy both overlap with the five-pattern Anthropic taxonomy
  without directly contradicting it — they are different framings of adjacent
  spaces (tool-building patterns vs. coordination topologies) rather than
  competing claims about the same design decisions.

- **Extends**:
  - `blog-addyosmani-code-agent-orchestra.md` — Osmani's three patterns
    (subagents, agent teams, Ralph loop) are a proper subset of the five
    Anthropic patterns. This post adds generator-verifier, message bus, and
    shared state as named patterns with formal mechanics and failure modes
    that Osmani did not provide. Critically, this post adds *decision criteria*
    for choosing between patterns, which Osmani's synthesis lacked.
  - `discussion-hn-ttal-multiagent-factory.md` — TTal's seven practitioner
    patterns lacked first-party Anthropic validation. This post provides the
    authoritative framing that grounds and validates the patterns TTal
    independently observed.
  - `blog-anthropic-harness-long-running.md` — That post documented one
    specific pattern (generator/evaluator) in depth. This post places it in
    a five-pattern taxonomy, adds explicit decision criteria for when to use
    it vs. alternatives, and names the failure mode that practitioners need
    to guard against.

- **Novel**:
  - **Formal five-pattern taxonomy with Anthropic authority**: No prior corpus
    source provides a complete, Anthropic-sanctioned coordination taxonomy with
    formal decision criteria. Practitioner taxonomies existed; an authoritative
    one did not.
  - **"Early victory problem" as a named failure mode**: The specific failure
    pattern — verifier rubber-stamps without explicit criteria — is named here
    for the first time in our corpus. harness-long-running described the failure
    behavior; this post names the pattern.
  - **"Information bottleneck" as the named failure mode for orchestrator-subagent**:
    The cross-cutting insight loss through handoffs is named explicitly here.
  - **Message bus pattern as a coordination topology**: No prior corpus source
    describes publish-subscribe agent coordination with a router. This is a
    genuinely new pattern for our corpus.
  - **Shared state pattern with convergence requirements**: The pattern of
    coordinator-free agents collaborating through a persistent store — and
    the explicit termination requirement — is new to the corpus.
  - **Pairwise decision criteria matrix**: Four explicit pairwise comparisons
    with named decision criteria for when to evolve from one pattern to another
    is new. Prior sources described patterns but not the transitions between them.
  - **Context-centric decomposition principle**: "Divide work by what context
    each agent needs rather than by what type of work it does" as an explicit
    design axiom is new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "Multi-Agent Coordination
  Patterns" section using this five-pattern taxonomy as the primary
  organizational framework. The generator-verifier, orchestrator-subagent,
  agent teams, message bus, and shared state patterns should each get a
  subsection with mechanics, failure modes, and the pairwise decision criteria
  for when to evolve. Anchor with the vendor recommendation (Claim 7):
  start with orchestrator-subagent. The context-centric decomposition principle
  (Claim 13) should replace the vaguer "task decomposition" framing currently
  in the chapter skeleton.

- **Chapter 02 (Harness Engineering)**: The generator-verifier failure mode
  (Claim 2, "early victory problem") should be added as a named anti-pattern
  alongside the evaluator prompt-tuning development loop from harness-long-
  running. The two sources together form the complete picture: this post names
  the failure; harness-long-running documents how to fix it (sprint contracts,
  evaluator log review loop).

- **Chapter 03 (Safety and Verification)**: The generator-verifier pattern is
  the structural answer to "how do you verify agent output without sycophancy?"
  Add this taxonomy as the foundation for the chapter's architecture guidance.
  Explicitly connect to harness-long-running's evaluator prompt-tuning
  methodology and the "explicit criteria before generation starts" requirement
  from Claim 2 here.

- **Chapter 02 or Chapter 03**: Add the "evolution-first" principle (Claim 12)
  as a named guideline: "Start with orchestrator-subagent. Observe the failure
  mode. Evolve to the next pattern only when you observe the specific failure
  that justifies added coordination complexity." Pair with the decision criteria
  table (Concrete Artifacts) as the operational guide for making the evolution
  decision.

- **Chapter 04 (Context Engineering)**: Add the context-centric decomposition
  principle (Claim 13) — "divide work by what context each agent needs, not
  by what type of work it does" — as a named principle. This reframes the
  decomposition problem from work partitioning to context partitioning, which
  is more directly connected to the context management content in Ch04.

## Extraction Notes

- The source was fetched from claude.com/blog in full. The five-pattern taxonomy,
  decision criteria, and failure modes were all accessible. The post references
  a companion post on single-agent vs. multi-agent decision criteria ("when NOT
  to use multi-agent") which was not fetched for this note — a separate source
  submission may be warranted.
- The post is dated April 10, 2026 and is published on the Anthropic Claude
  consumer blog (not the Anthropic engineering blog). Author is listed as
  Anthropic team, not an individual; no byline was visible in the fetched content.
- The generator-verifier pattern here is clearly the same architecture as the
  generator/evaluator in blog-anthropic-harness-long-running. No contradiction
  filing needed — the posts use different terminology for the same pattern.
- The "early victory problem" terminology appeared in the Prospector's triage
  comment and is consistent with the failure mode described in the source. Used
  here as the canonical name for this failure mode.
- The registry/sources.json file was checked and found to be an empty schema
  (`{"sources": {}, "last_updated": null}`). Per instructions, it was left
  alone.
