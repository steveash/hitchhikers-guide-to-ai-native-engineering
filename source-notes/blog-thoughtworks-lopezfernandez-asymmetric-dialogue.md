---
source_url: https://www.thoughtworks.com/insights/blog/generative-ai/how-to-talk-with-ai
source_type: blog-post
title: "How to talk with AI?"
author: Javier López Fernández
date_published: 2026-09-08
date_extracted: 2026-09-10
last_checked: 2026-09-10
status: current
confidence_overall: emerging
issue: "#3356"
---

# How to talk with AI?

> A Thoughtworks practitioner piece arguing that prompt engineering is the
> wrong unit of analysis for AI-assisted development, and proposing an
> "asymmetric dialogue" instead: humans speak prose, the AI must answer in
> small, formal artifacts (a test assertion, a type definition, a diagram),
> reviewed continuously in micro-batches rather than at end-of-process PR
> time, with automated fitness functions carrying the bulk of the feedback
> load and low feedback latency treated as a first-class engineering concern.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Generative AI" category;
  published September 8, 2026)
- **Author credibility**: Javier López Fernández, writing under the
  Thoughtworks Insights blog byline. No further bio or credentials are given
  on the page itself. This is a practitioner opinion/framework piece, not a
  data-backed study — it cites no metrics, no named case study, and no
  external sources. Its value is in naming and structuring a pattern
  (asymmetric dialogue, micro-batching, live-loop review), not in providing
  new empirical evidence. The venue (Thoughtworks Insights) carries some
  institutional credibility, but the piece itself reads as personal opinion
  ("We are currently suffering from a bizarre industry-wide obsession...")
  rather than a Thoughtworks-endorsed methodology.
- **Scope**: Covers a proposed interaction model for human-AI pair development
  (asymmetric dialogue, micro-batch artifact exchange, a three-step loop),
  an argument against end-of-process code review, a case for automated
  fitness-function feedback over manual review, and a section on keeping
  feedback-loop latency low (test pyramid, selective test execution,
  decoupled deployment units). Does NOT provide tooling recommendations,
  code examples, named case studies, benchmarks, or citations to other
  sources. Does NOT address multi-agent orchestration, context engineering,
  or governance — it is scoped narrowly to the single-developer/single-agent
  interaction loop.

## Extracted Claims

### Claim 1: The industry's current "prompt engineering" obsession — cheat-sheet incantations like "Act as a Senior Principal Architect" — is not software engineering but "spell-casting," because natural language is ambiguous and LLMs are non-deterministic, so a polite conversational reply reveals nothing about how the AI actually interpreted the request
- **Evidence**: Author's rhetorical framing and definitional argument; no external citation.
- **Confidence**: anecdotal
- **Quote**: "Every week, a new “prompt wizard” posts a cheat sheet claiming that if you frame your request with the right magic incantations “Act as a Senior Principal Architect with 20 years of experience...” the AI will suddenly emit flawless, production-ready software. This is not software engineering. This is spell-casting."
- **Our assessment**: A strongly-worded opinion rather than an argued case, but it sets up the piece's actual contribution (below) well: the real problem it identifies — that a conversational reply doesn't expose the model's actual plan — is a genuine and specific failure mode, distinct from generic "prompting is unreliable" complaints elsewhere in the corpus.

### Claim 2: The real challenge of AI-assisted development is uncovering the AI's intention — exposing its internal blueprint — before it writes production code, not forcing correct syntax out of it
- **Evidence**: Author's framing, restated across the piece as its organizing thesis.
- **Confidence**: emerging
- **Quote**: "The real challenge of AI-assisted development isn’t forcing a model to generate syntax. It is uncovering intention: exposing the AI’s internal blueprint before it touches a single line of production code."
- **Our assessment**: This reframes the human's job from "prompt better" to "verify intent before execution," which lines up with this corpus's broader intent-debt theme (see Cross-References) but applies it at the level of a single interaction turn rather than a whole codebase's documentation.

### Claim 3: An "asymmetric dialogue" is the ideal structure for AI-driven engineering — humans speak to the AI in natural language, but the AI must respond in formal artifacts (code snippets, architectural diagrams, type definitions, failing test assertions), not conversational prose
- **Evidence**: Author's proposed interaction model, justified by an asymmetry-of-strengths argument (human expressive intuition vs. machine formal precision).
- **Confidence**: emerging
- **Quote**: "This reveals the ideal asymmetric dialogue for AI-driven engineering: We speak to the AI in natural language, but the AI must respond to us in formal languages. We shouldn’t want the AI to answer with long, conversational paragraphs explaining its philosophy. We need the AI to answer with concrete, unyielding artifacts: a snippet of code, a focused architectural diagram, a type definition or a failing test assertion."
- **Our assessment**: This is the piece's central, most citable claim. It's a specific, actionable interaction rule (forbid prose responses, demand artifacts) rather than a vague "be specific" prompting tip, and it gives a concrete mechanism for why it should help: "Formal artifacts make hidden assumptions much harder to conceal" than a conversational summary does. We buy the underlying logic — a diff or a failing test is falsifiable in a way a paragraph of AI self-description is not — though the piece offers no evidence this actually reduces defect rates in practice, only the structural argument.

