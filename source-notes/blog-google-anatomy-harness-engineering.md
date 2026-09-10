---
source_url: https://developers.googleblog.com/the-anatomy-of-harness-engineering-how-to-evaluate-iterate-and-guard-ai-coding-agents/
source_type: blog-post
title: "The Anatomy of Harness Engineering: How to Evaluate, Iterate, and Guard AI Coding Agents"
author: Taylor Mullen (Principal Engineer, Google) and Christian Gunderman (Staff Software Engineer, Google)
date_published: 2026-09-09
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: emerging
issue: "#3355"
---

# The Anatomy of Harness Engineering: How to Evaluate, Iterate, and Guard AI Coding Agents

> Google's first-party framework for "behavioral evaluations" — fast,
> deterministic, unit-style assertions on discrete agent actions (tool calls,
> file modifications) that complement end-to-end benchmarks like Terminal-Bench
> and DeepSWE, sequenced after an initial dogfooding-only development phase.

## Source Context

- **Type**: blog-post (Google Developers Blog, published Sept. 9, 2026)
- **Author credibility**: Taylor Mullen (Principal Engineer) and Christian
  Gunderman (Staff Software Engineer) at Google, writing on the official
  Google Developers Blog. The post is illustrated with a code example against
  Google's own Antigravity SDK, indicating first-party production experience
  building and evaluating agentic coding harnesses at Google rather than
  third-party commentary. No named client engagement, benchmark table, or
  quantified before/after result is given — the post is a framework/philosophy
  piece with one worked code example, not an empirical study.
- **Scope**: Covers why end-to-end benchmarks (Terminal-Bench, DeepSWE) are
  insufficient alone, when in a project's lifecycle to introduce formal
  evaluation (the "dogfooding precedent"), the architecture of a "behavioral
  evaluation" (fast, deterministic, unit-style, local), a three-step process
  for building a behavioral eval suite, and a closing position that behavioral
  and end-to-end evals are complementary, not substitutes. Does NOT cover:
  holdout-set or train/test-style overfitting controls for the described
  self-tweaking prompt-optimization loop, quantified results from applying the
  framework, CI/CD pipeline wiring specifics beyond a one-line `pytest`
  invocation, or non-coding-agent use cases.

## Extracted Claims

### Claim 1: End-to-end benchmarks (Terminal-Bench, DeepSWE) are the de facto standard for evaluating coding agents, but a composite score movement gives no insight into which behavior changed or why
- **Evidence**: Opening anecdote naming two specific benchmarks and describing
  the common failure pattern of watching a composite score move without
  understanding the cause.
- **Confidence**: anecdotal (stated as a general practitioner pattern the
  authors have observed, not a measured frequency)
- **Quote**: "they run common end-to-end benchmarks like Terminal-Bench and DeepSWE, watch a composite score move by a few percentage points, and have no idea why it changed"
- **Our assessment**: This is a plausible, widely-relatable framing device
  rather than a novel empirical finding, but it sets up the article's central
  distinction cleanly: end-to-end scores answer "did it get better or worse"
  but not "which specific behavior changed." It names two concrete benchmarks
  which is useful for grounding — Terminal-Bench in particular already
  appears elsewhere in the corpus in a different context (Terminal Bench 2.0
  ranking-swing claim, see Cross-References).

### Claim 2: End-to-end benchmarks don't directly answer diagnostic questions about why a score changed (e.g., overconfidence on ambiguous prompts, skipped test-suite verification, hallucinated CLI flags)
- **Evidence**: Three specific diagnostic questions are posed as examples of
  what a dropped score leaves unanswered, followed by a direct claim about
  benchmarks' limits.
- **Confidence**: settled (this is a structural/definitional point about what
  a composite score can and cannot reveal, not a contested empirical claim)
- **Quote**: "End-to-end benchmarks don't typically directly answer these questions."
- **Our assessment**: This is the article's central diagnostic argument and
  the direct motivation for "behavioral evaluations." It's uncontroversial as
  stated (a single aggregate number cannot, by construction, localize which
  sub-behavior regressed) but the three example questions (ambiguous-prompt
  overconfidence, skipped test-suite verification, hallucinated CLI flags) are
  concrete and reusable as example failure categories for a guide section on
  designing behavioral assertions.

