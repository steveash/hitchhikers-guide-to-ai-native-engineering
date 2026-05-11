---
source_url: https://cursor.com/blog/typescript-sdk
source_type: blog-post
title: "Build programmatic agents with the Cursor SDK"
author: Cursor (Anysphere)
date_published: 2026-04-29
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#467"
---

# Build programmatic agents with the Cursor SDK

> Cursor's public beta SDK announcement gives external developers access to the same runtime, harness, and models that power Cursor's own agents — exposing intelligent context management, MCP servers, skills, hooks, and subagent delegation through a TypeScript API with cloud, self-hosted, and local runtime options.

## Source Context

- **Type**: blog-post (Cursor / Anysphere official product blog, April 29, 2026; no individual author attributed — company-authored announcement)
- **Author credibility**: Official Cursor engineering blog post announcing a public beta product. As a vendor product announcement, it has commercial motivation to present capabilities favorably. The technical specifics (dedicated VM per session, three runtime options, named harness components, code examples, customer quote from Faire) are concrete enough to treat as genuine product documentation. Treat claims about capabilities as emerging — first-party and commercially motivated, but backed by a live product.
- **Scope**: Covers the SDK API surface (TypeScript, cloud/self-hosted/local runtimes), harness capabilities exposed externally (context management, MCPs, skills, hooks, subagents), multi-model routing, Cloud Agents API integration, use cases (CI/CD, end-to-end automation, customer-facing embedding), four sample starter projects, and pricing model. Does NOT cover failure modes, rate limits, how the SDK handles long-running agent failures, session persistence details, latency of cloud vs. local, or how self-hosted workers communicate with Cursor's inference layer.

## Extracted Claims

### Claim 1: The Cursor SDK exposes the same runtime, harness, and models that power Cursor's own agents to external developers via TypeScript

- **Evidence**: Direct product announcement framing for the public beta release. The SDK is installed via `npm install @cursor/sdk` and provides the `Agent` class as the primary entry point.
- **Confidence**: emerging (vendor announcement; product is live and in public beta)
- **Quote**: "We're introducing the Cursor SDK so you can build agents with the same runtime, harness, and models that power Cursor."
- **Our assessment**: This is the core strategic claim. Prior Cursor sources (`blog-cursor-continual-harness-improvement.md`, `blog-cursor-composer2-technical-report.md`) document Cursor's harness from the internal engineering perspective. The SDK announcement is the first source in our corpus that makes the Cursor harness available as programmable external infrastructure. The implications for the guide are significant: the patterns Cursor's engineering posts describe as internal are now reproducible by third-party developers without building from scratch.

### Claim 2: Coding agents are evolving from interactive tools for individual developers to programmatic infrastructure for organizations

- **Evidence**: Opening framing of the announcement; consistent with the use cases described (CI/CD, end-to-end workflow automation, customer-facing embedding).
- **Confidence**: emerging (authorial framing, not a metric; but supported by the concrete use cases documented in the post)
- **Quote**: "Coding agents are evolving from interactive tools for individual developers to programmatic infrastructure for organizations."
- **Our assessment**: This is the market framing claim, not a technical claim. It positions the SDK as part of a broader shift from "developer uses AI assistant" to "organization runs AI agents as infrastructure." The customer use cases described in the post (CI/CD pipeline integration, Slack-to-PR workflows, customer-facing embedding) are concrete evidence for this direction. Consistent with `blog-cursor-amplitude-autonomous-pipeline.md` Claim 1 (event-driven pipeline replacing human triage role) and `blog-cursor-security-agents.md` Claim 9 (3,000+ PRs reviewed weekly) — both document organizations running agents as infrastructure rather than individual tools.

### Claim 3: Building capable coding agents requires meaningful engineering effort across sandboxing, state management, environment setup, and context management — the SDK abstracts this entirely

