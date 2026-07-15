---
source_url: https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/
source_type: blog-post
title: "The Tower Keeps Rising"
author: Armin Ronacher
date_published: 2026-07-13
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: anecdotal
issue: "#1877"
---

# The Tower Keeps Rising

> Armin Ronacher reframes the Tower of Babel as a story about coordination
> (shared language enabling collective power, not hubris being punished), then
> argues that coding agents remove the interpersonal friction — code review,
> conversation, having to explain a change — that used to force a team's
> understanding of a system to stay synchronized, so "vibecoded" scaled-up
> codebases drift toward Babel-like incoherence without construction ever
> visibly stopping.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; short essay, ~1,200
  words; three unnamed movements: the Bruegel/Babel framing, the diagnosis of
  software coordination via "shared language," and the AI-agent application;
  published 2026-07-13)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2,
  Click, and Sentry, and the author of the Pi coding agent. His blog is a
  designated `trusted-feed` source in this repo (seven prior source notes
  extracted: blog-ronacher-pi-oss.md, blog-ronacher-the-coming-loop.md,
  blog-ronacher-clanker-terminology.md, blog-ronacher-content-for-contents-
  sake.md, blog-ronacher-ai-nationalism-americans-only.md, blog-ronacher-
  communities-of-not.md, blog-ronacher-gaslighting-openness.md,
  blog-ronacher-local-models-focus-polish.md). This post is a short
  conceptual/metaphorical essay, not a data-backed analysis — it contains no
  metrics, named tools, or specific case studies. It is first-person
  reflection from a practitioner who runs large agent-assisted codebases
  (Pi) and has written extensively elsewhere (blog-ronacher-the-coming-loop.md)
  about the operational consequences of agentic and harness-loop development.
- **Scope**: Covers a single conceptual argument — that a software project's
  "shared language" (the team's common understanding of concepts, boundaries,
  invariants, and ownership) has historically been synchronized through
  interpersonal friction, and that AI agents remove that friction, allowing
  people to act independently in parts of a system without the coordination
  that previously forced shared understanding. Does NOT cover: specific
  remedies or mechanisms to restore coordination (the piece explicitly
  diagnoses without prescribing), named tools or companies, quantitative
  data, or a description of what a newcomer experiences entering such a
  codebase. The post ends on the diagnosis, not a solution.

## Extracted Claims

### Claim 1: The Tower of Babel story is fundamentally about coordination — shared language is the source of the builders' power, and losing it (not the tower's height) is what ends the project
- **Evidence**: Ronacher's reading of Genesis 11 and Bruegel's painting "The
  Tower of Babel," reframing the conventional "hubris punished" moral as
  instead a story about what shared language makes possible collectively.
- **Confidence**: anecdotal (a single author's literary/conceptual reframing,
  not a claim requiring empirical evidence)
- **Quote**: "The source of their power is coordination. They share a
  language and with that shared language they can combine their work into
  something no one of them could build alone."
- **Our assessment**: This reframing is the conceptual hinge the rest of the
  post depends on. By recasting Babel as a coordination story rather than a
  hubris story, Ronacher sets up the analogy to software teams: the builders'
  power came from shared language, not skill or ambition, and its loss (not
  a technical failure) is what halted construction in the biblical account.

### Claim 2: A software project's "shared language" is the team's common understanding of concepts, boundaries, invariants, and ownership — not the programming language or spoken language used
- **Evidence**: Ronacher's direct definitional claim, offered as the
  translation of the Babel metaphor into software terms.
- **Confidence**: anecdotal
- **Quote**: "The shared language of a software project is not English or
  Python but it is the common understanding of what its concepts mean, where
  the boundaries are, which invariants matter, who owns what, and why the
  system has the shape it does."
- **Our assessment**: This is a precise and citable definition — it names
  five specific components of shared understanding (concept meaning,
  boundaries, invariants, ownership, rationale for shape) rather than gesturing
  vaguely at "team alignment." It gives the guide a concrete checklist for what
  "shared understanding" actually consists of, useful for anyone trying to
  operationalize the idea rather than just naming it.

