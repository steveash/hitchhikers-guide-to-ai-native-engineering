---
source_url: https://www.thoughtworks.com/insights/articles/ai-assisted-migration-lessons
source_type: blog-post
title: "AI-assisted migration: Critical lessons from the modernization frontlines"
author: Shashank Mishra (Thoughtworks)
date_published: 2026-07-13
date_extracted: 2026-07-20
last_checked: 2026-07-20
status: current
confidence_overall: emerging
issue: "#2063"
---

# AI-Assisted Migration: Critical Lessons from the Modernization Frontlines

> A Thoughtworks/AWS ProServe case study at an unnamed "leading sports data
> and technology company" describing a four-component framework — Golden
> Rules with green/amber/red confidence markers, file:line source
> traceability, a phased expensive-extraction/cheap-generation split, and a
> shared steering-files/ADR context layer — that compressed an 80+-sport,
> multi-year legacy Java business-logic extraction program to three to four
> weeks of total effort by redirecting scarce SME review time toward
> AI-flagged ambiguities instead of blanket output verification.

## Source Context

- **Type**: blog-post (Thoughtworks Insights article, published July 13,
  2026, from the trusted feed `thoughtworks`; ~1,150-word case study with
  two named practitioner pull-quotes attributed by role only, not by name)
- **Author credibility**: Shashank Mishra is credited as the sole byline on
  Thoughtworks' commercial insights blog; no further bio/title is given in
  the article itself. Thoughtworks is an already-established trusted
  vendor-neutral consultancy source in this corpus (see
  `blog-thoughtworks-harrison-insurance-legacy-modernization.md`,
  `blog-thoughtworks-gall-supervisory-engineering.md`). The client company
  and both quoted practitioners (a "senior product manager" and a "senior
  engineering manager," "leading"/"major sports data and technology
  company") are anonymized — no company name, no individual names, no
  independently verifiable identity. AWS ProServe is named as a delivery
  partner but not quoted or independently cited. Treat all outcome metrics
  and quotes as emerging/anecdotal vendor case-study evidence: specific and
  internally consistent, but neither the client nor the individuals can be
  independently verified, and no benchmark or control group is described.
- **Scope**: Covers why the migration needed AI acceleration (contractual
  deadline pressure, months of manual per-sport extraction effort), the
  four-component framework used to accelerate business-logic extraction
  from a legacy Java codebase, timeline/effort outcome metrics, five
  organizational preconditions for the framework to work at enterprise
  scale, and a "from experience" limitations section. Does NOT cover: the
  target platform's technology stack, how code generation from the specs
  was actually implemented or verified (Step 4 states specs "feed directly
  into code generation" but gives no detail on that generation or its
  review), specific tooling/model names, per-sport variance in the 30–60
  minute extraction estimate, how confidence-marker thresholds were
  calibrated, or any named individual practitioner (all quotes are
  role-attributed only).

## Extracted Claims

### Claim 1: Golden Rules — including a green/amber/red confidence marker on every extracted fact — were formalized specifically to prevent the AI from inventing things or making assumptions about ambiguous legacy code
- **Evidence**: Author's direct description of the framework's first
  component, stated as a named design principle ("Golden Rules") with a
  concrete mechanism (the three-color marker) and a specific triggering
  condition (code ambiguity).
- **Confidence**: emerging (a first-party methodological description from a
  single vendor case study; the marker mechanism is specific and
  operational, but not independently verified or benchmarked against an
  unmarked baseline)
- **Quote**: "We formalized Golden Rules to prevent AI from inventing things
  or making assumptions. One was that if the code was ambiguous, the AI had
  to flag the ambiguity in its output so a human expert could resolve it. To
  achieve this, every extracted fact carried a green, amber or red
  confidence marker."
- **Our assessment**: The confidence-marker mechanism is a concrete,
  transferable pattern distinct from a binary "flag or don't flag" approach
  — a three-tier marker lets SMEs triage by severity rather than treating
  every flagged item identically. This is novel to the corpus's coverage of
  anti-hallucination guardrails for legacy-code comprehension specifically
  (as opposed to code generation or general agentic tool use).

### Claim 2: Source traceability — a file:line reference back to the legacy code on every extracted fact — is characterized as the real anti-hallucination mechanism, more load-bearing than the confidence marker itself
- **Evidence**: Author's direct claim, stated as a standalone sentence
  immediately following the confidence-marker description, explicitly
  naming traceability (not the marker) as "the real" mechanism.
- **Confidence**: emerging (a first-party prescriptive claim about which of
  two paired mechanisms matters more; plausible and consistent with the
  stated SME-availability bottleneck, but not tested against a
  marker-only or traceability-only variant)
- **Quote**: "Source traceability is the real anti-hallucination mechanism.
  Every extracted fact carries a file:line reference back to the legacy
  code."
- **Our assessment**: This is the single most quotable design claim in the
  source — it draws an explicit hierarchy between two guardrail mechanisms
  that are often presented as equivalent (confidence scoring vs. source
  citation), and states that verifiable provenance, not the model's own
  self-reported confidence, is what actually anchors trust. For legacy
  comprehension work specifically, this generalizes: a model's stated
  confidence is unverifiable, but a file:line pointer is independently
  checkable by a human in seconds.

### Claim 3: Highlighting exactly where SMEs should direct their expertise (via the confidence marker and file:line trace) freed subject matter experts from manually checking every AI output, overcoming limited SME availability as the migration's most critical speed blocker
- **Evidence**: Author's direct claim, naming "limited SME availability" as
  "the most critical blocker to migration speed," paired with a
  role-attributed pull-quote from a "senior product manager" at the client
  company.
- **Confidence**: anecdotal (single, role-attributed (not individually
  named) practitioner quote from an anonymized client, in a vendor-authored
  case study; no independent corroboration of SME time savings)
- **Quote**: "These were essential for overcoming the most critical blocker
  to migration speed: limited SME availability. By highlighting exactly
  where SMEs should direct their expertise, they were freed from manually
  checking every output."
- **Quote**: "Our SMEs can't spend their time investigating every fact
  extracted by the AI. Now, they can focus on resolving the ambiguities
  that matter, so we can onboard more sports faster and give our customers
  the reliable, accurate and consistent data services they need." —
  Senior product manager, leading sports data and technology company
- **Our assessment**: This names the specific bottleneck the entire
  framework is designed around — not raw extraction speed, but scarce human
  review capacity — and frames the confidence-marker/traceability
  combination (Claims 1–2) as a review-triage mechanism rather than purely
  an accuracy mechanism. This directly corroborates
  `blog-anthropic-code-migration-playbook.md` Claim 9's rule-vs-patch
  distinction and Claim 1's "fix the process" thesis in spirit: the fix
  here is redirecting human attention, not just accelerating AI output.

### Claim 4: Extraction (analyzing legacy code) is deliberately separated from generation (producing a readable spec) because the two have very different cost profiles — 30–60 minutes of expensive AI processing with human checkpoints per sport/module for extraction, versus 5–15 minutes of cheap AI processing for spec generation from already-extracted context
- **Evidence**: Author's direct description of the framework's second
  component, with specific time ranges for both phases and an explicit
  cost-asymmetry rationale (rerunning generation is cheap; rerunning
  extraction is not needed if only formatting changes).
- **Confidence**: emerging (specific, first-party time estimates for a
  single case study; internally consistent but not independently measured
  or benchmarked against an undifferentiated single-pass approach)
- **Quote**: "Analyzing a complex Java codebase is a time-consuming and
  expensive process. Done properly, for one sport and one module, it takes
  30–60 minutes of AI processing, with human checkpoints along the way. But
  turning structured data into a readable specification document is fast
  (and therefore relatively cheap). Given the right input containing
  extracted context, AI can generate a comprehensive spec in five to 15
  minutes. And if the format needs changing or a section needs
  restructuring, it's easy to just rerun the generation step, with no need
  to re-analyze the codebase."
- **Our assessment**: The specific insight — that separating an expensive,
  human-checkpointed comprehension step from a cheap, freely-rerunnable
  formatting/generation step lets you iterate on presentation without
  re-paying the comprehension cost — is a concrete, transferable harness
  design pattern for any AI-assisted code-understanding workflow, not
  specific to sports data or migrations. This mirrors, at the
  comprehension/generation-split level, the same "expensive prerequisite,
  cheap iteration after" structure that
  `blog-anthropic-code-migration-playbook.md` Claim 5 describes for its
  "judge" construction (expensive: categorize and validate the judge once;
  cheap: run it repeatedly afterward).

### Claim 5: Separating extraction from generation also enables parallel extraction across multiple sports simultaneously, and a new sport can go from zero to implementation-ready specs in roughly 30–45 minutes of setup, four to six hours of parallel extraction, and six to eight hours of SME review
- **Evidence**: Author's direct claim, giving a three-stage time breakdown
  for onboarding a single new sport under the framework.
- **Confidence**: emerging (specific first-party timeline for a single case
  study; internally consistent with Claim 4's per-module extraction
  estimate, but not independently verified)
- **Quote**: "This makes it possible to extract business logic from
  multiple sports in parallel, saving even more time. A new sport can go
  from zero to implementation-ready specs with around 30 to 45 minutes of
  setup, four to six hours of parallel extraction and six to eight hours of
  SME review."
- **Our assessment**: Notably, SME review (6–8 hours) is stated as taking
  longer than either setup or parallel extraction combined — this is
  consistent with Claim 3's framing of SME capacity as the pacing
  bottleneck, and directly foreshadows the "From experience" section's
  warning (Claim 11) that review becomes the pacing function once
  extraction runs in parallel. The per-sport breakdown is the most
  granular timeline data point in the source and is directly comparable to
  Claim 8's aggregate 10-sport figures.

### Claim 6: A shared context layer — steering files plus architecture decision records (ADRs) — prevents each new AI session from starting from scratch and improvising, so the AI follows decisions the team already made rather than guessing, and quality improvements compound across future sports
- **Evidence**: Author's direct description of the framework's third
  component, naming the specific artifacts (steering files, ADRs) and their
  function, plus a stated compounding benefit across future work.
- **Confidence**: emerging (first-party architectural description,
  internally coherent, not independently tested against a no-shared-context
  baseline within this source)
- **Quote**: "Lost context is one of the biggest barriers to AI
  acceleration. Every session starts from scratch, and without any context,
  AI improvises, leading to inconsistent, unusable results. The shared
  steering files played a big role in providing context for every AI
  session. We also maintained architecture decision records (ADR) that
  captured every significant structural choice, so the AI followed
  decisions the team had already made, rather than guessing. This shared
  context layer also meant that the benefits of every improvement decision
  were inherited by each future sport, amplifying investments in quality."
- **Our assessment**: This is architecturally identical to the "shared
  context layer" pattern already well-established in the corpus for
  code-migration harnesses — compare
  `blog-anthropic-code-migration-playbook.md` Claim 9's rulebook that
  "keeps growing" so fixes apply to all future batches, not just one file.
  This source's contribution is applying the identical pattern to the
  *comprehension* phase of a migration (extracting business logic) rather
  than the *translation* phase, and naming ADRs specifically (not just a
  rulebook) as a second context-layer artifact type.

### Claim 7: Code for the new platform is generated directly from the reviewed specs rather than from the legacy codebase or from human memory, closing a loop that "most migrations don't," and this spec-mediated path is more likely to surface previously undocumented behavior than direct code-to-code translation
- **Evidence**: Author's direct description of the framework's fourth
  component, framing the spec as a mandatory intermediate, reviewable
  artifact between legacy comprehension and new-platform implementation.
- **Confidence**: emerging (a first-party architectural claim about
  causal mechanism — why spec-mediated generation surfaces more
  undocumented behavior than direct translation — asserted rather than
  compared against a direct-translation control within this case study)
- **Quote**: "The purpose of the business logic extraction was to close a
  loop that most migrations don't: The legacy codebase goes in, structured
  specifications come out, and the new platform is built from the specs,
  rather than guesswork or memory." / "Specs from code were also more
  likely to surface behavior nobody had written down. The behavior was
  translated into a structured spec that could be reviewed and
  deliberately carried forward or changed."
- **Our assessment**: This is a distinct architectural choice from
  `blog-anthropic-code-migration-playbook.md`'s six-step process, which
  translates code directly (rulebook → translate → compile → match
  behavior) without a mandatory human-reviewable spec artifact in between.
  This source's spec-as-mandatory-checkpoint approach trades speed for an
  explicit human decision point on every piece of extracted behavior
  ("could be reviewed and deliberately carried forward or changed") —
  a meaningfully different risk/speed tradeoff for migrations where
  undocumented business logic, not translation mechanics, is the primary
  risk (see Guide Impact).

### Claim 8: Applying the framework reduced a 10-sport migration program from an estimated two to three years down to roughly three to four weeks of total effort, or as little as one to two days with full parallel execution; onboarding a new sport dropped from 10–15 weeks to under a day
- **Evidence**: Author's direct outcome-metric claim, stated as the
  article's headline result, with two distinct compression figures (total
  program effort, and marginal per-sport onboarding time).
