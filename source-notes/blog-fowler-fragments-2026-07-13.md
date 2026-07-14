---
source_url: https://martinfowler.com/fragments/2026-07-13.html
source_type: blog-post
title: "Fragments: July 13"
author: Martin Fowler (curator); contributors include Kief Morris, Sam Ruby, Birgitta Böckeler, Sebastian Raschka, Simon Willison, Josh Comeau, John Gruber, Dan Davies
date_published: 2026-07-13
date_extracted: 2026-07-14
last_checked: 2026-07-14
status: current
confidence_overall: emerging
issue: "#1850"
---

# Fragments: July 13 (Martin Fowler)

> A Fowler-curated fragment collection from the Thoughtworks Future of
> Software Development Retreat whose central contribution is Kief Morris's
> unifying observation that nearly every retreat session — code review,
> incident response, team structure — reduces to one recurring question:
> "How much do we let an agent decide, and how do we stay confident in what
> it does?" Paired with Sam Ruby's "managing by objective" reframing of
> non-engineers directing LLM agents as a hiring decision (not a permission
> question), concrete harness-engineering data points (agents.md kept under
> 200 lines; Rust-over-Python and property-based/formal-methods validation on
> the sensor side), a self-hosted-models discussion (sovereignty, information
> security, GPU talent scarcity, fine-tuning), and independent convergence
> from Birgitta Böckeler and Sebastian Raschka on Qwen 3.6 as the current
> local-model sweet spot.

## Source Context

- **Type**: blog-post (curated fragment collection — Fowler's "Fragments"
  series synthesizes first-hand retreat reporting with linked/summarized
  posts from named contributors under one dated URL; the July 13 entry
  covers the same Thoughtworks Future of Software Development Retreat as
  `blog-fowler-fragments-2026-07-06.md`, one week later)
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks,
  author of *Refactoring* and *Patterns of Enterprise Application
  Architecture*, and an original Agile Manifesto signatory. The
  `martinfowler.com` feed is designated `trusted-feed` in this repository.
  Fowler personally attended the retreat, giving this fragment first-hand-
  reporter status for the retreat content (harness engineering, self-hosted
  models, Kief Morris's synthesis, Sam Ruby's session). Named contributors
  for the non-retreat fragments: Birgitta Böckeler (Distinguished Engineer,
  Thoughtworks — prior corpus note `blog-fowler-boeckeler-local-models-viability.md`);
  Sebastian Raschka (independent ML educator/practitioner, not previously in
  this corpus); Simon Willison (creator of Django, high-signal independent AI
  commentator, dozens of prior corpus notes); Josh Comeau (developer
  educator, prior corpus note `blog-simonwillison-josh-comeau-course-sales-ai.md`);
  John Gruber (Daring Fireball, Apple-platform commentator, not previously in
  this corpus); Dan Davies (author/economist writing on expertise and AI, not
  previously in this corpus).
- **Scope**: Covers the retreat's harness-engineering session (guide-side
  context management, sensor-side validation), a self-hosted-models session,
  Kief Morris's cross-session synthesis on agent autonomy, Sam Ruby's "Bring
  Me a Rock" session on management-by-objective, a pointer to Böckeler's and
  Raschka's separate local-model posts, a Simon Willison cost-saving tip for
  the Fable model, Josh Comeau's developer-education sales decline, John
  Gruber's critique of Claude's Electron-based Mac app, and Dan Davies's
  contributory-vs-interactional-expertise distinction. Does NOT provide:
  session attendee counts, transcripts, or named speaker attribution for any
  individual harness-engineering or self-hosted-models tidbit (both sessions
  are presented as Fowler's own pooled paraphrase of "the discussion," not
  quotes from named individuals — unlike the Kief Morris and Sam Ruby
  sections, which name and quote specific attendees).

## Extracted Claims

### Claim 1: On the "guide" side of harness engineering, practitioners report that larger context windows do not make models focus correctly, and one attendee keeps their `agents.md` file under 200 lines to force focus
- **Evidence**: Fowler's own paraphrase of the retreat's harness-engineering
  session, attributed to "one attendee" rather than a named individual.
