---
source_url: https://simonwillison.net/2026/Apr/30/gpt-55-cyber-capabilities/
source_type: blog-post
title: "Our evaluation of OpenAI's GPT-5.5 cyber capabilities"
author: Simon Willison (link-blog to UK AI Security Institute evaluation)
date_published: 2026-04-30
date_extracted: 2026-05-11
last_checked: 2026-05-11
status: current
confidence_overall: emerging
issue: "#599"
---

# Our evaluation of OpenAI's GPT-5.5 cyber capabilities

> Simon Willison's link-blog post pointing to the UK AI Security Institute's independent
> evaluation of GPT-5.5 cyber capabilities: the key finding is that GPT-5.5 is comparable
> to Claude Mythos Preview on expert CTF tasks and the TLO corporate network attack
> simulation — but, critically, GPT-5.5 is generally available via the public API today,
> making frontier-level AI offensive cyber capability accessible to all developers and
> threat actors without research-access gating.

## Source Context

- **Type**: blog-post (Simon Willison link-blog, April 30 2026, ~70 words; links to the UK
  AI Security Institute blog post "Our evaluation of OpenAI's GPT-5.5 cyber capabilities"
  at aisi.gov.uk. The AISI blog post is the primary empirical anchor; Willison's post
  provides the corpus entry point and the key editorial observation about general
  availability. Both sources were fetched and are the basis for extraction.)
- **Author credibility**: Simon Willison is the creator of Django and a trusted-feed
  commentator on LLM tooling (designated `trusted-feed` in this repo). His editorial
  observation — that GPT-5.5 is "generally available right now" unlike Mythos — is a
  practitioner-level synthesis, not original research. The UK AI Security Institute (AISI)
  is an independent UK government body established specifically to evaluate advanced AI
  capabilities; this is their second evaluation in the AI cyber capability series, following
  the Claude Mythos Preview evaluation covered in `blog-simonwillison-cybersecurity-proof-of-work.md`.
  AISI evaluations are third-party, independent, and explicitly comparable across model
  generations because they use the same benchmark suite.
- **Scope**: Covers AISI's quantitative cyber capability evaluation of GPT-5.5 across
  expert-level CTF tasks and two cyber range simulations (TLO corporate network and Cooling
  Tower ICS). Also covers a jailbreak finding and safeguard update. Does NOT cover:
  the economic/proof-of-work framing (see `blog-simonwillison-cybersecurity-proof-of-work.md`),
  defensive program recommendations (see `blog-anthropic-ai-accelerated-offense.md`), or
  agent fleet deployment patterns (see `blog-cursor-security-agents.md`). The evaluation
  is conducted in controlled settings without active defenders or defensive tooling —
  all quantitative capability numbers should be treated as upper-bound estimates for
  weakly-defended targets.

## Extracted Claims

### Claim 1: GPT-5.5 is comparable to Claude Mythos Preview on AISI cyber benchmarks and is generally available today, unlike Mythos

- **Evidence**: Willison's editorial synthesis of the AISI evaluation. AISI data: GPT-5.5
  71.4% ±8.0% vs Mythos 68.6% ±8.7% on Expert-level tasks (overlapping confidence
  intervals — not statistically distinguishable). GPT-5.5 completed TLO in 2/10 attempts
  vs Mythos's 3/10. Mythos was available only as a preview model at time of the April 2026
  evaluations; GPT-5.5 is available on the standard OpenAI API.