### Claim 4: Human cognitive capacity to spot logical errors drops sharply as the size of an AI-proposed change grows, so batch size (the size of each AI response/artifact) must be drastically shrunk to keep cognitive load near zero
- **Evidence**: Author's argument, framed as a direct consequence of Claim 3; no cited cognitive-science source.
- **Confidence**: emerging
- **Quote**: "We cannot perform a meaningful mental model check on an AI that dumps a proposed change spanning fifty files, three complex diagrams and hundreds of lines of code. When the batch size explodes, our ability to spot logical errors drops significantly. To make this asymmetric loop work, we must drastically shrink the batch size of every interaction and iterate through problems incrementally."
- **Our assessment**: This is an application of a Lean/queueing-theory "small batch size" argument (explicitly named as such later in the piece — see Claim 9) to AI code review specifically. The claim that big-diff review degrades into "rubber-stamping" is plausible and consistent with general software-engineering folklore about large PRs, but the piece gives no threshold (how many files/lines is "too many") — it stays qualitative ("a single test assertion, a five-line interface definition").

### Claim 5: End-of-process code review — waiting for the AI to generate a large feature, then reviewing the finished PR — is an "obsolete anti-pattern" for AI-assisted development, because by the time fifty files exist, the reviewer is rubber-stamping syntax rather than reviewing logic
- **Evidence**: Author's argument, presented as a direct consequence of the micro-batch principle (Claim 4).
- **Confidence**: emerging
- **Quote**: "Waiting for the AI to generate a huge feature and conducting a “code review at the end” is an obsolete anti-pattern. By the time fifty files have been generated, you are no longer reviewing logic; you are just rubber-stamping syntax you don’t fully comprehend."
- **Our assessment**: A strong claim stated with no supporting data (no defect-rate comparison between end-of-PR and continuous review of AI-generated code). It is directionally consistent with Faros AI/GitClear findings cited in `blog-addyosmani-agentic-code-review.md` (Claim 2: review duration up 441.5%, 31.3% rise in PRs merging with zero review) that end-of-process review is already failing to scale for AI-generated volume — but that source diagnoses the same symptom and proposes a *different* fix (tiered review by blast radius, decision logs, circuit-breaker risk prediction) rather than this piece's prescription of continuous micro-batch review. Neither piece engages with the other's proposed fix, so we don't treat this as a contradiction — see Cross-References.

### Claim 6: The three-step intentional dialogue loop is: (1) expose a micro-blueprint (one failing test or interface signature, no implementation), (2) surgical human feedback in natural language on that visible artifact, (3) micro-execution where the AI implements only the minimal logic to satisfy that tiny contract
- **Evidence**: Author's prescribed workflow, given as a named three-step procedure with example prompts for each step.
- **Confidence**: emerging
- **Quote**: "Step 1: Exposing the micro-blueprint (intent check) [...] Instruct the AI: “Do not write feature implementation yet. Show me your intended next step as a tiny, visible contract with just one failing test or interface signature.” Step 2: Surgical human feedback on visible code [...] Step 3: Micro-execution & co-learning"
- **Our assessment**: This is the most concrete, directly-reusable artifact in the piece — a repeatable prompting/review procedure rather than a general principle. It resembles TDD's red-green-refactor loop applied to human-AI pairing, with the human acting as the reviewer at the "red" (failing test) stage before any implementation exists. Worth extracting as a candidate concrete workflow for a "how to prompt incrementally" guide section.

### Claim 7: Reviewing every AI-generated micro-increment manually still creates friction, so the primary feedback loop should be delegated to automated, deterministic mechanisms — compiler/type checks, linters and architectural rules, automated test runners, and fitness functions — rather than relying on human inspection of every step
- **Evidence**: Author's argument; lists four categories of automated feedback mechanism with one-line descriptions each.
- **Confidence**: emerging
- **Quote**: "While natural language is ideal for human critique, manually reviewing every micro-increment can still create friction. To keep velocity high without sacrificing rigor, we must delegate the primary feedback loop to automated mechanisms: hooks and fitness functions."
- **Our assessment**: This directly extends `blog-anthropic-claude-code-verification-loops-skills.md`'s "on-every-PR" and "chained" skill patterns for turning manual checks into automated gates — this piece makes the same architectural move (manual check → automated gate) but frames it as a cognitive-load argument specific to the micro-batch loop, rather than a skills-packaging mechanism.

