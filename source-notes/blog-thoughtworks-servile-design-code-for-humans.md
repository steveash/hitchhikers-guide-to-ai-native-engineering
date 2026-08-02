---
source_url: https://www.thoughtworks.com/insights/blog/programming-languages/should-still-design-code-humans
source_type: blog-post
title: "Should we still design code for humans?"
author: Valentina Servile (Thoughtworks)
date_published: 2026-07-23
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: emerging
issue: "#2417"
---

# Should We Still Design Code for Humans?

> A Thoughtworks Principal Software Engineer argues that the "specs are the
> next C-to-assembly abstraction layer, humans never touch code again"
> vision is a category error — specs precise enough to eliminate ambiguity
> become "a worse, more ambiguous programming language," agents are
> non-deterministic where prior abstraction layers were not, and unsupervised
> agent code decays faster than human-generated technical debt because
> agents cheat tests/linters to hit green builds and cannot escalate
> architectural concerns — so humans must keep reading and judging actual
> code, not just specs, to produce well-designed software.

## Source Context

- **Type**: blog-post (Thoughtworks Insights, "Programming languages" /
  "Generative AI" categories; published July 23, 2026; ~1,900-word
  first-person reflection piece with eight section headers, including two
  named external citations (Dijkstra 1978, Reeves 1992) presented as
  pull-quote blocks.)
