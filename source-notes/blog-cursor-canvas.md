---
source_url: https://cursor.com/blog/canvas
source_type: blog-post
title: "Interact with agent-created visualizations in canvases"
author: Alex Vandak Maloney (Cursor)
date_published: 2026-04-15
date_extracted: 2026-04-20
last_checked: 2026-04-20
status: current
confidence_overall: emerging
issue: "#244"
---

# Interact with agent-created visualizations in canvases

> Cursor 3.1 introduces canvases — React-based interactive dashboards agents produce as durable workspace artifacts — framing them as the primary mechanism for increasing information bandwidth beyond plain text and markdown, with four concrete internal use cases that each replace a previously manual or external workflow.

## Source Context

- **Type**: blog-post (Cursor product blog, product announcement, ~1,000 words, published April 15, 2026)
- **Author credibility**: Alex Vandak Maloney writing on the official Cursor blog. This is a vendor product announcement with commercial motivation; however, the claims are grounded in named internal use cases (Datadog, Databricks, Sentry MCPs; specific eval analysis and autoresearch workflows) and concrete business outcomes ("helped us release two new models in Cursor with far less effort"). Not independently verified, but specific enough to treat as genuine practitioner evidence from Cursor's own engineering team.
- **Scope**: Covers the canvas feature's architecture (React component library, durable artifact model), four internal Cursor use cases (incident response, PR review, eval analysis, autoresearch), and the skills mechanism for teaching agents new canvas types. Does NOT cover: canvas rendering performance, cost or token overhead, canvas API surface for third-party developers, failure modes (what happens when a canvas renders incorrectly or a MCP connection fails), or how canvases handle data refresh/staleness.

## Extracted Claims

### Claim 1: Agents can now produce interactive, durable visual artifacts (canvases) as first-class workspace objects rather than text responses

- **Evidence**: Product description — "With canvases, agents can create dashboards for real-world data as well as custom interfaces with logic and interactivity tailored to your request." Canvases are described as "durable artifacts that live alongside your other tools like the terminal, browser, and source control" in the Agents Window.
- **Confidence**: emerging (vendor-described; the architecture is concrete but not independently verified)
- **Quote**: "In the Agents Window, canvases are durable artifacts that live alongside your other tools like the terminal, browser, and source control."
- **Our assessment**: The key architectural claim here is *durability* and *workspace parity*. Prior agent outputs (markdown, text) are ephemeral chat responses; canvases are objects that persist in the workspace. This is not just a display improvement — it is a change in the ontological status of agent output: agents can now produce things rather than just say things. This matches the pattern in `blog-cursor-self-hosted-cloud-agents.md` (per-session VMs with terminal + browser as workspace primitives) — canvases extend that workspace surface to include interactive data artifacts.

### Claim 2: Canvases use a React-based UI library with first-party components, and agents are instructed to follow data visualization best practices

- **Evidence**: Explicit architecture description: "Cursor renders canvases using a React-based UI library with first-party components like tables, boxes, diagrams, and charts. We gave agents access to existing components in Cursor like diffs and to-do lists, and we also instructed it to follow data visualization best practices."
- **Confidence**: emerging (vendor-described implementation; React component library is a specific technical claim)
- **Quote**: "Cursor renders canvases using a React-based UI library with first-party components like tables, boxes, diagrams, and charts."
- **Our assessment**: Grounding canvases in React and a pre-built component library is a deliberate design choice: it constrains what agents can produce (they work from a palette of first-party components rather than generating arbitrary HTML/CSS) while making canvases predictable and safe. Exposing Cursor-native components (diffs, to-do lists) as canvas building blocks is the key interoperability claim — agents can embed existing IDE elements inside canvases. The "data visualization best practices" instruction in system prompt is a concrete example of how capability is shaped via instruction rather than code constraints.

### Claim 3: A skills mechanism lets practitioners teach agents new canvas types as reusable behaviors, avoiding the need to build and deploy a separate web app

