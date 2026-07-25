---
source_url: https://vercel.com/changelog/ai-sdk-7
source_type: blog-post
title: "AI SDK 7 is now available"
author: Gregor Martynus, Lars Grammel, Felix Arntz, Aayush Kapoor, Josh Singh (Vercel)
date_published: 2026-06-25
date_extracted: 2026-07-25
last_checked: 2026-07-25
status: current
confidence_overall: emerging
issue: "#2225"
---

# AI SDK 7 is now available

> Vercel's major-version changelog for AI SDK 7, introducing `HarnessAgent` —
> a standardized `Agent` interface for wrapping external agent harnesses
> (Claude Code, Codex, Deep Agents, OpenCode, Pi) — alongside `WorkflowAgent`
> durable execution, tool-approval policies with HMAC-signed replay, scoped
> per-tool context, first-class timeout budgets, sandboxed tool execution,
> a redesigned OpenTelemetry/tracing-channel observability layer, and MCP
> Apps (sandboxed-iframe UI rendering for MCP tools), plus two breaking
> requirements (Node.js 22, ESM-only imports) and a dedicated migration skill.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`;
  a long-form major-version release note with ten section headings, ~15
  embedded TypeScript/bash code examples, and a dedicated migration-guide
  section).
- **Author credibility**: First-party Vercel product-team announcement,
  credited to five named individuals (Gregor Martynus, Lars Grammel, Felix
  Arntz, Aayush Kapoor, Josh Singh) verified directly in the page's raw
  HTML byline. Lars Grammel and Gregor Martynus are established AI SDK
  core-team names from prior public AI SDK work; this reads as an
  engineering-authored release note (detailed API signatures, explicit
  breaking-change call-outs, package names) rather than a marketing post —
  no customer quotes, revenue figures, or adoption metrics are given
  anywhere in the source.
- **Scope**: Covers what changed across the entire `ai` package and its
  `@ai-sdk/*` satellite packages in the v6→v7 major version bump: agent
  development primitives (reasoning control, runtime/tool context, file
  and skill uploads, MCP Apps, a terminal UI), production-run primitives
  (tool approvals, `WorkflowAgent` durable execution, timeouts, sandboxed
  execution), a new external-harness-integration layer (`HarnessAgent`),
  observability (telemetry, `@ai-sdk/otel`, Node.js tracing channel,
  lifecycle callbacks, performance stats), multi-modal capabilities
  (realtime, video, speech/transcription, images-as-files, embeddings),
  UI/streaming/message-handling changes, and MCP client changes. Does
  **not** cover: pricing for any new capability, a GA timeline for the
  several features explicitly marked experimental (realtime, video
  generation), independent benchmarks or third-party validation of any
  claim, or named customer/production deployments using AI SDK 7 — every
  claim here is Vercel's own first-party description of what shipped, not
  independently verified production evidence.

## Extracted Claims

### Claim 1: AI SDK 7 is positioned as a major release expanding the SDK from model-call/chat primitives into a full agent-development, production-run, and observability platform spanning text, audio, realtime, image, and video
- **Evidence**: The changelog's opening framing sentence, immediately followed by a six-bullet "At a Glance" summary covering develop/run/integrate/observe/build-beyond-text/upgrade.
- **Confidence**: settled (first-party framing statement of the release's own scope, unambiguous as a description of what the vendor asserts it shipped)
- **Quote**: "AI SDK 7 is a major release for building production agents in TypeScript. The SDK has grown from model calls and chat primitives into a broader agent platform for developing, running, integrating, and observing agents across text, audio, realtime, image, and video."
- **Our assessment**: This is a vendor's own self-positioning claim, not an independently verified capability assessment — but the six-bullet structure it introduces (develop / run / integrate any harness / observe / build beyond text / upgrade) maps directly onto this note's claim organization below, since each bullet corresponds to a distinct, separately-documented feature set in the changelog body.

### Claim 2: AI SDK 7 requires Node.js 22 as a minimum runtime and drops CommonJS `require()` support entirely in favor of ESM-only imports
- **Evidence**: Stated explicitly as one of "two breaking requirements" in a dedicated "Before You Upgrade" section, with the specific native-API dependency named as the reason for the Node.js floor.
- **Confidence**: settled (explicit, unambiguous version/import-syntax requirement)
- **Quote**: "Node 22 is required because the SDK depends on APIs (including the native `fetch` implementation and improved `AsyncLocalStorage` semantics) that are not backported to earlier LTS lines." / "AI SDK 7 requires ESM imports (`import` syntax or `.mjs` files). CommonJS `require()` is not supported."
- **Our assessment**: This is a hard compatibility gate, not a soft recommendation — any team on Node 18/20 LTS or a CommonJS-only build pipeline cannot adopt AI SDK 7 without a runtime and/or module-system migration first. The stated mechanism (native `fetch`, `AsyncLocalStorage` semantics) is specific enough to be checkable against Node's own release notes, though this note does not independently verify that claim against Node.js's changelog.

### Claim 3: AI SDK 7 adds a provider-agnostic `reasoning` parameter on `generateText`/`streamText` that maps to provider-native reasoning-effort settings across ten named providers, with the caveat that exact behavior varies by provider
- **Evidence**: A worked code example (`reasoning: 'high'`) plus an explicit list of supported providers and an explicit caveat about behavioral variance.
- **Confidence**: settled (first-party API description with a runnable code example and an explicit named-provider list)
- **Quote**: "`generateText` and `streamText` now support a top-level `reasoning` option that maps to provider-native settings across OpenAI, Anthropic, Google, Groq, xAI, Bedrock, Fireworks, DeepSeek, Open Responses, and OpenAI-compatible providers. Note that exact behavior and available parameters vary by provider."
- **Our assessment**: This is a specific abstraction-layer design choice worth flagging for the guide: rather than each provider integration exposing its own reasoning-control API surface, AI SDK 7 centralizes it behind one parameter name (`reasoning`) that fans out to provider-specific settings underneath — while explicitly disclaiming that the abstraction is leaky ("exact behavior and available parameters vary by provider"). This is the same self-disclosed-limitation pattern this corpus has flagged as high-value elsewhere (e.g. `blog-vercel-enterprise-apps-and-agents.md` Claim 7's revocation caveat) — the vendor names the abstraction's own boundary rather than presenting it as uniform.

### Claim 4: AI SDK 7 introduces `HarnessAgent`, a standardized `Agent` interface (with `generate`/`stream` results) for wrapping external, established agent harnesses — Claude Code, Codex, Deep Agents, OpenCode, and Pi — behind the same interface used by the rest of the SDK
- **Evidence**: A dedicated "Integrate Agent Harnesses" section with a worked code example (`HarnessAgent` + `claudeCode` harness + `createVercelSandbox`), plus four bullet points naming the adapters, configurability, session durability, and gateway authentication.
- **Confidence**: settled (first-party API description with package names, a runnable code example, and an explicit list of the five named harnesses supported)
- **Quote**: "AI SDK 7 introduces a harness layer for bringing established agents into the AI SDK ecosystem. Wrap harnesses such as Claude Code, Codex, Deep Agents, OpenCode, and Pi behind the same agent interface used by the rest of the SDK." / "`HarnessAgent`: Run external agent harnesses through the AI SDK `Agent` interface, with standard `generate` and `stream` results."
- **Our assessment**: This is the single most novel and highest-value claim in this source for the guide's harness-engineering material. `blog-latentspace-ainews-meta-harness-summer.md` Claim 1 named "Vercel's Eve and HarnessAgent" as part of an asserted, self-described-as-"undocumented" lineage of meta-harnesses, with no primary source for `HarnessAgent` specifically available in the corpus at that time. This changelog is the primary, first-party documentation that pointer was asking for: `HarnessAgent` is not part of `eve` (Vercel's separate, previously-documented agent-building framework — see Cross-References, this changelog does not mention `eve` at all) but a distinct AI SDK 7 capability, shipped as `@ai-sdk/harness/agent` with per-harness adapter packages (e.g. `@ai-sdk/harness-claude-code`). It is explicitly a harness-of-harnesses/adapter layer — normalizing five *other* companies' and projects' agent runtimes behind one interface — which is architecturally closer to the "meta-harness" pattern (coordinating other harnesses rather than executing tools directly) than to an agent-authoring framework like `eve`.

### Claim 5: `HarnessAgent` runs support configurable sandboxes, instructions, custom skills and tools, durable/resumable sessions via workflow utilities, and Vercel OIDC-based authentication for AI Gateway
- **Evidence**: Four bullet points immediately following the `HarnessAgent` code example, each naming a distinct capability of harness runs.
- **Confidence**: settled (first-party enumeration of a shipping feature's properties)
- **Quote**: "Configurable harness runs: Harness agents can receive sandboxes, instructions, custom skills, and tools, so the same runtime can be shaped for different products and workflows." / "Durable, resumable sessions: Workflow utilities, session bridging, and APIs for interrupted-turn continuation make harness runs suitable for longer tasks." / "Gateway-ready authentication: Harness adapters support Vercel OIDC for AI Gateway, simplifying hosted and sandboxed agent execution."
- **Our assessment**: The durability claim here ("workflow utilities, session bridging... interrupted-turn continuation") uses the same underlying durable-execution machinery (`@ai-sdk/workflow`) documented for `WorkflowAgent` in Claim 7 below — meaning a wrapped Claude Code or Codex session running inside `HarnessAgent` can, per this claim, survive interruption the same way a native AI SDK agent can. No worked code example or further mechanism detail is given for exactly how session bridging/interrupted-turn continuation works for a wrapped external harness specifically (as opposed to a native `ToolLoopAgent`), so this should be read as a capability claim, not a documented mechanism.

### Claim 6: AI SDK 7 adds `toolApproval` policies at the call or agent level (user-approval, auto-approve, auto-deny, or a typed approval function), with an optional HMAC-signing mode that cryptographically binds a tool's original inputs to its approval token to prevent argument tampering between request and resumption
- **Evidence**: A worked code example (`toolApproval: { deleteFile: 'user-approval' }`) plus a dedicated "Hardened approval replay" bullet explaining the HMAC mechanism's purpose.
- **Confidence**: settled (first-party API and security-mechanism description with a runnable code example)
- **Quote**: "`generateText`, `streamText`, and `ToolLoopAgent` can define approval policies at the call or agent level. Policies can require user approval, auto-approve, auto-deny, or delegate to typed approval functions." / "Higher-risk approval flows can revalidate tool inputs and policies before continuation, use WorkflowAgent approval validation, and opt into HMAC signing. HMAC signing cryptographically binds the original tool inputs to the approval token, preventing tampering with tool arguments between the approval request and resumption."
- **Our assessment**: The HMAC-signed-replay detail is the more novel and guide-relevant half of this claim: it names a specific, concrete attack this design closes — an approval token issued for one set of tool arguments (e.g. "delete file X") being replayed or resumed against a *different*, tampered set of arguments (e.g. "delete file Y") if the approval flow spans an async gap (a human approving hours later, a process restart). This is a request-integrity concern distinct from, but structurally similar in spirit to, the credential-scoping concerns this corpus has documented for Vercel Connect (`blog-vercel-enterprise-apps-and-agents.md` Claim 6) — both are about narrowing what a previously-granted authorization can be used for at the moment it is actually exercised.

### Claim 7: AI SDK 7 introduces `WorkflowAgent` (in `@ai-sdk/workflow`) for long-running agents whose execution state is persisted to durable storage between steps, so an agent survives deploys, process restarts, interruptions, and delayed approvals
- **Evidence**: A dedicated "Durable execution" bullet with a worked code example (`new WorkflowAgent({ model, tools, runtimeContext })`) and an explicit list of the failure/interruption modes the persistence survives.
- **Confidence**: settled (first-party API description with a runnable code example, package name, and explicit list of survived interruption types)
- **Quote**: "`@ai-sdk/workflow` introduces `WorkflowAgent` for long-running agents. Execution state is persisted to durable storage between steps, so agents survive deploys, process restarts, interruptions, and delayed approvals."
- **Our assessment**: `blog-vercel-workflow-sdk-payload-compression.md` (a June 22, 2026 changelog, three days before this one) already documented that Workflow SDK 5 beta compresses run/hook/step payloads with zstd, and that `eve` — Vercel's separate agent-authoring framework — "builds durable agents on the Workflow SDK" and inherits that compression automatically. `WorkflowAgent` here is a new, AI-SDK-native class built on that same underlying `@ai-sdk/workflow` durable-execution machinery, but it is a distinct primitive from `eve` itself: this changelog never mentions `eve`, and `WorkflowAgent` is exposed directly through the `ai`/`@ai-sdk/workflow` packages rather than through `eve`'s own framework surface. Whether `eve`'s own durable-agent implementation is now built on `WorkflowAgent` specifically (as opposed to Workflow SDK primitives more generally) is not stated in either source — this is a real, unresolved gap between the two notes' claims, not a contradiction (see Cross-References).

### Claim 8: AI SDK 7 adds first-class timeout budgets — total, per-step, per-chunk, default-tool, and per-tool — with aborts raised as a `TimeoutError` that flows through stream and UI protocols
- **Evidence**: A worked code example (`timeout: { totalMs, stepMs, chunkMs, toolMs }`) plus explicit naming of the error type and its propagation path.
- **Confidence**: settled (first-party API description with a runnable code example)
- **Quote**: "Text generation and agent APIs can define total, per-step, per-chunk, default tool, and per-tool timeout budgets. Timeout aborts use `TimeoutError`, and abort reasons flow through stream and UI protocols."
- **Our assessment**: Five independent timeout granularities (total/step/chunk/default-tool/per-tool) is a notably fine-grained timeout model compared to the single, coarse "overall request timeout" pattern common in most HTTP client libraries — it lets a caller bound, for example, how long any single tool call may run without also bounding the total multi-step agent run to the same duration, or vice versa. No prior corpus source documents a timeout model at this granularity for agent execution specifically.

### Claim 9: AI SDK 7 adds sandboxed execution abstractions supporting command execution, streaming output, working directories, environment variables, abort signals, and step-level sandbox overrides
- **Evidence**: A worked tool-definition code example (`experimental_sandbox.run({ command })`) showing a tool erroring out cleanly (`throw new Error('Sandbox is not available')`) when no sandbox is configured.
- **Confidence**: settled (first-party API description with a runnable code example), though the API is explicitly marked `experimental_sandbox` in the code itself
- **Quote**: "The sandbox abstractions support command execution, streaming output, working directories, environment variables, abort signals, and step-level sandbox overrides."
- **Our assessment**: The `experimental_` prefix on the actual API surface (`experimental_sandbox`) is a signal this note flags explicitly because the surrounding prose does not call out the experimental status the way it does for realtime/video (Claim 12) — a practitioner reading only the bullet-point prose could reasonably assume this is stable, when the code example's own naming convention says otherwise.

### Claim 10: AI SDK 7 redesigns observability around global telemetry registration, a new dedicated `@ai-sdk/otel` package (moved out of the core `ai` package), and native Node.js tracing-channel emission for structured event subscription
- **Evidence**: Three separate bullets with worked code examples: `registerTelemetry()` for both a third-party integration (Langfuse) and `@ai-sdk/otel`, plus a `tracingChannel` subscription example using Node's `node:diagnostics_channel` module.
- **Confidence**: settled (first-party API description with three separate runnable code examples and explicit package/module names)
- **Quote**: "Register telemetry once and receive structured events across model calls, steps, tools, embeddings, reranking, and agent execution." / "OpenTelemetry support now lives in `@ai-sdk/otel`, with GenAI-semantic convention spans and metrics, supplemental AI SDK attributes, and span-enrichment hooks." / "AI SDK 7 emits structured telemetry through the Node.js tracing channel, allowing observability providers to subscribe once while preserving async context across streaming and tool execution."
- **Our assessment**: Moving OpenTelemetry out of the core `ai` package into a separate `@ai-sdk/otel` package (also documented as a breaking/migration item under "Other Migration Themes": "OpenTelemetry span collection is no longer built into the `ai` package") is a deliberate architectural decoupling — telemetry becomes an opt-in registration rather than bundled-by-default instrumentation. The Node.js tracing-channel addition is a distinct, lower-level mechanism (subscribing directly to Node's native diagnostics channel) that does not require OpenTelemetry at all, giving observability vendors a second, framework-agnostic integration point.

### Claim 11: AI SDK 7 adds sensitive-context controls that require runtime/tool context values to be explicitly opted into telemetry output, to prevent secrets from being exposed by default
- **Evidence**: A worked code example showing `runtimeContext: { userId, feature }` alongside `telemetry: { includeRuntimeContext: { userId: true, feature: true } }` as separate, explicit opt-ins.
- **Confidence**: settled (first-party API description with a runnable code example demonstrating the opt-in pattern)
- **Quote**: "Runtime and tool context can be deliberately included in telemetry, with controls to prevent secrets from being exposed by default."
- **Our assessment**: This is a "secure by default" design choice for the telemetry surface specifically — given that Claim 5 (`toolsContext`) and typed `runtimeContext` are explicitly designed to carry secrets/config values (e.g. API keys) scoped to individual tools, a telemetry system that captured all context by default would risk leaking exactly the values `toolsContext` was designed to scope narrowly. Requiring per-field opt-in (`includeRuntimeContext: { userId: true }`) closes that gap architecturally rather than relying on developer discipline to avoid logging secrets.

### Claim 12: MCP Apps — a new MCP capability in AI SDK 7 — let MCP tools render app-specific UI inside sandboxed iframes, distinguishing model-visible tools from app-only tools, communicating over JSON-RPC for tools, resources, logs, and display updates
- **Evidence**: A dedicated "MCP Apps" bullet plus a worked React code example (`MCPAppRenderer` with a `sandbox` URL and an `allowedTools` handler restriction) and a corresponding "App rendering" bullet in the separate "Configure MCP" section.
- **Confidence**: settled (first-party API description with a runnable code example and an explicit architectural distinction between model-visible and app-only tools)
- **Quote**: "MCP support now includes model-visible versus app-only tools, app metadata, sandboxed iframe rendering, and JSON-RPC communication for tools, resources, logs, and display updates." / "MCP Apps use tool metadata to render app-specific UI inside sandboxed iframes while keeping model-visible and app-only tools separate."
- **Our assessment**: The model-visible/app-only tool split is the architecturally interesting detail: it means an MCP server can expose UI-only affordances (e.g. a "refresh dashboard" button rendered inside the sandboxed iframe) that the *model* never sees as a callable tool and cannot invoke directly — only the rendered app UI can trigger them, via the `allowedTools` allowlist in the code example. This is a deliberate capability-narrowing mechanism at the MCP layer: some tool surface is reachable by the human interacting with the rendered app, but is explicitly withheld from the model's own tool-calling surface.

### Claim 13: AI SDK 7 promotes speech generation and transcription (`generateSpeech`, `transcribe`) to stable, non-experimental exports, while realtime voice/video conversation and video generation ship as explicitly experimental capabilities across multiple named providers
- **Evidence**: A "Stable speech and transcription" bullet with a code example, contrasted against separately-labeled "Realtime (experimental)" and "Video generation (experimental)" bullets naming specific supported providers for each.
- **Confidence**: settled (first-party stability-tier classification, explicitly distinguishing which multi-modal capabilities are stable versus experimental)
- **Quote**: "`generateSpeech`, `transcribe`, `SpeechResult`, and `TranscriptionResult` are stable exports." / "Realtime (experimental): Browser-to-provider WebSocket sessions for OpenAI, Google, and xAI, with audio/text conversations, client-driven tool calls, and normalized routing through AI Gateway." / "Video generation (experimental): Video generation works across AI Gateway, Google AI Studio, Google Vertex, fal, Replicate, ByteDance Seedance, Kling AI, Prodia, and xAI, with support for long-running SSE responses and safer bounded downloads."
- **Our assessment**: The explicit stable/experimental split is worth preserving for the guide as a signal of what production teams should build against today (speech/transcription) versus what remains subject to breaking changes (realtime, video) — nine distinct video-generation provider integrations shipping simultaneously (AI Gateway, Google AI Studio, Google Vertex, fal, Replicate, ByteDance Seedance, Kling AI, Prodia, xAI) is a notably broad initial provider surface for an experimental capability, suggesting Vercel is treating video-generation provider breadth as a launch priority even while marking the capability itself unstable.

### Claim 14: AI SDK 7 ships a dedicated migration skill (`npx skills add vercel/ai --skill migrate-ai-sdk-v6-to-v7`) and automated codemods (`npx @ai-sdk/codemod v7`) as the two primary upgrade mechanisms, with an explicit five-step manual upgrade path for changes codemods cannot fully automate
- **Evidence**: Dedicated "Upgrade Path" and "Configure Runtime and Packaging" sections with terminal commands, an AI-agent prompt template, and a five-step numbered list distinguishing automatable from manual-review changes.
- **Confidence**: settled (first-party migration tooling description with exact terminal commands and an explicit prompt template)
- **Quote**: "Codemods cannot fully decide runtime requirements, ESM imports, instruction/message behavior, runtime/tool context separation, approval policy placement, stream helper usage, and multi-step result shapes." / "Use the migrate-ai-sdk-v6-to-v7 skill and migrate my app from AI SDK v6 to v7."
- **Our assessment**: The explicit list of what codemods *cannot* automate (seven named categories, from runtime requirements to multi-step result shapes) is a concrete, checkable scope boundary for the automated-migration claim — Vercel is not asserting the codemods handle the full migration, only "the majority of renames, import changes, and API moves," with semantic/behavioral changes requiring human review regardless of tooling. The migration-skill distribution mechanism itself (`npx skills add vercel/ai --skill ...`, installable and directly promptable to "your AI coding agent") is a concrete instance of the general "skills as portable, installable upgrade knowledge" pattern already documented in this corpus (see Cross-References).

## Concrete Artifacts

### `HarnessAgent` usage example (verbatim, from "Integrate Agent Harnesses" section)

```typescript
Source: https://vercel.com/changelog/ai-sdk-7

import { HarnessAgent } from '@ai-sdk/harness/agent';
import { claudeCode } from '@ai-sdk/harness-claude-code';
import { createVercelSandbox } from '@ai-sdk/sandbox-vercel';

const agent = new HarnessAgent({
  harness: claudeCode,
  sandbox: createVercelSandbox({ runtime: 'node24' }),
  instructions: 'Review the repository and make a small, safe fix.',
});

const result = await agent.generate({
  prompt: 'Fix the failing unit test.',
});
```

### `WorkflowAgent` durable-execution example (verbatim, from "Run Agents in Production" section)

```typescript
Source: https://vercel.com/changelog/ai-sdk-7

import { WorkflowAgent } from '@ai-sdk/workflow';

const agent = new WorkflowAgent({
  model: 'openai/gpt-5.5',
  tools,
  runtimeContext: {
    userId: 'user_123',
  },
});
```

### Scoped tool context example (verbatim, from "Develop Agents" section)

```typescript
Source: https://vercel.com/changelog/ai-sdk-7

import { generateText, tool } from 'ai';
import * as z from 'zod/v4';

const result = await generateText({
  model: 'openai/gpt-5.5',
  tools: {
    weather: tool({
      inputSchema: z.object({ city: z.string() }),
      contextSchema: z.object({ apiKey: z.string() }),
      execute: async ({ city }, { context }) =>
        getWeather(city, context.apiKey),
    }),
  },
  toolsContext: {
    weather: {
      apiKey: process.env.WEATHER_API_KEY,
    },
  },
  prompt: 'What is the weather in SF?',
});
```

### Timeout budget example (verbatim, from "Run Agents in Production" section)

```typescript
Source: https://vercel.com/changelog/ai-sdk-7

import { generateText } from 'ai';

const result = await generateText({
  model: 'openai/gpt-5.5',
  timeout: {
    totalMs: 60_000,
    stepMs: 10_000,
    chunkMs: 2_000,
    toolMs: 5_000,
  },
  prompt: 'Research this issue and summarize it.',
});
```

### MCP Apps renderer example (verbatim, from "Develop Agents" section)

```tsx
Source: https://vercel.com/changelog/ai-sdk-7

import { experimental_MCPAppRenderer as MCPAppRenderer } from '@ai-sdk/react';
import { isToolUIPart } from 'ai';
{
  messages.map(message =>
    message.parts.map(part =>
      isToolUIPart(part) ? (
        <MCPAppRenderer
          key={part.toolCallId}
          part={part}
          sandbox={{ url: '/mcp-app-sandbox' }}
          loadResource={app => fetch(`/api/mcp-apps?uri=${app.resourceUri}`)}
          handlers={{ allowedTools: ['refreshDashboard'] }}
        />
      ) : null,
    ),
  );
}
```

### Migration tooling commands and API/rename summary (verbatim, from "Configure Runtime and Packaging" section)

```
Source: https://vercel.com/changelog/ai-sdk-7

Terminal:
  npx skills add vercel/ai --skill migrate-ai-sdk-v6-to-v7
  npx @ai-sdk/codemod v7

AI Prompt (to send to a coding agent):
  Use the migrate-ai-sdk-v6-to-v7 skill and migrate my app from AI SDK v6 to v7.

Coming out of experimental (renamed to stable):
  experimental_customProvider -> customProvider
  experimental_generateImage  -> generateImage
  experimental_output         -> output
  experimental_prepareStep    -> prepareStep
  experimental_telemetry      -> telemetry

Renamed APIs:
  system option           -> instructions
  onFinish                -> onEnd
  StreamTextResult.fullStream -> stream
  CallSettings split into model generation options and request/transport options

Deprecated:
  needsApproval on tool()/dynamicTool() -> use toolApproval on
    generateText/streamText/ToolLoopAgent
  result.toUIMessageStreamResponse() / result.toTextStreamResponse()
    -> use createUIMessageStreamResponse / createTextStreamResponse
  Vue Chat class -> use the useChat composable
```

## Cross-References

### Cross-reference verification notes
`blog-latentspace-ainews-meta-harness-summer.md`, `blog-latentspace-vercel-andrew-qu-eve.md`,
`blog-vercel-workflow-sdk-payload-compression.md`, `blog-vercel-enterprise-apps-and-agents.md`,
`blog-humanlayer-skill-issue-harness-engineering.md`, and `blog-anthropic-mcp-production-agents.md`
were re-read (in full or, for the longer notes, via their `### Claim N:` heading
list) during this extraction per MINER.md §4b, and every claim number cited
below was located and confirmed against that note's own numbered claims in
document order before writing this section.

- **Resolves an existing corpus pointer**:
  - `blog-latentspace-ainews-meta-harness-summer.md` Claim 1 named "Vercel's
    Eve and HarnessAgent" as part of an explicitly self-described-as-
    "undocumented" meta-harness lineage, with that note's own Cross-References
    and Guide Impact sections flagging it as "a list of harness-of-harnesses
    tools worth independent research/mining — none are currently documented
    in the corpus." This source is the first primary documentation of
    `HarnessAgent` specifically (Claim 4 here): a standardized `Agent`
    interface wrapping five named external harnesses (Claude Code, Codex,
    Deep Agents, OpenCode, Pi) behind one API. This resolves half of that
    pointer — `HarnessAgent`, not `eve` — with first-party technical detail
    (package names, a runnable code example, sandbox/durability/auth
    properties) that the digest-sourced note could not supply.
  - `blog-latentspace-vercel-andrew-qu-eve.md` documents `eve` in depth from
    its own lead engineer's first-party account (an agent-*building*
    framework assembled from reusable internal libraries — model/provider
    switching, fallbacks, resumability), explicitly *not* described there as
    a harness-of-harnesses. This source corroborates that distinction from
    the other direction: this AI SDK 7 changelog documents `HarnessAgent` in
    full without mentioning `eve` anywhere in its text (verified by
    searching the raw page HTML for the standalone word "eve" — zero
    matches), confirming `HarnessAgent` and `eve` are separate Vercel
    products/layers, not two names for the same thing. The meta-harness
    lineage note's phrasing ("Vercel's Eve and HarnessAgent") listed them
    together but did not claim they were the same thing; this source
    confirms they are architecturally distinct, addressing that note's own
    Andrew-Qu-note-directed recommendation to keep them separate in the
    guide.

- **Corroborates**:
  - `blog-vercel-workflow-sdk-payload-compression.md` Claim 6 (`eve` "builds
    durable agents on the Workflow SDK" and inherits zstd payload
    compression automatically, no code changes required): this source's
    Claim 7 (`WorkflowAgent`, also built on `@ai-sdk/workflow`, persists
    execution state to durable storage between steps) confirms the same
    underlying `@ai-sdk/workflow` durable-execution machinery is the shared
    foundation both `eve` and the new AI-SDK-native `WorkflowAgent` sit on
    top of — though (see Extends below) this source does not state whether
    `eve`'s implementation now uses `WorkflowAgent` specifically or a
    different layer of the same underlying Workflow SDK.
  - `blog-vercel-enterprise-apps-and-agents.md` Claim 6 (Vercel Connect
    scopes external-service credentials at individual-request granularity,
    e.g. one GitHub repository, read-only, for one call — "least privilege
    becomes the shape of the request"): this source's Claim 6 (HMAC-signed
    tool-approval replay, binding an approval token to its original tool
    arguments so it cannot be reused with tampered arguments) is a
    structurally similar request-integrity mechanism at a different layer —
    Connect narrows what an external credential can reach; AI SDK 7's HMAC
    approval signing narrows what an *already-approved* tool call can be
    resumed with. Both are instances of the same broader "scope
    authorization to the exact unit of work being performed, not a broader
    standing grant" architectural pattern this corpus has documented across
    multiple vendors.
  - `blog-anthropic-mcp-production-agents.md` Claim 1 ("Agents are only as
    useful as the systems they can reach") and its broader case for MCP as
    the standard production integration layer: this source's MCP-related
    claims (Claim 12, MCP Apps; the separate "Configure MCP" section's
    protocol-version and typed-tool-output additions) corroborate, from a
    second major vendor (Vercel, not Anthropic), that MCP is being actively
    extended as a richer agent-integration surface rather than treated as a
    finished, static protocol.

- **Extends**:
  - `blog-vercel-workflow-sdk-payload-compression.md`: extends that note's
    documentation of Vercel's durable-execution storage layer (zstd
    compression) with the AI-SDK-native class (`WorkflowAgent`) built on the
    same underlying package, and surfaces an open question that note's own
    Extraction Notes already flagged as unanswered ("how compression
    interacts with step-state serialization and resumability" — that note
    could not answer this from the compression changelog alone). This
    source does not answer it either: `WorkflowAgent`'s own description
    here says nothing about compression, so the interaction between the two
    features remains undocumented in the corpus after this extraction.
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 7 (hooks as
    "user-defined commands or scripts... executed at various points of the
    agent's lifecycle," positioned as the harness's deterministic-execution
    surface): this source's lifecycle-callback additions (Claim 10's
    `onStart`/`onStepEnd`/`onEnd` code example) are a related but distinct
    mechanism — callbacks observe and react to lifecycle events
    programmatically within the same process, rather than invoking
    separate, hookable external commands/scripts the way HumanLayer's
    "hooks" surface does. Both are lifecycle-event mechanisms, at different
    levels of the stack (in-process callback vs. externally-invoked script).
  - `blog-humanlayer-skill-issue-harness-engineering.md` Claim 12 (skills
    carry supply-chain-style security risk, "treat skills like `npm install
    random-package`"): this source's provider-skill-upload mechanism
    (`uploadSkill`, in the "Develop Agents" section, not separately claimed
    above but visible in the fetched source) and its own migration-skill
    distribution mechanism (Claim 14, `npx skills add vercel/ai --skill
    migrate-ai-sdk-v6-to-v7`) are a concrete instance of the same
    installable-skill pattern HumanLayer's warning addresses — a team
    running that exact command is trusting Vercel's own published skill,
    which is a lower-risk case (first-party, from the framework vendor
    itself) than the third-party-registry risk HumanLayer's claim warns
    about, but the underlying mechanism (an installable, agent-executable
    skill package) is the same one that warning applies to in general.

- **Contradicts**: None identified as a MINER.md §4a contradiction. No claim
  in this source directly opposes a claim in an existing corpus note.

- **Novel**:
  - **`HarnessAgent` as a standardized interface for wrapping external agent
    harnesses** (Claim 4): the first primary-source documentation in this
    corpus of a framework-level abstraction that normalizes multiple
    *other* companies' and projects' agent runtimes (Claude Code, Codex,
    Deep Agents, OpenCode, Pi) behind one common `Agent` interface with
    `generate`/`stream` results — resolving the meta-harness lineage
    pointer noted above.
  - **HMAC-signed tool-approval replay binding** (Claim 6): no prior corpus
    source documents cryptographically binding a tool-call approval token
    to its original arguments to prevent tampering during an async
    approval gap.
  - **Five-granularity timeout budget model for agent execution** (Claim
    8): total/per-step/per-chunk/default-tool/per-tool timeouts as
    independently configurable budgets is a level of execution-time control
    not previously documented in this corpus.
  - **Model-visible vs. app-only MCP tool separation with sandboxed-iframe
    UI rendering** (Claim 12): no prior corpus source documents an MCP
    mechanism for exposing tool surface reachable only by a rendered app UI
    and explicitly withheld from the model's own tool-calling surface.
  - **A provider-agnostic `reasoning` parameter fanning out to ten named
    providers' native reasoning-effort settings** (Claim 3): no prior
    corpus source documents a cross-provider reasoning-control abstraction
    at this breadth (ten named providers) in a general-purpose agent SDK.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add `HarnessAgent` (Claim 4, code
  example in Concrete Artifacts) as a concrete, primary-sourced example
  resolving the previously-unverified "meta-harness" pointer
  (`blog-latentspace-ainews-meta-harness-summer.md` Claim 1) — specifically,
  document that `HarnessAgent` is a distinct Vercel product from `eve`
  (this changelog never mentions `eve`), positioned as an adapter/
  normalization layer over five named external agent harnesses rather than
  an agent-authoring framework. This is a citable example for any guide
  discussion of "harness of harnesses" or meta-harness architecture that
  currently lacks a primary source.

- **Chapter 02 (Harness Engineering) — durable execution**: Add
  `WorkflowAgent` (Claim 7) alongside the existing Workflow SDK compression
  coverage (`blog-vercel-workflow-sdk-payload-compression.md`) as the
  AI-SDK-native durable-agent primitive, while flagging the open question
  neither source answers: whether `eve`'s own durable-agent implementation
  uses `WorkflowAgent` specifically, and how compression and durable
  execution interact for `WorkflowAgent` runs. Recommend this as a gap for
  a future source-submission if `eve`'s own documentation clarifies it.

- **Chapter 02 (Harness Engineering) — tool authorization**: Add HMAC-signed
  approval replay (Claim 6) as a concrete implementation pattern for
  request-integrity in async human-approval flows, alongside the existing
  Vercel Connect request-scoped-credential pattern
  (`blog-vercel-enterprise-apps-and-agents.md` Claim 6) — both are instances
  of narrowing authorization to the exact unit of work at the moment it is
  exercised, at two different layers (external credential scope vs.
  approved-tool-call argument integrity).

- **Chapter 03 (Verification)**: Add the five-granularity timeout-budget
  model (Claim 8) as a concrete mechanism for bounding agent runaway
  behavior at multiple levels (total run, per step, per chunk, per tool) —
  useful for any guide section on runtime safety controls for autonomous or
  semi-autonomous agent loops.

- **Chapter 03 (Verification) or Ch02**: Add the observability redesign
  (Claim 10: `@ai-sdk/otel` decoupled from core, Node.js tracing-channel
  emission) and the sensitive-context telemetry opt-in (Claim 11) as a
  concrete example of "secure by default" observability design — telemetry
  does not capture runtime/tool context (which may carry secrets) unless
  explicitly and individually opted in per field.

## Extraction Notes

1. **WebFetch output not trusted for quotes; raw HTML fetched and parsed
   instead.** An initial WebFetch pass returned a clean-reading but
   AI-summarized abstract, not verbatim source text, consistent with
   MINER.md §2a's warning. Per that section's guidance, the raw page was
   fetched directly via `curl` with a browser user-agent, the `<article>`
   element was isolated (370KB of a ~1MB page), and converted to plain
   Markdown with `html2text` (26.9KB of resulting text). Every `Quote`
   field in this note was located character-for-character in that
   locally-converted plain-text capture, not from the WebFetch summary
   pass. Byline author names and the publish date were independently
   verified against raw HTML timestamps (`2026-06-25T00:00`) and name
   strings, not taken on faith from the WebFetch pass.
2. **The "eve" cross-check was verified programmatically, not by eyeballing
   a search-results list.** To confirm `HarnessAgent` and `eve` are
   distinct (see Cross-References → Resolves an existing corpus pointer),
   the raw article HTML was searched with a word-boundary regex
   (`\beve\b`, case-insensitive) rather than a plain substring search — a
   naive substring search for "eve" returns false-positive matches inside
   words like "however" and "achieve"; the word-boundary search confirmed
   zero standalone occurrences of "eve" in the article content.
3. **No sub-pages followed beyond the main changelog.** The changelog
   contains no inline links to other Vercel blog posts or deeper
   documentation pages (unlike some other Vercel sources in this corpus,
   e.g. `blog-vercel-enterprise-apps-and-agents.md`, which linked a
   same-day companion post) — every claim above is drawn from the single
   changelog page itself. MINER.md §1's "follow up to 5 linked pages"
   guidance did not apply because no such substantive linked pages exist
   in this source.
4. **No contradiction issues filed.** No claim in this source opposes any
   existing corpus note; see Cross-References → Contradicts. One
   near-miss was evaluated (whether `WorkflowAgent`'s introduction here
   supersedes or conflicts with `eve`'s prior "builds durable agents on the
   Workflow SDK" framing) and judged not to rise to a contradiction — both
   claims are compatible descriptions of the same underlying Workflow SDK
   foundation, just with an open, unanswered question about how the two
   relate exactly (flagged in Guide Impact, not filed as a contradiction,
   since neither source makes a claim that opposes the other).
5. **Confidence calibration: emerging.** Individual claims are mostly rated
   "settled" because they are first-party, unambiguous descriptions of
   shipping API surfaces with runnable code examples, several independently
   verified against raw HTML. The note's overall confidence is "emerging"
   rather than "settled" because: (a) this is a single vendor's own release
   announcement with no independent verification, benchmark, or named
   customer/production evidence anywhere in the source; (b) several
   headline capabilities are explicitly marked experimental in code
   (`experimental_sandbox`, `experimental_MCPAppRenderer`,
   `experimental_useRealtime`, `experimental_generateVideo`) even where the
   surrounding prose does not always flag that status as prominently
   (Claim 9's assessment flags this gap specifically); and (c) several
   claims (Claim 5's `HarnessAgent` durability, Claim 7's `WorkflowAgent`
   relationship to `eve`) describe capabilities whose exact mechanism or
   interaction with other Vercel products is asserted but not fully
   documented within this source alone.
