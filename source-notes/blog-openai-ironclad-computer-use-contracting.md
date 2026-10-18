---
source_url: https://openai.com/index/advancing-computer-use-with-ironclad
source_type: blog-post
title: "Advancing computer use with Ironclad"
author: OpenAI
date_published: 2026-10-06
date_extracted: 2026-10-18
last_checked: 2026-10-18
status: current
confidence_overall: anecdotal
issue: "#4198"
---

# Advancing computer use with Ironclad

> OpenAI vendor-reported research collaboration: 11 contracting-software tasks scored on 8–50 rubric criteria, used to RL-train GPT-6 Astra, with a +13.4-point rubric gain and ~48% lower simulated time versus GPT-5.6 Sol, plus an open call for partner "failure examples".

## Source Context

- **Type**: blog-post (OpenAI "Publication", co-branded with partner Ironclad)
- **Author credibility**: OpenAI is the model trainer and sole evaluator; the partner (Ironclad) supplies a CTO quote only. All numbers are first-party, from an internal "research evaluation", with no external replication.
- **Scope**: Covers task construction, grading design, training approach (RL on synthetic tasks in hosted software environments), and one headline comparison. Does not give harness details, per-task results, failure-mode taxonomies, variance, or security controls. Its footnotes are the most informative part for evidence quality.
- **Access note**: openai.com returns 403 to direct fetches; text was read from a Wayback Machine snapshot of the same URL.

## Extracted Claims

### Claim 1: Astra scores higher and is faster than GPT-5.6 Sol on the 11 Ironclad research tasks
- **Evidence**: Table: mean rubric score 41.6% (Sol, High reasoning) vs 55.0% (Astra, Max reasoning); estimated average time per attempt 37.0 vs 19.2 minutes. An internal development model reached 63.7%.
- **Confidence**: anecdotal
- **Quote**: "On our research evaluation, its average score was 32% higher than GPT‑5.6 Sol’s, while estimated time per attempt was 48% lower."
- **Our assessment**: The 32% is relative (55.0/41.6 ≈ 1.32); absolute gain is 13.4 points, and 55% still means roughly half of criteria are unmet. Each model is run at its own best reasoning setting (Max vs High), so this is not a same-settings comparison. Sample is 11 tasks, with no confidence intervals.