### Claim 3: A behavioral evaluation measures discrete, observable agent actions (e.g., does it ask a clarifying question on an underspecified prompt, does it run the local validator before declaring a build-file edit complete) instead of whether an entire multi-file task was solved
- **Evidence**: Named as the reframe of the "paradigm shift" section, with
  three concrete example behavioral checks given.
- **Confidence**: emerging (a named practitioner framework with worked
  examples, not independently validated against an alternative evaluation
  strategy in a controlled comparison)
- **Quote**: "Instead of measuring whether the agent solved an entire multi-file refactor, a behavioral eval measures discrete, observable actions"
- **Our assessment**: This is the core definitional claim of the post and the
  most directly actionable one: "behavioral eval" is defined by contrast with
  "eval of the final outcome," and it corroborates (independently, from a
  different vendor) `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 6, which names an equivalent concept ("Agents as a unit: individual
  agents are unit tested to verify that they produce intended outcomes").
  Google's post supplies the paradigm name ("behavioral guideposts" vs.
  "report cards") that the Thoughtworks post's "Pytest for LLMs" framing
  lacks.

### Claim 4: Behavioral evaluations function like integration tests for improving agent harness operation, giving a baseline for the targeted behavior and a way to iteratively improve the prompt toward it
- **Evidence**: Direct definitional statement following the "report card"
  exam analogy that opens the "paradigm shift" section.
- **Confidence**: emerging
- **Quote**: "Behavioral evaluations function like integration tests for improving agent harness operation."
- **Our assessment**: The "integration test" analogy (as opposed to the later
  "unit-style checks" framing for the concrete implementation, Claim 5) is
  worth preserving distinctly — the post uses both analogies at different
  points, describing behavioral evals as integration-test-like at the concept
  level and unit-test-like at the implementation level. This dual framing is
  a minor internal looseness in the source's own terminology, not a
  contradiction, but the guide should pick one analogy for consistency rather
  than importing both.

### Claim 5: Bootstrapping an agent should start with developer instinct and dogfooding — running formal evaluations doesn't make sense until the agent can dogfood its own codebase, handle boilerplate, and execute routine developer tasks; evals belong to a second phase focused on ensuring forward progress and guarding against regressions
- **Evidence**: Explicit two-phase sequencing argument under the heading "When
  to evaluate: The dogfooding precedent."
- **Confidence**: emerging (stated as a recommended sequence from the authors'
  own experience building agent systems; no comparison against
  evals-from-day-one is given)
- **Quote**: "you start with developer instinct and dogfooding"
- **Quote (phase 2 definition)**: "Evals belong to the second phase of development: ensuring forward progress and guarding against regressions."
- **Our assessment**: This is a genuinely novel sequencing claim for the
  corpus — no existing source states a precondition (the agent must already
  be capable of dogfooding its own codebase) that must be met *before*
  investing in formal evaluation infrastructure. It corroborates the general
  value of dogfooding already present via `blog-langchain-better-harness-evals.md`
  (Claim 3's assessment notes that post "explicitly endorses 'agent
  dogfooding with visible feedback sharing' as a mechanism to accelerate
  failure-case discovery"), but LangChain frames dogfooding as an ongoing,
  post-launch trace-generation mechanism, whereas Google frames it as a
  pre-eval developmental gate with a specific readiness bar (boilerplate
  handling, routine task execution, writing its own tooling). This is a
  conditioning-variable distinction (when in the lifecycle dogfooding matters
  most), not a contradiction — both sources value dogfooding, for different
  purposes.

### Claim 6: The purpose of an evaluation suite is not to celebrate small score improvements (e.g., "2% better") but to give confidence that a harness change did not make the agent holistically worse
- **Evidence**: Direct statement of the evaluation suite's primary purpose,
  contrasting "celebrate incremental gains" with "guard against holistic
  regression."
- **Confidence**: emerging
- **Quote**: "The primary purpose of an evaluation suite is not to celebrate when you make the agent 2% better; it is to give you unshakeable confidence that a new prompt tweak, tool schema change, or model upgrade did not make the agent holistically worse."
- **Our assessment**: This directly corroborates `blog-langchain-better-harness-evals.md`
  Claim 12 ("Once our agent handles a case correctly, we don't want to lose
  that gain. The eval becomes a regression test.") — both sources converge on
  regression-guarding, not score-chasing, as the load-bearing purpose of an
  eval suite once an agent is functional. Google's framing adds "tool schema
  change" and "model upgrade" as explicit trigger events to guard against
  alongside prompt tweaks, which is a slightly broader trigger list than
  LangChain's prompt/tool-description-focused taxonomy.

### Claim 7: A robust behavioral evaluation framework separates behavioral assertions into fast, deterministic, unit-style checks that run locally, distinct from the broader (slower, more expensive) end-to-end benchmark suite
- **Evidence**: Direct architectural claim under "How a behavioral evaluation
  architecture works," followed by a concrete shell command showing sub-5-second
  local execution.
- **Confidence**: emerging
- **Quote**: "A robust harness evaluation framework separates behavioral assertions into fast, deterministic, unit-style checks that run locally."
- **Our assessment**: The "fast, deterministic, local" triad is the practical
  design constraint that makes the paradigm usable day-to-day (contrasted with
  the "high cost" of investigating end-to-end benchmark regressions mentioned
  in Claim 1). This corroborates `blog-thoughtworks-anand-agent-evaluation-framework.md`
  Claim 6's "Pytest for LLMs" framing of functional unit evals as "automated,
  assertion-based checks that catch regressions" — both sources independently
  converge on a pytest-style, fast-feedback-loop implementation for this
  layer of evaluation.

### Claim 8: Behavioral evals assert on intermediate execution steps (specific tool calls, file modifications) instead of final string equality, illustrated with a working pytest example against the Antigravity SDK that asserts a web-search tool call occurred for a live-weather query
- **Evidence**: Direct statement followed by a complete, runnable code
  example (see Concrete Artifacts).
- **Confidence**: emerging (a single worked example demonstrating the pattern;
  not a claim requiring independent verification beyond reading the code)
- **Quote**: "Behavioral evals assert on intermediate execution steps, like specific tool calls or file modifications, instead of final string equality"
- **Our assessment**: This is the most concrete, copy-pasteable artifact in
  the post. The code example's assertion — `assert types.BuiltinTools.SEARCH_WEB in tools` —
  is a clean illustration of the "discrete, observable action" principle from
  Claim 3: it tests *that the agent consulted live search* rather than
  grading the final prose answer about the weather. This is directly
  reusable as a template pattern in a guide section on writing behavioral
  assertions for any tool-calling agent framework, not just Antigravity.

### Claim 9: A rich behavioral eval suite enables automating prompt engineering — an LLM can be looped to tweak its own system prompt until a failing test passes, while the rest of the suite acts as a CI/CD-style guardrail against regressions
- **Evidence**: Direct statement following the code example, describing a
  self-optimizing loop pattern.
- **Confidence**: anecdotal (described as a capability the behavioral-eval
  architecture enables; no worked example, metrics, or guardrail
  implementation detail is given for this specific loop)
- **Quote**: "you can set up a loop where an LLM tweaks its own system prompt, iterating until a failing test finally passes, all while the rest of your test suite acts similar to how a CI/CD-style guardrail operates"
- **Our assessment**: This is a self-improvement-loop pattern (an LLM
  iteratively editing an artifact — here, its own system prompt — against a
  test signal) that sits in the same family of patterns discussed at length
  in `blog-lilianweng-harness-engineering-rsi.md` Claim 14, which warns that
  "a self-improvement loop optimizes whatever signal it is given. If the
  reward comes from unit tests, the agent may overfit to tests" and
  recommends evaluators/permission control sit *outside* the loop being
  optimized (held-out tests, trace audits, human review). Google's post
  gestures at a mitigation ("the rest of your test suite acts... as a
  guardrail," implying a held-out check distinct from the specific failing
  test being targeted) but does not explicitly name overfitting risk, a
  held-out/optimization-set split, or a human review gate for this specific
  loop the way `blog-langchain-better-harness-evals.md`'s six-step recipe
  does for its harness-optimization loop. We are not filing this as a formal
  contradiction per MINER.md §4a — Google's "rest of your test suite as
  guardrail" language is compatible with (if less explicit than) the
  held-out-set mitigation, so this reads as an omission of emphasis rather
  than an opposing claim. A guide section citing this pattern should
  explicitly append the held-out-set/human-review safeguards from the
  LangChain and Lilian Weng notes, since this post does not spell them out
  for the specific case of a self-tweaking prompt loop.

### Claim 10: Building a behavioral suite should start with a three-step loop, step 1: pick one recent, concrete failure mode as the target for a single new behavioral test
- **Evidence**: First of three named steps under "What to consider when
  building a behavioral suite."
- **Confidence**: emerging
- **Quote**: "Find a recent mistake your agent made, like forgetting to run unit tests before marking a task as done. Find a single, obvious action that slipped, and make that your target."
- **Our assessment**: This is a low-friction, actionable starting heuristic
  for teams with no behavioral eval suite at all — "start with one failure,
  one test" is a much lower activation-energy recommendation than "build a
  comprehensive eval architecture," and directly complements
  `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 9's
  observation that teams often start with only ~20% of scenarios automated.

