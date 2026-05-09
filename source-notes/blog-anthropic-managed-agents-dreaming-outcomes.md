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

> Anthropic's May 2026 follow-up to the April Managed Agents launch, introducing
> dreaming (scheduled batch pattern extraction from past sessions for agent
> self-improvement, research preview), promoting outcomes and multiagent
> orchestration from research preview to public beta, and presenting four new
> customer case studies demonstrating production deployments at Harvey, Netflix,
> Spiral by Every, and Wisedocs.

## Source Context

- **Type**: blog-post (official claude.com product announcement, May 6, 2026)
- **Author credibility**: First-party Anthropic announcement — maximum authority
  on platform feature descriptions and availability. Customer testimonials are from
  named companies (Harvey, Netflix, Spiral by Every, Wisedocs) with attributed use
  cases, raising them above generic marketing copy. Internal benchmarks (Outcomes
  +10 points, +8.4% docx, +10.1% pptx; Harvey ~6x completion rate) are vendor-run
  and not independently replicated. The ~6x Harvey metric is from Harvey's own tests,
  not Anthropic's, which is a slight evidential upgrade for that specific claim.
- **Scope**: Covers three capability updates — dreaming (new, research preview),
  outcomes (GA/public beta upgrade), and multiagent orchestration (GA/public beta
  upgrade) — with four customer case studies. Does NOT cover: API design, SDK
  integration specifics, pricing changes, how dreaming schedules are configured,
  or how the shared filesystem is implemented technically. This is a marketing
  announcement; implementation-level details live in the platform documentation.
- **Relationship to prior source**: This note extends
  `blog-anthropic-claude-managed-agents.md` (April 8, 2026 initial Managed Agents
  launch). That note documented outcomes and multi-agent coordination as in
  "research preview"; this note promotes them to public beta. Dreaming is entirely
  new — not mentioned in the April announcement. Read both notes together for a
  complete picture of the platform's evolution over its first month.

## Extracted Claims

### Claim 1: Dreaming is a new scheduled background process (research preview) that reviews past agent sessions, extracts patterns, and curates memories to enable agents to self-improve over time

- **Evidence**: First-party Anthropic product feature description, corroborated
  by Harvey testimonial showing ~6x completion rate improvement in their tests.
- **Confidence**: anecdotal (vendor feature description + one customer case)
- **Quote**: "Dreaming is a scheduled process that reviews your agent sessions and
  memory stores, extracts patterns, and curates memories so your agents improve
  over time."
- **Our assessment**: Dreaming introduces a qualitatively new architectural
  concept for Managed Agents — offline/batch self-improvement from accumulated
  session history. This is distinct from in-session memory (real-time learning
  during a session) and from outcomes-based iteration (the agent retrying during a
  single session). Dreaming operates between sessions, asynchronously. The
  architectural implication for practitioners: agents deployed on Managed Agents
  can improve without operator intervention, as long as they accumulate session
  history. The research preview status means access requires a separate request;
  Harvey's result cannot currently be reproduced by most practitioners.

### Claim 2: Dreaming and in-session memory form a two-layer architecture — memory captures learning as work happens; dreaming refines it between sessions by pulling patterns across multiple agents

- **Evidence**: Explicit architectural description in the announcement.
- **Confidence**: settled (first-party architectural description)
- **Quote**: "Together, memory and dreaming form a robust memory system for
  self-improving agents. Memory lets each agent capture what it learns _as it
  works_. Dreaming refines that memory _between sessions_, pulling shared
  learnings across agents and keeping it up-to-date."
- **Our assessment**: The two-layer framing (real-time in-session + batch
  between-session) is conceptually clean and maps to a known pattern in ML
  systems: online learning (in-session memory) vs. batch training (dreaming).
  The "pulling shared learnings across agents" phrase is significant — dreaming
  is not per-agent; it aggregates across all agents in a workspace, which means
  learnings from one agent's session improve all agents. This is an emergent
  organizational benefit invisible to any single agent run in isolation.

### Claim 3: Dreaming surfaces cross-session patterns that no single agent run can observe — recurring mistakes, emergent workflows, and preferences shared across a team

- **Evidence**: Product feature description.
- **Confidence**: anecdotal (vendor claim; no mechanism detail provided)
- **Quote**: "Dreaming surfaces patterns that a single agent can't see on its own,
  including recurring mistakes, workflows that agents converge on, and preferences
  shared across a team."
