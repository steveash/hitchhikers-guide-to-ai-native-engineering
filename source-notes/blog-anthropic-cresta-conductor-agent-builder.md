---
source_url: https://claude.com/blog/how-cresta-turned-cx-expertise-into-an-agent-builder-on-the-claude-agent-sdk
source_type: blog-post
title: "How Cresta turned CX expertise into an agent builder on the Claude Agent SDK"
author: Anthropic (Claude blog, "How startups build with Claude" series)
date_published: 2026-10-05
date_extracted: 2026-10-06
last_checked: 2026-10-06
status: current
confidence_overall: anecdotal
issue: "#3924"
---

# How Cresta turned CX expertise into an agent builder on the Claude Agent SDK

> First-party Anthropic case study of Cresta's Conductor, a meta-agent built on the Claude Agent SDK that builds and improves customer-experience agents, contributing a four-dimension evaluation rubric for agent builders, a rerun-on-model-upgrade safety net, and a "harden only the deterministic-critical paths" design heuristic.

## Source Context

- **Type**: blog-post (vendor case study, claude.com, 2026-10-05, ~5 min read)
- **Author credibility**: Published by Anthropic, quoting Cresta's Engineering Lead for Conductor (Renjie Li) and VP of Engineering (Xiangru Chen). It is a promotional customer story: the sole quantitative result ("roughly in half" deployment time) is self-reported by Cresta, with no baseline or methodology. Architectural descriptions are first-hand but high-level.
- **Scope**: Covers Conductor's purpose, its use of the Agent SDK as a harness, the flexible-vs-deterministic design question, Cresta's evaluation rubric, and four closing best practices. Does NOT cover: prompts, code, skill file formats, how the meta-agent is orchestrated internally, model versions currently used, costs, or failure modes.

## Extracted Claims

### Claim 1: Cresta uses the Claude Agent SDK as a general-purpose harness beneath a domain-specific control plane
- **Evidence**: Architecture description; Cresta layers CX workflows, tools and domain context over the SDK. No code shown.
- **Confidence**: anecdotal
- **Quote**: "The Claude Agent SDK sits beneath Conductor as a general-purpose execution harness."
- **Our assessment**: Credible and consistent with the "harness plus domain layer" split. The useful point is the division of labour: SDK for generic gather-context/call-tools/run-code, product team for data and domain logic.

### Claim 2: The same agentic dev harness used interactively (Claude Code) can be reused programmatically via the SDK to build agents inside a product
- **Evidence**: Engineering lead's account of internal use of Claude Code, then the SDK.
- **Confidence**: anecdotal
- **Quote**: "The Claude Agent SDK gave us a way to use that same agentic development harness programmatically."
- **Our assessment**: A concrete "dev tool to product feature" path. Plausible; single-company anecdote.

### Claim 3: A meta-agent that captures builders' proven patterns forms a "knowledge flywheel"
- **Evidence**: Description only: builders convert lessons from an agent build into a reusable memory artifact (patterns, business rules, evaluation approaches) and share it as a skill with the team.
- **Confidence**: anecdotal
- **Quote**: "This creates a knowledge flywheel that makes future development faster and more consistent."
- **Our assessment**: Interesting use of skills as the team-sharing unit for build learnings. The flywheel's effect is asserted, not measured.

### Claim 4: The hard design question is where an agent stays flexible versus where it needs explicit business rules
- **Evidence**: Engineering-lead quote tied to regulated-industry needs.
- **Confidence**: anecdotal
- **Quote**: "You don't want to go too deterministic, otherwise you create a giant decision tree trying to map out every possible branch… but there are enterprise-critical workflows that you need to make sure work all the time, especially for highly regulated industries with low risk tolerance,"
- **Our assessment**: Sensible and widely shared. The distinctive element is using historical conversations to decide the boundary and human-in-the-loop placement, though no detail on how is given.

### Claim 5: Deterministic pieces need tests against the requirements they enforce, updated as business rules change
- **Evidence**: Described Conductor feature: requirements and edge cases captured during build become tests in an evaluation module, used to monitor hardened workflows as policies and systems change.
- **Confidence**: anecdotal
- **Quote**: "Conductor turns requirements and edge cases captured during the build phases into tests within its evaluation module."
- **Our assessment**: Good practice (requirements to regression tests). No data on how well it works.

### Claim 6: Evaluate an agent-builder on four dimensions, not just task completion
- **Evidence**: Rubric table plus a task suite (build new agent, write a test case, change existing agent, root cause analysis).
- **Confidence**: anecdotal
- **Quote**: "Finishing the task is not the only bar. The team also looks at the outcomes, how Conductor got there, and what it used along the way."
- **Our assessment**: The outcome / execution path / quality-vs-curated-reference / resource-use rubric is a reusable template for evaluating any agent, including trajectory (tool/context use) and cost. Note it is judged vs "a curated reference", so reference curation is a hidden cost.

