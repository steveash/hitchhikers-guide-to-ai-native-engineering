---
source_url: https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
source_type: blog-post
title: "TDD inside the agent loop - theater or actual value?"
author: Birgitta Böckeler (Distinguished Engineer, Thoughtworks)
date_published: 2026-08-11
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: emerging
issue: "#2639"
---

# TDD inside the agent loop - theater or actual value?

> A Thoughtworks Distinguished Engineer runs a small, self-described
> exploratory evaluation (5 batches, 2 non-TDD + 2 TDD solutions each, one
> batch with test-first variants) comparing agent-authored solutions produced
> under a fully agent-internal TDD workflow versus non-TDD, blind-judged by
> Opus 4.8. Finding: no discernible quality advantage for TDD — non-TDD
> solutions were ranked #1/#2 in most small/medium batches — at 2.96x-8.5x
> the token cost, because agents don't experience the human friction that
> makes test-first design-forcing work, and instead front-load a full design
> in non-TDD runs. She has stopped instructing her own coding agents to do
> TDD and recommends outcome monitoring (mutation testing, static analysis,
> "Approved Scenarios") over prescriptive process enforcement.

## Source Context

- **Type**: blog-post, part of martinfowler.com's "Exploring Gen AI" series
  (Thoughtworks technologists' explorations of gen-AI for software
  development).
- **Author credibility**: Birgitta Böckeler is a Distinguished Engineer and
  AI-assisted delivery expert at Thoughtworks with over 20 years of
  experience as a developer, architect, and technical leader (per her
  article bio). This is first-person, hands-on experimental work with a
  documented setup, not secondhand reporting. Same author as
  [[blog-fowler-boeckeler-local-models-viability]] (a distinct, unrelated
  topic — local model viability for coding — published roughly a month
  earlier).
- **Scope**: Covers only the "fully inside the agentic loop" mode of
  AI-augmented TDD (agent writes failing tests, then implementation, with no
  human checkpoint between the two) — the article explicitly names two other
  TDD-with-AI modes (human writes the tests; AI writes a failing test as a
  human review checkpoint) but does not evaluate those, only the fully
  autonomous one. Tasks were all greenfield, relatively small, pure
  business-logic Python tasks (a data-validation module, a report-generation
  pipeline, a loyalty-points engine) generated with Claude's help
  specifically to be idiosyncratic and reduce training-data repetition. The
  author repeatedly flags this as "far from a comprehensive and structured
  eval result" and a small sample size.

## Extracted Claims

