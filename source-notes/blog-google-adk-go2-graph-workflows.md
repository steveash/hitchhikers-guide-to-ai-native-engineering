---
source_url: https://developers.googleblog.com/announcing-adk-go-20/
source_type: blog-post
title: "ADK for Go 2.0: build agent workflows as a graph"
author: Toni Klopfenstein (Developer Relations Engineer, ADK Developer Relations) and Sampath Kumar Maddula (Developer Programs Engineer), Google Developers Blog
date_published: 2026-06-30
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: settled
issue: "#1710"
---

# ADK for Go 2.0: build agent workflows as a graph

> Google's first-party 2.0 launch of Agent Development Kit (ADK) for Go,
> whose headline feature is a graph-based workflow engine — nodes and edges
> compose into an `agent.Agent`, with durable, cross-restart human-in-the-loop
> pausing, built-in retry/timeout/concurrency controls, and branch isolation
> as framework-level (not prompt-level) primitives, unified onto the same
> execution model as plain single-agent runs.

## Source Context

- **Type**: blog-post (official Google Developers Blog, first-party
  framework/SDK major-version launch announcement with inline Go code
  samples, published June 30, 2026)
- **Author credibility**: Toni Klopfenstein (Developer Relations Engineer,
  ADK Developer Relations) and Sampath Kumar Maddula (Developer Programs
  Engineer) are named Google staff, byline roles confirmed verbatim against
  the raw fetched HTML (see Extraction Notes). This is first-party vendor
  content about a Google-authored open-source library
  (`github.com/google/adk-go`), not independent practitioner analysis —
  treat feature descriptions and code samples as accurate representations of
  what shipped in 2.0, and treat ease-of-use/reliability framing as
  vendor-optimistic until independently exercised.
- **Scope**: Covers the ADK for Go 2.0 launch: the rationale for a
  graph-based workflow engine, the nine node-type taxonomy, edge/routing
  mechanics, an LLM-as-router pattern, dynamic (code-driven) orchestration,
  human-in-the-loop (HITL) semantics and durability, built-in
  retry/timeout/concurrency controls, agent modes (`Chat`/`Task`/
  `SingleTurn`), the unified node runtime, and the 1.0→2.0 migration/breaking
  changes. Also covers, via the linked migration guide
  (`README-v2.md`) and GitHub releases API, additional migration detail and
  the parallel-release timeline. Does NOT cover: benchmark numbers,
  pricing, a comparison against ADK for Python/Java/Kotlin feature parity
  beyond the one-line "if you've followed Python ADK 2.0, this will feel
  familiar" mention, or any third-party production case study using the
  graph engine (this is a feature-launch post, not a customer story).

## Extracted Claims

### Claim 1: ADK 2.0's headline feature is a graph-based workflow engine where a graph of nodes and edges is itself an `agent.Agent`, requiring no specialized harness or new server to run
- **Evidence**: First-party architectural framing plus a verbatim code
  sample constructing a two-node sequential graph (`upper` → `suffix`) via
  `workflow.Chain` and wrapping it in `workflowagent.New`.
- **Confidence**: settled (a direct, falsifiable code artifact and API
  design description of a shipped 2.0 feature; the ergonomic "no special
  harness" framing is vendor language but is corroborated by the concrete
  code sample using the same `runner`/`launcher`/`console` types Go ADK 1.0
  already used)
- **Quote**: "That wf is just an agent.Agent. It runs in the same runner,
  launcher, and console you already use — no special harness, no new
  server. A graph is an agent."
- **Our assessment**: This is the structurally significant claim in the
  post: rather than introducing a parallel "workflow runtime" alongside the
  existing single-agent runtime, ADK 2.0 makes a composed graph satisfy the
  same `agent.Agent` interface a single `LlmAgent` does. This is a stronger
  unification claim than either existing ADK note in the corpus makes —
  `blog-google-adk-kotlin-android-agents.md` and
  `blog-google-adk-a2a-contract-compliance.md` both describe multi-agent
  composition via sub-agent hierarchies (`subAgents=[...]`,
  `SequentialAgent`), which is a fixed, tree-shaped composition; this source
  generalizes that to an arbitrary graph (with cycles, fan-out/fan-in, and
  dynamic routing) while keeping the same external agent contract.

### Claim 2: Any node in a graph can pause execution and durably wait for a human response; resumption can be reconstructed purely by scanning session history, and the interrupt format is shared with Python ADK so a workflow can resume across a process restart or a different runtime
- **Evidence**: First-party description of the HITL durability mechanism,
  paired with a verbatim code sample (`workflow.NewRequestInputEvent`) and
  two named error types (`ErrInvalidResumeResponse`, `ErrNothingToResume`).
