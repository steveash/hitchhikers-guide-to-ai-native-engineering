---
source_url: https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md
source_type: blog-post
title: "How our agents build on-brand pages with design.md"
author: John Phamous (Design Engineer, Vercel)
date_published: 2026-08-31
date_extracted: 2026-09-29
last_checked: 2026-09-29
status: current
confidence_overall: emerging
issue: "#3788"
---

# How our agents build on-brand pages with design.md

> Vercel describes a three-part system (a public design.md, a documented stylesheet, and a scenario-based eval loop) for getting agents outside the codebase to produce on-brand pages, with a small measured result (39 vs 91 known failures) and candid caveats.

## Source Context

- **Type**: blog-post (official Vercel Blog, 12 min read, contributor credit to Kevin Corbett)
- **Author credibility**: Vercel design engineer describing an internal system used daily; first-party, no independent replication. The quantitative result is explicitly self-limited by the author.
- **Scope**: Covers why a naive prompt port of an in-repo skill failed, the design.md/stylesheet/eval-loop architecture, the review harness, a 6-page measurement, weekly feedback maintenance, and a six-step "build your own" recipe. It does not publish the design.md contents beyond excerpts shown as images, and does not give per-model breakdowns.

## Extracted Claims

### Claim 1: Naively porting an in-repo skill into one public prompt failed because models interpret prose design language differently and the prompt lacks the surrounding real components and examples
- **Evidence**: Vercel's own first attempt: collapsed the product-design skill's reference files into one URL-readable file.
- **Confidence**: anecdotal
- **Quote**: "every model reading it interpreted that description differently, generating vastly different pages from the same guidance."
- **Our assessment**: A concrete failure report inside a positive-pattern post. Supports the view that context around a skill (real components, shipped examples) is part of the skill's value and does not survive a flat text export. Single-vendor, unquantified.

### Claim 2: Subjective design vocabulary ("clean") is underspecified; the bigger gap is the missing in-repo examples
- **Evidence**: Author's diagnosis of the failed port.
- **Confidence**: anecdotal
- **Quote**: "Phrases like \"keep the layout clean\" can really mean anything. What is \"clean\"?"
- **Our assessment**: Matches the widely reported pattern that adjectives underconstrain output. The "Build your own" section operationalizes it: rewrite corrections as observable, checkable statements.

### Claim 3: The system needs three layers: guidance (design.md), a bounded public stylesheet, and an evaluation loop
- **Evidence**: Architecture description; the stylesheet packages headers, tables, stat strips and chart styles, and design.md documents its class names and tokens.
- **Confidence**: emerging
- **Quote**: "A public stylesheet that defines a bounded, documented vocabulary of classes and tokens."
- **Our assessment**: The division of labor (judgment in prose, mechanics in CSS, checks in code) is the reusable pattern. Note the stylesheet is not read by the agent, so the code never enters context.

### Claim 4: Taking layout/typography decisions away from the model via a stylesheet also saves context
- **Evidence**: Design rationale; stylesheet loads at render time in the browser.
- **Confidence**: anecdotal
- **Quote**: "the agent never actually reads the stylesheet itself."
- **Our assessment**: Neat context-engineering trick: reference a capability by documented names rather than loading its implementation. Analogous to tool descriptions vs. implementations.

### Claim 5: Naming recurring bad generated-design patterns helps agents avoid them
- **Evidence**: design.md includes an anti-pattern section (shown as an image excerpt).
- **Confidence**: anecdotal
- **Quote**: "allowing agents to recognize and avoid them far more reliably by giving the patterns names."
- **Our assessment**: The "far more reliably" is asserted, not measured. Plausible and consistent with Gotchas-style guidance.

### Claim 6: Guidance changed page structure and hierarchy, not just styling, in a single matched comparison
- **Evidence**: Renewal-proposal eval run once without and once with design.md; same model, prompt, data, viewport; no rerolls. Without: generic SaaS dashboard. With: led with the recommendation.
- **Confidence**: anecdotal (n=1 pair)
- **Quote**: "Without design.md, the model generated a generic SaaS dashboard."
- **Our assessment**: Illustrative, not statistical. The author frames it only as enough signal to keep building.

### Claim 7: Every rule earned its place through fixed scenarios, rounds, and re-runs, because a fix for one artifact can hurt another
- **Evidence**: Seven frozen scenarios (usage report, renewal proposal, benchmark report, planning page, build-vs-buy brief, security governance brief, deck); rounds run on Claude Opus 4.8 and Codex with GPT-5.5; over 200 runs total.
- **Confidence**: emerging
- **Quote**: "a change that helped one artifact could quietly hurt another."
- **Our assessment**: A regression-suite discipline applied to prompt/guidance files. The 200+ run count is the cost signal worth noting.

### Claim 8: Route each correction to the narrowest place that can enforce it
- **Evidence**: Table-width example: the correction went into both a design.md rule and a deterministic layout check.
- **Confidence**: emerging
- **Quote**: "Each correction a reviewer records gets landed in the narrowest place that can consistently enforce it."
- **Our assessment**: A crisp decision rule: prose for judgment, CSS for reusable mechanics, code for mechanically checkable failures. Also "when a single model fails in a way the others don't, we keep it out of the rules until it repeats" avoids overfitting guidance to one model.

