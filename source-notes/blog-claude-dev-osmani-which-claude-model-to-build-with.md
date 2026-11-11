---
source_url: https://claude.dev/blog/which-claude-model-should-you-build-with/
source_type: blog-post
title: "Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku"
author: Addy Osmani (Claude blog, Playbooks)
date_published: 2026-11-09
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: emerging
issue: "#4639"
---

# Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku

> Anthropic's playbook for model and effort choice: start on Opus 5.5 at medium, escalate in a fixed order (self-verification, then effort, then model), and mix models only at natural breaks, with per-model cache and thinking-block mechanics that make switching costly.

## Source Context

- **Type**: blog-post (vendor playbook, claude.dev Blog, 15 min read)
- **Author credibility**: Addy Osmani writes the claude.dev model guides (see the Opus 5.5 and Sonnet 5.5 notes). The post is Anthropic first-party. It draws on Anthropic's own benchmark runs and internal cost guides, so figures are vendor-reported, not independent.
- **Scope**: Covers the four GA models (Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.2; Mythos 5.2 only mentioned), a task-to-model table, pricing, cost/latency/context trade-offs, subagent pinning, advisor and orchestrator patterns, API compatibility gotchas, and a measurement procedure. It does not give new benchmark methodology; it points to the Fable 5.2 page and launch post for results.

## Extracted Claims

