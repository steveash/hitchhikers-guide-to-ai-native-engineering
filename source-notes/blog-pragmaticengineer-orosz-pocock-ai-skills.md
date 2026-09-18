---
source_url: https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock
source_type: blog-post
title: "AI Skills with Matt Pocock"
author: Gergely Orosz (interviewing Matt Pocock)
date_published: 2026-09-17
date_extracted: 2026-09-18
last_checked: 2026-09-18
status: current
confidence_overall: anecdotal
issue: "#3534"
---

# AI Skills with Matt Pocock

> A Pragmatic Engineer podcast interview in which Matt Pocock — creator of
> the 230,000-star `grill-me`/`wayfinder` skills repo and the AI Hero course —
> walks through his working practice for AI-assisted development: borrowing
> John Ousterhout's tactical/strategic programming split to argue agents have
> "eaten" tactical work, a spec-then-tickets planning pipeline driven by a
> ~150K-token single-session ceiling, "leading words" mined from classic
> software-engineering books (tracer bullets, vertical slices, deep modules,
> ubiquitous language) to steer agent behavior via the model's own training
> priors, "memento-driven development" (optimizing a codebase for an agent
> that wakes up with no memory every session), a day-shift/night-shift
> planning-then-AFK-delegation rhythm, a move from local to cloud/"multiplayer"
> agents, and a self-described "mixed" but pragmatic take on TDD for agents.

## Source Context

- **Type**: blog-post (podcast episode page, Pragmatic Engineer newsletter,
  newsletter.pragmaticengineer.com; published 2026-09-17; a long-form
  interview/conversation, not a written essay)
