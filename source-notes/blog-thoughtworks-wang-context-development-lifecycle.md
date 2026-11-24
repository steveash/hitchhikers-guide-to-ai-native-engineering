---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/understanding-context-development-lifecycle
source_type: blog-post
title: "Understanding the context development lifecycle"
author: Ni Wang
date_published: 2026-11-23
date_extracted: 2026-11-24
last_checked: 2026-11-24
status: current
confidence_overall: emerging
issue: "#4926"
---

# Understanding the context development lifecycle

> A conceptual Thoughtworks framing of context engineering as a four-stage lifecycle (design/create, discover/retrieve, runtime management, evaluate/improve), with a useful three-move taxonomy of compression and a codified-vs-ambient context split; it presents no measurements.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, Generative AI)
- **Author credibility**: Ni Wang, Senior Consultant at Thoughtworks. The post ties its stages to technologies in Technology Radar Vol. 35. The author states the techniques "aren't particularly new or novel", so this is synthesis, not first-hand experiment.
- **Scope**: Covers lifecycle stages, context types, MCP vs skills, context graphs, compression, subagents, programmatic tool calling, profiling and improvement loops. It contains no code, metrics, or case-study results. Radar items (e.g. "Naive context compression", "Graph-grounded codebase reasoning") are referenced but not reproduced.

## Extracted Claims

### Claim 1: Context engineering should be understood as a four-stage lifecycle, and each failure point needs a different intervention
- **Evidence**: Conceptual framing. The stages are Design and create; Discover and retrieve; Manage context at runtime; Evaluate and improve. Illustrated with hypothetical failures (agent never finds the governing ADR, misses a policy exception, follows a stale instruction, loses a detail in compression).
- **Confidence**: emerging
- **Quote**: "Failures such as these occur at different points in what's called the context development lifecycle, and each needs a different intervention."
- **Our assessment**: A useful organizing lens for triage (is it a knowledge, retrieval, runtime or feedback problem?). It is a model, not validated evidence. Other sources can slot under it.

### Claim 2: Context splits into codified (owned, version-controlled, reusable) and ambient (unowned, situational), attributed to Birgitta Böckeler
- **Evidence**: Attributed to a talk by Böckeler (not independently checked). Examples: codified = AGENTS.md, agent skills, ADRs; ambient = meeting notes, Slack.
- **Confidence**: emerging
- **Quote**: "Ambient context, by contrast, refers to things like meeting notes and Slack discussions; these lack clear ownership and organization and often relate to highly specific situations."
- **Our assessment**: A crisp vocabulary that is new to our corpus. The ambient category names the knowledge that never reaches AGENTS.md. Secondhand attribution; the underlying talk is not in the corpus.

### Claim 3: Ambient context has no easy fix, but agent-maintained knowledge bases have worked for some Thoughtworks teams
- **Evidence**: Anecdotal ("a number of Thoughtworks teams"). Pattern: an agent reads raw sources without modifying them and maintains a linked set of plain-text notes under a defined schema, shared by PMs, designers, developers and agents.
- **Confidence**: anecdotal
- **Quote**: "The pattern involves an agent reading raw source material without changing it, then creating and maintaining a linked collection of plain-text notes under a defined schema."
- **Our assessment**: Plausible and consistent with LLM-wiki-style practice, but there are no outcomes reported. Record as a pattern, not a result.

### Claim 4: Blindly trusting AI-generated context makes ambient context drift and causes overload; check for missing, incorrect or stale content
- **Evidence**: Assertion; points to Radar's "harness quality evaluation".
- **Confidence**: emerging
- **Quote**: "It's important to check whether anything is missing, incorrect or out of date."
- **Our assessment**: Agrees with common experience (LLM-generated CLAUDE.md bloat). The post offers no data on the failure rate.

### Claim 5: Loading all MCP tool definitions upfront consumes the window; skills separate discovery from loading and can carry usage guidance for MCP tools
- **Evidence**: Reasoned example (a database migration skill). No measurement.
- **Confidence**: emerging
- **Quote**: "Agent skills illustrate how discovery can be separated from loading."
- **Our assessment**: Consistent with Anthropic's progressive-disclosure guidance. The "access plus guidance work together" framing of MCP+skills is a clean articulation.

