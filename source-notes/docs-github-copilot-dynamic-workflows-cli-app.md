---
source_url: https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app
source_type: docs
title: "Dynamic workflows in Copilot CLI and the Copilot app"
author: GitHub (official changelog)
date_published: 2026-10-01
date_extracted: 2026-10-02
last_checked: 2026-10-02
status: current
confidence_overall: emerging
issue: "#3853"
---

# Dynamic workflows in Copilot CLI and the Copilot app

> GitHub's Oct 1, 2026 changelog announces public-preview "dynamic workflows" (code-defined orchestration of agents and automated steps) in Copilot CLI, the Copilot app, and the Copilot SDK, explicitly positioned as the deterministic counterpart to prompt-driven `/fleet` delegation.

## Source Context

- **Type**: docs (GitHub official product changelog, "2 minute read").
- **Author credibility**: GitHub's Copilot team; authoritative for what the feature is, where it is available, and its preview status. No metrics, benchmarks, or code samples appear on the page.
- **Scope**: Definition, capability list, six candidate use cases, and getting-started steps. Details are deferred to GitHub docs ("Creating a dynamic workflow"), which this note did not read.

## Extracted Claims

### Claim 1: A dynamic workflow is a program that fixes the steps and the points of agent involvement in code, leaving agents only the analysis/judgment parts
- **Evidence**: Vendor definition; one illustrative example (service incident investigation).
- **Confidence**: emerging
- **Quote**: "The steps, when to involve agents, and how to use their results are all defined in code, while agents handle the parts that need analysis or judgment."
- **Our assessment**: Same architectural split as Google ADK 2.0 (deterministic graph, narrow LLM nodes) and Claude Code dynamic workflows. Three major vendors converging on "code owns control flow, agents own judgment" is the real signal; this page supplies no evidence it works better.

### Claim 2: The main value proposition is reliability and observability for complex multi-agent work, with repeatable execution
- **Evidence**: Vendor assertion, plus the incident-investigation example.
- **Confidence**: anecdotal
- **Quote**: "These let you define an orchestration in code to get the reliability and observability that complex, multi-agent work demands."
- **Our assessment**: Plausible by construction (fixed steps), but no measurements. Note the claimed observability is not described (no trace/telemetry details).

### Claim 3: Workflows are distinct from `/fleet`: fleet delegates and coordinates subagents, a workflow executes a process defined in code
- **Evidence**: Explicit contrast in the post.
- **Confidence**: emerging
- **Quote**: "a dynamic workflow carries out a process defined in code"
- **Our assessment**: Useful taxonomy: model-orchestrated (fleet) vs code-orchestrated (workflow) multi-agent. Maps to the guide's autonomy-vs-determinism decision.

### Claim 4: Workflows can run commands/tools/services, parallelize independent tasks, pass structured results between stages, and have subagents verify each other
- **Evidence**: Bulleted capability list.
- **Confidence**: emerging
- **Quote**: "Have subagents verify each other’s findings."
- **Our assessment**: Cross-agent verification and structured stage hand-off are the same patterns as Claude's verification-before-return step. Structured intermediate results are a quiet but important design point.

### Claim 5: Workflows support human checkpoints: pause for review, ask for input, and resume later
- **Evidence**: Capability list plus use case of pausing a long, expensive run.
- **Confidence**: emerging
- **Quote**: "Pause at a checkpoint so you can review results and resume when you’re ready."
- **Our assessment**: Human-in-the-loop as a first-class workflow primitive rather than a prompt convention. Parallels Claude's resumable progress (Claude note Claim 7).

### Claim 6: Workflows live inside a Copilot extension, and can be authored by hand or written by Copilot using built-in authoring guidance
- **Evidence**: Vendor description.
- **Confidence**: emerging
- **Quote**: "The program itself lives inside a GitHub Copilot extension, which means it has access to Copilot’s powerful extensibility APIs."
- **Our assessment**: Differs from Claude, where the model writes the orchestration script ad hoc; here the workflow is a reusable, named artifact ("Ask 'What dynamic workflows are available?'"). Reusability is the emphasised use.

### Claim 7: Recommended use is for reusable processes or tasks needing stages, checks, or limits; plain chat suffices for quick/simple work
- **Evidence**: Six enumerated examples (release checks with review pause; parallel PR file review; dual-model agreement on unresolved review comments; codebase-wide sweeps; research→plan→implement; long pause/resume runs).
- **Confidence**: emerging
- **Quote**: "For a quick answer or a simple change, a normal prompt in the standard chat mode is usually sufficient."
- **Our assessment**: Sensible decision rule. The dual-model-agreement example (report only when both agree) is a concrete precision-over-recall verification pattern.

### Claim 8: Availability: public preview on all Copilot plans; always on in the Copilot app; CLI requires experimental mode
- **Evidence**: Getting-started section.
- **Confidence**: settled
- **Quote**: "Dynamic workflows are in public preview and subject to change."
- **Our assessment**: Contrast with Claude's Max/Team/Enterprise-only research preview. Guide advice should flag preview/instability.

## Concrete Artifacts

```
Source: GitHub changelog, Oct 1, 2026 ("Get started")
- Copilot app: always available, no setup.
- Copilot CLI: run with --experimental, or /experimental on in an interactive session; update with /update.
- Ask Copilot to create a workflow; ask "What dynamic workflows are available?"
- Feedback: /feedback in Copilot CLI.
Example use case (source): "Using code to find unresolved review comments on merged pull requests, then asking two models whether the comments still matter. The workflow’s code only reports findings when both agree."
```

## Cross-References

- **Corroborates**: `blog-google-adk-2-0-deterministic-workflows.md` Claim 2 and Claim 10 (use deterministic code when the process can be mapped in advance; agents for judgment) and Claim 6 (code-level routing). `blog-anthropic-dynamic-workflows-claude-code.md` Claim 3 (verification before return) and Claim 7 (resumable progress).
- **Contradicts**: None filed. Mild difference in authorship model (Copilot: reusable extension-hosted program; Claude Claim 2: model generates the script per task) is a design variation, not a contradiction.
- **Extends**: `docs-github-copilot-cli-sdk-session-credit-limits.md` and `docs-github-copilot-agent-plugins-1-0.md` (Copilot CLI/SDK extensibility surface); `docs-ghaw-copilot-sdk-driver-specification.md` (SDK-driven agents).
- **Novel**: The explicit fleet-vs-workflow split within one product, and dual-model-agreement filtering as a documented workflow example.

## Guide Impact

- **Chapter 03**: Add GitHub Copilot as a third vendor (with Anthropic and Google ADK) shipping code-defined multi-agent orchestration, and cite the `/fleet` vs workflow distinction as an example of model-orchestrated vs code-orchestrated delegation.
- **Chapter 05**: Cite the use-case list as examples of when to promote a repeated prompt into a reusable workflow, and the pause/resume checkpoint as a cost-control pattern.
- **Chapter 01**: Note preview status and all-plans availability in the tooling landscape; avoid effectiveness claims, as the source has none.

## Extraction Notes

- Read the full changelog page. The "Unlike /fleet" sentence is split across inline code formatting in the page text, so Claim 3's quote is a contiguous fragment; the full sentence reads, in the source, "Unlike `/fleet`, where Copilot delegates work to subagents and coordinates their work in parallel, a dynamic workflow carries out a process defined in code."
- Linked docs ("Creating a dynamic workflow") were not followed; source is thin on specifics, hence `emerging`.
