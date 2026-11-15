---
source_url: https://claude.com/resources/articles/building-always-on-agents
source_type: blog-post
title: "Building always-on agents"
author: William Hu (Anthropic)
date_published: 2026-11-13
date_extracted: 2026-11-15
last_checked: 2026-11-15
status: current
confidence_overall: emerging
issue: "#4742"
---

# Building always-on agents

> Anthropic reference architecture for proactive, stateful agents: five primitives (event inbox, timers, memory, permissions, outbox) wrapped around the ordinary agent loop, with concrete rules for concurrency, deferral, credentials and message pacing.

## Source Context

- **Type**: blog-post (Claude resources article, category "Best practices", product Claude Platform; 14 min read)
- **Author credibility**: William Hu, Anthropic; acknowledgements to Rodrigo Olivares and Michael Segner. First-party vendor guidance drawing on Anthropic products (Claude Code auto memory, auto mode, hooks; Messages API memory tool). Claims are design recommendations, not measured production results.
- **Scope**: Architecture of unattended/proactive agents. Contains no code or config, no incident reports, and only one quantitative figure (a vendor-reported cost benchmark). Does not cover multi-agent coordination, evals methodology (only says to build them), or specific scheduler implementations.

## Extracted Claims

### Claim 1: "Always-on" is a user-experience description; the agent actually sleeps and wakes into discrete runs inside sessions
- **Evidence**: Conceptual definition; no measurements.
- **Confidence**: emerging
- **Quote**: "An always-on agent is not actually “always on.” This is just a description of the user experience."
- **Our assessment**: Useful vocabulary: run = receive event, work, save; session = transcript of messages and tool calls. It reframes "always-on" as event-driven wakeups, which is cheaper and more recoverable than a resident process. Accept as a definition.

### Claim 2: Event sources should write to a durable inbox, not call the agent directly, because direct calls cause competing runs and lost events
- **Evidence**: Reasoned failure modes (simultaneous events, crash loses event); recommended three-component design (durable table, HTTP handler, background worker).
- **Confidence**: emerging
- **Quote**: "two events arriving at the same time can start competing runs, and a crash can lose an event entirely."
- **Our assessment**: Standard queue/outbox-style engineering applied to agents; sound. No evidence that it was tested against alternatives.

### Claim 3: The inbox is the source of truth; events are deduplicated by source ID, and a crashed worker is replaced by one that retries the same event
- **Evidence**: Design advice; relational DB with one row per event recommended; start with one inbox per user.
- **Confidence**: emerging
- **Quote**: "The inbox should be the source of truth."
- **Our assessment**: Matches durable-execution practice (see Cross-References). Note the retry implies at-least-once delivery; the article does not mention idempotency of side effects, which the Fowler/Prakash note treats as essential.

### Claim 4: Only one active worker per inbox, with three policies for events arriving mid-run: push to next run, fold into current run, or interrupt and restart
- **Evidence**: Design advice; the three options are listed without a recommendation of which to choose.
- **Confidence**: emerging
- **Quote**: "An inbox should only have one active worker at a time."
- **Our assessment**: The single-writer rule prevents duplicated work and overwrites. The mid-run policy choice is left to the implementer; the guide should present it as a decision point, not a settled answer.

### Claim 5: Handlers should acknowledge quickly and defer deeper verification (including prompt-injection checks) to the run; the worker should batch pending events
- **Evidence**: Webhook providers treat slow responses as failures; batching example is several user messages merged into one reply.
- **Confidence**: emerging
- **Quote**: "any deeper verification, such as checking for prompt injection, should be done during the run."
- **Our assessment**: Practical. Placing injection checks inside the run (where the model and tools are) rather than at the edge is a notable design choice, but the article gives no detail on how.

### Claim 6: Timers are either follow-ups (agent-set deadlines) or schedules (recurring), live in a store separate from the inbox, and never start runs directly
- **Evidence**: Design description with a three-step scheduler pass (find due timers; mark follow-up done or advance schedule to next occurrence; enqueue event and wake worker). Scheduler can be self-built or a durable execution engine.
- **Confidence**: emerging
- **Quote**: "A timer doesn’t initiate a run on its own."
- **Our assessment**: Clean separation: the inbox holds only ready work. Keeps the single-worker invariant intact for timer-driven runs.

### Claim 7: Memory needs its own durable store (directories of files mapped to a database or object store) so it outlives the worker, and should hold only what the agent cannot look up again
- **Evidence**: Cites Claude Code auto memory and the Messages API memory tool as file-directory implementations.
- **Confidence**: emerging
- **Quote**: "memory should only hold what the agent can’t look up again."
- **Our assessment**: Agrees with the selectivity findings in the components-of-agent-memory note. "Save a pointer instead" for data in other systems is a concrete, adoptable rule.

