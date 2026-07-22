---
source_url: https://blog.jetbrains.com/air/2026/07/what-s-new-air-gets-more-agents-local-models-and-java-kotlin-code-intelligence/
source_type: blog-post
title: "What's new: Air gets more agents, local models, and Java/Kotlin code intelligence"
author: Vladimir Gromozdin
date_published: 2026-07-21
date_extracted: 2026-07-22
last_checked: 2026-07-22
status: current
confidence_overall: settled
issue: "#2134"
---

# What's new: Air gets more agents, local models, and Java/Kotlin code intelligence

> JetBrains Air's July 21, 2026 release note announces the Agent Client Protocol (ACP,
> co-developed with Zed) as the mechanism letting Air connect to third-party coding agents
> (GitHub Copilot, OpenCode, Pi, Cline) beyond its four bundled agents, plus ACP-mediated
> local-model support via Ollama/LM Studio, Beta IntelliJ-powered Java/Kotlin language
> intelligence inside the agent task/review workflow, Windows Docker task parity with macOS,
> and several agent-run control features (full proposed-edit inspection, Claude context-window
> visibility, an "xhigh" reasoning effort tier, and a macOS sleep-prevention setting).

## Source Context

- **Type**: blog-post (official JetBrains Air blog, published July 21, 2026, 17:56 UTC;
  author Vladimir Gromozdin; product-release-note post, ~750 words, from the trusted feed
  `jetbrains-ai`)
- **Author credibility**: JetBrains staff writing on the official JetBrains Air blog about
  a feature release for JetBrains' own product. Authoritative for: what shipped, which
  product surface it lives in (Air specifically, not JetBrains AI Assistant/AI Chat or the
  GitHub Copilot plugin — three separate JetBrains-adjacent surfaces already documented
  elsewhere in this corpus), and the stated Beta/GA status of each feature. Not
  independently verified: no benchmark, screenshot walkthrough, or third-party account of
  actually using ACP-connected third-party agents in Air is given; this is a vendor
  release-note post, not a hands-on review.
- **Scope**: Covers six shipped features in the July 21, 2026 Air release — ACP-based
  multi-agent connectivity, the harness-vs-model framing for choosing an ACP agent,
  ACP-mediated local-model support, Beta Java/Kotlin language intelligence, Windows Docker
  task parity, and four "more control" features (proposed-edit inspection, Claude
  context-window visibility, an "xhigh" effort level, macOS sleep prevention). Does NOT
  cover: which specific ACP-compatible agents beyond the four named (Copilot, OpenCode, Pi,
  Cline) are supported, the technical mechanics of the ACP protocol itself (no spec link is
  given), pricing or plan-tier gating for any feature, or a walkthrough of the `acp.json`
  configuration files the post references but does not show.

## Extracted Claims

### Claim 1: Air can now connect to GitHub Copilot, OpenCode, Pi, Cline, and other ACP-compatible agents, extending a parallel-workspace/review workflow previously limited to Air's four bundled agents (Claude, Codex, Gemini CLI, Junie)
- **Evidence**: Framing statement in the article's opening summary and the "Bring your own agents and harnesses" section, naming the four bundled agents by contrast with the newly reachable third-party set.
- **Confidence**: settled (direct statement of a shipped product capability, not labeled preview)
- **Quote**: "Air gives coding agents separate workspaces where they can run tasks in parallel. You can then review each agent’s changes before they reach your codebase. Until now, this workflow was limited to the agents bundled with Air, including Claude, Codex, Gemini CLI, and Junie. You can now connect other supported agents and use them throughout the same task and review workflow."
- **Our assessment**: This establishes Air's parallel-workspace-plus-review workflow as agent-agnostic infrastructure that any ACP-compatible agent can now plug into, not a feature tied to a fixed agent roster. The four originally-bundled agents (Claude, Codex, Gemini CLI, Junie) were previously the entire addressable set; ACP support is what expands that set to include competitor-vendor agents (Copilot) and independent harnesses (OpenCode, Pi, Cline) without JetBrains building a bespoke integration for each.

