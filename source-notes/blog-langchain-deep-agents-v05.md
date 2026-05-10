---
source_url: https://www.langchain.com/blog/deep-agents-v0-5
source_type: blog-post
title: "Deep Agents v0.5"
author: The LangChain Team
date_published: 2026-04-07
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#106"
---

# Deep Agents v0.5

> LangChain introduces async subagent delegation — fire-and-forget background tasks
> with task IDs, stateful threads for mid-task course-correction, and heterogeneous
> remote deployments — alongside a protocol comparison (ACP vs. A2A vs. Agent Protocol)
> that documents why thread-and-run models map better to async agent coordination than
> session-based or broadly interoperable alternatives.

## Source Context

- **Type**: blog-post (LangChain engineering/product blog, April 7, 2026; announcement
  of a feature release for their "Deep Agents" framework built on LangGraph Platform)
- **Author credibility**: LangChain Team — first-party engineering authors for the
  LangGraph/Deep Agents stack. Authority is high for claims about their own platform's
  design decisions (protocol selection, deployment architecture) and engineering
  rationale. Claims about ACP and A2A are LangChain's assessment of those protocols
  from an implementer's perspective — not independent audits. The post is a product
  changelog + design rationale post, not a controlled study; confidence grades reflect
  this.
- **Scope**: Covers three specific additions in Deep Agents v0.5: (1) async subagent
  delegation with five background-task tools; (2) protocol selection rationale comparing
  ACP, A2A, and Agent Protocol; (3) multimodal filesystem expansion (PDFs, audio, video).
  Does NOT cover: pricing, performance benchmarks, comparison with competing frameworks
  (e.g., Anthropic's Managed Agents), LangGraph internals, or how agents handle auth.
  The post is ~400 words — compact and specific.

## Extracted Claims

### Claim 1: Synchronous (inline) subagents block the supervisor's entire execution loop while running, making them a bottleneck for long-running tasks

- **Evidence**: First-party engineering rationale for the async feature introduction.
  Concrete use cases cited: deep research, large-scale code analysis, multi-step data
  pipelines.
- **Confidence**: settled (structural property of synchronous call semantics; the
  engineering claim is sound regardless of platform)
- **Quote**: "Inline subagents block the supervisor's execution loop while they run."
- **Our assessment**: This is the core architectural problem the release solves. The
  blocking model means a supervisor handling a research request cannot respond to the
  user or take other action until the subagent returns — regardless of how long the
  subagent takes. This is not a LangChain-specific limitation; it is a structural
  consequence of synchronous subagent invocation in any agent framework. The claim
  is settled because it describes a property of synchronous I/O, not a platform-
  specific behavior. Practitioners using any framework where subagents block the
  orchestrator's context window or event loop face this problem.

### Claim 2: Async subagents return a task ID immediately and execute independently on a remote server, enabling parallel execution and user interaction during subagent work

- **Evidence**: First-party feature description. The behavior is structural — returning
  a task ID rather than blocking is the defining property of the async model.
- **Confidence**: settled (definitional property of the async model)
- **Quote**: "return a task ID immediately and execute independently on a remote server"
- **Our assessment**: The task-ID model is well-understood from distributed systems.
  Its application to agent orchestration is the novel part: supervisors can now launch
  multiple subagents, continue working with the user, and poll or be notified when
  results are ready. The quote also confirms the execution happens on a remote server —
  the subagent is not running as a local coroutine but as a remote process. This has
  implications for authentication, latency, and failure modes (network partitions, remote
  server crashes) that synchronous subagents don't have.

### Claim 3: Async subagents are stateful — they maintain their own thread across interactions, enabling mid-task course-correction without losing context

- **Evidence**: First-party feature description. The statefulness claim is contrasted
  explicitly with inline subagents (which are implicitly stateless per invocation).
- **Confidence**: emerging (platform implementation claim; verifiable in practice but
  not independently corroborated)
- **Quote**: "Unlike inline subagents, async subagents are also stateful: they maintain
  their own thread across interactions, so the supervisor can send follow-up instructions
  or course-correct mid-task."
- **Our assessment**: Mid-task course-correction is a qualitatively different capability
  from both fire-and-forget tasks and synchronous subagents. A supervisor that launches
  a research subagent can observe early results (via check_async_task) and redirect the
  subagent's focus before the task completes — without cancelling and restarting from
  scratch. The thread model (preserving conversation history across supervisor–subagent
  exchanges) is what enables this: the subagent picks up where it left off rather than
  starting fresh. This aligns with the stateful-context design pattern documented in
  `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 3, where memory persistence
  across sessions enables self-improvement — here the mechanism is thread persistence
  within a task.

### Claim 4: Async subagents enable heterogeneous deployments — a lightweight orchestrator can delegate to specialized remote agents running on different hardware, different models, or with their own tool sets

- **Evidence**: First-party design rationale. The heterogeneous deployment claim is a
  direct architectural consequence of remote async execution.
- **Confidence**: emerging (design claim; coherent but dependent on deployment
  infrastructure practitioners must build or adopt)
- **Quote**: "heterogeneous deployments, where a lightweight orchestrator delegates to
  specialized remote agents running on different hardware, using different models, or
  maintaining their own tool sets"
- **Our assessment**: This unlocks a class of architectures not possible with inline
  synchronous subagents: a cheap orchestrator model (e.g., Haiku) dispatching to a
  specialized expensive model (e.g., Opus) for the intensive subtask, running on
  GPU-capable infrastructure, with domain-specific tools. This is what multi-agent
  coordination patterns describe as "agent teams" with persistent specialist context,
  but realized across a network boundary rather than within a single process. The
  architectural pattern is theoretically supported by existing coordination pattern
  descriptions; this release provides a concrete implementation path.

### Claim 5: Five tools manage the async subagent task lifecycle — launch, status check, update, cancel, and list

- **Evidence**: First-party API documentation embedded in the release post.
- **Confidence**: settled (the API is documented by the framework authors)
- **Quote**: (no single direct quote; see Concrete Artifacts for the full tool table)
- **Our assessment**: The five-tool API design is notable for what it includes and
  implies. `update_async_task` (send follow-up instructions to a running task) is
  the mechanism for mid-task course-correction (Claim 3). `cancel_async_task` implies
  explicit lifecycle control — a supervisor that detects early results are off-track
  can cancel and replan rather than waiting for a bad result. `list_async_tasks` enables
  a supervisor managing many parallel subagents to maintain awareness of the system state.
  The set is minimal and covers the full lifecycle without over-engineering.

### Claim 6: ACP (Agent Client Protocol) was rejected for async subagents because its synchronous session model doesn't map to async task delegation and it lacks HTTP transport for remote deployments

- **Evidence**: First-party protocol evaluation. Two specific technical blockers named.
- **Confidence**: emerging (LangChain's assessment of ACP at the time of writing;
  ACP may evolve)
- **Quote**: "ACP is purpose built for editor-to-agent communication" and "built around
  a synchronous session model where the client sends a prompt and waits for a response,
  which doesn't map cleanly to async subagents" and "currently only supports stdio
  transport, which means the remote agent has to run as a local subprocess. HTTP support
  is on the roadmap but hasn't shipped, so ACP isn't viable for remote deployments today."
- **Our assessment**: Both blockers are structural, not cosmetic. A synchronous session
  model fundamentally can't express "start this task and check back later" without
  wrapping it in a polling protocol — which would negate the async model. The stdio-
  only transport constraint means ACP agents must be local subprocesses, directly
  contradicting the heterogeneous remote deployment goal (Claim 4). The "HTTP on roadmap"
  note suggests LangChain monitored ACP's development and found it insufficiently
  mature for their release timeline. This is a useful protocol maturity signal for
  practitioners evaluating ACP for their own remote agent deployments.

### Claim 7: A2A (Agent-to-Agent Protocol) was evaluated and found technically compatible — full HTTP support and native async task model — but not selected because LangChain prioritized faster iteration over broad interoperability; A2A support may be added in a future release

- **Evidence**: First-party protocol evaluation. The claim that A2A is "technically
  compatible" is specific — LangChain evaluated it against their requirements and found
  it adequate on the technical merits.
- **Confidence**: emerging (LangChain's current assessment; the "may be added" qualifier
  signals this is a deferred decision, not a rejection)
- **Quote**: "A2A is a closer fit and is technically compatible. It has full HTTP support
  and a native async task model. It's a strong protocol and is designed to solve broad
  agent interoperability challenges."
- **Our assessment**: The A2A evaluation reveals an explicit trade-off between
  interoperability scope and iteration speed. A2A is designed for broad interoperability
  across heterogeneous vendors; Agent Protocol is LangChain's own specification optimized
  for their platform. LangChain chose the protocol they control (faster iteration, less
  coordination overhead) over the protocol designed for cross-vendor interoperability.
  The "may be added" signals this is not a permanent rejection — if the ecosystem
  standardizes on A2A, LangChain would be in a position to add support without
  architectural rework. Practitioners planning multi-vendor agent interoperability
  should monitor whether A2A support materializes.

### Claim 8: Agent Protocol was selected because it is built around threads and runs, maps directly to the async subagent state model, and is already the underlying protocol for LangGraph Platform

- **Evidence**: First-party design rationale. The thread-and-run model alignment is
  a specific technical justification, not just a business preference.
- **Confidence**: emerging (first-party claim about their own platform's design; the
  alignment claim is coherent)
- **Quote**: "Agent Protocol is built around threads and runs. You create a thread to
  hold conversation context, start a run to kick off work, and check on it when you
  need the result."
- **Our assessment**: The thread-and-run model is a natural fit for async task delegation:
  a thread holds the conversation context between supervisor and subagent; a run
  represents the active execution. The supervisor creates a thread, starts a run, gets
  back a task ID, checks on it later — which is exactly the five-tool API (Claim 5).
  The prior art (already underlying LangGraph Platform) is an important pragmatic
  reason: the protocol is already deployed and proven in production, rather than being
  adopted speculatively. Practitioners can serve their own Agent Protocol–compliant
  agents to be usable as async subagents in this framework.

### Claim 9: Omitting the URL field enables ASGI co-deployment, where supervisor and subagents communicate in the same process without a network boundary

- **Evidence**: First-party implementation detail in the configuration documentation
  embedded in the post.
- **Confidence**: settled (documented behavior of the framework)
- **Quote**: "If the `url` field is omitted, Deep Agents will use ASGI transport to
  communicate with the sub-agent. This allows supervisor and sub-agents to be
  co-deployed and communicate in the same process."
- **Our assessment**: The ASGI transport option is significant for local development
  and for deployments where network latency or overhead is a concern. A practitioner
  can develop and test async subagent logic without standing up a remote server, then
  swap to HTTP-based remote deployment by adding a `url` field. This is a good
  ergonomic choice — the same code works locally (ASGI) and in production (HTTP remote).
  It also means the remote-execution failure modes (network partitions, server crashes)
  don't apply to co-deployed configurations, lowering the barrier to adopting the
  async model.

### Claim 10: Multimodal filesystem support expanded from images-only to PDFs, audio, video, and other file types using the same read_file tool with automatic MIME-type detection

- **Evidence**: First-party feature description. The "no API change" and "automatic
  detection" claims are specific implementation details.
- **Confidence**: settled (first-party feature documentation from the framework authors)
- **Quote**: "Deep Agents previously supported reading images from its virtual filesystem.
  This release extends multimodal support to PDFs, audio, video, and other file types."
  and "The agent uses the same `read_file` tool; no API change is required. File type
  is detected automatically from the extension, and the content is passed to the model
  as a native content block with the appropriate MIME type."
- **Our assessment**: The backward-compatible API design (same tool, automatic detection)
  is a good extensibility pattern — existing agents that use read_file for images get
  PDF/audio/video support for free without code changes. The "native content block with
  appropriate MIME type" phrasing aligns with how modern multimodal LLM APIs handle
  non-text inputs — the framework handles the encoding, the agent just reads the file.
  The caveat is that supported modalities depend on the underlying model (Claim 11).

### Claim 11: Supported multimodal input types depend on the underlying model — practitioners must check model profiles to know which modalities are available

- **Evidence**: First-party capability documentation. The model profiles feature is
  named as the introspection mechanism.
- **Confidence**: settled (model capability variation is a well-known constraint;
  the model profiles mechanism is a first-party documentation claim)
- **Quote**: "Which modalities are supported depends on the underlying model. You can
  check supported modalities programmatically via model profiles—each LangChain chat
  model exposes a profile that declares which input types it accepts."
- **Our assessment**: The model profiles API is the correct pattern for capability
  introspection: rather than hardcoding modality assumptions, agents check what the
  model supports at runtime. This is important for practitioners building agents intended
  to work across multiple models — the same agent definition should gracefully degrade
  or route to model-appropriate tasks based on profile data. For Ch04, this is a
  concrete mechanism for context routing based on model capability.

## Concrete Artifacts

### Python Configuration: Creating an Agent with an Async Subagent

```python
# Source: "Deep Agents v0.5," LangChain Team, April 7, 2026

from deepagents import AsyncSubAgent, create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    subagents=[
        AsyncSubAgent(
            name="researcher",
            description="Performs deep research on a topic.",
            url="https://my-agent-server.dev",
            graph_id="research_agent",
        ),
    ],
)
```

Note: Omit `url` to use ASGI co-deployment (same process). Supply `url` for remote
HTTP deployment using Agent Protocol.

### Async Task Management Tool API

```
# Source: "Deep Agents v0.5," LangChain Team, April 7, 2026

