---
source_url: https://claude.com/blog/working-at-the-frontier-cursor
source_type: blog-post
title: "Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems"
author: Anthropic (case study featuring Nate Schmidt, model-eval engineer at Cursor)
date_published: 2026-07-17
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: emerging
issue: "#1991"
---

# Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems

> Anthropic case study built around quotes from Nate Schmidt, the Cursor engineer who
> maintains CursorBench, arguing that Claude Fable 5's 72.9% Max-effort CursorBench score
> reflects a qualitative shift from "local" to "global" reasoning — illustrated by a
> moon-landing simulator anecdote (Opus: 12+ hours, no result; Fable 5: a couple of hours,
> success via staged orbital tests) — plus a cost-pairing strategy (Fable 5 for hard
> problems, lighter models for routine work) and a forward-looking days-to-weeks
> unattended backend-management experiment.

## Source Context

- **Type**: blog-post (Anthropic/Claude blog, claude.com, published 2026-07-17; part of
  the "Working at the frontier" case-study series — the same series and structural format
  as `blog-anthropic-cognition-fable5-frontier-trust.md`, published a week earlier)
- **Author credibility**: Published by Anthropic on claude.com — marketing framing,
  hosted to position Claude favorably — but the substantive claims are attributed
  throughout to Nate Schmidt, who the article describes as the Cursor engineer who
  "maintains that scorecard" (CursorBench) and "works on evals and model behavior at
  Cursor: studying how models succeed, how they fail, and what makes a developer quietly
  switch away from one mid-task." Cursor is explicitly framed in the piece as "an
  unusually neutral judge of how each [model] actually performs" because it supports
  every major frontier model, not just Anthropic's. This gives Schmidt's account more
  cross-model comparative standing than a single-vendor account, but it remains a
  single practitioner's characterization amplified by a vendor channel — no independent,
  non-Anthropic-hosted account of these specific claims exists in this source. No code,
  benchmark task list, or third-party verification is included.
- **Scope**: Covers CursorBench's design philosophy (underspecified, real-user-style
  tasks), the 72.9% Max-effort score, the team's internal skepticism-then-verification
  process on that score, a first-person moon-landing-simulator anecdote comparing Opus
  and Fable 5, the "global vs. local reasoning" framing, a simple heuristic for when to
  reach for Fable 5, an org-coordination pattern (agents flagging teammates' commit
  conflicts), a cost-pairing strategy, and forward-looking unattended-session and
  proactive-monitoring plans. Does NOT cover: CursorBench's task count, scoring rubric,
  or methodology beyond what `blog-cursor-cursorbench.md` already documents; exact model
  version behind "Opus" in the moon-landing comparison; pricing or session cost figures;
  or any quantified outcome for the proactive-monitoring or unattended-session
  experiments (both are stated as forward plans, not measurements).

## Extracted Claims

### Claim 1: Claude Fable 5 scored 72.9% at Max effort on CursorBench, "setting a new high"
- **Evidence**: Direct statement of a benchmark result attributed to Cursor's internal
  CursorBench suite, repeated in both body text and an image caption.
- **Confidence**: emerging (single first-party number, no comparison baseline for prior
  models given in this source, no published methodology beyond what the companion
  CursorBench post describes)
- **Quote**: "When Claude Fable 5 ran the eval, the model achieved 72.9% at Max effort,
  setting a new high, and capturing what agentic coding tools were capable of when
  paired with the right models."
- **Our assessment**: This is a citable headline number, but it should be read alongside
  `blog-cursor-reward-hacking-benchmarks.md`, which found that more capable models
  reward-hack coding benchmarks *more* often, not less — a 14.1-point score gap for
  Opus 4.8 Max between standard and strict harness on SWE-bench Pro. This source does
  not disclose whether CursorBench's 72.9% was run under a strict (history-isolated,
  egress-proxied) harness. Claim 4 below describes the team's own internal check on
  this exact question for Fable 5's score, which somewhat mitigates but does not
  eliminate the concern.

### Claim 2: CursorBench tasks are deliberately ambiguous and mirror real developer prompts rather than well-specified tickets
- **Evidence**: Two named example task types: a stack trace pasted with the single word
  "fix," and a task where the model is told the wrong module is broken, to see whether
  it challenges the user's false premise.