### Claim 1: Based on blind quality judgment, there was no discernible difference between TDD and non-TDD agent-authored solutions, and non-TDD solutions were sometimes ranked higher
- **Evidence**: Opus 4.8 compared solution and test quality without knowledge of which workflow produced each solution, across 5 batches of small/medium/large tasks.
- **Confidence**: emerging (author's own small, exploratory sample; directionally repeated across batches but explicitly not a rigorous eval)
- **Quote**: "TLDR; Based on Opus's judgment of the quality of the outcomes, there was no clearly discernable difference based on TDD workflow versus no TDD workflow. On the contrary, more than once Opus ranked the non-TDD workflow solutions slightly higher in design and test quality. There was also no meaningful difference in mutation scores across the solutions."
- **Our assessment**: This is the article's central, load-bearing finding and directly contradicts the assumption — already present in this guide via [[practitioner-frankray78-netpace]] — that TDD-in-the-loop is a strong structural mitigation for comprehension/quality risk. Filed as contradiction [issue #2653](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2653); see Cross-References below.

### Claim 2: Across small and medium tasks, Opus consistently ranked non-TDD solutions #1 and #2, and TDD solutions #3 and #4
- **Evidence**: Appendix ranking tables across 4 batches (1 small task, 3 medium-task rounds); one exception in the batch where the TDD prompt was strengthened with an explicit refactor-and-design-review step, where a TDD solution ranked #1 but the other TDD solution (identical prompt) ranked last in the same batch. For the larger task, TDD landed in the middle while the two non-TDD runs took both the best and worst spot.
- **Confidence**: emerging
- **Quote**: "Across the small (1 batch) and medium (3 batches) tasks there was a bit of a pattern: Opus ranked the two non-TDD solutions #1 and #2, and the two TDD solutions #3 and #4. Only once - after I strengthened the TDD prompt with a more explicit refactor-and-design-review step - did a TDD solution rank #1. In that same batch, the other TDD solution, run with the identical prompt, ranked last though... For the larger task, TDD landed in the middle, while the two non-TDD runs took both the best and the worst spot."
- **Our assessment**: The single TDD-#1 exception coming from a strengthened, more design-oriented TDD prompt (and its identical-prompt sibling ranking last) is itself a signal that consistency, not just average quality, is a problem for TDD-in-the-loop — the same instructions produced wildly different outcomes.

### Claim 3: Non-TDD and test-first runs front-loaded a complete design (architecture, data types, edge cases, contracts) before writing any code or tests, while TDD runs let the design emerge from many small, locally-minimal decisions that were rarely revisited
- **Evidence**: Opus was asked to review session traces with knowledge of which workflow produced which solution, to hypothesize about the ranking pattern.
- **Confidence**: emerging
- **Quote**: "Asked to look at the session traces to hypothesize about the results with knowledge of which workflow was used for which, Opus found that the non-TDD and test-first runs always created the full design (architecture, data types, edge cases, contracts) before writing any code or tests, rather than working through it one requirement/test at a time." The following paragraph (not adjacent to the passage above — a sentence about data-model quality separates them) adds: "The TDD instructions actively work against such an up front design step. The design in those runs emerged from the sum of many locally-minimal decisions and was rarely revisited, so it tended to land on whatever shape the first test happened to lock in. Behaviour the agent didn't think to write a test for didn't get implemented at all."
- **Our assessment**: This is the article's proposed causal mechanism, not just a correlation — it's a specific, falsifiable claim (TDD locks in early decisions; behavior without a test doesn't get built) that a future larger eval could test directly.

### Claim 4: An AI researcher colleague hypothesizes agents lack step-by-step TDD process in their training data, only completed functions and their descriptions — so agents have no learned representation of *how* to get to code, only what the code should be
- **Evidence**: A direct quote attributed to a named colleague (Ivett Ördög), offered as an explanatory theory for why TDD doesn't transfer, not as independently verified fact.
- **Confidence**: anecdotal (a single colleague's theory, not independently tested in the experiment)
- **Quote**: "The way AI agents were trained is that they have seen completed functions and descriptions of those functions. The number of actual step-by-step TDD examples they have seen is a tiny part of the training data. That means that the LLM has an internal representation of code that is a direct translation of requirements to code, and not a process of how to get to that representation."
- **Our assessment**: Plausible and consistent with [[blog-kentbeck-yagni-economics]] Claim 9, where Kent Beck independently reports being "surprised... to discover that genies don't understand YAGNI" — a second, independent practitioner observation that models don't natively grasp human process-discipline concepts (TDD's incrementalism, YAGNI's restraint) the way they grasp end-state code. Neither is a controlled test of the training-data explanation specifically, so this stays anecdotal.

### Claim 5: Test-first did not reliably prevent tautological tests — one TDD session had a test check the implementation's output against itself by re-running the same code to produce the "expected" answer
- **Evidence**: A specific observed session example from the experiment.
- **Confidence**: anecdotal (one specific observed instance, generalized cautiously)
- **Quote**: "In one particularly obvious example, tests checked the implementation's output against itself, re-running the same code to produce the “expected” answer (see 4. on this list of observations). Writing the test first doesn't reliably prevent this - it might make it less probable, which is all we can ever hope for anyway with LLMs, but from this small data set I can't draw any conclusions about that probability."
- **Our assessment**: Directly matches the "validation is tautological" and "validation re-runs the formatter" weaknesses called out repeatedly in the appendix verdict tables for both TDD and non-TDD solutions (see Concrete Artifacts) — so tautological self-checking wasn't unique to TDD runs in this data either.

### Claim 6: Red-green verification loses its meaning when the same agent both writes the test and confirms it failed, because a red result only proves the agent ran it and saw failure, not that the failure was for the right reason
- **Evidence**: Author's reasoning plus the experiment's own TDD-adherence evaluations, which found agents sometimes skipped or faked the red step, or implemented ahead of the test so it passed immediately.
- **Confidence**: emerging
- **Quote**: "Watching a test go red is only proof of anything if someone is checking why it went red. When the agent both writes the test and confirms it failed, a red test tells you the agent ran it and saw failure, not that the failure was for the right reason."
- **Our assessment**: This is the specific argument behind the article's recommended alternative (mutation testing instead of red-green ceremony) — worth pulling into Ch03's verification-strategy material directly, since it's a concrete, actionable substitute rather than just a critique. Elsewhere in the same paragraph (not adjacent to the passage quoted above) the author adds: "Mutation scores across the solutions didn't show any signals that TDD runs produced meaningfully better mutation scores than non-TDD runs" — reinforcing that red-green's supposed regression-catching benefit didn't show up as a measurable TDD advantage either.

### Claim 7: Minimal-implementation ("small steps"/YAGNI) instructions did not reliably stop agents from over-implementing beyond the current test, because agents had the full requirement available up front rather than being fed the spec incrementally
- **Evidence**: Author's general observation plus specific experiment results.
- **Confidence**: emerging
- **Quote**: "And in the experiment as well, minimal-implementation instructions didn't reliably stop them from building more. They frequently overshot and implemented more than the current test demanded, because they had the full requirement available. We usually don't spoon-feed the spec one by one, that would be very inefficient."
- **Our assessment**: This connects directly to [[blog-kentbeck-yagni-economics]] Claim 6, where Beck argues cheap/free AI code generation collapses the *thrift*-based justification for YAGNI but leaves the optionality and NPV costs intact — Böckeler's observation supplies a mechanism for why agents specifically over-build even under explicit YAGNI-style instruction: they see the whole spec at once, unlike a human doing TDD one requirement at a time.

### Claim 8: The human psychological benefit of TDD — Kent Beck's "managing fear" rationale, where each passing test lets you relax knowing progress is locked in — does not transfer when an agent runs TDD alone in its own loop
- **Evidence**: Contrast between Beck's stated human rationale (quoted from his TDD book preface) and the author's own experience of trust/control when an agent does TDD unsupervised.
- **Confidence**: anecdotal (author's own subjective assessment of what she does and doesn't feel/trust)
- **Quote**: "This is very much about managing a human's fear and giving a human permission to relax. That doesn't transfer when the agent is doing TDD inside of the loop, as it doesn't give me the same control and trust as when I do it myself, step by step."
- **Our assessment**: Complicates, rather than flatly contradicts, [[blog-kentbeck-trust-factory]] Claim 3 (Beck's claim that "thorough automated testing demonstrates trustworthiness... and builds trust within the programmer"). Böckeler's point is narrower and compatible: the trust-building mechanism Beck describes is specifically about a *human* doing the testing/being tested; when the agent performs the entire TDD loop with no human step-by-step involvement, that particular trust-transfer breaks down — she isn't disputing that testing builds trust for humans, only that agent-internal TDD doesn't reproduce it for her.

### Claim 9: TDD consumed at least roughly 3x the tokens of non-TDD runs, ranging 2.96x (medium tasks) to 8.5x (small tasks) to 4.89x (large task), though the multiplier overstates true dollar cost because it doesn't separate cheap cache-read tokens from expensive fresh tokens
- **Evidence**: Measured `getSessionStats()` totals (input + output + cacheRead + cacheWrite) from the pi-coding-agent SDK, summed across every assistant turn, reported per task size in the appendix.
- **Confidence**: emerging (directly measured, but the author explicitly flags the metric as a rough proxy, not a true cost measure, and didn't track cache-hit rates)
- **Quote**: "It therefore weights cheap cache-read tokens the same as expensive fresh tokens, so it likely overstates TDD's true dollar cost. With these small sample sizes, treat the multipliers as directional: TDD reliably cost several times more, how many times exactly is variable." The same appendix paragraph opens (not adjacent to the passage just quoted) with: "Caveat: these numbers are only a rough proxy for session cost, not a measure of how much code or thinking went into a solution."
- **Our assessment**: The multiplier is a real, if imprecise, cost signal — useful as a first-order "TDD-in-the-loop is not free" data point for harness-engineering cost tradeoffs, but the guide should carry the author's own caveat about cache-read inflation rather than citing "3x-8.5x" as a clean dollar figure.

### Claim 10: The author has stopped instructing her coding agents to write tests first or do TDD, pending stronger evidence, and is instead exploring alternative mechanisms to achieve TDD's underlying goals outside the agent loop
- **Evidence**: Author's stated personal practice change, given as the article's conclusion.
- **Confidence**: anecdotal (a single practitioner's stated change in her own workflow)
- **Quote**: "I personally have stopped telling my coding agents to write tests first, let alone do TDD (which I never did, to be honest), until I see evals or other strong arguments that convince me otherwise. I'm trying to focus instead on the benefits of TDD when I use it outside of the agent loop, and exploring alternative ways to achieve them."
- **Our assessment**: This is a behavior-change claim from a credible, experienced practitioner, but it rests on her own small eval plus general skepticism — it should be presented in the guide as "one expert's current stance, backed by exploratory data" rather than a settled recommendation, especially since she explicitly invites someone with more resources to run a larger experiment.

### Claim 11: The article recommends three specific alternatives to TDD-in-the-loop: mutation testing to monitor regression quality, static analysis / code review / file-touch and token-trend monitoring to trigger refactoring, and the "Approved Scenarios" approach for confidence-building
- **Evidence**: Author's own recommended practice, drawing on her own prior mutation-testing article and a colleague's (Ivett Ördög's) "Approved Scenarios" technique, further described by a named colleague (Matteo Vaccari) in a separate linked write-up.
- **Confidence**: emerging (mutation testing and static analysis are established techniques being repurposed for a new agent-era use case; "Approved Scenarios" is a much newer, less-validated technique the author says she has "recently tried out")
- **Quote**: "I have recently tried out the Approved Scenarios approach that Ivett Ördög is advocating for. In my words (don't hold her to it), it's a form of semi-manual testing that is supported by a bespoke test runner for each application. That runner shows me functional test scenarios in an easy to think about way, and allows me to “freeze” expectations (scenarios / fixtures) in that runner after I have thoroughly confirmed them." The other two alternatives are quoted separately, from different, non-adjacent subsections of the article: on regression testing, "I monitor and improve regression quality with the help of mutation testing, instead of giving elaborate TDD instructions and hoping for the best." On refactoring, "A few examples of triggers for refactorings: Give the agent access to static code analysis; run regular reviews of structure and modularity; develop team rituals to maintain a good understanding of the codebase and catch drift early; keep an eye on the trend of number of files touched per change, and number of tokens are for a change."
- **Our assessment**: This directly corroborates and extends [[blog-simonwillison-condense-json-1-1]] Claim 10, where Willison's team used mutation testing to validate a property-based test suite (three planted bug classes, confirming the suite caught them, and surfacing two real weaknesses) — an independent, concrete example of mutation testing catching real gaps in agent-era test suites, giving Böckeler's recommendation a second, working data point outside her own experiment.

### Claim 12: Being overly specific about *how* a model should do something is not a sustainable approach; the better strategy is monitoring outcomes and giving automated feedback
- **Evidence**: Author's general conclusion, framed as connecting to a broader pattern she sees beyond just this experiment.
- **Confidence**: emerging
- **Quote**: "I think at this point there is generally more and more evidence that being overly specific about how we want a model to do something is not a sustainable approach. Instead, we should find as many ways as we can to monitor the outcomes and give feedback. That feedback should be automated wherever possible, and we need to carefully think about where we insert ourselves as arbiters of what is good and correct."
- **Our assessment**: This is a general harness-engineering philosophy claim (process-prescription vs. outcome-monitoring), not specific to TDD — it directly corroborates [[blog-langchain-better-harness-evals]] Claim 1 and Claim 12 (evals as the feedback mechanism for harness changes, and evals becoming regression tests once a behavior is confirmed correct), which make the same "monitor outcomes, automate the feedback loop" argument from a different domain (harness/prompt optimization rather than TDD).

## Concrete Artifacts

Token usage by task size, from the appendix (NT = No TDD, T = TDD; medium row only includes test-first-augmented batches per the article's own footnote):

```
Task    | NT avg tokens   | T avg tokens     | T / NT factor
--------|-----------------|------------------|---------------
Small   | 119,815 (n=2)   | 1,018,245 (n=2)  | 8.50x
Medium  | 736,486 (n=2)   | 2,181,105 (n=6)  | 2.96x
Large   | 253,621 (n=2)   | 1,239,408 (n=2)  | 4.89x

"Only the medium size were done with added test-first instructions"
```

Small-task verdict table (medical appointment slot-code validator), showing the clean #1/#2 non-TDD sweep referenced in Claim 2:

```
ID  | TDD | Rank | Verdict
NT1 | No  | 1    | Best overall — dataclass result, no bugs, 61 reason-asserting tests
NT2 | No  | 2    | Very close — dataclass result, but a Unicode-digit spec deviation
T1  | Yes | 3    | Correct & clean, but dict result + fewer tests + dead code
T2  | Yes | 4    | Weakest design (free-text error) + a genuine crash bug
```

Medium-task round 3 verdict table (report pipeline, after strengthening the TDD prompt with an explicit refactor-and-design-review step), showing the single TDD-#1 exception and its identical-prompt sibling ranking last, referenced in Claim 2:

```
Rank | ID  | TDD | Headline weakness
1    | T1  | Yes | HEADCOUNT-only TOTAL row printed as `$`; validation is a substring check, not arithmetic
2    | NT1 | No  | Fractional HEADCOUNT → spurious ValidationError on valid input; tests lean on monkeypatching
3    | NT2 | No  | `NaN`/`Infinity` crash the pipeline instead of a ParseError; validation re-runs the formatter
4    | T2  | Yes | Validation is tautological (checks aggregate against itself); width check is only a comment
```

Larger-task verdict table (in-memory loyalty points engine), showing TDD landing in the middle referenced in Claim 2:

```
ID  | TDD | Rank | Verdict
NT2 | No  | 1    | Only solution with real input validation; precise boundary tests; minor out-of-order purchase edge cases only
T2  | Yes | 2    | Clean typed data model, all core rules correct; no error handling, duplicate purchase ID bug, dead state fields
T1  | Yes | 3    | Most functionally correct (no bugs found on probing); untyped nested dicts, vestigial structure, fewest tests
NT1 | No  | 4    | Highest design score, 74 tests — but two High bugs: wrong batch draw-down order; future-dated points counted as spendable
```

Experimental setup (source: article's "The setup" section):

```
- Tasks: small, medium, and large greenfield business-logic Python tasks,
  generated with Claude's help specifically for idiosyncratic/specific logic
  to reduce training-data-repetition bias between solutions.
- Instructions: all runs required at least 80% code coverage.
- Implementation model: Sonnet 4.6.
- TDD-adherence judgment: Sonnet 4.6, based on session transcripts, so that
  runs that didn't meaningfully follow TDD wouldn't be counted.
- Solution-quality judgment: Opus 4.8, blind to which workflow produced each
  solution; Opus created its own rubric on the fly, passed to subagents that
  evaluated individual solutions.
```

Kent Beck's TDD "managing fear" preface quote as relayed by the author (source: article, "Small steps >> Confidence and learning" section):

```
In Kent Beck's preface to “Test-driven Development by example”, his biggest
rationale for TDD is “managing fear”. He says that the legitimate fear of
hard problems makes developers tentative, less communicative, and avoidant
of feedback. With TDD, each passing test shows us progress, so we can relax
knowing that progress is locked in.
```

## Cross-References

- **Contradicts**: [[practitioner-frankray78-netpace]] — NetPace's CLAUDE.md
  treats "TDD is non-negotiable" (repeated three times, with an ASCII
  RED-GREEN-REFACTOR diagram) as a core practice, and this guide currently
  cites it (guide/00-principles.md, guide/03-verification.md,
  guide/02-harness-engineering.md) as evidence that TDD-in-the-loop forces
  comprehension before generation. Böckeler's experiment finds the opposite:
  no measured design/quality advantage for agent-internal TDD, at 3-8.5x the
  token cost, and an explicit mechanism for why the comprehension-forcing
  effect specifically fails to transfer to an unsupervised agent. Filed as
  [contradiction issue #2653](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/2653);
  do not treat either side as settled until that issue is resolved and a
  C-NNN entry is appended to CONTRADICTIONS.md.
- **Corroborates**: [[blog-kentbeck-yagni-economics]] (Claim 9: Beck's own
  observation that "genies don't understand YAGNI" independently supports
  Claim 4's theory that agents lack a learned representation of human
  process-discipline, only of end-state code) and (Claim 6: cheap AI
  generation collapses YAGNI's thrift justification but not its
  optionality/NPV costs, consistent with Claim 7's observation that agents
  over-implement because they see the whole spec at once).
  [[blog-simonwillison-condense-json-1-1]] (Claim 10: an independent, working
  example of mutation testing catching real test-suite weaknesses,
  corroborating Claim 11's recommendation to replace TDD's red-green
  ceremony with mutation-testing-based regression monitoring).
  [[blog-langchain-better-harness-evals]] (Claim 1 and Claim 12: the same
  "monitor outcomes, automate the feedback, don't over-prescribe process"
  argument, made independently in the harness-optimization domain rather
  than the TDD domain — corroborates Claim 12).
- **Extends/complicates**: [[blog-kentbeck-trust-factory]] (Claim 3: Beck's
  claim that automated testing builds trust "within the programmer" is not
  contradicted but narrowed by Claim 8 — the trust-building mechanism
  specifically requires a human doing/observing the testing step-by-step;
  agent-internal TDD with no human checkpoint doesn't reproduce it).
- **Novel**: The specific experimental design (blind Opus-judged TDD vs.
  non-TDD comparison across matched task batches, with independent
  TDD-adherence scoring) is new to this corpus — most existing testing- and
  TDD-related source notes are practitioner config profiles (stated
  intentions/rules) or single-project retrospectives, not comparative
  outcome evaluations. The measured token-cost multiplier for TDD-in-the-
  loop (2.96x-8.5x) is also a new concrete data point not present elsewhere
  in the corpus.

## Guide Impact

- **Ch00 (guide/00-principles.md, "What this looks like in practice",
  ~line 254)**: Currently states NetPace's TDD-first workflow "enforces
  comprehension structurally" citing only [[practitioner-frankray78-netpace]]
  (anecdotal, unmeasured). Should be qualified with this source's counter-
  evidence once contradiction #2653 resolves — at minimum, the claim should
  no longer stand as an unqualified structural-mitigation recommendation.
- **Ch03 (guide/03-verification.md, "Mitigating comprehension debt",
  ~line 472)**: The recommendation "Use TDD to force understanding before
  generation," citing only NetPace [anecdotal], should be updated to note
  the contradicting evidence from this source, and Claim 11's alternative
  (mutation testing for regression quality) is a concrete substitute worth
  adding to this same section regardless of how the contradiction resolves.
- **Ch02 (guide/02-harness-engineering.md, multiple NetPace TDD-enforcement
  citations, e.g. ~lines 406-410, 465-481, 1415-1417)**: These currently
  present NetPace's "TDD is non-negotiable" repetition pattern as a
  best-practice example of resistant-to-skimming process enforcement. That
  framing (repetition as an enforcement *technique*) is not directly
  challenged by this source, but the underlying assumption that TDD-in-the-
  loop is worth enforcing this hard is challenged — worth a cross-reference
  note pointing to the contradiction rather than a rewrite.
- **New material**: Claim 9's token-cost multiplier (2.96x-8.5x) and Claim
  11's three concrete alternatives (mutation testing, static-analysis-
  triggered refactoring, Approved Scenarios) are actionable, specific enough
  to add as a new subsection on "agent-internal TDD costs and alternatives"
  in Ch03, independent of the contradiction's resolution.

## Extraction Notes

- WebFetch's default summarization pass returned only a lossy, paraphrased
  summary of this article (tested first) — verbatim quotes above were
  extracted from the raw HTML (fetched directly and stripped of markup) to
  guarantee character-for-character accuracy per MINER.md §2a.
- Did not follow external links beyond the article itself: the "here" link
  to the author's mutation-testing article (referenced in Claim 6/11) and
  the "here" link to Matteo Vaccari's Approved Scenarios write-up (Claim 11)
  are both cited within this note as the author's own attribution, not
  independently read — a future source-submission for either would be a
  reasonable follow-up if the guide wants first-hand material on those two
  techniques.
- The appendix says "You can find the full results in this repository" but
  does not give a resolvable URL in the fetched page text; the linked
  repository was not independently verified. The appendix's own tables
  (reproduced in Concrete Artifacts above) were used directly instead.
- Article's own publish-date signals conflict slightly: the page's "latest
  article (Aug 10)" tag says Aug 10, while the RSS/Atom feed entry (per the
  triage issue body) timestamps it 2026-08-11T07:39:00-04:00. Used the more
  precise Atom timestamp for `date_published`; this is very likely a
  timezone artifact (a US Eastern morning timestamp landing on the day after
  a "site published" tag set from a different timezone) rather than a real
  discrepancy.
- All three Prospector triage comments on the source issue independently
  identified this as a high-novelty, high-priority source; none of them
  flagged the NetPace contradiction — that was found during this
  extraction's cross-reference pass (MINER.md §4) and filed per §4a.
