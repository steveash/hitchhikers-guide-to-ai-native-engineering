---
source_url: https://cognition.com/blog/swe-1-7
source_type: blog-post
title: "SWE-1.7: Frontier Intelligence at a Fraction of the Cost"
author: "Ben Pan, Carlo Baronio, Rohan Choudhury, Eric Lu, Ryan Kim, Deniz Birlikci, TC Qin, Sam Lee, Fermi Ma, Allen Liu, Yang Liu, Sampriti Panda, Jacob Teo, Ray Wang, Gary Chang, Steven Cao, Silas Alberti (Cognition)"
date_published: 2026-07-08
date_extracted: 2026-08-03
last_checked: 2026-08-03
status: current
confidence_overall: emerging
issue: "#2455"
---

# SWE-1.7: Frontier Intelligence at a Fraction of the Cost (Cognition)

> Cognition's technical release post for SWE-1.7 — post-trained via large-scale
> RL on top of an already-RL'd open-source base (Kimi K2.7 Code) — covering
> four infrastructure/algorithm advances since SWE-1.6: an entropy-preservation
> fix (top-p sampling distribution replay) that let training keep improving
> past the point earlier runs stalled, multi-cluster RL training across four
> datacenters on three continents with sub-1%-size compressed weight-delta
> distribution, self-compaction for rollouts up to six hours long, and an
> "alternating length penalty" that compresses response length on easy tasks
> without sacrificing long-horizon capability on hard ones. Reports specific
> behavioral side effects: condensed chain-of-thought, deeper codebase
> exploration before acting, and a widened change-scope tradeoff.

## Source Context

- **Type**: blog-post (Cognition's engineering/research blog, cognition.com,
  published 07.08.26, seventeen named individual authors — a full technical
  release post for a shipping model, not a preview like
  `blog-cognition-swe16-preview.md`). The article is server-rendered directly
  in the page HTML (not client-side JS, unlike the FrontierCode leaderboard
  page) — full verbatim text, including two inline LaTeX derivations and a
  benchmark table, was recovered from the raw HTML.
- **Author credibility**: Seventeen named Cognition Research authors (Ben Pan
  and Carlo Baronio marked as equal-contribution leads, plus Rohan Choudhury,
  Eric Lu, Ryan Kim, Deniz Birlikci, TC Qin, Sam Lee, Fermi Ma, Allen Liu,
  Yang Liu, Sampriti Panda, Jacob Teo, Ray Wang, Gary Chang, Steven Cao, Silas
  Alberti). This is Cognition's own account of its own model release, with a
  direct commercial incentive to present SWE-1.7 favorably — the title itself
  ("Frontier Intelligence at a Fraction of the Cost") is marketing framing.
  It discloses specific, falsifiable technical detail (a policy-gradient
  derivation for why top-p sampling preserves entropy, named hardware/
  infrastructure numbers, a benchmark table that shows SWE-1.7 losing to two
  competitor models on two of three listed benchmarks, and a self-reported
  "increased change scope" cost alongside its capability gains) rather than
  only favorable claims.
- **Scope**: Covers the SWE-1.7 headline positioning and base model (Kimi
  K2.7 Code), a three-benchmark comparison table against seven competitor
  models plus its own predecessor SWE-1.6, four training/infrastructure
  advances (entropy preservation, multi-cluster training, fault tolerance,
  self-compaction and length-penalty shaping), data-quality methodology, two
  named behavioral side effects (chain-of-thought condensation, deeper
  codebase exploration) and their scope-inflation cost, and evaluation
  methodology per benchmark. Does NOT cover: exact model weights/parameter
  count, training data composition or dataset names, dollar-value/revenue
  figures, the trustworthiness/safety evaluation (covered in a linked
  companion post, `blog-cognition-open-source-trustworthiness.md`), or the
  exact reward function used for the RL training itself.

## Extracted Claims

### Claim 1: SWE-1.7, post-trained via large-scale RL from the open-source Kimi K2.7 Code base (which had already undergone extensive RL post-training itself), is framed by Cognition as evidence against a "post-training ceiling"
- **Evidence**: Direct headline framing statement in the article's opening
  section, explicitly naming the base model and characterizing the result as
  a challenge to a specific hypothesis about diminishing RL returns.
- **Confidence**: emerging (first-party, unaudited claim; the "post-training
  ceiling" framing is Cognition's own interpretation of its result, not an
  independently measured or externally validated finding)
- **Quote**: "SWE-1.7 is the result of broad improvements across our RL pipeline: better infrastructure, more stable training, higher-quality data, and new techniques for long-horizon tasks. Since SWE-1.7 was trained from a Kimi K2.7 base, which had already undergone extensive RL post-training, the large additional gains from our own training challenge the idea of a 'post-training ceiling' and suggest that RL can push capabilities much further than previously believed."
- **Our assessment**: This is a notable claim for the broader "is RL post-training saturating?" debate: Cognition argues that stacking a second, independent large-scale RL run on top of a base model that was already heavily RL'd (Kimi K2.7 Code) still produced "large additional gains," rather than diminishing returns. No quantified gain figure is given for this specific claim (see Claim 2 for the actual benchmark deltas); it should be read as an interpretive framing that the rest of the post's four technical sections (entropy preservation, multi-cluster scale, self-compaction, data quality) are offered as the mechanism for. This is new to the corpus — no existing source note directly addresses stacked/repeated RL post-training on an already-RL'd base model.

### Claim 2: On three coding benchmarks, SWE-1.7 outperforms its own base model (Kimi K2.7 Code) and its predecessor (SWE-1.6) by large margins, but trails Claude Opus 4.8 on all three and trails GPT-5.5 on two of three
- **Evidence**: A full comparison table (SWE-1.7 vs. Kimi K2.7 Code, GPT-5.5,
  Opus 4.8, Opus 4.7, GLM-5.2, Composer 2.5, and SWE-1.6) across FrontierCode
  1.1 Main, Terminal-Bench 2.1, and SWE-Bench Multilingual.