### Claim 3: This shared language is not written down in any one place — it lives partly in documentation and code, but mostly in the social process of code review, conversation, argument, and having to explain a change to someone else
- **Evidence**: Ronacher's direct claim about where team knowledge actually
  resides, contrasted with where people assume it resides (docs, code).
- **Confidence**: anecdotal
- **Quote**: "This language is rarely written down in one place. It lives
  partly in documentation and code, but also in code review, conversations,
  arguments, and the experience of having to explain a change to somebody
  else."
- **Our assessment**: This is the load-bearing claim for the guide's
  documentation-vs-process distinction: if shared understanding lives
  primarily in social process rather than artifacts, then removing the social
  process (as agents do — Claim 4) removes the synchronization mechanism even
  if documentation and code remain fully intact. This directly complicates
  any guide advice that treats CLAUDE.md/AGENTS.md files as a full substitute
  for the human coordination they were meant to reduce, not eliminate.

### Claim 4: The friction of needing to read someone else's code, ask questions, and coordinate before changing a shared system was not just overhead — it was the mechanism that synchronized two people's understanding and surfaced disagreement
- **Evidence**: Ronacher's first-person account of what cross-boundary changes
  required before agents, framed as a specific, concrete example rather than
  an abstraction.
- **Confidence**: anecdotal
- **Quote**: "If I wanted to change your storage layer, I usually had to read
  your code, ask you questions, and perhaps coordinate with another team."
- **Additional quote**: "Some of it was the process by which your
  understanding became mine, and by which both of us discovered whether we
  still agreed about how the system worked."
- **Our assessment**: The second quote is the key mechanism claim: friction
  wasn't merely a cost of doing cross-boundary work, it was a *discovery*
  process — the act of explaining forced both parties to find out if their
  mental models still matched. This reframes "friction" from pure overhead
  (which most engineering-productivity framing treats it as) to a load-bearing
  quality-control step, which is the crux of why removing it (Claim 5) is
  risky rather than purely beneficial.

### Claim 5: Coding agents remove most of that coordination friction, letting one person independently make changes — via an agent — in parts of a system where they previously needed another person's involvement
- **Evidence**: Ronacher's direct claim, illustrated with a concrete
  three-person example of parallel independent agent-driven changes to the
  same system.
- **Confidence**: anecdotal
- **Quote**: "Agents remove much of that friction. I can ask an agent to add
  OAuth, you can ask one to add caching, and somebody else can ask one to
  rebuild the database from first principles and make the UI pink."
- **Additional quote**: "Agents now let us act in parts of the system where we
  would previously have needed other people and in code bases where the
  people would have revolved."
- **Our assessment**: This is the mechanism claim of the post: it names
  exactly what agents remove (the *need* to involve another person) rather
  than making the vaguer claim that "agents make people communicate less."
  The OAuth/caching/database-rebuild example is deliberately chosen to show
  three simultaneous, locally-reasonable, unsupervised changes to
  overlapping system concerns — each individually defensible, none
  coordinated with the others.

### Claim 6: "Vibecoded" scaled-up projects drift toward Babel-like incoherence not because people are unable to communicate, but because the system no longer forces them to
- **Evidence**: Ronacher's synthesis claim connecting the friction-removal
  mechanism (Claim 5) to the outcome he has personally observed in scaled
  agent-assisted projects.
- **Confidence**: anecdotal (a single practitioner's observation of "some"
  vibecoded projects; no named examples or codebases are given)
- **Quote**: "When I look at some vibecoded scaled-up projects the codebases
  become Babel not because nobody can communicate, but because nobody needs
  to."