- **Confidence**: emerging (third-party AISI evaluation; the general-availability claim is
  a factual observation by Willison, directly verifiable; the capability comparison carries
  the AISI's methodology caveats about controlled, undefended environments)
- **Quote**: "The UK's AI Security Institute previously evaluated Claude Mythos: now they've
  evaluated GPT-5.5 for finding security vulnerability and found it to be comparable to
  Mythos, but unlike Mythos it's generally available right now."
- **Our assessment**: This is the single most important editorial claim in the source. The
  AISI Mythos evaluation established a new capability frontier for AI cyber offense; this
  source establishes that the same capability level is now accessible to anyone with an
  OpenAI API key. For AI-native engineering teams: the threat model has changed. The
  Mythos evaluation indicated a research-access threat; this evaluation confirms the threat
  is now generally deployed. Teams that deferred security review on the grounds that Mythos
  was not publicly accessible can no longer use that deferral.

### Claim 2: GPT-5.5 achieves 71.4% (±8.0%) on Expert-level cyber tasks — the highest score AISI has recorded on this benchmark tier

- **Evidence**: AISI's benchmark suite of 95 narrow cyber tasks across four difficulty
  tiers. Expert-level tier: 21 tasks covering reverse engineering, web exploitation,
  cryptography, and exploitation against realistic targets with modern mitigations. The
  comparison scores: Mythos Preview 68.6% ±8.7%, GPT-5.4 52.4% ±9.8%, Opus 4.7
  48.6% ±10.0%. The AISI states this makes GPT-5.5 "one of the strongest models we have
  tested on our cyber tasks."
- **Confidence**: emerging (third-party independent evaluation; confidence intervals are
  reported; methodology is consistent with the prior Mythos evaluation, enabling
  cross-model comparison)
- **Quote**: "GPT-5.5 achieved an average pass rate of 71.4% (±8.0%) on Expert-level tasks"
- **Our assessment**: The 71.4% figure alone matters less than the comparison context:
  GPT-5.5 vs Mythos scores are statistically indistinguishable (overlapping CIs), while
  both are approximately 20 percentage points ahead of GPT-5.4 and Opus 4.7. This
  establishes a two-tier capability structure at the April 2026 frontier: a top tier
  (Mythos, GPT-5.5 at ~70%) and a second tier (GPT-5.4, Opus 4.7 at ~50%). For model
  selection in security contexts: both top-tier models are roughly equivalent on these
  benchmarks, but GPT-5.5 is publicly available while Mythos was not.

### Claim 3: GPT-5.5 is the second model ever to complete AISI's "The Last Ones" corporate network attack simulation, doing so in 2 of 10 attempts

- **Evidence**: AISI's "The Last Ones" (TLO) evaluation — a 32-step corporate network attack
  simulation built with SpecterOps, spanning four subnets with ~20 hosts. The agent must
  chain reconnaissance, credential theft, lateral movement across Active Directory forests,
  CI/CD supply-chain pivoting, and database exfiltration. Human expert estimated completion:
  ~20 hours. Token budget: 100M tokens per attempt. GPT-5.5: 2/10 end-to-end completions.
  Mythos Preview: 3/10 (was the first model to solve it). All other previously tested models:
  0/10.
- **Confidence**: emerging (AISI independent evaluation; same methodology as prior TLO
  testing; 10-attempt sample is the standard run count per AISI methodology)
- **Quote**: "the second model to solve one of our multi-step cyber-attack simulations
  end-to-end"
- **Our assessment**: GPT-5.5's 2/10 completion rate is slightly below Mythos's 3/10, but
  both are astronomically above the 0/10 baseline of all other tested models. The gap
  between "top-tier" models (Mythos, GPT-5.5) and "second-tier" (everything else) is
  binary on this benchmark: either you can complete TLO end-to-end or you cannot.
  Corroborates `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 2 on Mythos's
  3/10 TLO result. For AI-native engineering: TLO completion is the current empirical
  threshold for "autonomous AI can execute a complete multi-step corporate network
  attack." Two models have now crossed it, and one is publicly available.

### Claim 4: TLO performance continues to scale with the amount of inference compute spent

- **Evidence**: AISI's observation within the GPT-5.5 evaluation. This replicates the
  prior finding from the Mythos evaluation at the same 100M-token budget.
- **Confidence**: emerging (AISI direct observation; repeated across two separate model
  evaluations at the same token budget — strengthens the prior Mythos-era finding)
- **Quote**: "Performance on TLO continues to scale with the amount of inference compute
  spent"
- **Our assessment**: This corroborates `blog-simonwillison-cybersecurity-proof-of-work.md`
  Claim 4's observation that no saturation was detected at 100M tokens per attempt during
  the Mythos evaluation. The replication across two different top-tier models (Mythos, then
  GPT-5.5) under the same methodology strengthens the inference that the token-scaling
  relationship is a property of the task difficulty, not a quirk of one model. The economic
  implication — defenders must spend more tokens than attackers — now has support from
  two independent model evaluations.

### Claim 5: GPT-5.5 solved the rust_vm reverse-engineering CTF challenge in 10 minutes 22 seconds at $1.73 cost; a human expert required approximately 12 hours

- **Evidence**: AISI's demonstration of GPT-5.5 on a complex reverse-engineering task
  (rust_vm challenge). The task required reverse-engineering a stripped binary without
  source code. Human expert baseline: ~12 hours using Binary Ninja, gdb, Python, and Z3.
  GPT-5.5 result: 10 minutes 22 seconds with no human assistance, $1.73 USD API cost.
- **Confidence**: emerging (single AISI-reported case; specific time and cost are precise
  and independently verifiable in principle; the human baseline is AISI's expert estimate
  rather than a controlled trial)
- **Quote**: "GPT-5.5 solved the challenge in 10 minutes and 22 seconds with no human
  assistance"
- **Our assessment**: The speed ratio (~70×) and cost ($1.73 vs. hours of expert labor)
  are the concrete expressions of what AI-accelerated cyber offense means in practice. This
  is not about "AI can do some security tasks" — it is about an economically negligible API
  call replacing hours of senior expert work. For teams performing red-team exercises or
  CTF-style security audits: the cost threshold for a targeted AI-assisted reverse-engineering
  attempt has dropped to under $2. The $1.73 figure pairs with the $12,500 per full TLO run
  (from `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 5) to bracket the cost
  range from single-task ($1.73) to full multi-step attack simulation ($12,500+).

