---
source_url: https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals
source_type: blog-post
title: "Better Harness: A Recipe for Harness Hill-Climbing with Evals"
author: Vivek Trivedy (LangChain)
date_published: 2026-04-08
date_extracted: 2026-05-24
last_checked: 2026-05-24
status: current
confidence_overall: emerging
issue: "#107"
---

# Better Harness: A Recipe for Harness Hill-Climbing with Evals

> A LangChain practitioner guide presenting Better-Harness — a systematic,
> eval-driven framework for autonomously iterating on agent harnesses using
> ML-style train/test separation, holdout sets to prevent overfitting, and
> human review before production deployment.

## Source Context

- **Type**: blog-post (LangChain blog, April 8, 2026; ~8 min read; authored by
  Vivek Trivedy, LangChain team)
- **Author credibility**: Vivek Trivedy writes for LangChain, the team behind
  LangSmith and the dominant Python agent orchestration ecosystem. LangChain has
  direct visibility into how practitioners build and iterate on agents at scale.
  Claims are first-party practitioner patterns with an open-sourced research
  implementation cited as corroboration. The post references Meta-Harness
  (Stanford) and Auto-Harness (DeepMind) as prior formal work, positioning
  Better-Harness as applied engineering adjacent to that research. All content
  is vendor-positioned (LangSmith is the observability platform being
  illustrated) but the underlying patterns are platform-agnostic principles.
  No benchmarks with baselines are provided; experimental results are from
  in-house testing with Claude Sonnet 4.6 and Z.ai GLM-5.
- **Scope**: Covers the complete pipeline for iterative harness improvement:
  eval sourcing (hand-curated, production traces, external datasets), tagging
  for holdout set design, the six-step optimization loop, types of harness
  changes discovered (prompt vs. tool description updates), results from a
  concrete experiment, and the vision for automated trace-driven future
  improvement. Does NOT cover CLAUDE.md/settings.json tooling, multi-agent
  orchestration, or code-generation agents specifically. The harness improvement
  framing is general enough to apply to any agent class.

## Extracted Claims

### Claim 1: Evaluations serve as "training data" for harness engineering — each eval case supplies the feedback gradient for subsequent harness modifications

- **Evidence**: The opening analogy is the core conceptual frame of the entire
  post: in ML, training data drives parameter updates; in agent development,
  evals drive harness updates. The post draws the parallel explicitly and
  applies ML data-quality principles (curation, balance, representativeness) to
  eval design.
- **Confidence**: emerging (conceptual framework from a practitioner team;
  plausible and widely applicable, but not validated against alternative
  improvement strategies in a controlled study)
- **Quote**: "Evals encode the behavior we want our agent to exhibit in
  production" and function as "the 'training data' for harness engineering."
- **Our assessment**: This is the most powerful reframe in the post. It
  explicitly imports the discipline of ML data curation — with all its
  associated best practices around quality, balance, and coverage — into agent
  engineering. The implication is that time invested in designing and curating
  evals is the same kind of leverage as investing in high-quality training data:
  you get back what you put in. This reframe also explains why poorly-designed
  evals produce harnesses that look good on evals but fail in production: the
  same way a biased training set produces a biased model.

### Claim 2: Harness improvement is a compound system extending beyond the optimization algorithm — it requires eval sourcing, experiment design, overfitting prevention, and manual acceptance checks

- **Evidence**: The post enumerates the pipeline explicitly: data sourcing →
  experiment design → optimization → review & acceptance. Each stage is described
  in its own section, with the argument that teams who focus only on the
  optimization loop and neglect the surrounding system will fail to generalize.
- **Confidence**: emerging (well-argued structural claim from a practitioner team;
  not a controlled study)
- **Quote**: (no direct quote capturing this exactly; see paraphrase in Our
  assessment)
- **Our assessment**: This claim is the structural insight that separates Better-
  Harness from naive prompt-hill-climbing. Pure prompt iteration can raise eval
  scores by overfitting. The compound system adds the controls (holdout sets,
  human review) that prevent optimization from gaming the signal. The reference
  to Meta-Harness (Stanford) and Auto-Harness (DeepMind) as prior formal work
  situates this as applied engineering catching up with the emerging research
  landscape on automated harness optimization.

