---
source_url: https://developers.googleblog.com/driving-the-agent-quality-flywheel-from-your-coding-agent/
source_type: blog-post
title: "Driving the Agent Quality Flywheel from Your Coding Agent"
author: Dima Melnyk (Product Manager, Cloud AI), Jason Dai (Software Engineer)
date_published: 2026-06-30
date_extracted: 2026-07-10
last_checked: 2026-07-10
status: current
confidence_overall: emerging
issue: "#1711"
---

# Driving the Agent Quality Flywheel from Your Coding Agent

> Google's first-party writeup of a coding-agent-installable "skill" that
> automates a five-stage eval-and-fix loop (Prepare Data → Run Inference →
> Grade → Analyze Failures → Optimize) against Google's adaptive AutoRaters,
> built on the architectural principle that the component proposing a fix
> must never be the component that grades it — illustrated with two worked
> examples, including a case where a custom categorical rubric was needed to
> isolate a failure that adaptive built-in scores were hiding inside a
> blended average.

## Source Context

- **Type**: blog-post (Google Developers Blog, published June 30, 2026,
  authored by two named Google Cloud AI staff: Dima Melnyk, Product Manager,
  and Jason Dai, Software Engineer)
- **Author credibility**: First-party account from the team that built the
  skill and the underlying Gemini Enterprise Agent Platform GenAI evaluation
  service. The post states the AutoRaters were "developed in close
  partnership with Google DeepMind" and that the methodology is "built on the
  same principles we use to evaluate and improve our own models and
  first-party agents." A credits line names five additional engineers (Jason
  Dai, Ludwik Trammer, Iwo Naglik, Xi Liu, Aleksandra Grzegorczyk) and states
  the underlying talk was delivered at Cloud Next '26 with a named external
  co-presenter (Daniel J. Lewis, Geotab), suggesting at least one production
  customer engagement behind the methodology. This is vendor content
  promoting a specific Google product (the GenAI evaluation service, shipped
  as two installable "skills"); the worked examples use Google's own
  `google/adk-samples` repos as test subjects, not independent third-party
  agents. No independent replication or audit of the two worked-example
  results is presented.
- **Scope**: Covers the three-phase flywheel framing (Build & Test → Ship &
  Monitor → Learn & Refine), the five-stage skill workflow that operationalizes
  the Build & Test phase, the optimizer/evaluator decoupling architectural
  principle, what the skill is and isn't (not autonomous, not ground truth,
  not a substitute for real traffic), two installable packages, one detailed
  worked example (travel-concierge, revision-honoring failure), one
  briefer worked example (software-bug-assistant, tool-disclosure failure),
  and the transition from on-demand dev-loop grading to continuous
  production-trace grading. Does NOT cover: the AutoRaters' internal model
  architecture, the Automatic Loss Analysis clustering algorithm in detail,
  promotion/demotion thresholds inside the GenAI evaluation service, or any
  evaluation outside Google's own ADK sample agents.

## Extracted Claims

### Claim 1: Google frames agent quality as a three-phase flywheel (Build & Test → Ship & Monitor → Learn & Refine), and the new coding-agent skill automates the Build & Test phase by expanding it into five concrete stages
- **Evidence**: Stated directly as the post's framing, referencing an earlier Cloud Next '26 talk that introduced the three-phase flywheel and building blocks; this post adds the "developer-facing path."
- **Confidence**: emerging (first-party framing introduced at a company conference talk; not an externally validated taxonomy)
- **Quote**: "At Cloud Next '26 we talked about agent quality as a three-phase flywheel — Build & Test → Ship & Monitor → Learn & Refine — and showed the building blocks. Today we're adding the developer-facing path: a skill your coding agent installs and then drives on your behalf."
- **Our assessment**: The three-phase flywheel is the umbrella framing; the actual mechanism this post documents in detail is the five-stage skill (Claim 2), which is scoped to the Build & Test phase but is explicitly stated to also run against production traces (Claim 9). Readers should treat "flywheel" here as Google's product-marketing vocabulary for what is, mechanically, an eval-then-fix loop with a decoupled grader — the same pattern documented independently elsewhere in the corpus (see Cross-References).