- **Our assessment**: This is the post's central, most citable one-sentence
  claim. It draws a sharp distinction that matters for diagnosis: a team
  experiencing this failure mode will not show the obvious symptoms of a
  communication breakdown (people arguing, missed handoffs) — communication
  channels remain open and functional, they are simply no longer invoked,
  because agents make independent local action possible. This makes the
  failure mode harder to detect via typical team-health signals.

### Claim 7: Unlike the biblical Babel, where losing shared language halted construction immediately and visibly, AI-assisted development lets construction continue after architectural coherence has already been lost — masking the loss
- **Evidence**: Ronacher's closing argument, contrasting the biblical outcome
  (tower literally stops rising) with what he claims happens in agent-
  assisted codebases (the tower keeps rising).
- **Confidence**: anecdotal
- **Quote**: "The tower does not fall, and so we do not notice what was
  lost. It just keeps rising."
- **Our assessment**: This is the post's thesis-closing claim and its most
  original contribution: the danger isn't that coordination collapse stops
  progress (which would be self-correcting, since a stalled project forces
  attention), but that progress continues *unimpeded* after the collapse,
  removing the natural feedback signal that would otherwise prompt
  intervention. For the guide, this reframes "architectural drift" from a
  problem that eventually becomes visible through slowing velocity to one
  that can remain invisible indefinitely because velocity (or apparent
  velocity) is exactly what continues.

### Claim 8: Some "vibecoded" software already exhibits randomly or unexpectedly changing behavior, which prompted this line of thinking
- **Evidence**: Ronacher's opening personal observation, offered as the
  anecdotal trigger for the essay rather than a substantiated measurement.
- **Confidence**: anecdotal (a personal impression — "I feel" — with no named
  examples, codebases, or supporting data)
- **Quote**: "I feel that some vibecoded software changes somewhat randomly
  and unexpectedly."
- **Our assessment**: This is explicitly hedged ("I feel") and unsupported by
  any specific example in the post — it is the weakest-evidenced claim in the
  piece and functions as a motivating anecdote rather than a load-bearing
  argument. It should be read as context for why Ronacher started thinking
  about coordination loss, not as independent evidence of the phenomenon.

## Concrete Artifacts

### The Babel reframing (Genesis 11 + Bruegel)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/

Opening trigger: "I feel that some vibecoded software changes somewhat
randomly and unexpectedly."

Visual reference: "That made me think about Bruegel's 'The Tower of Babel'
which shows an already quite chaotic depiction of the Tower of Babel."

Biblical framing (Genesis 11, KJV, quoted in the post):
"the people is one, and they have all one language, [...] and now nothing
will be restrained from them."

Reframed moral: coordination (shared language) is the source of the
builders' power, not hubris — and its loss, not the tower's height, is
what the biblical account treats as consequential.
```

### The friction-removal mechanism, stated as a worked example

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/

Pre-agent state (friction as synchronization):
  "If I wanted to change your storage layer, I usually had to read your
  code, ask you questions, and perhaps coordinate with another team."
  "This friction synchronizes people."

Post-agent state (friction removed, three parallel unsupervised changes):
  "I can ask an agent to add OAuth, you can ask one to add caching, and
  somebody else can ask one to rebuild the database from first principles
  and make the UI pink."

Result named by the author:
  "When I look at some vibecoded scaled-up projects the codebases become
  Babel not because nobody can communicate, but because nobody needs to."

Closing thesis:
  "The tower does not fall, and so we do not notice what was lost.
  It just keeps rising."
```

## Cross-References

- **Extends**: `blog-ronacher-the-coming-loop.md` Claim 5 — that note's
  quote: "When you take that behavior and you put it behind loops, you tend
  to amplify it. If each iteration adds another small defense, the system
  slowly becomes less understandable while appearing more robust." That
  claim describes comprehensibility loss *within* a single agent/loop's
  accumulating local defenses. This post's Claims 4-6 add the *team-level*
  mechanism operating in parallel: comprehensibility loss isn't only an
  artifact of one loop's defensive-code accumulation, it's also a product of
  multiple people no longer needing to synchronize their mental models with
  each other at all, because each can act unilaterally through an agent. The
  two posts describe two independent, compounding causes of the same
  end state (a system nobody fully understands): per-loop defensive
  accumulation (the-coming-loop) and cross-person coordination loss (this
  post).

