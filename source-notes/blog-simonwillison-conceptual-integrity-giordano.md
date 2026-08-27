---
source_url: https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/
source_type: blog-post
title: "Conceptual integrity and counting lines of code"
author: Simon Willison (transcript excerpt of a conversation with Claire Giordano)
date_published: 2026-08-19
date_extracted: 2026-08-27
last_checked: 2026-08-27
status: current
confidence_overall: anecdotal
issue: "#2989"
---

# Conceptual Integrity and Counting Lines of Code

> Simon Willison posts two lightly-edited excerpts from his Talking Postgres
> podcast conversation with Claire Giordano: a defense of lines-of-code as a
> productivity metric that relocates the real constraint to team cognitive
> capacity, and an application of Fred Brooks' "conceptual integrity" (via
> the Winchester Mystery House analogy) to the risk that cheap agent-driven
> features erode architectural coherence once the time-cost discipline that
> used to gate feature requests disappears.

## Source Context

- **Type**: blog-post (Simon Willison's link/commentary blog, August 19,
  2026; a short post consisting of two "highlights" excerpted from "a
  lightly edited transcript" of an episode of the Talking Postgres podcast
  with Claire Giordano, topic "How AI is changing software development."
  Willison states the transcript was lightly edited with an explicit prompt
  to Claude: "very minor edits to remove disfluencies" — i.e., the excerpts
  are AI-cleaned spoken dialogue, not written prose.)
- **Author credibility**: Simon Willison is the creator of Django and one of
  the highest-signal independent AI-tooling commentators in the corpus
  (see `blog-simonwillison-vibe-coding-agentic-engineering.md`,
  `blog-simonwillison-james-shore-maintenance-costs.md`, and dozens of other
  notes). Claire Giordano hosts the Talking Postgres podcast; she is quoted
  directly for one analogy (Winchester Mystery House) but the bulk of the
  analytical content is Willison's own spoken argument. Willison's selection
  and re-publication of these two excerpts on his own blog is itself a
  relevance signal, consistent with how his other podcast-recap posts are
  treated in this corpus.
- **Scope**: Covers exactly two topics, each with a timestamp into the
  original recording: (1) at 35:01, why lines-of-code can be a meaningful
  productivity signal for coding agents specifically, and why team size
  remains necessary despite single-engineer throughput gains; (2) at 46:03,
  conceptual integrity (from *The Mythical Man-Month*) and how the falling
  cost of adding a feature erodes the discipline that used to enforce
  architectural coherence, illustrated via the Winchester Mystery House.
  Does NOT cover: specific tooling, measured data, team processes, or any
  content from the rest of the ~47+ minute episode outside these two
  excerpts. The post explicitly frames these as "a couple of my highlights,"
  not a full transcript or summary of the episode.

## Extracted Claims

### Claim 1: Lines of code is a meaningful productivity metric for coding agents because there is a known, hard human baseline to compare against — a few hundred LOC/day, with 200 debugged/tested/production lines being an unusually good day and 50-60 the typical case

- **Evidence**: Willison's own stated argument, offered as a rebuttal to the
  conventional wisdom that LOC is meaningless as a productivity measure. He
  grounds the claim in a specific numeric baseline for pre-agent human
  output.
- **Confidence**: anecdotal (a single practitioner's stated argument and
  self-estimated baseline numbers; not measured or surveyed)
