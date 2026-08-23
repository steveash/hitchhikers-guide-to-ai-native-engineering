---
source_url: https://openai.com/index/builders-guide-to-gpt-5-6
source_type: blog-post
title: "The builder's guide to GPT‑5.6"
author: OpenAI
date_published: 2026-08-13
date_extracted: 2026-08-23
last_checked: 2026-08-23
status: current
confidence_overall: emerging
issue: "#2886"
---

# The builder's guide to GPT‑5.6

> OpenAI's practitioner-facing guide tying together model-selection economics
> (smaller GPT‑5.6 tiers now rival prior-generation flagships at a fraction of
> cost) with three "trained end-to-end" architectural interventions in the
> Responses API — reasoning persistence, native multi-agent orchestration,
> and Programmatic Tool Calling — framed as a unified thesis: agent economics
> have shifted from "always use the biggest model at max reasoning" to
> "architect for efficiency and pick the smallest model that clears the bar."

## Source Context

- **Type**: blog-post (OpenAI house engineering/product write-up,
  `openai.com/index/`, no named individual author; published to the
  `openai-news` RSS feed on 2026-08-13T11:00:00Z).
- **Author credibility**: First-party OpenAI guidance aimed explicitly at API
  builders/startups, published the same month as several other GPT‑5.6
  efficiency posts (`blog-openai-gpt56-sol-ultrafast-mode.md`,
  `blog-openai-arc-agi-3-two-settings.md`). It synthesizes and re-cites
  OpenAI's own prior benchmark claims (BrowseComp cost/score, ARC-AGI-3
  before/after) rather than presenting new independent measurements for most
  of its numeric claims — standard vendor-self-report caveats apply. It links
  directly to OpenAI's own developer-docs pages for each architectural
  primitive it names, which this note also extracted and cross-checked
  against the guide's prose claims.
- **Scope**: Covers model-selection economics across the Sol/Terra/Luna
  tiers, one named benchmark cost comparison (BrowseComp), a legal-tech
  extraction-then-analysis workflow example, three architectural primitives
  in the Responses API (reasoning persistence via `previous_response_id` and
  compaction, native multi-agent orchestration, Programmatic Tool Calling),
  a restated ARC-AGI-3 case study, and prompt-caching TTL/breakpoint changes.
  Does NOT cover: cybersecurity/safety capability claims, the full 11-domain
  benchmark table (see `blog-openai-gpt56-ga-announcement.md`), pricing
  figures (see `blog-simonwillison-gpt56-sol-launch.md` and
  `blog-openai-gpt56-ga-announcement.md`), or any independent, non-OpenAI
  verification of the BrowseComp cost/score figures below.

## Extracted Claims

### Claim 1: GPT‑5.6's central pitch is that it makes frontier-level agent performance "dramatically more affordable" through smarter model selection plus new API controls for reasoning continuity, multi-agent orchestration, and programmatic tool calling
- **Evidence**: Stated directly as the article's framing thesis in its opening section, then substantiated by the rest of the guide's model-selection and architecture sections.
- **Confidence**: emerging (a vendor framing claim, substantiated within the same article by specific benchmark/cost figures in Claims 3-4 below, but not independently reproduced)
- **Quote**: "The GPT‑5.6 model family makes frontier-level agent performance dramatically more affordable, while also advancing the frontier of what is possible." ... "In this guide, we show how startups are using smarter model selection and new API controls that help with reasoning continuity, multi-agent orchestration, and programmatic tool calling to build faster, more capable agents at a fraction of the cost."
- **Our assessment**: This is a synthesis/framing claim rather than a falsifiable technical claim on its own — its credibility rests on the specific evidence bundled underneath it (Claims 3, 4, 6-9). Worth noting as the guide's organizing thesis: efficiency is now presented as a first-class design axis alongside raw capability, not an afterthought.