- **Confidence**: emerging (the code-level API surface for pausing and
  resuming — the event type, the error types, the schema-validation step —
  is a settled, direct description of shipped code; the durability
  *guarantee itself* ("resume after a process restart," "across different
  runtimes") is a vendor architectural claim not independently exercised in
  this extraction, so the overall claim is graded down to emerging)
- **Quote**: "And resume is durable. The run state lives in the session, and
  ADK can even reconstruct a paused workflow by scanning session history —
  so a workflow can resume after a process restart, or even across
  different runtimes, because the interrupt format is shared with Python
  ADK. Responses are validated against a schema, resume is idempotent, and
  you get clear errors (ErrInvalidResumeResponse, ErrNothingToResume) when
  something doesn't line up."
- **Our assessment**: This is the most concrete "resumability" claim in the
  corpus's ADK coverage: it names a specific recovery mechanism (rebuild
  paused state from session history, not from a separately-maintained
  workflow-engine store) and a specific cross-language compatibility
  property (Go and Python ADK share an interrupt wire format). If accurate,
  a team running a mixed Go/Python ADK deployment could pause a workflow in
  one runtime and resume it in the other — a stronger claim than typical
  single-language checkpoint/resume features.

### Claim 3: HITL resumption offers two distinct semantics — Handoff, where the human's answer flows directly to the next node, and Re-entry, where the paused node itself re-runs with the answer available via `ctx.ResumedInput(...)`
- **Evidence**: First-party enumeration of the two resume modes immediately
  following the pause/wait description.
- **Confidence**: settled (a direct, falsifiable API description — two
  named modes with distinct, described mechanics)
- **Quote**: "Handoff — the answer flows straight to the next node.
  Re-entry — the paused node re-runs with the human's response available
  via ctx.ResumedInput(...)."