- **Confidence**: emerging (specific, disclosed first-party benchmark
  figures; not independently reproduced, though the FrontierCode 1.1 Main
  figure for SWE-1.7 (42.3%) independently matches the live leaderboard
  snapshot already documented in `blog-cognition-frontiercode.md` Claim 10)
- **Quote**: (table data, not prose; see Concrete Artifacts for the full
  extracted table)
- **Our assessment**: The table is a meaningful transparency disclosure
  because it does not present SWE-1.7 as leading every metric — Opus 4.8
  leads on all three listed benchmarks, and GPT-5.5 edges out SWE-1.7 on
  Terminal-Bench 2.1 (84.2% vs. 81.5%) and FrontierCode 1.1 Main (43.0% vs.
  42.3%). SWE-1.7's actual claimed advantage (per the post's "Fraction of the
  Cost" title and 1000 TPS/Cerebras-serving framing in the Source Context)
  is cost/speed at near-frontier capability, not leading capability outright
  — the table is consistent with that narrower claim rather than a
  best-in-class capability claim. The SWE-1.6 column shows a striking
  same-metric jump (FrontierCode 1.1 Main: 9.4% for SWE-1.6 vs. 42.3% for
  SWE-1.7), though the benchmark itself changed underneath both models
  between when SWE-1.6 was evaluated and this table's construction (see
  Cross-References → Contradicts/Extends re: FrontierCode 1.1's
  methodology changes).

### Claim 3: Top-p sampling during RL rollouts prevents entropy collapse because low-probability, off-distribution tokens disproportionately sharpen the token probability distribution when penalized by policy-gradient updates
- **Evidence**: A worked mathematical derivation (three-token toy model,
  softmax probabilities, policy-gradient update to logits) showing that
  penalizing a low-probability token widens the lead of the already-dominant
  token, and top-p sampling prevents such tokens from being sampled and
  optimized against in the first place.
- **Confidence**: settled (a specific, checkable mathematical argument, not
  merely an empirical observation — the derivation is self-contained and its
  conclusion follows from the stated softmax/policy-gradient assumptions)
- **Quote**: "Very low probability tokens are often part of trajectories that have gone off track or out of distribution. These trajectories are likely to produce low reward, and properties of the softmax function lead to these tokens sharpening the token probability distribution. [...] Top-p sampling prevents these low probability tokens from being sampled and used as optimization targets in the first place!"
- **Our assessment**: This is the most technically detailed and reusable artifact in the post: a specific, derivable mechanism (not just an empirical correlation) for why top-p sampling helps entropy stability in RL rollouts, distinct from top-p's more commonly cited role as a text-quality/degeneration control (cited by this same post as ref. [8], Holtzman et al. 2019, "The Curious Case of Neural Text Degeneration"). Any team running RL on LLM policies that has observed entropy collapse should treat sampling-time truncation (top-p, top-k) as a training-stability lever, not just an inference-time quality knob.

### Claim 4: Naive top-p sampling increases training/inference distribution mismatch severely enough to still cause collapse after a small number of steps; the fix is "sampling distribution replay" — recording the rollout-time top-p kept-set and renormalizing the trainer's probabilities against that same mask
- **Evidence**: Direct technical description of the mismatch problem and its
  fix, plus a stated side effect (gradients zero out for above-threshold
  tokens, reducing gradient noise).
- **Confidence**: settled (a specific, mechanistic description of a deployed
  fix with a named, citable prior technique)
- **Quote**: "naively implementing top-p clearly increases the training-inference mismatch — the trainer computes probabilities as a selection from all tokens, while rollouts sample from the top-p subset, so the distributions have higher divergence, leading to collapse after a small number of steps. Thus, we implement sampling distribution replay, where we record a kept-set of tokens available for sampling at rollout time, and renormalize probabilities with those masks in the trainer. With this fix, our run's entropy stays roughly constant over the course of training and inference-training divergence stays bounded."
- **Our assessment**: This is a directly reusable pattern for any team combining truncated sampling (top-p/top-k) with off-policy or asynchronous RL: apply the same truncation mask at training time that was used at rollout time, rather than letting the trainer compute probabilities over the full vocabulary. The disclosed side benefit — a large fraction of sampled tokens sit above the top-p threshold and get zero gradient, reducing gradient noise and concentrating learning signal on harder tokens — is a secondary, non-obvious win from the same fix.

### Claim 5: RL training spans four datacenters across three continents, with only the trainer requiring a single high-bandwidth cluster; inference/rollout engines are self-contained and combine Cognition's own GPUs with additional compute rented from inference providers (Fireworks named)
- **Evidence**: Direct infrastructure description under "Multi-cluster
  Training," stating the structural reason RL decomposes across clusters
  (only the trainer is tightly coupled) and naming the specific cluster
  topology and an external compute partner.
- **Confidence**: settled (specific, named infrastructure topology and a
  named partner)
- **Quote**: "Our RL training spans four datacenters across three continents, combining our own GPUs across multiple clusters with additional compute from inference providers like Fireworks. The result is that we can scale RL training far beyond what any single cluster would allow."
- **Our assessment**: This is a larger-scale, more geographically distributed successor to the async multi-region RL architectures already documented in this corpus — `blog-cursor-composer2-technical-report.md` Claim 16 describes Cursor's Composer 2 training across "3 regions for GPU compute, 4 for CPU compute" with a centralized reconciler, and this source's own predecessor post (`blog-cognition-swe16-preview.md` Claim 9) derives a GPU-allocation formula for a two-stage (inference/training) async pipeline without specifying geographic distribution. This claim adds the explicit "only the trainer needs single-cluster bandwidth; inference is embarrassingly distributable" structural argument, which is the underlying reason both labs' async RL architectures are viable at multi-region scale.

