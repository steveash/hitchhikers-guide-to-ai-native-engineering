---
source_url: https://lucumr.pocoo.org/2026/10/6/codemode/
source_type: blog-post
title: "What is Codemode"
author: Armin Ronacher
date_published: 2026-10-06
date_extracted: 2026-10-07
last_checked: 2026-10-07
status: current
confidence_overall: anecdotal
issue: "#3946"
---

# What is Codemode

> Ronacher explains Pi 1.0's "Codemode" — a harness-side sandboxed JavaScript runtime through which the agent composes tool calls (including MCP tools and internal model APIs) outside the LLM context — via a brains-vs-hands framing, real session code, and a list of what MCP servers must change to work well with it.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org; first-person practitioner post, ~1,800 words plus code; published 2026-10-06)
- **Author credibility**: Armin Ronacher created Flask/Jinja2 and the Pi coding agent, and is a `trusted-feed` author in this repo. He is a first-party implementer of the feature described, so claims are design rationale and observed behavior, not controlled measurements.
- **Scope**: Why bash-only tooling is insufficient, the harness/execution-environment split, Codemode semantics in Pi (QuickJS in WASM), four real session examples (image generation, classifier-based issue triage, game-debugging loop, MCP calls), shortcomings of MCP servers for Codemode, and open problems. Does NOT cover: benchmarks or token measurements, security analysis beyond the sandbox constraints, or the details of Pi's MCP implementation.

## Extracted Claims

### Claim 1: Bash can only compose programs, but some LLM-native tools are not programs (image reading, sub-agents), so harness-provided tools remain necessary
- **Evidence**: Reasoned argument with two examples (`read`/`view_image`, sub-agent spawning).
- **Confidence**: settled (follows from how multimodal protocols work)
- **Quote**: "However bash has one fundamental limitation which is that it can only compose programs that run."
- **Our assessment**: Credible and a useful qualifier on the "just use CLIs" position. Sub-agent orchestration via a CLI talking to the harness over sockets is described as "a rather crude process", which is a judgment, not a measurement.

### Claim 2: There are two systems — the trusted harness ("brain") and the execution environment ("hands") — and sandboxing one does not sandbox the other
- **Evidence**: Architectural description of Pi; Gondolin sandbox cited as an example.
- **Confidence**: emerging
- **Quote**: "If you for instance use a sandboxing solution like Gondolin your bash stuff will be sandboxed just fine, but the harness itself will not be."
- **Our assessment**: Important for threat modelling: sandboxing "the agent" often only sandboxes the hands. The two sides also have different file systems and trust levels, which is why harness-side code needs its own sandbox.

### Claim 3: Codemode lets the LLM orchestrate operations on the harness side, inside its own deliberately limited sandbox
- **Evidence**: Pi implementation detail: QuickJS in WASM; the only escape is calling more tools.
- **Confidence**: emerging (first-party description, no independent verification)
- **Quote**: "In case of Pi it's running in QuickJS within a WASM runtime with intentional limitations: no network, no file system, no timers, limited RAM."
- **Our assessment**: The "only way out is tool calls" design means the permission surface equals the tool surface, which is a clean security property. The post notes the language could be swapped (Scheme, Starlark).

### Claim 4: Codemode composes tool calls without passing through the LLM's context, and returns larger outputs structurally than a plain bash tool call
- **Evidence**: Pi truncates plain bash output to trailing 2000 lines; Codemode gets full output.
- **Confidence**: emerging
- **Quote**: "If however the agent issues that invocation via Codemode, then the Codemode side gets larger outputs sent structurally."
- **Our assessment**: Consistent with other "keep intermediate data out of context" patterns, but no token numbers are given here.

### Claim 5: Because Codemode is JavaScript, agents express concurrency and probe-then-batch workflows
- **Evidence**: Observed agent behavior in Pi sessions; `Promise.all` examples; Pi caps concurrent tool executions at four with a queue.
- **Confidence**: anecdotal
- **Quote**: "A common way in which you see agents now use this, is to first probe at 5-10 items from some tool response to see what it looks like, and to then write a Codemode script that processes the next n items."
- **Our assessment**: A concrete, reusable agent behavior (sample a few, then script the rest). It also explains the failure mode in Claim 9.