- **Our assessment**: This is a specific design choice a practitioner needs
  to know before building a HITL graph: Handoff is appropriate when the
  paused node's job was only to *ask* (e.g., "should I proceed?") and a
  downstream node consumes the answer; Re-entry is appropriate when the
  paused node itself needs the answer to finish its own work (e.g., "here is
  the corrected value, now retry this computation"). Neither existing ADK
  note in the corpus (Kotlin/Android, Python/Go A2A) documents an
  HITL-resumption semantics distinction at this level of detail — this is
  new, specific implementation guidance for anyone building an approval-gate
  node.

### Claim 4: ADK 2.0 provides nine typed node constructors — function, emitting function, agent, tool, join, dynamic, workflow, parallel worker, and state-bound nodes — covering the common graph-composition cases without requiring developers to implement the `Node` interface by hand
- **Evidence**: First-party enumeration under "The building blocks," each
  node type given a one-to-two-sentence description and (for several) a
  code sample.
- **Confidence**: settled (a direct enumeration of shipped, named API types)
- **Quote**: "A node is any unit of work that implements the Node interface.
  You rarely write that interface by hand — ADK ships typed node
  constructors for the common cases." / "Join nodes are fan-in barriers:
  they wait for all predecessors and hand you a map of their outputs." /
  "State-bound nodes (NewFunctionNodeFromState) pull selected session-state
  values straight into a typed Params struct via state:\"<key>\" tags — no
  manual state plumbing."
- **Our assessment**: This taxonomy is the concrete vocabulary for the
  "graph of nodes and edges" framing in Claim 1. Two entries are especially
  notable for practitioners building coordination-pattern harnesses: join
  nodes are a named, typed fan-in-barrier primitive (rather than the
  developer writing their own `sync.WaitGroup`-equivalent aggregation
  logic), and state-bound nodes eliminate manual session-state
  read/write plumbing via struct tags — both reduce boilerplate that a
  hand-rolled orchestrator-subagent or shared-state topology (as described
  abstractly in `blog-anthropic-multi-agent-coordination-patterns.md`) would
  otherwise require a team to write themselves.

### Claim 5: Edges carry routing conditions — a node emits a routing value and matching edges fire — and this single mechanism produces every control-flow shape needed: sequential chains, conditional routers, fan-out/fan-in, nested sub-graphs, and cycles (a completed node can be re-triggered, making loops first-class)
- **Evidence**: First-party description of the edge/routing mechanism, with
  a verbatim `NewEdgeBuilder`/`AddRoutes`/`AddFanOut`/`AddFanIn` code sample
  and a named list of standard route types (`StringRoute`, `IntRoute`,
  `BoolRoute`, `MultiRoute`, `Default`).
- **Confidence**: settled (direct code artifact and enumeration from the
  source)
- **Quote**: "Sequential chains, conditional routers, fan-out/fan-in, nested
  sub-graphs, and even loops (a completed node can be re-triggered, so
  cycles are first-class) — all from edges and routes."
- **Our assessment**: Treating loops as first-class graph cycles (rather
  than a special-cased "while" construct bolted onto a otherwise-acyclic
  workflow engine) is the detail that most directly maps onto the
  "shared state" pattern's failure mode named in
  `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 5:
  reactive, token-burning loops without a convergence criterion). Because
  ADK 2.0 loops are graph cycles with the same per-node retry/timeout
  controls as any other node (see Claim 6), a developer gets a structural
  bound on loop behavior (max retries, timeout) "for free" from the graph
  primitive itself, rather than having to hand-write a separate termination
  condition as Anthropic's post recommends doing manually.

### Claim 6: Every node can carry a retry policy with exponential backoff and jitter (5 attempts, 1s initial delay, 60s cap, 2x backoff, full jitter by default), a per-node timeout, and a graph-wide concurrency cap — with no external dependency required
- **Evidence**: First-party description under "Resilience without the
  boilerplate," paired with a verbatim `workflow.NodeConfig{RetryConfig:
  workflow.DefaultRetryConfig()}` code sample and inline comment stating the
  default parameters.
- **Confidence**: settled (direct code artifact naming specific default
  values)
- **Quote**: "Every node can carry a retry policy with exponential backoff
  and jitter — no external dependency required" / "5 attempts, 1s initial
  delay, 60s cap, 2x backoff, full jitter"
- **Our assessment**: Naming the exact default retry parameters (not just
  "supports retries") is a specific, actionable detail — a team evaluating
  whether ADK's built-in retry is sufficient for a given node's failure
  profile (e.g., a flaky external API needing a longer cap than 60s) can
  compare directly against these defaults rather than reverse-engineering
  them from source. This is the first corpus ADK source to give concrete
  default retry-policy numbers rather than describing retry support only in
  the abstract.

### Claim 7: Parallel branches in a graph are isolated so that one branch's activity never leaks into another branch's LLM prompt history
- **Evidence**: First-party description in the same "Resilience without the
  boilerplate" section, immediately following the retry/timeout/concurrency
  description.
- **Confidence**: settled (a direct architectural claim about a shipped
  isolation mechanism, though "never leaks" is an absolute claim not
  independently stress-tested in this extraction)
- **Quote**: "isolate parallel branches so one branch's chatter never leaks
  into another's LLM prompt history"
- **Our assessment**: This is a concrete, framework-level instance of
  "context firewall" between concurrently-running agent branches — directly
  relevant to context-budget management in fan-out topologies, where an
  unintentionally shared prompt history across parallel branches would
  otherwise inflate every branch's context with irrelevant sibling
  conversation. It complements the `WithIsolationScope` option named for
  dynamic nodes (see Concrete Artifacts) as the same isolation guarantee
  applied to the graph's static parallel-worker/fan-out primitives, not only
  to dynamically orchestrated children.

### Claim 8: ADK 2.0 unifies single-agent execution and full-graph execution onto the same node runtime, meaning human-in-the-loop — previously implied to be workflow-only — now works for a plain `LlmAgent` too
- **Evidence**: First-party description under "Agent modes and one runtime
  to run them all."
- **Confidence**: settled (direct architectural description of a shipped
  runtime-unification change, corroborated by the "Upgrading from 1.0"
  section's breaking-change list, which requires all node/agent functions —
  not just workflow nodes — to take `agent.Context`)
- **Quote**: "Under the hood, the runner now drives a plain LlmAgent through
  the same node runtime that powers workflows. The payoff: single-agent
  apps and full graphs share one execution model, and human-in-the-loop now
  works for a plain LLM agent too — not just inside a workflow."
- **Our assessment**: This is the architectural reason the migration has
  breaking changes at all (Claim 10): unifying the runtime is what forces
  `ToolContext`/`CallbackContext` to merge into `agent.Context` for every
  caller, not just workflow authors. The payoff is that HITL — a feature
  this post frames as workflow-specific in its own HITL section — is
  actually a property of the whole runtime post-2.0, available even to a
  team that never adopts the graph/workflow engine at all.

### Claim 9: ADK 2.0 introduces three LLM agent modes — `Chat`, `Task`, and `SingleTurn` — so a coordinator can converse with the user while sub-agents quietly complete bounded tasks or run single-shot, with mode-specific helper tools installed automatically per agent role
- **Evidence**: First-party description under "Agent modes and one runtime
  to run them all," naming the three modes and three mode-specific helper
  tools (`finish_task`, `single_turn`, `task`).
- **Confidence**: settled (direct enumeration of shipped named modes and
  tools)
- **Quote**: "ADK 2.0 introduces modes for LLM agents — Chat, Task, and
  SingleTurn — so a coordinator can chat with the user while sub-agents
  quietly complete tasks or run single-shot. The right helper tools
  (finish_task, single_turn, task) are installed automatically based on
  each agent's role."
- **Our assessment**: This is a named, code-level version of the
  orchestrator/sub-agent distinction that other corpus sources describe only
  through prompting or role-naming — here the *mode itself* is a typed
  configuration on the agent, and the framework (not the developer's prompt)
  installs the matching tool set. This narrows the surface area for a
  sub-agent's tool set to drift from its intended role compared to a
  purely prompt-instructed division of labor.

### Claim 10: The 1.0→2.0 migration is "highly additive" — the entire workflow engine ships as new opt-in packages — with a small, enumerated set of mechanical breaking changes, the two largest being a node-function parameter change (`agent.InvocationContext` → `agent.Context`) and a required `context.Context` argument added to `session.NewEvent`
- **Evidence**: First-party "Upgrading from 1.0" section enumerating six
  breaking changes with before/after code for the parameter change, plus a
  link to a dedicated migration guide (`README-v2.md`), which was
  independently fetched and read in full (see Concrete Artifacts and
  Extraction Notes).
- **Confidence**: settled (a direct, itemized list of breaking changes from
  the source, corroborated by the actual migration-guide markdown fetched
  separately from the blog post)
- **Quote**: "ADK 2.0 is highly additive — the entire workflow engine is new
  packages you opt into. There are a few new and breaking changes that come
  with unifying the runtime; each has a simple, mechanical fix" / "That's
  the whole list. Public signatures for runner.Run/RunLive, agenttool, and
  the llmagent callbacks are unchanged."
- **Our assessment**: Explicitly bounding the blast radius of a major
  version bump ("that's the whole list," unchanged public signatures named)
  is unusually specific vendor reassurance — most major-version announcements
  in the corpus describe new features without this level of itemized
  migration accounting. Combined with the independently observed release
  timeline (Claim 13), this is a well-substantiated "low-friction major
  version" claim, not just marketing language.

### Claim 11: `session.NewEvent`'s new required `context.Context` parameter exists specifically so that time and UUID providers installed on the context can make workflow-engine events "deterministic, replay-safe" — not merely to pass context through for its own sake
- **Evidence**: Direct text from the dedicated migration guide
  (`README-v2.md`), fetched and read as raw markdown independently of the
  blog post (see Extraction Notes).
- **Confidence**: settled (verbatim primary-source migration documentation,
  not a summarized/paraphrased version)
- **Quote**: "The event ID and timestamp are now obtained through the
  platform package, so a time or UUID provider installed on ctx (see
  platform.WithTimeProvider and platform.WithUUIDProvider) controls them.
  This lets callers such as workflow engines produce deterministic,
  replay-safe events."
- **Our assessment**: This is the rationale the blog post itself omits (the
  post states the signature change but not *why*): making event
  ID/timestamp generation swappable via the context is what allows a
  workflow engine to replay recorded events deterministically for testing
  or for the paused-workflow reconstruction described in Claim 2 — without
  this, replayed events would get new, non-matching IDs/timestamps every
  run. This is a concrete instance of "context-boundary configuration
  injection" (a time/randomness provider threaded through `context.Context`)
  applied specifically to make agent event logs reproducible.

### Claim 12: The recommended fix for the `ToolContext`/`CallbackContext` merge in existing tests is not to patch each missing mock method reactively, but to embed `agent.StrictContextMock` and override only what a test needs — unoverridden methods panic with "not implemented" rather than silently returning a zero value
- **Evidence**: Direct text and code sample from the migration guide
  (`README-v2.md`), contrasting the reactive per-method patch against the
  recommended `StrictContextMock` embedding approach.
- **Confidence**: settled (verbatim primary-source migration documentation)
- **Quote**: "Adding each missing method by hand is reactive: every time the
  context surface grows, your mocks break again and you have to patch them.
  Instead, you can embed agent.StrictContextMock in your test fake and
  override only the methods your test actually uses... Un-overridden
  methods panic with \"not implemented\", so an unexpected call fails the
  test loudly instead of silently returning a zero value."
- **Our assessment**: This is a specific, transferable test-design
  principle beyond ADK itself: a strict mock that panics on any
  unoverridden call surfaces test gaps immediately (a test exercising an
  untested code path fails loudly) instead of the common mocking failure
  mode where an unoverridden method silently returns a zero value and the
  test passes despite exercising unintended behavior. This is a "fail loud,
  not quiet" mocking philosophy worth citing anywhere the guide discusses
  test-double design for agent harnesses.

### Claim 13: Google continued shipping a 1.x release (v1.5.0, June 1 2026) one day after ADK for Go v2.0.0 shipped (June 30, 2026), rather than cutting the 1.x line off immediately at the 2.0 launch
- **Evidence**: Independently observed via the GitHub Releases API for
  `google/adk-go` (not stated in the blog post itself) — `v2.0.0` published
  2026-06-30T14:24:36Z, `v1.5.0` published 2026-07-01T09:40:04Z.
- **Confidence**: settled (directly observed, timestamped repository release
  data, not an inference)
- **Quote**: (no direct quote; a release-timeline observation from
  `api.github.com/repos/google/adk-go/releases`, not blog-post prose — see
  Concrete Artifacts)
- **Our assessment**: This is a follow-up-page finding, not from the blog
  post text. It corroborates Claim 10's "highly additive, low-friction
  migration" framing with independent evidence: Google did not force an
  immediate hard cutover of the 1.x line at the moment 2.0 shipped, giving
  teams that are not ready for the (small) breaking-change list in Claim 10
  at least one more 1.x patch to land on. This is a small but concrete
  signal about how conservatively Google staged this major-version rollout
  in practice, beyond what the announcement post itself claims.

## Concrete Artifacts

### Minimal sequential graph (verbatim from source)
```go
import "google.golang.org/adk/v2/workflow"

upper  := workflow.NewFunctionNode("upper",  upperFn,  cfg)
suffix := workflow.NewFunctionNode("suffix", suffixFn, cfg)

edges := workflow.Chain(workflow.Start, upper, suffix)

wf, _ := workflowagent.New(workflowagent.Config{
    Name:  "simple_sequence_workflow",
    Edges: edges,
})
```
Source: developers.googleblog.com, "ADK for Go 2.0: build agent workflows
as a graph" (2026-06-30).

### Edge builder — routing, fan-out, fan-in (verbatim from source)
```go
b := workflow.NewEdgeBuilder()
b.AddRoutes(router, map[string]workflow.Node{
    "question":    answerNode,
    "statement":   commentNode,
    "exclamation": reactNode,
})
b.AddFanOut(planner, researchA, researchB, researchC) // parallel branches
b.AddFanIn(join, researchA, researchB, researchC)       // gather results
```
Source: same post, "Edges, routing, and the shapes you need."

### Human-in-the-loop request/pause (verbatim from source)
```go
event := workflow.NewRequestInputEvent(ctx, session.RequestInput{
    InterruptID:    "approve_refund",
    Message:        "Approve a $200 refund? (yes/no)",
    ResponseSchema: schema,
})
// yield the event; the node moves to "waiting"
```
Source: same post, "Human-in-the-loop, built in."

### Retry/backoff default config (verbatim from source)
```go
cfg := workflow.NodeConfig{ RetryConfig: workflow.DefaultRetryConfig() }
// 5 attempts, 1s initial delay, 60s cap, 2x backoff, full jitter
```
Source: same post, "Resilience without the boilerplate."

### 1.0 → 2.0 breaking-change list (verbatim summary from source)
```
1. Node/node-function signatures: agent.InvocationContext -> agent.Context
2. Unified context: ToolContext, CallbackContext removed; agent.Context only
3. Custom InvocationContext impls need IsolationScope() and ResumedInput(id string)
4. Event streams gain node fields (IsolationScope, Output, Routes,
   RequestedInput) and a NodeInfo metadata field
5. llmagent.New may install mode-specific tools; task-mode agents can't be
   static graph nodes
6. session.NewEvent(ctx context.Context, invocationID string) - context now required
```
Source: same post, "Upgrading from 1.0." Public signatures for
`runner.Run/RunLive`, `agenttool`, and llmagent callbacks are stated as
unchanged.

### `session.NewEvent` migration (verbatim from README-v2.md, fetched
directly from `raw.githubusercontent.com/google/adk-go/main/README-v2.md`,
independent of the blog post's WebFetch summary)
```go
// Before
ev := session.NewEvent(ctx.InvocationID())
// or
ev := session.NewEventWithContext(ctx, ctx.InvocationID())

// After
ev := session.NewEvent(ctx, ctx.InvocationID())
```
Source: `github.com/google/adk-go` `README-v2.md`, "Breaking changes" ->
"`session.NewEvent` now requires a `context.Context`."

### `StrictContextMock` test-double pattern (verbatim from README-v2.md)
```go
// Embed StrictContextMock and override only what the test needs.
type fakeContext struct {
	agent.StrictContextMock
}

var _ agent.Context = (*fakeContext)(nil)

func TestSomething(t *testing.T) {
	cc := &fakeContext{agent.StrictContextMock{Ctx: context.Background()}}
	// Override methods as needed, e.g. by adding them on fakeContext.
	// ...
}
```
Source: `github.com/google/adk-go` `README-v2.md`, "Mocks update required
for unified contexts" -> "Alternative: embed `agent.StrictContextMock`."

### Release timeline (independently queried, `api.github.com/repos/google/adk-go/releases`)
```
v2.0.0   2026-06-30T14:24:36Z
v1.5.0   2026-07-01T09:40:04Z   <- shipped one day AFTER v2.0.0
v1.4.0   2026-05-29T13:45:25Z
v1.3.0   2026-05-19T12:49:31Z
v1.2.0   2026-04-23T19:13:09Z
v1.1.0   2026-04-10T15:08:03Z
v1.0.0   2026-03-23T09:38:41Z
```
Source: GitHub Releases API for `google/adk-go`, queried 2026-07-10 (not
from the blog post).

### Runnable example directory listing (confirmed via GitHub Contents API,
`api.github.com/repos/google/adk-go/contents/examples/workflow`)
```
examples/workflow/
  basic/
  complex/
  dynamic/
  hitl_rerun/
  hitl_simple/
  routing/
```
Source: `google/adk-go` GitHub repository, queried 2026-07-10 — confirms the
`go run ./examples/workflow/...` paths named in the post's "Try it" section
resolve to real directories (the post itself additionally names
`dynamic/hitl/`, a subpath not independently verified at directory-listing
depth in this extraction).

## Cross-References

- **Corroborates**:
  - `blog-google-adk-a2a-contract-compliance.md` (Claim 9, `SequentialAgent`
    Coordinator chaining three sub-agents in a fixed sequence): this
    source's `workflow.Chain(workflow.Start, upper, suffix)` (Claim 1) is
    the Go-native, graph-primitive version of the same fixed-sequence
    composition idea — the A2A note's Python `SequentialAgent` is one
    specific, degenerate case (a linear chain with no branching or cycles)
    of the more general graph model this source describes.
  - `blog-google-adk-kotlin-android-agents.md` (Claim 5,
    `disallowTransferToPeers`/`disallowTransferToParent` as structural,
    code-level multi-agent topology locks rather than prompted instructions):
    this source's branch isolation (Claim 7) and `WithIsolationScope` option
    are the same "structural control, not prompted control" design
    philosophy applied to a different axis — preventing context/history
    leakage between concurrent branches rather than preventing control-flow
    escalation between parent/child/peer agents. Both sources independently
    show Google's ADK family encoding multi-agent guardrails as typed API
    surface rather than prompt text.
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 5, "shared
    state requires first-class termination conditions... at minimum: a time
    budget, a convergence threshold, or a designated judge agent"): this
    source's graph cycles with per-node retry/timeout bounds (Claims 5, 6)
    are a structurally different but complementary termination mechanism —
    a bounded retry count and timeout cap applied to a first-class loop
    primitive, rather than a time budget, convergence threshold, or judge
    agent applied to a free-form shared-state topology. Similar to
    `blog-google-adk-a2a-contract-compliance.md`'s ComplianceStep enum
    (a fourth termination mechanism already noted in that source's
    Cross-References), this is a fifth, framework-enforced variant: retry
    count and timeout as the graph engine's own convergence guard.

- **Contradicts**: None filed. See Extraction Notes for a considered,
  non-filed contrast against
  `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 2).