- **Author credibility**: Gergely Orosz is the interviewer; see this corpus's
  existing profile of him via `blog-pragmaticengineer-orosz-loop-engineering.md`,
  `blog-pragmaticengineer-orosz-horthy-context-engineering.md`, and
  `blog-pragmaticengineer-orosz-kentbeck-career.md`. The interview subject,
  Matt Pocock, is an independently-established voice in AI-assisted
  engineering practice — per this episode's own framing, creator of the
  `grill-me` and `wayfinder` skills (a repo the episode states is "now the
  second most starred skills repo in the world" at "230,000 stars"), the
  Total TypeScript course (">$2.5 million in total sales" per the episode
  description), and the AI Hero course. He is independently corroborated
  elsewhere in this corpus: `blog-latentspace-macmanus-wayfinder-skill.md`
  (a dedicated Latent Space interview about `wayfinder`),
  `blog-pragmaticengineer-orosz-loop-engineering.md` (his "dynamic Kanban"
  Ralph-loop variant), `blog-humanlayer-show-me-skill.md` (named among
  practitioners reacting to HumanLayer's `show-me` skill), and
  `blog-pragmaticengineer-orosz-code-review-approaches.md` (a third party,
  Andrea Francesco Speziale, independently endorsing `/grill-me` as a
  review-replacement workflow). This is a first-party practitioner interview
  — all claims about what works originate from Pocock's own described
  experience, not an independent evaluation.
- **Scope**: Covers Pocock's career background (voice coach to developer to
  educator), the origin and mechanics of the `grill-me` and `wayfinder`
  skills, a spec-then-tickets planning pipeline, the "leading words" concept
  for steering agents via classic software-engineering vocabulary,
  "memento-driven development," domain-driven-design-inspired skill work
  (`Grill with Docs`), cloud vs. local agent infrastructure, day-shift/
  night-shift delegation, his TDD stance, tech-debt/code-review automation,
  and closing career advice. Does NOT cover: the skills' full prompt/
  instruction text verbatim (only fragments are quoted in the interview
  itself), any usage metrics beyond GitHub star counts and course revenue,
  or independent verification of any effectiveness claim — this is entirely
  Pocock's own first-person account of his practice, delivered conversationally.

## Extracted Claims

### Claim 1: Borrowing John Ousterhout's tactical-vs-strategic-programming framework, Pocock argues AI agents have "largely eaten" tactical programming, leaving engineers to operate mainly at the strategic level
- **Evidence**: Pocock's own stated framework, explicitly attributed to
  Ousterhout (whom Orosz had separately interviewed, per
  `blog-pragmaticengineer-orosz-loop-engineering.md`'s and this transcript's
  own reference list, "The Philosophy of Software Design – with John
  Ousterhout").
- **Confidence**: anecdotal
- **Quote**: "I know you had John Asterhow on this podcast. I've been really
  wanting to chat to him myself. Like he's a huge influence on me. And he
  talks about the difference between tactical programming and strategic
  programming. AI has largely eaten tactical programming in my view, and
  it's up to us to handle the strategic."
- **Our assessment**: This is a clean, quotable framing device — not a
  measured claim, but a useful vocabulary borrow (from a named, credentialed
  source, Ousterhout's *A Philosophy of Software Design*) for describing
  where human judgment should concentrate as agents absorb routine
  implementation work. No prior corpus source applies the tactical/strategic
  split specifically to the human/agent division of labor; this is a novel,
  reusable framing for the guide (see Novel below).

### Claim 2: The `grill-me` skill — "interview the user relentlessly" — was inspired by a colleague's approach of having an agent interview its user, and has become Pocock's most popular skill by a wide margin
- **Evidence**: Pocock's own origin story plus a concrete adoption signal
  (GitHub star count for the skills repo as a whole).
- **Confidence**: anecdotal
- **Quote**: "this very, very simple skill, it's really just telling the
  agent to interview you relentlessly about the topic. It's a very small
  skill. It just has this weird emergent behaviour with it, where the models
  just start thinking a little bit outside the box." / "I think I got it
  originally from like a Tariq who works at ClawCode. He's saying basically
  get the agent to interview you and then you'll see better results."
- **Our assessment**: This corroborates `blog-latentspace-macmanus-wayfinder-skill.md`'s
  Source Context profile of Pocock as an active cross-pollinating
  skill-builder, and independently corroborates
  `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 10, which
  quotes a *different* practitioner (Speziale) independently praising
  `/grill-me` for the same reason (upfront alignment eliminating the need
  for later review). The attribution passage ("a Tariq who works at
  ClawCode") is very likely an auto-caption mis-transcription of "Thariq
  [Shihipar]" and "Claude Code" — see Extraction Notes; quoted verbatim
  rather than corrected.

### Claim 3: Grill-me's real value is closing a "communication gap" between human and agent — establishing scope and values, not just implementation details — because even the smartest models "can't read your mind"
- **Evidence**: Pocock's stated rationale for why a simple interview skill
  produces outsized results.
- **Confidence**: anecdotal
- **Quote**: "There is a communication gap between you and the agent, right?
  ... the agent, however good it is, however smart the model is, you know,
  even mythos, it can't read your mind." / "Grill Me is not only about
  implementation details. It's also about establishing, okay, do this. This
  is in scope. This is not in scope. Here's what I think is important. And
  so it's the agent getting to know you."
- **Our assessment**: This reframes `grill-me` as a scope/values-alignment
  tool rather than a spec-completeness tool — a distinction the guide's
  existing `wayfinder`-focused coverage does not make explicit. It's an
  assertion about *why* the skill works, not a tested mechanism, but it is
  a specific, actionable framing: use interrogation to surface unstated
  constraints and priorities, not only missing implementation detail.

### Claim 4: The `wayfinder` skill structures planning as a map (accumulated decisions) with typed tickets navigated through a "fog of war," and Pocock has run maps of 50-100 tickets across both engineering and non-engineering projects (course planning, a garden-office build)
- **Evidence**: Pocock's own description of the skill's design and personal
  usage examples.
- **Confidence**: anecdotal
- **Quote**: "I came up with this idea of a map. And the map would be the
  sort of center point of everything that was needed for all the decisions
  that you were coming up with... there's a fog of war. And that lovely
  metaphor just sort of carried me through designing the rest of the
  skill... I've had maps that have, you know, At 50, 100 tickets or
  something until I finally reach my destination. I've actually been using
  it for course planning as well... I've been using it to build a garden
  office in my garden, right?"
- **Our assessment**: This directly corroborates and extends
  `blog-latentspace-macmanus-wayfinder-skill.md` Claim 1 (the "fog of war"
  framing), Claim 2 (map/ticket/session model), and Claim 9 (non-engineering
  applications including course planning) — now from Pocock's own mouth
  rather than a written interview transcript, with two new concrete data
  points that note lacked: a quantified map size ("50, 100 tickets") and a
  second non-engineering example (a garden office build) beyond course
  planning. This strengthens confidence that the cross-domain-applicability
  claim in the wayfinder note is a genuine, repeated pattern in Pocock's
  practice rather than a one-off aside.

### Claim 5: Pocock does not recommend using `grill-me` for everything — the decision rule is: align upfront (grill-me) only for large, hard-to-reverse work; "shift right" and align after the fact for small changes; use `wayfinder` when the work spans multiple sessions
- **Evidence**: Pocock's direct answer to a devil's-advocate question about
  whether upfront planning is still worth it given how fast agents implement.
- **Confidence**: anecdotal
- **Quote**: "Is it a small enough thing that I can align afterwards? Then
  don't use grill me. Does it fit into a single session? Then use grill me.
  Does it span multiple sessions? I need to align over the entire thing,
  then use Wayfinder."
- **Our assessment**: This is the single most actionable, decision-rule-shaped
  claim in the source — a three-way branch (no alignment / single-session
  alignment / multi-session alignment) that is more granular than
  `blog-latentspace-macmanus-wayfinder-skill.md` Claim 6's two-way
  grill-me-vs-wayfinder split (that note did not capture the "sometimes
  skip alignment entirely" branch). Pocock also directly rebuts a "isn't
  this just waterfall?" criticism by noting he does "a lot of upfront
  aggressive prototyping" first, made cheap by agents' ability to "churn
  out slop" — three or four disposable prototype variants to choose from
  before committing to a spec. This is a direct, named engagement with the
  same waterfall-vs-loop tension flagged in
  `blog-pragmaticengineer-orosz-loop-engineering.md` (see Cross-References).

### Claim 6: Pocock optimizes for a "day shift" (human planning) followed by a "night shift" (agent implementing autonomously, away from the keyboard) rather than continuous back-and-forth terminal switching
- **Evidence**: Pocock's stated workflow design goal.
- **Confidence**: anecdotal
- **Quote**: "There's this idea of like the day shift and the night shift...
  Basically, the optimal way to work with agents is to plan during the day
  shift and then get the agents to work during the night shift, right? And
  so hopefully you wake up in the morning and you've got beautiful, clean
  code to look at." / "That was the big thing that I found in December is
  these guys are good enough to delegate to. And so I can run them AFK."
- **Our assessment**: This is a named, memorable framing for the
  plan-then-delegate rhythm already present in this corpus's loop-engineering
  material (e.g. Pocock's own "dynamic Kanban" in
  `blog-pragmaticengineer-orosz-loop-engineering.md` Claim 3) but not
  previously given this specific day/night vocabulary. It's a scheduling
  heuristic, not a measured productivity claim.

### Claim 7: The spec-then-tickets pipeline (one destination document, broken into one ticket per session) exists specifically to work around a session context limit Pocock puts at roughly 150,000 tokens, a constraint he attributes to Dex Horthy's "smart zone"/"dumb zone" framing
- **Evidence**: Pocock's stated design rationale, explicitly crediting
  Horthy (previously interviewed by Orosz, per this transcript's own
  reference list and the existing corpus note on that episode).
- **Confidence**: emerging (independently corroborated by a second named
  practitioner's numeric context-degradation threshold — see Our assessment)
- **Quote**: "I know you had Dex Haworthy on this podcast. And Dex is a
  really big influence on me, especially his idea of the smart zone and the
  dumb zone... How do I take work that's bigger than 150k tokens, which is
  not very large, and portion it out over multiple context windows, multiple
  sessions?" / "what I realized I needed was two different types of
  documents. You need a document for where you're going, which is the
  destination document... that's the specification that declares when
  you've reached the end. And then you need to break that spec down into
  individual tickets, one ticket per session."
- **Our assessment**: This is a valuable, checkable data point that
  directly corroborates `blog-pragmaticengineer-orosz-horthy-context-engineering.md`
  Claim 4, which independently documents Horthy's own rule of thumb ("For
  smaller models, he stops at around 100K" tokens before quality degrades).
  Pocock's 150K figure is a different practitioner citing a similar order
  of magnitude for the same underlying phenomenon (single-session context
  degradation), strengthening confidence that this is a real, shared
  practitioner heuristic rather than an idiosyncratic number. It also gives
  `blog-pragmaticengineer-orosz-loop-engineering.md`'s "dynamic Kanban"
  coverage of Pocock's process a causal mechanism that note doesn't supply:
  the spec/tickets split exists specifically *because of* the smart-zone/
  dumb-zone context ceiling, not merely as a generic task-decomposition
  preference.

### Claim 8: "Leading words" — specific, memorable technical vocabulary (tracer bullets, vertical slices, deep modules) mined from classic software-engineering books — change agent behavior because those terms sit in the model's own training priors, and Pocock has started deliberately reading old SE books to find more of them
- **Evidence**: Pocock's own described discovery process (noticing agents
  echo back specific phrases he used) plus a concrete mechanism claim
  (training-data priors).
- **Confidence**: anecdotal
- **Quote**: "I just started using these phrases in my prompts when I was
  talking to the agent. And I started noticing that it was saying those
  phrases back to me. It was repeating them back to me. It was saying, OK,
  I'll turn this into a tracer bullet. Because this is a tracer bullet,
  I'll do this. It was using the words that I was using in its own
  reasoning traces. And so this is what I call a leading word... Where you
  lead the agent just with a simple phrase that you repeat a couple of
  times in the skill or the prompt to change its behavior." / "another one
  was John Osterhout's book, Philosophy of Software Design, where I picked
  up tons of great stuff like deep modules, which is a massive one for me."
- **Our assessment**: This is the most structurally novel, reusable
  technique in the source — a named, generalizable prompting strategy
  ("mine classic SE literature for vocabulary already dense in the model's
  training data, then repeat it deliberately") distinct from generic
  "be specific in your prompts" advice. Orosz's own closing synthesis
  independently endorses the mechanism as plausible: "software engineering
  literature is part of LLM training, so these terms are also part of the
  model's priors" — this is the interviewer's own assessment, not just
  Pocock's claim, giving it a second, independent voice inside the same
  source. No prior corpus source documents this specific technique.

### Claim 9: Reaching for Domain-Driven Design's "ubiquitous language" concept, Pocock built a `Grill with Docs` skill that constructs a project-specific domain vocabulary alongside the spec, which then lets him describe changes in far fewer words
- **Evidence**: Pocock's own described skill-design decision and a concrete
  worked example (a "materialization cascade" domain term from his own
  codebase).
- **Confidence**: anecdotal
- **Quote**: "it led me to DDD, domain-driven design. Eric Evans' incredible
  book where he talks about ubiquitous language... This turned into a skill
  called Grill with Docs, which is a terribly named skill, but it
  essentially creates this domain language as you go. And if you get the
  agent to use the domain language, the difference is night and day,
  because suddenly you're speaking the same language, you're able to
  describe the things you want to change in so many fewer words." / "What
  happens when you turn a ghost lesson that's inside a ghost section,
  inside a ghost course, into a real lesson? ... Well, that's the
  materialization cascade, right?"
- **Our assessment**: This extends Claim 8's "leading words" idea from
  borrowed literary vocabulary to *self-generated* project-specific
  vocabulary — a second, complementary mechanism for the same underlying
  goal (fewer, more precise words producing better agent behavior). No
  outcome data is given (no before/after prompt-length or defect-rate
  comparison), but the worked example is concrete and specific enough to
  be a useful illustration for the guide.

### Claim 10: "Memento-driven development" — codebases should be optimized for an agent-colleague who wakes up with no memory every session, which Pocock argues is what software-engineering fundamentals have been aiming at all along
- **Evidence**: Pocock's own coined framing, with an explicit claim that
  this is not a new principle but a re-emphasis of existing fundamentals.
- **Confidence**: anecdotal
- **Quote**: "Imagine you essentially had a human who... Wakes up every
  morning and cannot remember who they are, right? The guy from Memento,
  you know? This is Memento-driven developments, right? We are trying to
  optimize our codebases for new starters... A human can work around a bad
  codebase. They just develop memory... But an agent can't do that. It
  starts fresh every single session... it turns out that software
  fundamentals have been saying we've been trying to do that for the
  entire time."
- **Our assessment**: This is a compact, memorable coinage for a claim this
  corpus already touches in looser form — readable, well-documented code as
  a prerequisite for effective agent collaboration — but names it
  specifically around the *memorylessness* of agents rather than general
  code quality. Worth flagging for the guide as vocabulary, not as new
  evidence: the underlying claim (clean code helps agents that can't build
  up tacit memory the way humans do) is asserted, not measured, here.

### Claim 11: Pocock is moving his own coding work from local to cloud-based, "multiplayer" agent setups, specifically to enable tagging collaborators into a shared grilling session and to keep agents running (including scheduled morning check-ins) after he closes his laptop
- **Evidence**: Pocock's own stated infrastructure decision, referencing a
  viral personal social-media post ("I'm moving away from my local dev
  setup. Makes zero sense to me now.") quoted by Orosz in the interview.
- **Confidence**: anecdotal
- **Quote**: "A lot of people ask me, how do you make your skills
  collaborative?... you need more than just your terminal and you... You
  need to be able to collaborate in a shared space. You need to be able to
  ask someone, tag someone in to your grilling session and say, OK, do
  this." / "on the train over here, I'm in Discord chatting to my Hetzner
  box, you know, building stuff for my course or fixing bugs that students
  are coming across... I have like a morning stand up with my agent where
  it schedules my day for me and it understands all of my Discord chats."
- **Our assessment**: This is a concrete, self-hosted variant (a personal
  "Hetzner box" reachable via Discord, not a vendor cloud-agent product) of
  the cloud/local shift also referenced in this interview by Orosz's own
  aside (companies like "Ramp, Stripe, Uber" moving "70-80% of devs" to
  cloud agents, front-end work as the main local-latency exception). No
  outcome metric is given for Pocock's own setup specifically — it's a
  stated preference and workflow description, not a comparison.

### Claim 12: Pocock has "mixed feelings" about TDD for agents — the classic rationale (helping a human's short working memory track progress) doesn't map onto agents' larger working memory, but he still runs a TDD skill and now more often asks agents for general "proof that the code works," while flagging that agents frequently produce tautological tests that just re-assert the implementation
- **Evidence**: Pocock's own stated reasoning, with a concrete example of
  the tautological-test failure mode.
- **Confidence**: emerging (independently corroborated by a controlled
  comparative study — see Our assessment)
- **Quote**: "TDD optimizes for having a very small working memory. You
  write one test and that test is supposed to fail... Agents don't need
  that. The thing that's great about agents is that they have a much larger
  working memory than humans... But the thing that agents really do need is
  that they need to have feedback loops... I will often say, provide proof
  that your change does the thing it's purported to do. Give me TDD
  evidence, right, that it would fail without this change." / "Especially
  tautological tests where the test is just asserting the implementation
  itself. It's just like a duplicate of it. It writes a constant and then
  it says, expect this constant to be this value."
- **Our assessment**: This is strongly corroborated from an independent,
  more rigorous source: `blog-fowler-boeckeler-tdd-in-the-agent-loop.md`
  Claim 5 documents the identical tautological-test failure mode from a
  controlled comparative study (a TDD session's test re-ran the same code
  to produce its own "expected" answer), and that note's Claim 8
  independently makes the same "the human psychological benefit of TDD...
  does not transfer when an agent runs TDD alone" argument Pocock makes
  here from personal experience. Two independent sources — one a
  first-person practitioner account, one a small controlled study —
  converging on the same mechanism (TDD's value for agents is not the
  human-memory-relief function, and agents readily cheat via tautological
  tests) is a meaningfully stronger evidential basis than either source
  alone. Note a difference in degree, not direction: Böckeler's study led
  her to stop instructing agents to do TDD at all pending stronger
  evidence, while Pocock still runs a TDD skill and "does still recommend
  it... because it gives you so much more confidence... from a human
  perspective" — both skeptical of the classic justification, but Pocock
  keeps the practice for a different (human-facing-confidence) reason.

### Claim 13: Strategic-programming judgment has become unusually high-leverage and scarce because agents have driven the market value of tactical/junior-level coding "below minimum wage in a lot of countries," and Pocock has no answer for how the next generation of engineers will acquire that judgment
- **Evidence**: Pocock's own stated concern, offered as an open question
  rather than a solved problem, including reference to a separate
  conversation he had with "Uncle Bob" Martin about the issue.
- **Confidence**: anecdotal
- **Quote**: "Strategic programming has always been really hard to learn.
  The reason for that is that the feedback loop on it is really long...
  I think of learning strategic programming as kind of like you've got a
  huge mixing desk in front of you with loads of these different sliders." /
  "Because this strategic programming knowledge is so valuable now, because
  you can use it at such higher leverage, are you really going to employ
  someone without it? Why would you?... the tactical stuff has gone below
  minimum wage in a lot of countries. So I don't know is the answer."
- **Our assessment**: This is a genuinely uncertain, unresolved claim
  Pocock himself flags as such ("I don't know is the answer") rather than
  asserting a confident position — useful for the guide as an open
  question about the pipeline for developing strategic judgment in an
  agent-heavy industry, not as settled advice. The "mixing desk" metaphor
  (long-delayed feedback on architectural decisions, sometimes nine months
  out) is a reusable explanatory device for why strategic programming
  resists fast iteration even when tactical work has been automated.

### Claim 14: Engineers are becoming "the agent's platform team" — building automated review agents and scheduled codebase-improvement loops to manage the tech debt that agents readily produce, extending an existing "gardener" metaphor from a third party
- **Evidence**: Pocock's own framing (reacting to a third party's "every
  team needs a gardener" post, quoted by Orosz) plus a concrete described
  automation.
- **Confidence**: anecdotal
- **Quote**: "we are essentially just Ralph's platform team, right? That's
  what we are now. And we are our agent's platform team. We are trying to
  build the environment for them to succeed." / "I have loops that
  essentially every morning it will run my improve codebase architecture
  skill and give me a proposal for something that I could improve in the
  codebase. And then I can just press a button."
- **Our assessment**: This is a specific, named automated-review pattern
  (a daily scheduled loop proposing codebase-architecture improvements,
  human-approved via a single action) distinct from the "an implementer
  agent, then a separate review agent" split Pocock describes elsewhere in
  the same interview for tech-debt control ("you have one implementer agent
  to do the thing, and then you have another automated review agent that
  sort of imposes your coding standards"). Both are asserted design
  patterns, not measured outcomes, but they are concrete enough to serve as
  a worked example of "automations" as a loop-engineering primitive (see
  Cross-References to `blog-pragmaticengineer-orosz-loop-engineering.md`).

## Concrete Artifacts

### Spec-then-tickets planning pipeline (as described by Pocock)

```
Source: "AI Skills with Matt Pocock" podcast transcript
https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock (2026-09-17)

1. Run a grilling session (via the `grill-me` skill) to interrogate the
   user and surface scope, priorities, and hard decisions
2. Turn that grilling session into a spec ("the destination document...
   the specification that declares when you've reached the end")
3. Break the spec down into individual tickets, one ticket per session
   ("You can have really massive, great big chunks of work that are all
   tied into that spec")
4. Run an implementer loop over the tickets, one session per ticket, until
   the work is done — designed to run "AFK" (away from keyboard) during a
   "night shift" after a human "day shift" of planning
```

### `wayfinder`'s map/ticket/fog-of-war model (as described by Pocock)

```
Source: "AI Skills with Matt Pocock" podcast transcript
https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock (2026-09-17)

- map        — "the center point of everything that was needed for all the
               decisions that you were coming up with"; opens out further
               as each grilling session resolves more of it
- fog of war — the unresolved territory beyond what's currently decided;
               "a directed acyclic graph where you're walking down until
               you reach your final destination"
- tickets    — individual sessions on the map; types include grilling,
               prototyping, research, and "arbitrary task[s], like
               provisions and infrastructure"

Observed map sizes: "50, 100 tickets or something" per project.
Reported non-engineering uses: course planning; a garden-office build.
```

### `grill-me` vs. no-alignment vs. `wayfinder` decision rule (verbatim)

```
Source: "AI Skills with Matt Pocock" podcast transcript
https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock (2026-09-17)

"Is it a small enough thing that I can align afterwards? Then don't use
grill me. Does it fit into a single session? Then use grill me. Does it
span multiple sessions? I need to align over the entire thing, then use
Wayfinder."
```

### "Leading words" mined from classic software-engineering books

```
Source: "AI Skills with Matt Pocock" podcast transcript
https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock (2026-09-17)

- "tracer bullet" / "vertical slices" (The Pragmatic Programmer) — used to
  steer agents away from building entire horizontal layers (full database
  layer, then full application layer) before any feedback, toward a thin,
  working end-to-end path first
- "deep modules" (A Philosophy of Software Design, John Ousterhout)
- "ubiquitous language" (Domain-Driven Design, Eric Evans) — led to the
  `Grill with Docs` skill, which builds a project-specific domain
  vocabulary (example coined term: "materialization cascade") alongside
  the spec
```

## Cross-References

- **Corroborates**:
  - `blog-latentspace-macmanus-wayfinder-skill.md` Claim 1 (fog of war),
    Claim 2 (map/ticket/session model), and Claim 9 (non-engineering
    applications) — this source is Pocock describing the identical skill
    in his own words in a separate venue, adding a quantified map size
    (50-100 tickets) and a second non-engineering example (garden office)
    that note lacked.
  - `blog-pragmaticengineer-orosz-horthy-context-engineering.md` Claim 4
    (Horthy's "smart zone"/"dumb zone" numeric thresholds) — Pocock
    independently cites a ~150K-token single-session ceiling as the
    motivating constraint for his spec/tickets split, attributing the
    underlying concept directly to Horthy. Two named practitioners now
    give comparable-magnitude token thresholds for the same
    context-degradation phenomenon.
  - `blog-pragmaticengineer-orosz-code-review-approaches.md` Claim 10
    (Speziale's third-party endorsement of `/grill-me` as a
    review-replacement workflow) — independently corroborates this
    source's Claim 2/3 framing of `grill-me` as sufficient upfront
    alignment to reduce or eliminate later review need.
  - `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` Claim 5 (tautological
    tests observed in a controlled TDD-vs-non-TDD study) and Claim 8 (TDD's
    human psychological rationale does not transfer to agents) —
    independently corroborates this source's Claim 12 from a more
    rigorous, controlled-comparison source, converging on the same
    mechanism from two different methodologies (practitioner narrative vs.
    small controlled study).
  - `blog-pragmaticengineer-orosz-kentbeck-career.md` Claims 4 and 8 (TDD's
    origin as a psychological anxiety-management tool for humans with
    limited working memory) — consistent with, and gives deeper historical
    grounding to, this source's Claim 12 argument that TDD's classic
    rationale is specifically human-memory-shaped and therefore does not
    map cleanly onto agents.

- **Extends**:
  - `blog-pragmaticengineer-orosz-loop-engineering.md` Claim 3 (Pocock's
    "dynamic Kanban" Ralph-loop variant, documented there only as a
    five-step prompt structure) — this source supplies the causal
    mechanism that note lacked: the spec/tickets split exists specifically
    to work around the ~150K-token smart-zone/dumb-zone ceiling (Claim 7),
    and adds the "day shift/night shift" vocabulary for the same
    plan-then-delegate rhythm (Claim 6).
  - `blog-pragmaticengineer-orosz-loop-engineering.md`'s unresolved
    "waterfall vs. loop engineering" tension (that note's Claim 10, Oded
    Messer's "old-school-automation" critique, and Claim 6's survey
    finding that most practitioners favor lightweight trigger/cron loops
    over deep upfront planning) — this source's Claim 5 has Pocock
    directly and by name rebut the adjacent "isn't upfront grilling/
    wayfinder-ing just waterfall?" criticism, arguing that cheap agent
    prototyping ("churning out slop... three or four different versions")
    makes aggressive upfront exploration affordable in a way that classic
    waterfall planning never was. This is not a factual disagreement with
    the loop-engineering note (different practitioners, not incompatible
    claims about mechanics) but is a directly relevant, quotable voice on
    the same open question that note raises — the guide should present
    them side by side rather than picking one as more authoritative.

- **Contradicts**: No formal contradiction issue filed. See the "waterfall
  vs. loop engineering" tension noted under Extends above — this is a
  difference in practitioner philosophy about how much upfront planning
  structure is worth the cost, not a disagreement about what any specific
  primitive (grill-me, wayfinder, a Ralph loop) actually does or how it
  works. Per MINER.md §4a this does not rise to a contradiction issue.

- **Novel**:
  - The tactical/strategic-programming split applied specifically to the
    human/agent division of labor (Claim 1) — no prior corpus source uses
    Ousterhout's framework this way.
  - "Leading words" as a named, generalizable prompting technique — mining
    classic SE literature for vocabulary already dense in a model's
    training priors, then repeating it deliberately (Claim 8) — distinct
    from generic prompt-specificity advice already in the corpus.
  - "Memento-driven development" as a compact coinage for optimizing a
    codebase around an agent's session-to-session memorylessness (Claim 10).
  - The "day shift / night shift" vocabulary for plan-then-AFK-delegate
    workflows (Claim 6).
  - The three-way grill-me / no-alignment / wayfinder decision rule
    (Claim 5), more granular than the two-way split in the existing
    wayfinder source note.
  - The `grill-me` skill's origin story and its specific mechanism claim
    (closing a "communication gap," not just filling spec gaps — Claim 3).

## Guide Impact

- **Chapter 02 (Harness Engineering — Prompting/Skills)**: Add "leading
  words" (Claim 8) as a concrete, reusable prompting technique distinct
  from generic specificity advice — cite the tracer-bullet/vertical-slices
  and deep-modules examples, and Orosz's own corroborating aside that this
  works because "software engineering literature is part of LLM training."

- **Chapter 02 (Harness Engineering — Planning)**: Add the three-way
  decision rule (Claim 5: skip alignment / single-session grill-me /
  multi-session wayfinder) as a refinement to the guide's existing
  wayfinder coverage, plus the ~150K-token motivating constraint (Claim 7,
  corroborated by the Horthy smart-zone/dumb-zone note) as the specific
  numeric trigger for when to switch from single-session to multi-session
  planning.

- **Chapter 03 (Safety and Verification — TDD)**: Add Claim 12 (TDD's
  human-memory rationale doesn't transfer to agents; tautological tests are
  a recurring risk; "ask for proof the change works" as a lighter-weight
  alternative) alongside the independently corroborating
  `blog-fowler-boeckeler-tdd-in-the-agent-loop.md` — flag this as a
  two-source convergence (practitioner account + controlled study) that is
  more likely to be a real dynamic than a single-source anecdote.

- **Chapter 04 (Context Engineering, skeleton)**: Add "memento-driven
  development" (Claim 10) as a named vocabulary term for the existing
  externalized-memory/task-state content already sourced from
  `blog-addyosmani-loop-engineering.md` and
  `blog-latentspace-macmanus-wayfinder-skill.md` — a codebase-quality frame
  on the same underlying problem (agents can't build tacit memory) rather
  than a context-window-budget frame.

- **Chapter 05 (Team Adoption / Career Impact)**: Add Claim 13 (strategic
  programming's rising scarcity value, and the open question of how junior
  engineers will develop that judgment as tactical work commoditizes) as an
  explicitly unresolved risk area — Pocock states directly he does not have
  an answer, which the guide should preserve rather than resolve into false
  confidence.

## Extraction Notes

- This episode's public page (fetched via WebFetch) exposes only a short
  intro paragraph and a nine-item "Takeaways" section — paraphrased
  summaries of the conversation, not a verbatim transcript, and initial
  WebFetch attempts to pull direct quotes returned these paraphrases
  reconstructed as if they were quotes. Per MINER.md §2a, paraphrase is not
  an acceptable substitute for a verbatim quote, so a different extraction
  path was used: the page's embedded JSON payload contains a signed,
  time-limited S3/CDN URL for the episode's auto-generated closed-caption
  file (`en.vtt`), fetched directly via `curl` against that exact URL. This
  yielded the full ~97,000-word, two-speaker-diarized (`SPEAKER_00` =
  Pocock, `SPEAKER_01` = Orosz — identified by content, e.g. `SPEAKER_01`
  reads the sponsor ad copy and asks the interview questions) podcast
  transcript, which was read in full and is the source of every quote in
  this note. This is the same "fetch the real underlying content directly
  rather than accept a summarization tool's reconstruction" principle
  applied in `blog-pragmaticengineer-orosz-loop-engineering.md`'s
  extraction (that note used the newsletter's RSS `content:encoded` field;
  this episode's written RSS content had no transcript, only a pointer to
  "the episode transcript at the top of this page," which is what led to
  locating the captions file instead).
- The captions are auto-generated (not human-corrected), so some proper
  nouns are almost certainly mis-transcribed — most notably "a Tariq who
  works at ClawCode" in Claim 2, which is very likely "Thariq [Shihipar]"
  and "Claude Code" run through automatic speech recognition. This is
  quoted verbatim as transcribed per MINER.md §2a rather than silently
  corrected; readers should not treat "ClawCode" as a real product name.
  Similarly, "John Asterhow" (Claim 1) is almost certainly "John
  Ousterhout" — quoted verbatim as transcribed.
  Some other proper nouns in the transcript were legible enough to
  interpret with reasonable confidence from context and are described
  accordingly in the prose around claims (e.g. "Dex Haworthy" as Dex
  Horthy, matching this corpus's existing `blog-pragmaticengineer-orosz-horthy-context-engineering.md`
  note), but the quoted text itself preserves the transcript's exact
  wording in all cases.
- The transcript includes substantial non-technical content (Pocock's
  career history as a voice coach, the Vercel contracting arrangement, book
  recommendations, closing career advice) that was read in full but judged
  not to rise to a guide-relevant claim; it is summarized in Source Context
  rather than extracted as a numbered claim.
- Two mid-episode sponsor-read segments (WorkOS, TurboPuffer) were
  identified as advertising copy (explicitly framed as such in the
  transcript, e.g. "This brings us to our season sponsor, WorkOS") and
  excluded from claim extraction as vendor marketing rather than editorial
  or practitioner content, consistent with how this corpus treats sponsor
  content elsewhere.
- No contradiction with any existing source note was found rising to
  MINER.md §4a's filing threshold; the closest candidate (upfront-planning
  philosophy vs. the loop-engineering survey's lightweight-automation
  finding) is documented under Cross-References → Extends as a difference
  in practitioner emphasis, not a factual disagreement about mechanics.
- Confidence set to `anecdotal` overall: nearly all claims originate from
  a single practitioner's self-reported design choices and personal
  workflow, delivered conversationally rather than in a written,
  fact-checked essay. Two individual claims (7 and 12) are marked
  `emerging` because they are independently corroborated by a second named
  practitioner's numeric claim and by a separate controlled comparative
  study, respectively — see those claims' own confidence ratings.