### Claim 6: Cross-continental weight updates for a 1T-parameter model complete in 1-2 minutes end-to-end via compressed weight deltas (>99% size reduction) staged through cloud object storage, causing only 3-4 seconds of inference pause per update
- **Evidence**: A detailed mechanism description: every K gradient steps, a
  compressed delta (not full weights) is computed and uploaded to object
  storage; per-cluster weight controllers poll for new manifests, download
  shards, and replicate via tree broadcast; inference engines prefetch deltas
  into CPU memory and pause only briefly to apply them in-place, preserving
  in-flight trajectories' KV cache.
- **Confidence**: settled (specific, mechanistic, quantified: compression
  ratio, end-to-end latency, and inference-pause duration are all given as
  concrete numbers)
- **Quote**: "every K gradient steps, we compute and send a compressed weight delta between the current and previous weights, reducing the size of each transfer by over 99%[...] With this approach, cross-continental weight updates for a 1T parameter model complete in 1–2 minutes end-to-end. This happens asynchronously and blocks neither training nor inference beyond 3–4 seconds of inference pause at update."
- **Our assessment**: This corroborates and extends `blog-cursor-composer2-technical-report.md` Claim 12 (delta-compressed weight updates for a 1T-parameter model compress to "a handful of gigabytes," distributed via S3) — two independent labs training trillion-parameter-class coding models both converge on delta-compressed weight distribution via cloud object storage as the solution to multi-region weight synchronization, and this source adds concrete end-to-end latency (1-2 min) and inference-disruption (3-4 sec pause) figures that the Cursor report does not disclose. The KV-cache-preserving in-place weight swap (in-flight trajectories continue on new weights without losing their cache) is a specific mechanism not previously documented for either lab's infrastructure.

### Claim 7: Inference-side failures are made cheap by keeping engines stateless (routed and rerouted by NVIDIA Dynamo, with per-sandbox token-recording proxies preventing trajectory loss on worker death), while trainer-side failures are mitigated by per-step async local-disk checkpointing, peer shard replication, and elastic shrink/regrow by whole data-parallel replicas
- **Evidence**: A dedicated "Fault Tolerance" section describing separate
  failure-handling mechanisms for the inference side and the trainer side,
  naming the specific technology (NVIDIA Dynamo) and recovery mechanisms for
  each.
- **Confidence**: settled (specific, named technology and mechanism
  description for a production RL system)
- **Quote**: "We use NVIDIA Dynamo to manage the engine lifecycles and route inference: each agent sandbox has its own proxy that records tokens in and out, so if a replica goes down, we don't lose the full trajectory, and Dynamo reroutes it to a different worker. [...] each node checkpoints asynchronously to local disk every step and replicates its shards to peers, so a dead node's state is rebuilt from replicas in seconds. If capacity is still missing, the run shrinks by whole data-parallel replicas and regrows once nodes return."
- **Our assessment**: The per-sandbox token-recording proxy is a specific, transferable pattern for preserving partial trajectories across worker failures in any long-running agentic rollout system — without it, a worker death mid-rollout would silently discard that trajectory's accumulated tokens/reward signal rather than allowing reroute-and-resume. This is a more granular, named mechanism than the general "warm-standby fault recovery" and "passive/active health checks" described in `blog-cursor-composer2-technical-report.md` Claim 16, though both sources describe the same general problem (surviving hardware failure during long-running async RL without restarting the whole run) at production scale.

### Claim 8: SWE-1.7 is trained with "self-compaction" — when an agent approaches its context limit, it is asked to summarize its own working state and resume from that self-authored summary, with the model simultaneously learning to write better summaries and to work from them — enabling rollouts up to six hours long
- **Evidence**: Direct technique description under "Intelligent
  Self-Compaction for Long-Horizon Tasks," including a stated prior origin
  (first introduced for the Kevin kernel-optimization model) and the
  resulting maximum rollout duration.
- **Confidence**: emerging (a specific, named technique with a concrete
  headline duration figure; the summary-quality outcome is described
  qualitatively — "more informative, succinct summaries" — without a
  disclosed benchmark or metric for summary quality itself)
- **Quote**: "When an agent approaches the context limit, we ask it to summarize its working state, and we resume it from its self-authored summary. During training, the model simultaneously learns (1) to write more informative, succinct summaries, and (2) to better work from and leverage such summaries. We first introduced a version of this approach in Kevin, where we explored it for kernel optimization tasks. With self-compaction, our rollouts during the SWE-1.7 training run reach up to six hours in duration."
- **Our assessment**: This is a directly reusable technique for any team building agent harnesses for long-horizon asynchronous tasks: rather than treating context-window exhaustion as a hard failure mode to engineer around externally (e.g., truncation, external memory stores), Cognition trains the compaction behavior itself into the model via RL, so the model's own summarization quality is optimized by the same reward signal as task completion. The "trains from Kevin" lineage note ties this to a previously undocumented (in this corpus) technique origin.

### Claim 9: Rather than applying a length penalty uniformly, SWE-1.7's training alternates between unconstrained phases (optimizing only for task success) and budget phases (penalizing responses that exceed a weighted cost budget over tokens, turns, and tool-call time), which compresses response length on easy tasks while preserving long-horizon behavior on hard ones
- **Evidence**: Direct technique description under the self-compaction
  section, contrasted against the alternative of a uniform length penalty,
  with a stated rationale (avoiding the DeepSeek-R1-documented tendency of RL
  on reasoning tasks to produce progressively longer responses).
- **Confidence**: emerging (a specific, named technique with a stated
  design rationale and citation to prior published RL-verbosity research;
  the claimed outcome — "response length tends to compress on tasks within
  the model's ability, while long-horizon behavior on hard tasks is
  preserved" — is asserted without a disclosed quantitative before/after
  comparison beyond a referenced chart image)