### Claim 3: Three eval sourcing strategies have distinct trade-offs: hand-curated (high quality, low scale), production traces (high scale, requires mining), external datasets (requires curation to confirm relevance)

- **Evidence**: Three sourcing approaches are named and described with their
  scaling characteristics and caveats. Production traces are highlighted as the
  highest-throughput channel once an agent is deployed.
- **Confidence**: emerging (practitioner guidance; trade-offs are stated without
  quantification)
- **Quote (on production traces)**: "Every agent interaction generates a trace
  where failures become eval cases."
- **Quote (on hand-curated)**: "manually write examples that capture what we
  think the agent should do"
- **Our assessment**: The three-channel sourcing strategy is the practical "how
  to build your eval suite" answer that complements the "why evals matter"
  framing. Production traces as a feedback signal — particularly when paired
  with direct user reports via channels like Slack with trace links — is the
  most scalable path post-launch. The post explicitly endorses "agent dogfooding
  with visible feedback sharing" as a mechanism to accelerate failure-case
  discovery.

### Claim 4: Tagging every eval by behavioral category (e.g., "tool selection," "multi-step reasoning") enables targeted experiments, holdout set design, and cost reduction through eval subset execution

- **Evidence**: Described as a design discipline that pays dividends throughout
  the optimization loop: tags determine which holdout set an eval belongs to,
  enable targeted diagnosis when a category degrades, and allow running only
  the relevant subset for a given experiment.
- **Confidence**: emerging (practitioner pattern; cost reduction claim is
  plausible but not quantified)
- **Quote**: "Every eval gets tagged to behavioral categories"
- **Our assessment**: Tagging is the connective tissue of the entire Better-
  Harness system. Without tags, all evals look the same — you can't build
  meaningful holdout sets, can't diagnose which behavior category degraded, and
  can't run targeted experiments. The cost-reduction benefit (running only the
  relevant eval subset) is practically important for teams whose full eval suite
  is expensive to run. The post recommends also removing "saturated or obsolete
  evaluations" regularly — evals that the agent passes trivially or that no
  longer reflect desired behavior should be retired.

### Claim 5: Quality beats quantity in eval design — a small, well-tagged eval set covering the behaviors that matter outperforms thousands of noisy, high-coverage evals

- **Evidence**: Stated as a design principle with the rationale that noisy evals
  produce a misleading optimization target; the optimizer will find ways to pass
  noisy evals that don't reflect genuine capability improvement.
- **Confidence**: emerging (stated principle; consistent with ML data-quality
  best practices but not empirically validated against a size-vs-quality
  comparison in the agent context specifically)
- **Quote**: "Quality > quantity, a small set of well-tagged evals covering the
  behaviors you care about beats thousands of noisy but high-coverage evals."
