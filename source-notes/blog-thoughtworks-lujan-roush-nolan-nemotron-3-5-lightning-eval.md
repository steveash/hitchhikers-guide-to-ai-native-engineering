---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/putting-nvidia-nemotron-3-5-lightning-test
source_type: blog-post
title: "Putting NVIDIA Nemotron 3.5 Lightning to the Test"
author: Gustavo Lujan, Allen Roush, Andy Nolan (Thoughtworks)
date_published: 2026-08-11
date_extracted: 2026-08-21
last_checked: 2026-08-21
status: current
confidence_overall: emerging
issue: "#2839"
---

# Putting NVIDIA Nemotron 3.5 Lightning to the Test

> A Thoughtworks technical evaluation of NVIDIA's Nemotron 3.5 Lightning (a
> 30B-MoE/3B-active model distilled from Nemotron 3 Ultra) reports a
> reproducible low-rank-adapter post-training workflow that roughly doubled
> legal-domain benchmark accuracy and improved healthcare-domain accuracy in
> a few GPU-hours, a separate "antislop" behavioral-tuning pass that cut
> stylistic AI writing tells by two-thirds with no measured quality loss, and
> a built-in speculative decoder giving 1.46-1.96x throughput that a custom
> EAGLE-3 draft head could match but not beat.

## Source Context

- **Type**: blog-post (practitioner technical evaluation, Thoughtworks
  Insights). Reports three linked technical reports hosted at
  research.thoughtworks.com/library/ for deeper methodology; this note
  extracts from the blog post itself, which summarizes all three reports
  with headline numbers, p-values, and a benchmark table.
- **Author credibility**: Gustavo Lujan, Allen Roush, and Andy Nolan are
  Thoughtworks practitioners publishing under the Thoughtworks Insights
  brand — a source already in this corpus as a trusted, vendor-neutral
  practitioner feed (see the many other `blog-thoughtworks-*` notes). This
  is a first-party hands-on evaluation with concrete numbers, statistical
  tests, and reproducible hardware specs, not a vendor announcement or news
  digest — a step up in rigor from `blog-thebatch-nemotron-agent-infra.md`,
  which reports Nvidia's own first-party benchmark claims for a different
  Nemotron variant secondhand.
- **Scope**: Covers three distinct experiments on Nemotron 3.5 Lightning: (1)
  low-rank-adapter (LoRA-style) domain post-training for legal and healthcare
  domains, evaluated via blind pairwise comparison and domain benchmarks; (2)
  an "antislop" behavioral fine-tuning pass to reduce repetitive/formulaic AI
  writing patterns, using Thoughtworks' own published antislop framework; (3)
  inference-speed benchmarking of the model's built-in speculative decoder
  versus a custom-trained EAGLE-3 draft head. Does not cover: the underlying
  LoRA rank/alpha hyperparameters or the training dataset composition, which
  the blog post does not state and which would require reading the three
  linked technical reports directly (not fetched in this extraction — see
  Extraction Notes).

## Extracted Claims

### Claim 1: Post-training Nemotron 3.5 Lightning on a legal-domain adapter produced a 75% win rate over the base model in blind pairwise comparisons, statistically significant at p < 0.001

- **Evidence**: Blind comparison of 163 question/answer pairs (112 won by the
  adapted model), judged by "an independent AI judge from a different model
  family" rather than human raters — a methodology detail worth flagging
  when weighing this claim.
- **Confidence**: emerging (single practitioner report with a stated
  significance test; judge is an LLM, not a human panel, and the specific
  judge model is not named in the blog post)
- **Quote**: "75% win rate"
- **Our assessment**: A p < 0.001 result on 163 comparisons is a real signal,
  not noise, but "judged by an independent AI judge from a different model
  family" is doing a lot of work here — LLM-judge preference does not
  necessarily track legal correctness or usefulness to a practicing lawyer.
  The CaseHOLD benchmark result (Claim 2) is the more objective corroborating
  data point for the same domain.

### Claim 2: The legal-domain adapter more than doubled CaseHOLD benchmark accuracy, from 35% to 77%

- **Evidence**: Direct before/after benchmark comparison on CaseHOLD, a
  published legal-reasoning benchmark (multiple-choice holding selection from
  case law).
- **Confidence**: emerging (single-source benchmark result, not independently
  reproduced by a third party in this extraction)
