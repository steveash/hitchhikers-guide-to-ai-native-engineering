---
source_url: https://latent.space/p/arca/
source_type: blog-post
title: "Agents Prompt People: Using Agents for Long-Horizon Financial Work"
author: Richard MacManus (Latent Space), interviewing Aman Singh (Arca)
date_published: 2026-10-31
date_extracted: 2026-11-13
last_checked: 2026-11-13
status: current
confidence_overall: anecdotal
issue: "#4703"
---

# Agents Prompt People: Using Agents for Long-Horizon Financial Work

> A practitioner-reported architecture from Arca (AI-native wealth management): per-client persistent memory for multi-day agent tasks, deterministic limits that keep agents away from money movement, a code-to-strict-format data-access layer, and a meta-agent that tunes the harness.

## Source Context

- **Type**: blog-post (Latent Space podcast write-up with timestamps; the page shows the summary, not the transcript)
- **Author credibility**: Written by Richard MacManus from a Latent Space interview with Aman Singh, lead AI Engineer at Arca, recorded at AI Engineer New York. Singh is a first-hand practitioner, but everything is self-reported. The page gives no metrics, code, error rates, costs, or failure cases.
- **Scope**: Covers Arca's memory, custom harness and model routing, deterministic safety restrictions, sandboxed code access to data, and the meta-agent. The podcast timestamps list further topics (compliance and auditability by default, turning staff feedback into evals, tax-bill approval example) that the page does not elaborate. Those would need the audio or the AIE talk.

## Extracted Claims

### Claim 1: Financial agent work is long-horizon but not long-running: tasks span up to ten days with many actors and handoffs
- **Evidence**: Speaker's description of Arca's production workloads (AIE presentation). No data.
- **Confidence**: anecdotal
- **Quote**: "It's very stop-start, there's many actors in between, many decision points, many handoffs,"
- **Our assessment**: The "long-horizon, not long-running" distinction is useful. The agent is mostly idle between human steps, so the problem is state continuity, not process uptime. Matches the framing in the Fowler/Prakash note, though Arca gives no mechanism beyond memory.

### Claim 2: Arca keeps persistent per-client memory that agents contribute to, tracking history, next steps, and ownership
- **Evidence**: Singh's description of an internal memory system. The schema is not shown.
- **Confidence**: anecdotal
- **Quote**: "All of this is being tracked by our memory systems"
- **Our assessment**: The fields listed (what has happened, what is tracked next, what is needed in the next couple of days vs long term, which individual owns which action) amount to a task-ledger design. This is an entity-scoped memory, closer to a case file than to conversational memory. The note has no detail on write policy, staleness, or conflicts.

### Claim 3: Arca built its own harness that picks a model per task using internal benchmarks
- **Evidence**: Stated by the article; Claude is the primary provider alongside OpenAI models. No benchmark numbers.
- **Confidence**: anecdotal
- **Quote**: "automatically selects the best model to use for a particular task, based on the company’s internal benchmarks."
- **Our assessment**: Plausible and consistent with Kepler's per-stage routing, but the selection mechanism is undescribed. Do not cite it as evidence that routing beats a single model.

### Claim 4: Owning the harness, rather than using a managed one, preserves the ability to switch model providers
- **Evidence**: Rationale given by the speaker (timestamp 13:46 "Why Arca owns its agent infrastructure"); no cost or switching evidence.
- **Confidence**: anecdotal
- **Quote**: "Arca has the flexibility to change model providers if it needs to."
- **Our assessment**: A real build-vs-buy argument (provider portability), but a one-sided one. Arca, a well-funded team, does not weigh it against the maintenance cost. Note the contrast with Cresta's "build on the SDK for commodity capability" stance.

### Claim 5: Agents are limited to analysis and proposals; trading and all money movement stay with a human advisor
- **Evidence**: Architecture description; the interview timestamps include a $100,000 tax-bill approval example that the page does not detail.
- **Confidence**: anecdotal
- **Quote**: "an agent’s role is limited to analysis and proposing solutions."
- **Our assessment**: A clear instance of the human-approval boundary. Consistent with the staged-not-auto-executed boundary in Anthropic's financial advisors note.

### Claim 6: Safety restrictions are deterministic and remove decisions from the agent
- **Evidence**: Speaker assertion. The enforcement mechanism (tool allowlists, gateways) is not described.
- **Confidence**: anecdotal
- **Quote**: "“All of our safety restrictions are fully deterministic,”"
- **Our assessment**: The principle (enforce in code, not prompts) is well supported elsewhere (Fowler/Prakash Claim 1). "Fully" is a strong self-report with no verification or failure data; treat as a design claim, not a measured guarantee. The page also says Arca runs verification checks for known issues such as prompt injection, which are presumably not all deterministic.