Tool               | Purpose
-------------------|----------------------------------------------------------
start_async_task   | Launch task on remote agent; returns task ID immediately
check_async_task   | Poll status and retrieve results when complete
update_async_task  | Send follow-up instructions to a running task
cancel_async_task  | Cancel a running task
list_async_tasks   | List all tracked tasks with their statuses
```

### Protocol Comparison (at time of v0.5 release)

```
# Source: "Deep Agents v0.5," LangChain Team, April 7, 2026

Protocol         | Fit for async subagents | HTTP transport | Selected?
-----------------|-----------------------|----------------|----------
ACP              | No — synchronous session model; no HTTP | stdio only | No
A2A              | Yes — native async task model, full HTTP | Yes | No (deferred)
Agent Protocol   | Yes — thread+run model maps to async | Yes (ASGI/HTTP) | Yes
```

**Agent Protocol selection rationale**: Already underlies LangGraph Platform; thread-
and-run model maps directly to async subagent state; LangChain controls the spec for
faster iteration. A2A deferred (not rejected): "Support for A2A may be added in a
future release."

## Cross-References

- **Corroborates**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 4 (agent teams vs.
    subagents: subagents are bounded, teammates are persistent and accumulate context):
    Async subagents in Deep Agents v0.5 occupy a middle ground — they are not bounded
    synchronous tasks (stateless per invocation) but they are also not persistent
    teammates that accumulate domain context over time. The stateful thread model (Claim 3
    here) enables something between the two: a bounded task that can receive mid-task
    updates but does not persist beyond task completion. This adds nuance to the
    two-category taxonomy in the Anthropic coordination patterns note.
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 3 (information bottleneck
    as the core failure mode of orchestrator-subagent): The blocking-supervisor problem
    (Claim 1 here) is a concrete manifestation of the information bottleneck failure mode.
    When a subagent blocks the supervisor, the supervisor cannot route new information
    to other subagents or to the user. Async delegation directly unblocks this.
  - `blog-anthropic-claude-managed-agents.md` Claim 3 (long-running sessions operating
    autonomously for hours, persisting through disconnections): Anthropic's Managed
    Agents platform claims to solve the same long-running autonomy problem at a
    platform/hosted level. Deep Agents v0.5 solves it at the framework level via
    async subagents. The two are parallel solutions targeting the same problem on
    different architectural layers (hosted platform vs. open framework).
  - `docs-ghaw-inline-sub-agents.md` Claim 1 (inline sub-agents embedded in workflow
    markdown files): gh-aw inline sub-agents are synchronous — the parent workflow
    invokes them and waits. Deep Agents' async subagents invert this: the supervisor
    delegates and continues rather than waiting. These are architecturally complementary
    — different platforms with different synchrony models for sub-agent delegation.

- **Contradicts**: None filed. No existing corpus source makes claims about ACP, A2A,
  or Agent Protocol that conflict with the protocol evaluation here. The async subagent
  model here is additive to existing synchronous subagent patterns in the corpus, not
  contradictory. The heterogeneous deployment claim (Claim 4) is consistent with but
  more specific than the remote-agent mentions in `blog-anthropic-claude-managed-agents.md`.

- **Extends**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 7 (recommended default:
    orchestrator-subagent) and Claim 8 (how long workers must maintain context determines
    pattern): Those claims address coordination topology for synchronous subagents. Deep
    Agents v0.5 adds the async dimension: when subtasks are long-running and blocking is
    unacceptable, async delegation enables the orchestrator-subagent pattern without
    the supervisor blocking. The decision criterion from Claim 8 there ("does the subtask
    require the agent to remember what it did in step 1 while executing step 5?") now
    has an additional axis: does the task need to run in the background while the
    supervisor continues working? If yes, async subagent.
  - `blog-anthropic-harness-long-running.md` (GAN-inspired generator/evaluator for
    long-running tasks): That post addressed the problem of long-running tasks using
    a synchronous generator/evaluator loop with sprint decomposition. Deep Agents v0.5
    offers a different approach to the same underlying problem: rather than decomposing
    long tasks into synchronous sprints, delegate them as async background tasks. These
    are complementary patterns; the right choice depends on whether the supervisor needs
    to actively coordinate between steps.

- **Novel**:
  - **Fire-and-forget async subagent delegation with task ID model**: No existing corpus
    source describes the task-ID-based async delegation pattern for agents. Existing
    coordination pattern sources describe synchronous delegation (orchestrator dispatches,
    waits for result, synthesizes). This is the first corpus source documenting the async
    version.
  - **Mid-task course-correction as a first-class capability**: The ability to send
    follow-up instructions to a running subagent (via `update_async_task`) without
    cancelling and restarting is new to the corpus. Existing sources describe retries and
    evaluator loops but not mid-task steering of a running agent.
  - **Protocol comparison: ACP vs. A2A vs. Agent Protocol** for agent interoperability:
    No existing corpus source addresses agent interoperability protocol standards. This
    is the first corpus coverage of Agent Protocol, ACP, and A2A as competing standards,
    with specific technical trade-offs documented.
  - **ASGI co-deployment transport as a local-development path**: No existing source
    describes ASGI as a transport mechanism between an orchestrator and its subagents.
    This is a useful ergonomic pattern for local development and testing.
  - **Model profiles for capability introspection**: The ability to programmatically
    query which modalities a given model supports (model profiles API) is new to the
    corpus. Existing sources treat model capability as static knowledge; this adds a
    runtime introspection mechanism.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add async subagent delegation as a harness
  pattern for long-running tasks. The current coordination patterns taxonomy
  (`blog-anthropic-multi-agent-coordination-patterns.md`) covers synchronous delegation
  only. This source adds the async dimension: when subtasks are long-running (research,
  code analysis, data pipelines) and blocking the supervisor is unacceptable, async
  delegation with task IDs enables the orchestrator-subagent pattern without suspension
  of the supervisor. The five-tool API (Concrete Artifacts) is the reference
  implementation.

- **Chapter 02 (Harness Engineering)**: The protocol comparison (Concrete Artifacts →
  Protocol Comparison table) is directly relevant to any practitioner deciding how to
  implement remote agent communication. Document ACP, A2A, and Agent Protocol as the
  three candidate standards, with LangChain's evaluation as the primary evidence for
  trade-offs. The key decision variables: synchrony model (ACP is synchronous; A2A and
  Agent Protocol are async-native) and transport (ACP is stdio-only today; A2A and
  Agent Protocol support HTTP).

- **Chapter 03 (Safety and Verification)**: Protocol standardization (Agent Protocol,
  A2A) is relevant to the interoperability and auditability dimensions of agent safety.
  Standardized protocols enable structured logging and tracing across agent boundaries.
  Note that LangChain deferred A2A in favor of faster iteration — a real trade-off
  between safety/auditability features (standardized interoperability) and development
  velocity.

- **Chapter 04 (Context Engineering)**: Mid-task course-correction (Claim 3, Claim 5)
  is a new context engineering pattern: the supervisor can observe intermediate results
  from a running async subagent and send updated instructions without losing the
  subagent's accumulated thread context. This enables progressive context refinement
  across the supervisor–subagent boundary — more nuanced than either synchronous
  dispatch (no mid-task correction) or cancellation and restart (loses all progress).
  Add to Ch04's coverage of context preservation across agent boundaries.

- **Chapter 04 (Context Engineering)**: Model profiles for capability introspection
  (Claim 11) belong in any Ch04 section on context routing — directing specific content
  types (PDFs, audio, video) to models that support those modalities. The model profiles
  API is a concrete implementation mechanism.

## Extraction Notes

- The source URL (https://blog.langchain.com/deep-agents-v0-5/) redirected with HTTP
  301 to https://www.langchain.com/blog/deep-agents-v0-5, which was fetched successfully.
- The post is compact (~400 words, 4 minutes read time) but covers three distinct
  features: async subagents, protocol selection, and multimodal expansion. All three
  were extracted fully.
- The post explicitly names three protocols (ACP, A2A, Agent Protocol) with specific
  technical trade-offs. This is unusual precision for a product blog post and suggests
  the LangChain team did a careful protocol evaluation before shipping.
- No sub-pages were followed — the post is self-contained with no substantive linked
  pages beyond what's mentioned in passing.
- No existing corpus source covers LangChain's Deep Agents framework, Agent Protocol,
  ACP, or A2A. Cross-references are to adjacent topics (coordination patterns, long-
  running tasks, inline sub-agents) rather than direct overlaps.
- The Prospector's triage identified "no existing coverage of async subagents or Agent
  Protocol patterns in current source notes" — confirmed by extraction.