- **Confidence**: anecdotal (single unnamed attendee's practice, relayed
  through Fowler's session summary, not a direct quote from the attendee)
- **Quote**: "While context windows have increased is size as models get more
  sophisticated, that doesn't mean that models will properly focus on the
  right bits. Models typically only focus attention on part of the context,
  and to get the best behavior, we need to manage that focus. One attendee
  keeps their context small, limiting the agents.md file to less than 200
  lines"
- **Our assessment**: This is a concrete, actionable number (sub-200-line
  `agents.md`) that no other corpus note currently states as a specific
  target — existing corpus coverage of context-window health management
  (`blog-fowler-fragments-2026-06-16.md` Claims 1-3, Chelsea Troy's
  conversation registers) addresses *when* to reset context, not *how large*
  a persistent guide file should be. The "models typically only focus
  attention on part of the context" framing is the underlying mechanism
  Fowler gives for why bigger context windows don't solve the focus problem
  by themselves — a useful, quotable rationale for keeping CLAUDE.md/
  AGENTS.md-style files deliberately terse rather than exhaustive. The
  200-line figure is a single anecdotal data point (unnamed attendee, no
  measurement of what breaks above that threshold), not a validated ceiling.

### Claim 2: On the "sensor" side of harness engineering, practitioners report two convergent patterns: shifting to languages with greater control (e.g. Rust over Python) and "leveling up" validation via property-based testing and formal-methods techniques
- **Evidence**: Fowler's own paraphrase of the same session, attributed to
  "one participant."
- **Confidence**: anecdotal (single unnamed participant's reported patterns)
- **Quote**: "On the sensor side, we see more attention on computational
  sensors. Two patterns from one participant was shifting to languages with
  greater controls, (eg Rust rather than Python) and \"leveling up\"
  validation approaches, using more property-based testing and techniques
  from formal methods. One commented that while they aren't smart enough to
  write specifications in a formal specification language, they are smart
  enough to read it and check it makes sense for their domain."
- **Our assessment**: This is a novel and specific claim for this corpus's
  harness-engineering coverage: no existing note documents Rust-over-Python
  as a deliberate sensor-side language choice motivated by AI-harness
  validation needs, nor property-based testing / formal methods as a named
  "leveling up" trend for computational sensors specifically. The closing
  detail — a practitioner who can *read and validate* a formal specification
  but not *author* one from scratch — is a distinct and useful framing for
  human-AI division of labor around formal methods: the human's role shifts
  from writing the spec to judging whether a generated spec matches domain
  intent, which parallels this corpus's broader "review > write" shift
  (see Cross-References) but applied specifically to formal-methods
  artifacts rather than code.

### Claim 3: Fowler declines to predict whether harness engineering will remain necessary as models improve, but observes that harnesses currently reduce token usage and enable weaker/local models to be useful
- **Evidence**: Fowler's own editorial reflection, closing the harness-
  engineering section of the fragment.
- **Confidence**: anecdotal (Fowler's own reasoned but explicitly
  non-predictive stance)
- **Quote**: "Will our attention on harnesses last long enough for our next
  retreat? Will the models just get so good that harnesses become
  unnecessary? Those with some mechanical sympathy for LLMs seem to think not
  - but are they overly coupled to the current state of technology? I find
  such speculation tends not to lead anywhere useful, I've not seen much
  success in guessing the future in the past, and with technology as radical
  as this, I don't see it being any easier. So for the moment, attention to
  harnesses pays off. We find it reduces token usage, and also allows weaker
  models to be useful, supporting such things as local hosting of open-weight
  models."
- **Our assessment**: This is a deliberately grounded, non-speculative
  framing that the guide should adopt directly: rather than taking a
  position on whether harness engineering is a permanent discipline or a
  transitional scaffolding that better models will obsolete, Fowler names
  two concrete, currently-true benefits (lower token usage; enabling weaker/
  local models) as the reason to invest in harnesses *today*, independent of
  how that question resolves. This directly connects the harness-engineering
  material (Claims 1-2) to the self-hosted-models material (Claims 4-7) in
  the same fragment — better harnesses are presented as a precondition for
  viable local-model deployment, not a separate topic.

### Claim 4: Self-hosted open-weight models are gaining interest for reasons beyond cost — model sovereignty (following government access restrictions), information security for data that can't be sent to a vendor, and the fact that a self-hosted model's usage improves your own model rather than the vendor's
- **Evidence**: Fowler's own paraphrase of the self-hosted-models session.
- **Confidence**: anecdotal (session paraphrase, not attributed to named
  individuals; the "government intervene to deny access" reference is
  asserted without a specific cited incident in this fragment)
- **Quote**: "Cost isn't the only factor, however, many folks find a desire
  to be independent of the frontier model firms to be the the driving force.
  After all we've seen the U.S. government intervene to deny access to
  models, increasing the desire for greater model sovereignty. Information
  security is also something to consider, some attendees just can't give
  models necessary data for critical work. Even without that, if someone
  else hosts the model then their model learns rather than your model."
- **Our assessment**: This adds a fourth, non-cost, non-security rationale
  for self-hosting that is largely new to this corpus's self-hosted-models
  coverage: "if someone else hosts the model then their model learns rather
  than your model" — a training-dynamics argument (whoever hosts inference
  captures the improvement signal) distinct from the sovereignty and
  information-security arguments that are already better-documented
  elsewhere (see Cross-References). The government-access-restriction
  framing is asserted as a given ("we've seen") without a specific named
  incident in this fragment, so it should be cited as a stated motivation
  rather than a documented event unless a dedicated source confirms it.

### Claim 5: Several retreat participants' companies had already been self-hosting models for up to a couple of years, predating the current cost-driven interest spike
- **Evidence**: Fowler's own paraphrase of the session.
- **Confidence**: anecdotal (unattributed to specific companies or
  individuals)
- **Quote**: "although recent events have increased interest, several
  participants worked with companies that had been self-hosting for up to a
  couple of years."
- **Our assessment**: This is a useful corrective against reading self-
  hosting purely as a reactive 2026 cost-crisis response (the framing implicit
  in this corpus's token-cost-crisis cluster, e.g.
  `blog-thoughtworks-kamelman-token-crisis.md`): some organizations have a
  multi-year track record with self-hosted models predating the current
  price pressure, suggesting self-hosting expertise already exists in some
  organizations and isn't purely a 2026 improvisation. No company names or
  outcome data are given, so this should be cited as an existence claim
  (mature self-hosting practice predates the crisis) rather than evidence
  about self-hosting's success rate.

### Claim 6: Self-hosting model economics may repeat the private-cloud cost-overrun pattern, and success depends on whether hosting a model turns out to be simpler than hosting a private cloud — with GPU-operations talent scarcity flagged as the likely hard part, creating an opportunity for professional-services firms
- **Evidence**: Fowler's own analytical framing of the session's open
  question.
- **Confidence**: anecdotal (Fowler's own analogy and inference, not a
  measured comparison)
- **Quote**: "Is this trudging down the same path of self-hosted clouds,
  which led to lots of folks spending excessive funds on half-arsed private
  clouds? The answer hinges upon whether it ends up being simpler to host a
  model than a cloud, perhaps due to a simpler interaction protocol. The hard
  part of this may be the talent required to efficiently use the GPUs,
  managing an inference data center currently isn't a widely available
  skill. Even self-hosted models are a cost to operate, capital costs in
  GPUs, ongoing costs in electricity. The physical design of a data center
  can affect optimal usage. There's an opportunity here for professional
  services firms to help companies manage this."
- **Our assessment**: This is a specific, falsifiable historical analogy
  (self-hosted-clouds overspend pattern) applied to self-hosted models, with
  a named candidate root cause (GPU-operations talent scarcity, not model
  quality or hardware cost) for why the analogy might repeat. It corroborates
  and sharpens `blog-thoughtworks-lovin-gall-local-inference-boundary.md`
  Claim 5 (on-device inference trades $0 marginal token cost for hard
  physical constraints) at the enterprise-datacenter scale rather than the
  consumer-device scale: both sources converge on "self-hosted/local
  inference is not simply free," but this fragment locates the hidden cost
  in operational talent and datacenter design rather than context-window/
  RAM ceilings. The "professional services opportunity" framing is
  Thoughtworks-adjacent business interest (Fowler is Thoughtworks' Chief
  Scientist) and should be read with that in mind.

### Claim 7: Cost control for self-hosted or mixed-model deployments may increasingly rely on a broker model that decides which model is the right choice for a given job, rather than teaching individual engineers to pick weaker models themselves
- **Evidence**: Fowler's own framing of a session discussion point.
- **Confidence**: anecdotal (speculative framing, no implementation example
  given in this fragment)
- **Quote**: "Cost control also involves teaching people to pick the right
  model for the job. Can we teach engineers, or indeed other users, to pick a
  less-powerful model? This, of course, could be a job for model itself,
  acting as a broker, deciding which model is the best choice to tackle
  certain jobs."
- **Our assessment**: This "model as broker, deciding which model to use"
  idea is the same underlying pattern as Claim 12 below (Simon Willison's
  concrete Fable tip to delegate smaller tasks to cheaper models using the
  orchestrating model's own judgment) — this fragment documents the pattern
  twice, once as a speculative session idea (here) and once as an already-
  shipping practitioner technique (Claim 12), which strengthens its standing
  from purely speculative to partially demonstrated. See Cross-References.

### Claim 8: Self-hosting may drive greater adoption of fine-tuning, with the hypothesis that domain-fine-tuned models will need less reasoning and consume fewer tokens than general-purpose models for the same domain-specific tasks
- **Evidence**: Fowler's own framing of the session discussion.
- **Confidence**: anecdotal (stated as a forward-looking hypothesis, "we
  could well find," not a measured result)
- **Quote**: "Self-hosting may lead to a greater use of fine-tuning.
  Currently that's a niche activity, but over time we could well find that
  models that are fine-tuned to a particular domain need less reasoning,
  consume less tokens, and thus are cheaper to operate. We are seeing models
  trained specifically to support programming."
- **Our assessment**: This connects self-hosting (Claims 4-6) to token-cost
  governance (this corpus's existing token-cost-crisis cluster) via a
  specific proposed mechanism — fine-tuning reduces the *reasoning* a model
  needs to do at inference time for in-domain tasks, not just the model's
  size. That's a distinct cost lever from the model-routing/broker idea in
  Claim 7: routing picks an existing cheaper model for a job, while
  fine-tuning would make a *given* model cheaper for its specialized job.
  Presented as a hypothesis, not a validated finding — no benchmark or case
  study accompanies this claim in the fragment.

### Claim 9: Kief Morris identifies a single unifying theme across nearly all of the retreat's disparate-seeming sessions (code review, incident response, team structure): "How much do we let an agent decide, and how do we stay confident in what it does?"
- **Evidence**: Fowler's direct account and endorsement of Kief Morris's
  synthesis, explicitly contrasted with Fowler's own admitted skepticism of
  after-the-fact conference narrative-making.
- **Confidence**: emerging (a named, credible retreat-attendee synthesis,
  independently endorsed by Fowler — himself skeptical of grand narratives
  in general — as "a convincing one, even to a narrative-denier like me")
- **Quote**: "But they weren't. Nearly every one of them was a different
  facet of the same argument. How much do we let an agent decide, and how do
  we stay confident in what it does?" ... "Underneath all of these sessions,
  the operations debate, the wide-remit team, the dark-factory spectrum, the
  argument about who's allowed to steer the model, people were making the
  same handful of choices over and over about a single thing: the unit of
  work they were prepared to hand to an agent. How big it is. How much of
  the job it covers. What you do to get it ready to hand over. How you check
  what comes back. What you put around the agent to keep it inside the
  lines."
- **Our assessment**: This is the single most citable framing in the source
  and a strong candidate for a chapter-level organizing principle: it
  reframes a scattered set of guide topics (code review posture, incident-
  response delegation, team-structure/wide-remit-team design, harness
  guardrails) as five concrete decision variables around one underlying
  question — the size of the unit of work delegated to an agent, and the
  checks placed around it. This gives the guide a unifying vocabulary that
  spans chapters currently treated as separate topics (harness engineering,
  verification, team adoption, governance). Fowler's own explicit
  self-skepticism about conference narratives, and his statement that this
  is the exception, is worth preserving as a credibility signal for the
  claim's strength.

### Claim 10: Sam Ruby argues that with LLMs, iterative "bring me a rock" rejection-based exploration shifts from a management dysfunction to a defensible working style, because machines return new attempts in minutes rather than days
- **Evidence**: Fowler's summary and direct quote of Sam Ruby's own stated
  reasoning for his retreat session.
- **Confidence**: emerging (a named practitioner's own explicit argument,
  reported first-hand by an attendee)
- **Quote**: "Sam had already written why he thought with LLMs, this
  changed from a slur to a defensible way to work. When its a bunch of
  tireless machines with endless patience, that return new rocks in minutes
  rather than days, then an approach like this (using the brainstorming
  register becomes a defensible way to work."
- **Our assessment**: "Bring me a rock" traditionally names a manager
  substituting serial rejection ("no, not that one") for the harder work of
  articulating what they actually want, at direct cost to the person doing
  the fetching. Ruby's argument is that the *cost* side of this equation
  changes qualitatively when the "fetcher" is a tireless machine returning
  results in minutes: the same behavior that wastes a human employee's days
  becomes a legitimate brainstorming/elimination technique with LLMs. This
  is conceptually adjacent to this corpus's existing register-based
  framings (Chelsea Troy's "Brainstorming" register in
  `blog-fowler-fragments-2026-06-16.md` Claim 1) but adds an explicit
  argument for *why* iterative rejection specifically becomes legitimate —
  the machine's patience and speed, not just a named conversational mode.

### Claim 11: Ruby reframes the question "should non-engineers be allowed to steer an LLM agent directly" as a management decision, not a permission question — when a manager routes work to an LLM instead of their team, they have effectively made a hire, and Peter Drucker's 1959 "manage by objective, not by method" principle applies because the agent, like a knowledge worker, out-knows the manager on specifics
- **Evidence**: Sam Ruby's own description of his session's discussion,
  quoted at length by Fowler.
- **Confidence**: emerging (a named practitioner's own developed argument,
  reported first-hand; the Drucker attribution is Ruby's own framing,
  not independently verified against Drucker's original text by this Miner)
- **Quote**: "When a manager reaches for an LLM instead of routing the work
  to the team that reports to them, they didn't pick up a tool — they made a
  hire. And you don't ask permission to manage your own team; a manager who
  decides a piece of work is better given to a new participant than to the
  existing one is doing the most ordinary thing a manager does. Framed that
  way, the permission question dissolves into an older, better-understood
  one — the one Drucker named in 1959: when the worker knows more about the
  specifics than the manager does, you manage by objective, not by method.
  The non-engineer steering an agent is exactly that manager, out-known by
  the thing they're directing, and the slop the room feared is the old
  danger of managing by method when you should be managing by objective. The
  question isn't may they hire? It's do they know how to manage by
  objective? — which you can teach, hire for, and hold people to without
  anyone first becoming an engineer."
- **Our assessment**: This is the fragment's most fully-developed and
  guide-relevant argument. It directly reframes a governance/access-control
  question (who is "allowed" to direct an agent) that this corpus's
  governance cluster (`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`)
  treats primarily as a legal-authority problem, into a management-skill
  problem: the qualifying question is not the directing person's engineering
  credentials but whether they can state a clear objective and evaluate
  whether it was met, a teachable and hireable-for skill independent of
  coding ability. This is a genuinely novel framing for this corpus — no
  existing note applies Drucker's management-by-objective doctrine to the
  question of non-engineers directing AI agents. It should be read as one
  practitioner's persuasive reframing (Ruby's own argument, endorsed by
  Fowler and the retreat room), not a settled resolution to the "should
  non-engineers use agents directly" debate.

### Claim 12: Conformance tests (sensors) are more valuable than specifications (guides) for capturing an agent's unstated objectives, but it is hard to imagine all the conformance tests needed to specify everything that shouldn't happen — and building/communicating a model of the workflow remains a necessarily human-involved activity even if the agent participates in constructing that model
- **Evidence**: Fowler's own synthesis, following directly from the Ruby
  session discussion.
- **Confidence**: anecdotal (Fowler's own reflective argument, not
  attributed to a specific named individual beyond Fowler; consistent with,
  but distinct from, Ruby's session content)
- **Quote**: "We have some hope here - we hear more experiences that suggest
  that recent models can do an excellent job of finding (and hopefully
  fixing) security holes. The careful precision of the machine outruns the
  sloppy if imaginative thinking in squishyware. Perhaps we can assume the
  genie can take care of some of our unstated objectives. Conformance tests
  (sensors) are more valuable than specifications (guides), but it's hard to
  imagine all the conformance tests that are needed to say what shouldn't
  happen." ... "Even if the genie builds the model itself, it needs to teach
  us that model, because the model helps us imagine and communicate the
  goals, the objectives that we give to the machine."
- **Our assessment**: This is a direct, explicit statement of a
  sensors-over-specs preference already implicit in this corpus's harness-
  engineering material (guide vs. sensor framing appears throughout this
  fragment itself, Claims 1-2), but paired here with an important caveat:
  conformance tests cannot exhaustively enumerate everything an agent
  shouldn't do, so guides/specifications retain a residual role for
  unstated-objective coverage that sensors structurally cannot close. The
  closing point — that even an agent-constructed model of a workflow must be
  taught back to the humans directing it — is a specific argument against
  full model-building delegation: communicability of the model to humans is
  treated as a requirement, not an optional nicety, because it's what lets
  humans articulate and refine the objectives given to the agent in the
  first place.

### Claim 13: Birgitta Böckeler and Sebastian Raschka, working independently, both converge on Qwen 3.6 as the current sweet spot for local agentic programming
- **Evidence**: Fowler's own pointer connecting two separately published
  posts he describes as "a nice, if accidental, complement" to each other.
- **Confidence**: emerging (two independent named practitioners converging
  on the same specific model, one already fully documented in this corpus
  with detailed methodology)
- **Quote**: "If you follow my feeds (which you probably do if you're
  reading this), then you'll know that Birgitta Böckeler has written a
  couple of memos on working with local models. She first looked the
  factors that influence how viable they are for programming, and then
  related some of her recent experiences evaluating such models. As a nice,
  if accidental, complement to these, Sebastian Raschka wrote a detailed
  guide to his local model environment. Like Birgitta, he's found the Qwen
  3.6 model to be the current sweet spot for local agentic programming."
- **Our assessment**: Böckeler's Qwen 3.6 35B MoE conclusion is already
  fully extracted in this corpus at
  `blog-fowler-boeckeler-local-models-viability.md` Claim 4 ("The Qwen3.6
  35B-A3B MoE model gave the best balance of parameter count, RAM footprint,
  speed, and quality of any model tested"). This fragment's contribution is
  the pointer to a second, independent named practitioner (Sebastian
  Raschka, not previously in this corpus) reaching the same specific-model
  conclusion via his own separate local-model-environment write-up, which
  raises Böckeler's single-practitioner "Qwen 3.6 sweet spot" finding from
  anecdotal to independently-corroborated anecdotal. Raschka's own post was
  not independently fetched in this extraction (see Extraction Notes) — this
  claim rests on Fowler's characterization of Raschka's conclusion, not a
  direct quote from Raschka.

### Claim 14: Simon Willison shares a cost-saving technique for the Fable model: instruct it to use other (presumably cheaper) models for smaller tasks, applying its own judgment about which model to use for which task
- **Evidence**: Fowler's one-line pointer to a Willison tip.
- **Confidence**: anecdotal (single-sentence pointer, no worked example,
  measured savings, or implementation detail given in this fragment)
- **Quote**: "Simon Willison shares a useful tip to save money while using
  the latest Anthropic Fable model[:] Tell Fable to use other models for
  smaller tasks, applying its own judgement about which model to use."
- **Our assessment**: This is a concrete, practitioner-shared technique that
  is the practical, already-in-use version of the speculative "model as
  broker" session idea in Claim 7 — here, the orchestrating model itself is
  told to delegate smaller tasks to other (cheaper) models using its own
  judgment, rather than requiring a separate broker component or a human
  routing decision. The fragment gives no detail on how this instruction is
  phrased, what savings resulted, or which "other models" Fable delegates to
  — this should be treated as a technique pointer for follow-up (a dedicated
  Willison source note on this tip, if one is mined, would raise this from
  anecdotal to a fully-specified pattern) rather than a validated cost-
  reduction result in its own right.

### Claim 15: Josh Comeau's online course sales are down to roughly ⅓ of prior levels this year, and other developer-education course creators report the same pattern — revenue down 50%+, engagement declining, attributed to AI both suppressing purchase incentive (job-security anxiety) and substituting for paid content (LLM tutoring "slurping up" and regurgitating creator content without consent or compensation)
- **Evidence**: Fowler's summary of Josh Comeau's own reporting, previously
  documented in full in this corpus.
- **Confidence**: anecdotal (single self-reported figure plus secondhand,
  unnamed peer reports — already flagged with this same confidence rating in
  the fuller existing corpus note)
- **Quote**: "His been successful for most of this decade but has found his
  online courses have had only ⅓ the sales this year. He attributes this to
  AI, partly as people worry if it's worth spending money on a job that may
  not have a future, but also because AI can provide personalized tutoring."
  ... "I've spoken to a few course creators now, and we're all seeing the
  same trend. Revenue down 50%+. Fewer people engaging with our content.
  People switching to LLMs, which slurp up all of our work and regurgitate
  it, without consent or compensation."
- **Our assessment**: This content is already fully extracted in this
  corpus's dedicated note, `blog-simonwillison-josh-comeau-course-sales-ai.md`
  (Claims 1, 2, 5), including the important qualification (that note's Claim
  6) that Comeau's own follow-up narrows the "⅓" figure to a comparison
  against the course's own Early Access launch specifically, and that the
  course remains profitable even at that reduced volume — a qualification
  this Fowler fragment (like Willison's original re-quote) omits. This
  fragment's distinct value is Fowler's independent curatorial amplification
  of the same story to the Thoughtworks/retreat audience, one week+ after
  Willison's original post, indicating the story is circulating as a
  cross-community signal beyond Willison's readership. No new figures or
  claims beyond what the dedicated note already documents; see
  Cross-References.

### Claim 16: John Gruber criticizes Anthropic's Electron-based Claude desktop app for Mac, and Fowler uses this to raise a broader question about whether the "least-common-denominator" cross-platform UI era is ending now that coding agents can build platform-specific interfaces efficiently
- **Evidence**: Fowler's summary and partial quote of Gruber's critique,
  followed by Fowler's own extrapolation.
- **Confidence**: anecdotal (Gruber's opinion piece plus Fowler's own
  speculative extrapolation; no data on actual cross-platform-vs-native
  development cost/time comparisons is given)
- **Quote**: "John Gruber is annoyed that Claude's desktop app for MacOS in
  uses Electron. \"Electron guarantees that an app feels just as wrong on
  all platforms.\" He has some tasty invective for the folks at Anthropic
  with ties to the Electron platform." ... "The deeper question here is
  whether there should be a future for cross-platform front-ends in the
  world of agentic programming. There's lots of evidence that coding agents
  do a great job of building the same thing in multiple languages and
  platform ecosystems. That should mean that the days of least-denominator
  cross-platform UIs are numbered - and that number is small."
- **Our assessment**: The specific, checkable factual claim here is narrow
  (Claude's Mac desktop app uses Electron, per Gruber's critique) — the
  larger claim (agentic coding tools make maintaining N platform-native
  codebases as cheap as maintaining one cross-platform codebase, therefore
  cross-platform frameworks will decline) is Fowler's own speculative
  extrapolation from Gruber's specific complaint, not itself evidenced with
  data, case studies, or a named team that has actually replaced a
  cross-platform app with agent-maintained platform-native equivalents. This
  is worth flagging in the guide as a plausible but untested hypothesis
  about how agentic coding could reshape platform/framework strategy, not
  as a demonstrated outcome.

### Claim 17: Dan Davies distinguishes "contributory expertise" (held by those actively advancing a field) from "interactional expertise" (held by those who have absorbed a field through extensive engagement with contributory experts without doing the primary work themselves), and questions whether machines trained on a much larger corpus than any human could read can develop genuine contributory expertise or only a machine-scale version of interactional expertise
- **Evidence**: Fowler's summary and quote of Dan Davies's argument, plus
  Fowler's own first-person application of the distinction to himself,
  including a quote from Brian Foote describing this self-aware position as
  being "an intellectual jackal with good taste in carrion"
- **Confidence**: anecdotal (a conceptual distinction proposed by a named
  author, explicitly flagged by Davies himself as hard to draw empirically;
  Fowler's self-application is a personal reflection, not a general finding)
- **Quote**: "Dan Davies tries to draw a distinction between interactional
  and contributory expertise. Contributory expertise is that held by people
  who are doing the work to advance a field of study, interaction expertise
  is held by folks that spend time talking to contributory experts, building
  up a decent store of knowledge themselves, but not steeped in the
  day-to-day of the work." ... "the question that I think is quite important
  is whether there is a similar kind of distinction between the kind of
  expertise that it's possible for a machine to get by industralised
  consumption and interaction with a much larger corpus of literature than
  any human being could inhale, and genuine contributory expertise that
  could apply to entirely new situations outside that literature."
- **Quote** (Fowler's self-application, citing Brian Foote): "my skill is
  only that of someone who is good at selecting and explaining the ideas of
  others. (As Brian Foote put it more memorably: \"an intellectual jackal
  with good taste in carrion\".) But there's skill in being a good jackal too
  - and we don't really know yet where the real boundaries of the LLMs will
  lie."
- **Our assessment**: This is a genuinely novel conceptual contribution for
  this corpus's discussion of what remains distinctively human as AI
  capability grows: rather than framing the open question as "can machines
  match human output quality," Davies frames it as "can machines acquire
  contributory expertise (the ability to advance a field into genuinely new
  situations) versus only interactional expertise (fluent synthesis of
  existing work)" — and the question is stated as genuinely open, not
  answered, by both Davies and Fowler. Fowler's willingness to place his own
  professional value (as a synthesizer/explainer, not an originator of new
  ideas — "my career is devoid of any original ideas") on the interactional
  side of that line, while noting it as still valuable ("there's skill in
  being a good jackal too"), is a notable admission from one of this
  corpus's most-cited authorities and a useful frame for any guide
  discussion of which human skills remain differentiated from AI capability.

## Concrete Artifacts

### Harness engineering session tidbits (paraphrased, unattributed to individuals, from Fowler's own summary)

```
Source: Martin Fowler, "Fragments: July 13" (fragments/2026-07-13.html)

GUIDE SIDE (context management):
- Larger context windows do not guarantee correct model focus; models
  attend to only part of the context
- One attendee limits their agents.md file to under 200 lines

SENSOR SIDE (computational sensors):
- Shift to languages with greater control (e.g. Rust rather than Python)
- "Leveling up" validation via property-based testing and formal-methods
  techniques
- One participant: "not smart enough to write specifications in a formal
  specification language, but smart enough to read it and check it makes
  sense for their domain"

CLOSING FRAME (Fowler's own):
- Harnesses currently reduce token usage and enable weaker/local models to
  be useful; speculation about whether this remains true as models improve
  is explicitly declined as unproductive
```

### Self-hosted models session (paraphrased, unattributed to individuals, from Fowler's own summary)

```
Source: Martin Fowler, "Fragments: July 13" (fragments/2026-07-13.html)

DRIVERS NAMED:
- Rising token costs
- Model sovereignty (following government access-restriction events)
- Information security (data that can't leave the org)
- Training dynamics ("if someone else hosts the model then their model
  learns rather than your model")
- Several participants' companies had already self-hosted for "up to a
  couple of years" before the current cost-driven interest spike

RISKS / OPEN QUESTIONS NAMED:
- Possible repeat of the private-cloud overspending pattern
- Hinges on whether hosting a model is simpler than hosting a cloud
- GPU-operations talent scarcity flagged as the likely hard part
- Capital costs (GPUs) + ongoing costs (electricity) + datacenter physical
  design all affect optimal usage
- Named opportunity: professional services firms helping companies manage
  inference datacenter operations

COST-CONTROL IDEAS NAMED:
- Teaching engineers/users to pick less-powerful models for a given job
- A broker model deciding which model is the best choice per job
- Greater fine-tuning adoption: domain-tuned models hypothesized to need
  less reasoning and consume fewer tokens for in-domain tasks
```

### Kief Morris's unifying synthesis (verbatim, from the page)

```
Source: Martin Fowler quoting/paraphrasing Kief Morris, "Fragments: July 13"
        (fragments/2026-07-13.html)

"Nearly every one of them was a different facet of the same argument. How
much do we let an agent decide, and how do we stay confident in what it
does?"

"He looks at code review, questions whether it matters, but sees that the
rigor that many associate with code review shifts to other forms. He
describes the disagreements about how much we should trust an agent to
identify and fix production incidents. He sees that the contrast between
how much leeway teams give to agents depends on the context they are
operating"

"Underneath all of these sessions, the operations debate, the wide-remit
team, the dark-factory spectrum, the argument about who's allowed to steer
the model, people were making the same handful of choices over and over
about a single thing: the unit of work they were prepared to hand to an
agent. How big it is. How much of the job it covers. What you do to get it
ready to hand over. How you check what comes back. What you put around the
agent to keep it inside the lines."
```

### Sam Ruby's "Bring Me a Rock" session (verbatim, from the page)

```
Source: Sam Ruby (quoted by Martin Fowler), "Fragments: July 13"
        (fragments/2026-07-13.html)

"The room pulled it somewhere narrower than I'd framed, and the narrower
place was the more interesting one: not how to explore by elimination but
who should even be allowed to. Product managers, increasingly people
managers, are reaching for these models directly, and seasoned engineers get
measurably better results from them than untrained people do — so the worry
followed. If expertise is what separates a good outcome from slop, should
non-engineers be steering the model at all?

It's a fair question, and I think it's the wrong one, because it mistakes
the act. When a manager reaches for an LLM instead of routing the work to
the team that reports to them, they didn't pick up a tool — they made a
hire. And you don't ask permission to manage your own team; a manager who
decides a piece of work is better given to a new participant than to the
existing one is doing the most ordinary thing a manager does. Framed that
way, the permission question dissolves into an older, better-understood one
— the one Drucker named in 1959: when the worker knows more about the
specifics than the manager does, you manage by objective, not by method. The
non-engineer steering an agent is exactly that manager, out-known by the
thing they're directing, and the slop the room feared is the old danger of
managing by method when you should be managing by objective. The question
isn't may they hire? It's do they know how to manage by objective? — which
you can teach, hire for, and hold people to without anyone first becoming an
engineer."
```

## Cross-References

### Cross-reference verification notes
Before writing citations below, `blog-fowler-fragments-2026-07-06.md`,
`blog-fowler-fragments-2026-06-16.md`, `blog-fowler-boeckeler-local-models-viability.md`,
`blog-thoughtworks-lovin-gall-local-inference-boundary.md`,
`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`,
`blog-thoughtworks-gall-supervisory-engineering.md`,
`blog-thoughtworks-kamelman-token-crisis.md`, and
`blog-simonwillison-josh-comeau-course-sales-ai.md` were re-read directly
(MINER.md §4b) and claim numbers below were confirmed against those notes'
numbered `### Claim N:` headings in document order.

- **Corroborates**:
  - `blog-fowler-fragments-2026-06-16.md` Claims 1-3 (Chelsea Troy's four
    conversation registers, including "Brainstorming: Generate options, I'll
    evaluate them separately"): this fragment's Claim 10 (Sam Ruby's
    "bring me a rock" iterative-rejection-as-brainstorming argument) is a
    second, independently-argued case for the same underlying practice — an
    LLM's speed and patience make an iterative, elimination-based
    interaction style legitimate — approached from a management-dysfunction
    angle rather than a context-hygiene angle.
  - `blog-fowler-boeckeler-local-models-viability.md` Claim 4 (Qwen3.6 35B
    MoE gave the best balance of parameters, RAM, speed, and quality of any
    model Böckeler tested, becoming her go-to local model): this fragment's
    Claim 13 supplies a second, independent named practitioner (Sebastian
    Raschka) reaching the identical specific-model conclusion via a
    separate evaluation, raising this corpus's Qwen 3.6-as-local-sweet-spot
    finding from single-practitioner anecdotal to independently-corroborated
    anecdotal.
  - `blog-thoughtworks-lovin-gall-local-inference-boundary.md` Claim 5
    (on-device inference trades $0 marginal token cost for hard physical
    constraints developers must design around): this fragment's Claim 6
    (self-hosting's hidden cost is GPU-operations talent scarcity and
    datacenter design, not just capital/electricity) makes the analogous
    "not actually free" argument at enterprise-datacenter scale rather than
    consumer-on-device scale — the two sources converge on the same theme
    (local/self-hosted inference has real, non-obvious operating costs)
    from opposite ends of the deployment-scale spectrum.
  - `blog-thoughtworks-gall-supervisory-engineering.md` Claim 2 ("the human
    engineer evaluates whether the agent actually solved the right problem"
    rather than writing the code) and Claim 7 (the "directing/evaluating/
    correcting" pillars): this fragment's Claim 9 (Kief Morris's unifying
    "how much do we let an agent decide" question) and Claim 11 (Ruby's
    manage-by-objective reframing) both operate at the same conceptual
    layer — defining what a human retains responsibility for as delegation
    increases — but this fragment's framing is broader (applies across code
    review, incident response, and team structure, not just the coding
    "middle loop") and adds the specific unit-of-work decomposition (size,
    scope, handoff prep, check mechanism, guardrails) that the supervisory-
    engineering note does not name explicitly.
  - `blog-simonwillison-josh-comeau-course-sales-ai.md` Claims 1, 2, 5 (⅓
    sales figure, AI "double whammy" attribution, peer creators' 50%+
    revenue decline): this fragment's Claim 15 is Fowler's independent
    curatorial amplification of the same story, adding no new figures but
    corroborating that the story is circulating beyond Willison's original
    readership into the Thoughtworks/retreat community roughly six weeks
    after the underlying Bluesky thread (2026-05-03) and Willison's re-quote
    (2026-07-03).

- **Contradicts**: None identified as a MINER.md §4a contradiction. No claim
  in this fragment materially opposes an existing corpus note's claim in a
  way that would change guide advice.

- **Extends**:
  - `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md` Claim 4
    (an agent's public-facing title/styling is a legal design decision
    carrying different apparent authority — "Junior Clerk" vs. "VP of
    Procurement" — requiring infrastructure-layer enforcement): this
    fragment's Claim 11 (Ruby's management-by-objective reframing of who may
    direct an agent) addresses a related but distinct question — not what
    apparent authority an agent's presentation carries to third parties, but
    what qualifies a *human* to direct an agent's work in the first place.
    Read together, the two sources cover both sides of "who gets to act
    through an agent, and under what authority": Gordon/Kamelman on the
    agent's presented authority to external parties, Ruby on the internal
    manager's qualification to direct the agent at all. Chapter 05
    governance material should cite both.
  - `blog-fowler-fragments-2026-07-06.md` (the prior week's fragment from
    the same retreat): that note documents session-level architecture/design
    tidbits and the "harness engineering wasn't a term at the Feb 2026 Utah
    retreat, ubiquitous by July 2026 Europe retreat" terminology-adoption
    timeline (Claim 3). This fragment is Fowler's continuation of coverage
    of the same retreat one week later, adding the harness-engineering
    session's *content* (this note's Claims 1-3) where the prior fragment
    only established that the session *existed* and that the term had
    recently entered wide use.
  - `blog-thoughtworks-kamelman-token-crisis.md` (Claims 1, 9 — token spend
    as a cross-functional governance problem with no clear owner; waste
    traceable to unrevisited prototyping-phase defaults): this fragment's
    self-hosted-models session (Claims 4-8) proposes self-hosting,
    model-brokering, and fine-tuning as three concrete upstream responses to
    the same cost pressure that note diagnoses, without directly citing that
    note's crisis framing — the two sources should be read together as
    diagnosis (Kamelman) and candidate remedies (this fragment).

- **Novel**:
  - **Sub-200-line `agents.md` as a specific context-management target**
    (Claim 1): no existing corpus note states a specific line-count target
    for a persistent guide file.
  - **Rust-over-Python and property-based/formal-methods validation as named
    "sensor-side" harness-engineering trends** (Claim 2): new to this
    corpus's harness-engineering material, including the specific
    human-reads-but-doesn't-author-formal-specs division of labor.
  - **"If someone else hosts the model then their model learns rather than
    your model" as a training-dynamics rationale for self-hosting**
    (Claim 4): a distinct rationale from cost, sovereignty, or information
    security, not previously documented in this corpus's self-hosting
    coverage.
  - **GPU-operations talent scarcity, not hardware cost or model quality, as
    the likely hard part of self-hosting at scale** (Claim 6): a specific,
    named bottleneck new to this corpus.
  - **Kief Morris's "how much do we let an agent decide, and how do we stay
    confident in what it does" unifying frame, with its five-part unit-of-
    work decomposition** (Claim 9): the most significant new organizing
    concept in this fragment — no existing corpus note names this as a
    cross-cutting question spanning code review, incident response, and team
    structure simultaneously.
  - **Sam Ruby's Drucker-1959 "manage by objective" reframing of non-
    engineers directing LLM agents as a hiring decision** (Claim 11): new
    management-theory vocabulary applied to agent-governance access
    questions, not present elsewhere in this corpus.
  - **Dan Davies's contributory-vs-interactional-expertise distinction,
    applied to whether machines can acquire genuine contributory expertise
    from a larger-than-human corpus** (Claim 17): a novel framing for
    discussing what remains distinctively human under AI capability growth,
    including Fowler's own notable self-placement on the interactional side
    of that line.

## Guide Impact

- **Chapter 02/03 (Harness Engineering)**: Add the sub-200-line `agents.md`
  data point (Claim 1) and the "models only attend to part of the context"
  rationale as a concrete illustration for why persistent guide files should
  be kept terse, alongside existing corpus context-management material
  (Chelsea Troy's registers, `blog-fowler-fragments-2026-06-16.md`). Add the
  Rust-over-Python and property-based/formal-methods sensor-side trend
  (Claim 2) as a named validation-strategy option, including the
  read-not-author division of labor for formal specifications. Add Fowler's
  "harnesses currently reduce token usage and enable weaker models" framing
  (Claim 3) as the grounded, non-speculative justification for harness
  investment, explicitly declining to take a position on long-term
  necessity.

- **Chapter 05/06 (Self-Hosted Models / Cost Governance)**: Add the four
  named self-hosting drivers (Claim 4: sovereignty, information security,
  training dynamics, cost) and the private-cloud-overspend risk analogy with
  its named bottleneck — GPU-operations talent scarcity (Claim 6) — as a
  candidate section on self-hosted model economics, cross-referenced with
  `blog-thoughtworks-lovin-gall-local-inference-boundary.md`'s consumer-scale
  "not actually free" finding. Add the model-broker cost-control idea
  (Claim 7) paired with Simon Willison's concrete Fable delegation tip
  (Claim 14) as a two-source (speculative + practitioner-demonstrated) case
  for model-routing-by-the-model-itself as a cost lever, alongside
  fine-tuning (Claim 8) as a distinct token-reduction mechanism.

- **Chapter 05 (Team Adoption / Governance)**: Add Kief Morris's unifying
  frame (Claim 9) as a candidate organizing principle for a chapter section
  spanning code review posture, incident-response delegation, and team
  structure — explicitly naming the five decision variables (unit size, job
  coverage, handoff preparation, output checking, guardrails) as a checklist.
  Add Sam Ruby's management-by-objective reframing (Claim 11) as a specific,
  citable answer to "should non-engineers direct agents directly," to be
  presented alongside (not in place of) the legal/apparent-authority framing
  already sourced from `blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`.
  Add the conformance-tests-over-specifications preference with its explicit
  caveat (Claim 12: sensors can't enumerate everything that shouldn't
  happen, and agent-built models must still be taught back to humans) as a
  balancing point against any guide section that over-indexes on sensors as
  a complete substitute for human-authored guides/specs.

- **Chapter 01 (Landscape / Market Context)**: Add Claim 15 (Josh Comeau
  developer-education decline) as a secondary citation alongside the fuller
  existing note, noting only that the story is now corroborated as
  circulating in a second practitioner community (Thoughtworks retreat, via
  Fowler) six-plus weeks after the original report — do not treat this as
  new quantitative evidence. Add Claim 16 (Gruber's Electron critique /
  Fowler's cross-platform-UI-decline speculation) as an open, untested
  hypothesis about agentic coding's effect on platform/framework strategy,
  flagged explicitly as speculation rather than a documented outcome. Add
  Claim 17 (Davies's contributory-vs-interactional-expertise distinction,
  with Fowler's self-application) as a citable framing for any guide
  discussion of which human skills remain differentiated from AI capability
  as models improve.

## Extraction Notes

- **WebFetch returned a condensed, non-verbatim summary on the first pass**
  (the same pattern documented in `blog-fowler-fragments-2026-07-06.md` and
  other Thoughtworks/Fowler-sourced notes in this corpus), and a second,
  more targeted WebFetch pass returned a paraphrased markdown conversion
  rather than character-for-character source text. Per MINER.md §2a, no
  quote in this note was taken from either WebFetch pass. Instead, the live
  page was fetched directly via `curl` (HTTP 200) and the article body was
  extracted by stripping HTML tags and decoding entities from the raw
  response. All quotes in this note are taken from that locally-parsed
  verbatim text, cross-checked by re-reading the parsed output alongside the
  section structure.
- **Two linked sub-sources were not independently fetched**: Sebastian
  Raschka's local-model-environment post (Claim 13) and the specific Simon
  Willison post containing the Fable delegation tip (Claim 14). Both are
  flagged as follow-up mining candidates — a dedicated Raschka source note
  would raise Claim 13 from a Fowler-mediated pointer to a directly-quoted
  claim, and a dedicated Willison source note on the Fable tip would supply
  the missing implementation detail (exact instruction phrasing, measured
  savings) for Claim 14. Neither link URL was resolved to a fetchable
  address in the parsed HTML output, consistent with this corpus's prior
  observation (`blog-thoughtworks-gordon-kamelman-agentic-scope-authority.md`
  Extraction Notes) that outbound links are sometimes stripped by
  tag-stripping HTML-to-text extraction.
- **No contradiction issues filed.** Cross-referenced against this corpus's
  self-hosted-models cluster, token-cost-crisis cluster, governance cluster,
  and the two prior Fowler fragments notes; no claim here materially opposes
  an existing corpus claim in a way that would change guide advice.
- **Confidence rated "emerging" overall.** This fragment combines Fowler's
  own first-hand session paraphrase (Claims 1-8, unattributed to named
  individuals, hence individually rated anecdotal) with named, directly-
  quoted, higher-confidence practitioner arguments (Claims 9-11, Kief Morris
  and Sam Ruby, both attending and speaking in their own words) and several
  further named-contributor pointers of varying depth (Claims 13-17). No
  claim rises to independently-measured/settled status on its own; several
  are corroborated by existing corpus notes (see Cross-References), which is
  the basis for the overall "emerging" rather than "anecdotal" rating,
  consistent with how the two prior Fowler fragments notes in this corpus
  were rated.