### Claim 6: Codemode can persist state into the session transcript, readable by later Codemode calls, on the harness host rather than the sandbox
- **Evidence**: The `store("sentiment_results", results)` call in the classification example.
- **Confidence**: anecdotal
- **Quote**: "Codemode also allows you to throw state into the transcript!"
- **Our assessment**: A lightweight cross-call memory mechanism that avoids filesystem access. The post later concedes durability is "trickier" (Claim 11).

### Claim 7: Internal model APIs (image generation, one-shot classifiers like Jev) are exposed only through Codemode, not as regular tools, to avoid wasting context
- **Evidence**: Working code: `models.generateImages()`; `models.classify()` running over 100 GitHub issues; a 30-step game-driving loop using Jev as a per-step decision model.
- **Confidence**: anecdotal (author's own sessions; code is agent-written and re-indented)
- **Quote**: "those Pi APIs are exposed via Codemode, but not via regular tools where they would just waste context."
- **Our assessment**: Novel pattern: treat small decision models as library calls inside agent-written scripts. Connects to the Jev/System-One notes listed below.

### Claim 8: With MCP, tools are not exposed to the LLM at all; the agent uses progressive discovery via tool search inside Codemode
- **Evidence**: Description plus Sentry MCP example, where the agent called tools it had not discovered, informed by a system-prompt notice that the server exists.
- **Confidence**: emerging
- **Quote**: "because we do not actually expose any of the MCP tools to the LLM, the agent first uses provided APIs to issue a tool search within Codemode"
- **Our assessment**: Shifts MCP token cost from definitions-in-context to on-demand discovery, but it relies on the model having seen the server during RL (the author says "presumably").

### Claim 9: MCP works "not amazingly well" with Codemode today; servers should return structured content, consistent results, large binary support, and composable tool search
- **Evidence**: Four listed recommendations; a failure case where a server token-optimizes by result size so a 5-item probe succeeds but a max-batch call fails.
- **Confidence**: emerging
- **Quote**: "This can cause an initial probe with 5 items to succeed, but then fail when the server returns the maximum batch size."
- **Our assessment**: Actionable MCP-server design checklist (use `outputSchema`, keep result shapes stable). Large binary data and cross-server tool search are acknowledged protocol gaps.

### Claim 10: "Codemode in Codemode" (e.g. Cloudflare's MCP server taking JavaScript) is a bad temporary crutch
- **Evidence**: Cloudflare MCP example with JS strings nested in JS; named problems are double JSON escaping, small-model confusion, and inner code being unable to call outer tools.
- **Confidence**: anecdotal
- **Quote**: "It means double JSON escaping, easy for smaller models to get confused by and the inner code cannot call the outer tools."
- **Our assessment**: Pushes back on the server-side code-execution pattern recommended in `blog-anthropic-mcp-production-agents`: that pattern fits non-Codemode harnesses, but is awkward in Codemode harnesses.

### Claim 11: This is not a reversal of the earlier "use CLIs / Code is all you need" position, and open problems remain (durability, deterministic language, images/binary, small models)
- **Evidence**: Author's own framing and list of open issues; suggests durable-workflow-engine snapshots or Starlark.
- **Confidence**: emerging
- **Quote**: "Images, binary data and just the inability of this pattern to work with smaller models is also something that needs to be fleshed out."
- **Our assessment**: Honest limits. The "doesn't work with smaller models" caveat matters for cost-sensitive harness design.

## Concrete Artifacts

Setting (Ronacher, "What is Codemode"): Codemode is enabled by default only when MCP is enabled; turn on with:

```
"defaultTools": ["+codemode"]
```

Image generation (agent-written Pi session code, from the source):

```js
const [painter] = await models.getAvailableOfType("image");
const result = await models.generateImages(painter, {
  input: [{ type: "text", text: "A cute little puppy sitting on a grassy " +
    "lawn, soft natural light, photorealistic" }],
});
if (result.stopReason !== "stop") return result.errorMessage;

for (const block of result.output) {
  if (block.type === "image") image(block);
  else text(block.text);
}
```

Batch classification pattern (abridged from the source's 100-issue Jev sentiment example):

```js
const jev = await models.getModelOfType("classifier", "typesafe", "jev-latest");
const r = await tools.bash({ command: "gh issue list --state open --limit 100 --json number,title,body,comments" });
const results = await Promise.all(issues.map(async (issue) => { /* models.classify(jev, {state, questions}) */ }));
store("sentiment_results", results);
```

Structure of the MCP call example: `tools.mcp__sentry__find_organizations({})` followed by `Promise.allSettled(...)` over `tools.mcp__sentry__find_projects(...)`, with per-item error handling. The source also contains a 30-step `tankctl` game-debugging loop where a classifier picks an action (attack/approach/dodge/powerup) each step.

Source-stated runtime facts: QuickJS in WASM; no network, filesystem, or timers; limited RAM; max 4 concurrent tool executions with queueing; bash output in plain tool calls truncated to trailing 2000 lines.

## Cross-References

- **Corroborates**: `blog-anthropic-mcp-production-agents` Claim 11 (programmatic tool calling processes results in a sandbox rather than returning them raw to the model) and Claim 10 (tool search defers loading tool definitions) — Codemode is a harness-side implementation of both ideas. `blog-bswen-mcp-token-cost` Claim 5 (MCP token cost vs bash) is the problem Codemode's no-definitions-in-context approach addresses.
- **Contradicts**: None filed. Tension, not a contradiction: `blog-anthropic-mcp-production-agents` Claim 7 recommends servers expose a code-accepting tool run in a server-side sandbox; Ronacher (Claim 10 above) reports this nests badly in Codemode harnesses. These differ by harness context, so no contradiction issue was filed.
- **Extends**: `blog-ronacher-what-is-reasoning` (tool-calling behavior comes from RL training; this note builds on that) and `blog-ronacher-pi-oss` (Pi as the working harness). `blog-simonwillison-jev-decision-models` — Codemode shows Jev-style classifiers used as library calls inside agent scripts. `blog-simonwillison-cloudflare-mcp-api-fallback` shows the Cloudflare MCP's limits from another angle.
- **Novel**: The brain/hands trust split with the observation that sandboxing bash does not sandbox the harness; harness-only model APIs (image/classify) as non-tool Codemode functions; `store()` session-transcript state; probe-then-batch behavior; an MCP-server checklist for Codemode compatibility.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "harness-side code execution (Codemode)" subsection: tools exposed via a no-network/no-FS sandbox runtime where the only side effects are tool calls; cite this note for the bash-vs-harness-native tool boundary (image reads, sub-agents).
- **Chapter 04 (Context/Tools, where `blog-anthropic-mcp-production-agents` Claims 10–11 are used)**: Add Codemode as a third context-saving technique next to tool search and programmatic tool calling, noting its limits (small models, binary data).
- **Chapter 06 (Security & Threat Model)**: State the harness/execution-environment split explicitly: sandboxing the execution environment does not protect the harness, and harness-side code needs its own constrained runtime.
- **MCP server guidance**: Add the four server-side recommendations (structured output via `outputSchema`, consistent result shapes regardless of size, binary handling, composable tool search).

## Extraction Notes

- Read the full post (fetched raw HTML, stripped to text); all quotes were copied from that text. No sub-pages followed; the post's links (earlier "Code Is All You Need" / "MCP needs code" posts, Gondolin, Jev, Cloudflare) were not read.
- No metrics or benchmarks in the source; all claims are practitioner assertions. Code is agent-generated from the author's real sessions.
- Triage comments suggested Ch06 relevance; the post's security content is limited to the sandbox constraints and the trust split, so impact there is modest.