### Claim 8: Four memory categories for always-on agents: user instructions (always loaded), user notes, past messages, and per-task progress files; larger sets load only an index
- **Evidence**: Taxonomy plus a diagram (not reproduced in the page text).
- **Confidence**: emerging
- **Quote**: "Task progress: For each ongoing task, the agent should keep a progress file that covers what’s been done and what’s left."
- **Our assessment**: The "past messages" category (so nothing is repeated to the user) and per-task progress files are the incremental ideas relative to existing memory notes. Progress file resembles the Ralph-loop/progress-file pattern used in coding agents.

### Claim 9: Context overhead (system prompt, tool definitions, memory files) is paid on every run, so keep it lean and use prompt caching; long sessions can be compacted or replaced, both losing detail
- **Evidence**: Design advice.
- **Confidence**: emerging
- **Quote**: "Both approaches lose detail, so anything that needs to persist should be saved to memory along the way."
- **Our assessment**: Pairs naturally with index-only loading in Claim 8. A new session starts with overhead plus triggering events; an existing session restores prior messages.

### Claim 10: Dreaming (offline review of past sessions) can be layered on top of in-run memory writes
- **Evidence**: One paragraph; defers to a separate Anthropic post on agent memory.
- **Confidence**: emerging
- **Quote**: "Dreaming can replace outdated entries and find patterns that only show up across many runs."
- **Our assessment**: Thin here; the substantive evidence lives in the dreaming notes.

### Claim 11: Permissions are where always-on agents carry the most risk; use a credential-injecting proxy outside the agent environment
- **Evidence**: Recommended pattern, no incident data.
- **Confidence**: emerging
- **Quote**: "The agent sends requests without credentials, and the proxy injects the real credentials before forwarding."
- **Our assessment**: Strong, adoptable pattern: the agent never holds secrets, limiting what prompt injection can exfiltrate. Same direction as vault-injected env vars in the scheduled-vaults note.

### Claim 12: Auto mode (classifier review of higher-risk actions) lets always-on agents work without constant input, but user review remains necessary for the most important decisions
- **Evidence**: Cites Claude Code auto mode.
- **Confidence**: emerging
- **Quote**: "User review, however, is still necessary for the most important decisions."
- **Our assessment**: Consistent with auto-mode notes; those also document bypasses (see Cross-References), so classifier-only gating should not be presented as sufficient.

### Claim 13: Deferred tool calls end the run, save the session mid-call, and resume on a later inbox event carrying the user's answer; the worker is free in the meantime
- **Evidence**: Mechanism description; user prompt surfaced e.g. via an interactive card built with MCP Apps; relies on Claude Code hook deferral.
- **Confidence**: emerging
- **Quote**: "When a call is deferred, the run ends and the session is saved mid-call."
- **Our assessment**: The key insight is that approval becomes just another inbox event, so no process blocks waiting for a human. Staleness of the deferred decision is not discussed (compare Fowler/Prakash Claim 9).

### Claim 14: A run ends in one of three ways (send, send nothing, or deferred call); a formal outbox is optional and needed only for pacing or error recovery
- **Evidence**: Design description; outbox table plus dispatcher mirroring inbox plus worker.
- **Confidence**: emerging
- **Quote**: "You only need a formal outbox when you want to pace your agent’s messages or allow your agent to recover from errors."
- **Our assessment**: Good guidance against over-building; start with a "send" tool.

### Claim 15: Message volume should be tuned with evals, and agents should start quiet and earn attention
- **Evidence**: Recommendation only; no eval design or results.
- **Confidence**: anecdotal
- **Quote**: "In practice, it’s better for the agent to start quiet and then earn more of the user’s attention over time."
- **Our assessment**: Plausible and consistent with notification-fatigue experience, but unsupported by data. The explicit "no send" outcome is the mechanism.

### Claim 16: Recent models make always-on agents practical via better judgment and cheaper long-horizon intelligence (vendor-reported: Opus 5.5 cost 78% less per solved task than Opus 5 on one long-horizon coding benchmark, versus 40% on typical workloads)
- **Evidence**: Single vendor benchmark figure; benchmark unnamed and not linked in the page text.
- **Confidence**: anecdotal
- **Quote**: "on one long-horizon coding benchmark, Opus 5.5 cost 78% less per solved task than Opus 5, compared with 40% less on typical workloads."
- **Our assessment**: Attribute to Anthropic; do not generalize. Unnamed benchmark, self-reported, and the motivation is marketing-adjacent.

