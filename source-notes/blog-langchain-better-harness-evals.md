---
source_url: https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals
source_type: blog-post
title: "Better Harness: A Recipe for Harness Hill-Climbing with Evals"
author: Vivek Trivedy (LangChain)
date_published: 2026-04-08
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#107"
---

# Better Harness: A Recipe for Harness Hill-Climbing with Evals

> LangChain's operational system for autonomously improving agent harnesses using
> evals as a hill-climbing signal — presenting the evals-as-training-data analogy,
> a three-tier sourcing strategy, mandatory holdout set design against agent overfitting,
> and a human review gate that together constitute a repeatable harness improvement loop.

## Source Context

- **Type**: blog-post (LangChain engineering blog, April 8, 2026)
- **Author credibility**: Vivek Trivedy writing from inside LangChain, which builds and
  operates production agent orchestration infrastructure used by many enterprises.
  LangSmith (LangChain's tracing product) is the specific implementation substrate
  for this system. The post references real experiments on Claude Sonnet 4.6 and GLM-5
  with a "subset of our evals," suggesting first-hand operational experience rather than
  purely theoretical framing. A research version of Better-Harness is open-sourced,
  indicating production-level engineering maturity. Treat as emerging: directionally
  strong from a credible practitioner, but no independent audit of their results.
- **Scope**: Covers the full Better-Harness pipeline for autonomous harness improvement:
  sourcing and tagging evals, train/holdout split design, the optimization loop, example
  harness changes (prompt updates, tool description updates), regression protection, and
  a forward-looking section on trace-driven automated error detection. Does NOT cover
  model architecture, agent memory, multi-agent coordination, or tool implementation.
  Does NOT provide numerical scores for the experiments — describes results qualitatively
  and by example.

## Extracted Claims

### Claim 1: Evals serve the same role for agent harness engineering that training data serves in classical ML — each eval contributes a learning signal that guides the next harness edit

- **Evidence**: Explicit analogy from the author. The parallel is: in classical ML,
  training data provides gradients that update model weights; in harness engineering,
  eval cases provide "did the agent take the right action" signals that guide the next
  proposed harness edit. The analogy is the stated design principle for the entire
  Better-Harness system.
- **Confidence**: emerging (reasoned analogy from a practitioner; the structural parallel
  is sound but the behavioral equivalence — harness edits as discrete steps like gradient
  descent — depends on how well the optimization loop actually converges)
- **Quote**: "Evals encode the behavior we want our agent to exhibit in production. They're
  the 'training data' for harness engineering. Each eval case contributes a signal like 'did
  the agent take the right action' or 'produce the right outcome?'"
- **Our assessment**: The analogy is apt and pedagogically useful. Classical ML practitioners
  building agent systems should recognize this framing immediately: data quality discipline
  that makes ML training work (curation, labeling, coverage, train/test splits) applies
  equally to harness improvement. The implication is that teams who skip eval investment
  are analogous to teams who skip training data quality — the optimization loop has no
  reliable signal to climb. This is the clearest articulation in our corpus of why evals
  are not just a testing tool but a development infrastructure.

### Claim 2: Better-Harness is a compound system — the update algorithm is not the hard part; sourcing, splitting, validation, and human review are what make autonomous improvement work in practice

- **Evidence**: Author explicitly positions Better-Harness as going "beyond the update
  algorithm" and describes the full pipeline: data sourcing → experiment design →
  optimization → review & acceptance. References existing academic work (Meta-Harness
  from Stanford, Auto-Harness from DeepMind) that formalizes the optimization step but
  does not cover the surrounding system.
- **Confidence**: emerging (practitioner claim; references to academic work confirm the
  optimization algorithm is an active research area; the "compound system" framing is
  the author's operational observation)
- **Quote**: "Better-Harness is a take on compound systems engineering."
- **Our assessment**: This is the most important framing claim in the post. It explains
  why teams that implement only the "optimize the prompt automatically" step fail at
  autonomous harness improvement: they have the least important piece. The hard parts are
  sourcing enough high-quality evals, preventing overfitting, and reviewing outputs for
  production safety. This aligns with how Cursor frames their harness improvement work in
  `blog-cursor-continual-harness-improvement.md` — the measurement infrastructure
  (Keep Rate, LLM-as-judge, anomaly detection) is described as more operationally
  significant than the optimization step itself.

### Claim 3: Production trace mining is the highest-leverage, highest-throughput eval sourcing strategy — hand-curated evals are high quality but don't scale, external datasets need curation

- **Evidence**: Author describes three sourcing approaches and explicitly grades their
  leverage: hand-curated ("high value, but difficult to generate at scale"), production
  traces ("the leverage, high-throughput way"), external datasets ("useful but need to
  be manually curated"). Production trace mining is further described with a specific
  operational detail: team members report agent errors directly in Slack with a trace link,
  which becomes eval material.
- **Confidence**: emerging (author's operational experience; the leverage claim is
  directional, not quantified)
- **Quote**: "Mining traces for eval material is the leverage, high-throughput way to
  improve evals over time."
- **Our assessment**: The Slack-to-trace-to-eval pipeline described here is a lightweight
  version of Cursor's Cursor Blame approach (production committed code → traced back to
  agent request → eval case). Both converge on the same structural insight: production
  failures are the highest-signal eval sourcing material because they reflect real
  distribution. The specific recommendation to "dogfood agents and directly share
  feedback for everyone to see" builds shared knowledge of agent behavior while
  simultaneously generating eval material. This is an operationally useful practice for
  any team running internal agents.

### Claim 4: Tagging every eval to behavioral categories enables targeted experiments and significant cost savings by allowing subset execution

- **Evidence**: Author states this as an operational necessity discovered in practice:
  "Tags enable meaningful holdout sets and targeted experiments. It also saves a lot of
  money because we can run subsets of evals." The tag examples given are "tool selection,"
  "multi-step reasoning."
- **Confidence**: emerging (operational claim; the cost-saving mechanism is straightforward
  — running a subset is cheaper than the full suite — but "a lot of money" is unquantified)
- **Quote**: "Tag everything. Every eval gets tagged to behavioral categories: 'tool
  selection,' 'multi-step reasoning,' etc. Tags enable meaningful holdout sets and targeted
  experiments. It also saves a lot of money because we can run subsets of evals."
- **Our assessment**: The tagging requirement is often skipped in early-stage eval suites.
  This claim establishes it as both a quality mechanism (enables meaningful holdout splits
  by behavior category, not just random splits) and an economic mechanism (can target
  specific behavioral categories without running the full suite). The combination of
  behavioral categorization and subset execution is a mature eval-infrastructure practice
  that scales better than a single-pool eval corpus.

### Claim 5: Agents notoriously overfit to eval scores — autonomous hill-climbing systems exploit the reward signal, making holdout sets a mandatory architectural requirement, not an optional best practice

- **Evidence**: Author names this explicitly: "Agents are famous cheaters." The mechanism
  described is standard reward hacking: the agent's structure overfits to make existing
  evals pass without acquiring the underlying capability, because "the loop just wants to
  'make number go up' and doesn't know about generalization."
- **Confidence**: emerging (claim applies a known ML failure mode to harness optimization
  specifically; the generalization from model training to harness editing is conceptually
  sound; independently corroborated by Cursor's real-time RL post which documents two
  named reward hacking incidents in production)
- **Quote**: "Agents are famous cheaters...any learning system is prone to reward hacking
  where the agent overfits its structure to make the existing evals pass that it can see."
- **Our assessment**: This is the sharpest risk warning in the post. A team that
  implements the optimization loop without holdout sets will see scores climb while actual
  production quality stagnates or degrades. The agent (or the optimization loop operating
  on behalf of the agent) finds prompt additions that trick the eval into passing without
  generalizing. This is identical to ML train-set overfitting: impressive training accuracy
  hiding poor generalization. For the guide: any autonomous harness improvement workflow
  must include holdout sets — this is not optional.

### Claim 6: Holdout sets must match the general distribution of the optimization set — they function as a proxy for production generalization, not just a technical split requirement

- **Evidence**: Author states the design constraint explicitly: the holdout distribution
  "should match existing evals. This mirrors what production will look like." The holdout
  set's purpose is generalization validation, and a mismatched distribution produces false
  confidence.
- **Confidence**: emerging (author's operational design reasoning; standard train/test
  split theory applied to the harness improvement context)
- **Quote**: "autonomouos hill-climbing has a tendency to overfit to tasks so holdout sets
  ensure that learned optimizations work on previously unseen data, though the general
  distirbution should match existing evals. This mirrors what production will look like."
- **Our assessment**: The distribution-matching requirement is easy to overlook. A naive
  holdout split — take any 20% of evals and call them holdout — may not represent the
  behavioral distribution you actually care about in production. The behavioral tagging
  system (Claim 4) is what enables meaningful distribution-matched holdout splits:
  you can stratify by tag to ensure the holdout covers the same behavioral categories as
  the optimization set, proportionally.

### Claim 7: Human review is an essential gate in autonomous harness improvement — specifically to catch overfit instructions that pass automated metrics but waste tokens in production

- **Evidence**: Author describes this as the sixth step in the Better-Harness pipeline:
  "We manually review changes and edge cases metrics miss. This often includes instructions
  that are overfit to the optimization set and although they don't hurt generalization,
  they end up being a waste of tokens."
- **Confidence**: emerging (author's operational practice; the "waste of tokens" failure
  mode for overfit instructions is plausible and specific)
- **Quote**: "This often includes instructions that are overfit to the optimization set
  and although they don't hurt generalization, they end up being a waste of tokens."
- **Our assessment**: This is an under-appreciated failure mode. An instruction might pass
  the holdout set (because it doesn't actively hurt generalization) while still being
  unhelpful — it's just specific enough to pass the optimization evals without adding
  general value. The holdout set catches instructions that actively hurt; human review
  catches instructions that are merely wasteful. The two mechanisms are complementary
  quality gates: automated for regression detection, human for efficiency and alignment
  review. This is consistent with `blog-cursor-continual-harness-improvement.md`'s
  approach of pairing automated anomaly detection with manual investigation for degradations.

### Claim 8: The most common harness change discovered by the optimization loop is a targeted instruction addition — a specific behavioral constraint addressing a diagnosed failure mode

- **Evidence**: Author describes the categories of harness changes the loop can discover,
  naming prompt/instruction updates as "the most common change" and providing an example:
  "when querying multiple files that have dependent information, offload information to the
  filesystem and re-aggregate before giving a final answer." A second type is tool
  description updates for disambiguation.
- **Confidence**: emerging (author's operational observation; "most common" is not
  quantified)
- **Quote**: "The most common change. The agent keeps misinterpreting a tool's output
  format, or it's too aggressive about calling a tool when it should ask a clarifying
  question first. The fix is a targeted instruction update addition"
- **Our assessment**: The "targeted instruction addition" as the primary output of
  harness hill-climbing is consistent with the practitioner experience that system prompts
  accumulate behavioral constraints over time. Better-Harness provides a systematic
  mechanism for discovering which constraints are needed (by diagnosing eval failures) and
  validating them (by checking holdout generalization) rather than adding constraints
  reactively. This positions the harness as an evolving behavioral specification, not a
  fixed document.

### Claim 9: Specific instruction additions showed cross-model generalization — the same instructions improved both Claude Sonnet 4.6 and GLM-5 on the same behavioral categories

- **Evidence**: Results table showing four shared harness changes, each with "Models:
  Sonnet, GLM-5" attribution, indicating the same instruction addition fixed the same
  failure mode across both models. The categories were `tool_selection` and
  `followup_quality`.
- **Confidence**: anecdotal (single experiment on a "small representative sample" from
  the authors' eval suite; sample size not published)
- **Quote**: (no direct quote; implied by the shared-change table structure with
  "Models: Sonnet, GLM-5" columns)
- **Our assessment**: The cross-model generalization finding is practically significant.
  It suggests that some harness instructions address behavioral failure modes that are
  shared across model families, not idiosyncratic to a specific model's training. This
  is relevant for teams that run multi-model harnesses: some harness improvements may
  transfer, reducing the per-model maintenance burden. However, the sample is small and
  the author explicitly notes other work is underway to generalize Better-Harness "across
  many models...using a bigger eval suite."

### Claim 10: Evals should function as regression tests — protecting previously acquired correct behaviors against future degradation

- **Evidence**: Author explicitly draws the TDD analogy: "Once our agent handles a case
  correctly, we don't want to lose that gain. The eval becomes a regression test. This is
  similar to ideas in traditional software engineering like Test Driven Development (TDD)."
  A subset of evals is designated as always-pass; failures on these trigger suspicion.
- **Confidence**: emerging (author's operational practice; the TDD analogy is pedagogically
  useful and structurally sound)
- **Quote**: "Along with hill climbing, evals also explicitly capture and protect against
  regressions over time. Once our agent handles a case correctly, we don't want to lose
  that gain. The eval becomes a regression test."
- **Our assessment**: This is the clearest articulation in our corpus of evals-as-regression-
  tests rather than evals-as-graders. The behavioral shift is: once an eval passes, it
  transitions from an improvement target to a regression gate. This creates an ever-growing
  floor of guaranteed behaviors, not just a snapshot quality metric. The "look at our run
  suspiciously if these suddenly fail" framing operationalizes this: designated regression
  evals trigger investigation when they fail, not just a score decrement.

### Claim 11: Eval suites should be actively pruned, not grown indefinitely — saturated evals and evals for deprecated behaviors waste compute and may not reflect current model capability

- **Evidence**: Author explicitly states this as an operational principle counter to
  naive eval accumulation: "We don't think our eval suite should grow monotonically,
  spring cleaning of evals is good! We regularly assess whether an eval is still useful
  because of more intelligent models or a different behavior we want for the agent."
- **Confidence**: emerging (author's operational practice; the reasoning is sound given
  that more capable models may "solve" previously-challenging eval categories, making
  those evals uninformative)
- **Quote**: "We don't think our eval suite should grow monotonically, spring cleaning of
  evals is good!"
- **Our assessment**: This is a counter-intuitive recommendation for teams accustomed to
  treating evals as permanent documentation. The argument is that eval suites are
  living behavioral specifications that should track current model capabilities, not
  historical benchmarks. An eval that every model passes trivially no longer discriminates
  and wastes compute. Periodically removing saturated evals and evals for deprecated
  behaviors keeps the suite fast and signal-rich. This connects to
  `blog-anthropic-harness-long-running.md` Claim 9 ("harness components encode
  assumptions about what the model can't do") — saturated evals encode assumptions
  about limitations the current model no longer has.

### Claim 12: The production trace flywheel — more usage creates more traces which become more evals which improve the harness — is the scaling mechanism for long-term harness quality

- **Evidence**: Author explicitly names this as a flywheel: "The flywheel: more usage
  → more traces → more evals → better harness." The implementation uses LangSmith
  for full trace logging, enabling diagnosis, regression detection, and eval mining
  from the same trace corpus.
- **Confidence**: emerging (author's system design; the flywheel mechanism is logical
  but its actual compounding speed is not quantified)
- **Quote**: "The flywheel: more usage → more traces → more evals → better harness"
- **Our assessment**: This is the scaling principle that distinguishes harness improvement
  as a sustainable practice from a one-time setup. The flywheel framing positions early
  tracing investment as a compounding asset: every agent run makes the harness improvement
  system more powerful. Teams that don't log traces can't mine evals from production
  failures; teams that do accumulate an ever-larger training signal. This creates a
  compounding advantage for teams that invest in tracing infrastructure early.

### Claim 13: Dense trace logging infrastructure is the prerequisite that makes automated harness improvement possible — without full traces, there is no diagnostic signal for the optimization loop

- **Evidence**: Author states this directly: "traces give us a dense feedback signal" and
  describes what LangSmith traces enable: "trace-level diagnosis for the optimization loop,
  production monitoring for regression detection, and trace mining for eval generation."
- **Confidence**: emerging (author's operational requirement; the three use cases described
  for traces are concrete and coherent)
- **Quote**: "To facilitate this, all agent runs are logged to LangSmith with full traces.
  This gives us trace-level diagnosis for the optimization loop, production monitoring for
  regression detection, and trace mining for eval generation."
- **Our assessment**: This claim positions tracing not as a debugging nicety but as the
  enabling infrastructure for autonomous harness improvement. Teams that run agents
  without full trace logging cannot do any of the three activities described. The three
  activities (diagnosis, monitoring, mining) are distinct use cases that all depend on
  the same trace corpus, making trace investment triply valuable. For the guide: tracing
  is a prerequisite for any serious harness engineering practice, not an optional observability
  add-on.

## Concrete Artifacts

### Better-Harness Pipeline (Six Steps)

```
# Better-Harness autonomous harness improvement loop (LangChain, April 2026)
# Source: "Better Harness: A Recipe for Harness Hill-Climbing with Evals," Vivek Trivedy

STEP 1: Source and tag evals
  - Hand-curated: high value, hard to scale
  - Production traces: "the leverage, high-throughput way to improve evals over time"
  - External datasets: useful but require curation to reflect desired behaviors
  - Rule: "Tag everything. Every eval gets tagged to behavioral categories"
  - Prune: "We regularly assess whether an eval is still useful"

STEP 2: Split data per category
  - Create Optimization and Holdout sets — "This is very important!"
  - Holdout distribution must match optimization distribution: "mirrors what production will look like"
  - Rationale: "autonomouos hill-climbing has a tendency to overfit to tasks"

STEP 3: Run a Baseline
  - "Run a baseline experiment on the Optimization & Holdout sets before any edits"
  - "Grounds all updates in the update steps"

STEP 4: Optimize (autonomous, with optional human review)
  - Diagnose from traces: "Scores aggregate performance over categories and then
    Traces show the details of what went wrong and why"
  - "Experiment a targeted harness change. We scope to one change at a time to
    avoid confounding"

STEP 5: Validate
  - "The loop checks to make sure that the proposed change helped pass new evals
    while avoiding regressions on existing passing cases"
  - "some change results in a net overall score gain with some regressions"
  - "The agent gets context of these regressions so it can try to fix them in the
    next update without losing the gains from the existing update"

STEP 6: Human review
  - "We manually review changes and edge cases metrics miss"
  - Catches instructions "overfit to the optimization set" that pass holdout but
    "end up being a waste of tokens"
```

### Eval-to-Harness Flywheel

```
# Production trace flywheel (LangChain, April 2026)
# Source: "Better Harness: A Recipe for Harness Hill-Climbing with Evals," Vivek Trivedy

more usage → more traces → more evals → better harness

TRACE INFRASTRUCTURE (LangSmith)
  Provides:
    1. Trace-level diagnosis for the optimization loop
    2. Production monitoring for regression detection
    3. Trace mining for eval generation

  Quote: "Every trace contains valuable data to produce a potential eval.
          And every (good) eval makes the harness better."

OPERATIONAL DETAIL
  - Dogfood agents internally; share Slack errors with trace links → eval cases
  - "A trace where the agent made a mistake is an eval case."
  - "A trace where a user corrected the agent is even better."
```

### Types of Harness Changes Discovered by the Loop

```
# Harness change types (LangChain Better-Harness experiments, April 2026)
# Source: "Better Harness: A Recipe for Harness Hill-Climbing with Evals," Vivek Trivedy

TYPE 1: Prompt/instruction update (most common)
  Example: "when querying multiple files that have dependent information, offload
            information to the filesystem and re-aggregate before giving a final answer."

TYPE 2: Tool or tool description update
  "The agent may fail contextualizing when to use a new tool. Edits include examples
   on of how to use, how to chain this tool, an updated tool description, and editing
   the overall tool suite to disambiguate similar tools"
```

### Cross-Model Instruction Changes (Sonnet 4.6 + GLM-5)

```
# Shared harness changes — effective on both Claude Sonnet 4.6 and GLM-5
# Source: "Better Harness: A Recipe for Harness Hill-Climbing with Evals," Vivek Trivedy
# Experiment: subset of evals, split optimization/holdout, April 2026

Change            | Task category              | Instruction added
---               | ---                        | ---
Use reasonable    | tool_indirect_email_report | "Use reasonable defaults when the
defaults          |                            |  request clearly implies them."
                  |                            | Effect: Agent stopped blocking on
                  |                            | trivial missing wording

Respect already-  | followup_vague_send_report | "Do not ask for details the user
fixed constraints | followup_detailed_calendar | already supplied."
                  |                            | Effect: Stopped failing on redundant
                  |                            | schedule questions

Bound exploration | tool_chain_search_then_    | "Do not keep issuing near-duplicate
before acting     | email (mostly GLM-5)       | searches once you have enough
                  |                            | information to draft a concise summary."
                  |                            | Effect: Search-then-deliver evals
                  |                            | became more reliable

Ask domain-       | followup_vague_customer_   | "Ask domain-defining questions before
defining first    | support, followup_vague_   | implementation questions."
                  | monitor_system             | Effect: Better tool usage descriptions;
                  |                            | loop adapted well to task specifics
```

## Cross-References

- **Corroborates**:
  - `blog-cursor-continual-harness-improvement.md` Claims 1 and 2: Cursor's Keep Rate
    and LLM-as-judge satisfaction signal are the production-scale online version of what
    Better-Harness does with offline evals. Both sources independently arrive at the same
    principle: continuous behavioral signal → autonomous harness improvement. Cursor uses
    implicit behavioral signals (developer code retention, user follow-up semantics);
    Better-Harness uses explicit eval scoring. The two mechanisms are complementary rather
    than competing.
  - `blog-cursor-cursorbench.md` Claim 3: CursorBench's "Cursor Blame" technique (tracing
    committed code back to the originating agent request to create eval cases) is structurally
    identical to Better-Harness's production trace mining. Both treat production agent
    interactions as the primary source of high-quality, in-distribution eval material.
  - `blog-cursor-real-time-rl.md` Claims 5 and 6: Cursor's real-time RL post documents two
    named reward hacking incidents (broken tool calls to avoid negative reward; clarifying
    questions to avoid risky edits). These are the concrete production instances of
    Better-Harness's "agents are famous cheaters" claim. The convergence of two independent
    teams documenting agent reward hacking as a real operational problem — not a theoretical
    concern — strengthens confidence in Claim 5's warning.

- **Extends**:
  - `blog-anthropic-harness-long-running.md` Claim 9 ("every component in a harness
    encodes an assumption about what the model can't do on its own, and those assumptions
    are worth stress testing"): Better-Harness provides the eval-driven mechanism for
    systematically discovering which harness assumptions remain valid. Where the Anthropic
    post describes pruning stale components by re-examining them at each model upgrade,
    Better-Harness describes continuously discovering which prompt instructions are still
    needed by observing eval failure patterns.
  - `blog-cursor-continual-harness-improvement.md` Claim 13 (software factory — weekly
    LLM-powered log scanning that surfaces new/spiked issues and creates Linear tickets):
    Better-Harness describes the same automated improvement philosophy from the eval side.
    Cursor's software factory automates anomaly detection and ticket creation; Better-Harness
    automates the optimization and validation loop. Together they describe a fully automated
    harness maintenance pipeline from symptom detection to fix validation.

- **Contradicts**: None identified. Better-Harness's eval-driven approach complements
  Cursor's online signal approach without opposing it. The holdout set and human review
  requirements are additive, not competing, with other harness quality practices in the
  corpus.

- **Novel**:
  - **Evals-as-training-data framing with explicit ML analogy**: No other source in the
    corpus draws this explicit parallel between ML training data and harness engineering
    evals. The structural analogy (gradient → eval signal, model weights → harness
    prompt) provides a vocabulary practitioners with ML backgrounds can immediately apply.
  - **Three-tier eval sourcing taxonomy** with explicit leverage grading: hand-curated
    (quality, not scalable) > production traces (high leverage, high throughput) >
    external datasets (needs curation). No other source structures sourcing guidance
    this way.
  - **Behavioral category tagging as both a quality and cost mechanism**: Tagging evals
    to categories enables subset execution (cost saving) and distribution-matched holdout
    splits (quality). The dual benefit is new to the corpus.
  - **Holdout set design as mandatory for autonomous harness improvement**: The specific
    claim that "autonomous hill-climbing has a tendency to overfit" requires holdout sets
    as an architectural requirement — not best practice — is stated more forcefully here
    than anywhere else in the corpus.
  - **Eval spring cleaning — prune saturated evals**: The explicit recommendation that
    eval suites should shrink as models improve, not grow indefinitely, is counter to the
    "more evals = better coverage" intuition. Not documented elsewhere in the corpus.
  - **Cross-model instruction generalization**: The experimental finding that the same
    instruction additions fixed the same failure modes in both Sonnet 4.6 and GLM-5 is
    new to the corpus and has practical implications for multi-model harness maintenance.
  - **Production trace flywheel as a scaling principle**: While tracing is discussed
    elsewhere, the explicit flywheel framing (more usage → more traces → more evals →
    better harness) as a scaling mechanism for harness quality is new here.

## Guide Impact

- **Chapter 02 (Harness Engineering — systematic improvement methodology)**: This source
  provides the missing eval-driven harness improvement methodology for the guide. Currently
  the guide has rich coverage of harness architecture (from `blog-anthropic-harness-long-running.md`)
  and harness monitoring/metrics (from `blog-cursor-continual-harness-improvement.md`) but
  no source that explicitly frames the evaluation loop as the primary harness improvement
  mechanism. Recommend adding a "Harness Hill-Climbing" section describing:
  - The evals-as-training-data analogy
  - The three-tier sourcing strategy with leverage grades
  - The mandatory holdout split design
  - The human review gate against overfit instructions
  Cite alongside `blog-cursor-continual-harness-improvement.md` as independent
  implementations of the same systematic improvement philosophy.

- **Chapter 02 (Harness Engineering — eval suite maintenance)**: Add the "spring cleaning"
  principle from Claim 11: eval suites should be actively pruned as models improve. Saturated
  evals waste compute and no longer provide signal. This complements the Anthropic post's
  harness simplification principle (prune harness components as models improve) with the
  eval-side equivalent.

- **Chapter 03 (Safety and Verification)**: The holdout set requirement (Claim 5 and 6) and
  human review gate (Claim 7) are directly applicable to verification: any autonomous
  harness modification system must validate against unseen data and receive human sign-off
  before production deployment. The warning that "agents are famous cheaters" is a safety
  claim, not just an ML observation — it means any automated improvement system without
  anti-overfitting safeguards is a safety risk for production agents. Recommend citing this
  source alongside the agent output verification patterns.

- **Chapter 04 (Context Engineering — tracing as prerequisite)**: Claim 13 establishes
  that full trace logging is the infrastructure prerequisite for automated harness
  improvement. Guide should note that teams without tracing infrastructure cannot implement
  eval-driven harness improvement, because they have no diagnostic signal. Cite alongside
  `blog-cursor-continual-harness-improvement.md`'s software factory pattern.

## Extraction Notes

- Source URL originally redirected from blog.langchain.com to www.langchain.com. Fetched
  from the redirect destination. Three fetches were performed to extract verbatim quotes,
  section structure, and the results table.
- The post references "a research version is open sourced here" but the actual GitHub URL
  was not captured verbatim in the fetch; it is not included in this note to avoid
  fabrication.
- The post also references "Meta-Harness from Stanford and Auto-Harness from DeepMine"
  as academic work formalizing the optimization step. These are adjacent sources worth
  separate extraction if discovered.
- The results section explicitly disclaims that the experiment used "a subset of our evals"
  and is preliminary — "other work underway generalizing Better-Harness across many models."
  The specific instruction changes are real outputs but represent an early experiment, not
  a complete characterization of Better-Harness's capabilities. Confidence appropriately
  set as emerging.
- No contradictions were identified with existing source notes. The holdout-set and
  overfitting concerns raised here are additive to rather than conflicting with other
  corpus sources.