- **Our assessment**: The three named pattern types — recurring mistakes, emergent
  workflows, shared preferences — map to real operational use cases. Recurring
  mistake correction is the most immediately valuable (Harvey's filetype
  workarounds). Shared preferences across a team is the most novel: it implies
  dreaming extracts implicit team standards from accumulated agent outputs, not
  just individual agent history. No mechanism description is provided for how
  patterns are distinguished from noise; the reliability of this extraction is
  not documented.

### Claim 4: Harvey's agents achieved approximately 6x improvement in completion rates using dreaming, because agents retained tool-specific and filetype learnings between sessions

- **Evidence**: Named customer case study (Harvey, legal AI company using Managed
  Agents for long-form legal drafting). The ~6x figure is from Harvey's own tests,
  not Anthropic's benchmarks.
- **Confidence**: anecdotal (single company; internal metric; not independently
  audited)
- **Quote**: "With dreaming, their agents remember what they learned between
  sessions, including filetype workarounds and tool-specific patterns. Completion
  rates went up ~6x in their tests."
- **Our assessment**: The Harvey case is the most concrete evidence for dreaming's
  value. The specific mechanism — remembering filetype workarounds and tool-specific
  patterns — is the type of operational knowledge that accumulates slowly through
  manual iteration in DIY harness configurations (documented in
  `blog-anthropic-harness-long-running` as the iterative tuning loop). Dreaming
  automates that knowledge accumulation. The ~6x figure should be read as
  directional, not as a controlled experiment result. Harvey's legal use case
  (long-form document generation with complex tool interactions) is well-suited
  to dreaming: high repetition, consistent task structure, many opportunities to
  accumulate filetype and formatting patterns.

### Claim 5: Outcomes (promoted from research preview to public beta) let practitioners write a success rubric and the agent iterates toward it — improving task success by up to 10 percentage points over a standard prompting loop, with the largest gains on the hardest problems

- **Evidence**: Anthropic internal benchmark. The April 2026 announcement
  (blog-anthropic-claude-managed-agents.md, Claim 4) cited the same "+10 points"
  figure when outcomes was in research preview; this post confirms it at public beta
  with additional file-type specifics.
- **Confidence**: anecdotal (internal Anthropic benchmark; consistent with April
  figure; not independently replicated)
- **Quote**: "In testing, outcomes improved task success by up to 10 points over a
  standard prompting loop, with the largest gains on the hardest problems."
- **Our assessment**: The promotion from research preview to public beta is
  significant — outcomes is now accessible without a separate access request.
  The "+10 points" figure is consistent with the April announcement, suggesting
  Anthropic's internal test results are stable. The "largest gains on hardest
  problems" qualifier continues to apply: the outcome loop provides the most
  value when single-shot prompting fails. For easy tasks where a single response
  already succeeds, outcomes adds overhead without benefit.

### Claim 6: Outcomes produces measurable file generation quality improvements: +8.4% task success on docx and +10.1% on pptx in Anthropic internal benchmarks

- **Evidence**: Anthropic internal benchmarks cited in the announcement. These are
  more specific than the April "+10 points" figure — they break down the improvement
  by file type.
- **Confidence**: anecdotal (internal benchmark; task-type-specific; not independent)
- **Quote**: "Outcomes also improved file generation quality, with +8.4% task success
  on docx and +10.1% on pptx in our internal benchmarks."
- **Our assessment**: The file-type breakdown is useful because it names a specific
  task category (structured file generation) with specific metrics. pptx shows a
  slightly larger gain than docx, which may reflect that PowerPoint generation has
  more evaluable structure (slide count, visual hierarchy) than Word documents.
  These numbers are precision markers, not validated generalization results. They
  tell practitioners "outcomes helps most when your task has objectively evaluable
  outputs" — a rubric for when to reach for outcomes vs. standard prompting.

### Claim 7: Wisedocs reduced document review time by 50% while maintaining quality standards by using outcomes-based rubric grading against their internal guidelines

- **Evidence**: Named customer testimonial (Wisedocs, document intelligence
  company).
- **Confidence**: anecdotal (single company; self-reported metric)
- **Quote**: "Reviews now run 50% faster, while staying aligned with their team's
  standards."
- **Our assessment**: Wisedocs' use case (document quality checking against
  internal guidelines) is a strong fit for outcomes: the rubric is the internal
  guideline itself. The 50% speed improvement suggests the agent completes review
  tasks without the iteration overhead of human re-review cycles — rather than the
  outcome loop's retry overhead, the improvement comes from higher first-pass
  quality reducing human review. The phrase "while staying aligned with their
  team's standards" implies the key practitioner concern (that faster = lower
  quality) is addressed by the rubric mechanism.