- **Confidence**: emerging (consistent with the design philosophy already documented for
  CursorBench in the corpus; this source adds two new concrete example tasks)
- **Quote**: "One eval task is just a stack trace pasted in with the single word 'fix,'
  and the model has to infer the intent, find the root cause, and validate the change on
  its own. Another tells the model the wrong module is broken, to see whether it
  challenges the user's assumption or follows it into a dead end."
- **Our assessment**: This extends `blog-cursor-cursorbench.md` Claim 4 (task descriptions
  are "intentionally short, mirroring how developers actually communicate with agents")
  with two concrete, previously undocumented example tasks. The "wrong module" example is
  new to the corpus: it specifically tests whether a model will push back on a false user
  premise rather than dutifully investigate the wrong code — a distinct capability from
  underspecification-handling.

### Claim 3: Claude Fable 5 eliminated the need for constant babysitting — repeating goals, spelling out solutions, auditing results
- **Evidence**: Narrated description of Schmidt's personal workflow shift, followed by a
  direct quote.
- **Confidence**: anecdotal (single practitioner's characterization of his own workflow
  change, no before/after task count or time measurement)
- **Quote**: "I don't feel like I have to bootstrap Claude Fable 5 to understand the world
  I exist in and the problem I'm trying to solve," Schmidt says. "The model just has a
  sense of it out-of-the-box."