### Claim 6: Progressive context disclosure is "just-in-time procurement": conventions load on directory entry, schemas on table write, policies at the decision point
- **Evidence**: Principle with three concrete examples; no data.
- **Confidence**: emerging
- **Quote**: "A convention that applies to one directory should arrive when the agent enters that directory, not on every call."
- **Our assessment**: Concrete, actionable examples of scoped loading (path-scoped rules, nested instruction files). Matches Nandyala/Pani's index-first and path-scoped guidance.

### Claim 7: A context graph lets agents retrieve reasoning (exceptions, supersession) rather than just chunks; graph-grounded code retrieval should be evaluated against native search
- **Evidence**: Conceptual; the author hedges that native coding-agent search sometimes performs better.
- **Confidence**: emerging
- **Quote**: "A chunk can tell the agent what a policy says. A graph can tell it that the policy has an exception, that the exception was granted for a specific case, and that a later decision superseded it."
- **Our assessment**: The hedge ("teams should evaluate whether the added graph structure improves accuracy and total cost on their own codebases") is the valuable part. Graph retrieval is not presented as a default.

### Claim 8: Compression comprises three distinct moves that teams conflate: trimming at the boundary, pruning after use, and compaction
- **Evidence**: Taxonomy with definitions; no measurement.
- **Confidence**: emerging
- **Quote**: "The third move is compaction: summarising decisions, progress and open questions, then starting a fresh context window."
- **Our assessment**: The most reusable contribution. Trimming (select fields, truncate logs, originals stay put) and pruning (drop old results, keep a retrieval path) are lossless-ish relative to compaction (lossy summary). Maps onto harness behaviors catalogued in the compaction research note (e.g., reversible event stores vs LLM-summary compaction).

### Claim 9: Naive compression can cost more than it saves: over-trimming forces re-retrieval, pruning/compaction reduces prompt-cache reuse, and summaries add token and latency cost
- **Evidence**: Reasoned argument citing the Radar's "Naive context compression" (Caution ring). No numbers in this post.
- **Confidence**: emerging
- **Quote**: "The useful measure is not the size of the compressed context, it is whether compression improves the whole task, including accuracy and total cost."
- **Our assessment**: Corroborated quantitatively by research-wasnotwas-context-compaction (cost per compaction call, cache burn). This post supplies the framing; that note supplies the numbers.

### Claim 10: Subagents reduce the main agent's context but not necessarily total work or cost; programmatic tool calling keeps intermediate results out of the window entirely
- **Evidence**: Conceptual comparison.
- **Confidence**: emerging
- **Quote**: "The context window sees the answer, not the transcript."
- **Our assessment**: The "subagents don't reduce total cost" caveat is useful and often omitted. Programmatic tool calling as a distinct alternative to subagents is thinly covered elsewhere in our corpus.

### Claim 11: Context profiling from existing session traces is an accessible first step; verify changes by comparing similar-task sessions before and after
- **Evidence**: Practical advice; no tooling named.
- **Confidence**: emerging
- **Quote**: "Reviewing a session is an accessible first step before investing in dedicated profiling tools."
- **Our assessment**: Low-cost, actionable. Success criteria listed are lower total cost, less repeated retrieval, or better task quality.

### Claim 12: Feedback flywheels and self-improving harnesses only work with a named owner and review cadence
- **Evidence**: Assertion; refers to Radar concepts.
- **Confidence**: emerging
- **Quote**: "A named owner and a regular review cadence help make the loop an ongoing practice, with changes tested and maintained over time."
- **Our assessment**: Corroborates the ownership emphasis in Geraldo's harness-as-product note. The self-improving harness is described as "test those changes against real or replayed tasks", with no safeguards beyond that.