- **Evidence**: Direct characterization of the agent-building problem before the SDK existed.
- **Confidence**: emerging (authorial framing; the specific components named are consistent with the engineering complexity documented in `blog-cursor-composer2-technical-report.md` Claim 6 on the Anyrun platform)
- **Quote**: "Building fast, reliable, and capable coding agents that run safely against your data requires meaningful engineering effort: secure sandboxing, durable state and session management, environment setup, and context management."
- **Our assessment**: The four named components — sandboxing, durable state, environment setup, context management — map directly to what the Composer 2 technical report describes as Cursor's internal infrastructure (Anyrun: Firecracker VMs, forking, environment cloning; self-summarization for context management). The SDK claim is that this complexity is now a solved problem for developers who want to build on top of Cursor's stack, rather than building the same stack from scratch. This is a concrete answer to "how hard is it to build a production agent harness?" — the answer is "hard enough that Cursor built an SDK to abstract it."

### Claim 4: Cloud SDK sessions run on the same optimized runtime as Cloud Agents, with per-session dedicated VMs, sandboxing, and a reconnect-after-disconnect feature for long-running agents

- **Evidence**: Product feature description with specific technical details (dedicated VM, strong sandboxing, repo clone, dev environment).
- **Confidence**: emerging (vendor-described; consistent with the Anyrun architecture in `blog-cursor-composer2-technical-report.md` and the self-hosted cloud agents architecture in `blog-cursor-self-hosted-cloud-agents.md`)
- **Quote**: "Cloud sessions initiated from the SDK run on the same optimized runtime used for Cloud Agents. Each agent gets its own dedicated VM with strong sandboxing, a clone of the repo, and a fully configured development environment."
- **Our assessment**: The reconnect feature is the most operationally novel element here: "Agents keep going when your laptop sleeps or network drops. You can stream the conversation and reconnect later." This means SDK cloud agents are not request-response — they are long-running asynchronous workloads that survive network disconnects. The code example shows a fire-and-check-later pattern (`agent.send(...)` returns a `run.id`, which can be retrieved later with `Agent.getRun(run.id, ...)`). This is a different programming model from synchronous API calls and enables the CI/CD use case: kick off a task, get a run ID, check back when CI needs the result.

### Claim 5: Three runtime deployment options let organizations balance capability, security, and development speed without changing agent logic

- **Evidence**: Three runtime options documented with specific trade-offs: cloud (optimized VM, sandboxed), self-hosted workers (code execution inside org network), local (fast iteration).
- **Confidence**: emerging (vendor-described; self-hosted workers reference the same architecture as `blog-cursor-self-hosted-cloud-agents.md`)
- **Quote**: "When you need a different runtime, the same SDK can run agents on self-hosted workers, keeping code and tool execution inside your network, or locally on your machine for fast iteration."
- **Our assessment**: The three-runtime design is significant for enterprise adoption: the same agent code can be developed locally, tested in self-hosted workers (internal infrastructure access), and run at scale in cloud. The runtime is a configuration parameter, not an architectural commitment. This eliminates the problem documented in `blog-cursor-amplitude-autonomous-pipeline.md` Claim 4 (the "false plateau" where local-only agents hit memory and resource limits) — teams can start local and migrate to cloud without rewriting agent logic.

### Claim 6: The SDK exposes the full Cursor harness externally: codebase indexing, semantic search, instant grep, MCP servers, skills (auto-loaded from .cursor/skills/), hooks (.cursor/hooks.json), and subagent delegation

