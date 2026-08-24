---
source_url: https://addyosmani.com/blog/agentic-code-quality/
source_type: blog-post
title: "Agentic Code Quality"
author: Addy Osmani
date_published: 2026-08-08
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: emerging
issue: "#2912"
---

# Agentic Code Quality

> Osmani argues that human code review cannot scale to agent-generated
> volume, so software quality has to relocate into deterministic
> "constraints" (tests, mutation testing, code metrics, linters, security
> scans) placed throughout the loop — not just at a final review gate — and
> offers a three-lever framework (scale verification, throttle generation,
> or lower the bar) for what to do when change volume outruns verification
> capacity.

## Source Context

- **Type**: blog-post (short, single-essay framework piece; also
  cross-posted to the author's Substack). No third-party datasets, studies,
  or external citations are linked anywhere in the body — unlike
  `blog-addyosmani-own-the-outer-loop.md` (Sonar, GitLab, Wharton, Anthropic
  citations) or `blog-addyosmani-agentic-code-review.md` (Faros AI,
  CodeRabbit, GitClear, GitHub citations), this post is pure practitioner
  synthesis/framework with no external evidence attached. The only named
  external reference is a figure ("Guillermo's list," an embedded image of
  a Guillermo Rauch tweet/post enumerating low-stakes situations where
  skipping code review is acceptable) whose actual list content is not
  reproduced as text on the page — only Osmani's own caption describing it.
- **Author credibility**: Addy Osmani is an engineering and evangelism
  leader who spent over 14 years at Google leading developer experience
  across Chrome and, in recent years, AI (Gemini, coding agents, and
  agentic engineering), most recently as a Director at Google Cloud AI. He
  is already a top-cited corpus source
  (`blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-loop-engineering.md`, `blog-addyosmani-intent-debt.md`,
  `blog-addyosmani-new-software-lifecycle.md`,
  `blog-addyosmani-own-the-outer-loop.md`,
  `blog-addyosmani-agentic-code-review.md`). Unlike his data-synthesis
  posts, this one is closer in kind to "Own the Outer Loop": a framework/
  naming piece built from his own operating experience rather than
  aggregated third-party measurement, so its claims should be weighted as
  practitioner authority, not independently verified research.
- **Scope**: Covers why constraint-based "quality gates" have to replace
  exhaustive human review at agent-generation volume; enumerates gate types
  (tests, mutation testing, code-quality metrics, linters/architecture
  rules); frames the open problems this model leaves (agent autonomy under
  ambiguity, and trust that must be "hard-earned" rather than assumed);
  argues constraints should apply throughout the loop (before, during, and
  at the production boundary) rather than as one end-of-pipeline review;
  decomposes quality into multiple non-correctness dimensions
  (maintainability, performance, security, efficiency, comprehensibility);
  names "back-pressure" as the general mechanism constraints implement; and
  gives a three-lever response to verification capacity being outrun by
  agent output volume (scale verification, throttle generation, lower the
  bar), plus a caution to also deliberately relax constraints in some
  places to raise throughput. Does NOT give a worked example of any
  specific quality gate's implementation (no code, no config, no named
  tool beyond "linting tools like ESLint" mentioned once in passing); does
  NOT quantify any of its claims (no percentages, no measured outcomes);
  does NOT reproduce "Guillermo's list" as text, only Osmani's paraphrase
  of what it shows.

## Extracted Claims