### Claim 2: The multi-agent connectivity is made possible by the Agent Client Protocol (ACP), an open protocol jointly developed by JetBrains and Zed, which gives agents and development environments a shared communication mechanism without requiring a bespoke per-agent integration
- **Evidence**: Direct statement of the underlying mechanism in the "Bring your own agents and harnesses" section.
- **Confidence**: settled (direct statement of protocol authorship and function)
- **Quote**: "This is made possible by the Agent Client Protocol (ACP), an open protocol developed by JetBrains and Zed. ACP gives coding agents and development environments a shared way to communicate. When an agent supports ACP, Air can connect it to its workspace without requiring a separate integration built specifically for that agent."
- **Our assessment**: This is a cross-vendor interoperability claim: JetBrains explicitly names Zed (a competing IDE vendor) as ACP's co-developer, and frames ACP's value as eliminating custom per-agent integration work. This mirrors the "any ACP-compatible agent" language already documented for JetBrains AI Assistant's own agent picker (see Cross-References) — the same protocol now underlies at least two separate JetBrains products (AI Assistant and Air).

### Claim 3: Air can connect to the GitHub Copilot CLI through its ACP server mode, letting practitioners use their company-managed Copilot access inside Air — solving the previously-blocking case where a company approved only Copilot and could not use Air at all
- **Evidence**: Explicit problem/solution framing in the "Use your company's approved coding agent in Air" section.
- **Confidence**: settled (direct statement of shipped capability and the specific organizational problem it addresses)
- **Quote**: "Air can now connect to the GitHub Copilot CLI through its ACP server mode. This lets you use your company-managed Copilot access in Air: The Copilot CLI runs the coding agent and provides access to the available models, while Air adds parallel workspaces and its review workflow."
- **Our assessment**: This names the precise organizational adoption blocker the feature removes: "Previously, if your company had only approved GitHub Copilot, that meant you could not use Air because Air could not connect to the Copilot access your company provided." The division of labor is explicit and reusable as a general pattern for evaluating any ACP integration: the connected agent (here, Copilot CLI) owns model access and task execution; Air contributes only the parallel-workspace and review-workflow layer on top, not the agent or model itself.

### Claim 4: A coding agent's harness (the software that gathers context, calls tools, manages the task, and turns model responses into code changes) is presented as a choice independent of model choice — Air lets practitioners pick an ACP harness such as OpenCode or Pi and configure it with whichever model or provider that harness supports
- **Evidence**: Explicit model-vs-harness distinction in the "Use the agent harness you prefer" section, followed by two concrete pairing examples.
- **Confidence**: settled (direct architectural framing and concrete usage examples from the vendor)
- **Quote**: "A model is only one part of a coding agent. The harness is the software around it: It gathers context, calls tools, manages the task, and turns the model’s responses into code changes. Different harnesses approach this workflow differently and support different model providers."
- **Quote**: "Air can now connect to supported ACP agents such as OpenCode and Pi. You choose the harness and configure it with a model or provider it supports. For example, you could use OpenCode with your preferred cloud provider or Pi with a local model."
- **Our assessment**: This is a reusable conceptual framing for the guide independent of Air specifically: "harness" and "model" are named as two separable axes of choice, and ACP is the mechanism that lets a workspace tool like Air remain harness-agnostic. The two paired examples (OpenCode + cloud provider; Pi + local model) also foreshadow Claim 5 — harness choice and local-vs-cloud model choice are shown as orthogonal decisions a practitioner can mix independently.

### Claim 5: Local-model support was one of Air's most-requested features; practitioners can now run a model on their own computer via a local model runner such as Ollama or LM Studio, with an ACP-compatible coding agent connecting to that local model and Air connecting to that agent, enabling offline development
- **Evidence**: Explicit statement of demand and mechanism in the "Work with local models" section.
- **Confidence**: settled (direct statement of shipped capability and its user-demand rationale)
- **Quote**: "Local-model support was one of our most requested additions. You can now use a model running on your computer through a local model runner such as Ollama or LM Studio. An ACP-compatible coding agent connects to the local model, and Air connects to that agent."
- **Quote**: "This lets you develop with a model that runs offline and choose the one that best fits your codebase, task, or environment."
- **Our assessment**: The connection chain is explicit and three layers deep: local model runner (Ollama/LM Studio) → ACP-compatible agent → Air. Air itself does not talk to the local model directly; it only talks to the ACP agent, which is itself responsible for talking to the local runner. This is a concrete architectural detail worth preserving for the guide: "local model support" in an IDE-adjacent tool like Air does not necessarily mean the tool has its own local-inference client — it can mean the tool merely trusts an ACP-compatible agent to handle that connection.

