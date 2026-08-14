---
source_url: https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5
source_type: blog-post
title: "Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5"
author: Anthropic (case study featuring Vladislav Tankov, CTO at JetBrains Agent Systems)
date_published: 2026-08-13
date_extracted: 2026-08-14
last_checked: 2026-08-14
status: current
confidence_overall: emerging
issue: "#2689"
---

# Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5

> Anthropic case study built around an interview with JetBrains Agent Systems CTO
> Vladislav Tankov, covering JetBrains' private-repo evaluation pipeline (Claude
> Fable 5: 44.3% Python pass rate vs. Opus 4.8's 28.2%, 22% fewer steps), a
> workhorse-vs-reasoning-partner model-selection heuristic (Opus vs. Fable 5),
> spec-driven agentic app rewriting, white-box security testing against
> JetBrains' own products, and an infrastructure-centric enterprise safety
> stance that explicitly defers model safety to Anthropic's red-teaming.

## Source Context

- **Type**: blog-post (Anthropic/Claude blog, claude.com/blog, published
  2026-08-13; corporate case study built around quotes from a named
  practitioner, no individual Anthropic byline — same publication pattern as
  `blog-anthropic-cognition-fable5-frontier-trust.md`)
- **Author credibility**: Published by Anthropic — marketing framing, hosted
  to position Claude Fable 5 favorably — but the substantive claims are
  attributed throughout to Vladislav Tankov, identified in the article's
  subtitle as "JetBrains Agent Systems CTO." JetBrains is a major IDE/dev-tool
  vendor (IntelliJ IDEA, PyCharm, Kotlin) that serves, per the article, 12.5
  million active users and 88 of the Fortune Global 100 — giving Tankov's
  organization direct, large-scale production exposure to model evaluation
  and deployment decisions. No independent/non-Anthropic-hosted account of
  these claims exists in this source; treat as a single-practitioner account
  amplified by a vendor channel, same caveat as the Cognition case study. No
  benchmark methodology detail (task count, task composition of the private
  eval suite, exact repos used), architecture diagram, or third-party
  verification is included.
- **Scope**: Covers JetBrains' private-repo/monorepo evaluation pipeline and
  headline benchmark numbers, a model-selection heuristic (Opus as workhorse
  vs. Fable 5 for hard reasoning), a spec-driven long-running agentic app
  rewrite use case, white-box security testing of JetBrains' own products,
  data retention and safety tradeoffs, an infrastructure-vs-model-tweaking
  enterprise safety stance, and a "cockpit" framing for JetBrains' future
  agentic-development-lifecycle product direction. Does NOT cover: the exact
  composition or size of JetBrains' private eval suite, pricing, the specific
  vulnerabilities found via white-box testing, quantified data on how often
  the "workhorse vs. reasoning partner" heuristic is followed in practice, or
  any named product roadmap detail beyond the "cockpit" metaphor.

## Extracted Claims

### Claim 1: JetBrains evaluates frontier models against large eval sets built on its own private repositories, including its internal monorepo, rather than relying on public benchmarks alone
- **Evidence**: Direct statement of JetBrains' evaluation methodology, given in response to a question about how Claude Fable 5 scored relative to previous models.
- **Confidence**: settled (first-party statement of a described, ongoing internal practice)
- **Quote**: "We're a coding company, so we have a big evaluation pipeline: large eval sets on private repositories, including our monorepo."
- **Our assessment**: This is a private-repo evaluation practice, not a claim about results — it is the methodological premise for Claims 2 and 3. It corroborates `blog-anthropic-choosing-claude-model.md` Claim 9's stated reason for custom evaluations (benchmark saturation among top-tier models), and mirrors `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 1 (Cognition's "we trust no eval" stance, gating adoption on its own engineers' judgment) — both are large coding organizations independently converging on the same practice: don't trust public benchmarks alone for frontier-model adoption decisions, build your own private eval pipeline instead.