### Claim 11: Step 2 of the loop: assertion rigidity should scale with task complexity — strict single-turn assertions for simple tasks with one optimal solution path, but fuzzier outcome-based checks (an LLM-as-a-judge) for complex tasks where the model may take an unexpected but correct path
- **Evidence**: Explicit decision rule distinguishing two assertion styles by
  task-complexity, naming "LLM-as-a-judge" for the complex case.
- **Confidence**: emerging (a stated decision heuristic; no comparative data
  on false-positive/false-negative rates for either assertion style)
- **Quote**: "for more complex tasks, the model may take an unexpected but entirely correct path. In those scenarios, avoid enforcing a rigid tool sequence. Instead, use fuzzier, outcome-based checks, such as an LLM-as-a-judge, to evaluate whether the agent's chosen steps successfully and safely solved the problem."
- **Our assessment**: This gives a concrete decision rule ("is there one
  optimal solution path, or many valid ones?") for choosing between strict
  assertions and LLM-as-a-judge scoring — more specific than generic
  "sometimes use an LLM judge" advice. It is complementary to, not
  competing with, `blog-thoughtworks-anand-agent-evaluation-framework.md`'s
  persona-based/unit/observability layering — Google's rule operates *within*
  what Thoughtworks calls the "functional unit eval" layer, deciding how
  strict a given unit assertion should be.

### Claim 12: Step 3 of the loop: automate batch evaluations (aggregating pass rates across multiple runs) rather than blocking PRs on single, noisy eval runs, because AI model behavior is nondeterministic
- **Evidence**: Explicit rationale (single-run noise from model
  nondeterminism) plus the recommended mitigation (batch aggregation, tracked
  as a directional signal over time).
- **Confidence**: emerging
- **Quote**: "Rather than blocking PRs on single eval runs that can be noisy due to nondeterminism of AI models, automate batch evaluations to pull a larger volume of data."
- **Our assessment**: This is a specific, actionable CI-design recommendation
  (don't gate a PR on one noisy run; aggregate and track a trend) that
  addresses a failure mode not explicitly named in the other harness-eval
  corpus sources — `blog-langchain-better-harness-evals.md`'s recipe runs a
  baseline and validates against holdout sets but doesn't specifically discuss
  single-run noise from nondeterminism as a reason to batch. This is a novel,
  practical addition: model nondeterminism as a distinct justification for
  batched evaluation, separate from the overfitting/holdout-set justification
  LangChain gives for its own design choices.

## Concrete Artifacts

### Behavioral eval code example (pytest + Google Antigravity SDK)

```python
# Source: developers.googleblog.com, "The Anatomy of Harness Engineering"
# (Taylor Mullen & Christian Gunderman, Google, Sept. 9, 2026)
# "Example written for the Antigravity SDK."

import pytest
from google.antigravity import Agent, LocalAgentConfig, types

@pytest.mark.asyncio
async def test_agent_uses_web_search_for_live_weather():
    """Assert that the agent consults ground truth rather than guessing."""
    config = LocalAgentConfig()
    async with Agent(config) as agent:
        response = await agent.chat("What's the weather like in Mountain View, California?")
        tools = [call.name async for call in response.tool_calls]

        # Assert behavior, not output prose
        assert types.BuiltinTools.SEARCH_WEB in tools, (
            "Agent answered from memory without consulting live search."
        )
```

### Local behavioral suite invocation

```shell
# Source: developers.googleblog.com, "The Anatomy of Harness Engineering"
# Run local behavioral suite in under 5 seconds
pytest evals/behavioral/ -v
```

### Article section structure (for navigation / re-reading)

```
1. (intro) — end-to-end benchmark trap
2. The paradigm shift: Report cards vs. behavioral guideposts
3. When to evaluate: The dogfooding precedent
4. How a behavioral evaluation architecture works
   4a. Writing a behavioral eval (code example)
5. What to consider when building a behavioral suite
   5a. Pick one failure mode
   5b. Write flexible assertions based on task complexity
   5c. Automate batch evaluations to monitor stability
6. Final thoughts
```

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-anand-agent-evaluation-framework.md` Claim 6 ("The
    'Pytest' for LLMs... automated, assertion-based checks that catch
    regressions"; "Agents as a unit: individual agents are unit tested to
    verify that they produce intended outcomes") — independently converges
    with this source's Claims 3, 7, 8 on a unit-test-style, discrete-action
    evaluation layer, from a different vendor.
  - `blog-langchain-better-harness-evals.md` Claim 12 ("Once our agent
    handles a case correctly, we don't want to lose that gain. The eval
    becomes a regression test.") — corroborates this source's Claim 6 (eval
    suites exist to guard against holistic regression, not chase incremental
    score gains).
  - `blog-langchain-better-harness-evals.md` Claim 3's assessment (dogfooding
    with visible feedback sharing accelerates failure-case discovery) —
    corroborates the general value of dogfooding in this source's Claim 5,
    though the two sources place dogfooding at different points in the
    project lifecycle (see Claim 5's "Our assessment" for the distinction).

- **Contradicts**: None filed. Claim 9 (automating prompt engineering via a
  self-tweaking loop) sits in tension with the overfitting-risk warnings in
  `blog-lilianweng-harness-engineering-rsi.md` Claim 14 and the
  holdout-set/human-review structure in `blog-langchain-better-harness-evals.md`'s
  six-step recipe — this source recommends the self-tweaking pattern without
  spelling out those safeguards. Per MINER.md §4a's guidance on when *not* to
  file, this reads as an omission of emphasis rather than a materially
  opposing claim (Google's own "rest of your test suite acts as a guardrail"
  language is compatible with, if less explicit than, a held-out check), so
  no contradiction issue was opened. See Claim 9's "Our assessment" for the
  full reasoning.

- **Extends**:
  - `blog-thoughtworks-anand-agent-evaluation-framework.md`: that source names
    the "functional unit eval" layer and its Pytest-for-LLMs analogy but does
    not give a worked, runnable code example or a decision rule for when to
    use strict assertions vs. an LLM-as-a-judge. This source supplies both
    (Claim 8's code example; Claim 11's complexity-based decision rule).
  - `blog-langchain-better-harness-evals.md`: that source's six-step
    hill-climbing recipe includes explicit holdout-set/human-review
    overfitting controls for an automated harness-optimization loop; this
    source describes a simpler version of the same self-tweaking pattern
    (Claim 9) without those controls spelled out, making the LangChain recipe
    the more complete methodology for anyone adopting Google's pattern in
    production.

- **Novel**:
  - **The "Report Cards vs. behavioral guideposts" paradigm framing** (Claim
    1-4): no existing source note names this specific dual metaphor for the
    end-to-end-benchmark-vs-discrete-action-assertion distinction, though the
    underlying practice (unit-style behavioral checks) is independently
    corroborated elsewhere.
  - **The two-phase "dogfooding precedent" as a formal gate before
    introducing evals** (Claim 5): no existing source states a specific
    developmental readiness bar (the agent must be able to dogfood its own
    codebase, handle boilerplate, execute routine tasks) that should be met
    *before* investing in a behavioral eval suite.
  - **Task-complexity-scaled assertion rigidity as an explicit decision rule**
    (Claim 11): strict assertions for single-optimal-path tasks, LLM-as-a-judge
    for tasks with multiple valid solution paths — not stated as an explicit
    rule elsewhere in the corpus.
  - **Model nondeterminism (rather than overfitting) as the stated reason to
    batch evaluations** (Claim 12): a distinct justification for batched/
    aggregated eval runs not named in the LangChain holdout-set methodology.
  - **A complete, runnable code example against Google's Antigravity SDK**
    (Concrete Artifacts) illustrating the tool-call-assertion pattern
    end-to-end.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the "Report Cards vs. behavioral
  guideposts" framing (Claims 1-4) as a named paradigm alongside the existing
  LangChain (Better-Harness) and Thoughtworks (three-layer architecture)
  evaluation content, specifically as the *conceptual* motivation slot that
  precedes both — it answers "why build unit-style evals at all" before the
  guide gets into "how" (LangChain's recipe) and "what layers" (Thoughtworks'
  architecture).
- **Chapter 02 (Harness Engineering)**: Add the dogfooding-precedent sequencing
  (Claim 5) as explicit "when to start" guidance: don't invest in a formal
  eval suite until the agent can dogfood its own codebase and handle routine
  tasks reliably. This fills a real gap — the existing corpus (LangChain,
  Thoughtworks) describes how to build and structure an eval suite once you've
  decided to, but not when in a project's life that decision becomes worth
  making.
- **Chapter 02 (Harness Engineering)**: Add the runnable pytest/Antigravity
  code example and the general pattern it demonstrates (assert on tool calls,
  not on final output prose) as a copy-adaptable template for practitioners
  writing their first behavioral eval, cross-referenced against Thoughtworks'
  "Pytest for LLMs" framing for the same layer.
- **Chapter 02 (Harness Engineering) — caution**: When citing the
  self-tweaking-prompt-loop pattern (Claim 9), append the overfitting/
  held-out-set safeguards from `blog-langchain-better-harness-evals.md` and
  the reward-hacking warning from `blog-lilianweng-harness-engineering-rsi.md`
  Claim 14 — this source describes the automation opportunity but not the
  safety controls in the same depth as those two sources.
- **Chapter 03 (Safety and Verification)**: Add the nondeterminism-driven
  batch-evaluation rationale (Claim 12) as a distinct, named justification
  for aggregating eval runs (alongside, not instead of, the overfitting-driven
  holdout-set rationale from LangChain) — CI pipelines that gate PRs on a
  single agent eval run are vulnerable to false-negative blocks purely from
  model sampling variance, independent of any overfitting concern.

## Extraction Notes

- Fetched via direct HTTP download (`curl`) of the article's HTML, then
  stripped of markup and HTML-entity-decoded locally, rather than relying
  solely on WebFetch's AI-summarization pass — this was done because
  WebFetch's fetch-time model declined to reproduce extended verbatim text
  (citing copyright caution) and, in an earlier pass, produced quotes joined
  with ellipses that spliced non-adjacent sentence fragments together
  (explicitly disallowed by MINER.md §2a). All quotes in this note were
  re-verified against the locally-parsed, entity-decoded article text and are
  contiguous fragments from single sentences (a few quotes reconstruct a
  sentence split across inline bold-tag markup — e.g. "Evals belong to the
  second phase of development: ensuring forward progress and guarding against
  regressions" — where the underlying HTML breaks the sentence across `<b>`
  tags rather than across distinct sentences).
- The full article is short (single-page, ~850 words of body text, one code
  example, one shell command) and entirely self-contained — no sub-pages or
  linked deep-dives were present to follow, aside from a link to "the full
  repo" for the Antigravity SDK example, which is a code repository link, not
  a substantive prose page, and was not fetched separately.
- No contradiction issue was filed. The one point of tension identified
  (self-tweaking prompt loop vs. reward-hacking/overfitting safeguards
  documented elsewhere in the corpus) was assessed against MINER.md §4a's
  "when not to file" criteria and judged to be a difference of emphasis/
  completeness rather than a materially opposing claim — see Claim 9 and the
  Cross-References "Contradicts" entry for the full reasoning.
- Confidence set to `emerging`: first-party production framing from credible
  Google engineers with one concrete, verifiable code artifact, but the post
  is a philosophy/framework piece with no quantified before/after results,
  no named case study, and several claims (e.g., Claim 9's self-tweaking loop)
  described as a capability rather than a validated, safeguarded practice.