### Claim 6: Air now supports Java and Kotlin language intelligence, including mixed Java/Kotlin projects, powered by the IntelliJ IDEA code engine, currently in Beta
- **Evidence**: Explicit feature and status statement opening the "Navigate Java and Kotlin projects and catch errors" section.
- **Confidence**: emerging (explicitly labeled Beta by the source)
- **Quote**: "Air now supports Java and Kotlin language intelligence, including mixed Java/Kotlin projects, powered by the IntelliJ IDEA code engine (in Beta)."
- **Our assessment**: This brings IntelliJ's own code-navigation engine into Air's task-authoring and review surfaces specifically — not just the IDE proper. It is scoped to Java/Kotlin only in this release; no other language is named as receiving the same treatment.

### Claim 7: Java/Kotlin language intelligence in Air serves two distinct moments in the agent workflow — before a task (jump to definitions, find usages, search symbols, follow code paths, to give the agent more precise context) and after a task (Air highlights errors and warnings in the affected code so practitioners can inspect problems before accepting changes, without opening the IDE or waiting for a compile failure)
- **Evidence**: Two consecutive paragraphs in the "Navigate Java and Kotlin projects and catch errors" section, one describing pre-task navigation and one describing post-task error highlighting.
- **Confidence**: settled (direct, specific description of both workflow moments)
- **Quote**: "While creating a task, you can jump to definitions, find usages, search for symbols, and follow code paths directly in Air. This helps you understand the code the agent will touch and give it more precise context."
- **Quote**: "After the agent finishes, Air highlights errors and warnings in the affected Java and Kotlin code. You can inspect problems before accepting the changes, without opening your IDE or waiting for the code to fail during compilation."
- **Our assessment**: The "before" use (navigation to sharpen the prompt/context a practitioner gives the agent) and the "after" use (catching compiler-detectable errors before accepting an agent's diff) are functionally different applications of the same underlying IntelliJ code-intelligence engine. The "after" use in particular is a concrete instance of shifting error detection earlier than a build/CI step — catching type or reference errors at review time rather than after the change is already merged and compiled.

### Claim 8: Air can now run agent tasks in Docker containers on Windows, matching functionality that already existed on macOS, with Docker Desktop required
- **Evidence**: Direct statement in the "Docker tasks now run on Windows" section, naming the isolation use case and the prerequisite.
- **Confidence**: settled (direct statement of shipped capability and its explicit prerequisite)
- **Quote**: "Air can now run agent tasks in Docker containers on Windows, matching the existing macOS support. Use Docker tasks when you want dependencies and agent commands to run in an isolated container instead of directly on your machine. Docker Desktop is required."
- **Our assessment**: This is a platform-parity claim (Windows catching up to macOS) rather than a new capability class. The stated use case — isolating dependencies and agent commands in a container "instead of directly on your machine" — frames Docker tasks as Air's isolation/sandboxing option, conceptually adjacent to the local-vs-cloud sandbox distinction already documented for the separate GitHub Copilot JetBrains plugin (see Cross-References), though this source does not use the word "sandbox" and does not compare the two.

### Claim 9: Air now shows Claude Agent's context-window usage and token counts for a given task, intended to help practitioners recognize when a long task is approaching its context limit and decide whether to finish or start a new task
- **Evidence**: Direct statement in the "More control during agent runs" section, one of four bullet-style control features.
- **Confidence**: settled (direct statement of a shipped visibility feature and its stated purpose)
- **Quote**: "See how much context Claude has used for a given task. Air now shows context-window usage and token counts for Claude Agent. This helps you recognize when a long task is approaching its context limit and decide whether to finish the task or start a new one."
- **Our assessment**: This feature is explicitly scoped to Claude Agent only in this source — no other bundled or ACP-connected agent is named as receiving the same context-usage display. The stated purpose (deciding whether to finish or restart a task as context fills up) is a practical operational decision point that context-window transparency enables directly.

### Claim 10: Claude Fable, Opus, and Sonnet 5 now support an "xhigh" effort level in Air for tasks that need more reasoning
- **Evidence**: Direct statement in the "More control during agent runs" section.
- **Confidence**: settled (direct statement of a shipped model-configuration option, naming the specific model family it applies to)
- **Quote**: "Adjust the effort level for demanding tasks. Claude Fable, Opus, and Sonnet 5 now support an “xhigh” effort level for when a task needs more reasoning."
- **Our assessment**: This is scoped explicitly to the named Claude model family (Fable, Opus, Sonnet 5) inside Air; the source does not state whether "xhigh" is an Air-specific UI exposing an existing Anthropic API parameter or a new reasoning tier introduced with this release. No further mechanism detail (cost or latency impact of "xhigh" versus lower effort levels) is given in this source.

### Claim 11: Air now includes a macOS setting that prevents the computer from sleeping while an agent is working, so long-running tasks continue while the practitioner steps away
- **Evidence**: Direct statement in the "More control during agent runs" section, the fourth control feature listed.
- **Confidence**: settled (direct statement of a shipped, platform-specific setting)
- **Quote**: "Keep your Mac awake during long tasks. Enable the new macOS setting to prevent your computer from sleeping while an agent is working, and ensure your task continues while you step away."
- **Our assessment**: A small but practically important operational detail for anyone running long, unattended agent tasks locally on macOS — without this setting, a sleeping machine would presumably interrupt or stall an in-progress task. The source states this is macOS-specific; no equivalent Windows or Linux setting is mentioned.

## Concrete Artifacts

### Air's ACP connection chain, as described (local models)

```
Local model runner (Ollama or LM Studio, running on the practitioner's machine)
        |
        v
ACP-compatible coding agent (e.g., an agent that supports connecting to a local model)
        |
        v
JetBrains Air (connects to the ACP agent; contributes parallel workspaces + review workflow)

Source: "What's new: Air gets more agents, local models, and Java/Kotlin code
intelligence," JetBrains Air blog, July 21, 2026 (Vladimir Gromozdin).
```

### July 21, 2026 Air release — feature inventory

```
1. ACP multi-agent connectivity
   Newly connectable: GitHub Copilot (via Copilot CLI, ACP server mode), OpenCode, Pi,
   Cline, "other ACP-compatible agents"
   Previously bundled only: Claude, Codex, Gemini CLI, Junie
   Protocol: Agent Client Protocol (ACP), co-developed by JetBrains and Zed

2. Local model support
   Runners named: Ollama, LM Studio
   Mechanism: local runner -> ACP agent -> Air (Air does not connect to the local
   model directly)

3. Java/Kotlin language intelligence (Beta)
   Engine: IntelliJ IDEA code engine
   Pre-task: jump to definitions, find usages, search symbols, follow code paths
   Post-task: highlights errors/warnings in agent-affected code before changes are
   accepted, without opening the IDE or waiting for a compile failure
   Covers mixed Java/Kotlin projects

4. Windows Docker task support
   Matches existing macOS Docker task support
   Requirement: Docker Desktop
   Use case: isolate dependencies/agent commands in a container instead of running
   directly on the host machine

5. More control during agent runs
   - Full proposed-edit inspection before granting permission (Proposed Change tab,
     vs. a short chat snippet)
   - Claude Agent context-window usage + token count display, per task
   - "xhigh" effort level for Claude Fable, Opus, and Sonnet 5
   - macOS setting to prevent sleep during long-running agent tasks

Source: JetBrains Air blog, July 21, 2026.
```

## Cross-References

### Cross-reference verification notes
Claims cited from `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md`,
`blog-jetbrains-codex-recommended-agent.md`, and
`docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` were re-read directly in
those notes before citing (per MINER.md §4b); claim numbers are counted top-to-bottom
in document order as they appear in each cited note.

- **Corroborates**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Claim 1: that note
    documents GitHub Copilot becoming a first-class, natively selectable agent inside
    **JetBrains AI Assistant**'s own agent picker via ACP, on June 30, 2026 ("GitHub
    Copilot is a first-class option in the AI Assistant agent picker"). This source's
    Claims 1–3 corroborate ACP as JetBrains' general-purpose cross-product agent
    interoperability mechanism — the same protocol now also connects Copilot (plus
    OpenCode, Pi, Cline) into **Air**, a separate JetBrains product from AI Assistant.
    Together the two sources establish ACP is being used to connect third-party agents
    into at least two distinct JetBrains-built surfaces, not a single-product
    integration.
  - `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` Claim 1: that note
    documents the GitHub Copilot JetBrains *plugin* expanding BYOK to arbitrary
    OpenAI-compatible custom endpoints on July 14, 2026, closing a prior gap where
    JetBrains BYOK was limited to named providers. This source's Claim 5 (Ollama/LM
    Studio local-model support in Air, via an ACP agent) corroborates a parallel trend
    across two separate JetBrains-adjacent products — both expanding beyond a
    fixed/named model-provider list toward practitioner-supplied or self-hosted model
    access — though the two sources use different mechanisms (custom OpenAI-compatible
    endpoint configuration vs. ACP-agent-mediated local runner connection) and should
    not be treated as the same integration path.