- **Evidence**: Two examples: (1) "You can create skills to teach agents how to create different kinds of canvases. For example, the Docs Canvas skill allows Cursor to generate an interactive architecture diagram of your repo." (2) For eval analysis: "instead, we operationalized it directly with a skill in Cursor" after the team "considered building and deploying a web app to automate this process."
- **Confidence**: emerging (concrete examples from Cursor's own practice; the skill mechanism itself is described but not detailed)
- **Quote**: "instead, we operationalized it directly with a skill in Cursor"
- **Our assessment**: The skills mechanism is the most consequential claim for the guide. It asserts that "write an agent skill that creates a canvas" can substitute for "build and deploy a web app" for data-intensive internal tooling. Cursor's own eval analysis case is the primary evidence: the alternative (a web app) was explicitly considered and rejected in favor of the skill. This is a concrete guide-relevant decision: before building a data dashboard web app, consider whether an agent skill producing a canvas can serve the same purpose with less infrastructure overhead.

### Claim 4: Canvases resolve the information bandwidth problem with MCP-sourced observability data that was previously unworkable as markdown tables

- **Evidence**: Incident response use case: "Before canvases, the agent would represent time-series data in a markdown table, which was hard to interpret and required additional steps to visualize. Now, the agent can create visualizations in a canvas that join data from multiple sources, including local debug files, into a single chart."
- **Confidence**: anecdotal (Cursor's own internal experience; not independently verified)
- **Quote**: "the agent would represent time-series data in a markdown table, which was hard to interpret and required additional steps to visualize"
- **Our assessment**: The markdown-table-for-time-series-data failure mode is a genuine ergonomic problem with current chat-based agents — it is a specific, nameable pain point. The claim is that canvases solve this by making the rendering step native to the agent's output rather than requiring the user to copy data to an external tool. The multi-source join (Datadog + Databricks + Sentry MCPs + local debug files into one chart) is the concrete capability that was previously impossible in a single agent interaction.

### Claim 5: Canvases enable agents to group PR changes logically and prioritize review order, replacing the undifferentiated diff presentation of traditional review tools

- **Evidence**: PR review use case: "Traditional tools present all changes equally, requiring us to figure out what parts of the diff are most important. With canvases, Cursor can logically group changes together, prioritize what's most important for you to review, and present a rich interface for you to explore the change set. It can even write pseudocode representations for tricky algorithms."
- **Confidence**: anecdotal (internal Cursor usage; no comparative study)
- **Quote**: "Traditional tools present all changes equally, requiring us to figure out what parts of the diff are most important."
- **Our assessment**: The diagnosis is accurate — existing PR review tools (GitHub, GitLab) do not prioritize diff sections; they present changes in file/hunk order. The claim that an agent can logically group changes and assign review priority is plausible given sufficient context. The "pseudocode for tricky algorithms" detail is novel: an agent can generate explanatory content *alongside* the original diff, reducing the reviewer's burden of understanding unfamiliar code. This is a direct implementation of the verification-as-bottleneck thesis from `blog-addyosmani-code-agent-orchestra.md` Claim 5 — the agent is acting as a reviewer assistant, not just a diff display.

### Claim 6: Cursor used a canvas skill to replace what would have been a dedicated web app for eval analysis, enabling two model releases with materially less effort

- **Evidence**: Eval analysis use case: "Previously, engineers had to inspect request IDs one at a time to identify patterns. We considered building and deploying a web app to automate this process, but instead, we operationalized it directly with a skill in Cursor. The skill allows agents to read all of the rollouts in an eval, group failures, and build a canvas for investigating eval failures and cluster failure modes. This allows us to identify harness bugs that were hidden before, and recently helped us release two new models in Cursor with far less effort."
- **Confidence**: anecdotal (Cursor's internal engineering team; named outcome but no quantification)
- **Quote**: "recently helped us release two new models in Cursor with far less effort"
- **Our assessment**: This is the most analytically important claim in the source for the guide. The specific decision point — "web app vs. agent skill + canvas" — is extractable as a design decision heuristic. The business outcome (two model releases with less effort) is a concrete, if anecdotal, validation. "Identify harness bugs that were hidden before" is worth noting: the canvas grouping of failure modes surfaced insights that per-request inspection missed, suggesting the visualization itself (not just automation) generated new analytical value.

### Claim 7: Canvas enables autoresearch agents to visualize hypothesis progress in real time, enabling check-in without interrupting execution

- **Evidence**: Autoresearch use case: "With canvases, the agent can visualize its research progress while running experiments, enabling the user to check on progress and see the hypothesis the agent is currently testing."
- **Confidence**: anecdotal (described as an experiment, not a deployed workflow)
- **Quote**: "enabling the user to check on progress and see the hypothesis the agent is currently testing"
- **Our assessment**: The long-running agent observability use case is directly relevant to the `blog-ghaw-agent-observability.md` discussion of monitoring autonomous agents. The specific pattern here — agent writes to a canvas as a continuous progress log, user reads canvas to check status without sending a message — is a concrete alternative to polling or structured logging. It is asynchronous human-agent communication mediated by a durable artifact. The autoresearch framing connects to `blog-cursor-multi-agent-kernels.md`, where a similar optimization loop ran for 3 weeks autonomously.

### Claim 8: Canvases are part of a broader "information bandwidth" initiative that also includes Design Mode and upgraded voice input

- **Evidence**: "Recent improvements like Design Mode and upgraded voice input are all part of our effort to increase information bandwidth. We want to remove friction in human-agent collaboration and make it easier to express your intent beyond plain text."
- **Confidence**: emerging (product strategy framing from vendor; internally consistent)
- **Quote**: "We want to remove friction in human-agent collaboration and make it easier to express your intent beyond plain text."
- **Our assessment**: The "information bandwidth" framing is the guiding concept behind this feature and several others. It names a structural problem: plain text is a low-bandwidth communication channel between humans and agents, in both directions (user → agent intent, agent → user output). Canvases address the output direction; voice input and Design Mode address the input direction. This is a coherent product strategy thesis, not just a feature announcement. For the guide: "information bandwidth" is a useful vocabulary term for the problem canvases solve.

### Claim 9: Canvas workflows with MCP data joins enable insights agents would miss with text-only output

- **Evidence**: Incident response use case: "Datadog, Databricks, and Sentry MCPs in Cursor have enabled us to dive into observability data with agents, which often find insights that we'd miss on our own."
- **Confidence**: anecdotal (Cursor's internal experience; "often find insights we'd miss" is qualitative)
- **Quote**: "which often find insights that we'd miss on our own"
- **Our assessment**: The claim that canvas + MCP data joins produces insights missed by human review is significant but under-evidenced. It is consistent with the multi-agent kernel work in `blog-cursor-multi-agent-kernels.md` (agents discovering non-obvious optimizations) but on a much shorter time scale. The specific mechanism — joining time-series data from three separate observability tools into a single visualization — plausibly enables pattern-spotting that per-tool inspection misses. Treat as directionally credible but not yet validated at the level needed for guide citation without hedging.

## Concrete Artifacts

### Canvas Architecture Overview

```
Cursor Canvas System (Cursor 3.1, April 2026)

Rendering:
  - React-based UI library
  - First-party components: tables, boxes, diagrams, charts
  - Native Cursor components exposed as canvas elements: diffs, to-do lists
  - Agents instructed to follow data visualization best practices

Workspace integration:
  - Durable artifacts (persist in workspace, not ephemeral chat messages)
  - Lives alongside: terminal, browser, source control in Agents Window

Skills mechanism:
  - Practitioners create skills to teach agents new canvas types
  - Skill = pre-configured canvas template + agent instructions
  - Example: Docs Canvas skill → interactive architecture diagram of repo
```

### Cursor's Four Internal Canvas Use Cases

```
1. Incident Response Dashboard
   MCPs: Datadog (metrics), Databricks (data), Sentry (errors) + local debug files
   Before: Agent returned time-series data as markdown table (hard to interpret,
           required external steps to visualize)
   After:  Agent joins multi-source data into a single canvas chart in-context
   Key capability: Multi-MCP data join → single visualization, no context switch

2. PR Review Interface
   Before: Traditional tools present all changes equally; reviewer decides priority
   After:  Agent logically groups changes, prioritizes review order, writes
           pseudocode for tricky algorithms, provides rich exploration interface
   Key capability: Agent acts as review assistant, not just diff renderer

3. Eval Analysis (replaces a web app)
   Before: Engineers inspected request IDs one at a time; considered building a
           dedicated web app
   After:  Agent skill reads all rollouts, groups failures, clusters failure modes
           into an investigation canvas; no web app deployed
   Business outcome: Identified hidden harness bugs; released 2 new Cursor models
                     with "far less effort"
   Key pattern: Agent skill + canvas = viable substitute for internal data tooling

4. Autoresearch Progress Visualization
   Use case: Long-running optimization experiments (see blog-cursor-multi-agent-kernels.md)
   After:  Agent writes research progress to canvas as it runs experiments
   Key capability: Asynchronous check-in without interrupting agent execution;
                   user sees current hypothesis being tested
```

### Information Bandwidth Framework

```
Cursor's "information bandwidth" framing (Cursor 3.1 blog, April 2026):

Problem: Plain text / markdown is a low-bandwidth human-agent communication channel
         in both directions:
   - User → Agent: limited by text expression of intent
   - Agent → User: limited by text/markdown rendering of results

Solutions by direction:
   Agent → User output bandwidth:
     - Canvases: React-based interactive dashboards as durable workspace artifacts
   User → Agent input bandwidth:
     - Design Mode (referenced but not detailed in this post)
     - Upgraded voice input (referenced but not detailed)

Goal: "Remove friction in human-agent collaboration and make it easier to express
      your intent beyond plain text."
```

## Cross-References

- **Corroborates**: `blog-cursor-self-hosted-cloud-agents.md` — that source documents Cursor's Agents Window architecture (terminal, browser, desktop environment as workspace primitives). Canvases extend the Agents Window surface to include interactive data artifacts. The per-session VM isolation pattern from that source (each agent session gets a dedicated, full-stack environment) is the infrastructure layer that makes durable canvas artifacts meaningful — they persist in a stable workspace.

- **Corroborates**: `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("The bottleneck has shifted from code generation to verification") — the PR review canvas use case is a direct implementation of agent-assisted verification. The canvas groups and prioritizes changes to reduce human review friction, exactly the "verification bottleneck" pattern Osmani names. The pseudocode generation for tricky algorithms is a concrete technique for lowering the review burden.

- **Corroborates**: `blog-cursor-multi-agent-kernels.md` Claim 4 (agents independently calling the benchmarking pipeline during runs) — the autoresearch canvas use case describes the same autonomous experiment loop. The canvas is the observability mechanism that lets users check on that loop without interrupting it. Both sources describe long-running autonomous agent loops where the human's role shifts from directing to monitoring.

- **Corroborates**: `blog-ghaw-agent-observability.md` — the autoresearch canvas is a concrete implementation of agent observability: a durable artifact the agent writes to during execution that the user reads asynchronously to check status. This is a different implementation of the same need (monitoring long-running agents) that observability tooling addresses externally.

- **Extends**: `blog-cursor-security-agents.md` and `blog-cursor-multi-agent-kernels.md` — those sources document Cursor's MCP-based agent fleet patterns. This source shows MCP data flowing *into* canvas visualizations (Datadog + Databricks + Sentry → incident dashboard), demonstrating that MCP + canvas is a composable pattern: MCPs provide the data layer, canvases provide the presentation layer.

- **Extends**: `blog-addyosmani-code-agent-orchestra.md` — Osmani's "information bandwidth" concern is implicit throughout that post (rich agent output doesn't fit in chat). This source makes the concept explicit and names it. The guide can cite Osmani as evidence that the problem exists and this source as one concrete solution Cursor chose.

- **Contradicts**: None identified. The canvas feature is additive; it does not contradict any existing source's claims. The "skills as a substitute for web apps" pattern in Claim 3/6 is novel rather than contradictory.

- **Novel**:
  - **Agent-produced interactive visual artifacts as durable workspace objects**: No existing source note documents agents producing persistent, interactive artifacts (as opposed to text responses). This is a new ontological category: agents can now *make things* in the workspace, not just *say things*.
  - **Skills mechanism for canvas types**: Teaching agents new canvas types via skills (pre-configured canvas templates) is not documented elsewhere. It is a form of specialization injection — composing new agent capability by teaching it a new output format.
  - **"Information bandwidth" as a named design goal**: The explicit framing of human-agent collaboration friction as an information bandwidth problem, with canvases as the output-direction solution, is new vocabulary for the guide.
  - **Agent skill as substitute for internal web app**: The decision pattern (should we build a web app, or operationalize this as a canvas skill?) is extractable as a design heuristic and not documented in any existing source note.
  - **Multi-MCP data join into a single visualization**: The incident response use case (Datadog + Databricks + Sentry → one canvas chart) demonstrates a cross-tool synthesis pattern in agent output that text rendering cannot replicate.

## Guide Impact

- **Chapter 01 (Daily Workflows — agent output and information consumption)**: Add the canvas model as a concrete example of the next evolution in agent output formats. After explaining the current state (agents return text/markdown), introduce the canvas pattern: agents can produce durable, interactive artifacts for data-intensive tasks. Frame the "information bandwidth" concept as the underlying problem canvases address. The PR review canvas use case is directly actionable for developers using Cursor 3.1.

- **Chapter 02 (Harness Engineering — skills and reusable agent behaviors)**: Add the "skills as canvas templates" pattern as a concrete implementation of the broader skills/harness concept. The eval analysis case is the extractable example: rather than building and deploying a web app, Cursor's team wrote a canvas skill. This is a design decision heuristic practitioners can apply: for internal data tooling with a bounded, repeated use case, evaluate whether a canvas skill meets the need before committing to a full web app.

- **Chapter 04 (Context Engineering — MCP data flows and agent output)**: The MCP + canvas pattern (MCPs provide multi-source data, canvas provides presentation) is a concrete composition example. Chapter 04 should describe how MCP tool results can flow into agent-generated visualizations, enabling in-context analytics that previously required external tools. The Datadog/Databricks/Sentry incident dashboard is the canonical example.

- **Chapter 04 (Context Engineering — long-running agent observability)**: The autoresearch canvas (agent writes progress to canvas during execution; user reads asynchronously) is a concrete observability pattern for long-running agents. Add as an alternative to external monitoring: for agents running inside Cursor, a canvas updated by the agent during execution gives the user a persistent status artifact that does not require polling or interrupting the agent.

- **Chapter 05 (Agent UX and human-agent collaboration)**: The "information bandwidth" framing is the organizing concept for a chapter on how agents communicate results to humans. Beyond Cursor-specific canvases, the underlying principle — that rich structured output reduces human cognitive load and improves verification quality — applies broadly. Use canvases as the motivating concrete example; generalize to the principle that agent output format is a first-class design decision.

## Extraction Notes

- Source is a short product announcement blog post (~1,000 words, six sections). It is high on concrete use cases and low on implementation details. The React component library, the skills mechanism, and the MCP data join pattern are named but not technically detailed.
- The four use cases all describe Cursor's own internal workflows, not customer deployments — this is Cursor dogfooding their own product. It is genuine practitioner evidence but from a single organization with a commercial incentive to present the feature favorably.
- Design Mode and upgraded voice input are mentioned as related features in the "information bandwidth" initiative but not described in this post. They would be separate sources if they contain novel claims.
- The blog post does not discuss failure modes, limitations, or cases where the canvas approach was tried and did not work. This is common for product announcements; the guide should hedge claims accordingly.
- Three Prospector triage comments agreed on medium novelty. The canvas-as-artifact pattern (not the React implementation detail) is the novel contribution to the guide's corpus.
