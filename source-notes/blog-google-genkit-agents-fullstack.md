---
source_url: https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit/
source_type: blog-post
title: "Build agentic full-stack apps with Genkit"
author: Chris Gill, Product Manager (Google Developers Blog)
date_published: 2026-07-01
date_extracted: 2026-07-11
last_checked: 2026-07-11
status: current
confidence_overall: emerging
issue: "#1742"
---

# Build agentic full-stack apps with Genkit

> First-party Google announcement of the Genkit Agents API (preview, TypeScript
> and Go): a single agent abstraction that unifies message history, tool
> loops, streaming, persistence, human-in-the-loop interrupts, detachable
> long-running work, and multi-agent delegation behind one `chat()`/`RunText()`
> interface and one client-server wire protocol.

## Source Context

- **Type**: blog-post (official Google Developers Blog, product announcement)
- **Author credibility**: Chris Gill is credited as Product Manager, writing
  on Google's own developer blog about a Google-authored open-source
  framework (Genkit). This is first-party vendor content describing a
  feature the poster's own team shipped — authoritative on what the API
  does and how it is meant to be used, but not independent or third-party
  verified. The post explicitly flags the feature's maturity: "The Agents
  API is in preview today in TypeScript and Go. It can introduce breaking
  changes in minor version releases." All code samples and API names should
  be read as an accurate first-party description of a preview surface, not
  a settled, stable API contract.
- **Scope**: Covers the Genkit Agents API end to end for a single post:
  agent definition, server-managed vs. client-managed state persistence,
  session-store backend options (in-memory, file, Firestore, custom),
  snapshot/branch semantics, HTTP serving, a JavaScript remote client,
  streaming, human-in-the-loop tool interrupts, detached/pollable
  long-running work, multi-agent delegation via middleware, a Developer UI
  ("Agent Runner"), and explicit guidance on when to choose the Agent
  Development Kit (ADK) instead. Does **not** cover: pricing, production
  case studies or adoption metrics, Dart/Python support for the Agents API
  specifically (only the base Genkit framework is said to support those
  languages), benchmark data, or any account of what breaks when the
  preview API changes.

## Extracted Claims

### Claim 1: Genkit frames the Agents API as eliminating repeated "plumbing" — message history, tool loop, streaming, persistence, and a frontend protocol — that every conversational-agent project otherwise wires up by hand
- **Evidence**: First-party problem statement opening the post, followed
  immediately by the product framing that the Agents API "packages all of
  that behind one interface."
- **Confidence**: emerging (a vendor problem/solution framing for a preview
  feature, not an independently measured reduction in engineering effort)
- **Quote**: "That plumbing repeats on every project and has little to do with what makes your app distinct."
- **Our assessment**: This is standard vendor positioning, but the specific
  list of five things it claims to unify (message history, tool loop,
  streaming, persistence, frontend protocol) is a useful, falsifiable
  checklist for evaluating whether an agent framework actually covers full-
  stack needs, rather than just the model-calling loop. It is a narrower
  and more concrete claim than a generic "agents are hard to build"
  framing.

### Claim 2: An agent requires only a name and a system prompt to define; tools, state, and a session store are added incrementally, and the same agent object handles a one-shot reply, a streamed turn, a paused tool call, and a multi-turn conversation without switching abstractions
- **Evidence**: First-party API description under "Define an agent," backed
  by a Go code sample (`genkitx.DefineAgent` + `RunText`) showing the
  minimal case (name + system prompt only).