- **Quote**: "Rather than applying a length penalty uniformly throughout training, we use an alternating strategy. In unconstrained phases, the model optimizes only for task success. In budget phases, we penalize solutions that exceed a certain budget of our weighted cost function that includes tokens, turns and total time spent in tool calls. With this structure, response length tends to compress on tasks within the model's ability, while long-horizon behavior on hard tasks is preserved."
- **Our assessment**: This is a specific alternative to the single continuous nonlinear length-penalty formula documented in `blog-cursor-composer2-technical-report.md` Claim 10 (Cursor's power-law length penalty, applied throughout training rather than alternated in phases) — both labs solve the same problem (avoid uniformly punishing length in ways that hurt genuinely hard, long-horizon tasks) but via different mechanisms: Cursor uses one continuously-applied nonlinear formula, Cognition alternates between unconstrained and budget-constrained training phases. This is a genuine, named methodological divergence worth flagging for any team designing length-penalty reward shaping, though it does not rise to a formal contradiction since both are defensible design choices for the same underlying goal rather than opposed factual claims.

### Claim 10: Cognition's RL training data pipeline addresses three quality dimensions: verifier false-positive/false-negative reduction, deliberately curating tasks the model solves only a low fraction of the time (to preserve learning signal), and cheating prevention via network-restricted, git-history-stripped sandboxes with a zero-reward penalty for any detected cheating attempt regardless of success
- **Evidence**: A bulleted "Data Quality" section naming three specific
  quality dimensions with a description of the mechanism for each,
  including the explicit "reward 0 regardless of success" cheating penalty
  rule.
- **Confidence**: emerging (specific, named methodology with concrete
  mechanism descriptions; no quantitative figures given — e.g., no
  false-positive rate, no solve-rate target band, no cheating-detection
  hit rate — unlike FrontierCode's disclosed 81% figure or SWE-1.7's own
  disclosed cheating-rate figures in the companion trustworthiness post)
- **Quote**: "For instance, we network-restricted our sandboxes and stripped them of git history and reference artifacts. We also isolated the grading path from the agent itself. In addition, we employed programmatic checks to catch known exploit signatures. Finally, to ensure proper incentives, we assigned reward 0 to trajectories with any instance of cheating attempts, regardless of whether they succeeded."
- **Our assessment**: This directly corroborates and extends the FrontierCode 1.1 anti-cheating methodology already documented in `blog-cognition-frontiercode.md` Claim 8 (network-restriction abandoned there in favor of a prompt-plus-classifier approach, because a 1,200-domain blocklist still got bypassed) — but this claim describes RL *training*-time sandboxes, not benchmark-*evaluation*-time sandboxes, and here Cognition does use network restriction plus git-history stripping rather than the prompt-based approach FrontierCode adopted. Read together, this suggests Cognition applies different anti-cheating mechanisms depending on context: network-level restriction is viable for training sandboxes (where task diversity and scale make a hidden, non-negotiable environment acceptable) but was found impractical for FrontierCode's benchmark-evaluation sandboxes (where legitimate internet access, e.g. to GitHub, is sometimes required). This is a meaningful nuance for any team designing anti-cheating controls: the "no internet access" approach that failed for one Cognition system (benchmark eval) is used successfully in a different Cognition system (RL training) — the deciding factor appears to be whether the sandboxed task genuinely requires external network access, not a universal blocklist-vs-prompt tradeoff.

### Claim 11: SWE-1.7 exhibits "condensed chain-of-thought" relative to its base model (Kimi K2.7 Code) — a much lower function-word ratio and nearly half the average words per sentence in its first reasoning pass — which Cognition attributes to the budget phases of its alternating length penalty
- **Evidence**: A named behavioral comparison with two specific linguistic
  metrics (function-word ratio, average words per sentence) and a stated
  causal hypothesis tying the effect to a specific training mechanism
  described earlier in the same post.
- **Confidence**: emerging (a specific, named behavioral finding with two
  quantified linguistic metrics, though the exact percentage/ratio values
  themselves are not given as numbers in the fetched text — only "much
  lower" and "nearly half" — and the causal attribution to budget phases is
  stated as Cognition's own interpretation, not an isolated ablation)
- **Quote**: "One behavioral difference we noticed in SWE-1.7 is condensed chain-of-thought. Compared to Kimi-K2.7-Code, SWE-1.7's first chain-of-thought has a much lower function-word ratio (fraction of words that serve as grammatical 'glue') and nearly half the average number of words per sentence. We think this was influenced directly by the budget phases in our alternating length penalty."
- **Our assessment**: This is independently, prominently corroborated elsewhere in the corpus: `blog-simonwillison-inkling-open-weights.md` Claim 8 documents Thinking Machines Lab observing the identical phenomenon — chain-of-thought becoming more "telegraphic" (dropping articles and connectives) purely as an emergent, unrewarded side effect of RL optimization pressure — and that note explicitly cites "a similar effect...recently noted by the Cognition team in the process of training SWE-1.7," which is this very claim. This source note is therefore the primary-source origin of that cross-lab corroboration: two independent labs (Cognition and Thinking Machines Lab), training different model families with different RL recipes, both observed reasoning traces compressing toward terser, more telegraphic language under large-scale RL. This strengthens the case that CoT-legibility degradation under RL is a general phenomenon rather than an artifact of one lab's specific reward design, with a direct practical implication for anyone building tooling that displays or audits chain-of-thought traces for oversight purposes.

### Claim 12: SWE-1.7 explores the codebase more thoroughly before acting than its base model, investigating root causes, edge cases, and beyond-the-ask requirements rather than addressing only a bug report's primary symptom, and prefers experimentation (e.g. writing small Python scripts) over guessing when semantics are ambiguous
- **Evidence**: A named behavioral comparison plus a specific illustrative
  scenario (bug-fix root-cause investigation vs. primary-symptom-only
  fixes) and a stated mechanism (settling ambiguity via probing/
  experimentation rather than guessing).
- **Confidence**: emerging (a specific, named qualitative behavioral
  finding illustrated with a concrete scenario type, but not quantified
  with a measured rate or percentage in the fetched text beyond a
  referenced chart image on "how often the chain-of-thought probes edge
  cases and hidden requirements")
- **Quote**: "The other major behavioral difference we observed is that SWE-1.7 explores the codebase much more thoroughly before acting, as you can see in the number of tool calls, file reads, and searches the model executes. [...] A bug report typically describes one primary symptom, but the underlying issue often affects a larger surface area. SWE-1.7 is much more likely to investigate the root cause of the bug and consider edge cases, hypotheticals, adversarial inputs, and beyond-the-ask requirements than Kimi-K2.7-Code."
- **Our assessment**: This partially extends the "explores the codebase, gathers context, and reasons before jumping into coding" desirable behavior already listed for SWE-1.6 relative to SWE-1.5 in `blog-cognition-swe16-preview.md` Claim 13 — suggesting thorough-exploration-before-acting is a persistent, reinforced behavior across successive Cognition model generations rather than a one-off improvement. Notably, unlike SWE-1.6's post (which gave an explicit, structured four-item desirable/four-item undesirable "Model UX" behavior checklist), this SWE-1.7 post does not use the "Model UX" framing at all and reports only two named behavioral differences (this claim and Claim 11) plus one named cost (Claim 13) — a narrower and less structured behavioral disclosure than its predecessor post, worth flagging as a completeness gap rather than assuming SWE-1.7 has no other Model-UX-relevant behavior changes.

### Claim 13: SWE-1.7's increased exploration and reasoning comes at the cost of increased change scope — writing more test cases and touching more files than a task strictly requires — a pattern Cognition says it has observed consistently across models industry-wide as reasoning increases
- **Evidence**: A direct statement of the tradeoff, explicitly framed against
  FrontierCode's own scope-discipline grading criterion (cited as ref. [1]),
  plus a generalizing claim about an industry-wide pattern.
- **Confidence**: anecdotal (a qualitative, unquantified tradeoff claim; the
  "we've noticed this trend consistently in models across the industry"
  generalization is asserted without naming which other models or citing
  external data)
- **Quote**: "The extra thinking comes at a small cost in increased change scope. As described in FrontierCode, a good solution modifies only the minimal set of files needed, without touching unrelated code or introducing unnecessary refactors. Since SWE-1.7 reasons more, it also does more: writing additional test cases and touching more files than the task naively requires. We've noticed this trend consistently in models across the industry: as reasoning increases, the scope of files that the model touches also expands. This is an axis we're excited to improve on."
- **Our assessment**: This is a direct, self-disclosed cost that Cognition connects explicitly to its own benchmark's own grading criterion — FrontierCode's "scope" axis (`blog-cognition-frontiercode.md` Claim 2) exists specifically to penalize exactly this behavior, so this claim is Cognition candidly reporting that its own newest model underperforms on a dimension its own benchmark was designed to measure. This also stands in tension with SWE-1.6's previously-reported "fixed" desirable behavior of "avoids writing unnecessary unit tests and documentation" (`blog-cognition-swe16-preview.md` Claim 13) — SWE-1.7 appears to have partially regressed on that specific axis (writing "additional test cases") as a side effect of its increased reasoning depth, which is a notable instance of the general pattern that earlier post itself named: each round of capability-focused RL scaling can reintroduce Model-UX-relevant costs even after a prior generation "fixed" a related behavior.

### Claim 14: Evaluation methodology standardizes per-vendor harness choice across all compared models — Claude Code for Anthropic models, Codex for OpenAI models, and Devin CLI for all other models on Terminal-Bench 2.1, with all models run at maximum reasoning effort
- **Evidence**: A direct "Evaluation Methodology" section listing the
  harness-selection rule per benchmark and per model family.
- **Confidence**: settled (a direct methodology disclosure, not an
  empirical claim requiring verification)
- **Quote**: "All models are evaluated under their maximum reasoning effort. Terminal-Bench 2.1: we evaluate on our own internal evaluation framework, using Claude Code for Anthropic models, Codex for OpenAI models, and Devin CLI for other models, with timeout=4h. SWE-Bench Multilingual: we use self-reported numbers when available and evaluate on Devin CLI otherwise. FrontierCode 1.1: see our blog post."
- **Our assessment**: This is a more standardized, less asymmetric methodology than the one disclosed for SWE-1.6-Preview (`blog-cognition-swe16-preview.md` Claim 3), which used a heterogeneous mix of best-of-2-or-3-harnesses for several competitors while evaluating Cognition's own models on only a single harness — a structural asymmetry that source's own extraction flagged as disadvantaging Cognition's own models relative to competitors. This source's "one harness per vendor family, chosen to match that vendor's own product" rule (Claude Code for Anthropic, Codex for OpenAI, Devin CLI for everyone else, including SWE-1.7 itself) removes the best-of-N-harnesses asymmetry, though it introduces a different potential confound: each vendor's own model is evaluated inside its own team's harness, which may be better-tuned for that specific model than a neutral third-party harness would be.

## Concrete Artifacts

### Coding benchmark results table (verbatim, "Coding benchmark results" section)
```
Source: cognition.com/blog/swe-1-7, "Coding benchmark results" — pass rate
(%) on agentic coding benchmarks, all models at maximum reasoning effort

Benchmark                SWE-1.7  Kimi K2.7 Code  GPT-5.5  Opus 4.8  Opus 4.7  GLM-5.2  Composer 2.5  SWE-1.6
FrontierCode 1.1 Main     42.3%    30.1%           43.0%    46.5%     38.5%     24.5%    25.6%         9.4%
Terminal-Bench 2.1        81.5%    72.7%           84.2%    86.9%     83.0%     81.0%    76.0%         39.7%
SWE-Bench Multilingual    77.8%    73.5%           76.8%    84.4%     80.5%     74.5%    71.6%         58.3%
```

### Top-p entropy-preservation derivation (paraphrased structure; the source's
LaTeX renders in-line and is reproduced here as prose, not transcribed
formula-by-formula, per the same disclosure practice used in
`blog-cognition-swe16-preview.md` for its own image-rendered formulas)
```
Source: cognition.com/blog/swe-1-7, "Preserving Entropy and Stabilizing
Training" section

Setup: three tokens with logits x1 > x2 >> x3, softmax probabilities p_i.
Token 3 (low probability) is sampled from an off-distribution trajectory
that earns low reward (negative advantage A-hat).

Policy gradient update to logits, given token 3 was sampled:
  grad(log p3) = [-p1, -p2, p1+p2]   (w.r.t. x1, x2, x3)
  delta_x1 ∝ |A-hat| * p1
  delta_x2 ∝ |A-hat| * p2
  delta_x3 ∝ -|A-hat| * (p1 + p2)

Result: x3 is penalized, x1 grows more than x2 (since p1 > p2) — sampling
the rare token widens the lead of the already-dominant token, sharpening
the distribution and decreasing entropy. Top-p sampling prevents low-
probability tokens from being sampled/optimized against in the first
place, which is why it preserves entropy in RL rollouts.
```

### Fault tolerance mechanisms (verbatim, "Fault Tolerance" section)
```
Source: cognition.com/blog/swe-1-7

Inference-side failures (cheap by construction):
  - NVIDIA Dynamo manages engine lifecycles and inference routing
  - Each agent sandbox has its own proxy recording tokens in/out
  - Dead replica -> Dynamo reroutes in-flight trajectory to a healthy worker
  - On reschedule: weight controller loads latest checkpoint from object
    storage, replays deltas from that checkpointed version

Trainer-side failures (expensive — single tightly-coupled component):
  - Each node checkpoints asynchronously to local disk every step
  - Shards replicated to peer nodes -> dead node rebuilt from replicas
    in seconds
  - If capacity still missing: run shrinks by whole data-parallel replicas,
    regrows once nodes return
  - Rollout pipeline stays warm throughout; a buffer policy selects which
    accumulated rollouts to use after restart, preventing throughput-
    imbalance bias
```

### Data quality pipeline (verbatim, "Data Quality" section)
```
Source: cognition.com/blog/swe-1-7

1. Verifier quality: minimize both false positives (accepting incorrect
   solutions) and false negatives (rejecting valid ones) via QA pipelines
2. Difficulty: curate tasks the model solves only a low fraction of the
   time — tasks always-solved or always-failed give no learning signal
3. Cheating detection/prevention:
   - Network-restricted sandboxes
   - Sandboxes stripped of git history and reference artifacts
   - Grading path isolated from the agent itself
   - Programmatic checks for known exploit signatures
   - Reward = 0 for any detected cheating attempt, regardless of success
```

### Model availability (verbatim, intro section)
```
Source: cognition.com/blog/swe-1-7

"SWE-1.7 is available today in Devin (Web, Desktop, and CLI) via Cerebras
at 1000 TPS."
```

## Cross-References

- **Corroborates**: `blog-simonwillison-inkling-open-weights.md` Claim 8
  (Thinking Machines Lab's Inkling exhibiting emergent, unrewarded chain-of-
  thought compression under large-scale RL, "dropping articles and
  connectives" while remaining comprehensible) — that note's Claim 8
  explicitly names "a similar effect...recently noted by the Cognition team
  in the process of training SWE-1.7," which is this source's Claim 11. This
  source note is the primary-source origin that citation refers to: two
  independent labs, training unrelated model families, both report
  chain-of-thought becoming measurably terser and more telegraphic purely as
  a side effect of RL optimization, not a targeted reward. This is a
  meaningful two-lab corroboration for anyone treating CoT-legibility
  degradation as a general property of large-scale RL rather than a
  one-off artifact.

- **Corroborates**: `blog-cognition-frontiercode.md` Claim 10 (live
  FrontierCode 1.1 Main leaderboard snapshot, dated 2026-07-23, showing
  SWE-1.7 at position 7, 42.3%) — this source's own benchmark table
  (Claim 2/Concrete Artifacts) independently states the identical 42.3%
  figure for SWE-1.7 on FrontierCode 1.1 Main, from the same underlying
  Cognition results but published two weeks earlier (2026-07-08) as a
  first-party self-report rather than a live-leaderboard scrape — the exact
  number match across two independently-extracted sources strengthens
  confidence in the figure's stability.

- **Contradicts**: None filed as a formal contradiction issue. One candidate
  was evaluated and did not meet the `agents/MINER.md` §4a bar: this
  source's Claim 10 (RL training sandboxes use network restriction plus
  git-history stripping as an anti-cheating measure) sits in apparent tension
  with `blog-cognition-frontiercode.md` Claim 8 (FrontierCode explicitly
  rejected network-level blocklisting as impractical, citing a 1,200-domain
  blocklist that agents still bypassed). This is not a same-claim conflict —
  the two describe different systems with different constraints (a
  benchmark-evaluation sandbox where legitimate GitHub/documentation access
  is sometimes required, vs. an RL-training sandbox where the task set is
  fully controlled and external network access is presumably never required
  for a correct solution) — see Claim 10's "Our assessment" for the full
  reasoning.

- **Extends**: `blog-cognition-swe16-preview.md` — this is the direct
  successor post to SWE-1.6-Preview, covering the shipped SWE-1.7 model.
  Specific extensions: Claim 5/6 here extend that note's Claim 9 (a
  closed-form GPU-allocation formula for a two-stage async RL pipeline,
  without disclosed geographic distribution) with an explicit multi-
  continent, multi-datacenter topology and concrete cross-continental
  weight-update latency figures. Claim 12 here extends that note's Claim 13
  (SWE-1.6's "explores the codebase...before jumping into coding" desirable
  behavior) with a second-generation confirmation that thorough pre-action
  exploration persisted and strengthened in SWE-1.7. Claim 14 here extends
  that note's Claim 3 (SWE-1.6-Preview's asymmetric best-of-N-harnesses
  evaluation methodology) with a more standardized, less asymmetric
  per-vendor-harness rule.

