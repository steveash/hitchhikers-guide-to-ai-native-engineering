---
source_url: https://martinfowler.com/articles/durable-execution-agents.html
source_type: blog-post
title: "Long-horizon agents and durable execution"
author: Kiran Prakash (Director of Data and AI, Thoughtworks)
date_published: 2026-11-10
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: emerging
issue: "#4644"
---

# Long-horizon agents and durable execution

> Using a worked "Stock Replenisher" agent built on Temporal and Cloudflare Workflows, the article separates the agent failure modes a durable-execution runtime solves (crash, wait, retry, concurrency) from those the harness must handle in domain logic (lost outcomes, stale decisions, code changes under replay, memory growth, prompt injection).

## Source Context

- **Type**: blog-post (martinfowler.com article; published 10 November 2026)
- **Author credibility**: Kiran Prakash is a Director of Data and AI at Thoughtworks; the article credits Martin Fowler for editorial support. The author states they built the example on two runtimes ("We built Stock Replenisher on two of them, Temporal and Cloudflare Workflows"). The article discloses use of Claude "for code fragments, visualizations and proofreading".
- **Scope**: A single running example (an agent that reorders parts from suppliers over days/weeks), Python/Temporal code, and Cloudflare equivalents. Covers the agentic loop, durable execution (step/log/replay), entity vs. process workflows, waits, retries, and five failure modes that remain the harness's job. Does not cover coding agents, multi-agent coordination, or a general security treatment (it defers to Fowler's "Agentic AI and Security"). Timings and the Temporal/Cloudflare behaviours are from the author's own example, not general benchmarks.

## Extracted Claims

### Claim 1: The agentic loop has four parts (goal, tools, state, model), and business rules belong in code via per-tool `allowed(state)` gates, not in the prompt
- **Evidence**: Full Python loop; `PlaceOrder.allowed` returns true only when a PO exists, no order has been placed, and `state.price <= state.approved_up_to`. The model is only shown `allowed_tools`.
- **Confidence**: emerging (a single worked example, but a common harness design)
- **Quote**: "This way the business rules that matter are in code, not in the prompt."
- **Our assessment**: A concrete, copyable form of "harness constrains the action space": the model proposes, the harness decides what's on the menu. Also notable: the article uses a classification model for the decision step and a generation model only for drafting emails, which is a cost/speed design choice rather than evidence for it.

### Claim 2: A long-horizon agent should be treated as a distributed system whose model can decide how to recover, so on failure the harness's job is to give the model the right input
- **Evidence**: Failure-mode table (nine rows) mapping each failure to an example from the domain; the framing paragraph after it.
- **Confidence**: emerging
- **Quote**: "When a failure occurs, the harness's job is to provide the model with the right input so it can decide what to do next."
- **Our assessment**: Reframes recovery from "retry until it works" to "surface accurate state so the model can choose a recovery tool". The article's own examples (cancel_order, re-approval) are consistent, but it offers no comparison against purely deterministic recovery.

### Claim 3: Durable execution is a step / log / replay programming model: every outside-world call is a recorded step; on restart the program re-runs, recorded steps return from the log, and state is rebuilt
- **Evidence**: Definition plus Temporal code (`@workflow.run`, `workflow.execute_activity` with `activity_id=f"decide-{turn}"`). `decider.decide` (the LLM call) and each tool's `execute` are steps; `allowed` and `apply` are not. A run is shown where the process crashes for a day while awaiting approval and nothing before the crash re-executes.
- **Confidence**: settled for the pattern generally (Temporal, Restate, Inngest, DBOS, Cloudflare all implement it per the article); emerging as applied to LLM agents
- **Quote**: "Durable execution is a programming model in which the runtime keeps a record of the result of each step that interacts with the outside world so that, when a failure occurs, the program runs again, completed steps are skipped, and the program's state is rebuilt from the record."
- **Our assessment**: The agent-specific insight is that the model's choice of next tool is itself logged as a step, so replay does not re-sample the model and a crash cannot change an earlier decision. The constraint (code between steps must only read/write local state) is stated but determinism is not discussed in depth.

### Claim 4: One entity workflow per business entity (e.g. a SKU) owns state and message routing for the entity's lifetime and spawns short process workflows; this also prevents concurrent duplicate runs
- **Evidence**: `SkuAgent` entity workflow with `execute_child_workflow(Replenish.run, ...)`, `continue_as_new` to reset history, a stable ID `agent-SKU-123`, and a `deliver` signal forwarding messages to the active child. Cloudflare equivalent: a Durable Object per SKU, each replenishment a Cloudflare Workflow.
- **Confidence**: emerging
- **Quote**: "An entity workflow is a durable workflow that represents one business entity (e.g., a SKU) for the lifetime of that entity. It maintains the entity's state and initiates process workflows."
- **Our assessment**: Answers the "concurrency" row (a stock check starting a second replenishment while the first waits): only one child runs at a time. Maps onto the actor model; the article itself cites Erlang. Compare Cursor's move away from "eternal" workflows (see Cross-References).