### Claim 8: Multiagent orchestration (promoted from research preview to public beta) enables a lead agent to break work into pieces and delegate each to a specialist subagent with its own independent model, prompt, and tools

- **Evidence**: First-party Anthropic product feature description. Promoted to
  public beta (was research preview in the April announcement).
- **Confidence**: settled (first-party feature description at GA)
- **Quote**: "When there is too much work for a single agent to do well, multiagent
  orchestration lets a lead agent break the job into pieces and delegate each one
  to a specialist with its own model, prompt, and tools."
- **Our assessment**: The availability of per-subagent model selection is the
  most significant implementation detail here. Practitioners can assign different
  Claude models to different roles within the same workflow — cheap models for
  routing and intake, expensive models for generation (see Claim 10, Spiral by
  Every). The "too much work for a single agent to do well" framing is a useful
  practical trigger: when single-agent quality degrades under task complexity, add
  a second layer of agents rather than prompting harder. This aligns with the
  orchestrator-subagent pattern in `blog-anthropic-multi-agent-coordination-patterns`
  (Claim 3: orchestrator-subagent failure mode is information bottleneck, not
  quality degradation per se, but the use case is the same).

### Claim 9: Subagents work in parallel on a shared filesystem with persistent event history, enabling the lead agent to check in mid-workflow because every agent remembers what it has done

- **Evidence**: Product feature description with the Spiral by Every and Netflix
  case studies as implicit corroboration (both require parallel execution +
  state visibility).
- **Confidence**: settled (first-party feature description)
- **Quote**: "These specialists work in parallel on a shared filesystem and
  contribute to the lead agent's overall context. The lead agent can check back
  in with other agents mid-workflow because events are persistent and every agent
  remembers what it's done."
- **Our assessment**: Two infrastructure claims in one: (a) shared filesystem
  across parallel subagents — implies outputs of one subagent can be read by
  another, enabling coordination without message-passing; (b) persistent event
  history — the lead agent can re-query subagent state mid-workflow, not just
  collect final outputs. The second claim is particularly important for recovery:
  if one subagent hits an error, the lead agent can observe that via the event
  log and redirect rather than failing the whole workflow. This is the "recover
  from errors" infrastructure described in the April announcement, now made
  concrete at the multiagent level. The fan-out investigation example in the
  next quote illustrates the shared-filesystem pattern.

### Claim 10: Mixed-model orchestration is a viable cost-quality optimization — Spiral by Every routes requests with a fast cheap model (Haiku) and delegates drafting to capable expensive models (Opus) as subagents

- **Evidence**: Named customer case study (Spiral by Every, writing agent). Full
  technical pattern described with named models.
- **Confidence**: anecdotal (single company implementation; models named explicitly)
- **Quote**: "Spiral by Every is using multiagent orchestration and outcomes to
  power the writing agent behind their new API and CLI. The lead agent runs on
  Haiku: it fields incoming requests, poses quick follow-up questions when needed,
  then delegates the drafting to subagents running on Opus."
- **Our assessment**: This is the first explicit mixed-model orchestration case
  study in our corpus with named model assignments. The Haiku-as-router /
  Opus-as-worker split is a concrete implementation of the cost-quality tradeoff
  in multi-agent systems: cheap-and-fast for intake/routing decisions, expensive-
  and-capable for the high-value generation work. The combined use of multiagent
  orchestration (for routing + delegation) and outcomes (for quality enforcement)
  shows these features composing in practice, not just in theory. Practitioners
  designing multi-agent systems can use this as a reference architecture for
  writing or any other task that distinguishes high-volume intake from
  low-volume high-quality generation.

## Concrete Artifacts

### Platform Status Matrix: May 2026 (vs. April 2026)

```
Feature                        | April Status         | May Status
-------------------------------|----------------------|------------------
Long-running sessions          | GA                   | GA (unchanged)
Checkpointing / persistence    | GA                   | GA (unchanged)
Credential management          | GA                   | GA (unchanged)
Scoped permissions             | GA                   | GA (unchanged)
Execution tracing (Console)    | GA                   | GA (unchanged)
Prompt-and-response mode       | GA                   | GA (unchanged)
Outcomes / self-eval loop      | Research Preview     | PUBLIC BETA
Multi-agent coordination       | Research Preview     | PUBLIC BETA
Memory (in-session)            | not mentioned        | PUBLIC BETA
Webhooks                       | not mentioned        | PUBLIC BETA
Dreaming (batch self-improve)  | not present          | Research Preview (NEW)
```