- **Quote**: "A lot of people will tell you it makes no sense to measure productivity in lines of code. I'd actually disagree, because there's a hard limit. In the before-times, a software engineer could produce a few hundred lines of production-ready code per day — and 200 lines of working, debugged, production-level code is an incredibly good day. Most days you'd produce 50 or 60."
- **Our assessment**: This is a direct, named rebuttal of "LOC is a bad
  metric" orthodoxy, but it is narrower than it first appears: Willison is
  not defending LOC as a general engineering KPI, he is defending it as a
  before/after comparison point specifically for coding-agent throughput,
  conditional on quality holding (see Claim 2). The 200 LOC/day "good day"
  and 50-60 LOC/day "typical day" figures are close in order of magnitude to
  the ~200 LOC/day baseline Willison used in
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7 ("The SDLC
  was designed for ~200 LOC/day and does not scale to 2,000 LOC/day"), which
  strengthens confidence that this is a stable personal estimate rather than
  an offhand number invented for this specific conversation.

### Claim 2: A thousand lines of agent-produced debugged code per day is "a very meaningful improvement" over the human baseline, but only if code quality (maintainability, test coverage) is held constant — and achieving that quality bar with agents requires a large amount of skill, knowledge, and experience, which is what distinguishes senior engineers

- **Evidence**: Direct continuation of Willison's own argument, explicitly
  conditioning the "1000 LOC/day is meaningful" claim on quality parity.
- **Confidence**: anecdotal (practitioner claim; the ~5x jump from "200 good
  day" to "1000 lines" is Willison's own illustrative number, not measured)
- **Quote**: "If agents let you produce a thousand lines of debugged code, that really is a very meaningful improvement — as long as the code is the same quality: maintainable, tested, all of that. You can get to that point with agents, but it takes a huge amount of skill and knowledge and experience. That's what senior engineers are made of."
- **Our assessment**: The load-bearing qualifier is "as long as the code is
  the same quality" — Willison is not claiming agents produce 5x more
  *good* code by default, only that 5x more good code is possible and
  meaningful when a skilled engineer drives the agent. This is consistent
  with the corpus's dominant finding that agent-driven velocity gains
  degrade code quality unless actively managed (`paper-miller-speed-cost-quality.md`
  Claim 2, 41.6% persistent cognitive-complexity increase after Cursor
  adoption; `blog-simonwillison-james-shore-maintenance-costs.md` Claim 1,
  the inverse-maintenance-cost requirement). Willison's framing implicitly
  agrees with Shore and Miller et al.: the quality-preserving version of
  high-LOC agent output is the hard, skill-gated case, not the default case.

### Claim 3: Even with a single engineer able to do far more work via agents, teams remain necessary because the limiting factor shifts from code-production speed to cognitive capacity to stay on top of the code — teams exist to load-balance that cognitive capacity, not to add more hands for typing code

- **Evidence**: Willison's own argument, explicitly posed as an answer to
  the rhetorical question "why should a company have more than one
  engineer?" if a single engineer's agent-assisted throughput is high
  enough.
- **Confidence**: anecdotal (single practitioner's reasoning; not measured
  or surveyed; though internally consistent with his other stated positions)
- **Quote**: "I can do way more work as a single engineer than I could without agents. So you could argue, why should a company have more than one engineer? Beyond the obvious bus factor thing — a team of one is a very badly designed team — the answer is that the new limiting factor is cognitive capacity. I can churn out code a hundred times faster. I don't have the cognitive capacity to stay on top of 100 times the amount of code. So you still need a team of engineers, so you can load balance that cognitive capacity across the team."
- **Our assessment**: This is a specific and useful reframing for the team-
  design chapters: it names *why* teams persist under agent-driven velocity
  gains (cognitive-capacity load-balancing) rather than the more common
  framing of "teams exist because there's more code to write." It is
  compatible with, and adds a mechanism to, `blog-thebatch-ng-aiteam-structure.md`
  Claim 6 (small 2-10 person AI-native teams favor generalists) — Ng
  describes the resulting team *shape*; Willison names the underlying
  *reason* teams don't shrink to one person despite per-engineer throughput
  gains. Note the "hundred times faster" figure here is casual hyperbole
  relative to the "thousand lines" (roughly 5x-20x the "good day" baseline)
  figure two paragraphs earlier in the same excerpt — Willison is not
  internally precise about the multiplier, and the guide should treat the
  qualitative claim (cognitive capacity, not code-typing capacity, is now
  the bottleneck) as the durable takeaway rather than either specific number.

### Claim 4: Well-designed software has "conceptual integrity" (a term from *The Mythical Man-Month*) — no surprises, exactly the right domain of coverage, everything fitting together — and this is much harder to maintain with coding agents, because an engineer can conceive of a feature, prompt for it, and have it built minutes later, causing the software to "grow little weird bumps in funny different directions"

- **Evidence**: Willison's own argument, explicitly citing Fred Brooks' *The
  Mythical Man-Month* by name and applying the "conceptual integrity"
  concept to agent-driven feature addition.
- **Confidence**: anecdotal (a named concept borrowed from a classic text,
  applied by a single practitioner to a new context; not measured)
- **Quote**: "There's a concept in The Mythical Man-Month — conceptual integrity — where well-designed software has an integrity to it: there are no surprises in it, it covers exactly the right domain of things, everything fits together and makes sense. That's so much harder with coding agents, where you can have an idea for a feature, run a prompt, and five minuteslater you've got the feature. Your software grows little weird bumps in funny different directions."
  (Note: "five minuteslater" is reproduced exactly as it appears in the
  source's raw HTML — verified directly against the page source, not a
  transcription artifact introduced during extraction.)
- **Our assessment**: This is the most novel and guide-relevant claim in the
  source. No existing corpus note names conceptual integrity or *The
  Mythical Man-Month* explicitly, despite the corpus containing substantial
  adjacent coverage of complexity growth under agent-driven development
  (`paper-miller-speed-cost-quality.md` Claim 2, persistent complexity
  increase) and of the SDLC's throughput assumptions breaking down
  (`blog-simonwillison-vibe-coding-agentic-engineering.md` Claims 7-8).
  Willison's contribution is a *mechanism* for those measured outcomes: it
  is not merely that agents produce more, lower-quality code on average — it
  is that the marginal cost of proposing and shipping a feature has dropped
  low enough that features get added without the deliberative pause that
  used to filter out architecturally-incoherent ideas. This is a causal
  claim underneath Miller et al.'s complexity measurement, parallel to how
  Shore's maintenance-cost model provides a causal mechanism for the same
  measurement from an economic angle.

### Claim 5: Claire Giordano frames the conceptual-integrity erosion problem using the analogy of the Winchester Mystery House — a house continuously and incoherently expanded over decades

- **Evidence**: Direct quote attributed to Giordano in the transcript
  excerpt, immediately following Willison's conceptual-integrity
  explanation.
- **Confidence**: anecdotal (an analogy offered in conversation, not an
  argued claim with evidence of its own)
- **Quote**: "You know my analogy for that? The Winchester Mystery House."
- **Our assessment**: The analogy itself carries no independent evidentiary
  weight — it is illustrative, not argumentative — but it is a citable,
  memorable framing device for the guide to use when explaining conceptual-
  integrity erosion to practitioners. See Claim 6 for Willison's elaboration
  of the analogy's specifics.

### Claim 6: Willison elaborates the Winchester Mystery House analogy (140 rooms added over 40 years by a widow who believed she needed to keep building to appease ghosts) as a direct parallel to coding agents: the "rooms" (features) keep getting added because the cost of adding them has dropped so much, and the result is that conceptual integrity falls apart, making subsequent decisions about the software harder

- **Evidence**: Willison's own elaboration and explicit parallel-drawing
  between the historical anecdote and the coding-agent situation.
- **Confidence**: anecdotal (an analogy elaborated by the author; the
  "it's harder to make decisions about it" consequence is asserted, not
  measured)
- **Quote**: "It's got 140 rooms, because the woman who built it was the widow of the guy who invented the Winchester rifle, and her psychic told her she'd be haunted by the ghosts of everyone killed with that rifle unless she kept building the house forever. So for 40 years she kept adding new rooms. [...] That's exactly the problem with coding agents and software: it's very easy to keep adding new rooms, because the cost of adding those rooms is so much cheaper. What you end up with is something where the conceptual integrity falls apart — and then it's harder to make decisions about it."
- **Our assessment**: The specific downstream harm named here — "it's harder
  to make decisions about it" — is a distinct claim from the complexity/
  maintainability harms already well-documented in the corpus (harder to
  read, harder to test, more static-analysis warnings). Willison is naming
  a decision-quality cost: once conceptual integrity is gone, evaluating
  *which* future changes are architecturally sound becomes harder because
  there is no longer a coherent design to reason against. This is a
  plausible but unmeasured extension of the corpus's complexity-cost
  findings, and should be flagged in the guide as an argued-but-unmeasured
  risk rather than an established one.

### Claim 7: The discipline that used to prevent conceptual-integrity erosion was not deliberate design governance — it was simply the amount of time a feature took to build, which forced engineers to only pursue ideas they could justify against that time cost; when the time cost drops to an hour, that same idea becomes far easier to justify

- **Evidence**: Willison's own closing synthesis of the two-part argument
  (LOC/cognitive-capacity and conceptual integrity), presented as the
  unifying explanation for both halves of the excerpt.
- **Confidence**: anecdotal (a synthesizing claim, argued but not measured)
- **Quote**: "It all keeps coming back to discipline. It used to be that the discipline was enforced on you by the amount of time it took. You'd come up with an idea for a crazy feature and think 'yeah, but that would take me a week — I cannot justify that, so I'll forget about it.' If it takes an hour, it's so much easier to justify."
- **Our assessment**: This is the strongest and most guide-actionable claim
  in the source: it identifies effort-cost as a *hidden* design-governance
  mechanism that architecture discipline never had to formalize, because it
  was structurally guaranteed by the pre-agent economics of software
  production. Coding agents remove that guarantee without replacing it,
  which means teams must now *actively choose* to install the discipline
  that used to be free. This directly parallels Charity Majors' claim in
  `blog-simonwillison-charity-majors-code-economics.md` Claim 4 ("AI demands
  more engineering discipline. Not less") but supplies the specific
  mechanism Majors' excerpt does not: the discipline in question is
  architectural/scope discipline gated by feature cost, not general
  code-quality discipline gated by review rigor. The two sources should be
  read together: Majors names the normative conclusion (more discipline
  needed), Willison names one specific, previously-invisible discipline
  mechanism (time-cost-as-gatekeeper) that AI adoption silently deletes.

## Concrete Artifacts

### Full excerpt structure (verbatim, from the raw page HTML)

```
Source: Simon Willison, simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/
Published: 19th August 2026, 10:46pm
Context line (verbatim): "Last week I recorded an episode of the Talking
Postgres podcast with Claire Giordano on the subject of "How AI is changing
software development". We had a really great conversation. Here are a
couple of my highlights from a lightly edited transcript (prompt to Claude:
"very minor edits to remove disfluencies")."

Excerpt 1 — timestamp 35:01, "lines of code" argument (Willison, uninterrupted)
Excerpt 2 — timestamp 46:03, "conceptual integrity" section (Willison + Giordano dialogue)

Post-script (verbatim): "(Side-note: the Wikipedia article includes credible
sources that dispute the story about the psychic.)"

Tags: ai, generative-ai, llms, podcast-appearances, coding-agents
```

### The LOC/cognitive-capacity argument (verbatim, timestamp 35:01)

```
Source: simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/

"A lot of people will tell you it makes no sense to measure productivity in
lines of code. I'd actually disagree, because there's a hard limit. In the
before-times, a software engineer could produce a few hundred lines of
production-ready code per day — and 200 lines of working, debugged,
production-level code is an incredibly good day. Most days you'd produce 50
or 60.

If agents let you produce a thousand lines of debugged code, that really is
a very meaningful improvement — as long as the code is the same quality:
maintainable, tested, all of that. You can get to that point with agents,
but it takes a huge amount of skill and knowledge and experience. That's
what senior engineers are made of.

I can do way more work as a single engineer than I could without agents. So
you could argue, why should a company have more than one engineer? Beyond
the obvious bus factor thing — a team of one is a very badly designed team —
the answer is that the new limiting factor is cognitive capacity. I can
churn out code a hundred times faster. I don't have the cognitive capacity
to stay on top of 100 times the amount of code. So you still need a team of
engineers, so you can load balance that cognitive capacity across the team."
```

### The conceptual integrity dialogue (verbatim, timestamp 46:03)

```
Source: simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/

Simon: "There's a concept in The Mythical Man-Month — conceptual integrity —
where well-designed software has an integrity to it: there are no surprises
in it, it covers exactly the right domain of things, everything fits
together and makes sense. That's so much harder with coding agents, where
you can have an idea for a feature, run a prompt, and five minuteslater
you've got the feature. Your software grows little weird bumps in funny
different directions."

Claire: "You know my analogy for that? The Winchester Mystery House."

Simon: "It's got 140 rooms, because the woman who built it was the widow of
the guy who invented the Winchester rifle, and her psychic told her she'd be
haunted by the ghosts of everyone killed with that rifle unless she kept
building the house forever. So for 40 years she kept adding new rooms.

That's exactly the problem with coding agents and software: it's very easy
to keep adding new rooms, because the cost of adding those rooms is so much
cheaper. What you end up with is something where the conceptual integrity
falls apart — and then it's harder to make decisions about it.

It all keeps coming back to discipline. It used to be that the discipline
was enforced on you by the amount of time it took. You'd come up with an
idea for a crazy feature and think 'yeah, but that would take me a week — I
cannot justify that, so I'll forget about it.' If it takes an hour, it's so
much easier to justify."
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7 ("The
    SDLC was designed for ~200 LOC/day and does not scale to 2,000 LOC/day")
    and Claim 8 (the SDLC's throughput assumption is now false): this
    source's ~200 LOC/day human baseline (Claim 1) and its team-of-one
    thought experiment (Claim 3) are the same throughput-disruption argument
    Willison has made before, now extended with the cognitive-capacity
    mechanism for why teams persist despite the disruption. The two sources
    share the same author and the same underlying LOC/day estimate, three
    months apart, which strengthens confidence that ~200 LOC/day is a
    stable personal estimate rather than an ad hoc number.
  - `blog-simonwillison-charity-majors-code-economics.md` Claim 4 ("AI
    demands more engineering discipline. Not less"): Claim 7 in this note
    supplies the specific discipline mechanism (time-cost-as-architectural-
    gatekeeper) that Majors' normative claim does not name. Read together,
    Majors states the conclusion and Willison supplies one concrete
    mechanism for why it is true.
  - `blog-simonwillison-james-shore-maintenance-costs.md` Claim 1 (AI tools
    only produce net benefit if maintenance cost drops by the inverse of the
    productivity multiplier) and Claim 5 (current agents appear to increase,
    not decrease, maintenance costs): this source's Claim 2 (quality parity
    is a hard, skill-gated condition for high-LOC output to be "meaningful")
    is consistent with Shore's economic framing — both treat "more code,
    same quality" as the difficult, non-default case.
  - `paper-miller-speed-cost-quality.md` Claim 2 (41.6% persistent increase
    in cognitive complexity post-Cursor-adoption): Willison's Claims 4 and 6
    (conceptual integrity erosion, "little weird bumps in funny different
    directions") describe, from a design-narrative angle, the same
    phenomenon Miller et al. measure empirically as rising cognitive
    complexity. Willison supplies a plausible causal mechanism (dropped
    feature-addition cost removing the discipline that used to gate scope
    creep) for an outcome the corpus has so far only measured, not explained.
  - `blog-thebatch-ng-aiteam-structure.md` Claim 6 (small 2-10 person
    AI-native teams favor generalists over deep specialists): compatible
    with this source's Claim 3 (teams persist to load-balance cognitive
    capacity, not to add code-typing hands). Ng describes the resulting team
    shape; Willison names the underlying capacity-allocation reason teams
    of one remain "badly designed" even when a single engineer's raw
    throughput is very high.

- **Contradicts**: None filed. No existing corpus note stakes out the
  opposing position that lines-of-code is categorically meaningless as a
  productivity signal for agent-assisted work (the corpus's existing LOC
  coverage — `paper-miller-speed-cost-quality.md`'s velocity measurements,
  `blog-simonwillison-vibe-coding-agentic-engineering.md`'s throughput
  claims — measures LOC change without taking a normative position on
  whether LOC is a *good* metric), so Willison's defense of LOC-as-signal
  does not materially oppose a specific existing claim. Checked open
  `contradiction`-labeled issues and `CONTRADICTIONS.md` before concluding
  this; no LOC-metric-validity entry exists there.

- **Extends**: `blog-simonwillison-james-shore-maintenance-costs.md` and
  `paper-miller-speed-cost-quality.md` by supplying a design-discipline
  causal mechanism (Claims 4, 6, 7) for complexity/maintenance-cost outcomes
  those sources measure or model but do not explain in architectural terms.

- **Novel** (not present elsewhere in the corpus):
  - **"Conceptual integrity" and *The Mythical Man-Month*, named explicitly**:
    no other source note in the corpus cites Brooks' term or book directly,
    despite substantial adjacent coverage of complexity growth.
  - **The Winchester Mystery House analogy**: a specific, citable framing
    device for explaining architectural incoherence-through-accumulation to
    practitioners, not found elsewhere in the corpus.
  - **Time-cost-as-hidden-architectural-governance**: the specific
    observation that the discipline preventing feature bloat was never a
    formal process — it was an emergent property of code being expensive to
    produce — and that this governance mechanism silently disappears under
    agent-driven development unless replaced deliberately.
  - **The "load balance cognitive capacity across the team" framing** for
    why teams persist despite per-engineer throughput multipliers: distinct
    from the corpus's existing team-shape claims (Ng's generalist/ratio
    observations), this names the underlying resource being distributed
    (cognitive capacity to stay on top of code) rather than the resulting
    team composition.

## Guide Impact

- **Chapter 02 (or wherever the guide discusses productivity metrics)**:
  Add Willison's conditional defense of LOC-as-signal (Claims 1-2): LOC can
  be a legitimate agent-productivity indicator *only* when paired with an
  explicit quality-parity check (tested, maintainable, reviewed) — cite
  alongside Miller et al.'s complexity findings so the guide does not
  present raw LOC growth as inherently positive. Currently the guide has no
  explicit position reconciling "LOC went up" with "is that good" for
  agent-assisted teams; this source, read with Miller et al. and Shore,
  supports the recommendation: track LOC alongside cognitive-complexity and
  maintenance-cost metrics, never LOC alone.

- **Chapter 03/04 (team design / cognitive load)**: Add Claim 3's framing —
  teams exist post-agent-adoption to load-balance cognitive capacity across
  the codebase, not to add code-production hands — as an explicit
  explanation for why "why not just have one 100x engineer?" is the wrong
  question. Pair with `blog-thebatch-ng-aiteam-structure.md` Claim 6 for the
  resulting small-generalist-team shape this reasoning implies.

- **Chapter on architecture/software design under agents (wherever the
  guide discusses maintaining coherent system design)**: This is the
  source's highest-value contribution. Recommend adding a named "conceptual
  integrity" section that: (1) defines the term via Brooks/Willison; (2)
  states the mechanism explicitly — falling feature-cost removes the
  implicit time-cost gatekeeper that used to filter architecturally
  incoherent feature ideas; (3) recommends that teams install an explicit,
  deliberate substitute for that discipline (e.g., architectural review
  gates, an explicit "does this fit the product's actual domain" check
  before implementation) rather than assuming code review alone will catch
  scope-incoherence the way time-cost used to. This is currently absent from
  the guide's coverage of complexity growth, which (via Miller et al. and
  Shore) documents the *symptom* (rising complexity, rising maintenance
  cost) without naming this specific *mechanism* (discipline-through-effort
  silently disappearing).

## Extraction Notes

- The source is short (two excerpts, ~500 words total of transcript
  content) but dense; both excerpts were read in full via two independent
  fetches — a WebFetch summary pass and a direct raw-HTML text extraction
  (curl + tag-stripping) — and cross-checked against each other. All quotes
  in this note were copied from the raw-HTML extraction, which preserves
  exact source punctuation and spacing.
- The apparent typo "five minuteslater" (missing space) in Claim 4's quote
  was verified directly against the page's raw HTML source (via `curl`, not
  the rendered/JS view) to confirm it is present in the source itself and
  not an artifact introduced by this extraction's tooling — there is no
  intervening HTML tag between "minute" and "later" in the source markup.
  It is reproduced verbatim per the no-alteration rule in MINER.md §2a.
  Reviewers checking this quote against the live page should expect to see
  the same missing space.
  Editor's note (not in source): the sentence should read "...and five
  minutes later you've got the feature."
- The full ~47-minute Talking Postgres podcast episode itself was not
  located or fetched; extraction is limited to Willison's own two excerpts
  as published on his blog, consistent with the post's framing as "a couple
  of my highlights" rather than a full transcript. If the guide later needs
  more of the episode's content, the primary episode should be sourced
  directly from the Talking Postgres podcast feed, not reconstructed from
  this post.
- No contradiction was found requiring a filed issue. See the Contradicts
  entry under Cross-References for the reasoning.
- Cross-reference verification performed before writing: all cited claim
  numbers were re-read from their source notes in this session immediately
  before citing them —
  `blog-simonwillison-vibe-coding-agentic-engineering.md` Claim 7 (line 162)
  and Claim 8 (line 182); `blog-simonwillison-charity-majors-code-economics.md`
  Claim 4 (line 111); `blog-simonwillison-james-shore-maintenance-costs.md`
  Claim 1 (line 50) and Claim 5 (line 130); `paper-miller-speed-cost-quality.md`
  Claim 2 (line 51); `blog-thebatch-ng-aiteam-structure.md` Claim 6 (line 133).
  All verified against the actual claim text at those locations.
- Confidence rated `anecdotal` overall: every claim in this source is a
  single practitioner's stated argument or an analogy offered in
  conversation — none is backed by measurement, survey, or citation to
  external data. The value of the source is analytical framing and
  vocabulary (conceptual integrity, Winchester Mystery House, cognitive-
  capacity load-balancing), not empirical evidence. The guide should cite it
  for framing and terminology, and pair it with the corpus's measured
  sources (Miller et al., Shore) wherever an empirical backstop is needed.
