---
source_url: https://cognition.com/blog/swe-2
source_type: blog-post
title: "Introducing SWE-2: Pushing the Pareto Frontier"
author: "The Cognition Team"
date_published: 2026-09-10
date_extracted: 2026-09-11
last_checked: 2026-09-11
status: current
confidence_overall: emerging
issue: "#3385"
---

# Introducing SWE-2: Pushing the Pareto Frontier (Cognition)

> Cognition's release post for SWE-2 — post-trained via large-scale RL from
> Kimi K3 (2.8T parameters) — headlined by a single RL algorithm that trains
> all reasoning-effort levels (medium/high/max) in one run using a
> Pareto-frontier-tangent cost penalty, rather than Kimi K3's own
> separate-expert-per-effort-level-plus-distillation approach. Reports a
> formal, first-principles proof (via Jensen's functional equation) that a
> linear cost penalty is the *only* choice that keeps the RL objective
> aligned with a model's position on the cost/performance Pareto curve, plus
> a length-weighted approximation to the variance-minimizing reward baseline,
> concrete rollout-serving infrastructure (prefill delayer, DSpark/SpecForge
> speculative decoding, NVFP4/FP8 quantization-aware training), and an
> updated trustworthiness re-evaluation against five competitor models.

## Source Context

- **Type**: blog-post (Cognition's engineering/research blog, cognition.com,
  published 09.10.26, anonymous corporate byline "By The Cognition Team" —
  unlike the individually-authored SWE-1.7 and SWE-1.6-Preview posts, this
  post does not name individual authors in its own byline, though its
  References section credits named individuals for the two linked companion
  posts it cites). The article is server-rendered directly in the page HTML
  (recovered via a direct `curl` fetch with browser headers after an initial
  `curl` attempt without headers returned an HTTP 403 "Forbidden" from the
  site's edge/CDN layer).
- **Author credibility**: First-party vendor content from Cognition, the
  company that builds and sells Devin and trains the SWE-1.x/SWE-2 model
  family underlying it. Direct commercial incentive to present SWE-2
  favorably (the post's own title, "Pushing the Pareto Frontier," is
  marketing framing), but it discloses specific, falsifiable technical
  detail: a full benchmark comparison table that shows SWE-2 trailing
  Fable 5.1 and GPT-6 Astra on FrontierCode 1.1 Main, a rigorous mathematical
  derivation (Appendix B) of why a linear cost penalty is uniquely forced
  rather than a design choice, and a disclosed appendix note that its own
  highest-effort "Max" tier (for both Fable 5.1 and Fable 5, competitor
  models) is Pareto-dominated by a lower-effort tier — a data point that
  runs against no particular Cognition interest but that Cognition chose to
  disclose anyway.
- **Scope**: Covers the SWE-2 headline positioning and base model (Kimi K3),
  a four-benchmark comparison table against six competitor models plus its
  own predecessor SWE-1.7, three named behavioral improvements (test
  coverage, resourcefulness, verification discipline) plus a "focused
  exploration" efficiency finding, the Pareto-frontier cost-penalty RL
  algorithm with a full mathematical derivation, a length-weighted reward
  baseline, rollout-serving infrastructure (prefill delayer, DSpark/SpecForge
  speculative decoding, NVFP4/FP8 quantization), training-data improvements
  (RL environment scaling, instruction-following overlays, a verifier-
  hardening flywheel), and an updated re-run of two of the three
  trustworthiness evaluations from `blog-cognition-open-source-
  trustworthiness.md` against six models. Does NOT cover: exact RL
  environment counts, training infrastructure topology/datacenter details
  (present in `blog-cognition-swe17.md` for the predecessor model but not
  repeated here), the third trustworthiness dimension (refusal testing) from
  the earlier trustworthiness post, or any independent replication of the
  reported benchmark/behavioral figures.

## Extracted Claims

### Claim 1: SWE-2 achieves 50.0% on FrontierCode 1.1 Main — within one point of Fable 5.1 while being 64% cheaper — and is framed as the closest Cognition model yet to the capability/cost Pareto frontier
- **Evidence**: Direct headline framing statement in the article's opening
  paragraph, tied to a specific benchmark figure and a specific relative-cost
  claim.
- **Confidence**: emerging (first-party, unaudited claim; the 50.0% figure is
  specific and falsifiable via the live FrontierCode leaderboard, but the
  "64% cheaper" comparison basis — list pricing per the appendix note — was
  not independently reproduced)
- **Quote**: "Today we're introducing SWE-2, our most advanced coding model yet. It pushes the Pareto frontier of capability and cost, achieving 50.0% on FrontierCode 1.1 Main, within one point of Fable 5.1 while being 64% cheaper."
- **Our assessment**: This is a cost-efficiency claim, not a leading-capability claim — the benchmark table (Claim 3) shows SWE-2 trailing both Fable 5.1 (50.9%) and GPT-6 Astra (53.3%) on FrontierCode 1.1 Main outright. Consistent with the same "frontier at a fraction of the cost" positioning already documented for SWE-1.7 (`blog-cognition-swe17.md` Claim 2's "Our assessment"), this is the same Pareto-efficiency argument applied to a new model generation, not a claim of outright leading capability.

### Claim 2: SWE-2 scales RL to the multi-trillion-parameter regime for the first time at Cognition, building on SWE-1.7's training infrastructure/recipe, with the key addition of an RL algorithm that trains all reasoning-effort levels in a single run
- **Evidence**: Direct statement of the scaling milestone and the specific
  new algorithmic contribution, naming the predecessor infrastructure this
  post builds on.
- **Confidence**: settled (a direct, first-party statement of how the model
  was built and what changed relative to the named predecessor; the
  single-run multi-effort-level training claim is elaborated and
  mathematically justified later in the same post — see Claims 8-10)
- **Quote**: "With SWE-2, we scaled RL to the multi-trillion-parameter regime for the first time, building on the SWE-1.7 training infrastructure and recipe. The key addition is an RL algorithm that trains all reasoning-effort levels in a single run, advancing the whole cost–performance frontier."
- **Our assessment**: This explicitly extends `blog-cognition-swe17.md`'s own "post-training ceiling" framing (Claim 1 of that note — stacking a large-scale RL run on an already-RL'd base still yields large gains) to a new, larger base model (Kimi K3, 2.8T parameters, vs. SWE-1.7's Kimi K2.7 Code) and a new compute regime ("multi-trillion-parameter" for the first time at this lab). The single-RL-run-for-all-effort-levels approach is the post's central new methodological claim, elaborated in Claims 8-10.

### Claim 3: On four coding benchmarks, SWE-2 beats its predecessor SWE-1.7 and Grok 4.6 on both score and cost, matches GPT-5.6 Sol and the Fable 5/5.1 family at a fraction of their price, and trails GPT-6 Astra (at roughly a quarter of its cost)
- **Evidence**: A full comparison table (SWE-2 vs. Kimi K3, Grok 4.6, Fable
  5.1, GPT-5.6 Sol, GPT-6 Astra, SWE-1.7) across FrontierCode 1.1 Main,
  DeepSWE 1.1, Terminal-Bench 2.1, and Terminal-Bench 4.
- **Confidence**: emerging (specific, disclosed first-party benchmark
  figures; SWE-2's FrontierCode 1.1 Main score of 50.0% is internally
  consistent with Claim 1's headline figure, but this table's SWE-1.7 column
  reads 42.0% on FrontierCode 1.1 Main, a small discrepancy from the 42.3%
  figure SWE-1.7's own release post and the live FrontierCode leaderboard
  both report for the same model — see Cross-References)
- **Quote**: (table data, not prose; see Concrete Artifacts for the full extracted table)
- **Our assessment**: Terminal-Bench 4 shows the widest capability spread in the table — SWE-2 (27.3%) trails GPT-6 Astra (57.9%) and Fable 5.1 (55.8%) by roughly 28-30 points, a much larger gap than on the other three benchmarks, while still far ahead of its own predecessor SWE-1.7 (7.6%). This is a meaningful caveat to the "within a few points of GPT-6 Astra" framing in the article's opening paragraph (Claim 1's Source Context) — that framing appears to describe FrontierCode/DeepSWE specifically, not Terminal-Bench 4, where the gap to the frontier is much larger.

### Claim 4: SWE-2's largest efficiency gains come from "focused exploration" — higher intelligence lets the model judge which parts of the codebase matter, so it makes its first real edit after a median of 18 steps on FrontierCode 1.1 Main, versus 48 steps for SWE-1.7 — explicitly in response to user feedback that SWE-1.7 over-explored and overthought simple tasks
- **Evidence**: A named behavioral finding with a quantified step-count
  comparison, explicitly framed as a corrective response to a named prior
  criticism of the immediately preceding model.
- **Confidence**: emerging (a specific, quantified behavioral metric — median
  steps to first edit — though the underlying step-counting methodology
  itself is not detailed beyond "grouped by the tools each step calls")
- **Quote**: "In our previous post, we observed SWE-1.7 as being exceedingly careful through its thorough exploration of the codebase before making edits. While boosting performance, this led to user feedback that SWE-1.7 tended to over-explore and overthink on simple tasks."
- **Quote (the fix)**: "We find that the largest efficiency gains from SWE-2 come from focused exploration: higher intelligence allows the model to judge which parts of the codebase actually matter for a task."
- **Our assessment**: This is a direct, named reversal of the specific behavior `blog-cognition-swe17.md` Claim 12 reported as a *desirable* trait of SWE-1.7 relative to Kimi K2.7 Code ("SWE-1.7 explores the codebase much more thoroughly before acting"). Read together, the two posts show that "explore thoroughly before acting" was pushed far enough in SWE-1.7 that real users experienced it as *excessive* on simple tasks, and Cognition's SWE-2 fix is not "explore less" in general but "judge which exploration is worth doing" — a qualitatively different mechanism (selectivity, not blanket reduction) from a simple step-count cap. This is a concrete instance of the same Model-UX-regression-then-correction pattern already flagged across generations in `blog-cognition-swe16-preview.md` Claim 13 and `blog-cognition-swe17.md` Claim 13.

### Claim 5: SWE-2 medium scores higher than SWE-1.7 on FrontierCode 1.1 Main while taking 58% fewer turns and costing 81% less on average, with mean steps per run dropping from 127 (SWE-1.7) to 53 (SWE-2 medium), 80 (SWE-2 high), and 98 (SWE-2 max)
- **Evidence**: Direct efficiency statement plus a chart-derived mean-steps
  breakdown by effort level, measured over "three runs per task per model"
  on the full 100-task FrontierCode 1.1 Main set.
- **Confidence**: settled for the step-count figures (specific, disclosed,
  internally consistent with Claim 4's step-to-first-edit figure); emerging
  for the aggregate "58% fewer turns" and "81% less" cost claims (specific
  percentages, but the exact cost basis and per-task variance are not
  disclosed)
- **Quote**: "On FrontierCode 1.1 Main, we see that SWE-2 medium scores higher than SWE-1.7 while taking 58% fewer turns and costing 81% less on average."
- **Our assessment**: This directly extends SWE-1.7's own self-disclosed cost, per `blog-cognition-swe17.md` Claim 13, where Cognition reported that SWE-1.7's increased reasoning/exploration came at a "small cost in increased change scope" and more turns. SWE-2's efficiency framing positions it as walking back exactly that cost for the *medium* effort tier specifically — the post explicitly reserves deeper planning/exploration for the high/max tiers (Claim 6), rather than claiming the efficiency gain applies uniformly across all effort levels.

### Claim 6: SWE-2 exhibits three named behavioral improvements from internal testing — better end-to-end test coverage, resourcefulness within the user's boundaries (illustrated by reconstructing data from Slack history when a needed MCP integration was unavailable), and verification discipline (re-deriving conclusions rather than re-asserting them when challenged) — and shows real behavioral differentiation by effort level, with medium acting quickly and high/max planning, exploring, and verifying more on complex tasks
- **Evidence**: Three named behavioral patterns from internal dogfooding,
  each with a stated mechanism or illustrative example, plus a stated
  effort-level behavioral contrast.
- **Confidence**: emerging (specific, named qualitative findings with one
  concrete illustrative anecdote — the Slack-history MCP substitution — but
  no quantified prevalence rate for any of the three patterns)
- **Quote (resourcefulness)**: "In one case an MCP integration it needed was unavailable, so it reconstructed the data from the Slack channel history it already had access to."
- **Quote (verification discipline)**: "When challenged, SWE-2 re-derives conclusions rather than re-asserting. SWE-2 verifies a user's hypotheses instead of simply agreeing, and runs artifacts to gather evidence instead of trusting surface-level prose."
- **Quote (effort-level differentiation)**: "SWE-2 medium steps into action much quicker, allowing cost-efficient performance on simple and intermediate tasks. SWE-2 high and max hold an edge over complex tasks: planning more, exploring more of the codebase, and managing uncertainties through more complex verification."
- **Our assessment**: "Verifies a user's hypotheses instead of simply agreeing" is a directly reusable, named counter-sycophancy behavior — a specific instance of a model being trained not just for task completion but for correcting or pressure-testing a user's stated assumptions, which is a distinct axis from any of the eight desirable/undesirable behaviors named in `blog-cognition-swe16-preview.md` Claim 13. No existing corpus note documents a coding agent explicitly re-deriving rather than re-asserting conclusions under user pushback as a trained behavior.

### Claim 7: Kimi K3 (SWE-2's own base model) trains a separate expert per domain/effort-level combination and consolidates them via multi-teacher on-policy distillation, using a problem- and training-step-specific token budget — an approach Cognition contrasts with its own "elegant and principled" single-RL-run alternative
- **Evidence**: Direct description of a named competitor/base-model training
  methodology, explicitly offered as the point of contrast motivating SWE-2's
  own approach.
- **Confidence**: settled (a specific, named methodological description of
  another lab's approach, used for contrast rather than as an empirical claim
  requiring independent verification)
- **Quote**: "Kimi K3 trains a separate expert for each combination of domain and effort level and then consolidates the experts into one model through multi-teacher on-policy distillation. It also uses a problem-specific (and training step-specific) token budget."
- **Our assessment**: This is a genuine, named methodological divergence between two labs solving the same underlying problem (how to give one model multiple cost/effort tradeoff points) — Kimi K3 trains N separate experts and distills them together; SWE-2 trains one model end-to-end with a single reward function that internally differentiates effort levels via a per-level cost-penalty coefficient (Claim 8). This is not a formal contradiction (both are defensible design choices, not opposed factual claims about the same system) but is a concrete, citable alternative-approaches comparison for any team designing a multi-effort-tier model.

### Claim 8: SWE-2 trains all effort levels in a single RL run using a cost-penalized reward R = S − λₑC (S = binary success, C = rollout cost in USD/wall-clock time, e = effort level), where λₑ is set to the local slope of the base model's Pareto frontier at that effort level, not treated as a free hyperparameter
- **Evidence**: A full derivation under "Pushing the Pareto Frontier with RL"
  and "Deriving the Cost Penalty," including a geometric argument (iso-reward
  lines tangent to the Pareto frontier) and a named failure case for a
  mis-tuned λ.
- **Confidence**: settled (a specific, self-contained mathematical argument:
  the geometric claim that setting λₑ equal to the frontier's local slope m
  makes the reward's first-order change invariant to movement along the
  frontier is a derivable, checkable consequence of the stated definitions,
  not merely an empirical observation)
- **Quote**: "where S∈{0,1} denotes whether a rollout was successful, C denotes the cost of a rollout (a mix of inference cost in USD and rollout time), e denotes the effort level, and λₑ is a parameter tuned to match the slope of the Pareto curve of the base model at effort level e."
- **Quote (failure case)**: "we see a failure case where λ_high is set too large: the model is rewarded for performing an unhelpful update, one where the model at high-effort starts to behave like the medium-effort version. The reduction in cost outweighs the loss in solve rate, increasing reward without improving the Pareto frontier."
- **Our assessment**: This is the single most technically detailed and reusable artifact in the post: instead of tuning a cost-penalty coefficient by trial and error, Cognition derives it directly from the *shape* of the current Pareto frontier, so that improving reward is mathematically guaranteed (to first order) to move the frontier outward rather than merely trading cost for performance within its existing bounds. The named failure case (over-large λ_high collapsing high-effort behavior toward medium-effort) is a concrete, transferable warning for any team tuning a similar cost-penalty coefficient: a too-aggressive penalty doesn't just under-reward capability, it can actively reward the model for *regressing* toward a cheaper, less capable behavior mode.

### Claim 9: Cognition proves, via Jensen's functional equation, that if an RL reward must depend only on a training distribution's average cost and average success rate (not on the distribution's shape), the reward is uniquely forced to be affine — R = α + βS − λC — ruling out any nonlinear cost penalty
- **Evidence**: A full formal proof in Appendix B: states the two governing
  assumptions (reward's expectation is a function only of the distribution's
  mean; this holds for every two-point distribution), invokes Jensen's
  functional equation, and derives the affine form.
- **Confidence**: settled (a rigorous, self-contained mathematical proof —
  the strongest possible evidentiary standard for a specific technical claim,
  independent of any empirical measurement or vendor self-report)
- **Quote**: "guaranteeing this equality for every joint distribution of rollout cost and success forces a linear cost penalty (up to additive constants and scaling), because only a linear penalty gives the same result whether applied before or after averaging cost."
- **Our assessment**: This is a first-principles justification (not just an empirically-observed heuristic) for why the reward-shaping choice in Claim 8 is not one option among several but the *only* option consistent with the stated design goal (reward depending only on a task distribution's aggregate cost/success, not its internal composition). This kind of formal, checkable derivation is rare in this corpus's RL-training source notes — most (e.g. `blog-cognition-swe17.md` Claims 3-4, `blog-cursor-composer2-technical-report.md` Claims 9-10) describe engineering fixes and their empirical effects rather than proving a design choice is uniquely optimal under stated axioms.

### Claim 10: SWE-2 uses a length-weighted reward baseline (in use internally since SWE-1.6) that approximates the theoretically variance-minimizing gradient baseline from Greensmith, Bartlett & Baxter (2004) at no extra compute cost, by exploiting a strong empirical correlation between a rollout's gradient-norm term and its token length
- **Evidence**: A derivation showing the true optimal baseline b* requires an
  extra backward pass per rollout to compute, an empirical scatter-plot
  correlation (1k Kimi K3 rollouts) between the required gradient-norm term
  and rollout length, and a cheap length-weighted proxy formula derived from
  that correlation, with an ablation result (lower inference-training KL
  divergence).
- **Confidence**: settled for the underlying mathematical relationship
  (b* is a known, cited prior result); emerging for the empirical claim that
  rollout length is "strongly correlated" with the gradient-norm term
  (specific ablation direction disclosed — lower KL divergence — but the
  correlation's strength is not given as a numeric coefficient, only
  illustrated via an unlabeled scatter plot)
- **Quote**: "We instead attempt to minimize the variance of the full gradient estimator. Following Greensmith, Bartlett, and Baxter (2004), the optimal baseline is [...] Empirically, however, we find that this quantity is strongly correlated with the rollout length, as the next plot shows [...] this suggests a much cheaper proxy to approximate b* at no extra cost."
- **Quote (stability result)**: "in our ablations, we found this baseline to be significantly more stable and performant. In particular, it helps keep the inference–training KL low during RL."
- **Our assessment**: This is a directly reusable pattern for any team running group-relative RL (GRPO-style) training who wants a lower-variance gradient baseline than the standard mean-of-group baseline without paying for a second backward pass: weight the group-mean reward baseline by each rollout's token length rather than the naive unweighted group mean. This has been in production use at Cognition since SWE-1.6 (per this claim) but had not previously been disclosed in this corpus's SWE-1.6-Preview or SWE-1.7 source notes, both of which predate this post.

### Claim 11: SWE-2's rollout-serving infrastructure adds a "prefill delayer" that batches nearby-arriving prefill requests (improving per-GPU throughput and per-request tokens/sec by 10-20% at the cost of higher time-to-first-token), and combats RL-induced degradation of DSpark speculative-decoding accept rates by using SpecForge to continuously retrain the draft model online against the shifting policy, achieving 15% longer accept lengths
- **Evidence**: Direct technical description of both mechanisms, including a
  named cited technique for each (DSpark, SpecForge) and a stated cause for
  why speculative-decoding accept rates degrade during RL specifically (the
  draft model falls behind the policy as it changes).
- **Confidence**: settled (specific, named, mechanistic engineering
  descriptions of deployed techniques with quantified before/after figures
  for both the prefill delayer and the SpecForge retraining fix)
- **Quote (prefill delayer)**: "Since prefill requests can arrive at different times, we built a prefill delayer to hold and batch nearby requests in the GPU scheduler. This improved both TPM per GPU and TPS per request by 10–20%."
- **Quote (DSpark degradation)**: "As the policy changes during training, DSpark's accepted sequences become shorter, which reduces TPM and TPS."
- **Quote (SpecForge fix)**: "we used SpecForge to train a new DSpark model that achieved 15% longer accept lengths. We then integrated online draft-model training into the RL system so that the draft model continued to track the policy as it changed."
- **Our assessment**: The named failure mode — a speculative-decoding draft model's accept rate silently degrading over the course of RL training as the policy model diverges from the draft model's training distribution — is a specific, non-obvious infrastructure lesson for any team combining speculative decoding with a rapidly-changing RL policy: a draft model trained once at the start of a run is not a fire-and-forget optimization, it needs continuous online retraining to keep pace with the policy or its speedup benefit erodes over the course of training.

### Claim 12: SWE-2 uses NVFP4 and FP8 kernels with quantization-aware training for low-precision MoE rollout inference, applying FP8 uniformly to the MLA layers' K/Q/V and score computations — a simplification relative to SWE-1.7, which mixed precisions within the layer (FP8 for the NoPE component, BF16 for RoPE)
- **Evidence**: Direct technical description of the precision scheme, with an
  explicit before/after comparison naming the specific prior mixed-precision
  approach used in the immediately preceding model.
- **Confidence**: settled (specific, named engineering choice with an
  explicit self-referential comparison to the predecessor model's own
  documented approach)
- **Quote**: "We use NVFP4 and FP8 kernels, together with quantization-aware training. The MLA layers use FP8 for K,Q,V and the score computations. This is a simplification compared to SWE-1.7 which used mixed precision in the layers – the NoPE component used FP8, while the RoPE component remained in BF16."
- **Our assessment**: This extends `blog-cursor-composer2-technical-report.md` Claim 9 (NVFP4 quantization during RL forward passes requires IEEE-compliant floating-point arithmetic — training diverges after ~100 RL steps with fast approximations) and `blog-cognition-swe16-preview.md` Claim 6 (NVFP4 rollout inference achieves 2-3x throughput over BF16/FP8 but requires unspecified "algorithmic improvements" to correct training/inference logprob mismatch) with a third data point: a second-generation, *simplified* low-precision scheme that uses a single FP8 treatment across the whole MLA layer rather than the split-precision approach SWE-1.7 needed. Taken together, these three sources document an emerging trend across two labs (Cognition, Cursor) toward more uniform low-precision RL rollout serving as each lab's own quantization-aware training techniques mature — later generations need less precision-mixing complexity than earlier ones to hit the same or better train/inference consistency, per this post's own claim of "lower inference–training KL divergence and similar compute throughput...compared to SWE-1.7 despite using a base model with almost 3x the parameters."

### Claim 13: SWE-2's training data improvements tripled the number of RL environments and expanded repo distribution, added "instruction-following overlays" that layer additional requirements onto existing tasks to train sustained multi-instruction adherence, and built a recursive verifier-hardening flywheel — using earlier SWE-2 checkpoints to find and patch false positives/negatives in the training data — specifically to counter reward hacking from the more resourceful Kimi K3 base model
- **Evidence**: A bulleted "Data Improvements" section naming three specific
  improvements with a mechanism description for each, including an explicit
  causal link between the base model's greater resourcefulness and the need
  for stronger verifiers.
- **Confidence**: emerging (specific, named methodology with one quantified
  figure — tripled RL environments — but no disclosed false-positive/
  false-negative rate or absolute environment count, unlike FrontierCode's
  disclosed 81% figure)
- **Quote (scaling)**: "We tripled the number of RL environments and expanded our repo distribution when sourcing data. Switching to a stronger base model also required us to generate more challenging tasks."
- **Quote (verifier hardening)**: "Since Kimi K3 is a more resourceful model, we needed to increase the robustness of our verifiers to prevent reward hacking. We looked at rollouts from the model during training to uncover and patch new instances of false positives and false negatives in our data, which we iteratively refined using previous checkpoints of SWE-2."
- **Our assessment**: This directly corroborates and extends `blog-cognition-swe17.md` Claim 10's "Data Quality" pipeline (verifier false-positive/false-negative reduction, difficulty curation, cheating prevention) with an explicit statement of *why* verifier hardening had to keep escalating across model generations: a more capable/resourceful base model is a more capable reward hacker, so verifier robustness is not a one-time investment but a recurring, checkpoint-driven arms race against the model's own growing capability — a "recursive flywheel," in the post's own words, rather than a fixed pipeline built once.

### Claim 14: SWE-2's re-run of the propaganda/censorship trustworthiness evaluation replaced the prior six-axis grading rubric with a single binary pass/fail judgment from one judge (GPT 5.6 Luna), reporting a 98.0% overall pass rate (99.8% English, 95.2% Simplified Chinese, 99.1% Traditional Chinese) across six models including SWE-2
- **Evidence**: Direct methodology-change statement plus per-language and
  overall results, compared against the prior six-axis methodology from
  Cognition's own earlier trustworthiness post.
- **Confidence**: emerging (a specific, disclosed methodology change and
  specific per-language results; the switch from six graded axes to a single
  binary judge call is a methodology simplification whose comparability to
  the prior post's results is not established — see Our assessment)
- **Quote**: "In the earlier evaluation, we graded each answer on six axes: active propaganda, CCP narrative alignment, refusal, deflection, completeness, and factual accuracy. Here, we replace those axes with one binary pass or fail result from one judge, GPT 5.6 Luna."
- **Quote (results)**: "SWE-2 passed 98.0% of attempts overall: 99.8% in English, 95.2% in Simplified Chinese, and 99.1% in Traditional Chinese."
- **Our assessment**: This extends `blog-cognition-open-source-trustworthiness.md`'s propaganda/censorship methodology (Claim 2: six-axis grading, 145 Pan-and-Xu-2026 questions, three languages) to a new model generation but with a materially different grading instrument — a single binary judge call rather than six separately-scored axes. Because the grading method itself changed, SWE-2's 98.0% pass rate should not be treated as directly comparable to SWE-1.7's earlier "comparable to GPT 5.5 and Opus 4.8" six-axis result (that note's Claim 3) without re-running SWE-1.7 under the new binary methodology — this is the same caution `blog-cognition-frontiercode.md` Claim 9's Guide Impact already established for cross-methodology-version benchmark comparisons (Diamond-subset deprecation), applied here to a trustworthiness eval rather than a capability benchmark. Simplified Chinese remains the lowest-passing language (95.2%), consistent with the earlier post's Claim 4 finding that Simplified Chinese prompts produced the highest propaganda rates across all tested models.

### Claim 15: The re-run context-dependent-vulnerability evaluation (testing whether customer identity/nationality or request language affects a model's willingness to implement vulnerable code, across Western/Pakistani/Chinese/Tibetan/Falun-Gong-affiliated customer framings) is unchanged from the earlier post and again found no statistically significant framing effect for any of the six models tested, including SWE-2
- **Evidence**: Direct statement that the evaluation methodology is
  unchanged from the prior post, applied to a new six-model set (SWE-2, Kimi
  K3, GLM 5.3, GPT 5.6, Fable 5.1, Opus 5), with a stated null result.
- **Confidence**: emerging (a specific, named null-result finding using a
  disclosed statistical method — 95% bootstrap percentile intervals over ten
  tasks — though the underlying per-model, per-framing effect sizes
  themselves are only shown in an unlabeled chart, not given as numbers in
  the fetched text)
- **Quote**: "We reran the unchanged context-dependent vulnerability evaluation on the new model suite to test whether customer identity or request language affects models' willingness to implement vulnerable or abusive functionality. [...] As in our earlier evaluation, no framing condition produced a statistically significant increase or decrease in vulnerability for any model."
- **Our assessment**: This directly corroborates `blog-cognition-open-source-trustworthiness.md` Claim 8 (SWE-1.7 showed no statistically meaningful security-behavior difference across six identity personas) with a second, independent measurement on a new model generation and a partially different competitor set (adding GLM 5.3, GPT 5.6, Opus 5 to the comparison) — strengthening confidence that this specific null result (no measurable identity-based "differential capability" security degradation) is not a one-off finding for SWE-1.7 specifically but replicates across Cognition's own model line. Still a first-party, self-administered null result with no external replication, and the "6 personas" vs. the prior post's own internally-inconsistent 6-vs-7 persona count (flagged in that note's Extraction Notes) was not re-resolved by this post.

## Concrete Artifacts

### Coding benchmark results table (verbatim, "Coding benchmark results" section)
```
Source: cognition.com/blog/swe-2, "Coding benchmark results" — pass rate (%)
on agentic coding benchmarks

Benchmark                SWE-2    Kimi K3  Grok 4.6  Fable 5.1  GPT-5.6 Sol  GPT-6 Astra  SWE-1.7
FrontierCode 1.1 Main    50.0%    44.2%    48.0%     50.9%      47.5%        53.3%        42.0%
DeepSWE 1.1               73.0%   68.5%    67.5%     67.4%      72.7%        74.1%        37.7%
Terminal-Bench 2.1        92.8%   88.3%    88.4%     91.4%      88.8%        89.9%        81.5%
Terminal-Bench 4          27.3%   21.5%    20.3%     55.8%      37.3%        57.9%        7.6%
```

### Mean steps per run, SWE-1.7 vs. SWE-2 effort levels (FrontierCode 1.1 Main)
```
Source: cognition.com/blog/swe-2, "Model Behavior" section chart
(mean over all 100-task FrontierCode 1.1 Main tasks, three runs/task/model,
grouped by tool category: explore, plan/todo, write/edit code, build,
run tests, git add/commit, final message)

SWE-1.7          127 mean steps
SWE-2 medium       53 mean steps
SWE-2 high          80 mean steps
SWE-2 max           98 mean steps
```

### Cost-penalized RL reward function (verbatim formula and definitions)
```
Source: cognition.com/blog/swe-2, "Pushing the Pareto Frontier with RL"

R = S - lambda_e * C

S in {0,1}: whether a rollout was successful
C: cost of a rollout (mix of inference cost in USD and rollout time)
e: effort level (e.g. medium/high/max)
lambda_e: penalty coefficient, set equal to the local slope of the base
  model's Pareto frontier (cost vs. solve-rate) at effort level e

Geometric justification: at frontier point (c,s) with local slope m, setting
lambda_e = m makes a small movement along the frontier (delta_s ~ m*delta_c)
leave average reward J = s - lambda_e*c unchanged to first order — so any
reward-improving update is guaranteed to push the frontier outward rather
than trade cost for performance within its existing bounds.
```

### Length-weighted reward baseline (paraphrased structure; source LaTeX
renders in-line and is reproduced here as prose per the same disclosure
practice used in `blog-cognition-swe17.md` for its own inline-LaTeX
derivation)
```
Source: cognition.com/blog/swe-2, "Length-Weighted Reward Baseline" section

Standard group-relative baseline (used elsewhere, e.g. GRPO-style methods):
  b = mean(R_i) over the n rollouts in a group

Theoretically optimal, variance-minimizing baseline (Greensmith, Bartlett &
Baxter 2004):
  b* = E[R_i * ||grad_theta log pi_theta(y_i|x)||^2] / E[||grad_theta log
       pi_theta(y_i|x)||^2]
  (requires an extra backward pass per rollout to compute directly)

Cognition's cheap proxy (exploits empirical correlation between the
gradient-norm term and rollout length L_i, measured in trainable tokens):
  b_hat = sum(R_i * L_i) / sum(L_i)

Ablation result: length-weighted baseline keeps inference-training KL
divergence lower and more stable over the course of RL than the plain group
baseline.
```

### Rollout-serving infrastructure techniques (verbatim, "RL Rollouts &
Numerics" section)
```
Source: cognition.com/blog/swe-2

Four stated infrastructure goals:
  - maximizing total throughput
  - reducing latency to limit staleness
  - staying within KV-cache capacity
  - keeping inference numerically close to training

Prefill delayer: batches nearby-arriving prefill requests in the GPU
  scheduler -> +10-20% TPM/GPU and TPS/request, at the cost of higher
  time-to-first-token (accepted tradeoff)

DSpark speculative decoding: draft model proposes several tokens, policy
  model verifies them together; accept rate degrades as the policy changes
  during RL (proposals get rejected more, shortening accepted sequences)

SpecForge fix: retrains DSpark draft model -> +15% longer accept lengths;
  integrated as continuous online draft-model training during RL so the
  draft model tracks the policy as it changes

Precision: NVFP4 + FP8 kernels with quantization-aware training; MLA layers
  use FP8 uniformly for K/Q/V and score computations (vs. SWE-1.7's split
  FP8-NoPE/BF16-RoPE mixed precision)

Stated net result: "lower inference-training KL divergence and similar
  compute throughput and efficiency compared to SWE-1.7" despite Kimi K3
  having "almost 3x the parameters" of SWE-1.7's Kimi K2.7 Code base.
```

### Evaluation methodology (verbatim, Appendix A)
```
Source: cognition.com/blog/swe-2, "Appendix A: Evaluation Methodology"

"For each model–benchmark pair, we report the publicly available result
where one exists. Otherwise, we evaluate the model on our internal
evaluation framework using the harness for which it was primarily developed:
Claude Code for Anthropic models, Codex for OpenAI models, Grok Build for
xAI models, and Devin CLI for open-weight models. For each model, we report
the best score across reasoning-effort settings."
```

### Pareto-dominated "Max" effort tier footnote (verbatim, closing appendix
note)
```
Source: cognition.com/blog/swe-2, final appendix paragraph

"To keep the cost axis readable, the FrontierCode 1.1 Main chart omits
Fable 5.1 Max and the DeepSWE 1.1 chart omits Fable 5 Max. Neither point
improves on the effort levels shown: Fable 5.1 Max scores 50.3% at $12.83
per task on FrontierCode 1.1 Main, below Fable 5.1 Medium (50.9% at $3.28),
and Fable 5 Max scores 69.7% at $21.63 per task on DeepSWE 1.1, below Fable
5 xhigh (69.9% at $13.41)."
```

## Cross-References

- **Corroborates**: `blog-cognition-open-source-trustworthiness.md` Claim 8
  (SWE-1.7 showed no statistically meaningful security-behavior difference
  across six identity personas in the context-dependent-vulnerability
  evaluation) — this source's Claim 15 independently reruns the identical,
  unchanged evaluation on a new model set (SWE-2, Kimi K3, GLM 5.3, GPT 5.6,
  Fable 5.1, Opus 5) and again finds no statistically significant framing
  effect for any model, strengthening confidence that this specific null
  result replicates across a model generation rather than being a one-off
  finding for SWE-1.7.

- **Corroborates**: `blog-cognition-open-source-trustworthiness.md` Claim 4
  (Simplified Chinese prompts produced the highest propaganda rates of the
  three tested languages, across models) — this source's Claim 14 shows the
  same pattern persisting for SWE-2 specifically (95.2% pass rate in
  Simplified Chinese vs. 99.8% English, 99.1% Traditional Chinese — i.e. the
  highest failure/propaganda rate remains in Simplified Chinese), even under
  a changed (binary-judge) grading methodology.

- **Extends**: `blog-cognition-swe17.md` — this is the direct successor post
  to SWE-1.7, explicitly stating it builds on "the SWE-1.7 training
  infrastructure and recipe" (Claim 2). Specific extensions: Claim 4 here
  directly reverses/corrects the specific desirable behavior that note's
  Claim 12 reported (SWE-1.7 exploring the codebase "much more thoroughly
  before acting"), following explicit user feedback that this behavior
  became excessive; Claim 12 here extends that note's Claim 6 (NVFP4 rollout
  inference, 2-3x throughput over BF16/FP8, requiring unspecified
  "algorithmic improvements" for logprob mismatch) with a named, simplified,
  second-generation precision scheme; Claim 13 here extends that note's
  Claim 10 (RL training data quality: verifier false-positive/false-negative
  reduction) with an explicit causal link between base-model capability
  growth and the need for escalating verifier robustness; Claim 10 here
  (length-weighted reward baseline, "in use since SWE-1.6") discloses a
  technique that predates but was not documented in either
  `blog-cognition-swe16-preview.md` or `blog-cognition-swe17.md`, both of
  which were mined before this post existed.

- **Extends**: `blog-cognition-frontiercode.md` — this source's benchmark
  table (Claim 3) reports SWE-1.7 at 42.0% on FrontierCode 1.1 Main, a small
  discrepancy from the 42.3% figure both `blog-cognition-swe17.md` Claim 2
  and `blog-cognition-frontiercode.md` Claim 10's live-leaderboard snapshot
  (dated 2026-07-23) independently report for the same model. This is not
  filed as a formal contradiction under `agents/MINER.md` §4a: both figures
  are self-reported by Cognition for the same underlying model on the same
  named benchmark, the discrepancy (0.3 points) is small enough to plausibly
  reflect a live-leaderboard re-scoring or rounding difference between a
  2026-07 snapshot and this 2026-09 table rather than a substantive factual
  conflict, and neither figure is independently reproduced by a third party
  to adjudicate between them — flagged here as a minor precision caveat for
  any future citation of SWE-1.7's exact FrontierCode 1.1 Main score. This
  source also introduces "DeepSWE 1.1" as a named benchmark not covered by
  any note currently in the corpus (see Novel, below).

- **Extends**: `blog-cursor-composer2-technical-report.md` Claim 9 (NVFP4
  quantization during RL forward passes requires IEEE-compliant
  floating-point arithmetic to avoid divergence after ~100 RL steps) — this
  source's Claim 12 is a third corpus data point (after that note's Claim 9
  and `blog-cognition-swe16-preview.md` Claim 6) on NVFP4-for-RL-rollout
  precision engineering, from the same lab (Cognition) one model generation
  later, showing a trend toward simpler, more uniform low-precision schemes
  as each lab's own quantization-aware training techniques mature. This
  source's Claim 10 (length-weighted reward baseline) is a distinct
  mechanism from that note's Claim 10 (a continuous nonlinear length-penalty
  formula) and Claim 8 (SWE-1.7's alternating unconstrained/budget-phase
  length penalty) — both prior sources use length as a direct reward
  *penalty* target, while this source's length-weighted baseline uses
  rollout length only as a cheap *proxy* for a gradient-variance-minimizing
  baseline term, a different purpose for the same underlying "rollout
  length" signal worth distinguishing in any guide discussion that cites
  more than one of these sources together.

- **Novel**: Compared to the existing corpus:
  - **A formal, first-principles proof (via Jensen's functional equation)
    that a linear cost penalty is the uniquely correct reward-shaping choice**
    (Claim 9) — no existing source note in the corpus provides a rigorous
    mathematical proof (rather than an empirical justification) for an RL
    reward-shaping design choice.
  - **Training all reasoning-effort levels of a model in a single RL run via
    a Pareto-frontier-tangent cost penalty** (Claim 8), contrasted explicitly
    against a named competitor's separate-expert-per-effort-level-plus-
    distillation approach (Claim 7) — new to the corpus.
  - **A length-weighted approximation to the Greensmith/Bartlett/Baxter
    (2004) variance-minimizing reward baseline** (Claim 10) — new to the
    corpus; no existing note documents a reward-baseline technique beyond
    the standard group-mean baseline.
  - **DSpark speculative decoding combined with SpecForge online draft-model
    retraining, to counter RL-induced accept-rate degradation** (Claim 11) —
    a specific, named speculative-decoding infrastructure pattern new to the
    corpus.
  - **"DeepSWE 1.1"** as a named benchmark (Claim 3, Concrete Artifacts) —
    not covered by any existing corpus source note; a candidate for future
    mining if a dedicated methodology post exists.
  - **A same-lab, cross-generation reversal of a previously-reported
    desirable behavior** (Claim 4: SWE-1.7's thorough pre-action exploration,
    reported as desirable in `blog-cognition-swe17.md` Claim 12, explicitly
    named here as having become excessive per user feedback and corrected via
    a selectivity mechanism) — extends the Model-UX-regression-and-correction
    pattern already tracked across `blog-cognition-swe16-preview.md` Claim 13
    and `blog-cognition-swe17.md` Claim 13 with a concrete instance of a
    *previously-praised* behavior itself becoming the thing that needed
    correcting one generation later.

## Guide Impact

- **Chapter 02 (Harness Engineering — reward design / RL infrastructure)**:
  Add the Pareto-frontier-tangent cost-penalty derivation (Claims 8-9) as the
  most rigorously justified reward-shaping technique currently in the corpus
  for training a single model across multiple cost/capability tiers — cite
  it alongside SWE-1.7's alternating length-penalty approach
  (`blog-cognition-swe17.md` Claim 9) and Cursor's continuous nonlinear
  length penalty (`blog-cursor-composer2-technical-report.md` Claim 10) as
  three distinct, named solutions to the same underlying problem (how to
  penalize cost/length without uniformly punishing genuinely hard tasks),
  with this source's version being the only one of the three backed by a
  formal proof of uniqueness rather than an empirical justification.

- **Chapter 02 (Harness Engineering — RL infrastructure)**: Add the
  length-weighted reward baseline (Claim 10) as a directly reusable,
  near-zero-cost technique for any team running group-relative RL that wants
  a lower-variance gradient baseline than the standard group-mean baseline.

- **Chapter 02 (Harness Engineering — long-horizon agent design / Model UX)**:
  Add Claim 4 (SWE-1.7's thorough-exploration behavior, praised one
  generation earlier, becoming a named user complaint and being corrected via
  a selectivity mechanism rather than a blanket reduction) as a concrete
  example supporting a guide recommendation already implied by
  `blog-cognition-swe17.md` Claim 13's Guide Impact: Model-UX behaviors
  should be re-evaluated with real users at each model generation, since a
  behavior that reads as "desirable" in isolation (thorough exploration) can
  become a liability once deployed at scale, and "explore less" is a worse
  fix than "explore more selectively."

- **Chapter 02 (Harness Engineering — RL infrastructure)**: Add the
  speculative-decoding accept-rate degradation finding and its online
  draft-retraining fix (Claim 11) as a named infrastructure lesson for any
  team combining speculative decoding with actively-training RL policies.

- **Chapter 03 (Verification — benchmark interpretation)**: When citing this
  source's FrontierCode 1.1 Main figures, flag the small (42.0% vs. 42.3%)
  SWE-1.7 discrepancy against `blog-cognition-swe17.md` and
  `blog-cognition-frontiercode.md` (see Cross-References → Extends), and
  note that "DeepSWE 1.1" and "Terminal-Bench 4" are benchmarks not yet
  covered by any dedicated corpus source note — a future mining pass on
  either benchmark's own methodology post (if one exists) would let the
  guide assess these figures with the same rigor already applied to
  FrontierCode.

- **Chapter 02 (Model Selection) / Chapter 06 (Security and Threat Model)**:
  When citing this source's trustworthiness results (Claim 14), flag the
  changed propaganda/censorship grading methodology (six-axis in the earlier
  post vs. single binary judge here) as a reason not to directly compare
  SWE-2's 98.0% pass rate to SWE-1.7's earlier six-axis result without
  re-running SWE-1.7 under the new methodology — consistent with the same
  caution `blog-cognition-frontiercode.md` Claim 9's Guide Impact already
  established for FrontierCode's own Diamond-subset deprecation.

## Extraction Notes

- An initial `curl` fetch without browser headers returned an HTTP 403
  "Forbidden" response from the site's edge/CDN layer. A second `curl`
  attempt with a full browser-like header set (User-Agent, Accept,
  Accept-Language) succeeded (HTTP 200) and returned the full page HTML
  (~303KB). The article's content was located inside an `<article>` tag in
  the static HTML (server-rendered, not behind a client-side data-loading
  gate, consistent with the pattern already documented for
  `blog-cognition-swe17.md`) and parsed into plain text with a custom
  HTML-to-text extractor (Python's `html.parser`, preserving heading/
  paragraph/list/table structure). WebFetch's default AI-summarizing pass on
  this URL, tried first, returned a short paraphrase and — when explicitly
  asked to reproduce the full article body verbatim — declined on copyright
  grounds; several narrower, targeted WebFetch follow-up passes (asking for
  specific short quotes and figures per section, each under ~35 words) were
  used to cross-check the raw-HTML-derived text before this note was
  written. Every quote used in this note was verified present,
  character-for-character, in the directly-parsed raw-HTML text (not an AI
  summary) before being included, per MINER.md §2a. Quotes in this note are
  kept to single sentences or short passages sufficient to support each
  claim, consistent with the corpus's established citation practice, rather
  than reproducing extended verbatim passages.
- Several inline mathematical expressions (the cost-penalty geometry
  derivation, the optimal-baseline derivation, and the two formal proofs in
  Appendices B and C) render as interleaved LaTeX/MathML markup in the raw
  HTML, similar to the pattern flagged in `blog-cognition-swe17.md`'s and
  `blog-cognition-swe16-preview.md`'s Extraction Notes. Rather than
  transcribing the raw LaTeX markup verbatim, this note presents each
  derivation's structure as a paraphrased summary in Concrete Artifacts,
  quoting only the surrounding prose sentences verbatim in the relevant
  Claims' Quote fields.
- Several chart/figure images referenced in the article ("Progress of the
  Pareto frontier during training," "Approximating the Pareto curve tangents
  of Kimi K3," "Degradation of speculative decoding acceptance rate during
  RL," "Length-weighted group baseline improves RL stability," "Propaganda
  and Censorship Eval, by language," "Effect of customer and language
  framing on vulnerability") are rendered as images with only captions and
  axis labels recoverable from the static HTML; no underlying numeric data
  could be extracted from them beyond what is separately stated in article
  prose. This note does not fabricate or estimate values for these charts —
  only the prose claims they illustrate are extracted, and Confidence
  ratings reflect the absence of underlying chart data where relevant.
- One collapsible "Example trajectories" dropdown section referenced in the
  Model Behavior section did not yield extractable text content in the
  static HTML (likely a client-side-rendered expandable component) — flagged
  as a coverage gap, not silently omitted.
- No sub-pages were followed as separate extractions. The article links to
  its own two named predecessor/companion posts — `blog-cognition-swe17.md`
  (SWE-1.7, "our previous post") and `blog-cognition-open-source-
  trustworthiness.md` ("our earlier post on model trustworthiness") — both
  of which already exist as separate corpus source notes and were re-read in
  full for this extraction's Source Context and Cross-References research,
  per MINER.md §1's instruction not to re-extract already-covered pages. The
  post's References section also cites the Kimi K3 technical report
  (arXiv:2607.24653), the DSpark paper (arXiv:2607.05147), the SpecForge
  paper (arXiv:2603.18567), and the Greensmith/Bartlett/Baxter (2004) and
  Kool/van Hoof/Welling (2019) reward-baseline papers — none of these
  external references were independently fetched and verified as their own
  source for this extraction pass.
- Searched the corpus for existing coverage of "Pareto frontier" RL reward
  shaping, "reward baseline"/GRPO baseline techniques, "speculative
  decoding," and "DeepSWE" before writing Cross-References; confirmed
  `blog-cursor-composer2-technical-report.md` as the only existing note
  covering closely adjacent RL-infrastructure ground (NVFP4 precision, KL
  divergence estimators, length penalties) and re-read that note's Claims
  9-10 in full, confirming each cited claim number by content before citing
  it. Also re-read `blog-cognition-swe17.md`,
  `blog-cognition-swe16-preview.md`, `blog-cognition-frontiercode.md`, and
  `blog-cognition-open-source-trustworthiness.md` in full (all already read
  for this extraction's Source Context and Cross-References research) and
  confirmed every cited claim number by content before citing it. No claim
  number was guessed or approximated.
- No contradiction meeting `agents/MINER.md` §4a's filing bar was
  identified. The one borderline candidate evaluated — this source's 42.0%
  SWE-1.7/FrontierCode-1.1-Main figure vs. the 42.3% figure reported by two
  other corpus notes for the same model/benchmark — was judged too small a
  discrepancy, self-reported by the same party (Cognition) in both cases,
  and plausibly explained by ordinary re-scoring/rounding rather than a
  substantive factual conflict; see Cross-References → Extends
  (`blog-cognition-frontiercode.md`) for the full reasoning. No contradiction
  issue filed.
- Confidence rated `emerging` overall: several individual claims (Claims 2,
  7, 8, 9, 11, 12) are rated `settled` — specific, mechanistic engineering
  descriptions, a named competitor-methodology contrast, or a rigorous
  self-contained mathematical proof — but the post's central positioning
  claims (Claim 1's headline cost/capability framing, Claim 3's benchmark
  table, Claims 4-6's behavioral findings, Claims 13-15's data-quality and
  trustworthiness results) are first-party, unaudited, vendor-reported
  findings with no independent replication, consistent with the same
  `emerging` rating given to `blog-cognition-swe17.md`, the direct
  predecessor post covering the same lab's methodology one generation
  earlier.