- **Contradicts**: None identified. No existing corpus note makes a claim about Air,
  ACP-based multi-agent connectivity, or local-model support in Air that this source
  opposes. No contradiction issue filed.

- **Extends**:
  - `docs-github-copilot-jetbrains-ai-assistant-picker-june2026.md` Concrete Artifacts
    → "JetBrains Copilot Surfaces — Product Map": that note's product map names two
    JetBrains-facing Copilot surfaces (the Copilot plugin, and JetBrains AI Assistant).
    This source establishes a third, distinct surface — **JetBrains Air**, a separate
    parallel-workspace/review product — that is also now ACP-connectable to Copilot
    (Claim 3) alongside OpenCode, Pi, and Cline (Claim 1). The guide's inventory of
    JetBrains AI product surfaces should be updated to include Air as a third,
    independently evolving integration point, distinct from both the Copilot plugin and
    AI Assistant.
  - `blog-jetbrains-codex-recommended-agent.md` Claim 9: that note documents JetBrains
    AI Chat's "recommended agent" feature, where Codex is the default but users "can
    switch to Junie, Claude Agent, or other ACP-compatible agents at any time." This
    source's Claim 1 gives concrete texture to what "other ACP-compatible agents" can
    mean in practice — Copilot, OpenCode, Pi, Cline — though this source describes Air
    specifically, not the AI Chat/AI Assistant surface that note covers. Whether Air and
    AI Chat share the same underlying ACP-agent roster, or maintain independent lists, is
    not established by either source and is flagged here as an open question.