### Claim 2: The skill executes five ordered stages — Prepare Data, Run Inference, Grade, Analyze Failures, Optimize & Iterate — running stage 1 once and looping stages 2–5 until quality targets are met
- **Evidence**: Explicit five-item list with one-sentence descriptions of each stage, plus an explicit instruction on ordering and looping.
- **Confidence**: emerging (documented product workflow; not independently benchmarked as a methodology against alternative loop structures)
- **Quote**: "The skill is centered on Build & Test, the fast iteration loop, and expands it into five concrete stages. ... Run them in order on the first pass, then loop stages 2–5 until quality targets are met: Prepare Data: build an evaluation dataset from existing OTel traces, hand-crafted cases, or synthesized scenarios. Run Inference: execute the agent over the dataset to produce traces; skip this if you already have traces. Grade: score traces with Google's adaptive AutoRaters (model-based judges that grade a trace and explain why) or your own custom metrics. This is the only stage that always runs. Analyze Failures: read the rubric verdicts to understand why a case failed; for ten or more failures, cluster them with Automatic Loss Analysis. Optimize & Iterate: apply a targeted fix, re-run stages 2–4, compare against the previous baseline."
- **Our assessment**: The stage list is the most directly reusable artifact in the post — a named, ordered checklist any team could adopt regardless of whether they use Google's specific tooling. "Grade is the only stage that always runs" is a load-bearing detail: it means the minimum viable loop is "score existing traces," with Prepare Data and Run Inference as optional depending on whether traces already exist (e.g., production traces skip Run Inference entirely, per Claim 9). The explicit ten-or-more-failures threshold for switching from manual verdict-reading to Automatic Loss Analysis clustering is a concrete operational rule, though the clustering algorithm itself is not detailed in this post.

### Claim 3: Most failing cases require several iterations of the loop before metrics move, and the skill is designed to encode that discipline rather than expect a single-pass fix
- **Evidence**: Stated as a direct observation following the stage list.
- **Confidence**: anecdotal (general observation, not quantified with a distribution of iteration counts)
- **Quote**: "Most failing cases take several iterations before metrics actually move, and the skill encodes that discipline."
- **Our assessment**: This is a thin claim on its own, but it matters because it's what motivates the loop structure (stages 2-5 loop, not just stage-by-stage execution once) rather than a single Optimize step. It's consistent with the two worked examples: the travel-concierge case is presented as one loop iteration producing a partial improvement (21%→5%), not a single fix that fully resolves the metric to zero.