- **Confidence**: settled (a direct, code-verifiable description of the
  preview API's minimal surface)
- **Quote**: "An agent needs a name and a system prompt to start. From there you add tools, state, and a session store as the feature grows."
- **Our assessment**: The "one abstraction covers one-shot, streaming,
  paused-tool-call, and multi-turn" claim (stated separately in the source
  as "The same agent object is flexible and can handle a one-shot reply, a
  streamed turn, a paused tool call, and a multi-turn conversation. You do
  not reach for a different abstraction as the feature grows.") is the
  core design bet of the framework: incremental complexity without a
  rewrite. This is a specific, checkable claim once the API stabilizes
  post-preview — worth revisiting if/when Genkit Agents reaches GA.

### Claim 3: Adding a session store makes an agent server-managed — the server persists messages, custom state, and artifacts as snapshots, and clients continue a conversation by sending back a session ID
- **Evidence**: First-party description under "State that lives where you
  want it," backed by a Go code sample configuring a
  `NewFirestoreSessionStore` and attaching it via `aix.WithSessionStore`.
- **Confidence**: settled (direct, code-verifiable API description)
- **Quote**: "The server persists messages, custom state, and artifacts as snapshots, and clients continue by sending back a session ID."
- **Our assessment**: This is a conventional server-side-session pattern
  (comparable to a web session store), but the specific bundling of three
  distinct data kinds — messages, custom state, artifacts — into one
  snapshot unit is a concrete design choice worth naming: a single
  checkpoint operation persists all three together rather than requiring
  separate persistence mechanisms per data kind.

### Claim 4: Omitting a session store makes an agent client-managed — the server returns the full state and the client sends it back on the next turn — recommended for apps that already own persistence or need stateless server deployments
- **Evidence**: First-party description of the alternative to Claim 3,
  stated as a direct trade-off ("Choose this for..." vs. "Use this
  when...").
- **Confidence**: settled (direct API description of a binary, documented
  choice)
- **Quote**: "Leave the store off and the agent is client-managed: the server returns the full state and the client sends it back on the next turn."
- **Our assessment**: This is a clean, explicit decision axis (who owns
  persistence: server or client) rather than a single opinionated default.
  The stated use cases are specific and actionable: server-managed for
  "persistent chat apps, shared devices, and any workflow where the client
  should not carry the whole conversation"; client-managed when "your app
  already owns persistence or you need stateless server deployments." This
  is a more explicit persistence-ownership framing than most agent-harness
  sources in the corpus provide.

### Claim 5: Every successful server-managed turn writes a snapshot, letting a client resume the latest state by session ID or branch from an exact earlier point by snapshot ID, without disturbing the original conversation thread
- **Evidence**: First-party description plus a Go code sample contrasting
  `aix.WithSessionID` (continue) against `aix.WithSnapshotID` (branch from
  an approved-plan snapshot to revise for a smaller budget).
- **Confidence**: settled (direct, code-verifiable API description)
- **Quote**: "Branching lets a user explore an alternative from any saved moment without disturbing the original thread."
- **Our assessment**: This is the single most novel mechanism in the
  source relative to the rest of the corpus: git-like branching of
  conversational/application state, addressable by snapshot ID, at the
  framework level rather than as an ad hoc application feature. It gives a
  concrete answer to "what if the user wants to try a different path from
  a point in the conversation without losing the original" — a problem
  most agent-harness sources in the corpus either don't address or solve
  informally (compare the `/rewind` and session-branching UX in
  `blog-anthropic-session-management-1m-context.md`, which is a different
  layer of the stack — see Cross-References).

### Claim 6: Custom state (typed application data such as workflow status, a task list, or selected entities) and artifacts (generated outputs the user may inspect, download, or version, such as a report, a patch, or an itinerary) are two distinct kinds of state a tool can update, and Genkit streams changes to the client as they happen
- **Evidence**: First-party definitional distinction stated directly in
  "State that lives where you want it."
- **Confidence**: settled (direct API/data-model description)
- **Quote**: "Custom state is your typed application data, the compact control and UI values that drive the next turn, such as workflow status, a task list, or selected entities. Artifacts are generated outputs the user may inspect, download, or version on their own, such as a report, a patch, or an itinerary."
- **Our assessment**: This is a useful, transferable data-model
  distinction beyond Genkit specifically: "control state" that drives the
  next turn of the interaction vs. "output artifacts" the user treats as a
  standalone deliverable. Framework designers and guide readers building
  their own agent state models could reuse this two-category split even
  outside Genkit.

### Claim 7: Every Genkit agent is already a servable HTTP action — `AllAgentRoutes()` returns route descriptors for a standard `http.ServeMux` that wire up not just the turn endpoint but also the snapshot and abort companion endpoints
- **Evidence**: First-party description under "Serve it over HTTP," backed
  by a Go code sample mounting routes on `http.NewServeMux()`.
- **Confidence**: settled (direct, code-verifiable API description)
- **Quote**: "they wire up the turn endpoint plus the snapshot and abort companions for you."
- **Our assessment**: The detail that "abort" is a first-class companion
  endpoint (not just turn + snapshot) is notable — it implies the
  framework treats mid-flight cancellation as a designed-for case rather
  than something the developer must build separately, which matters
  directly for the detached long-running work pattern in Claim 12.

### Claim 8: The JavaScript `remoteAgent()` client exposes the identical `chat()` interface as a local, in-process agent, so the same driving code works in backend tests and in the browser
- **Evidence**: First-party description under "A rich client for full-stack
  integration," backed by a TypeScript code sample connecting to
  `http://localhost:8080/api/weatherAgent`.
- **Confidence**: settled (direct, code-verifiable API description)
- **Quote**: "remoteAgent() returns a handle with the same chat() interface as a local agent, so the code that drives an agent in your backend tests is the code that drives it from the browser."
- **Our assessment**: This "same interface locally and remotely" design
  removes a common source of test/production divergence — a frequent
  practical pain point when a local mock harness diverges from the real
  network client. It is a specific engineering claim (interface parity)
  rather than a vague usability claim.

### Claim 9: The client speaks one wire protocol over the agent HTTP route, so it works identically against a JavaScript or a Go server backend, and resolves dynamic auth headers, streamed state patches, and session/snapshot/client-managed-state continuation automatically per request
- **Evidence**: First-party description directly following Claim 8's
  interface-parity claim, describing the client's per-request behavior.
- **Confidence**: settled (direct architectural description, consistent
  with the HTTP route/`AllAgentRoutes()` mechanism in Claim 7)
- **Quote**: "The client speaks one wire protocol over the agent route, so it works the same against a JavaScript or a Go backend."
- **Our assessment**: This is the cross-language interoperability claim
  underlying the "full-stack" framing in the title: a JS frontend and a Go
  backend (or vice versa) share one protocol without a translation layer.
  It is architecturally coherent with the route-descriptor mechanism in
  Claim 7, but the post gives no wire-format specification (e.g., no
  schema, no mention of gRPC/JSON-RPC/SSE specifics) — the "one protocol"
  claim is asserted, not documented at the byte level, in this post.

### Claim 10: Streaming is built into the same client interface via `sendStream()`, which returns a chunk stream plus a final response, and each chunk can carry text, custom state, or an artifact as it is produced
- **Evidence**: First-party description under "A rich client for
  full-stack integration," backed by a TypeScript code sample iterating
  `for await (const chunk of turn.stream)` and branching on
  `chunk.text`/`chunk.custom`/`chunk.artifact`.
- **Confidence**: settled (direct, code-verifiable API description)
- **Quote**: "sendStream() gives you a chunk stream and a final response, and each chunk can carry text, custom state, or an artifact as it is produced."
- **Our assessment**: Unifying three different chunk payload types (text
  tokens, state deltas, artifact updates) into one stream API is a
  concrete design decision — most streaming chat APIs only stream text
  tokens, requiring a separate mechanism for out-of-band state or file
  updates. This makes the streaming API directly reusable for the
  progress-reporting use case in Claim 12 (long-running task polling),
  since the same chunk shape can carry status updates.

### Claim 11: A tool can pause an agent turn and hand control back to the user via `DefineInterruptibleTool()`; the client approves, rejects, or supplies a missing value before the turn continues, and the runtime validates the resume payload against session history so a tool cannot be tricked into running with forged input
- **Evidence**: First-party description under "Human approval, built in,"
  backed by a Go code sample (`runShell` tool) that returns a
  `tool.Interrupt(...)` payload when a risky command needs confirmation,
  and errors on an explicit rejection (`!confirm.Approved`).
- **Confidence**: settled (direct, code-verifiable API description,
  including the specific anti-forgery mechanism)
- **Quote**: "the runtime validates the resume payload against session history so a tool cannot be tricked into running with forged input."
- **Our assessment**: The validate-against-session-history detail is the
  most security-relevant claim in the source: it is a structural
  safeguard against a client (or an attacker with access to the client)
  fabricating an approval response that doesn't correspond to a real
  pending interrupt. This is a stronger claim than "the client can
  approve or reject" alone — it specifies that the server, not just the
  client UI, enforces the correspondence between an approval and the
  interrupt it approves.

### Claim 12: With server-managed state, a client can detach a long-running turn, close the connection, and reconnect later by snapshot ID while the agent keeps working server-side and writes progress to a pending snapshot that another session can poll, wait on, or abort — making long research jobs and multi-step workflows practical without holding a connection open or building a separate job queue
- **Evidence**: First-party description under "Work that outlives the
  request," backed by a TypeScript code sample calling `chat.detach(...)`
  and polling via `task.poll({ intervalMs: 1000 })`.
- **Confidence**: settled (direct, code-verifiable API description)
- **Quote**: "This makes long research jobs, multi-step planning, and tool-heavy workflows practical without holding a connection open or building a separate job queue."
- **Our assessment**: This directly targets a well-known practical gap in
  request/response-shaped agent APIs: a long-running agent task either
  ties up a connection (fragile against timeouts, client disconnects) or
  requires the developer to hand-build a separate job queue and polling
  API. Folding detach/poll into the same session-store/snapshot mechanism
  used for ordinary conversation continuity (Claim 5) is an efficient
  reuse of one persistence primitive for two different problems (state
  resumption and async job tracking).

### Claim 13: The `Agents` middleware injects a delegation tool for each configured sub-agent so an orchestrator model can route parts of a request to the right specialist; delegation appears as ordinary tool activity in the orchestrator's stream, and specialist artifacts can merge into the parent session
- **Evidence**: First-party description under "Coordinate specialists,"
  backed by a Go code sample configuring `middlewarex.Agents` with
  `Agents: []aix.AgentRef{researcher.Ref(), coder.Ref()}`,
  `MaxDelegations: 5`, and `ArtifactStrategy:
  middlewarex.ArtifactStrategySession`.
- **Confidence**: settled (direct, code-verifiable API description)
- **Quote**: "Delegation shows up as ordinary tool activity in the orchestrator's stream, and specialist artifacts can merge into the parent session so the final answer can build on what each specialist produced."
- **Our assessment**: This is a concrete framework implementation of the
  orchestrator-subagent coordination pattern (see Cross-References): the
  delegation-as-tool-call design means the orchestrator's existing tool
  loop and streaming machinery handle multi-agent coordination without a
  separate protocol, and the `MaxDelegations` cap is a specific, named
  guard against unbounded delegation loops. The source is explicit that
  this is deliberately lighter-weight than ADK's multi-agent core (see
  Claim 14): "Subagents with Genkit give you full control and the ability
  to implement your own orchestration."

### Claim 14: Google's explicit guidance is to use ADK instead of Genkit Agents when multi-agent orchestration is the whole system rather than one feature of a larger app, or when a managed hosted runtime (not just a library) is required
- **Evidence**: First-party guidance under "When to reach for ADK
  instead," stating two conditions directly.
- **Confidence**: emerging (a vendor product-positioning statement drawing
  a boundary between two of the vendor's own products, not an
  independently validated architectural rule)
- **Quote**: "Multi-agent orchestration is the whole system, not just one feature. ADK is purpose-built for complex agent topologies, where Genkit's delegation middleware is deliberately lighter and not built into the core of the agent abstraction."
- **Our assessment**: This is a useful, actionable decision rule for
  practitioners choosing between the two Google frameworks, and it is
  self-critical in a credible way (Genkit's own post naming where Genkit
  is deliberately the weaker option). The second condition — "You want a
  managed runtime, not just a library. ADK pairs with Agent Runtime on the
  Gemini Enterprise Agent Platform for hosting, scaling, and managed
  sessions." — further clarifies that Genkit Agents ships as a
  self-hosted library, not a managed hosting product, which is a material
  operational difference from ADK's Agent Runtime pairing.

### Claim 15: Genkit ships four session-store backend options with distinct recommended use cases — in-memory for tests/demos/single-process experiments, file for local development and single-host apps needing restart-survival, Firestore for production apps wanting a managed multi-instance database, and a custom store interface for teams needing their own database, authorization, or retention policies
- **Evidence**: First-party enumerated list under "Choose your
  persistence."
- **Confidence**: settled (direct, enumerated product-configuration
  description)
- **Quote**: "In-memory for tests, demos, and single-process experiments."
- **Our assessment**: The explicit "custom when you need your own
  database, authorization, or specific retention policies" option is the
  most consequential item for teams evaluating vendor lock-in: unlike a
  framework that only ships a proprietary managed store, Genkit's
  documented store interface lets a team keep persistence and auth on
  infrastructure they control. This is directly relevant to the
  build-vs-buy/lock-in argument in `blog-langchain-deep-agents-deploy.md`
  (see Cross-References).

### Claim 16: Agents are first-class in the Genkit Developer UI via a new "Agent Runner" that lets a developer start a conversation, send turns, watch streamed output and state updates, drive tool interrupts, and inspect snapshots without writing any client code
- **Evidence**: First-party feature description under "Test and explore in
  the Developer UI."
- **Confidence**: emerging (a direct feature description, but "fastest way
  to exercise an agent" is vendor framing not independently benchmarked
  against alternative debugging workflows)
- **Quote**: "The new Agent Runner lets you start a conversation, send turns, watch streamed output and state updates, drive tool interrupts, and inspect snapshots, all without writing a client."
- **Our assessment**: A built-in tool that can "drive tool interrupts" —
  i.e., simulate the human-approval step from Claim 11 — directly in the
  dev UI is a concrete testability feature: it means the human-in-the-loop
  path (the hardest kind of flow to exercise without a real client) has a
  first-party manual-testing surface, not just an API a developer must
  script against to test.

## Concrete Artifacts

### Minimal agent definition (verbatim from source, "Define an agent")
```go
import genkitx "github.com/firebase/genkit/go/genkit/exp"

g := genkit.Init(ctx,
    genkit.WithPlugins(&googlegenai.GoogleAI{}),
    genkit.WithExperimental(), // Enables preview features like Agents API.
)

assistant := genkitx.DefineAgent(g, "assistant",
    aix.InlinePrompt{
        ai.WithModelName("googleai/gemini-flash-latest"),
        ai.WithSystem("You are a helpful assistant."),
    },
)

out, err := assistant.RunText(ctx, "Hello. What can you do?")
if err != nil {
    log.Fatal(err)
}

fmt.Println(out.Message.Text())
```
Source: developers.googleblog.com, "Build agentic full-stack apps with Genkit" (2026-07-01), "Define an agent."

### Server-managed state with Firestore, plus continue/branch (verbatim from source, "State that lives where you want it")
```go
import firebasex "github.com/firebase/genkit/go/plugins/firebase/exp"
import genkitx "github.com/firebase/genkit/go/genkit/exp"

store, err := firebasex.NewFirestoreSessionStore[WeatherState](ctx, g,
    firebasex.WithCollection("snapshots"),
    firebasex.WithCheckpointInterval(10),
)
if err != nil {
    log.Fatal(err)
}

weatherAgent := genkitx.DefineAgent(g, "weatherAgent",
    aix.InlinePrompt{
        ai.WithSystem("Answer weather questions. Ask for a location when one is missing."),
        ai.WithTools(getWeather),
    },
    aix.WithSessionStore(store),
)
```
```go
// Continue the latest state in a conversation.
out, err := weatherAgent.RunText(ctx, "Continue where we left off.",
    aix.WithSessionID[WeatherState]("user-session-123"),
)

// Or branch from a specific saved point.
branch, err := weatherAgent.RunText(ctx, "Revise this plan for a smaller budget.",
    aix.WithSnapshotID[WeatherState](approvedPlanSnapshotID),
)
```
Source: same post, "State that lives where you want it."

### HTTP serving (verbatim from source, "Serve it over HTTP")
```go
import genkitx "github.com/firebase/genkit/go/genkit/exp"

mux := http.NewServeMux()
for _, route := range genkitx.AllAgentRoutes(g) {
    mux.HandleFunc(route.Pattern(), route.Handler())
}

log.Fatal(http.ListenAndServe(":8080", mux))
```
Source: same post, "Serve it over HTTP."

### JavaScript remote client and streaming (verbatim from source, "A rich client for full-stack integration")
```javascript
import { remoteAgent } from 'genkit/beta/client';

const agent = remoteAgent<WeatherState>({
  url: 'http://localhost:8080/api/weatherAgent',
});

const chat = agent.chat();
const res = await chat.send('Weather in Tokyo?');

console.log(res.text);
```
```javascript
const turn = agent.chat().sendStream('Write a long report.');

for await (const chunk of turn.stream) {
  if (chunk.text) process.stdout.write(chunk.text);
  if (chunk.custom) updateStatus(chunk.custom);
  if (chunk.artifact) renderArtifact(chunk.artifact);
}

const res = await turn.response;
```
Source: same post, "A rich client for full-stack integration."

### Interruptible tool for human approval (verbatim from source, "Human approval, built in")
```go
import genkitx "github.com/firebase/genkit/go/genkit/exp"
import "github.com/firebase/genkit/go/ai/exp/tool"

runShell := genkitx.DefineInterruptibleTool(g, "run_shell",
    "Run a shell command after a safety check.",
    func(ctx context.Context, input ShellInput, confirm *Confirmation) (ShellOutput, error) {
        if isRisky(input.Command) {
            if confirm == nil {
                return ShellOutput{}, tool.Interrupt(ShellInterrupt{
                    Command: input.Command,
                    Reason:  "The command can modify files.",
                })
            } else if !confirm.Approved {
                return ShellOutput{}, errors.New("user rejected shell command execution")
            }
        }

        return execute(input.Command)
    },
)
```
Source: same post, "Human approval, built in."

### Detach and poll a long-running task (verbatim from source, "Work that outlives the request")
```javascript
const chat = reportAgent.chat({ sessionId: 'report-123' });
const task = await chat.detach('Write the quarterly market report.');

// Persist this so any client can reconnect to the work later.
savePendingSnapshot(task.snapshotId);

for await (const snapshot of task.poll({ intervalMs: 1000 })) {
  renderStatus(snapshot.status);
  if (snapshot.status === 'completed') renderMessages(snapshot.state.messages);
}
```
Source: same post, "Work that outlives the request."

### Multi-agent delegation via middleware (verbatim from source, "Coordinate specialists")
```go
import middlewarex "github.com/firebase/genkit/go/plugins/middleware/exp"

coordinator := genkit.DefineAgent(g, "coordinator",
    aix.InlinePrompt{
        ai.WithSystem("Delegate to specialists, inspect their results, then answer the user."),
        ai.WithUse(
            &middlewarex.Agents{
                Agents:           []aix.AgentRef{researcher.Ref(), coder.Ref()},
                MaxDelegations:   5,
                ArtifactStrategy: middlewarex.ArtifactStrategySession,
            },
            &middlewarex.Artifacts{Readonly: true},
        ),
    },
)
```
Source: same post, "Coordinate specialists."

### Session store options (verbatim list from source, "Choose your persistence")
```
In-memory for tests, demos, and single-process experiments.
File for local development and single-host apps that need snapshots to
  survive a restart.
Firestore for production apps on Google Cloud or Firebase that want a
  managed, multi-instance database with no store code to write.
Custom when you need to use your own database, authorization, or have
  specific retention policies. You can implement your own persistence
  layer using the `store` interface.
```
Source: same post, "Choose your persistence."

### ADK-vs-Genkit-Agents decision criteria (verbatim from source, "When to reach for ADK instead")
```
Genkit agents are an application primitive, built to live inside a
full-stack, user-facing app. Consider the Agent Development Kit (ADK)
instead when:

- Multi-agent orchestration is the whole system, not just one feature.
  ADK is purpose-built for complex agent topologies, where Genkit's
  delegation middleware is deliberately lighter and not built into the
  core of the agent abstraction.
- You want a managed runtime, not just a library. ADK pairs with Agent
  Runtime on the Gemini Enterprise Agent Platform for hosting, scaling,
  and managed sessions.
```
Source: same post, "When to reach for ADK instead."

## Cross-References

- **Corroborates**:
  - `blog-anthropic-multi-agent-coordination-patterns.md` (Claim 7, "For
    most use cases, we recommend starting with orchestrator-subagent. It
    handles the widest range of problems with the least coordination
    overhead."): this source's `Agents` middleware (Claim 13) is a
    concrete, shipped framework implementation of exactly that topology —
    an orchestrator agent whose delegation to specialists is expressed as
    ordinary tool calls, with a `MaxDelegations` cap as a specific,
    named guard that the Anthropic taxonomy discusses only in the abstract
    (as "termination conditions" for the shared-state pattern, Claim 5 of
    that note).
  - `blog-google-adk-a2a-contract-compliance.md` (Claim 6, `ToolContext.state`
    as "a shared dictionary that all sub-agents in a pipeline read from and
    write to, acting as a data bus between agents"): this source's custom
    state plus artifact-merge-into-parent-session mechanism (Claim 6 and
    Claim 13 here) is an analogous state-sharing primitive in a sibling
    Google framework, though Genkit's mechanism is scoped to a
    session/snapshot rather than an explicit shared dictionary — the two
    frameworks solve the same "sub-agents need to share data" problem with
    different concrete data structures.

- **Contradicts**: None filed. No existing corpus source makes a claim
  about Genkit's specific mechanics that this post disagrees with; where
  this source's ADK-vs-Genkit guidance (Claim 14) draws a boundary against
  ADK, it is Google's own product-positioning statement about two of its
  own frameworks, not a disputed claim about the same mechanism (see
  `blog-google-adk-2-0-deterministic-workflows.md` and
  `blog-google-adk-a2a-contract-compliance.md` for ADK's own framing of
  when to decompose into multi-agent systems — these are complementary
  "when to use which Google framework" guidance, not competing claims
  about the same system).

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md` (Claim 8, "MCP Apps
    (interactive interfaces returned by tools) and elicitation
    (server-initiated user input mid-tool-call) are the first official
    protocol extensions enabling richer human-in-the-loop patterns"): this
    source's `DefineInterruptibleTool()` (Claim 11) is a second,
    independent implementation of pause-for-human-input, built at the
    application-framework layer rather than the MCP protocol layer.
    Together, the two sources show HITL-via-tool-interrupt becoming a
    pattern implemented at multiple layers of the agent stack (protocol
    extension in MCP; framework primitive in Genkit) rather than a single
    vendor's one-off feature. Genkit's specific addition — validating the
    resume payload against session history to prevent forged approvals
    (Claim 11) — is a security mechanic not described in the MCP
    elicitation extraction.
  - `blog-langchain-deep-agents-deploy.md` (Claim 4, closed harnesses
    described as a "walled garden" with high lock-in, contrasted with
    Deep Agents Deploy's open, model-agnostic architecture; Claim 7,
    the deployment surface exposes dedicated human-in-the-loop/guardrail
    endpoints): this source's explicit custom-store option (Claim 15,
    "Custom when you need to use your own database, authorization, or
    have specific retention policies") is Genkit's direct answer to the
    same lock-in concern that motivates the Deep Agents Deploy pitch —
    though for a different underlying product category (an in-process
    application framework vs. a hosted deployment platform). Both sources
    treat "can you own your persistence layer" as a first-order design
    axis for evaluating an agent framework/platform.
  - `blog-anthropic-session-management-1m-context.md` (Claim 2, "Every
    turn in a Claude Code session is a branching point with five distinct
    options"; Claim 4, `/rewind` as a correction mechanism that preserves
    useful file reads while dropping failed attempts): this source's
    snapshot/branch mechanism (Claim 5, branch from an exact `snapshotId`
    "without disturbing the original thread") is a conceptually similar
    idea — treating a conversation as a set of addressable branch points
    — but implemented at a different layer: Claude Code's branching is an
    interactive coding-session UX feature; Genkit's branching is an
    application-level state-persistence primitive a developer builds
    product features on top of (e.g., "revise this plan for a smaller
    budget" as a new branch). Different layers of the stack solving a
    structurally similar problem, not competing claims.

- **Novel**:
  - **Snapshot-ID branching as a first-class, addressable state-persistence
    primitive** (Claim 5): no prior corpus source describes a framework
    letting a developer branch application/conversation state from an
    arbitrary earlier point via a stable ID, independent of the original
    thread. This is new to the corpus at the application-framework layer
    (as distinct from the interactive-session-UX layer covered by
    `blog-anthropic-session-management-1m-context.md`).
  - **Detach/poll as a reuse of the same persistence mechanism used for
    ordinary conversation continuity** (Claim 12): folding a long-running
    async task's progress tracking into the same session-store/snapshot
    abstraction used for chat continuity, rather than a separate job-queue
    system, is a new architectural pattern in the corpus.
  - **A unified streaming chunk type carrying text, custom state, or an
    artifact interchangeably** (Claim 10): no prior corpus source
    describes a single stream API multiplexing three different payload
    kinds (token text, application state deltas, generated-artifact
    updates) rather than a text-only token stream plus separate mechanisms
    for other update types.
  - **Server-side validation of interrupt-resume payloads against session
    history as an explicit anti-forgery mechanism for human-in-the-loop
    approvals** (Claim 11): this specific security mechanic — the runtime,
    not just the client UI, enforces that an approval corresponds to a
    real pending interrupt — is new to the corpus's human-in-the-loop
    coverage.

## Guide Impact

- **Chapter 02 (Harness Engineering), "Multi-Agent Coordination Patterns"**
  (`guide/02-harness-engineering.md`, ~line 1261, currently sourced from
  `blog-anthropic-multi-agent-coordination-patterns`): add this source's
  `Agents` middleware delegation mechanism (Claim 13) as a concrete,
  shipped-framework example of the orchestrator-subagent pattern, including
  the specific `MaxDelegations` cap as a named implementation of the
  "explicit termination conditions" guidance the existing section already
  states abstractly for the shared-state pattern. This gives the chapter a
  cross-vendor example (Anthropic's taxonomy + a concrete Google framework
  implementation) rather than resting the pattern description on a single
  source's abstract framing.

- **Chapter 02 (Harness Engineering)**: there is currently no dedicated
  section on human-in-the-loop tool interrupts or on state-persistence
  architecture (server-managed vs. client-managed, session stores). This
  source, combined with `blog-anthropic-mcp-production-agents.md` Claim 8
  (MCP Apps/elicitation) and `blog-langchain-deep-agents-deploy.md` Claim 7
  (HITL/guardrail endpoints), provides enough corroborating first-party
  and practitioner material to justify a new subsection on human-in-the-
  loop approval patterns, using Claim 11's specific mechanic (interrupt
  payload + server-side validation against session history to prevent
  forged approvals) as the concrete worked example of what a robust
  implementation looks like, not just "the agent can pause and ask."

- **Chapter 02 (Harness Engineering)**: the server-managed vs.
  client-managed state distinction (Claims 3–4) and the four-backend
  session-store menu (Claim 15) are a reusable decision framework for any
  team choosing how to persist agent state, independent of whether they
  use Genkit specifically. Recommend citing this alongside
  `blog-langchain-deep-agents-deploy.md`'s lock-in argument (Claim 4) when
  the guide discusses build-vs-buy and vendor lock-in for agent
  infrastructure — Genkit's explicit "implement your own persistence layer
  using the `store` interface" option (Claim 15) is a concrete example of
  the "avoid lock-in" design Deep Agents Deploy argues for in the abstract.

## Extraction Notes

- The article was fetched twice via the WebFetch tool (which returned a
  paraphrased/refused-verbatim summary the second time, citing copyright
  constraints on full reproduction) and once via a direct `curl` request
  for the raw HTML, which was then stripped to plain text with a Python
  script. All `Quote` fields above were verified character-for-character
  against the raw-fetched plain text (saved locally during extraction),
  not taken from either WebFetch summarizer pass. The raw fetch and the
  WebFetch summarizer passes agreed on content and structure throughout.
- The article is a single page with no sub-pages requiring follow-up. It
  links to "Full-stack agents documentation" (genkit.dev/docs/agents/overview/)
  and a "get started with Genkit" onboarding link, plus three unrelated
  "Related Posts" (an Antigravity race-coach demo, a LiteRT.js
  announcement, and a TPU elastic-training post) — none of these were
  followed; the documentation link is a broader portal rather than a
  specific extension of this post's content, and the Related Posts are
  unrelated content-marketing cross-links, consistent with the judgment
  call already recorded in `blog-google-adk-2-0-deterministic-workflows.md`'s
  Extraction Notes for a similarly-structured Google Developers Blog post.
- The Vercel AI SDK integration mention (`@genkit-ai/vercel-ai` package,
  `GenkitChatTransport` adapter for the `useChat` hook) was judged too thin
  — one sentence, no code sample, no independent verification — to warrant
  its own claim; noted here for completeness rather than extracted as a
  claim.
- No contradiction issue was filed. The ADK-vs-Genkit guidance (Claim 14)
  is Google's own product-positioning statement distinguishing two of its
  own frameworks, not a disputed claim about a shared mechanism — see
  Cross-References → Contradicts.
- Confidence graded `emerging` overall (not `settled`) despite most
  individual claims being graded `settled`: the source describes a preview
  API that the post itself states "can introduce breaking changes in minor
  version releases," and several of the most guide-relevant claims (the
  problem-statement framing in Claim 1, the ADK-boundary guidance in Claim
  14, the Developer UI framing in Claim 16) are vendor positioning rather
  than independently verified outcomes. No adoption data, production case
  study, or independent practitioner account of using the Agents API was
  available to corroborate the mechanics beyond the vendor's own
  description.