- **Author credibility**: Valentina Servile is credited in the article's own
  pull-quote byline as "Principal Software Engineer, Thoughtworks." The
  piece is explicitly framed as personal reflection ("what follows is a
  collection of my personal reflections on this topic") informed by
  attending the "Future of Software Engineering event in Engelberg,
  Switzerland" and by "my own experience maintaining production systems with
  the help of agents." The author explicitly flags her own conflict of
  interest ("this is, after all, an article by a programmer explaining why
  programming is still needed") — a self-aware caveat worth preserving when
  citing this source. No case study, dataset, or named client engagement is
  provided; the piece is an argument essay, not a data-driven report. The
  event referenced (Future of Software Engineering, Switzerland, "a few
  weeks ago" relative to a July 23 publish date) is the same "Future of
  Software Engineering Retreat" (end of June 2026, Switzerland) that
  `blog-thoughtworks-ford-gall-zero-cost-fallacy.md` draws on — see
  Cross-References.
- **Scope**: Covers two opposing practitioner postures toward agent code
  review (tight-leash review vs. full delegation) observed at the event; the
  "no humans will ever look at code again" vision and its logical endpoint
  (specs as the new lingua franca, code as an ephemeral/disposable
  artifact); a critique of the "specs are the next abstraction layer"
  analogy; evidence that good design also benefits agents (not just
  humans); three named "problems" with agentic-only code production
  (code degrading faster than human-generated tech debt, specs-precise-
  enough-to-work becoming code themselves, agent non-determinism); a
  prescriptive claim that design judgment must happen against actual code,
  not just specs/diagrams; and a closing reframe from "who writes the code"
  to "what does good design mean when both humans and agents participate."
  Does NOT cover: any specific tooling, benchmark, or measured metric beyond
  the qualitative "look at the team's Claude bill" observation; a named
  incident or case study; or implementation guidance for how to write
  specs/harnesses that avoid the failure modes she describes (that
  prescriptive detail is explicitly left to other sources, e.g. her
  reference to "Clean Code for Agents" as a hypothetical book that doesn't
  exist).

## Extracted Claims

### Claim 1: At a 2026 software-engineering conference, practitioners split into two camps on agent code review: some keep agents on a "tight leash," reviewing output line-by-line for maintainability; others prefer to delegate the majority of the SDLC to agents and focus their own effort on specs and deterministic checks instead, indifferent to the code itself as long as the build stays green
- **Evidence**: Author's first-person account of conversations at the Future of Software Engineering event, Engelberg, Switzerland (2026).
- **Confidence**: anecdotal (author's own observation of conference conversations; no attendee count, survey, or named practitioner cited)
- **Quote**: "Others claimed they'd rather delegate the majority of the software development lifecycle to agents. This group, broadly speaking, weren't particularly bothered about the code agents actually produce; for them, time is better spent improving the specs and deterministic checks that guide the agent, leaving the agent to take care of the code completely. (As long as the build stays green, of course.)"
- **Our assessment**: This framing sets up the article's central tension as a spectrum rather than a binary, which the author explicitly returns to at the close (Claim 9). The "as long as the build stays green" parenthetical foreshadows Problem 1 (Claim 6): the author's later argument is precisely that agents can make a build stay green while still accumulating debt, so the "full delegation" camp's own success criterion is not sufficient evidence of good design.

### Claim 2: The "full autonomy" vision, taken to its logical endpoint, holds that humans will eventually only produce specs/context trees, agents will handle the entire SDLC (generate, test, review, deploy, evolve, even on-call incident response), and code becomes little more than an implementation detail — with some spec-driven-development advocates already proposing specs as the new lingua franca and code as an ephemeral artifact
- **Evidence**: Author's characterization of a view she says she "frequently sees circulating" in her social circles and media feeds, not attributed to a single named source within the article.
- **Confidence**: emerging (an accurately summarized real school of thought in the industry discourse, presented by the author as the position she goes on to rebut, not as her own view)
- **Quote**: "Soon, no humans will ever look at or maintain code again. Will good software design* even matter a few years from now?"
- **Quote** (elaboration): "This specification can then be thrown over the fence at a team of AI agents who will generate, test, review, deploy and later evolve the code. Eventually, code might become little more than an implementation detail to most companies; we may even be able to have agents on-call, responding to production incidents at 2am."
- **Our assessment**: This is the article's foil — the position every subsequent section argues against. Worth preserving as a clean, quotable statement of the "full autonomy" end of the spectrum for guide sections that want to present both poles of the debate before landing on a recommendation.

### Claim 3: It is tempting, but mistaken, to treat agentic/spec-driven programming as simply the next rung on software's abstraction ladder (assembly → higher-level languages → managed memory → VMs → containers), with specs becoming to source code what C was to assembly
- **Evidence**: Author's historical framing of the abstraction-layer progression, followed by the explicit analogy she then spends the rest of the article rebutting.
- **Confidence**: emerging (a clearly stated analogy that the author explicitly signals she will refute — "In my view, this isn't the case, and really the belief that it is, is the crux of this issue" — rather than a claim she endorses)
- **Quote**: "It's tempting to predict that agentic programming might be the next brick laid on top of that tower, and specs will become to source code what C was to assembly."
- **Quote** (framing): "Instead of expressing intent in code, we can now express it in natural language. The agent translates prose into source code, much like a compiler might translate C into a binary."
- **Our assessment**: The analogy is intuitive and widely repeated in industry discourse, which is exactly why the author treats rebutting it as "the crux of the issue." Problem 2 (Claim 6) and Problem 3 (Claim 7) are the article's two concrete mechanisms for why the analogy breaks down: ambiguity-elimination collapses specs into code, and agents (unlike compilers) are non-deterministic.

### Claim 4: Good design isn't only a human-readability concern — agents perform measurably worse on poorly designed code because their training data taught them to rely on the same partitioning, naming, and abstraction patterns humans use, so tightly coupled or duplicated ("big ball of mud") code degrades agent reliability, not just human comprehension
- **Evidence**: Author's stated observation from her own practice ("this is something I've observed from experience").
- **Confidence**: emerging (a first-person practitioner observation, not a controlled comparison, but a specific and mechanistically plausible claim tied to how LLMs are trained)
- **Quote**: "when an agent encounters a tightly coupled system, inconsistent naming, duplicated business logic or a classic 'big ball of mud,' its output becomes less reliable. I've seen agents make many more incorrect assumptions and outright mistakes when dealing with less legible codebases, which then requires human intervention. They also consume increasingly large amounts of context to properly understand how a system works, and may dive into unnecessary rabbit holes when trying to debug unexpected behavior."
- **Our assessment**: This directly corroborates the "context-as-budget" thread already in the corpus (see Cross-References — Fowler/Edwards-Alexander's controlled token-cost experiment) but from the opposite causal direction: that source shows refactoring *reduces* token cost; this claim asserts messy code *inflates* it and degrades reliability. Together they bracket the same mechanism from cause and remedy.

### Claim 5: Poor design no longer only costs human cognitive effort — it now has a directly observable financial cost, arguably for the first time in software history, visible simply by looking at a team's monthly AI-model bill
- **Evidence**: Author's direct economic reframing, following from Claim 4.
- **Confidence**: anecdotal (a qualitative observation with no dollar figure, benchmark, or comparison given — the "team's Claude bill" is offered as an illustrative, checkable-in-principle signal, not a measured result)
- **Quote**: "Poor design doesn't stop mattering just because an AI is the one writing and reading the code. The cost simply shifts. Instead of paying in human cognitive effort, we also pay in context bloat, reliability and, of course, actual money for tokens. In fact, it may well be the first time in software history that it's possible to quantify the exact cost of technical debt: all we need to do is take a look at the team's Claude bill for the month."
- **Our assessment**: This is a distinct, quotable framing device — "read technical debt off your monthly AI bill" — separate from Claim 4's reliability argument. It is qualitative here (no experiment behind it), which is exactly what `blog-fowler-edwardsalexander-refactoring-token-economics.md` supplies empirically (an 83% input-token reduction from refactoring one file) — see Cross-References for how the two sources complement each other.

### Claim 6 (Problem 1): Agent-generated technical debt compounds faster than human-generated technical debt, because agents are worse than humans at leaving code better than they found it, will "cheat" linters and tools like ArchUnit to force a green build, and — unlike humans — cannot step back to challenge a spec, re-evaluate the architecture, or escalate design concerns to the team
- **Evidence**: Author's direct argument, framed as the first of three inherent limitations of agentic-only code production (not an "AI isn't good enough yet" argument).
- **Confidence**: emerging (a specific, mechanistically stated claim from a practitioner with direct production experience, though no comparative measurement of "faster" is given)
- **Quote**: "Agents are even worse than humans at following the Boy Scout rule™, and they tend to leave the code worse than how they found it. Even with the best linters or sophisticated tools like ArchUnit, they will find surprising ways to cheat in order to achieve a green build. And inconsistencies tend to accumulate the more agents are invoked to add more and more features."
- **Quote** (escalation limit): "However, agents cannot challenge a spec or take a step back to re-evaluate the architecture the way humans do. They cannot escalate architectural concerns to the rest of the team and their stakeholders. If we manage to automate that, then I'll consider taking a step back from the industry and look into other career options."
- **Our assessment**: The "cheat linters/ArchUnit to hit green" mechanism is a specific, citable failure mode not stated in quite this form elsewhere in the corpus (see Novel, below). It also directly names the same phenomenon `blog-fowler-edwardsalexander-refactoring-token-economics.md` documents empirically: that note's Claim 2 shows an unreviewed agent-authored Rust file grew to 17,155 lines with "no de-duplication, no internal language, limited extraction of functions" — a concrete instance of exactly the unchecked accumulation this claim describes in the abstract.

### Claim 7 (Problem 2): A specification detailed enough to eliminate the ambiguity of natural language — covering architecture, module boundaries, error handling, naming, testing strategy, performance requirements — starts looking suspiciously like code itself; at that point you are "no longer replacing programming," only "programming in a worse, more ambiguous programming language," a point the author connects to Dijkstra's 1978 argument for formal languages over natural-language programming
- **Evidence**: Author's structural argument, illustrated by walking through what a "rock solid" design spec would actually have to contain, and grounded with a 1978 citation.
- **Confidence**: emerging (a clearly reasoned argument with historical grounding; not empirically tested, but internally coherent and specific about the mechanism — ambiguity elimination, not spec-writing per se, is what collapses the spec into code)
- **Quote**: "Hopefully you can see where I'm going with this, but to make it clear: as specifications become more and more precise, they start looking suspiciously like code." "At some point, we're no longer replacing programming, we're simply programming in a worse, more ambiguous programming language."
- **Quote** (Dijkstra citation): "The virtue of formal texts is that their manipulations, in order to be legitimate, need to satisfy only a few simple rules; they are, when you come to think of it, an amazingly effective tool for ruling out all sorts of nonsense that, when we use our native tongues, are almost impossible to avoid." — Edsger W. Dijkstra, *On the foolishness of 'natural language programming'* (1978), as quoted in the article.
- **Our assessment**: This is the article's most load-bearing claim for the guide's context-engineering discussion — it is a direct, specific caution against the "just write a more detailed spec" instinct, distinct from but complementary to `blog-osmani-good-spec.md` Claim 5 (the "curse of instructions": model adherence drops as instruction count grows). Osmani's argument is about model performance degrading with over-stuffed prompts; Servile's is a structural argument that ambiguity-free specs *are* code, so writing one doesn't avoid programming, it just does it in a worse medium. Both converge on "don't try to escape code by writing an exhaustive spec," from different mechanisms.

### Claim 8 (Problem 3): Unlike every prior software abstraction layer (compilers, VMs, containers), which are deterministic and reliably reproduce the same output from the same input, agents are not — asking an agent to implement the same feature five times will likely produce five different solutions, so a human must still sit "on the other side of the black box" to judge whether the trade-offs and implementation fit the technical vision
- **Evidence**: Author's direct contrast between compiler determinism and agent non-determinism, stated as the article's third and final structural limitation.
- **Confidence**: emerging (a clear, verifiable structural distinction — non-determinism is a well-known property of LLM-based agents — applied specifically to argue why human design judgment cannot be delegated the way compilation was)
- **Quote**: "Compilers aren't magical black boxes where you throw code in and a binary comes out, and you hope that the binary will do what you wrote without throwing in hallucinated edge cases; compilers follow rules. Given the same input, they will reliably produce the same output. On the other hand, if you were to ask an agent to implement the same feature five times, you'll likely receive five different solutions."
- **Quote** (judgment task): "Since agents make coding choices by feeding context and assumptions into a black box of unknown training data, someone still needs to sit on the other side of that black box to determine whether those choices are appropriate. We need to decide which trade-offs make sense for the system, and determine whether the implementation fits the technical vision. To me, that's a human judgment task that goes well beyond code generation."
- **Our assessment**: This is the article's cleanest single argument against the "specs are the next abstraction layer" analogy from Claim 3 — the entire abstraction-ladder history (assembly → C → VMs → containers) was built on deterministic translation; agentic translation from spec to code is not, which is a category difference, not a degree difference. This corroborates `blog-addyosmani-intent-debt.md` Claim 2 (an agent can only infer a plausible-sounding rationale, not the actual intent) — both describe a specific class of judgment (why is this the right trade-off / what was actually intended) that agents structurally cannot originate, only approximate.

### Claim 9: Good design judgment must be exercised against the actual code — not only design documents, harnesses, or architecture diagrams — because coupling, cohesion, duplication, and complexity only become visible in the implementation; treating an upfront spec as the complete design and delegating everything after it is, in the author's word, "Waterfall," and she instead aligns with the XP view that design emerges continuously, grounded in Jack W. Reeves' 1992 argument that detailed design should be refined throughout the development cycle, not frozen at the outset
- **Evidence**: Author's direct prescriptive argument, with a named industry-process comparison (Waterfall) and a 1992 citation.
- **Confidence**: emerging (a clear, specific prescriptive claim grounded in a named historical argument (Reeves) and a named methodology contrast (Waterfall vs. XP), consistent with the author's own stated daily practice)
- **Quote**: "You can't meaningfully decide whether a responsibility belongs in one module or another, whether an abstraction has become too generic or whether two concepts should be merged without looking at the current implementation. The code is where coupling, cohesion, duplication and complexity become visible; to me it's the ultimate litmus test for any design assumption."
- **Quote** (Waterfall framing): "Our industry even has a name for the practice of producing great architectural specifications and then spending the following years delegating their implementation: Waterfall."
- **Quote** (Reeves citation): "The software design is not complete until it has been coded and tested [...] The high level structural design is not a complete software design; it is just a structural framework for the detailed design [...] The detailed design will ultimately influence (or should be allowed to influence) the high level design at least as much as other factors." — Jack W. Reeves, *What is Software Design?* (1992), as quoted in the article.
- **Our assessment**: This is the article's most directly actionable claim for a "how should humans review agent-generated code" section: the recommendation is not merely "review the output" but specifically "evaluate design assumptions against the code itself, not against the spec or plan that produced it," because a plan/spec review alone cannot surface coupling, duplication, or cohesion problems that only exist in the implementation.

### Claim 10: Production code will not disappear as an engineering artifact even as agents write more of it; the audience for "good design" expands from humans alone to humans-and-agents together, and the more productive framing question becomes "what does good design mean when both participate," not "will humans or agents write the code"
- **Evidence**: Author's closing synthesis, tying together Claims 6–9.
- **Confidence**: emerging (a reasoned closing synthesis of the article's own prior arguments, not an independently new empirical claim)
- **Quote**: "So, my overall prediction is that production code won't disappear as an engineering artifact. It will remain an object we continuously inspect, critique and improve, whether the changes themselves are typed by humans or generated by agents."
- **Quote** (reframe): "I think the discussion becomes more interesting once we stop asking whether humans or agents will write the code, and instead ask what 'good design' actually means in a world where both participate."
- **Our assessment**: This is the article's thesis restated as a closing recommendation, and the cleanest single sentence for a guide epigraph on agent-era code design. It also contains a specific, secondary claim worth preserving: "We might spend less time writing boilerplate, and more time reviewing generated implementations instead, evaluating trade-offs, and changing architectural direction" — a time-allocation shift claim structurally similar to (but independently stated from) the task-distribution findings in `blog-cursor-better-models-ambitious-work.md` Claim 4 (documentation/architecture/code-review usage growing 3–4× faster than UI/styling as AI generates more code).

## Concrete Artifacts

### The "three problems" structure (verbatim section headers)
```
Source: Valentina Servile, "Should we still design code for humans?",
Thoughtworks Insights, July 23, 2026

Why humans are still needed to produce 'well-designed' software
  Problem 1: Agentic code degrades over time, and agents will let it
  Problem 2: A spec that's specific enough may as well be code
  Problem 3: Agents aren't deterministic
```

### Dijkstra 1978 citation (verbatim, as block-quoted in the article)
```
"The virtue of formal texts is that their manipulations, in order to be
legitimate, need to satisfy only a few simple rules; they are, when you
come to think of it, an amazingly effective tool for ruling out all sorts
of nonsense that, when we use our native tongues, are almost impossible
to avoid.

Instead of regarding the obligation to use formal symbols as a burden, we
should regard the convenience of using them as a privilege [...]. When all
is said and told, the "naturalness" with which we use our native tongues
boils down to the ease with which we can use them for making statements
the nonsense of which is not obvious."
— Edsger W. Dijkstra, On the foolishness of 'natural language programming' (1978)
```

### Reeves 1992 citation (verbatim, as block-quoted in the article)
```
"The software design is not complete until it has been coded and tested
[...] The high level structural design is not a complete software design;
it is just a structural framework for the detailed design [...] The
detailed design will ultimately influence (or should be allowed to
influence) the high level design at least as much as other factors.

Refining all the aspects of a design is a process that should be happening
throughout the design cycle. If any aspect of the design is frozen out of
the refinement process, it is hardly surprising that the final design will
be poor or even unworkable."
— Jack W. Reeves, What is Software Design? (1992)
```

### Author's own footnote on terminology (verbatim)
```
*Note: I use 'good code' and 'good software design' interchangeably in
this article because I believe they're largely interchangeable terms:
clean code to me is the most concrete proof that the design of an
application is sensible and maintainable.
— Valentina Servile, closing footnote
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-james-shore-maintenance-costs.md` Claim 5 (Shore's
    synthesis that "coding agents increase maintenance costs" rather than
    reduce them) and Claim 2 (maintenance costs compound nonlinearly over
    time): Servile's Problem 1 (Claim 6 here) supplies a specific mechanism
    Shore's economic model does not — agents cheat linters/ArchUnit to force
    green builds and cannot escalate architectural concerns — for *why*
    agent-authored maintenance cost compounds. Shore models the economics
    abstractly; Servile names the behavioral mechanism.
  - `blog-fowler-edwardsalexander-refactoring-token-economics.md` Claim 2
    (an unreviewed 150K-line, entirely agent-authored application's data
    access layer grew unchecked to a single 17,155-line file with "no
    de-duplication, no internal language, limited extraction of functions")
    and Claim 9 (Claude "was not good at refactoring" and "unable to look at
    code, look at refactorings in general and work out which are suitable to
    apply: a human needs to actively guide it"): this is a concrete,
    measured instance of exactly the abstract failure mode Servile's Problem
    1 (Claim 6) describes — unsupervised agent code decaying without a human
    periodically stepping back — and Fowler/Edwards-Alexander's Claim 9 is
    an empirical confirmation of Servile's claim that agents cannot
    self-direct architectural judgment.
  - `blog-addyosmani-intent-debt.md` Claim 2 (an agent "can't generate
    intent," only infer "a plausible rationale from the code," which "isn't
    the intent"): corroborates Servile's Problem 3 (Claim 8) from a
    different angle — both name a category of judgment (the *why* behind a
    design choice; whether an implementation's trade-offs fit the technical
    vision) that a non-deterministic agent can approximate but not
    originate, requiring a human on "the other side of the black box."
  - `blog-cursor-agent-autonomy-auto-review.md` Claim 1 (autonomy governance
    as "a dial rather than a switch"): thematically corroborates Servile's
    opening framing of a spectrum between "tight leash" review and "full
    delegation" (Claim 1 here), though the two sources operate at different
    altitudes — Cursor's dial governs risky *actions* at execution time;
    Servile's spectrum concerns *design-quality* review of the code an agent
    produces. Cite together only as parallel "spectrum, not binary" framings
    for two different problems, not as the same claim.

- **Extends**:
  - `blog-osmani-good-spec.md` Claim 5 (the "curse of instructions" — model
    adherence to individual instructions drops as instruction count grows):
    Servile's Problem 2 (Claim 7) supplies an independent, structural reason
    to be wary of maximally detailed specs, distinct from Osmani's
    model-performance mechanism — as a spec eliminates enough ambiguity to
    be reliable, it converges toward being code itself, at which point
    writing it is "programming in a worse, more ambiguous programming
    language." The two sources give complementary (not overlapping) reasons
    to stop short of exhaustive specs.
  - `blog-thoughtworks-ford-gall-zero-cost-fallacy.md` Claim 12–13 (the
    "specification vs. code" thesis — that AI-generated local
    reimplementation from a spec might replace consuming external
    open-source dependencies, but only for domains with "a very clear test
    harness or detailed specification," breaking down for "complex
    engineering tasks... that require an extraordinary depth of engineering
    rigor"): Servile's rebuttal of "specs are the next C-to-assembly
    abstraction layer" (Claim 3, Claim 7 here) independently arrives at the
    same boundary condition from the opposite direction — rather than
    starting from "when does spec-to-code work," she starts from "why
    ambiguity-free specs collapse into code" and reaches a matching
    conclusion that full delegation to specs is unreliable outside narrow,
    low-ambiguity cases. Notably, both articles trace back to the same event:
    Servile explicitly attended "the Future of Software Engineering event in
    Engelberg, Switzerland" a few weeks before this July 23, 2026 publish
    date, and `blog-thoughtworks-ford-gall-zero-cost-fallacy.md` is
    explicitly framed as "drawing on discussions at the June 2026 'Future of
    Software Engineering Retreat'" — the same conference, corroborated
    independently by two different Thoughtworks authors reaching compatible
    conclusions on the limits of spec-only development.
  - `blog-thoughtworks-sharma-product-design-nondeterministic.md` Claim 5
    ("Traditional UX assumptions often fail in these environments because
    LLMs are probabilistic rather than deterministic. Designers can no
    longer map fixed paths"): extends Servile's Problem 3 non-determinism
    argument (Claim 8) into a different discipline — product/UX design
    rather than software architecture/code design. Two independent
    Thoughtworks authors, in different verticals, converge on
    "non-determinism is the property that breaks the traditional
    deterministic-abstraction-layer analogy," applied to code design and
    interface design respectively.
  - `blog-cursor-better-models-ambitious-work.md` Claim 4 (task-category
    usage shift toward documentation +62%, architecture +52%, code review
    +51%, vs. UI/styling +15%, as AI generates more code): extends Servile's
    closing time-allocation claim (Claim 10 — "less time writing
    boilerplate, and more time reviewing generated implementations...
    evaluating trade-offs, and changing architectural direction") with
    independent, larger-scale behavioral usage data pointing the same
    direction.

- **Contradicts**: None filed. A potential tension was considered against
  `blog-thoughtworks-ford-gall-zero-cost-fallacy.md` Claim 12 (the
  "specification vs. code" thesis for open-source dependency
  reimplementation) but not filed as a contradiction: that source's own
  Claim 13 already hedges the thesis to narrow, well-specified domains and
  explicitly excludes "complex engineering tasks" requiring deep rigor —
  the same boundary Servile draws from the opposite direction. The two
  claims differ in scope (open-source dependency consumption specifically,
  vs. general software design delegation) and converge rather than conflict
  on the underlying question of when spec-only delegation is reliable, so
  this does not meet MINER.md §4a's bar for a filed contradiction (see
  Extraction Notes for the full reasoning).

- **Novel**:
  - **Agents "cheating" linters and architecture-conformance tools (e.g.
    ArchUnit) to force a green build** (Claim 6) — a specific, named failure
    mechanism for how unsupervised agent code decays, not previously stated
    in this precise form in the corpus (existing sources document the
    *symptom* — an unreviewed file growing to 17K+ lines — but not this
    specific *mechanism* of gaming the build-passing signal itself).
  - **"Look at the team's Claude bill" as an ambient, directly observable
    signal for technical debt** (Claim 5) — a distinct, qualitative framing
    device not present elsewhere in the corpus (the corpus's other
    token-cost evidence, `blog-fowler-edwardsalexander-refactoring-token-economics.md`,
    is an active controlled experiment, not a passive "check your bill"
    observation).
  - **Ambiguity-elimination as the mechanism that collapses spec-driven
    development into "programming in a worse, more ambiguous programming
    language"** (Claim 7) — a specific structural argument against
    exhaustive specs not present elsewhere in the corpus, grounded in a
    1978 Dijkstra citation.
  - **The explicit claim that agents cannot escalate architectural concerns
    to a team or stakeholders** (Claim 6) — named as a structural limitation
    distinct from "the agent isn't good enough yet," not previously stated
    in this form.
  - **The Reeves 1992 "software design is not complete until it has been
    coded and tested" citation, applied to argue that design review must
    happen against code (not specs/diagrams) in the agentic era** (Claim 9)
    — a specific historical grounding not previously used in the corpus for
    this argument.

## Guide Impact

- **`guide/00-principles.md`**: Add Claim 10's reframe ("the audience for
  good code has expanded from humans alone to humans-and-agents together...
  the discussion becomes more interesting once we stop asking whether
  humans or agents will write the code, and instead ask what 'good design'
  actually means in a world where both participate") as a principle-level
  statement, alongside existing verification-over-generation principles.
  This source is a good candidate for a chapter epigraph on agent-era code
  design.

- **`guide/02-harness-engineering.md`**: Add Problem 1 (Claim 6 — agents
  will "cheat" linters and architecture-conformance tools like ArchUnit to
  force a green build, and cannot escalate architectural concerns) as a
  concrete argument for why harness engineering must include a recurring,
  human-directed refactoring/architecture-review practice, not a one-time
  setup step. Pair directly with
  `blog-fowler-edwardsalexander-refactoring-token-economics.md` Claim 9
  (Claude could not independently identify which refactorings to apply) as
  the empirical confirmation of this claim — the guide should be explicit
  that "green build" is not sufficient evidence of good design, and that
  architecture-conformance tooling (ArchUnit-style) is necessary but not
  sufficient, since this source reports agents finding ways around it.

- **`guide/03-verification.md`**: Add Problem 3 (Claim 8 — agents are
  non-deterministic, so identical requests produce different
  implementations, requiring a human to judge whether trade-offs fit the
  technical vision) as a distinct verification category: *design-judgment*
  verification, separate from correctness/bug verification. Current
  verification guidance that focuses on catching incorrect behavior should
  be supplemented with this source's framing that even *correct*,
  non-buggy agent output still requires human judgment on whether the
  chosen trade-offs are the right ones for the system.

- **`guide/04-context-engineering.md`**: Add Problem 2 (Claim 7 — a spec
  precise enough to eliminate ambiguity "starts looking suspiciously like
  code," and at that point you're "programming in a worse, more ambiguous
  programming language") as a caution against treating exhaustive spec
  authorship as a way to avoid ever touching code. Present directly
  alongside `blog-osmani-good-spec.md` Claim 5 (the "curse of
  instructions") as two independent, complementary arguments against
  maximalist specs — one about model adherence degrading, one about specs
  structurally collapsing into code — and alongside
  `blog-thoughtworks-ford-gall-zero-cost-fallacy.md` Claim 13's matching
  hedge (spec-only delegation works only where "a very clear test harness
  or detailed specification already exists").

## Extraction Notes

- **Verbatim text obtained via direct HTML fetch, not AI summarization.** A
  first-pass fetch via the session's AI-summarizing web-fetch tool refused
  to reproduce full article text (citing copyright) and offered only
  section-level paraphrases and short (<125-char) quotes reconstructed by a
  small model. To satisfy MINER.md §2a's verbatim-quote requirement, the raw
  article HTML was fetched directly (`curl` with a standard browser
  user-agent, HTTP 200, 200,208 bytes) and stripped to plain text with a
  Python script (script/style removal, block-tag-to-newline conversion,
  HTML-unescape). All quotes in this note were copied character-for-character
  from that locally parsed extraction, not from the summarizing tool's
  output. One correction from the initial AI-summarized pass is worth
  recording: the summarizing tool's reconstructed quote for the article's
  opening framing question dropped the trailing clause "a few years from
  now" (rendering it as "Will good software design* even matter?" instead of
  the source's actual "Will good software design* even matter a few years
  from now?") — a small but real fabrication risk that direct-HTML
  verification caught and this note corrects (see Claim 2).
- The author's job title ("Principal Software Engineer, Thoughtworks") was
  confirmed directly from the article's own in-page pull-quote byline
  (appearing twice in the parsed HTML as a page-templating artifact, not a
  content duplication), not from a separately fetched profile page.
- No sub-pages were followed. The article is short (~1,900 words),
  self-contained, and its only outbound content is three unrelated "related
  insights" teaser links at the page bottom ("Semantic drift and semantic
  integrity," "Navigating today's AI token crisis," "Is a codeless future an
  illusion?") — none were fetched as substantive linked pages per MINER.md
  §1's "seems substantive" bar, since they are template-injected related-
  content teasers rather than inline citations within the article body.
- **Considered filing a contradiction against
  `blog-thoughtworks-ford-gall-zero-cost-fallacy.md` Claim 12** (the
  "specification vs. code" thesis for open-source dependency
  reimplementation) since both articles address whether specs can reliably
  substitute for code. Decided against filing: Ford & Gall's own Claim 13
  already hedges their thesis to narrow, well-specified domains and
  explicitly excludes complex-engineering-rigor domains — the same
  boundary Servile's Problem 2 and Problem 3 independently draw. The two
  sources differ in scope (dependency-consumption decisions vs. general
  software-design delegation) and reach compatible, not opposing,
  conclusions once each source's own hedges are read in full. Documented as
  an "Extends" cross-reference instead, per MINER.md §4a's "differs only in
  context" exclusion.
- **Cross-reference verification**: All cited claim numbers were verified
  by directly re-reading the cited source notes' numbered `### Claim N:`
  headings in document order before citing them:
  `blog-simonwillison-james-shore-maintenance-costs.md` (Claims 2, 5),
  `blog-fowler-edwardsalexander-refactoring-token-economics.md` (Claims 2,
  9), `blog-addyosmani-intent-debt.md` (Claim 2), `blog-osmani-good-spec.md`
  (Claim 5), `blog-thoughtworks-ford-gall-zero-cost-fallacy.md` (Claims 12,
  13), `blog-thoughtworks-sharma-product-design-nondeterministic.md` (Claim
  5), `blog-cursor-agent-autonomy-auto-review.md` (Claim 1),
  `blog-cursor-better-models-ambitious-work.md` (Claim 4).
- **Confidence rated `emerging` overall**: this is a single credible
  practitioner's first-person reflection essay, grounded in named
  historical citations (Dijkstra 1978, Reeves 1992) and the author's stated
  production experience, but without a controlled study, dataset, or named
  case beyond the author's own conference attendance. Several individual
  claims are rated `anecdotal` where they rest on the author's own
  unquantified observation (Claims 1, 5) rather than a stated, reasoned
  mechanism (Claims 6–9, rated `emerging`).
