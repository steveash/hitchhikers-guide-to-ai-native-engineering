---
source_url: https://openai.com/index/third-moment-research
source_type: blog-post
title: "How Third Moment Research runs 10,000 agents for 36+ hours"
author: OpenAI (customer story; named quotes from Third Moment co-founders Adam Khakhar and Jeffrey Yan)
date_published: 2026-10-14
date_extracted: 2026-10-26
last_checked: 2026-10-26
status: current
confidence_overall: anecdotal
issue: "#4349"
---

# How Third Moment Research runs 10,000 agents for 36+ hours

> An OpenAI customer story with a few specific harness details (Codex as a subagent inside an outer supervising harness, trajectory-mining to remove agent polling waste, agent-run penetration tests of the sandbox) wrapped in vendor-reported headline numbers that carry no methodology.

## Source Context

- **Type**: blog-post (OpenAI "Startup" customer story, published October 14, 2026; auto-discovered via the `openai-news` trusted feed).
- **Author credibility**: Vendor-authored marketing. Named co-founders (Adam Khakhar, Jeffrey Yan) are quoted, but there is no independent measurement and the piece promotes OpenAI models/products (GPT-6 family, Codex, Daybreak).
- **Scope**: Covers one deployment (quantitative-finance research agents), how Codex was used to fix an environment bottleneck, harness structure, model selection rationale, security testing, and a roadmap. Does NOT cover: crash/stuck-agent detection mechanics, checkpointing, cost figures, how "improves with use" is measured, retry/escalation thresholds, or failures.

## Extracted Claims

### Claim 1: Agents polling for a long-running tool wasted tokens and polluted context; fixing the tool's runtime (not the agent) was the remedy
- **Evidence**: Anecdote of Codex analysing thousands of recorded simulation trajectories with timestamps and the codebase; reported backtest speedup ~3 hours to ~3–5 minutes. Stat card: "97% Reduction in backtest time with Codex".
- **Confidence**: anecdotal
- **Quote**: "While waiting, agents repeatedly polled for completion, wasting tokens and filling their context with status checks."
- **Our assessment**: A credible and generalisable pattern: mine trajectories for wasted-turn patterns and fix the environment. Figures are vendor-reported with no before/after methodology. Note the 97% card is consistent with the 3h → 3–5min claim only roughly.

### Claim 2: Using a coding agent over recorded trajectories plus the codebase can locate environment bottlenecks and ship the fix
- **Evidence**: Same anecdote; Codex profiled the backtest, found a caching optimisation and memory-packing technique, "experimented with solutions and deployed the fix to production".
- **Confidence**: anecdotal
- **Quote**: "Codex uncovered a bottleneck: backtesting a trading strategy across a year of order-level US equity data took several hours."
- **Our assessment**: Interesting as an agent-improves-its-own-environment loop; the article does not say what human review gated the production deploy.

### Claim 3: To handle agents that stop early, Codex is wrapped as a subagent inside an outer harness that inspects the trajectory and decides retry / terminate / escalate to human
- **Evidence**: Architecture description only; no thresholds, rates, or examples.
- **Confidence**: anecdotal
- **Quote**: "The outer harness examines the trajectory when a task is left unfinished and determines whether to retry, terminate the job, or escalate to human review."
- **Our assessment**: The most directly relevant extractable pattern for the Prospector's "stuck agent" question, but thin: no detail on how "unfinished" is detected, retry caps, or how often escalation happens.

### Claim 4: The per-agent environment is the default Codex harness in Docker, with a large data volume, documentation, and a research repo with modular components
- **Evidence**: Configuration description (terabyte of data, modules for feature engineering, GPU-supported model training, trading strategies, simulation).
- **Confidence**: anecdotal
- **Quote**: "For quantitative research, the team runs the default Codex harness inside a Dockerized environment."
- **Our assessment**: Notable that they use the stock harness rather than a bespoke one; customisation is in the environment and the outer supervisor.

### Claim 5: The Codex harness gives agents plan, objective-setting, subagent-spawning, and context-compaction tools, which is how sessions stay coherent over days
- **Evidence**: Author statement plus a co-founder quote; no ablation.
- **Confidence**: anecdotal
- **Quote**: "In a single session, GPT-6.1 Sol is able to maintain a coherent thread of computational research across days of compute without losing the plot."
- **Our assessment**: The quote is a testimonial, not evidence. The article attributes persistence to compaction + subagents, but gives no data on compaction quality or failure.

### Claim 6: Model capability progression changed agent autonomy from executing prescribed experiments to designing follow-ups to root-cause investigation via parallel subagents
- **Evidence**: Co-founder's recollection ("Adam says"), tied to model versions GPT-5.5 → 5.6 → GPT-6 family.
- **Confidence**: anecdotal
- **Quote**: "Now with GPT‑6 Astra, GPT‑6 Sol, and GPT‑6.1 Sol, agents can investigate root causes through hundreds of experiments running in parallel with subagents."
- **Our assessment**: Consistent with the "harness assumptions go stale as models improve" theme, but it is one team's perception.