- **Confidence**: emerging (specific, named outcome figures from a single
  vendor case study; internally consistent with the per-sport/per-module
  time estimates in Claims 4–5, but no independent verification, and the
  "would have taken two to three years" baseline is a counterfactual
  estimate, not a measured prior-project baseline)
- **Quote**: "By applying AI within this framework, a 10-sport migration
  program that would have taken two to three years was reduced to around
  three to four weeks of total effort — or as little as one to two days
  with parallel execution. Onboarding time for a new sport dropped from 10
  to 15 weeks to less than a day, because each sport inherits shared
  templates."
- **Our assessment**: The "would have taken" baseline is explicitly a
  counterfactual estimate rather than a measured before/after on the same
  program — the same evidentiary caveat that applies to
  `blog-cursor-nab-legacy-migration.md`'s velocity claims (Claim 6's "3x
  faster than expected," Claim 7's "5-8x improvement"). The magnitude here
  (years to weeks, i.e. roughly 30-50x for the total-effort figure) is
  substantially larger than any single velocity multiplier previously in
  the corpus's migration notes, which should raise scrutiny rather than
  be taken at face value — it is one data point from one anonymized
  client, reported by the vendor that ran the engagement.

### Claim 9: A senior engineering manager at the client company reports the framework converted undocumented "tribal knowledge" that would have taken many months of manual effort to uncover into a fast, systematic decision process for what business logic to carry forward, change, or drop
- **Evidence**: Role-attributed pull-quote (not individually named) from
  the client company, placed immediately after the headline outcome
  metrics (Claim 8).