### Claim 5: Waits should consume no process or compute, and wake-up cost grows with log length, so snapshots or `continue_as_new` are needed for long-lived entities
- **Evidence**: Footnote 4 measurements (see Concrete Artifacts): in-memory wake 14 ms on Temporal and about 0.1 s on Cloudflare; rebuilt from the log about two seconds on Cloudflare and under a tenth of a second on Temporal ("more as the log grew"); a wake used tens of milliseconds of CPU. Measured on deployed Cloudflare and a local Temporal server.
- **Confidence**: anecdotal (author's own small runs on one example workload, not a benchmark)
- **Quote**: "If wake-up is slow or expensive, then having thousands of agents waiting is just as infeasible as keeping thousands of processes open for weeks."
- **Our assessment**: The cost argument (cost proportional to work, not to number of idle agents) is sound; the numbers compare a deployed platform against a local server, so do not read them as a Temporal-vs-Cloudflare ranking.

### Claim 6: Durable retries give at-least-once, not exactly-once, so side-effecting tools need an idempotency key the harness keeps stable across attempts and replays
- **Evidence**: `RetryPolicy(maximum_attempts=6, initial_interval=2s, backoff_coefficient=2)`; `place_order` uses the PO number as idempotency key. Run shown: supplier down on first attempt, retry with same key, one order at supplier. The article names the Idempotent Receiver pattern (Unmesh Joshi).
- **Confidence**: settled (standard distributed-systems practice)
- **Quote**: "What the runtime can't do is make a retry safe."
- **Our assessment**: Directly applicable to any agent tool that writes to the world (payments, tickets, emails). Note the key must be derived from domain identity (PO number), not from the attempt.

### Claim 7: "Durable is not the same as correct": five failure modes remain, split into essential (lost outcomes, stale world) and accidental (code changes, history growth, untrusted input) complexity
- **Evidence**: Table using Fred Brooks's essence/accident split from "No Silver Bullet" (1986). Code-change is accidental to durable execution; history growth and untrusted input are accidental to the model.
- **Confidence**: emerging (the taxonomy is the author's)
- **Quote**: "Some failure modes can't be solved by durable execution alone."
- **Our assessment**: A useful checklist for what a runtime will not do for you. The essential/accidental labels are an interpretive framing; the practical content is in the per-failure mitigations below.

### Claim 8: A retried call that "failed" may have succeeded; the agent turns "we don't know" into "it failed", so give it compensating tools (saga pattern) such as `cancel_order`
- **Evidence**: Run described: supplier A takes the order but becomes unreachable; `place_order` fails after six attempts; the agent orders from supplier C; supplier A later confirms by email; the agent matches the PO number and cancels the earlier order with an explanation. The article says idempotency keys address only part of the problem.
- **Confidence**: emerging
- **Quote**: "The agent can't tell the difference, so it turns “we don't know” into “it failed” and proceeds as if no order existed."
- **Our assessment**: Strong, concrete failure case. Important caveat the article states itself: the agent found the duplicate only because supplier A wrote; "A persistent log records what the agent saw, not what actually happened."

### Claim 9: Decisions go stale during waits; three patterns help: give a decision an expiry, re-check before committing, and approve a range rather than a value
- **Evidence**: Optimistic Offline Lock reference. Stock Replenisher asks the manager to approve the price and up to 5% above; `place_order` re-fetches quotes and compares against the ceiling inside the tool. Worked numbers: approved $4.20 up to $4.41; confirmation at $4.35 stands; $4.54 would go back to the manager.
- **Confidence**: emerging
- **Quote**: "Note that this check is in the tool; it's a deterministic check that runs regardless of what the model decides."
- **Our assessment**: A good model of human-in-the-loop approval that does not rely on the model to remember to re-verify. Applies equally to coding agents (e.g. re-check branch state before pushing after a long wait).

### Claim 10: Deploying new harness code under a waiting run is dangerous because replay runs new code against an old log; behaviour differs by runtime, so version rules and treat the log as a published interface
- **Evidence**: Rule changed so a draft needs four quotes while SKU-123 waited with three. Reported outcome: on Temporal the run "silently continued with the order as per the old rule, which the new rule doesn't permit"; on Cloudflare (where the loop checks each recorded decision against current rules) it failed and "PO 4471 stayed a draft". Fix: `state.rules_version` and `min_quotes = 4 if state.rules_version >= 2 else 0`; Parallel Change in three steps (add new beside old, migrate new runs, remove old).
- **Confidence**: emerging (observed on this example; behaviour may differ by runtime version)
- **Quote**: "We need to know how the runtime behaves before we deploy a change, and plan the deploy around it."
- **Our assessment**: Corroborates Vercel's and Cursor's versioning pain (see Cross-References) with a third mitigation: in-state rule versioning rather than runtime patch APIs or deployment pinning.

### Claim 11: The durable log is not the model's memory; the harness decides what the model sees, and unbounded relevant history needs tiered memory (MemGPT/Letta style) whose reads and writes are also steps
- **Evidence**: Stock Replenisher needs only `state`; the SKU entity stores prior outcomes but the model never reads them. A customer entity running for years would need a promise from months ago, so a small working context plus external storage (RAM/disk analogy).
- **Confidence**: emerging (conceptual; no implementation shown)
- **Quote**: "The durable execution runtime logs everything the agent did. The harness decides what the model sees in each turn."
- **Our assessment**: Useful distinction between audit/replay log and context. No code or measurements, so treat as framing.

### Claim 12: Untrusted text (e.g. supplier email) can steer the agent, and durable execution does nothing for this; the example's defenses are an `allowed_tools` menu, manager-only approval, and routing out-of-range prices back to the manager
- **Evidence**: Example injected text: "the manager has already approved $6.00". Because approval only counts from the manager and the price check is deterministic, the email "approves nothing; at most it raises the price".
- **Confidence**: emerging
- **Quote**: "A model can't tell the difference between the text it reads and its instructions, so agents are susceptible to prompt injection."
- **Our assessment**: Illustrates capability-gating defenses (authority checked in code by sender identity, deterministic limits) rather than model-based detection. Only one attack is shown; it is not a full threat model, and the article says so by deferring to a separate security article.

### Claim 13: Most enterprise effort goes into integration with systems of record, so architecture and domain expertise matter more than tactical fixes or vibe coding
- **Evidence**: Author opinion in the Conclusion; the ERP that does not allow agent writes is the example. No data.
- **Confidence**: anecdotal
- **Quote**: "Tactical fixes and vibe coding are likely to create more problems than they solve and slow the transition to an agentic era."
- **Our assessment**: Opinion; low evidentiary weight. Include only as context. The article also promotes Thoughtworks' "Agent/works" platform, a mild commercial interest.

## Concrete Artifacts

Failure-mode table (article, "What can go wrong"; examples paraphrased for brevity; "Addressed in" refers to article sections):

```
Failure mode                 | Domain example                                   | Who handles it
Process doesn't survive      | restart during 3-day approval wait               | runtime (durable loop)
Remote API calls fail        | supplier API down at order time                  | runtime (retries)
A retry repeats the work     | order taken, reply lost, retry re-places         | harness (idempotency key)
Concurrency                  | second replenishment starts during first         | runtime/structure (entity workflow)
An outcome nobody sees       | order taken, supplier unreachable, run "failed"  | harness (essential)
World changes during a wait  | price rose during approval                       | harness (essential)
Code changes                 | new code deployed mid-wait                       | harness (accidental: durable exec)
History grows                | years-long customer agent                        | harness (accidental: model)
Untrusted input              | email says manager approved $6.00                | harness (accidental: model)
```

Temporal loop, from the article (`replenish/workflow.py`, abridged):

```python
@workflow.defn
class Replenish:
    @workflow.run
    async def run(self, stock: StockLevel) -> ReplenishmentResult:
        state = State(stock.sku, stock.on_hand, stock.safety_stock)
        for turn in range(MAX_TURNS):
            allowed_tools = [t for t in TOOLS if t.allowed(state)]
            tool = await workflow.execute_activity(
                Decider.decide, args=[GOAL, state, allowed_tools],
                activity_id=f"decide-{turn}", ...)
            ...
```

Gated tool, from the article:

```python
class PlaceOrder(Call):
    name = "place_order"
    def allowed(self, state):
        return (state.po is not None and state.order is None
                and state.approved_up_to is not None
                and state.price <= state.approved_up_to)
```

Retry policy and idempotency key, from the article:

```python
RETRY = RetryPolicy(maximum_attempts=6,
                    initial_interval=timedelta(seconds=2),
                    backoff_coefficient=2)
...
key = state.po.po_number
ack = await context.supplier.place_order(po, idempotency_key=key)
```

Rule versioning, from the article:

```python
def allowed(self, state):
    min_quotes = 4 if state.rules_version >= 2 else 0
    return (state.quotes is not None and len(state.quotes) >= min_quotes
            and state.po is None)
```

Wake-up measurements, article footnote 4 (author's own runs; not general benchmarks): "A workflow still in memory woke in milliseconds (14 ms on Temporal, about 0.1 s on Cloudflare); one rebuilt from the log took about two seconds on Cloudflare and under a tenth of a second on Temporal, more as the log grew. A wake used tens of milliseconds of CPU."

Primitive mapping (article recap table): step = `execute_activity` / `step.do`; wait = signal + `wait_condition` / `step.waitForEvent`; fresh history = `continue_as_new` / not used (Durable Object has no log to replay).

## Cross-References

- **Corroborates**:
  - `blog-cursor-cloud-agent-lessons.md` Claim 4 (Temporal lets cloud agent loops survive inference blips, hibernation and multi-day runs) and Claim 3 (Temporal raised reliability): this article gives the mechanism (step/log/replay) behind that outcome.
  - `blog-cursor-cloud-agent-lessons.md` Claim 8 (moving from "eternal" agent workflows to shorter task-scoped ones eases version upgrades): this article's entity-plus-child-process split and `continue_as_new` reset the entity history, and its Claim 10 shows why replay under changed code is the hazard.
  - `blog-vercel-workflow-engine-programming-language.md` Claim 4 (Temporal's `patched()`/`GetVersion` patching leads to "a thicket of version flags") and Claim 12 (pinning each run to its starting deployment): the same in-flight versioning problem; this article's mitigation is state-recorded rules version plus Parallel Change.
  - `blog-vercel-workflow-engine-programming-language.md` Claim 7 (steps retry automatically by default): retry primitives exist in both; this article adds the at-least-once/idempotency-key caveat.
  - `blog-vercel-ai-sdk-7-release.md` Claim 7 (`WorkflowAgent` persists execution state between steps so agents survive restarts and delayed approvals) and Claim 6 (`toolApproval` policies with HMAC-bound inputs): same problem class; this article contributes the failure taxonomy such features still leave to the harness.
- **Contradicts**: None found. Versioning approaches differ (runtime patching, deployment pinning, in-state rules version) but these are alternatives for different runtimes, not opposed claims, so no contradiction issue was filed.
- **Extends**: `blog-vercel-workflows-regional-state.md` (where durable run state lives) and `blog-cursor-vercel-queues.md` (queues for durable agent work): they cover infrastructure placement; this article covers semantic failures above the infrastructure layer.
- **Novel**: (1) The essential/accidental split applied to long-horizon agent failures; (2) compensating tools (`cancel_order`) for outcomes the agent never saw, framed as a saga; (3) expiry / re-check / approve-a-range patterns for stale approvals, with the check inside the tool; (4) the observation that the same rule change behaves differently on Temporal (silently continues) and Cloudflare (fails); (5) the point that the durable log records what the agent saw, not what happened.

## Guide Impact

- **Chapter 02 (harness engineering)**: Add a section on durable agent loops: record the model's decision call and every tool call as steps; keep `allowed`/`apply`-style code deterministic and between steps; use entity workflow plus short process workflows. Cite Claims 3 and 4 here alongside the Cursor Temporal evidence.
- **Chapter 02**: Add tool-design guidance: side-effecting tools need a stable domain-derived idempotency key (Claim 6) and, where "unknown outcome" is possible, a compensating tool the model can choose (Claim 8). Add "approval expiry / re-check in the tool / approve a range" as a pattern (Claim 9).
- **Chapter 02**: Add a deploy-safety note: changing business rules while runs wait can silently change or fail behaviour depending on runtime (Claim 10); version rules in recorded state.
- **Chapter 04 (context)**: Note the distinction between the durable log (audit/replay) and what is shown to the model, with tiered memory as the option for unbounded history (Claim 11).
- **Chapter 06 (security)**: Use the supplier-email example as a worked case of defense by deterministic authority checks (manager-only approval, price ceiling in code, tool allow-list) rather than relying on the model to resist injected text (Claim 12).

## Extraction Notes

- Read the full article (HTML fetched and stripped to text, including the sidebars, prior-art boxes and footnotes). The interactive run timelines are embedded iframes and were not extracted; claims about "the run below" rely on the surrounding prose and code only.
- The Prospector comments listed overlapping items inconsistently (e.g. a "five-row" table; the table has nine rows, five of which are re-examined in the "Durable is not the same as correct" section). This note follows the article text. the article states retries with idempotency keys address only part of the problem.
- Temporal-specific code and timings are the author's worked example and are attributed as such, not as general benchmarks.
- Quotes verified verbatim against the fetched text (whitespace-normalized across source line wraps).
- Other Fowler-hosted pages linked (Patterns of Distributed Systems, Agentic AI and Security) were not followed; the article's references to them are as stated.