### Claim 2: The time savings are simulated, not measured
- **Evidence**: Footnote 1 on the headline claim.
- **Confidence**: settled (it is the authors' own caveat)
- **Quote**: "The times are simulated estimates based on assumed model processing and generation speeds, not measured customer time savings."
- **Our assessment**: The "48% lower" is a function of assumed generation speeds and step count, not wall-clock behavior in production. Do not cite it as a latency or productivity result.

### Claim 3: Success means the whole configured process works across situations, not that each step is right
- **Evidence**: Worked example of a software-purchase process with Finance approval above a threshold, Security review, and Legal review of nonstandard terms; the agent must verify both sides of the threshold.
- **Confidence**: emerging
- **Quote**: "Getting individual steps right is not enough: the finished process must work across the situations it was designed to handle."
- **Our assessment**: Useful framing for evaluating agents on configuration-style work: grade the resulting artifact's behavior (branch coverage), not the click trace. This matches a verify-against-original-requirements stance, but no test method is described.

### Claim 4: Tasks were built with domain experts and graded by per-task rubrics of 8–50 criteria
- **Evidence**: 11 tasks across legal, commercial and procurement (NDAs, procurement approvals, a jurisdiction-dependent reusable clause); ~30–40 minutes for an experienced user.
- **Confidence**: emerging
- **Quote**: "We evaluated each task against 8 to 50 criteria, depending on its complexity."
- **Our assessment**: Granular rubrics give partial-credit signal ("which parts a model got right") and are a concrete eval-design pattern. Rubric content and grader (human vs model) are not disclosed.

### Claim 5: Training used hosted partner environments plus synthetic tasks and reinforcement learning
- **Evidence**: Ironclad provided hosted product environments; researchers built synthetic tasks from public SEC EDGAR contracts with PII-removal filters; no customer or internal data used (footnote 2).
- **Confidence**: anecdotal
- **Quote**: "Ironclad also provided hosted software environments of their product where the models could practice these tasks."
- **Our assessment**: The pattern is sandboxed replica environments + synthetic data for agent training. Relevant to evaluation/sandbox design, but the training recipe itself is not reproducible from this post.

### Claim 6: Agents losing track of one business rule mid-task limits what can be delegated; human oversight and the platform remain essential
- **Evidence**: Ironclad framing, no data.
- **Confidence**: anecdotal
- **Quote**: "If an agent loses track of one of those rules halfway through a task, that limits what a software company can confidently ask it to do."
- **Our assessment**: Consistent with the 55% score but stated as opinion. Partner has a commercial interest in "a full contracting platform remains essential".

### Claim 7: OpenAI is soliciting concrete failure cases from partners as the starting point for training
- **Evidence**: Call for applications describing requirements for a partner submission.
- **Confidence**: emerging
- **Quote**: "If your team has one, we’d like to see a concrete example: what you’re asking the agent to do, evidence of where it fails, and how you would judge a successful result."
- **Our assessment**: A lab-side statement of the failure → graded task → RL loop. Notably, it says today's agents "still can’t reliably complete" important professional tasks, an admission of limits in the same post that touts gains.

## Concrete Artifacts

```
Source: OpenAI, "Advancing computer use with Ironclad", 2026-10-06 (results table)
Metric                              GPT-5.6 Sol (High)   GPT-6 Astra (Max)
Mean rubric score                   41.6%                55.0%
Estimated avg time per attempt      37.0 minutes         19.2 minutes
Internal development model (Astra precursor): 63.7%
Clip example (single task): Astra ~94% of criteria in ~20 min; Sol ~85% in ~32 min.
Setup: 11 tasks, 8–50 criteria each, ~30–40 min for an experienced human per task.
```

Partner-submission requirements (paraphrased from "Work with us" section): concrete example, evidence of failure, success criteria, domain experts, secure test environment, data safe for research use.

## Cross-References

- **Corroborates**: `blog-latentspace-openai-devday-cua-and-api-interview` also presents first-party, unverified OpenAI computer-use claims; both reflect OpenAI's push on professional-work computer use.
- **Contradicts**: None found.
- **Extends**: `blog-anthropic-computer-use-best-practices` and `blog-anthropic-dispatch-computer-use` cover computer-use guidance and product framing from the other lab; this adds a rubric-graded, enterprise-software eval example. `blog-anthropic-claude-legal-industry` covers legal-vertical agents via MCP connectors, whereas this one is GUI/computer-use in a contracting SaaS.
- **Novel**: Contracting/CLM configuration as a computer-use benchmark; vendor environments + EDGAR-derived synthetic tasks + RL; explicit disclosure that time savings are simulated.

## Guide Impact

- **Chapter 02**: At most a cautionary citation for agent evaluation: rubric-graded artifact behavior (8–50 criteria per task) beats step-level scoring, and "time per attempt" figures must be labeled simulated vs measured. Do not use the 32%/48% numbers as general evidence.
- **Chapter 06**: No security content in the source. Any threat-model use would be inference only (agents configuring approval rules is a privileged action); do not attribute it to OpenAI.

## Extraction Notes

- Read in full via Wayback snapshot (direct fetch blocked). The embedded clips and any images were not viewable; the Astra/Sol 94%/85% clip numbers come from captions.
- Model names (GPT-6 Astra, GPT-5.6 Sol) are as given in the source.
- Thin on method; confidence is `anecdotal` because all evidence is vendor-reported on 11 tasks.
- The Prospector's concern about marketing is partly valid; retained because of concrete eval design and explicit caveats.