### Claim 6: AISI expert red-teamers found a universal jailbreak effective across all malicious cyber queries in approximately 6 hours; OpenAI made safeguard updates but verification was blocked by a configuration issue

- **Evidence**: AISI's safety evaluation process. Red-teaming found a jailbreak effective
  across "all malicious cyber queries provided by OpenAI, including multi-turn agentic
  contexts." Development time: ~6 hours of expert red-teaming. OpenAI subsequently made
  safeguard stack updates. A configuration issue prevented AISI from verifying the
  effectiveness of the final updated version.
- **Confidence**: anecdotal (AISI-reported safety finding; the specifics of the jailbreak
  are not publicly disclosed; the "configuration issue" preventing verification introduces
  uncertainty about the final safety state)
- **Quote**: "we identified a universal jailbreak that elicited violative content across
  all malicious cyber queries"
- **Our assessment**: This is the most consequential safety finding in the evaluation for
  AI-native engineers. A universal jailbreak across all cyber-malicious queries means the
  safety controls on GPT-5.5's cyber capabilities were breakable by an expert in a working
  day. The resolution is incomplete — AISI could not verify the fix. For harness designers:
  this reinforces that API-level safety controls for powerful models are not a sufficient
  substitute for architecture-level constraints (prompt injection defense, output sandboxing,
  task scope restriction). The AISI finding is that even the vendor's own safeguard stack
  was bypassed; harnesses that rely on the model refusing malicious requests cannot assume
  robustness. This extends the harness-level safety guidance from
  `blog-cursor-security-agents.md` (verified outputs, shadow mode gradual trust rollout).

### Claim 7: GPT-5.5 cannot solve the "Cooling Tower" industrial control system simulation — no model has yet succeeded on this range

- **Evidence**: AISI's Cooling Tower evaluation — a 7-step industrial control system attack
  simulation. GPT-5.5 was unable to solve it. No prior tested model has succeeded. The
  Basic task suite (lower difficulty) has been fully saturated since February 2026.
- **Confidence**: emerging (AISI observation; ICS-specific task failure is consistent with
  the general pattern that GPT-5.5 may excel on corporate network attack while ICS/OT attack
  requires different domain knowledge)
- **Quote**: (no direct AISI quote on Cooling Tower; the finding is: GPT-5.5 unable to
  solve; no model has succeeded yet)
- **Our assessment**: The Cooling Tower failure is a meaningful capability boundary: current
  frontier models can complete sophisticated corporate IT network attacks autonomously but
  cannot complete ICS/OT attack chains. For AI-native engineering teams in industrial
  sectors: ICS-specific systems have a different risk profile from corporate IT at this
  capability level. The basic-tier saturation (fully solved since Feb 2026) paired with
  Cooling Tower failure shows the difficulty gradient is steep, not smooth.

### Claim 8: Rapid improvement on cyber tasks may be part of a more general trend in frontier model capability

- **Evidence**: AISI's closing observation across multiple evaluations: the Basic suite was
  fully saturated (100% pass rate) by February 2026; Expert-level scores have jumped from
  ~0% (pre-April 2025, per Mythos evaluation data) to ~70% within a year. The pace from the
  Mythos evaluation to GPT-5.5 (approximately two weeks between publication dates, likely
  months of evaluation work) shows rapid succession.