- **Novel**:
  - **ACP-mediated local-model support for a JetBrains agentic-development product**
    (Claim 5): no prior corpus source documents a local model runner (Ollama, LM Studio)
    being connected into a JetBrains product through an intermediary ACP agent, as
    opposed to a direct BYOK/custom-endpoint configuration.
  - **Explicit harness-vs-model separation as a stated design framing** (Claim 4): "A
    model is only one part of a coding agent... different harnesses approach this
    workflow differently" is a clearer, more explicit statement of harness/model
    independence than prior corpus sources, which document harness or model choice
    separately but do not name the distinction as a deliberate two-axis design decision.
  - **IntelliJ-powered Java/Kotlin language intelligence inside an agent task/review
    workflow specifically** (Claims 6–7): prior corpus JetBrains sources document IDE
    features or agent-picker/model-selection features, but none document IDE-grade
    code-navigation and post-task error highlighting being surfaced inside a
    parallel-workspace agent-review tool (as opposed to the IDE proper).
  - **Per-task Claude context-window/token visibility inside Air specifically** (Claim
    9): this is the first corpus source documenting this feature for Air; it is scoped
    explicitly to Claude Agent only.

## Guide Impact

- **Chapter 06 (Agent Orchestration)**: Add Air's ACP-based multi-agent connectivity
  (Claim 1) and the explicit harness-vs-model framing (Claim 4) as a concrete example of
  a workspace/orchestration tool becoming agent-agnostic infrastructure via an open
  protocol, rather than a fixed-roster tool requiring per-agent integration work. Note
  the "use your company's approved agent" pattern (Claim 3) as a specific organizational
  adoption blocker that ACP connectivity removes — relevant to any guide discussion of
  tool selection under corporate agent-vendor lock-in.