### Outcomes Benchmark Data (Anthropic internal, May 2026)

```
Task type              | Improvement vs. standard prompting
-----------------------|------------------------------------
Task success (overall) | up to +10 points
docx file generation   | +8.4% task success
pptx file generation   | +10.1% task success

Conditions:
  - "Largest gains on hardest problems"
  - Internal Anthropic benchmark
  - Not independently replicated
```

### Customer Deployment Patterns (May 2026)

```
Company         | Features Used            | Key Result
----------------|--------------------------|--------------------------------
Harvey          | Dreaming                 | ~6x completion rate improvement;
                |                          | agents retain filetype workarounds
                |                          | + tool patterns between sessions
                |                          | (legal long-form drafting)
Netflix         | Multiagent orchestration | Parallel log analysis across
                |                          | hundreds of builds (fan-out)
Spiral by Every | Multiagent + Outcomes    | Haiku lead agent routes + delegates
                |                          | to Opus drafting subagents; outcomes
                |                          | enforces editorial quality
Wisedocs        | Outcomes                 | 50% faster document reviews while
                |                          | maintaining team standards
```

### Spiral by Every Architecture (Mixed-Model Multiagent)

```
Lead Agent: Claude Haiku
  - Fields incoming writing requests
  - Poses follow-up clarifying questions
  - Delegates drafting tasks

Drafting Subagents: Claude Opus
  - Execute actual content generation
  - Subject to outcomes-based quality rubric
  - Work with user voice/preferences from memory

Combined: multiagent orchestration (routing) + outcomes (quality enforcement)
Source: Spiral by Every implementation, claude.com blog May 2026
```

### Fan-Out Parallelism Example (Netflix pattern)

```
Lead agent: coordination + synthesis
  └─ Subagent 1: deploy history analysis
  └─ Subagent 2: error log analysis
  └─ Subagent 3: metrics analysis
  └─ Subagent N: support tickets analysis

"For example, a lead agent can run an investigation while subagents fan out
through deploy history, error logs, metrics, and support tickets."
(claude.com blog, May 2026)
```

## Cross-References

- **Corroborates**:
  - **blog-anthropic-claude-managed-agents.md**: The April 2026 initial launch
    note documented outcomes (Claim 5) and multi-agent coordination (Claim 6) as
    research preview features; this May note confirms their promotion to public
    beta. The "+10 points" outcomes benchmark figure is consistent between the two
    posts (April's "up to 10 points over a standard prompting loop" equals this
    post's identical phrasing). The core infrastructure claims from April (sessions,
    checkpointing, scoped permissions, execution tracing) are unchanged in the May
    post, which focuses entirely on the three new/promoted capabilities.
  - **blog-anthropic-multi-agent-coordination-patterns.md**: The multiagent
    orchestration pattern here — lead agent breaks work into pieces, delegates to
    specialist subagents with independent model/prompt/tools — maps directly to
    the orchestrator-subagent pattern described in that post. The persistent event
    history (subagents maintain state visible to the lead agent) addresses the
    information bottleneck failure mode identified in that taxonomy. The mixed-model
    Spiral by Every pattern (Haiku router + Opus worker) is a concrete application
    of the model-selection tradeoff implicit in that taxonomy.
  - **discussion-hn-ttal-multiagent-factory.md**: Managed Agents' multiagent
    orchestration is the hosted version of the Manager/Worker architecture TTal
    implements locally. Both use a coordinator agent to delegate to specialists;
    both use parallelism. The key difference is execution environment and build-vs-buy.
    The Netflix fan-out pattern (parallel subagents scanning different data sources)
    is architecturally identical to TTal's parallel worker pattern.
  - **blog-cursor-real-time-rl.md**: Dreaming (batch extraction of patterns from
    accumulated session history to improve future performance) is thematically
    similar to Cursor's real-time RL (using production inference as reward signal
    to improve future performance). Both use accumulated operational data as a
    training/improvement signal. The key difference: Cursor's approach is
    real-time, model-weight-level, and requires RL infrastructure; dreaming is
    batch, memory-level, and requires only session history. Dreaming is available
    to practitioners without ML infrastructure; RL is not.

- **Contradicts**: None filed. The outcomes status change (research preview →
  public beta) is a factual update, not a contradiction of the April note. The
  April note correctly described outcomes as research preview at the time of that
  writing; this note correctly describes it as public beta now.