### Claim 7: The eval task suite doubles as a safety net when models or the framework change
- **Evidence**: Process description; same tasks and same scoring rerun on each new Claude model or Conductor framework update.
- **Confidence**: anecdotal
- **Quote**: "Those same tasks function as a safety net."
- **Our assessment**: Strong, practical pattern for model-upgrade regression testing. No results (e.g. regressions caught) are reported.

### Claim 8: Conductor cut initial deployment time roughly in half
- **Evidence**: Self-reported by Cresta, "early use cases across Cresta and its partners". No sample size or baseline.
- **Confidence**: anecdotal
- **Quote**: "Cresta reports that in early use cases across Cresta and its partners, Conductor cut initial deployment time roughly in half."
- **Our assessment**: Marketing-grade number; treat as directional only.

### Claim 9: Dogfood the builder internally first; release only when output matches an expert engineer's
- **Evidence**: Cresta's own history: forward-deployed team used it first.
- **Confidence**: anecdotal
- **Quote**: "Conductor ran as an internal tool first, and only became a product once its output matched what an engineer with deep AI expertise would build."
- **Our assessment**: Reasonable release gate (expert-parity), though subjective.

### Claim 10: Initial build is ~20% of effort; 80% is testing, optimization and continuous improvement
- **Evidence**: Stated as a best practice; no supporting measurement.
- **Confidence**: anecdotal
- **Quote**: "The initial build is only about 20% of the effort, the other 80% is the testing, optimization, and continuous improvement that follows, so design your tooling around the iteration loop, not the launch."
- **Our assessment**: Rule-of-thumb, not data. Directionally matches other sources emphasizing evaluation and iteration over initial generation.

### Claim 11: Build on the SDK for commodity capability; invest only in unique advantages
- **Evidence**: Cresta's build-vs-buy line; SDK review covered data privacy, tenant architecture, org-level key distribution, controls, observability.
- **Confidence**: anecdotal
- **Quote**: "That lets us put our engineering investment where Cresta creates the most durable customer value,"
- **Our assessment**: Vendor-flattering but a legitimate buy-vs-build argument; note the enterprise vetting checklist.

## Concrete Artifacts

Evaluation rubric (Source: "How Cresta evaluates Conductor" table):

```
Evaluation       | Question it answers
Outcome          | Did Conductor produce the requested, usable artifact?
Execution path   | Did it use the appropriate tools and required context?
Quality          | How does the result compare with a curated reference?
Resource use     | How much time and model usage did the task require?
```

Eval task suite (source list): Build a new agent; Write a test case for one; Change an agent that already exists; Perform root cause analysis.

Example CX ambiguity cases cited: refund request without naming the purchase; billing problem and login issue in one message; refund request after the return window closed.

No code, config or transcripts are in the source.

## Cross-References

- **Corroborates**: `blog-anthropic-claude-managed-agents.md` Claim 4 (outcome-based self-evaluation loop) on defining success criteria for agent iteration; `blog-anthropic-multi-agent-coordination-patterns.md` Claim 12 (start simple and evolve from observed failure modes) on iterating after launch; `blog-anthropic-asana-coachable-agents.md` Claim 6 (memory ownership maps to domain expertise, experts set agents up so others benefit), similar to Conductor's expert-pattern sharing.
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-anthropic-claude-managed-agents.md` (agent infrastructure) with the builder-side view: evaluation discipline and meta-agent design for a team shipping many agents.
- **Novel**: Agent-builds-agents (meta-agent) as a production product; the four-dimension builder eval rubric including execution path and resource use; rerunning the same task suite on each model release as a safety net; using historical conversations to decide deterministic vs flexible boundaries.

## Guide Impact

- **Evaluation chapters**: Add the outcome / execution path / quality-vs-reference / resource-use rubric as an example of evaluating agents beyond pass/fail (cite this note Claim 6), flagged anecdotal.
- **Model-upgrade guidance**: Recommend keeping a fixed task suite with fixed scoring to rerun on new models or harness changes (Claim 7).
- **Multi-agent / meta-agent content**: Add Conductor as a case study of an agent building agents on the Agent SDK (Claims 1-3); the guide currently has no meta-agent example.
- **Design trade-offs**: Cite Claim 4/5 for "harden only enterprise-critical paths, test them against requirements, leave the rest flexible".
- **Do not** cite the "half" deployment-time or 20/80 figures as evidence; they are unsupported self-reports.

## Extraction Notes

- Read the full article (fetched directly from the source URL; the page has no linked sub-pages of substance). Quotes were copied from the page text; the Claim 4 quote ends at the source's trailing comma.
- The source is thin on implementation detail; it is a marketing-oriented case study. Confidence is therefore `anecdotal` overall.