- **Extends**: `blog-ronacher-the-coming-loop.md` Claim 8 — that note's
  quote: "The metaphor I like to reach for is one of moving from software as
  a deterministic machine to software as an organism... We treat it, we
  monitor it, we stabilize it, but we do not necessarily comprehend it." The
  organism metaphor names the *end state* of lost comprehension. This post's
  Claim 6 ("nobody needs to communicate") names a specific *mechanism* that
  produces that end state at the team level, complementary to the individual
  defensive-coding mechanism the-coming-loop already documents.

- **Extends**: `blog-ronacher-the-coming-loop.md` Claim 11 — that note's
  quote: "Either we need to find clever ways to jolt the human back into the
  loop and make the changes of the loops legible long term, or we need to
  find better ways to compose these ever more complex systems." That claim
  identifies legibility of agent-generated *changes* as an open problem for
  harness design. This post supplies the underlying reason legibility is
  hard to restore once lost: the interpersonal process that used to build
  legibility (code review, explaining a change, arguing about it) is exactly
  what agents let people skip, so the loss compounds silently rather than
  being caught by a single legibility mechanism.

- **Corroborates**: `failure-decker-4hr-session-loss.md` Lesson 2 — that
  note's quote: "the nuanced understanding of why we'd structured things a
  certain way — gone," and its root-cause analysis that "the 'why' lives in
  the back-and-forth that gets summarized away." That failure report
  documents the same phenomenon this post describes — architectural
  rationale living in dialogue rather than in artifacts — but at the scale
  of a single session lost to compaction, rather than a whole team's shared
  understanding lost to removed coordination. Both sources independently
  locate the "why" of a system in conversation/process rather than in
  code or docs, and both identify that losing the conversational layer
  loses the rationale even when the artifacts (code, session logs) survive.

- **Contradicts**: No specific existing source note makes a claim that
  directly opposes this post's core argument (that agent-enabled
  friction removal degrades cross-team shared understanding). This post's
  framing is in tension with any guide section that treats reduced
  cross-team back-and-forth purely as a productivity win — but no source
  note currently makes that unqualified claim, so no contradiction issue is
  filed. The Assayer should flag if a source note advocating unqualified
  reduction of code-review/coordination overhead as a pure efficiency gain
  is identified.

- **Novel**:
  - **The Babel-as-coordination (not hubris) reframing applied to software
    teams**: No existing corpus source uses this framing. It gives the guide
    a citable, memorable analogy for architectural coherence loss distinct
    from the organism metaphor already documented in blog-ronacher-the-
    coming-loop.md.
  - **A five-part definition of a software project's "shared language"**
    (concept meaning, boundaries, invariants, ownership, system shape): no
    prior corpus source breaks "shared understanding" into named components
    this specifically.
  - **Friction as a synchronization mechanism, not just overhead**: prior
    corpus sources (e.g. blog-ronacher-content-for-contents-sake.md, which
    argues for adding friction/backpressure against content flooding) treat
    friction as a deliberate countermeasure to add. This post is the first
    to argue that *pre-existing, already-present* interpersonal friction in
    software development was quietly performing team-synchronization work
    all along, before anyone deliberately added it as a policy.
  - **"Construction continues after coordination collapses" as a named
    failure mode**: this is the sharpest and most novel claim in the post
    (Claim 7) — the risk isn't that AI-driven development stalls when
    understanding is lost, but that it doesn't, removing the natural signal
    that would otherwise prompt human intervention. No existing corpus
    source names this specific asymmetry between visible failure and silent
    continuation.

## Guide Impact

