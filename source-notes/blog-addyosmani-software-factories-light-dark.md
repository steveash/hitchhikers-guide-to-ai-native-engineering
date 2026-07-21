---
source_url: https://addyosmani.com/blog/software-factories/
source_type: blog-post
title: "Software Factories, Light and Dark"
author: Addy Osmani
date_published: 2026-07-20
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: emerging
issue: "#2097"
---

# Software Factories, Light and Dark

> Osmani names the "dark factory" (fully automated, no human ever reads the
> diff) as a specific, named risk distinct from ordinary automation, argues
> harness/model improvements alone cannot pay down the resulting comprehension
> debt, and proposes "back pressure" (autonomy bounded by cheap, frequent,
> unfakeable verification) as the rule for deciding which loops may run dark
> vs. which must stay "lit" with a human reading the output before it ships.

## Source Context

- **Type**: blog-post (personal blog, addyosmani.com; published July 20,
  2026; ~2,600 words). Explicitly builds on and credits a named conference
  talk — Dex Horthy (co-founder of HumanLayer), "Harness Engineering is not
  Enough: Why Software Factories Fail," given at AI Engineer World's Fair —
  rather than presenting the core argument as Osmani's own primary research.
- **Author credibility**: Addy Osmani spent 14+ years at Google leading
  developer experience across Chrome and, more recently, AI (Gemini, coding
  agents, agentic engineering), most recently as a Director at Google Cloud
  AI. He is already the corpus's most heavily represented single author
  (`blog-addyosmani-code-agent-orchestra.md`, `blog-addyosmani-loop-engineering.md`,
  `blog-addyosmani-intent-debt.md`, `blog-addyosmani-own-the-outer-loop.md`,
  `blog-addyosmani-agentic-code-review.md`, `blog-addyosmani-new-software-lifecycle.md`,
  `blog-addyosmani-earning-taste-judgment.md`). As in those posts, his
  contribution here is synthesis and naming, not original data — this post's
  one concrete anecdote (a four-month fully-automated factory failure) is
  attributed secondhand to Dex Horthy, not observed directly by Osmani. No
  primary link to a Horthy write-up of the four-month experience is given;
  only the AIEWF talk is cited by name.
- **Scope**: Defines a three-layer stack (loop → harness → factory) with the
  review gate named as the only non-scaling box; names and defines "dark" and
  "lit" (light) factories via a manufacturing-lights-out analogy; argues
  harness engineering alone cannot solve comprehension debt for anything
  beyond small/short-cycle changes in complex or brownfield systems; states
  the "back pressure" rule (autonomy bounded by what can be cheaply and
  reliably verified); gives concrete criteria for when a loop may run
  unattended (cheap, frequent, unfakeable check); revisits the
  loop-vs-explicit-graph/state-machine debate; and closes with an
  inner-loop/outer-loop division of labor between agents and engineers. Does
  NOT provide original benchmarks, a controlled comparison of dark vs. lit
  factory outcomes, or implementation detail for any specific harness/tooling
  choice — it is a structural/definitional and cautionary piece.

## Extracted Claims

### Claim 1: A software factory is three concepts stacked — the loop (one agent's gather/act/check cycle), the harness (the walls, tools, and gates around a loop), and the factory (many harnessed loops feeding one review gate under human ownership) — and the review gate is the only expensive, non-scaling box in the whole system
- **Evidence**: Author's structural framing, presented as the organizing
  definition for the rest of the post.
- **Confidence**: emerging (a named structural taxonomy, not measured; extends
  the author's own prior loop/harness distinction with an explicit third
  layer)