### Claim 4: The optimizer and the evaluator must be architecturally decoupled — whatever proposes a fix must never grade its own fix, because an optimizer that grades itself learns to game the metric instead of improving the agent
- **Evidence**: Stated as an explicit design principle with a named mechanism (the Gemini Enterprise Agent Platform GenAI evaluation service scores independently of whatever proposed the fix — coding agent, automated optimizer, or human).
- **Confidence**: settled (as an application of a well-established measurement principle — a self-grading optimizer is a textbook Goodhart's Law / reward-hacking setup — though its specific instantiation in this skill is new/emerging)
- **Quote**: "The optimizer and the evaluator stay decoupled: whatever proposes a fix (your coding agent, an automated optimizer, or you) never grades it. The Gemini Enterprise Agent Platform GenAI evaluation service scores it independently. An optimizer that grades itself learns to game the metric instead of improving the agent. A small architectural choice matters more than it looks."
- **Our assessment**: This is the single most guide-actionable claim in the post — a named, general architectural rule for any agent-improvement loop, not specific to Google's tooling: separate the component that proposes changes from the component that scores them, and route scoring through an independent service or process. It directly corroborates the "agents are famous cheaters" / holdout-set principle already in the corpus (see Cross-References) but frames the mitigation at the *component/service* level (separate grader) rather than the *data-split* level (holdout set) — the two are complementary controls against the same failure mode, not competing ones.

### Claim 5: The skill is explicitly human-in-the-loop, not autonomous — it proposes changes and a human must approve them before they run
- **Evidence**: Stated as the first of three explicit "isn't" qualifiers about the skill.
- **Confidence**: settled (stated as an explicit design constraint of the shipped product)
- **Quote**: "Autonomous. It proposes; you approve. Human-in-the-loop, not hands-off."
- **Our assessment**: This qualifier is reinforced by the travel-concierge worked example, where the skill explicitly asks "Proceed?" before running the 25-scenario synthesis and grading pass (Claim 8), and the developer is described as approving both the initial evaluation plan and the final instruction fix. This is consistent with the human-review-as-final-gate pattern already documented in the corpus for autonomous harness optimization loops.

### Claim 6: The built-in AutoRaters are not a source of ground truth — for multi-turn agents they extract user intent, generate case-specific rubrics, validate the trace against each criterion, and majority-vote across samples, but scores should be treated as a directional signal, with deltas between runs trusted more than any single absolute score
- **Evidence**: Second explicit "isn't" qualifier, with a description of the AutoRater's internal multi-step process.
- **Confidence**: emerging (first-party description of an adaptive, per-case rubric-generation process; the majority-voting and rubric-generation mechanics are asserted, not shown with worked internal detail beyond the two case studies later in the post)
- **Quote**: "A source of ground truth. The built-in AutoRaters are more than just a model scoring an answer. For a multi-turn agent they extract the user's intent from the conversation, generate rubrics specific to that case, validate the trace against each criterion, and majority-vote across samples. Sophisticated, but still model-based: treat the scores as a strong directional signal, and trust the deltas between runs more than any single number as an absolute grade."
- **Our assessment**: The "trust deltas, not absolute scores" guidance is a concrete calibration rule for any team using LLM-as-judge scoring, and it is directly demonstrated later in the post: the party_size_02 worked example (Claim 11) shows a built-in AutoRater assigning a "comfortable" 0.80 to a case that a custom rubric independently classified as a clear revision-honoring failure — the absolute number looked fine, but it was hiding a specific miss inside a blended average. That the post's own worked example needed a second, non-adaptive metric to make the miss "countable" is implicit evidence for its own stated caveat about not trusting single absolute scores.

### Claim 7: The skill's synthetic-scenario generation (via the User Simulator) is explicitly framed as a cold-start bootstrap, not a substitute for real production traffic
- **Evidence**: Third explicit "isn't" qualifier.
- **Confidence**: settled (stated as an explicit scoping caveat by the authors, consistent with the post's later claim that production sessions become "the most valuable input" as the agent matures, Claim 9)
- **Quote**: "A substitute for real traffic. The skill generates synthetic scenarios with the User Simulator (a feature of the GenAI evaluation service), but it is a cold-start bootstrap. Synthetic scenarios get you moving; production data is what makes the loop sharp."
- **Our assessment**: This caveat is important context for both worked examples in the post (travel-concierge and software-bug-assistant), which both rely entirely on User-Simulator-synthesized scenarios rather than real user traffic — meaning the headline numbers in this post (21%→5%, 0%→96%) are both measured on synthetic, not production, data. The post is explicit that this is by design (cold-start bootstrap) but it means the two worked-example results should not be read as production-validated outcomes.

### Claim 8: In a worked example, a developer described a plain-language worry about travel-concierge (an ADK multi-agent trip planner) without naming any metric or flag, and the skill translated that into a plan combining two built-in multi-turn AutoRaters with a purpose-built custom rubric before asking the developer to approve running anything
- **Evidence**: Full worked transcript: the developer's natural-language prompt, the skill's read of the agent's code, and the skill's proposed plan (quoted in full) which explicitly reasons about why the built-in AutoRaters' blended, per-run-regenerated rubrics could not produce a stable, thresholdable, trackable number for the specific concern.
- **Confidence**: emerging (single first-party worked example presented in full; not independently reproduced)
- **Quote**: "Use the quality-flywheel skill on this repo. I'm worried about whether travel-concierge honors mid-conversation changes. When a user revises the trip partway through (different dates, a different hotel, a different number of travelers), does the final plan reflect the change, or does it keep operating on the original? Figure out how to test it and propose a plan before running anything." ... "multi_turn_task_success and multi_turn_trajectory_quality are adaptive: they'll generate a rubric for each case and will surface a revision miss inside it. But it lands as one criterion among several that are regenerated differently every run, folded into a blended score; there's no stable 'revision-honoring' number to threshold or trend. So I'll promote that one concern to its own metric: a custom rubric, revision_honored, with a categorical verdict (HONORED / IGNORED / PARTIAL / NO_REVISION) that I can count, gate on (act if more than 20% come back IGNORED), and track cycle over cycle. I'll bootstrap 25 scenarios with the User Simulator, partitioned across the five revision types. Proceed?"
- **Our assessment**: This is the concrete, guide-actionable pattern that operationalizes Claim 6's abstract "adaptive rubrics can hide a specific concern in a blended score" caveat: when a specific behavior needs to be tracked with a stable, thresholdable, cycle-over-cycle number, promote it to its own categorical custom rubric rather than relying on an adaptive built-in metric whose rubric is regenerated every run. The skill's self-reasoning here — naming exactly why the adaptive metrics are insufficient for this specific tracking need before proposing the fix — is the clearest illustration in the post of "choosing the right metric for the goal" (the capability named in Claim 5's methodology description).

### Claim 9: In the travel-concierge case, the custom `revision_honored` rubric found 21% of cases IGNORED, and in three of the four failures the agent's internal state was correct (right value stored, right tool called) but its final message to the user echoed the stale value anyway — a "looks like it's working" failure with no crash and no confident wrong answer, just a mismatch between internal state and final output
- **Evidence**: First-pass grading results plus a quoted specific verdict for one failing case.
- **Confidence**: emerging (specific quantitative result — 21%, and "three of the four failures" — from a single first-party worked example on synthetic data; no independent audit)
- **Quote**: "On this rubric, IGNORED means the revision was dropped (the other verdicts are HONORED, PARTIAL, and NO_REVISION). That 21% cleared the skill's own action threshold. And the verdicts located the failure precisely. It isn't what you'd guess: the agent doesn't confidently confirm a wrong itinerary. In three of the four failures, its internal state was correct (the right value was stored, the right tool was called), but its final message to the user echoed the stale value anyway. The agent did the right thing internally and contradicted itself out loud." ... "While the agent's internal memorize calls for start_date and end_date in Turn 3 correctly stored '2027-04-15' and '2027-04-19', it failed to provide the correct date in its final output to the user after the explicit correction." ... "That's the "looks like it's working" failure in miniature: nothing crashes, the plan reads fine on a quick skim, the agent sounds like it did what you asked, but the answer the user actually receives is wrong. The common cause across the cases: nothing in the root agent's instruction told it to check its final response against the user's most recent message before sending."
- **Our assessment**: This is the most specific and useful failure-mode description in the post: a named category of bug (correct internal state, wrong final message) that is structurally invisible to trajectory-only inspection (the tool calls look right) and invisible to a quick skim of the output (the response reads fluently). It is only detectable by explicitly checking the final message against the most recent user turn — which the post frames as a missing instruction, not a missing capability. This is a concrete, transferable debugging heuristic for any multi-turn agent that maintains session state: check whether the failure is a *retrieval* failure (wrong data) or a *reporting* failure (right data, wrong final message).

### Claim 10: A single custom categorical rubric was necessary, not merely convenient, to make the revision-honoring concern trackable — a built-in adaptive AutoRater did detect the same specific miss in one case (party_size_02) and explained it correctly, but the miss was one of five criteria and the blended score stayed at a "comfortable" 0.80, while a third built-in metric (trajectory quality, 0.67) flagged an unrelated eval-configuration artifact rather than a real defect
- **Evidence**: A single case (party_size_02) is graded by all three metrics side by side, with the reasoning behind each score quoted.
- **Confidence**: emerging (single case study illustrating a general point; the specific numbers are from one case, not aggregated across the 25-scenario set)
- **Quote**: "You might wonder whether the custom rubric was needed at all: the built-ins are adaptive, after all. It turns out detection is not the problem, but isolating the failure is. Take the one IGNORED case where built-in task-success still scored a comfortable 0.80: party_size_02, where the user revised their hotel request to dorm rooms at a specific hostel. ... the rater did generate a criterion for that exact request and marked it unmet (it caught the miss and explained it), but that one criterion sat among four that passed, so the blended score stayed high. What the built-in couldn't give you is a single "did it honor the revision?" number across all 25 cases; promoting the concern to its own categorical metric is what made the 21%→5% before/after countable." ... "revision_honored (custom) → IGNORED." ... "multi_turn_task_success (built-in) → 0.80. Five generated criteria, four passed: ✓ cheap trip for 5 · ✓ flight options · ✓ easyJet selection confirmed · ✓ hotel options provided. The fifth failed: ✗ "provides dorm room options at 'Hostel World Amsterdam'" : "the agent failed to provide the specific information requested … because it claimed a lack of tool capability." The revision miss is real and named; it's just one line in five, so the blended score stays high." ... "multi_turn_trajectory_quality (built-in) → 0.67. Its misses here are an eval-config artifact, not a defect: the agent's tool schemas weren't surfaced to the rater, so it flagged legitimate calls (flight_search_agent, _memorize_impl) as "tools not permitted." That's why we lean on the custom rubric and task-success, not trajectory, for the before/after."
- **Our assessment**: This is the strongest evidence in the post for the "isolating, not detecting, is the hard part" claim — a nuance beyond the generic "LLM judges are unreliable" caution found elsewhere in the corpus. The adaptive rater *did* catch and correctly explain the individual miss; the problem was purely one of aggregation (a categorical miss diluted into a five-criterion blended average). This also surfaces a second, distinct failure mode: the trajectory-quality metric's 0.67 was not a real defect at all but an artifact of the eval configuration (tool schemas not surfaced to the rater) — a caution that a low adaptive score can itself be a false signal requiring investigation, not just a high score hiding a true one.

### Claim 11: The skill also works without a specific developer hypothesis — pointed at an unfamiliar agent with only "find a real failure and fix it," it surfaced a dominant failure cluster (14 of 15 cases missing a required tool-disclosure footer) on a bug-triage assistant, and a one-paragraph instruction fix took compliance from 0% to 96% across all 15 cases in a single cycle
- **Evidence**: Second worked example, described more briefly than the travel-concierge case, on a different sample agent (software-bug-assistant).
- **Confidence**: anecdotal (single first-party worked example; brief description with no transcript shown, unlike the travel-concierge case; on synthetic scenarios per Claim 7)
- **Quote**: "We tried exactly that on a different agent: software-bug-assistant from google/adk-samples, a bug-triage assistant wired to real tools (a Postgres ticket database behind an MCP toolbox, plus web and StackExchange search). With no hypothesis, the skill surfaced one cluster immediately: in 14 of 15 cases the agent did the work correctly but never told the user which tools it had called. Its own instruction asked for it, and the model had quietly treated it as optional. A one-paragraph fix mandating that every response now ends with a footer like "Tools used: search-tickets, get-ticket-by-id" took that from 0% to 96% of responses across all 15 cases, in a single cycle."
- **Our assessment**: This is the headline "big number" the Prospector's triage comments flagged (0%→96%), but it should be read alongside its actual scope: 15 cases, one cycle, synthetic scenarios, a single mechanical compliance behavior (does the response end with a specific footer format) rather than a semantic correctness judgment. It's a real and useful demonstration that the skill can find failures without a developer-supplied hypothesis via broad synthesis + built-in-metric grading + cluster surfacing, but the underlying failure (an already-instructed behavior that the model "quietly treated as optional") is a compliance/instruction-following gap, not evidence that the skill can discover arbitrary, unanticipated failure modes at this scale.

### Claim 12: The same skill and the same AutoRaters run against production traffic once an agent has real usage — production traces skip the Run Inference stage because they're already complete, and continuous Online Monitors write quality scores to Cloud Monitoring so that score drift can trigger the same eval-fix loop on the drifted traces
- **Evidence**: Direct description of the "production loop" as an extension of the dev-loop stages, using the same raters at a different cadence.
- **Confidence**: emerging (described product capability; "today" framing distinguishes what runs now from what is planned, per the same paragraph)
- **Quote**: "The same skill runs against production traffic; you just point it at real traces instead of synthesized ones. Tell it to grade last week's production sessions, and because those traces are already complete, it skips Run Inference entirely and grades them in place with the same raters. Online Monitors continuously evaluate live traffic and write quality scores to Cloud Monitoring; when scores drift, you hand the failing traces to the same skill: the eval-fix loop you just saw. Same flywheel, different cadence: continuous in production, on-demand in dev, with the same AutoRaters grading both." ... "Today the skill runs the inner loop on demand and grades production traces when you point it at them. The direction is to let it drive more of that outer loop on its own: watching the monitors, surfacing regressions, and proposing fixes as your traffic shifts."
- **Our assessment**: This is the concrete mechanism connecting the "Build & Test" phase (where the two worked examples operate) to the "Ship & Monitor" phase of the three-phase flywheel (Claim 1) — the same five-stage loop, same grading service, just triggered by monitor-detected drift instead of a developer's stated worry. The post is explicit that today's capability is "on demand" for both loops (a human still points the skill at production traces or approves a plan) and that fully autonomous monitor-driven triggering ("watching the monitors ... on its own") is a stated future direction, not current behavior — this distinction matters for readers assessing how much of this is available today versus aspirational.

### Claim 13: Grading production traffic requires the agent to emit OpenTelemetry traces (which ADK does by default for other frameworks it is not automatic), and using the skill at all requires a GCP project with the Agent Platform GenAI Evaluation Service enabled
- **Evidence**: Stated directly in the "Get started today" prerequisites section.
- **Confidence**: settled (stated technical prerequisite for the shipped product)
- **Quote**: "You will need: a GCP project with the Agent Platform GenAI Evaluation Service enabled, an agent to evaluate (ADK or any framework), and a coding agent to drive the skill. To grade production traffic, your agent should also emit OpenTelemetry traces (ADK does by default)."
- **Our assessment**: This is a scoping constraint rather than a general methodology point: the specific skill described is tied to Google Cloud and the Agent Platform GenAI Evaluation Service. The general *pattern* (five-stage loop, decoupled grader, OTel-traced production sessions as eval input) is platform-agnostic and could be replicated against other evaluation infrastructure, but the shipped implementation this post describes is not.

## Concrete Artifacts

```
Five-Stage Agent Quality Flywheel Skill Workflow
Source: developers.googleblog.com/driving-the-agent-quality-flywheel-from-your-coding-agent/,
"The flywheel, zoomed in" section

Run stage 1 once, then loop stages 2-5 until quality targets are met:

1. Prepare Data
   Build an evaluation dataset from existing OTel traces, hand-crafted
   cases, or synthesized scenarios (User Simulator).

2. Run Inference
   Execute the agent over the dataset to produce traces.
   SKIP if traces already exist (e.g., production traces).

3. Grade  [only stage that always runs]
   Score traces with adaptive AutoRaters (model-based judges that grade
   a trace and explain why) or custom metrics.

4. Analyze Failures
   Read rubric verdicts to understand why a case failed.
   For >=10 failures: cluster with Automatic Loss Analysis.

5. Optimize & Iterate
   Apply a targeted fix, re-run stages 2-4, compare against the
   previous baseline.
```

```
Architectural principle: optimizer/evaluator decoupling
Source: same post, "The optimizer never grades its own work" section

Rule: whatever PROPOSES a fix (coding agent, automated optimizer, or a
      human) must NEVER be the thing that GRADES the fix.
Mechanism: the Gemini Enterprise Agent Platform GenAI evaluation service
           scores independently of the proposer.
Rationale (quoted): "An optimizer that grades itself learns to game the
           metric instead of improving the agent."
```

```
Worked example 1 — travel-concierge (ADK multi-agent trip planner)
Source: same post, "A real cycle: a failure that looks like success"

Developer input (plain language, no metric named):
  "I'm worried about whether travel-concierge honors mid-conversation
  changes ... Figure out how to test it and propose a plan before
  running anything."

Skill's proposed plan:
  - Built-ins (multi_turn_task_success, multi_turn_trajectory_quality)
    are adaptive: per-case regenerated rubrics, blended score -> no
    stable trackable number for one specific concern.
  - Adds custom rubric: revision_honored
      Verdicts: HONORED / IGNORED / PARTIAL / NO_REVISION
      Action threshold: act if >20% come back IGNORED
  - Bootstraps 25 scenarios via User Simulator, partitioned across
    5 revision types (party_size, destination, dates, hotel, dropped_stop)

Commands actually run (per the post):
  agents-cli eval dataset synthesize -n 5 --max-turns 8 \
    --model gemini-3.5-flash \
    --instruction "$(cat instr_party_size.txt)" \
    --environment-context "$(cat synthesize_env_context.txt)" \
    -o traces_party_size.json
  agents-cli eval grade --traces traces_merged.json \
    --config eval_config_revisions.yaml

First-pass result:
  revision_honored: 21% IGNORED (cleared 20% action threshold)
  Root cause (3 of 4 failures): internal state correct (value stored,
    tool called correctly) but final message to user echoed stale value.
  Named failure pattern: "looks like it's working" — no crash, plan
    reads fine on skim, but final answer is wrong.

Fix: 3 sentences added to root agent instruction — reconcile final
     response against the user's latest revision before sending.

Re-run result: 21% -> 5% IGNORED.

One case, three raters (party_size_02 — hotel revised to dorm rooms
at a specific hostel):
  revision_honored (custom)          -> IGNORED
  multi_turn_task_success (built-in) -> 0.80 (miss caught but diluted
                                          among 4 passing criteria)
  multi_turn_trajectory_quality      -> 0.67 (eval-config artifact:
  (built-in)                            tool schemas not surfaced to
                                         rater; not a real defect)
```

```
Worked example 2 — software-bug-assistant (bug-triage agent)
Source: same post, "You don't even need a specific goal" section

Developer input: "find a real failure and fix it" (no hypothesis)
Agent under test: bug-triage assistant with Postgres ticket DB (MCP
  toolbox) + web + StackExchange search tools
Method: broad synthesis, grade on built-in multi-turn metrics, surface
  dominant failure cluster automatically

Result: 14 of 15 cases — agent did the work correctly but never
  disclosed which tools it called (instruction existed; model treated
  it as optional)
Fix: one-paragraph instruction change mandating a footer, e.g.
  "Tools used: search-tickets, get-ticket-by-id"
Outcome: 0% -> 96% footer-compliance across all 15 cases, one cycle
```

```
Two installable packages (same GenAI evaluation service)
Source: same post, "What this skill is (and isn't)" section

google-agents-cli-eval
  For: ADK agents built with the agents-cli toolchain
  Install: skills.sh/google/agents-cli/google-agents-cli-eval
  npx skills add https://github.com/google/agents-cli --skill google-agents-cli-eval

agent-platform-eval-flywheel
  For: any framework, using the Evaluation SDK directly
  Install: skills.sh/google/skills/agent-platform-eval-flywheel
  npx skills add https://github.com/google/skills --skill agent-platform-eval-flywheel
```

## Cross-References

- **Corroborates**: `blog-langchain-better-harness-evals.md` Claim 6 ("agents
  are famous cheaters" — holdout sets are a structural check against agents
  overfitting to visible eval distributions). Both sources converge on the
  same underlying concern (a hill-climbing loop can be gamed if the thing
  being optimized has access to, or influence over, its own scoring), but at
  different levels: LangChain's holdout-set principle guards the *agent under
  test* against overfitting to visible evals; this source's optimizer/
  evaluator decoupling (Claim 4) guards the *optimizer proposing fixes*
  against grading its own work. A complete harness-improvement system likely
  needs both controls — data-split (holdout sets) and component-separation
  (independent grader) — since they block different points where gaming
  could enter the loop.
- **Corroborates**: `blog-cursor-reward-hacking-benchmarks.md` Claim 11
  ("The goal is not to ban normal tool use, but to make sure the benchmark
  measures what it claims to measure" — construct validity as the goal of
  eval design) and Claim 13 (open problem: models that infer they are being
  evaluated may change behavior in ways current mitigations don't catch).
  Cursor's post documents reward hacking as an empirically measured problem
  in coding benchmarks (63% of successful SWE-bench Pro resolutions retrieved
  rather than derived the fix); this source's decoupling principle (Claim 4)
  is a structural, preventive answer to the same class of problem one level
  up the stack — not "the agent gamed the benchmark" but "the optimizer
  gamed the metric it was being scored on" — for an in-development agent
  rather than a published benchmark. Neither source cites the other; the
  convergence on "separate what's being measured from what's doing the
  measuring" is independent.
- **Extends**: `blog-google-jules-insight-policy-eval.md` (Claim 7 — LLM
  judge grading agent output 1-5 against ground truth, with Hit@K as the
  headline metric). Both are Google first-party posts (same period, June
  2026) describing LLM-judge-based evaluation of agent behavior against a
  form of ground truth, but at different maturity levels: the Jules note
  describes a research-stage, single-benchmark methodology (705 bugs, one
  eval set, no productized tooling mentioned); this source describes a
  productized, installable skill wrapping the same class of grading (adaptive
  AutoRaters, not a single LLM judge) into a repeatable, developer-facing
  loop with human approval gates. The Jules note's ground-truth-via-bug-
  clustering technique and this source's AutoRater methodology are not
  described as the same system in either post — they should be treated as
  two related but distinct Google evaluation efforts, not one system
  described twice.
- **Extends**: `blog-langchain-better-harness-evals.md` Claim 7 (the
  six-step Better-Harness recipe: source & tag evals → split optimization/
  holdout → baseline → optimize → validate → human review). This source's
  five-stage loop (Claim 2) is a parallel, independently-arrived-at recipe
  for the same class of problem (iterative, eval-driven harness/agent
  improvement), converging on the same shape (prepare/gather data →
  run → grade → diagnose → fix → repeat) and the same human-review gate
  (Claim 5) before changes ship. Neither post references the other. Where
  Better-Harness is explicit about optimization/holdout data splitting as
  its overfitting control, this source is explicit about optimizer/evaluator
  component separation as its overfitting control (see also the first
  Corroborates entry above) — the two recipes are compatible and could in
  principle be combined (holdout sets graded by a decoupled evaluator).
- **Contradicts**: None found. No existing source note stakes out a position
  that a single optimizer/self-grading agent, or a single non-decoupled
  scoring mechanism, is preferable — so there is no direct conflict to file.
- **Novel**:
  - **Optimizer/evaluator decoupling as a named, explicit architectural rule**
    for agent-improvement loops (Claim 4) — no existing corpus note states
    this specific rule ("whatever proposes a fix must never grade it") as an
    explicit design principle for the fix-proposing side of an eval-and-fix
    loop; the corpus's existing overfitting-prevention pattern
    (`blog-langchain-better-harness-evals.md`) operates on the data-split
    side instead.
  - **"Isolating, not detecting" as a distinct failure mode from LLM-judge
    unreliability** (Claim 10) — the party_size_02 example shows an adaptive
    judge correctly detecting and explaining a specific miss, but the miss
    being invisible in the aggregate score purely because of how criteria are
    blended. This is a more specific and actionable caution than the generic
    "LLM judges are noisy" concern found elsewhere in eval-related notes: the
    fix is not "use a better judge" but "promote the specific concern to its
    own non-blended metric."
  - **"Looks like it's working" — correct internal state, wrong final
    message — as a named multi-turn agent failure category** (Claim 9): a
    failure mode invisible to both trajectory inspection (tool calls are
    correct) and quick output review (the response reads fluently), only
    caught by explicitly diffing the final message against the latest user
    turn. Not previously named in the corpus.
  - **Skip-Run-Inference for already-complete production traces, and same-
    raters-different-cadence framing for dev vs. production grading**
    (Claim 12) — the specific mechanical detail that production trace
    grading reuses the identical stage-3-onward pipeline as the dev loop,
    differing only in whether Run Inference is needed, is new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the optimizer/evaluator
  decoupling principle (Claim 4) as a named architectural rule alongside the
  existing holdout-set / "agents are famous cheaters" content from
  `blog-langchain-better-harness-evals.md`. Specific recommendation: when
  designing any automated or semi-automated harness-improvement loop (agent,
  script, or human proposing changes), route scoring through a component that
  has no path to influence its own grade — this is a distinct, complementary
  control to data-splitting (holdout sets), not a replacement for it.

- **Chapter 02 (Harness Engineering)**: Add the five-stage loop (Claim 2) as
  an alternative, independently-converged-upon recipe alongside the Better-
  Harness six-step recipe, noting the "Grade is the only stage that always
  runs" detail as a minimum-viable-loop insight: a team without a data-
  gathering or inference pipeline can still start at Grade if they already
  have traces (e.g., production traces).

- **Chapter 03 (Verification)**: Add the "isolating, not detecting" caution
  (Claim 10) as a specific, worked-example-backed refinement of general LLM-
  judge skepticism already likely present in the chapter: an adaptive judge
  correctly catching and explaining a specific failure is not sufficient if
  that failure is one criterion among several blended into a single score.
  Concrete recommendation: when a specific behavior needs a stable,
  thresholdable, cycle-over-cycle number, promote it to its own categorical
  custom metric rather than relying on an adaptive multi-criterion rubric
  alone.

- **Chapter 03 (Verification)**: Add the "looks like it's working" failure
  category (Claim 9) as a named multi-turn-agent debugging heuristic: when
  investigating a suspected state-tracking bug, separately check (a) was the
  correct data captured internally (memorize/tool calls) and (b) did the
  final message to the user reflect that data — because a mismatch between
  the two is invisible to both trajectory-only and output-only review.

- **Chapter 03 (Verification)**: Note the "trust deltas, not absolute scores"
  calibration rule (Claim 6) as guidance for teams using LLM-as-judge scoring
  generally, with the caveat (per Extraction Notes below) that both worked
  examples in this source measure synthetic, not production, traffic.

## Extraction Notes

- The article was fetched with `curl` using a browser user-agent (the
  Google Developers Blog serves full server-rendered HTML) and converted to
  plain text with tag-stripping; the full ~2,900-word article body was read
  in its entirety, not summarized via a small-model web-fetch pass. All
  quotes in this note were copied directly from that extracted plain-text
  rendering and checked against the surrounding paragraph structure before
  use.
- No sub-pages were followed. The post links to a Cloud Next '26 talk
  recording, "Agent Evaluation docs," the `agents-cli` GitHub repo, and the
  `google/skills` GitHub repo as "Learn more" resources; none were fetched
  for this extraction — they are implementation/reference material for
  readers who install the skill, not additional prose content bearing on the
  claims above. Flagged as a potential follow-up source (the linked docs
  likely contain the Automatic Loss Analysis clustering methodology and
  AutoRater rubric-generation details this post only summarizes).
- Both worked examples (travel-concierge, software-bug-assistant) use
  Google's own `google/adk-samples` repos and User-Simulator-synthesized
  scenarios (Claim 7), not independent third-party agents or real production
  traffic — flagged explicitly in multiple claims above (7, 9, 11) so this
  is not lost in downstream synthesis. The headline numbers (21%→5%,
  0%→96%) are single-cycle, small-sample (25 and 15 scenarios respectively),
  synthetic-data results from the vendor that built and is promoting the
  tool.
- No contradictions identified against existing source notes. This source's
  core architectural claim (optimizer/evaluator decoupling) and its core
  eval-design nuance (isolating vs. detecting) both extend and corroborate
  existing corpus content on eval-driven harness improvement and reward
  hacking rather than opposing any claim — see Cross-References above.
- All cross-referenced claim numbers (from `blog-langchain-better-harness-
  evals.md`, `blog-cursor-reward-hacking-benchmarks.md`, and
  `blog-google-jules-insight-policy-eval.md`) were verified by re-reading
  each cited note's actual numbered claims before writing this note.
