---
source_url: https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/
source_type: blog-post
title: "Does Speaking to Agents Like Cavemen Really Save 65% of Tokens? We Test"
author: Denis Shiryaev (JetBrains AI)
date_published: 2026-07-06
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: emerging
issue: "#1637"
---

# Does Speaking to Agents Like Cavemen Really Save 65% of Tokens? We Test

> JetBrains AI runs a controlled A/B benchmark of the "Caveman" prompt-compression
> skill against real multi-step agentic tasks and finds the advertised 65%
> token-saving claim collapses to roughly 8.5% output-token savings once code,
> diffs, and tool calls (which the skill leaves untouched) dominate the token
> budget — with no measurable quality degradation but a cost benefit fragile
> enough to invert on a single long-context outlier task.

## Source Context

- **Type**: blog-post (practitioner empirical benchmark / vendor blog, JetBrains
  AI, published 2026-07-06)
- **Author credibility**: Denis Shiryaev, writing on the official JetBrains AI
  blog. The post is not a marketing claim but a direct empirical test of someone
  else's marketing claim (the Caveman skill's own advertised 65% figure), using
  a named benchmark suite (SkillsBench), a named sandboxed test platform (Harbor
  0.17), a named model (`claude-sonnet-5`), and disclosed budget (~$106 across
  ~240 trials). No individual author bio/title is given in the byline, but the
  methodology disclosure (task counts, statistical test, dollar totals) is
  concrete enough to evaluate independently of the author's personal credentials.
- **Scope**: Covers a single prompt-compression skill ("Caveman") tested against
  a single benchmark suite (SkillsBench, 86 of 87 tasks) on a single model
  (`claude-sonnet-5`) via Claude Code 2.1.200 in a Harbor-sandboxed environment.
  Does NOT cover: other prompt-compression techniques, other models, chat-only
  (non-agentic) workloads (where the 65% claim may hold — the post explicitly
  scopes that claim to "chat-style Q&A"), or long-term/production cost behavior
  beyond the ~240-trial test window.

## Extracted Claims

### Claim 1: Real-world output-token savings from the Caveman skill converge to about 8.5%, not the advertised 65%
- **Evidence**: Full-run measurement across 82 paired tasks, comparing baseline
  vs. forced-Caveman-activated output token totals.
- **Confidence**: settled (first-party measured result, disclosed absolute
  token counts)
- **Quote**: "at scale the saving converges to -8.5% (592k to 542k output
  tokens over 82 paired tasks)."
- **Our assessment**: This is the headline empirical finding and the reason
  the source is worth citing: it replaces a vendor-marketing percentage with
  a measured one, using disclosed absolute numbers (592k → 542k tokens) rather
  than an unverifiable ratio. An 8.5% output-token reduction is real but roughly
  7.6x smaller than the advertised figure.

### Claim 2: The 65% claim originates from the Caveman skill's own marketing pitch, not from independent measurement
- **Evidence**: The post directly quotes the skill's own self-description/README
  copy as the source of the 65% figure.