### Claim 8: Automated feedback mechanisms (hooks, test runners, fitness functions) must feed the AI exact, unambiguous failure detail — stack traces, compiler errors, failed assertion diffs — rather than a vague summary, so the AI can self-correct before a human looks at the result
- **Evidence**: Author's argument, given as the mechanism by which automated feedback closes the loop without human involvement.
- **Confidence**: emerging
- **Quote**: "When a git hook or test runner fails, it shouldn’t send the AI a vague summary. It must feed the AI exact stack traces, compiler errors and failed assertion diffs. This provides the LLM with a zero-ambiguity feedback loop: the machine generates a formal proposal, the automated fitness function evaluates it against deterministic rules and the AI corrects its own trajectory before the human even looks at the result."
- **Our assessment**: This is a specific, checkable design constraint for any hook/CI integration feeding an agent (raw error output, not summarized/truncated output) — the kind of detail that's easy to get wrong in practice if a team pipes hook output through a lossy summarizer. It's a useful, narrow addition even though the piece gives no example of what "vague summary" failure mode it's reacting to.

### Claim 9: Low feedback-loop latency is a core engineering responsibility for AI-assisted development, because if every micro-step requires a slow test suite or build, the developer spends the day watching progress bars instead of iterating — engineering teams should optimize the test pyramid toward fast unit tests, run only tests scoped to the changed module, and decouple deployment units to keep compilation targets small
- **Evidence**: Author's argument, explicitly named as an application of Lean batch-size principles; three concrete tactics listed (test pyramid optimization, selective test execution, decoupled deployment units).
- **Confidence**: emerging
- **Quote**: "If every micro-step requires running a 10-minute test suite, waiting for a full monolithic build to compile or watching an LLM churn through thousands of tokens, you will spend half your day staring at progress bars. That isn't a flow state; it’s paralysis. [...] Optimizing the AI feedback loop is fundamental Lean engineering: shrink the batch size, eliminate waiting time and protect the team’s flow state."
- **Our assessment**: This connects the micro-batch interaction pattern (Claim 4) to concrete architectural prerequisites — you can't do micro-batch AI review well on a slow, tightly-coupled monolith. The three tactics (test pyramid, selective execution, decoupled units) are standard software-engineering advice pre-dating AI assistance, but the piece's contribution is tying them explicitly to AI-loop velocity as the reason they now matter more, not just as general hygiene.

### Claim 10: The solution to AI-assisted development is not "big design upfront" either — the closing argument frames the micro-batch/asymmetric-dialogue loop as a middle path between unstructured mega-prompting and heavyweight upfront specification
- **Evidence**: Author's closing statement, asserted without elaboration.
- **Confidence**: anecdotal
- **Quote**: "Stop trying to write the perfect prompt to guess what the AI will do. Stop thinking that the solution is big design upfront. It’s not. It never was. Speak in prose, demand formal artifacts in return, keep the batch size small and build the software together."
- **Our assessment**: This is a closing rhetorical flourish rather than a developed argument — "big design upfront" is named but never actually discussed or contrasted with the proposed loop anywhere else in the piece. We note it for completeness but treat it as the weakest-supported claim in the source; it reads as a coda gesturing at Agile-vs-waterfall framing rather than a substantiated position.

## Concrete Artifacts

Example prompt for Step 1 of the three-step loop (intent check), quoted verbatim:

```
"Do not write feature implementation yet. Show me your intended
next step as a tiny, visible contract with just one failing test
or interface signature."
```

Example surgical feedback phrasing given for Step 2 (used twice in the
piece, in slightly different form):

```
“This interface leaks domain logic into the persistence layer,”
“This test scenario misses the refund boundary condition”
“This assertion misses the boundary case when the balance hits zero”
“Reuse this domain entity instead of inventing a new DTO here”
```

Four-category taxonomy of automated feedback mechanisms (source's own
grouping, condensed):

```
- Compiler & type checks: catching structural mismatches and type
  violations instantly.
- Linters & architectural rules: enforcing code style, layer
  boundaries and dependency constraints automatically.
- Automated test runners: verifying whether the proposed logic
  satisfies existing invariants or makes new assertions pass.
- Fitness functions: running architectural assertions that measure
  coupling, complexity metrics or security boundaries.
```