- **Chapter 05 (Team Adoption)**: The existing "Multi-Repo Coordination
  Topologies" section and the parallel-adoption discussion of complexity
  drift (citing paper-miller-speed-cost-quality.md) currently frame
  coordination as a structural/tooling problem (which repo owns what, how
  metrics drift). This source adds a distinct, complementary claim: even
  within a single well-structured repo, coordination can silently fail
  because agents remove the *social* requirement to involve another person
  before touching shared system boundaries (storage layers, shared
  invariants). Recommend adding a specific callout, citing Claim 4-6, that
  teams adopting agent-driven parallel workstreams should deliberately
  preserve a cross-boundary review requirement (not just a code-review gate,
  but a "does this change any invariant another team relies on" check) —
  precisely because agents make it possible to skip that step without any
  visible failure signal.

- **Chapter 04 (Context Engineering)**: The existing content on architectural
  rationale loss during compaction (citing failure-decker-4hr-session-loss.md
  Lesson 2, at the "The architectural rationale is the first thing
  compaction destroys" passage) documents rationale loss *within* a single
  session. This source (Claim 3) generalizes the same insight to the
  *team* level: a project's shared language "lives...in code review,
  conversations, arguments" as much as in documentation. Recommend the
  chapter note that AGENTS.md/CLAUDE.md files and ADRs, while necessary, are
  not sufficient replacements for the interpersonal process that used to
  build shared understanding — they capture facts, not the negotiated
  agreement-checking that conversation provided.

- **Chapter 00 (Principles)**: Consider citing Claim 6-7 as a concrete
  articulation of why "verification over generation" (or an equivalent
  principle) needs a team-level counterpart, not just a per-change one: a
  system where every individual agent-assisted change is locally verified
  can still accumulate global incoherence if no mechanism forces
  cross-person review of shared invariants. The "tower keeps rising" framing
  is a useful one-line citation for why this failure mode is easy to miss —
  velocity and test-passing continue even as coordination erodes.

## Extraction Notes

- The full article text could not be reproduced verbatim through WebFetch
  (the tool declined full reproduction as a copyright precaution). Instead,
  extraction was done through multiple targeted WebFetch queries requesting
  (a) section structure and paraphrased summaries, (b) short, exact,
  attributed quotes under ~35 words each for specific claims, and (c)
  verification passes re-confirming exact wording and surrounding context
  for the most load-bearing quotes (the "code review, conversations,
  arguments" sentence and the "Agents now let us act..." sentence were both
  independently re-verified word-for-word in a follow-up query). All quotes
  in this note are the tool's reported verbatim extractions from the source
  page; no quote was reconstructed or paraphrased and presented as a direct
  quote.
- The post is short (~1,200 words) and purely conceptual/metaphorical — it
  contains no named codebases, no metrics, no code samples, and no proposed
  remedies. This was confirmed via a dedicated query: the author diagnoses
  the problem but explicitly does not propose mechanisms to restore shared
  understanding. This should not be read as a gap in extraction; it is a
  genuine limitation of the source, noted in Source Context and reflected in
  the `anecdotal` confidence rating.
- Two external links in the source (Bruegel's painting on Wikipedia, the
  Genesis 11 passage on Bible Gateway/KJV) were not independently fetched;
  they are supporting cultural/textual references rather than empirical
  evidence, and the KJV Genesis quote is public-domain text reproduced
  directly from the post's own citation.
- Cross-references were verified against the actual claim numbering in
  `blog-ronacher-the-coming-loop.md` (Claims 5, 8, 11) and the lesson
  numbering in `failure-decker-4hr-session-loss.md` (Lesson 2) by reading
  each cited note in full before writing the citation. No claim/lesson
  numbers were guessed.
- No contradiction issue filed. This post's argument is in tension with an
  unqualified "less coordination overhead = pure productivity win" framing,
  but no existing source note makes that unqualified claim, so there is no
  concrete contradiction to file per MINER.md §4a's "when NOT to file"
  guidance (the opposing position doesn't currently exist in the corpus).