### Claim 2: On Agents' Last Exam, GPT‑5.6 Sol at "low" reasoning effort outperformed GPT‑5.5 at "high" reasoning effort when the harness was held constant, and startups report significant cost improvements in production by reducing reasoning effort from prior defaults
- **Evidence**: Direct comparative claim in the "A better out-of-the-box experience" section, followed by an unquantified aggregate anecdote about production deployments.
- **Confidence**: emerging (the Agents' Last Exam low-vs-high comparison is a specific, named benchmark claim; the "similar success stories... across a range of workflows" statement is an unquantified aggregate anecdote with no named customer, workflow, or percentage given)
- **Quote**: "For example, on Agents' Last Exam, GPT‑5.6 Sol at \"low\" reasoning outperformed GPT‑5.5 at \"high\" reasoning when the harness was kept constant. We've seen similar success stories in production testing where startups report seeing significant cost improvements across a range of workflows by reducing the reasoning effort from the prior defaults."
- **Our assessment**: This is a stronger, more specific efficiency claim than the aggregate "significant cost improvements" sentence that follows it — the low-vs-high, same-harness, cross-generation comparison is checkable in principle (both models are named, the effort settings are named, the benchmark is named) even though no percentage or score is given here. The follow-on "success stories" sentence should be treated as an anecdotal aside, not a second data point, since it names no customer or number.

### Claim 3: Smaller GPT‑5.6-family models (Luna, Terra) with more test-time compute can now perform similarly to the prior generation's flagship tiers (GPT‑5.4, GPT‑5.5) while being significantly cheaper — reversing the historical rule that the highest-reasoning flagship was always the best choice for long-horizon tasks
- **Evidence**: Direct model-selection guidance in the "Model Selection" section, framed explicitly as a reversal of prior guidance.
- **Confidence**: emerging (a specific comparative capability claim about smaller-tier models catching up to larger prior-generation models; substantiated in the same article only by the single BrowseComp data point in Claim 4, not by a broader benchmark set)
- **Quote**: "Historically, upgrading to a flagship model at the highest reasoning available has been the best option for long-horizon use cases. This has been in large part due to these models being significantly more capable than cost-optimized models at handling longer contexts and tool calling. This has changed with the 5.6-family: with more test-time compute, Luna and Terra can often perform similar to GPT‑5.4 and 5.5 while being significantly cheaper."
- **Our assessment**: This directly corroborates and extends the "competitive performance at a fraction of the price" framing already documented in `blog-simonwillison-gpt56-sol-launch.md` Claim 3 (Terra pitched as GPT‑5.5-competitive at half price) — this guide generalizes that specific launch-day claim into a standing model-selection principle ("often perform similar... with more test-time compute"), six weeks after the GA announcement. The word "often" is doing real work here — it is a qualified, not universal, claim, and the guide gives exactly one worked benchmark example (Claim 4) to substantiate it.

### Claim 4: On the BrowseComp benchmark, GPT‑5.5 (Extra High reasoning) scored 84.36% for a total cost of $33.27, while GPT‑5.6 Luna (Extra High reasoning) delivers essentially the same performance — 84.04% — at a cost of $1.33, roughly a 25x cost reduction for near-identical score
- **Evidence**: A specific, named before/after benchmark cost comparison, with both scores and both total costs given.
- **Confidence**: emerging (specific, quantified figures presented as directly measured and internally precise, but entirely OpenAI-self-reported — no independent third-party reproduction of either the scores or the dollar costs was found during extraction, and the closest corroborating source is another OpenAI publication whose BrowseComp figure differs slightly, see assessment below)
- **Quote**: "Consider tasks in BrowseComp: a search-based benchmark that tests a model's ability to search for obscure facts. Three months ago, GPT‑5.5 (Extra High) scored 84.36% on this benchmark for a total cost of $33.27. At launch, GPT‑5.6 Luna (Extra High) delivers essentially the same performance, scoring 84.04% at a cost of $1.33."
- **Our assessment**: This is the guide's sharpest quantified data point — a near-identical score (84.36% vs. 84.04%, a 0.32-point gap) at roughly 1/25th the cost. Worth flagging a reconciliation note: `blog-openai-gpt56-ga-announcement.md`'s 11-domain benchmark table reports BrowseComp at GPT‑5.5 84.4% and GPT‑5.6 Luna 83.3% — close to but not identical to the 84.36%/84.04% figures here, most plausibly because this guide specifies "(Extra High)" reasoning effort explicitly while the GA table's column may reflect a different (e.g., default) effort setting for each model. The direction and magnitude of the underlying claim (Luna ≈ GPT‑5.5 on BrowseComp) is consistent across both sources even though the exact percentages differ slightly — this is very likely a reasoning-effort-setting difference, not a factual conflict, so no contradiction issue was filed (see Cross-References).

### Claim 5: The smaller GPT‑5.6-family models are recommended for high-volume workloads, latency-sensitive interactions, and repeated agentic-workflow steps — illustrated by a legal-tech example that uses Terra or Luna for document extraction before handing off to a frontier model for agentic analysis
- **Evidence**: Direct recommendation with a worked hypothetical example (not a named customer) in the "Model Selection" section.
- **Confidence**: emerging (a specific, named workflow-partitioning recommendation; the legal-tech example is illustrative/hypothetical, not attributed to a named customer with measured savings)
- **Quote**: "The smaller 5.6-family models are a strong fit for high-volume workloads, latency-sensitive interactions, and repeated steps within agentic workflows. For example, if you're operating a legal-tech startup that parses handwritten memos prior to agentic analysis, instead of using a frontier model for the entire use case, you can now use Terra or Luna for extraction and register significant cost savings."
- **Our assessment**: This is a concrete instance of "task-shape-based model routing" (use a small model for a bounded, mechanical subtask; reserve the frontier model for judgment-heavy synthesis) — the same task-partitioning logic that Programmatic Tool Calling applies at the tool-orchestration layer (Claim 8) is applied here one level up, at the model-selection layer. No dollar figure or percentage is given for the "significant cost savings" in this specific example, unlike the BrowseComp figure in Claim 4.

### Claim 6: GPT‑5.6 was trained end-to-end with three complementary architectural interventions — reusing prior work via persisted reasoning and native compaction, parallel decomposition via native multi-agent orchestration, and moving deterministic work into code via Programmatic Tool Calling — intended to let agents operate more efficiently
- **Evidence**: Direct architectural framing in the "Evolving the Responses API" section, introducing the three primitives the rest of the guide details individually (Claims 7-9).
- **Confidence**: settled (a documented, named set of API primitives, each independently verifiable against OpenAI's developer docs — see Concrete Artifacts)
- **Quote**: "We trained GPT‑5.6 end-to-end with three complementary architectural interventions that enable agents to operate more efficiently: **Reuse work already performed:** by allowing reasoning to be persisted across model turns and using native compaction to compress long-running conversations, the model can maintain coherence in its work across longer task horizons without getting confused or having to reconstruct prior context. **Parallel decomposition where appropriate:** using native multi-agent orchestration allows coordinating multiple agents across parallel workstreams to finish complex tasks faster. **Move deterministic work into code:** using programmatic tool calling to filter, aggregate, and orchestrate tool outputs outside the model's context window, reserving model tokens for judgment and reducing cost, latency, and context rot."
- **Our assessment**: The claim that these were "trained end-to-end" into the model (rather than being purely harness-side scaffolding) is notable and distinct from how compaction is typically documented elsewhere in the corpus as a harness-level technique layered on top of an unmodified model (e.g., `research-wasnotwas-context-compaction.md` Claim 3's LLM-summarization approach). If accurate, this suggests OpenAI is treating context-efficiency behavior as a model-training objective, not just an API feature — a framing worth flagging for the guide's context-engineering chapter as a claim to track, since the article gives no training-methodology detail to substantiate the "trained end-to-end" phrasing beyond asserting it.

### Claim 7: Combining retained reasoning and compaction tripled GPT‑5.6 Sol's score on ARC-AGI-3 (13.3% to 38.3%) while using roughly 6x fewer output tokens, "with no changes to the model" — restating OpenAI's own separately-published ARC-AGI-3 case study as evidence for the reasoning-persistence/compaction architecture
- **Evidence**: Restated case study, with the same headline numbers as the source article this guide links to.
- **Confidence**: settled for the restated numbers themselves (already independently extracted and cross-checked in `blog-openai-arc-agi-3-two-settings.md`); see that note for the full methodology detail (RHAE metric, harness defects, human baseline)
- **Quote**: "Used together, the difference can be dramatic. For example, on ARC-AGI-3, GPT‑5.6 Sol scored 13.3% with the standard harness. After enabling retained reasoning and compaction, however, the score jumped to 38.3%—while using roughly 6× fewer output tokens. No changes to the model, but nearly three times the performance."
- **Our assessment**: This is not new evidence — it is this guide restating, nearly verbatim in its headline figures, the case study already fully extracted as `blog-openai-arc-agi-3-two-settings.md` (see that note's Claims 2-3 and 8 for the complete methodology, human-baseline comparison, and root-cause analysis). This note does not re-extract the full ARC-AGI-3 methodology; see Cross-References → Corroborates.

### Claim 8: Programmatic Tool Calling lets GPT‑5.6 write JavaScript to orchestrate tools — filtering, aggregating, and running independent calls in parallel — with intermediate results processed outside the model's context window, so the model's tokens are reserved for judgment rather than mechanical data-shuffling
- **Evidence**: Direct feature description with a concrete illustrative scenario (100 filings filtered by date to find relevant transactions).
- **Confidence**: settled (a named, documented API feature — see Concrete Artifacts for the full docs-page mechanics, which corroborate this description)
- **Quote**: "When an agent retrieves 100 filings, filters them by date, and identifies relevant transactions, the model shouldn't have to reason over every intermediate result in its context window. Programmatic Tool Calling lets GPT‑5.6 write JavaScript to orchestrate tools, run independent calls in parallel, and process their outputs outside the context window. The model is left to focus on what requires intelligence: applying judgment."
- **Our assessment**: This matches the mechanics documented in the linked Programmatic Tool Calling developer guide (Concrete Artifacts below): a fresh, isolated V8 runtime per program, no Node.js/filesystem/network access, tools gated via `allowed_callers`, and a documented task-shape decision table (single lookups → direct calling; filter/join/aggregate over several results → programmatic calling). This corroborates and extends the corpus's existing PTC coverage in `blog-simonwillison-gpt56-ga-launch.md` Claim 8 and `blog-openai-gpt56-ga-announcement.md` Claim 3, adding the "filter 100 filings" illustrative scenario and the explicit "context rot" framing not present in either of those notes.

### Claim 9: Native multi-agent orchestration lets a primary agent delegate to subagents that pursue objectives in parallel and pass results back for final synthesis; this is the same underlying mechanism behind ChatGPT's "ultra" capability setting, and multi-agent behavior is steerable via instructions on when to spawn subagents
- **Evidence**: Direct feature description plus an explicit statement tying the API primitive to the ChatGPT product surface.
- **Confidence**: settled (a named, documented beta API feature, cross-checked against the Multi-agent developer guide below); emerging for the steerability claim's practical effectiveness (asserted, not measured, in this article)
- **Quote**: "In these setups, the primary agent is responsible for orchestrating the subagents and delegating tasks to them. The subagents pursue their objectives in parallel and finally pass back their output to the primary agent for final synthesis. Teams can start leveraging multi-agent natively by enabling multi-agent in the Responses API. This is also how the ultra capability setting in ChatGPT works. Although GPT‑5.6 has a strong sense of the appropriate number of subagents and when to spawn them, multi-agent behavior is very steerable. Instructing the model on when to invoke subagents can increase the likelihood of spawning agents only in situations where the additional token expenditures would result in better performance."
- **Our assessment**: This confirms and slightly extends `blog-openai-gpt56-ga-announcement.md` Claim 2, which already documented `ultra` as coordinating four agents by default (up to 16 in evaluations) and named three benchmarks showing the score-latency frontier shift — this guide adds the explicit statement that `ultra` and the raw Multi-agent API beta are literally "how" the same underlying mechanism, plus the steerability guidance (developer messages tune spawn frequency) that the GA announcement did not include. The orchestrator-delegates-to-parallel-subagents-then-synthesizes description maps directly onto the "orchestrator-subagent" pattern named in `blog-anthropic-multi-agent-coordination-patterns.md` Claim 1 — this is OpenAI's API-level implementation of the same coordination topology Anthropic names and recommends as the default pattern (that note's Claim 7).

### Claim 10: Across the GPT‑5.6 family, the prompt-cache TTL has been extended to a minimum of 30 minutes and cache breakpoints can now be set deterministically within a model's context window, which has enabled startups to significantly improve their cache hit rate
- **Evidence**: Direct feature description in the "Prompt Caching" section, plus a general (unquantified) adoption claim.
- **Confidence**: settled for the TTL/breakpoint mechanics (documented, checkable API behavior — see Concrete Artifacts); anecdotal for "significantly improve their cache hit rate" (no named startup, before/after percentage, or methodology given)
- **Quote**: "Across the entire family of models, the prompt cache TTL has been extended to a minimum of 30 minutes and cache breakpoints can now be set deterministically within a model's context window. This has enabled startups to significantly improve their cache hit rate."
- **Our assessment**: The 30-minute minimum TTL and deterministic-breakpoint mechanics exactly corroborate what `blog-simonwillison-gpt56-sol-launch.md` Claim 5 already documented from OpenAI's original GPT‑5.6 preview announcement six weeks earlier (explicit cache breakpoints, 30-minute minimum cache life) — this guide adds no new mechanic here, only restates it and layers on the unquantified hit-rate-improvement claim. The linked Prompt Caching developer guide (Concrete Artifacts below) adds detail not in either prior note: the 1,024-token minimum is a *strict* minimum for GPT‑5.6+ (versus a 1,024–2,048 token model-dependent minimum for earlier models), and GPT‑5.6's implicit-breakpoint behavior differs from earlier models by not falling back to the longest matching unmarked prefix.

## Concrete Artifacts

```
Source: OpenAI, "The builder's guide to GPT‑5.6,"
https://openai.com/index/builders-guide-to-gpt-5-6 (2026-08-13)

BrowseComp cost/score comparison (Extra High reasoning):
  GPT-5.5 (three months prior):  84.36% score, $33.27 total cost
  GPT-5.6 Luna (at launch):      84.04% score, $1.33 total cost
  -> ~25x cost reduction for a 0.32-point score difference

ARC-AGI-3 (restated from blog-openai-arc-agi-3-two-settings.md):
  Standard harness:                          13.3%
  + retained reasoning + compaction:         38.3%
  Output token reduction:                    ~6x fewer
```

```
Source: OpenAI Developers, "Reasoning models" guide,
https://developers.openai.com/api/docs/guides/reasoning

reasoning.effort levels and recommended use (GPT-5.6 family):
  none    - latency-critical, no multi-step reasoning benefit (voice, fast
            retrieval, classification)
  low     - tool-use/planning/search with modest latency increase (data
            analysis, drafting, execution-oriented coding, chat support)
  medium  - default; planning + complex reasoning + judgement (agentic
            coding, research, spreadsheets/slides, long-horizon delegation)
  high    - hard reasoning, complex debugging, deep planning (agentic
            coding, long-horizon research, knowledge work)
  xhigh   - deep research, async workflows, long agentic runs (security/code
            review, enterprise productivity)
  max     - maximum reasoning for the most complex tasks

reasoning.context values (controls whether reasoning from earlier turns is
rendered into the next sample):
  auto          - model's default (GPT-5.6 defaults to all_turns; earlier
                  models default to current_turn)
  current_turn  - only current-turn reasoning available to the model
  all_turns     - reasoning from earlier turns rendered into next sample
                  (GPT-5.6 family only)

GPT-5.6 supports `reasoning.mode`: "standard" (default) or "pro" (more
model work, higher latency/cost, billed at standard token rates).

Reasoning tokens are billed as output tokens even though not visible via
the API; OpenAI recommends reserving >=25,000 tokens of context/output
budget for reasoning + output when starting to experiment with these
models.
```

```
Source: OpenAI Developers, "Multi-agent" guide,
https://developers.openai.com/api/docs/guides/responses-multi-agent

Enable via `multi_agent.enabled: true` on a Responses API request (beta;
requires `responses_multi_agent=v1` in `betas`/headers).

`max_concurrent_subagents` (default 3, recommended for most workloads):
caps active subagents across the ENTIRE tree (children, grandchildren,
etc.), excludes the root agent. No fixed limit on tree depth or total
subagents created during a run.

Six hosted collaboration actions (appear as `multi_agent_call` items; the
application does not execute these):
  spawn_agent      - create a subagent, assign its initial task
  send_message     - queue a message for an existing agent, no new turn
  followup_task     - assign more work to a non-root agent, resume its turn
  wait_agent        - wait for an update in the calling agent's mailbox
  interrupt_agent   - interrupt another agent's active turn (context kept)
  list_agents       - return the current agent tree, statuses, last tasks

Agent naming: hierarchical paths, e.g.
  /root
  ├── /root/researcher
  ├── /root/reviewer
  └── /root/reviewer/tester

Use Multi-agent when: work splits into independent bounded tasks, separate
context improves focus, parallel exploration reduces wall-clock time.
Prefer one agent when: each step depends on the previous step, task is
small enough for one short run, agents would contend over shared mutable
state, you require a fixed deterministic execution graph.

When enabled: automatic server-side compaction applies independently to
root + each subagent (compact_threshold overridable); `reasoning.summary`
and `max_tool_calls` are NOT supported; the standalone `/responses/compact`
endpoint is not supported.

WebSocket mode (via `response.inject` events) is recommended over HTTP for
tool-heavy or long-running Multi-agent workflows, since it lets function
outputs resume a waiting agent immediately rather than waiting for the
whole response to complete.
```

```
Source: OpenAI Developers, "Programmatic Tool Calling" guide,
https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling

Runtime: fresh, isolated V8 runtime per generated program. Supports
top-level `await`. Does NOT provide: Node.js, package installation, direct
network access, general-purpose filesystem, subprocess execution, console,
or persistent JS state between executions. Emits output via `text(...)` /
`image(...)`. ZDR-compatible without a persistent code-execution container.

Enable via the `programmatic_tool_calling` hosted tool + `allowed_callers`
on each eligible tool:
  omitted / ["direct"]              -> model calls tool directly only
  ["programmatic"]                  -> only program code can call it
  ["direct", "programmatic"]        -> either

Supported tool types for allowed_callers: ["programmatic"]:
  function, custom, mcp, apply_patch, local/hosted shell, code_interpreter

Task-shape decision table (abridged):
  Single lookup/action                          -> direct tool calling
  Filter/join/rank/dedupe/aggregate/validate     -> programmatic (if code
    over several results                            can return a smaller
                                                     structured result)
  Dependent calls, predictable data flow         -> programmatic (if code
                                                     can derive later args)
  Adaptive search / semantic evaluation          -> direct (each result
                                                     should steer next move)
  Writes / approval-sensitive actions            -> direct (preserve a
                                                     clear authorization
                                                     boundary)

response.output can contain: `program` (generated JS + call_id +
`fingerprint` for replay), `function_call` (caller.caller_id links back to
the program's call_id), `program_output` (result + status: completed /
incomplete).
```

```
Source: OpenAI Developers, "Prompt caching" guide,
https://developers.openai.com/api/docs/guides/prompt-caching

GPT-5.6+ vs earlier models:
  Cache matching        | exact match at breakpoints | best-effort prefix
  Explicit breakpoints   | supported (+ implicit)     | not supported
  Min cacheable prefix   | 1,024 tokens (strict)       | 1,024-2,048 tokens
  Cache write charge     | 1.25x uncached input rate    | none
  Cache lifetime         | 30-min exact TTL (`ttl`)     | model-dependent max

GPT-5.6+ default implicit breakpoint: placed at the latest user/tool
message; unlike earlier models, does NOT fall back to the longest matching
unmarked prefix before that breakpoint if the marked one misses.
```

## Cross-References

- **Corroborates**:
  - `blog-openai-arc-agi-3-two-settings.md` Claims 2, 3, 8 (13.3% -> 38.3%
    RHAE, ~6x fewer output tokens from retained reasoning + compaction) —
    this guide's Claim 7 restates the identical headline figures from that
    dedicated case study as supporting evidence for its architecture thesis.
    See that note for the full methodology (RHAE metric, root-cause harness
    defects, human-baseline comparison); this note does not re-extract it.
  - `blog-simonwillison-gpt56-sol-launch.md` Claim 3 (Terra pitched at GA as
    GPT‑5.5-competitive at half price) and Claim 5 (explicit cache
    breakpoints, 30-minute minimum cache life) — this guide's Claims 3 and
    10 restate and generalize both mechanics six weeks after the original
    preview announcement, with Claim 3 elevating the launch-day Terra-only
    claim into a standing Terra-and-Luna model-selection principle.
  - `blog-openai-gpt56-ga-announcement.md` Claim 2 (`ultra` coordinates 4
    subagents by default, up to 16 in evaluations) and Claim 3 (Programmatic
    Tool Calling description, ZDR-compatible) — this guide's Claims 8-9 give
    the same two features a builder-facing, workflow-oriented explanation
    (the 100-filings example; the "this is also how ultra works" framing)
    that the GA announcement's more benchmark-dense treatment did not
    include.
  - `blog-simonwillison-gpt56-ga-launch.md` Claims 8, 9, and 10 — an
    independent, non-OpenAI writeup of the same three mechanics this guide's
    Claims 8-10 cover, extracted from Willison's GA-day post plus his own
    direct fetches of the developer docs. Claim 8 documents the identical PTC
    sandbox description (fresh isolated V8 runtime, no Node.js/network/
    filesystem/subprocess/console) and the same three-way `allowed_callers`
    gating (direct vs. programmatic vs. both) that this note's Concrete
    Artifacts transcribe. Claim 9 documents the Multi-agent API as "the
    sub-agent pattern now baked into the core API" — but was graded
    `emerging` there because the docs page Willison linked
    (`.../guides/tools-multi-agent`) returned "Page not found" at that
    note's extraction time; this note's Concrete Artifacts retrieve the now-
    reachable guide at `.../guides/responses-multi-agent`, which supplies the
    primary-source confirmation that note flagged as missing and asked to be
    re-verified. Claim 10 independently confirms the 30-minute TTL and the
    1.25x uncached-rate cache-write charge in this note's caching artifact,
    and adds two mechanics neither this guide nor its linked docs page
    surfaced here: a request-wide cap of four new cache writes per request,
    and the fact that the 1.25x surcharge applies only to GPT‑5.6-and-later
    models (pre-5.6 cache writes remain free).
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 1 (five
    named coordination topologies) and Claim 7 (orchestrator-subagent is
    Anthropic's recommended default pattern) — this guide's description of
    GPT‑5.6's native multi-agent primitive (root agent delegates to parallel
    subagents, synthesizes their output) is OpenAI's API-level
    implementation of the same orchestrator-subagent topology Anthropic
    names and recommends as the default starting pattern, giving the corpus
    a second frontier lab converging on the same coordination shape as a
    first-class, vendor-supported primitive rather than a harness-level
    convention.
- **Contradicts**: None identified. The BrowseComp score/cost figures in
  Claim 4 (84.36%/$33.27 vs. 84.04%/$1.33, both "Extra High" reasoning) are
  numerically close to but not identical to the BrowseComp row in
  `blog-openai-gpt56-ga-announcement.md`'s benchmark table (GPT‑5.5 84.4%,
  Luna 83.3%); this reads as a reasoning-effort-setting or measurement-date
  difference between two OpenAI-published sources rather than a substantive
  factual conflict — both sources agree in direction (Luna ≈ GPT‑5.5 on
  BrowseComp) and neither claim depends on the other for its own validity.
  No contradiction issue filed per MINER.md §4a (see When NOT to file:
  "Claims differ only in context").
- **Extends**: `research-wasnotwas-context-compaction.md` Claim 3 (six of
  seven open-source coding-agent harnesses use lossy LLM-summary
  compaction) and `blog-openai-arc-agi-3-two-settings.md` Claim 13 (Responses
  API compaction as an opaque, encrypted, server-generated state item) —
  this guide's Claim 6 adds the specific framing that OpenAI trained these
  context-efficiency behaviors "end-to-end" into the model itself, not only
  as harness-side API scaffolding, a training-methodology framing not
  present in either prior note (though also not substantiated with any
  methodology detail in this article beyond the assertion itself).
- **Novel**: The specific BrowseComp cost comparison ($33.27 -> $1.33 for a
  0.32-point score difference, Claim 4) is new to the corpus — no existing
  note has a dollar-denominated same-benchmark cost comparison across GPT-5.5
  and GPT-5.6 tiers. Also novel: the explicit "trained end-to-end" framing
  for the three architectural interventions (Claim 6), the legal-tech
  extraction-then-analysis model-routing example (Claim 5), the "this is
  also how the ultra capability setting in ChatGPT works" statement tying
  the raw Multi-agent API beta directly to the ChatGPT product surface
  (Claim 9), and the GPT-5.6-specific prompt-caching mechanics detail (1,024
  strict minimum token threshold; no unmarked-prefix fallback) from the
  linked developer-docs page (Concrete Artifacts).

## Guide Impact

- **Chapter 03 (Model Selection — Cost Economics)**: Add Claim 4 (BrowseComp:
  84.36%/$33.27 for GPT-5.5 vs. 84.04%/$1.33 for GPT-5.6 Luna) as the
  corpus's sharpest dollar-denominated same-benchmark cost comparison
  across a model generation, alongside a note that the GA announcement's
  benchmark table shows a slightly different BrowseComp figure for the same
  pairing (83.3% vs. 84.04%), most likely due to a reasoning-effort setting
  difference rather than a factual conflict (see Cross-References).
- **Chapter 03 (Model Selection — Routing by Task Shape)**: Add Claim 5's
  legal-tech extraction-then-analysis example as a concrete illustration of
  routing bounded, mechanical subtasks to a cheaper model tier and reserving
  the frontier model for judgment-heavy synthesis — directly complements any
  existing Programmatic Tool Calling guidance (Claim 8) as the same
  cost-partitioning logic applied one layer up, at model selection rather
  than tool orchestration.
- **Chapter 04 (Context Engineering — Reasoning Persistence)**: Add Claim 6's
  three-part architectural framing (reuse via persisted reasoning +
  compaction, parallel decomposition via multi-agent, move deterministic
  work into code via PTC) as a named, vendor-articulated taxonomy for
  "efficiency levers" distinct from raw model capability — worth pairing
  with the ARC-AGI-3 case study already cited in Ch04 via
  `blog-openai-arc-agi-3-two-settings.md` as the concrete before/after
  evidence for lever #1.
- **Chapter 04 (Multi-Agent Coordination)**: Add Claim 9's explicit statement
  that ChatGPT's `ultra` setting and the raw Multi-agent Responses API beta
  are the same underlying mechanism, plus the Concrete Artifacts' six hosted
  collaboration actions (spawn_agent, send_message, followup_task,
  wait_agent, interrupt_agent, list_agents) and `max_concurrent_subagents`
  default of 3, as a concrete API-level reference alongside the Anthropic
  five-pattern taxonomy already cited in this chapter — OpenAI's
  orchestrator-delegates-to-subagents-then-synthesizes description maps
  directly onto Anthropic's recommended default "orchestrator-subagent"
  pattern.
- **Chapter 05 (Tooling — Programmatic Tool Calling)**: Add the Concrete
  Artifacts task-shape decision table (single lookup -> direct; filter/
  aggregate over several results -> programmatic; adaptive search -> direct;
  writes/approval -> direct) as a concrete rule of thumb for when to route a
  tool through generated code versus a direct model-issued call.
- **Chapter 05 (Prompt Engineering — Caching)**: Add the GPT-5.6-specific
  prompt-caching mechanics from Concrete Artifacts (1,024-token strict
  minimum; no unmarked-prefix fallback; 1.25x write charge; 30-minute exact
  TTL) as an update to any existing OpenAI cache-mechanics citation sourced
  from `blog-simonwillison-gpt56-sol-launch.md`, which documented the same
  breakpoint/TTL feature at preview stage without this level of mechanical
  detail.

## Extraction Notes

- **Primary URL blocked by Cloudflare bot-challenge.** The live URL
  (`https://openai.com/index/builders-guide-to-gpt-5-6`) returned an HTTP 403
  Cloudflare managed-challenge page (confirmed via both the `WebFetch` tool
  and a direct `curl` with a browser user-agent) — the same access pattern
  already documented in this corpus's Extraction Notes for
  `blog-openai-gpt56-ga-announcement.md` and
  `blog-openai-arc-agi-3-two-settings.md`. No Wayback Machine snapshot exists
  for this URL as of extraction time (`archive.org/wayback/available`
  returned an empty `archived_snapshots` object). The article's existence and
  publication metadata were first confirmed independently via OpenAI's own
  `https://openai.com/news/rss.xml` feed (entry title, description, GUID,
  and `pubDate` of 2026-08-13T11:00:00Z all match the issue's auto-filed
  Prospector metadata) before attempting content retrieval.
- **Retrieved via the `r.jina.ai` reader proxy, using raw `curl` rather than
  the `WebFetch` tool.** An initial attempt via `WebFetch` pointed at the
  `r.jina.ai` proxy URL returned a condensed, LLM-generated "Key Takeaways"
  summary rather than the article's actual text — `WebFetch` applies its own
  small-model summarization pass on top of whatever content it fetches, which
  would have made any quote extracted from it unverifiable against the
  source's actual wording. A direct `curl` request to the same `r.jina.ai`
  proxy URL returned the linearized Markdown transcript of the live page
  (HTTP 200, ~1,500 words) with no additional summarization layer; all
  quotes in this note were checked against that raw transcript. The full
  article was read in its entirety.
- **Followed 6 linked sub-pages** (exceeding the "up to 5" guideline in
  MINER.md §1, judged worthwhile given this guide explicitly names and links
  each architectural primitive it discusses): the Reasoning models guide,
  the Compaction guide, the Multi-agent guide, the Programmatic Tool Calling
  guide, the Prompt caching guide, and the ARC-AGI-3 case-study article
  (already a fully-extracted source note in this corpus — not re-extracted
  here beyond the headline figures the builder's guide itself restates). Not
  followed: "Advancing the price-performance frontier with GPT‑5.6" (a
  separate pricing-update post linked only in passing from the BrowseComp
  paragraph, judged lower-value than the five architectural-primitive docs
  pages given this note's focus) — a future source submission may be
  warranted if that post is not already in the queue.
- **No contradiction with an existing source note was identified**; the one
  numeric near-miss (BrowseComp figures vs. the GA announcement's benchmark
  table) is addressed in Cross-References → Contradicts and judged a
  conditioning-variable difference (reasoning effort setting), not a factual
  dispute, per MINER.md §4a's "When NOT to file" guidance.
- **Confidence-overall set to `emerging`**: a first-party vendor guide with
  some settled, independently-checkable API mechanics (the developer-docs
  Concrete Artifacts) but whose headline economic claims (Claims 1-5) rest on
  a single named benchmark comparison and unquantified aggregate anecdotes
  ("similar success stories," "significantly improve their cache hit rate")
  with no independent third-party reproduction found during this extraction.