### Claim 7: Agents get code-execution access to data via a translate-to-strict-format, discard-the-code, guardrail-the-format pipeline
- **Evidence**: Speaker's description. The agent itself is not sandboxed; sandboxes are used for computation.
- **Confidence**: anecdotal
- **Quote**: "you install guardrails on that format before it reaches your back end."
- **Our assessment**: The most novel pattern here. The agent-written code is treated as untrusted; only a normalized, constrained representation of its data request crosses into the backend, and the code itself is thrown away. This keeps the flexibility of code (aggregation, munging) while giving guardrails a fixed schema to validate. Unanswered: what the format is, how expressive it is, and what happens when valid code cannot be expressed in it.

### Claim 8: A meta-agent analyzes advisor feedback and agent traces to suggest harness changes
- **Evidence**: Description only. It is not said whether suggestions are auto-applied or human-reviewed, or how effective they are.
- **Confidence**: anecdotal
- **Quote**: "meta-agent"
- **Our assessment**: The quote is only the label; the rest of the claim is the article's paraphrase ("A “meta-agent” is used to analyze all this data and suggest changes to the harness"). The inputs (human feedback plus traces) are the interesting part. The timestamp "Turning staff feedback into evals and improvements" suggests feedback also feeds evals, but the page does not say. Ties to Cresta's meta-agent but with an operational feedback loop rather than pattern capture.

### Claim 9: The design goal is that agents prompt people more than people prompt agents
- **Evidence**: Framing quote from Singh; agents do most background work with humans making final decisions.
- **Confidence**: anecdotal
- **Quote**: "agents prompt people more than people prompt agents.”"
- **Our assessment**: A product/UX inversion: the agent drives the workflow and asks humans for decisions at checkpoints. It explains why the memory must track who owns each action. Worth noting as a pattern name; unsupported by usage data.

## Concrete Artifacts

No code, config, or metrics in the source. The only structured material is the speaker's list of what per-client memory tracks (attributed to Singh, podcast discussion):

```
Per-client memory fields (as described by Aman Singh, paraphrased from article quote):
- what has happened so far
- what is being tracked next
- what needs to happen immediately (next couple of days)
- what is tracked for the long term
- which individual is responsible for which action
```

Data-access pattern (as described; no implementation shown):

```
agent writes code in sandbox -> translated to strict expected format -> code discarded
-> guardrails validate the format -> backend
```

## Cross-References

- **Corroborates**: `blog-fowler-prakash-long-horizon-agents-durable-execution.md` Claim 1 (business rules in code via per-tool gates, not prompts) and Claim 2 on long-horizon agents as stop-start systems; `blog-anthropic-claude-financial-advisors.md` Claim 5 (regulated actions require human approval and are staged); `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3 (deterministic infrastructure around the model) and Claim 7 (per-stage model routing).
- **Contradicts**: None found. No contradiction issue filed. (Cresta Claim 11 recommends building on an SDK for commodity capability, while Arca argues for owning the harness; this is a differing context/trade-off, not a direct contradiction.)
- **Extends**: `blog-fowler-prakash-long-horizon-agents-durable-execution.md` Claim 11 (the durable log is not the model's memory; tiered memory) with a concrete per-client memory example; `blog-anthropic-cresta-conductor-agent-builder.md` Claim 3 (meta-agent) with an operations-feedback-driven meta-agent; `blog-anthropic-components-of-agent-memory.md` (cross-session memory) with an entity-scoped task-ledger use case; `blog-latentspace-ainews-finance-vertical-aie-nyc.md` (finance track at AIE NYC; this episode is from the same conference).
- **Novel**: the "translate agent code to strict format, discard code, guardrail the format" data-access pattern; the "agents prompt people" framing; a meta-agent fed by human-advisor feedback plus traces; owning the harness explicitly for provider portability.

## Guide Impact

- **Ch04 (harness / orchestration)**: Could add the Arca meta-agent loop (advisor feedback + traces -> proposed harness changes) as a self-reported example next to the Cresta meta-agent, flagged anecdotal; and the provider-portability argument for owning a harness.
- **Ch06 (memory / long-horizon)**: Could cite per-client persistent memory tracking history, next actions, time horizon, and owner as an example of entity-scoped task memory for stop-start work of up to ten days (anecdotal).
- **Ch08 (safety / human approval)**: Could add the "analysis and proposals only; money movement human-only; enforced deterministically" boundary and the code-to-strict-format guardrail pattern as a design to evaluate, with the caveat that no failure data exists.
- **Ch10 (verification / auditability)**: Low direct impact; the page only mentions compliance and auditability by timestamp. Do not cite for auditability claims.

## Extraction Notes

- Fetched the page via curl and read the full text; it is a short write-up (~14k chars including site chrome), not a transcript. Timestamp topics without body text (compliance, evals from staff feedback, tax-bill example, hidden fees) were not extracted as claims.
- The page links to a YouTube video and Singh's AIE presentation; these were not accessible as text, so the note rests only on the article.
- Per the Prospector's caveats, all claims are practitioner self-report; confidence is anecdotal. Quotes were copied verbatim from the page; the Claim 6 and Claim 9 quotes retain the page's curly-quote characters.
- Cross-referenced claim numbers were checked against the cited notes' `### Claim` headings.