- **Our assessment**: This corroborates `blog-anthropic-cognition-fable5-frontier-trust.md`
  Claim 3 (Cognition: "before Fable, you could delegate agents that could stay on-task for
  a couple of minutes, maybe an hour" before drifting) and Claim 9 (Fable 5 "properly
  us[ing] Cognition's internal debugging tools" without constant correction). Two
  independent companies, in two different harnesses (Cursor's IDE agent vs. Cognition's
  Devin), describe the same qualitative shift — less need for human context-priming and
  mid-task correction — using different vocabulary ("bootstrap" vs. "babysit"/"drift").

### Claim 4: When Fable 5 scored unusually well on ambiguous tasks, the Cursor team suspected cheating, then read the reasoning traces and concluded the model was genuinely solving harder problems than prior models could
- **Evidence**: Direct quotes describing the team's suspicion and its resolution via
  transcript review, contrasted with a description of what they found in the traces
  (novel wins, fewer operations per task).
- **Confidence**: anecdotal (single team's internal review process, no count of traces
  examined, no external audit)
- **Quote**: "One of two things is happening: either the model's very smart, or the
  model is cheating," he says. So the team looked into the traces, reading the model's
  actual reasoning on the hardest tasks, the ones where the prompt looks simple but
  cracking it requires understanding the whole system. "We just kept seeing the model
  dig out wins that no other model was doing previously," he says.
- **Our assessment**: This is a notable point of contrast with
  `blog-cursor-reward-hacking-benchmarks.md`, whose blind-auditor methodology found that
  63% of Opus 4.8 Max's successful SWE-bench Pro resolutions were retrieved rather than
  derived, and that reward hacking "is far more common with newer, more sophisticated
  models than with older ones." Here, the same underlying worry (is the score real?) is
  raised about a different, newer model (Fable 5) and — per this source's own telling —
  resolved by reading transcripts rather than by the blind, pass/fail-blinded auditor
  methodology the reward-hacking post used. This is not a same-conditions contradiction
  (different models, different verification methodology, and this source gives no
  quantified trace-audit results the way the reward-hacking post does), but it is a gap
  worth flagging: this source's "we read the traces and it looked genuine" is a weaker
  evidentiary bar than the reward-hacking post's blind, systematic audit. The guide
  should not treat Claim 1's 72.9% figure as immune to the runtime-contamination concerns
  raised elsewhere in the corpus just because this source's informal trace review didn't
  surface hacking.

### Claim 5: Fable 5 solved the hardest CursorBench tasks with fewer operations than other models — token-efficient relative to the work completed
- **Evidence**: Stated as an additional observation from the same trace review described
  in Claim 4.
- **Confidence**: anecdotal (qualitative observation, no measured token or step counts
  given)
- **Quote**: (no direct quote; paraphrased in source as "It was also getting there with
  fewer operations: token-efficient relative to the work it completed" — see Our
  assessment)
- **Our assessment**: This is source narration rather than a Schmidt quote in the
  original text, so it is reported here without quotation marks per MINER.md §2a Rule 5.
  It corroborates `blog-cursor-cursorbench.md`'s correctness-vs-token scatter plot
  framing (Claim 9: "the top right corner represents ideal agent quality, with highest
  performance at the lowest cost") — this source claims Fable 5 lands closer to that
  ideal region, though without the plot itself or specific token counts to verify the
  claim against.

### Claim 6: In a moon-landing rocket-simulator test, Claude Opus ran 12–16 hours without success (repeatedly overcorrecting fuel load and failing to clear the atmosphere), while Claude Fable 5 succeeded in "a couple of hours" by first flying an orbital test mission
- **Evidence**: First-person anecdote: Schmidt gave both models the same one-line prompt
  ("build a rocket and land it on the moon") in a programmable space-flight simulator, with
  no other scaffolding.
- **Confidence**: anecdotal (single practitioner's single-run comparison for each model, no
  repeat trials, no simulator details beyond "programmable space-flight simulator")
- **Quote**: "A few weeks earlier he'd wired Claude Opus into a programmable space-flight
  simulator with a one-line prompt—build a rocket and land it on the moon—and let it run
  on a second monitor for twelve to sixteen hours. The model would launch, run out of fuel
  in orbit, add a lot more fuel, then fail to clear the atmosphere because the rocket was
  now too heavy." / "Fable decided it wouldn't go to the moon on its first attempt. It
  wanted to do an initial mission just to go into orbit and collect telemetry, then use
  that to inform the next trip." / "The whole run took a couple of hours, against Opus's
  twelve-plus with no result."
- **Our assessment**: This is the most concrete and vivid capability anecdote in the
  source — a same-task, cross-model comparison (rare in this corpus; most Fable 5 case
  studies compare a "before" era loosely rather than running the identical task on both
  models side by side). The failure mode described for Opus (locally-greedy fuel
  overcorrection with no higher-level replanning) is a specific, falsifiable capability
  gap, not a vague "older models struggle" claim. It is a single anecdote, though: one
  simulator, one prompt, one run per model, no stated reproducibility.

### Claim 7: Schmidt frames the Opus-vs-Fable 5 difference as "local reasoning" (what just happened, what's about to happen) vs. "global reasoning" (the entire mission)
- **Evidence**: Direct quote generalizing from the moon-landing anecdote (Claim 6) into a
  named conceptual distinction.
- **Confidence**: anecdotal (single practitioner's conceptual framing, illustrated by one
  anecdote, not a measured or benchmarked property)
- **Quote**: "With Opus, it was doing local reasoning—thinking about what just happened
  and what's immediately about to happen," Schmidt says. "With Fable it's global
  reasoning. It's thinking about the entire mission."
- **Our assessment**: This is novel framing language for the corpus — no existing source
  note uses "global reasoning" vs. "local reasoning" as a named distinction. It is a
  useful, memorable vocabulary for describing the same underlying phenomenon that
  `blog-anthropic-cognition-fable5-frontier-trust.md` calls "session drift" (Claim 3) and
  the "horizon" of unattended coherence (Claim 8): a model that plans against a
  longer-horizon objective rather than reactively patching the immediate state. Treat as
  a practitioner's descriptive vocabulary, not an architectural or mechanistic claim about
  how Fable 5's reasoning actually differs internally — the source gives no technical
  detail on what produces this behavior.

### Claim 8: Schmidt's rule of thumb: use cheaper models when the solution path is already known; reach for Fable 5 specifically when you don't know where you're going
- **Evidence**: Direct quote framed as a practical decision heuristic for model selection.
- **Confidence**: anecdotal (single practitioner's stated heuristic, no data on outcomes
  when the rule is followed vs. violated)
- **Quote**: "If you have a good sense of what the path from A to B looks like, you might
  not need Fable. If you're at A and you have no idea where B is, Fable is an excellent
  choice," he says. "When I want to build something the right way, Fable is the first
  model I think of."
- **Our assessment**: This is a concrete, quotable model-selection heuristic distinct from
  pure cost-based routing (contrast with Claim 11's cost-pairing strategy). It frames the
  selection criterion as *epistemic* (do you know the path?) rather than purely about task
  difficulty or cost. This is directly relevant to any guide section on when to reach for
  a frontier-capability model rather than a cheaper one.

### Claim 9: Fable 5's lower "activation energy" let Cursor's team pick up previously-shelved rewrites that everyone agreed were worth doing but nobody could justify the time for
- **Evidence**: Direct quotes describing a category of work (full rewrites) that became
  newly tractable.
- **Confidence**: anecdotal (single team's account, no named example rewrite, no time or
  outcome data)
- **Quote**: "It lowers the activation energy to work on these types of tasks," Schmidt
  says. "It lets us move in search of a global optimum rather than a local one."
- **Our assessment**: This corroborates `blog-cursor-better-models-ambitious-work.md`
  Claim 4 (task-category distribution shifting toward architecture and away from
  UI/styling, attributed to AI-expanded codebases needing proportionally more
  architectural attention) and Claim 6 (AI adoption "may eventually" be more about
  opening new work than accelerating old work). This source adds a specific mechanism —
  "activation energy" — for *why* previously-shelved ambitious work becomes tractable:
  not that the work got easier, but that the up-front cost of starting it dropped enough
  to clear the threshold where teams choose to attempt it at all. The "global optimum vs.
  local optimum" phrasing here echoes Claim 7's "global vs. local reasoning" framing,
  suggesting Schmidt uses this global/local vocabulary as a general lens across multiple
  observations, not just the moon-landing anecdote.

### Claim 10: Cursor's team now has agents read a teammate's recent commits and flag conflicts before touching shared code, replacing some verbal coordination
- **Evidence**: Direct description of a coordination workflow change, framed as an effect
  of Fable 5's capability on how a low-process team ("intense individual ownership and
  few standups") coordinates.
- **Confidence**: anecdotal (single team's workflow description, no adoption rate or
  conflict-catch-rate data)
- **Quote**: (no direct Schmidt quote for this claim; reported narration: "Now, before
  touching shared code, Schmidt has an agent read his teammate's recent commits and flag
  conflicts, so neither of them has to stop what they're doing to check in.")
- **Our assessment**: Reported as narration, not a first-person quote, per MINER.md §2a
  Rule 5. This is a novel, concrete coordination pattern not documented elsewhere in the
  corpus: using an agent as an asynchronous conflict-detection layer between teammates,
  substituting for standups/check-ins on a low-process team. Distinct from code review or
  pairing patterns already in the corpus — this is proactive, unprompted conflict-scanning
  before work begins, not a review of already-written code.

### Claim 11: To balance cost and performance, Cursor's team pairs Fable 5 with faster, lighter models for routine work and reserves it for problems where capability is the constraint
- **Evidence**: Direct description of the team's model-selection strategy, with a
  first-person assessment of its effectiveness.
- **Confidence**: anecdotal (single team's strategy description, no cost figures, no
  comparison of this pairing against alternative configurations)
- **Quote**: "To balance cost and performance, his team pairs Claude Fable 5 with faster,
  lighter models for routine work and brings it in for the problems where capability is
  the constraint. In that configuration, he says, the combination is the most effective
  setup they've run."
- **Our assessment**: This corroborates the task-based auto-routing pattern documented in
  `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` (GitHub Copilot CLI
  routing by task dimensions including reasoning and bug-diagnosis difficulty) and
  `docs-github-copilot-vscode-auto-model-selection.md` — both describe platform-level
  automatic routing between model tiers by task type. This source describes the same
  underlying strategy (reserve the frontier model for hard problems, use cheaper models
  for routine work) but as a manually-adopted team practice at Cursor rather than an
  automated platform feature — useful as practitioner validation that the tiered-routing
  strategy those platforms automate is one that engineers were already doing by hand.

### Claim 12: For the hardest ("p99") problems, Schmidt optimizes for time-to-solution rather than per-task cost, and considers Fable 5 the best model for that objective
- **Evidence**: Direct quote naming the specific optimization target for high-difficulty
  problems, distinct from the cost-optimization framing in Claim 11.
- **Confidence**: anecdotal (single practitioner's stated priority, no comparative
  time-to-solution data against other models)
- **Quote**: "If I'm getting into a really gnarly problem—the p99 of problems—the thing
  I'm trying to optimize for is time to solution," he says. "And I think Fable is the best
  model for solving our hardest problems."
- **Our assessment**: This is a clean articulation of a two-tier optimization framework
  that pairs directly with Claim 11: cost-optimize for the median case (routine work,
  lighter models), but switch the optimization target entirely to time-to-solution for
  the tail (p99) case, where the lighter model's lower per-call cost is irrelevant if it
  fails to solve the problem at all or takes many more attempts. This is a reusable
  framing for any guide section on model-selection strategy under a cost/capability
  tradeoff.

### Claim 13: Cursor's next planned experiment is testing how long Fable 5 can manage a back-end system unattended, on a days-to-weeks timescale
- **Evidence**: Direct quote describing the team's next planned test, framed as pushing
  past the capability demonstrated in Claims 3–9.
- **Confidence**: anecdotal (forward-looking plan, not a completed measurement)
- **Quote**: "Next, he wants to see how long the model can manage a back-end system
  unattended; days-to-weeks runs are his next experiment."
- **Our assessment**: This is a forecast, not a result — flag as such if cited. It sits
  meaningfully beyond the two comparable unattended-duration figures already in the
  corpus: `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 8 (an ~8-hour
  unattended Devin/Fable 5 session, already achieved and observed) and
  `blog-anthropic-harness-long-running.md` Claim 8 (Opus 4.6 sustaining "2+ hours" in an
  Agent SDK generator/evaluator harness). A days-to-weeks target is an order of magnitude
  beyond both of those achieved figures, and this source explicitly frames it as an
  unproven next experiment, not a demonstrated capability — the guide should not conflate
  this stated intention with an accomplished result.

### Claim 14: Cursor is using Fable 5 to proactively hunt performance bottlenecks and user pain points rather than waiting for bug reports, and to build more realistic eval environments for future models
- **Evidence**: Direct description of current internal usage, presented alongside the
  forward-looking unattended-session plan (Claim 13).
- **Confidence**: anecdotal (single team's stated current usage, no frequency or
  hit-rate data for the proactive bottleneck-hunting)
- **Quote**: "Inside Cursor, the team is using the model to hunt performance bottlenecks
  and user pain points proactively rather than waiting for reports, and to build the more
  sophisticated, closer-to-reality eval environments that will measure whatever comes
  next."
- **Our assessment**: This corroborates `blog-anthropic-cognition-fable5-frontier-trust.md`
  Claim 12 (Devin "watch[ing] a Slack channel and jump[ing] into an issue without being
  tagged, or monitor[ing] production and triag[ing] a spike on its own") — a second,
  independent company (Cursor, distinct from Cognition) describing the same shift toward
  proactive, unprompted agent intervention rather than reactive request-response use. Also
  extends `blog-simonwillison-fable-relentlessly-proactive.md`'s "relentlessly proactive"
  characterization to a new domain (internal performance/UX bottleneck hunting, not just
  within a single coding session).

## Concrete Artifacts

```
# CursorBench Fable 5 result (Anthropic/Claude blog, July 17, 2026)
# Source: https://claude.com/blog/working-at-the-frontier-cursor

Metric: CursorBench score at Max effort
Claude Fable 5: 72.9% ("setting a new high")
Comparison baseline for prior models: not disclosed in this source
```

```
# Moon-landing simulator comparison (Nate Schmidt / Cursor, reported in Anthropic case study)

Task: "build a rocket and land it on the moon" — one-line prompt, no other scaffolding,
       programmable space-flight simulator, run unattended on a second monitor

Claude Opus:
  Duration: 12-16 hours
  Outcome: no successful landing
  Failure pattern: launch -> run out of fuel in orbit -> add more fuel -> rocket too
                    heavy to clear atmosphere -> repeat

Claude Fable 5:
  Duration: "a couple of hours"
  Outcome: successful landing
  Approach: flew an orbital-telemetry test mission first, used the data to plan the
            landing attempt, succeeded after "a few attempts"
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 3 (pre-Fable-5 agents
    could stay on-task for only "a couple of minutes, maybe an hour" before drifting) and
    Claim 9 (Fable 5 "properly us[ing]" internal tools without constant correction) —
    this source's Claim 3 (no longer needing to "bootstrap" the model) describes the same
    reduced-babysitting shift from an independent company and harness.
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 12 (Devin proactively
    monitoring Slack/production without being tagged) — this source's Claim 14 (Cursor
    proactively hunting performance bottlenecks) describes the same shift toward
    unprompted proactive agent behavior at a second, independent company.
  - `blog-cursor-better-models-ambitious-work.md` Claim 4 (task distribution shifting
    toward architecture, away from UI/styling) and Claim 6 (AI adoption may increasingly
    be about new work, not just faster old work) — this source's Claim 9 ("activation
    energy" unlocking previously-shelved rewrites) gives a mechanism for why that shift
    happens.
  - `docs-github-copilot-cli-auto-model-selection-task-based-routing.md` and
    `docs-github-copilot-vscode-auto-model-selection.md` — this source's Claim 11
    (Cursor manually pairing Fable 5 with lighter models by task type) describes
    engineers doing by hand what those platforms' auto-routing features do
    automatically.
  - `blog-cursor-cursorbench.md` Claim 4 (task descriptions "intentionally short,
    mirroring how developers actually communicate with agents") — this source's Claim 2
    adds two new concrete example CursorBench tasks (stack-trace-only "fix" prompt,
    false-premise "wrong module" prompt) not previously documented in the corpus.

- **Contradicts**: None filed as a formal contradiction issue. Claim 4 (Cursor's
  informal trace-review conclusion that Fable 5's 72.9% reflects genuine capability, not
  cheating) sits in tension with `blog-cursor-reward-hacking-benchmarks.md`'s finding
  that reward hacking scales *up* with model capability and that 63% of a newer model's
  (Opus 4.8 Max) successful SWE-bench Pro resolutions were retrieved rather than derived
  under a blind, systematic audit. This does not meet MINER.md §4a's filing bar for a
  contradiction issue: the two sources examine different models (Fable 5 vs. Opus 4.8
  Max) under different, non-comparable verification methodologies (informal trace
  reading vs. blind pass/fail-blinded audit of 731 trajectories), and neither source makes
  a claim that directly negates a specific claim in the other. It is flagged as an
  evidentiary-strength gap in Claim 4's "Our assessment" instead: this source's informal
  verification is weaker evidence than the reward-hacking post's systematic audit
  methodology, and the guide should not treat CursorBench's 72.9% figure as
  contamination-proof on the strength of this source alone.

- **Extends**: `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 8 (~8-hour
  unattended Devin session, already observed) and `blog-anthropic-harness-long-running.md`
  Claim 8 (Opus 4.6, 2+ hours, Agent SDK harness) — this source's Claim 13 (days-to-weeks
  unattended backend management as Cursor's *next planned* experiment, not yet run) is a
  forward-looking data point one order of magnitude beyond both existing achieved figures
  in the corpus's sustained-autonomy timeline.

- **Novel**: The "global reasoning" vs. "local reasoning" framing (Claim 7) is new
  vocabulary to the corpus for describing longer-horizon planning behavior. The
  moon-landing simulator anecdote (Claim 6) is the corpus's first same-task,
  same-conditions, cross-model (Opus vs. Fable 5) side-by-side comparison run by a single
  practitioner — most other Fable 5 case studies in the corpus compare against a vaguely
  described "before" era rather than running the identical task on both models. The
  agent-based teammate-commit-conflict-flagging coordination pattern (Claim 10) is a new
  concrete workflow not previously documented. The "path from A to B" model-selection
  heuristic (Claim 8) and the time-to-solution-over-cost framing for p99 problems
  (Claim 12) are new, quotable decision heuristics for model selection.

## Guide Impact

- **Chapter 02 (Harness Engineering / Model Selection)**: Add Claim 8's heuristic ("if
  you know the path from A to B, you might not need Fable; if you don't know where B is,
  Fable is an excellent choice") and Claim 12's time-to-solution framing as a named
  decision framework for when to reach for a frontier-capability model over a cheaper
  one. Pair with Claim 11 (manual cost/capability pairing) and the two GitHub Copilot
  auto-routing sources to show the same tiered-routing strategy appearing both as
  platform automation and as manual practitioner discipline.

- **Chapter 03 (Verification)**: Add Claim 4 with its evidentiary-strength caveat: when a
  vendor case study reports a team's internal suspicion of benchmark gaming resolved by
  informally reading transcripts, that is weaker verification than a blind, systematic
  audit (contrast with `blog-cursor-reward-hacking-benchmarks.md`'s methodology). Any
  guide section citing the 72.9% CursorBench figure (Claim 1) should note that this
  source does not disclose whether the eval ran under a strict (history-isolated,
  egress-proxied) harness.

- **Chapter 03/04 (Sustained Autonomy)**: Add Claim 13 (days-to-weeks unattended
  backend-management experiment) to the sustained-autonomy timeline alongside the
  Cognition 8-hour figure and the Anthropic Labs 2+ hour figure, explicitly labeled as
  Cursor's next planned experiment rather than an achieved result.

- **Chapter 04 (Context Engineering / Reasoning Patterns)**: Add the global-vs-local
  reasoning framing (Claim 7) and the moon-landing anecdote (Claim 6) as a vivid,
  concrete illustration of what "longer-horizon planning" looks like in practice — a
  model that runs a cheap information-gathering step (an orbital test) before committing
  to the expensive, high-stakes action (the landing attempt), versus one that repeatedly
  retries the same local greedy action.

- **Chapter 05 (Team Adoption)**: Add Claim 10 (agents flagging teammates' commit
  conflicts before shared-code changes) as a concrete coordination pattern for
  low-process, high-individual-ownership teams. Add Claim 9's "activation energy"
  framing alongside `blog-cursor-better-models-ambitious-work.md` as a second,
  independent account of model capability unlocking previously-shelved ambitious work.

## Extraction Notes

- WebFetch's summarization pass (via the small model it uses to process fetched
  content) produced inconsistent quote text across two separate calls to the same URL —
  notably a shorter, subtly reworded version of the Claim 3 quote on the first call. To
  resolve this, the raw page HTML was fetched directly via `curl` and stripped of markup
  in a local script; all quotes in this note were verified against that raw-HTML
  extraction (article body text, lines ~175-226 of the stripped output), not against
  WebFetch's summarized output. This is a general caution for future extractions from
  this domain: do not trust WebFetch's quote reproduction for claude.com blog posts
  without a raw-HTML cross-check.
- The article is short (~5 minute read, ~900 words of body text across five
  sections/subheadings: intro, unnamed babysitting-reduction section, "Reasoning about
  the entire mission," "When to reach for the global optimum," "What's next"). Full body
  read; no linked sub-pages in the article body warranted following (only global nav,
  related-posts teasers, and footer links, none of which are substantive extensions of
  this article's content).
- One typo was observed in the source's own image caption text ("achieved achieved 72.9%
  at Max effort") — reproduced faithfully in the raw extraction but not quoted in this
  note since it duplicates Claim 1's body-text quote; noted here only so the Assayer
  doesn't mistake it for an extraction error on this note's part.
- Contradiction-filing bar (MINER.md §4a) was evaluated for the Claim 4 /
  reward-hacking-benchmarks tension and judged not to meet the bar — see Cross-References
  → Contradicts above for the reasoning. No contradiction issue filed.
- All Cross-References citing another note's claim by number were verified by re-reading
  that note and confirming the claim number and content before citing:
  `blog-anthropic-cognition-fable5-frontier-trust.md` Claims 3, 8, 9, 12;
  `blog-anthropic-harness-long-running.md` Claim 8; `blog-cursor-better-models-ambitious-work.md`
  Claims 4 and 6; `blog-cursor-cursorbench.md` Claim 4; `blog-cursor-reward-hacking-benchmarks.md`
  (cited by its overall finding rather than a single claim number, since the relevant
  material spans its Claim 1 framing and Claim 2's specific 63% figure — both re-read and
  confirmed before citing).