- **Quote**: "A software factory is many harnessed loops running at once, fed by a queue of work and drained through a review gate into production, with humans owning the whole thing from above."
- **Additional quote (the cost claim)**: "By and large, every box in this diagram is almost zero cost: generation, tests, scanning. They all run at scale for negligible cost. There is only one expensive box that proves stubbornly resistant to scaling, and that's the review gate."
- **Our assessment**: This directly extends `blog-addyosmani-loop-engineering.md`'s
  loop/harness distinction (that post frames loop engineering as "one floor
  above" harness engineering) with an explicit third layer named "factory,"
  and gives the review-gate-as-sole-bottleneck claim a compact diagrammatic
  form. It is consistent with, and a cleaner restatement of, the
  verification-is-the-constraint thesis already well established in this
  corpus (see Cross-References), but the specific "every box is near-zero
  cost except review" framing is a new, quotable compression of that thesis.

### Claim 2: A dark factory is one where code ships that no human has read, verified only by other machines — the term is borrowed directly from manufacturing's lights-out factories (FANUC since 2001, Xiaomi in 2024), where the physical absence of light signals the physical absence of a human on the floor
- **Evidence**: Author's definitional framing plus a direct historical/
  industrial analogy.
- **Confidence**: emerging (a named definitional claim; the manufacturing
  precedent is a factual historical reference, not independently verified in
  this extraction, but used only as an explanatory analogy, not as evidence
  for the software claim itself)
- **Quote**: "A dark factory runs with the lights physically off, because the only things on the floor are machines and machines don't need light to see. A dark software factory is the same move: code ships that no human has read, verified only by other machines."
- **Additional quote**: "In software, the floor is the diff. Whoever wrote the diff, whoever reviewed it, whoever shipped it, those humans are gone, and what remains is a diff verified only by the machines that built it."
- **Our assessment**: This is the post's headline naming contribution and the
  reason the Prospector rated it high-novelty across three independent triage
  passes. No existing corpus source names this specific failure mode this
  precisely — prior corpus treatments of "human out of the loop" risk (e.g.
  `blog-kentbeck-trust-factory.md`'s "single player" genie development,
  `blog-simonwillison-vibe-coding-agentic-engineering.md`'s accountability
  gap) describe the same general territory without this manufacturing-derived
  vocabulary or the explicit light/dark binary framing.

### Claim 3: Comprehension debt — the widening gap between how much code exists and how much any human still understands — is the specific mechanism by which dark factories fail, and it accumulates quietly with tests green the whole way rather than producing a dramatic failure
- **Evidence**: Author's definitional claim plus a secondhand anecdote
  attributed to Dex Horthy: running a fully automated code factory for about
  four months during which no human looked at the generated code, which
  "required painstaking manual debugging to pinpoint" once problems surfaced.
- **Confidence**: emerging for the definitional claim (comprehension debt
  itself is independently well-supported elsewhere in this corpus, see
  Cross-References); anecdotal for the specific four-month dark-factory
  failure story, which is a single secondhand account with no primary
  write-up linked
- **Quote**: "Comprehension debt is the widening gap between how much code exists and how much any human still understands. A dark factory doesn't pay it down; it takes it on as fast as it can, with the tests green the whole way."
- **Additional quote**: "The ultimate reckoning, when it comes, will not be a dramatic 'it all goes sideways' moment. It will be quiet and late."
- **Our assessment**: The definitional claim is not new — this corpus already
  has settled-confidence backing for the underlying phenomenon via the
  Anthropic RCT (17-point comprehension-quiz gap, 50% vs. 67%, independently
  cited in `blog-addyosmani-own-the-outer-loop.md` Claim 7 and
  `blog-addyosmani-code-agent-orchestra.md`). What's new here is applying it
  specifically as the failure mechanism of *fully automated* pipelines rather
  than of AI-assisted-but-reviewed coding generally, and pairing it with a
  concrete (if secondhand, single-source) production failure story at the
  four-month mark. Treat the four-month figure and "required painstaking
  manual debugging" detail as anecdotal until a primary Horthy source is
  located and mined.

### Claim 4: Harness engineering alone cannot win the fight against comprehension debt for anything beyond small, short-cycle changes — the failure shows up specifically in complex, brownfield, professionally-maintained systems, not in weekend projects or greenfield toys
- **Evidence**: Author's structural argument contrasting model-only automated
  coding's success on small/greenfield tasks against its failure on
  long-lived, professionally-maintained systems.
- **Confidence**: emerging (a reasoned argument built on the comprehension-debt
  mechanism above, not independently measured; the "three to six months"
  figure is asserted without a data source)
- **Quote**: "there's an inherent in-model failure in trying to keep up with codebase quality over the long game and through additive changes, and I think there's good reason to believe that models alone will ultimately lose that battle against comprehension debt."
- **Additional quote**: "Three to six months into a project, you're already drowning in unread code."
- **Our assessment**: This is a direct, if implicit, tension with the
  optimistic framing in `blog-anthropic-harness-long-running.md` Claim 13
  ("the space of interesting harness combinations doesn't shrink as models
  improve. Instead, it moves"). We do not treat this as a filed contradiction
  per MINER.md §4a: the two claims are about different axes — Anthropic's
  claim is about harness *capability* tracking the model's capability
  frontier (a quality/complexity argument), while Osmani's claim here is
  about whether *unreviewed* pipelines accumulate an unrecoverable
  understanding gap over calendar time regardless of model or harness
  quality (a verification/accountability argument). A team could accept both:
  harnesses keep getting more capable at generating correct code, and
  comprehension debt still accumulates if nobody reads what they generate.
  Flagged for the Assayer to double-check this judgment given how close the
  titles/framing are ("Harness Engineering is not Enough" vs. Anthropic's
  harness-design retrospective).

### Claim 5: Back pressure is the rule that a loop can only be granted as much autonomy as can be cheaply and reliably verified — verification, not generation, is the actual constraint on a software factory's throughput
- **Evidence**: Author's named principle, illustrated with a funnel metaphor
  and Dex Horthy's framing that volume alone isn't the problem — a surplus of
  bad, unverifiable PRs is.
- **Confidence**: emerging (a named organizing principle, consistent with and
  extending prior corpus claims about the verification bottleneck, but
  asserted rather than measured in this post)
- **Quote**: "Back pressure is the rule that you can only hand a loop as much autonomy as you can cheaply and reliably verify, and not one inch more. Verification, not generation, is the real constraint on a factory."
- **Additional quote**: "Generation is a wide mouth; verification is the narrow neck. Speeding up the mouth just deepens the pile at the neck."
- **Our assessment**: This sharpens the verification-bottleneck thesis already
  present via `blog-addyosmani-code-agent-orchestra.md`, `blog-addyosmani-agentic-code-review.md`,
  and `blog-addyosmani-own-the-outer-loop.md` into a specific, actionable
  autonomy-granting rule rather than a general observation about where the
  bottleneck sits. Note this post's "back pressure" is a different, though
  compatible, usage from `blog-humanlayer-skill-issue-harness-engineering.md`,
  which names "back-pressure" as a specific harness *surface* (filtering/
  summarizing raw verification output before it re-enters context, e.g. not
  dumping a full test suite into the context window). Osmani's usage here is
  the higher-level autonomy-budgeting principle; HumanLayer's is the
  lower-level context-management mechanism that a back-pressure-respecting
  harness would need. Not a contradiction — different altitudes of the same
  underlying concern — but worth flagging so the guide doesn't conflate the
  two if both are cited under the same term.

### Claim 6: A lit (light) factory doesn't just re-add review at the end of the pipeline — it moves human judgment upstream to product, design, and architecture decisions, before an agent starts a loop at all
- **Evidence**: Author's structural argument, illustrated by the claim that
  reviewing a two-hundred-line plan up front is cheaper than reviewing
  two-thousand lines of generated code after the fact.
- **Confidence**: emerging (a structural/prescriptive claim, not measured)
- **Quote**: "A lit factory is the same pipeline with the lights left on where judgment lives. The agents still do most of the building, but a human reads what comes out before it ships, and the lights stay on wherever a wrong call is expensive."
- **Additional quote**: "The lit version doesn't tack review onto the end but moves the point of human judgment upstream, to the product, the design, and the architecture before an agent starts a loop."
- **Our assessment**: This is consistent with, and gives an economic
  justification for, `blog-osmani-good-spec.md`'s spec-first guidance and
  `blog-addyosmani-own-the-outer-loop.md`'s Quality/Verdict/Answerability
  triad (Claim 3 there: a human Verdict is made only after evidence crosses
  the loop boundary). The "cheaper to review a 200-line plan than 2,000 lines
  of generated code" framing is a new, concrete cost argument for upfront
  design review not stated this specifically elsewhere in the corpus.

### Claim 7: Deliberate architectural discipline (types, test seams, legible call stacks, well-defined component boundaries, dependency injection) is not new advice, but it now does double duty as a cheap, hard-to-fake safety net against agent mistakes — because models are reinforcement-trained against their own harness and tools, not against long-term maintainability
- **Evidence**: Author's structural argument, listing five specific
  architectural practices and stating the mechanism (agents are trained to be
  fluent with tools/idioms, not to preserve long-term maintainability).
- **Confidence**: emerging (a reasoned mechanism claim; the RL-training
  characterization of "the coding agents that feel most capable" is asserted,
  not sourced to a specific training disclosure)
- **Quote**: "good types and method signatures so that mistakes are caught by the compiler instead of in production; test seams where we can pin behavior and make change observable; laying out the code so the next reader, human or model, knows where to find the thing they care about; keeping call stacks short and legible; keeping component boundaries well defined so a change doesn't have a huge blast radius; and dependency injection so we can swap out one piece for another."
- **Additional quote**: "That safety net has to live outside the model, because the model won't supply it. [...] The deliberate architecture we've always talked about is the tool that catches that debt, and the investment we make in it is us buying back our autonomy."
- **Our assessment**: This converges with `blog-kentbeck-trust-factory.md`'s
  central move (Claim 3: XP practices as trust-building mechanisms, not just
  productivity mechanisms) via a different route — Beck reframes
  human-facing practices as building *inter-human* trust; Osmani reframes
  architectural practices as building a *safety net against agent mistakes*.
  Two independent authors, in the same three-month window, are converging on
  "standard software engineering discipline is no longer justified only on
  correctness grounds — it now also functions as delegation infrastructure."
  Neither cites the other. Worth citing together in the guide as independent
  corroboration of the same reframing from different angles (trust economics
  vs. verification economics).

### Claim 8: A loop earns fully-automated ("dark") status only if its check is cheap, runs at high frequency, and relies on an oracle that can't be easily faked out and doesn't drift over time — concrete examples are green/red test oracles, type gates, property tests, and a review agent with a real rubric
- **Evidence**: Author's explicit criteria list, paired with Dex Horthy's rule
  of thumb that an agent holds up for three to ten steps before starting to
  lose the thread past twenty steps, attributed to context accumulation.
- **Confidence**: emerging (a named decision rule; the "3-10 / past 20"
  step-count figures are a rule of thumb attributed to Horthy, not an
  independently measured threshold)
- **Quote**: "A loop can earn itself fully automated status only if the check is cheap, runs at high frequency, and relies on something that can't be easily faked out. [...] When done can be proven not just by you but by a machine, you've reached automation."
- **Additional quote**: "Dex's rule of thumb: an agent holds up for three to ten steps, then starts losing the thread past twenty. [...] Sprawling loops hide mistakes in the corners, which is another way of saying they never earned lights-out status."
- **Our assessment**: This is the post's most actionable, checklist-style
  content — a concrete gate for "should this specific loop run unattended?"
  distinct from the more abstract back-pressure principle (Claim 5). It
  pairs naturally with `blog-anthropic-harness-long-running.md`'s sprint
  decomposition and evaluator-cost-benefit findings (that post's Claim 10:
  the evaluator is worth its cost only when the task exceeds solo model
  capability) as a complementary "when to automate the check itself" answer.
  A concrete illustrative example given in the post: Horthy described "a
  nightly GitHub Actions cron that fixes exactly one anti-pattern, a lint
  violation or a needlessly optional prop, commits, and opens one small pull
  request, all on its own" as a loop narrow and low-stakes enough to run
  dark; the post explicitly contrasts this with not wanting to "risk waking
  up to a broken auth system, billing engine, or public API contract."

### Claim 9: The current rediscovery of explicit control-flow graphs/state machines for agent orchestration is not a new technique — it is software re-admitting it always needed the flowchart, after briefly trying to throw the diagram away and let a model pick its own path tool-call by tool-call
- **Evidence**: Author's structural argument, citing Dex Horthy's framing that
  "software was always going to have that structure" and quoting Horthy's
  characterization of most "agentic" systems as mostly deterministic code
  with LLM steps sprinkled in.
- **Confidence**: emerging (an argument about industry trend/rediscovery, not
  measured; corroborated by named tooling examples cited in the post —
  LangGraph, LlamaIndex Workflows, Jerry Liu's hybrid workflow-graph
  approach, David Khourshid's state-machine framing)
- **Quote**: "The genuinely new move was trying to throw the diagram away, leaning on a loop where the model picks the path tool call by tool call, until it declares itself done. That felt like liberation, right up until it met a ten-year-old codebase, and the discipline everyone is now rediscovering, owning your control flow, is really just walking the graph back around the loop."
- **Additional quote (Horthy)**: "mostly deterministic code, with LLM steps sprinkled in at just the right points."
- **Our assessment**: This gives the back-pressure principle (Claim 5) a
  concrete implementation form — a predefined directed graph with conditional
  edges is "back pressure drawn as a diagram," since it trades some of the
  agent's freedom for mandatory checks and legible failure points. This is a
  useful bridge between this post's abstract autonomy-budgeting rule and
  concrete orchestration-tooling choices, not previously connected this
  explicitly elsewhere in the corpus.

### Claim 10: Engineers own the outer loop — deciding whether an approach is right, verifying that a diagnosis and implementation are sound, approving the change, and carrying the consequences of being wrong — while agents run the inner loop of investigation, implementation, and testing
- **Evidence**: Author's closing structural argument, restating a division of
  labor between agent execution and human accountability.
- **Confidence**: emerging (a structural/normative claim, not measured; this
  specific inner-loop/outer-loop pairing is stated identically in the
  author's own dedicated prior post — see assessment)
- **Quote**: "The bits you own are what I'd call the outer loop: decide whether it's the right way to address the problem, verify that the diagnosis and implementation are sound, approve the change, and carry the consequences of being wrong."
- **Additional quote**: "Robots are fine operating in the dark, but humans need to see what they're doing. If everything on the factory floor is dark, and you can't see anything, and you can't even find the light switch, that's where the danger is."
- **Our assessment**: This is a compressed restatement of
  `blog-addyosmani-own-the-outer-loop.md` Claim 2 and Claim 3 (agents run the
  inner execution loop; engineers own the outer accountability loop; a human
  Verdict happens only after evidence crosses the boundary) — same author,
  same terminology, five days apart. It adds no new mechanism beyond that
  fuller post but does add the "light switch" framing device that ties the
  outer-loop claim back to this post's central dark/lit metaphor. Because
  this pairing of "inner loop"/"outer loop" already has a filed terminology
  contradiction against `blog-thoughtworks-gall-supervisory-engineering.md`
  (see [#1940](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1940),
  filed from `blog-addyosmani-own-the-outer-loop.md`), no new contradiction
  issue is filed here — this post's usage is identical to the already-flagged
  one, not a new collision.

## Concrete Artifacts

### The loop → harness → factory stack (as stated in the post)

```
Source: Addy Osmani, "Software Factories, Light and Dark,"
https://addyosmani.com/blog/software-factories/ (July 20, 2026)

Loop:     "one agent doing a single job on repeat: gather context, take an
          action, check the result, and go again until some condition is met."
Harness:  "the walls around a loop: the sandbox it runs in, the tools it can
          reach, the memory that survives between runs, and the gates that
          decide what 'done' means."
Factory:  "many harnessed loops running at once, fed by a queue of work and
          drained through a review gate into production, with humans owning
          the whole thing from above."

"Loop → harness → factory. A factory isn't a smarter agent; it's many
harnessed loops feeding one review gate, with a human owning the outer loop."
```

### "What earns a loop the dark" — criteria for unattended automation

```
Source: same post

A loop may run fully automated ("dark") only if:
  1. The check is cheap.
  2. The check runs at high frequency.
  3. The check relies on something that can't be easily faked out
     (a "green-or-red oracle") and doesn't drift over time.

Fits: type gates, property tests, a review agent with a real rubric.
Rule of thumb (attributed to Dex Horthy): an agent holds up for 3-10 steps,
then starts losing the thread past 20 steps, because of context
accumulation -- short loops are cheap to verify, sprawling loops hide
mistakes in the corners.

Worked safe-to-automate example (attributed to Dex Horthy): "a nightly
GitHub Actions cron that fixes exactly one anti-pattern, a lint violation
or a needlessly optional prop, commits, and opens one small pull request,
all on its own."

Keep the lights on (do NOT automate) when: "a wrong answer is expensive and
only a person can catch it" -- subtle production bugs, large blast radii,
decisions shaping a year or more of work.
```

### Architecture-as-safety-net practices (verbatim list)

```
Source: same post

"good types and method signatures so that mistakes are caught by the
compiler instead of in production; test seams where we can pin behavior
and make change observable; laying out the code so the next reader, human
or model, knows where to find the thing they care about; keeping call
stacks short and legible; keeping component boundaries well defined so a
change doesn't have a huge blast radius; and dependency injection so we
can swap out one piece for another."
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-own-the-outer-loop.md` Claim 7 (Anthropic RCT: 17-point
    comprehension-quiz gap, 50% vs. 67%) and Claim 2/3 (inner-loop = agent
    execution, outer-loop = human accountability, evidence-gated Verdict):
    this post's comprehension-debt mechanism (Claim 3) and inner/outer-loop
    close (Claim 10) both restate that post's already-settled claims in the
    dark/lit metaphor's vocabulary.
  - `blog-addyosmani-loop-engineering.md` (loop/harness distinction, "loop
    engineering sits one floor above the harness"): Claim 1 here adds the
    explicit third layer ("factory") on top of that post's two-layer stack.
  - `blog-addyosmani-code-agent-orchestra.md`, `blog-addyosmani-agentic-code-review.md`,
    `blog-addyosmani-own-the-outer-loop.md` (verification-is-the-bottleneck
    thesis, present across all three): Claim 5's "back pressure" rule and
    the funnel metaphor ("generation is a wide mouth; verification is the
    narrow neck") is a sharper, autonomy-budgeting version of the same
    thesis running through the author's own prior posts.
  - `blog-kentbeck-trust-factory.md` Claim 3 (XP practices reframed as
    trust-building mechanisms, not just productivity mechanisms): Claim 7
    here reframes standard architectural discipline as a safety net against
    agent mistakes via an independent route (verification economics rather
    than trust economics). Two different authors, same three-month window,
    converging on "standard engineering discipline now does double duty as
    AI-delegation infrastructure" — worth citing together.
  - `blog-anthropic-harness-long-running.md` Claim 10 (the evaluator is
    worth its cost only when the task exceeds solo model capability): the
    same task-relative cost-benefit logic underlies this post's Claim 8
    criteria for which loops may run dark.

- **Contradicts**: None filed. The closest tension is between Claim 4
  ("harness engineering is not enough" against long-run comprehension debt
  in complex/brownfield systems) and `blog-anthropic-harness-long-running.md`
  Claim 13 ("the space of interesting harness combinations doesn't shrink as
  models improve. Instead, it moves"). Per MINER.md §4a this was judged to be
  a difference in what's being claimed (harness *capability* tracking the
  model frontier vs. *unreviewed* pipelines accumulating an unrecoverable
  understanding gap regardless of harness quality), not a claim that would
  drive opposite guide advice — both could be true simultaneously. Flagged
  in Claim 4's assessment for the Assayer to double-check given the close
  titular echo ("Harness Engineering is not Enough" vs. Anthropic's harness
  post).

- **Extends**:
  - `blog-latentspace-aiewf-loops-software-factories-dispatch.md` (AIEWF
    day-2 dispatch, Claim 2: Allie Howe introduced the "Software Factories"
    track citing Geoffrey Huntley's "everything is a ralph loop"): this post
    is the corpus's first deep extraction of the *content* of Dex Horthy's
    named AIEWF talk ("Harness Engineering is not Enough: Why Software
    Factories Fail"), which the dispatch note does not cover directly (its
    Claim 2 covers only Howe's track-introduction framing, citing Huntley,
    not Horthy). No standalone Horthy/HumanLayer source note yet exists for
    the talk itself — this post is a secondhand route into its argument and
    should be flagged as a lead for a future Miner if a primary Horthy
    write-up or talk recording becomes available (see Extraction Notes).
  - `blog-humanlayer-skill-issue-harness-engineering.md` (Claim 8:
    "back-pressure" named as a harness configuration surface for filtering
    raw verification output): this post's Claim 5 uses "back pressure" for
    the higher-level autonomy-budgeting principle rather than the
    lower-level context-filtering mechanism — related but not identical
    usage of the same term by two different authors from the same broader
    HumanLayer/Horthy intellectual circle (Horthy co-founded HumanLayer).
  - `blog-addyosmani-intent-debt.md` Claim 10 (comprehension debt and intent
    debt are complementary, not overlapping, risks): this post's dark-factory
    framing is a specific instance of the comprehension-debt risk that note
    already names, applied narrowly to fully-unattended pipelines.

- **Novel**:
  - **"Dark factory" / "lit factory" as named, opposed terms**, borrowed
    explicitly from manufacturing's lights-out-factory precedent (FANUC
    since 2001, Xiaomi in 2024) — not present in any existing corpus source.
    Prior corpus "factory" mentions (`blog-ghaw-pelis-agent-factory-intro.md`,
    `docs-ghaw-agent-factory-status.md`, `blog-kentbeck-trust-factory.md`,
    `blog-latentspace-aiewf-loops-software-factories-dispatch.md`) use
    "factory" as a general production-pipeline metaphor without this
    specific dark/lit distinction or its criteria for which mode a given
    loop belongs in.
  - **Concrete "what earns a loop the dark" criteria** (Claim 8: cheap +
    high-frequency + unfakeable oracle) as an explicit decision checklist —
    more specific than any existing corpus source's treatment of "when can
    you trust an agent to run unattended."
  - **Bob Bemer's 1968 "The economics of program production" as the named
    historical origin of "software factory"** — new provenance information
    not present elsewhere in the corpus.
  - **Dex Horthy's 3-10-step / 20-step rule of thumb for loop verifiability**
    — a specific, quotable heuristic not previously in the corpus.
  - **The manufacturing lights-out-factory analogy itself** (FANUC, Xiaomi)
    as the explanatory device for why "dark" is the chosen term — new to the
    corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the loop → harness → factory
  three-layer stack (Claim 1) as the chapter's top-level structural framing,
  extending the existing loop/harness distinction from
  `blog-addyosmani-loop-engineering.md` with the explicit "factory" layer and
  its stated bottleneck (the review gate is the only non-scaling box). Add
  the "what earns a loop the dark" checklist (Claim 8) as a concrete
  decision tool for practitioners deciding which specific automations may
  run unattended — this is more actionable than the corpus's existing
  general verification-bottleneck guidance.

- **Chapter 02/03 boundary — the dark factory as a named risk**: Add "dark
  factory" (Claim 2) as a named, specific failure mode distinct from
  "insufficient review" as a general caution — it names the end state (a
  pipeline where literally no human reads any diff) rather than a vague
  warning about review quality. Pair with the comprehension-debt mechanism
  (Claim 3) and this corpus's existing settled evidence for the underlying
  phenomenon (`blog-addyosmani-own-the-outer-loop.md` Claim 7, the Anthropic
  RCT).

- **Chapter 03 (Verification)**: Add "back pressure" (Claim 5) as a named
  principle for autonomy budgeting: grant a loop only as much unattended
  autonomy as can be cheaply and reliably verified. Distinguish explicitly
  from `blog-humanlayer-skill-issue-harness-engineering.md`'s narrower
  "back-pressure" harness surface (filtering verification output) so the
  guide doesn't conflate the two uses of the same term under one definition.

- **Chapter 02 — Architecture as delegation infrastructure**: Add Claim 7's
  reframing of standard architectural discipline (types, seams, legible call
  stacks, bounded blast radius, DI) as a safety net specifically against
  agent mistakes, cited alongside `blog-kentbeck-trust-factory.md`'s
  independent XP-as-trust-factory reframing as two convergent arguments for
  why "boring" engineering discipline is not optional under AI acceleration.

- **Chapter 05 (Team Adoption)**: Add the lit-factory upstream-judgment
  argument (Claim 6 — review a 200-line plan instead of 2,000 lines of
  generated code) as a concrete cost justification for spec-first / design-
  review-first adoption patterns, alongside the existing `blog-osmani-good-spec.md`
  guidance.

## Extraction Notes

- Full article text was fetched via `curl` with a browser user-agent and
  converted from raw HTML to plain text with a Python stdlib tag-stripping
  pass (WebFetch's summarizer declined to reproduce quotable passages beyond
  short fragments when asked for the full text, consistent with the pattern
  noted in several other Osmani-post source notes in this corpus). All
  quotes above were checked against that raw-text extraction, not a
  summarized rendering.
- The post's central argument is explicitly presented as Osmani's synthesis
  of Dex Horthy's AIEWF talk ("Harness Engineering is not Enough: Why
  Software Factories Fail") — Osmani states he is giving "my take on" the
  talk's central slide. No link to a recording, slide deck, or primary
  Horthy write-up of the talk is given in the post, and no standalone corpus
  source note for that talk exists yet (see Cross-References → Extends).
  The four-month dark-factory failure anecdote (Claim 3) and the 3-10/20-step
  rule of thumb (Claim 8) are both attributed to Horthy secondhand through
  this post; a future Miner should attempt to locate and directly mine a
  primary Horthy/HumanLayer source for these two claims if one surfaces.
- No sub-pages were followed. The post contains no self-referential links to
  the author's own prior posts (unlike `blog-addyosmani-loop-engineering.md`
  and `blog-addyosmani-new-software-lifecycle.md`, which each linked several
  of the author's earlier pieces) — its cross-references in this note are
  this Miner's own inference from corpus knowledge, not links the post itself
  provides.
- The post ends with the line "Pangram scored this article as 100% human
  written" — an AI-detection-tool self-disclosure not otherwise substantive
  to any claim, noted here only because it is an unusual authorial choice
  (explicitly asserting the post itself was not AI-generated) that the
  Assayer may want context for if it appears in a quote check.
- One candidate contradiction was evaluated (Claim 4 vs.
  `blog-anthropic-harness-long-running.md` Claim 13) and judged not to meet
  the MINER.md §4a filing bar — see Cross-References → Contradicts for the
  full reasoning. No contradiction issue was filed.
- Cross-references to `blog-addyosmani-own-the-outer-loop.md`,
  `blog-addyosmani-loop-engineering.md`, `blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-agentic-code-review.md`, `blog-addyosmani-intent-debt.md`,
  `blog-kentbeck-trust-factory.md`, `blog-anthropic-harness-long-running.md`,
  `blog-humanlayer-skill-issue-harness-engineering.md`, and
  `blog-latentspace-aiewf-loops-software-factories-dispatch.md` were each
  re-read in full before citing; no claim numbers were guessed.