- **Confidence**: anecdotal (AISI editorial inference; not a controlled study of capability
  growth rate)
- **Quote**: "rapid improvement on cyber tasks may be part of a more general trend"
- **Our assessment**: This is AISI's own interpretation of the trajectory. Corroborates
  `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 3's framing (0% → 73% on
  expert CTF within one year) and `blog-anthropic-ai-accelerated-offense.md`'s 24-month
  countdown claim. The "more general trend" language is AISI hedging — they are observing
  rapid capability improvement but not formally attributing it to a specific mechanism.
  For the guide: the trend language from an independent government evaluator carries more
  weight than vendor claims of the same observation.

## Concrete Artifacts

### Simon Willison's Post (Full Text)

```
"Our evaluation of OpenAI's GPT-5.5 cyber capabilities"
Simon Willison's Weblog — April 30, 2026

"The UK's AI Security Institute previously evaluated Claude Mythos: now they've
evaluated GPT-5.5 for finding security vulnerability and found it to be comparable
to Mythos, but unlike Mythos it's generally available right now."

Tags: ai, openai, generative-ai, llms, anthropic, claude, ai-security-research, gpt
```

### AISI Expert-Level CTF Benchmark: GPT-5.5 vs Frontier Models

```
AISI Expert-Level Advanced Task Performance (April 2026)
Source: UK AI Security Institute — "Our evaluation of OpenAI's GPT-5.5 cyber capabilities"
95 narrow cyber tasks across 4 tiers; 21 Expert-level tasks evaluated here

Model                    | Expert-level pass rate | 95% CI (±1 SE)
-------------------------|------------------------|----------------
GPT-5.5                  | 71.4%                  | ±8.0%
Claude Mythos Preview    | 68.6%                  | ±8.7%
GPT-5.4                  | 52.4%                  | ±9.8%
Claude Opus 4.7          | 48.6%                  | ±10.0%

Notes:
  - GPT-5.5 and Mythos confidence intervals overlap substantially — not statistically
    distinguishable as different capability levels
  - GPT-5.4 and Opus 4.7 form a lower tier ~20 percentage points below
  - Basic suite fully saturated since February 2026
  - AISI: "GPT-5.5 is one of the strongest models we have tested on our cyber tasks"
  - Token budget: 50M tokens for Advanced task evaluation
```

### AISI "The Last Ones" (TLO) Cyber Range: Updated Results

```
AISI TLO Evaluation — 32-step corporate network attack simulation (SpecterOps)
Source: UK AI Security Institute

Simulation: 4 subnets, ~20 hosts
Steps: reconnaissance → credential theft → lateral movement (AD forests) →
       CI/CD supply-chain pivot → database exfiltration
Human expert baseline: ~20 hours
Token budget: 100M tokens per attempt

Results (end-to-end completion rate, 10 attempts each):

Model                    | TLO Completion
-------------------------|----------------
Claude Mythos Preview    | 3/10 (first to solve)
GPT-5.5                  | 2/10 (second to solve)
All other tested models  | 0/10

Key finding: "Performance on TLO continues to scale with the amount of inference
compute spent" — no saturation observed at 100M-token budget

Caveat: "We cannot say from these results whether GPT-5.5 would succeed against a
well-defended target." Ranges "lack the active defenders, defensive tooling, and
alert penalties that real-world environments typically have."
```

### rust_vm CTF Challenge: GPT-5.5 vs Human Expert

```
rust_vm Reverse Engineering CTF Challenge
Source: UK AI Security Institute demonstration case

Task: Reverse-engineer a stripped binary without source code

Human expert: ~12 hours using Binary Ninja, gdb, Python, and Z3
GPT-5.5:       10 minutes 22 seconds, no human assistance, $1.73 USD API cost

Speed ratio: ~70× faster
Cost: sub-$2 per attempt vs. hours of senior expert labor
```

### AISI Jailbreak Finding Summary

```
AISI Safety Finding: Universal Jailbreak
Source: UK AI Security Institute GPT-5.5 evaluation

Finding: "we identified a universal jailbreak that elicited violative content
          across all malicious cyber queries"
Scope:   All malicious cyber queries provided by OpenAI; multi-turn agentic
          contexts included