### Claim 9: Deterministic checks catch mechanical failures; humans judge hierarchy, composition, and reader fit
- **Evidence**: Eval-loop design; a model judge also wrote critiques each round; blind A/B rounds at milestones to keep, revise, or revert changes.
- **Confidence**: emerging
- **Quote**: "people judge the subjective parts that can't be automated"
- **Our assessment**: Hybrid human + deterministic + LLM-critique grading; the model judge is used for feedback, not as the final arbiter.

### Claim 10: With design.md, first-attempt pages had 39 known failures vs 91 without (57% fewer), with strong caveats
- **Evidence**: 3 desktop scenarios x 2 conditions, Codex with GPT-5.5, first attempt only, deterministic checks counted.
- **Confidence**: anecdotal (six pages; author says so)
- **Quote**: "The pages generated with design.md had 39 of those failures. The pages generated without it had 91, which works out to 57% fewer in this test."
- **Our assessment**: Honest but weak evidence. Author notes checks only catch already-seen failures, the sample is tiny, and every page still had a ship-blocking failure. Do not cite as an effect size; cite as "encoded failures tend to stay gone."

### Claim 11: Production usage feedback, aggregated weekly, keeps the guidance current and seeds new eval scenarios
- **Evidence**: @design-agent (built on eve) in Slack; feedback from Slack, GitHub reviews and Figma is grouped by automation into proposed changes, reviewed by a person; complaint frequency tracked over time.
- **Confidence**: emerging
- **Quote**: "if people start asking for a kind of page we have never tested, that request becomes a new eval scenario."
- **Our assessment**: A closed feedback loop with a human in the merge path. The metric (complaint recurrence should fall after a fix) doubles as a diagnostic for a bad rule, unloaded rule, missing primitive, or need for a check.

### Claim 12: Start small: one artifact, a saved baseline, observable corrections, one blind matched comparison
- **Evidence**: Six-step recipe; suggests multiple independent first-attempt trials for reliability, holdouts, version recording, and human-reviewed final changes.
- **Confidence**: emerging
- **Quote**: "You cannot tell whether new context helped without a before."
- **Our assessment**: A practical, low-cost onboarding path for guidance evals that fits teams without an eval runner.

## Concrete Artifacts

Scenario list (source, "We wrote seven of them"):

```
Usage and performance report
Renewal proposal
Benchmark report
Interactive planning page
Build-versus-buy brief
Security governance brief
Presentation deck
```

Correction-routing rule (paraphrased from source section "Turning corrections into rules and checks", not a quote):

```
judgment change      -> prose in design.md
reusable mechanic    -> stylesheet primitive
mechanically checkable -> deterministic check in code
harness problem      -> stays in harness
single-model failure -> hold out of rules until it repeats
```

Metric (source, "Measuring whether it worked"): 39 failures with design.md vs 91 without across six first-attempt pages; "well over 200 runs" to build the file.

Rewrite example from source: "Let evidence tables use the full available width" instead of "Make the table feel less cramped".

## Cross-References

- **Corroborates**: `blog-anthropic-claude-design-product-designer-workflow.md` Claim 11 (unguided Claude regresses to "favorite aesthetics"; explicit style guidance is needed) and Claim 2 (feeding brand guidelines into the prompt layer yields on-brand output). `blog-anthropic-claude-code-skills-lessons.md` Claim 6 (Gotchas built from observed failures) parallels the failure-driven rule accrual and named anti-patterns here.
- **Contradicts**: None found.
- **Extends**: `blog-anthropic-claude-code-skills-lessons.md` Claim 5 (skill folder as context engineering/progressive disclosure) by showing what breaks when a skill is flattened for use outside its repo. `blog-vercel-eve-extensions.md` / `blog-vercel-eve-integrations-cli.md` for eve-based agents (the @design-agent is built on eve).
- **Novel**: Stylesheet-as-documented-vocabulary that never enters context; correction-routing rule (prose / CSS / deterministic check); model-specific failures held out of rules until repeated; a small measured with/without failure count with honest limits. The triage's overlap suggestion (`blog-vercel-enterprise-apps-and-agents.md`) is only loosely related (same vendor).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the correction-routing rule (prose vs reusable mechanics vs deterministic checks) as a pattern for where to encode an accepted fix, citing Claims 8 and 3.
- **Chapter 04 (Context Engineering)**: Add "reference by documented names, not implementation" (Claim 4) and the finding that flattening an in-repo skill into a public prompt loses example context (Claim 1).
- **Evaluation chapter**: Cite the scenario/round/blind-A/B method (Claims 7, 9, 12) as a lightweight guidance-eval recipe; cite Claim 10 only as a weak, self-caveated data point.

## Extraction Notes

- Read the full article text (fetched HTML, stripped). Images (design.md excerpt, before/after renders) are not readable, so their contents are not extracted.
- Linked pages (the earlier product-design post, Anthropic's evals guide, eve template) were not followed; the article is self-contained on the method.
- Cross-reference claim numbers were checked against the cited notes' `### Claim N` headings.