- **Evidence**: Explicit enumeration of harness components in the product announcement.
- **Confidence**: emerging (product feature list; consistent with Cursor's documented internal harness)
- **Quote**: "Agents launched through the SDK benefit from the same harness that powers Cursor across our desktop app, CLI, and web app"
- **Our assessment**: The five harness components named are significant individually:
  (1) **Intelligent context management** (indexing/semantic search/grep) — this is the context retrieval infrastructure described abstractly in `blog-cursor-continual-harness-improvement.md` Claim 12, now available to SDK agents.
  (2) **MCP servers** — available via `.cursor/mcp.json` config file or passed inline; same pattern as the security MCP in `blog-cursor-security-agents.md` Claim 2.
  (3) **Skills** — "Agents pick up skills automatically from your repo's `.cursor/skills/` directory." Auto-discovery means agent behavior is configured by repo contents, not hardcoded in agent logic.
  (4) **Hooks** — "Observe, control, and extend the agent loop across cloud, self-hosted, and local with a `.cursor/hooks.json` file." Hooks apply in all three runtimes.
  (5) **Subagents** — "Delegate subtasks to named subagents with their own prompts and models, which the main agent spawns via the `Agent` tool." Named subagents with distinct prompts and models is a first-class SDK feature.

### Claim 7: Multi-model routing requires only a single field change, letting teams optimize cost/capability tradeoff per task without rebuilding agent logic

- **Evidence**: API design claim supported by the code examples in the post (model field in `Agent.create()`).
- **Confidence**: emerging (vendor design claim; API surface is live in public beta)
- **Quote**: "Route agents to the best model for the task at hand, with your desired balance of cost and capability, with a single field change."
- **Our assessment**: The code examples show `model: { id: "composer-2" }` and `model: { id: "gpt-5.5" }` as interchangeable model configurations. This is the SDK-level implementation of the multi-model routing pattern documented operationally in `blog-cursor-continual-harness-improvement.md` Claim 8 (OpenAI vs. Anthropic native tool format provisioning). The "single field change" framing abstracts away the harness-level complexity of model-specific tool format provisioning — the SDK handles that internally. For practitioners: the per-task model selection documented in Cursor's production harness is now available as a configuration parameter without building the routing layer.

### Claim 8: The updated Cloud Agents API allows SDK-started runs to appear in Cursor's Agents Window and web app, enabling programmatic start with optional human takeover

- **Evidence**: Product feature description of the Cloud Agents API integration.
- **Confidence**: emerging (vendor-described feature; API is live in public beta)
- **Quote**: "The SDK uses the updated Cloud Agents API, which allows cloud agent runs to show up in Cursor's Agents Window and web app. You can start a task programmatically and then jump into Cursor to inspect progress or take over the work."
- **Our assessment**: The "start programmatically, inspect/take over in IDE" pattern is novel to the corpus. It creates a hybrid human-agent workflow that is neither fully autonomous nor fully interactive: an agent starts unattended, a human checks in (or doesn't), and can take over if needed. This is distinct from the "shadow mode → PR commenting → blocking gate" gradual rollout pattern in `blog-cursor-security-agents.md` Claim 4 — it is an ad-hoc supervision mechanism rather than a staged trust-building process. For the guide: this pattern enables the "human-in-the-loop only when needed" workflow without requiring the agent to stop and ask for help.

### Claim 9: Teams are deploying SDK agents in CI/CD pipelines, end-to-end workflow automations, and embedded in customer-facing products

- **Evidence**: Three named deployment patterns; one named customer (Faire) with an attributed quote from George Jacob (Senior Engineering Manager).
- **Confidence**: emerging (three named deployment patterns; one named customer quote; vendor-authored case documentation)
- **Quote**: "Many teams are invoking agents directly from CI/CD pipelines, creating automations for end-to-end workflows, and embedding agents into their core products."
- **Our assessment**: The specific CI/CD use case documented is: "programmatic agents that are kicked off directly from CI/CD to summarize changes, identify root causes for CI failures, and update PRs with fixes." This is an extension of the pattern in `blog-cursor-amplitude-autonomous-pipeline.md` Claim 1 (Slack→Linear→PR pipeline) to CI/CD triggers. The customer-facing embedding use case is novel: "end users now get an agent experience without leaving the host application" — this positions Cursor's SDK as a platform for building AI products, not just internal tooling. The Faire quote adds: "running our own programmatic agents on that same cloud runtime, without managing VMs or working around memory limits, to keep our codebase healthy without constant developer intervention."

### Claim 10: When a cloud agent finishes, it can open a PR, push a branch, or attach demos and screenshots as structured outputs

- **Evidence**: Product feature description. The cloud code example shows `autoCreatePR: true` as a configuration option.
- **Confidence**: emerging (vendor-described; the PR URL is returned via `result.git?.branches[0]?.prUrl` in the code example)
- **Quote**: "When the agent finishes, it can open a PR, push a branch, or attach demos and screenshots."
- **Our assessment**: Structured outputs (PR URL, branch reference, screenshots) close the loop between the agent's work and the CI/CD or review system that needs to consume it. The `autoCreatePR: true` configuration means PR creation is opt-in — teams can start programmatic agents without PR auto-creation for internal workflows, then add it when ready for external deliverables. The screenshot/demo attachment is relevant for UI-generating agents — a web app prototyping agent can produce a runnable demo alongside the code.

### Claim 11: Composer 2 is positioned as a specialized coding model achieving frontier-level performance at a fraction of general-purpose model costs, making it the default for SDK use

- **Evidence**: Product framing directly in the SDK announcement.
- **Confidence**: emerging (vendor claim about their own model; quantitative support in `blog-cursor-composer2-technical-report.md` Claim 4 which shows 61.3% CursorBench vs. GPT-5.4's 63.9% at lower cost)
- **Quote**: "Composer 2, a specialized coding model that achieves frontier-level performance at a fraction of the cost of general-purpose models, you get the best combination of intelligence and efficiency for most coding agent tasks."
- **Our assessment**: The SDK announcement bundles the model recommendation with the harness announcement — this is not a neutral presentation. The quantitative evidence in the Composer 2 technical report (61.3% on CursorBench vs. GPT-5.4 at 63.9%) supports "near-frontier" but not "frontier-level." For practitioners: the SDK makes Composer 2 the obvious default, but the multi-model routing API allows substitution. Teams with specific model requirements (OpenAI tools, Anthropic models) can use those via the same SDK without harness rearchitecting.

### Claim 12: The SDK is priced at standard token-based consumption, distinct from interactive tool subscription pricing

- **Evidence**: Pricing model described in the closing section.
- **Confidence**: settled (stated pricing model; consistent with cloud agent pricing in the Cursor product)
- **Quote**: "The Cursor SDK is available to all users and is billed based on standard, token-based consumption pricing."
- **Our assessment**: Token-based consumption pricing means SDK use scales with agent usage rather than seat licenses. For organizations running agents at scale (CI/CD, automated workflows), the cost model is different from interactive tool subscriptions: the same usage by one person at a desk or a hundred CI pipeline runs cost identically. This is a practitioner-relevant pricing consideration when deciding between interactive tools and programmatic agents for a given workload.

## Concrete Artifacts

### Minimal SDK Initialization

```typescript
// Source: cursor.com/blog/typescript-sdk (April 29, 2026)
import { Agent } from "@cursor/sdk";

const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "composer-2" },
  local: { cwd: process.cwd() },
});

const run = await agent.send("Summarize what this repository does");

for await (const event of run.stream()) {
  console.log(event);
}
```

### Cloud Agent with Auto-PR (Fire-and-Check-Later Pattern)

```typescript
// Source: cursor.com/blog/typescript-sdk (April 29, 2026)

// Initiate cloud agent to start a task...:
const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY!,
  model: { id: "gpt-5.5" },
  cloud: {
    repos: [{ url: "https://github.com/cursor/cookbook", startingRef: "main" }],
    autoCreatePR: true,
  },
});

const run = await agent.send("Fix the auth token expiry bug");
console.log(`Started ${run.id}`);

// ...check back in later, from anywhere:
const result = await (
  await Agent.getRun(run.id, { runtime: "cloud", agentId: run.agentId })
).wait();
console.log(result.git?.branches[0]?.prUrl);
```

### SDK Harness Components Reference

```
Source: cursor.com/blog/typescript-sdk (April 29, 2026)

INTELLIGENT CONTEXT MANAGEMENT
  - Codebase indexing (full repo indexed for agent use)
  - Semantic search (query by meaning, not just filename/content)
  - Instant grep (fast exact-match text search across codebase)
  Purpose: "help agents get to the right outcome faster and more efficiently"

MCP SERVERS
  - Via .cursor/mcp.json config file
  - Or passed inline on the SDK call
  - Supported transports: stdio or HTTP

SKILLS
  - Auto-loaded from .cursor/skills/ directory
  - Quote: "Agents pick up skills automatically from your repo's `.cursor/skills/` directory."

HOOKS
  - Configured via .cursor/hooks.json
  - Available across cloud, self-hosted, and local runtimes
  - Quote: "Observe, control, and extend the agent loop"

SUBAGENTS
  - "Delegate subtasks to named subagents with their own prompts and models"
  - Main agent spawns subagents via the `Agent` tool
  - Named subagents — each has its own distinct prompt and model
```

### Three-Runtime Deployment Model

```
Source: cursor.com/blog/typescript-sdk (April 29, 2026)

CLOUD
  - Same optimized runtime as Cloud Agents
  - Dedicated VM per session with strong sandboxing
  - Clone of repo + fully configured dev environment
  - Reconnect after network drop/laptop sleep
  - Outputs: auto-PR, branch push, demos/screenshots
  - Shows up in Cursor's Agents Window and web app

SELF-HOSTED WORKERS
  - Code and tool execution stays inside org network
  - Same harness as cloud (feature parity)
  - Targets: regulated/compliance-sensitive environments

LOCAL
  - Runs on developer's machine
  - Fast iteration for development
  - Limited by local resources (memory, concurrent agents)

Model routing: single `model: { id: "..." }` field change; works across all runtimes.
```

### Sample Starter Projects

```
Source: cursor.com/blog/typescript-sdk (April 29, 2026)

Quickstart         — minimal Node.js: create local agent, send one prompt, stream response
Prototyping tool   — web app: spin up agents to scaffold projects in sandboxed cloud environment
Kanban board       — agent-powered task assignment: drag card → agent picks up work →
                     opens PR → posts result back as attachment
Coding agent CLI   — terminal interface to spawn Cursor agents from command line
```

### Faire Customer Quote on SDK Value Proposition

```
Source: cursor.com/blog/typescript-sdk (April 29, 2026)
George Jacob, Senior Engineering Manager, Faire:

"Cursor offers a great cloud experience for running many agents in parallel from
the editor and CLI. We're excited about the SDK as a path to running our own
programmatic agents on that same cloud runtime, without managing VMs or working
around memory limits, to keep our codebase healthy without constant developer
intervention."
```

## Cross-References

- **Corroborates**: `blog-cursor-self-hosted-cloud-agents.md` Claim 3 (inference/execution split: cloud-side inference, on-prem execution) and Claim 4 (per-session VM isolation) — The SDK's cloud runtime uses the same dedicated-VM-per-session architecture described in the March 2026 self-hosted agents post. The SDK extends this to external developers. The self-hosted worker option in the SDK directly corroborates the self-hosted agent architecture described there: the same outbound-HTTPS worker pattern, same harness feature parity (Claim 11 in that note: "identical functionality to cloud-hosted variants").

- **Corroborates**: `blog-cursor-amplitude-autonomous-pipeline.md` Claim 2 (60–70% auto-merge Bugbot), Claim 3 (hourly cron legacy-migration automations) — The CI/CD integration and workflow automation use cases documented in the SDK announcement are the same patterns Amplitude describes as production deployments. The SDK formalizes the API surface for the patterns Amplitude implemented. The Faire quote ("to keep our codebase healthy without constant developer intervention") maps directly to Amplitude's autonomous pipeline approach.

- **Corroborates**: `blog-cursor-continual-harness-improvement.md` Claim 12 (harness evolved from heavy static context toward dynamic tool-fetched context) — The SDK's "intelligent context management" (indexing, semantic search, grep) is the mature dynamic-context harness described in that post, now exposed externally. The skills (auto-loaded from `.cursor/skills/`) and hooks (`.cursor/hooks.json`) are the same configuration-driven extension mechanisms described there.

- **Corroborates**: `blog-cursor-security-agents.md` Claim 8 (MCP as coordination substrate for agent fleet) and Claim 2 (MCP deployed as Lambda for persistent state and deduplication) — The SDK's first-class MCP server support (inline or via config file) is the same MCP infrastructure pattern documented in Cursor's internal security agent fleet. External developers can now use the same MCP-as-coordination-substrate pattern by wiring in their own MCP servers to SDK agents.

- **Extends**: `blog-cursor-self-hosted-cloud-agents.md` — The March 2026 self-hosted agents post described a product feature (run Cursor agents in your own infrastructure). The SDK announcement extends that to a programmatic API: the same runtime is now accessible via TypeScript with fire-and-check-later semantics, run ID retrieval, and model routing. The SDK is the developer-experience layer built on top of the self-hosted agent infrastructure.

- **Extends**: `blog-cursor-composer2-technical-report.md` Claim 6 (Anyrun platform: 500+ pods/second, Firecracker VMs, fork/snapshot, hundreds of thousands of concurrent sandboxed environments) — The SDK's cloud runtime is the external developer-facing surface of the Anyrun platform described in the Composer 2 technical report. Anyrun provides the "dedicated VM with strong sandboxing, a clone of the repo, and a fully configured development environment" per session. The SDK abstracts Anyrun into a `cloud: { repos: [...] }` configuration block.

- **Extends**: `blog-cursor-continual-harness-improvement.md` Claim 13 (automated "software factory" — weekly LLM-powered log scanning that surfaces issues and creates Linear tickets, with Cloud Agents triggerable from Linear) — The SDK provides the programmatic foundation for exactly this kind of automated software factory. The Amplitude post (`blog-cursor-amplitude-autonomous-pipeline.md`) and Cursor's own harness maintenance loop both use Cloud Agents as automation workers; the SDK formalizes the API for this pattern.

- **Novel**: The following patterns are new to the corpus:
  - **Reconnect pattern for long-running cloud agents**: The ability to disconnect from a running cloud agent and reconnect later (`Agent.getRun(run.id, ...)`) is not documented in any prior source note. It enables CI/CD fire-and-forget: kick off an agent, get a run ID, check the result when needed without maintaining a persistent connection.
  - **Programmatic start with IDE takeover**: Starting an agent via SDK and then jumping into the Cursor IDE to inspect/take over the work is a novel hybrid human-agent workflow not documented elsewhere in the corpus.
  - **External developer access to the Cursor harness as infrastructure**: No prior source documents Cursor offering its harness (skills, hooks, subagents, context management) as programmable infrastructure for third-party agent builders. All prior Cursor sources describe internal use of the same harness.
  - **Kanban board as agent architecture**: The agentic kanban pattern (drag card → agent picks up work → opens PR → posts result as attachment) is a concrete end-to-end user interaction model for programmatic agents not described elsewhere.
  - **Customer-facing embedding**: Embedding Cursor agents in products where end users "get an agent experience without leaving the host application" is a new deployment model not covered by any existing source note (all prior notes cover developer-facing or internal tooling use cases).
  - **Token-consumption pricing for programmatic agents vs. seat pricing for interactive tools**: The explicit pricing model distinction (token-based consumption, not subscription) is the first direct statement in the corpus that programmatic agent pricing differs from interactive tool pricing.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the Cursor SDK as the primary reference for "what does a production harness include?" The SDK's enumerated harness components — codebase indexing, semantic search, grep, MCP servers, skills, hooks, subagents — form a concrete checklist for practitioners evaluating or building agent harnesses. Cite Claim 6 alongside `blog-cursor-continual-harness-improvement.md` Claim 12 (the harness evolved from static to dynamic context): the SDK exposes the mature version of that harness, so practitioners building new harnesses can start from this feature set rather than rediscovering it. The "meaningful engineering effort" framing (Claim 3) validates the guide's advice to use existing harness infrastructure rather than building from scratch.

- **Chapter 02 (Harness Engineering — multi-runtime deployment)**: Add the three-runtime model (cloud/self-hosted/local) as the recommended deployment progression for programmatic agents: develop locally, test in self-hosted, run at scale in cloud. This directly addresses the "false plateau" failure mode in `blog-cursor-amplitude-autonomous-pipeline.md` Claim 4 — local resource limits are solved by cloud runtimes, and the SDK makes switching a single configuration change rather than an architectural rewrite.

- **Chapter 07 (Multi-agent Systems)**: The SDK's named subagent delegation ("Delegate subtasks to named subagents with their own prompts and models, which the main agent spawns via the `Agent` tool") is the harness-level implementation of the planner-worker pattern documented in `blog-cursor-multi-agent-kernels.md`. Add as a concrete API-level example of subagent composition. The kanban board sample (agent picks up work from card → opens PR → posts result) is the end-user-visible version of this pattern.

- **Chapter 04 (Context Engineering)**: The SDK's intelligent context management (codebase indexing, semantic search, instant grep) is the mature answer to context provisioning for code agents. Cite this alongside `blog-cursor-continual-harness-improvement.md` Claim 12 as evidence that leading harnesses have fully shifted from static pre-injected context to dynamic tool-fetched context. For practitioners: when building on the Cursor SDK, you inherit this dynamic context layer; when building a custom harness, design these retrieval primitives in from the start.

- **Chapter 06 (Enterprise Adoption / Deployment)**: The three-runtime option directly addresses enterprise security requirements (self-hosted workers keep code inside the network). Cite alongside `blog-cursor-self-hosted-cloud-agents.md` as the full picture of Cursor's enterprise deployment model — the SDK makes all three runtimes accessible from the same code without architectural divergence. The token-based consumption pricing (Claim 12) is relevant to enterprise cost modeling: programmatic agents at scale have a different cost structure than per-seat interactive tools.

- **New section: Programmatic Agents as Infrastructure**: The guide should distinguish between interactive agent use (developer → IDE → agent → output) and programmatic agent use (CI/CD → SDK → agent → PR/artifact). This source is the clearest statement in the corpus of that distinction: "Coding agents are evolving from interactive tools for individual developers to programmatic infrastructure for organizations." The reconnect pattern (Claim 4), fire-and-check-later API (Claim 8 code example), and CI/CD use case (Claim 9) together define the programmatic agent programming model. No prior source in the corpus articulates this distinction this clearly.

## Extraction Notes

- Blog post fetched at https://cursor.com/blog/typescript-sdk and read in full. The post is a product announcement (~800 words) with two embedded TypeScript code examples, a section on harness capabilities, a section on what teams are building, four sample project descriptions, and a closing section on pricing. No sub-pages were linked beyond the documentation URL and sample project repository (neither fetched — they would provide implementation detail rather than new strategic claims).
- The blog post has no individual author attribution. Treat as "Cursor (Anysphere)" corporate authorship.
- The native `/sdk` skill referenced in the post ("use Cursor's native `/sdk` skill to help you start building") is a harness-side agent behavior available inside the Cursor IDE — a skill that helps developers build SDK agents. Not extracted as a separate claim since it is a UX affordance, not an architectural pattern.
- Date published (April 29, 2026) is from the RSS feed entry in the issue body: "Published: Wed, 29 Apr 2026 12:00:00 +0000".
- No contradictions to file: The SDK announcement is additive to all existing Cursor source notes. It exposes existing internal infrastructure externally but does not contradict any internal engineering claims. The Composer 2 cost/performance claim (Claim 11) is consistent with `blog-cursor-composer2-technical-report.md` Claim 4's quantitative evidence.