- **Extends**:
  - `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 2, "dynamic
    workflows dynamically write orchestration scripts — Claude itself
    generates the coordination logic, not the user"): this source's
    "dynamic orchestration in plain Go" (dynamic nodes, `RunNode(...)`,
    Concrete Artifacts) is a related but distinctly *narrower* capability —
    the graph *shape* in ADK Go 2.0 is still authored by the developer ahead
    of time; only a dynamic node's *internal* child-invocation order is
    determined at runtime by ordinary Go code (loop counts, accumulation,
    fan-out over a runtime-sized list). Anthropic's dynamic workflows, by
    contrast, have the model itself write the orchestration script — a
    qualitatively more autonomous authoring model. This is a genuine
    taxonomy distinction ("who authors the orchestration topology: a
    developer ahead-of-time with a bounded dynamic-node escape hatch, vs. a
    model at runtime") rather than a factual disagreement between the two
    sources, so no contradiction issue was filed per MINER.md §4a's "differ
    only in context" guidance — these are two different products solving
    related but distinct problems (a typed application framework vs. an
    interactive coding-agent feature).
  - `blog-anthropic-dynamic-workflows-claude-code.md` (Claim 3, built-in
    "verification-before-return" as a platform primitive) and
    (Claim 7, automatic progress-saving for resumable long-running jobs):
    this source's durable HITL resumption (Claims 2, 3) is a concrete,
    code-level realization of "automatic progress saving" for a different
    product surface (a Go application framework vs. an interactive coding
    agent) — both name durable resume-after-interruption as a first-class
    property, but this source specifies the actual mechanism (session
    history reconstruction, schema-validated idempotent resume, named error
    types) where the Anthropic post names the property without mechanism
    detail.
  - `guide/04-context-engineering.md`'s "Restart Recovery Pattern" section
    (~lines 563-660, sourced from Claude Code-specific handoff-file and
    session-JSONL patterns): this source's durable, cross-runtime workflow
    resumption (Claim 2) is a framework-level analog for a different kind of
    application (a Go multi-agent service, not an interactive coding
    session) — instead of a developer-authored handoff file, ADK
    reconstructs paused state from the session's own event history.

- **Novel**:
  - **A typed, nine-node graph-composition taxonomy with first-class cycles
    and fan-in barriers** (Claims 1, 4, 5): no prior corpus ADK source
    (Kotlin/Android, Python/Go A2A) describes multi-agent composition as an
    arbitrary node/edge graph with named join, dynamic, and state-bound
    node types — prior sources describe tree-shaped sub-agent hierarchies
    or fixed sequential chains only.
  - **Cross-language (Go/Python), cross-restart durable HITL resumption via
    a shared interrupt wire format** (Claim 2): no prior corpus source
    describes a multi-agent framework whose paused-workflow state can be
    reconstructed purely from session history and resumed in a different
    language runtime than the one that paused it.
  - **Named default retry-policy parameters as a graph-engine primitive**
    (Claim 6: 5 attempts, 1s initial delay, 60s cap, 2x backoff, full
    jitter): no prior corpus ADK source gives concrete numeric retry
    defaults; prior sources mention retry/resilience only in the abstract.
  - **A "fail loud, not quiet" strict-mock test-double pattern**
    (Claim 12): novel to the corpus as a named testing philosophy —
    panicking on unoverridden mock methods rather than returning a silent
    zero value.
  - **Independent evidence of a conservative, staggered major-version
    rollout** (Claim 13): the one-day-later 1.x patch release after the 2.0
    launch is a small but concrete, independently-observed data point about
    migration risk management that is not stated in the announcement post
    itself.

## Guide Impact

- **Chapter 02 (Harness Engineering), "Multi-Agent Coordination Patterns"**
  (`guide/02-harness-engineering.md`, ~lines 1261-1349, currently sourced
  entirely from `blog-anthropic-multi-agent-coordination-patterns` as an
  abstract five-pattern taxonomy): add this source's graph model as a
  worked example of a shipped framework where several of those five
  patterns collapse into configurations of one primitive — a sequential
  chain (Claim 1) is orchestrator-subagent's simplest case; `AddFanOut`/
  `AddFanIn` (Claim 5) is orchestrator-subagent's parallel-dispatch
  variant; a graph cycle with bounded retry/timeout (Claims 5, 6) is a
  structurally-bounded version of the shared-state pattern's "reactive
  loop" failure mode, addressed with a framework-level guard (retry count,
  timeout cap) rather than a manually-designed termination condition. Also
  add the "isolate parallel branches" primitive (Claim 7) next to the
  orchestrator-subagent "information bottleneck" failure-mode guard text —
  this is a concrete framework mechanism for the context-isolation half of
  that guard, complementing (not replacing) the cross-cutting-propagation
  design work the guard also calls for.

- **Chapter 04 (Context Engineering), "Restart Recovery Pattern"**
  (~lines 563-660) and **"Sub-agents as parallel context firewalls"**
  (~lines 989-1012): cite this source's durable HITL resumption (Claim 2)
  as a framework-level contrast to the guide's current CLAUDE.md/handoff-file
  recovery pattern — ADK reconstructs paused-workflow state from session
  event history rather than from an agent-authored handoff artifact, and
  the interrupt format is shared across languages. Cite Claim 7 (branch
  isolation, "one branch's chatter never leaks into another's LLM prompt
  history") as a concrete, framework-enforced instance of the "context
  firewall" principle applied specifically to concurrently-running parallel
  branches, complementing the sub-agent-as-firewall framing already in that
  section.

- **Chapter 06 (Security Threat Model), "Gradual trust rollout: shadow →
  inform → gate"** (~lines 166-206, currently sourced from
  `blog-cursor-security-agents` and framed around a CI/PR merge-gate
  mechanism with no described runtime architecture): add this source's
  HITL pause/resume primitive (Claims 2, 3) as one concrete architecture for
  implementing a "gate" stage inside an agent's own execution — a node
  pauses and durably waits for approval (Handoff or Re-entry semantics)
  rather than the gate being enforced externally by CI. This is a
  complementary mechanism, not a replacement: Cursor's gate blocks a merge
  event; ADK's gate blocks a node's own execution mid-workflow.

## Extraction Notes

- Read the full post via two extraction methods: (1) the WebFetch tool's
  small-model summarizer for an initial overview pass, and (2) a direct
  `curl` fetch of the raw HTML, stripped to plain text with a Python regex
  script, used to independently verify every `Quote` field above
  character-for-character. This was necessary: several phrases the
  summarizer reported (e.g., "A graph functions as an agent," "reconstruct
  paused workflows," "largely additive," "durably waits") did **not** match
  the raw HTML text verbatim (the actual wording is "A graph is an agent,"
  "reconstruct a paused workflow," "highly additive," "the workflow durably
  waits for the answer" / "resume is durable") — those paraphrased
  summarizer versions were discarded and only the raw-fetched text was used
  for every `Quote` field in this note.
- Followed two linked pages beyond the blog post itself, per MINER.md §1:
  (1) `github.com/google/adk-go/blob/main/README-v2.md`, fetched as raw
  markdown via `raw.githubusercontent.com` (not just WebFetch's summarizer)
  specifically to verify the migration-guide quotes in Claims 10-12
  character-for-character — this is the source for Claims 11 and 12, which
  are not covered in the blog post's own text at that level of detail; and
  (2) the GitHub Releases and Contents APIs for `google/adk-go`
  (`api.github.com/repos/google/adk-go/releases` and
  `.../contents/examples/workflow`), which is the source for Claim 13 (the
  1.5.0-after-2.0.0 release timeline) and the example-directory
  confirmation in Concrete Artifacts. Did not follow the `pkg.go.dev`
  API-reference links (`Node interface`, `Route interface`) or the
  `examples/workflow/routing/llm/` GitHub subpath beyond confirming the
  parent `examples/workflow/` directory exists — a deeper extraction of the
  actual Go source in those example directories is a candidate for a
  future, separate mining pass if the repository's code itself becomes
  independently notable.
- Considered filing a contradiction issue per MINER.md §4a between this
  source's "dynamic orchestration in plain Go" (dynamic nodes) and
  `blog-anthropic-dynamic-workflows-claude-code.md`'s "dynamically writes
  orchestration scripts" claim, since both use "dynamic" for
  runtime-determined orchestration. Concluded this is not a contradiction:
  the two sources describe different authorship models (developer-authored
  graph shape with a bounded runtime escape hatch, vs. model-authored
  orchestration scripts) for different products (a typed Go application
  framework vs. an interactive coding-agent feature), which is a scope/
  definitional difference, not opposing claims about the same mechanism —
  see Cross-References → Extends for the full reasoning. No contradiction
  issue filed.
- Confidence graded `settled` overall: the large majority of claims (1,
  3-13) are direct, falsifiable code artifacts, named API surfaces, or
  independently-verified primary-source text (the blog post's raw HTML and
  the separately-fetched `README-v2.md`), not vendor framing requiring
  independent benchmarking. Claim 2's durability *guarantee* (as opposed to
  its API surface) is the one claim graded `emerging` rather than `settled`
  within this note, since "resume after a process restart" and "across
  different runtimes" were not independently exercised in this extraction —
  see that claim's own confidence rationale.