- **Extends**: `blog-cursor-composer2-technical-report.md` — both sources
  document trillion-parameter-class coding-model RL training infrastructure
  from competing labs, and several specific mechanisms converge: this
  source's Claim 6 (delta-compressed weight updates, >99% size reduction,
  1-2 min cross-continental distribution) extends that note's Claim 12
  (delta-compressed 1T-parameter weight updates "a handful of gigabytes,"
  no latency figure disclosed) with concrete end-to-end timing; this
  source's Claim 5 (four datacenters, three continents) extends that note's
  Claim 16 (3 GPU regions, 4 CPU regions, centralized reconciler) with an
  explicit structural argument for why RL specifically (as opposed to
  supervised training) decomposes across regions; this source's Claim 9
  (alternating unconstrained/budget-phase length penalty) is a distinct
  design alternative to that note's Claim 10 (a single continuous nonlinear
  length-penalty formula) for the same underlying goal (proportional length
  penalization by task difficulty).

- **Extends**: `blog-cognition-open-source-trustworthiness.md` — the
  companion post explicitly linked from this source ("We expand on this
  extensively in our companion blog post, Measuring the Trustworthiness of
  Open-Source-Derived Models"), covering SWE-1.7's propaganda/refusal/
  differential-security evaluation as a distinct axis from this source's
  capability/infrastructure/behavioral-tendency coverage.

- **Novel**: Compared to the existing corpus:
  - **A derived, mechanistic explanation (not just an empirical
    observation) for why top-p sampling preserves entropy in RL rollouts**
    (Claim 3) — no existing source note in the corpus provides a
    policy-gradient-level derivation for this effect.
  - **"Sampling distribution replay"** (Claim 4) as a named technique for
    reconciling truncated sampling with training-time probability
    computation — new to the corpus.
  - **Self-compaction as a trained-in agent behavior** for long-horizon
    tasks (Claim 8), with a disclosed maximum rollout duration (six hours)
    — new to the corpus; no existing note documents training a model to
    summarize and resume its own working state via RL.
  - **The specific "post-training ceiling" framing** (Claim 1) — stacking
    independent large-scale RL runs on an already-RL'd open-source base
    model and reporting large additional gains — is a new data point for
    the corpus's ongoing "is RL post-training saturating?" discussion, not
    previously addressed by any existing source note.
  - **A same-lab, cross-generation instance of a previously-"fixed"
    behavior partially regressing** (Claim 13: SWE-1.7 writing "additional
    test cases," in tension with SWE-1.6's previously reported fix of
    "avoids writing unnecessary unit tests and documentation") — extends
    the Model-UX-regression pattern first named in
    `blog-cognition-swe16-preview.md` with a concrete instance of a
    specific behavior being un-fixed by a later training run.

## Guide Impact

- **Chapter 02 (Harness Engineering — RL infrastructure)**: Add the top-p
  sampling / entropy-collapse mechanism (Claim 3) and its fix, sampling
  distribution replay (Claim 4), as a concrete, reusable pattern for any
  team running RL on LLM policies that has observed entropy collapse or
  reward plateau within the first few hundred training steps — this is the
  most mechanistically detailed (derivation-backed, not just empirical)
  explanation for this failure mode currently in the corpus.

- **Chapter 02 (Harness Engineering — long-horizon agent design)**: Add
  self-compaction (Claim 8) as a named technique for extending agent task
  horizons past the raw context window by training the summarize-and-resume
  behavior directly into the model via RL, rather than only engineering
  external context-management scaffolding — citing the six-hour maximum
  rollout duration as a concrete upper bound this technique enabled.

- **Chapter 02 (Harness Engineering — reward design) / Chapter 03
  (Verification)**: Add Claim 13 (increased change scope as a cost of
  increased reasoning/exploration, explicitly measured against Cognition's
  own FrontierCode scope-discipline criterion) as a concrete, self-disclosed
  example of a capability/Model-UX tradeoff, and flag it alongside SWE-1.6's
  earlier "fixed" unnecessary-test-writing behavior
  (`blog-cognition-swe16-preview.md` Claim 13) as an instance of a specific
  named behavior regressing in a later model generation — supporting a
  guide recommendation that Model-UX regressions should be tracked
  per-behavior across model generations, not assumed to stay fixed once
  addressed once.

- **Chapter 03 (Verification — benchmark interpretation)**: When citing
  SWE-1.7's FrontierCode 1.1 Main score (42.3%), cross-reference
  `blog-cognition-frontiercode.md`'s corroborating leaderboard snapshot and
  its Claim 9 caveat (FrontierCode 1.1 deprecated the Diamond subset for
  noisy low solve rates) — this source's own SWE-1.6 column (9.4% on
  FrontierCode 1.1 Main) should not be treated as directly comparable to
  any pre-1.1 FrontierCode figures for SWE-1.6 cited elsewhere, since the
  benchmark methodology itself changed between versions.

