---
source_url: https://cursor.com/blog/basis
source_type: blog-post
title: "How Basis builds long-horizon accounting agents with Cursor"
author: Cursor (case study featuring Mitch Troyanovsky, cofounder, Basis)
date_published: 2026-09-04
date_extracted: 2026-09-05
last_checked: 2026-09-05
status: current
confidence_overall: emerging
issue: "#3250"
---

# How Basis builds long-horizon accounting agents with Cursor

> Cursor customer case study introducing "behavior specs" — Markdown files that
> define expected agent conduct for a judge to score against a recorded
> trajectory (true/false/NA) rather than a prompt shown to the agent — as
> Basis's answer to a specific accounting-domain problem: a correct final tax
> return can hide an unreliable process, and outcome evaluation alone cannot
> explain every consequential decision in a multi-hour, hundreds-of-decisions
> trajectory.

## Source Context

- **Type**: blog-post (Cursor company blog, "customers" category, published
  September 4, 2026; auto-discovered via the trusted `cursor-blog` RSS feed)
- **Author credibility**: Unsigned Cursor-authored case study built around two
  named, attributed quotes from Mitch Troyanovsky, cofounder of Basis (an
  accounting-automation company). This is vendor-published customer-marketing
  content (Cursor promoting a customer's usage of Cursor) rather than
  independent reporting or a first-party Cursor engineering post — closer in
  kind to `blog-anthropic-kepler-verifiable-ai-financial.md` and
  `blog-anthropic-carta-healthcare-context-engineering.md` (vendor blog +
  named customer practitioner quotes) than to `blog-cursor-agent-swarm-model-economics.md`
  (Cursor's own first-party engineering disclosure). Production metrics (40%
  of top 25 accounting firms, 6-7x speed vs. human time on Form 1065 returns)
  are self-reported by Basis via Cursor's blog, with no methodology, sample
  size, or independent audit disclosed. Treat structural/architectural claims
  (behavior specs, the development loop, the "context is production input"
  framing) as credible practitioner description; treat the headline
  performance figures as vendor-published, unverified claims.
- **Scope**: Covers why Basis considers accounting workflows harder to
  evaluate than typical long-horizon agent tasks, the "behavior spec"
  methodology and its judge-based scoring mechanism, the development loop that
  connects specs to runtime changes, why Basis uses Cursor specifically
  (editor/Markdown-preview/model-switching features), and headline production
  metrics. Does NOT cover: the actual contents of any behavior spec (no
  example spec is reproduced), the judge model or its accuracy/calibration,
  Braintrust's specific role or product beyond being named as co-releaser of
  the open standard, the runtime/agent architecture Basis uses to execute
  work, or any numbers on how many specs exist, how often specs fail, or how
  much the false-verdict-to-runtime-fix cycle actually improved measured
  behavior.

## Extracted Claims

### Claim 1: Basis agents complete Form 1065 partnership tax returns — work that takes a human roughly 30-40 hours — in roughly 6-7 hours, and are used by 40% of the top 25 accounting firms

- **Evidence**: Headline production metrics stated directly in the article and
  repeated in a sidebar stat callout ("Up to 6x faster").
- **Confidence**: anecdotal (self-reported vendor/customer figures; no
  methodology, sample size, or independent verification of the hours estimate
  or the firm-adoption percentage)
- **Quote**: "On a Form 1065 partnership return, work that can take roughly 30
  to 40 hours of human time can be completed by a Basis agent in roughly 6 to
  7 hours." / "Basis is trusted by 40% of the top 25 firms, and by leading
  accounting firms more broadly."
- **Our assessment**: A ~5x-6x time reduction on a specific, well-known tax
  form is a concrete and falsifiable-in-principle claim, but nothing in the
  article discloses how the human-hours baseline was measured (whose returns,
  what complexity tier, staffed by whom) or what fraction of Basis's returns
  require human rework after the agent's pass. The 40%-of-top-25-firms figure
  is a customer-count claim with no named customers or usage-depth detail.
  Useful as color for "this is a real production deployment, not a demo," not
  as a rigorous productivity benchmark.

### Claim 2: Long-horizon does not just mean the agent runs for hours — it means hundreds of decisions across a trajectory where later steps depend on earlier ones, requiring the system to preserve state, incorporate tool-call results, and recover from failures across more information than fits in a single context window, while early mistakes can compound and the final result may not reveal where the problem began

- **Evidence**: Definitional framing statement opening the "Work that cannot
  be reduced to a single prompt" section.
- **Confidence**: emerging (a structural/mechanistic claim about how errors
  propagate in long agent trajectories, consistent with — but not
  independently tested against — the mechanism described)
- **Quote**: "Long-horizon does not just mean the agent runs for several
  hours. It means hundreds of decisions across a trajectory, with later steps
  often depending on earlier ones. The system must preserve relevant state,
  incorporate the results of tool calls, and recover from failures, sometimes
  across more information than fits in a single context window. Errors can
  compound. An early mistake can affect later research, calculations, tool
  calls, and artifacts, while the final result may not reveal where the
  problem began."
- **Our assessment**: This redefines "long-horizon" away from wall-clock
  duration and toward decision-count and dependency-depth, which is a more
  useful operational definition for deciding when a task needs long-horizon
  tooling (state preservation, tool-result incorporation, failure recovery)
  versus when it doesn't. The final sentence — the output may not reveal
  where a problem began — is the mechanistic justification for why the
  behavior-spec/judge approach (Claims 4-6) is necessary rather than
  optional: if the failure signature is invisible in the final artifact, only
  process-level (not outcome-level) evaluation can catch it.

### Claim 3: Accounting makes long-horizon evaluation harder than the general case for three specific reasons — most outcomes lack a cheap, objective test; ground-truth examples from real production work are expensive to create and hard to scale; and a final outcome may take hours or days to produce and review — so even a correct final result can hide an unreliable process (right answer without research authority, correct number without a preserved source, a usable workbook via a non-generalizing process)

- **Evidence**: Direct enumeration of three domain-specific evaluation
  obstacles, followed by three named examples of "correct outcome, bad
  process" failure modes.
- **Confidence**: emerging (a reasoned, domain-specific elaboration of a
  general problem — outcome evaluation missing process failures — rather
  than a novel mechanism claim; each of the three named examples is
  illustrative, not measured)
- **Quote**: "Many outcomes do not have a cheap, objective test. Ground-truth
  examples drawn from real production work are expensive to create and
  difficult to scale. A final outcome may take hours or days to produce and
  review." / "Even a correct final result can hide an unreliable process. An
  agent might reach the correct tax return without research authority,
  extract the correct number without preserving its source, or produce a
  usable workbook through a process that will not generalize. Outcome
  evaluation still matters, but it is expensive to run, and it cannot explain
  every consequential decision inside a long trajectory."
- **Our assessment**: This is the article's central diagnostic claim, and it
  is a domain-specific instantiation of a problem this corpus already
  documents at the model-safety level (see Cross-References:
  `blog-openai-safety-alignment-long-horizon-models.md` Claim 1 — long
  trajectories give more chances for problems evaluations don't catch) and
  at the regulated-industry-practitioner level (`blog-anthropic-kepler-verifiable-ai-financial.md`
  Claim 11 — auditability, not accuracy, is the irreducible trust
  requirement). Basis's contribution is naming the specific mechanism by
  which "correct outcome" and "reliable process" can diverge in accounting
  work — missing research authority, unpreserved sources, non-generalizing
  workbooks — which gives the abstract "outcome evaluation is insufficient"
  thesis three concrete, domain-recognizable failure shapes.

### Claim 4: A behavior spec is a Markdown file defining recurring conduct expected from an agent in a specific situation — written for the people and judges reviewing a recorded trajectory, not shown to the agent and not a prompt — and a useful spec states when the behavior applies, what evidence to inspect, what decision and action should follow, what to do when evidence is incomplete, and what failure looks like, so the behavior is judgeable without scripting every step

- **Evidence**: Direct definitional description in the "Behavior specs make
  the standard explicit" section.
- **Confidence**: emerging (a named methodology description from a single
  company, not independently validated, but concrete and specific enough to
  be adopted or tested by another team)
- **Quote**: "A behavior spec is a Markdown file that defines recurring
  conduct expected from an agent in a specific situation. It is written for
  the people and judges reviewing a recorded trajectory. It is not a prompt,
  and it is not shown to the agent." / "A useful spec makes clear when the
  behavior applies, what evidence the agent should inspect, what decision it
  should make, what action should follow, what to do when evidence is
  incomplete, and what failure looks like. The goal is to make the behavior
  judgeable without scripting every step."
- **Our assessment**: This is the most novel artifact in the source and new
  to the corpus (see Cross-References: Novel). The key structural choice —
  the spec is deliberately *not* shown to the agent — separates it from every
  prompt/instruction pattern already in the corpus (CLAUDE.md, AGENTS.md,
  skill files, system prompts): those all shape agent behavior directly; a
  behavior spec instead defines a standard the agent's *actual* behavior is
  measured against after the fact. This is closer in spirit to a test
  assertion or an acceptance-criteria document than to a prompt, and it
  explicitly targets the "judgeable without scripting every step" middle
  ground between a rigid rule-based check and an unstructured "did this seem
  fine?" review.

### Claim 5: A judge receives the behavior spec, the observable trajectory, and the evidence (tool calls, artifacts, retrieved sources, decision records), and returns true, false, or NA, which lets the team evaluate selected parts of a process without needing a complete ground-truth answer for the whole task

- **Evidence**: Direct description of the judging mechanism, immediately
  following the spec definition (Claim 4).
- **Confidence**: emerging (a described mechanism from a single company; no
  detail on the judge's model, calibration, agreement rate with human
  reviewers, or false-positive/negative rate is given)
- **Quote**: "The judge receives the spec, the observable trajectory, and the
  evidence (tool calls, artifacts, retrieved sources, decision records). It
  returns true, false, or NA. That lets the team evaluate selected parts of
  the process without a complete ground-truth answer for the whole task."
- **Our assessment**: The three-way (true/false/NA) verdict — rather than a
  binary pass/fail — is a specific, transferable design detail: NA lets the
  judge abstain when a behavior's precondition never arose in a given
  trajectory, avoiding the false-failure noise a binary scheme would produce
  on inapplicable cases. This is a partial-coverage evaluation strategy
  functionally similar to Kepler Finance's three-axis failure attribution
  (`blog-anthropic-kepler-verifiable-ai-financial.md` Claim 8: reasoning vs.
  context vs. execution) and Carta Healthcare's granular prompt/context/retrieval
  attribution (`blog-anthropic-carta-healthcare-context-engineering.md` Claim
  5) — all three are responses to the same underlying problem (a single
  outcome-level judgment can't diagnose which part of a multi-stage or
  multi-behavior process failed), but Basis's mechanism is the only one of
  the three built around scoring named, spec-defined *behaviors* against a
  trajectory rather than scoring pipeline *stages* against an execution
  layer boundary.

### Claim 6: The development loop connecting specs to runtime keeps the spec and the implementation separate — an engineer writes or refines a behavior spec in Cursor, the agent performs the work in production, a judge scores the recorded trajectory against the spec, a false verdict identifies a gap between intended and actual behavior, and the team then revises runtime context/tools/prompts/execution (in Cursor) and reruns to measure improvement — with the spec treated as the fixed standard and the implementation as the thing that changes to meet it

- **Evidence**: Direct seven-step loop description in the "The development
  loop" section.
- **Confidence**: emerging (a described operational process from a single
  company; no data on loop iteration count, time-to-fix, or measured
  before/after improvement on any specific behavior is given)
- **Quote**: "A false verdict identifies a gap between the intended behavior
  and the runtime implementation." / "The spec and the runtime stay separate.
  The spec is the standard. The implementation changes until the agent meets
  it consistently."
- **Our assessment**: Treating the spec as immutable-relative-to-the-runtime
  is the governance principle that makes the whole system meaningful — if
  engineers could edit the spec whenever the agent failed it, the loop would
  measure nothing. This is architecturally analogous to Kepler's provenance-first
  principle (`blog-anthropic-kepler-verifiable-ai-financial.md` Claim 9:
  design the constraint in from the start, don't retrofit it) and to
  `blog-lilianweng-harness-engineering-rsi.md` Claim 14's "evaluator and
  permission control should sit outside the loop that evolves the harness" —
  all three sources independently converge on keeping the scoring standard
  structurally separate from the thing being optimized, though Basis's
  version is a human-governed spec/runtime split rather than a technical
  read-only constraint on infrastructure (contrast with Weng's Claim 11, AHE's
  read-only runs/tracer/verifier).

### Claim 7: Basis and Braintrust released the behavior-spec format as an open standard, grown from Basis's own production-accounting experience, so other teams can define and evaluate agent behavior using the same general format

- **Evidence**: Single stated sentence in the "The development loop" section,
  naming Braintrust as co-releaser without further detail.
- **Confidence**: anecdotal (a single unelaborated sentence; no link to the
  standard, no specification document, no detail on Braintrust's specific
  contribution or role, and no indication of adoption by any other team)
- **Quote**: "The behavior-spec approach grew from Basis's experience building
  production agents for accounting. Basis and Braintrust released it as an
  open standard so other teams can define and evaluate agent behavior using
  the same general format."
- **Our assessment**: This is a significant claim for the corpus if it holds
  up — an open, named, cross-vendor specification for agent-behavior
  evaluation would be a new category of artifact — but the source gives no
  way to locate or inspect the standard itself (no URL, no repository, no
  version). This should be treated as a lead for a follow-up source
  submission (search for a published Basis/Braintrust behavior-spec standard
  document or repository) rather than as a claim the guide can cite
  substantively yet. No other corpus source mentions Braintrust in this
  capacity (checked via `grep -il braintrust source-notes/`; the one existing
  match, `blog-vercel-eve-integrations-cli.md`, documents Braintrust only as
  an `eve add instrumentation/braintrust` observability integration, an
  unrelated product surface).

### Claim 8: Basis treats the context an agent reads — prompts, skills, instructions, tool descriptions — with the same rigor as code, because context is written in natural language and the organization and wording of that context (not just its content) changes what the model does next, unlike a traditional program that interprets the same valid code the same way regardless of file organization

- **Evidence**: Direct framing statement in the "Context is a production
  input" section, contrasting LLM context sensitivity with traditional
  program behavior.
- **Confidence**: settled (the underlying mechanism — that context wording
  and organization measurably affect model behavior, and that this differs
  from traditional deterministic code execution — is well-established and
  independently corroborated elsewhere in the corpus; see Cross-References)
- **Quote**: "A traditional program interprets the same valid code the same
  way regardless of how neatly the files are organized. With language
  models, the organization and wording of context change what the model does
  next. A vague sentence, a buried exception, or a misleading example can
  change production behavior. Generating a context file and shipping it
  without reading it is a production risk."
- **Our assessment**: The explicit code-vs-context contrast ("a traditional
  program interprets the same valid code the same way... with language
  models, the organization and wording of context change what the model does
  next") is a clean, quotable articulation of why context engineering is a
  distinct discipline from software engineering rather than a subset of it.
  This corroborates the "context as the real work" thesis in
  `blog-anthropic-carta-healthcare-context-engineering.md` Claim 1 and
  McRaven's "content engineering" vocabulary in
  `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 4, and the final
  sentence ("generating a context file and shipping it without reading it is
  a production risk") is a specific, actionable warning against
  auto-generating CLAUDE.md/AGENTS.md-style context files without human
  review — directly relevant to the ETH Zurich LLM-generated-AGENTS.md
  finding already in the corpus via `blog-addyosmani-code-agent-orchestra.md`
  Claim 7.

### Claim 9: What makes Cursor suited to this work, per Basis, is a real editor for revising context/spec wording, live Markdown preview alongside editing, working with a model directly in the same environment as the text, easy model switching mid-iteration, and a side-by-side file-and-agent-window loop — with cofounder Mitch Troyanovsky specifically citing Markdown preview as "an underrated differentiator" for iterating specs, skills, and other Markdown docs

- **Evidence**: Direct enumeration of five features in the "Cursor is where
  they revise the agent" section, plus a named, attributed quote from
  Troyanovsky.
- **Confidence**: anecdotal (single-customer, first-party-platform-promotional
  framing — this is Cursor's own blog naming reasons a customer prefers
  Cursor; no comparison to alternative editors/environments is offered)
- **Quote**: "Mitch Troyanovsky, cofounder of Basis, called this an underrated
  differentiator for iterating specs, skills, and other Markdown docs." /
  "Cursor is where we inspect the context that shapes the agent, and revise
  it until the behavior holds." — Mitch Troyanovsky, Co-founder of Basis
- **Our assessment**: This is vendor-promotional content (Cursor explaining
  why its own product is well-suited to a workflow it is showcasing) and
  should be weighted accordingly — it is evidence that a real-editor
  workflow with live Markdown preview and inline model access is *useful*
  for behavior-spec authoring, not evidence that Cursor specifically is
  necessary or superior to comparable tooling. The generalizable takeaway for
  the guide is the workflow shape itself (editor + live preview + inline
  model + side-by-side agent window, for iterating natural-language
  governance artifacts), independent of which vendor's product supplies it.

### Claim 10: Basis's cofounder frames the value of behavior specs as verifying process, not just outcome — "a correct tax answer can still hide a bad process," and the spec is how the team judges whether the agent checked primary authority, independent of whether the final return is correct

- **Evidence**: Direct, named, attributed quote from Troyanovsky, restating
  and personalizing the Claim 3 thesis from the founder's own perspective.
- **Confidence**: emerging (a named practitioner's stated design rationale,
  consistent with the rest of the article's framing, but a single quote from
  one company's cofounder)
- **Quote**: "A correct tax answer can still hide a bad process. I want to
  know if the agent checked primary authority, not just if the return is
  right. The spec is how we judge that." — Mitch Troyanovsky, Co-founder of
  Basis
- **Our assessment**: This is the clearest single-sentence articulation in
  the source of *why* Basis built behavior specs rather than simply scaling
  up outcome-based evaluation — it names "checked primary authority" as a
  concrete example of a process property that a correct final number cannot
  reveal on its own. For the guide, this is a strong, quotable justification
  for process-level (not just outcome-level) evaluation in any domain where
  professional standards govern *how* a correct answer must be reached, not
  merely whether it is reached (tax research, legal citation, clinical
  diagnosis criteria, audit trail requirements).

## Concrete Artifacts

### The behavior-spec development loop (as enumerated in the source)

```
Source: "How Basis builds long-horizon accounting agents with Cursor," Cursor, September 4, 2026

1. The team agrees on a recurring behavior worth measuring.
2. An engineer writes or refines the behavior spec in Cursor.
3. The agent performs its work in production, producing a recorded trajectory.
4. A judge evaluates each behavior against the spec, returning true, false, or NA.
5. A false verdict identifies a gap between the intended behavior and the
   runtime implementation.
6. The team updates the runtime context, tools, prompts, or execution
   framework. That wording gets revised in Cursor.
7. The team runs the agent again and measures whether the behavior improves.

Governing rule: "The spec and the runtime stay separate. The spec is the
standard. The implementation changes until the agent meets it consistently."
```

### Behavior spec required contents (as described, no example spec reproduced in source)

```
Source: "How Basis builds long-horizon accounting agents with Cursor," Cursor, September 4, 2026

A useful behavior spec makes clear:
  - When the behavior applies
  - What evidence the agent should inspect
  - What decision it should make
  - What action should follow
  - What to do when evidence is incomplete
  - What failure looks like

Judge inputs: the spec + the observable trajectory + evidence (tool calls,
artifacts, retrieved sources, decision records)
Judge output: true / false / NA
```

### Headline metrics (as published)

```
Source: "How Basis builds long-horizon accounting agents with Cursor," Cursor, September 4, 2026

Form 1065 partnership return:  30-40 human hours -> 6-7 agent hours (up to 6x faster)
Firm adoption:                 trusted by 40% of the top 25 accounting firms
Deliverable scale:             agents perform 5+ hours of work on a single deliverable
Built on Cursor:                since day one
Open standard:                  behavior-spec format released jointly by Basis and Braintrust
```

## Cross-References

### Cross-reference verification notes
Before writing the citations below, `blog-anthropic-kepler-verifiable-ai-financial.md`,
`blog-anthropic-carta-healthcare-context-engineering.md`,
`blog-openai-safety-alignment-long-horizon-models.md`, and
`blog-lilianweng-harness-engineering-rsi.md` were re-read directly (MINER.md
§4b) and every claim number cited below was confirmed against those notes'
numbered `### Claim N:` headings in document order. `blog-vercel-eve-integrations-cli.md`
was checked via `grep -il braintrust source-notes/*.md` to confirm it was the
only other corpus mention of Braintrust before writing Claim 7's assessment.

- **Corroborates**:
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 11 (auditability,
    not accuracy, is the irreducible trust requirement in regulated financial
    AI — "How am I supposed to trust something I can't audit?") and Claim 2
    (ambiguity escalation matters more than benchmark scores because one
    wrong early assumption compounds through all downstream steps): this
    source's Claim 3 ("even a correct final result can hide an unreliable
    process") and Claim 10 (Troyanovsky's "a correct tax answer can still
    hide a bad process") independently arrive at the same
    process-over-outcome principle from a different regulated-finance
    practitioner, in a different sub-domain (accounting vs. equity research)
    and a different vendor (Cursor vs. Anthropic/Claude).
  - `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 8 (automated
    evaluation attributing failures to reasoning/context/execution) and
    `blog-anthropic-carta-healthcare-context-engineering.md` Claim 5
    (granular evaluation attributing failure to prompt, context, or
    retrieval): this source's judge mechanism (Claim 5 — true/false/NA
    scoring of named behaviors against a trajectory) is a third,
    independently-arrived-at instance of the same underlying strategy —
    decompose an opaque end-to-end judgment into named, separately-scorable
    units — applied to *behaviors within a trajectory* rather than *pipeline
    stages*.
  - `blog-anthropic-carta-healthcare-context-engineering.md` Claim 1 ("the
    hardest problems we solved weren't about building a perfect prompt, they
    were about context construction") and
    `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 4 ("content
    engineering optimizes the system around [a call]... while prompt
    engineering optimizes a call"): this source's Claim 8 ("the organization
    and wording of context change what the model does next," unlike a
    traditional program) is a third independent vendor/customer pairing
    converging on the same "context, not prompt wording, is the production
    lever" thesis, with a novel explicit contrast to traditional
    deterministic-code behavior that neither Carta nor Kepler states.
  - `blog-lilianweng-harness-engineering-rsi.md` Claim 14 ("the evaluator and
    permission control should likely sit outside the loop that evolves
    harness") and `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 9
    ("provenance has to shape the entire system, not get added at the end"):
    this source's Claim 6 (the spec stays fixed; only the runtime
    implementation changes to meet it) is a governance-layer instance of the
    same "keep the standard structurally separate from the thing being
    optimized" principle, applied to a human-authored evaluation spec rather
    than to read-only infrastructure (Weng's AHE example) or day-one
    architectural provenance design (Kepler).

- **Contradicts**: None identified. No claim in this source materially
  opposes an existing corpus note's claim in a way that would drive different
  guide advice. No contradiction issue filed.

- **Extends**: `blog-openai-safety-alignment-long-horizon-models.md` Claim 1
  ("the same persistence that makes [long-horizon models] useful also gives
  them more opportunities to take unwanted actions... in ways that
  evaluations intended for shorter-horizon models may miss") and Claim 3
  (pre-deployment evaluation conditions never perfectly match real deployment
  conditions): that source documents the evaluation-coverage-gap problem in
  an adversarial/safety-incident context (a model exploiting a sandbox,
  evading a scanner). This source extends the same structural
  problem — long trajectories create failure surface that outcome-level
  evaluation can't see — into a non-adversarial, purely
  process-quality context: a well-behaved production agent doing legitimate
  accounting work can still take an unreliable path to a correct answer, with
  no misalignment or exploit involved. Read together, the two sources show
  the "evaluate the trajectory, not just the outcome" principle holds for
  both safety-critical and quality-critical long-horizon failure modes.

- **Novel**:
  - **Behavior specs as a named artifact class**: a Markdown document that
    defines expected agent conduct for a *judge* to score against a recorded
    trajectory, explicitly not shown to the agent and not a prompt. No prior
    corpus source documents an evaluation artifact with this specific
    property (deliberately withheld from the agent it evaluates) — every
    other context/instruction artifact in the corpus (CLAUDE.md, AGENTS.md,
    skills, system prompts, Kepler's ontology, Carta's context-assembly
    layer) is designed to be read by the agent, not withheld from it.
  - **Three-way true/false/NA behavior verdicts against a recorded
    trajectory**: distinct from binary pass/fail outcome grading and from
    the pipeline-stage attribution schemes in Kepler and Carta (which
    attribute failure to a stage of a fixed pipeline, not to a named,
    spec-defined behavior that may or may not be applicable to a given run).
  - **An open, cross-vendor "behavior-spec" standard co-released by Basis and
    Braintrust** (Claim 7): if substantiated by a locatable specification
    document, this would be the corpus's first example of a named,
    shared, cross-company evaluation-format standard for agent behavior —
    distinct from benchmark suites (SWE-bench, Terminal-Bench) and from
    single-company internal evaluation frameworks (Kepler's, Carta's, this
    source's own). Currently under-evidenced (a single sentence, no link) —
    flagged as a follow-up research target, not a settled claim.
  - **Explicit code-vs-context behavioral contrast** (Claim 8): "a
    traditional program interprets the same valid code the same way
    regardless of how neatly the files are organized. With language models,
    the organization and wording of context change what the model does
    next" is a more precise articulation of why context engineering differs
    from software engineering than any single sentence found elsewhere in
    the corpus's context-engineering notes.

## Guide Impact

- **Chapter 03 (Verification)**: Add "behavior specs" (Claim 4) as a named
  pattern distinct from existing evaluation approaches in the guide: a
  Markdown artifact that defines a judgeable standard of conduct, withheld
  from the agent, scored true/false/NA against a recorded trajectory (Claim
  5) rather than against a final outcome. Present it alongside Kepler's
  reasoning/context/execution attribution
  (`blog-anthropic-kepler-verifiable-ai-financial.md` Claim 8) and Carta's
  prompt/context/retrieval attribution
  (`blog-anthropic-carta-healthcare-context-engineering.md` Claim 5) as a
  third member of a "decompose the judgment into named, separately-scorable
  units" family — the guide should note the distinction (behavior-vs-stage
  decomposition) rather than treating all three as interchangeable.

- **Chapter 03 (Verification)**: Add "a correct outcome can hide an
  unreliable process" (Claims 3 and 10) as a named justification for
  process-level evaluation, with Basis's three concrete failure shapes
  (correct answer without research authority; correct number without a
  preserved source; a usable but non-generalizing workbook process) as
  domain-recognizable examples the guide can cite alongside Kepler's parallel
  "auditability over accuracy" framing
  (`blog-anthropic-kepler-verifiable-ai-financial.md` Claim 11).

- **Chapter 03 (Verification) / Kill Criteria or Governance sections**: Add
  the spec/runtime separation rule (Claim 6 — "the spec and the runtime stay
  separate; the spec is the standard, the implementation changes until the
  agent meets it consistently") as a concrete governance discipline: when an
  evaluation standard can be silently loosened by whoever is trying to pass
  it, the standard stops measuring anything. Cross-reference with Weng's
  "evaluator and permission control ... outside the loop" principle
  (`blog-lilianweng-harness-engineering-rsi.md` Claim 14) as the same rule
  stated for a self-improving-harness context rather than a human-governed
  spec context.

- **Chapter 04 (Context Engineering)**: Add the explicit code-vs-context
  contrast (Claim 8: unlike traditional code, "the organization and wording
  of context change what the model does next") as a concrete framing
  sentence for why context engineering is treated as a distinct discipline,
  alongside the existing Carta ("the real work") and Kepler ("content
  engineering") citations. Add the closing warning — "generating a context
  file and shipping it without reading it is a production risk" — as direct,
  quotable support for the existing caution (via
  `blog-addyosmani-code-agent-orchestra.md` Claim 7) against shipping
  unreviewed LLM-generated AGENTS.md/CLAUDE.md files.

- **Follow-up research flag (not a guide-content recommendation)**: Claim 7
  (an open Basis/Braintrust behavior-spec standard) is under-evidenced in
  this source alone. Recommend the Prospector queue a search for a
  standalone specification document or repository if one exists publicly —
  if substantiated, it would upgrade Claim 4/5's methodology from
  "one company's internal practice" to "a named, adoptable open format,"
  which materially changes how confidently the guide could recommend it.

## Extraction Notes

- WebFetch's default AI-summarization pass on this URL returned only a
  ~250-word condensed summary (paraphrased figures, no verbatim section
  text), the same limitation documented in this corpus's other Cursor-blog
  extractions (e.g. `blog-cursor-agent-swarm-model-economics.md` Extraction
  Notes). To obtain quote-accurate text, the article's raw HTML was fetched
  directly via `curl` with a standard browser user agent (HTTP 200, ~334KB),
  and the article body was extracted with a Python/BeautifulSoup script that
  removed `<svg>`/`<script>`/`<style>`/navigation elements before extracting
  block-level text. The resulting plain text contained all eleven section
  headings, all body paragraphs, and both named Troyanovsky quotes (each
  appearing twice in the raw extraction, once in a promotional summary card
  and once in the main article body — consistent, not conflicting, text).
  All quotes above were copied character-for-character from that extracted
  text.
- The article is short (~900 words of body text) and fully self-contained: no
  sub-pages, footnotes, or inline citations to external documents (including
  the claimed Basis/Braintrust open standard, which is named but not linked)
  were present to follow. The "More customer stories" related-links section
  at the bottom (Nokia, IMDEX, Vercel) links to case studies already in the
  corpus (`blog-cursor-nokia-codebase-analysis.md`) or unrelated topics; none
  were followed as part of this extraction.
- No example behavior spec, judge prompt, or trajectory-evidence record is
  reproduced anywhere in the source — every description of the spec format
  and judge mechanism (Claims 4-6, Concrete Artifacts) is the article's own
  prose description, not a quoted artifact. This caps how concretely the
  guide can illustrate the pattern without a follow-up source (see Guide
  Impact's follow-up research flag).
- No contradiction with any existing corpus source was found; none was
  filed, per MINER.md §4a.
