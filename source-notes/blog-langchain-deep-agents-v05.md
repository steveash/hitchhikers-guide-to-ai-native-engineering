---
source_url: https://www.langchain.com/blog/deep-agents-v0-5
source_type: blog-post
title: "Deep Agents v0.5"
author: LangChain Team
date_published: 2026-04-07
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#106"
---

# Deep Agents v0.5

> LangChain's v0.5 release note introducing async (non-blocking) subagents — a
> fire-and-forget delegation pattern that lets a supervisor continue working while
> remote sub-tasks execute — along with an explicit three-way protocol selection
> rationale (Agent Protocol over ACP and A2A) and expanded multimodal filesystem
> support.

## Source Context

- **Type**: blog-post (LangChain blog, April 7, 2026; ~4 min read; byline "The
  LangChain Team")
- **Author credibility**: The LangChain Team writes for LangChain, the
  maintainers of LangGraph, LangSmith, and the Deep Agents platform. This is a
  first-party product release note. Claims about what Deep Agents v0.5 provides
  are authoritative for the product. The protocol comparison (ACP vs. A2A vs.
  Agent Protocol) reflects LangChain's own architectural decision with stated
  reasoning — it represents their evaluation, not a neutral third-party analysis.
  No customer benchmarks or testimonials appear.
- **Scope**: Covers two feature areas: (1) async subagents — motivation, five
  management tools, three-protocol comparison, and co-deployment option;
  (2) expanded multimodal filesystem support for PDFs, audio, video, and other
  file types. Does NOT cover: benchmarks, customer deployments, pricing, or
  breaking API changes. This is a minor-version release note on top of the
  initial Deep Agents platform launch documented in
  `blog-langchain-deep-agents-deploy.md` (issue #132).

## Extracted Claims

### Claim 1: Inline subagents block the supervisor's execution loop while they run, creating a bottleneck as addressable task lengths increase

- **Evidence**: The motivation section of the post. Presented as the structural
  limitation that async subagents solve.
- **Confidence**: emerging (first-party characterization of the failure mode; the
  underlying claim — synchronous subagent calls block the calling agent — is
  architecturally sound and not vendor-specific)
- **Quote**: "Inline subagents are effective for short, focused tasks, but they
  block the supervisor's execution loop while they run."
- **Our assessment**: This is the clearest statement of the inline-vs-async
  trade-off in our corpus. The failure mode is real: any synchronous subagent
  call holds the supervisor until the subagent completes, preventing the
  supervisor from responding to users, launching other work, or handling
  interrupts. The problem compounds as tasks grow longer — research, code
  analysis, and data pipelines can run for minutes rather than seconds. This
  motivates the async pattern independently of any vendor product.

### Claim 2: Async subagents use a fire-and-forget interaction model — the supervisor launches a task and continues working while the subagent executes independently on a remote server

- **Evidence**: The "Async Subagents" section; the fire-and-forget model is
  described as the core interaction pattern.
- **Confidence**: emerging (first-party feature description; the fire-and-forget
  + task-ID pattern is a standard async programming pattern applied to agent
  delegation)
- **Quote**: "The interaction model is fire-and-forget: the main agent launches a
  task, continues working or talking to the user, and checks back for results
  when needed."
- **Our assessment**: The concrete user-visible benefit — the supervisor "continues
  working or talking to the user" — converts what would otherwise be an extended
  silence (synchronous wait) into a live interaction with the user while work
  proceeds in the background. For practitioners designing long-running
  orchestration workflows, the choice between synchronous and async subagent
  delegation directly determines whether the user experience degrades while
  sub-tasks run.

### Claim 3: Async subagents are stateful with their own thread — the supervisor can send mid-task follow-up instructions and course-correct without restarting the subagent

- **Evidence**: Explicit claim in the async subagents section; the thread
  persistence property is described as the mechanism enabling mid-task updates.
- **Confidence**: emerging (first-party feature description; the thread model is
  the same abstraction as OpenAI's Assistants API threads)
- **Quote**: "Unlike inline subagents, async subagents are also stateful: they
  maintain their own thread across interactions, so the supervisor can send
  follow-up instructions or course-correct mid-task."
- **Our assessment**: Thread persistence is what distinguishes this from simple
  fire-and-forget remote calls. Without thread state, a mid-task update would
  require canceling and restarting. With thread state, the supervisor's
  follow-up instruction arrives as a new message in the subagent's existing
  conversation — the subagent can incorporate course corrections without losing
  prior progress. This is the most novel behavioral property introduced in v0.5.

### Claim 4: Deep Agents v0.5 provides five dedicated tools for the complete async task lifecycle: start, check, update, cancel, and list

- **Evidence**: Explicit table in the post listing the five tools with their
  purposes.
- **Confidence**: settled (first-party API documentation; specific tool names
  from the product release)
- **Quote**: (no single direct quote captures all five; tool names from a table)
- **Our assessment**: The five tools cover the full lifecycle of an async task:
  launch (`start_async_task`) → monitor (`check_async_task`) → steer
  (`update_async_task`) → terminate (`cancel_async_task`) → audit
  (`list_async_tasks`). Having `cancel_async_task` as a first-class tool is the
  correct design for safety: supervisors should be able to abort in-flight work,
  not only wait for completion. The `list_async_tasks` tool enables a supervisor
  managing multiple concurrent subagents to maintain awareness of all in-flight
  work.

### Claim 5: ACP was rejected for async subagent communication because its synchronous session model doesn't map to async tasks and it only supports stdio transport

- **Evidence**: Protocol comparison section; ACP's two problems are stated
  explicitly.
- **Confidence**: emerging (LangChain's own evaluation of ACP as of April 2026;
  stated as first-party assessment, not independent analysis)
- **Quote**: "ACP has two problems for our use case. First, it's built around a
  synchronous session model where the client sends a prompt and waits for a
  response, which doesn't map cleanly to async subagents. Second, it currently
  only supports stdio transport, which means the remote agent has to run as a
  local subprocess."
- **Our assessment**: Both objections are architectural, not incidental. The
  synchronous session model is the fundamental mismatch: async subagents require
  a non-blocking dispatch model, which ACP's request-response structure cannot
  provide. The stdio-only transport restriction makes ACP unsuitable for
  distributed deployments where the supervisor and subagent run on different
  hosts — a core use case for heterogeneous agent teams. ACP appears for the
  first time in our corpus here; this evaluation is the only characterization
  we have.

### Claim 6: A2A was acknowledged as a close fit with full HTTP and native async task support, but was not selected because async subagents are still evolving and required a protocol allowing faster iteration

- **Evidence**: Protocol comparison section; A2A is acknowledged as technically
  compatible but not selected for iteration-speed reasons.
- **Confidence**: emerging (LangChain's own assessment; the characterization of
  A2A's capabilities is the most detailed in our corpus; the iteration-speed
  rationale is stated but not elaborated)
- **Quote**: "A2A is a closer fit and is technically compatible. It has full
  HTTP support and a native async task model...However, since async subagents are
  still evolving, we prioritized a protocol that allows for faster iteration."
- **Our assessment**: This is a qualified endorsement of A2A rather than a
  rejection. LangChain describes A2A as having the right design
  ("push/pull subscriptions, agent discovery, capability negotiation") but
  defers it because evolving an external standard is slower than evolving their
  own spec. The explicit statement that A2A "is technically compatible" and
  "future support is possible" makes this a "not yet" rather than "no." For
  practitioners evaluating agent-to-agent protocols, this note is the most
  detailed comparative assessment in the corpus.

### Claim 7: Agent Protocol was selected because its threads-and-runs model maps directly onto async subagent semantics — a thread holds context and a run dispatches work, matching how subagents operate across mid-task updates

- **Evidence**: Protocol selection rationale; the thread-run mapping is presented
  as the primary reason for selection alongside LangChain's existing investment
  in the spec.
- **Confidence**: emerging (first-party selection rationale; the architectural fit
  argument is coherent and the threads+runs model is well-established in agent
  infrastructure)
- **Quote**: "Agent Protocol is built around threads and runs. You create a thread
  to hold conversation context, start a run to kick off work, and check on it
  when you need the result. That maps directly onto how async subagents work."
- **Our assessment**: The thread-run abstraction enables Claim 3's stateful
  mid-task updates without additional infrastructure: a mid-task follow-up from
  the supervisor is a new run on the existing thread, and the subagent picks up
  with its full prior context intact. The second reason for selection — Agent
  Protocol already underlies LangGraph Platform — means LangChain can iterate
  quickly on the spec without third-party coordination.

### Claim 8: Mid-task updates preserve subagent thread history — when the supervisor sends a follow-up instruction, the remote agent picks up in context rather than starting fresh

- **Evidence**: Agent Protocol selection section; this property is described as
  a direct consequence of the threads model.
- **Confidence**: emerging (first-party claim; the mechanism — thread history
  preservation on follow-up — follows from the Agent Protocol design)
- **Quote**: "It also means subagents are stateful across interactions. When you
  send a mid-task update, the remote agent picks up in context because the thread
  history is preserved."
- **Our assessment**: This directly addresses the information bottleneck failure
  mode of orchestrator-subagent patterns (see Cross-References). When a
  supervisor discovers new information mid-workflow that changes what a subagent
  should do, it can send an update rather than canceling and restarting. The
  subagent receives the update in the context of everything it has already done —
  making course correction a first-class operation rather than a workaround.

### Claim 9: Any Agent Protocol-compliant service is a valid async subagent target — LangSmith-deployed agents, custom FastAPI services using server stubs, or any other compliant implementation

- **Evidence**: "Server Protocol Details" section; three categories of valid
  targets are named with example links.
- **Confidence**: settled (first-party documentation; the interoperability claim
  follows directly from Agent Protocol being an open specification)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The open-target design is the key architectural benefit of
  building on an open protocol: practitioners are not locked into LangSmith-
  deployed agents as subagents. Any existing service that implements Agent
  Protocol — including a custom FastAPI service wrapping a legacy system — can
  participate as an async subagent. This enables the heterogeneous deployment
  pattern: a lightweight orchestrator can delegate to specialized remote agents
  regardless of how those agents are built or deployed.

### Claim 10: If the `url` field is omitted, Deep Agents uses ASGI transport for same-process supervisor-subagent communication, enabling co-deployment without network round-trips

- **Evidence**: Implementation detail in the async subagents section; presented
  as a co-deployment convenience.
- **Confidence**: emerging (first-party feature description)
- **Quote**: "If the `url` field is omitted, Deep Agents will use ASGI transport
  to communicate with the sub-agent."
- **Our assessment**: The ASGI transport option solves a development ergonomics
  problem: teams can run supervisor + sub-agents in the same process for local
  development without setting up separate servers. The design cleanly separates
  the communication model (ASGI vs. HTTP) from the semantic model (threads+runs),
  so switching from local co-deployment to distributed production deployment
  requires only adding the `url` parameter. This is a practical escape hatch
  that makes local testing significantly simpler.

### Claim 11: Deep Agents v0.5 adds PDFs, audio, video, and other file types to the existing image support in the virtual filesystem, using the same `read_file` tool with automatic extension-based type detection

- **Evidence**: "Expanded Multi-Modal Support" section; the design decision to
  reuse `read_file` and auto-detect from extension is described explicitly.
- **Confidence**: settled (first-party feature documentation; specific file types
  named)
- **Quote**: "Importantly, which modalities are supported depends on the
  underlying model."
- **Our assessment**: The API-stable design (same `read_file` tool, no new call
  signatures) means existing agents that read images gain multimodal capability
  without code changes. The critical caveat — modality support depends on the
  underlying model — means practitioners cannot assume PDF or audio support
  across all model providers. The model profile mechanism (each LangChain chat
  model exposes a profile declaring accepted input types) is the correct
  architecture for this constraint: the framework checks capability before
  passing an unsupported content block.

### Claim 12: Model capability for multimodal input is introspectable at runtime via model profiles — each LangChain chat model exposes a profile declaring its accepted input types

- **Evidence**: Implementation detail in the multimodal section.
- **Confidence**: emerging (first-party feature description; the mechanism is
  described at a high level without implementation detail)
- **Quote**: (no direct quote; described without verbatim-extractable definition)
- **Our assessment**: Model profiles solve the multi-provider multimodal
  capability question programmatically. Deep Agents supports nine model
  providers (from `blog-langchain-deep-agents-deploy.md`), and their multimodal
  capabilities differ. Hardcoding per-model capability flags becomes a
  maintenance burden; profiles let each model self-declare, so adding a new
  provider or updating a model's capabilities requires updating the profile,
  not the application code.

## Concrete Artifacts

### Async Subagent Definition (from release note)

```python
# Source: "Deep Agents v0.5," LangChain Team, 2026-04-07
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

`AsyncSubAgent` specs mix freely with existing `SubAgent` and `CompiledSubAgent`
specs. `create_deep_agent` routes each to the appropriate middleware based on
type. Omit `url` to use ASGI co-deployment transport.

### Five Async Task Management Tools

```
# Source: "Deep Agents v0.5," LangChain Team, 2026-04-07

Tool                 | Purpose
---------------------+----------------------------------------------------------
start_async_task     | Launch task on remote agent; returns task ID immediately
check_async_task     | Poll task status; retrieve result when complete
update_async_task    | Send follow-up instructions to a running task
cancel_async_task    | Cancel a running task
list_async_tasks     | List all tracked tasks with current statuses

Interaction model: fire-and-forget.
  "The main agent launches a task, continues working or talking to the user,
   and checks back for results when needed."
Multiple async subagents run concurrently.
```

### Protocol Comparison (from release note)

```
# Source: "Deep Agents v0.5," LangChain Team, 2026-04-07

ACP (Agent Client Protocol)
  Status:  REJECTED
  Reason 1: "built around a synchronous session model where the client sends
             a prompt and waits for a response, which doesn't map cleanly to
             async subagents"
  Reason 2: "currently only supports stdio transport, which means the remote
             agent has to run as a local subprocess"
  HTTP support: No (roadmap)
  Async model: No

A2A (Agent-to-Agent Protocol)
  Status:  DEFERRED ("not yet")
  Reason:  "since async subagents are still evolving, we prioritized a
            protocol that allows for faster iteration"
  Note:    "technically compatible" — "full HTTP support and a native async
            task model"; future support described as possible
  Async model: Yes (native)
  Features: push/pull subscriptions, agent discovery, capability negotiation

Agent Protocol  ← SELECTED
  Basis:   LangChain's own open specification; already underlies LangGraph
  Model:   Threads + runs
           "You create a thread to hold conversation context, start a run
            to kick off work, and check on it when you need the result."
  Async fit: "That maps directly onto how async subagents work."
  State:   "When you send a mid-task update, the remote agent picks up in
            context because the thread history is preserved."
  Transport: HTTP (remote, url specified) or ASGI (co-deployed, url omitted)
```

### Async Subagent Deployment Options

```
# Source: "Deep Agents v0.5," LangChain Team, 2026-04-07

REMOTE (url specified in AsyncSubAgent):
  Transport: HTTP
  Valid targets (any Agent Protocol-compliant implementation):
    - Agents deployed with LangSmith
    - Custom FastAPI service using server stubs
    - Any other Agent Protocol-compliant implementation
  Examples:
    Python: github.com/langchain-ai/deepagents/tree/main/examples/async-subagent-server
    JS:     github.com/langchain-ai/deepagentsjs/tree/main/examples/async-subagent-server

CO-DEPLOYED (url omitted):
  Transport: ASGI (same-process)
  "If the `url` field is omitted, Deep Agents will use ASGI transport to
   communicate with the sub-agent."
  Use: local development, testing, co-located supervisor + sub-agents
```

## Cross-References

- **Corroborates**:
  - `blog-langchain-deep-agents-deploy.md` (Claim 2): That post characterizes
    the production deployment problem as three steps (orchestration + sandboxes
    + endpoints). Async subagents extend the architecture by adding remote agent
    delegation on top of that deployment foundation. Both posts share the
    underlying premise that synchronous, single-machine agent execution is
    insufficient for production workloads.
  - `blog-anthropic-managed-agents-dreaming-outcomes.md` (Claim 7): Managed
    Agents describes "events are persistent and every agent remembers what it's
    done" and a lead agent that can "check back in with other agents mid-workflow."
    The async subagent thread-persistence property (Claim 3 here) is the
    open-source parallel of that Anthropic-side capability — both products
    independently converge on stateful threads as the mechanism for mid-workflow
    coordination.
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 7): "For most
    use cases, we recommend starting with orchestrator-subagent. It handles the
    widest range of problems with the least coordination overhead." Async
    subagents are the Deep Agents implementation of the orchestrator-subagent
    pattern, adding the non-blocking property that makes the pattern practical
    for longer-running sub-tasks.

- **Extends**:
  - `blog-langchain-deep-agents-deploy.md` (Claim 7): The predecessor post lists
    A2A as an endpoint "so you can call your deployed agents in a multi-agent
    setup" and Agent Protocol as "so you can easily write beautiful UIs." This
    v0.5 post provides the actual implementation rationale for choosing Agent
    Protocol over A2A for async subagent communication — Agent Protocol is now
    used as the supervisor-subagent coordination channel, extending its role
    beyond UI-building. The A2A vs. Agent Protocol trade-off is now documented
    with technical depth that the earlier post lacked.
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 3): That note
    identifies the "information bottleneck" as the core failure mode of
    orchestrator-subagent: subagents completing bounded tasks surface
    cross-cutting insights the orchestrator cannot efficiently route back. The
    `update_async_task` tool (mid-task follow-up instructions, Claim 3 here)
    directly addresses this failure mode — the supervisor can steer a running
    subagent when new information arrives, without canceling and restarting.
    Thread history preservation (Claim 8 here) means the course correction
    arrives in full context.
  - `blog-langchain-deep-agents-deploy.md` (Claim 9): The predecessor described
    co-deployment sandboxes (Daytona, Runloop, Modal, LangSmith) as the
    execution environment model. This v0.5 post adds the remote-agent-as-subagent
    deployment model — where the "subagent" is a separate running service rather
    than a sandboxed process — which is architecturally distinct from the sandbox
    model. The two deployment models serve different purposes: sandboxes for
    code execution; remote agents for specialized agent capabilities.

- **Contradicts**: None filed. The A2A characterization in
  `blog-langchain-deep-agents-deploy.md` (Claim 7, where A2A is listed as a
  deployed-agent endpoint for multi-agent setups) and this post's protocol
  comparison (A2A acknowledged as well-designed but not selected for the
  orchestrator-to-subagent communication channel) reflect different layers of
  the same stack. The deployed-agent endpoint surface (A2A is still available
  for callers reaching a deployed Deep Agent) vs. the internal orchestration
  channel (Agent Protocol is used between supervisor and async subagents) are
  distinct; no factual conflict.

- **Novel**:
  - **Async fire-and-forget subagent delegation as a named pattern with a
    five-tool API**: No existing corpus note documents an open-source agent
    framework providing async non-blocking subagent delegation with a dedicated
    start/check/update/cancel/list task management API. Claude Managed Agents
    has async coordination, but as managed infrastructure; this is the
    open-source equivalent.
  - **ASGI co-deployment transport for same-process supervisor-subagent
    communication**: The option to omit `url` and use in-process ASGI transport
    for co-deployed agents is not described elsewhere in the corpus. It is a
    practical development ergonomic with no prior precedent.
  - **Three-way protocol comparison with explicit selection rationale (ACP vs.
    A2A vs. Agent Protocol)**: This is the first detailed agent-to-agent
    communication protocol comparison in the corpus. ACP appears for the first
    time here; the characterization of A2A as "technically compatible" but
    deferred for iteration speed is the most specific trade-off analysis of A2A
    in the corpus.
  - **Mid-task subagent steering via `update_async_task` with thread history
    preservation**: The ability to send follow-up instructions to a running
    subagent while preserving its full context is not described in any existing
    corpus note. It converts async subagents from pure fire-and-forget into
    steerable background processes.
  - **Model capability introspection via model profiles**: The mechanism of
    each LangChain chat model exposing a profile declaring its accepted input
    types is not described in any existing corpus note. It is a practical
    solution to the "does this model support this file type?" question in
    multi-model multimodal deployments.

## Guide Impact

- **Chapter 02 (Harness Engineering — Orchestrator-Subagent Pattern)**: Add
  async subagent delegation as the practical mechanism for applying the
  orchestrator-subagent pattern (from `blog-anthropic-multi-agent-coordination-
  patterns.md`) to long-running sub-tasks. The key guidance: when subagents are
  long-running, synchronous delegation creates a bottleneck; use async delegation
  so the supervisor remains responsive during subagent execution. The five-tool
  API (Concrete Artifacts) is the reference implementation.

- **Chapter 02 (Harness Engineering — Protocol Landscape)**: Add the three-way
  protocol comparison (ACP vs. A2A vs. Agent Protocol, Concrete Artifacts) as
  the most detailed agent-to-agent communication protocol trade-off analysis in
  the corpus. Specifically: ACP's stdio-only transport disqualifies it for
  distributed deployments; A2A is technically capable but its size imposes
  iteration costs; Agent Protocol's threads+runs model fits async task semantics
  and allows faster evolution. This expands the protocol landscape section that
  `blog-langchain-deep-agents-deploy.md` opened by naming A2A and Agent Protocol
  without trade-off detail.

- **Chapter 02 (Harness Engineering — Safety)**: The `cancel_async_task` tool
  should be called out explicitly as a required safety mechanism in any async
  subagent system, not an optional one. Orchestrators should include cancellation
  paths in their control flow rather than relying on timeout-based termination.

- **Chapter 04 (Context Engineering — Mid-Task State)**: Mid-task subagent
  steering (`update_async_task` + thread history preservation, Claim 8) is a
  new form of context management: the supervisor can inject new context into a
  running subagent's thread without full restart. This is a lightweight
  alternative to the sprint-decomposition + context-reset pattern from
  `blog-anthropic-harness-long-running.md` when the subagent is making progress
  but needs redirection.

- **Chapter 04 (Context Engineering — Multimodal)**: Add the model profile
  introspection mechanism (Claim 12) as the correct pattern for multimodal-
  capable harnesses: query modality support at runtime from model profiles
  rather than hardcoding it per model. This future-proofs multimodal harnesses
  against model upgrades and provider changes.

## Extraction Notes

- The source URL `blog.langchain.com/deep-agents-v0-5/` redirects to
  `www.langchain.com/blog/deep-agents-v0-5`. The `source_url` frontmatter uses
  the canonical form.
- Two WebFetch passes were performed: the first for full content extraction and
  the second for verbatim quote verification of key claims. Quotes in the
  Extracted Claims section come from the second, quote-targeted pass and are
  confirmed to be character-for-character from the source. Where the extraction
  showed truncated fragments, "(no direct quote; see paraphrase in Our
  assessment)" was used rather than reconstructing.
- ACP (Agent Client Protocol) appears for the first time in this corpus. No
  prior corpus note mentions ACP. Its description here is from LangChain's
  perspective; independent documentation was not fetched.
- The code example uses `model="anthropic:claude-sonnet-4-6"`. The
  `provider:model-id` string format is LangChain's model provider convention.
- Three related LangChain posts from May 2026 were referenced in the article
  sidebar and may warrant separate extraction: "Introducing Managed Deep Agents"
  (May 13, 2026), "New in Deep Agents v0.6" (May 13, 2026), and "Give Your
  Agents an Interpreter" (May 20, 2026). These likely document the continued
  evolution of the async subagent pattern introduced here.
- Confidence set to `emerging`: the feature claims are first-party from LangChain
  (high credibility on their own product), the architectural patterns are
  technically sound, but the async subagent system was new at v0.5 (April 2026)
  and no independent practitioner validation exists in the corpus at extraction
  time.