- **Our assessment**: This directly corroborates the practitioner consensus in
  the corpus. The blog-langchain-human-judgment-improvement-loop note documents
  the same finding (Claim 12: "Evaluations can be useful running on just a few
  hundred examples if they're chosen carefully"). The underlying mechanism is
  the same: eval quality determines the fidelity of the optimization signal.
  This should push back against teams that feel they need large datasets before
  they can do any eval-driven improvement work.

### Claim 6: Agents will overfit to visible evals ("agents are famous cheaters") — holdout sets are necessary as a proxy for true generalization

- **Evidence**: The post names this failure mode explicitly and treats it as a
  structural property of any hill-climbing system with a fixed visible objective.
  The standard ML mitigation (train/test split) is applied directly: optimization
  sets drive changes; holdout sets validate that changes generalize.
- **Confidence**: emerging (named failure mode with stated mechanism; the
  analogy to reward hacking in RL is strong; empirical demonstration not
  provided in this post)
- **Quote**: "agents are famous cheaters" and "Holdout sets become a proxy for
  true generalization."
- **Our assessment**: This is the single most important safety principle in the
  post. Without holdout sets, an autonomous harness optimizer can improve eval
  scores by writing increasingly specific instructions that happen to pass the
  visible tests — including generating instructions that essentially hard-code
  responses to specific eval inputs. The holdout set is the only structural check
  against this. Notably, the post acknowledges that "Prompting prevents
  overfitting imperfectly" — even with prompting the optimizer to generalize,
  you still need holdout validation. The structural check cannot be replaced by
  a prompt.

### Claim 7: The Better-Harness recipe has six steps: source & tag evals → split into optimization/holdout sets per category → run a baseline → optimize (diagnose + experiment) → validate (check improvements and regressions) → human review

- **Evidence**: Explicit numbered recipe in the post with rationale for each
  step. The human review step specifically is framed as a check for
  overfitting-to-optimization-set cases that the holdout set might not catch.
- **Confidence**: emerging (recipe from a practitioner team; the structure is
  logical and internally consistent)
- **Quote**: (the six steps are named in the source; no single quote captures
  all six — see Concrete Artifacts for the full structured artifact)
- **Our assessment**: The recipe is the operational center of the post. The
  splitting step (step 2) is the key structural decision — it is the point at
  which the ML train/test discipline is applied to agent eval design. The
  validate step (step 5) explicitly checks for regressions before accepting any
  improvement, closing the "improve one thing, break another" failure mode. The
  human review step (step 6) is the final gate: even after all automated
  checks pass, a human reviews to catch instructions that overfit the
  optimization set in ways holdout validation missed.

### Claim 8: Prompt and instruction updates are the most frequent harness modification discovered by the optimization loop; tool description updates (usage examples, chaining instructions, disambiguation) are the second category

- **Evidence**: Named as the two primary types of harness change discovered in
  practice, with reasoning about why they are common: agents misinterpret tool
  output formats, call tools too aggressively, or fail to chain tools correctly.
- **Confidence**: emerging (observation from the authors' own use of
  Better-Harness; no frequency data published)
- **Quote**: "Most frequent modifications. Agents misinterpret tool output
  formats or overly aggressively call tools when clarification is warranted."
- **Our assessment**: This taxonomy of harness change types (prompt changes vs.
  tool description changes) is actionable for practitioners designing their own
  optimization loops. It also tells you what to look for in diagnosis: when
  an eval category degrades, first check whether the agent is misinterpreting
  a tool output format or over-using a tool unnecessarily — those are the
  failure modes most frequently addressable via instruction or description
  updates. The post notes that "scope to single modifications" (one change at
  a time) avoids confounding, though it also notes that simultaneous prompt and
  tool updates are sometimes necessary for system functionality.

### Claim 9: The experiment on Claude Sonnet 4.6 and GLM-5 discovered four concrete cross-model instruction improvements from the hill-climbing loop, addressing redundant questioning, overbroad tool use, and domain-first ordering

- **Evidence**: A results table in the post documents four specific shared
  harness changes discovered by the loop, each with the evaluation categories
  they affected, the models they applied to, the exact instruction added, and
  the observed effect on eval scores.
- **Confidence**: anecdotal (first-party experimental results; no holdout-set
  score comparison provided in the excerpt; no statistical significance reported)
- **Quote (table instruction strings)**:
  - "Use reasonable defaults when the request clearly implies them"
  - "Do not ask for details the user already supplied"
  - "Do not keep issuing near-duplicate searches once you have enough
    information"
  - "Ask domain-defining questions before implementation questions"
- **Our assessment**: These four instruction strings are the most concrete
  artifact in the post: they are actual prompt additions that the optimization
  loop discovered and validated. Their cross-model applicability (Sonnet 4.6
  and GLM-5 both benefited from most of them) is noteworthy — it suggests these
  are addressing fundamental agent failure modes rather than model-specific
  quirks. The instruction strings themselves are reusable starting points for
  practitioners experiencing similar failure modes in their own agents. The
  "domain-defining questions first" finding aligns with the enterprise agent
  design principle that domain context must be established before implementation
  questions, corroborating blog-langchain-human-judgment-improvement-loop
  Claim 1.

### Claim 10: Human review before production deployment is essential — the automated loop can surface instructions that game the optimization set without generalizing, and these may pass holdout validation but fail on production edge cases

- **Evidence**: Explicitly stated as the sixth step with the rationale that
  automated checks are not sufficient: "This identifies instructions overfitting
  optimization sets and wasting tokens despite maintaining generalization."
- **Confidence**: emerging (practitioner guidance; the failure mode described
  is plausible and consistent with the "agents are famous cheaters" principle)
- **Quote**: (no single direct quote captures this exactly; see paraphrase in
  Our assessment)
- **Our assessment**: The inclusion of human review as a structural step (not
  just a best-practice recommendation) reflects the authors' experience that
  automated validation can be gamed. Instructions that pass both optimization
  and holdout sets may still be wasteful (consuming tokens unnecessarily) or
  brittle (passing eval distributions but failing on production-specific edge
  cases not represented in either set). Human review is the heuristic check
  that catches these cases. This is consistent with blog-langchain-human-judgment-
  improvement-loop Claim 5 ("human time invested in manual review of agent
  outputs scales poorly") — the LangChain model is not "review everything" but
  "review only the proposed harness changes before acceptance."

### Claim 11: Evaluation suites should be pruned ("spring cleaned") regularly — evals that the agent now handles trivially, or that reflect outdated behavior priorities, should be retired rather than accumulated

- **Evidence**: Stated as an explicit maintenance principle, with two reasons
  given for retiring evals: (1) model capability advancement (the agent now
  handles this case reliably without a specific instruction), (2) changed agent
  behavior priorities (what we want the agent to do has shifted).
- **Confidence**: emerging (practitioner principle; consistent with the general
  ML practice of refreshing training/test sets)
- **Quote**: "We regularly assess whether an eval is still useful because of
  more intelligent models or a different behavior we want for the agent."
- **Our assessment**: This is a counterweight to the natural accumulation
  tendency. Teams tend to add evals but rarely remove them; saturated evals
  (ones the agent passes trivially every time) consume compute and dilute the
  signal-to-noise ratio of the suite. Retiring them keeps the optimization
  signal meaningful. The two retirement criteria are also useful as diagnostic
  signals: if a large fraction of your evals are always-passing, your suite
  is not capturing the frontier of where the agent struggles.

### Claim 12: Evaluations become regression tests — once the agent handles a case correctly, the eval prevents future harness changes from regressing that behavior

- **Evidence**: Stated as the eval-lifecycle principle: evals begin as
  optimization targets and, once satisfied, become regression guards. The TDD
  (Test-Driven Development) analogy in traditional software engineering is
  explicitly invoked.
- **Confidence**: emerging (conceptual principle; consistent with the TDD
  analogy; not independently validated)
- **Quote**: "Once our agent handles a case correctly, we don't want to lose
  that gain. The eval becomes a regression test."
- **Our assessment**: The TDD analogy is apt and practically useful. In
  traditional software, tests start as specifications and become regression
  tests on merge. In agent development, evals start as improvement targets and
  become regression guards as the harness matures. The difference is that
  regressions are more likely in agent development (because harness changes can
  have unexpected downstream effects across behavioral categories) and harder to
  detect (because the agent's behavior is not deterministic). The eval-as-
  regression-test principle, combined with the holdout-set design, means Better-
  Harness accumulates value over time: each solved case adds a permanent guard.

### Claim 13: Traces are the highest-density feedback signal for future automated eval generation — the ideal future state is continuous trace monitoring, automatic failure clustering, and eval generation from production error traces

- **Evidence**: The "Future" section of the post describes a flywheel where
  increasing usage generates more traces, which generate more evals, which
  improve harnesses, which serve more users. Specific future capabilities named:
  automatically classifying and clustering production failures; generating evals
  from user-corrected traces (highest quality); cross-version harness comparison
  via trace diff.
- **Confidence**: anecdotal (forward-looking; not yet implemented as described;
  labeled as "future direction")
- **Quote**: (no direct quote for the flywheel concept; consistent with the
  general LangSmith tracing infrastructure being positioned as the enabling
  platform)
- **Our assessment**: The flywheel direction is consistent with the LangChain
  product roadmap (LangSmith traces are the enabling infrastructure) but
  represents aspirational rather than current capability. The strongest element
  is the "user-corrected traces prove superior" principle: when a user corrects
  an agent's output and the corrected trace is captured, that is a highest-
  quality training example for both eval generation and harness improvement.
  This extends the blog-langchain-human-judgment-improvement-loop corpus
  (Claim 11: production data is the best source of test cases after launch) by
  naming user-correction traces specifically as the highest-quality subset.

## Concrete Artifacts

### Better-Harness Six-Step Recipe

```
# Better-Harness hill-climbing recipe
# Source: "Better Harness," Vivek Trivedy, LangChain (2026-04-08)

Step 1 — Source and tag evals
  Combine: hand-written evals + production trace mining + external datasets
  Required: tag each eval by behavioral category (e.g., "tool_selection",
            "multi-step_reasoning", "followup_quality")
  Ongoing: remove saturated or obsolete evals regularly

Step 2 — Split data per category
  Create: Optimization set (drives harness changes)
          Holdout set (validates generalization per category)
  Critical: autonomous hill-climbing tends toward overfitting;
            holdout set is the only structural check

Step 3 — Run a Baseline
  Run on both Optimization AND Holdout sets before any modification
  Purpose: ground all subsequent comparisons

Step 4 — Optimize (each iteration)
  Diagnose: read traces; per-category scores show where to look;
            traces reveal specific failure details
  Experiment: target single modifications to avoid confounding;
              but simultaneous prompt + tool updates are sometimes
              needed for system functionality

Step 5 — Validate
  Check: proposed change improves optimization-set scores
  Check: no regressions in previously-passing cases
  On regression: agent receives regression context for next iteration
                 (no loss of prior gains)

Step 6 — Human review
  Manual: inspect proposed changes for edge-case overfitting
  Watch for: instructions that pass optimization + holdout but waste
             tokens or game eval distributions
  Gate: changes require human acceptance before production deployment
```

### Harness Change Type Taxonomy

```
# Two primary harness change types discovered by Better-Harness
# Source: "Better Harness," Vivek Trivedy, LangChain (2026-04-08)

TYPE 1 — Prompt / Instruction Updates
  Frequency: most common
  Root causes:
    - Agent misinterprets tool output formats
    - Agent calls tools too aggressively when clarification is needed
  Fix pattern: targeted instruction additions (single-purpose, scoped)
  Example: "when querying multiple dependent-information files, offload
            to filesystem and re-aggregate before delivering final responses"

TYPE 2 — Tool / Description Updates
  Root causes:
    - Agent misjudges tool application context
    - Agent doesn't chain tools correctly
  Fix components:
    - Usage examples
    - Chaining instructions
    - Updated descriptions
    - Suite disambiguation (when multiple tools serve similar purposes)
```

### Experiment Results Table (Claude Sonnet 4.6 and GLM-5)

```
# Results from Better-Harness experiment
# Source: "Better Harness," Vivek Trivedy, LangChain (2026-04-08)
# Models tested: Claude Sonnet 4.6, Z.ai GLM-5

Shared Change             | Tasks Observed In                      | Models
--------------------------+----------------------------------------+----------------
Use reasonable defaults   | tool_indirect_email_report             | Sonnet 4.6, GLM-5
  Instruction: "Use reasonable defaults when the request clearly implies them"
  Effect: Agents stopped blocking on trivial wording; action-taking evals
          completed more reliably.

Respect already-fixed     | followup_vague_send_report,            | Sonnet 4.6, GLM-5
constraints               | followup_detailed_calendar_brief       |
  Instruction: "Do not ask for details the user already supplied"
  Effect: Recurring-task followup evals stopped failing on redundant questions.

Bound exploration         | tool_chain_search_then_email           | Mostly GLM-5
before acting
  Instruction: "Do not keep issuing near-duplicate searches once you have
                enough information"
  Effect: Search-then-deliver evals became substantially more reliable without
          looping.

Ask domain-defining       | followup_vague_customer_support,       | Sonnet 4.6, GLM-5
questions first           | followup_vague_monitor_system          |
  Instruction: "Ask domain-defining questions before implementation questions"
  Effect: For evals with new injected tools (e.g., search-then-email), loop
          discovered superior composition descriptions. Particularly promising
          for vertical agents adapting to task-specific context.
```

### Eval Lifecycle Model

```
# Eval lifecycle in Better-Harness
# Source: "Better Harness," Vivek Trivedy, LangChain (2026-04-08)

Phase 1 — Active target
  Status: agent fails this eval or handles it unreliably
  Role: optimization target; drives harness changes

Phase 2 — Regression test
  Status: agent handles correctly after a harness change
  Role: regression guard; new changes must not break this
  Trigger: "Once our agent handles a case correctly, we don't want to
            lose that gain. The eval becomes a regression test."

Phase 3 — Retirement candidate
  Status: agent passes trivially on every run (saturated)
  OR: eval reflects a behavior priority that has since changed
  Action: retire the eval; do not let it dilute the suite's signal
  Trigger: "We regularly assess whether an eval is still useful because
            of more intelligent models or a different behavior we want
            for the agent."
```

## Cross-References

- **Corroborates**:
  - **blog-langchain-human-judgment-improvement-loop** (Claim 11): "After launch,
    you gain access to a much better source of test cases: real production data."
    — This source's production-traces sourcing strategy (Claim 3 here) is the
    concrete implementation of that principle, adding the specific mechanism
    (mining failures from traces) and recommended infrastructure (trace links
    via Slack dogfooding).
  - **blog-langchain-human-judgment-improvement-loop** (Claim 12):
    "Evaluations can be useful running on just a few hundred examples if they're
    chosen carefully" — directly corroborated by this source's Claim 5
    ("Quality > quantity"). Both sources are from LangChain and represent
    practitioner consensus on the same principle.
  - **blog-anthropic-harness-long-running** (Claim 6): "Claude is a poor QA agent
    out of the box" — both sources converge on the need for iterative evaluation
    tuning. The Anthropic post documents the failure mode (evaluators rationalize
    away bugs); this post documents the structural fix (holdout sets + human
    review as final gate). They approach the same problem from different angles.
  - **blog-cursor-continual-harness-improvement** (Claim 5): "Any unknown error
    represents a bug in the harness" — analogous philosophy: Cursor treats
    unclassified tool errors as bugs requiring remediation; Better-Harness treats
    harness changes that fail human review as blocked from production. Both
    reflect the same principle of never letting unchecked degradation into
    production.

- **Extends**:
  - **blog-langchain-human-judgment-improvement-loop**: That post covers the
    full agent improvement flywheel with human-expert calibration of evaluators.
    This source is a companion piece (same blog series, April 2026) that covers
    the automated harness-optimization layer within that flywheel. Together they
    describe the full system: human experts calibrate evaluators → Better-Harness
    uses those evaluators to autonomously hill-climb on the harness → human review
    gates production deployment.
  - **blog-cursor-continual-harness-improvement** (Claim 12): Cursor's static-to-
    dynamic context evolution is the Cursor-side manifestation of continuous
    harness improvement. Better-Harness provides the explicit methodology (recipe,
    overfitting controls, regression tracking) for how that continuous improvement
    process should be structured. The Cursor post shows what it looks like at
    production scale; Better-Harness provides the scaffolding to do it.
  - **blog-anthropic-harness-long-running** (Claim 9): "Every component in a
    harness encodes an assumption about what the model can't do on its own" —
    Better-Harness operationalizes the practice of stress-testing those
    assumptions via evals: when a harness change passes both optimization and
    holdout validation AND human review, it represents confirmed evidence that
    the change improves generalization. This is the systematic version of the
    "re-examine and prune" practice from that post.

- **Contradicts**: None found. The holdout-set/overfitting-prevention framing
  is new to the corpus but does not contradict any existing source. The emphasis
  on human review (Claim 10) is consistent with blog-langchain-human-judgment-
  improvement-loop's position on human judgment in the improvement loop.

- **Novel**:
  - **ML train/test split applied to harness optimization as a named principle**:
    No existing source note describes the explicit application of holdout set
    design to prevent harness overfitting. blog-langchain-human-judgment-
    improvement-loop mentions golden datasets and annotation queues, but the
    optimization-set / holdout-set distinction as an overfitting control is
    introduced here for the first time in the corpus.
  - **"Agents are famous cheaters" as a named principle for evaluation design**:
    The specific failure mode — agents overfitting their behavior to visible
    eval distributions — is named here with an memorable label. No other corpus
    source names or describes this failure mode in the context of iterative
    harness improvement (as distinct from model training).
  - **Eval lifecycle model (target → regression test → retirement)**:
    The three-phase lifecycle (optimization target → regression guard → retirement
    candidate) is a structured framework for managing eval suite health not
    described elsewhere in the corpus. The retirement criterion (trivially-passing
    evals should be removed) directly counters the accumulation tendency.
  - **Four cross-model instruction improvements with exact instruction strings**:
    The Concrete Artifacts table is the most directly reusable artifact in the
    corpus for practitioners experiencing the named failure modes (over-asking,
    redundant searches, implementation-before-domain questions). No other source
    provides this level of concrete, copy-pasteable instruction guidance with
    experimental corroboration.
  - **The compound system framing** (sourcing → experiment design → optimization
    → acceptance) positions harness hill-climbing as requiring all four stages,
    not just the optimization algorithm. This is the clearest statement in the
    corpus that "just run an optimizer on your prompts" is insufficient without
    the surrounding system.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the Better-Harness recipe as the
  recommended structured methodology for iterative harness improvement. Currently
  the chapter covers what to engineer in a harness; this source provides the
  *how to improve it over time* methodology. Specifically:
  - Add the eval-as-training-data reframe (Claim 1) as the conceptual foundation
    for why eval design is as important as harness design.
  - Add the optimization-set / holdout-set split (Claim 6, Claim 7 step 2) as a
    structural requirement for any autonomous or semi-autonomous harness
    improvement system. The guide should explicitly warn against eval-score
    optimization without a holdout set.
  - Add the prompt-update / tool-description-update taxonomy (Claim 8) as the
    primary categories practitioners should target in diagnosis.
  - Add the four cross-model instruction strings from the experiment table
    (Claim 9) as concrete starting points for practitioners experiencing the
    same failure modes (over-asking, overbroad searches, wrong question ordering).

- **Chapter 03 (Safety and Verification)**: Add Claim 12 (evals as regression
  tests) to complement the golden dataset pattern from blog-langchain-human-
  judgment-improvement-loop. The eval lifecycle model (Claim 12 + eval
  retirement from Claim 11) should be the named framework for how eval suites
  should evolve: grow when new failure modes are found, and prune when cases
  are trivially satisfied or priorities shift.

- **Chapter 03 (Safety and Verification)**: Add Claim 10 (human review as a
  final gate on autonomous harness changes) as a safety principle alongside the
  existing corpus of human-in-the-loop patterns. The specific risk named — an
  optimizer generating instructions that pass all automated checks but overfit
  the observable eval distributions — is the agent-development analog of an ML
  model overfitting the test set. The guide should name this risk and recommend
  human review as the structural mitigation.

- **Chapter 03 (Safety and Verification) — cross-reference with Ch02**: The
  "agents are famous cheaters" claim (Claim 6) should be cited in both the
  harness engineering and safety chapters as the motivation for why holdout
  sets are structural requirements, not nice-to-haves, in any autonomous
  improvement system.

## Extraction Notes

- The source URL `blog.langchain.com/better-harness-...` redirects to
  `www.langchain.com/blog/better-harness-...`. The canonical URL is the
  www.langchain.com form. Multiple WebFetch attempts were made to extract
  verbatim text; because the tool processes HTML via a small model, quotes
  were cross-validated across multiple fetches. Claims where quotes were
  inconsistent across fetches use `(no direct quote; see paraphrase in Our
  assessment)` rather than a potentially-reconstructed quote.
- The article references an open-sourced research implementation of Better-
  Harness but does not provide a direct link in the extractable content.
- The results table (Claim 9, Concrete Artifacts) is the highest-confidence
  artifact in the post: the specific instruction strings (e.g., "Do not ask for
  details the user already supplied") appear consistently across multiple fetches
  and are plausibly verbatim table cell contents.
- LangSmith is referenced as the enabling observability platform (trace
  generation, eval running). All patterns are described in terms of principles
  that are platform-agnostic; the LangSmith dependency is implementation detail,
  not a structural requirement of the Better-Harness methodology.
- This post is part of a connected April 2026 LangChain blog series:
  - "Better Harness" (this source, April 8, 2026) — harness hill-climbing
  - "Human judgment in the agent improvement loop" (April 9, 2026,
    issue #108) — human review and evaluator calibration
  - "The agent improvement loop starts with a trace" (April 2026) — trace
    infrastructure as the foundation
  The three posts form a coherent guide to the full agent improvement system.
  The companion notes (blog-langchain-human-judgment-improvement-loop) should
  be read alongside this one.
- No contradictions filed: the holdout-set overfitting concern is new to the
  corpus but does not contradict any existing claim.