### Claim 2: On JetBrains' private eval suite, Claude Fable 5 posted a 44.3% Python pass rate against Opus 4.8's 28.2%, a 16-point improvement
- **Evidence**: Specific before/after percentage figures attributed to JetBrains' internal eval suite.
- **Confidence**: emerging (specific numeric comparison from a credible, large-scale source, but the eval suite's task count, task composition, and exact methodology are not disclosed in this source)
- **Quote**: "Claude Fable 5 is both more accurate and more efficient than prior models. It posted the best Python pass rate in our suite at 44.3%, against 28.2% for Opus 4.8, a 16-point jump."
- **Our assessment**: A ~16-point absolute jump on an undisclosed private benchmark is directionally consistent with `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 6 (Cognition's Frontier Code benchmark: prior Opus ~10% vs. Fable 5 ~30% on the hardest subset) — a second, independently run private coding benchmark also shows a large Fable-5-over-Opus jump, though the two benchmarks are not comparable in absolute terms (different task sets, different Opus baseline version, different pass-rate definitions). Should be cited as JetBrains' internal claim, not an independently reproducible result.

### Claim 3: In a head-to-head comparison on the same eval suite, Claude Fable 5 solved 18 Python tasks that Opus 4.8 missed and lost only 2 tasks that Opus 4.8 solved
- **Evidence**: Task-level win/loss comparison on the same private eval suite referenced in Claims 1–2.
- **Confidence**: emerging (specific task-level counts, but underlying task set and total task count are not disclosed)
- **Quote**: "In a head-to-head comparison, Claude Fable 5 solved 18 Python tasks that Opus 4.8 missed and lost only 2."
- **Our assessment**: This 18-vs-2 asymmetry is a more granular data point than the aggregate 16-point pass-rate gap (Claim 2) — it shows the improvement is not evenly distributed but concentrated in specific tasks Opus 4.8 could not solve at all, with very little regression on tasks Opus 4.8 already handled. Useful as a concrete illustration of what a "16-point pass-rate jump" looks like at the task level, though the total task-set size (needed to judge whether 18-vs-2 out of, e.g., 50 or 500 tasks) is not given.

### Claim 4: Claude Fable 5 needed about 22% fewer steps than Opus 4.8 to reach a solution, and on Java tasks specifically, Opus 4.8 repeatedly pulled in outside resources that rarely helped in JetBrains' environment while Fable 5 worked with the code already present
- **Evidence**: Efficiency comparison (step count) plus a named example of a specific inefficient behavior (Opus 4.8 reaching for external resources on Java tasks) that Fable 5 did not exhibit.
- **Confidence**: emerging (specific efficiency figure and behavioral observation from the same undisclosed-methodology private eval suite as Claims 1–3)
- **Quote**: "Claude Fable 5 needed about 22% fewer steps than Opus 4.8 to reach a solution."
- **Quote**: "On Java tasks, Opus 4.8 repeatedly tried to pull in outside resources that almost never help in our environment, while Claude Fable 5 skipped that entirely and worked with the code in front of it."
- **Our assessment**: "Pulling in outside resources that almost never help" is a concrete, named inefficiency pattern (reaching for external dependencies/resources instead of working with the existing codebase) that is more specific and actionable than a generic "fewer steps" efficiency claim — it names the mechanism behind at least part of the step-count reduction for one language (Java) specifically. The step-count reduction itself is not broken down by language, so the 22% figure should be read as an aggregate across the suite, of which the Java-specific behavior is one contributing example, not the whole explanation.

### Claim 5: JetBrains' model-selection heuristic treats Opus as the reliable default "workhorse" and reaches for Claude Fable 5 specifically for hard-reasoning tasks where the practitioner is themselves uncertain how to proceed
- **Evidence**: Direct statement of JetBrains' internal decision rule for choosing between Opus and Fable 5.
- **Confidence**: settled (stated as a clear internal decision rule, though with no quantified split of how often each path is taken)
- **Quote**: "Opus is seen as a workhorse: you can be very sure it will do the work. You go to Claude Fable 5 when you really need good reasoning, when you almost need a partner, and you're not sure yourself how to do the thing."
- **Our assessment**: This directly corroborates `blog-anthropic-choosing-claude-model.md` Claim 5, Anthropic's own stated rule of thumb: "if your evals or internal testing show Opus struggling on some tasks, then Fable is the answer. If Opus already clears the quality bar, then its speed and price profile may make it the better choice." JetBrains' framing adds a qualitative dimension Anthropic's own post does not state as explicitly — Fable 5 as a reasoning "partner" for tasks where the practitioner's own uncertainty, not just task difficulty, is the trigger for reaching for the stronger model. This is a second, independent practitioner account converging on the same Opus-vs-Fable decision boundary Anthropic itself recommends.

### Claim 6: JetBrains' most popular long-running agentic-coding use case for Claude Fable 5 is spec-driven app implementation, where specifications can themselves be agent-generated from an existing app, enabling near-black-box rewrites of an app from one runtime, framework, or language to another
- **Evidence**: Direct description of the workflow and its two components (agent implementing from a spec; agent generating the spec from an existing app) in response to a question about when JetBrains uses Fable 5 over other models.
- **Confidence**: settled (direct description of a described, ongoing internal use case)
- **Quote**: "Another popular Claude Fable 5 use case is long-running agentic-coding experimentation. We provide an agent running Claude Fable 5 with specifications (in the form of text and images) and make it implement sophisticated IDE-like apps. The interesting thing here is that specifications can also be generated by the agent, based on the existing app. Joining these two components allows us to rewrite the app from one runtime, framework, or language to another in a nearly black-box setup."
- **Our assessment**: The two-component pattern here (agent-generated spec extraction from an existing app, then agent-driven re-implementation from that spec) is a specific, reusable architecture for large-scale migration work — it separates "understand what the app currently does" from "build it again in a new target," with an agent doing both halves and a spec as the intermediate artifact. This is more concrete than a generic "AI-assisted migration" claim: the spec is explicitly named as the interface between the two agent runs, and the result is characterized as "nearly black-box," implying limited human involvement in the loop beyond providing initial specs and images.

### Claim 7: JetBrains runs white-box vulnerability testing against its own products using Claude Fable 5-class models, and its security team is explicitly preparing for external actors using frontier models to probe JetBrains' products for vulnerabilities
- **Evidence**: Direct statement combining JetBrains' own defensive use of frontier models with an explicit forward-looking threat-model statement about external attackers.
- **Confidence**: settled (direct statement of both a current internal practice and an explicit stated expectation about future external threats)
- **Quote**: "We run white-box testing against our own products to find vulnerabilities, and our security team is preparing for the fact that not only are we running the model—people outside the company will be running Claude Fable 5, or similar-class models, to probe for vulnerabilities across all of our products."
- **Our assessment**: This names a dual-use dynamic explicitly and symmetrically: the same class of model JetBrains uses defensively (white-box testing its own code) is anticipated to be used offensively by external actors against JetBrains' products. This is a specific, named instance of "frontier models as both attacker and defender tooling" from a major dev-tool vendor's own security team, not a generic industry observation — relevant to any guide discussion of AI-accelerated offense/defense symmetry alongside `blog-anthropic-ai-accelerated-offense.md`.

### Claim 8: JetBrains would prefer zero data retention but accepts limited retention as a tradeoff, on the condition that human review of retained data is restricted to investigating the most serious flagged cases
- **Evidence**: Direct statement of JetBrains' position on data retention, given in response to a question about safety and data retention with frontier models.
- **Confidence**: settled (direct statement of a stated internal policy position, though "most serious flagged cases" is not further defined with specific criteria or thresholds)
- **Quote**: "We'd prefer zero data retention. But I don't see any other way for you to understand what was asked and where a classifier may have worked incorrectly. As long as reviews are only to investigate the most serious cases flagged, I'm okay with it."
- **Our assessment**: This is a conditional acceptance, not an unconditional one — the stated tradeoff (zero retention preferred, limited retention accepted) is explicitly scoped to review of flagged/serious cases only, not general access to retained prompts. This corroborates `blog-anthropic-choosing-claude-model.md`'s Concrete Artifacts note that Mythos/Fable "both require limited data retention" — JetBrains' statement is a practitioner's account of accepting that same tradeoff, with an explicit condition attached (review scope limited to serious flagged cases) that the Anthropic model-selection post does not itself state.

### Claim 9: JetBrains does not attempt to independently verify frontier model safety itself; it explicitly relies on Anthropic's red-teaming and safety work, and focuses its own effort on systematic deployment-time infrastructure and harness controls around the model rather than modifying the model
- **Evidence**: Direct statement of JetBrains' enterprise safety philosophy, given in response to a question about safety and data retention.
- **Confidence**: settled (direct statement of a described organizational stance)
- **Quote**: "We're not a company trying to create the safest model ourselves. We expect that the red teaming and everything else done on Anthropic's side is enough to believe the model is safe. Then we take a systematic approach to deployment, where we can guarantee safety: creating the infrastructure and the safety net around the model and the harness, rather than tweaking the model itself."
- **Our assessment**: This is a clean statement of a division-of-labor safety model — vendor (Anthropic) owns model-level safety via red-teaming, deploying organization (JetBrains) owns deployment-level safety via infrastructure and harness controls. This directly corroborates `blog-anthropic-ciso-guide-agentic-ai.md` Claim 2's four-question risk assessment framework and Claim 3's "principle of least agency" (grant the narrowest capability that completes the task) — both are examples of the same infrastructure-centric, not model-centric, approach to enterprise agent safety. JetBrains' statement is notable as an explicit customer-side articulation of trusting the vendor's model-safety work rather than attempting to duplicate it.

### Claim 10: JetBrains describes a shift in attitude toward frontier AI in 2026 among both its customers and its own staff, from AI skepticism to acceptance that AI is a durable part of software development
- **Evidence**: Direct statement characterizing the change in attitude over the course of 2026.
- **Confidence**: anecdotal (subjective characterization by a single executive, no survey or measured data on skeptic-to-accepter conversion)
- **Quote**: "we moved from having AI skeptics among our customers and inside the company to seeing that AI is here to stay. Literally every skeptic in the company has changed."
- **Our assessment**: "Literally every skeptic in the company has changed" is a strong, unqualified claim with no supporting data (headcount, survey, or specific examples of skeptics who changed their view) — should be read as an executive's characterization of organizational sentiment, not a measured outcome. Directionally consistent with the general 2026 corpus narrative of increasing frontier-model adoption but should not be over-cited as evidence of universal internal consensus at JetBrains specifically.

### Claim 11: JetBrains frames its future product direction around a "cockpit for software development" — a space where agents and people collaborate and where people manage the development process — and sees an opportunity to build products across the full agentic software development lifecycle that powers that cockpit
- **Evidence**: Direct statement of JetBrains' forward-looking product framing, given in response to a question about what's next on JetBrains' AI roadmap.
- **Confidence**: anecdotal (forward-looking product vision statement, not a shipped product or roadmap commitment with dates)
- **Quote**: "What matters now is a kind of cockpit for software development: a space in which agents and people collaborate, and where people can manage the development process."
- **Quote**: "We see an opportunity to build the next generation of products across the agentic software development lifecycle that powers that cockpit."
- **Our assessment**: The "cockpit" metaphor is a specific, named framing for a human-agent collaboration workspace, distinct from a single product feature — it positions the human role as managing/overseeing a process that agents execute, rather than performing the work directly. No specific product name or ship date is attached to this framing in the source; it should be treated as JetBrains' stated strategic direction, not a described or shipped product.

## Concrete Artifacts

```
JetBrains private eval suite results (Claude Fable 5 vs. Opus 4.8)
Source: claude.com/blog, "Securing the frontier: How JetBrains evaluates
and deploys Claude Fable 5," 2026-08-13

Python pass rate:        Fable 5 44.3%  vs.  Opus 4.8 28.2%   (16-point gap)
Head-to-head task wins:  Fable 5 solved 18 tasks Opus 4.8 missed
                          Fable 5 lost only 2 tasks to Opus 4.8
Steps to solution:       Fable 5 needed ~22% fewer steps than Opus 4.8
Java-specific behavior:  Opus 4.8 repeatedly pulled in outside resources
                          that "almost never help"; Fable 5 worked with
                          the code already present

JetBrains scale (as stated in the article):
  12.5 million active users
  88 of the Fortune Global 100 as customers
```

```
Spec-driven agentic app rewrite workflow (as described)
Source: same URL, "When do you use Claude Fable 5 over other models?" section

1. Agent (running Claude Fable 5) generates a specification (text + images)
   from an EXISTING app
2. A second agent run (Claude Fable 5) implements a sophisticated IDE-like
   app FROM that specification
3. Combining (1) and (2) => near-black-box rewrite of an app from one
   runtime/framework/language to another
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, claims in cited source notes were verified by
re-reading those notes directly (MINER.md §4b). Claim numbers in cited notes
are counted top-to-bottom in document order as they appear in each note.

- **Corroborates**:
  - `blog-anthropic-choosing-claude-model.md` Claim 5 ("The general rule of
    thumb is if your evals or internal testing show Opus struggling on some
    tasks, then Fable is the answer. If Opus already clears the quality bar,
    then its speed and price profile may make it the better choice.") — this
    source's Claim 5 (JetBrains: Opus as workhorse, Fable 5 for hard
    reasoning) is a second, independent practitioner account that lands on
    the same Opus-vs-Fable decision boundary Anthropic itself recommends,
    with an added qualitative dimension (Fable 5 as "partner" when the
    practitioner is themselves uncertain).
  - `blog-anthropic-choosing-claude-model.md` Claim 9 (benchmark saturation
    among top-tier models is why Anthropic recommends custom evaluations
    over public benchmarks) — this source's Claim 1 (JetBrains' private-repo
    eval pipeline, including its monorepo) is a concrete, named instance of
    exactly the practice Claim 9 recommends, from an independent large
    coding-tool vendor rather than from Anthropic itself.
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 1 (Cognition:
    "the team trusts its own engineers over any score... its highest-taste
    developers put each new model through a real day of work") — this
    source's Claim 1 is a second large coding organization independently
    building and relying on a private evaluation pipeline rather than public
    benchmarks for frontier-model adoption decisions, strengthening the
    pattern as cross-organizational rather than a single-company practice.
  - `blog-anthropic-cognition-fable5-frontier-trust.md` Claim 6 (Cognition's
    private "Frontier Code" benchmark: prior Opus ~10% vs. Fable 5 ~30% on
    the hardest subset) — this source's Claim 2 (JetBrains' private suite:
    Opus 4.8 28.2% vs. Fable 5 44.3% Python pass rate) is a second,
    independently run private coding benchmark also showing a large
    Fable-5-over-Opus improvement, though the two benchmarks use different
    task sets, different Opus baseline versions, and different scoring
    definitions, so the absolute numbers are not directly comparable.
  - `blog-anthropic-ciso-guide-agentic-ai.md` Claim 3 ("the principle of
    least agency tells you what to do with the four-question assessment:
    grant the narrowest capability that still completes the task") — this
    source's Claim 9 (JetBrains: "creating the infrastructure and the safety
    net around the model and the harness, rather than tweaking the model
    itself") is a customer-side statement of the same infrastructure-centric
    safety philosophy Anthropic's own CISO guide prescribes, with JetBrains
    explicitly framing model-safety verification as Anthropic's
    responsibility (via red-teaming) and deployment-safety as its own.

- **Contradicts**: None identified. No existing corpus note makes a claim
  about JetBrains' evaluation methodology, Opus-vs-Fable-5 selection, or
  enterprise safety stance that this source opposes. No contradiction issue
  filed.

- **Extends**:
  - `blog-anthropic-cognition-fable5-frontier-trust.md`: that note documents
    an AI-coding-product company's (Cognition/Devin) practitioner account of
    Fable 5 as a step change for sustained unattended agentic sessions. This
    source documents a different large dev-tool vendor's (JetBrains)
    practitioner account of Fable 5 evaluation and deployment, adding a
    second organization's independent benchmark numbers, model-selection
    heuristic, and — new to this pairing — a security-testing and enterprise
    safety-governance angle that the Cognition case study does not cover.
  - `blog-anthropic-choosing-claude-model.md`: that note documents
    Anthropic's own first-party model-selection framework and recommends
    custom evaluations over public benchmarks specifically for top-tier
    models. This source supplies a concrete, named customer implementation
    of both recommendations (private eval pipeline; Opus-vs-Fable decision
    rule) from JetBrains' side, with specific numbers Anthropic's own post
    does not provide for any single customer.
  - `blog-anthropic-ciso-guide-agentic-ai.md`: that note documents Anthropic's
    own prescriptive enterprise-safety framework (four-question risk
    assessment, least agency, seven operational controls). This source
    supplies a customer's (JetBrains) own account of adopting the same
    infrastructure-over-model-tweaking philosophy, plus a specific data-
    retention tradeoff position (Claim 8) not covered in the CISO guide.

- **Novel**:
  - **The "18 Python tasks solved, 2 lost" head-to-head task-level
    comparison** (Claim 3): no prior corpus source reports task-level
    win/loss counts for a Fable-5-vs-Opus comparison; prior sources report
    only aggregate pass-rate or benchmark-percentage figures.
  - **The specific named inefficiency pattern of Opus 4.8 "pulling in
    outside resources that almost never help" on Java tasks** (Claim 4): no
    prior corpus source names this specific behavioral difference between
    Opus and Fable 5 on a specific language.
  - **The two-agent, spec-as-intermediate-artifact app rewrite pattern**
    (Claim 6): an agent generating a specification from an existing app,
    then a second agent implementing from that spec to enable a "nearly
    black-box" cross-runtime/framework/language rewrite, is a new pattern to
    this corpus — prior migration-related sources (e.g., the code-migration
    playbook) do not describe an agent-generated-spec intermediate step.
  - **A named dev-tool vendor's security team explicitly stating it expects
    external attackers to use frontier models against its own products**
    (Claim 7): this specific forward-looking threat-model statement, from a
    company the size and reach of JetBrains, is new to the corpus.
  - **A customer's explicit conditional acceptance of limited data
    retention, scoped to review of only the most serious flagged cases**
    (Claim 8): prior corpus sources document Anthropic's own retention
    requirements for Mythos/Fable access, but not a customer's own stated
    conditions for accepting that tradeoff.

## Guide Impact

- **Chapter 04 (Evaluation & Benchmarking)**: Add Claim 1 (JetBrains' private
  monorepo eval pipeline) and Claim 2/3 (44.3% vs. 28.2% Python pass rate;
  18-vs-2 head-to-head task comparison) as a second concrete, named-company
  example of building a private evaluation suite for frontier-model
  adoption decisions, alongside `blog-anthropic-cognition-fable5-frontier-
  trust.md`'s Frontier Code benchmark. The guide should note both examples
  as internal, non-reproducible benchmarks (task composition undisclosed in
  both cases) rather than citing the specific percentages as
  externally-verifiable facts about model capability.

- **Chapter 04 (Model Selection)**: Add Claim 5 (Opus as workhorse, Fable 5
  for hard reasoning/uncertainty) as a second, independent practitioner
  account directly corroborating Anthropic's own stated rule of thumb
  (`blog-anthropic-choosing-claude-model.md` Claim 5). Currently the guide's
  model-selection section likely cites only Anthropic's own framing; this
  source lets the guide show a customer independently landing on the same
  decision boundary, which strengthens the recommendation's credibility
  beyond a single vendor's self-description.

- **Chapter 05 (Multi-agent systems & Orchestration)**: Add Claim 6 (the
  spec-generation-then-implementation two-agent rewrite pattern) as a
  concrete architecture for large-scale, low-human-touch app migration or
  rewrite work — worth cross-referencing against any existing guide content
  on agentic code migration, since the "agent generates the spec, a second
  agent implements from the spec" split is a specific, reusable pattern not
  otherwise documented in the corpus at this level of detail.

- **Chapter 06/07 (Security / Deployment Safety)**: Add Claim 7 (JetBrains'
  white-box self-testing plus explicit anticipation of external frontier-
  model-powered attackers) as a concrete instance of the dual-use dynamic
  around frontier coding models — pair with `blog-anthropic-ai-accelerated-
  offense.md` for the broader offense/defense symmetry framing. Add Claim 9
  (infrastructure-and-harness-centric safety, explicit reliance on
  Anthropic's red-teaming for model-level safety) as a named customer
  articulation of the vendor/deployer safety division of labor that
  `blog-anthropic-ciso-guide-agentic-ai.md` prescribes — useful as a
  practitioner-side confirmation that this division of labor is actually
  practiced, not just recommended by the vendor. Add Claim 8 (JetBrains'
  conditional acceptance of limited data retention, scoped to serious
  flagged-case review only) as a concrete example of how an enterprise
  customer negotiates the data-retention tradeoff described more abstractly
  in `blog-anthropic-choosing-claude-model.md`'s Mythos/Fable access
  requirements.

## Extraction Notes

1. **WebFetch returned AI-summarized/paraphrased content on the first pass,
   and refused full verbatim reproduction on a subsequent pass citing
   copyright concerns**: consistent with the pattern noted in several prior
   source notes in this corpus (e.g. `blog-jetbrains-agentic-ai-governance.md`,
   `blog-jetbrains-air-acp-local-models.md`), the fetch tool does not return
   raw article text on a general request. To recover verbatim quotes, four
   separate targeted WebFetch passes were run, each requesting specific,
   short (1–3 sentence) direct quotes on a named topic (evaluation
   methodology, model selection, security testing, data retention, agentic
   rewrite use case, safety philosophy, skepticism-to-acceptance shift,
   roadmap framing, byline/title). A fifth pass specifically re-verified two
   quotes that had been returned with ellipsis truncation in earlier passes
   (the Java-tasks/outside-resources sentence, and the spec-driven-rewrite
   paragraph) by requesting the full surrounding paragraph without omission;
   both were returned in full on that pass and are quoted here in full,
   replacing the earlier truncated versions. All quotes used in this note
   were returned as complete, non-ellipsized sentences from at least one
   pass.
2. **No sub-pages followed**: the article is a single-page Q&A-style case
   study (question/answer interview format) with no linked footnotes or
   related-post links surfaced in the fetched content that met MINER.md
   §1's "substantive linked page" bar.
3. **No paywall or access issues**: the article was fully readable via
   WebFetch across all passes.
4. **Confidence graded "emerging" overall**: while several individual claims
   (methodology statements, direct policy/philosophy statements) are graded
   "settled" because they are unambiguous first-party statements of current
   practice, the headline numeric claims (Claims 2–4) rest on an undisclosed
   private eval suite with no published task count, task composition, or
   independent verification — the same caveat applied to the comparable
   Cognition Frontier Code benchmark in `blog-anthropic-cognition-fable5-
   frontier-trust.md`. The overall grade follows that precedent: numeric
   claims from an undisclosed private benchmark, hosted on a vendor channel,
   from a single practitioner account, without independent corroboration of
   the specific figures.
5. **No contradictions found**: cross-referencing against the corpus (see
   Cross-References above) found this source fully consistent with existing
   Anthropic and JetBrains-adjacent notes on model selection, evaluation
   methodology, and enterprise safety philosophy. No contradiction issue
   filed.