Three latency-reduction tactics (source's own grouping, condensed):

```
- Optimizing the test pyramid: push coverage down from slow E2E/UI
  tests to fast, isolated unit tests.
- Selective test execution: scope test/hook runs to the changed
  module rather than the full repo on every micro-commit.
- Decoupled deployment units: break monoliths into smaller modules
  so compilation targets stay small.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-verification-loops-skills.md` — both sources
    argue for turning manual verification steps into automated gates that
    run on every change; this piece frames the same move as a cognitive-load
    necessity of micro-batch review (Claim 7), the Anthropic piece frames it
    as a skills-packaging pattern (standalone/embedded/chained/on-every-PR).
  - `blog-addyosmani-agentic-code-review.md` — both sources diagnose the
    same underlying symptom (AI-generated volume breaks traditional
    end-of-PR review); this piece's Claim 5 ("rubber-stamping syntax you
    don't fully comprehend") is a qualitative restatement of the same
    failure mode that the Osmani piece quantifies via Faros AI/GitClear
    data (441.5% review-duration increase, 31.3% rise in zero-review
    merges). See the note under Claim 5 for how their proposed fixes
    diverge without directly conflicting.
  - `blog-langchain-human-judgment-improvement-loop.md` — both
    sources argue that human judgment should be captured as automated,
    calibrated checks (evaluators / fitness functions) rather than spent on
    repeated manual review, though the LangChain piece is scoped to
    post-deployment production agents and this piece is scoped to the
    in-IDE development loop.

- **Contradicts**: None identified. No existing source note in this corpus
  makes a claim that directly opposes the asymmetric-dialogue or micro-batch
  principles here; the closest tension (Claim 5 vs. the tiered-review
  framework in `blog-addyosmani-agentic-code-review.md`) is a difference in
  proposed remedy for the same diagnosed problem, not a factual conflict, so
  no contradiction issue was filed per MINER.md §4a's guidance on
  conditioning variables ("use tiered review for high blast-radius changes"
  vs. "use continuous micro-batch review" are plausibly complementary, not
  opposed).

- **Extends**: `blog-addyosmani-intent-debt.md` — Osmani's piece argues
  organizations must externalize intent into durable artifacts (specs,
  AGENTS.md, ADRs) so agents don't have to fabricate rationale; this piece
  operates one level down, at the single-interaction-turn level, proposing a
  mechanism (forced formal-artifact responses, Claim 3) for surfacing the
  AI's *momentary* interpretation of intent before code is written, rather
  than durable documentation of intent for future sessions. The two are
  complementary time horizons on the same underlying problem (agents acting
  on intent they don't actually have).

- **Novel**: The "asymmetric dialogue" framing itself (Claim 3) — prose in,
  formal artifacts out, as an explicit communication-boundary rule — is new
  to this corpus. So is the specific zero-ambiguity feedback-loop
  requirement for hooks (Claim 8: raw stack traces/diffs, not summaries)
  and the explicit three-step named procedure (Claim 6). The Lean
  batch-size argument (Claim 4/9) is a known idea applied to a new context
  (AI code review specifically) rather than a new idea in itself.

## Guide Impact

- **Chapter 02** (prompt design / human-AI interaction): Currently the guide
  likely covers prompting technique and context engineering generally.
  Recommend adding the asymmetric-dialogue rule as a concrete interaction
  pattern: instruct agents to respond with a small formal artifact (failing
  test, interface signature, diagram) before implementation, rather than a
  prose plan — citing this source's Claim 3 and the Step 1 prompt template
  in Concrete Artifacts. This is a specific, reusable prompting instruction,
  not just a philosophy.
- **Chapter 04** (developer integration / verification loops): Recommend
  citing Claim 8 (hooks must feed exact stack traces/diffs, not summaries)
  as a specific design constraint when documenting how to wire git
  hooks/CI into an agent loop — this is a checkable implementation detail
  that complements the more abstract "on-every-PR" skill pattern already
  sourced from `blog-anthropic-claude-code-verification-loops-skills.md`.
- **Chapter 05** (workflow design / team adoption): Recommend flagging
  Claim 5's "end-of-process review is dead" position as one side of an
  open tension with the tiered/risk-based review framework already sourced
  from `blog-addyosmani-agentic-code-review.md` — the guide should present
  both as context-dependent options (continuous micro-review for
  low-blast-radius iterative work; tiered/audited review for high-
  blast-radius changes) rather than picking one, since neither source
  argues against the other directly.

## Extraction Notes

The article is short (~1,700 words) and was read in full via a direct fetch
of the live page (no paywall, no linked sub-pages worth following — the
"More insights" footer links to three unrelated Thoughtworks articles, not
elaborations of this piece). The piece contains no citations, footnotes, or
external references of its own, so no linked pages were followed per
MINER.md §1. All ten claims above are drawn from the single page; none are
inferred or extrapolated beyond what the text states. Confidence is graded
`emerging` at the overall level because the piece is a structured, named
framework with internally consistent reasoning (above the bar for
`anecdotal`), but it is a single author's opinion with zero external
evidence, data, or corroborating citations of its own (below the bar for
`settled`). Two individual claims (1 and 10) are graded `anecdotal`
specifically because they are rhetorical framing rather than argued
positions.