### Claim 13: Context engineering is an operational capability (supply chain, retrieval layer, runtime policy, eval suite, feedback loop), each needing an owner and a standard; the unit of improvement shifts from one prompt to whether the system's context improves over time
- **Evidence**: Thesis statement; the post concedes the underlying techniques are not new.
- **Confidence**: emerging
- **Quote**: "Each one should have an owner and a standard."
- **Our assessment**: Organizational framing rather than evidence. The closing "context is becoming an organizational asset" is opinion.

## Concrete Artifacts

No code or configs. The post's structural artifacts, attributed to Ni Wang:

```
Lifecycle stages and their stated goals (Ni Wang, Thoughtworks, 2026-11-23)
1. Design and create          - Define the relevant knowledge for an agent, create context as a team.
2. Discover and retrieve      - Make context discoverable and accessible in a context window friendly manner.
3. Manage context at runtime  - Keep the working context concise and useful during agent execution as tasks change.
4. Evaluate and improve       - Evaluate and measure context lifecycle practices end-to-end and using runtime feedback to improve persistent assets and harnesses.

Compression moves: (1) trimming at the boundary, (2) pruning after use, (3) compaction.
Operational capability: knowledge supply chain, retrieval layer, runtime policy, evaluation suite, feedback loop.
```

## Cross-References

- **Corroborates**: `research-wasnotwas-context-compaction` (Claim 2: one compaction call costs ~$0.40 and burns cached throughput; supports this post's cache-reuse caveat; Claim 6 and Claim 7: reversible/non-destructive designs correspond to pruning with retrievable originals). `blog-thoughtworks-sonawane-context-rot-in-ai-agents` (Claim 12: measure task outcomes, not context size; similar to this post's "whole task" metric). `blog-thoughtworks-nandyala-pani-bounded-context-bounded-attention` (Claim 4: index-first loading; Claim 5: subagents as context firewalls). `blog-thoughtworks-geraldo-harness-is-a-product` (Claim 8: evals need an owner and review cadence; Claim 9: self-improving loops can drift). `blog-anthropic-context-engineering-claude-5` (Claim 6: progressive disclosure; Claim 8: skills as lightweight guides).
- **Contradicts**: None found. No contradiction issue filed. The post's graph-retrieval hedge (native search sometimes wins) is a conditioning variable, not an opposing claim.
- **Extends**: `blog-thoughtworks-gall-layered-context-enterprise-data` (Claims 3 and 4: a metadata map plus on-demand loading; this post adds the lifecycle and context-graph framing). `blog-thoughtworks-nandyala-pani-engineering-the-harness` (Claim 13: harness as versioned, reviewed software; this post extends ownership to all context assets).
- **Novel**: The codified vs ambient split; the explicit three-move compression taxonomy (trimming / pruning / compaction); programmatic tool calling presented as an alternative to subagents; the agent-maintained linked-notes knowledge base pattern; context profiling via existing session traces as a first step.

## Guide Impact

- **Chapter 04**: Add the three-move compression taxonomy (trimming at the boundary, pruning after use with retrievable originals, compaction) as a framing ahead of compaction details, and cite the "whole task, including accuracy and total cost" test alongside the research-wasnotwas cost numbers. Add the codified vs ambient distinction when discussing what belongs in AGENTS.md vs what stays unwritten. Optionally use the four stages as a diagnostic checklist, labeled as practitioner framing, not validated.
- **Chapter 04**: Add the just-in-time loading examples (directory entry, table write, decision point) as concrete illustrations of progressive disclosure.
- **Chapter 02**: Note that subagents shrink the main context without necessarily reducing total cost, and mention programmatic tool calling as the alternative that keeps intermediate results out of the window. Reinforce named-owner and review-cadence guidance for harness improvement loops, citing this alongside the Geraldo note.

## Extraction Notes

- The page was fetched directly and read in full; WebFetch only returned a summary, so quotes were taken from the raw HTML text. No sub-pages were followed; Radar entries are referenced but not linked in the extracted text.
- Source is conceptual, with no metrics. All confidences are capped at emerging or anecdotal.
- The Böckeler talk is cited secondhand and was not located.
- Cross-referenced claim numbers were checked against the cited notes' headings.