- **Chapter 04 (Model Selection & Local Models)**: Add the three-layer local-model
  connection chain (local runner → ACP agent → workspace tool, Claim 5) as a concrete
  architectural pattern for "local model support" claims generally: a tool advertising
  local-model support may not talk to the local runner directly, and practitioners
  evaluating such claims should check which layer actually owns the connection. Note
  this is the first corpus documentation of this specific chain for a JetBrains product;
  pair with `docs-github-copilot-jetbrains-byok-sandboxing-july2026.md` Claim 1 (custom
  OpenAI-compatible endpoints) as a contrasting, non-ACP-mediated mechanism for reaching
  self-hosted or local models in a sibling JetBrains-adjacent product.

- **Chapter 05 (IDE-Native Development)**: Add the pre-task/post-task Java/Kotlin
  language-intelligence pattern (Claims 6–7) as a concrete illustration of moving
  compiler-grade error detection earlier in the agent review loop — catching type/
  reference errors when reviewing a proposed diff, before it is accepted, rather than
  after a build or CI run. Note the Beta status and Java/Kotlin-only scope; do not
  generalize to other languages without further source evidence.

- **Chapter 02 / Chapter 06 (Cost and Context Management)**: Add per-task Claude
  context-window/token visibility (Claim 9) and the "xhigh" effort level (Claim 10) as
  examples of surfacing cost/context signals directly in an agent-workflow tool's UI, to
  support the operational decision of whether to continue or restart a long-running
  task. Scope explicitly to Claude Agent in Air; do not assume parity with other
  agents/models in the same tool.

## Extraction Notes

1. **WebFetch returned an AI-summarized paraphrase, not verbatim text**: as with several
   prior source notes in this corpus, the first WebFetch call against this URL returned a
   condensed, reworded summary (e.g., collapsing "Air can now connect to the GitHub
   Copilot CLI through its ACP server mode" into "Air can now connect to multiple coding
   agents through the Agent Client Protocol"), unusable for direct quotes per MINER.md
   §2a. To recover verbatim text, the raw HTML was fetched directly via `curl`, `<script>`
   and `<style>` blocks were stripped, and the article body (identified by the `<h1
   id="major-updates">` anchor through the "Subscribe to Air blog updates" footer marker)
   was converted to plain text by hand. All `Quote` fields in this note were copied
   character-for-character from that raw-text extraction, including curly apostrophes
   (’) and curly quotation marks ("xhigh") as they appear in the source's rendered HTML —
   not from either WebFetch pass.
2. **No sub-pages followed**: the only substantive outbound link in the article body
   (beyond the author-profile link, download links, and tag-archive links) is a "setup
   guide for GitHub Copilot, OpenCode, or Cline with a local Ollama model" link, which
   resolves to an X/Twitter post (`x.com/getsome_air/status/...`), not a docs page. Per
   MINER.md §1's "substantive linked page" bar, a social-media post referencing but not
   containing the actual `acp.json` configuration content was not fetched as a
   sub-source. This is flagged as a gap: the article references working `acp.json`
   configurations for GitHub Copilot, OpenCode, and Cline-with-local-Ollama but does not
   show them, and this note could not recover that configuration detail from the linked
   tweet.
3. **Source is a short, single-page release note (~750 words)**: eleven claims were
   extracted, representing essentially all substantive content in the post (six named
   feature sections plus the ACP framing paragraphs). No claim count padding was needed
   or attempted.
4. **No contradictions found**: this source is consistent with every existing JetBrains-
   and Copilot-in-JetBrains-scoped note in the corpus; it documents ACP and local-model
   support for a product (Air) not previously covered. No contradiction issue filed.
5. **Confidence graded "settled" overall**: ten of eleven claims describe features stated
   definitively as shipped, without a preview/Beta qualifier (the source's own framing is
   "gets more agents" — present tense, not "coming soon"). Claim 6 (Java/Kotlin language
   intelligence) is explicitly labeled Beta by the source and graded "emerging"
   individually; this does not pull the overall grade down because it is the only
   qualified claim among eleven, and the qualifier is the source's own explicit label,
   not this note's inference.