- **Confidence**: anecdotal (single role-attributed practitioner quote,
  anonymized, in a vendor-authored case study)
- **Quote**: "We had a lot of important but undocumented logic hidden in
  our legacy codebase, which would have taken many months of engineering
  effort to uncover manually. Now, we have a fast, systematic way to
  extract business logic and decide what to take with us to the new
  platform, what needs to change and what we don't need." — Senior
  engineering manager, major sports data and technology company
- **Our assessment**: The "decide what to take... what needs to change and
  what we don't need" framing is notable: it positions the extraction
  output not merely as documentation of existing behavior but as decision
  input for an active carry-forward/modify/drop triage — consistent with
  Claim 7's framing of the spec as something to be "deliberately carried
  forward or changed," not just a passive translation artifact.

### Claim 10: Five organizational conditions are named as essential preconditions for the framework to work at enterprise scale: shared context ownership by a single team, SME review capacity that keeps pace with extraction throughput, upfront-aligned success criteria for what a complete spec looks like, cross-team visibility into extraction sequencing, and codebase stability during analysis windows
- **Evidence**: Author's direct prescriptive list, presented as
  generalized preconditions ("apply to almost any large-scale
  modernization program") rather than specific to the sports-data case
  study.
- **Confidence**: emerging (a first-party prescriptive generalization
  drawn from one case study; internally coherent but not tested against a
  program missing one or more of these conditions within this source)
- **Quote**: "Shared context ownership: A single team stewards the
  reference materials, so output quality stays aligned." / "SME review
  capacity: Within a stable framework, extraction and generation will
  quickly gather pace, and review must keep up or program timelines will
  slide." / "Aligned success criteria: To prevent costly rework, you need
  upfront agreement on what constitutes a complete spec, which edge cases
  must be captured and which inconsistencies should be flagged." /
  "Cross-team visibility: Information silos create the most expensive
  delays, so keep everyone aligned on extraction sequencing and the specs
  they'll implement against." / "Codebase stability: When source code is
  in flux, you're trying to analyze a moving target. Brief freezes during
  analysis windows allow you to build a focused understanding of the
  codebase."
- **Our assessment**: "Codebase stability" — recommending brief code
  freezes during analysis windows — is the most concrete and actionable
  item in this list, and the most likely to be organizationally
  contentious (freezing a codebase mid-migration has real delivery cost).
  "SME review capacity" restates Claim 3/Claim 5's bottleneck as an
  explicit precondition rather than an observed outcome, reinforcing that
  this is the framework's central constraint, named three separate times
  across the article in three different forms (blocker, timeline
  component, precondition).

### Claim 11: Even with Golden Rules and traceability guardrails, AI can still misread the intent of dense legacy code, SME review remains a potential bottleneck if extraction outpaces review capacity, spec correctness does not guarantee behavioral correctness (a complete spec can still carry forward a legacy bug), and reference materials require ongoing maintenance or output quality drifts
- **Evidence**: Author's direct "From experience" limitations section,
  stated after the outcome metrics and organizational preconditions,
  listing four distinct residual risks.
- **Confidence**: emerging (first-party, self-reported limitations from
  the same vendor case study; presented as general cautions rather than
  specific incidents that occurred in this engagement)
- **Quote**: "Even the best AI can still misread the intent behind dense
  legacy code. Guardrails reduce this risk, but they don't eliminate it.
  And SME review can still create a bottleneck. If extraction runs in
  parallel but SME capacity doesn't, review becomes the pacing function
  and timelines stretch. Plus, while a consistent spec structure improves
  speed, it doesn't guarantee correct behavior. A spec can be complete but
  still carry forward a legacy bug or outdated rule. And finally, there's
  a maintenance cost to keeping the reference materials up to date; if the
  shared context drifts, the output quality drifts with it. Overall, the
  lesson is this: use AI to accelerate disciplined engineering work and
  expert human review, not to bypass them."
- **Our assessment**: This is the most credibility-strengthening section
  of the source precisely because it is a vendor case study self-reporting
  limitations rather than only touting outcomes. The "spec can be complete
  but still carry forward a legacy bug" point is an important, specific
  hedge on Claim 8's headline speed numbers: a fast, complete-looking spec
  is not the same as a *correct* spec, and this source does not claim the
  framework validates behavioral correctness — only that it makes
  extraction and review faster and more directed. This should temper any
  guide framing of this source as evidence that AI-assisted extraction
  eliminates migration risk.

### Claim 12: The framework was explicitly modeled on principles similar to "harness engineering," a term the article attributes via an outbound link rather than defining independently
- **Evidence**: A single sentence introducing the four-component framework,
  containing an inline hyperlink to
  `https://martinfowler.com/articles/harness-engineering.html` on the
  phrase "harness engineering" (confirmed present in the article's raw
  HTML).
- **Confidence**: anecdotal (a naming/framing choice, not an empirical
  claim; the article does not itself define or elaborate the term beyond
  the outbound link)
- **Quote**: "To ensure AI-powered acceleration didn't come at the expense
  of accuracy and consistency, we created a framework following similar
  principles to harness engineering, supporting AI to do its work in a
  controlled, repeatable way by implementing four key components."
- **Our assessment**: This is the article's only explicit self-positioning
  within a named methodology, and it points outward to Martin Fowler's site
  rather than to a Thoughtworks-original definition — notable since
  Thoughtworks and Fowler are closely associated (Fowler is Thoughtworks'
  Chief Scientist). This corroborates that "harness engineering" is
  treated as an established, citable term of art by (at least) this
  Thoughtworks author, rather than a term this article is coining. No
  further detail on the referenced Fowler article's content is extracted
  here — it was not fetched as part of this note (see Extraction Notes).

## Concrete Artifacts

### Business problem framing (verbatim)

```
Source: Shashank Mishra, "AI-assisted migration: Critical lessons from the
modernization frontlines," Thoughtworks Insights, July 13, 2026

"To show you how we tackle this challenge during a large-scale migration,
we'll explore an example at a leading sports data and technology company.
The company was modernizing a critical platform, but the build wasn't
progressing fast enough to meet the contractual deadline for retiring the
legacy platform. The delays were largely due to the months of effort
required to manually extract business logic from the legacy Java codebase
for each of the 80+ sports that had to be onboarded. So, Thoughtworks
partnered with AWS ProServe and the company's teams to accelerate business
logic extraction using AI."
```

### Four-component framework (as named and ordered in source)

```
Source: Shashank Mishra, Thoughtworks Insights, July 13, 2026

1. Golden Rules keep AI on track
   - Prevent invention/assumption; flag ambiguous code for human resolution
   - Every extracted fact: green/amber/red confidence marker
   - Every extracted fact: file:line reference to legacy code (source
     traceability — named "the real anti-hallucination mechanism")

2. A phased approach separates what's expensive from what's fast
   - Extraction (legacy code analysis): 30-60 min per sport/module,
     human checkpoints, expensive
   - Generation (spec from extracted context): 5-15 min, cheap, freely
     rerunnable without re-analyzing the codebase
   - Enables parallel extraction across sports

3. A shared context layer keeps AI informed
   - Shared steering files (per-session context)
   - Architecture decision records (ADRs) capturing structural choices
   - Benefits of improvement decisions inherited by every future sport

4. Code is generated directly from specs
   - Legacy codebase -> structured specs -> new platform code
   - Specs reviewed and deliberately carried forward or changed
   - Not code-to-code translation and not generation from memory/guesswork
```

### Outcome metrics (verbatim figures)

```
Source: Shashank Mishra, Thoughtworks Insights, July 13, 2026

Per-module extraction:        30-60 minutes (AI processing, human checkpoints)
Spec generation from context: 5-15 minutes
New sport, zero to specs:     ~30-45 min setup + 4-6 hrs parallel extraction
                               + 6-8 hrs SME review
10-sport program, total effort: 2-3 years (counterfactual) -> 3-4 weeks
                                 (or 1-2 days with full parallel execution)
New sport onboarding time:      10-15 weeks -> <1 day (shared-template
                                 inheritance)
```

### Five organizational preconditions (verbatim list)

```
Source: Shashank Mishra, Thoughtworks Insights, July 13, 2026

- Shared context ownership: a single team stewards the reference materials
- SME review capacity: review must keep pace with extraction/generation or
  program timelines slide
- Aligned success criteria: upfront agreement on what a "complete" spec is,
  which edge cases must be captured, which inconsistencies get flagged
- Cross-team visibility: avoid information silos on extraction sequencing
  and implementation targets
- Codebase stability: brief freezes during analysis windows so the AI is
  not analyzing a moving target
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-code-migration-playbook.md` Claim 9 (a rulebook "keeps
    growing" so a recurring mistake is fixed once and inherited by all
    future batches, not patched per-file) — this source's Claim 6 (shared
    steering files + ADRs, with "benefits of every improvement decision...
    inherited by each future sport") describes the identical compounding-
    context pattern, applied to legacy comprehension rather than code
    translation.
  - `blog-anthropic-code-migration-playbook.md` Claim 5 (a "judge" must be
    built and validated once, expensively, then run cheaply and repeatedly
    thereafter) — this source's Claim 4 (expensive 30-60 min extraction vs.
    cheap, freely-rerunnable 5-15 min generation) is the same
    expensive-prerequisite/cheap-iteration cost-asymmetry pattern, applied
    to a comprehension-then-documentation pipeline instead of a
    translate-then-verify pipeline.
  - `blog-cursor-nab-legacy-migration.md` Claim 5 (Cursor's Ask
    Mode/Plan Mode generating user stories and API specs from legacy code
    reverse engineering, compressing BizCalc pre-development work from 2
    months to 1 week) and Claim 6 (AI-generated flowcharts and business-
    logic summaries unblocking an Assembly migration) — both sources
    independently describe AI's core legacy-modernization value as
    *extracting and documenting undocumented business logic*, not
    accelerating code generation directly. This source adds a more
    granular, structured extraction methodology (Golden Rules, confidence
    markers, file:line traceability) than NAB's mode-based workflow
    description, and a longer time horizon (a 10-sport, 80+-sport-total
    program vs. NAB's single-project accounts).
  - `blog-thoughtworks-harrison-insurance-legacy-modernization.md` Claim 7
    (AI reduces the cost of *understanding* a legacy estate — "not by
    removing the hard work, and not by turning modernization into a
    push-button exercise") — this source's Claim 11 ("From experience")
    section is a concrete, specific instantiation of that same hedge: AI
    accelerates extraction and review-direction, but does not guarantee
    behavioral correctness ("a spec can be complete but still carry
    forward a legacy bug"), and still requires disciplined engineering and
    expert human review.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 2 ("In the
    middle loop, the human engineer's job is to evaluate whether the agent
    actually solved the right problem, not to write the code") — this
    source's confidence-marker/file:line-traceability mechanism (Claims
    1-3) is a concrete operational implementation of that supervisory role
    specifically for legacy-comprehension work: the human's job becomes
    resolving AI-flagged ambiguities, not re-deriving or re-checking every
    extracted fact from scratch.

- **Contradicts**: None identified. This source's outcome figures (a
  10-sport program compressed from an estimated 2-3 years to 3-4 weeks) are
  a larger multiplier than any single figure in
  `blog-cursor-nab-legacy-migration.md` (3x, 5-8x) or
  `blog-thoughtworks-harrison-insurance-legacy-modernization.md` (no
  specific multiplier given), but this is a difference in scale/reporting
  rather than a substantive disagreement about mechanism — all three
  sources agree that AI's primary migration value is compressing the cost
  of *understanding* legacy systems, and this source's own Claim 11
  explicitly hedges against reading its headline number as evidence that
  the underlying engineering/review discipline can be skipped, which is
  consistent with the more conservative framing in the insurance-modernization
  note rather than in tension with it.

- **Extends**:
  - `blog-anthropic-code-migration-playbook.md` (the six-step
    rulebook/dependency-map/gap-inventory -> stress-test -> translate ->
    compile -> run -> match-behavior process): that source's process
    translates code directly and does not include a mandatory
    human-reviewable intermediate spec artifact; this source's Claim 7
    (code generated directly from specs, not from code) describes a
    materially different pipeline shape for the same broad problem
    (migrating a legacy system with AI assistance) — spec-mediated
    generation vs. direct code-to-code translation. The guide should treat
    these as two distinct architectural patterns with different tradeoffs
    (see Guide Impact), not as competing implementations of the same
    pattern.
  - `blog-cursor-nab-legacy-migration.md` Claim 6 (Assembly migration
    "previously categorically impossible due to expertise scarcity," AI
    substituting for missing expertise): this source's framing is
    different — the client's engineers were not described as lacking
    Java expertise; the blocker was named specifically as *time* (months of
    manual effort per sport) and *SME review bandwidth*, not expertise
    scarcity. This is a distinct AI-migration-value category from NAB's
    Assembly case: accelerating expert-available-but-time-constrained work,
    versus unblocking expertise-unavailable work.

- **Novel**:
  - **The green/amber/red confidence-marker mechanism** paired explicitly
    with file:line source traceability, and the explicit claim that
    traceability (not the confidence score) is "the real anti-hallucination
    mechanism" — no prior corpus source names this specific paired
    mechanism or states this hierarchy between the two guardrail types.
  - **The extraction/generation cost-asymmetry split** (30-60 min expensive
    extraction vs. 5-15 min cheap, freely-rerunnable generation) as an
    explicit, named design principle for a legacy-comprehension pipeline
    specifically (distinct from the code-translation-pipeline cost
    asymmetries already in the corpus).
  - **Spec-mediated code generation as an alternative to direct
    code-to-code translation** for migrations — a materially different
    pipeline architecture from the corpus's existing migration
    methodology source (`blog-anthropic-code-migration-playbook.md`).
  - **A five-item named checklist of organizational preconditions**
    (shared context ownership, SME review capacity, aligned success
    criteria, cross-team visibility, codebase stability) for scaling an
    AI-assisted legacy-comprehension framework across a multi-unit program
    — no prior corpus source presents this specific a checklist for
    migration program scaling.
  - **An explicit, first-party "harness engineering" self-attribution**
    with an outbound citation to Martin Fowler's article on the term —
    the first corpus source to explicitly name-check "harness engineering"
    as the methodology it is following, rather than the corpus's editorial
    voice applying that label to a source's practices.

## Guide Impact

- **Chapter 04/05 (Migration & Modernization patterns)**: Add the
  green/amber/red confidence-marker + file:line traceability pattern as a
  concrete, named guardrail combination for AI-assisted legacy-code
  comprehension work, citing this source alongside
  `blog-anthropic-code-migration-playbook.md`'s "judge" validation pattern
  as two different anti-hallucination mechanisms serving the same
  underlying goal (trustworthy AI-generated migration artifacts) at
  different pipeline stages (comprehension vs. translation verification).
  Explicitly cite Claim 2's hierarchy claim (traceability over confidence
  score) as a specific, actionable design recommendation.
- **Chapter 04/05 (Migration & Modernization patterns)**: Add the
  extraction/generation cost-asymmetry split (Claim 4) as a named harness
  design pattern for any AI-assisted code-comprehension workflow: separate
  the expensive, human-checkpointed analysis step from the cheap,
  freely-rerunnable formatting/presentation step so iteration on the latter
  never re-triggers the former. Pair with this source's five
  organizational-precondition checklist (Claim 10) as a scaling
  readiness assessment for teams considering the same framework.
- **Chapter 05 (Human-in-the-loop frameworks)**: Add this source's explicit
  operational definition of "human-in-the-loop" for legacy migration: not
  reviewing all AI output, but using AI-generated signals (confidence
  markers, source traces) to *redirect* scarce human review capacity toward
  the subset of output that actually needs expert judgment (Claims 1-3).
  This is a more specific, mechanism-level answer to the triage issue's
  "what does human-in-the-loop AI framework mean operationally?" question
  than any prior corpus migration source provides. Pair with Claim 11's
  self-reported limitations (SME review can still become the bottleneck;
  spec completeness does not guarantee behavioral correctness) as a
  necessary counterweight so the guide does not present this pattern as a
  solved problem.
- **Chapter 04/05**: Note the spec-mediated code-generation architecture
  (Claim 7) as a distinct alternative to `blog-anthropic-code-migration-playbook.md`'s
  direct code-to-code translation pipeline, worth naming explicitly as a
  design choice: spec-mediation adds a mandatory human-reviewable
  checkpoint (higher assurance, more human time) versus direct translation
  with automated verification (faster, less explicit human review per
  unit of code) — the guide should frame this as a tradeoff decision point
  tied to how much undocumented/high-risk business logic a given migration
  is expected to contain, not as one approach being strictly better.

## Extraction Notes

- The article was fetched via `curl` with a browser user-agent directly
  (not through the WebFetch tool's summarization pass) after confirming the
  raw HTML contained the full article body inline (no client-side
  rendering/`__NEXT_DATA__` payload was needed). HTML tags were stripped
  programmatically and all quotes in this note were copied character-for-
  character from that raw-text extraction, satisfying MINER.md §2a. One
  HTML numeric entity (`&#43;`) was identified and decoded to `+` (in the
  "80+ sports" figure); no other unresolved entities were present in the
  extracted text.
- No sub-pages were followed. The article's "Recommended content" footer
  links to three unrelated Thoughtworks articles ("The evolving landscape
  of the sports industry," "How to keep large projects on track with
  business capability mapping," "A playbook for winning in the new era of
  sports and entertainment") which are not migration- or AI-specific and
  were judged out of scope for this extraction. The article's one
  substantive inline link — to Martin Fowler's "harness engineering"
  article (`martinfowler.com/articles/harness-engineering.html`, cited in
  Claim 12) — was not fetched as a sub-page; this note only records that
  the link exists and what surrounding text says, not the linked article's
  own content. A future source note specifically on Fowler's harness
  engineering article (if not already in the corpus) could deepen this
  connection.
- The source is fully anonymized: no client company name, no individual
  practitioner names (only role titles: "senior product manager," "senior
  engineering manager"), consistent with Thoughtworks' other case-study
  articles already in this corpus that do name individuals (e.g.
  `blog-thoughtworks-harrison-insurance-legacy-modernization.md`'s named
  author with no client case study at all). This is a materially weaker
  evidentiary basis than `blog-cursor-nab-legacy-migration.md`'s five
  named-and-titled NAB practitioners — flagged here because the Assayer
  should weigh confidence accordingly; `confidence_overall` is set to
  `emerging` rather than `settled` primarily for this reason, plus the
  unverified/counterfactual nature of the headline 2-3-years-to-3-4-weeks
  figure (Claim 8).
- No contradiction was identified that rose to the level of filing a
  formal contradiction issue per MINER.md §4a — see Cross-References →
  Contradicts above for the reasoning (scale/reporting difference, not a
  disagreement about underlying mechanism).