- **Quote**: "from 35% to 77%"
- **Our assessment**: This is the strongest single data point in the source
  because CaseHOLD is a fixed, objective benchmark rather than an LLM-judged
  preference comparison. A 42-point jump on a domain-specific benchmark from
  a low-rank adapter trained in "a few hours" on one node is a large
  capability delta for a comparatively cheap post-training pass, assuming the
  benchmark wasn't part of the adapter's training data (not addressed in the
  blog post — see Extraction Notes).

### Claim 3: The legal-domain adapter preserved general capability, staying within 1.5 points of the base model on reasoning, mathematics, and legal-knowledge benchmarks

- **Evidence**: Comparison of adapted-vs-base model scores across a general
  benchmark suite (specific benchmark names for this comparison are not
  listed in the blog post beyond "reasoning, mathematics, and legal
  knowledge").
- **Confidence**: emerging
- **Quote**: "within 1.5 points of the base model"
- **Our assessment**: This is the claim that makes the domain-adaptation
  result actionable rather than merely impressive — a 42-point domain gain
  (Claim 2) would be far less useful if it came at the cost of general
  capability regression. A small adapter that doesn't measurably degrade
  general reasoning is consistent with how LoRA-style adapters are commonly
  claimed to work (base weights frozen, small additive parameters), though
  the blog post doesn't confirm the adapter mechanism was literally LoRA
  (rank/alpha not stated).

### Claim 4: Post-training Nemotron 3.5 Lightning on a healthcare-domain adapter produced a 60% win rate over the base model in blind comparisons (p = 0.002), with clinical prediction error falling 24% and answer-token accuracy rising from 64% to 69%

- **Evidence**: 167 question/answer pairs compared (82 won by the adapted
  model), same LLM-judge methodology as the legal evaluation, plus a
  separate clinical-accuracy metric.
- **Confidence**: emerging (same single-practitioner-report caveat as Claim
  1; healthcare domain adds direct-harm stakes if this were deployed without
  further validation)
- **Quote**: "answer-token accuracy rose from 64% to 69%"
- **Our assessment**: The healthcare win rate (60%) and effect size are
  smaller than the legal domain's (75% win rate, doubled CaseHOLD accuracy),
  suggesting domain adaptation gains are not uniform across domains — legal
  reasoning over case-law text may be a more learnable pattern for a
  low-rank adapter than clinical judgment. The source does not discuss why
  the two domains diverge, which the guide should flag as an open question
  rather than assume a single "domain adaptation works this well" number.

### Claim 5: A separate "antislop" behavioral-tuning pass identified 4,267 overused stylistic patterns in the model's output and eliminated 66.4% of them via ~13,000 generated training examples, with no measured loss in writing quality

- **Evidence**: Applied Thoughtworks' own previously-published antislop
  framework (MIT-licensed, referenced at arxiv.org/pdf/2510.15061) to
  identify and retrain away repetitive "AI writing tell" patterns; trained on
  two H100 GPUs over roughly thirteen hours.
- **Confidence**: emerging
- **Quote**: "66.4% of the identified overused patterns were eliminated"
- **Our assessment**: This is a distinct intervention from the domain
  adapters (Claims 1-4) — it targets stylistic tics (repetitive phrasing,
  formulaic transitions — the "AI writing tell" phenomenon) rather than
  domain accuracy. A two-thirds reduction in identified overused patterns
  without a stated drop in a human-facing quality metric is a notable result
  for teams trying to make model output read less mechanically, though
  "writing quality was statistically unchanged" is itself measured by
  whatever quality metric the linked antislop technical report defines —
  not detailed in the blog post itself.

### Claim 6: The antislop tuning pass preserved vocabulary richness at 98.4% of baseline while writing quality was statistically unchanged

- **Evidence**: Stated companion metrics to the 66.4% pattern-elimination
  result, from the same experiment.
- **Confidence**: emerging
- **Quote**: "vocabulary richness held at 98.4% of baseline"
- **Our assessment**: Vocabulary richness holding near-constant is a useful
  proxy that the intervention didn't just make output blander or more
  repetitive in a different way — a plausible failure mode for aggressive
  anti-repetition training that this metric appears designed to catch.

### Claim 7: The antislop tuning pass had mixed, non-uniform effects on downstream task benchmarks — a slight gain on MMLU-Pro, a real drop on HumanEval+ and tau-bench, and no change on IFEval

- **Evidence**: Before/after benchmark table comparing the "original" and
  "antislop" model versions: MMLU-Pro 0.703 to 0.713; HumanEval+ 0.750 to
  0.707; IFEval 0.387 to 0.387 (unchanged); tau-bench customer-service 0.640
  to 0.624.
- **Confidence**: emerging (this is the source's own reported table; not
  independently reproduced)
- **Quote**: (no direct quote captured for this table; see Concrete
  Artifacts for the reproduced values)
- **Our assessment**: This is the most important nuance the headline "no
  quality loss" framing (Claims 5-6) glosses over: HumanEval+ dropped 4.3
  points and tau-bench dropped 1.6 points after antislop tuning, even though
  the source's own "writing quality was statistically unchanged" claim
  presumably refers to a different (prose-quality) metric than these
  task-benchmark scores. A guide citing this source should present both the
  antislop framing and this benchmark table together rather than repeating
  only the "no quality loss" claim, since the coding and agentic-tool-use
  benchmarks moved in the wrong direction.

### Claim 8: Nemotron 3.5 Lightning is a 30B-parameter mixture-of-experts model with 3B active parameters, distilled from NVIDIA's larger Nemotron 3 Ultra

- **Evidence**: Architecture description in the source, distinguishing this
  "Lightning" variant from the larger Nemotron model family.
- **Confidence**: settled (model architecture facts, not a benchmark claim)
- **Quote**: "a 30B mixture-of-experts with 3B active parameters distilled
  from NVIDIA's frontier Nemotron 3 Ultra"
- **Our assessment**: This is a materially smaller, cheaper model than the
  Nemotron 3 Super 120B-A12B variant already in this corpus (see
  Cross-References) — 3B active parameters vs. 12B active, and distilled
  rather than trained from scratch. The two Nemotron notes in this corpus
  now cover opposite ends of the same model family's size/cost spectrum,
  which is useful for a guide section comparing open-weights model sizing
  tradeoffs for agentic vs. domain-specific deployments.

### Claim 9: Nemotron 3.5 Lightning's built-in native speculative decoder delivers 1.46-1.96x the throughput of unaccelerated decoding, reducing measured inference cost from $0.477 to $0.250 per million output tokens

- **Evidence**: 2,091 throughput measurements across three workloads and
  concurrency levels 1-128, comparing the model's default-enabled built-in
  multi-token-prediction speculative decoder against unaccelerated decoding,
  on H200 and B200 GPU generations.
- **Confidence**: emerging (single-practitioner measurement at meaningful
  sample size, but self-reported and not independently reproduced)
- **Quote**: "1.46–1.96× the throughput of unaccelerated decoding"
- **Our assessment**: A near-halving of per-token output cost from a
  decoder that ships enabled by default (no extra engineering work required)
  is a strong, immediately actionable result for teams running this specific
  model. The range (1.46x-1.96x) spanning three workloads and a wide
  concurrency sweep gives more confidence than a single best-case number
  would.

### Claim 10: A custom-trained EAGLE-3 speculative-decoding draft head, trained specifically for this model, matched but did not exceed the throughput of the built-in native decoder

- **Evidence**: Direct comparison between a bespoke EAGLE-3 draft head
  (trained by the Thoughtworks team, presumably against their own
  domain-adapted checkpoint) and the model's default built-in decoder.
- **Confidence**: emerging (single practitioner test, one model, one
  architecture generation)
- **Quote**: (no direct quote; see paraphrase above and Concrete Artifacts —
  the WebFetch tool declined to reproduce the exact sentence verbatim beyond
  short fragments, but confirmed "matched but didn't exceed" as the reported
  outcome across two independent fetches)
- **Our assessment**: This is a genuinely useful negative result: building a
  custom draft head is real engineering investment, and finding it doesn't
  beat a vendor-shipped default is actionable information that saves other
  teams the same effort — for this specific model. It is in tension with a
  different corpus source's stronger claim about traffic-specific draft
  model training; see Cross-References → Contradicts below. This note does
  not resolve that tension.

## Concrete Artifacts

```
Nemotron 3.5 Lightning post-training evaluation (Thoughtworks, Aug 2026)
Source: thoughtworks.com/insights/blog/generative-ai/putting-nvidia-nemotron-3-5-lightning-test

MODEL
  Architecture:  30B mixture-of-experts, 3B active parameters
  Lineage:       Distilled from NVIDIA Nemotron 3 Ultra

DOMAIN ADAPTATION (low-rank adapters, single node, 8x H100 80GB, "a few hours")
  Legal:
    Blind comparison:  75% win rate (112/163), p < 0.001
    CaseHOLD:          35% -> 77%
    General capability: within 1.5 points of base model
                        (reasoning, mathematics, legal knowledge)
  Healthcare:
    Blind comparison:  60% win rate (82/167), p = 0.002
    Clinical prediction error: -24%
    Answer-token accuracy:     64% -> 69%
  Judge methodology: "an independent AI judge from a different model family"
                      (LLM judge, not human raters; judge model not named)

ANTISLOP BEHAVIORAL TUNING (2x H100 80GB, ~13 hours)
  Overused patterns identified: 4,267
  Training examples generated: ~13,000
  Patterns eliminated:          66.4%
  Vocabulary richness:          98.4% of baseline
  Writing quality:               statistically unchanged (prose-quality metric)

  Downstream benchmark table (original -> antislop):
    MMLU-Pro:      0.703 -> 0.713
    HumanEval+:    0.750 -> 0.707
    IFEval:        0.387 -> 0.387
    tau-bench (customer service): 0.640 -> 0.624

INFERENCE SPEED (H200 / B200 GPUs, 2,091 measurements,
                  3 workloads, concurrency 1-128)
  Built-in native speculative decoder (default enabled):
    Throughput gain:  1.46x-1.96x vs. unaccelerated decoding
    Cost:             $0.477 -> $0.250 per million output tokens
  Custom-trained EAGLE-3 draft head:
    Result: matched but did not exceed built-in decoder throughput

LINKED TECHNICAL REPORTS (not independently fetched in this extraction)
  - research.thoughtworks.com/library/post-training-nvidia-nemotron-3-5-lightning-enterprise-domains
  - research.thoughtworks.com/library/teaching-model-stop-writing-like-model
  - research.thoughtworks.com/library/eagle-3-speculative-decoding-nvidia-nemotron-3-5-lightning
  - antislop framework paper: arxiv.org/pdf/2510.15061 (MIT-licensed)
```

## Cross-References

- **Corroborates**: `blog-thebatch-nemotron-agent-infra.md` Claim 6 (Nemotron
  3 Super's free/permissive commercial-use license terms) — this note's
  subject, Nemotron 3.5 Lightning, is presumably distributed under a similar
  NVIDIA open-weights licensing approach, though this blog post does not
  restate license terms itself; flagged here as a plausible-but-unconfirmed
  extension rather than a verified corroboration.

- **Contradicts**: Filed as contradiction issue
  [#2851](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2851).
  Claim 10 here (a custom-trained EAGLE-3 draft head "matched but did not
  exceed" Nemotron 3.5 Lightning's built-in speculative decoder) is in
  tension with `blog-latentspace-baseten-inference-engineering-masterclass.md`
  Claim 2, in which Baseten's Ali Taha states that traffic-specific
  custom-trained draft models can achieve near-perfect token acceptance and
  states he could "guarantee" high acceptance for a narrow, dedicated
  workload — implying custom draft training should outperform a generic
  decoder. This note's Claim 10 is a direct empirical test of that thesis
  under near-ideal conditions for it (a draft head trained specifically for
  a single narrow, already domain-adapted deployment) and found no edge.
  No verdict is asserted here — see the filed issue for both sides and the
  asymmetry the resolver should weigh (whether the built-in decoder in this
  specific case was already unusually strong because NVIDIA trained it
  jointly with the base model).

- **Extends**: `blog-thebatch-nemotron-agent-infra.md` — that note covers
  Nemotron 3 Super 120B-A12B, a much larger, general-purpose agentic variant
  from the same model family (announced March 2026). This note's Nemotron
  3.5 Lightning (30B-MoE/3B-active, distilled, "Lightning" branding implying
  low-latency/cost focus) sits at the opposite end of the same family's
  size spectrum, and — unlike the Batch note's secondhand vendor-benchmark
  reporting — supplies a first-party, reproducible post-training workflow
  with real hardware/time budgets rather than only inference-serving
  benchmarks.

- **Novel**: 
  - Domain-specific low-rank post-training (legal and healthcare) as a
    reproducible, cheap (single-node, few-hours) workflow with blind
    LLM-judge comparisons and objective benchmark deltas is not present
    elsewhere in this corpus — the closest existing material
    (`blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 8) only
    notes fine-tuning as a *risk* category (an org's own fine-tuning could
    make a model more compliant with dangerous instructions), not as a
    capability-improvement technique with measured results.
  - The "antislop" behavioral-tuning technique (identifying and retraining
    away specific overused stylistic patterns, i.e. "AI writing tells") with
    a quantified before/after pattern-elimination rate is new to this
    corpus. No other note addresses reducing AI writing tells via targeted
    fine-tuning; the closest adjacent corpus material addresses AI writing
    style as a code-quality/"slop" concept in a different sense
    (`blog-ghuntley-engineer-away-slop.md`, about verification bottlenecks
    in code, not stylistic text patterns) and is not a close match.
  - The negative result on custom EAGLE-3 draft-head training (Claim 10) is
    the first data point in this corpus testing whether bespoke speculative
    decoders beat vendor-shipped built-in ones, and is the basis for the
    filed contradiction above.

## Guide Impact

- **Chapter on Model Selection (open-weights domain specialization)**: Add
  this source as concrete evidence that low-rank domain post-training of a
  small (3B-active) open-weights model can produce large, targeted
  capability gains (CaseHOLD 35%->77%) in a single-node, few-hour training
  run, while holding general capability within ~1.5 points. Recommend citing
  Claims 1-4 together (not just the win-rate numbers) since the LLM-judge
  methodology (Claim 1) is a real limitation the guide should surface
  alongside the more objective CaseHOLD result (Claim 2).

- **Chapter on Model Selection / Writing Quality**: Add Claim 5-7 as the
  corpus's first data point on deliberately fine-tuning away "AI writing
  tells." The guide should present the antislop benchmark table (Claim 7)
  alongside the "no quality loss" headline framing (Claims 5-6), since
  HumanEval+ and tau-bench both regressed after antislop tuning — a nuance
  the source's own framing does not foreground.

- **Chapter on Infrastructure Optimization (inference cost / speculative
  decoding)**: Add Claim 9 (1.46x-1.96x throughput, $0.477->$0.250 per
  million output tokens from a default-enabled built-in decoder) as a
  concrete, reproducible inference-cost data point. Add Claim 10 as a
  caution against assuming custom draft-head training is worth the
  engineering investment without first benchmarking the vendor's built-in
  decoder — and flag the open contradiction (#2851) with Baseten's
  traffic-specific-training claim rather than presenting either as settled
  guidance.

## Extraction Notes

- This extraction is based on the Thoughtworks blog post itself, not the
  three linked technical reports it references (research.thoughtworks.com
  post-training, antislop, and EAGLE-3 reports). The blog post supplies
  headline numbers, p-values, and one benchmark table, but does not state
  LoRA rank/alpha, adapter parameter counts, training dataset composition or
  size, or the identity of the LLM judge model used for blind comparisons.
  A deeper extraction of the three linked technical reports would be needed
  to evaluate methodology rigor (e.g., whether CaseHOLD questions overlapped
  with training data) — flagged here rather than assumed.
- Quotes in this note were verified via multiple independent fetches of the
  live source page; the fetch tool declined to reproduce long verbatim
  passages (citing copyright), so all quotes here are short (a few words to
  one short phrase) rather than full sentences. Where no safe verbatim
  fragment was available for a claim (Claim 10), this is marked explicitly
  rather than fabricated, per MINER.md §2a.
- Filed contradiction issue #2851 against
  `blog-latentspace-baseten-inference-engineering-masterclass.md` Claim 2
  (re-read in full and confirmed as Claim 2 in that note before citing) per
  MINER.md §4a/§4b.
- Checked `source-notes/` for other Nemotron and Thoughtworks
  post-training/speculative-decoding notes; found and cross-referenced
  `blog-thebatch-nemotron-agent-infra.md` (same model family, different
  variant/generation) and `blog-latentspace-baseten-inference-engineering-masterclass.md`
  (speculative decoding mechanics, source of the filed contradiction).
  `blog-thoughtworks-gall-kimi-k3-multi-model-era.md` Claim 8 was checked
  and found only tangentially related (fine-tuning as a safety risk, not a
  capability-improvement technique) — not cited as a strong cross-reference.