- **Confidence**: settled (directly attributed to the skill's own promotional text)
- **Quote**: "Its pitch is best described in its own dialect: > Skill make agent
  talk like caveman...65% output token saved."
- **Our assessment**: Distinguishing "vendor/tool-author claim" from "independently
  measured result" is exactly the discipline this corpus should apply to every
  optimization claim. Here the entire gap between 65% and 8.5% is explained by
  where each number comes from: one is a promotional headline, the other is a
  disclosed 82-task paired benchmark.
- **Confidence**: settled

### Claim 3: The gap between claimed and measured savings exists because agent output tokens are dominated by code, diffs, and tool calls, which Caveman deliberately leaves unchanged — only "think-out-loud" narration gets compressed
- **Evidence**: The author's causal explanation for why the 65% chat-style
  figure does not transfer to agentic workloads.
- **Confidence**: emerging (the authors' own interpretation of their result,
  though well-supported by the disclosed mechanism of the skill)
- **Quote**: "The advertised 65% belongs to chat-style Q&A, not to coding agents."
- **Our assessment**: This is the most transferable insight in the post for
  guide purposes: any prompt-compression technique that only touches narration
  text will have its effective savings capped by the narration share of total
  output tokens in agentic workloads — and that share appears to be small
  relative to code/diff/tool-call tokens. This mechanism-level explanation is
  more durable than the specific 8.5% figure, since it would apply to any
  similar "talk tersely" skill, not just Caveman.

### Claim 4: The benchmark used a disclosed, reproducible methodology — Harbor 0.17 sandboxed environment, Claude Code 2.1.200 on `claude-sonnet-5`, SkillsBench (86 of 87 tasks), ~240 trials for about $106
- **Evidence**: Methodology section of the post, naming the sandbox platform,
  harness version, model, benchmark suite, and total spend.
- **Confidence**: settled (first-party disclosed methodology)
- **Quote**: "SkillsBench (`benchflow/skillsbench`): 86 of 87 tasks" run on
  "`claude-sonnet-5`."
- **Our assessment**: Methodology disclosure at this level (named sandbox
  version, named benchmark repo, model ID, dollar total) is above the bar for
  most practitioner blog-post benchmarks in the corpus and is what makes the
  8.5%/65% comparison in Claim 1 usable rather than anecdotal.

### Claim 5: Across 82 paired tasks, Caveman-on and Caveman-off arms produced statistically indistinguishable task quality (sign test p = 0.82)
- **Evidence**: A sign test over paired task outcomes (64 tied, 18 non-ties)
  comparing baseline vs. forced-Caveman task scores.
- **Confidence**: settled (disclosed statistical test with p-value)
- **Quote**: "Across 82 paired tasks in the full run, the answer is no: the
  arms are statistically indistinguishable."
- **Quote (p-value)**: "Sign test over the 18 non-ties: p = 0.82, far from
  any significant difference."
- **Our assessment**: This is the strongest reassurance in the post for anyone
  considering adopting Caveman: the compression does not appear to cost task
  success, at least on this benchmark and model. Practitioners should read
  this as "no detected harm on SkillsBench with claude-sonnet-5," not as a
  universal guarantee across all task types or models.

### Claim 6: A pilot run of only 10 tasks showed a misleadingly large -30% token saving that "dissolved" once the sample size grew to the full 82-task run
- **Evidence**: The author's own reported pilot-vs-full-run comparison.
- **Confidence**: settled (first-party reported result of their own two-stage
  testing process)
- **Quote**: "Our first 10-task run 'showed' a -30% token saving. It dissolved
  as sample size grew."
- **Our assessment**: This is a methodology lesson independent of the Caveman
  result itself: small-sample pilot benchmarks of agentic tasks can produce
  dramatically overstated effect sizes that regress toward a much smaller true
  effect as N grows. Any single-digit-task "we tested it and got X%" claim
  elsewhere in the corpus should be discounted accordingly unless it discloses
  a comparable sample size.

### Claim 7: Real-world cost savings from Caveman are fragile — a single outlier task crossing a pricing-tier boundary can flip the aggregate cost comparison from a saving to a net loss
- **Evidence**: The full-run dollar totals showed the Caveman arm as more
  expensive overall, traced to one task's context length crossing a long-context
  pricing tier.
- **Confidence**: settled (first-party disclosed dollar totals and root-cause
  trace)
- **Quote**: "The entire inversion came from a single trial: one dependency-audit
  task ballooned past the 200k long-context pricing tier."
- **Quote (totals)**: "the raw arm totals in our full run showed the skill arm
  11.6% more expensive: USD 40.60 vs. USD 36.39."
- **Our assessment**: This is a distinct and separately valuable finding from
  Claim 1: even a real, measured per-task token saving does not guarantee a
  real aggregate dollar saving, because model pricing tiers (e.g., a long-context
  surcharge past 200k tokens) can be triggered or avoided by small differences
  in prompt length. A technique that trims average tokens can still net-lose
  money if it changes which side of a pricing cliff a handful of expensive
  tasks land on. Guide-relevant: cost claims for token-reduction techniques
  should be evaluated in dollars at the pricing-tier level, not just in raw
  token percentages.

### Claim 8: The authors' final recommendation is to treat Caveman as low-risk and optional ("use it if you like it") rather than a serious cost-optimization lever, since realistic agentic savings top out in the high single digits
- **Evidence**: The post's closing verdict, synthesizing the quality-parity
  finding (Claim 5) and the modest-savings finding (Claim 1).
- **Confidence**: anecdotal (this is the authors' own judgment call/recommendation,
  not an additional measurement)
- **Quote**: "Recommendation: use it if you like it."
- **Quote**: "Just do not expect huge savings on daily agentic tasks: a
  high-single-digit percentage is the realistic ceiling."
- **Our assessment**: A fair synthesis of their own data: no detected quality
  cost (Claim 5) makes adoption low-risk, but the realistic ceiling (high
  single digits, not 65%) means practitioners should not select or prioritize
  this technique as a primary cost-control lever for agentic workloads.

## Concrete Artifacts

```
# Benchmark setup (from post's Methodology section)
# Source: https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/

Platform:    Harbor 0.17 (Docker-sandboxed test environment)
Harness:     Claude Code 2.1.200
Model:       claude-sonnet-5
Benchmark:   SkillsBench (benchflow/skillsbench) — 86 of 87 tasks
Trial count: ~240 trials
Budget:      ~USD 106 total spend
Design:      A/B — baseline arm vs. forced-Caveman-activated arm, paired per task

# Results
Pilot run (10 tasks):        -30% token "saving" (did not replicate at scale)
Full run (82 paired tasks):  -8.5% output tokens (592k -> 542k)
Quality:                     64 ties, 18 non-ties; sign test p = 0.82 (no significant difference)
Cost (full-run totals):      Caveman arm USD 40.60 vs. baseline USD 36.39 (+11.6%, driven
                              by one dependency-audit task crossing the 200k long-context
                              pricing tier)
```

## Cross-References

- **Corroborates**: None found — no existing corpus note independently measures
  the real-world token savings of a "terse narration" prompt-compression skill
  on agentic (as opposed to chat) workloads.
- **Extends**: `docs-ghaw-effective-tokens-specification.md` Claim 3 (the ET
  spec's default weighting of output/reasoning tokens at 4.0x vs. 1.0x for
  input) explains part of the *mechanism* behind this source's Claim 3: agent
  sessions are dominated by output-class tokens (code, diffs, tool calls), and
  that spec formalizes why output tokens carry outsized cost weight. This
  source adds the empirical observation that a technique compressing only the
  narration slice of output tokens therefore captures only a small fraction of
  the theoretical output-token budget.
- **Contradicts**: None identified requiring a contradiction issue. The
  Prospector's triage flagged potential overlap with
  `blog-anthropic-dynamic-workflows-claude-code.md` Claim 8 ("dynamic workflows
  consume substantially more tokens... requiring careful budget monitoring")
  and `docs-ghaw-effective-tokens-specification.md`, but on inspection neither
  makes a claim about prompt-compression savings that this source's findings
  oppose. Dynamic Workflows Claim 8 is a caution about *increased* consumption
  from parallel sub-agent orchestration — a different mechanism and a different
  direction of effect than a technique aimed at *reducing* narration tokens.
  These are complementary cost concerns, not competing claims about the same
  variable, so this is a conditioning-variable difference (per MINER.md §4a),
  not a contradiction — no issue filed.
- **Novel**: This is the first corpus source to (a) empirically test a
  vendor/tool-author token-savings marketing claim against a controlled agentic
  benchmark, (b) quantify the gap between claimed and measured savings with
  disclosed absolute numbers, (c) document the "small-pilot overstates effect
  size" methodology trap (Claim 6) in the context of agent benchmarking, and
  (d) document that pricing-tier boundaries (e.g., a 200k long-context
  surcharge) can invert an aggregate cost comparison even when per-task token
  savings are real (Claim 7).

## Guide Impact

- **Chapter 04 (Agent Optimization and Prompt Engineering)**: Add this source
  as the concrete counter-example to any prompt-compression or "terse prompting"
  technique advertised with a large token-saving percentage. Lead with Claim 1
  (8.5% measured vs. 65% claimed) and Claim 3 (mechanism: compression only
  touches narration, not code/diffs/tool calls, which dominate agent output).
  Recommend that practitioners evaluating any similar skill ask specifically
  what fraction of a typical agentic session's output tokens are narration vs.
  code/tool-call tokens before trusting a headline savings percentage.

- **Chapter 03 (Cost and Efficiency) / Chapter 02 (Foundations — cost
  measurement methodology)**: Add Claim 7 (pricing-tier inversion) as a
  concrete caution for any team benchmarking token-reduction techniques: a
  real average per-task token reduction can still produce a net cost *increase*
  in aggregate if it changes which tasks land on the far side of a long-context
  pricing tier. Cost claims for optimization techniques should be validated in
  dollars at realistic task-size distributions, not just in average token
  percentages. Pair with `docs-ghaw-effective-tokens-specification.md`'s
  explicit design choice that ET is deliberately billing-independent — this
  source is a concrete illustration of why a compute-normalized metric like ET
  and an actual-dollar-cost metric can diverge.

- **Chapter 04 (Benchmarking methodology)**: Add Claim 6 (10-task pilot showing
  -30%, collapsing to -8.5% at 82 tasks) as a general caution about small-sample
  agentic benchmarks. No existing corpus note documents this specific
  pilot-vs.-full-run regression pattern; it is a useful methodological warning
  for practitioners running their own quick A/B tests on agent behavior changes.

## Extraction Notes

- The source was retrieved via the WebFetch tool, which processes page content
  through an intermediate AI model rather than returning raw HTML/text. Four
  fetch passes were made: (1) a general summary pass, (2) a targeted pass
  requesting specific single-sentence verbatim quotes for each major claim,
  (3) a pass for author/byline and section-by-section paraphrase (used only for
  Source Context and Claim framing, not as quoted material), and (4) a final
  targeted pass re-requesting the exact endorsement/recommendation sentence,
  the origin-of-65%-claim sentence, the token-count sentence, the cost-inversion
  sentence, the p-value sentence, and the pilot-run sentence. Quotes used in
  this note are the ones returned consistently as exact, attributed sentences
  across passes 2 and 4; passages the tool only paraphrased are not quoted.
- The post's own numbers have a small internal reconciliation gap worth
  flagging: the benchmark is described as covering "86 of 87 tasks," while the
  quality/token results are reported "over 82 paired tasks." The post does not
  explicitly state what happened to the remaining ~4 tasks (excluded, errored,
  or unpaired); this note reports both figures as given rather than
  reconciling them.
- No individual author bio or title was found on the page beyond the byline
  name (Denis Shiryaev); Source Context reflects that limitation.
- No sub-pages or linked follow-up posts were identified as substantive enough
  to follow per MINER.md §1 — the post is a single self-contained benchmark
  write-up.
- No contradiction issue was filed. The two "overlapping" notes flagged by the
  Prospector's triage comments were checked directly (see Cross-References)
  and neither makes a claim this source's findings dispute.