## Concrete Artifacts

No code or config in the source. The architecture, as described in "How everything fits together" (paraphrased by us as a flow, not a quote):

```
event source -> handler (ack fast) -> INBOX (durable table, dedupe by source id)
timer store (follow-ups, schedules) -> scheduler (polls) -> INBOX
INBOX -> single worker (batches pending) -> run in new or resumed session
run: load memory (instructions, notes index, past msgs, task progress index)
     -> act under permissions (credential proxy, auto mode, deferred calls)
     -> update memory
     -> outcome: send | send nothing | deferred call
OUTBOX (optional table) -> dispatcher -> user
user reply / approval -> INBOX (resumes saved session)
```

Scheduler pass (summarized from source): find due timers; mark follow-up done or advance schedule to next occurrence; add event to inbox and wake worker.

## Cross-References

- **Corroborates**: `blog-anthropic-components-of-agent-memory.md` Claim 9 (injected top memory layer stays small) and Claim 2 (write only what is likely relevant) support the "index only, store what cannot be looked up" rules (Claims 7-8 here). `blog-anthropic-managed-agents-scheduled-vaults.md` Claim 4 (credentials injected from a vault rather than exposed in the sandbox) corroborates the credential-proxy pattern (Claim 11 here). `blog-fowler-prakash-long-horizon-agents-durable-execution.md` Claim 4 (one entity workflow prevents concurrent duplicate runs) corroborates single-worker-per-inbox (Claim 4 here), and its Claim 5 (waits consume no compute) corroborates sleeping between runs.
- **Contradicts**: None found. (Auto-mode bypass material in `blog-simonwillison-breaking-auto-mode.md` does not oppose this article's claim directly; it qualifies Claim 12 and is noted as a caution, so no contradiction issue was filed.)
- **Extends**: `blog-anthropic-claude-code-routines.md` Claims 2-5 (scheduled, API and webhook triggers; persistent per-PR sessions) cover triggers only, whereas this article specifies the inbox/timer substrate behind them. `blog-anthropic-claude-managed-agents-memory.md` Claim 2 (memories as mounted files) is extended with always-on categories. `blog-anthropic-managed-agents-dreaming-outcomes.md` Claim 1 (dreaming as scheduled cross-session review) is referenced at Claim 10 here. `blog-fowler-prakash-long-horizon-agents-durable-execution.md` Claims 3 and 6 (replay log, at-least-once retries) are the reliability layer this article only gestures at ("durable execution engine").
- **Novel**: The five-primitive decomposition as a whole; inbox-as-source-of-truth with three mid-run event policies; follow-up vs schedule timers kept out of the inbox; deferred tool call as save-and-resume via inbox event; past-messages memory category; optional outbox with send / no-send / defer outcomes; "start quiet and earn attention".

## Guide Impact

- **Chapter 01 (Daily Workflows)**: Add a short section on unattended/proactive agents using the run/session cycle and per-task progress files as the handoff mechanism between runs. Note the article's single-worker rule as the guard against overlapping runs.
- **Chapter 02 (Harness Engineering)**: Add an "always-on harness" pattern: inbox, timer store plus scheduler, single worker, deferred tool calls that end the run and resume on an event. Present the mid-run event policy (queue, fold in, interrupt) as an explicit design choice. Flag that idempotency of retried side effects must be added (from the Fowler/Prakash note) since this article omits it.
- **Chapter 04 (Context Engineering)**: Cite the per-run context overhead point, index-only loading for notes and progress files, and compaction vs new session ("both lose detail, so persist to memory").
- **Chapter 06 (Security Threat Model)**: Cite the credential-injecting proxy as a recommended mitigation for unattended agents, auto mode as necessary-but-insufficient gating, and deferred calls as the human-approval mechanism. Label all as vendor recommendations without incident data.
- **Cost claims**: If the 78% figure is used anywhere, attribute it to Anthropic as a single unnamed-benchmark vendor claim.

## Extraction Notes

- Fetched the full article HTML directly and read all of it; quotes were copied from the extracted page text (curly apostrophes preserved). Diagrams referenced in the page ("The diagram below...") are not visible in text; the memory example setup was not extracted.
- The article links to a separate Anthropic post on agent memory (dreaming) and to Claude Code docs; these were not followed because the existing corpus already has notes on them (`blog-anthropic-components-of-agent-memory.md`).
- Evidence is design guidance only; confidence is therefore `emerging` overall, with `anecdotal` on the cost figure and the outbox-tuning advice.
- Cross-reference claim numbers were verified against the headings of the cited notes.