### Claim 1: Human code review cannot scale to agent-generated code volume, so quality checks must increasingly live in the harness, environment, and operating system around the agent rather than in a human reading the diff
- **Evidence**: Author's opening framing, stated as personal practice
  ("I still read and review code, but am very intentional about where I am
  comfortable with constraints as the check") plus the core thesis
  restated as its own bolded sentence.
- **Confidence**: emerging (practitioner's stated operating principle, not
  measured)
- **Quote**: "For much of human history, we've evaluated code quality via code review: someone reads what you wrote and makes sure it's clean, thoughtful, fast, understandable, and tests well. For agents, that approach doesn't scale well; there's just too much code for anyone to read. As a result, more and more of our quality checks have to happen in the harness, environment, and operating system around the agent."
- **Additional quote (thesis sentence)**: "Software quality now depends on the constraints you set around your agents."
- **Our assessment**: This is the post's title claim and its most citable
  one-liner. It directly corroborates the review-capacity-crisis argument
  already documented with hard numbers in
  `blog-addyosmani-agentic-code-review.md` (Claim 2: Faros AI's 22,000-
  developer study, median review duration up 441.5%, PRs merging with zero
  review up 31.3%) — this post supplies the prescriptive response
  (relocate quality into constraints) to the empirical problem that other
  post quantifies. It is also a sharper, harness-specific restatement of
  `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("the bottleneck is no
  longer generation, it's verification").

### Claim 2: Constraints are called "quality gates" and take several concrete forms — unit/property/acceptance tests, mutation testing, and code-quality metrics like cyclomatic complexity and line length
- **Evidence**: Author's enumerated taxonomy of gate types.
- **Confidence**: emerging (practitioner taxonomy, not benchmarked against
  alternatives)
- **Quote**: "We call these constraints quality gates, and they take many forms. They include conventional unit tests, property tests, and acceptance tests. They include mutation testing, where we generate variations of code, run it against the same tests, and make sure that people aren't sneaking bugs in that we're missing. They're metrics around code quality, such as cyclomatic complexity and line length, that help keep things readable."
- **Our assessment**: The mutation-testing item is the most independently
  corroborated part of this claim: `blog-simonwillison-condense-json-1-1.md`
  Claim 10 documents a concrete, working example of mutation testing
  (three deliberately planted bug classes, confirmed caught, surfacing two
  real test-suite weaknesses) validating a property-based test suite, and
  `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claim 11 independently
  recommends mutation testing as a named alternative to TDD's red-green
  ceremony for agent-era regression monitoring. This post is the first in
  our corpus to name mutation testing specifically as one item in a broader
  "quality gates" taxonomy alongside code-quality metrics, rather than as a
  standalone technique.

### Claim 3: A concrete heuristic for when it's acceptable to skip reading code entirely is how low the stakes are — no users, throwaway code, prototype; once stakes rise, either a human or the constraints must read the code
- **Evidence**: Reference to an embedded image ("Guillermo's list," a
  Guillermo Rauch tweet/post) plus Osmani's own caption interpreting it.
- **Confidence**: anecdotal (the underlying list itself is not reproduced
  as text on the page — only Osmani's paraphrase of its pattern)
- **Quote**: "Guillermo's list is a good test for whether you can afford to skip reading. Notice that every \"yes\" is really a statement about how low the stakes are - no users, throwaway code, prototype. Once the stakes go up, something has to read the code. If it isn't you on every diff then it has to be the constraints."
- **Our assessment**: The specific content of Guillermo Rauch's list is not
  recoverable from this page (it's an image with only descriptive alt text:
  "Guillermo Rauch lists the low-stakes situations in which not reading
  code may be acceptable"), so we can only extract Osmani's summary of the
  pattern, not the original list. The underlying idea — stakes determine
  whether *anything* needs to read the code, and if not a human, then the
  constraints must — is a useful, quotable framing not present elsewhere in
  the corpus, but it should be attributed as Osmani's gloss on someone
  else's list, not as an independently verifiable claim.

### Claim 4: The constraint model leaves two open problems — agent autonomy under missing/ambiguous information, and trust, which must be "hard-earned" rather than assumed — and the fix for both is an environment that gives agents trustworthy feedback and low-damage failure modes
- **Evidence**: Author's structural argument naming the two gaps
  explicitly.
- **Confidence**: emerging (structural/experiential claim, not measured)
- **Quote**: "One issue is autonomy; agents might apply their intentions well, but may fail when there's missing information or when what they try to do is ambiguous. [...] Many of the reasons that humans fail to ship great code are shared with what agents might do: brittle environments that don't hold up under script-driven stress, nondeterministic builds, missing permissions, and weak tests."
- **Additional quote (trust)**: "The other important issue is trust. We can't credulously hand off intent to something even as smart and robust as a modern agent without checking for correctness. We start with trust, but it has to be hard-earned."
- **Additional quote (target environment)**: "The environment we're after is one where an agent can do real work, get feedback it can trust, and fail without doing much damage."
- **Our assessment**: The "brittle environments... shared with what agents
  might do" framing is a useful reframe: it argues agent failures are often
  the *same* environmental failures that already cause human engineers to
  ship bad code (flaky builds, missing permissions, weak tests), not a
  novel agent-specific risk category — which argues for fixing the
  environment generally rather than building agent-specific guardrails on
  top of a broken one. No existing corpus source states this equivalence
  this directly, though it is consistent with the general
  harness-quality-determines-agent-quality thesis running through
  `blog-lilianweng-harness-engineering-rsi.md` and similar sources (not
  independently re-verified here).

### Claim 5: Constraints must apply throughout the loop's lifecycle — some shape work before it begins, some give feedback while the agent works, some decide whether output can cross the production boundary — not as a single end-of-pipeline review
- **Evidence**: Author's structural framing, restated later as the
  "back-pressure ... throughout the loop" principle (Claim 8).
- **Confidence**: emerging (architectural prescription, not measured)
- **Quote**: "Some constraints shape work before it begins. Others give feedback while the agent is working. Others decide whether its output can cross the production boundary at all."
- **Our assessment**: This three-phase decomposition (before / during /
  boundary) is a more granular version of the general
  "verification-throughout-the-loop, not just at the end" principle already
  present in the corpus. It corroborates and slightly extends
  `blog-addyosmani-own-the-outer-loop.md` Claim 3 (evidence must cross the
  loop boundary before a human Verdict is possible) — that post names the
  human-facing boundary moment specifically; this post frames the same
  boundary as one of three constraint touchpoints, adding the "before work
  begins" and "during work" phases that the other post doesn't name as
  distinct.

### Claim 6: Use a deliberately broad, distinct-responsibility set of constraint types (type safety, performance, late-stage security scanning, custom architecture rules enforced by linters like ESLint) rather than relying solely on unit tests, with hooks to pull in agents or humans when checks break
- **Evidence**: Author's prescriptive recommendation, drawn from stated
  personal experience ("In my experience it helps to...").
- **Confidence**: anecdotal (personal practice recommendation, no
  comparative data given)
- **Quote**: "In my experience it helps to have a broader, but intentionally chosen, set of checks for your constraints instead of solely relying on unit tests. The idea is that each check has a distinct responsibility and that can range from type safety and performance to late-stage security scanning. Folks can define their own constraints too, including architecture rules that linting tools like ESLint can enforce. Many of these tools have built-in hooks that can be used to pull in agents, or humans, when things break."
- **Our assessment**: This is the most concretely actionable claim in the
  post — "distinct-responsibility checks" plus "hooks that pull in agents
  or humans when things break" is close to an implementation sketch, even
  though no specific hook mechanism or tool config is shown. It is
  consistent with, but more general than, the "deterministic tools for
  deterministic work" editorial tenet already reflected in
  `blog-addyosmani-new-software-lifecycle.md` Claim 7's discussion of
  AGENTS.md-adjacent tooling.

### Claim 7: The future of human "code review" is intentional targeting of scarce human attention toward nuanced judgment problems, with humans pulled in only when automated guardrails break — putting a human check into an otherwise machine-speed system has a real productivity cost
- **Evidence**: Author's prescriptive argument, restated as a standalone
  bolded assertion.
- **Confidence**: emerging (prescriptive/structural claim, not measured)
- **Quote**: "AI gives us high volume code generation and velocity, but this can also mean it gets harder for humans to review every single change. You have to instead be intentional with where their attention is going. If you put a human check into a system that otherwise moves at machine speed, don't be surprised if that impacts productivity. Human attention is scarce and valuable so we should proactively direct it to those most nuanced problems that require our judgment. Downstream humans should only be pulled in when the automated guardrails for constraints break."
- **Additional quote (subheading)**: "Human \"code review\" in the future is going to look very different"
- **Our assessment**: This directly corroborates
  `blog-addyosmani-agentic-code-review.md` Claim 11's "human in the loop
  becomes human on the loop: sampling, spot-checking and auditing the
  system" — same reviewer-posture shift, framed here in terms of
  attention-scarcity economics ("if you put a human check into a
  machine-speed system, don't be surprised if that impacts productivity")
  rather than that post's sampling/auditing vocabulary. Also corroborates
  `blog-addyosmani-own-the-outer-loop.md` Claim 10's four-loop human
  oversight decomposition (constraints/sampling/audit/ownership) — "pulled
  in only when automated guardrails break" matches that post's "the human
  doesn't need to be in the inner loop" framing.

### Claim 8: Software quality is not a single metric but a collection of signals across multiple dimensions — correctness, maintainability, performance, security, efficiency, and comprehensibility — and it matters more whether constraints are challenging enough than how many exist
- **Evidence**: Author's definitional/prescriptive claim, restated twice
  in near-identical wording later in the post.
- **Confidence**: emerging (definitional framework, not measured)
- **Quote**: "Correctness is one important dimension, but you may care about others as well, like maintainability, performance, security, efficiency, and comprehensibility. Just as correctness decomposes into many signal types, so does the rest of quality. And while it matters how many constraints we have in place, it matters more whether they're challenging enough to meet our bar for quality and production readiness."
- **Additional quote (restated)**: "Software quality isn't a single metric. Think of it as a collection of signals of varying importance to you and your team."
- **Our assessment**: This multi-dimension decomposition of quality (beyond
  correctness) is new vocabulary for our corpus in this explicit,
  enumerated form. It gives a checklist-shaped structure — six named
  dimensions — that existing corpus sources touch on individually
  (security via `blog-anthropic-*` sources, comprehensibility/intent via
  `blog-addyosmani-intent-debt.md`) but have not previously assembled into
  one named list attributed to a single framework.

### Claim 9: Back-pressure — compilers rejecting invalid code, tests failing, security policies blocking bad practices, CI declining to deploy — is the general mechanism constraints implement, and it should exist throughout the loop rather than as a single review at the very end
- **Evidence**: Author's definitional framing, restated as a standalone
  bolded assertion.
- **Confidence**: emerging (definitional/architectural claim, not measured)
- **Quote**: "Back-pressure can be implemented through many tools: compilers rejecting invalid code, tests failing, security policies blocking bad practices, CI declining to deploy. Ideally it exists throughout the loop, not as a single review at the very end of all the work."
- **Additional quote (subheading, verbatim including source typo)**: "Constraints and back-pressure let agents catch bad work before its a problem"
- **Our assessment**: "Back-pressure" as the named umbrella term for
  constraint mechanisms is a useful, compact vocabulary addition. It is
  consistent with — and gives a general mechanism name to —
  `blog-addyosmani-own-the-outer-loop.md`'s closing operating model ("put
  quality inside the loop... back-pressure mechanisms bound autonomy"),
  which uses the same term without defining its component mechanisms as
  explicitly as this post does (compiler rejection, test failure, security
  policy blocking, CI refusal).

### Claim 10: When agent-generated change volume exceeds verification capacity, teams have three response levers — scale the verification system, reduce the agent generation rate, or lower the quality bar — and should be ready to use all three, while also considering deliberately relaxing constraints elsewhere (e.g., agent swarms/software factories) to raise throughput
- **Evidence**: Author's prescriptive framework, given as an explicit
  numbered set of options in prose.
- **Confidence**: emerging (prescriptive framework, not tested against a
  real capacity-overrun scenario in this post)
- **Quote**: "If we run out of room in the verification loop, we need to do one of several things. First, we can scale our verification system and create more capacity to constrain and push back on changes that come in. Second, we can reduce the rate at which agents generate new changes so that verification can catch up to the volume of work. Third, we can lower our quality bar so that verification doesn't push back as hard as it otherwise might."
- **Additional quote (loosening in the other direction)**: "we should not stop short of realizing that we could actually get more done by un-constraining in some directions. Maybe we can increase the speed of agent-generated changes by providing swarms of agent developers or automated software factories to create changes without waiting for us to review each of them."
- **Our assessment**: This three-lever framework (scale / throttle / lower
  the bar) is the most operationally concrete, novel contribution of the
  post — it names "lower the quality bar" as a legitimate, explicit lever
  rather than treating it as a failure mode to always avoid, which is a
  franker framing than most of the corpus's verification-scaling
  discussion. It is a useful complement to the tiering approach in
  `blog-addyosmani-agentic-code-review.md` Claim 7 (tier review rigor by
  blast radius, not by author) — that post's tiering is one concrete way to
  implement this post's "scale verification system" lever without
  uniformly raising cost.

### Claim 11: Constraints should be deliberately, unevenly distributed — strong where they serve both correctness and throughput goals, relaxed where they serve neither — rather than applied uniformly across a whole system
- **Evidence**: Author's prescriptive argument, restated with near-
  identical wording twice in the post's closing section.
- **Confidence**: emerging (prescriptive framework, not measured)
- **Quote**: "We need to make deliberate decisions about where to apply strong constraints and where to remove or relax them. Apply strong constraints where they're serving both of these goals. Don't support them if they're not serving one or both. Be ready to raise or lower standards as the case may require."
- **Additional quote (spectrum framing)**: "There is a spectrum from innovation-focused at one end to quality-focused at the other. Somewhere along the way, we have to make choices about where we want to be on that spectrum."
- **Our assessment**: This generalizes Claim 10's three-lever framework
  into a standing design principle (constraint placement is itself a
  choice with trade-offs, not a maximize-everywhere default). It is a
  direct, actionable counterpoint to any guide advice that reads as "add
  more quality gates everywhere" — the post explicitly argues for
  *removing* constraints where they don't serve the dual goal of
  correctness and throughput.

### Claim 12: The "ultimate constraint" in the system is the human/organizational willingness to stand behind the decisions and actions taken to build and operate the system — but even this self-imposed accountability constraint requires a deliberate trade-off about how much it restrains, rather than being maximized
- **Evidence**: Author's closing structural argument.
- **Confidence**: emerging (normative/prescriptive claim, not measured)
- **Quote**: "The ultimate constraint in this system is the one we place on ourselves to stand behind the decisions and actions we've taken to build the system and to operate it. But like all other constraints, we need to make thoughtful trade-offs about how much we want our own judgment to restrain, to back-pressure, and to act as a final check."
- **Our assessment**: This reframes accountability itself as one more
  "constraint" subject to the same scale/throttle/relax trade-off logic as
  the technical gates (Claims 10-11), rather than as an unconditional
  standing obligation. This is a notably different framing from
  `blog-addyosmani-own-the-outer-loop.md` Claim 13's "accountability
  contract" proposal, which treats accountability as a fixed per-change
  artifact requirement, not itself a dial to be turned up or down. Both
  posts name accountability as the final backstop, but this post is the
  first in the corpus to explicitly frame accountability as adjustable
  rather than absolute — worth flagging as a nuance rather than a
  contradiction, since neither post directly addresses the other's framing.

## Concrete Artifacts

```
Source: Addy Osmani, "Agentic Code Quality,"
https://addyosmani.com/blog/agentic-code-quality/ (August 8, 2026)

Quality gate taxonomy, named verbatim:
  - Conventional unit tests, property tests, acceptance tests
  - Mutation testing ("generate variations of code, run it against the
    same tests, and make sure that people aren't sneaking bugs in that
    we're missing")
  - Code-quality metrics: cyclomatic complexity, line length
  - Type safety and performance checks
  - Late-stage security scanning
  - Custom architecture rules enforced by linters (ESLint named as an
    example)

Three-lever response to verification capacity being outrun by agent
output volume:
  1. Scale the verification system (more capacity to constrain/push back)
  2. Reduce the agent generation rate (let verification catch up)
  3. Lower the quality bar (verification pushes back less hard)
  + Counter-lever: deliberately relax constraints elsewhere (agent swarms/
    automated software factories) to raise throughput without uniformly
    lowering quality everywhere.

Named quality dimensions (beyond correctness): maintainability,
performance, security, efficiency, comprehensibility ("being easy to
understand").

Back-pressure mechanisms named: compilers rejecting invalid code, tests
failing, security policies blocking bad practices, CI declining to deploy.
```

```
Source: same post — embedded diagrams (image content not reproducible
from page text; alt-text captions preserved below):

1. constraints-pile-combined.svg: "An AI agent surrounded by quality gates
   for correctness, security, performance, accessibility, maintainability,
   cost efficiency, and comprehensibility." (Note: alt text lists
   "accessibility" and "cost efficiency" as additional dimensions not named
   in the surrounding prose, which only lists correctness, maintainability,
   performance, security, efficiency, comprehensibility — see Extraction
   Notes.)
2. guillermo-rauch-code-review.png: "Guillermo Rauch lists the low-stakes
   situations in which not reading code may be acceptable." (figcaption
   quoted in full under Claim 3.)
3. autonomy-earned.svg: "A change is routed to high, gated, or human-
   decided autonomy according to its risk, evidence, and track record."
4. software-factory-loop.svg: "A software factory loop from intent through
   implementation, verification, production, and monitoring."
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-agentic-code-review.md` Claim 2 (Faros AI: median
    review duration +441.5%, PRs merged with zero review +31.3%) —
    supplies the quantitative "why" behind this post's Claim 1 (review
    can't scale to agent volume, quality must move into the harness).
    Claim 11 there ("human on the loop": sampling/spot-checking/auditing)
    directly corroborates this post's Claim 7 (intentional human-attention
    targeting, humans pulled in only on guardrail breaks).
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 ("the bottleneck is
    no longer generation, it's verification") — this post's Claim 1 is a
    harness-specific restatement of the same shift.
  - `blog-addyosmani-own-the-outer-loop.md` Claim 3 (evidence must cross
    the loop boundary before a human Verdict is possible) — corroborated
    and extended by this post's Claim 5's three-phase (before/during/
    boundary) constraint framing. Claim 10 there (four human-oversight
    loops: constraints/sampling/audit/ownership) corroborates this post's
    Claim 7. This post's Claim 9 ("back-pressure... throughout the loop")
    names the general mechanism behind that post's closing "back-pressure
    mechanisms bound autonomy" line without defining its component
    mechanisms as explicitly.
  - `blog-simonwillison-condense-json-1-1.md` Claim 10 (mutation testing
    validated a property-based test suite by catching three planted bug
    classes) and `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claim 11
    (mutation testing recommended as a TDD alternative for agent-era
    regression monitoring) — both independently corroborate this post's
    Claim 2 naming mutation testing as a quality-gate mechanism.

- **Contradicts**: None identified as a direct opposition. Flagging one
  internal nuance rather than a cross-source contradiction: this post's
  Claim 12 (accountability itself is a dial subject to trade-offs) sits in
  tension with — but does not directly contradict — the more fixed,
  unconditional framing of accountability in
  `blog-addyosmani-own-the-outer-loop.md` Claim 13 (the "accountability
  contract" as a standing per-change artifact requirement). Since neither
  post engages the other's framing directly and both are the same author's
  own synthesis rather than competing empirical claims, this does not meet
  the bar in MINER.md §4a for filing a contradiction issue — noted here
  for the Assayer's awareness instead.

- **Extends**:
  - `blog-addyosmani-agentic-code-review.md` Claim 7 (tier review rigor by
    blast radius, not by author) — this post's Claim 10 (three-lever
    response to capacity overrun) names blast-radius tiering as one
    concrete way to "scale the verification system" lever without
    uniformly raising cost everywhere.
  - `blog-addyosmani-own-the-outer-loop.md` Claim 1 (Quality/Verdict/
    Answerability triad) — this post's enumerated quality-gate taxonomy
    (Claim 2) and multi-dimension quality decomposition (Claim 8) give
    concrete operational content to that triad's "Quality" leg, which the
    earlier post names but does not itself decompose into gate types.

- **Novel**:
  - The explicit three-lever framework for responding to verification
    capacity overrun (scale / throttle / lower the bar), including naming
    "lower the quality bar" as a legitimate option rather than a failure
    mode (Claim 10).
  - The six-dimension quality decomposition (correctness, maintainability,
    performance, security, efficiency, comprehensibility) assembled into
    one named list (Claim 8).
  - "Back-pressure" as an explicitly defined umbrella term with four named
    component mechanisms (compiler rejection, test failure, security-
    policy blocking, CI refusal) (Claim 9).
  - Framing accountability itself as an adjustable constraint subject to
    trade-offs, rather than a fixed standing obligation (Claim 12).
  - The "brittle environments... shared with what agents might do" framing
    — agent failures as often the same environmental failures that already
    cause human engineers to ship bad code, not a novel agent-specific risk
    category (Claim 4).

## Guide Impact

- **Chapter 02 (guide/02-harness-engineering.md)**: Add the quality-gate
  taxonomy (Claim 2: unit/property/acceptance tests, mutation testing,
  code-quality metrics, type-safety/performance/security checks,
  linter-enforced architecture rules) as a concrete checklist for what a
  harness's constraint layer should include, citing this source alongside
  the mutation-testing corroboration in
  `blog-simonwillison-condense-json-1-1.md` and
  `blog-fowler-boeckeler-tdd-in-the-agent-loop.md`. Add Claim 6's "hooks
  that pull in agents or humans when things break" as a design requirement
  for constraint tooling.

- **Chapter 03 (guide/03-verification.md)**: Add the three-lever framework
  (Claim 10: scale verification / throttle generation / lower the bar) as
  an explicit decision framework for teams whose agent output has outrun
  review capacity — this is a franker, more actionable articulation than
  existing corpus material of what to actually do when verification
  capacity is exceeded, including naming "lower the bar" as a legitimate
  (if costly) lever. Add the six-dimension quality decomposition (Claim 8)
  as a checklist for what "quality" should mean beyond test-passing
  correctness.

- **Chapter 00 (guide/00-principles.md)**: Add Claim 1's core thesis
  ("software quality now depends on the constraints you set around your
  agents") as a named principle alongside the existing
  verification-bottleneck and human-on-the-loop principles already sourced
  from this author's other posts. Add Claim 11 (constraints should be
  deliberately uneven — strong where they serve correctness+throughput,
  relaxed elsewhere — not maximized everywhere) as a counterweight to any
  guide language that could be read as "add more gates everywhere."

## Extraction Notes

- Full article text fetched via `curl` with a browser user-agent, then
  stripped of HTML tags with a Python stdlib script (no external
  HTML-parsing libraries available in this environment) so that every
  quote above could be checked character-for-character against the raw
  page markup. WebFetch was used only once, for initial orientation
  (returned a condensed AI-generated summary, not used as a quote source).
  This follows the same method used in `blog-addyosmani-own-the-outer-loop.md`
  and other Osmani-post extractions in this corpus.
- The post is short (12 body paragraphs) and contains no linked external
  sources of any kind (contrast with "Own the Outer Loop," which links
  five named third-party studies/reports). All claims here are Osmani's
  own synthesis; confidence is capped at "emerging" throughout except
  Claim 3, which is "anecdotal" because its underlying evidence (Guillermo
  Rauch's list) is an image whose content is not recoverable as text.
  `confidence_overall` for this note is set to "emerging" to reflect that
  the entire source is a single author's framework piece with zero
  external verification, not a mix of settled and emerging claims.
- One inconsistency flagged for the Assayer: the alt text on the
  `constraints-pile-combined.svg` diagram lists "accessibility" and "cost
  efficiency" as quality dimensions, but the surrounding prose text (twice
  restated) only names correctness, maintainability, performance,
  security, efficiency, and comprehensibility. This may be a diagram/prose
  drift within the source itself rather than an extraction error — flagged
  under Concrete Artifacts rather than silently reconciled into a single
  seven- or eight-item list.
- No contradiction meeting the MINER.md §4a bar was identified; the one
  internal-nuance tension with `blog-addyosmani-own-the-outer-loop.md`
  Claim 13 is noted under Cross-References → Contradicts but not filed as
  an issue, since both are the same author's own framing rather than
  opposing empirical claims about the same topic.
- All cross-reference claim numbers above (from
  `blog-addyosmani-agentic-code-review.md`,
  `blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-own-the-outer-loop.md`,
  `blog-addyosmani-new-software-lifecycle.md`,
  `blog-simonwillison-condense-json-1-1.md`, and
  `blog-fowler-boeckeler-tdd-in-the-agent-loop.md`) were verified by
  re-reading each cited note's actual claim numbering before writing this
  note; none were guessed.
