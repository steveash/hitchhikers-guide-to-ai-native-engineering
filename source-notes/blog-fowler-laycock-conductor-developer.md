---
source_url: https://martinfowler.com/rachels-ramblings/conductor-developer.html
source_type: blog-post
title: "The Conductor Developer"
author: Rachel Laycock
date_published: 2026-07-31
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: anecdotal
issue: "#2385"
---

# The Conductor Developer

> Thoughtworks CTO Rachel Laycock argues that AI has not changed what good
> software looks like but has changed what's scarce — human attention — and
> that great developers are shifting from solo "flow" execution to
> orchestrating 8-12 parallel AI agents, a role she likens to a conductor
> holding the whole score in their head rather than playing every instrument.

## Source Context

- **Type**: blog-post (short first-person reflective essay, ~900 words,
  part of Laycock's "Rachel's Ramblings" series on martinfowler.com; explicitly
  framed by its own TL;DR as "capturing ideas before they're fully formed" —
  see the series bio: "This is where I capture ideas before they're fully
  formed, challenge my own thinking and occasionally wander off on interesting
  tangents.")
- **Author credibility**: Rachel Laycock is CTO at Thoughtworks (per her
  author byline and bio on the article page, linked to her LinkedIn profile:
  linkedin.com/in/rachellaycock/). She writes from personal first-hand
  observation ("when I watch developers using AI today...", "I was talking to
  an engineer recently...") and from her own experience transitioning into
  the CTO role, rather than from any cited study, survey, or named company
  case. This is a single senior practitioner/executive's reflective essay, not
  an empirical report — no data, no named companies (the "engineer" and
  "Chief People and Leadership Officer" she quotes are unnamed), no
  methodology.
- **Scope**: Covers a conceptual reframing of what is scarce in AI-assisted
  development (attention, not code-generation speed), a concrete practitioner
  data point about parallel-agent counts (8-12), the conductor/orchestra
  metaphor, and a parallel drawn to executive energy-management coaching.
  Does NOT cover: any specific tooling, harness configuration, CLAUDE.md-style
  guidance, concrete techniques for managing multiple agents, or any
  quantitative measurement of outcomes. It closes on an open question
  ("How do we redesign engineering careers...") rather than an answer.

## Extracted Claims

### Claim 1: AI has not changed what good software looks like; it has changed what is scarce — human attention is now the development bottleneck, following coding and (implicitly) design/verification as the bottleneck has moved through the delivery lifecycle
- **Evidence**: Author's own stated realization, presented as a correction to
  her own prior framing ("I was wrong").
- **Confidence**: anecdotal
- **Quote**: "AI didn’t change what great software looks like. It changed what’s scarce. Human attention is now the bottleneck."
- **Our assessment**: This is the article's organizing thesis. It is a
  plausible, well-articulated generalization from personal observation, not a
  measured finding — the author gives no data on where prior bottlenecks
  (coding, design, verification) actually sat before this shift, only that
  she "expected the bottlenecks to move through the software delivery
  lifecycle" and now believes attention is next. Worth citing as a framing
  device rather than a settled claim.

### Claim 2: The best developers Laycock knows are no longer spending their day in solo, uninterrupted "flow" — they are orchestrating multiple AI agents instead
- **Evidence**: Author's direct observation of practitioners she knows.
- **Confidence**: anecdotal
- **Quote**: "The best developers I know aren’t spending all day in flow anymore. They’re orchestrating agents."
- **Our assessment**: This is a sharp, quotable claim but rests entirely on
  the author's personal circle of observed developers — no count, no named
  examples, no comparison group. It sits in direct tension with
  `blog-thoughtworks-mugrage-is-developer-experience-dead.md` Claim 6, which
  frames the loss of flow state under agentic workflows as a cost
  ("context-switching noise... constantly interrupts deep problem-solving and
  flow state") rather than a positive evolution. See Cross-References —
  Contradicts below.

### Claim 3: Developers running multiple AI agents are functioning less like programmers and more like orchestra conductors — the conductor doesn't play every instrument but holds the whole system/score in their head, bringing in voices, changing tempo, and shaping the performance as it unfolds
- **Evidence**: Extended analogy drawn from watching musician Jacob Collier
  conduct.
- **Confidence**: anecdotal
- **Quote**: "He’s not trying to play every instrument himself. He’s listening to the whole piece, hearing what doesn’t quite fit, bringing different voices in at the right moment, changing the energy, changing the tempo and shaping the performance as it unfolds. Increasingly, that’s what great software developers look like."
- **Our assessment**: This is the article's namesake metaphor. It is a useful
  vocabulary device but not a mechanism — it doesn't specify how a developer
  actually decides "what doesn't quite fit" when reviewing agent output, only
  that this is the shape of the new role. Notably, this article's use of
  "conductor" to mean the human orchestrating multiple agents is the inverse
  of the terminology in `blog-addyosmani-code-agent-orchestra.md`, whose
  summary describes "moving from single-agent 'conductor' interaction to
  multi-agent 'orchestrator' management" — i.e. Osmani's piece uses
  "conductor" for the single-agent mode and "orchestrator" for the
  multi-agent mode, the opposite pairing from Laycock's. This is a
  terminology inconsistency across the corpus, not a substantive
  disagreement about what the multi-agent role entails.

### Claim 4: The conductor's value comes from understanding the whole score, not from superior instrumental skill — the orchestra needs a conductor because someone has to hold the whole system in their head, not because the musicians lack talent
- **Evidence**: Continuation of the Jacob Collier analogy, generalized to
  software development.
- **Confidence**: anecdotal
- **Quote**: "A great conductor is first and foremost a great musician. They could play the instruments themselves. That’s not why they’re standing on the podium. Their value comes from understanding the whole score. The orchestra doesn’t need the conductor because the musicians aren’t talented enough. It needs the conductor because someone has to hold the whole system in their head."
- **Our assessment**: This directly corroborates
  `blog-fowler-garg-orchestrator-tax.md` Claim 8, which argues from a
  separate, more technical incident that "the orchestrator is the only part
  of the system that accumulates understanding across a long session... The
  subagents don't, and that's by design." Laycock's musical framing and
  Garg's context-engineering framing converge independently on the same
  structural claim: the human/orchestrator's distinct value is holding
  system-level understanding that the individual agents/subagents don't
  retain.

### Claim 5: The developer-as-conductor's specific activities are deciding which agent tackles which problem, providing context, evaluating what comes back, spotting subtle mistakes, and deciding what needs another iteration versus what's ready to move on
- **Evidence**: Author's direct enumeration of orchestration activities.
- **Confidence**: anecdotal
- **Quote**: "They’re deciding which agent should tackle which problem. They’re providing context. They’re evaluating what comes back. They’re spotting subtle mistakes. They’re deciding what deserves another iteration and what is ready to move on."
- **Our assessment**: This enumeration maps closely onto the "three pillars"
  named independently by another Thoughtworks author in
  `blog-thoughtworks-gall-supervisory-engineering.md` Claim 7 (directing,
  evaluating, correcting): Laycock's "deciding which agent tackles which
  problem" and "providing context" correspond to Gall's "directing," her
  "evaluating what comes back" and "spotting subtle mistakes" correspond to
  Gall's "evaluating," and her "deciding what deserves another iteration"
  corresponds to Gall's "correcting." Two Thoughtworks-affiliated authors,
  writing independently (one as a conceptual framework piece on Thoughtworks
  Insights, one as a personal reflection on martinfowler.com), converge on
  essentially the same three-part taxonomy of the human's job when
  supervising agents, without citing each other.

### Claim 6: A practitioner reported regularly running eight AI agents in parallel, and the author has heard similar numbers — up to ten or twelve — from others, with attention becoming the constraint beyond that range
- **Evidence**: First-person anecdote from an unnamed engineer, corroborated
  by unspecified "others."
- **Confidence**: anecdotal
- **Quote**: "I was talking to an engineer recently who told me they regularly have eight AI agents running in parallel. I’ve heard similar numbers from others. Ten. Twelve. Beyond that, they become the bottleneck."
- **Our assessment**: This is the article's single most concrete, checkable
  data point, but it comes from unnamed sources with no methodology. It sits
  within — but toward the high end of — a range already established
  elsewhere in the corpus: `blog-addyosmani-code-agent-orchestra.md` Claim 8
  recommends a 3-5 agent "sweet spot" as a WIP limit while noting Boris
  Cherny "reportedly runs 15+," and
  `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 2 documents a
  non-technical PM running 15+ named subagents. Laycock's 8-12 figure sits
  between Osmani's conservative recommendation and the higher-end anecdotes,
  reinforcing that concurrent-agent counts vary widely by practitioner and
  task rather than converging on one number — a range/conditioning-variable
  situation, not a contradiction (per MINER.md §4a, differing numbers without
  a stated mechanism for why they differ don't rise to a filing-worthy
  contradiction).

### Claim 7: Managing multiple parallel AI agents resembles the author's own experience as a CTO managing many simultaneous streams of unstructured work (documents, decisions, guidance requests) rather than producing work herself
- **Evidence**: Author's first-person description of her own executive
  workload.
- **Confidence**: anecdotal
- **Quote**: "As CTO, I rarely produce the work myself anymore. Instead, I have lots of streams of work progressing at once. A strategy document comes back for feedback. A client opportunity needs a decision. Someone wants guidance on a technical trade-off. Another team needs context before they can move."
- **Our assessment**: This is the article's load-bearing analogy — executive
  cognitive load as a preview of what developer cognitive load is becoming.
  It's a single-person comparison (her own job to the conductor role), not
  independent evidence that the two are functionally equivalent, but it is a
  distinct angle from the existing corpus's PM-as-orchestrator case study
  (`blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 1, which argues
  project-management skill, not executive skill, transfers to agent
  orchestration). Laycock's version is specifically about executive-style
  attention/energy management, not PM-style task scoping and delegation —
  a related but distinct transferable-skill claim.

### Claim 8: What the author needed to learn as a new CTO was not time management but energy management — the real challenge was constant context switching, an endless stream of decisions, and the feeling that nothing was ever completely finished
- **Evidence**: Author's first-person account of her own transition into
  the CTO role.
- **Confidence**: anecdotal
- **Quote**: "What I really needed to learn was how to manage my energy. The challenge wasn’t the hours. It was the constant context switching. The endless stream of decisions. The feeling that nothing was ever completely finished."
- **Our assessment**: This names a specific cognitive-cost mechanism (energy
  depletion via context-switching and decision fatigue, distinct from raw
  time/hours) that closely parallels — from the opposite framing — the
  "context-switching noise" cost Mugrage names for agentic development
  workflows in `blog-thoughtworks-mugrage-is-developer-experience-dead.md`
  Claim 6 ("agentic workflows are inherently transactional... which
  constantly interrupts deep problem-solving and flow state"). Laycock
  frames this as a learnable executive skill to develop; Mugrage frames the
  developer-side equivalent as an unaddressed organizational cost driving
  burnout. Read together they describe the same underlying phenomenon
  (context-switching/decision-fatigue replacing flow as the dominant
  cognitive cost) from complementary angles — one prescriptive (learn to
  manage it, as executives have), one diagnostic (organizations haven't
  built support for it yet).

### Claim 9: An executive coach taught the author four practices for managing this kind of cognitive load: protect your attention, manage your energy, reduce unnecessary decisions, and create systems that help your brain rather than just your calendar
- **Evidence**: Author's first-person account of executive coaching she
  received.
- **Confidence**: anecdotal
- **Quote**: "Protect your attention. / Manage your energy. / Reduce unnecessary decisions. / Create systems that help your brain, not just your calendar."
- **Our assessment**: This is the article's most concrete, transferable
  artifact — four short, actionable principles (see Concrete Artifacts
  below). They are presented as executive-coaching wisdom being proposed for
  transfer to developers, not as developer-specific guidance already
  validated in that context — the author explicitly frames this as a
  hypothesis about what's coming, not a documented developer intervention.

### Claim 10: Organizations have spent decades building executive-coaching infrastructure (decision-making under incomplete information, cognitive load management, prioritization, energy protection) but have not yet begun building equivalent infrastructure for developers, even as the tools themselves are being redesigned around agent orchestration
- **Evidence**: Author's direct argument, prompted by a conversation with her
  company's Chief People and Leadership Officer.
- **Confidence**: anecdotal
- **Quote**: "we’ve spent decades helping executives succeed in this kind of environment. We coach them to make decisions with incomplete information, manage cognitive load, prioritize relentlessly and protect their energy. Yet we’re still preparing developers for a world of individual execution. We’re redesigning the tools, but we haven’t started redesigning the job."
- **Our assessment**: This is the article's most direct guide-relevant claim
  — it names a concrete organizational gap (coaching/career development for
  attention-management has not caught up to tooling change) rather than just
  describing the shift itself. It is corroborated qualitatively by the
  unnamed Chief People and Leadership Officer's quoted reaction ("I knew
  something fundamental was changing. I just didn’t know how to help. Now I
  do.") — though that is a single secondhand internal quote from an unnamed
  source, not independent verification.

### Claim 11: The shift is not developers becoming managers, nor AI replacing engineering — engineering expertise is being applied in a different, higher-leverage place because execution has become much faster, and this applies more broadly than software (the author suspects developers are simply the first knowledge workers to experience this)
- **Evidence**: Author's direct clarification, anticipating a likely
  misreading of her own argument.
- **Confidence**: anecdotal
- **Quote**: "I don’t think software developers are becoming managers. I don’t think AI is replacing engineering. I think engineering expertise is simply being applied in a different place, and much more often, because execution has become so much faster."
- **Our assessment**: This is a useful boundary-setting claim — it
  distinguishes the "conductor" framing from a "developers become people
  managers" reading, which is a common but distinct claim elsewhere (e.g. the
  PM-as-orchestrator framing in
  `blog-anthropic-vlasenko-pm-agent-orchestration.md`). It corroborates
  `blog-thoughtworks-mugrage-is-developer-experience-dead.md` Claim 3
  ("cognitive architect" who orchestrates rather than builds) and
  `blog-thoughtworks-jamieson-flow-game.md` Claim 9 (developer as
  "playmaker") in asserting the role changes in kind, not that it becomes
  people-management. The "first knowledge workers to experience it"
  extension to other professions is explicitly flagged by the author as an
  aside she hasn't developed ("I'll save that thought for another
  rambling") — worth citing only as a raised-but-unexplored idea.

## Concrete Artifacts

### The executive coach's four practices (verbatim, as a list)
```
Source: martinfowler.com/rachels-ramblings/conductor-developer.html

Protect your attention.
Manage your energy.
Reduce unnecessary decisions.
Create systems that help your brain, not just your calendar.
```

### The article's closing question (verbatim)
```
Source: martinfowler.com/rachels-ramblings/conductor-developer.html

"How do we redesign engineering careers when human attention becomes the
scarce resource?"
```

## Cross-References

- **Corroborates**:
  - `blog-fowler-garg-orchestrator-tax.md` Claim 8 (the orchestrator is the
    only part of a multi-agent system that accumulates understanding across
    a session; subagents are meant to be disposable) — this source's Claim 4
    (the conductor's value is holding the whole score/system in their head,
    not superior instrumental skill) independently arrives at the same
    structural claim via a musical rather than context-engineering framing.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 7 (supervisory
    engineering's three pillars: directing, evaluating, correcting) — this
    source's Claim 5 (deciding which agent tackles which problem, providing
    context, evaluating output, spotting mistakes, deciding on iteration)
    maps closely onto the same three-part taxonomy, from a second
    Thoughtworks-affiliated author writing independently.
  - `blog-thoughtworks-mugrage-is-developer-experience-dead.md` Claim 3 (the
    developer's role has shifted from builder to "cognitive architect" who
    orchestrates agents through high-level intent) and
    `blog-thoughtworks-jamieson-flow-game.md` Claim 9 (developer as
    "playmaker" who reads the play and supplies context) — this source's
    Claim 11 (engineering expertise applied in a different place, not
    developers becoming managers, not AI replacing engineering) is a third,
    independent naming of the same builder-to-orchestrator role shift.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 8 (WIP limits: 3-5 agent
    "sweet spot," with Boris Cherny "reportedly" running 15+) and
    `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 2 (a
    non-technical PM ran 15+ named parallel subagents) — this source's
    Claim 6 (practitioners running 8-12 parallel agents before attention
    becomes the bottleneck) is a third independent data point in the same
    range, reinforcing that concurrent-agent counts vary by practitioner
    rather than converging on a single number.

- **Contradicts**:
  - `blog-thoughtworks-mugrage-is-developer-experience-dead.md` Claim 6
    (agentic workflows are inherently transactional and constantly
    interrupt deep problem-solving and flow state, framed as an unaddressed
    cognitive cost driving burnout) versus this source's Claim 2 (the best
    developers "aren't spending all day in flow anymore. They're
    orchestrating agents," framed as a positive evolution of the role) and
    Claim 8 (moving from flow/time management to energy management is framed
    as a learnable, valuable executive-style skill). Both sources agree flow
    state is being displaced by a more fragmented, orchestration-style
    workflow; they diverge sharply on whether this displacement is
    presented as primarily a cost to be mitigated (Mugrage: "verification
    fatigue," "context-switching noise," burnout) or primarily a role
    evolution to be embraced and trained for (Laycock: conductor metaphor,
    executive-coaching parallel, no mention of burnout). This is a real
    difference in guide-relevant framing — whether the guide should present
    the loss of solo flow state as a problem DevEx practice must solve, or
    as a skill transition developers and organizations should invest in
    coaching for — so a contradiction issue has been filed:
    **See #2401** (Loss of developer flow state under AI agent orchestration:
    unaddressed burnout cost vs. embraced role evolution).

- **Extends**:
  - `blog-anthropic-vlasenko-pm-agent-orchestration.md` Claim 1
    (project-management skill transfers directly to multi-agent
    orchestration) — this source's Claim 7 (managing parallel agents
    resembles the author's own experience managing many simultaneous
    executive work streams) offers a second, distinct transferable-skill
    hypothesis: executive-style attention/energy management, rather than
    PM-style task scoping and delegation. The two sources together suggest
    at least two different management disciplines (PM and executive) may
    both be partially transferable to agent orchestration, via different
    mechanisms.

- **Novel**:
  - **The conductor/orchestra metaphor grounded in a specific analogy** (a
    named musician, Jacob Collier, observed conducting) is new phrasing to
    the corpus, though the underlying orchestrator-vs-worker-agent structure
    is already documented (see Corroborates above). Notably uses "conductor"
    for the opposite role than `blog-addyosmani-code-agent-orchestra.md`
    does (see Claim 3's assessment) — a terminology inconsistency worth
    flagging for the Smith if both sources are cited in the same guide
    section.
  - **The executive-coaching-to-developer-coaching transfer argument**
    (Claim 10) — no existing corpus source frames the developer/AI-agent
    attention-management skill gap specifically as a *coaching and career
    infrastructure* gap (as opposed to a tooling or process gap). This is
    the article's most distinctive, guide-relevant contribution.
  - **The four-practice executive-coaching artifact** (protect attention /
    manage energy / reduce unnecessary decisions / build brain-first
    systems) is not present in any existing corpus source in this exact
    form.

## Guide Impact

- **Chapter 04 or 05 (Team Dynamics / Career Redesign)**: Add Claim 10 (the
  organizational-coaching gap between executive attention-management
  training and developer attention-management training) as a specific,
  named gap for team-adoption and career-development discussions — this is
  more concrete than most "roles are changing" claims already in the corpus
  because it names *what kind of organizational support* is missing
  (coaching infrastructure), not just that the role is changing. Pair with
  the four-practice artifact (Concrete Artifacts) as a starting point for
  what that coaching might contain, explicitly caveated as borrowed from
  executive coaching and unvalidated in a developer context.

- **Chapter 02 or 04 (Multi-Agent Orchestration)**: Add the 8-12
  parallel-agent data point (Claim 6) alongside the existing 3-5 (Osmani) and
  15+ (Vlasenko, Cherny-via-Osmani) figures already in the corpus, to
  reinforce that any guide recommendation on concurrent-agent counts should
  be presented as a wide practitioner-observed range rather than a single
  number, with "attention becomes the bottleneck" as the qualitative signal
  for the ceiling rather than any fixed count.

- **Chapter 04/05 (whichever covers human-role framing)**: When citing this
  source's positive framing of the flow-to-orchestration shift (Claim 2),
  cross-reference the filed contradiction (#2401) against
  `blog-thoughtworks-mugrage-is-developer-experience-dead.md` so the guide
  does not present "developers moving away from flow state" as uniformly
  positive or uniformly negative — the two framings should be presented
  together as an open tension pending the contradiction's resolution.

## Extraction Notes

- WebFetch's summarizing pass on this URL returned a condensed, paraphrased
  ~200-word summary rather than the source's own wording (consistent with
  the copyright-caution behavior already documented in this corpus's other
  source notes, e.g. `blog-fowler-garg-orchestrator-tax.md` Extraction
  Notes). The full article was instead fetched via `curl` with a browser
  user-agent directly against the raw HTML, and every quote above was taken
  verbatim from the `paperBody` div of that HTML.
- The article links to two other pages: martinfowler.com's own
  "FutureOfSoftwareDevelopment" bliki entry (referenced only in passing, as
  "a topic for another ramble" the author explicitly declines to develop
  here) and the Wikipedia page for Jacob Collier (background on the musician
  used for the analogy, not itself a claim source). Neither was followed as
  a separate source, since the article does not develop either link's
  content into a claim of its own.
- This is a short, single-author reflective essay with no data, no named
  companies, and only unnamed secondhand quotes (the "engineer" and the
  "Chief People and Leadership Officer" are both unnamed) — confidence is
  set to `anecdotal` overall. The value of the piece for the guide is as a
  named framing/vocabulary contribution (conductor metaphor, the
  attention-as-bottleneck thesis, the executive-coaching-transfer argument)
  rather than as verified evidence of outcomes.
- A contradiction was identified against
  `blog-thoughtworks-mugrage-is-developer-experience-dead.md` on whether the
  loss of developer flow state under agent orchestration is best framed as
  an unaddressed burnout cost or an embraceable role evolution — filed as
  issue #2401 per MINER.md §4a. No verdict is asserted in this note; the
  verdict is left for the contradiction issue's resolution.