### Claim 1: Start most work on Opus 5.5 at medium effort; move down or up by task type
- **Evidence**: Task-to-model table in the post; pricing (Opus 5.5 is half Fable 5.2's per-token price).
- **Confidence**: emerging (vendor guidance, supported by benchmark examples below)
- **Quote**: "The quick answer is that you should start most work on Opus 5.5 at its default effort level, medium ."
- **Our assessment**: A concrete default. It differs from the claude.com explainer's "start with the most intelligent generally available model" (contradiction filed as #4657). Note the post itself says well-specified work can still need Opus or Fable ("A migration or a performance optimization can have clear specs and still be difficult enough to warrant Opus 5.5"), so spec clarity alone is not the routing signal.

### Claim 2: Escalation order when a model is not good enough: self-verification, then one effort level, then the next model at lower effort
- **Evidence**: Stated procedure; supported by the SWE-bench Pro effort numbers (Claim 3).
- **Confidence**: emerging
- **Quote**: "Often providing a means of self-verification is more cost effective and adds less latency than changing effort levels."
- **Our assessment**: Useful ordered rule. The three steps are: (1) check the model can verify its own work with a test, build or endpoint-calling script; (2) raise effort one level; (3) move up a model, "starting at a lower effort level than you used on the smaller one." It ranks verification above model choice, which fits the guide's verification chapter. Not independently tested.

### Claim 3: Effort has steep cost curves on SWE-bench Pro for Opus 5.5
- **Evidence**: Anthropic-run SWE-bench Pro numbers, relative to high effort.
- **Confidence**: emerging (vendor-reported, no raw table, single benchmark)
- **Quote**: "on SWE-bench Pro, Opus 5.5 at medium scored about 2.5 points lower for about 70% of the cost as the high effort setting. At low it scored about 8 points lower for about a third of the cost. At xhigh it scored about 1.4 points higher for 2.5 times the cost of high ."
- **Our assessment**: Gives diminishing returns past high with numbers. Only deltas are provided, no absolute scores, so we cannot reconstruct the curve.

### Claim 4: Low effort with automatic re-run of failures at high beat all-high on cost and pass rate
- **Evidence**: Same SWE-bench Pro subset: ~97% at ~$0.17/task vs. 95.3% at $0.29/task.
- **Confidence**: emerging (single subset, requires automatic outcome checks)
- **Quote**: "If you can check outcomes automatically, run everything at a low level and re-run only the failures at a high one."
- **Our assessment**: A cascade pattern whose precondition is a reliable automated verifier. Matches the "verify first" ordering in Claim 2. Does not report how pass rates were counted for the re-run (e.g., whether failure detection used ground-truth tests, which would flatter the result). Treat as an upper bound.

### Claim 5: At the hardest tier the model price gap can close; test Fable 5.2 before raising Opus past high
- **Evidence**: FrontierCode 2.0 (45.3% vs 45.5%, about half the cost per task); Terminal-Bench 3.0 (Fable 5.1 at max 58.0% vs Opus 5.5 at high 58.9% with half the tokens, cited from "Spending your effort").
- **Confidence**: emerging
- **Quote**: "On FrontierCode 2.0, Fable 5.2 at high scored about level with Opus 5.5 at max (45.3% vs. 45.5%) for roughly half the cost per task."
- **Our assessment**: Strong for the claim that per-token price does not equal per-task cost. Both benchmarks are Anthropic's own runs. Practical rule: past high, compare "one more effort level" against "next model at lower effort."

### Claim 6: Price the hardest tasks, because they dominate spend
- **Evidence**: One 20-problem search benchmark.
- **Confidence**: anecdotal (single example)
- **Quote**: "On one 20-problem search benchmark, two problems carried 43% of the spend."
- **Our assessment**: Good evaluation hygiene: cost comparisons on average tasks understate the tail. One data point, but the mechanism is plausible.

### Claim 7: Large context is paid on every turn, but most is billed as cache reads; keep the big model's context lean
- **Evidence**: Price table (cache read $0.20/M on Opus 5.5 and Fable 5.2, $0.10 Sonnet 5.5); cost example from the "What a task costs on Opus 5.5" post: a cache read costs about $0.03 at 150K context, about $0.004 at 20K.
- **Confidence**: emerging
- **Quote**: "One takeaway from this is that a lean main context matters more the bigger the main model is."
- **Our assessment**: Pairs with subagent delegation (Claim 11). Also notes that on cache-heavy runs the Fable/Opus gap collapses to uncached input and output, where Fable costs twice as much.

### Claim 8: Haiku 5.5 is the only model with prompt-length-tiered pricing; compare on cost per finished task for long prompts
- **Evidence**: Price table: $0.10/$0.50 per M up to 100K prompt tokens, $0.50/$2.50 above.
- **Confidence**: settled (published list prices)
- **Quote**: "Haiku 5.5 is the only model where the token price varies by prompt length."
- **Our assessment**: The post says the long tier is still a quarter of Sonnet 5.5's per-token price and short prompts cost a twentieth of Sonnet's input price. The break-even depends on Haiku needing more retries, which the post tells readers to measure rather than gives.

### Claim 9: The prompt cache belongs to the model that wrote it; switch models at natural breaks, after /compact or with a written plan
- **Evidence**: Product mechanics stated by the vendor.
- **Confidence**: settled (vendor-documented behaviour)
- **Quote**: "The prompt cache belongs to the model that wrote it. Your first turn on a new model pays the cache-write price on the whole conversation."
- **Our assessment**: Directly affects mid-session `/model` switching and per-turn routers. Mitigations given: run `/compact` first in Claude Code, start a fresh session with a short written plan, or on the API open with a summary rather than full history.

### Claim 10: Thinking blocks are model-bound; moving down a tier, or from Fable 5.2 to any other GA model, drops earlier reasoning (request still succeeds)
- **Evidence**: Compatibility matrix in the post: Opus 5.5 reads Sonnet 5.5 and Haiku 5.5 blocks; Sonnet 5.5 reads Haiku 5.5; Fable 5.2 reads Opus 5.5, Sonnet 5.5 and Haiku 5.5; Fable 5.1 reads Opus 5.5 (Claude API).
- **Confidence**: settled (vendor documentation, referenced to the Preserved thinking page)
- **Quote**: "A move down a tier loses the earlier reasoning, because a model never reads the blocks of a model above it."
- **Our assessment**: Silent loss is the hazard: "the API drops them and the request still succeeds." Extends the Sonnet 5.5 note's narrower statement that only Sonnet 5 to 5.5 keeps reasoning.

### Claim 11: Pin subagents to cheaper models, and keep code edits and judgment on the main model
- **Evidence**: Agent definition example; `CLAUDE_CODE_SUBAGENT_MODEL` default; rationale about misread search results.
- **Confidence**: emerging
- **Quote**: "Keep small models on work where a mistake is cheap to spot, like finding files, running tests and reading logs."
- **Our assessment**: Concrete, checkable config. Includes caveats: the built-in Explore subagent now runs on the session's model (capped at Opus on the API), so define your own `Explore` with `model: haiku` to keep it cheap. It also warns that `opusplan` puts edits on Sonnet, the reverse of this advice, and should be measured before adoption.

### Claim 12: The `haiku` alias now resolves to Haiku 5.5 on the Anthropic API only (Claude Code v2.1.293+); cloud providers still resolve to Haiku 4.5
- **Evidence**: Stated version/provider detail.
- **Confidence**: settled for the date of the post
- **Quote**: "On Amazon Bedrock, Google Cloud, Microsoft Foundry and Claude Platform on AWS, it still resolves to Haiku 4.5."
- **Our assessment**: A silent provider-dependent behaviour difference that matters for subagent pinning in enterprise setups. Pin with `ANTHROPIC_DEFAULT_HAIKU_MODEL` for consistency. Will age quickly.

### Claim 13: The advisor tool (beta) did not clearly beat the executor alone in the platform's own cost guide
- **Evidence**: Opus 5.5 high executor with Fable 5.1 advisor: 90.1% at $2.92 per attempt, 1.7 points over Opus 5.5 alone at high for about 2.1 times the money; pairing restrictions (a Fable 5.2 executor accepts only Fable 5.2 or Mythos 5.2).
- **Confidence**: emerging
- **Quote**: "of the four pairings in its advisor table, none clearly beat its executor alone, and an advisor can help only when the executor consults it."
- **Our assessment**: Tempers the more optimistic advisor result in the claude.com explainer (Sonnet 5 plus Fable 5 advisor within 10% of Fable 5 at 63% of price). Different pairings and benchmarks, so not a strict contradiction. The post says to measure the executor's consult rate first.

### Claim 14: Opus lead with Sonnet workers cut cost by about a third on bulk work at about the same score
- **Evidence**: Internal defect-search benchmark over about 22 million tokens of source, up to 25 parallel Sonnet 5.5 workers, versus Opus 5.5 alone at default effort.
- **Confidence**: anecdotal (internal benchmark, no details)
- **Quote**: "Skip it for one chain of dependent steps or for work that fits in one context window."
- **Our assessment**: The useful part is the boundary condition: orchestration only pays off for work larger than one context window. Consistent with the fold-subagents note's skepticism.

### Claim 15: Build requests for the strictest model if one system uses several; let code, not a model, pick the model for simple routing rules
- **Evidence**: Compatibility list: Fable 5.2 returns 400 if earlier history (system prompt, tools, earlier message) changes before a thinking block; Opus 5.5 and Fable 5.2 always think; `tool_choice` `any`/`tool` returns 400 on Sonnet 5.5, Opus 5.5 and Fable 5.2; Haiku 4.5 to 5.5 needs `budget_tokens` replaced with effort and non-default `temperature`/`top_p`/`top_k` removed.
- **Confidence**: settled (API behaviour, vendor-documented)
- **Quote**: "When the routing rule is simple, such as one model for each step type, let code pick the model rather than asking a model to."
- **Our assessment**: Concrete migration checklist. The append-only history requirement is the least obvious one for custom harnesses.

### Claim 16: Measure on your own tasks; keep a multi-model setup only if it beats every single-model point on a score-vs-spend plot
- **Evidence**: A four-step procedure.
- **Confidence**: emerging
- **Quote**: "Plot score against spend. Keep a multi-model setup only if it beats every single-model point on that chart."
- **Our assessment**: A clear acceptance test for routers. Also says to run each candidate in its own session so runs do not share a cache.

## Concrete Artifacts

Subagent definition (source: "Put subagents on smaller models"):

```
---
name: log-reader
description: Reads test output and logs, and reports each failing case. Use after a test run.
tools: Read, Grep, Glob, Bash
model: haiku
---
Read the logs you're given. For each failure, report the file, the test name and the first error line. Don't edit any files.
```

API list prices per million tokens (source: "The four models side by side"; input/output):

```
Haiku 5.5   $0.10 / $0.50 (<=100K prompt), $0.50 / $2.50 (>100K); cache read $0.01 / $0.05
Sonnet 5.5  $2 / $10;  cache read $0.10
Opus 5.5    $4 / $20;  cache read $0.20; fast mode: yes
Fable 5.2   $8 / $40;  cache read $0.20; fast mode: yes
All: 1M context, 128K max output.
Default effort on API: Haiku medium; Sonnet high (medium in Claude Code); Opus medium; Fable high (medium in Claude Code)
```

Task-to-model routing (condensed from the post's table):

```
Everyday engineering / multi-PR work     Opus 5.5, medium then high
Classification, routing, extraction      Haiku 5.5, medium
Subagents (search, logs, summaries)      Haiku 5.5 or Sonnet 5.5
Chat / interactive                       Sonnet 5.5, low or medium
Well-scoped coding / spec-driven         Sonnet 5.5, medium then high
Repeated agent tasks (review, drafting)  Sonnet 5.5, medium
Computer use / vision-heavy              Opus 5.5, medium
Major refactors, migrations, architecture,
  leading many subagents, deep research  Fable 5.2, medium then high (API default high)
Unsure                                   Opus 5.5, medium
```

Effort figures, Opus 5.5 on SWE-bench Pro vs. high (source: "Latency against accuracy"): medium about -2.5 pts at ~70% cost; low about -8 pts at ~1/3 cost; xhigh about +1.4 pts at 2.5x cost. Low with failures re-run at high: ~97% at ~$0.17/task vs. 95.3% at $0.29/task all-high.

## Cross-References

- **Corroborates**: `blog-claude-dev-thariq-spending-your-effort.md` Claim 3 (each effort level yields benchmark and token uplift) and Claim 9 (more effort does not fix a wrong approach); this post says effort "won't give a model knowledge or skill it doesn't have." `blog-claude-dev-osmani-building-with-sonnet-55.md` Claim 4 (forced `tool_choice` returns 400), Claim 6 (computer-use toolset), and Claim 16 (Sonnet for well-scoped work with a way to check). `blog-anthropic-choosing-claude-model.md` Claim 7 (effort is a second axis; higher class at lower effort can be more efficient) matches the "test the next model at a lower effort" rule. `blog-anthropic-choosing-claude-model.md` Claim 9 (custom evals) matches the "measure on your own work" section.
- **Contradicts**: `blog-anthropic-choosing-claude-model.md` Claim 1 recommends starting with "the most intelligent generally available model"; this post says start on Opus 5.5 at medium. Filed as #4657. No verdict is assigned here. Claim 13 here (advisor pairings not clearly beating the executor alone) is in tension with Claim 8 of that note (Sonnet 5 plus Fable 5 advisor within 10% at 63% of price) but the pairings and benchmarks differ, so it is recorded as a conditioning difference, not filed.
- **Extends**: `blog-claude-dev-osmani-building-with-sonnet-55.md` Claim 5 (thinking blocks model-bound; only Sonnet 5 to 5.5 keeps reasoning) with the full cross-model read matrix and the Fable 5.2 drop rule; Claim 14 (effort change invalidates cache) with the model-switch cache-write cost. `blog-claude-dev-osmani-getting-the-most-out-of-opus-55.md` Claim 14 (fast mode) with fast-mode availability across the four models (Opus and Fable only). `blog-anthropic-fold-subagents-into-main-agent-loop.md` Claim 2 (subagents justified under specific conditions) with a cost-based reason (cheap models on verbose reads) and the one-context-window boundary for orchestration. `blog-anthropic-safely-scaling-multi-agent-teams-fable-5-2.md` is a same-day sibling post; it covers Fable 5.2 team safety, not model choice.
- **Novel**: The three-step escalation ladder with SWE-bench Pro effort deltas; low-then-rerun-failures cascade numbers; the Fable 5.2 vs. Opus 5.5 at max FrontierCode 2.0 comparison; cache-per-model switch cost; full thinking-block compatibility matrix; Explore-subagent model change and `haiku` alias provider split; the `opusplan` caution; Haiku's 5x long-prompt tier.

## Guide Impact

- **Chapter 01**: Add the Opus 5.5 medium default and the "self-verification, then effort, then model at lower effort" ladder to model-choice guidance, and present it alongside the claude.com "start with the most capable" position pending resolution of #4657. Cite the effort-cost deltas as vendor-reported.
- **Chapter 02**: In the subagent section, add `model: haiku` pinning, `CLAUDE_CODE_SUBAGENT_MODEL`, the Explore-subagent behaviour change, and the `haiku` alias provider split. Add the warning that `opusplan` moves edits to Sonnet.
- **Chapter 03**: Reference the low-effort-plus-rerun-failures cascade as a verification-driven cost pattern that only works with automated outcome checks.
- **Chapter 04**: Note that prompt caches are per model (first turn after a switch pays a full cache write), that thinking blocks do not transfer downward, and that lean main context matters more as the main model gets bigger.

## Extraction Notes

- Fetched the full page HTML and read the whole article (about 21K characters of text). Followed no linked pages; the linked posts (Spending your effort, What a task costs on Opus 5.5, Preserved thinking) are either already in the corpus or only cited for figures, which are marked as vendor-reported here.
- Quotes were copied from the extracted page text; the page renders some inline code with stray spaces (e.g. "medium ."), which are preserved in quotes.
- All benchmark and cost figures are Anthropic's own and not independently verified. Triage comments mentioned a "up to 30% faster" Fable 5.2 claim (the post says "Fable 5.2 generates output up to 30% faster than Fable 5.1") and Sonnet 5.5 30% faster than Sonnet 5; these are noted only here as unquantified vendor claims.