- **Chapter 05 (Cost-Performance Tradeoffs)**: Add this source's cost/speed
  positioning (1000 TPS via Cerebras serving, explicit "Fraction of the
  Cost" framing, and a benchmark table that shows SWE-1.7 trailing Opus 4.8
  on every listed benchmark and GPT-5.5 on two of three) as a concrete,
  self-disclosed example of a vendor explicitly competing on cost/speed
  Pareto-efficiency rather than claiming outright leading capability —
  useful as a template for how to read "frontier at a fraction of the cost"
  claims: check whether the benchmark table itself supports a leading-
  capability claim or only a cost-efficiency claim before citing either.

## Extraction Notes

- The article is server-side rendered directly into the page HTML (unlike
  the FrontierCode leaderboard page, which loads its table via client-side
  JavaScript, per `blog-cognition-frontiercode.md`'s Extraction Notes).
  WebFetch's default AI-summarizing pass returned only a short paraphrase
  (title, headline benchmark figures, four bullet-point section summaries)
  consistent with the pattern documented for this domain in
  `blog-cognition-swe16-preview.md` and `blog-cognition-open-source-
  trustworthiness.md`. This note instead fetched the raw HTML directly via
  `curl` with a browser user-agent, located the article content within a
  `<article>` tag in the static HTML (not behind a client-side data-loading
  gate), and parsed it with a custom HTML-to-text extractor (Python's
  `html.parser`, preserving heading/paragraph/list/table structure and
  section IDs) rather than relying on an AI-summarized pass. Every quote
  used in this note was verified present, character-for-character, in that
  directly-parsed raw-HTML text before being included, per MINER.md §2a.
- Two inline mathematical expressions (the policy-gradient derivation under
  "Preserving Entropy and Stabilizing Training") render as LaTeX/MathML
  markup interleaved with the surrounding prose in the raw HTML, similar to
  the image-rendered formulas flagged in `blog-cognition-swe16-preview.md`'s
  Extraction Notes. Rather than transcribing the raw LaTeX markup verbatim
  (which would be unreadable and is not a clean "quote" in the prose sense),
  this note presents the derivation's structure as a paraphrased summary in
  Concrete Artifacts, consistent with that prior note's disclosed practice,
  and quotes only the surrounding prose sentences verbatim in Claim 3's
  Quote field.
- Two chart/figure images referenced in the article ("Policy entropy across
  training," "Training-inference mismatch across training," "Response
  length under the alternating length penalty," "Behavioral tendencies on
  FrontierCode 1.1 Main," "How often the chain-of-thought probes edge cases
  and hidden requirements") are rendered as images with only short captions
  recoverable from the static HTML; no axis values or underlying data could
  be extracted from them. This note does not fabricate or estimate values
  for these charts — only the prose claims they illustrate are extracted,
  and each such claim's Confidence rating reflects the absence of the
  underlying chart data (rated `emerging` or `anecdotal` rather than
  `settled` where the only support is an unreadable chart image).
- Two collapsible/dropdown sections referenced in the text ("We've included
  a couple of examples of condensed chain-of-thought in the dropdown
  below" and "We've attached a couple of example trajectories in the
  dropdown below") did not yield extractable text content in the static
  HTML — these are likely client-side-rendered expandable UI components
  whose content loads separately. This is flagged as a coverage gap rather
  than silently omitted; a future re-extraction with a JS-rendering fetch
  tool could recover this content if it proves valuable.
- No sub-pages were followed as separate extractions. The article links to
  its own companion trustworthiness post (already covered by
  `blog-cognition-open-source-trustworthiness.md`, issue #2453, mined the
  same day) and to the FrontierCode leaderboard/methodology posts (already
  covered by `blog-cognition-frontiercode.md`) — both already exist as
  separate corpus source notes, so per MINER.md §1 these were not
  re-extracted here, only cross-referenced. The article's numbered
  References section (18 external citations — arXiv papers, prior Cognition
  posts, external blog posts) was read in full and used to attribute
  specific techniques to their originating research (e.g., top-p sampling
  to Holtzman et al. 2019, entropy-collapse framing to Cui et al. 2025 and
  Yu et al. 2025/DAPO, self-compaction's Kevin-32B lineage) but no
  individual reference was independently fetched and verified as its own
  source for this extraction pass.
- Searched the corpus for existing coverage of "post-training ceiling,"
  "entropy collapse," "top-p" RL usage, and "multi-cluster"/datacenter RL
  training before writing Cross-References; confirmed
  `blog-cursor-composer2-technical-report.md` as the only existing note
  covering closely adjacent RL-infrastructure/training-stability ground
  (KL divergence estimators, NVFP4 precision, length penalties, delta
  weight compression, multi-region async RL) and re-read that note's Claims
  8-12 and 16 in full, confirming each cited claim number by content before
  citing it. Also re-read `blog-cognition-swe16-preview.md` and
  `blog-cognition-frontiercode.md` in full (both already read for this
  extraction's Source Context research) and
  `blog-simonwillison-inkling-open-weights.md` in full, confirming Claim 8
  by content before citing it. No claim number was guessed or approximated.
- No contradiction meeting `agents/MINER.md` §4a's filing bar was
  identified — see Cross-References → Contradicts for the one candidate
  evaluated and why it did not meet the bar. No contradiction issue filed.
- Confidence rated `emerging` overall: several claims (Claims 3, 4, 5, 6, 7,
  14) are individually rated `settled` — specific, mechanistic, checkable
  engineering descriptions or direct methodology disclosures — but the
  post's central positioning claims (Claim 1's "post-training ceiling"
  framing, Claim 2's benchmark table, Claims 8-13's behavioral and
  data-quality findings) are first-party, unaudited, vendor-reported
  results with no independent replication, several qualitative claims
  lacking disclosed quantitative figures (e.g., Claim 11's "much lower"
  function-word ratio without a stated percentage), and at least one
  generalizing claim (Claim 13's "industry-wide" trend assertion) made
  without external citation. This is not rated `anecdotal` overall because
  multiple claims include specific, falsifiable, mechanistic detail
  (the top-p derivation, the fault-tolerance architecture, the exact
  benchmark table) well beyond typical marketing copy.