### Claim 7: Token efficiency, not peak benchmark score, drives day-to-day model choice; stronger models are reserved where signal value is high
- **Evidence**: Co-founder quote; tiered use (cheaper GPT-5.6 Terra for targeted checks; strongest reasoning for deep research); internal benchmark on reducing a scoreboard service's latency, measured as expert-solution runtime divided by model-solution runtime, subject to correctness (Astra won; no numbers).
- **Confidence**: anecdotal
- **Quote**: "GPT-6.1 Sol is currently our most-used model given its token efficiency. It completes tasks with the fewest tokens while delivering performance similar to GPT-6 Astra."
- **Our assessment**: Useful model-routing heuristic at 10,000-agent scale where tokens dominate cost; no cost numbers given, and the vendor is selling all these models.

### Claim 8: At scale, sandbox escape risk is tested by having agents themselves penetration-test the simulation environment before launch (Daybreak)
- **Evidence**: Co-founder statements; no findings reported.
- **Confidence**: anecdotal
- **Quote**: "The tests check whether an agent could break out of its research environment and access the wider network."
- **Our assessment**: Pre-launch automated adversarial testing of the agent environment is a good practice; this is also a product plug and reports zero results.

### Claim 9: The system improves agents by mining behavior for recurring weaknesses and generating synthetic scenarios around them, repeated as new issues emerge
- **Evidence**: Description of the company's approach only; "According to Adam, their work has improved the baseline trading system" is the sole outcome claim.
- **Confidence**: anecdotal
- **Quote**: "The team uses those scenarios to improve agents, repeating the process as new issues emerge."
- **Our assessment**: The "improve with use" headline is essentially unevidenced here. Treat as a stated design, not a result.

### Claim 10: Roadmap: hundreds of thousands of collaborating subagents and chains of dozens of dependent experiments
- **Evidence**: Stated ambition.
- **Confidence**: anecdotal
- **Quote**: "Third Moment plans to expand from individual investigations to hundreds of thousands of collaborating subagents."
- **Our assessment**: Aspirational; exclude from guide as evidence.

## Concrete Artifacts

Headline stat cards (OpenAI page, vendor-reported, no methodology):

```
10,000   Agents running concurrently
36–48    Hours per autonomous research session
97%      Reduction in backtest time with Codex
1        Trillion OpenAI tokens in a single day
```

Architecture as described (paraphrased diagram, not from source):

```
outer harness (GPT-6 Sol / GPT-6.1 Sol)
  └─ Codex harness as subagent (Docker; 1 TB data + docs + research repo)
        tools: plan, set objectives, spawn subagents, compact context
  on unfinished task: inspect trajectory -> retry | terminate | escalate to human
```

## Cross-References

- **Corroborates**: `blog-cursor-continual-harness-improvement.md` Claim 3 (context rot: wasted tool-call output degrades later decisions and wastes tokens) — Third Moment's polling-status-check pollution is the same failure from a different cause; `blog-anthropic-harness-long-running.md` Claim 9 (harness components encode assumptions about model limits that go stale) — Claim 6 here describes capability shifts changing what agents can do.
- **Contradicts**: None found. (Checked against `blog-anthropic-harness-long-running.md` Claim 7/8, which concern context anxiety; this source does not report that behaviour or its absence.)
- **Extends**: `blog-anthropic-harness-long-running.md` — adds an outer supervisory harness with retry/terminate/escalate, versus its planner/generator/evaluator split; `blog-cursor-continual-harness-improvement.md` Claim 13 (log scanning to find and remediate degradation) — similar trajectory-mining loop, here also fixing the environment.
- **Novel**: Wrapping an off-the-shelf coding harness as a subagent of an outer supervisor; trajectory-mining to find tool-latency-induced polling waste; agent-driven pen-testing of the agent sandbox before launch at 10,000-agent scale.

## Guide Impact

- **Long-running agents / orchestration chapters**: Could cite the outer-harness retry/terminate/escalate pattern as one reported design for unfinished tasks, flagged as anecdotal and lacking thresholds.
- **Context/tooling chapters**: Add "slow tools cause polling loops that burn context; fix the tool or provide blocking/async completion" as an example, citing this source alongside Cursor's context-rot claim.
- **Security/sandboxing chapters**: Mention pre-launch agent-driven penetration testing of the agent environment as a reported practice; do not cite as evidence of efficacy.
- Do not use the headline numbers (10,000 agents, 97%, 1T tokens) as evidence; they are unmethodologised.

## Extraction Notes

- The OpenAI page returns a JS/cookie gate to curl and HTTP 403 to WebFetch. The full article text was read from an Internet Archive (Wayback) snapshot of the same URL; quotes were taken from that copy. Chart/figure content beyond the stat cards was not visible.
- No sub-pages followed; the article links only to the company site and related OpenAI posts.
- The Prospector's questions about checkpointing, crashed-agent restarts, state persistence across the run, and cost/error metrics are NOT answered by the article. It is mostly a customer story with a few specific harness details.
- Cross-referenced claim numbers were verified against the cited notes' `### Claim N` headings.