Dev time: ~6 hours of expert red-teaming

Response: OpenAI made safeguard stack updates
Outcome:  A configuration issue prevented UK AISI from verifying the final
          version's effectiveness — resolution inconclusive at time of publication
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 2: The Mythos TLO result
    (3/10 completions) reported in the Breunig/Willison April 14 post is confirmed
    in this AISI evaluation: "Mythos Preview was the first model to solve TLO, doing
    so in 3 of 10 attempts." The new source adds GPT-5.5 as the second model at 2/10.
  - `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 4: The April 14 source
    found "no saturation observed at 100M token budget" for Mythos TLO performance. The
    new source replicates this observation for GPT-5.5 ("Performance on TLO continues to
    scale with the amount of inference compute spent") — two independent evaluations of
    different models confirming the same scaling behavior.
  - `blog-anthropic-ai-accelerated-offense.md`: Anthropic's 24-month countdown claim and
    AISI's "rapid improvement on cyber tasks may be part of a more general trend" (Claim 8
    here) are independent corroborations of the same capability-trajectory observation.
    The AISI observation carries independent weight because it comes from a government body,
    not the model vendor.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 11: That note's VulnLMP
    evaluation places GPT-5.5 in the "high" cybersecurity threat tier (OpenAI's own
    self-evaluation). The AISI third-party evaluation here corroborates the general
    capability tier claim — GPT-5.5 is at frontier cyber capability — with independent
    methodology and quantitative CTF/cyber-range data.

- **Contradicts**: No material contradictions filed. The Expert-level CTF percentage for
  Mythos (68.6% ±8.7% in this source vs. 73% in `blog-simonwillison-cybersecurity-proof-of-work.md`
  Claim 3) differs numerically. However: (1) the values are within statistical error of
  each other (68.6% ± 8.7% spans 59.9% to 77.3%, which includes 73%); (2) the two figures
  may reflect slightly different benchmark calibrations between the April 14 (Mythos
  evaluation) and April 30 (GPT-5.5 evaluation) AISI publications; (3) both figures
  support the same guide-relevant claim (Mythos is at frontier expert CTF level). This is
  measurement variance, not a guide-advice-changing contradiction.

- **Extends**:
  - `blog-simonwillison-cybersecurity-proof-of-work.md`: That source introduced the
    Claude Mythos AISI evaluation data, establishing the proof-of-work economic framing and
    the Mythos capability baseline. This source extends it with: (a) a direct GPT-5.5
    comparison on the same benchmarks, (b) the critical general-availability distinction
    (Mythos was preview-only; GPT-5.5 is public API), (c) the Cooling Tower capability
    boundary (ICS simulation unsolvable by current models), and (d) the universal jailbreak
    safety finding.
  - `blog-cursor-security-agents.md`: The Cursor security agent fleet is architecturally
    relevant here. This AISI source provides the empirical capability context that justifies
    the Cursor investment: the fleet was built to defend against exactly the kind of
    adversarial capability (70%+ expert CTF, TLO-completing agents) that AISI now confirms
    is publicly available.

- **Novel**:
  - **General availability of frontier AI cyber capability**: The first in-corpus source
    to explicitly state that frontier-level AI offensive cyber capability (comparable to
    Claude Mythos) is now available on a public commercial API. All prior corpus sources
    framing the cyber threat (Mythos, Project Glasswing) involved preview or research-access
    models. This source closes that gap.
  - **Cross-model AISI Expert-level CTF comparison table**: The four-model comparison
    (GPT-5.5, Mythos, GPT-5.4, Opus 4.7) with reported confidence intervals on the same
    benchmark is the first in-corpus dataset enabling like-for-like quantitative comparison
    of frontier AI cyber capability across vendors and model generations.
  - **Universal jailbreak finding at 6-hour expert effort**: The first in-corpus AISI
    report documenting a successful jailbreak of a frontier model's cyber safety controls,
    with a quantified development time (6 hours). The inconclusive verification of the fix
    adds a safety caveat not present in prior notes.
  - **rust_vm speed comparison** ($1.73 / 10 min 22 sec vs. 12-hour human): The first
    in-corpus concrete time/cost comparison for AI vs. human on a specific real-world
    security task, establishing that the economic barrier to an AI-assisted targeted attack
    on a stripped binary is under $2.
  - **Cooling Tower ICS capability boundary**: The first explicit statement in the corpus
    that a specific class of cyber range (ICS/OT simulation) is unsolvable by current
    frontier models, while corporate-IT simulation is not. Establishes a capability
    boundary relevant to industrial sector risk assessments.

## Guide Impact

- **Chapter 03 or Chapter 04 (Safety and Security — Threat Landscape)**: The general
  availability finding (Claim 1) should trigger an update to any section that frames the
  AI cyber threat as primarily a research/preview-model problem. Specific update: "As of
  May 2026, frontier-level AI offensive cyber capability is publicly available via commercial
  API (GPT-5.5). AISI's independent evaluation places GPT-5.5 on par with Claude Mythos
  Preview — the model that was the first to complete a 32-step corporate network attack
  simulation autonomously. Teams that deferred security review because capable models were
  research-access-only should revisit that deferral." Cite: AISI evaluation (this source)
  and `blog-simonwillison-cybersecurity-proof-of-work.md` for the economic framing.

- **Chapter 03 (Safety and Verification — Model Safety Controls)**: The jailbreak finding
  (Claim 6) should inform a note about the limits of relying on model-level safety controls
  in security-sensitive deployments: "AISI's evaluation of GPT-5.5 found a universal
  jailbreak effective across all malicious cyber queries, developed in approximately 6 hours
  of expert effort. Harnesses handling security-sensitive tasks should not rely on model
  refusals as a primary safety control. Architecture-level constraints — output sandboxing,
  task scope restriction, human-in-the-loop gates — are required." This complements
  `blog-cursor-security-agents.md`'s graduated trust rollout (shadow mode before blocking)
  and `blog-anthropic-ai-accelerated-offense.md`'s recommendations.

- **Chapter 02 (Harness Engineering — Model Selection for Security Tasks)**: The four-model
  CTF comparison table (Claim 2) and the TLO results (Claim 3) provide the most current
  quantitative basis for model selection when deploying AI for security scanning or red-team
  work. Recommend adding: the two-tier capability structure (top: GPT-5.5/Mythos at ~70%;
  second tier: GPT-5.4/Opus 4.7 at ~50%); the note that top-tier scores are not
  statistically distinguishable; and the practical note that GPT-5.5 is generally available
  while Mythos remained a preview model.

- **Chapter 03 (Safety and Security — Cost of Attack)**: The rust_vm $1.73 / 10-minute
  finding (Claim 5) pairs with `blog-simonwillison-cybersecurity-proof-of-work.md` Claim 5
  ($12,500 per TLO campaign attempt) to give practitioners a cost range: single targeted
  reverse-engineering task ($1.73) to full multi-step corporate network attack simulation
  ($12,500). The guide should note both cost anchors so teams can calibrate threat budgets
  proportional to asset sensitivity.

## Extraction Notes

1. **Source structure**: The Willison post is ~70 words — a pure link post. The AISI blog
   post at aisi.gov.uk is the substantive source and was fetched directly. All quantitative
   claims originate from the AISI blog; Claim 1 and the general-availability framing are
   from Willison.

2. **AISI evaluation environment caveat**: All quantitative results apply to controlled
   research environments without active defenders, defensive tooling, or alert penalties.
   The AISI explicitly states: "We cannot say from these results whether GPT-5.5 would
   succeed against a well-defended target." All capability numbers should be treated as
   upper bounds for weakly-defended targets.

3. **Measurement variance in Mythos CTF numbers**: The Mythos Preview Expert-level score
   is reported as 68.6% ±8.7% in this source (AISI GPT-5.5 evaluation) vs. approximately
   73% in `blog-simonwillison-cybersecurity-proof-of-work.md` (AISI Mythos evaluation).
   These values are within statistical error; the discrepancy likely reflects benchmark
   recalibration between the two AISI evaluation publications. No contradiction filed.

4. **Jailbreak fix verification blocked**: AISI reports that "a configuration issue
   prevented UK AISI from verifying the final version's effectiveness" of OpenAI's safeguard
   updates. The current state of GPT-5.5's cyber safety controls — as of the April 30
   evaluation — is unverified by AISI. This is a live safety open item at time of
   publication.

5. **No sub-pages followed beyond the AISI blog post itself**: The Willison post links only
   to the AISI evaluation page. No related sub-pages were fetched.