- **Extends**:
  - **blog-anthropic-claude-managed-agents.md** (April 2026): This May note
    extends the April note in three ways: (1) adds dreaming as an entirely new
    capability; (2) updates the status of outcomes and multiagent orchestration
    from research preview to public beta; (3) adds four new customer case studies
    (Harvey, Netflix, Spiral by Every, Wisedocs) not in the April launch post.
    The April note documented eight customers (Notion, Rakuten, Asana, Sentry,
    Atlassian, Vibecode, General Legal, Blockit); the May note documents four
    different ones, expanding the corpus of production deployment evidence.

- **Novel**:
  - **Dreaming as an architectural pattern**: No existing source note describes
    a batch, scheduled, between-session self-improvement mechanism for deployed
    agents. This is entirely new to our corpus. The closest analogue is Cursor's
    real-time RL (which also uses session data to improve future performance), but
    the mechanisms and requirements are very different.
  - **Two-layer memory architecture** (in-session memory + between-session
    dreaming): The explicit framing of these two layers as a coherent memory
    system — with different timescales and different scopes — is a new
    architectural concept for the guide.
  - **Mixed-model orchestration with named models**: The Spiral by Every case
    is the first explicit named-model assignment in a multiagent deployment in
    our corpus (Haiku = routing, Opus = generation). Practitioners now have a
    reference for how to assign models by role, not just by capability.
  - **Outcomes for quality enforcement in editorial/document workflows**: The
    Wisedocs and Spiral by Every cases extend outcomes beyond its Anthropic-internal
    benchmark (structured file generation) into editorial quality enforcement
    workflows. This expands the known use-case space for outcomes beyond what the
    April note documented.

## Guide Impact

- **Chapter 05 (Multi-Agent Orchestration)** or wherever multi-agent patterns
  land: Add the persistent event history pattern as a key infrastructure
  requirement. "Events are persistent and every agent remembers what it's done"
  is a prerequisite for mid-workflow lead-agent check-ins and error recovery.
  DIY multiagent harnesses must implement this; Managed Agents provides it. Add
  mixed-model orchestration (Haiku/Opus split) as a concrete cost optimization
  reference architecture alongside the fan-out parallelism pattern (Netflix).

- **Chapter on Agent Self-Improvement / Long-Running Agents**: Add dreaming as
  a new architectural pattern for agent self-improvement via batch processing of
  accumulated session history. Contrast with: in-session memory (real-time),
  outcomes-based iteration (within-session retry), and Cursor-style RL (model
  weights). Dreaming occupies a unique position: it's asynchronous, between-session,
  and operates at the memory layer rather than the model or inference layer.

- **Chapter 02 (Harness Engineering) build-vs-buy section** (introduced in
  blog-anthropic-claude-managed-agents.md guide impact): Update to note that
  outcomes and multiagent orchestration are now public beta — the April note
  should be revised to remove the "research preview" status qualifiers for
  these two capabilities.

- **Chapter on Model Selection / Cost Optimization**: Add mixed-model orchestration
  as a pattern — cheap fast models for routing/intake/triage, capable expensive
  models for high-value generation. The Spiral by Every case (Haiku + Opus) is
  the reference implementation. This is a cost-quality optimization that applies
  to any multiagent workflow with distinguishable low-value routing work and
  high-value generation work.

## Extraction Notes

- This note should be read as a direct update to `blog-anthropic-claude-managed-agents.md`
  (issue #205). The April note captures the launch; this May note captures the
  first evolution. The guide impact of the April note should be revisited in light
  of the status changes documented here (outcomes and multiagent now public beta).
- Four customer case studies in this post (Harvey, Netflix, Spiral by Every,
  Wisedocs) are entirely different from the eight cited in the April post, expanding
  the documented deployment evidence. None of the eight April customers appear in
  this post, suggesting Anthropic selected different customers for maximum novelty
  in the follow-up announcement.
- The "dreaming" access request path is described as a form submission (research
  preview with gated access). No URL is provided in the post for that form; it
  appears to be accessible from Claude Console.
- Public beta features (outcomes, multiagent orchestration, memory, webhooks) are
  described as available via Claude Console without a separate access request.
- The Wisedocs quote "Reviews now run 50% faster, while staying aligned with their
  team's standards" was attributed to Wisedocs in the post but the exact attributee
  (name/title) was not captured by WebFetch extraction. The quote itself is
  consistent across multiple fetch calls.
- The Harvey ~6x figure comes from Harvey's own internal tests, not Anthropic
  benchmarks. This makes it slightly more credible as an operational metric than
  vendor benchmarks, but still single-company and internal.
